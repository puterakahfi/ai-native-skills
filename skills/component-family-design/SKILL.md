---
name: component-family-design
description: Classify interface elements as atoms, molecules, organisms, templates, or pages; then preserve one canonical component family across routes through invariant anatomy, configurable slots, bounded variants, adaptive family identity, and route-instance mapping. Use when a redesign creates a new header, navbar, sidebar, shell, card family, form family, or other repeated interface region that may duplicate an existing family.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/design/component-family-design.contract.yaml
  ai-native-skills.contract-version: ^1.0.0
  ai-native-skills.boundary.covers: '["atomic_design_hierarchy_classification","canonical_component_family_inventory","organism_family_definition","template_family_definition","invariant_anatomy_and_slot_definition","bounded_variant_governance","route_to_family_instance_mapping","cross_route_component_family_consistency","adaptive_family_identity_preservation","family_reuse_extension_creation_or_migration_decisions","component_family_drift_diagnosis","cross_route_family_acceptance_criteria"]'
  ai-native-skills.boundary.delegates: '["design_token_definition","visual_style_or_brand_direction","task_level_component_pattern_selection","generic_breakpoint_mechanics","repository_framework_or_import_mapping","product_specific_component_implementation","final_rendered_accessibility_or_architecture_acceptance"]'
  ai-native-skills.related_skills: '["ui-components","design-layout","adaptive-component-design","implementation-context-discovery","design-system","design-review","redesign-workflow","master-engineer"]'
---

# Component Family Design

A route may need different content without needing a different component family.

```text
component capability
→ hierarchy classification
→ family inventory
→ invariant anatomy + configurable slots
→ bounded variants
→ adaptive family contract
→ repository mapping
→ implementation
→ cross-route verification
```

## Core contract interface

```yaml
required_inputs:
  - product_intent
  - target_surfaces
  - component_inventory
  - route_inventory
  - existing_design_system
allowed_outputs:
  - interface_hierarchy_classification
  - canonical_component_family_inventory
  - organism_family_contracts
  - template_family_contracts
  - invariant_anatomy_map
  - configurable_slot_map
  - bounded_variant_matrix
  - route_to_family_instance_map
  - adaptive_family_contract
  - family_reuse_extension_or_creation_decisions
  - family_drift_findings
  - family_migration_plan
  - cross_route_acceptance_criteria
  - rendered_family_evidence
quality_gates:
  - every_major_shared_surface_has_a_hierarchy_classification
  - equivalent_product_roles_are_checked_against_existing_families
  - family_invariant_anatomy_and_configurable_slots_are_explicit
  - route_differences_are_configuration_or_bounded_variants_when_fit
  - organism_and_template_ownership_are_not_conflated
  - adaptive_variants_preserve_family_identity_and_shared_semantics
  - new_family_creation_has_a_proven_role_or_capability_gap
  - route_to_family_instance_mapping_is_complete
  - cross_route_visual_interaction_and_accessibility_evidence_is_planned
  - source_inspection_alone_is_not_accepted_as_rendered_family_consistency
```

## Load when

- a new header, navbar, sidebar, shell, footer, card system, filter bar, form region, or repeated interface region is proposed;
- two routes perform the same product role with separate components;
- a dedicated product surface should feel specific without drifting from the application vocabulary;
- desktop and mobile use different patterns and must remain one family;
- a redesign introduces route-local spacing, branding, actions, or interaction anatomy;
- Atomic Design classification would clarify whether work belongs to an atom, molecule, organism, template, or page.

Do not load for a one-off atom or molecule when no shared family or cross-route responsibility exists.

## Ownership

```text
ui-components
  selects the component capability and task-level pattern

component-family-design
  owns hierarchy, family anatomy, slots, variants, route instances,
  and cross-route consistency

adaptive-component-design
  owns fit and substitution across actual contexts

implementation-context-discovery
  maps the accepted family to repository components, paths, tokens, and libraries

master-engineer
  implements the family and route adapters

design-review
  independently verifies rendered family consistency
```

## Hierarchy model

Use the labels as composition responsibilities, not file-size rules:

```text
atom
  indivisible interface primitive
  examples: icon, text token, button primitive

molecule
  small composition with one local purpose
  examples: brand lockup, nav item, search field group

organism
  reusable interface region with a distinct product responsibility
  examples: AppHeader, ProductSidebar, FilterToolbar, CheckoutSummary

template
  page-level arrangement of organisms and content regions
  examples: AppShell, ProductShell, DocumentationShell

page
  template instance with real route content and configuration
```

A navbar/header is normally an organism. A shell that places header, main, footer, and sidebar is a template.

## Hard rules

1. Classify the requested surface before creating a route-local component.
2. Search existing organisms and templates, not only atoms and primitive components.
3. Same product role should use the same family when that family fits.
4. Different labels, links, actions, or product context do not automatically justify a new family.
5. Declare invariant anatomy separately from configurable slots.
6. Treat route-specific differences as configuration or bounded variants before creating a new organism.
7. A variant may change content and optional regions; it may not accidentally change shared focus, keyboard, semantics, rhythm, or interaction vocabulary.
8. Desktop inline navigation and mobile Sheet navigation may be adaptive variants of one header family.
9. Adaptive substitution must preserve family identity, destinations, state, analytics identity, and accessibility relationships.
10. A new family requires a proven product-role or capability gap.
11. Source reuse alone does not prove rendered family consistency.
12. Implemented output requires cross-route rendered and interaction evidence through `design-review`.

## Procedure

### 1. Classify the interface hierarchy

For every material requested element, record:

```yaml
interface_hierarchy_classification:
  surface: <surface>
  level: atom | molecule | organism | template | page
  product_role: <role>
  evidence: []
```

### 2. Inventory existing families

Inspect current routes, components, stories, examples, variants, and rendered surfaces.

```yaml
canonical_component_family_inventory:
  - family_name: AppHeader
    hierarchy_level: organism
    route_instances: []
    variants: []
    ownership: <path or package>
    status: canonical | migration_target | legacy | unknown
```

Do not conclude that no family exists merely because component filenames differ.

### 3. Define the family contract

```yaml
component_family_contract:
  family_name: <name>
  hierarchy_level: organism | template
  product_role: []

  invariant_anatomy: []
  configurable_slots: []

  shared_visual_contract:
    typography_roles: []
    spacing_roles: []
    control_vocabulary: []
    active_state: <contract>
    focus_state: <contract>
    elevation_or_shell_treatment: <contract>

  shared_interaction_contract: []
  shared_accessibility_contract: []

  bounded_variants: []
  route_instances: []
  prohibited_parallel_implementations: []
```

### 4. Separate invariant anatomy from slots

For an `AppHeader` family, a typical split is:

```text
invariants
  shell height and container
  identity region
  primary navigation region
  utility action region
  mobile navigation trigger
  focus and active-state vocabulary

slots
  title and supporting label
  navigation items
  utility actions
  optional parent or escape link
  active-state strategy
```

### 5. Select the family decision

Choose one:

```text
reuse_existing_family
reuse_existing_family_variant
extend_family_with_bounded_variant
compose_existing_families
migrate_route_local_implementation_into_family
create_new_family_after_proven_role_gap
unresolved
```

Record rejected alternatives and the evidence for any new family.

### 6. Define adaptive family identity

Hand actual width and interaction fitness to `adaptive-component-design`, but preserve:

```yaml
adaptive_family_contract:
  shared_product_role: <role>
  shared_information_identity: []
  shared_state: []
  wide_variant: <pattern>
  constrained_variant: <pattern>
  preserved_destinations: []
  preserved_actions: []
  focus_and_keyboard_expectations: []
  analytics_identity: []
```

### 7. Map routes to instances

```yaml
route_to_family_instance_map:
  - route: /en
    template_family: AppShell
    organism_family: AppHeader
    variant: portfolio

  - route: /ai-skills
    template_family: AppShell
    organism_family: AppHeader
    variant: product
```

### 8. Verify cross-route consistency

Check real routes together:

- invariant anatomy;
- container, height, spacing, and typography roles;
- shared control and icon vocabulary;
- hover, active, focus, disabled, and theme behavior;
- desktop and constrained-width variants;
- destination and state equivalence;
- route-specific differences trace to declared slots or variants.

## Diagnosis

```text
COMPONENT_FAMILY_DRIFT
  equivalent product roles use unrelated implementations

ORGANISM_DUPLICATION
  a route rebuilds a fit shared organism

TEMPLATE_FAMILY_BYPASS
  a page recreates shell structure instead of using the fit template

VARIANT_BOUNDARY_BREACH
  a variant changes invariant anatomy or shared behavior without approval

FAMILY_CAPABILITY_GAP
  no existing family can satisfy the material product role

IMPLEMENTATION_DEFECT
  the family is correct but one instance is broken
```

## PKahfi regression case

```text
portfolio navbar
+ dedicated AI Skills navbar
+ mobile Sheet improves constrained navigation

invalid result:
  two unrelated navbar organisms with different anatomy and UX vocabulary

required result:
  AppHeader organism family
  + portfolio variant
  + product variant
  + shared mobile Sheet behavior
  inside AppShell template family
```

Menu content, actions, active-state strategy, and parent link may differ. Shell anatomy, identity treatment, control vocabulary, theme action, responsive transformation, and accessibility contract must remain family-owned.

## Required output

```yaml
component_family_design:
  interface_hierarchy_classification: []
  canonical_component_family_inventory: []
  organism_family_contracts: []
  template_family_contracts: []
  invariant_anatomy_map: []
  configurable_slot_map: []
  bounded_variant_matrix: []
  route_to_family_instance_map: []
  adaptive_family_contracts: []
  family_decisions: []
  family_drift_findings: []
  migration_plan: []
  cross_route_acceptance_criteria: []
  rendered_family_evidence: []
  evidence_gaps: []

  handoff:
    component_pattern: ui-components
    adaptive_fitness: adaptive-component-design
    repository_mapping: implementation-context-discovery
    tokens_and_theme: design-system
    implementation: master-engineer
    acceptance: design-review
```

## Stop conditions

Return `FAIL`, `PARTIAL`, or `NOT_VERIFIED` when:

- hierarchy is not classified;
- equivalent route roles are not checked against existing families;
- invariant anatomy and configurable slots are conflated;
- a route-local organism bypasses a fit family;
- an adaptive variant loses shared family identity or semantics;
- a new family lacks a proven role or capability gap;
- route-instance mapping is incomplete;
- source similarity is presented as rendered cross-route acceptance.
