# Refinement Lock and Change Budget

Load this reference before editing an artifact during `design-refinement`.

The purpose is to prove that a focused correction changed only what the verified finding required while preserving accepted direction, passing regions, component contracts, content, assets, and unaffected behavior.

## Refinement lock

```yaml
refinement_lock:
  accepted_direction: <reference or summary>
  target_findings:
    - gate_id: <canonical id>
      governing_reviewer: <reviewer>
      status: <FAIL | PARTIAL>
      region: <region>
      evidence: []

  target_regions: []
  preserved_gate_ids: []
  preserved_regions: []
  preserved_component_contracts: []
  locked_content: []
  locked_assets: []
  locked_brand_and_tokens: []
  preserved_behavior_and_states: []

  allowed_change_layers: []
  protected_change_layers: []
  adjacent_regression_gates: []
  required_evidence: []
  rollback_point: <artifact/ref>
```

Protected by default:

```text
passing regions and gates
page macrostructure
visual language and token system
component family and shared state contract
content and supplied assets
unaffected responsive contexts
unaffected interaction states
```

A protected item may change only when it is explicitly added to the target scope and the lifecycle route remains valid.

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

Every changed file, region, component-contract field, visual property, or behavior must map to:

```text
a verified target finding
or
a necessary dependency with a documented causal relationship
```

The following exceed the budget unless explicitly approved and rerouted:

```text
page re-theme
new visual language
macrostructure replacement
unrelated typography or spacing changes
component substitution without verified pattern mismatch
content rewriting outside the target finding
opportunistic cleanup
new route, feature, or product behavior
```

## Diagnosis and correction ownership

```text
PATTERN_MISMATCH
  component family is wrong for the task or context
  → adaptive-component-design + master-design

IMPLEMENTATION_DEFECT
  component contract is correct, implementation is broken
  → local implementation owner

CONTENT_PRESSURE
  realistic content exceeds the contract
  → adaptive-component-design and possibly design-strategy

SYSTEM_CONSTRAINT
  design-system primitive cannot satisfy the contract
  → design-system/ui-components + implementation owner

LOCAL_VISUAL_DEFECT
  bounded hierarchy, spacing, readability, or expression failure
  → relevant specialist + implementation owner

DOMAIN_SPECIALIST_DEFECT
  correction requires specialist-domain knowledge
  → governing domain reviewer/specialist
```

Do not replace a component to avoid fixing a local defect. Do not preserve a component that is proven unfit for the task.

## Before/after manifest

```yaml
before_after_change_manifest:
  baseline_ref: <ref>
  refined_ref: <ref>

  changed:
    - region_or_path: <value>
      target_finding: <gate id>
      change_layer: <layer>
      properties_or_contract_fields: []
      rationale: <why required>
      budget_status: <IN_BUDGET | REQUIRED_DEPENDENCY | OUT_OF_BUDGET>

  preserved:
    - region_or_contract: <value>
      evidence_before: <reference>
      evidence_after: <reference>
      status: <PRESERVED | REGRESSED | NOT_VERIFIED>

  component_contract_delta:
    component_family_before: <value>
    component_family_after: <value>
    diagnosis: <class>
    shared_state_delta: <none or explicit change>
    semantics_delta: <none or explicit change>

  budget_status: <PASS | EXCEEDED | NOT_VERIFIED>
```

`PASS` requires all changes to be in budget or documented required dependencies, and every protected item to be preserved with suitable evidence.

## Adaptive component refinement

For cross-context components, preserve or verify:

```text
component role and task
selected value and available choices
event semantics
URL/query/filter state
analytics identity
accessible name and relationships
focus behavior
loading/disabled/empty/error semantics
```

When substitution is required, capture:

```text
verified PATTERN_MISMATCH or CONTENT_PRESSURE
actual available-width evidence
realistic content cases
substitution boundary
rejected alternatives
shared state-equivalence contract
```

## Focused verification packet

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
  evidence_gaps: []
```

A build or source diff does not replace rendered or interaction evidence when output behavior changed.

## Route escalation

```text
change budget can resolve the finding
  → continue refinement

component family is locally unfit but page direction remains valid
  → adaptive-component-design decision inside refinement

direction, macrostructure, visual language, or multiple foundational clusters must change
  → redesign-workflow

primary-domain coverage is LIMITED or ROUTE_ELSEWHERE
  → load specialist or narrow the claim

finding is NOT_VERIFIED
  → collect evidence, do not invent a patch
```

## Completion guard

```text
□ Target findings are verified FAIL or PARTIAL.
□ Accepted direction remains valid.
□ Target and preserve sets are explicit.
□ Change budget is declared before editing.
□ Component fitness diagnosis precedes substitution.
□ Every change maps to a finding or required dependency.
□ Protected regions and contracts have before/after evidence.
□ Adjacent and affected hard gates are rechecked.
□ Shared component state and semantics remain equivalent.
□ Focused facade verdict permits completion.
□ Out-of-budget changes are reverted, approved, or rerouted.
```
