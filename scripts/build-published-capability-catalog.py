#!/usr/bin/env python3
"""Build and verify the consumer-facing capability catalog."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

DEFAULT_ROOT = Path(__file__).resolve().parents[1]
VALID_TYPES = {"skill", "workflow", "meta-skill"}


class CatalogError(RuntimeError):
    pass


def read_json(path: Path, root: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        try:
            display = path.relative_to(root)
        except ValueError:
            display = path
        raise CatalogError(f"{display} is not valid JSON: {error}") from error


def validate_revision(revision: str) -> None:
    if not re.fullmatch(r"[0-9a-f]{40}", revision):
        raise CatalogError("source revision must be an exact 40-character lowercase Git SHA")


def validate_inventory(inventory: dict) -> tuple[dict, list[dict]]:
    if inventory.get("schema_version") != 1:
        raise CatalogError("inventory schema_version must be 1")

    items = inventory.get("items")
    counts = inventory.get("counts")
    if not isinstance(items, list) or not isinstance(counts, dict):
        raise CatalogError("inventory must contain items and counts")

    names: set[str] = set()
    for item in items:
        if not isinstance(item, dict):
            raise CatalogError("every capability entry must be an object")
        name = item.get("name")
        capability_type = item.get("type")
        path = item.get("path")
        if not all(isinstance(value, str) and value for value in (name, capability_type, path)):
            raise CatalogError("every capability requires name, type, and path")
        if name in names:
            raise CatalogError(f"duplicate capability identity: {name}")
        names.add(name)
        if capability_type not in VALID_TYPES:
            raise CatalogError(f"unknown capability type for {name}: {capability_type}")
        expected_path = f"skills/{name}/SKILL.md"
        if path != expected_path:
            raise CatalogError(
                f"canonical path mismatch for {name}: expected {expected_path}, found {path}"
            )

    computed = {
        "skill": sum(item["type"] == "skill" for item in items),
        "workflow": sum(item["type"] == "workflow" for item in items),
        "meta-skill": sum(item["type"] == "meta-skill" for item in items),
        "total": len(items),
    }
    if counts != computed:
        raise CatalogError(
            f"inventory counts do not match items: expected {computed}, found {counts}"
        )

    return counts, items


def source_files(root: Path) -> dict[str, Path]:
    discovery = root / "catalog" / "capability-discovery"
    return {
        "inventory": root / "docs" / "capability-inventory.json",
        "facets": discovery / "facets.json",
        "classifications": discovery / "classifications.json",
        "topics": discovery / "topics.json",
        "job_profiles": discovery / "job-profiles.json",
    }


def build_catalog(revision: str, root: Path) -> dict:
    validate_revision(revision)
    files = source_files(root)
    documents = {name: read_json(path, root) for name, path in files.items()}
    counts, items = validate_inventory(documents["inventory"])

    for name in ("facets", "classifications", "topics", "job_profiles"):
        if documents[name].get("schema_version") != 2:
            raise CatalogError(f"{name} schema_version must be 2")

    return {
        "schema_version": 1,
        "catalog_version": "1.0.0",
        "compatibility": {
            "additive_changes_supported": True,
            "breaking_change_requires_consumer_review": True,
        },
        "source": {
            "repository": "puterakahfi/ai-native-skills",
            "revision": revision,
            "inventory_schema_version": 1,
            "discovery_schema_version": 2,
            "files": {
                name: path.relative_to(root).as_posix()
                for name, path in files.items()
            },
        },
        "inventory": {
            "counts": counts,
            "capabilities": items,
        },
        "discovery": {
            "facets": documents["facets"],
            "classifications": documents["classifications"],
            "topics": documents["topics"],
            "job_profiles": documents["job_profiles"],
        },
    }


def render(catalog: dict) -> str:
    return json.dumps(catalog, indent=2, ensure_ascii=False, sort_keys=True) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-revision")
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT, help=argparse.SUPPRESS)
    parser.add_argument("--output", type=Path, help=argparse.SUPPRESS)
    args = parser.parse_args()
    if args.write == args.check:
        parser.error("choose exactly one of --write or --check")

    root = args.root.resolve()
    output = (
        args.output.resolve()
        if args.output
        else root / "catalog" / "published" / "capability-catalog.json"
    )

    try:
        if args.check:
            if not output.is_file():
                try:
                    display = output.relative_to(root)
                except ValueError:
                    display = output
                raise CatalogError(f"{display} is missing")
            current = read_json(output, root)
            revision = current.get("source", {}).get("revision")
            if not isinstance(revision, str):
                raise CatalogError("published catalog source.revision is missing")
            expected = render(build_catalog(revision, root))
            actual = output.read_text(encoding="utf-8")
            if actual != expected:
                raise CatalogError("published capability catalog drifted from canonical sources")
        else:
            if not args.source_revision:
                raise CatalogError("--source-revision is required with --write")
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_text(render(build_catalog(args.source_revision, root)), encoding="utf-8")
    except CatalogError as error:
        print(f"published catalog error: {error}", file=sys.stderr)
        return 1

    try:
        display = output.relative_to(root)
    except ValueError:
        display = output
    action = "verified" if args.check else "generated"
    print(f"Published capability catalog {action}: {display}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
