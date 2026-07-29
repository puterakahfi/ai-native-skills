# PRD Readiness Rubric

Load this reference for PRD review and before claiming an authored or revised PRD is ready.

## Upstream prerequisite

Before applying this rubric to a new authoring request, verify that the problem, target users, attributable intent, and sufficient upstream Discovery/Product Brief context exist. When they do not, route to `product-development-workflow` Discovery rather than evaluating a fabricated PRD.

## Status vocabulary

```text
PASS            applicable requirement is satisfied by inspectable artifact content
FAIL            artifact content contradicts or misses an applicable requirement
NOT_VERIFIED    evidence, source, target, or authority cannot be proven
NOT_APPLICABLE  domain does not apply and includes a credible rationale
```

Do not use `PASS` for planned future work, inferred approval, or uninspected evidence.

## Dimensions

### 1. Problem and evidence

Pass when the problem is an outcome rather than a proposed solution, affected users/current behavior are clear, upstream sources are referenced, and evidence, assumptions, unknowns, and confidence are separated.

### 2. Users and value

Pass when primary users are explicit, excluded users are named when material, and user/business value is attributable and not merely feature description.

### 3. Goals, metrics, and scope

Pass when goals are measurable outcomes, non-goals exist, metrics include targets or explicit evidence actions, and scope-in/out are both explicit.

### 4. Functional requirements

Pass when requirements have stable IDs, observable behavior, source/goal/scope traces, and avoid unreviewed implementation detail.

### 5. Non-functional requirements

Pass when relevant quality domains are specified and testable, or explicitly `NOT_APPLICABLE` with rationale.

### 6. Acceptance and traceability

Pass when each material requirement has verifiable acceptance criteria and the chain to verification method/evidence is reviewable.

### 7. Risks, dependencies, and unknowns

Pass when material constraints, dependencies, risks, assumptions, and open questions are explicit, with owners/next actions when attributable.

### 8. Analytics and evidence plan

Pass when claimed metrics and runtime acceptance have a plausible measurement/verification route, while future evidence is not represented as observed proof.

### 9. Launch readiness

Pass when launch criteria cover applicable product acceptance, domain reviews, analytics, observability, support, rollout/rollback, and known-risk handling—not only code completion.

### 10. Lifecycle and provenance

Pass when artifact identity/version/status, effective Product Brief or parent PRD sources, material revision changes, supersession, and approval boundaries are explicit where applicable.

## Verdict algorithm

```text
BLOCKED
  any mandatory PRD input is absent; or
  high-risk evidence/authority/dependency is NOT_VERIFIED; or
  a mandatory legal, security, privacy, safety, compliance, or scope-authority gate is unresolved

NEEDS_REVISION
  no hard blocker exists, but one or more applicable dimensions FAIL

READY
  all applicable dimensions PASS or have justified NOT_APPLICABLE status,
  no blocker exists, and missing non-blocking evidence is explicitly contained
```

`READY` never implies `APPROVED`.

## Profile-specific interpretation

### Feature PRD

All dimensions apply except product-level details that are credibly inherited from an effective Product Brief or parent PRD. Inherited decisions require references.

### Full Product PRD

All dimensions apply. A broad `NOT_APPLICABLE` claim requires stronger rationale than a narrow feature scope.

## Required review output

```yaml
prd_readiness:
  artifact_ref: ""
  effective_version: ""
  profile: FEATURE_PRD | FULL_PRODUCT_PRD
  verdict: READY | NEEDS_REVISION | BLOCKED
  dimensions:
    problem_and_evidence:
      status: PASS | FAIL | NOT_VERIFIED | NOT_APPLICABLE
      findings: []
    users_and_value:
      status: PASS | FAIL | NOT_VERIFIED | NOT_APPLICABLE
      findings: []
    goals_metrics_and_scope:
      status: PASS | FAIL | NOT_VERIFIED | NOT_APPLICABLE
      findings: []
    functional_requirements:
      status: PASS | FAIL | NOT_VERIFIED | NOT_APPLICABLE
      findings: []
    non_functional_requirements:
      status: PASS | FAIL | NOT_VERIFIED | NOT_APPLICABLE
      findings: []
    acceptance_and_traceability:
      status: PASS | FAIL | NOT_VERIFIED | NOT_APPLICABLE
      findings: []
    risks_dependencies_and_unknowns:
      status: PASS | FAIL | NOT_VERIFIED | NOT_APPLICABLE
      findings: []
    analytics_and_evidence_plan:
      status: PASS | FAIL | NOT_VERIFIED | NOT_APPLICABLE
      findings: []
    launch_readiness:
      status: PASS | FAIL | NOT_VERIFIED | NOT_APPLICABLE
      findings: []
    lifecycle_and_provenance:
      status: PASS | FAIL | NOT_VERIFIED | NOT_APPLICABLE
      findings: []
  blockers: []
  next_actions: []
  approval:
    status: VERIFIED | NOT_VERIFIED | ROUTE_FOR_APPROVAL
    authority_ref: ""
```

## Review discipline

- Cite exact sections, requirement IDs, criteria, or missing fields.
- Separate document-quality failure from missing external evidence.
- Do not silently repair a review-only artifact.
- Do not lower a gate because implementation already exists.
- Do not infer product acceptance from merged code, passing CI, or a newer document timestamp.
- Report one concrete next action for every blocker.
- Do not evaluate an upstream Product Brief as though it were a PRD; route it to its governing Discovery gate.

## Independent review lenses

When risk or scope warrants, route independent review to:

```text
product authority     intent, value, priority, scope, approval
engineering reviewer  feasibility constraints without rewriting product intent
design reviewer       experience coverage and acceptance implications
security/privacy      applicable trust, data, and abuse boundaries
QA/eval reviewer      testability, traceability, and evidence sufficiency
```

Reviewers provide evidence or findings; they do not silently take over product authority.
