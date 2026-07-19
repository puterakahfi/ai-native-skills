# Product Acceptance and Release Boundary

Load this reference during Phase 6 and Phase 7 of `product-development-workflow`.

Feature verification proves one implemented slice. Product acceptance proves the complete verified MVP satisfies every in-scope PRD criterion. Release approval determines whether the accepted candidate may proceed under product policy.

## Boundary

```text
new-feature-workflow
  feature-level verified scope, implementation, evidence,
  technical review, and merge authorization

product-development Phase 6
  product-level reconciliation of every verified MVP criterion,
  cross-feature behavior, reviewer coverage, evidence gaps,
  accepted-risk authority, and release blockers

product-development Phase 7
  release preparation only after RELEASE_READY
  and the required release approval is resolved
```

A merged feature does not automatically prove complete MVP acceptance, release readiness, or release permission.

## Acceptance context

```yaml
acceptance_context:
  product: <product>
  prd_version: <effective verified version>
  mvp_scope: <effective verified scope>
  technical_spec: <reference>
  implementation_refs: []
  code_review_verdicts: []

  decision_provenance:
    report: <reference>
    authoritative_record_ids: []
    conflicts: []
    unresolved_requirements: []

  affected_domains:
    architecture: <true | false>
    logic: <true | false>
    data: <true | false>
    security: <true | false>
    user_facing_design: <true | false>
    generated_or_exported_visual: <true | false>
    performance: <true | false>
    accessibility: <true | false>
    operations: <true | false>

  required_reviewers: []
  available_reviewers: []
  accepted_risk_policy: <product policy>
  release_approval_policy: <product policy>
```

Run `decision-provenance` before treating any PRD/MVP version, scope removal, accepted risk, or release approval as authoritative.

## Acceptance evidence matrix

Create one row for every criterion in the effective verified MVP scope.

```yaml
acceptance_matrix:
  - criterion_id: AC-01
    criterion: <observable expected outcome>
    affected_domains: [logic, user_facing_design]
    decision_record_ids: [DEC-MVP-01]
    evidence_required:
      - type: interaction
        context: <flow, viewport, input, state>
      - type: test
        context: <test boundary>
    evidence_available:
      - <direct evidence reference>
    evidence_gaps: []
    governing_reviewers:
      - code-review-workflow
      - design-review/built-in-interactive
    reviewer_verdicts:
      code_review: APPROVED
      design_review: PASS
    status: PASS
    release_blocking: false
    accepted_risk: null
```

Allowed row statuses:

```text
PASS
  direct evidence verifies the complete in-scope criterion

CONDITIONAL
  verified scope passes and only a verified non-blocking risk remains

FAIL
  direct evidence proves the criterion is not satisfied

NOT_VERIFIED
  evidence, reviewer coverage, or decision provenance is insufficient

NOT_APPLICABLE
  criterion/domain does not apply to the effective verified MVP slice
```

Rules:

```text
one in-scope criterion → one matrix row
evidence must match the criterion and affected domain
NOT_VERIFIED blocks release readiness
accepted risk cannot override a failed hard gate
accepted risk cannot replace a missing primary-domain reviewer
scope removal or NOT_APPLICABLE reclassification requires verified product authority
one evidence item may support several rows, but each row keeps its own status
```

## Decision provenance checks

Verify claims such as:

```text
“AC-07 was removed from scope”
“the owner accepted this risk”
“the latest PRD supersedes the approved version”
“all feature PRs merged, so the MVP is ready”
“release notes mean release is approved”
```

```text
verified authoritative source covers the exact scope/action
  → use the decision record

agent-authored document or status is the only support
  → NON_AUTHORITATIVE
  → preserve the last verified decision

implementation or merge state is the only support
  → OBSERVED_IMPLEMENTATION_STATE
  → proves state, not product acceptance or approval

conflicting authoritative sources lack explicit supersession
  → PROVENANCE_BLOCKED

another required approval remains
  → ROUTE_FOR_APPROVAL
```

## Accepted risk record

```yaml
accepted_risk:
  risk_id: <id>
  criterion_ids: []
  condition: <specific non-blocking condition>
  direct_evidence: []
  verified_non_blocking_reason: <reason>
  authority_record_id: <decision record>
  owner: <owner>
  mitigation: <action>
  expiry_or_review_date: <when required>
  status: <VERIFIED_ACCEPTED | PROVENANCE_BLOCKED | ROUTE_FOR_APPROVAL>
```

Accepted risk cannot hide missing evidence, a hard-gate failure, a required reviewer gap, or an unresolved scope decision.

## Evidence selection

### Technical behavior

Use direct evidence such as:

```text
unit/integration/contract/end-to-end tests
runtime or integration observation
migration or data verification
error and recovery behavior
security or threat evidence
performance measurements
operational health and rollback evidence
```

A green build does not prove untested product behavior.

### User-facing digital product

Route changed user-facing scope through `design-review`:

```yaml
design_acceptance:
  design_domain: digital-interface
  surface_profile: <web | mobile | desktop profile>
  artifact_state: <rendered-interactive | mixed | source-only>
  review_depth: release
  coverage_mode: <BUILT_IN | ADAPTER_COVERED | LIMITED | ROUTE_ELSEWHERE>
  domain_reviewers: []
  evidence_available: []
  evidence_gaps: []
```

Evidence may include:

```text
changed viewports and orientations
critical journey states
keyboard, pointer, touch, or gesture behavior
runtime and console health
accessibility semantics and focus
loading, empty, error, permission, success, and recovery states
realistic content and locked assets
```

A screenshot cannot prove runtime, keyboard operation, hidden states, or flow completion.

### Static/generated visual output

Use final-size/export evidence plus applicable fidelity and content checks:

```text
crop and safe-area
resolution and compression
logo/product/person fidelity
price/date/contact/claim accuracy
channel placement
specialized domain reviewer when required
```

### Specialized design domain

```text
BUILT_IN or ADAPTER_COVERED
  complete-domain acceptance may be evaluated

LIMITED REVIEW
  useful universal findings, but complete-domain acceptance blocked

ROUTE ELSEWHERE
  stop and load the required domain reviewer
```

## Reviewer reconciliation

Do not average unrelated reviewer verdicts.

```text
code-review-workflow
  APPROVED        → implementation review requirement passes
  REQUEST CHANGES → affected rows remain FAIL/NOT_VERIFIED
  BLOCKED         → acceptance remains blocked

design-review
  PASS             → design portion may pass
  CONDITIONAL PASS → requires verified non-blocking risk authority
  NEEDS WORK       → affected rows FAIL
  CRITICAL         → acceptance blocked
  LIMITED REVIEW   → complete required domain acceptance blocked
  ROUTE ELSEWHERE  → reviewer coverage blocked

other domain reviewers
  map direct findings to criterion rows and hard gates
```

Technical review approval does not self-authorize product release.

## Release eligibility

### RELEASE_READY

All conditions must hold:

```text
all in-scope rows are PASS or permitted CONDITIONAL
no release-blocking FAIL or NOT_VERIFIED remains
all applicable hard gates pass
all required code reviews are APPROVED
primary-domain coverage is complete
applicable domain evidence exists
accepted risks have verified authority and are non-blocking
PRD/MVP/scope decision provenance is PASS
```

### NOT_READY

Any condition is sufficient:

```text
an in-scope row is FAIL or release-blocking NOT_VERIFIED
code review is REQUEST CHANGES or BLOCKED
required design verdict is NEEDS WORK, CRITICAL, LIMITED REVIEW, or ROUTE ELSEWHERE
an applicable hard gate fails
required reviewer, evidence, or decision source is missing
accepted risk lacks verified authority
```

Release notes, version tags, changelogs, and rollback plans do not convert `NOT_READY` into `RELEASE_READY`.

## Release approval

```text
APPROVED
  RELEASE_READY
  + provenance PASS
  + all required product-policy approvals resolved

NOT_APPROVED
  NOT_READY
  or provenance blocked
  or required authority rejected the action

ROUTE_FOR_APPROVAL
  RELEASE_READY
  but another required authority has not decided
```

`RELEASE_READY` is a quality result. `APPROVED` is the permission result for the release action.

## Release handoff

Only after `RELEASE_READY` and approval resolution, produce:

```yaml
release_handoff:
  acceptance_verdict: RELEASE_READY
  release_approval: <APPROVED | ROUTE_FOR_APPROVAL>
  decision_record_ids: []
  prd_version: <reference>
  mvp_scope: <reference>
  acceptance_matrix: <reference>
  code_review_verdicts: []
  domain_review_verdicts: []
  accepted_risks: []
  release_notes: <reference>
  version_or_tag: <value>
  rollback_plan: <reference>
  deployment_readiness: <status>
```

When approval is `ROUTE_FOR_APPROVAL`, artifacts may be prepared, but no release action should be represented as completed.

## Product acceptance report

```text
PRODUCT ACCEPTANCE — <product / MVP>
────────────────────────────────────
PRD: <effective verified reference>
MVP scope: <effective verified reference>
Decision provenance: <verdict + record IDs>

Acceptance rows:
  PASS: <count>
  CONDITIONAL: <count>
  FAIL: <count>
  NOT_VERIFIED: <count>
  NOT_APPLICABLE: <count>

Required reviewers:
  Code review: <verdicts>
  Design domain/coverage: <route and verdict>
  Other domains: <verdicts or N/A>

Hard gates: <passed / failed / not verified>
Release blockers: <list or none>
Accepted risks: <authority, owner, mitigation, expiry>

RELEASE ELIGIBILITY: RELEASE_READY | NOT_READY
RELEASE APPROVAL: APPROVED | NOT_APPROVED | ROUTE_FOR_APPROVAL
Next: release preparation | approval route | return to implementation/verification
```

## Anti-patterns

| Anti-pattern | Correct behavior |
|---|---|
| Every PR merged, therefore product accepted | Reconcile all verified MVP criteria and cross-feature behavior |
| Agent-written PRD means scope approved | Verify attributable product authority |
| Criterion disappears from matrix | Require verified scope-removal decision |
| Tests green, therefore visual flow passed | Collect domain-appropriate rendered evidence |
| Screenshot proves runtime/accessibility | Mark unsupported behavior NOT_VERIFIED |
| Universal score approves specialist output | Require the primary-domain reviewer |
| Risk accepted without authority | Keep it blocked or route for approval |
| RELEASE_READY means release now | Separate quality readiness from release approval |
