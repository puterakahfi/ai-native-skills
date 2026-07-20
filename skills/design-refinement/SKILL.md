---
name: design-refinement
description: Bounded design correction workflow — consume an evidence-backed design-review result, lock accepted direction and passing regions, diagnose the owning defect, patch within an explicit change budget, verify target and preservation evidence, then run focused facade re-review and learning promotion.
license: MIT
metadata:
  ai-native-skills.version: 2.1.1
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: workflow
  ai-native-skills.requires: "design-audit design-review master-design skill-evolution skill-eval"
  ai-native-skills.implements: ai-native-core/contracts/skills/quality/design-refinement.contract.yaml
  ai-native-skills.contract-version: "^1.2.0"
  ai-native-skills.related_skills: '["adaptive-component-design","redesign-workflow","ui-components","accessibility","readability","responsiveness","design-strategy","master-engineer"]'
---

# Design Refinement

## Reviewed core contract interface

Source: `ai-native-core/contracts/skills/quality/design-refinement.contract.yaml` · compatible line: `^1.2.0`

```yaml
required_inputs:
- target_url_or_artifact
- prior_facade_review
- target_findings
- accepted_direction
- preservation_contract
allowed_outputs:
- refinement_route_decision
- refinement_lock
- component_fitness_or_defect_diagnosis
- change_budget
- targeted_patch_plan
- refined_artifact
- before_after_change_manifest
- gate_status_delta_report
- preservation_evidence_report
- adjacent_regression_report
- focused_review_result
- learning_candidate_report
- learning_promotion_report
- skill_patch_log
- regression_eval_result
- promotion_commit
- residual_gap_report
quality_gates:
- accepted_direction_must_be_explicit_and_still_valid
- target_findings_must_be_verified_FAIL_or_PARTIAL
- primary_domain_coverage_and_governing_reviewers_must_be_sufficient
- refinement_lock_and_change_budget_must_precede_patch
- passing_gates_regions_component_contracts_and_assets_are_preserved_by_default
- no_drive_by_redesign_retheme_or_opportunistic_cleanup
- diagnosis_distinguishes_pattern_mismatch_from_implementation_defect
- component_substitution_requires_verified_component_fitness_reasoning
- every_change_maps_to_target_finding_or_required_dependency
- before_after_manifest_and_preservation_evidence_are_required
- target_adjacent_preserved_and_affected_hard_gates_are_rechecked
- contextual_hard_gates_are_reviewer_owned_not_global
- focused_facade_verdict_controls_completion
- candidate_fix_must_be_verified_before_shared_learning_promotion
- every_verified_reusable_fix_has_a_skill_evolution_verdict
- every_promoted_shared_patch_has_regression_eval
- max_iterations_exit_includes_honest_gap_and_preservation_report
```

Expose the route decision, component-fitness or defect diagnosis, targeted patch plan, refined artifact, and gate-status delta explicitly. These outputs remain bounded by the refinement lock and preservation contract.

Keep this interface synchronized with the pinned core contract. Exact declarations make ownership reviewable; they do not replace rendered, runtime, accessibility, or product evidence.

Correct verified design failures without reopening the whole design.

This workflow owns the refinement boundary, preservation lock, change budget, defect routing, targeted verification, focused re-review, and learning handoff. The design-review facade and governing reviewers own gate meaning and acceptance. Specialist skills own narrow correction reasoning.

## Hard rules

```text
1. Begin from canonical FAIL or PARTIAL findings with sufficient reviewer coverage.
2. NOT_VERIFIED returns to evidence collection, not an invented design patch.
3. Accepted direction and page macrostructure must still be valid.
4. Declare target and preserve sets before editing.
5. Declare a change budget before editing.
6. Preserve passing gates, regions, component contracts, assets, content, behavior, and unaffected contexts by default.
7. Diagnose pattern mismatch separately from implementation defect.
8. Component substitution requires verified component-fitness reasoning.
9. Every changed region, file, property, or behavior must map to a target finding or necessary dependency.
10. No drive-by redesign, re-theme, content rewrite, or opportunistic cleanup.
11. Verify target gates, adjacent regressions, protected regions, and affected hard gates.
12. Re-review through design-review; “looks better” is not acceptance.
13. LIMITED or ROUTE_ELSEWHERE coverage cannot certify a specialist correction.
14. After two failed patches in one region, re-read and replan before another attempt.
15. Promote reusable knowledge only after the real artifact and preservation contract pass.
```

## Route decision

Use refinement when all are true:

```text
accepted direction remains valid
verified target findings are known
correction is bounded to a component, region, behavior, content, or expression layer
primary-domain coverage is BUILT_IN or ADAPTER_COVERED
passing work should remain stable
required evidence is obtainable
```

Route elsewhere:

```text
unknown findings or insufficient evidence
→ design-audit or verification

direction, macrostructure, visual language, or multiple foundational clusters are wrong
→ redesign-workflow

local component family may be unfit while page direction remains valid
→ adaptive-component-design inside the refinement loop

component contract is correct and implementation alone is broken
→ local implementation owner under the same refinement lock

specialist-domain coverage is insufficient
→ required domain reviewer/specialist
```

A score alone never chooses the route.

## Inputs

```yaml
refinement_input:
  target: <editable artifact, URL, or repository surface>
  prior_review: <design-review result>
  accepted_direction: <reference or summary>
  target_findings:
    - gate_id: <canonical id>
      governing_reviewer: <reviewer>
      status: <FAIL | PARTIAL>
      region: <region>
      evidence: []
  preservation_contract:
    preserved_gate_ids: []
    preserved_regions: []
    preserved_component_contracts: []
    locked_content_assets_and_brand: []
    preserved_behavior_and_states: []
  design_domain: <inherited>
  surface_profile: <inherited>
  coverage_mode: <inherited>
  domain_reviewers: []
  max_iterations: 3
```

## Canonical loop

```text
1. VALIDATE REVIEW STATE
   canonical findings, evidence, coverage, governing reviewers, accepted direction

2. DECLARE REFINEMENT LOCK
   target regions, protected gates/regions/contracts/assets/behavior

3. DECLARE CHANGE BUDGET
   allowed files, regions, layers, properties, contract fields, dependencies, rollback

4. DIAGNOSE DEFECT
   pattern mismatch | implementation defect | content pressure |
   system constraint | local visual defect | domain specialist defect

5. APPLY SMALLEST FIX
   correct owner and layer, inside budget

6. VERIFY
   target gates, adjacent regressions, protected work,
   component-state equivalence, contextual hard gates, actual contexts

7. FOCUSED FACADE RE-REVIEW
   inherited route, selected target + regression gates, fresh evidence

8. LEARNING REVIEW
   skill-evolution + skill-eval after verified reusable correction

9. DELIVER OR HAND OFF
   accepted, residual gap, redesign route, local owner, or specialist
```

Load `references/refinement-lock-and-change-budget.md` before the first edit.

## Defect diagnosis

```text
PATTERN_MISMATCH
  selected component family is wrong for task/content/context
  → adaptive-component-design + master-design

IMPLEMENTATION_DEFECT
  selected component contract is correct but code/artifact is broken
  → local implementation owner

CONTENT_PRESSURE
  realistic content exceeds component or layout contract
  → adaptive-component-design and possibly design-strategy

SYSTEM_CONSTRAINT
  design-system primitive cannot satisfy the required contract
  → design-system/ui-components + implementation owner

LOCAL_VISUAL_DEFECT
  bounded hierarchy, readability, spacing, composition, or expression issue
  → relevant visual specialist

DOMAIN_SPECIALIST_DEFECT
  correction requires specialist-domain knowledge
  → governing domain reviewer/specialist
```

Visible symptoms do not choose the owner. Read the full governing gate and component contract first.

## Refinement lock

Protect by default:

```text
accepted direction and page macrostructure
passing gates and regions
component family and shared-state semantics
visual language and unaffected tokens
supplied content, assets, brand, and claims
unaffected responsive contexts and interaction states
```

A protected item may change only if explicitly added to scope and the route remains refinement. A broad protected-layer change triggers replan or redesign routing.

## Change budget

```yaml
change_budget:
  allowed_regions: []
  allowed_files_or_artifacts: []
  allowed_component_contract_fields: []
  allowed_visual_properties: []
  allowed_behavioral_properties: []
  required_dependencies: []
  expected_side_effects: []
  protected_or_forbidden_changes: []
  rollback_point: <ref>
```

Every mutation must map to a target finding or required dependency. Exceeding the budget blocks focused acceptance until the excess is reverted, explicitly approved, or rerouted.

## Adaptive component corrections

When a cross-context component is involved, verify:

```text
actual available width
realistic option count and label pressure
pattern-fitness diagnosis
adaptation or substitution boundary
selected value and choices
URL/query/filter state
change events and analytics identity
accessible relationships and focus behavior
loading/disabled/empty/error semantics
```

Do not replace a valid rail merely because one arrow is missing. Do not preserve tabs when realistic content proves the component family unfit.

## Before/after proof

Produce:

```yaml
before_after_change_manifest:
  baseline_ref: <ref>
  refined_ref: <ref>
  changed:
    - region_or_path: <value>
      target_finding: <gate id>
      properties_or_contract_fields: []
      budget_status: <IN_BUDGET | REQUIRED_DEPENDENCY | OUT_OF_BUDGET>
  preserved:
    - region_or_contract: <value>
      evidence_before: <reference>
      evidence_after: <reference>
      status: <PRESERVED | REGRESSED | NOT_VERIFIED>
  component_contract_delta: <none or explicit delta>
  budget_status: <PASS | EXCEEDED | NOT_VERIFIED>
```

No visible change in a screenshot is insufficient when protected behavior, state, semantics, or responsive contexts could have changed.

## Verification

Collect only applicable evidence:

```text
digital interface
  affected target and boundary widths, themes, states, inputs,
  focus/semantics, overflow, runtime, realistic content

static visual
  final size, destination context, crop/safe area,
  content/asset fidelity, export quality

presentation
  affected slide, adjacent narrative, delivery scale, data/source integrity

brand identity or another specialist domain
  governing reviewer evidence contract

repository patch
  effective diff, changed-file mapping, relevant technical checks,
  rendered evidence when output changed
```

Always recheck:

```text
target gates
adjacent regression gates
preserved gates and regions
preserved component contracts and shared state
affected reviewer-owned hard gates
new evidence gaps
change-budget status
```

## Focused facade re-review

```yaml
review_route:
  design_domain: <inherited>
  surface_profile: <inherited>
  artifact_state: <current>
  review_depth: focused
  coverage_mode: <inherited>
  domain_reviewers: <inherited>
  selected_gates: <target + adjacent regression gates>
  selected_components: <affected components>
  evidence_available: <focused verification packet>
```

```text
PASS
  target and preservation contracts pass

CONDITIONAL PASS
  only explicit non-blocking gaps outside the required refinement boundary

NEEDS WORK
  continue bounded loop

CRITICAL
  stop and route to redesign, emergency local fix, or specialist

LIMITED REVIEW / ROUTE ELSEWHERE
  load reviewer or narrow the claim
```

## Learning review

After each verified reusable fix:

```text
skill-evolution + skill-eval
```

Promote only generalized reasoning to the correct owner. Product names, paths, accidental breakpoints, local class names, and raw case history remain local.

## Exit report

```yaml
refinement_result:
  design_domain: <domain>
  coverage_mode: <mode>
  target_gate_progression: []
  final_facade_verdict: <verdict>
  change_budget_status: <PASS | EXCEEDED | NOT_VERIFIED>
  changed_regions_and_files: []
  preserved_regions_and_contracts: []
  preservation_regressions: []
  component_contract_delta: <value>
  iterations: <N>
  evidence_packet: <reference>
  learning_verdicts: []
  residual_gaps: []
  handoff: <none | verification | local implementation | redesign | specialist>
```

The workflow is incomplete when target findings are called fixed without fresh focused review, when preservation lacks evidence, or when a verified reusable fix has no learning verdict.
