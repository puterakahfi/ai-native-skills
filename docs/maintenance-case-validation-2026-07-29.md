# Maintenance Case Composition — Implementation Validation

Issue: `#249`  
Parent epic: `#246`  
Architecture decision: `#247` / `docs/lifecycle-completion-architecture-decision-2026-07-29.md`

## Execution context

```yaml
operation: CREATE_AND_UPDATE_COMPOSITION
new_capability: maintenance-case
package_type: skill
pattern: facade
primary_workflow: skill-authoring-workflow
branch: 249-maintenance-case-composition
base: 246-lifecycle-completion@ef6b80bd6b718d69aa397d45e9add85e1fa4b470
core_contract: NONE_FOR_MVP
router_contract_compatibility: "~0.2"
```

## Observable outputs

- `skills/maintenance-case/SKILL.md`
- `skills/maintenance-case/references/signal-routing-and-closure.md`
- `contracts/tests/maintenance-case.test.yaml`
- updated `skills/workflow-router/SKILL.md` `1.8.0 → 1.9.0`
- expanded `contracts/tests/workflow-router.test.yaml`

## Acceptance assessment

| Criterion | Status | Evidence |
|---|---|---|
| Operate-and-maintain is a recurring loop, not phase 13 | PASS | facade procedure and explicit boundary |
| No competing maintenance workflow/router | PASS | `workflow-router` remains sole primary route selector |
| Signal taxonomy covers incident, defect, security, dependency, performance, reliability, cost, data, product, docs, deprecation, debt, preventive work | PASS | explicit taxonomy |
| Active incident and non-active defect remain distinct | PASS | route table, reference, dedicated regressions |
| Exactly one primary route per bounded case | PASS | hard gate and conflict classification |
| Mitigation and permanent correction can split into linked cases | PASS | procedure/reference/regressions |
| Actual outcome evidence required for closure | PASS | outcome-specific evidence and closure gate |
| Provider success/CI/merge/plan are not generalized into operational success | PASS | verification rules and regressions |
| Documentation assurance participates in case closure | PASS | explicit integration and blocking state |
| Continuity preserves case identity, evidence, blockers, and next action | PASS | output/handoff contract and regression |
| Product-defined severity, thresholds, on-call, and action authority remain product-owned | PASS | inputs, hard gates, ownership boundary |
| New route vocabulary does not silently change Core | PASS_WITH_FLAG | declared adapter-local fallback refinement under `~0.2`; Core RFC deferred |
| Role composition changes required | NOT_APPLICABLE | existing `role-switcher` already assigns owner/specialists/reviewers; no duplicate logic added |

## Self-review

```yaml
package_shape: PASS
frontmatter_identity: PASS
facade_boundary: PASS
workflow_router_ownership: PRESERVED
single_primary_route: PASS
core_contract_compatibility: PASS_WITH_ADAPTER_LOCAL_EXTENSION
product_policy_leakage: NONE
behavioral_regression_contracts: PRESENT
scripts_and_local_tests: NOT_APPLICABLE
inventory_and_published_catalog: DEFERRED_TO_250_INTEGRATION
independent_review: LIMITED_SAME_EXECUTION_CONTEXT
```

## Known gaps

- Repository-hosted validators and CI have not yet run for this branch.
- Capability inventory and orchestration manifest integration are consolidated in #250.
- Runtime persistence and execution receipts remain #250.
- Real operational evidence remains #251.
- Core route expansion or maintenance contract promotion remains prohibited without post-#251 RFC evidence.

## Handoff to #250

```yaml
capability_id: maintenance-case
role: specialist
produces:
  - maintenance_signal_assessment
  - maintenance_routing_input
  - maintenance_case_record
  - maintenance_outcome_record
  - maintenance_followup
completion_evidence:
  - signal_identity_and_time_recorded
  - evidence_confidence_recorded
  - active_incident_status_explicit
  - exactly_one_primary_route_selected_by_workflow_router
  - linked_execution_and_review_refs_recorded
  - actual_outcome_evidence_recorded
  - documentation_impact_reconciled
  - closure_and_followup_recorded
required_orchestration_scenarios:
  - active_incident
  - verified_regression
  - dependency_or_security_signal
  - performance_or_reliability_signal
  - product_metric_or_feedback_signal
  - documentation_drift
  - preventive_maintenance
  - maintenance_resume
```

## Capability evolution verdict

```text
LOCAL_ONLY
```

The adapter-local facade and router refinement require integrated and real maintenance validation before any Core RFC.