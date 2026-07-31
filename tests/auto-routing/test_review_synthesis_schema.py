"""
Unit tests for hermes-auto-routing-review-synthesis fixtures.
Validates review_receipts, synthesis_receipts, and origin_return_receipts
against their schemas. Tests independence rules, state ladder, and negative patterns.

Run: python3 -m pytest tests/auto-routing/test_review_synthesis_schema.py -v
"""

import pytest
import yaml
import jsonschema
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.parent
SCHEMAS = {
    "review": yaml.safe_load((REPO_ROOT / "schemas/auto-routing/review-receipt.schema.yaml").read_text()),
    "synthesis": yaml.safe_load((REPO_ROOT / "schemas/auto-routing/synthesis-receipt.schema.yaml").read_text()),
    "origin_return": yaml.safe_load((REPO_ROOT / "schemas/auto-routing/origin-return-receipt.schema.yaml").read_text()),
}
FIXTURES_DIR = REPO_ROOT / "contracts/fixtures/auto-routing"


def load_fixture(name):
    return yaml.safe_load((FIXTURES_DIR / name).read_text())


# ── Approved flow ─────────────────────────────────────────────────────────────

def test_approved_review_receipts_validate():
    fixture = load_fixture("positive-review-approved.yaml")
    for r in fixture.get("review_receipts", []):
        jsonschema.validate(r, SCHEMAS["review"])


def test_approved_synthesis_receipt_validates():
    fixture = load_fixture("positive-review-approved.yaml")
    jsonschema.validate(fixture["synthesis_receipt"], SCHEMAS["synthesis"])


def test_approved_origin_return_validates():
    fixture = load_fixture("positive-review-approved.yaml")
    jsonschema.validate(fixture["origin_return_receipt"], SCHEMAS["origin_return"])


def test_approved_flow_independence_verified():
    fixture = load_fixture("positive-review-approved.yaml")
    for r in fixture["review_receipts"]:
        assert r["independence"]["verdict"] == "VERIFIED"
        assert r["independence"]["compromises"] == []


def test_approved_flow_final_status_approved():
    fixture = load_fixture("positive-review-approved.yaml")
    assert fixture["synthesis_receipt"]["final_status"] == "approved"


def test_approved_flow_approved_claim_asserted():
    fixture = load_fixture("positive-review-approved.yaml")
    approved_claim = fixture["synthesis_receipt"]["promoted_claims"].get("approved", {})
    assert approved_claim.get("asserted") is True


def test_approved_flow_unresolved_has_merge_and_accept():
    """merge + accept are always unresolved — external actions outside fleet scope."""
    fixture = load_fixture("positive-review-approved.yaml")
    unresolved = [c["claim"] for c in fixture["synthesis_receipt"].get("unresolved_claims", [])]
    assert "merged to main" in unresolved
    assert "accepted by product owner" in unresolved


def test_approved_flow_origin_return_status_delivered():
    fixture = load_fixture("positive-review-approved.yaml")
    assert fixture["origin_return_receipt"]["status"] == "delivered"


def test_approved_flow_origin_delivery_channel_matches_origin():
    fixture = load_fixture("positive-review-approved.yaml")
    orr = fixture["origin_return_receipt"]
    assert orr["delivery_channel"] == orr["origin"]["channel"]


# ── Changes requested flow ────────────────────────────────────────────────────

def test_changes_requested_review_receipt_validates():
    fixture = load_fixture("positive-review-changes-requested.yaml")
    for r in fixture.get("review_receipts", []):
        jsonschema.validate(r, SCHEMAS["review"])


def test_changes_requested_synthesis_validates():
    fixture = load_fixture("positive-review-changes-requested.yaml")
    jsonschema.validate(fixture["synthesis_receipt"], SCHEMAS["synthesis"])


def test_changes_requested_origin_return_validates():
    fixture = load_fixture("positive-review-changes-requested.yaml")
    jsonschema.validate(fixture["origin_return_receipt"], SCHEMAS["origin_return"])


def test_changes_requested_final_status_reviewed_not_approved():
    """changes_requested verdict must NOT yield final_status=approved."""
    fixture = load_fixture("positive-review-changes-requested.yaml")
    sr = fixture["synthesis_receipt"]
    assert sr["final_status"] == "reviewed"
    assert sr["final_status"] != "approved"


def test_changes_requested_approved_claim_not_asserted():
    """approved claim must be asserted=false when verdict=changes_requested."""
    fixture = load_fixture("positive-review-changes-requested.yaml")
    approved_claim = fixture["synthesis_receipt"]["promoted_claims"].get("approved", {})
    assert approved_claim.get("asserted") is False


def test_changes_requested_independence_limited_has_compromises():
    """LIMITED independence must document compromises."""
    fixture = load_fixture("positive-review-changes-requested.yaml")
    for r in fixture["review_receipts"]:
        if r["independence"]["verdict"] == "LIMITED":
            assert len(r["independence"]["compromises"]) > 0


def test_changes_requested_unresolved_has_approved():
    """Unresolved claims must include 'approved' when verdict=changes_requested."""
    fixture = load_fixture("positive-review-changes-requested.yaml")
    unresolved = [c["claim"] for c in fixture["synthesis_receipt"].get("unresolved_claims", [])]
    assert "approved" in unresolved


# ── Negative: independence violation ─────────────────────────────────────────

def test_independence_violation_receipt_validates():
    """Even a NOT_VERIFIED receipt must be schema-valid."""
    fixture = load_fixture("negative-review-independence-violation.yaml")
    for r in fixture.get("review_receipts", []):
        jsonschema.validate(r, SCHEMAS["review"])


def test_independence_violation_verdict_not_verified():
    fixture = load_fixture("negative-review-independence-violation.yaml")
    for r in fixture["review_receipts"]:
        assert r["independence"]["verdict"] == "NOT_VERIFIED"


def test_independence_violation_synthesis_blocked_approved_claim():
    """synthesis_notes must block approved claim when independence=NOT_VERIFIED."""
    fixture = load_fixture("negative-review-independence-violation.yaml")
    blocked = [c["claim"] for c in fixture.get("synthesis_notes", {}).get("blocked_claims", [])]
    assert "approved" in blocked


def test_independence_violation_required_action_present():
    fixture = load_fixture("negative-review-independence-violation.yaml")
    action = fixture.get("synthesis_notes", {}).get("required_action", "")
    assert action.strip(), "independence violation fixture missing required_action"


# ── Negative: unsupported completion claim ────────────────────────────────────

def test_unsupported_claim_documents_violation():
    fixture = load_fixture("negative-synthesis-unsupported-claim.yaml")
    v = fixture.get("synthesis_violation", {})
    assert v.get("attempted_claim") == "merged"
    assert v.get("evidence_lineage") == "temporary_delegation"
    assert v.get("violation", "").strip()
    assert v.get("correct_action", "").strip()


# ── Cross-fixture invariants ──────────────────────────────────────────────────

REVIEW_FIXTURES = [
    "positive-review-approved.yaml",
    "positive-review-changes-requested.yaml",
    "negative-review-independence-violation.yaml",
]


@pytest.mark.parametrize("fixture_file", REVIEW_FIXTURES)
def test_review_receipts_reference_plan(fixture_file):
    fixture = load_fixture(fixture_file)
    fixture_plan_id = fixture.get("plan_id")
    for r in fixture.get("review_receipts", []):
        assert r["plan_id"] == fixture_plan_id


@pytest.mark.parametrize("fixture_file", REVIEW_FIXTURES)
def test_review_receipt_independence_has_compromises_when_not_verified(fixture_file):
    """NOT_VERIFIED or LIMITED independence must have non-empty compromises."""
    fixture = load_fixture(fixture_file)
    for r in fixture.get("review_receipts", []):
        verdict = r["independence"]["verdict"]
        if verdict in ("NOT_VERIFIED", "LIMITED"):
            assert len(r["independence"].get("compromises", [])) > 0, (
                f"{fixture_file}: {r['receipt_id']} has {verdict} independence but no compromises"
            )
