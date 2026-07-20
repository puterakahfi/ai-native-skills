---
name: adaptive-component-design
description: Selects, preserves, or substitutes UI component patterns across available widths and input contexts from the user task, real container width, realistic content pressure, discoverability, accessibility, and interaction cost. Use when a component fits one context but overlaps, clips, hides choices, or becomes awkward in another.
license: MIT
metadata:
  ai-native-skills.version: 1.2.4
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/design/adaptive-component-design.contract.yaml
  ai-native-skills.contract-version: "~1.1"
  ai-native-skills.boundary.covers: '["component_fitness_diagnosis","context_specific_component_selection","cross_context_component_substitution","responsive_pattern_transformation","navigation_component_adaptation","content_density_adaptation","interaction_mode_adaptation","shared_state_and_semantics_across_variants","overflow_and_disclosure_affordance_behavior","adaptation_boundary_verification"]'
  ai-native-skills.boundary.delegates: '["visual_style_and_brand_expression","page_level_macrostructure_selection","design_token_definition","generic_breakpoint_and_fluid_grid_mechanics","implementation_framework_specific_code","product_specific_component_library_mapping"]'
  ai-native-skills.related_skills: '["master-design","design-review","design-refinement","responsiveness","design-strategy","ux-ui-patterns","ux-patterns-for-developers","accessibility","ui-components","component-family-design"]'
---

# Adaptive Component Design

## Reviewed core contract interface

Source: `ai-native-core/contracts/skills/design/adaptive-component-design.contract.yaml` · compatible line: `~1.1`

```yaml
required_inputs:
- product_intent
- user_tasks
- content_inventory
- component_inventory
- target_contexts
allowed_outputs:
- component_fitness_record
- viewport_strategy
- component_substitution_matrix
- adaptation_boundary_map
- component_selection_rationale
- rejected_component_alternatives
- navigation_pattern_selection
- content_density_strategy
- interaction_mode_mapping
- shared_state_and_semantics_contract
- affordance_state_contract
- responsive_behavior_contract
- boundary_acceptance_criteria
- realistic_content_stress_evidence
- rendered_interaction_evidence
quality_gates:
- each_major_component_has_an_explicit_context_strategy
- component_pattern_selected_from_user_task_content_and_context
- requested_component_is_treated_as_a_proposed_solution_not_an_immutable_requirement
- diagnosis_distinguishes_pattern_mismatch_from_implementation_defect
- adaptation_mode_is_declared_for_each_relevant_context
- substitution_boundaries_are_derived_from_real_content_and_available_width
- primary_choices_are_not_hidden_without_product_rationale
- navigation_pattern_matches_information_architecture_and_context
- dense_data_has_explicit_small_width_transformation
- tabs_and_horizontal_collections_expose_truthful_overflow_affordance
- directional_controls_reflect_actual_scroll_availability
- touch_pointer_and_keyboard_interactions_are_defined_when_applicable
- interactive_targets_do_not_overlap_or_clip
- component_variants_preserve_shared_value_state_event_semantics_analytics_and_accessible_relationships
- hidden_content_is_non_critical_justified_and_still_reachable_when_required
- component_choice_includes_rejected_alternatives_and_tradeoffs
- acceptance_criteria_cover_actual_targets_and_adaptation_boundaries
- realistic_content_and_text_expansion_are_verified
- code_inspection_alone_is_not_accepted_as_visual_verification
```

Treat a requested component as a proposed solution. Use product intent, tasks, content, current components, and target contexts to compare alternatives. Horizontal collections need truthful overflow affordances; touch, pointer, and keyboard behavior must be defined, and targets may not overlap or clip.

Keep this interface synchronized with the pinned core contract. Exact declarations make ownership reviewable; they do not replace rendered, runtime, accessibility, or product evidence.

Select the component pattern that preserves the user task, product meaning, state, semantics, and information priority at the **actual available width**.

Responsive design may change the component family. It must not blindly compress a desktop pattern or replace a fit component merely because its implementation is broken.

## Role

```text
narrow cross-context component decision
→ adaptive-component-design may advise directly

broad design or redesign
→ owner: master-design
→ specialist: adaptive-component-design
→ implementation: master-engineer when patching
→ acceptance: design-review
```

This skill owns component fitness, context-specific selection, cross-context substitution, responsive pattern transformation, navigation and content-density adaptation, interaction-mode adaptation, shared state semantics, overflow/disclosure affordances, and adaptation-boundary evidence.

It delegates visual style and brand expression, page-level macrostructure, design-token definition, generic breakpoint and fluid-grid mechanics, framework-specific implementation code, and product-specific component-library mapping to the corresponding specialist or implementation owner. `master-engineer` owns repository implementation when required; `design-review` owns final acceptance.

## Hard rules

```text
1. Start from the user task, not the requested component name.
2. Measure actual container width after shell, sidebars, gutters, and adjacent controls.
3. Separate screenshot artifact dimensions, browser CSS viewport, and actual available container width; they are not interchangeable evidence.
4. Device labels and common viewport numbers are contexts or samples, not canonical selection rules.
5. Derive adaptation boundaries from real content failure and passing points.
6. Separate pattern mismatch from implementation defects.
7. Preserve a fit component when the issue is local implementation.
8. Replace an unfit component even when it already exists in the design system.
9. Keep primary choices discoverable unless a product reason justifies disclosure.
10. Different component patterns must preserve product meaning and controlled state.
11. When an accepted organism or template family exists, substitutions must remain declared variants of that family unless `component-family-design` approves a new family.
12. Verify realistic content, text expansion, states, input modes, and boundary widths.
13. Screenshots alone do not prove keyboard, dynamic affordances, state equivalence, family identity, or the viewport that produced the artifact.
14. Implemented output requires independent design-review evidence.
```

## Diagnose before fixing

```text
PATTERN_MISMATCH
  component family does not fit the task, content, or context

IMPLEMENTATION_DEFECT
  component family fits but behavior or rendering is broken

CONTENT_PRESSURE
  realistic content exceeds the current component contract

SYSTEM_CONSTRAINT
  available primitive or design system blocks required behavior
```

A valid rail with a missing left control is an implementation defect. Numerous dynamic searchable choices forced into tabs are a pattern mismatch.

Load `references/component-fitness-and-boundaries.md` for the full decision procedure, component-fitness record, pattern guidance, state-equivalence contract, rail behavior, and boundary verification.

## Decision summary

```text
name task and priority
→ establish visual-evidence provenance
→ measure real width
→ inventory realistic content pressure
→ identify input/display contexts
→ diagnose problem class
→ compare preserve/reflow/scroll/disclose/substitute options
→ select smallest fit pattern
→ identify real adaptation boundary
→ define shared state and semantics
→ record rejected alternatives
→ verify target and boundary contexts
```

## Component selection principles

- Few short peer views may fit tabs or segmented controls.
- Stable primary discovery categories should remain visibly discoverable.
- Numerous, dynamic, searchable, or long options often need Select, combobox, sheet, popover, or filter panel.
- Dense comparison requires an explicit constrained-width strategy; cards are not the automatic answer.
- Existing design-system primitives are preferred only when they fit the task.
- Custom behavior needs documented reasoning, but library consistency never justifies an unfit pattern.

These are hypotheses, not fixed mobile/tablet/desktop mappings.

## Horizontal rails

A selected rail must provide:

```text
native swipe or trackpad scrolling
visible continuation when more content exists
right control only when forward movement exists
left control only when backward movement exists
paired controls when both directions exist
controls synchronized with actual scroll position
state refresh after resize, content change, and selection
keyboard-reachable controls with accessible names
no permanently covered item
```

A permanent right-only chevron is incomplete.

## Shared state contract

Across variants preserve:

```text
selected value and available choices
product meaning and labels
change event semantics
URL/query/filter state when applicable
analytics identity
accessible relationships
focus and keyboard expectations
loading, disabled, empty, and error semantics
```

## Verification

Use actual product contexts plus:

```text
widest known failing width
narrowest known passing width
immediately before and after adaptation boundaries
intermediate widths where behavior changes non-linearly
```

Stress with applicable realistic labels, highest expected option count, localization/text expansion, zoom, dynamic content, states, orientation, and input modes.

An image embedded in chat, documentation, or an issue tracker may be resized independently of the browser that produced it. Do not use the image file width as proof of a mobile, tablet, or desktop runtime state. Prefer capture metadata or browser evidence. When those are unavailable, active component variants may support a hypothesis, but the actual CSS viewport and available container width remain `NOT_VERIFIED` until measured.

Do not require one universal list of viewport numbers. Common device sizes are useful samples only.

## Output

```yaml
adaptive_component_handoff:
  component_fitness: <record>
  diagnosis: <class>
  selected_strategy: <strategy>
  substitution_boundaries: []
  shared_state_and_semantics: <contract>
  rejected_alternatives: []
  implementation_owner: <owner>
  preserved_behavior: []
  boundary_acceptance_criteria: []
  rendered_evidence_required: []
  design_review_route:
    review_depth: focused
    selected_gates: []
```

## Quality gates

Return failure or `NOT_VERIFIED` when applicable:

- choice is based only on device name or existing implementation;
- screenshot artifact width is treated as the runtime CSS viewport without provenance;
- actual available width is unknown;
- pattern mismatch and implementation defect are conflated;
- primary choices are hidden without rationale;
- intermediate widths are not evaluated;
- adaptation boundaries are guessed from framework defaults;
- controls overlap, clip, obscure items, or lie about scroll availability;
- required options are unreachable with applicable input methods;
- variants drift in value, event, URL, analytics, label, or focus semantics;
- realistic content or text expansion was not tested;
- implementation is accepted from source inspection alone;
- the specialist changes page strategy or visual direction without the design owner.

## Completion evidence

```text
visual-evidence provenance: artifact dimensions, known CSS viewport, and available container width
component fitness record
selected and rejected patterns
adaptation mode by actual context
observed adaptation boundaries
shared state and semantics contract
accepted component family and variant identity when applicable
realistic content stress results
rendered evidence at target and boundary contexts
interaction evidence for applicable input modes
design-review verdict for implemented output
remaining assumptions or limitations
```
