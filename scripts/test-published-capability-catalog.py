#!/usr/bin/env python3
"""Network-independent regression harness for the Published Capability Catalog."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent / "build-published-capability-catalog.py"
REVISION = "a" * 40


def run(*args: str, expect_success: bool = True) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        check=False,
        capture_output=True,
        text=True,
    )
    if expect_success and result.returncode != 0:
        raise RuntimeError(f"command failed: {result.stdout}{result.stderr}")
    if not expect_success and result.returncode == 0:
        raise RuntimeError("expected command failure, but command succeeded")
    return result


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def base_inventory() -> dict:
    return {
        "schema_version": 1,
        "source": "skills/*/SKILL.md frontmatter",
        "counts": {"skill": 0, "workflow": 1, "meta-skill": 1, "total": 2},
        "items": [
            {
                "name": "new-feature-workflow",
                "type": "workflow",
                "path": "skills/new-feature-workflow/SKILL.md",
            },
            {
                "name": "systems-reasoning",
                "type": "meta-skill",
                "path": "skills/systems-reasoning/SKILL.md",
            },
        ],
    }


def seed(root: Path) -> None:
    write_json(root / "docs" / "capability-inventory.json", base_inventory())
    write_json(
        root / "catalog" / "capability-discovery" / "facets.json",
        {"schema_version": 2, "facets": {}},
    )
    write_json(
        root / "catalog" / "capability-discovery" / "classifications.json",
        {"schema_version": 2, "classification_groups": []},
    )
    write_json(
        root / "catalog" / "capability-discovery" / "topics.json",
        {"schema_version": 2, "topics": []},
    )
    write_json(
        root / "catalog" / "capability-discovery" / "job-profiles.json",
        {"schema_version": 2, "job_profiles": []},
    )


def expect_failure(root: Path, output: Path, expected: str) -> None:
    result = run(
        "--write",
        "--source-revision",
        REVISION,
        "--root",
        str(root),
        "--output",
        str(output),
        expect_success=False,
    )
    combined = result.stdout + result.stderr
    if expected not in combined:
        raise RuntimeError(f"expected failure containing {expected!r}; got:\n{combined}")


def main() -> int:
    workspace = Path(tempfile.mkdtemp(prefix="ai-native-published-catalog-test-"))
    try:
        root = workspace / "fixture"
        output = workspace / "capability-catalog.json"
        seed(root)

        run(
            "--write",
            "--source-revision",
            REVISION,
            "--root",
            str(root),
            "--output",
            str(output),
        )
        first = output.read_bytes()
        run("--check", "--root", str(root), "--output", str(output))
        run(
            "--write",
            "--source-revision",
            REVISION,
            "--root",
            str(root),
            "--output",
            str(output),
        )
        if output.read_bytes() != first:
            raise RuntimeError("repeated generation was not byte-identical")

        catalog = json.loads(output.read_text(encoding="utf-8"))
        if catalog["source"]["revision"] != REVISION:
            raise RuntimeError("exact revision provenance was not preserved")
        if catalog["inventory"]["counts"]["total"] != 2:
            raise RuntimeError("canonical counts were not preserved")

        inventory_path = root / "docs" / "capability-inventory.json"
        inventory = base_inventory()
        inventory["items"].append(dict(inventory["items"][0]))
        inventory["counts"]["workflow"] = 2
        inventory["counts"]["total"] = 3
        write_json(inventory_path, inventory)
        expect_failure(root, output, "duplicate capability identity")

        seed(root)
        inventory = base_inventory()
        inventory["counts"]["total"] = 3
        write_json(inventory_path, inventory)
        expect_failure(root, output, "inventory counts do not match items")

        seed(root)
        inventory = base_inventory()
        inventory["items"][0]["path"] = "skills/wrong/SKILL.md"
        write_json(inventory_path, inventory)
        expect_failure(root, output, "canonical path mismatch")

        seed(root)
        write_json(
            root / "catalog" / "capability-discovery" / "topics.json",
            {"schema_version": 3, "topics": []},
        )
        expect_failure(root, output, "topics schema_version must be 2")

        seed(root)
        invalid_revision = run(
            "--write",
            "--source-revision",
            "main",
            "--root",
            str(root),
            "--output",
            str(output),
            expect_success=False,
        )
        if "exact 40-character" not in invalid_revision.stderr:
            raise RuntimeError("mutable revision was not rejected")

        seed(root)
        run(
            "--write",
            "--source-revision",
            REVISION,
            "--root",
            str(root),
            "--output",
            str(output),
        )
        output.write_text("{}\n", encoding="utf-8")
        drift = run("--check", "--root", str(root), "--output", str(output), expect_success=False)
        if "source.revision is missing" not in drift.stderr:
            raise RuntimeError("malformed committed artifact was not rejected")

        print("Published Capability Catalog harness passed.")
        return 0
    finally:
        shutil.rmtree(workspace, ignore_errors=True)


if __name__ == "__main__":
    raise SystemExit(main())
