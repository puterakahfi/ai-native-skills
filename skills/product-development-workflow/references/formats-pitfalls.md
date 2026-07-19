# Formats, Stop Points, Pitfalls, and Verification

## Stop Points

```text
after_discovery_recommendation
after_experiment_design
after_prd_draft
after_mvp_plan
after_technical_spec
before_release
after_post_launch_review
```

Rules:

```text
planning-only requests stop after the agreed planning artifact
full execution still stops at destructive or external side-effect boundaries
before_release is valid only after RELEASE_READY product acceptance
```

## Planning Mode

```text
PRODUCT DEVELOPMENT WORKFLOW
Mode: planning
Current phase: discovery | requirements | mvp_slice | technical_spec
Stop point: <stop point>

Opportunity:
- target users and job
- user value
- business value
- success metric
- evidence/assumption state

Recommended MVP:
- scope in/out
- included acceptance criteria
- experiment or implementation recommendation

Readiness:
- READY | NEEDS REVISION | BLOCKED
- blocking gaps

Next approval:
- <decision required>
```

## Implementation Mode

```text
PRODUCT DEVELOPMENT WORKFLOW
Mode: implementation
Current phase: implementation
Feature slice: <feature>
Acceptance criteria: <IDs>

Evidence:
- technical
- runtime/integration
- design route/verdict when applicable
- security/performance/accessibility when applicable

Code review: APPROVED | REQUEST CHANGES | BLOCKED
Scope drift: <none or required update>
Next: <feature slice | product acceptance | return path>
```

## Product Acceptance Mode

```text
PRODUCT ACCEPTANCE — <product / MVP>
PRD: <reference>
MVP scope: <reference>

Rows:
  PASS: <count>
  CONDITIONAL: <count>
  FAIL: <count>
  NOT_VERIFIED: <count>
  NOT_APPLICABLE: <count>

Reviewer coverage:
- code review
- design domain/coverage
- security
- performance
- accessibility
- operations

Hard gates: <status>
Release blockers: <list>
Accepted risks: <owner, expiry, mitigation>

RELEASE ELIGIBILITY: RELEASE_READY | NOT_READY
Next: release preparation | implementation/verification | required reviewer | scope change
```

## Execution Status

```text
PRODUCT DEVELOPMENT WORKFLOW
Mode: execution
Current phase: <phase>
Gate: PASS | FAIL | BLOCKED | NOT_READY | RELEASE_READY
Evidence:
- <tool output, test, URL, review verdict, commit, artifact, or matrix row>
Next phase or return path:
- <value>
Approval required:
- <value or none>
```

## Common Pitfalls

1. **Starting with code.** A vague product starts with discovery and PRD.
2. **Skipping non-goals.** Without them, MVP becomes the full-product fantasy.
3. **Losing criterion IDs.** Tasks, evidence, and acceptance cannot trace back reliably.
4. **Feature approval treated as product approval.** Phase 6 must reconcile the complete MVP.
5. **Green CI treated as release readiness.** CI proves only its observed technical scope.
6. **Screenshot treated as runtime proof.** Hidden states, keyboard, accessibility, and flow remain unverified.
7. **Missing domain reviewer hidden by universal score.** Required primary-domain coverage blocks release.
8. **Release artifacts written to bypass acceptance.** Notes and rollback cannot turn `NOT_READY` into `RELEASE_READY`.
9. **Deploy treated as launch.** Launch needs users, support, analytics, and feedback.
10. **No stop point.** Vague requests stop after PRD/MVP recommendation by default.
11. **Overloading one response.** Large product work remains phase-gated and evidence-backed.

## Verification Checklist

```text
□ discovery happened before PRD when opportunity was vague
□ PRD exists and is READY before technical spec
□ MVP scope is smaller than the full product
□ every in-scope criterion has a stable ID and evidence plan
□ technical spec tasks trace to criterion IDs
□ implementation uses new-feature-workflow boundaries
□ user-facing changes have rendered/exported evidence when required
□ every criterion has an acceptance-matrix status
□ code-review-workflow verdicts are APPROVED for required feature scope
□ required domain reviewers and hard gates are resolved
□ Phase 6 verdict is RELEASE_READY before release preparation
□ release has notes, version/tag, changelog, and rollback plan
□ deployment health is verified before launch
□ launch has support, analytics, monitoring, and feedback
□ post-launch learning updates the next PRD, experiment, or backlog
```