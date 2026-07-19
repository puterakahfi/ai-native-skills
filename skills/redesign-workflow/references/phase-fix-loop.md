# Phase 11–12 — Defect Classification, Scope Cleanup, Fix, Verify, and Learn

Use this reference after:

```text
design-review returns verified FAIL or PARTIAL findings
or scope_diff_report returns BLOCKED
```

`NOT_VERIFIED` returns to evidence collection unless a verified implementation defect prevents verification. Scope contamination is handled as a workflow integrity blocker, not forced into a design gate.

## Core loops

### Design finding

```text
facade finding
→ resolve governing reviewer and root cause
→ classify correction ownership
→ apply the smallest valid correction
→ verify the real case and preservation set
→ regenerate scope diff when repository files changed
→ focused facade re-review
→ run learning review after a verified reusable fix
```

### Scope contamination

```text
scope_diff_report BLOCKED
→ identify path, change type, causal owner, and preservation risk
→ restore, remove, split, or re-approve a true dependency
→ regenerate effective final diff
→ proceed to facade review only after scope PASS
```

Do not patch a shared skill merely because product implementation failed. Do not patch product code to hide a missing reviewer, unsupported claim, evidence gap, or contaminated branch.

## Finding, evidence gap, and scope blocker

```text
FAIL / PARTIAL
  verified design condition exists
  eligible for design-defect classification

NOT_VERIFIED
  relevant evidence is missing
  return to verification or narrow the claim
  do not score zero or invent a design fix

NOT_APPLICABLE
  no correction required

SCOPE BLOCKED
  final effective delivery diff violates confirmed scope
  correct the delivery boundary before passing review or merge claim
```

## Design defect record

For every failed or partial canonical gate:

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
  correction_owner: <skill, workflow, artifact, lock owner, or specialist>
  correction_scope: <smallest valid scope>
  verification_required: []
  preservation_checks: []
```

## Scope contamination record

For every `OUT_OF_SCOPE`, `UNKNOWN`, or preserved-path violation:

```yaml
scope_contamination:
  path: <path or artifact>
  change_type: <added | modified | deleted | renamed | binary | submodule>
  classification: <OUT_OF_SCOPE | UNKNOWN | PRESERVED_PATH_VIOLATION>
  baseline_ref: <ref>
  causal_owner: <owner or unknown>
  reason_not_in_scope: <reason>
  valuable_work_preservation: <branch, artifact, commit, or not applicable>
  correction_action: <restore | remove | split | re-approve dependency | handoff>
  approval_requirement: <none | spec re-approval | owner decision>
  verification_required:
    - regenerate scope_diff_report
```

Do not delete valuable unrelated work merely to clean the redesign. Preserve it in the rightful branch or artifact first.

## Design defect classes

### `reusable_skill_defect`

A reusable capability is missing or teaches materially wrong reasoning across contexts.

```text
candidate reusable rule → test on real artifact → verify → skill-evolution
```

### `reference_knowledge_defect`

The owning skill is correct but its on-demand detail, matrix, examples, or evidence guidance is incomplete or misleading.

### `workflow_orchestration_defect`

Route, role composition, delegation, phase order, scope capture, state, approval, evidence handoff, or reviewer loading is wrong.

The missing final-diff gate discovered during a real redesign is this class. The concrete product paths remain in the product run artifact; only the reusable scope reasoning is promoted.

### `local_implementation_defect`

Reusable rules are sufficient and repository/artifact implementation is wrong.

### `product_design_lock_defect`

Supplied brand, content, asset, component, behavior, path, or design-system locks conflict or cannot all be satisfied.

### `domain_specialist_defect`

Correction requires specialist knowledge owned by a domain reviewer or another specialist.

## Classification rules

```text
missing reusable decision factor across contexts
  → reusable_skill_defect

on-demand explanation or evidence matrix incomplete
  → reference_knowledge_defect

correct skill not loaded, phase misordered, baseline/scope not captured
  → workflow_orchestration_defect

CSS, framework, state, route, export, or repository-specific bug
  → local_implementation_defect

conflicting supplied identity, content, system, or path constraint
  → product_design_lock_defect

identity, packaging, motion, or other specialist correction
  → domain_specialist_defect

unrelated effective changed path
  → scope contamination record; do not invent a design gate
```

Visible symptoms do not determine ownership. Inspect provenance and the effective diff first.

## Resolve scope contamination safely

```text
unrelated added file
  → preserve elsewhere if valuable, then remove from effective diff

unrelated modification to existing file
  → restore baseline version or split the valid work

unrelated deleted file
  → restore it from baseline

true required dependency omitted from spec
  → document causal relationship and acceptance criterion
  → re-enter approval policy

unknown ownership
  → remain BLOCKED and hand off to repository owner

submodule pointer
  → verify exact target commit and explain why the redesign requires it
```

Branch history does not need rewriting merely to pass this gate. The effective final diff must be clean and reproducible.

## Apply the smallest correction

```text
preserve passing gates and accepted direction
change only the owning layer and affected scope
record every touched file, region, skill, or contamination entry
avoid drive-by redesign and opportunistic cleanup
avoid global rules derived from one product
retain rollback and unrelated-work preservation paths
```

A candidate shared rule is not shared knowledge until the real artifact passes.

## Verify by governing domain

Use `delegation-and-verification.md` and governing reviewer evidence rules.

```text
digital interface
  affected rendering, states, inputs, focus, overflow, runtime, implementation

visual communication
  final-size, crop, content/asset fidelity, export quality

presentation
  affected slide, narrative adjacency, delivery scale, data/source

brand identity
  marks/variants, geometry, small size, mono/inverse,
  lockup/application/reproduction evidence

other
  domain reviewer evidence contract
```

After any repository correction, also re-check:

```text
scope_diff_report
target gates
adjacent regression gates
preserved gates, paths, and locks
affected contextual hard gates
new evidence gaps
```

If verification fails, continue the bounded loop. Do not update shared knowledge from a failed attempt.

## Focused re-review

Invoke the facade with inherited route and fresh evidence only after scope integrity passes:

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
  exit when acceptance, preservation, and scope also pass

NEEDS WORK / CRITICAL
  iterate while bounded attempts remain

LIMITED REVIEW
  load reviewer or narrow claim; do not treat as fix success

ROUTE ELSEWHERE
  stop unsupported approval path
```

## Automatic learning review

After each verified reusable fix, run:

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

The learning review must capture before/after evidence and owner, extract why the fix worked, remove product names and paths, test transfer conditions and counterexamples, check duplicate knowledge, add/update regression eval, run contract checks, and record the write result honestly.

Do not promote an unverified idea, product-specific layout, unknown workaround, or specialist rule into the workflow by convenience.

## Iteration safety

```yaml
loop:
  iteration: 1
  max_iterations: 5
  active_design_defects: []
  active_scope_contamination: []
  target_gates: []
  preserved_gates: []
  local_patches: []
  learning_candidates: []
  learning_verdicts: []
  facade_verdict_history: []
  scope_status_history: []
```

Scope sanitation before facade review does not consume a design iteration unless it changes the redesigned artifact.

After two failed patches in the same region:

```text
1. Re-read the complete affected artifact and dependencies.
2. Reconfirm governing reviewer or causal owner.
3. Mark preserved and locked regions and paths.
4. Create a rewrite, split, or alternative-pattern plan.
5. Rewrite only when justified and approved.
6. Run full affected verification and scope diff.
```

Never apply a blind third micro-patch to the same region.

## Exit report

```yaml
correction_report:
  iterations: <N>
  final_scope_status: <PASS | BLOCKED | NOT_APPLICABLE>
  final_facade_verdict: <verdict>
  scope_contamination_resolved: []
  scope_contamination_remaining: []
  target_gate_progression: []
  preserved_gate_regressions: []
  local_implementation_patches: []
  product_lock_decisions: []
  specialist_handoffs: []
  learning_verdicts: []
  promotion_commits: []
  residual_findings: []
  evidence_gaps: []
  final_status: <ACCEPTED | SCOPE_BLOCKED | MAX_ITERATIONS_REACHED | LIMITED | ROUTED_ELSEWHERE>
```

The phase is incomplete when a verified reusable fix occurred but no learning-review verdict was recorded.
