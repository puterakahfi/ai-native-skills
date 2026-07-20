---
name: implementation-context-discovery
description: Discover and lock an existing repository's implementation ecosystem before code production. Maps canonical frameworks, component and styling systems, iconography, utilities, state/form/query/data tooling, and build/test conventions; then decides reuse, extension, composition, semantic-native implementation, or evidence-backed new dependency introduction.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/engineering/implementation-context-discovery.contract.yaml
  ai-native-skills.contract-version: ^1.0.0
  ai-native-skills.boundary.covers: '["repository_implementation_ecosystem_discovery","canonical_framework_runtime_and_tooling_classification","component_system_and_shared_utility_inventory","styling_token_and_iconography_implementation_mapping","state_form_query_data_and_build_test_tooling_mapping","repository_convention_lock_definition","reuse_extension_composition_native_or_dependency_decision","capability_gap_and_parallel_system_diagnosis","new_dependency_evidence_and_consequence_record","implementation_mapping_before_code_production","implementation_context_verification_planning"]'
  ai-native-skills.boundary.delegates: '["product_specific_component_implementation","design_pattern_or_component_fitness_selection","visual_style_brand_or_design_system_definition","runtime_behavior_visual_quality_or_accessibility_acceptance","architecture_compliance_acceptance_after_implementation","dependency_purchase_legal_or_licensing_approval","product_specific_migration_execution","backend_domain_or_business_policy","repository_write_or_merge_execution"]'
  ai-native-skills.related_skills: '["master-engineer","architecture-review","ui-components","design-system","design-iconography","adaptive-component-design","new-feature-workflow","design-refinement","redesign-workflow","code-review-workflow"]'
---

# Implementation Context Discovery

Inspect the repository before choosing how to implement.

```text
repository evidence
→ implementation context profile
→ canonicality decisions
→ convention locks
→ reuse / extend / compose / semantic-native / dependency decision
→ implementation mapping
→ implementation
→ independent architecture review
```

Frameworks, component libraries, styling systems, icon packages, form/state/query tools, and build systems are product adapters. This skill discovers which choices the repository currently accepts; it does not prescribe one universal stack.

## When to load

Load before code production or material code changes when:

- implementing a redesign or design refinement in an existing repository;
- adding a user-facing feature, shared component, route, module, integration, or reusable utility;
- choosing whether to reuse, extend, compose, or create a component;
- considering a new framework, component, icon, state, form, query, animation, table, validation, or styling dependency;
- a repository contains multiple competing or legacy implementation systems;
- design output must be mapped to the actual product implementation system;
- architecture review would otherwise be the first place stack drift is discovered.

Do not load for a pure design artifact with no code or repository implementation boundary.

## Ownership

```text
implementation-context-discovery
  owns repository evidence, canonicality, convention locks,
  implementation decision ladder, and pre-code mapping

master-engineer or product implementation owner
  owns actual code and product-specific composition

adaptive-component-design / design-interaction
  own component fitness and behavior decisions

design-system / design-iconography
  own design-system meaning and expressive iconography rules

architecture-review
  independently verifies the resulting implementation after code exists
```

This skill is not architecture approval and does not write code by itself.

## Hard rules

1. Inspect repository evidence before implementation.
2. Package presence alone does not prove canonical status.
3. Actual usage, repetition, shared ownership, repository convention, and current decisions matter together.
4. Distinguish canonical, migration target, legacy, deprecated, experimental, transitive-only, and unknown tooling.
5. Reuse a fit canonical component or utility before creating a local duplicate.
6. Extend or compose canonical primitives before introducing a parallel system.
7. Native semantic platform elements remain valid when no shared abstraction or richer contract is needed.
8. Do not reject native HTML merely because a component library exists.
9. Do not mix icon, component, styling, state, form, query, or data systems without evidence and authority.
10. A new dependency requires a proven capability gap, reviewed alternatives, consequences, ownership, and approval.
11. Newer, more popular, or agent-preferred tooling does not override repository decisions.
12. A migration target does not silently authorize mixed systems during ordinary feature work.
13. Source inspection may prove imports and configuration alignment; it cannot prove runtime, visual, interaction, or accessibility acceptance.
14. Preserve independent `architecture-review` after implementation.
15. Unknown or conflicting context remains `NOT_VERIFIED`; do not invent the stack.

## Required inputs

```text
repository_ref
implementation_scope
target_surface
proposed_changes
```

Collect applicable optional evidence:

```text
engineering contract and ADRs
package manifests and lockfiles
workspace and framework configuration
path aliases and composition roots
component registry/configuration
shared UI packages and source components
representative current imports and usage
styling configuration and semantic tokens
icon imports, wrappers, and usage
state, form, query, animation, table, and data patterns
build, lint, test, Storybook, examples, and fixtures
migration, deprecation, and replacement records
dependency and approval policy
preservation requirements
```

Load `references/repository-evidence-and-canonicality.md` for the evidence inventory and status rules.

## Procedure

### 1. Bound the implementation question

Record:

```yaml
implementation_question:
  repository_ref: <branch, commit, worktree, or source snapshot>
  implementation_scope: <feature, component, route, module, or patch>
  target_surface: <surface>
  proposed_changes: []
  preservation_requirements: []
  authority_sources: []
  evidence_available: []
  evidence_gaps: []
```

Do not inspect the whole ecosystem aimlessly. Start from the affected capability families, then inspect adjacent shared systems that can be changed or bypassed by the patch.

### 2. Inventory repository evidence

Inspect evidence, not package names alone.

```text
manifest/lockfile
  proves declared or resolved dependency presence

configuration
  proves selected framework, aliases, registry, tokens, or tooling setup

actual imports and repeated usage
  prove real implementation practice

shared package/component ownership
  proves intended reuse boundary

engineering contract or ADR
  proves declared authority and migration direction

legacy/deprecation evidence
  prevents stale dependencies from being treated as canonical
```

For source-copied component systems, inspect registry files, component source, primitive imports, variant utilities, class-composition utilities, and repeated import paths. Do not require a package with the component system's marketing name.

### 3. Classify canonicality

Every material capability family receives one status:

```text
canonical
accepted_but_local
migration_target
legacy
deprecated
experimental
transitive_only
unknown
```

Use combined evidence:

```text
declared dependency or repository source
+ actual usage
+ repetition or shared ownership
+ repository convention
+ current engineering/architecture decision
```

One signal alone is insufficient.

### 4. Declare convention locks

```yaml
convention_lock:
  capability_family: <family>
  selected_system: <system or native platform>
  status: <canonicality status>
  policy: <preserve | extend | migrate | unresolved>
  evidence: []
  allowed_extension_points: []
  forbidden_parallel_systems: []
  scoped_exceptions: []
  owner_or_authority: <source>
```

Applicable families include:

- application framework and UI runtime;
- component system and primitives;
- styling and semantic token system;
- iconography implementation family and wrappers;
- state, form, query, animation, table, and data tooling;
- routing, composition, build, lint, test, and story tooling;
- accessibility, security, and performance implementation patterns.

### 5. Apply the implementation decision ladder

Evaluate in order:

```text
1. reuse existing component or utility
2. reuse an existing variant
3. add a bounded variant to the canonical abstraction
4. compose canonical primitives
5. create a product-specific component using canonical primitives
6. use a semantic native platform element when no abstraction is needed
7. introduce a dependency only after a proven capability gap
```

Do not jump to option 7 because it is familiar or convenient.

Load `references/reuse-extension-and-dependency-decisions.md` for the comparison record and dependency gate.

### 6. Produce implementation mapping

Map design or feature intent to actual repository adapters.

```yaml
implementation_mapping:
  requirement: <requirement>
  owning_module_or_surface: <owner>
  selected_decision: <reuse | variant | extend | compose | product-specific | semantic-native | dependency-candidate>
  canonical_components_or_utilities: []
  canonical_tokens_or_styles: []
  canonical_icons_or_wrappers: []
  state_form_query_or_data_tools: []
  expected_paths_and_imports: []
  prohibited_parallel_implementations: []
  required_tests_and_runtime_evidence: []
  architecture_review_checks: []
```

This mapping is the engineering handoff. It must exist before code production.

### 7. Classify problems correctly

```text
STACK_CONTEXT_MISSING
  implementation started without sufficient repository context

CONVENTION_DRIFT
  a fit canonical abstraction was bypassed without evidence

CAPABILITY_GAP
  accepted systems cannot satisfy a proven requirement

DEPENDENCY_DRIFT
  an unapproved parallel or duplicate dependency was introduced

IMPLEMENTATION_DEFECT
  context and mapping were correct, but execution is broken
```

A native semantic element is not `CONVENTION_DRIFT` merely because a component library is present.

### 8. Verify and hand off

Load `references/verification-and-workflow-handoff.md`.

Verify:

- changed imports and dependencies match the mapping;
- reused or extended components preserve their contract;
- scoped custom components compose accepted primitives;
- native choices are semantically and behaviorally sufficient;
- no local parallel style, icon, state, form, query, or component system was created;
- new dependency approval and consequence records are complete;
- runtime, visual, interaction, accessibility, performance, and security claims use their governing evidence;
- `architecture-review` remains an independent post-implementation gate.

## Required output

```yaml
implementation_context_discovery:
  repository_evidence_inventory: []

  implementation_context_profile:
    framework_runtime_map: []
    component_system_map: []
    canonical_component_inventory: []
    styling_system_map: []
    iconography_implementation_map: []
    state_form_data_tooling_map: []
    workspace_build_test_map: []

  canonicality_decisions: []
  convention_locks: []
  reuse_extension_decisions: []
  new_dependency_decisions: []
  implementation_mapping: []
  convention_drift_findings: []
  evidence_gaps: []
  verification_plan: []

  handoff:
    component_fitness: adaptive-component-design
    interaction_behavior: design-interaction
    product_implementation: master-engineer_or_product_adapter
    post_implementation_acceptance: architecture-review
```

## Failure signals

Return `BLOCKED`, `PARTIAL`, or `NOT_VERIFIED` when:

- implementation begins before repository evidence is inspected;
- a package name is treated as canonical without usage or authority evidence;
- multiple systems conflict and no current authority resolves them;
- a fit shared component is rebuilt locally without reason;
- a second icon, component, styling, state, form, query, or data system is introduced casually;
- a migration target is mixed into ordinary work without a migration decision;
- a new dependency lacks a proven gap, alternatives, consequences, owner, or approval;
- native semantics are rejected by dogma rather than evaluated against the requirement;
- implementation mapping is missing before code;
- source-only evidence is used to claim runtime, visual, interaction, or accessibility PASS;
- architecture review is skipped because this discovery was completed.

## Contract coverage

Required inputs:

```text
repository_ref
implementation_scope
target_surface
proposed_changes
```

Allowed outputs and quality gates are declared in the reviewed core contract. Keep this adapter synchronized with that interface; exact metadata and textual coverage do not replace repository or runtime evidence.
