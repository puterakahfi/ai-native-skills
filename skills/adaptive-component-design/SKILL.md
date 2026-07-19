---
name: adaptive-component-design
description: Selects, preserves, or substitutes UI component patterns across available widths and input contexts from the user task, real container width, realistic content pressure, discoverability, accessibility, and interaction cost. Use when a component fits one context but overlaps, clips, hides choices, or becomes awkward in another.
license: MIT
metadata:
  ai-native-skills.version: 1.2.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/design/adaptive-component-design.contract.yaml
  ai-native-skills.contract-version: "~1.1"
  ai-native-skills.related_skills: '["master-design","design-review","design-refinement","responsiveness","design-strategy","ux-ui-patterns","ux-patterns-for-developers","accessibility","ui-components"]'
---

# Adaptive Component Design

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

This skill owns component fitness, adaptation/substitution, shared state semantics, overflow/disclosure affordances, and boundary evidence. It does not own page macrostructure, visual language, product strategy, generic breakpoint mechanics, or final acceptance.

## Hard rules

```text
1. Start from the user task, not the requested component name.
2. Measure actual container width after shell, sidebars, gutters, and adjacent controls.
3. Device labels and common viewport numbers are contexts or samples, not canonical selection rules.
4. Derive adaptation boundaries from real content failure and passing points.
5. Separate pattern mismatch from implementation defects.
6. Preserve a fit component when the issue is local implementation.
7. Replace an unfit component even when it already exists in the design system.
8. Keep primary choices discoverable unless a product reason justifies disclosure.
9. Different component families must preserve product meaning and controlled state.
10. Verify realistic content, text expansion, states, input modes, and boundary widths.
11. Screenshots alone do not prove keyboard, dynamic affordances, or state equivalence.
12. Implemented output requires independent design-review evidence.
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
component fitness record
selected and rejected patterns
adaptation mode by actual context
observed adaptation boundaries
shared state and semantics contract
realistic content stress results
rendered evidence at target and boundary contexts
interaction evidence for applicable input modes
design-review verdict for implemented output
remaining assumptions or limitations
```
