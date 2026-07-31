"""
Unit tests for hermes-auto-routing-dispatch fixtures.
Validates dispatch_receipts against dispatch-receipt.schema.yaml.
Tests dispatch mode semantics, depends_on ordering, and failure evidence.

Run: python3 -m pytest tests/auto-routing/test_dispatch_schema.py -v
"""

import pytest
import yaml
import jsonschema
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.parent
SCHEMA_PATH = REPO_ROOT / "schemas/auto-routing/dispatch-receipt.schema.yaml"
FIXTURES_DIR = REPO_ROOT / "contracts/fixtures/auto-routing"


@pytest.fixture(scope="module")
def schema():
    return yaml.safe_load(SCHEMA_PATH.read_text())


def load_dispatch_receipts(fixture_file):
    fixture = yaml.safe_load((FIXTURES_DIR / fixture_file).read_text())
    return fixture.get("dispatch_receipts", [])


# ── Durable dispatch fixture ──────────────────────────────────────────────────

def test_durable_dispatch_receipts_validate(schema):
    """All durable dispatch receipts must validate against schema."""
    for receipt in load_dispatch_receipts("positive-dispatch-durable.yaml"):
        jsonschema.validate(receipt, schema)


def test_durable_dispatch_has_worker_session_id():
    """Durable worker receipts must have worker_session_id in proof."""
    for receipt in load_dispatch_receipts("positive-dispatch-durable.yaml"):
        assert receipt["dispatch_mode"]["kind"] == "durable_worker"
        proof = receipt["dispatch_mode"]["proof"]
        assert "worker_session_id" in proof, (
            f"receipt {receipt['receipt_id']}: durable_worker proof missing worker_session_id"
        )
        assert "profile_id" in proof, (
            f"receipt {receipt['receipt_id']}: durable_worker proof missing profile_id"
        )


def test_durable_dispatch_profile_ids_match_fleet():
    """Durable dispatch profile_ids must be valid fleet agent profiles."""
    valid_profiles = {
        "agent-orchestrator", "agent-product", "agent-architecture",
        "agent-design", "agent-frontend", "agent-backend", "agent-review"
    }
    for receipt in load_dispatch_receipts("positive-dispatch-durable.yaml"):
        profile = receipt["dispatch_mode"]["proof"].get("profile_id", "")
        assert profile in valid_profiles, (
            f"receipt {receipt['receipt_id']}: unknown profile '{profile}'"
        )


def test_durable_dispatch_eligible_for_durable_acceptance():
    """Durable fixture notes must confirm durable_acceptance_eligible: true."""
    fixture = yaml.safe_load((FIXTURES_DIR / "positive-dispatch-durable.yaml").read_text())
    assert fixture.get("dispatch_notes", {}).get("durable_acceptance_eligible") is True


# ── Temporary dispatch fixture ────────────────────────────────────────────────

def test_temporary_dispatch_receipts_validate(schema):
    """All temporary dispatch receipts must validate against schema."""
    for receipt in load_dispatch_receipts("positive-dispatch-temporary.yaml"):
        jsonschema.validate(receipt, schema)


def test_temporary_dispatch_has_delegate_task_id():
    """Temporary delegation receipts must have delegate_task_id + parent_session_id."""
    for receipt in load_dispatch_receipts("positive-dispatch-temporary.yaml"):
        assert receipt["dispatch_mode"]["kind"] == "temporary_delegation"
        proof = receipt["dispatch_mode"]["proof"]
        assert "delegate_task_id" in proof, (
            f"receipt {receipt['receipt_id']}: temporary proof missing delegate_task_id"
        )
        assert "parent_session_id" in proof, (
            f"receipt {receipt['receipt_id']}: temporary proof missing parent_session_id"
        )


def test_temporary_dispatch_not_eligible_for_durable_acceptance():
    """Temporary fixture must explicitly mark durable_acceptance_eligible: false."""
    fixture = yaml.safe_load((FIXTURES_DIR / "positive-dispatch-temporary.yaml").read_text())
    notes = fixture.get("dispatch_notes", {})
    assert notes.get("non_durable") is True
    assert notes.get("durable_acceptance_eligible") is False


def test_temporary_dispatch_has_synthesis_restriction():
    """Temporary fixture must document synthesis restriction against external claims."""
    fixture = yaml.safe_load((FIXTURES_DIR / "positive-dispatch-temporary.yaml").read_text())
    restriction = fixture.get("dispatch_notes", {}).get("synthesis_restriction", "")
    assert restriction.strip(), "temporary dispatch fixture missing synthesis_restriction note"


# ── Blocked dispatch fixture ──────────────────────────────────────────────────

def test_blocked_dispatch_receipts_validate(schema):
    """Blocked dispatch receipts must still validate against schema."""
    for receipt in load_dispatch_receipts("negative-dispatch-blocked.yaml"):
        jsonschema.validate(receipt, schema)


def test_blocked_dispatch_has_blocked_status():
    """Blocked fixture receipts must have status: blocked."""
    for receipt in load_dispatch_receipts("negative-dispatch-blocked.yaml"):
        assert receipt["status"] == "blocked", (
            f"receipt {receipt['receipt_id']}: expected status=blocked, got {receipt['status']}"
        )


def test_blocked_dispatch_has_actionable_error():
    """Blocked fixture must have actionable_error and blocked_downstream."""
    fixture = yaml.safe_load((FIXTURES_DIR / "negative-dispatch-blocked.yaml").read_text())
    notes = fixture.get("dispatch_notes", {})
    assert notes.get("actionable_error", "").strip(), "blocked fixture missing actionable_error"
    assert notes.get("blocked_downstream"), "blocked fixture missing blocked_downstream list"
    assert notes.get("blocking_reason", "").strip(), "blocked fixture missing blocking_reason"


def test_blocked_dispatch_has_resume_action():
    """Blocked fixture must document resume action."""
    fixture = yaml.safe_load((FIXTURES_DIR / "negative-dispatch-blocked.yaml").read_text())
    assert fixture.get("dispatch_notes", {}).get("resume_action", "").strip(), (
        "blocked fixture missing resume_action"
    )


# ── Cross-fixture invariants ──────────────────────────────────────────────────

def test_all_receipts_have_unique_receipt_ids():
    """receipt_id must be unique across all dispatch receipts."""
    all_ids = []
    for fixture_file in [
        "positive-dispatch-durable.yaml",
        "positive-dispatch-temporary.yaml",
        "negative-dispatch-blocked.yaml",
    ]:
        for r in load_dispatch_receipts(fixture_file):
            all_ids.append(r["receipt_id"])
    assert len(all_ids) == len(set(all_ids)), f"Duplicate receipt_ids: {all_ids}"


def test_all_receipts_reference_known_plan():
    """All receipts must reference the same plan_id as their fixture."""
    for fixture_file in [
        "positive-dispatch-durable.yaml",
        "positive-dispatch-temporary.yaml",
        "negative-dispatch-blocked.yaml",
    ]:
        fixture = yaml.safe_load((FIXTURES_DIR / fixture_file).read_text())
        fixture_plan_id = fixture.get("plan_id")
        for receipt in fixture.get("dispatch_receipts", []):
            assert receipt["plan_id"] == fixture_plan_id, (
                f"{fixture_file}: receipt plan_id '{receipt['plan_id']}' "
                f"!= fixture plan_id '{fixture_plan_id}'"
            )
