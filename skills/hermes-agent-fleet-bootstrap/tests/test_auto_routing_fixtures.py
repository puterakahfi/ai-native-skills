"""Fixture validation for auto-routing receipts (Epic #304).

Positive fixtures MUST validate against every relevant schema. Negative fixtures
may be either schema-negative (invalid receipt shape) or behavior-negative
(schema-valid evidence for a blocked/not-verified outcome). The latter became
intentional after the #304 runtime acceptance slice: many failure scenarios are
valid receipts whose semantics are blocked.
"""
from __future__ import annotations

import unittest
from pathlib import Path

import jsonschema
import yaml

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_DIR = REPO_ROOT / "schemas" / "auto-routing"
FIXTURE_DIR = REPO_ROOT / "contracts" / "fixtures" / "auto-routing"


def _load(name: str) -> dict:
    return yaml.safe_load((SCHEMA_DIR / f"{name}.schema.yaml").read_text())


SCHEMAS = {
    "task-routing-plan": _load("task-routing-plan"),
    "orchestrator-action-receipt": _load("orchestrator-action-receipt"),
    "dispatch-receipt": _load("dispatch-receipt"),
    "worker-receipt": _load("worker-receipt"),
    "review-receipt": _load("review-receipt"),
    "synthesis-receipt": _load("synthesis-receipt"),
    "origin-return-receipt": _load("origin-return-receipt"),
}

SCALAR_MAP = {
    "plan": "task-routing-plan",
    "orchestrator_action_receipt": "orchestrator-action-receipt",
    "origin_return_receipt": "origin-return-receipt",
    "synthesis_receipt": "synthesis-receipt",
}
LIST_MAP = {
    "dispatch_receipts": "dispatch-receipt",
    "worker_receipts": "worker-receipt",
    "review_receipts": "review-receipt",
}


def _validation_errors(doc: dict) -> list[str]:
    errors: list[str] = []
    for key, schema_name in SCALAR_MAP.items():
        payload = doc.get(key)
        if payload is None:
            continue
        try:
            jsonschema.validate(payload, SCHEMAS[schema_name])
        except jsonschema.ValidationError as exc:
            errors.append(f"{key}: {exc.message}")
    for key, schema_name in LIST_MAP.items():
        for index, item in enumerate(doc.get(key) or []):
            try:
                jsonschema.validate(item, SCHEMAS[schema_name])
            except jsonschema.ValidationError as exc:
                errors.append(f"{key}[{index}]: {exc.message}")
    return errors


class AutoRoutingFixtureTests(unittest.TestCase):
    def test_fixture_directory_exists(self) -> None:
        self.assertTrue(FIXTURE_DIR.is_dir(), f"missing {FIXTURE_DIR}")

    def test_positive_fixtures_validate(self) -> None:
        positives = sorted(FIXTURE_DIR.glob("positive-*.yaml"))
        self.assertGreaterEqual(len(positives), 4, "expected at least 4 positive fixtures")
        for path in positives:
            with self.subTest(fixture=path.name):
                doc = yaml.safe_load(path.read_text())
                errors = _validation_errors(doc)
                self.assertEqual(errors, [], f"positive fixture rejected: {errors}")

    def test_negative_fixtures_are_rejected(self) -> None:
        negatives = sorted(FIXTURE_DIR.glob("negative-*.yaml"))
        self.assertGreaterEqual(len(negatives), 4, "expected at least 4 negative fixtures")
        for path in negatives:
            with self.subTest(fixture=path.name):
                doc = yaml.safe_load(path.read_text())
                errors = _validation_errors(doc)
                if errors:
                    continue
                expected = doc.get("expected_behavior") or {}
                blocked_statuses = {
                    "blocked",
                    "not_verified",
                    "needs_work",
                    "ready_with_limitations",
                }
                semantic_statuses = [
                    str(expected.get("verdict", "")).lower(),
                    str(expected.get("status", "")).lower(),
                    str(doc.get("planner_output", {}).get("status", "")).lower(),
                    *[
                        str(receipt.get("status", "")).lower()
                        for receipt in doc.get("dispatch_receipts", []) or []
                    ],
                ]
                self.assertTrue(
                    any(status in blocked_statuses for status in semantic_statuses)
                    or bool(doc.get("violation"))
                    or bool(doc.get("dispatch_notes", {}).get("blocking_reason"))
                    or bool(doc.get("synthesis_notes", {}).get("violation"))
                    or bool(doc.get("synthesis_violation"))
                    or bool(doc.get("schema_notes", {}).get("this_fixture_is_behavioral")),
                    "negative fixture must be schema-invalid or explicitly semantic-negative",
                )


if __name__ == "__main__":
    unittest.main()
