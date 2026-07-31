"""Schema self-checks for auto-routing receipts (Slice 1 of Epic #304).

Verifies every schema under `schemas/auto-routing/` is a valid JSON-schema
draft-07 document.
"""
from __future__ import annotations

import unittest
from pathlib import Path

import jsonschema
import yaml

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_DIR = REPO_ROOT / "schemas" / "auto-routing"

EXPECTED_SCHEMAS = {
    "task-routing-plan": "TaskRoutingPlan",
    "orchestrator-action-receipt": "OrchestratorActionReceipt",
    "dispatch-receipt": "DispatchReceipt",
    "worker-receipt": "WorkerReceipt",
    "review-receipt": "ReviewReceipt",
    "synthesis-receipt": "SynthesisReceipt",
    "origin-return-receipt": "OriginReturnReceipt",
}


class AutoRoutingSchemaTests(unittest.TestCase):
    def test_schema_directory_exists(self) -> None:
        self.assertTrue(SCHEMA_DIR.is_dir(), f"missing {SCHEMA_DIR}")

    def test_all_expected_schemas_present(self) -> None:
        found = {p.stem.replace(".schema", "") for p in SCHEMA_DIR.glob("*.schema.yaml")}
        self.assertEqual(found, set(EXPECTED_SCHEMAS))

    def test_each_schema_self_validates(self) -> None:
        for stem, title in EXPECTED_SCHEMAS.items():
            with self.subTest(schema=stem):
                doc = yaml.safe_load((SCHEMA_DIR / f"{stem}.schema.yaml").read_text())
                self.assertEqual(doc.get("title"), title)
                self.assertEqual(doc.get("$schema"), "http://json-schema.org/draft-07/schema#")
                jsonschema.Draft7Validator.check_schema(doc)


if __name__ == "__main__":
    unittest.main()
