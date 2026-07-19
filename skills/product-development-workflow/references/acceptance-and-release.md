# Product Acceptance and Release Eligibility

Load this reference during Phase 6 and Phase 7 of `product-development-workflow`.

Feature verification proves one implemented slice. Product acceptance proves the complete approved MVP satisfies every in-scope PRD acceptance criterion and is eligible to enter release preparation.

## Boundary

```text
new-feature-workflow
  feature-level scope, implementation, technical/rendered verification,
  submission, and code-review approval

product-development Phase 6
  product-level reconciliation of every MVP acceptance criterion,
  cross-feature behavior, reviewer coverage, evidence gaps, and release blockers

product-development Phase 7
  release artifacts after Phase 6 returns RELEASE_READY
```

A merged or approved feature does not automatically prove the complete MVP, cross-feature journey, operational requirement, or launch criterion.

## Acceptance Context

Record before scoring release readiness:

```yaml
acceptance_context:
  product: <product>
  prd_version: <version or reference>
  mvp_scope: <approved slice>
  technical_spec: <reference>
  implementation_refs: []
  code_review_verdicts: []
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
```

## Acceptance Evidence Matrix

Create one row for every in-scope PRD acceptance criterion.

```yaml
acceptance_matrix:
  - criterion_id: AC-01
    criterion: <observable expected outcome>
    affected_domains: [logic, user_facing_design]
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
  verified scope passes and only an explicit non-blocking risk remains

FAIL
  direct evidence proves the criterion is not satisfied

NOT_VERIFIED
  evidence or reviewer coverage cannot prove the criterion

NOT_APPLICABLE
  criterion/domain does not apply to the approved MVP slice
```

Rules:

```text
one in-scope criterion → one matrix row
evidence must match the criterion and affected domain
NOT_VERIFIED is release-blocking unless scope is formally changed
accepted risk cannot override a hard-gate failure
accepted risk cannot replace a missing primary-domain reviewer
one evidence item may support several rows, but each row keeps its own status
```

## Evidence Selection

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

Route changed user-facing scope through the `design-review` facade with:

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

Required evidence depends on affected criteria and may include:

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
specialized domain reviewer when the primary domain requires one
```

### Specialized design domain

```text
BUILT_IN or ADAPTER_COVERED
  complete-domain acceptance may be evaluated

LIMITED REVIEW
  universal findings may be useful, but required complete-domain acceptance is blocked

ROUTE_ELSEWHERE
  stop and load the required domain reviewer
```

## Reviewer Reconciliation

Do not average unrelated reviewer verdicts into one vague score.

```text
code-review-workflow
  APPROVED        → implementation review requirement passes
  REQUEST CHANGES → affected rows remain FAIL/NOT_VERIFIED
  BLOCKED         → acceptance remains blocked

design-review
  PASS             → design portion may pass
  CONDITIONAL PASS → only explicit non-blocking risks may remain
  NEEDS WORK       → affected rows FAIL; release blocked
  CRITICAL         → acceptance blocked
  LIMITED REVIEW   → complete required domain acceptance blocked
  ROUTE ELSEWHERE  → reviewer coverage blocked
security/performance/accessibility
  map direct findings to the affected criterion rows and hard gates
```

When several findings share one root cause, describe the root cause once but retain each criterion's independent acceptance status.

## Release Eligibility

After all rows are reconciled, issue one product-level verdict.

### RELEASE_READY

All conditions must hold:

```text
all in-scope rows are PASS or permitted CONDITIONAL
no release-blocking FAIL or NOT_VERIFIED row remains
all applicable hard gates pass
all required feature/code reviews are APPROVED
primary-domain reviewer coverage is complete for required claims
security, performance, accessibility, and operational evidence exists when applicable
accepted risks are explicit, non-blocking, owned, and time-bounded
```

### NOT_READY

Any condition is sufficient:

```text
an in-scope row is FAIL or release-blocking NOT_VERIFIED
code-review-workflow is REQUEST CHANGES or BLOCKED
required design verdict is NEEDS WORK, CRITICAL, LIMITED REVIEW, or ROUTE ELSEWHERE
an applicable hard gate fails
required reviewer or evidence is missing
accepted risk is used to hide a blocker
```

Release notes, version tags, changelogs, and rollback plans do not convert `NOT_READY` into `RELEASE_READY`.

## Release Handoff

Only after `RELEASE_READY`, produce:

```yaml
release_handoff:
  acceptance_verdict: RELEASE_READY
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

Phase 7 may prepare release artifacts, but deployment still requires `deployment-workflow` health and rollback gates.

## Product Acceptance Report

```text
PRODUCT ACCEPTANCE — <product / MVP>
────────────────────────────────────
PRD: <reference>
MVP scope: <reference>

Acceptance rows:
  PASS: <count>
  CONDITIONAL: <count>
  FAIL: <count>
  NOT_VERIFIED: <count>
  NOT_APPLICABLE: <count>

Required reviewers:
  Code review: <verdicts>
  Design domain/coverage: <route and verdict>
  Security: <verdict or N/A>
  Performance: <verdict or N/A>
  Accessibility: <verdict or N/A>

Hard gates: <passed / failed / not verified>
Release blockers: <list or none>
Accepted risks: <owned, expiry, mitigation>

RELEASE ELIGIBILITY: RELEASE_READY | NOT_READY
Next: release preparation | return to implementation/verification | load reviewer
```

## Anti-Patterns

| Anti-pattern | Correct behavior |
|---|---|
| Every PR merged, therefore product accepted | Reconcile all PRD criteria and cross-feature behavior |
| Tests green, therefore visual flow passed | Collect domain-appropriate rendered evidence |
| Screenshot proves runtime/accessibility | Mark unsupported behavior NOT_VERIFIED |
| Universal score approves an identity system | Require the primary-domain reviewer |
| One average hides a hard failure | Report hard gates and criterion status separately |
| Release notes written before acceptance | Release preparation starts only after RELEASE_READY |
| Risk accepted without owner or expiry | Make risk explicit, bounded, and non-blocking |
