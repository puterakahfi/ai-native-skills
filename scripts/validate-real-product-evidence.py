#!/usr/bin/env python3
"""Validate Product Image Production real-product evidence bundles.

This validator checks evidence completeness, cross-reference integrity, category
coverage, hard-gate status, downstream reuse, and independent-review separation.
It does not inspect remote binaries or replace human visual acceptance.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Iterable

SCHEMA_VERSION = 1
PASS = "PASS"
NOT_VERIFIED = "NOT_VERIFIED"
EVIDENCE_CLASSES = {"real_product_acceptance", "contract_fixture"}
REQUIRED_CATEGORIES = {
    "rigid_packaged_product",
    "reflective_or_translucent_product",
    "organic_irregular_soft_edge_product",
}
REQUIRED_FIDELITY_LOCKS = {
    "shape",
    "packaging",
    "logo",
    "label_text",
    "material",
    "product_color",
    "distinguishing_details",
}
REQUIRED_EXPORT_CHECKS = {
    "transparent_png_integrity",
    "no_canvas_clipping",
    "no_halo_or_fringe",
    "no_residue",
    "crop_and_padding",
    "effective_resolution",
    "export_integrity",
}
REQUIRED_EXPORT_ROLES = {
    "product_asset_master",
    "catalog_output",
    "commercial_output",
}
REQUIRED_STATIC_VISUAL_GATES = {
    "product_fidelity",
    "alpha_edge_quality",
    "destination_fit",
}
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


class EvidenceValidationError(RuntimeError):
    """Raised when an evidence bundle violates a hard contract."""


def require(condition: bool, path: str, message: str) -> None:
    if not condition:
        raise EvidenceValidationError(f"{path}: {message}")


def require_mapping(value: Any, path: str) -> dict[str, Any]:
    require(isinstance(value, dict), path, "must be an object")
    return value


def require_list(value: Any, path: str, *, non_empty: bool = False) -> list[Any]:
    require(isinstance(value, list), path, "must be an array")
    if non_empty:
        require(bool(value), path, "must not be empty")
    return value


def require_text(value: Any, path: str) -> str:
    require(isinstance(value, str) and bool(value.strip()), path, "must be a non-empty string")
    return value.strip()


def require_status(value: Any, path: str, expected: str = PASS) -> str:
    actual = require_text(value, path)
    require(actual == expected, path, f"must be {expected}, got {actual}")
    return actual


def require_sha256(value: Any, path: str) -> str:
    digest = require_text(value, path).lower()
    require(bool(SHA256_RE.fullmatch(digest)), path, "must be a lowercase 64-character SHA-256")
    return digest


def require_dimensions(value: Any, path: str) -> list[int]:
    dimensions = require_list(value, path)
    require(len(dimensions) == 2, path, "must contain [width, height]")
    require(
        all(isinstance(item, int) and item > 0 for item in dimensions),
        path,
        "width and height must be positive integers",
    )
    return dimensions


def require_refs(value: Any, path: str) -> list[str]:
    refs = require_list(value, path, non_empty=True)
    normalized: list[str] = []
    for index, ref in enumerate(refs):
        normalized.append(require_text(ref, f"{path}[{index}]"))
    require(len(normalized) == len(set(normalized)), path, "must not contain duplicate references")
    return normalized


def validate_authorization(case: dict[str, Any], path: str) -> set[str]:
    authorization = require_mapping(case.get("authorization"), f"{path}.authorization")
    require_text(authorization.get("source_owner_or_license"), f"{path}.authorization.source_owner_or_license")
    require(authorization.get("use_authorized") is True, f"{path}.authorization.use_authorized", "must be true")
    require(
        authorization.get("provider_processing_authorized") is True,
        f"{path}.authorization.provider_processing_authorized",
        "must be true",
    )
    return set(require_refs(authorization.get("authority_refs"), f"{path}.authorization.authority_refs"))


def validate_source(case: dict[str, Any], path: str) -> None:
    source = require_mapping(case.get("source"), f"{path}.source")
    require_text(source.get("asset_ref"), f"{path}.source.asset_ref")
    require_sha256(source.get("sha256"), f"{path}.source.sha256")
    require_dimensions(source.get("dimensions"), f"{path}.source.dimensions")
    require_text(source.get("declared_product_identity"), f"{path}.source.declared_product_identity")
    require_status(source.get("provenance_status"), f"{path}.source.provenance_status")


def validate_operations(case: dict[str, Any], path: str, authority_refs: set[str]) -> None:
    operations = require_list(case.get("operations"), f"{path}.operations", non_empty=True)
    for index, raw_operation in enumerate(operations):
        operation_path = f"{path}.operations[{index}]"
        operation = require_mapping(raw_operation, operation_path)
        require_text(operation.get("operation"), f"{operation_path}.operation")
        require_text(operation.get("purpose"), f"{operation_path}.purpose")
        authorization_ref = require_text(operation.get("authorization_ref"), f"{operation_path}.authorization_ref")
        require(
            authorization_ref in authority_refs,
            f"{operation_path}.authorization_ref",
            "must reference a declared authority record",
        )
        require_text(operation.get("preservation_impact"), f"{operation_path}.preservation_impact")
        require_refs(operation.get("evidence_refs"), f"{operation_path}.evidence_refs")


def validate_provider_execution(case: dict[str, Any], path: str) -> str:
    execution = require_mapping(case.get("provider_execution"), f"{path}.provider_execution")
    require_text(execution.get("adapter"), f"{path}.provider_execution.adapter")
    require_text(execution.get("run_ref"), f"{path}.provider_execution.run_ref")
    executor = require_text(execution.get("executor"), f"{path}.provider_execution.executor")
    require_status(execution.get("status"), f"{path}.provider_execution.status")
    attribution = require_mapping(
        execution.get("version_attribution"), f"{path}.provider_execution.version_attribution"
    )
    require(bool(attribution), f"{path}.provider_execution.version_attribution", "must not be empty")
    for key, value in attribution.items():
        require_text(key, f"{path}.provider_execution.version_attribution key")
        require_text(value, f"{path}.provider_execution.version_attribution.{key}")
    require_list(execution.get("limitations", []), f"{path}.provider_execution.limitations")
    return executor


def validate_exports(case: dict[str, Any], path: str) -> dict[str, str]:
    exports = require_list(case.get("exports"), f"{path}.exports", non_empty=True)
    by_role: dict[str, str] = {}
    seen_hashes: set[str] = set()
    for index, raw_export in enumerate(exports):
        export_path = f"{path}.exports[{index}]"
        export = require_mapping(raw_export, export_path)
        role = require_text(export.get("role"), f"{export_path}.role")
        require(role not in by_role, f"{export_path}.role", f"duplicate export role {role}")
        artifact_ref = require_text(export.get("artifact_ref"), f"{export_path}.artifact_ref")
        digest = require_sha256(export.get("sha256"), f"{export_path}.sha256")
        require(digest not in seen_hashes, f"{export_path}.sha256", "must identify a distinct artifact")
        seen_hashes.add(digest)
        require_text(export.get("format"), f"{export_path}.format")
        require_dimensions(export.get("dimensions"), f"{export_path}.dimensions")
        require_status(export.get("status"), f"{export_path}.status")
        by_role[role] = artifact_ref
    missing_roles = sorted(REQUIRED_EXPORT_ROLES - set(by_role))
    require(not missing_roles, f"{path}.exports", f"missing required roles: {', '.join(missing_roles)}")
    return by_role


def validate_fidelity_review(case: dict[str, Any], path: str) -> None:
    review = require_mapping(case.get("product_fidelity_review"), f"{path}.product_fidelity_review")
    require_refs(review.get("comparison_refs"), f"{path}.product_fidelity_review.comparison_refs")
    lock_statuses = require_mapping(
        review.get("lock_statuses"), f"{path}.product_fidelity_review.lock_statuses"
    )
    missing_locks = sorted(REQUIRED_FIDELITY_LOCKS - set(lock_statuses))
    require(not missing_locks, f"{path}.product_fidelity_review.lock_statuses", f"missing locks: {', '.join(missing_locks)}")
    for lock in sorted(REQUIRED_FIDELITY_LOCKS):
        require_status(lock_statuses.get(lock), f"{path}.product_fidelity_review.lock_statuses.{lock}")
    require_status(review.get("status"), f"{path}.product_fidelity_review.status")
    require_list(review.get("findings", []), f"{path}.product_fidelity_review.findings")


def validate_mask_edge_export_review(case: dict[str, Any], path: str) -> None:
    review = require_mapping(case.get("mask_edge_export_review"), f"{path}.mask_edge_export_review")
    require_refs(review.get("actual_size_refs"), f"{path}.mask_edge_export_review.actual_size_refs")
    require_refs(review.get("background_test_refs"), f"{path}.mask_edge_export_review.background_test_refs")
    checks = require_mapping(review.get("checks"), f"{path}.mask_edge_export_review.checks")
    missing_checks = sorted(REQUIRED_EXPORT_CHECKS - set(checks))
    require(not missing_checks, f"{path}.mask_edge_export_review.checks", f"missing checks: {', '.join(missing_checks)}")
    for check in sorted(REQUIRED_EXPORT_CHECKS):
        require_status(checks.get(check), f"{path}.mask_edge_export_review.checks.{check}")
    require_status(review.get("status"), f"{path}.mask_edge_export_review.status")
    require_list(review.get("findings", []), f"{path}.mask_edge_export_review.findings")


def validate_downstream_handoff(case: dict[str, Any], path: str, exports: dict[str, str]) -> None:
    handoff = require_mapping(case.get("downstream_handoff"), f"{path}.downstream_handoff")
    expected = {
        "product_asset_master_ref": exports["product_asset_master"],
        "catalog_output_ref": exports["catalog_output"],
        "commercial_output_ref": exports["commercial_output"],
    }
    for field, export_ref in expected.items():
        actual = require_text(handoff.get(field), f"{path}.downstream_handoff.{field}")
        require(actual == export_ref, f"{path}.downstream_handoff.{field}", "must reference the matching export")
    require_status(handoff.get("status"), f"{path}.downstream_handoff.status")


def validate_independent_review(case: dict[str, Any], path: str, executor: str) -> None:
    review = require_mapping(case.get("independent_review"), f"{path}.independent_review")
    reviewer = require_text(review.get("reviewer"), f"{path}.independent_review.reviewer")
    require(reviewer != executor, f"{path}.independent_review.reviewer", "must be independent from provider executor")
    require_text(review.get("design_review_ref"), f"{path}.independent_review.design_review_ref")
    gates = require_mapping(
        review.get("static_visual_gate_statuses"), f"{path}.independent_review.static_visual_gate_statuses"
    )
    require(bool(gates), f"{path}.independent_review.static_visual_gate_statuses", "must not be empty")
    missing_gates = sorted(REQUIRED_STATIC_VISUAL_GATES - set(gates))
    require(
        not missing_gates,
        f"{path}.independent_review.static_visual_gate_statuses",
        f"missing gates: {', '.join(missing_gates)}",
    )
    for gate, status in gates.items():
        require_text(gate, f"{path}.independent_review.static_visual_gate_statuses key")
        require_status(status, f"{path}.independent_review.static_visual_gate_statuses.{gate}")
    require_status(review.get("verdict"), f"{path}.independent_review.verdict")


def validate_case(raw_case: Any, index: int) -> dict[str, Any]:
    path = f"cases[{index}]"
    case = require_mapping(raw_case, path)
    case_id = require_text(case.get("case_id"), f"{path}.case_id")
    category = require_text(case.get("product_category"), f"{path}.product_category")
    require(category in REQUIRED_CATEGORIES, f"{path}.product_category", f"unsupported category {category}")
    authority_refs = validate_authorization(case, path)
    validate_source(case, path)
    validate_operations(case, path, authority_refs)
    executor = validate_provider_execution(case, path)
    exports = validate_exports(case, path)
    validate_fidelity_review(case, path)
    validate_mask_edge_export_review(case, path)
    validate_downstream_handoff(case, path, exports)
    validate_independent_review(case, path, executor)
    require_list(case.get("limitations", []), f"{path}.limitations")
    require_status(case.get("overall_status"), f"{path}.overall_status")
    return {
        "case_id": case_id,
        "product_category": category,
        "status": PASS,
        "exports": exports,
    }


def validate_reuse(
    bundle: dict[str, Any], case_exports: dict[str, dict[str, str]]
) -> dict[str, str]:
    reuse = require_mapping(bundle.get("prepared_asset_reuse"), "prepared_asset_reuse")
    case_ref = require_text(reuse.get("case_ref"), "prepared_asset_reuse.case_ref")
    require(case_ref in case_exports, "prepared_asset_reuse.case_ref", "must reference a validated case")
    pam_ref = require_text(reuse.get("product_asset_master_ref"), "prepared_asset_reuse.product_asset_master_ref")
    catalog_ref = require_text(reuse.get("catalog_output_ref"), "prepared_asset_reuse.catalog_output_ref")
    commercial_ref = require_text(reuse.get("commercial_output_ref"), "prepared_asset_reuse.commercial_output_ref")
    require(len({pam_ref, catalog_ref, commercial_ref}) == 3, "prepared_asset_reuse", "must reference three distinct artifacts")
    expected = case_exports[case_ref]
    require(
        pam_ref == expected["product_asset_master"],
        "prepared_asset_reuse.product_asset_master_ref",
        "must reference the selected case Product Asset Master",
    )
    require(
        catalog_ref == expected["catalog_output"],
        "prepared_asset_reuse.catalog_output_ref",
        "must reference the selected case catalog output",
    )
    require(
        commercial_ref == expected["commercial_output"],
        "prepared_asset_reuse.commercial_output_ref",
        "must reference the selected case commercial output",
    )
    require_status(reuse.get("status"), "prepared_asset_reuse.status")
    return {
        "case_ref": case_ref,
        "product_asset_master_ref": pam_ref,
        "catalog_output_ref": catalog_ref,
        "commercial_output_ref": commercial_ref,
    }


def walk_statuses(value: Any, path: str = "bundle") -> Iterable[tuple[str, str]]:
    if isinstance(value, dict):
        for key, item in value.items():
            child = f"{path}.{key}"
            if key in {"status", "verdict", "overall_status", "provenance_status"} and isinstance(item, str):
                yield child, item
            yield from walk_statuses(item, child)
    elif isinstance(value, list):
        for index, item in enumerate(value):
            yield from walk_statuses(item, f"{path}[{index}]")


def build_report(bundle: dict[str, Any]) -> dict[str, Any]:
    require(bundle.get("schema_version") == SCHEMA_VERSION, "schema_version", f"must be {SCHEMA_VERSION}")
    evidence_class = require_text(bundle.get("evidence_class"), "evidence_class")
    require(evidence_class in EVIDENCE_CLASSES, "evidence_class", f"must be one of {sorted(EVIDENCE_CLASSES)}")
    require_text(bundle.get("epic"), "epic")
    require_text(bundle.get("validation_issue"), "validation_issue")

    cases = require_list(bundle.get("cases"), "cases", non_empty=True)
    validated_cases = [validate_case(case, index) for index, case in enumerate(cases)]
    case_ids = [case["case_id"] for case in validated_cases]
    require(len(case_ids) == len(set(case_ids)), "cases", "case_id values must be unique")

    categories = {case["product_category"] for case in validated_cases}
    missing_categories = sorted(REQUIRED_CATEGORIES - categories)
    require(not missing_categories, "cases", f"missing required categories: {', '.join(missing_categories)}")

    case_exports = {case["case_id"]: case["exports"] for case in validated_cases}
    reuse = validate_reuse(bundle, case_exports)
    summary = require_mapping(bundle.get("acceptance_summary"), "acceptance_summary")
    require_status(summary.get("source_authorization"), "acceptance_summary.source_authorization")
    require_status(summary.get("provider_backed_execution"), "acceptance_summary.provider_backed_execution")
    require_status(summary.get("product_asset_master_acceptance"), "acceptance_summary.product_asset_master_acceptance")
    require_status(summary.get("downstream_reuse"), "acceptance_summary.downstream_reuse")
    require_status(summary.get("independent_visual_acceptance"), "acceptance_summary.independent_visual_acceptance")
    require_status(summary.get("real_product_acceptance"), "acceptance_summary.real_product_acceptance")

    production_claim = bundle.get("production_readiness_claim")
    require(isinstance(production_claim, bool), "production_readiness_claim", "must be boolean")

    if evidence_class == "contract_fixture":
        require(production_claim is False, "production_readiness_claim", "contract fixtures cannot claim production readiness")
    else:
        require(production_claim is True, "production_readiness_claim", "real acceptance bundles must explicitly claim readiness")
        non_pass_statuses = [(path, status) for path, status in walk_statuses(bundle) if status != PASS]
        require(not non_pass_statuses, "bundle", f"contains non-PASS statuses: {non_pass_statuses[:5]}")

    return {
        "schema_version": SCHEMA_VERSION,
        "evidence_class": evidence_class,
        "validation_issue": bundle["validation_issue"],
        "case_count": len(validated_cases),
        "category_coverage": sorted(categories),
        "case_results": validated_cases,
        "prepared_asset_reuse": reuse,
        "hard_gate_result": PASS,
        "production_readiness_claim": production_claim,
        "validator_boundary": {
            "remote_binary_resolution": NOT_VERIFIED,
            "semantic_visual_quality": NOT_VERIFIED,
            "human_review_authenticity": NOT_VERIFIED,
        },
    }


def load_json(path: Path) -> dict[str, Any]:
    try:
        document = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise EvidenceValidationError(f"{path}: file not found") from exc
    except json.JSONDecodeError as exc:
        raise EvidenceValidationError(f"{path}: invalid JSON at line {exc.lineno}, column {exc.colno}") from exc
    return require_mapping(document, str(path))


def load_bundle(path: Path) -> dict[str, Any]:
    bundle = load_json(path)
    if "case_files" not in bundle:
        return bundle

    case_files = require_list(bundle.get("case_files"), "case_files", non_empty=True)
    require("cases" not in bundle, "bundle", "must use either cases or case_files, not both")
    resolved_cases: list[dict[str, Any]] = []
    for index, raw_ref in enumerate(case_files):
        ref = require_text(raw_ref, f"case_files[{index}]")
        relative = Path(ref)
        require(not relative.is_absolute(), f"case_files[{index}]", "must be repository-relative")
        require(".." not in relative.parts, f"case_files[{index}]", "must not traverse parent directories")
        resolved_cases.append(load_json(path.parent / relative))
    bundle["cases"] = resolved_cases
    return bundle


def write_report(path: Path, report: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def compare_report(path: Path, report: dict[str, Any]) -> None:
    expected = load_json(path)
    require(expected == report, str(path), "does not match deterministic validator output")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle", type=Path, required=True, help="Evidence bundle JSON")
    parser.add_argument("--report", type=Path, help="Write deterministic validation report")
    parser.add_argument("--compare", type=Path, help="Compare report against an immutable receipt")
    parser.add_argument(
        "--allow-contract-fixture",
        action="store_true",
        help="Allow evidence_class=contract_fixture for repository tests only",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    try:
        bundle = load_bundle(args.bundle)
        if bundle.get("evidence_class") == "contract_fixture" and not args.allow_contract_fixture:
            raise EvidenceValidationError(
                "evidence_class: contract_fixture requires --allow-contract-fixture and cannot prove acceptance"
            )
        report = build_report(bundle)
        if args.report:
            write_report(args.report, report)
        if args.compare:
            compare_report(args.compare, report)
    except EvidenceValidationError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1

    print(
        f"PASS: {report['case_count']} cases, "
        f"{len(report['category_coverage'])} categories, "
        f"evidence_class={report['evidence_class']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
