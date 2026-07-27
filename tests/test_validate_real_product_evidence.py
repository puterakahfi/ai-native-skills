from __future__ import annotations

import copy
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "validate-real-product-evidence.py"
SPEC = importlib.util.spec_from_file_location("validate_real_product_evidence", MODULE_PATH)
assert SPEC and SPEC.loader
validator = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = validator
SPEC.loader.exec_module(validator)


CATEGORIES = [
    "rigid_packaged_product",
    "reflective_or_translucent_product",
    "organic_irregular_soft_edge_product",
]


def digest(seed: int) -> str:
    return f"{seed:064x}"[-64:]


def make_case(index: int, category: str) -> dict:
    case_id = f"CASE-{index}"
    pam_ref = f"evidence://{case_id}/product-asset-master.png"
    catalog_ref = f"evidence://{case_id}/catalog.png"
    commercial_ref = f"evidence://{case_id}/commercial.png"
    return {
        "case_id": case_id,
        "product_category": category,
        "authorization": {
            "source_owner_or_license": "Fixture Owner / test-only license",
            "use_authorized": True,
            "provider_processing_authorized": True,
            "authority_refs": [f"evidence://{case_id}/authorization"],
        },
        "source": {
            "asset_ref": f"evidence://{case_id}/source.jpg",
            "sha256": digest(index * 10 + 1),
            "dimensions": [1200, 1200],
            "declared_product_identity": f"Test product {index}",
            "provenance_status": "PASS",
        },
        "operations": [
            {
                "operation": "background removal",
                "purpose": "prepare transparent product master",
                "authorization_ref": f"evidence://{case_id}/authorization",
                "preservation_impact": "source pixels preserved inside accepted mask",
                "evidence_refs": [f"evidence://{case_id}/operation-record"],
            }
        ],
        "provider_execution": {
            "adapter": "test-adapter",
            "run_ref": f"evidence://{case_id}/run",
            "executor": f"executor-{index}",
            "status": "PASS",
            "version_attribution": {"adapter": "1.0.0", "engine": "fixture"},
            "limitations": [],
        },
        "exports": [
            {
                "role": "product_asset_master",
                "artifact_ref": pam_ref,
                "sha256": digest(index * 10 + 2),
                "format": "PNG",
                "dimensions": [1600, 1600],
                "status": "PASS",
            },
            {
                "role": "catalog_output",
                "artifact_ref": catalog_ref,
                "sha256": digest(index * 10 + 3),
                "format": "PNG",
                "dimensions": [1600, 1600],
                "status": "PASS",
            },
            {
                "role": "commercial_output",
                "artifact_ref": commercial_ref,
                "sha256": digest(index * 10 + 4),
                "format": "PNG",
                "dimensions": [1080, 1350],
                "status": "PASS",
            },
        ],
        "product_fidelity_review": {
            "comparison_refs": [f"evidence://{case_id}/fidelity-comparison"],
            "lock_statuses": {
                "shape": "PASS",
                "packaging": "PASS",
                "logo": "PASS",
                "label_text": "PASS",
                "material": "PASS",
                "product_color": "PASS",
                "distinguishing_details": "PASS",
            },
            "status": "PASS",
            "findings": [],
        },
        "mask_edge_export_review": {
            "actual_size_refs": [f"evidence://{case_id}/actual-size"],
            "background_test_refs": [f"evidence://{case_id}/white", f"evidence://{case_id}/black"],
            "checks": {
                "transparent_png_integrity": "PASS",
                "no_canvas_clipping": "PASS",
                "no_halo_or_fringe": "PASS",
                "no_residue": "PASS",
                "crop_and_padding": "PASS",
                "effective_resolution": "PASS",
                "export_integrity": "PASS",
            },
            "status": "PASS",
            "findings": [],
        },
        "downstream_handoff": {
            "product_asset_master_ref": pam_ref,
            "catalog_output_ref": catalog_ref,
            "commercial_output_ref": commercial_ref,
            "status": "PASS",
        },
        "independent_review": {
            "reviewer": f"reviewer-{index}",
            "design_review_ref": f"evidence://{case_id}/design-review",
            "static_visual_gate_statuses": {
                "product_fidelity": "PASS",
                "alpha_edge_quality": "PASS",
                "destination_fit": "PASS",
            },
            "verdict": "PASS",
        },
        "limitations": [],
        "overall_status": "PASS",
    }


def make_bundle(*, evidence_class: str = "contract_fixture") -> dict:
    cases = [make_case(index + 1, category) for index, category in enumerate(CATEGORIES)]
    reuse_case = cases[0]
    return {
        "schema_version": 1,
        "epic": "puterakahfi/ai-native-skills#140",
        "validation_issue": "puterakahfi/ai-native-skills#145",
        "evidence_class": evidence_class,
        "production_readiness_claim": evidence_class == "real_product_acceptance",
        "cases": cases,
        "prepared_asset_reuse": {
            "case_ref": reuse_case["case_id"],
            "product_asset_master_ref": reuse_case["downstream_handoff"]["product_asset_master_ref"],
            "catalog_output_ref": reuse_case["downstream_handoff"]["catalog_output_ref"],
            "commercial_output_ref": reuse_case["downstream_handoff"]["commercial_output_ref"],
            "status": "PASS",
        },
        "acceptance_summary": {
            "source_authorization": "PASS",
            "provider_backed_execution": "PASS",
            "product_asset_master_acceptance": "PASS",
            "downstream_reuse": "PASS",
            "independent_visual_acceptance": "PASS",
            "real_product_acceptance": "PASS",
        },
    }


class RealProductEvidenceValidatorTest(unittest.TestCase):
    def test_complete_contract_fixture_passes_without_claiming_readiness(self):
        report = validator.build_report(make_bundle())
        self.assertEqual("PASS", report["hard_gate_result"])
        self.assertFalse(report["production_readiness_claim"])
        self.assertEqual(3, report["case_count"])
        self.assertEqual(sorted(CATEGORIES), report["category_coverage"])
        self.assertEqual("NOT_VERIFIED", report["validator_boundary"]["remote_binary_resolution"])

    def test_complete_real_acceptance_manifest_passes_contract_gate(self):
        report = validator.build_report(make_bundle(evidence_class="real_product_acceptance"))
        self.assertTrue(report["production_readiness_claim"])
        self.assertEqual("real_product_acceptance", report["evidence_class"])

    def test_missing_category_fails_closed(self):
        bundle = make_bundle()
        bundle["cases"] = bundle["cases"][:2]
        with self.assertRaisesRegex(validator.EvidenceValidationError, "missing required categories"):
            validator.build_report(bundle)

    def test_missing_provider_authorization_fails_closed(self):
        bundle = make_bundle()
        bundle["cases"][0]["authorization"]["provider_processing_authorized"] = False
        with self.assertRaisesRegex(validator.EvidenceValidationError, "provider_processing_authorized"):
            validator.build_report(bundle)

    def test_operation_authority_must_reference_declared_record(self):
        bundle = make_bundle()
        bundle["cases"][0]["operations"][0]["authorization_ref"] = "evidence://undeclared/authority"
        with self.assertRaisesRegex(validator.EvidenceValidationError, "declared authority record"):
            validator.build_report(bundle)

    def test_non_independent_reviewer_fails_closed(self):
        bundle = make_bundle()
        case = bundle["cases"][0]
        case["independent_review"]["reviewer"] = case["provider_execution"]["executor"]
        with self.assertRaisesRegex(validator.EvidenceValidationError, "must be independent"):
            validator.build_report(bundle)

    def test_failed_hard_gate_fails_closed(self):
        bundle = make_bundle()
        bundle["cases"][1]["mask_edge_export_review"]["checks"]["no_canvas_clipping"] = "FAIL"
        with self.assertRaisesRegex(validator.EvidenceValidationError, "no_canvas_clipping: must be PASS"):
            validator.build_report(bundle)

    def test_downstream_handoff_must_match_exports(self):
        bundle = make_bundle()
        bundle["cases"][2]["downstream_handoff"]["catalog_output_ref"] = "evidence://wrong/catalog.png"
        with self.assertRaisesRegex(validator.EvidenceValidationError, "must reference the matching export"):
            validator.build_report(bundle)

    def test_prepared_asset_reuse_must_match_selected_case_exports(self):
        bundle = make_bundle()
        bundle["prepared_asset_reuse"]["catalog_output_ref"] = bundle["cases"][1]["downstream_handoff"]["catalog_output_ref"]
        with self.assertRaisesRegex(validator.EvidenceValidationError, "selected case catalog output"):
            validator.build_report(bundle)

    def test_required_static_visual_gate_cannot_be_omitted(self):
        bundle = make_bundle()
        del bundle["cases"][0]["independent_review"]["static_visual_gate_statuses"]["destination_fit"]
        with self.assertRaisesRegex(validator.EvidenceValidationError, "missing gates: destination_fit"):
            validator.build_report(bundle)

    def test_contract_fixture_cannot_claim_production_readiness(self):
        bundle = make_bundle()
        bundle["production_readiness_claim"] = True
        with self.assertRaisesRegex(validator.EvidenceValidationError, "contract fixtures cannot claim"):
            validator.build_report(bundle)

    def test_real_acceptance_cannot_contain_not_verified_status(self):
        bundle = make_bundle(evidence_class="real_product_acceptance")
        bundle["cases"][0]["independent_review"]["verdict"] = "NOT_VERIFIED"
        with self.assertRaisesRegex(validator.EvidenceValidationError, "must be PASS"):
            validator.build_report(bundle)

    def test_cli_requires_explicit_contract_fixture_flag(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            bundle_path = root / "bundle.json"
            report_path = root / "report.json"
            bundle_path.write_text(json.dumps(make_bundle()), encoding="utf-8")
            self.assertEqual(1, validator.main(["--bundle", str(bundle_path)]))
            self.assertEqual(
                0,
                validator.main(
                    [
                        "--bundle",
                        str(bundle_path),
                        "--report",
                        str(report_path),
                        "--allow-contract-fixture",
                    ]
                ),
            )
            self.assertTrue(report_path.is_file())

    def test_cli_resolves_repository_relative_case_files(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            bundle = make_bundle()
            cases = bundle.pop("cases")
            case_dir = root / "cases"
            case_dir.mkdir()
            refs = []
            for index, case in enumerate(cases):
                ref = f"cases/case-{index + 1}.json"
                (root / ref).write_text(json.dumps(case), encoding="utf-8")
                refs.append(ref)
            bundle["case_files"] = refs
            bundle_path = root / "bundle.json"
            bundle_path.write_text(json.dumps(bundle), encoding="utf-8")
            loaded = validator.load_bundle(bundle_path)
            self.assertEqual(3, len(loaded["cases"]))
            self.assertEqual("PASS", validator.build_report(loaded)["hard_gate_result"])

    def test_case_file_parent_traversal_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            bundle = make_bundle()
            bundle.pop("cases")
            bundle["case_files"] = ["../outside.json"]
            bundle_path = root / "bundle.json"
            bundle_path.write_text(json.dumps(bundle), encoding="utf-8")
            with self.assertRaisesRegex(validator.EvidenceValidationError, "must not traverse"):
                validator.load_bundle(bundle_path)

    def test_compare_detects_receipt_drift(self):
        report = validator.build_report(make_bundle())
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "receipt.json"
            path.write_text(json.dumps(report), encoding="utf-8")
            validator.compare_report(path, report)
            drifted = copy.deepcopy(report)
            drifted["case_count"] = 99
            with self.assertRaisesRegex(validator.EvidenceValidationError, "does not match"):
                validator.compare_report(path, drifted)


if __name__ == "__main__":
    unittest.main()
