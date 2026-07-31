"""
Unit tests for hermes-auto-routing-planner fixtures.
Validates all positive plan fixtures against task-routing-plan.schema.yaml.
Tests that negative fixtures are structurally consistent (status=blocked/not_verified, plan=null).

Run: python3 -m pytest tests/auto-routing/test_planner_schema.py -v
"""

import pytest
import yaml
import jsonschema
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.parent
SCHEMA_PATH = REPO_ROOT / "schemas/auto-routing/task-routing-plan.schema.yaml"
FIXTURES_DIR = REPO_ROOT / "contracts/fixtures/auto-routing"

POSITIVE_PLAN_FIXTURES = [
    "positive-redesign-ui.yaml",
    "positive-backend-bug.yaml",
    "positive-prd-plan.yaml",
    "positive-review-only-plan.yaml",
]

NEGATIVE_FIXTURES = [
    "negative-ambiguous-request.yaml",
    "negative-missing-context.yaml",
]


@pytest.fixture(scope="module")
def schema():
    return yaml.safe_load(SCHEMA_PATH.read_text())


@pytest.mark.parametrize("fixture_file", POSITIVE_PLAN_FIXTURES)
def test_positive_plan_validates_against_schema(schema, fixture_file):
    """All positive plan fixtures must validate against task-routing-plan schema."""
    fixture = yaml.safe_load((FIXTURES_DIR / fixture_file).read_text())
    plan = fixture.get("plan", fixture)  # some fixtures have top-level 'plan' key
    jsonschema.validate(plan, schema)


@pytest.mark.parametrize("fixture_file", POSITIVE_PLAN_FIXTURES)
def test_positive_plan_has_exactly_one_primary_workflow(fixture_file):
    """Each positive plan must have exactly one non-empty primary_workflow."""
    fixture = yaml.safe_load((FIXTURES_DIR / fixture_file).read_text())
    plan = fixture.get("plan", fixture)
    assert plan.get("primary_workflow"), f"{fixture_file}: primary_workflow missing or empty"


@pytest.mark.parametrize("fixture_file", POSITIVE_PLAN_FIXTURES)
def test_positive_plan_reviewer_independence_target_consistent(fixture_file):
    """
    Reviewers whose profile also appears as a worker must have independence_target: LIMITED.
    Reviewers whose profile does NOT appear as a worker must have independence_target: VERIFIED.

    Note: agent-review may legitimately appear as both a worker (quality-check step producing
    artifacts) and as a reviewer (independent sign-off). When it does, independence_target
    must be LIMITED. VERIFIED is only valid when the reviewer profile is absent from workers.
    """
    fixture = yaml.safe_load((FIXTURES_DIR / fixture_file).read_text())
    plan = fixture.get("plan", fixture)
    worker_profiles = {w["profile"] for w in plan.get("workers", [])}
    for reviewer in plan.get("reviewers", []):
        profile = reviewer["profile"]
        target = reviewer.get("independence_target")
        if profile in worker_profiles:
            assert target == "LIMITED", (
                f"{fixture_file}: reviewer '{profile}' also appears as worker — "
                f"independence_target must be LIMITED, got '{target}'"
            )
        else:
            assert target == "VERIFIED", (
                f"{fixture_file}: reviewer '{profile}' is independent from workers — "
                f"independence_target must be VERIFIED, got '{target}'"
            )


@pytest.mark.parametrize("fixture_file", POSITIVE_PLAN_FIXTURES)
def test_positive_plan_depends_on_refs_resolve(fixture_file):
    """All depends_on refs must resolve to a worker_id in the same plan."""
    fixture = yaml.safe_load((FIXTURES_DIR / fixture_file).read_text())
    plan = fixture.get("plan", fixture)
    workers = plan.get("workers", [])
    worker_ids = {w["worker_id"] for w in workers}
    for worker in workers:
        for dep in worker.get("depends_on", []):
            assert dep in worker_ids, (
                f"{fixture_file}: worker '{worker['worker_id']}' depends_on "
                f"'{dep}' which is not in worker_ids {worker_ids}"
            )


@pytest.mark.parametrize("fixture_file", POSITIVE_PLAN_FIXTURES)
def test_positive_plan_no_duplicate_worker_profiles(fixture_file):
    """No two workers in the same plan may share the same profile."""
    fixture = yaml.safe_load((FIXTURES_DIR / fixture_file).read_text())
    plan = fixture.get("plan", fixture)
    profiles = [w["profile"] for w in plan.get("workers", [])]
    assert len(profiles) == len(set(profiles)), (
        f"{fixture_file}: duplicate worker profiles found: {profiles}"
    )


def test_review_only_plan_has_no_implementation_workers():
    """Review-only plan must not contain implementation worker profiles."""
    fixture = yaml.safe_load((FIXTURES_DIR / "positive-review-only-plan.yaml").read_text())
    plan = fixture.get("plan", fixture)
    impl_profiles = {"agent-design", "agent-frontend", "agent-backend"}
    worker_profiles = {w["profile"] for w in plan.get("workers", [])}
    overlap = impl_profiles & worker_profiles
    assert not overlap, f"Review-only plan should not have implementation workers: {overlap}"


def test_prd_plan_has_no_implementation_workers():
    """PRD plan must not contain frontend/backend implementation workers."""
    fixture = yaml.safe_load((FIXTURES_DIR / "positive-prd-plan.yaml").read_text())
    plan = fixture.get("plan", fixture)
    impl_profiles = {"agent-frontend", "agent-backend"}
    worker_profiles = {w["profile"] for w in plan.get("workers", [])}
    overlap = impl_profiles & worker_profiles
    assert not overlap, f"PRD plan should not have implementation workers: {overlap}"


@pytest.mark.parametrize("fixture_file", NEGATIVE_FIXTURES)
def test_negative_fixture_has_null_plan(fixture_file):
    """Negative fixtures must have plan: null (no plan emitted on block)."""
    fixture = yaml.safe_load((FIXTURES_DIR / fixture_file).read_text())
    assert fixture.get("planner_output", {}).get("plan") is None, (
        f"{fixture_file}: negative fixture should have plan: null"
    )


@pytest.mark.parametrize("fixture_file", NEGATIVE_FIXTURES)
def test_negative_fixture_has_blocking_status(fixture_file):
    """Negative fixtures must have status blocked or not_verified."""
    fixture = yaml.safe_load((FIXTURES_DIR / fixture_file).read_text())
    status = fixture.get("planner_output", {}).get("status")
    assert status in ("blocked", "not_verified"), (
        f"{fixture_file}: expected blocked/not_verified, got '{status}'"
    )


@pytest.mark.parametrize("fixture_file", NEGATIVE_FIXTURES)
def test_negative_fixture_has_blocking_reason(fixture_file):
    """Negative fixtures must explain why they are blocked."""
    fixture = yaml.safe_load((FIXTURES_DIR / fixture_file).read_text())
    reason = fixture.get("planner_output", {}).get("blocking_reason", "")
    assert reason.strip(), f"{fixture_file}: blocking_reason is missing or empty"
