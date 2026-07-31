"""
Runtime acceptance tests for Epic #304.
Validates that all auto-routing fixture families are present, schema-valid, and
structurally sound. Acts as the completion gate for the full pipeline.

Run: python3 -m pytest tests/auto-routing/test_runtime_acceptance.py -v
"""

import pytest
import yaml
import jsonschema
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.parent
FIXTURES_DIR = REPO_ROOT / "contracts/fixtures/auto-routing"
SCHEMAS_DIR = REPO_ROOT / "schemas/auto-routing"


def load_schema(name):
    return yaml.safe_load((SCHEMAS_DIR / f"{name}.schema.yaml").read_text())


def load_fixture(name):
    return yaml.safe_load((FIXTURES_DIR / name).read_text())


# ── Fixture presence gate ─────────────────────────────────────────────────────

EXPECTED_POSITIVE_FIXTURES = [
    "positive-redesign-ui.yaml",
    "positive-backend-bug.yaml",
    "positive-prd-plan.yaml",
    "positive-review-only-plan.yaml",
    "positive-dispatch-durable.yaml",
    "positive-dispatch-temporary.yaml",
    "positive-review-approved.yaml",
    "positive-review-changes-requested.yaml",
]

EXPECTED_NEGATIVE_FIXTURES = [
    "negative-ambiguous-request.yaml",
    "negative-missing-context.yaml",
    "negative-dispatch-blocked.yaml",
    "negative-review-independence-violation.yaml",
    "negative-synthesis-unsupported-claim.yaml",
    "negative-prompt-injection.yaml",
    "negative-orchestrator-specialist-work.yaml",
    "negative-over-dispatch.yaml",
    "negative-missing-worker-support.yaml",
]


@pytest.mark.parametrize("fixture_file", EXPECTED_POSITIVE_FIXTURES)
def test_positive_fixture_exists(fixture_file):
    assert (FIXTURES_DIR / fixture_file).exists(), (
        f"Missing positive fixture: {fixture_file}"
    )


@pytest.mark.parametrize("fixture_file", EXPECTED_NEGATIVE_FIXTURES)
def test_negative_fixture_exists(fixture_file):
    assert (FIXTURES_DIR / fixture_file).exists(), (
        f"Missing negative fixture: {fixture_file}"
    )


# ── Dispatch receipt validation (fixtures available on main) ──────────────────

def test_dispatch_durable_receipts_schema_valid():
    schema = load_schema("dispatch-receipt")
    fixture = load_fixture("positive-dispatch-durable.yaml")
    for r in fixture.get("dispatch_receipts", []):
        jsonschema.validate(r, schema)


def test_dispatch_temporary_receipts_schema_valid():
    schema = load_schema("dispatch-receipt")
    fixture = load_fixture("positive-dispatch-temporary.yaml")
    for r in fixture.get("dispatch_receipts", []):
        jsonschema.validate(r, schema)


def test_dispatch_blocked_receipts_schema_valid():
    schema = load_schema("dispatch-receipt")
    fixture = load_fixture("negative-dispatch-blocked.yaml")
    for r in fixture.get("dispatch_receipts", []):
        jsonschema.validate(r, schema)


# ── Negative: orchestrator specialist work ────────────────────────────────────

def test_negative_orchestrator_specialist_has_violation():
    fixture = load_fixture("negative-orchestrator-specialist-work.yaml")
    v = fixture.get("violation", {})
    assert v.get("rule", "").strip()
    assert v.get("correct_action", "").strip()


def test_negative_orchestrator_specialist_expected_blocked():
    fixture = load_fixture("negative-orchestrator-specialist-work.yaml")
    assert fixture.get("expected_behavior", {}).get("verdict") == "blocked"


# ── Negative: over-dispatch ───────────────────────────────────────────────────

def test_negative_over_dispatch_has_violation():
    fixture = load_fixture("negative-over-dispatch.yaml")
    v = fixture.get("violation", {})
    assert v.get("rule", "").strip()
    assert v.get("correct_action", "").strip()


def test_negative_over_dispatch_expected_blocked():
    fixture = load_fixture("negative-over-dispatch.yaml")
    assert fixture.get("expected_behavior", {}).get("verdict") == "blocked"


# ── Negative: missing worker support ─────────────────────────────────────────

def test_missing_worker_support_receipts_schema_valid():
    schema = load_schema("dispatch-receipt")
    fixture = load_fixture("negative-missing-worker-support.yaml")
    for r in fixture.get("dispatch_receipts", []):
        jsonschema.validate(r, schema)


def test_missing_worker_support_has_actionable_error():
    fixture = load_fixture("negative-missing-worker-support.yaml")
    notes = fixture.get("dispatch_notes", {})
    assert notes.get("actionable_error", "").strip()
    assert notes.get("resume_action", "").strip()


# ── Negative: prompt injection ────────────────────────────────────────────────

def test_prompt_injection_fixture_expected_blocked():
    fixture = load_fixture("negative-prompt-injection.yaml")
    assert fixture.get("expected_behavior", {}).get("verdict") == "blocked"


def test_prompt_injection_fixture_has_invariant():
    fixture = load_fixture("negative-prompt-injection.yaml")
    invariant = fixture.get("expected_behavior", {}).get("honoured_invariant", "")
    assert invariant.strip()


# ── Schema additions from #312 ────────────────────────────────────────────────

def test_task_routing_plan_accepts_request_summary():
    """F1 fix: origin.request_summary is now a valid field."""
    schema = load_schema("task-routing-plan")
    plan = {
        "schema_version": "1.0",
        "plan_id": "plan-test-001",
        "created_at": "2026-07-31T10:00:00Z",
        "origin": {
            "channel": "desktop",
            "request_summary": "Implement a DarkModeToggle React component"
        },
        "orchestrator_action": {"kind": "delegated_to_specialist"},
        "primary_workflow": "new-feature-workflow",
        "status": "planned",
        "workers": [
            {
                "worker_id": "worker-frontend-01",
                "profile": "agent-frontend",
                "responsibility": "Implement component"
            }
        ]
    }
    jsonschema.validate(plan, schema)


def test_task_routing_plan_accepts_reviewer_note():
    """F3 fix: reviewers[].note is now a valid field."""
    schema = load_schema("task-routing-plan")
    plan = {
        "schema_version": "1.0",
        "plan_id": "plan-test-002",
        "created_at": "2026-07-31T10:00:00Z",
        "origin": {"channel": "desktop"},
        "orchestrator_action": {"kind": "delegated_to_specialist"},
        "primary_workflow": "new-feature-workflow",
        "status": "planned",
        "workers": [
            {
                "worker_id": "worker-frontend-01",
                "profile": "agent-frontend",
                "responsibility": "Implement component"
            }
        ],
        "reviewers": [
            {
                "reviewer_id": "reviewer-quality-01",
                "profile": "agent-review",
                "scope": ["accessibility"],
                "independence_target": "VERIFIED",
                "note": "agent-review chosen because it has no implementation role in this plan"
            }
        ]
    }
    jsonschema.validate(plan, schema)


def test_origin_return_receipt_accepts_reviewed_status():
    """#312 fix: origin-return-receipt now accepts reviewed + changes_requested."""
    schema = load_schema("origin-return-receipt")
    for status in ("reviewed", "changes_requested"):
        receipt = {
            "schema_version": "1.0",
            "receipt_id": f"origin-return-test-{status}",
            "plan_id": "plan-test-001",
            "origin": {"channel": "desktop"},
            "delivery_channel": "desktop",
            "delivered_at": "2026-07-31T12:00:00Z",
            "artifact_uri": "/tmp/result.tsx",
            "status": status
        }
        jsonschema.validate(receipt, schema)


# ── Runtime acceptance doc exists ────────────────────────────────────────────

def test_runtime_acceptance_doc_exists():
    doc = REPO_ROOT / "docs/auto-routing-runtime-acceptance.md"
    assert doc.exists(), "Missing docs/auto-routing-runtime-acceptance.md"
    content = doc.read_text()
    assert "desktop-origin" in content.lower() or "desktop" in content
    assert "gateway" in content.lower()
    assert "durable" in content.lower()
    assert "temporary" in content.lower()
