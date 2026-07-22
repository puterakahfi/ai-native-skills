#!/usr/bin/env python3
"""Derive and validate the executable capability inventory from SKILL.md metadata."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
README_PATH = ROOT / "README.md"
TAXONOMY_PATH = ROOT / "docs" / "skills.md"
SNAPSHOT_PATH = ROOT / "docs" / "capability-inventory.json"
VALID_TYPES = ("skill", "workflow", "meta-skill")


class InventoryError(RuntimeError):
    """Raised when executable metadata or documentation drifts."""


def scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def parse_skill(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise InventoryError(f"{path.relative_to(ROOT)}: missing opening frontmatter delimiter")

    try:
        end = next(
            index
            for index, line in enumerate(lines[1:], start=1)
            if line.strip() == "---"
        )
    except StopIteration as exc:
        raise InventoryError(
            f"{path.relative_to(ROOT)}: missing closing frontmatter delimiter"
        ) from exc

    frontmatter = lines[1:end]
    name: str | None = None
    capability_type: str | None = None

    for line in frontmatter:
        name_match = re.match(r"^name:\s*(.+?)\s*$", line)
        if name_match:
            name = scalar(name_match.group(1))
            continue

        type_match = re.match(r"^\s+ai-native-skills\.type:\s*(.+?)\s*$", line)
        if type_match:
            capability_type = scalar(type_match.group(1))

    relative = path.relative_to(ROOT)
    if not name:
        raise InventoryError(f"{relative}: missing top-level name")
    if not capability_type:
        raise InventoryError(f'{relative}: missing metadata["ai-native-skills.type"]')
    if capability_type not in VALID_TYPES:
        raise InventoryError(
            f"{relative}: invalid ai-native-skills.type {capability_type!r}; "
            f"expected one of {', '.join(VALID_TYPES)}"
        )

    return {
        "name": name,
        "type": capability_type,
        "path": relative.as_posix(),
    }


def derive_inventory() -> dict[str, object]:
    if not SKILLS_DIR.is_dir():
        raise InventoryError("skills directory is missing")

    capability_dirs = sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir())
    missing_entrypoints = [
        path.name for path in capability_dirs if not (path / "SKILL.md").is_file()
    ]
    if missing_entrypoints:
        raise InventoryError(
            "Capability directories missing SKILL.md: " + ", ".join(missing_entrypoints)
        )

    items = [parse_skill(path / "SKILL.md") for path in capability_dirs]
    name_counts = Counter(item["name"] for item in items)
    duplicate_names = sorted(
        name for name, count in name_counts.items() if count > 1
    )
    if duplicate_names:
        raise InventoryError("Duplicate capability names: " + ", ".join(duplicate_names))

    path_mismatches = []
    for item in items:
        directory_name = Path(item["path"]).parent.name
        if directory_name != item["name"]:
            path_mismatches.append(
                f"{item['path']}: directory {directory_name!r} != name {item['name']!r}"
            )
    if path_mismatches:
        raise InventoryError("Capability path/name mismatch: " + "; ".join(path_mismatches))

    counts = Counter(item["type"] for item in items)
    ordered_items = sorted(items, key=lambda item: (item["type"], item["name"]))
    return {
        "schema_version": 1,
        "source": "skills/*/SKILL.md frontmatter",
        "counts": {
            "skill": counts["skill"],
            "workflow": counts["workflow"],
            "meta-skill": counts["meta-skill"],
            "total": len(items),
        },
        "items": ordered_items,
    }


def expected_snapshot_text(inventory: dict[str, object]) -> str:
    return json.dumps(inventory, indent=2, ensure_ascii=False) + "\n"


def validate_snapshot(inventory: dict[str, object]) -> None:
    if not SNAPSHOT_PATH.is_file():
        raise InventoryError(
            f"{SNAPSHOT_PATH.relative_to(ROOT)} is missing; regenerate it from metadata"
        )
    expected = expected_snapshot_text(inventory)
    actual = SNAPSHOT_PATH.read_text(encoding="utf-8")
    if actual != expected:
        raise InventoryError(
            f"{SNAPSHOT_PATH.relative_to(ROOT)} drifted from executable metadata; "
            "run scripts/verify-capability-inventory.py --write-snapshot"
        )


def validate_readme_counts(counts: dict[str, int]) -> None:
    text = README_PATH.read_text(encoding="utf-8")
    match = re.search(
        r"\*\*(\d+) skills · (\d+) workflows · (\d+) meta-skills\*\*", text
    )
    if not match:
        raise InventoryError("README.md: inventory summary was not found")
    actual = tuple(int(value) for value in match.groups())
    expected = (counts["skill"], counts["workflow"], counts["meta-skill"])
    if actual != expected:
        raise InventoryError(
            f"README.md inventory counts {actual} do not match metadata {expected}"
        )


def validate_taxonomy_counts(counts: dict[str, int]) -> None:
    text = TAXONOMY_PATH.read_text(encoding="utf-8")
    patterns = {
        "skill": r"^- `skill`: (\d+)$",
        "workflow": r"^- `workflow`: (\d+)$",
        "meta-skill": r"^- `meta-skill`: (\d+)$",
        "total": r"^- Total executable skills: (\d+)$",
    }
    for key, pattern in patterns.items():
        match = re.search(pattern, text, flags=re.MULTILINE)
        if not match:
            raise InventoryError(f"docs/skills.md: missing inventory count for {key}")
        actual = int(match.group(1))
        expected = counts[key]
        if actual != expected:
            raise InventoryError(
                f"docs/skills.md {key} count {actual} does not match metadata {expected}"
            )


def documented_workflows() -> set[str]:
    text = TAXONOMY_PATH.read_text(encoding="utf-8")
    section_match = re.search(
        r"^### Current workflows\s*$([\s\S]*?)(?=^### |^---\s*$)",
        text,
        flags=re.MULTILINE,
    )
    if not section_match:
        raise InventoryError("docs/skills.md: Current workflows section was not found")

    rows = re.findall(
        r"^\| `([^`]+)` \|", section_match.group(1), flags=re.MULTILINE
    )
    if not rows:
        raise InventoryError("docs/skills.md: Current workflows table has no capability rows")
    duplicates = sorted(name for name, count in Counter(rows).items() if count > 1)
    if duplicates:
        raise InventoryError(
            "docs/skills.md: duplicate workflow rows: " + ", ".join(duplicates)
        )
    return set(rows)


def validate_workflow_table(inventory: dict[str, object]) -> None:
    expected = {
        item["name"] for item in inventory["items"] if item["type"] == "workflow"
    }
    actual = documented_workflows()
    missing = sorted(expected - actual)
    extra = sorted(actual - expected)
    errors: list[str] = []
    if missing:
        errors.append("missing workflows: " + ", ".join(missing))
    if extra:
        errors.append("non-workflows or stale rows: " + ", ".join(extra))
    if errors:
        raise InventoryError(
            "docs/skills.md workflow table drifted: " + "; ".join(errors)
        )


def validate_documentation(inventory: dict[str, object]) -> None:
    counts = inventory["counts"]
    validate_readme_counts(counts)
    validate_taxonomy_counts(counts)
    validate_workflow_table(inventory)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write-snapshot",
        action="store_true",
        help="Regenerate docs/capability-inventory.json from SKILL.md metadata.",
    )
    parser.add_argument(
        "--skip-docs",
        action="store_true",
        help="Skip README and docs/skills.md drift validation.",
    )
    args = parser.parse_args()

    try:
        inventory = derive_inventory()
        if args.write_snapshot:
            SNAPSHOT_PATH.write_text(
                expected_snapshot_text(inventory), encoding="utf-8"
            )
        else:
            validate_snapshot(inventory)
        if not args.skip_docs:
            validate_documentation(inventory)
    except InventoryError as error:
        print(f"inventory error: {error}", file=sys.stderr)
        return 1

    counts = inventory["counts"]
    print(
        "Capability inventory verified: "
        f"{counts['skill']} skills, {counts['workflow']} workflows, "
        f"{counts['meta-skill']} meta-skills, {counts['total']} total."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
