# Phase 11–12 — Classify, Hand Off, Fix, Verify, and Learn

Use this reference after:

```text
design-review returns verified FAIL or PARTIAL findings
scope_diff_report returns BLOCKED
decision provenance or concurrency integrity blocks correction
```

`NOT_VERIFIED` returns to evidence collection unless a verified implementation defect prevents verification. Do not invent a design fix for missing evidence.

## Correction routes

```text
verified local or component finding + accepted direction remains valid
→ design-refinement with lock and change budget

local component family may be unfit
→ adaptive-component-design inside design-refinement

page direction, macrostructure, visual language, or multiple foundational clusters are wrong
→ redesign-workflow replan

implementation contract is correct but local code/artifact is broken
→ implementation owner under the refinement lock

scope/provenance/concurrency blocker
→ owning integrity contract, not a design score

specialist-domain correction
→ governing domain reviewer/specialist
```

## Finding status boundary

```text
FAIL / PARTIAL
  verified design condition exists
  eligible for diagnosis and correction

NOT_VERIFIED
  evidence is missing
  return to verification or narrow the claim

NOT_APPLICABLE
  no correction required

SCOPE BLOCKED
  effective delivery diff violates confirmed scope

PROVENANCE BLOCKED
  material decision source or authority is unresolved

CONCURRENT WRITE BLOCKED
  stable artifact cannot be established safely
```

## Defect record

For every verified failed or partial canonical gate:

```yaml
defect:
  canonical_gate_id: <id>
  governing_reviewer: <reviewer>
  status: <FAIL | PARTIAL>
  observation: <verified condition>
  evidence: []
  impact: <user, accessibility, fidelity, runtime, communication, or delivery>
  affected_region: <region>

  diagnosis: <PATTERN_MISMATCH | IMPLEMENTATION_DEFECT | CONTENT_PRESSURE |
              SYSTEM_CONSTRAINT | LOCAL_VISUAL_DEFECT | DOMAIN_SPECIALIST_DEFECT>
  existing_component_or_design_contract: <reference or none>
  existing_relevant_rule: <reference or none>
  correction_owner: <owner>
  correction_scope: <smallest valid scope>
  adjacent_regression_gates: []
  preservation_checks: []
  verification_required: []
```

Visible symptoms do not determine ownership.

## Diagnosis

```text
PATTERN_MISMATCH
  component family is unfit for task/content/context
  → adaptive-component-design + master-design

IMPLEMENTATION_DEFECT
  component contract is fit but rendering or behavior is broken
  → local implementation owner

CONTENT_PRESSURE
  realistic content exceeds the component/layout contract
  → adaptive-component-design and possibly design-strategy

SYSTEM_CONSTRAINT
  design-system primitive cannot satisfy the required contract
  → design-system/ui-components + implementation owner

LOCAL_VISUAL_DEFECT
  bounded hierarchy, readability, spacing, composition, or expression failure
  → relevant visual specialist

DOMAIN_SPECIALIST_DEFECT
  correction requires specialist-domain knowledge
  → governing specialist/reviewer
```

Do not replace a fit component merely to avoid fixing implementation. Do not preserve an unfit component because it already exists.

## Bounded refinement handoff

When the accepted direction remains valid, hand the defect to `design-refinement`:

```yaml
refinement_handoff:
  accepted_direction: <reference>
  design_domain: <domain>
  surface_profile: <profile>
  coverage_mode: <mode>
  domain_reviewers: []

  target_findings:
    - gate_id: <id>
      governing_reviewer: <reviewer>
      diagnosis: <class>
      region: <region>
      evidence: []

  refinement_lock:
    target_regions: []
    preserved_gate_ids: []
    preserved_regions: []
    preserved_component_contracts: []
    locked_content_assets_and_brand: []
    preserved_behavior_and_states: []
    protected_change_layers: []

  change_budget:
    allowed_regions: []
    allowed_files_or_artifacts: []
    allowed_component_contract_fields: []
    allowed_visual_properties: []
    allowed_behavioral_properties: []
    required_dependencies: []
    protected_or_forbidden_changes: []
    rollback_point: <ref>

  adjacent_regression_gates: []
  required_evidence: []
  expected_output:
    - before_after_change_manifest
    - preservation_evidence_report
    - focused_design_review_result
```

A vague “make it better” handoff is invalid.

## Component correction rules

For adaptive components, preserve or explicitly verify:

```text
component role and user task
actual available width and content contract
selected value and available choices
event semantics
URL/query/filter state
analytics identity
accessible relationships and focus behavior
loading/disabled/empty/error semantics
```

```text
rail is fit but left arrow is missing
→ IMPLEMENTATION_DEFECT
→ preserve rail contract
→ fix directional affordance state

30 searchable dynamic choices are forced into tabs
→ PATTERN_MISMATCH
→ adaptive component decision
→ preserve shared product state across variants
```

## Scope and integrity blockers

For `OUT_OF_SCOPE`, `UNKNOWN`, or preserved-path violations:

```yaml
scope_contamination:
  path: <path or artifact>
  change_type: <added | modified | deleted | renamed | binary | submodule>
  classification: <OUT_OF_SCOPE | UNKNOWN | PRESERVED_PATH_VIOLATION>
  baseline_ref: <ref>
  causal_owner: <owner or unknown>
  valuable_work_preservation: <branch, artifact, commit, or N/A>
  correction_action: <restore | remove | split | re-approve dependency | handoff>
  verification_required: [regenerate scope_diff_report]
```

Preserve valuable unrelated work in its rightful lifecycle before removing it from the redesign delivery.

For provenance or concurrent-write blockers, stop affected writes and follow the owning references. Do not hide those blockers inside a visual correction.

## Apply the smallest correction

```text
preserve passing gates and accepted direction
stay inside the refinement lock and change budget
change only the owning layer and affected scope
record every touched region/file/contract field
avoid drive-by redesign and opportunistic cleanup
retain rollback and unrelated-work preservation paths
```

A candidate reusable rule is not shared knowledge until the real artifact and preservation contract pass.

## Verification packet

After the correction, produce:

```yaml
focused_verification_packet:
  target_gate_results: []
  adjacent_regression_gate_results: []
  affected_hard_gate_results: []
  preservation_evidence: []
  before_after_change_manifest: <reference>
  change_budget_status: <PASS | EXCEEDED | NOT_VERIFIED>
  component_state_equivalence: <PASS | FAIL | NOT_APPLICABLE | NOT_VERIFIED>
  target_and_boundary_contexts: []
  scope_diff_status: <PASS | BLOCKED | NOT_APPLICABLE>
  evidence_gaps: []
```

By domain:

```text
digital interface
  affected rendering, target/boundary widths, states, input modes,
  focus, overflow, runtime, realistic content

visual communication
  final size, crop, content/asset fidelity, export quality

presentation
  affected slide, adjacent narrative, delivery scale, data/source

brand identity
  marks/variants, geometry, small size, mono/inverse,
  lockup/application/reproduction evidence

other
  governing domain reviewer evidence contract
```

Build success alone is not design verification.

## Focused facade re-review

Invoke `design-review` after applicable integrity gates pass:

```yaml
review_route:
  design_domain: <inherited>
  surface_profile: <inherited>
  artifact_state: <current>
  review_depth: focused
  coverage_mode: <inherited>
  domain_reviewers: <inherited>
  selected_gate_ids: <target and adjacent gates>
  selected_components: <affected components>
  evidence_available: <focused verification packet>
```

```text
PASS
  exit only when refinement lock, budget, preservation, and target gates pass

CONDITIONAL PASS
  only explicit non-blocking gaps outside the required refinement boundary

NEEDS WORK / CRITICAL
  continue bounded loop or re-route

LIMITED REVIEW / ROUTE ELSEWHERE
  load reviewer or narrow claim
```

A facade score cannot override exceeded change budget, preservation regression, or integrity blockers.

## Learning review

After each verified reusable correction:

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

Promote only generalized reasoning to the correct specialist owner. Keep product names, paths, accidental breakpoints, and raw case history local.

## Iteration safety

```yaml
loop:
  iteration: 1
  max_iterations: 5
  active_design_defects: []
  active_integrity_blockers: []
  target_gates: []
  preserved_gates: []
  refinement_locks: []
  change_budget_history: []
  facade_verdict_history: []
  learning_verdicts: []
```

After two failed patches in the same region:

```text
re-read the full component/artifact and dependencies
reconfirm diagnosis and governing owner
reconfirm protected regions and contracts
compare alternative pattern or rewrite plans
rewrite only when justified and approved
run full affected verification
```

Never apply a blind third micro-patch.

## Exit report

```yaml
correction_report:
  iterations: <N>
  final_scope_status: <PASS | BLOCKED | NOT_APPLICABLE>
  final_facade_verdict: <verdict>
  target_gate_progression: []
  diagnoses: []
  change_budget_status: <PASS | EXCEEDED | NOT_VERIFIED>
  changed_regions_and_files: []
  preserved_regions_and_contracts: []
  preservation_regressions: []
  component_contract_delta: <value>
  integrity_blockers_remaining: []
  learning_verdicts: []
  residual_findings: []
  evidence_gaps: []
  final_status: <ACCEPTED | BLOCKED | MAX_ITERATIONS_REACHED | LIMITED | ROUTED_ELSEWHERE>
```

The phase is incomplete when a correction is called accepted without a focused facade verdict, preservation evidence, and change-budget result.
