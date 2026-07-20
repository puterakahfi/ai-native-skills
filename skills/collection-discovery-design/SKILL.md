---
name: collection-discovery-design
description: Diagnose how users find, browse, narrow, compare, monitor, and resume within catalogs, registries, directories, feeds, tables, galleries, and search results. Use when collection scale, growth, grouping, filtering, sorting, traversal, or progressive disclosure may require a strategy before choosing tabs, pagination, load-more, infinite scroll, facets, trees, drawers, or other interaction adapters.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/design/collection-discovery-design.contract.yaml
  ai-native-skills.contract-version: ^1.0.0
  ai-native-skills.boundary.covers: '["collection_shape_and_discovery_pressure_diagnosis","retrieval_mode_analysis_and_prioritization","browse_search_and_narrowing_strategy","collection_organization_presentation_strategy","filtering_faceting_and_sorting_strategy","traversal_strategy","progressive_disclosure_strategy","collection_state_and_context_preservation","adapter_capability_selection","adapter_selection_rationale_and_tradeoffs","collection_specific_context_adaptation_requirements","realistic_collection_stress_planning","discovery_strategy_verification"]'
  ai-native-skills.boundary.delegates: '["taxonomy_definition_and_content_meaning","user_research_execution","visual_style_and_brand_expression","interaction_adapter_behavior_and_accessibility_implementation","cross_context_component_fitness_and_substitution_details","generic_breakpoint_grid_and_fluid_layout_mechanics","framework_or_component_library_specific_implementation","backend_search_index_query_and_storage_implementation","product_specific_ranking_or_business_policy","final_design_acceptance"]'
  ai-native-skills.related_skills: '["design-strategy","information-architecture","design-interaction","adaptive-component-design","responsiveness","accessibility","design-review","design-audit","redesign-workflow","ux-patterns-for-developers"]'
---

# Collection Discovery Design

Diagnose the collection before naming the component.

```text
collection evidence + retrieval tasks
→ discovery pressures
→ discovery strategy
→ adapter capabilities
→ context-specific components
→ rendered and runtime verification
```

Pagination, tabs, infinite scroll, load-more, filters, facets, grouped previews, trees, and drawers are possible adapters. None of them is the domain by itself.

## When to load

Load for a surface containing a meaningful collection:

- catalog, registry, directory, gallery, marketplace, feed, search results, table, admin list, knowledge base, library, inbox, or activity stream;
- long or growing groups;
- users who need lookup, browse, narrow, compare, monitor, or return to prior position;
- questions such as “Do we need pagination?”, “Should these categories become tabs?”, “Which filters matter?”, or “Why is mobile so long?”;
- audit findings where the root cause may be the collection model rather than one broken component.

Do not load for a single isolated control whose collection strategy is already accepted. Route that concern directly to `adaptive-component-design` or `design-interaction`.

## Ownership

```text
information-architecture
  owns taxonomy definition and content meaning

collection-discovery-design
  owns retrieval diagnosis and collection discovery strategy

design-interaction
  owns selected adapter behavior and accessibility details

adaptive-component-design
  owns component fitness and substitution across actual contexts

responsiveness
  owns generic layout and breakpoint mechanics

design-review
  owns acceptance
```

This skill advises strategy. It does not implement UI or backend search infrastructure.

## Hard rules

1. Start from user retrieval tasks, not the requested component name.
2. Item count alone is never a diagnosis.
3. Define the discovery model before selecting adapters.
4. Separate taxonomy meaning from how the taxonomy is presented.
5. The same collection may use different adapters by context while preserving state and meaning.
6. Preserve fit existing behavior unless evidence supports change.
7. Every selected adapter must trace to a task, pressure, constraint, and tradeoff.
8. Record rejected alternatives; never silently jump from symptom to component.
9. Do not use tabs for numerous dynamic searchable options.
10. Do not use infinite scroll for deterministic positional tasks without an explicit recovery model.
11. Virtualization solves rendering pressure, not discovery by itself.
12. Source inspection cannot prove scanability or discoverability.
13. Screenshots cannot prove keyboard, restoration, dynamic loading, or backend performance.
14. Implemented output requires `design-review`.

## Procedure

### 1. Establish collection evidence

Collect the required inputs:

```text
product_intent
user_tasks
collection_inventory
item_schema
current_volume
target_contexts
```

Then capture known optional evidence: expected growth, update frequency, heterogeneity, taxonomy, lookup frequency, comparison needs, return-position needs, deterministic location/shareability, query/index capability, performance constraints, analytics, accessibility, localization, and preservation requirements.

Load `references/diagnosis-and-strategy.md` for the inventory record, retrieval modes, pressure diagnosis, and strategy procedure.

### 2. Prioritize retrieval modes

Classify and rank:

```text
known_item_lookup
exploratory_browse
narrow_and_refine
compare
monitor_updates
resume_prior_context
hierarchical_drill_down
```

Multiple modes may coexist. Name the primary mode and the supporting modes before selecting any adapter.

### 3. Diagnose discovery pressure

Use one or more evidence-backed pressures:

```text
LOOKUP_PRESSURE
BROWSE_OVERLOAD
NARROWING_GAP
COMPARISON_PRESSURE
HIERARCHY_PRESSURE
CONTEXT_LOSS_RISK
GROWTH_PRESSURE
UPDATE_STREAM_PRESSURE
PERFORMANCE_PRESSURE
CROSS_CONTEXT_PRESSURE
NO_MATERIAL_DISCOVERY_PRESSURE
```

Do not translate “many items” directly into `pagination`. State what task is failing and why.

### 4. Define the strategy

Before components, specify:

- default entry;
- organization;
- browse versus search balance;
- narrowing and sorting;
- traversal;
- progressive disclosure;
- detail access;
- context and state preservation;
- verification plan.

### 5. Select adapter capabilities

Load `references/adapter-selection.md`.

Select the smallest replaceable set of capabilities needed across:

```text
organization
narrowing
traversal
disclosure
detail_access
```

Then hand behavior to `design-interaction` and context-specific component selection to `adaptive-component-design`.

### 6. Preserve state across adapters

Load `references/state-and-verification.md`.

Define applicable query, filters, sort, selected group/view, position or cursor, expanded/selected item, return behavior, URL/shareability, analytics identity, and accessibility relationships.

A desktop grouped registry and a mobile grouped preview may be different components while still implementing one strategy and one state contract.

### 7. Verify

Stress the strategy with realistic cases:

- highest expected volume and growth;
- longest and ambiguous labels;
- mixed retrieval tasks;
- target contexts and adaptation boundaries;
- empty, loading, error, no-result, partial, and stale states where applicable;
- keyboard, pointer, touch, assistive technology, restoration, and back behavior;
- measured backend performance when making performance claims.

Return `NOT_VERIFIED` for evidence that is not available.

## Adapter handoff

```yaml
collection_discovery_handoff:
  collection_diagnosis:
    primary_retrieval_mode: <mode>
    secondary_retrieval_modes: []
    pressures: []
    evidence: []
    unknowns: []

  collection_discovery_strategy:
    default_entry_strategy: <strategy>
    organization_strategy: <strategy>
    browse_search_balance: <strategy>
    narrowing_strategy: <strategy>
    sorting_strategy: <strategy>
    traversal_strategy: <strategy>
    progressive_disclosure_strategy: <strategy>
    detail_access_strategy: <strategy>

  adapter_capability_requirements:
    organization: []
    narrowing: []
    traversal: []
    disclosure: []
    detail_access: []

  context_adaptation_strategy:
    contexts: []
    adaptation_boundaries: []
    preserved_meaning: []
    preserved_state: []

  collection_state_contract:
    applicable_fields: []
    url_or_shareable_state_policy: <policy>
    return_and_restore_behavior: <behavior>

  adapter_selection_rationale: []
  rejected_adapter_alternatives: []
  realistic_data_stress_plan: []
  boundary_acceptance_criteria: []
  rendered_discovery_evidence: []
  evidence_gaps: []

  handoff:
    taxonomy: information-architecture
    behavior_and_a11y: design-interaction
    component_fitness: adaptive-component-design
    responsive_mechanics: responsiveness
    implementation: engineering_or_product_adapter
    acceptance: design-review
```

## Failure signals

Return `FAIL`, `PARTIAL`, or `NOT_VERIFIED` when:

- collection inventory or item schema is unknown;
- primary retrieval mode is not named;
- the answer is based on a fixed count threshold;
- tabs, pagination, or infinite scroll are treated as universal;
- search, browse, and filtering roles are conflated;
- facets or sort options do not map to real user decisions;
- traversal loses required position, context, or shareability;
- mobile hides primary discovery paths without a recovery route;
- adapters drift in query, filter, sort, selection, URL, analytics, or accessibility semantics;
- realistic growth and boundary contexts are not tested;
- visual, interaction, runtime, or performance claims exceed available evidence.

## Contract coverage

Required inputs:

```text
product_intent
user_tasks
collection_inventory
item_schema
current_volume
target_contexts
```

Allowed outputs:

```text
collection_diagnosis
retrieval_mode_map
collection_discovery_strategy
browse_search_balance
organization_strategy
narrowing_strategy
sorting_strategy
traversal_strategy
progressive_disclosure_strategy
detail_access_strategy
context_adaptation_strategy
collection_state_contract
adapter_capability_requirements
adapter_selection_rationale
rejected_adapter_alternatives
realistic_data_stress_plan
boundary_acceptance_criteria
rendered_discovery_evidence
```

Quality gates:

```text
collection_inventory_and_item_schema_are_known_before_strategy_selection
primary_and_secondary_retrieval_modes_are_explicit
diagnosis_uses_combined_pressures_not_item_count_alone
browse_search_and_narrowing_roles_are_explicit
taxonomy_meaning_and_collection_presentation_remain_separate
discovery_strategy_precedes_component_or_adapter_selection
adapter_capabilities_trace_to_diagnosis_user_tasks_and_constraints
pagination_tabs_infinite_scroll_and_other_adapters_are_not_selected_by_count_threshold_alone
primary_discovery_paths_remain_reachable_and_discoverable
grouping_facets_and_sorting_trace_to_meaningful_user_decisions
traversal_strategy_preserves_required_position_context_and_shareability
cross_context_adapters_preserve_query_filter_sort_selection_and_semantics
rejected_alternatives_and_tradeoffs_are_recorded
realistic_data_growth_and_boundary_contexts_are_verified
rendered_and_runtime_claims_use_appropriate_evidence
```
