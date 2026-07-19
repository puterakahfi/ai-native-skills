# Orchestration State and Decisions

Load this reference after the redesign route is selected. It owns durable workflow state, phase handoffs, integrity blocker precedence, approval behavior, and output contracts. Specialist design knowledge remains in the relevant port/reviewer references.

## Role composition

```yaml
role_composition:
  lifecycle_owner: redesign-workflow
  design_owner: master-design
  implementation_owner: null
  repository_write_owner: null
  decision_authority_owners: []
  specialists: []
  reviewer_facade: design-review
  domain_reviewers: []
  coverage_mode: null
```

```text
patch or executable prototype
  → implementation_owner: master-engineer or runtime equivalent
  → exactly one repository_write_owner at a time

digital-interface
  → built-in interactive reviewer

visual-communication
  → built-in static reviewer

presentation
  → built-in presentation reviewer

brand-identity
  → brand-identity-review when available; otherwise LIMITED/handoff

other
  → declared domain reviewer; otherwise LIMITED/ROUTE_ELSEWHERE
```

## Durable run state

```yaml
run:
  id: redesign-<id>
  state: initialized
  route: redesign
  iteration: 0
  max_iterations: 5
  output_mode: prototype
  approval_mode: spec-gated
  baseline_ref: <ref>

repository:
  branch: <branch or null>
  inspected_head: <sha or null>
  expected_head: <sha or null>
  stable_head: <sha or null>
  write_owner: <owner or null>
  head_sequence: []
  contention_cycles: 0

decisions:
  records: []
  authoritative_record_ids: []
  provenance_verdict: null
  conflicts: []
  unresolved_requirements: []

scope:
  products: []
  routes_or_surfaces: []
  allowed_paths: []
  allowed_change_types: []
  expected_generated_files: []
  expected_deletions: []
  preserved_paths: []
  preserved_routes: []
  out_of_scope: []

locks:
  brand: []
  design_system: []
  content: []
  assets: []
  behavior: []
  routes: []
  preserved_regions: []

roles:
  design_owner: <owner>
  implementation_owner: <owner or null>
  repository_write_owner: <owner or null>
  specialists: []
  reviewer_facade: design-review
  domain_reviewers: []

artifacts:
  route_decision: null
  role_composition: null
  decision_provenance_report: null
  delegation_plan: null
  preflight_report: null
  design_direction: null
  layered_redesign_plan: null
  value_alignment_report: null
  redesign_spec: null
  redesigned_artifact: null
  production_report: null
  verification_report: null
  scope_diff_report: null
  concurrency_report: null
  design_review_result: null
  defect_report: null
  fix_report: null
  learning_review: null
  delivery_manifest: null
```

Lifecycle states:

```text
initialized → routed → roles_composed → preflight_complete → direction_selected
→ plan_ready → spec_ready → awaiting_approval → producing → verifying
→ provenance_blocked | scope_blocked | concurrent_write_blocked | reviewing
→ classifying_defect → fixing → accepted → delivered
```

## Phase responsibilities

### Route, compose, initialize

Emit one lifecycle route and one explicit role composition. Capture baseline, branch, expected head, initial decision sources, confirmed scope, locks, and approval requirements before production.

### Preflight

Inspect complete available evidence, not only the visually interesting region:

```text
existing brand/product equity
content and information architecture
actual audience and task
trust and conversion requirements
surface density and interaction complexity
design system and framework
assets and production constraints
current effective diff
concurrent writers or automation
preserve/refine/replace candidates
evidence and decision-source gaps
```

### Direction, layered plan, and value alignment

Direction must compare alternatives and explain why rejected options are less fit. Mark each layer `preserve`, `refine`, `replace`, or `not_applicable`:

```text
strategy
foundation
structure
components
expression
interaction
content
implementation
```

Run `business-value-alignment` before decorative production. A change with no user, message, delivery, or business value should be narrowed or stopped.

### Spec confirmation

Run `decision-provenance` for every material scope, lock, dependency, override, ownership, or approval claim.

```text
provenance PASS
  → update the spec only inside the verified decision boundary

PROVENANCE_BLOCKED
  → preserve last verified scope/lock
  → stop dependent mutation

ROUTE_FOR_APPROVAL
  → pause the affected action
  → route to required authority
```

Lock:

```text
design domain and profile
direction and macrostructure rationale
changed and preserved layers
content and asset inventory
viewing contexts and required states
acceptance criteria and evidence
delegation and governing owners
baseline and allowed paths/routes/change types
expected outputs/deletions and preserved paths/routes
verified out-of-scope list
write owner and approval mode
```

A new route or feature absent from the approved baseline remains a scope expansion until a verified authoritative decision explicitly includes it.

### Production

Before every repository mutation:

```text
record expected head + intended paths + governing decision records
→ resolve actual head immediately before write
→ write only when actual == expected
→ on drift, inspect code delta and decision provenance before retry
```

Never force-push over uninspected concurrent work. Never replay a stale full-file body merely with a refreshed blob SHA.

### Verification

Patch verification must produce:

```text
decision_provenance_report
scope_diff_report
concurrency_report
domain verification evidence
preservation results
implementation checks required by the delivery boundary
```

All reports must reference the actual stable head or final artifact. Missing evidence remains `NOT_VERIFIED`.

### Review

Invoke the facade only after applicable provenance, scope, and concurrency integrity pass.

Facade output includes:

```text
design domain and loaded reviewers
canonical gate results
coverage mode
evidence coverage
primary-domain coverage
contextual hard-gate status
verdict and prioritized findings
scope limitations and handoff
```

### Defect, fix, and learning

```text
design FAIL/PARTIAL
  → canonical gate + governing reviewer + correction owner

NOT_VERIFIED
  → return to evidence collection or narrow claim

scope contamination
  → restore, remove, preserve-and-split, or obtain verified bounded approval

provenance conflict
  → stop dependent writes and route explicit supersession/approval

concurrent conflict
  → stop writes, declare one owner, or isolate a real lifecycle boundary
```

Apply the smallest valid correction. After a verified reusable fix, run `skill-evolution + skill-eval`.

## Delivery precedence

```text
PROVENANCE_BLOCKED / ROUTE_FOR_APPROVAL
  → no passing delivery for the affected claim

SCOPE_BLOCKED
  → restore, remove, split, or obtain verified dependency approval

CONCURRENT_WRITE_BLOCKED
  → stop writes and coordinate one owner/stable branch

CRITICAL / NEEDS WORK
  → fix while bounded attempts remain

LIMITED REVIEW / ROUTE ELSEWHERE
  → load reviewer, narrow claim, or hand off

PASS
  → only when provenance, scope, concurrency, acceptance, evidence,
    coverage, reviewer-owned hard gates, and preservation pass

CONDITIONAL PASS
  → only explicit non-blocking risks inside verified authority;
    contamination, missing approval, or write contention cannot be accepted as risk

MAX ITERATIONS REACHED
  → deliver best preserved attempt with explicit gaps; never label PASS
```

Average score and mergeability never override provenance, scope, concurrency, verdict, coverage, evidence gaps, hard gates, locks, or acceptance criteria.

## Approval policy

```text
autonomous
  no routine pause, but it never means inferred consent;
  provenance, destructive, irreversible, policy, or conflicting writes still stop

spec-gated
  pause when scope or direction materially differs from verified request/spec

patch-gated
  pause before repository patch or full-file rewrite

fully-gated
  pause before production, every patch, and full-file rewrite
```

Always require explicit verified authority for destructive/irreversible work, production-environment changes, user-content deletion, material scope expansion, lock removal, approval bypass, or unresolved owner conflict.

## Output contract

Always expose:

```text
route_decision
role_composition
decision_provenance_report
delegation_plan
loop_summary
delivery_manifest
```

When applicable:

```text
run_state
preflight_report
design_direction
layered_redesign_plan
value_alignment_report
redesign_spec
redesigned_artifact
production_report
verification_report
scope_diff_report
concurrency_report
design_review_result
defect_report
fix_report
learning_review
gap_report
```

## Final orchestration guard

```text
□ One lifecycle route and one role composition are active.
□ Baseline, decision records, confirmed scope, exclusions, and locks are captured.
□ Production and verification artifacts refer to the actual stable head.
□ Integrity blockers take precedence over facade delivery claims.
□ Every handoff names the next owner, required evidence, and safe preserved state.
□ Blocked or bounded attempts remain honestly labeled.
```
