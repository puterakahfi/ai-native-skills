#!/usr/bin/env python3
"""Validate the canonical design-review gate registry and migration map."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "skills" / "design-review" / "references" / "gate-registry.yaml"
MIGRATIONS_PATH = ROOT / "skills" / "design-review" / "references" / "gate-migrations.yaml"
REFERENCES_DIR = REGISTRY_PATH.parent

NAMESPACE_RE = re.compile(r"^[A-Z][A-Z0-9]{0,5}$")
CANONICAL_NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
TABLE_GATE_RE = re.compile(
    r"^\|\s*([A-Z][A-Z0-9]{0,5}[1-9][0-9]*)\s+([^|]+?)\s*\|",
    re.MULTILINE,
)


class RegistryError(ValueError):
    """Raised when the gate registry or migrations are invalid."""


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise RegistryError(f"missing required file: {path}")
    with path.open(encoding="utf-8") as handle:
        document = yaml.safe_load(handle)
    if not isinstance(document, dict):
        raise RegistryError(f"{path}: root must be a mapping")
    return document


def require_mapping(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise RegistryError(f"{label} must be a mapping")
    return value


def require_string(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise RegistryError(f"{label} must be a non-empty string")
    return value.strip()


def require_string_list(value: Any, label: str) -> list[str]:
    if not isinstance(value, list) or not value:
        raise RegistryError(f"{label} must be a non-empty list")
    return [require_string(item, f"{label}[{index}]") for index, item in enumerate(value)]


def normalize_title(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip()).casefold()


def resolve_namespace(gate_id: str, namespaces: dict[str, Any]) -> str:
    matches = [
        namespace
        for namespace in namespaces
        if gate_id.startswith(namespace)
        and gate_id[len(namespace) :].isdigit()
        and int(gate_id[len(namespace) :]) > 0
    ]
    if len(matches) != 1:
        raise RegistryError(
            f"gate id '{gate_id}' must resolve to exactly one registered namespace; "
            f"matches={matches}"
        )
    return matches[0]


def resolve_owner_path(owner: str) -> Path:
    """Resolve built-in owner filenames or repo-relative external owner paths."""
    raw = Path(owner)
    if raw.is_absolute():
        raise RegistryError(f"owner path must be repository-relative: {owner}")

    candidate = ROOT / raw if owner.startswith("skills/") else REFERENCES_DIR / raw
    resolved = candidate.resolve()
    root = ROOT.resolve()
    try:
        resolved.relative_to(root)
    except ValueError as error:
        raise RegistryError(f"owner path escapes repository root: {owner}") from error

    if not resolved.is_file():
        raise RegistryError(f"owner reference does not exist: {resolved}")
    return resolved


def validate_hard_gate_policy(value: Any, label: str) -> None:
    if isinstance(value, bool):
        return
    policy = require_mapping(value, label)
    when = require_string_list(policy.get("when"), f"{label}.when")
    if len(set(when)) != len(when):
        raise RegistryError(f"{label}.when contains duplicates")


def flatten_registry(
    document: dict[str, Any],
) -> tuple[dict[str, dict[str, Any]], dict[str, Any]]:
    metadata = require_mapping(document.get("registry"), f"{REGISTRY_PATH}: registry")
    require_string(metadata.get("id"), f"{REGISTRY_PATH}: registry.id")
    registry_version = require_string(
        metadata.get("version"), f"{REGISTRY_PATH}: registry.version"
    )

    allowed_statuses = set(
        require_string_list(
            metadata.get("allowed_statuses"),
            f"{REGISTRY_PATH}: registry.allowed_statuses",
        )
    )
    allowed_domains = set(
        require_string_list(
            metadata.get("allowed_design_domains"),
            f"{REGISTRY_PATH}: registry.allowed_design_domains",
        )
    )

    applicability_groups = require_mapping(
        document.get("applicability_groups"),
        f"{REGISTRY_PATH}: applicability_groups",
    )
    for name, profiles in applicability_groups.items():
        require_string(name, f"{REGISTRY_PATH}: applicability group name")
        require_string_list(profiles, f"{REGISTRY_PATH}: applicability_groups.{name}")

    namespaces = require_mapping(document.get("namespaces"), f"{REGISTRY_PATH}: namespaces")
    for namespace, config in namespaces.items():
        require_string(namespace, f"{REGISTRY_PATH}: namespace")
        if not NAMESPACE_RE.fullmatch(namespace):
            raise RegistryError(f"{REGISTRY_PATH}: invalid namespace '{namespace}'")
        require_string(
            require_mapping(config, f"{REGISTRY_PATH}: namespaces.{namespace}").get(
                "purpose"
            ),
            f"{REGISTRY_PATH}: namespaces.{namespace}.purpose",
        )

    gate_groups = require_mapping(document.get("gate_groups"), f"{REGISTRY_PATH}: gate_groups")
    normalized: dict[str, dict[str, Any]] = {}
    names_by_namespace: set[tuple[str, str]] = set()

    for group_name, raw_group in gate_groups.items():
        group = require_mapping(raw_group, f"{REGISTRY_PATH}: gate_groups.{group_name}")
        defaults = require_mapping(
            group.get("defaults"), f"{REGISTRY_PATH}: gate_groups.{group_name}.defaults"
        )
        raw_gates = require_mapping(
            group.get("gates"), f"{REGISTRY_PATH}: gate_groups.{group_name}.gates"
        )
        if not raw_gates:
            raise RegistryError(f"{REGISTRY_PATH}: gate group '{group_name}' has no gates")

        for gate_id, raw_gate in raw_gates.items():
            if gate_id in normalized:
                raise RegistryError(f"{REGISTRY_PATH}: duplicate gate id '{gate_id}'")

            gate = dict(defaults)
            gate.update(require_mapping(raw_gate, f"{REGISTRY_PATH}: gate {gate_id}"))
            namespace = resolve_namespace(gate_id, namespaces)
            gate["id"] = gate_id
            gate["namespace"] = namespace

            canonical_name = require_string(
                gate.get("canonical_name"), f"{REGISTRY_PATH}: {gate_id}.canonical_name"
            )
            if not CANONICAL_NAME_RE.fullmatch(canonical_name):
                raise RegistryError(
                    f"{REGISTRY_PATH}: {gate_id}.canonical_name must be kebab-case"
                )
            name_key = (namespace, canonical_name)
            if name_key in names_by_namespace:
                raise RegistryError(
                    f"{REGISTRY_PATH}: duplicate canonical name '{canonical_name}' "
                    f"in namespace '{namespace}'"
                )
            names_by_namespace.add(name_key)

            require_string(gate.get("title"), f"{REGISTRY_PATH}: {gate_id}.title")
            owner = require_string(gate.get("owner"), f"{REGISTRY_PATH}: {gate_id}.owner")
            resolve_owner_path(owner)

            design_domain = require_string(
                gate.get("design_domain"), f"{REGISTRY_PATH}: {gate_id}.design_domain"
            )
            if design_domain not in allowed_domains:
                raise RegistryError(
                    f"{REGISTRY_PATH}: {gate_id} has unsupported design_domain "
                    f"'{design_domain}'"
                )

            status = require_string(gate.get("status"), f"{REGISTRY_PATH}: {gate_id}.status")
            if status not in allowed_statuses:
                raise RegistryError(
                    f"{REGISTRY_PATH}: {gate_id} has unsupported status '{status}'"
                )

            applicability = require_string(
                gate.get("applicability"),
                f"{REGISTRY_PATH}: {gate_id}.applicability",
            )
            if applicability not in applicability_groups:
                raise RegistryError(
                    f"{REGISTRY_PATH}: {gate_id} references unknown applicability group "
                    f"'{applicability}'"
                )

            weight = gate.get("default_weight")
            if not isinstance(weight, int) or isinstance(weight, bool) or weight <= 0:
                raise RegistryError(
                    f"{REGISTRY_PATH}: {gate_id}.default_weight must be a positive integer"
                )

            validate_hard_gate_policy(
                gate.get("hard_gate_policy"),
                f"{REGISTRY_PATH}: {gate_id}.hard_gate_policy",
            )
            normalized[gate_id] = gate

    if not normalized:
        raise RegistryError(f"{REGISTRY_PATH}: no gates registered")

    return normalized, {
        "registry_version": registry_version,
        "namespaces": namespaces,
        "applicability_groups": applicability_groups,
    }


def validate_owner_definitions(gates: dict[str, dict[str, Any]]) -> None:
    discovered: dict[str, str] = {}
    owner_refs = sorted({gate["owner"] for gate in gates.values()})

    for owner_ref in owner_refs:
        owner_path = resolve_owner_path(owner_ref)
        text = owner_path.read_text(encoding="utf-8")
        for gate_id, title in TABLE_GATE_RE.findall(text):
            if gate_id in discovered:
                raise RegistryError(
                    f"gate '{gate_id}' is defined by multiple owners: "
                    f"{discovered[gate_id]} and {owner_ref}"
                )
            discovered[gate_id] = owner_ref

            if gate_id not in gates:
                raise RegistryError(f"{owner_path}: defines unregistered gate '{gate_id}'")
            registry_gate = gates[gate_id]
            if registry_gate["owner"] != owner_ref:
                raise RegistryError(
                    f"{owner_path}: gate '{gate_id}' owner mismatch; "
                    f"registry says {registry_gate['owner']}"
                )
            if normalize_title(title) != normalize_title(registry_gate["title"]):
                raise RegistryError(
                    f"{owner_path}: gate '{gate_id}' title '{title.strip()}' "
                    f"does not match registry title '{registry_gate['title']}'"
                )

    active_ids = {gate_id for gate_id, gate in gates.items() if gate["status"] == "active"}
    missing_definitions = sorted(active_ids - set(discovered))
    if missing_definitions:
        raise RegistryError(
            f"active gates missing owner-table definitions: {missing_definitions}"
        )

    non_active_definitions = sorted(
        gate_id for gate_id in discovered if gates[gate_id]["status"] != "active"
    )
    if non_active_definitions:
        raise RegistryError(
            f"non-active gates still defined as active owner-table rows: "
            f"{non_active_definitions}"
        )


def canonical_target(value: Any, label: str) -> str:
    if isinstance(value, str):
        return require_string(value, label)
    mapping = require_mapping(value, label)
    return require_string(mapping.get("canonical_id"), f"{label}.canonical_id")


def validate_migrations(
    gates: dict[str, dict[str, Any]],
    registry_version: str,
    namespaces: dict[str, Any],
) -> None:
    document = load_yaml(MIGRATIONS_PATH)
    metadata = require_mapping(
        document.get("migration_map"), f"{MIGRATIONS_PATH}: migration_map"
    )
    migration_registry_version = require_string(
        metadata.get("registry_version"),
        f"{MIGRATIONS_PATH}: migration_map.registry_version",
    )
    if migration_registry_version != registry_version:
        raise RegistryError(
            f"{MIGRATIONS_PATH}: registry version {migration_registry_version} "
            f"does not match {registry_version}"
        )

    aliases = require_mapping(document.get("aliases", {}), f"{MIGRATIONS_PATH}: aliases")
    deprecated = require_mapping(
        document.get("deprecated", {}), f"{MIGRATIONS_PATH}: deprecated"
    )
    reserved_namespaces = require_mapping(
        document.get("reserved_namespaces", {}),
        f"{MIGRATIONS_PATH}: reserved_namespaces",
    )

    for alias_id, target_value in aliases.items():
        if alias_id in gates:
            raise RegistryError(
                f"{MIGRATIONS_PATH}: alias '{alias_id}' collides with a registered gate"
            )
        target = canonical_target(target_value, f"{MIGRATIONS_PATH}: aliases.{alias_id}")
        if target not in gates or gates[target]["status"] != "active":
            raise RegistryError(
                f"{MIGRATIONS_PATH}: alias '{alias_id}' targets non-active gate '{target}'"
            )

    for deprecated_id, config_value in deprecated.items():
        if deprecated_id not in gates or gates[deprecated_id]["status"] != "deprecated":
            raise RegistryError(
                f"{MIGRATIONS_PATH}: deprecated id '{deprecated_id}' must exist "
                f"in the registry with status deprecated"
            )
        config = require_mapping(
            config_value, f"{MIGRATIONS_PATH}: deprecated.{deprecated_id}"
        )
        replacements = require_string_list(
            config.get("replaced_by"),
            f"{MIGRATIONS_PATH}: deprecated.{deprecated_id}.replaced_by",
        )
        for replacement in replacements:
            if replacement not in gates or gates[replacement]["status"] != "active":
                raise RegistryError(
                    f"{MIGRATIONS_PATH}: deprecated id '{deprecated_id}' targets "
                    f"non-active replacement '{replacement}'"
                )

    for namespace in reserved_namespaces:
        if namespace in namespaces:
            raise RegistryError(
                f"{MIGRATIONS_PATH}: reserved namespace '{namespace}' already exists "
                f"in the registry"
            )
        if not NAMESPACE_RE.fullmatch(namespace):
            raise RegistryError(
                f"{MIGRATIONS_PATH}: invalid reserved namespace '{namespace}'"
            )

    retained = require_mapping(document.get("retained"), f"{MIGRATIONS_PATH}: retained")
    verified_legacy_ids = retained.get("verified_legacy_ids", [])
    if not isinstance(verified_legacy_ids, list):
        raise RegistryError(
            f"{MIGRATIONS_PATH}: retained.verified_legacy_ids must be a list"
        )
    for gate_id in verified_legacy_ids:
        gate_id = require_string(
            gate_id, f"{MIGRATIONS_PATH}: retained.verified_legacy_ids"
        )
        if gate_id not in gates or gates[gate_id]["status"] != "active":
            raise RegistryError(
                f"{MIGRATIONS_PATH}: retained legacy id '{gate_id}' is not active"
            )


def main() -> int:
    registry_document = load_yaml(REGISTRY_PATH)
    gates, context = flatten_registry(registry_document)
    validate_owner_definitions(gates)
    validate_migrations(
        gates,
        context["registry_version"],
        context["namespaces"],
    )

    active = sum(1 for gate in gates.values() if gate["status"] == "active")
    contextual_hard = sum(
        1 for gate in gates.values() if isinstance(gate["hard_gate_policy"], dict)
    )
    owners = sorted({gate["owner"] for gate in gates.values()})

    print(
        f"Validated design gate registry {context['registry_version']}: "
        f"{len(gates)} gate(s), {active} active, "
        f"{len(context['namespaces'])} namespace(s), "
        f"{contextual_hard} contextual hard gate(s)"
    )
    print(f"Owners: {', '.join(owners)}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (RegistryError, yaml.YAMLError) as error:
        print(f"design gate registry validation failed: {error}", file=sys.stderr)
        raise SystemExit(1) from error
