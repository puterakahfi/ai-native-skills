#!/usr/bin/env python3
"""Build and verify the consumer-facing capability catalog."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "catalog" / "published" / "capability-catalog.json"
INVENTORY = ROOT / "docs" / "capability-inventory.json"
DISCOVERY = ROOT / "catalog" / "capability-discovery"
SOURCE_FILES = {
    "inventory": INVENTORY,
    "facets": DISCOVERY / "facets.json",
    "classifications": DISCOVERY / "classifications.json",
    "topics": DISCOVERY / "topics.json",
    "job_profiles": DISCOVERY / "job-profiles.json",
}
VALID_TYPES = {"skill", "workflow", "meta-skill"}
CATALOG_SCHEMA_VERSION = 1
CATALOG_VERSION = "1.0.0"


class CatalogError(RuntimeError):
    """Raised when canonical source data or a published catalog is invalid."""


def read_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise CatalogError(f"{path}: invalid JSON: {error}") from error
    if not isinstance(value, dict):
        raise CatalogError(f"{path}: root must be an object")
    return value


def validate_revision(revision: str) -> None:
    if not re.fullmatch(r"[0-9a-f]{40}", revision):
        raise CatalogError("source revision must be an exact 40-character lowercase Git SHA")


def validate_inventory(inventory: dict[str, Any]) -> tuple[dict[str, int], list[dict[str, Any]]]:
    if inventory.get("schema_version") != 1:
        raise CatalogError("inventory schema_version must be 1")
    items = inventory.get("items")
    counts = inventory.get("counts")
    if not isinstance(items, list) or not isinstance(counts, dict):
        raise CatalogError("inventory must contain object counts and array items")

    names: set[str] = set()
    normalized: list[dict[str, Any]] = []
    for raw in items:
        if not isinstance(raw, dict):
            raise CatalogError("every capability entry must be an object")
        name, capability_type, path = raw.get("name"), raw.get("type"), raw.get("path")
        if not all(isinstance(value, str) and value for value in (name, capability_type, path)):
            raise CatalogError("every capability requires non-empty name, type, and path")
        if name in names:
            raise CatalogError(f"duplicate capability identity: {name}")
        names.add(name)
        if capability_type not in VALID_TYPES:
            raise CatalogError(f"unknown capability type for {name}: {capability_type}")
        expected_path = f"skills/{name}/SKILL.md"
        if path != expected_path:
            raise CatalogError(f"canonical path mismatch for {name}: expected {expected_path}, found {path}")
        normalized.append(dict(raw))

    computed = {
        "skill": sum(item["type"] == "skill" for item in normalized),
        "workflow": sum(item["type"] == "workflow" for item in normalized),
        "meta-skill": sum(item["type"] == "meta-skill" for item in normalized),
        "total": len(normalized),
    }
    if counts != computed:
        raise CatalogError(f"inventory counts do not match items: expected {computed}, found {counts}")
    return computed, normalized


def collect_references(value: Any, known: set[str], location: str = "discovery") -> None:
    """Fail closed on explicit capability reference fields with unknown identities."""
    if isinstance(value, dict):
        for key, child in value.items():
            child_location = f"{location}.{key}"
            if key in {"capability", "capabilities", "skills", "workflows", "meta_skills"}:
                refs = [child] if isinstance(child, str) else child if isinstance(child, list) else []
                for ref in refs:
                    if isinstance(ref, str) and ref not in known:
                        raise CatalogError(f"unknown capability reference at {child_location}: {ref}")
            collect_references(child, known, child_location)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            collect_references(child, known, f"{location}[{index}]")


def build_catalog(revision: str, source_files: dict[str, Path] | None = None) -> dict[str, Any]:
    validate_revision(revision)
    files = source_files or SOURCE_FILES
    documents = {name: read_json(path) for name, path in files.items()}
    counts, items = validate_inventory(documents["inventory"])
    known = {item["name"] for item in items}

    for name in ("facets", "classifications", "topics", "job_profiles"):
        if documents[name].get("schema_version") != 2:
            raise CatalogError(f"{name} schema_version must be 2")
        collect_references(documents[name], known, name)

    return {
        "schema_version": CATALOG_SCHEMA_VERSION,
        "catalog_version": CATALOG_VERSION,
        "compatibility": {
            "policy": "semver",
            "additive_changes_supported": True,
            "breaking_change_requires_consumer_review": True,
        },
        "source": {
            "repository": "puterakahfi/ai-native-skills",
            "revision": revision,
            "inventory_schema_version": 1,
            "discovery_schema_version": 2,
            "files": {name: path.relative_to(ROOT).as_posix() for name, path in files.items()},
        },
        "inventory": {"counts": counts, "capabilities": items},
        "discovery": {
            "facets": documents["facets"],
            "classifications": documents["classifications"],
            "topics": documents["topics"],
            "job_profiles": documents["job_profiles"],
        },
    }


def compatibility_changes(previous: dict[str, Any], current: dict[str, Any]) -> dict[str, list[str]]:
    """Classify catalog identity/type changes for consumers."""
    if previous.get("schema_version") != current.get("schema_version"):
        return {"additive": [], "breaking": ["schema_version changed"]}

    def identities(catalog: dict[str, Any]) -> dict[str, str]:
        capabilities = catalog.get("inventory", {}).get("capabilities", [])
        if not isinstance(capabilities, list):
            raise CatalogError("catalog inventory.capabilities must be an array")
        result: dict[str, str] = {}
        for item in capabilities:
            if not isinstance(item, dict) or not isinstance(item.get("name"), str) or not isinstance(item.get("type"), str):
                raise CatalogError("catalog capability entries require name and type")
            result[item["name"]] = item["type"]
        return result

    before, after = identities(previous), identities(current)
    additive = [f"capability added: {name}" for name in sorted(after.keys() - before.keys())]
    breaking = [f"capability removed: {name}" for name in sorted(before.keys() - after.keys())]
    for name in sorted(before.keys() & after.keys()):
        if before[name] != after[name]:
            breaking.append(f"capability type changed: {name} ({before[name]} -> {after[name]})")
    return {"additive": additive, "breaking": breaking}


def render(catalog: dict[str, Any]) -> str:
    return json.dumps(catalog, indent=2, ensure_ascii=False, sort_keys=True) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    parser.add_argument("--source-revision")
    parser.add_argument("--baseline", type=Path)
    args = parser.parse_args()

    try:
        if args.write:
            if not args.source_revision:
                raise CatalogError("--source-revision is required with --write")
            catalog = build_catalog(args.source_revision)
            OUTPUT.parent.mkdir(parents=True, exist_ok=True)
            OUTPUT.write_text(render(catalog), encoding="utf-8")
            print(f"Published capability catalog generated: {OUTPUT.relative_to(ROOT)}")
        else:
            if not OUTPUT.is_file():
                raise CatalogError(f"{OUTPUT.relative_to(ROOT)} is missing")
            current = read_json(OUTPUT)
            revision = current.get("source", {}).get("revision")
            if not isinstance(revision, str):
                raise CatalogError("published catalog source.revision is missing")
            expected = render(build_catalog(revision))
            actual = OUTPUT.read_text(encoding="utf-8")
            if actual != expected:
                raise CatalogError("published capability catalog drifted from canonical sources")
            if args.baseline:
                changes = compatibility_changes(read_json(args.baseline), current)
                print(json.dumps(changes, sort_keys=True))
                if changes["breaking"]:
                    raise CatalogError("breaking catalog changes require explicit consumer review")
            print(f"Published capability catalog verified: {OUTPUT.relative_to(ROOT)}")
    except CatalogError as error:
        print(f"published catalog error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
