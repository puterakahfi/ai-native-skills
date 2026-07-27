#!/usr/bin/env python3
"""Validate commercial creative claim-lock and provider fidelity handoffs.

The validator checks contract completeness and decision consistency. It does not
perform OCR, inspect binary pixels, authenticate reviewers, or replace independent
visual review. Observed content and gate results must be supplied as evidence.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Iterable

SCHEMA_VERSION = 1
PASS = "PASS"
SUPPORTED_EVIDENCE_CLASSES = {"provider_handoff_acceptance", "contract_fixture"}
SUPPORTED_KINDS = {
    "rendered_text",
    "factual_claim",
    "specification",
    "price",
    "contact",
    "legal_text",
    "brand_mark",
}
RENDER_POLICIES = {"required", "allowed", "metadata_only"}
NORMALIZATIONS = {"exact", "whitespace_only", "case_insensitive"}
REQUIRED_FIDELITY_LOCKS = {
    "preserve_shape",
    "preserve_packaging",
    "preserve_logo",
    "preserve_label_text",
    "preserve_material",
    "preserve_product_color",
    "preserve_distinguishing_details",
}
REQUIRED_NEGATIVE_CONSTRAINTS = {
    "no_additional_content",
    "no_inferred_claims",
    "preserve_product_truth",
}
HARD_GATES = {"SV8", "SV9", "SV11"}
BLOCKING_STATES = {
    "INTAKE_BLOCKED",
    "ASSET_BLOCKED",
    "COMPARISON_BLOCKED",
    "REVIEW_BLOCKED",
    "BLOCKED",
    "NOT_VERIFIED",
}
ACCEPTING_STATES = {"ACCEPTED", "DELIVERED"}


class ValidationError(RuntimeError):
    """Raised when a handoff bundle violates the contract."""


def require(condition: bool, path: str, message: str) -> None:
    if not condition:
        raise ValidationError(f"{path}: {message}")


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


def normalize(value: str, mode: str) -> str:
    if mode == "exact":
        return value
    if mode == "whitespace_only":
        return " ".join(value.split())
    if mode == "case_insensitive":
        return value.casefold()
    raise ValidationError(f"normalization: unsupported mode {mode}")


def require_unique(values: Iterable[str], path: str) -> None:
    items = list(values)
    require(len(items) == len(set(items)), path, "must contain unique values")


def validate_authority(payload: dict[str, Any]) -> set[str]:
    authority = require_mapping(payload.get("authority"), "authority")
    refs = [require_text(item, f"authority.refs[{index}]") for index, item in enumerate(
        require_list(authority.get("refs"), "authority.refs", non_empty=True)
    )]
    require_unique(refs, "authority.refs")
    return set(refs)


def validate_ledger(payload: dict[str, Any], authority_refs: set[str]) -> tuple[dict[str, dict[str, Any]], list[dict[str, Any]]]:
    ledger = require_mapping(payload.get("authorized_content_ledger"), "authorized_content_ledger")
    require_text(ledger.get("ledger_id"), "authorized_content_ledger.ledger_id")
    require(
        ledger.get("unknown_content_policy") == "prohibit",
        "authorized_content_ledger.unknown_content_policy",
        "must be prohibit",
    )

    declared_refs = [require_text(item, f"authorized_content_ledger.authority_refs[{index}]") for index, item in enumerate(
        require_list(ledger.get("authority_refs"), "authorized_content_ledger.authority_refs", non_empty=True)
    )]
    require(set(declared_refs).issubset(authority_refs), "authorized_content_ledger.authority_refs", "must reference declared authority")

    items = require_list(ledger.get("authorized_items"), "authorized_content_ledger.authorized_items", non_empty=True)
    by_id: dict[str, dict[str, Any]] = {}
    for index, raw in enumerate(items):
        path = f"authorized_content_ledger.authorized_items[{index}]"
        item = require_mapping(raw, path)
        content_id = require_text(item.get("content_id"), f"{path}.content_id")
        require(content_id not in by_id, f"{path}.content_id", "must be unique")
        kind = require_text(item.get("kind"), f"{path}.kind")
        require(kind in SUPPORTED_KINDS, f"{path}.kind", f"must be one of {sorted(SUPPORTED_KINDS)}")
        value = require_text(item.get("value"), f"{path}.value")
        authority_ref = require_text(item.get("authority_ref"), f"{path}.authority_ref")
        require(authority_ref in authority_refs, f"{path}.authority_ref", "must reference declared authority")
        render_policy = require_text(item.get("render_policy"), f"{path}.render_policy")
        require(render_policy in RENDER_POLICIES, f"{path}.render_policy", f"must be one of {sorted(RENDER_POLICIES)}")
        normalization_mode = require_text(item.get("normalization", "exact"), f"{path}.normalization")
        require(normalization_mode in NORMALIZATIONS, f"{path}.normalization", f"must be one of {sorted(NORMALIZATIONS)}")
        by_id[content_id] = {
            "content_id": content_id,
            "kind": kind,
            "value": value,
            "authority_ref": authority_ref,
            "render_policy": render_policy,
            "normalization": normalization_mode,
        }

    prohibited = require_list(ledger.get("prohibited_items", []), "authorized_content_ledger.prohibited_items")
    normalized_prohibited: list[dict[str, Any]] = []
    for index, raw in enumerate(prohibited):
        path = f"authorized_content_ledger.prohibited_items[{index}]"
        item = require_mapping(raw, path)
        kind = require_text(item.get("kind"), f"{path}.kind")
        require(kind in SUPPORTED_KINDS or kind == "any", f"{path}.kind", "must be a supported kind or any")
        value = require_text(item.get("value"), f"{path}.value")
        reason = require_text(item.get("reason"), f"{path}.reason")
        normalized_prohibited.append({"kind": kind, "value": value, "reason": reason})

    unresolved = require_list(ledger.get("unresolved_items", []), "authorized_content_ledger.unresolved_items")
    for index, raw in enumerate(unresolved):
        path = f"authorized_content_ledger.unresolved_items[{index}]"
        item = require_mapping(raw, path)
        require_text(item.get("proposed_value"), f"{path}.proposed_value")
        require_text(item.get("reason"), f"{path}.reason")
        require(item.get("status") == "NOT_VERIFIED", f"{path}.status", "must be NOT_VERIFIED")

    return by_id, normalized_prohibited


def validate_handoff(payload: dict[str, Any], ledger_items: dict[str, dict[str, Any]]) -> dict[str, Any]:
    ledger = require_mapping(payload.get("authorized_content_ledger"), "authorized_content_ledger")
    handoff = require_mapping(payload.get("provider_execution_handoff"), "provider_execution_handoff")
    require_text(handoff.get("handoff_id"), "provider_execution_handoff.handoff_id")
    require_text(handoff.get("locked_brief_ref"), "provider_execution_handoff.locked_brief_ref")
    require(
        handoff.get("authorized_content_ledger_ref") == ledger.get("ledger_id"),
        "provider_execution_handoff.authorized_content_ledger_ref",
        "must match authorized_content_ledger.ledger_id",
    )
    require_text(handoff.get("operation_or_design_plan_ref"), "provider_execution_handoff.operation_or_design_plan_ref")
    require_text(handoff.get("provider_specific_translation_owner"), "provider_execution_handoff.provider_specific_translation_owner")
    producer = require_text(handoff.get("binary_execution_owner"), "provider_execution_handoff.binary_execution_owner")

    ids = [require_text(item, f"provider_execution_handoff.authorized_content_ids[{index}]") for index, item in enumerate(
        require_list(handoff.get("authorized_content_ids"), "provider_execution_handoff.authorized_content_ids", non_empty=True)
    )]
    require_unique(ids, "provider_execution_handoff.authorized_content_ids")
    require(set(ids).issubset(ledger_items), "provider_execution_handoff.authorized_content_ids", "contains unknown content id")
    required_ids = {item_id for item_id, item in ledger_items.items() if item["render_policy"] == "required"}
    require(required_ids.issubset(ids), "provider_execution_handoff.authorized_content_ids", "must include every required content id")

    exact_text = require_list(handoff.get("exact_rendered_text", []), "provider_execution_handoff.exact_rendered_text")
    seen_text_ids: set[str] = set()
    for index, raw in enumerate(exact_text):
        path = f"provider_execution_handoff.exact_rendered_text[{index}]"
        item = require_mapping(raw, path)
        content_id = require_text(item.get("content_id"), f"{path}.content_id")
        value = require_text(item.get("value"), f"{path}.value")
        require(content_id in ledger_items, f"{path}.content_id", "must reference authorized content")
        authorized = ledger_items[content_id]
        require(authorized["kind"] != "brand_mark", f"{path}.content_id", "brand marks belong in approved_mark_ids")
        require(
            normalize(value, authorized["normalization"]) == normalize(authorized["value"], authorized["normalization"]),
            f"{path}.value",
            "must preserve authorized value",
        )
        seen_text_ids.add(content_id)

    required_text_ids = {
        item_id for item_id, item in ledger_items.items()
        if item["render_policy"] == "required" and item["kind"] != "brand_mark"
    }
    require(required_text_ids.issubset(seen_text_ids), "provider_execution_handoff.exact_rendered_text", "must include required rendered content")

    mark_ids = [require_text(item, f"provider_execution_handoff.approved_mark_ids[{index}]") for index, item in enumerate(
        require_list(handoff.get("approved_mark_ids", []), "provider_execution_handoff.approved_mark_ids")
    )]
    for item_id in mark_ids:
        require(item_id in ledger_items, "provider_execution_handoff.approved_mark_ids", f"unknown content id {item_id}")
        require(ledger_items[item_id]["kind"] == "brand_mark", "provider_execution_handoff.approved_mark_ids", f"{item_id} is not a brand_mark")

    specific_product = handoff.get("specific_product_required")
    require(isinstance(specific_product, bool), "provider_execution_handoff.specific_product_required", "must be boolean")
    product_refs = require_list(handoff.get("product_reference_refs", []), "provider_execution_handoff.product_reference_refs")
    locks = require_mapping(handoff.get("preservation_locks", {}), "provider_execution_handoff.preservation_locks")
    if specific_product:
        require(bool(product_refs), "provider_execution_handoff.product_reference_refs", "must not be empty for a specific product")
        missing_locks = sorted(REQUIRED_FIDELITY_LOCKS - {key for key, value in locks.items() if value is True})
        require(not missing_locks, "provider_execution_handoff.preservation_locks", f"missing true locks: {missing_locks}")

    negative_constraints = set(require_text(item, f"provider_execution_handoff.negative_constraints[{index}]") for index, item in enumerate(
        require_list(handoff.get("negative_constraints"), "provider_execution_handoff.negative_constraints", non_empty=True)
    ))
    missing_constraints = sorted(REQUIRED_NEGATIVE_CONSTRAINTS - negative_constraints)
    require(not missing_constraints, "provider_execution_handoff.negative_constraints", f"missing constraints: {missing_constraints}")

    comparison_required = require_mapping(handoff.get("comparison_required"), "provider_execution_handoff.comparison_required")
    for field in ("authorized_content", "brand_fidelity", "product_fidelity", "content_accuracy"):
        require(comparison_required.get(field) is True, f"provider_execution_handoff.comparison_required.{field}", "must be true")

    return {"producer": producer, "specific_product": specific_product}


def detect_violations(
    payload: dict[str, Any],
    ledger_items: dict[str, dict[str, Any]],
    prohibited_items: list[dict[str, Any]],
    handoff_context: dict[str, Any],
) -> dict[str, list[str]]:
    output = require_mapping(payload.get("provider_output_comparison"), "provider_output_comparison")
    require_text(output.get("output_ref"), "provider_output_comparison.output_ref")
    require(
        output.get("ledger_ref") == payload["authorized_content_ledger"]["ledger_id"],
        "provider_output_comparison.ledger_ref",
        "must match ledger id",
    )

    violations: dict[str, list[str]] = {
        "unauthorized_content": [],
        "altered_authorized_content": [],
        "omitted_required_content": [],
        "prohibited_content": [],
        "hard_gate_failures": [],
        "unverified_hard_gates": [],
    }

    detected = require_list(output.get("detected_content", []), "provider_output_comparison.detected_content")
    detected_authorized_ids: set[str] = set()
    for index, raw in enumerate(detected):
        path = f"provider_output_comparison.detected_content[{index}]"
        item = require_mapping(raw, path)
        kind = require_text(item.get("kind"), f"{path}.kind")
        require(kind in SUPPORTED_KINDS, f"{path}.kind", "unsupported kind")
        value = require_text(item.get("value"), f"{path}.value")
        content_id = item.get("authorized_content_id")
        if content_id is None:
            violations["unauthorized_content"].append(f"{kind}:{value}")
        else:
            content_id = require_text(content_id, f"{path}.authorized_content_id")
            if content_id not in ledger_items:
                violations["unauthorized_content"].append(f"{kind}:{value}")
            else:
                authorized = ledger_items[content_id]
                detected_authorized_ids.add(content_id)
                if kind != authorized["kind"]:
                    violations["altered_authorized_content"].append(f"{content_id}:kind")
                if normalize(value, authorized["normalization"]) != normalize(authorized["value"], authorized["normalization"]):
                    violations["altered_authorized_content"].append(f"{content_id}:value")

        for prohibited in prohibited_items:
            kind_matches = prohibited["kind"] in {"any", kind}
            if kind_matches and normalize(value, "case_insensitive") == normalize(prohibited["value"], "case_insensitive"):
                violations["prohibited_content"].append(f"{kind}:{value}")

    for item_id, item in ledger_items.items():
        if item["render_policy"] == "required" and item_id not in detected_authorized_ids:
            violations["omitted_required_content"].append(item_id)

    declared_unmatched = require_list(output.get("unmatched_content", []), "provider_output_comparison.unmatched_content")
    for index, item in enumerate(declared_unmatched):
        violations["unauthorized_content"].append(require_text(item, f"provider_output_comparison.unmatched_content[{index}]"))

    declared_altered = require_list(output.get("altered_authorized_content", []), "provider_output_comparison.altered_authorized_content")
    for index, item in enumerate(declared_altered):
        violations["altered_authorized_content"].append(require_text(item, f"provider_output_comparison.altered_authorized_content[{index}]"))

    gates = require_mapping(output.get("fidelity_gates"), "provider_output_comparison.fidelity_gates")
    for gate in HARD_GATES:
        status = require_text(gates.get(gate), f"provider_output_comparison.fidelity_gates.{gate}")
        require(status in {"PASS", "FAIL", "NOT_VERIFIED", "NOT_APPLICABLE"}, f"provider_output_comparison.fidelity_gates.{gate}", "invalid status")
        if status == "FAIL":
            violations["hard_gate_failures"].append(gate)
        elif status == "NOT_VERIFIED":
            violations["unverified_hard_gates"].append(gate)
        elif gate == "SV9" and handoff_context["specific_product"] and status == "NOT_APPLICABLE":
            violations["unverified_hard_gates"].append("SV9:NOT_APPLICABLE_FOR_SPECIFIC_PRODUCT")

    for key in violations:
        violations[key] = sorted(set(violations[key]))
    return violations


def validate_decision(payload: dict[str, Any], producer: str, violations: dict[str, list[str]]) -> dict[str, Any]:
    output = require_mapping(payload.get("provider_output_comparison"), "provider_output_comparison")
    review = require_mapping(payload.get("independent_review"), "independent_review")
    reviewer = require_text(review.get("reviewer"), "independent_review.reviewer")
    require(reviewer != producer, "independent_review.reviewer", "must differ from binary execution owner")
    review_verdict = require_text(review.get("verdict"), "independent_review.verdict")
    require(review_verdict in {"PASS", "CONDITIONAL_PASS", "NEEDS_WORK", "CRITICAL", "NOT_VERIFIED"}, "independent_review.verdict", "invalid verdict")

    review_gates = require_mapping(review.get("gates"), "independent_review.gates")
    comparison_gates = require_mapping(output.get("fidelity_gates"), "provider_output_comparison.fidelity_gates")
    for gate in HARD_GATES:
        status = require_text(review_gates.get(gate), f"independent_review.gates.{gate}")
        require(status in {"PASS", "FAIL", "NOT_VERIFIED", "NOT_APPLICABLE"}, f"independent_review.gates.{gate}", "invalid status")
        comparison_status = require_text(comparison_gates.get(gate), f"provider_output_comparison.fidelity_gates.{gate}")
        if comparison_status == "FAIL":
            require(status == "FAIL", f"independent_review.gates.{gate}", "must reflect the comparison FAIL")
        if comparison_status == "NOT_VERIFIED":
            require(status != "PASS", f"independent_review.gates.{gate}", "cannot PASS when comparison is NOT_VERIFIED")

    decision = require_mapping(payload.get("decision"), "decision")
    state = require_text(decision.get("state"), "decision.state")
    accepted = decision.get("accepted")
    delivered = decision.get("delivered")
    require(isinstance(accepted, bool), "decision.accepted", "must be boolean")
    require(isinstance(delivered, bool), "decision.delivered", "must be boolean")
    routes = [require_text(item, f"decision.return_routes[{index}]") for index, item in enumerate(
        require_list(decision.get("return_routes", []), "decision.return_routes")
    )]

    violation_count = sum(len(items) for items in violations.values())
    comparison_status = require_text(output.get("result"), "provider_output_comparison.result")
    require(comparison_status in {"PASS", "FAIL", "PARTIAL", "NOT_VERIFIED"}, "provider_output_comparison.result", "invalid status")

    if violation_count:
        require(comparison_status != "PASS", "provider_output_comparison.result", "cannot PASS with violations")
        require(state in BLOCKING_STATES, "decision.state", "must be a blocking state when violations exist")
        require(not accepted, "decision.accepted", "must be false when violations exist")
        require(not delivered, "decision.delivered", "must be false when violations exist")
        require(review_verdict not in {"PASS", "CONDITIONAL_PASS"}, "independent_review.verdict", "cannot pass review with violations")

        content_violations = any(violations[key] for key in (
            "unauthorized_content", "altered_authorized_content", "omitted_required_content", "prohibited_content"
        ))
        product_failure = "SV9" in violations["hard_gate_failures"] or any(
            value.startswith("SV9") for value in violations["unverified_hard_gates"]
        )
        brand_failure = "SV8" in violations["hard_gate_failures"]

        if content_violations:
            require(
                review_gates["SV11"] in {"FAIL", "NOT_VERIFIED"},
                "independent_review.gates.SV11",
                "must be non-PASS when content violations exist",
            )
            require(
                any(route in routes for route in ("authority_owner+design-refinement", "prompt-engineer", "provider-adapter")),
                "decision.return_routes",
                "content violations require an authority, prompt, or provider return route",
            )
        unauthorized_marks = any(
            value.startswith("brand_mark:")
            for key in ("unauthorized_content", "prohibited_content")
            for value in violations[key]
        )
        if unauthorized_marks:
            require(
                review_gates["SV8"] in {"FAIL", "NOT_VERIFIED"},
                "independent_review.gates.SV8",
                "must be non-PASS when unauthorized marks exist",
            )
        if product_failure:
            require(
                "design-refinement+product-image-production" in routes,
                "decision.return_routes",
                "SV9 failure requires design-refinement+product-image-production",
            )
        if brand_failure:
            require(
                any(route in routes for route in ("authority_owner+design-refinement", "prompt-engineer", "provider-adapter")),
                "decision.return_routes",
                "SV8 failure requires an authority, prompt, or provider return route",
            )
    else:
        require(comparison_status == "PASS", "provider_output_comparison.result", "must PASS when no violations exist")
        require(review_verdict == "PASS", "independent_review.verdict", "must PASS when accepting")
        require(state in ACCEPTING_STATES, "decision.state", "must be ACCEPTED or DELIVERED")
        require(accepted, "decision.accepted", "must be true")
        if state == "DELIVERED":
            require(delivered, "decision.delivered", "must be true for DELIVERED")

    return {
        "state": state,
        "accepted": accepted,
        "delivered": delivered,
        "reviewer": reviewer,
        "review_verdict": review_verdict,
        "return_routes": routes,
        "violation_count": violation_count,
    }


def validate_bundle(payload: dict[str, Any]) -> dict[str, Any]:
    require_mapping(payload, "root")
    require(payload.get("schema_version") == SCHEMA_VERSION, "schema_version", f"must be {SCHEMA_VERSION}")
    evidence_class = require_text(payload.get("evidence_class"), "evidence_class")
    require(evidence_class in SUPPORTED_EVIDENCE_CLASSES, "evidence_class", f"must be one of {sorted(SUPPORTED_EVIDENCE_CLASSES)}")
    case_id = require_text(payload.get("case_id"), "case_id")

    authority_refs = validate_authority(payload)
    ledger_items, prohibited_items = validate_ledger(payload, authority_refs)
    handoff_context = validate_handoff(payload, ledger_items)
    violations = detect_violations(payload, ledger_items, prohibited_items, handoff_context)
    decision = validate_decision(payload, handoff_context["producer"], violations)

    return {
        "schema_version": SCHEMA_VERSION,
        "case_id": case_id,
        "evidence_class": evidence_class,
        "status": "PASS",
        "contract_result": "BLOCKED_AS_REQUIRED" if decision["violation_count"] else "ACCEPTED_AS_REQUIRED",
        "violations": violations,
        "decision": decision,
        "boundaries": {
            "binary_pixel_inspection": "NOT_VERIFIED",
            "ocr_or_text_detection": "NOT_VERIFIED",
            "reviewer_authenticity": "NOT_VERIFIED",
            "semantic_product_fidelity": "SUPPLIED_EVIDENCE_ONLY",
        },
    }


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    require(isinstance(payload, dict), str(path), "root must be an object")
    return payload


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True)
        handle.write("\n")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path, help="Handoff evidence JSON")
    parser.add_argument("--report", type=Path, help="Write deterministic validation report")
    parser.add_argument("--compare", type=Path, help="Compare report with an immutable receipt")
    args = parser.parse_args(argv)

    try:
        report = validate_bundle(load_json(args.input))
        if args.compare:
            expected = load_json(args.compare)
            require(report == expected, "compare", f"report differs from {args.compare}")
        if args.report:
            write_json(args.report, report)
        print(json.dumps(report, indent=2, sort_keys=True))
        return 0
    except (OSError, json.JSONDecodeError, ValidationError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
