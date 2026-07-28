#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "build-published-capability-catalog.py"
spec = importlib.util.spec_from_file_location("published_catalog", MODULE_PATH)
assert spec and spec.loader
catalog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(catalog)

REVISION = "a" * 40


def inventory(items: list[dict]) -> dict:
    return {
        "schema_version": 1,
        "counts": {
            "skill": sum(item["type"] == "skill" for item in items),
            "workflow": sum(item["type"] == "workflow" for item in items),
            "meta-skill": sum(item["type"] == "meta-skill" for item in items),
            "total": len(items),
        },
        "items": items,
    }


class PublishedCatalogTest(unittest.TestCase):
    def write_sources(self, root: Path, inv: dict, discovery: dict | None = None) -> dict[str, Path]:
        discovery = discovery or {"schema_version": 2}
        files = {}
        payloads = {
            "inventory": inv,
            "facets": discovery,
            "classifications": discovery,
            "topics": discovery,
            "job_profiles": discovery,
        }
        for name, payload in payloads.items():
            path = root / f"{name}.json"
            path.write_text(json.dumps(payload), encoding="utf-8")
            files[name] = path
        return files

    def test_build_is_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            items = [{"name": "alpha", "type": "skill", "path": "skills/alpha/SKILL.md"}]
            files = self.write_sources(root, inventory(items))
            first = catalog.render(catalog.build_catalog(REVISION, files))
            second = catalog.render(catalog.build_catalog(REVISION, files))
            self.assertEqual(first, second)

    def test_duplicate_identity_fails_closed(self) -> None:
        items = [
            {"name": "alpha", "type": "skill", "path": "skills/alpha/SKILL.md"},
            {"name": "alpha", "type": "skill", "path": "skills/alpha/SKILL.md"},
        ]
        with self.assertRaisesRegex(catalog.CatalogError, "duplicate capability identity"):
            catalog.validate_inventory(inventory(items))

    def test_unknown_type_fails_closed(self) -> None:
        items = [{"name": "alpha", "type": "plugin", "path": "skills/alpha/SKILL.md"}]
        with self.assertRaisesRegex(catalog.CatalogError, "unknown capability type"):
            catalog.validate_inventory(inventory(items))

    def test_broken_reference_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            items = [{"name": "alpha", "type": "skill", "path": "skills/alpha/SKILL.md"}]
            discovery = {"schema_version": 2, "capabilities": ["missing"]}
            files = self.write_sources(root, inventory(items), discovery)
            with self.assertRaisesRegex(catalog.CatalogError, "unknown capability reference"):
                catalog.build_catalog(REVISION, files)

    def test_addition_is_non_breaking(self) -> None:
        before = {"schema_version": 1, "inventory": {"capabilities": [{"name": "a", "type": "skill"}]}}
        after = {"schema_version": 1, "inventory": {"capabilities": [{"name": "a", "type": "skill"}, {"name": "b", "type": "workflow"}]}}
        changes = catalog.compatibility_changes(before, after)
        self.assertEqual(changes["breaking"], [])
        self.assertEqual(changes["additive"], ["capability added: b"])

    def test_removal_and_type_mutation_are_breaking(self) -> None:
        before = {"schema_version": 1, "inventory": {"capabilities": [{"name": "a", "type": "skill"}, {"name": "b", "type": "skill"}]}}
        after = {"schema_version": 1, "inventory": {"capabilities": [{"name": "a", "type": "workflow"}]}}
        changes = catalog.compatibility_changes(before, after)
        self.assertIn("capability removed: b", changes["breaking"])
        self.assertIn("capability type changed: a (skill -> workflow)", changes["breaking"])

    def test_malformed_revision_is_rejected(self) -> None:
        with self.assertRaisesRegex(catalog.CatalogError, "40-character"):
            catalog.validate_revision("main")


if __name__ == "__main__":
    unittest.main()
