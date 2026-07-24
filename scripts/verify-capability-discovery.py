#!/usr/bin/env python3
"""Validate capability discovery facets, topics, and job profiles against inventory."""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
INVENTORY_PATH = ROOT / "docs" / "capability-inventory.json"
MANIFEST_PATH = ROOT / "catalog" / "capability-discovery" / "manifest.json"
SCHEMA_VERSION = 2
FACET_KEYS = ("domains", "lifecycle_stages", "concerns", "ecosystems")
CLASSIFICATION_METADATA_KEYS = ("cross_cutting_reason",)
FILE_KEYS = ("facets", "classifications", "topics", "job_profiles")
MAX_NON_WORKFLOW_DOMAINS = 3
REQUIRED_JOB_PROFILES = {
    "product-planning",
    "engineering-quality",
    "security-engineering",
}
REQUIRED_TOPICS = {
    "product-management",
    "software-architecture",
    "engineering-quality",
    "security-engineering",
    "design-ui",
    "agent-workflows",
    "ai-agent-systems",
    "operations-reliability",
    "developer-experience",
    "growth-marketing",
}


class DiscoveryError(RuntimeError):
    """Raised when discovery data is invalid or drifts from inventory."""


def load_json(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise DiscoveryError(f"{path.relative_to(ROOT)} is missing")
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise DiscoveryError(
            f"{path.relative_to(ROOT)} is invalid JSON: {error}"
        ) from error
    if not isinstance(value, dict):
        raise DiscoveryError(f"{path.relative_to(ROOT)} must contain a JSON object")
    return value


def require_string(value: Any, location: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise DiscoveryError(f"{location} must be a non-empty string")
    return value


def require_string_list(
    value: Any,
    location: str,
    *,
    allow_empty: bool = False,
) -> list[str]:
    if not isinstance(value, list):
        raise DiscoveryError(f"{location} must be a list")
    if not allow_empty and not value:
        raise DiscoveryError(f"{location} must not be empty")
    if any(not isinstance(item, str) or not item.strip() for item in value):
        raise DiscoveryError(f"{location} must contain only non-empty strings")
    duplicates = sorted(name for name, count in Counter(value).items() if count > 1)
    if duplicates:
        raise DiscoveryError(
            f"{location} contains duplicates: {', '.join(duplicates)}"
        )
    return value


def load_catalog() -> dict[str, dict[str, Any]]:
    manifest = load_json(MANIFEST_PATH)
    if manifest.get("schema_version") != SCHEMA_VERSION:
        raise DiscoveryError(
            f"catalog manifest schema_version must be {SCHEMA_VERSION}"
        )
    require_string(manifest.get("source"), "catalog manifest source")

    files = manifest.get("files")
    if not isinstance(files, dict):
        raise DiscoveryError("catalog manifest files must be an object")
    missing_keys = sorted(set(FILE_KEYS) - set(files))
    extra_keys = sorted(set(files) - set(FILE_KEYS))
    if missing_keys or extra_keys:
        parts: list[str] = []
        if missing_keys:
            parts.append("missing: " + ", ".join(missing_keys))
        if extra_keys:
            parts.append("unknown: " + ", ".join(extra_keys))
        raise DiscoveryError("catalog manifest file keys invalid: " + "; ".join(parts))

    loaded: dict[str, dict[str, Any]] = {}
    for key in FILE_KEYS:
        relative = Path(require_string(files[key], f"catalog manifest files.{key}"))
        path = (ROOT / relative).resolve()
        try:
            path.relative_to(ROOT.resolve())
        except ValueError as error:
            raise DiscoveryError(
                f"catalog manifest files.{key} escapes repository root"
            ) from error
        document = load_json(path)
        if document.get("schema_version") != SCHEMA_VERSION:
            raise DiscoveryError(
                f"{relative.as_posix()} schema_version must be {SCHEMA_VERSION}"
            )
        loaded[key] = document
    return loaded


def inventory_types(inventory: dict[str, Any]) -> dict[str, str]:
    items = inventory.get("items")
    if not isinstance(items, list) or not items:
        raise DiscoveryError("docs/capability-inventory.json has no items")

    result: dict[str, str] = {}
    for index, item in enumerate(items):
        if not isinstance(item, dict):
            raise DiscoveryError(f"inventory.items[{index}] must be an object")
        name = require_string(item.get("name"), f"inventory.items[{index}].name")
        capability_type = require_string(
            item.get("type"), f"inventory.items[{index}].type"
        )
        if name in result:
            raise DiscoveryError(f"inventory contains duplicate capability {name!r}")
        result[name] = capability_type
    return result


def validate_facet_definitions(document: dict[str, Any]) -> dict[str, set[str]]:
    facets = document.get("facets")
    if not isinstance(facets, dict):
        raise DiscoveryError("facets must be an object")

    missing_keys = sorted(set(FACET_KEYS) - set(facets))
    extra_keys = sorted(set(facets) - set(FACET_KEYS))
    if missing_keys or extra_keys:
        parts: list[str] = []
        if missing_keys:
            parts.append("missing: " + ", ".join(missing_keys))
        if extra_keys:
            parts.append("unknown: " + ", ".join(extra_keys))
        raise DiscoveryError("facet keys invalid: " + "; ".join(parts))

    allowed: dict[str, set[str]] = {}
    for facet_key in FACET_KEYS:
        values = facets.get(facet_key)
        if not isinstance(values, list) or not values:
            raise DiscoveryError(f"facets.{facet_key} must be a non-empty list")

        ids: list[str] = []
        for index, item in enumerate(values):
            location = f"facets.{facet_key}[{index}]"
            if not isinstance(item, dict):
                raise DiscoveryError(f"{location} must be an object")
            ids.append(require_string(item.get("id"), f"{location}.id"))
            require_string(item.get("label"), f"{location}.label")
            if "description" in item:
                require_string(item.get("description"), f"{location}.description")

        duplicates = sorted(name for name, count in Counter(ids).items() if count > 1)
        if duplicates:
            raise DiscoveryError(
                f"facets.{facet_key} duplicate ids: {', '.join(duplicates)}"
            )
        allowed[facet_key] = set(ids)
    return allowed


def resolve_classification(
    defaults: dict[str, Any],
    override: dict[str, Any],
    allowed: dict[str, set[str]],
    location: str,
) -> tuple[dict[str, list[str]], str | None]:
    permitted = set(FACET_KEYS) | set(CLASSIFICATION_METADATA_KEYS)
    unknown_default_keys = sorted(set(defaults) - permitted)
    if unknown_default_keys:
        raise DiscoveryError(
            f"{location}.defaults has unknown keys: "
            + ", ".join(unknown_default_keys)
        )
    unknown_override_keys = sorted(set(override) - permitted)
    if unknown_override_keys:
        raise DiscoveryError(
            f"{location} has unknown keys: " + ", ".join(unknown_override_keys)
        )

    result: dict[str, list[str]] = {}
    for facet_key in FACET_KEYS:
        values = require_string_list(
            override.get(facet_key, defaults.get(facet_key)),
            f"{location}.{facet_key}",
        )
        unknown = sorted(set(values) - allowed[facet_key])
        if unknown:
            raise DiscoveryError(
                f"{location}.{facet_key} unknown values: " + ", ".join(unknown)
            )
        result[facet_key] = values

    reason = override.get(
        "cross_cutting_reason",
        defaults.get("cross_cutting_reason"),
    )
    if reason is not None:
        reason = require_string(reason, f"{location}.cross_cutting_reason")
    return result, reason


def validate_classifications(
    document: dict[str, Any],
    inventory: dict[str, str],
    allowed: dict[str, set[str]],
) -> dict[str, dict[str, list[str]]]:
    groups = document.get("classification_groups")
    if not isinstance(groups, list) or not groups:
        raise DiscoveryError("classification_groups must be a non-empty list")

    group_ids: list[str] = []
    assignments: list[str] = []
    resolved: dict[str, dict[str, list[str]]] = {}

    for group_index, group in enumerate(groups):
        location = f"classification_groups[{group_index}]"
        if not isinstance(group, dict):
            raise DiscoveryError(f"{location} must be an object")

        group_ids.append(require_string(group.get("id"), f"{location}.id"))
        defaults = group.get("defaults")
        if not isinstance(defaults, dict):
            raise DiscoveryError(f"{location}.defaults must be an object")

        capabilities = require_string_list(
            group.get("capabilities"), f"{location}.capabilities"
        )
        unknown = sorted(set(capabilities) - set(inventory))
        if unknown:
            raise DiscoveryError(
                f"{location}.capabilities unknown: " + ", ".join(unknown)
            )
        assignments.extend(capabilities)

        overrides = group.get("overrides", {})
        if not isinstance(overrides, dict):
            raise DiscoveryError(f"{location}.overrides must be an object")
        outside = sorted(set(overrides) - set(capabilities))
        if outside:
            raise DiscoveryError(
                f"{location}.overrides outside group: " + ", ".join(outside)
            )

        for capability in capabilities:
            override = overrides.get(capability, {})
            if not isinstance(override, dict):
                raise DiscoveryError(
                    f"{location}.overrides.{capability} must be an object"
                )
            classification, cross_cutting_reason = resolve_classification(
                defaults,
                override,
                allowed,
                f"{location}.overrides.{capability}",
            )
            domain_count = len(classification["domains"])
            if inventory[capability] != "workflow":
                if (
                    domain_count > MAX_NON_WORKFLOW_DOMAINS
                    and cross_cutting_reason is None
                ):
                    raise DiscoveryError(
                        f"{capability!r} has {domain_count} primary domains; "
                        "non-workflow capabilities may use at most "
                        f"{MAX_NON_WORKFLOW_DOMAINS} without cross_cutting_reason"
                    )
                if (
                    domain_count <= MAX_NON_WORKFLOW_DOMAINS
                    and cross_cutting_reason is not None
                ):
                    raise DiscoveryError(
                        f"{capability!r} has unnecessary cross_cutting_reason"
                    )
            resolved[capability] = classification

    duplicate_groups = sorted(
        name for name, count in Counter(group_ids).items() if count > 1
    )
    if duplicate_groups:
        raise DiscoveryError(
            "classification_groups duplicate ids: " + ", ".join(duplicate_groups)
        )

    duplicate_assignments = sorted(
        name for name, count in Counter(assignments).items() if count > 1
    )
    if duplicate_assignments:
        raise DiscoveryError(
            "capabilities assigned to multiple groups: "
            + ", ".join(duplicate_assignments)
        )

    missing = sorted(set(inventory) - set(assignments))
    extra = sorted(set(assignments) - set(inventory))
    if missing or extra:
        parts: list[str] = []
        if missing:
            parts.append("missing: " + ", ".join(missing))
        if extra:
            parts.append("unknown: " + ", ".join(extra))
        raise DiscoveryError("capability discovery coverage mismatch: " + "; ".join(parts))

    return resolved


def validate_topics(
    document: dict[str, Any],
    inventory: dict[str, str],
) -> int:
    topics = document.get("topics")
    if not isinstance(topics, list) or not topics:
        raise DiscoveryError("topics must be a non-empty list")

    topic_ids: list[str] = []
    for topic_index, topic in enumerate(topics):
        location = f"topics[{topic_index}]"
        if not isinstance(topic, dict):
            raise DiscoveryError(f"{location} must be an object")

        topic_ids.append(require_string(topic.get("id"), f"{location}.id"))
        require_string(topic.get("label"), f"{location}.label")
        require_string(topic.get("description"), f"{location}.description")

        capabilities = require_string_list(
            topic.get("capabilities"), f"{location}.capabilities"
        )
        starting_points = require_string_list(
            topic.get("starting_points"), f"{location}.starting_points"
        )
        unknown = sorted(set(capabilities) - set(inventory))
        if unknown:
            raise DiscoveryError(
                f"{location}.capabilities unknown: " + ", ".join(unknown)
            )
        outside = sorted(set(starting_points) - set(capabilities))
        if outside:
            raise DiscoveryError(
                f"{location}.starting_points outside topic capabilities: "
                + ", ".join(outside)
            )

    duplicate_ids = sorted(
        name for name, count in Counter(topic_ids).items() if count > 1
    )
    if duplicate_ids:
        raise DiscoveryError("topics duplicate ids: " + ", ".join(duplicate_ids))

    missing_topics = sorted(REQUIRED_TOPICS - set(topic_ids))
    if missing_topics:
        raise DiscoveryError(
            "topics missing required entries: " + ", ".join(missing_topics)
        )
    return len(topics)


def validate_job_profiles(
    document: dict[str, Any],
    inventory: dict[str, str],
) -> int:
    profiles = document.get("job_profiles")
    if not isinstance(profiles, list) or not profiles:
        raise DiscoveryError("job_profiles must be a non-empty list")

    profile_ids: list[str] = []
    for profile_index, profile in enumerate(profiles):
        location = f"job_profiles[{profile_index}]"
        if not isinstance(profile, dict):
            raise DiscoveryError(f"{location} must be an object")

        profile_ids.append(require_string(profile.get("id"), f"{location}.id"))
        require_string(profile.get("label"), f"{location}.label")
        require_string(profile.get("question"), f"{location}.question")

        routes = profile.get("workflow_routes")
        if not isinstance(routes, list) or not routes:
            raise DiscoveryError(f"{location}.workflow_routes must be non-empty")
        for route_index, route in enumerate(routes):
            route_location = f"{location}.workflow_routes[{route_index}]"
            if not isinstance(route, dict):
                raise DiscoveryError(f"{route_location} must be an object")
            require_string(route.get("when"), f"{route_location}.when")
            workflow = require_string(
                route.get("workflow"), f"{route_location}.workflow"
            )
            capability_type = inventory.get(workflow)
            if capability_type is None:
                raise DiscoveryError(
                    f"{route_location}.workflow unknown capability {workflow!r}"
                )
            if capability_type != "workflow":
                raise DiscoveryError(
                    f"{route_location}.workflow must reference a workflow; "
                    f"{workflow!r} is {capability_type!r}"
                )

        groups = profile.get("capability_groups")
        if not isinstance(groups, list) or not groups:
            raise DiscoveryError(f"{location}.capability_groups must be non-empty")

        grouped: list[str] = []
        for group_index, group in enumerate(groups):
            group_location = f"{location}.capability_groups[{group_index}]"
            if not isinstance(group, dict):
                raise DiscoveryError(f"{group_location} must be an object")
            require_string(group.get("purpose"), f"{group_location}.purpose")
            required = require_string_list(
                group.get("required"), f"{group_location}.required"
            )
            optional = require_string_list(
                group.get("optional"),
                f"{group_location}.optional",
                allow_empty=True,
            )
            unknown = sorted(set(required + optional) - set(inventory))
            if unknown:
                raise DiscoveryError(
                    f"{group_location} unknown capabilities: " + ", ".join(unknown)
                )
            grouped.extend(required + optional)

        repeated = sorted(name for name, count in Counter(grouped).items() if count > 1)
        if repeated:
            raise DiscoveryError(
                f"{location} repeats capabilities across groups: "
                + ", ".join(repeated)
            )

        require_string_list(
            profile.get("expected_evidence"), f"{location}.expected_evidence"
        )
        require_string(profile.get("completion_gate"), f"{location}.completion_gate")

    duplicate_ids = sorted(
        name for name, count in Counter(profile_ids).items() if count > 1
    )
    if duplicate_ids:
        raise DiscoveryError(
            "job_profiles duplicate ids: " + ", ".join(duplicate_ids)
        )

    missing_profiles = sorted(REQUIRED_JOB_PROFILES - set(profile_ids))
    if missing_profiles:
        raise DiscoveryError(
            "job_profiles missing required profiles: " + ", ".join(missing_profiles)
        )
    return len(profiles)


def main() -> int:
    try:
        inventory_document = load_json(INVENTORY_PATH)
        catalog = load_catalog()
        inventory = inventory_types(inventory_document)
        allowed = validate_facet_definitions(catalog["facets"])
        resolved = validate_classifications(
            catalog["classifications"], inventory, allowed
        )
        topic_count = validate_topics(catalog["topics"], inventory)
        profile_count = validate_job_profiles(catalog["job_profiles"], inventory)
    except DiscoveryError as error:
        print(f"discovery error: {error}", file=sys.stderr)
        return 1

    print(
        "Capability discovery verified: "
        f"{len(resolved)} classified capabilities, "
        f"{topic_count} topics, {profile_count} job profiles."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
