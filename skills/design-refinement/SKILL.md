---
name: design-refinement
description: Bounded design correction workflow — consume an evidence-backed design-review result, lock accepted direction and passing regions, discover affected repository implementation conventions, patch within an explicit change budget, verify target, preservation, convention, and technical evidence, then run focused architecture/design re-review and learning promotion.
license: MIT
metadata:
  ai-native-skills.version: 2.2.1
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: workflow
  ai-native-skills.requires: "design-audit design-review master-design master-engineer implementation-context-discovery architecture-review skill-evolution skill-eval"
  ai-native-skills.implements: ai-native-core/contracts/workflows/design-refinement.contract.yaml
  ai-native-skills.contract-version: ^1.2.0
  ai-native-skills.related_skills: '["adaptive-component-design","redesign-workflow","ui-components","accessibility","readability","responsiveness","design-strategy","design-system","design-iconography"]'
---

# Design Refinement

## Reviewed core contract interface

Source: `ai-native-core/contracts/workflows/design-refinement.contract.yaml` · compatible line: `^1.2.0`

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

Keep this interface synchronized with the pinned core contract. Exact declarations make ownership reviewable; they do not replace rendered, runtime, accessibility, architecture, or product evidence.

Correct verified design failures without reopening the whole design or bypassing the repository's accepted implementation ecosystem.

This workflow owns refinement boundaries, preservation locks, change budgets, defect routing, targeted verification, focused re-review, and learning handoff. `implementation-context-discovery` owns pre-code repository mapping. `master-engineer` owns the patch. `architecture-review`, `design-review`, and governing domain reviewers own acceptance.

## Hard rules

```text
1. Begin from canonical FAIL or PARTIAL findings with sufficient reviewer coverage.
2. NOT_VERIFIED returns to evidence collection, not an invented patch.
3. Accepted direction and macrostructure must still be valid.
4. Declare target and preserve sets before editing.
5. Declare a change budget before editing.
6. Preserve passing gates, regions, component contracts, assets, content, behavior, unaffected contexts, and repository convention locks by default.
7. Diagnose pattern mismatch, system constraint, convention drift, dependency drift, and implementation defect separately.
8. Component substitution requires verified component-fitness reasoning.
9. Repository patches require implementation-context discovery for the affected capability families before code.
10. Reuse, bounded extension, composition, or semantic-native implementation precedes a new dependency proposal.
11. Every changed region, path, import, dependency, property, or behavior must map to a target finding or required dependency.
12. No drive-by redesign, re-theme, content rewrite, dependency migration, framework swap, or opportunistic cleanup.
13. Verify target gates, adjacent regressions, protected regions, affected convention locks, and reviewer-owned hard gates.
14. Run architecture-review for code patches and design-review for visual/design acceptance.
15. “Looks better,” “uses the right import,” and “build passes” are different evidence classes and cannot replace required review.
16. LIMITED or ROUTE_ELSEWHERE coverage cannot certify a specialist correction.
17. After two failed patches in one region, re-read and replan before another attempt.
18. Promote reusable knowledge only after the real artifact, preservation contract, convention locks, and governing reviews pass.
```

## Route decision

Use refinement when all are true:

```text
accepted direction remains valid
verified target findings are known
correction is bounded to a component, region, behavior, content, expression, or implementation layer
primary-domain coverage is BUILT_IN or ADAPTER_COVERED
passing work and canonical repository systems should remain stable
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

component strategy is fit but repository implementation mapping is missing
→ implementation-context-discovery before patch

accepted design cannot be satisfied by current canonical implementation systems
→ implementation-context-discovery CAPABILITY_GAP decision + required authority

fit canonical implementation was bypassed
→ CONVENTION_DRIFT; smallest repository-consistent correction

approved mapping is correct and code alone is broken
→ IMPLEMENTATION_DEFECT; local implementation owner

specialist-domain coverage is insufficient
→ required domain reviewer/specialist
```

A score or visible symptom alone never chooses the route.

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
    preserved_repository_conventions: []

  implementation_context:
    repository_ref: <ref or null>
    affected_capability_families: []
    profile_ref: <implementation_context_profile or null>
    convention_locks: []
    reuse_extension_decisions: []
    dependency_decisions: []
    implementation_mapping: []
    prohibited_parallel_systems: []
    evidence_gaps: []

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
   target regions, protected gates/regions/contracts/assets/behavior/conventions

3. DECLARE CHANGE BUDGET
   allowed files, regions, layers, properties, imports, dependencies,
   contract fields, expected side effects, rollback

4. DISCOVER IMPLEMENTATION CONTEXT
   for repository patches, inspect affected framework/component/styling/icon/
   state/form/query/data/build conventions and produce implementation mapping

5. DIAGNOSE DEFECT
   PATTERN_MISMATCH | CONTENT_PRESSURE | SYSTEM_CONSTRAINT |
   CONVENTION_DRIFT | DEPENDENCY_DRIFT | IMPLEMENTATION_DEFECT |
   LOCAL_VISUAL_DEFECT | DOMAIN_SPECIALIST_DEFECT

6. APPLY SMALLEST FIX
   correct owner and layer, inside budget and convention locks

7. VERIFY
   target gates, adjacent regressions, protected work, imports/dependencies,
   component-state equivalence, convention conformance, actual contexts

8. FOCUSED REVIEW
   architecture-review for code + design-review/governing reviewer for design

9. LEARNING REVIEW
   skill-evolution + skill-eval after verified reusable correction

10. DELIVER OR HAND OFF
   accepted, residual gap, redesign route, dependency authority,
   local owner, or specialist
```

Load `references/refinement-lock-and-change-budget.md` before the first edit and `implementation-context-discovery/references/verification-and-workflow-handoff.md` before repository patch production.

## Defect diagnosis

```text
PATTERN_MISMATCH
  selected component family is wrong for task/content/context
  → adaptive-component-design + master-design

CONTENT_PRESSURE
  realistic content exceeds component or layout contract
  → adaptive-component-design and possibly design-strategy

SYSTEM_CONSTRAINT
  canonical implementation system cannot satisfy the accepted design contract
  → implementation-context-discovery CAPABILITY_GAP decision

CONVENTION_DRIFT
  fit canonical component/utility/system was bypassed without evidence
  → implementation-context-discovery + local implementation owner

DEPENDENCY_DRIFT
  unapproved duplicate or parallel library/system was introduced
  → revert or route through dependency authority + architecture-review

IMPLEMENTATION_DEFECT
  selected design and repository mapping are correct, but code/artifact is broken
  → local implementation owner

LOCAL_VISUAL_DEFECT
  bounded hierarchy, readability, spacing, composition, or expression issue
  → relevant visual specialist

DOMAIN_SPECIALIST_DEFECT
  correction requires specialist-domain knowledge
  → governing domain reviewer/specialist
```

Visible symptoms do not choose the owner. Read the governing gate, component contract, and implementation-context profile first.

## Refinement lock

Protect by default:

```text
accepted direction and page macrostructure
passing gates and regions
component family and shared-state semantics
visual language and unaffected tokens
supplied content, assets, brand, and claims
unaffected responsive contexts and interaction states
canonical component/styling/icon/state/form/query/data/build systems
approved imports, aliases, wrappers, and module ownership
```

A protected item may change only when explicitly added to scope with required authority. Broad visual-system or implementation-system change triggers replan, redesign, migration, or feature routing.

## Change budget

```yaml
change_budget:
  allowed_regions: []
  allowed_files_or_artifacts: []
  allowed_component_contract_fields: []
  allowed_visual_properties: []
  allowed_behavioral_properties: []
  allowed_imports_or_shared_abstractions: []
  required_dependencies: []
  prohibited_parallel_systems: []
  expected_side_effects: []
  protected_or_forbidden_changes: []
  rollback_point: <ref>
```

Every mutation must map to a target finding or required dependency. Exceeding the budget blocks focused acceptance until reverted, explicitly approved, or rerouted.

## Component and repository corrections

When a cross-context component is involved, verify:

```text
actual available width and realistic content pressure
pattern-fitness diagnosis and adaptation boundary
selected value, choices, URL/query/filter state
change events and analytics identity
accessible relationships and focus behavior
loading/disabled/empty/error semantics
canonical component candidates and variants
shared primitives, tokens, icons, and state/form/query systems
expected imports and paths
prohibited parallel implementations
```

Do not replace a valid rail because one arrow is missing. Do not preserve tabs when realistic content proves the component family unfit. Do not build a local dropdown when the fit canonical selector already owns the required behavior.

## Before/after proof

```yaml
before_after_change_manifest:
  baseline_ref: <ref>
  refined_ref: <ref>
  changed:
    - region_or_path: <value>
      target_finding: <gate id>
      properties_contract_fields_imports_or_dependencies: []
      budget_status: <IN_BUDGET | REQUIRED_DEPENDENCY | OUT_OF_BUDGET>
  preserved:
    - region_or_contract: <value>
      evidence_before: <reference>
      evidence_after: <reference>
      status: <PRESERVED | REGRESSED | NOT_VERIFIED>
  component_contract_delta: <none or explicit delta>
  implementation_context_delta: <none or explicit delta>
  budget_status: <PASS | EXCEEDED | NOT_VERIFIED>
```

No visible screenshot change is insufficient when behavior, state, semantics, responsive contexts, imports, dependencies, or shared conventions could have changed.

## Verification

Collect only applicable evidence:

```text
digital interface
  affected target/boundary widths, themes, states, inputs,
  focus/semantics, overflow, runtime, realistic content

static visual
  final size, destination context, crop/safe area,
  content/asset fidelity, export quality

presentation or specialist domain
  governing reviewer evidence contract

repository patch
  effective diff, changed-file mapping, import/dependency audit,
  implementation-context conformance, relevant technical checks,
  rendered/runtime evidence when output or behavior changed,
  architecture-review
```

Always recheck:

```text
target and adjacent regression gates
preserved gates, regions, component contracts, and shared state
preserved convention locks and prohibited parallel systems
affected reviewer-owned hard gates
new evidence gaps and change-budget status
```

## Focused review route

```yaml
review_route:
  design_domain: <inherited>
  surface_profile: <inherited>
  artifact_state: <current>
  review_depth: focused
  coverage_mode: <inherited>
  domain_reviewers: <inherited>
  architecture_review: <required for code patch | not applicable>
  selected_gates: <target + adjacent regression gates>
  selected_components: <affected components>
  implementation_context_ref: <profile/mapping>
  evidence_available: <focused verification packet>
```

```text
PASS
  target, preservation, convention, architecture, and applicable design contracts pass

CONDITIONAL PASS
  only explicit non-blocking gaps outside the required boundary with authority

NEEDS WORK
  continue bounded loop

CRITICAL
  stop and route to redesign, migration/dependency authority, emergency local fix, or specialist

LIMITED REVIEW / ROUTE ELSEWHERE / NOT_VERIFIED
  load reviewer, collect evidence, or narrow the claim
```
