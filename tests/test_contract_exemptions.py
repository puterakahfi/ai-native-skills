from __future__ import annotations

import datetime as dt
import unittest
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "contract-exemption.schema.yaml"


class ContractExemptionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.schema = yaml.safe_load(SCHEMA.read_text())
        Draft202012Validator.check_schema(cls.schema)
        cls.validator = Draft202012Validator(cls.schema, format_checker=FormatChecker())
        cls.paths = sorted((ROOT / "skills").glob("*/contract.exemption.yaml"))

    def test_repository_exemptions_are_schema_valid(self):
        self.assertGreater(len(self.paths), 0)
        failures = {}
        for path in self.paths:
            payload = yaml.safe_load(path.read_text())
            errors = [error.message for error in self.validator.iter_errors(payload)]
            if errors:
                failures[path.relative_to(ROOT).as_posix()] = errors
        self.assertEqual({}, failures)

    def test_missing_review_date_is_rejected(self):
        payload = yaml.safe_load(self.paths[0].read_text())
        del payload["contract_exemption"]["review_date"]
        errors = list(self.validator.iter_errors(payload))
        self.assertTrue(any("review_date" in error.message for error in errors), errors)

    def test_exemptions_are_time_bounded(self):
        today = dt.datetime.now(dt.timezone.utc).date()
        overdue = []
        for path in self.paths:
            payload = yaml.safe_load(path.read_text())["contract_exemption"]
            review_date = dt.date.fromisoformat(payload["review_date"])
            if review_date < today:
                overdue.append(path.relative_to(ROOT).as_posix())
        self.assertEqual([], overdue)

    def test_exemption_and_declaration_do_not_coexist(self):
        collisions = [
            path.parent.relative_to(ROOT).as_posix()
            for path in self.paths
            if (path.parent / "adapter.conformance.yaml").exists()
        ]
        self.assertEqual([], collisions)

    def test_classification_scope_and_blocking_issue_are_consistent(self):
        failures = []
        for path in self.paths:
            exemption = yaml.safe_load(path.read_text())["contract_exemption"]
            classification = exemption["classification"]
            scope = set(exemption["scope"])
            blocking_issue = exemption["revisit"].get("blocking_issue")
            if classification == "core_gap":
                if "core_gap_tracking" not in scope or not blocking_issue:
                    failures.append(path.relative_to(ROOT).as_posix())
            elif classification == "provider_specific":
                if "provider_specific_execution" not in scope or blocking_issue:
                    failures.append(path.relative_to(ROOT).as_posix())
            elif classification == "third_party_delegation":
                if "third_party_delegation" not in scope or blocking_issue:
                    failures.append(path.relative_to(ROOT).as_posix())
        self.assertEqual([], failures)

    def test_retired_compatibility_records_are_absent(self):
        migration = yaml.safe_load(
            (ROOT / "docs" / "compatibility-registry-migration.yaml").read_text()
        )["compatibility_registry_migration"]
        remaining = [
            record["path"]
            for record in migration["retired_records"]
            if (ROOT / record["path"]).exists()
        ]
        self.assertEqual([], remaining)


if __name__ == "__main__":
    unittest.main()
