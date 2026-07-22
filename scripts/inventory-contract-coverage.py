#!/usr/bin/env python3
"""Inventory executable contract coverage and compatibility registry integrity.

The inventory is intentionally descriptive. It never generates adapter conformance
claims or exemptions from legacy metadata.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable

import yaml

OFFICIAL_TYPES = {"skill", "workflow", "meta-skill"}
CONFORMANCE_FILE = "adapter.conformance.yaml"
EXEMPTION_FILES = ("contract.exemption.yaml", "contract-exemption.yaml")
SEMVER_PIN = re.compile(r"^(?:\^|~)?\d+\.\d+(?:\.\d+)?(?:-[0-9A-Za-z.-]+)?$")


def parse_scalar(value: Any) -> Any:
    if not isinstance(value, str):
        return value
    stripped = value.strip()
    if not stripped:
        return stripped
    if stripped[0] in "[{" and stripped[-1] in "]}":
        try:
            return json.loads(stripped)
        except json.JSONDecodeError:
            return value
    return value


def parse_frontmatter(path: Path) -> tuple[dict[str, Any], list[str]]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}, ["missing_yaml_frontmatter"]
    end = text.find("\n---", 4)
    if end < 0:
        return {}, ["unterminated_yaml_frontmatter"]
    try:
        payload = yaml.safe_load(text[4:end]) or {}
    except yaml.YAMLError as exc:
        return {}, [f"invalid_yaml_frontmatter:{exc.__class__.__name__}"]
    if not isinstance(payload, dict):
        return {}, ["frontmatter_root_not_mapping"]
    return payload, errors


def namespaced(metadata: dict[str, Any], key: str) -> Any:
    return parse_scalar(metadata.get(f"ai-native-skills.{key}"))


def normalized_list(value: Any) -> list[str]:
    value = parse_scalar(value)
    if value is None or value == "":
        return []
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    return [str(value).strip()]


def detect_patterns(metadata: dict[str, Any]) -> list[str]:
    patterns: set[str] = set()
    for key in ("pattern", "patterns"):
        patterns.update(normalized_list(namespaced(metadata, key)))
    for candidate in ("facade", "domain-reviewer", "runtime-adapter", "port-adapter"):
        value = namespaced(metadata, candidate)
        if value is True or str(value).lower() == "true":
            patterns.add(candidate)
    return sorted(patterns)


def load_yaml(path: Path) -> tuple[Any, list[str]]:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8")), []
    except (OSError, yaml.YAMLError) as exc:
        return None, [f"invalid_yaml:{exc.__class__.__name__}"]


def relative(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def resolve_contract_path(value: str, core_root: Path | None) -> tuple[str | None, bool | None]:
    normalized = value.strip()
    if normalized.startswith("ai-native-core/"):
        normalized = normalized.removeprefix("ai-native-core/")
    if not core_root:
        return normalized, None
    return normalized, (core_root / normalized).exists()


def inventory_skill(path: Path, root: Path, core_root: Path | None) -> dict[str, Any]:
    payload, errors = parse_frontmatter(path)
    metadata = payload.get("metadata") or {}
    if not isinstance(metadata, dict):
        metadata = {}
        errors.append("metadata_not_mapping")

    skill_id = str(payload.get("name") or path.parent.name)
    official_type = str(namespaced(metadata, "type") or "").strip()
    if official_type not in OFFICIAL_TYPES:
        errors.append("invalid_or_missing_official_type")

    implements = str(namespaced(metadata, "implements") or "").strip()
    contract_version = str(namespaced(metadata, "contract-version") or "").strip()
    contract_path, contract_exists = resolve_contract_path(implements, core_root) if implements else (None, None)

    if implements and not contract_version:
        errors.append("contract_version_missing")
    if contract_version and not SEMVER_PIN.fullmatch(contract_version):
        errors.append("contract_version_pin_invalid")
    if implements and contract_exists is False:
        errors.append("contract_path_missing")

    conformance_path = path.parent / CONFORMANCE_FILE
    exemption_path = next((path.parent / name for name in EXEMPTION_FILES if (path.parent / name).exists()), None)

    if conformance_path.exists():
        classification = "contract_backed_v2"
    elif implements:
        classification = "legacy_contract_backed"
    elif exemption_path:
        classification = "reviewed_exemption"
    else:
        classification = "unowned"

    if errors:
        classification = "invalid"

    return {
        "id": skill_id,
        "path": relative(path, root),
        "type": official_type or None,
        "patterns": detect_patterns(metadata),
        "version": namespaced(metadata, "version"),
        "implements": contract_path,
        "contract_version": contract_version or None,
        "contract_path_exists": contract_exists,
        "legacy_boundary": {
            "covers": normalized_list(namespaced(metadata, "boundary.covers")),
            "delegates": normalized_list(namespaced(metadata, "boundary.delegates")),
        },
        "conformance_path": relative(conformance_path, root) if conformance_path.exists() else None,
        "exemption_path": relative(exemption_path, root) if exemption_path else None,
        "classification": classification,
        "errors": sorted(errors),
    }


def walk_items(value: Any, prefix: tuple[str, ...] = ()) -> Iterable[tuple[tuple[str, ...], Any]]:
    if isinstance(value, dict):
        for key, child in value.items():
            yield from walk_items(child, (*prefix, str(key)))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk_items(child, (*prefix, str(index)))
    else:
        yield prefix, value


def likely_repository_key(key: str) -> bool:
    return key in {"repository", "repo", "repository_url", "repository_full_name"}


def likely_implementation_path(key: str) -> bool:
    return key in {"implementation_path", "skill_path", "entrypoint", "adapter_path"}


def likely_contract_path(key: str) -> bool:
    return key in {"contract_path", "implements", "core_contract_path"}


def likely_version_pin(key: str) -> bool:
    return key in {"contract_version", "version_pin", "version_range", "compatible_version"}


def normalize_repo_coordinate(value: str) -> str:
    value = value.strip().removesuffix(".git")
    for prefix in ("https://github.com/", "git@github.com:", "github.com/"):
        if value.startswith(prefix):
            value = value.removeprefix(prefix)
    return value.strip("/")


def inventory_compat(path: Path, root: Path, core_root: Path | None) -> dict[str, Any]:
    payload, errors = load_yaml(path)
    if not isinstance(payload, dict):
        return {
            "path": relative(path, root),
            "ids": [],
            "repository_coordinates": [],
            "implementation_paths": [],
            "contract_paths": [],
            "version_pins": [],
            "errors": sorted(errors + ["compat_root_not_mapping"]),
        }

    ids: set[str] = set()
    repositories: list[dict[str, Any]] = []
    implementations: list[dict[str, Any]] = []
    contracts: list[dict[str, Any]] = []
    pins: list[dict[str, Any]] = []

    for key_path, raw in walk_items(payload):
        if not key_path or not isinstance(raw, (str, int, float)):
            continue
        key = key_path[-1]
        value = str(raw).strip()
        location = ".".join(key_path)
        if key in {"id", "adapter_id", "skill_id", "runtime_adapter_id", "binding_id"} and value:
            ids.add(value)
        if likely_repository_key(key) and value:
            normalized = normalize_repo_coordinate(value)
            repositories.append({"field": location, "value": value, "normalized": normalized})
            if "/" not in normalized or normalized.count("/") != 1:
                errors.append(f"invalid_repository_coordinate:{location}")
        if likely_implementation_path(key) and value:
            normalized = value.removeprefix("ai-native-skills/")
            exists = (root / normalized).exists()
            implementations.append({"field": location, "value": normalized, "exists": exists})
            if not exists:
                errors.append(f"missing_implementation_path:{location}")
        if likely_contract_path(key) and value:
            normalized, exists = resolve_contract_path(value, core_root)
            contracts.append({"field": location, "value": normalized, "exists": exists})
            if normalized and normalized.startswith("skills/"):
                errors.append(f"circular_implementation_as_contract:{location}")
            if exists is False:
                errors.append(f"missing_contract_path:{location}")
        if likely_version_pin(key) and value:
            pins.append({"field": location, "value": value, "valid": bool(SEMVER_PIN.fullmatch(value))})
            if not SEMVER_PIN.fullmatch(value):
                errors.append(f"invalid_version_pin:{location}")

    implementation_values = {item["value"] for item in implementations}
    contract_values = {item["value"] for item in contracts}
    if implementation_values & contract_values:
        errors.append("circular_contract_and_implementation_path")

    return {
        "path": relative(path, root),
        "root_keys": sorted(str(key) for key in payload),
        "ids": sorted(ids),
        "repository_coordinates": repositories,
        "implementation_paths": implementations,
        "contract_paths": contracts,
        "version_pins": pins,
        "errors": sorted(set(errors)),
    }


def build_inventory(root: Path, core_root: Path | None) -> dict[str, Any]:
    skills = [inventory_skill(path, root, core_root) for path in sorted((root / "skills").glob("*/SKILL.md"))]
    compat_files = sorted((root / "compat").rglob("*.compat.yaml")) if (root / "compat").exists() else []
    compat = [inventory_compat(path, root, core_root) for path in compat_files]

    id_locations: dict[str, list[str]] = defaultdict(list)
    for record in compat:
        for adapter_id in record["ids"]:
            id_locations[adapter_id].append(record["path"])
    duplicate_ids = {key: value for key, value in sorted(id_locations.items()) if len(value) > 1}

    type_counts = Counter(record["type"] or "missing" for record in skills)
    pattern_counts = Counter(pattern for record in skills for pattern in record["patterns"])
    classification_counts = Counter(record["classification"] for record in skills)

    return {
        "contract_coverage_inventory": {
            "schema_version": "0.1.0",
            "repository": "puterakahfi/ai-native-skills",
            "issue": 26,
            "core_repository": "puterakahfi/ai-native-core",
            "summary": {
                "executable_artifacts": len(skills),
                "official_types": dict(sorted(type_counts.items())),
                "patterns": dict(sorted(pattern_counts.items())),
                "coverage": dict(sorted(classification_counts.items())),
                "compatibility_manifests": len(compat),
                "compatibility_manifests_with_errors": sum(bool(item["errors"]) for item in compat),
                "duplicate_compatibility_ids": len(duplicate_ids),
            },
            "artifacts": skills,
            "compatibility_manifests": compat,
            "duplicate_compatibility_ids": duplicate_ids,
            "interpretation": [
                "legacy_contract_backed means path and version metadata exist but no reviewed v2 declaration exists",
                "unowned means neither an authoritative contract nor a reviewed exemption is declared",
                "inventory presence does not prove structural conformance or executable behavior",
                "compatibility path existence does not prove runtime or product acceptance",
            ],
        }
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="ai-native-skills repository root")
    parser.add_argument("--core-root", help="optional checked-out ai-native-core root")
    parser.add_argument("--output", default="docs/contract-coverage-discovery.yaml")
    parser.add_argument("--check", action="store_true", help="fail when generated output differs")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    core_root = Path(args.core_root).resolve() if args.core_root else None
    inventory = build_inventory(root, core_root)
    rendered = yaml.safe_dump(inventory, sort_keys=False, allow_unicode=True)
    output = root / args.output

    if args.check:
        if not output.exists() or output.read_text(encoding="utf-8") != rendered:
            print(f"FAIL — {output.relative_to(root)} is stale")
            return 1
        print(f"PASS — {output.relative_to(root)} matches the repository")
        return 0

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(rendered, encoding="utf-8")
    summary = inventory["contract_coverage_inventory"]["summary"]
    print(yaml.safe_dump(summary, sort_keys=False).strip())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
