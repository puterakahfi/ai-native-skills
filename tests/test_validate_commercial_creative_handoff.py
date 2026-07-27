from __future__ import annotations

import copy
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "validate-commercial-creative-handoff.py"
SPEC = importlib.util.spec_from_file_location("validate_commercial_creative_handoff", MODULE_PATH)
assert SPEC and SPEC.loader
validator = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = validator
SPEC.loader.exec_module(validator)


def make_bundle() -> dict:
    return {
        "schema_version": 1,
        "evidence_class": "contract_fixture",
        "case_id": "CLAIM-LOCK-VALID",
        "authority": {
            "refs": ["authority://brief", "authority://brand", "authority://product"]
        },
        "authorized_content_ledger": {
            "ledger_id": "ACL-1",
            "authority_refs": ["authority://brief", "authority://brand", "authority://product"],
            "unknown_content_policy": "prohibit",
            "authorized_items": [
                {
                    "content_id": "TEXT-BRAND",
                    "kind": "rendered_text",
                    "value": "HMNS",
                    "authority_ref": "authority://brand",
                    "render_policy": "required",
                    "normalization": "exact",
                },
                {
                    "content_id": "TEXT-PRODUCT",
                    "kind": "rendered_text",
                    "value": "ORGSM",
                    "authority_ref": "authority://product",
                    "render_policy": "required",
                    "normalization": "exact",
                },
                {
                    "content_id": "SPEC-VOLUME",
                    "kind": "specification",
                    "value": "100 ml",
                    "authority_ref": "authority://product",
                    "render_policy": "allowed",
                    "normalization": "whitespace_only",
                },
                {
                    "content_id": "MARK-HMNS",
                    "kind": "brand_mark",
                    "value": "asset://hmns-logo",
                    "authority_ref": "authority://brand",
                    "render_policy": "allowed",
                    "normalization": "exact",
                },
            ],
            "prohibited_items": [
                {"kind": "factual_claim", "value": "Long Lasting", "reason": "not authorized"},
                {"kind": "brand_mark", "value": "crown", "reason": "not supplied"},
            ],
            "unresolved_items": [],
        },
        "provider_execution_handoff": {
            "handoff_id": "PEH-1",
            "locked_brief_ref": "brief://1",
            "authorized_content_ledger_ref": "ACL-1",
            "authorized_content_ids": ["TEXT-BRAND", "TEXT-PRODUCT", "SPEC-VOLUME", "MARK-HMNS"],
            "exact_rendered_text": [
                {"content_id": "TEXT-BRAND", "value": "HMNS"},
                {"content_id": "TEXT-PRODUCT", "value": "ORGSM"},
                {"content_id": "SPEC-VOLUME", "value": "100   ml"},
            ],
            "approved_mark_ids": ["MARK-HMNS"],
            "specific_product_required": True,
            "product_reference_refs": ["asset://source-product"],
            "preservation_locks": {
                "preserve_shape": True,
                "preserve_packaging": True,
                "preserve_logo": True,
                "preserve_label_text": True,
                "preserve_material": True,
                "preserve_product_color": True,
                "preserve_distinguishing_details": True,
            },
            "operation_or_design_plan_ref": "plan://1",
            "provider_specific_translation_owner": "prompt-engineer",
            "binary_execution_owner": "provider-adapter",
            "negative_constraints": [
                "no_additional_content",
                "no_inferred_claims",
                "preserve_product_truth",
            ],
            "comparison_required": {
                "authorized_content": True,
                "brand_fidelity": True,
                "product_fidelity": True,
                "content_accuracy": True,
            },
        },
        "provider_output_comparison": {
            "output_ref": "artifact://commercial.png",
            "ledger_ref": "ACL-1",
            "detected_content": [
                {"kind": "rendered_text", "value": "HMNS", "authorized_content_id": "TEXT-BRAND"},
                {"kind": "rendered_text", "value": "ORGSM", "authorized_content_id": "TEXT-PRODUCT"},
                {"kind": "specification", "value": "100 ml", "authorized_content_id": "SPEC-VOLUME"},
                {"kind": "brand_mark", "value": "asset://hmns-logo", "authorized_content_id": "MARK-HMNS"},
            ],
            "unmatched_content": [],
            "altered_authorized_content": [],
            "fidelity_gates": {"SV8": "PASS", "SV9": "PASS", "SV11": "PASS"},
            "result": "PASS",
        },
        "independent_review": {
            "reviewer": "design-review",
            "verdict": "PASS",
            "gates": {"SV8": "PASS", "SV9": "PASS", "SV11": "PASS"},
        },
        "decision": {
            "state": "ACCEPTED",
            "accepted": True,
            "delivered": False,
            "return_routes": [],
        },
    }


def make_blocked(bundle: dict, *, routes: list[str] | None = None) -> dict:
    bundle["provider_output_comparison"]["result"] = "FAIL"
    bundle["independent_review"]["verdict"] = "CRITICAL"
    bundle["independent_review"]["gates"]["SV11"] = "FAIL"
    bundle["decision"] = {
        "state": "COMPARISON_BLOCKED",
        "accepted": False,
        "delivered": False,
        "return_routes": routes or ["authority_owner+design-refinement"],
    }
    return bundle


class ClaimLockValidatorTests(unittest.TestCase):
    def test_valid_bundle_passes(self) -> None:
        report = validator.validate_bundle(make_bundle())
        self.assertEqual(report["contract_result"], "ACCEPTED_AS_REQUIRED")
        self.assertEqual(report["decision"]["violation_count"], 0)

    def test_unknown_content_policy_must_prohibit(self) -> None:
        bundle = make_bundle()
        bundle["authorized_content_ledger"]["unknown_content_policy"] = "allow"
        with self.assertRaisesRegex(validator.ValidationError, "must be prohibit"):
            validator.validate_bundle(bundle)

    def test_authorized_item_requires_declared_authority(self) -> None:
        bundle = make_bundle()
        bundle["authorized_content_ledger"]["authorized_items"][0]["authority_ref"] = "authority://missing"
        with self.assertRaisesRegex(validator.ValidationError, "must reference declared authority"):
            validator.validate_bundle(bundle)

    def test_handoff_must_reference_ledger(self) -> None:
        bundle = make_bundle()
        bundle["provider_execution_handoff"]["authorized_content_ledger_ref"] = "ACL-WRONG"
        with self.assertRaisesRegex(validator.ValidationError, "must match"):
            validator.validate_bundle(bundle)

    def test_required_text_must_be_in_handoff(self) -> None:
        bundle = make_bundle()
        bundle["provider_execution_handoff"]["exact_rendered_text"] = [
            {"content_id": "TEXT-BRAND", "value": "HMNS"}
        ]
        with self.assertRaisesRegex(validator.ValidationError, "must include required"):
            validator.validate_bundle(bundle)

    def test_specific_product_requires_source_reference(self) -> None:
        bundle = make_bundle()
        bundle["provider_execution_handoff"]["product_reference_refs"] = []
        with self.assertRaisesRegex(validator.ValidationError, "must not be empty"):
            validator.validate_bundle(bundle)

    def test_specific_product_requires_all_fidelity_locks(self) -> None:
        bundle = make_bundle()
        bundle["provider_execution_handoff"]["preservation_locks"]["preserve_label_text"] = False
        with self.assertRaisesRegex(validator.ValidationError, "missing true locks"):
            validator.validate_bundle(bundle)

    def test_handoff_requires_negative_constraints(self) -> None:
        bundle = make_bundle()
        bundle["provider_execution_handoff"]["negative_constraints"].remove("no_inferred_claims")
        with self.assertRaisesRegex(validator.ValidationError, "missing constraints"):
            validator.validate_bundle(bundle)

    def test_unsupported_claim_blocks_delivery(self) -> None:
        bundle = make_blocked(make_bundle())
        bundle["provider_output_comparison"]["detected_content"].append(
            {"kind": "factual_claim", "value": "Long Lasting", "authorized_content_id": None}
        )
        report = validator.validate_bundle(bundle)
        self.assertIn("factual_claim:Long Lasting", report["violations"]["unauthorized_content"])
        self.assertIn("factual_claim:Long Lasting", report["violations"]["prohibited_content"])

    def test_unsupported_specification_blocks_delivery(self) -> None:
        bundle = make_blocked(make_bundle())
        bundle["provider_output_comparison"]["detected_content"].append(
            {"kind": "specification", "value": "250 ml", "authorized_content_id": None}
        )
        report = validator.validate_bundle(bundle)
        self.assertIn("specification:250 ml", report["violations"]["unauthorized_content"])

    def test_unsupported_mark_blocks_delivery(self) -> None:
        bundle = make_blocked(make_bundle(), routes=["provider-adapter"])
        bundle["independent_review"]["gates"]["SV8"] = "FAIL"
        bundle["provider_output_comparison"]["detected_content"].append(
            {"kind": "brand_mark", "value": "crown", "authorized_content_id": None}
        )
        report = validator.validate_bundle(bundle)
        self.assertIn("brand_mark:crown", report["violations"]["prohibited_content"])

    def test_altered_authorized_text_blocks_delivery(self) -> None:
        bundle = make_blocked(make_bundle())
        bundle["provider_output_comparison"]["detected_content"][1]["value"] = "ORGASM"
        report = validator.validate_bundle(bundle)
        self.assertIn("TEXT-PRODUCT:value", report["violations"]["altered_authorized_content"])

    def test_missing_required_content_blocks_delivery(self) -> None:
        bundle = make_blocked(make_bundle())
        bundle["provider_output_comparison"]["detected_content"] = [
            item for item in bundle["provider_output_comparison"]["detected_content"]
            if item["authorized_content_id"] != "TEXT-PRODUCT"
        ]
        report = validator.validate_bundle(bundle)
        self.assertIn("TEXT-PRODUCT", report["violations"]["omitted_required_content"])

    def test_product_fidelity_failure_requires_product_image_route(self) -> None:
        bundle = make_blocked(
            make_bundle(),
            routes=["design-refinement+product-image-production"],
        )
        bundle["provider_output_comparison"]["fidelity_gates"]["SV9"] = "FAIL"
        bundle["independent_review"]["gates"]["SV9"] = "FAIL"
        report = validator.validate_bundle(bundle)
        self.assertIn("SV9", report["violations"]["hard_gate_failures"])

    def test_product_fidelity_failure_rejects_wrong_return_route(self) -> None:
        bundle = make_blocked(make_bundle(), routes=["provider-adapter"])
        bundle["provider_output_comparison"]["fidelity_gates"]["SV9"] = "FAIL"
        bundle["independent_review"]["gates"]["SV9"] = "FAIL"
        with self.assertRaisesRegex(validator.ValidationError, "requires design-refinement"):
            validator.validate_bundle(bundle)

    def test_producer_cannot_be_reviewer(self) -> None:
        bundle = make_bundle()
        bundle["independent_review"]["reviewer"] = "provider-adapter"
        with self.assertRaisesRegex(validator.ValidationError, "must differ"):
            validator.validate_bundle(bundle)

    def test_violations_cannot_be_accepted(self) -> None:
        bundle = make_bundle()
        bundle["provider_output_comparison"]["detected_content"].append(
            {"kind": "factual_claim", "value": "Premium Quality", "authorized_content_id": None}
        )
        with self.assertRaisesRegex(validator.ValidationError, "cannot PASS with violations"):
            validator.validate_bundle(bundle)

    def test_content_violation_requires_sv11_non_pass(self) -> None:
        bundle = make_blocked(make_bundle())
        bundle["independent_review"]["gates"]["SV11"] = "PASS"
        bundle["provider_output_comparison"]["detected_content"].append(
            {"kind": "factual_claim", "value": "Premium Quality", "authorized_content_id": None}
        )
        with self.assertRaisesRegex(validator.ValidationError, "SV11"):
            validator.validate_bundle(bundle)

    def test_review_gate_must_reflect_comparison_failure(self) -> None:
        bundle = make_blocked(
            make_bundle(),
            routes=["design-refinement+product-image-production"],
        )
        bundle["provider_output_comparison"]["fidelity_gates"]["SV9"] = "FAIL"
        bundle["independent_review"]["gates"]["SV9"] = "PASS"
        with self.assertRaisesRegex(validator.ValidationError, "must reflect the comparison FAIL"):
            validator.validate_bundle(bundle)

    def test_cli_writes_deterministic_report(self) -> None:
        bundle = make_bundle()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "bundle.json"
            report_path = root / "report.json"
            source.write_text(json.dumps(bundle), encoding="utf-8")
            exit_code = validator.main(["--input", str(source), "--report", str(report_path)])
            self.assertEqual(exit_code, 0)
            written = json.loads(report_path.read_text(encoding="utf-8"))
            self.assertEqual(written, validator.validate_bundle(bundle))


if __name__ == "__main__":
    unittest.main()
