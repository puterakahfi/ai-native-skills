# Requirements and Evidence Traceability

Load this reference when writing requirements, acceptance criteria, metrics, or an evidence plan.

## Requirement writing rule

A product requirement states observable behavior or a verifiable product quality. It does not prescribe implementation unless an attributable constraint requires it.

Good:

```text
REQ-1: A non-technical user can generate an editable landing-page draft from supplied business information.
```

Not ready:

```text
Use Next.js server actions and PostgreSQL.
The feature should work correctly.
Improve the user experience.
```

The first statement is solution design unless it is a verified constraint. The others are not observable.

## Stable identifiers

Use product-defined formats, but keep identifiers stable inside one effective PRD.

```text
G-1       goal
MET-1     success or guardrail metric
S-IN-1    scope-in item
S-OUT-1   scope-out item
REQ-1     functional requirement
NFR-1     non-functional requirement
AC-1      acceptance criterion
EV-1      expected or observed evidence
RISK-1    risk
Q-1       open question
LC-1      launch criterion
```

Do not renumber accepted identifiers merely for presentation. Mark removed or deferred items rather than reusing their IDs for different meaning.

## Requirement record

```yaml
requirement:
  id: REQ-1
  statement: ""
  rationale: ""
  priority: MUST | SHOULD | COULD | PRODUCT_DEFINED
  source_refs: []
  traces_to_goals: []
  traces_to_scope: []
  acceptance_criteria: []
  verification_methods: []
  status: PROPOSED | ACCEPTED | DEFERRED | REMOVED | NOT_VERIFIED
```

Priority is a decision, not list position. Do not fabricate priority authority.

## Acceptance criteria

Use Given/When/Then or an equivalent observable form.

```yaml
acceptance_criterion:
  id: AC-1
  given: ""
  when: ""
  then: ""
  traces_to: [REQ-1]
  verification_method: automated_test | runtime_inspection | user_test | analytics | review | product_defined
  expected_evidence: ""
```

An acceptance criterion should define:

- relevant precondition or context;
- user/system action or trigger;
- observable result;
- error, permission, empty, or recovery behavior when material;
- trace to at least one requirement;
- a plausible verification method.

## Metrics and analytics

A measurable metric needs more than a label.

```yaml
metric:
  id: MET-1
  name: ""
  type: primary | activation | adoption | guardrail | learning
  target_or_threshold: ""
  measurement_method: ""
  measurement_window: ""
  source_or_event: ""
  confidence: low | medium | high
```

If a target is unknown, name it as `NOT_VERIFIED` and define the smallest evidence-gathering step. Do not convert an unknown target into an arbitrary number.

## Evidence states

```text
EXPECTED_EVIDENCE   planned proof not yet observed
OBSERVED_EVIDENCE   attributable output actually inspected
NOT_RUN             verification was defined but not executed
NOT_VERIFIED        source or result cannot be proven
FAIL                observed evidence contradicts the criterion
PASS                observed evidence satisfies the exact criterion and scope
```

Never label expected future evidence as `PASS`.

## Traceability matrix

Feature and Full Product PRDs should make the chain reviewable:

```yaml
traceability:
  - goal: G-1
    metrics: [MET-1]
    scope: [S-IN-1]
    requirements: [REQ-1]
    acceptance_criteria: [AC-1]
    verification:
      method: runtime_test
      expected_evidence: EV-1
      observed_evidence: NOT_RUN
```

The minimum required chain is:

```text
requirement → acceptance criterion → verification method/evidence
```

For a full evidence-driven PRD, prefer:

```text
source evidence/decision → goal → metric → scope → requirement
→ acceptance criterion → verification → evidence
```

## Analytics and evidence plan

```yaml
evidence_plan:
  analytics_events:
    - name: ""
      proves_metrics: []
      properties: []
      privacy_constraints: []
  verification_items:
    - criterion: AC-1
      method: ""
      environment: ""
      expected_evidence: ""
      reviewer: ""
  unresolved_evidence:
    - item: ""
      owner: ""
      next_action: ""
      blocking: true
```

Instrumentation detail belongs in downstream technical specification; the PRD owns what must be measured and why.

## Traceability failure rules

Return `NEEDS_REVISION` when:

- a requirement has no observable acceptance criterion;
- an acceptance criterion has no requirement trace;
- a metric has no target/threshold and no explicit evidence-gathering action;
- acceptance depends on runtime behavior but no verification method exists;
- scope items cannot be linked to product goals or requirements;
- requirement IDs change meaning across a revision.

Return `BLOCKED` when the missing link depends on unresolved product authority, unavailable high-risk evidence, or a mandatory external constraint.
