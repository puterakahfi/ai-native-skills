---
name: implementation-context-discovery
description: Discover an existing repository's implementation ecosystem before code production. Maps canonical frameworks, real component and variant coverage, registry availability, typography roles, styling, icons, utilities, state/form/query/data tooling, and build/test conventions; then selects semantic-native use, reuse, extension, composition, canonical registry addition, product-specific implementation, or an evidence-backed dependency candidate.
license: MIT
metadata:
  ai-native-skills.version: 1.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/engineering/implementation-context-discovery.contract.yaml
  ai-native-skills.contract-version: ^1.1.0
  ai-native-skills.boundary.covers: '["repository_implementation_ecosystem_discovery","canonical_framework_runtime_and_tooling_classification","component_system_shared_utility_variant_and_registry_inventory","component_capability_coverage_mapping","typography_role_and_token_mapping","semantic_native_eligibility_mapping","styling_token_and_iconography_implementation_mapping","state_form_query_data_and_build_test_tooling_mapping","repository_convention_lock_definition","reuse_extension_composition_registry_native_or_dependency_decision","capability_gap_and_parallel_system_diagnosis","new_dependency_evidence_and_consequence_record","implementation_mapping_before_code_production","implementation_context_verification_planning"]'
  ai-native-skills.boundary.delegates: '["product_specific_component_implementation","design_pattern_or_component_fitness_selection","visual_style_brand_or_design_system_definition","runtime_behavior_visual_quality_or_accessibility_acceptance","architecture_compliance_acceptance_after_implementation","dependency_purchase_legal_or_licensing_approval","product_specific_migration_execution","backend_domain_or_business_policy","repository_write_or_merge_execution"]'
  ai-native-skills.related_skills: '["master-engineer","architecture-review","ui-components","design-system","design-iconography","design-typography","adaptive-component-design","new-feature-workflow","design-refinement","redesign-workflow","code-review-workflow"]'
---

# Implementation Context Discovery

```text
repository evidence
→ canonicality
→ component coverage + typography roles
→ convention locks
→ semantic-native precheck or component decision ladder
→ implementation mapping
→ code
→ independent architecture review
```

This skill discovers repository choices. It does not prescribe shadcn, Tailwind, Lucide, React, or another universal stack.

## Load when

- implementing a redesign, refinement, or feature in an existing repository;
- selecting, extending, composing, adding, or creating a component;
- mapping typography decisions to repository roles and tokens;
- considering a new component, icon, styling, state, form, query, table, animation, or validation dependency;
- multiple current, legacy, experimental, or migration systems coexist.

Do not load for a pure design artifact with no code boundary.

## Ownership

```text
implementation-context-discovery
  repository evidence, canonicality, component coverage,
  typography mapping, convention locks, pre-code mapping

adaptive-component-design / design-interaction
  component fitness and behavior

design-system / design-typography / design-iconography
  design meaning and expression

master-engineer or product adapter
  implementation

architecture-review
  independent post-implementation acceptance
```

## Hard rules

1. Inspect repository evidence before implementation.
2. Package presence or a component-system name alone does not prove canonicality or component availability.
3. Inspect actual source, exports, variants, stories/examples, representative usage, and ownership.
4. Map requested component capability coverage before creating a component.
5. Reuse a fit component or existing variant before local duplication.
6. Prefer bounded extension and canonical primitive composition before a product-specific or parallel system.
7. Check the accepted canonical registry when a component is absent locally.
8. Registry-generated source becomes repository-owned and must be reviewed.
9. Map typography families and semantic roles before creating route-local type scales.
10. Semantic HTML is valid when no richer shared interaction or product contract is needed.
11. Semantic structure does not authorize recreating canonical Dialog, Select, Tabs, Tooltip, Button, or similar behavior.
12. Do not mix component, icon, styling, typography, state, form, query, or data systems without evidence and authority.
13. A new dependency requires a proven capability gap, alternatives, consequences, ownership, and approval.
14. Source alignment does not prove component fitness, runtime, visual, interaction, or accessibility acceptance.
15. Unknown or conflicting context remains `NOT_VERIFIED`.

## Required evidence

```text
engineering contracts and ADRs
manifests, lockfiles, workspace and framework configuration
aliases and composition roots
component registry configuration
component source, exports, variants, stories, tests, and usage
canonical registry availability
font loaders, type tokens, semantic roles, and usage
styling configuration and semantic tokens
icon imports and wrappers
state, form, query, animation, table, and data patterns
build, lint, test, Storybook, examples, and fixtures
migration, deprecation, dependency, and approval policy
```

Load:

- `references/repository-evidence-and-canonicality.md` for evidence and status rules;
- `references/component-system-coverage-and-typography.md` for coverage, registry, semantic-native, and typography mapping;
- `references/reuse-extension-and-dependency-decisions.md` for decision records;
- `references/verification-and-workflow-handoff.md` before acceptance handoff.

## Procedure

### 1. Bound the question

Record `repository_ref`, `implementation_scope`, `target_surface`, `proposed_changes`, requested capabilities, preservation requirements, authority sources, and evidence gaps.

### 2. Classify repository systems

Use combined evidence:

```text
declared dependency or repository source
+ actual usage
+ repetition or shared ownership
+ repository convention
+ current engineering or architecture decision
```

Classify each material system as `canonical`, `accepted_but_local`, `migration_target`, `legacy`, `deprecated`, `experimental`, `transitive_only`, or `unknown`.

For source-copied systems such as shadcn/ui, inspect registry configuration, shared source, primitive imports, variants, `cn`, tokens, stories, and repeated imports. Do not require a marketing-name package.

### 3. Map component coverage and typography

For every requested capability, review installed components, variants, bounded extension, composition, canonical registry availability, semantic-native eligibility, and interaction/accessibility/token contracts.

Choose one coverage status:

```text
covered_by_existing_component
covered_by_existing_variant
covered_by_bounded_variant
covered_by_composition
available_from_canonical_registry
requires_product_specific_component
semantic_native_is_sufficient
proven_capability_gap
unknown
```

Map typography roles: page title, section title, subsection title, body, supporting text, label, metadata, and code.

### 4. Lock conventions

For each relevant family, record the selected system, canonicality status, preserve/extend/migrate policy, evidence, allowed extension points, forbidden parallel systems, scoped exceptions, and authority.

### 5. Select the implementation adapter

For structural/content needs, first evaluate semantic-native eligibility.

For interactive or system-owned capabilities, evaluate in order:

```text
1. existing canonical component or utility
2. existing canonical variant
3. bounded variant
4. canonical primitive composition
5. component from the canonical registry
6. product-specific component using canonical primitives
7. dependency candidate after a proven capability gap
```

### 6. Produce implementation mapping

```yaml
implementation_mapping:
  requirement: <requirement>
  coverage_status: <status>
  selected_decision: <semantic-native | reuse | reuse-variant | extend | compose | add-canonical-registry-component | product-specific | dependency-candidate>
  canonical_components_or_utilities: []
  canonical_variants: []
  canonical_registry_additions: []
  typography_roles: []
  canonical_tokens_or_styles: []
  canonical_icons_or_wrappers: []
  expected_paths_and_imports: []
  prohibited_parallel_implementations: []
  required_tests_and_runtime_evidence: []
  architecture_review_checks: []
```

The mapping must exist before code production.

### 7. Classify findings

```text
STACK_CONTEXT_MISSING
COMPONENT_COVERAGE_MISSING
CONVENTION_DRIFT
CAPABILITY_GAP
DEPENDENCY_DRIFT
IMPLEMENTATION_DEFECT
```

### 8. Verify and hand off

Verify imports, dependencies, coverage, variants, registry additions, primitive composition, typography roles, semantic-native sufficiency, and absence of parallel systems. Keep runtime, component-fit, visual, interaction, accessibility, performance, security, and architecture acceptance separate.

## Required output

```yaml
implementation_context_discovery:
  repository_evidence_inventory: []
  implementation_context_profile:
    framework_runtime_map: []
    component_system_map: []
    canonical_component_inventory: []
    component_capability_coverage_map: []
    component_variant_inventory: []
    typography_role_map: []
    semantic_native_eligibility_map: []
    styling_system_map: []
    iconography_implementation_map: []
    state_form_data_tooling_map: []
    workspace_build_test_map: []
  canonicality_decisions: []
  convention_locks: []
  reuse_extension_decisions: []
  official_registry_component_decisions: []
  new_dependency_decisions: []
  implementation_mapping: []
  convention_drift_findings: []
  evidence_gaps: []
  verification_plan: []
  handoff:
    component_fitness: adaptive-component-design
    interaction_behavior: design-interaction
    visual_typography_meaning: design-typography_or_design_owner
    product_implementation: master-engineer_or_product_adapter
    post_implementation_acceptance: architecture-review
```

## Stop conditions

Return `BLOCKED`, `PARTIAL`, or `NOT_VERIFIED` when coverage is missing, a fit component or variant is duplicated, a canonical registry option is skipped without evidence, a route invents a parallel typography system, semantic structure excuses duplicated interaction behavior, a parallel system is introduced casually, dependency authority is incomplete, or source-only evidence claims runtime acceptance.
