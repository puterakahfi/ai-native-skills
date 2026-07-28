#!/usr/bin/env python3
"""Build and verify the consumer-facing capability catalog."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

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


class CatalogError(RuntimeError):
    pass


def read_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise CatalogError(f"{path.relative_to(ROOT)} is not valid JSON: {error}") from error


def validate_revision(revision: str) -> None:
    if not re.fullmatch(r"[0-9a-f]{40}", revision):
        raise CatalogError("source revision must be an exact 40-character lowercase Git SHA")


def build_catalog(revision: str) -> dict:
    validate_revision(revision)
    documents = {name: read_json(path) for name, path in SOURCE_FILES.items()}
    inventory = documents["inventory"]
    items = inventory.get("items")
    counts = inventory.get("counts")
    if not isinstance(items, list) or not isinstance(counts, dict):
        raise CatalogError("inventory must contain items and counts")

    names: set[str] = set()
    for item in items:
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

    computed = {
        "skill": sum(item["type"] == "skill" for item in items),
        "workflow": sum(item["type"] == "workflow" for item in items),
        "meta-skill": sum(item["type"] == "meta-skill" for item in items),
        "total": len(items),
    }
    if counts != computed:
        raise CatalogError(f"inventory counts do not match items: expected {computed}, found {counts}")

    for name in ("facets", "classifications", "topics", "job_profiles"):
        if documents[name].get("schema_version") != 2:
            raise CatalogError(f"{name} schema_version must be 2")

    return {
        "schema_version": 1,
        "catalog_version": 1,
        "compatibility": {
            "change_model": "additive-by-default",
            "breaking_when": [
                "schema_version changes",
                "catalog_version changes incompatibly",
                "capability identity is removed",
                "capability executable type changes",
                "required fields are removed",
            ],
        },
        "source": {
            "repository": "puterakahfi/ai-native-skills",
            "revision": revision,
            "files": {name: path.relative_to(ROOT).as_posix() for name, path in SOURCE_FILES.items()},
        },
        "inventory": inventory,
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
    args = parser.parse_args()
    if args.write == args.check:
        parser.error("choose exactly one of --write or --check")

    try:
        if args.check:
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
        else:
            if not args.source_revision:
                raise CatalogError("--source-revision is required with --write")
            OUTPUT.parent.mkdir(parents=True, exist_ok=True)
            OUTPUT.write_text(render(build_catalog(args.source_revision)), encoding="utf-8")
    except CatalogError as error:
        print(f"published catalog error: {error}", file=sys.stderr)
        return 1

    print(f"Published capability catalog {'verified' if args.check else 'generated'}: {OUTPUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
