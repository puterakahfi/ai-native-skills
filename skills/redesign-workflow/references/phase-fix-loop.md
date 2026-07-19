# Phase 11–12 — Defect Classification, Fix, Verify, and Learn

Use this reference after facade review returns verified `FAIL` or `PARTIAL` findings. `NOT_VERIFIED` returns to evidence collection unless a verified implementation defect prevents verification.

## Core loop

```text
facade finding
→ resolve governing reviewer and root cause
→ classify correction ownership
→ apply the smallest valid correction
→ verify the real case
→ focused facade re-review
→ run learning review after a verified reusable fix
```

Do not patch a shared skill merely because a product implementation failed. Do not patch product code to hide a missing reviewer, unsupported claim, or verification gap.

## Finding versus evidence gap

```text
FAIL / PARTIAL
  verified condition exists
  eligible for defect classification

NOT_VERIFIED
  relevant evidence is missing
  return to verification or narrow the claim
  do not score zero or invent a design fix

NOT_APPLICABLE
  no correction required
```

## Defect record

For every failed or partial gate:

```yaml
defect:
  canonical_gate_id: <id>
  governing_reviewer: <reviewer>
  status: <FAIL | PARTIAL>
  observation: <verified condition>
  evidence: []
  impact: <user, business, accessibility, fidelity, runtime, or delivery>
  affected_region: <region>
  existing_relevant_rule: <rule or none>
  defect_class: <class>
  correction_owner: <skill, workflow, product artifact, lock owner, or specialist>
  correction_scope: <smallest valid scope>
  verification_required: []
  preservation_checks: []
```

## Defect classes

### `reusable_skill_defect`

Use when a reusable capability is missing or teaches materially wrong reasoning across contexts.

```text
candidate reusable rule
→ test on real artifact
→ verify
→ promote through skill-evolution
```

### `reference_knowledge_defect`

Use when the owning skill is correct but its on-demand detail, matrix, examples, or evidence guidance is incomplete or misleading.

```text
candidate reference improvement
→ apply to real case
→ verify
→ promote after successful transfer check
```

### `workflow_orchestration_defect`

Use when route, role composition, delegation, phase order, state, approval, evidence handoff, or reviewer loading is wrong.

```text
patch orchestration
→ resume from safe phase
→ verify the complete affected path
```

### `local_implementation_defect`

Use when reusable rules are sufficient and the repository/artifact implementation is wrong.

```text
implementation owner patches local artifact
→ verify target and adjacent regressions
→ keep product-specific detail local
```

### `product_design_lock_defect`

Use when supplied brand, content, asset, component, behavior, or design-system locks are inconsistent, incomplete, or impossible to satisfy together.

```text
identify lock conflict
→ route to lock owner / user decision
→ do not silently override a lock
```

### `domain_specialist_defect`

Use when the correction requires specialist knowledge owned by the loaded domain reviewer or another unavailable specialist.

```text
route to governing domain specialist
→ do not copy specialist correction knowledge into workflow or facade
```

## Classification rules

```text
missing reusable decision factor across contexts
  → reusable_skill_defect

on-demand explanation/matrix incomplete
  → reference_knowledge_defect

correct skills not loaded or phases misordered
  → workflow_orchestration_defect

CSS/framework/state/route/export/repository-specific bug
  → local_implementation_defect

conflicting supplied identity/content/system constraints
  → product_design_lock_defect

identity/packaging/motion/other specialist correction
  → domain_specialist_defect

existing rule is clear but ignored
  → local implementation or orchestration; do not duplicate the rule
```

The visible symptom does not determine ownership. A misaligned logo variant may be a local file error, a broken identity master, or missing construction guidance; inspect provenance first.

## Apply the smallest correction

```text
preserve passing gates and accepted direction
change only the owning layer and affected scope
record every touched file/region/skill
avoid drive-by redesign
avoid global rules derived from one product
retain rollback path
```

A candidate shared rule is not shared knowledge until the real artifact passes.

## Verify by governing domain

Use `delegation-and-verification.md` and the governing reviewer evidence rules.

```text
digital interface
  affected rendering, states, inputs, focus, overflow, runtime, implementation

visual communication
  final-size, crop, content/asset fidelity, export quality

presentation
  affected slide, narrative adjacency, delivery scale, data/source

brand identity
  affected marks/variants, geometry, small size, mono/inverse,
  lockup/application/reproduction evidence

other
  domain reviewer evidence contract
```

Re-check:

```text
target gates
adjacent regression gates
preserved gates and locks
affected contextual hard gates
new evidence gaps
```

If verification fails, continue the bounded loop. Do not update shared knowledge from the failed attempt.

## Focused re-review

Invoke the facade with inherited route and fresh evidence:

```yaml
review_route:
  design_domain: <inherited>
  surface_profile: <inherited>
  review_depth: focused
  coverage_mode: <inherited>
  domain_reviewers: <inherited>
  selected_gate_ids: <target and adjacent gates>
  evidence_available: <fresh packet>
  evidence_gaps: []
```

Outcomes:

```text
PASS / permitted CONDITIONAL PASS
  exit correction loop when acceptance and preservation also pass

NEEDS WORK / CRITICAL
  iterate while bounded attempts remain

LIMITED REVIEW
  load reviewer or narrow claim; do not treat as fix success

ROUTE ELSEWHERE
  stop unsupported approval path
```

## Automatic learning review

After each verified fix, run:

```text
skill-evolution + skill-eval
```

Allowed learning verdicts:

```text
PROMOTED
EVAL_ONLY
LOCAL_ONLY
DUPLICATE
DEFERRED_UNVERIFIED
NOT_WRITTEN_READ_ONLY
```

The learning review must:

```text
capture before/after evidence and governing reviewer
extract why the correction worked
remove product names, paths, classes, and accidental breakpoints
classify the correct owner: specialist skill, reference, workflow,
contract, eval-only, product lock, or local implementation
test transfer conditions and counterexamples
check for duplicate existing knowledge
add/update a regression eval for promoted behavior
run relevant contract/eval checks when available
record commit/write result honestly
```

Do not promote:

```text
an unverified idea
an exact product-specific layout or selector
a workaround whose underlying reason is unknown
a specialist rule into the facade or workflow by convenience
```

## Iteration safety

```yaml
loop:
  iteration: 1
  max_iterations: 5
  active_defects: []
  target_gates: []
  preserved_gates: []
  local_patches: []
  learning_candidates: []
  learning_verdicts: []
  facade_verdict_history: []
```

After two failed patches in the same region:

```text
1. Re-read the complete affected file/artifact and dependencies.
2. Reconfirm governing reviewer and correction owner.
3. Mark preserved and locked regions.
4. Create a rewrite or alternative-pattern plan.
5. Rewrite only when justified and approval policy allows it.
6. Run the full affected verification strategy.
```

Never apply a blind third micro-patch to the same region.

## Exit report

```yaml
correction_report:
  iterations: <N>
  final_facade_verdict: <verdict>
  target_gate_progression: []
  preserved_gate_regressions: []
  local_implementation_patches: []
  product_lock_decisions: []
  specialist_handoffs: []
  learning_verdicts: []
  promotion_commits: []
  residual_findings: []
  evidence_gaps: []
  final_status: <ACCEPTED | MAX_ITERATIONS_REACHED | LIMITED | ROUTED_ELSEWHERE>
```

The phase is incomplete when a verified reusable fix occurred but no learning-review verdict was recorded.