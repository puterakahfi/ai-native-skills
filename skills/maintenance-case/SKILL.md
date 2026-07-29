---
name: maintenance-case
description: Facade skill for qualifying operational and product signals, normalizing a bounded maintenance case, preparing evidence-backed routing input for workflow-router, preserving cross-workflow continuity, and closing the case with actual outcome and follow-up evidence without creating a competing maintenance lifecycle.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.pattern: facade
  ai-native-skills.related_skills: '["workflow-router","role-switcher","incident-response","bugfix-workflow","new-feature-workflow","deployment-workflow","code-review-workflow","design-audit","design-refinement","redesign-workflow","observability-design","resilience-engineering","security-review","technical-debt-governance","documentation-assurance","task-continuity","product-development-workflow","skill-evolution"]'
---

# Maintenance Case

Operate-and-maintain is a recurring composition, not a thirteenth product-development phase and not a new primary workflow.

This facade qualifies signals, creates a bounded case identity, normalizes evidence, prepares routing input, links activity across the selected governing workflow, and determines whether the bounded case can close. `workflow-router` still selects exactly one primary lifecycle or standalone capability.

## Facade contract

```yaml
facade:
  capability: maintenance_case_management
  owns:
    - signal_intake_and_qualification
    - evidence_confidence_and_active_incident_classification
    - bounded_case_identity_scope_and_outcome
    - workflow_router_input_preparation
    - cross_workflow_evidence_linkage
    - closure_readiness_and_followup
    - recurrence_and_problem_management_handoff
  does_not_own:
    - primary_workflow_selection
    - incident_mitigation_or_bugfix_implementation
    - feature_or_design_delivery
    - deployment_execution
    - security_or_product_decisions
    - product_specific_severity_thresholds
    - merge_release_or_deployment_authority
    - continuous_monitoring_runtime
  built_in_strategies:
    - operational_signal_case
    - product_or_user_signal_case
    - preventive_maintenance_case
  extension_contract: product_maintenance_policy
  fallback_policy: fail_closed
  output_contract: maintenance_case_report
```

## Trigger

Load when a signal may require engineering or product action, including:

```text
active incident or service degradation
verified defect or regression
security or dependency finding
performance, reliability, cost, or data-quality anomaly
operational configuration or migration issue
user feedback or product metric movement
documentation drift or deprecation requirement
technical debt or maintainability finding
scheduled preventive maintenance
```

Do not load for routine explanation-only questions. Monitoring design remains with `observability-design`; this facade begins when a signal or bounded preventive action needs qualification and traceability.

## Required inputs

```yaml
maintenance_case_input:
  signal_description: string
  signal_source_refs: []
  observed_at: string
  environment_or_product_context: []
  affected_subjects: []
  requested_or_expected_outcome: string
  product_maintenance_policy_refs: []
  known_authority_and_constraints: []
```

If signal identity, source, observed time, affected subject, or intended outcome cannot be established, return `NOT_VERIFIED` and do not route to production action.

## Signal taxonomy

Classify exactly one primary signal class and any secondary concerns:

```text
ACTIVE_INCIDENT
SERVICE_DEGRADATION
VERIFIED_DEFECT
SECURITY_FINDING
DEPENDENCY_OR_PLATFORM_CHANGE
PERFORMANCE_REGRESSION
RELIABILITY_RISK
COST_ANOMALY
DATA_OR_MIGRATION_ISSUE
USER_OR_PRODUCT_SIGNAL
DOCUMENTATION_DRIFT
DEPRECATION_OR_REMOVAL
TECHNICAL_DEBT
PREVENTIVE_MAINTENANCE
NOT_VERIFIED
```

Classification is evidence, not the primary route.

## Procedure

### Phase 1 — Intake and qualify

1. Resolve signal source, observed time, environment, affected subject, and reporter.
2. Separate direct evidence, inference, assumptions, and unknowns.
3. Determine whether impact is active now, historical, predicted, or preventive.
4. Resolve product-defined severity, priority, and on-call authority when applicable.
5. Record immediate safety, security, data, or rollback constraints.

**Gate:** no action route from an unqualified or anonymous material signal.

### Phase 2 — Establish bounded maintenance case

Create:

```yaml
maintenance_case_record:
  case_id: string
  signal_class: string
  active_incident: true | false | not_verified
  subject_refs: []
  environment_refs: []
  problem_statement: string
  expected_outcome: string
  evidence_refs: []
  assumptions: []
  unknowns: []
  owner_role: string
  authority_refs: []
  documentation_impact: pending | required | not_applicable | not_verified
  status: QUALIFYING | ROUTED | ACTIVE | VERIFYING | CLOSABLE | CLOSED | BLOCKED
```

The case scope must be bounded enough to close even though observation continues.

### Phase 3 — Prepare routing input

Produce evidence-backed input for `workflow-router`:

```text
active incident
  → incident-response standalone capability

verified non-active defect or regression
  → bugfix-workflow

approved improvement or new capability
  → new-feature-workflow

unknown design deficiency
  → design-audit

known narrow design failure
  → design-refinement

broad design direction replacement
  → redesign-workflow

release, deploy, rollback, or environment delivery action
  → deployment-workflow

review-only request
  → code-review-workflow or applicable domain review

product value uncertainty or metric movement
  → product-development product-validation / experiment composition

documentation-only correction
  → documentation-assurance under verified governing context

technical debt finding
  → technical-debt-governance, then workflow-router if code change is approved

unqualified signal
  → BLOCKED or further investigation; no guessed route
```

This table is adapter-local composition. It does not redefine the canonical Core route taxonomy.

### Phase 4 — Link governing execution

After `workflow-router` selects one primary route:

1. preserve the maintenance case ID in issue, branch, PR, run, review, deployment, and documentation evidence;
2. attach only justified specialists and overlays;
3. preserve authority and accepted-risk records;
4. use `task-continuity` for checkpoints and handoffs;
5. require `documentation-assurance` before closure when documentation impact is material or not verified.

The facade does not perform the selected workflow's implementation or review.

### Phase 5 — Verify actual outcome

Closure evidence must match the case outcome:

```text
incident
  actual service restoration, mitigation, resolution criteria, postmortem and actions

defect
  reproduction no longer fails for the expected reason, regression and affected suites pass

deployment/configuration
  actual target environment and candidate health are verified

performance/reliability/cost/data
  relevant measured signal returns to or reaches the accepted threshold

user/product signal
  engineering action is distinct from reviewed product-value evidence

documentation drift
  actual source is corrected, verified, and reviewed

preventive maintenance
  planned action executed, verified, and residual risk recorded
```

Provider success, green CI, merged code, or a written plan alone does not prove the actual maintenance outcome.

### Phase 6 — Close or continue

A bounded case may close only when:

- expected outcome has direct evidence or an explicit non-pass status;
- governing workflow and actions are traceable;
- required reviews and authorization states are recorded;
- documentation impact is reconciled;
- residual risk, recurrence, problem-management, and backlog actions have owners;
- exactly one next eligible action or observation owner is named.

Allowed closure verdicts:

```text
CLOSED_RESOLVED
CLOSED_WITH_FOLLOWUP
PARTIALLY_COMPLETED
NOT_VERIFIED
BLOCKED
CANCELLED
SUPERSEDED
```

`CLOSED` does not mean the product stops being observed.

## Output contract

```yaml
maintenance_case_report:
  case_record: {}
  signal_assessment:
    primary_class: string
    active_incident: true | false | not_verified
    confidence: HIGH | MEDIUM | LOW | NOT_VERIFIED
    evidence_refs: []
    gaps: []
  routing_input:
    requested_outcome: string
    recommended_route_class: string
    primary_route_selected_by: workflow-router
    required_overlays: []
    required_reviewers: []
    route_blockers: []
  linked_execution_refs: []
  documentation_assurance_ref: string | not_applicable | not_verified
  outcome_evidence: []
  closure_verdict: CLOSED_RESOLVED | CLOSED_WITH_FOLLOWUP | PARTIALLY_COMPLETED | NOT_VERIFIED | BLOCKED | CANCELLED | SUPERSEDED
  residual_risks: []
  recurrence_or_problem_actions: []
  next_eligible_action: string
  next_owner: string
```

## Hard gates

- [ ] Signal source, observed time, affected subject, environment/context, and expected outcome are explicit.
- [ ] Direct evidence, inference, assumptions, and unknowns remain distinct.
- [ ] Active incident status is explicit before choosing incident response.
- [ ] Maintenance-case recommendation never substitutes for `workflow-router` selection.
- [ ] Exactly one primary route is selected.
- [ ] Product-defined severity, thresholds, on-call, and action authority are preserved.
- [ ] The case ID links issue, execution, review, deployment, documentation, outcome, and follow-up evidence.
- [ ] Actual target outcome evidence is required before resolved closure.
- [ ] Provider success, CI, merge, plan, or local test alone is not generalized into operational or product success.
- [ ] Documentation impact is reconciled before closure.
- [ ] Residual risk and recurrence actions have owners.
- [ ] Bounded case closure remains separate from continuous observation.
- [ ] Closure does not synthesize merge, release, deployment, accepted-risk, or product acceptance authority.

## Failure classifications

| Finding | Meaning | Result |
|---|---|---|
| `SIGNAL_IDENTITY_MISSING` | Source, time, subject, or environment unresolved | `NOT_VERIFIED` |
| `ACTIVE_INCIDENT_NOT_CLASSIFIED` | Urgency and mitigation route are ambiguous | `BLOCKED` |
| `ROUTING_CONFLICT` | More than one primary route is asserted | `BLOCKED` |
| `ROUTER_BYPASSED` | Facade or specialist acts as primary router | `BLOCKED` |
| `OUTCOME_EVIDENCE_MISSING` | Resolution claimed without direct evidence | `NOT_VERIFIED` |
| `ENVIRONMENT_NOT_VERIFIED` | Delivery/provider result lacks target health evidence | `NOT_VERIFIED` |
| `DOCUMENTATION_GATE_OPEN` | Required documentation remains incomplete | `PARTIALLY_COMPLETED` or `BLOCKED` |
| `FOLLOWUP_OWNER_MISSING` | Residual risk or recurrence action is orphaned | `BLOCKED` |
| `FALSE_CLOSURE` | Case is marked resolved beyond available evidence | `NEEDS_WORK` |
| `AUTHORITY_CONFLATION` | Technical outcome is treated as approval/acceptance | `BLOCKED` |

## Handoff

```text
signal
→ maintenance-case qualifies and normalizes
→ workflow-router selects one primary route
→ role-switcher composes owner/specialists/reviewers
→ governing workflow executes and verifies
→ documentation-assurance reconciles documentation impact
→ maintenance-case evaluates bounded closure and follow-up
→ task-continuity preserves the next observation or action
```

## Capability evolution boundary

This MVP is an adapter-layer facade without a Core contract. After #251, promote only stable cross-adapter semantics supported by real product and maintenance cases.