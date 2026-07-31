from __future__ import annotations

import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


PACKAGE = Path(__file__).resolve().parents[1]
RUNNER = PACKAGE / "scripts" / "hermes_fleet_runtime_acceptance.py"
FIXTURE = PACKAGE / "tests" / "fixtures" / "runtime-acceptance-pass-with-limitations.json"
SPEC = importlib.util.spec_from_file_location("hermes_fleet_runtime_acceptance", RUNNER)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class RuntimeAcceptanceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.evidence = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def evaluate(self, evidence=None):
        return MODULE.evaluate(copy.deepcopy(evidence or self.evidence))

    def test_sanitized_structural_evidence_passes_with_explicit_limitations(self) -> None:
        code, receipt = self.evaluate()
        self.assertEqual(code, MODULE.EXIT_OK)
        self.assertEqual(receipt["verdict"], "PASS_WITH_LIMITATIONS")
        self.assertFalse(receipt["telegram_live_verified"])
        self.assertFalse(receipt["model_driven_workers_verified"])
        self.assertIn("live_telegram_round_trip_not_verified", receipt["limitations"])
        self.assertIn(
            "provider_backed_specialist_execution_not_verified",
            receipt["limitations"],
        )
        self.assertFalse(receipt["credentials_exposed"])

    def test_full_live_evidence_can_reach_pass(self) -> None:
        evidence = copy.deepcopy(self.evidence)
        evidence["review_independence"] = {
            "status": "VERIFIED_SEPARATE_RUNTIME",
            "limitations": [],
        }
        evidence["telegram"] = {
            "evidence_level": "LIVE",
            "configured_profile": "agent-orchestrator",
            "gateway_started": True,
            "message_received": True,
            "response_returned": True,
            "credential_values_redacted": True,
            "legacy_gateway_running": False,
        }
        evidence["model_driven_workers"] = {
            "evidence_level": "LIVE",
            "specialist_execution_observed": True,
            "worker_profiles": ["agent-backend", "agent-review"],
        }
        code, receipt = self.evaluate(evidence)
        self.assertEqual(code, MODULE.EXIT_OK)
        self.assertEqual(receipt["verdict"], "PASS")

    def test_raw_telegram_token_is_rejected(self) -> None:
        evidence = copy.deepcopy(self.evidence)
        evidence["telegram"]["token"] = "123456789:abcdefghijklmnopqrstuvwxyzABCDE"
        with self.assertRaisesRegex(MODULE.AcceptanceError, "secret material"):
            self.evaluate(evidence)

    def test_legacy_gateway_running_fails(self) -> None:
        evidence = copy.deepcopy(self.evidence)
        evidence["telegram"]["legacy_gateway_running"] = True
        code, receipt = self.evaluate(evidence)
        self.assertEqual(code, MODULE.EXIT_NEEDS_WORK)
        self.assertEqual(receipt["verdict"], "NEEDS_WORK")
        self.assertIn("telegram_gateway_safety_failed", receipt["findings"])

    def test_profile_order_or_set_drift_fails(self) -> None:
        evidence = copy.deepcopy(self.evidence)
        evidence["profiles"][1], evidence["profiles"][2] = (
            evidence["profiles"][2],
            evidence["profiles"][1],
        )
        code, receipt = self.evaluate(evidence)
        self.assertEqual(code, MODULE.EXIT_NEEDS_WORK)
        self.assertIn("target_profile_set_or_order_mismatch", receipt["findings"])

    def test_planning_cannot_invoke_implementation_agents(self) -> None:
        evidence = copy.deepcopy(self.evidence)
        evidence["scenarios"][0]["selected_profiles"].append("agent-backend")
        code, receipt = self.evaluate(evidence)
        self.assertEqual(code, MODULE.EXIT_NEEDS_WORK)
        self.assertTrue(
            any(item.startswith("routing_contract_failed:planning-only") for item in receipt["findings"])
        )

    def test_backend_requires_agent_review(self) -> None:
        evidence = copy.deepcopy(self.evidence)
        evidence["scenarios"][1]["selected_profiles"] = ["agent-backend"]
        evidence["scenarios"][1]["review"] = {
            "required": False,
            "verdict": "NOT_RUN",
        }
        code, receipt = self.evaluate(evidence)
        self.assertEqual(code, MODULE.EXIT_NEEDS_WORK)
        self.assertIn("routing_contract_failed:backend-change", receipt["findings"])

    def test_ui_cannot_route_to_backend(self) -> None:
        evidence = copy.deepcopy(self.evidence)
        evidence["scenarios"][2]["selected_profiles"].append("agent-backend")
        code, receipt = self.evaluate(evidence)
        self.assertEqual(code, MODULE.EXIT_NEEDS_WORK)
        self.assertIn("routing_contract_failed:ui-change", receipt["findings"])

    def test_orchestrator_cannot_be_counted_as_specialist_worker(self) -> None:
        evidence = copy.deepcopy(self.evidence)
        evidence["scenarios"][1]["selected_profiles"].append("agent-orchestrator")
        code, receipt = self.evaluate(evidence)
        self.assertEqual(code, MODULE.EXIT_NEEDS_WORK)
        self.assertIn("orchestrator_counted_as_worker:backend-change", receipt["findings"])

    def test_all_specialists_cannot_be_invoked_without_need(self) -> None:
        evidence = copy.deepcopy(self.evidence)
        evidence["scenarios"][1]["selected_profiles"] = list(MODULE.SPECIALISTS)
        code, receipt = self.evaluate(evidence)
        self.assertEqual(code, MODULE.EXIT_NEEDS_WORK)
        self.assertIn("all_specialists_invoked:backend-change", receipt["findings"])

    def test_missing_worker_profile_fails_model_sync_and_structure(self) -> None:
        evidence = copy.deepcopy(self.evidence)
        evidence["profiles"].pop()
        evidence["model_sync"]["target_profiles"].pop()
        code, receipt = self.evaluate(evidence)
        self.assertEqual(code, MODULE.EXIT_NEEDS_WORK)
        self.assertIn("target_profile_set_or_order_mismatch", receipt["findings"])
        self.assertIn("model_sync_evidence_failed", receipt["findings"])

    def test_absent_review_independence_limit_is_rejected(self) -> None:
        evidence = copy.deepcopy(self.evidence)
        evidence["review_independence"] = {
            "status": "LIMITED_SHARED_RUNTIME",
            "limitations": [],
        }
        code, receipt = self.evaluate(evidence)
        self.assertEqual(code, MODULE.EXIT_NEEDS_WORK)
        self.assertIn("review_independence_not_honestly_disclosed", receipt["findings"])

    def test_cli_writes_machine_readable_receipt(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            receipt_path = Path(tmp) / "receipt.json"
            code = MODULE.main(
                [
                    "native-ai-engineering",
                    "--evidence",
                    str(FIXTURE),
                    "--receipt",
                    str(receipt_path),
                    "--json",
                ]
            )
            self.assertEqual(code, MODULE.EXIT_OK)
            receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
            self.assertEqual(receipt["verdict"], "PASS_WITH_LIMITATIONS")
            self.assertEqual(receipt["fleet_id"], "native-ai-engineering")


if __name__ == "__main__":
    unittest.main()
