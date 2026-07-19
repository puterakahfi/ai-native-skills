# Component Fitness and Adaptation Boundaries

Load this reference when deciding whether to preserve, repair, reflow, scroll, disclose, or substitute a component across contexts.

## Diagnose before fixing

```text
PATTERN_MISMATCH
  The component family does not fit the task, content, or context.

IMPLEMENTATION_DEFECT
  The component family fits, but behavior or rendering is broken.

CONTENT_PRESSURE
  Realistic content exceeds the current component contract.

SYSTEM_CONSTRAINT
  The available primitive or design system cannot express the required behavior.
```

Visible overflow alone does not prove `PATTERN_MISMATCH`. A valid horizontal rail with a missing left control is an implementation defect. Eight dynamic searchable choices forced into tabs are a pattern mismatch.

## Visual evidence provenance

Before calling a screenshot mobile, tablet, desktop, narrow, or wide, distinguish three different measurements:

```text
artifact_dimensions
  pixel dimensions of the uploaded or embedded image file

rendered_css_viewport
  browser CSS viewport that produced the interface

available_container_width
  width left for the component after shell, sidebar, gutters, and adjacent controls
```

They may all be different. Chat applications, issue trackers, documents, and image pipelines may resize a screenshot after capture. A 358px-wide artifact can still depict a tablet or desktop render. Active component variants such as a desktop sidebar, line tabs, or a multi-column table may support a hypothesis about the original state, but they do not replace capture metadata or runtime measurement.

When provenance is unavailable:

```text
artifact width only
→ rendered viewport: NOT_VERIFIED
→ available container width: NOT_VERIFIED
→ do not patch responsive composition from the artifact width alone
```

## Decision sequence

1. Name the task and priority.
2. Establish evidence provenance: artifact dimensions, known CSS viewport, and known container width.
3. Measure actual container width after shell, gutters, sidebars, and adjacent controls.
4. Inventory realistic option count, label lengths, content growth, visibility needs, and frequency.
5. Identify input and display contexts: touch, pointer, keyboard, mixed, orientation, zoom, and text scaling.
6. Diagnose the problem class.
7. Compare preserve, reflow, resize, scroll, collapse, disclose, hide, and substitute.
8. Select the smallest pattern that preserves task completion and discoverability.
9. Find the actual passing/failure boundary with realistic content.
10. Define shared value, state, events, URL/query behavior, analytics identity, accessible relationships, and focus behavior.
11. Record rejected alternatives and trade-offs.
12. Verify immediately before and after every adaptation boundary.

## Component fitness record

```yaml
component_fitness:
  region: <region>
  component_role: <navigation | filter | selection | comparison | editing | other>
  user_task: <task>
  diagnosis: <PATTERN_MISMATCH | IMPLEMENTATION_DEFECT | CONTENT_PRESSURE | SYSTEM_CONSTRAINT>

  evidence_provenance:
    artifact_dimensions: <width x height or unknown>
    rendered_css_viewport: <width x height or NOT_VERIFIED>
    available_container_width: <px, bounded range, or NOT_VERIFIED>
    source: <browser evidence | capture metadata | uploaded artifact | other>

  content_contract:
    option_count: <range>
    longest_realistic_labels: []
    priority_groups: []
    dynamic_growth: <expected behavior>

  actual_contexts:
    - available_width: <px or bounded range>
      input_modes: []
      orientation: <value or N/A>
      content_case: <case>
      current_result: <pass | fail | partial>

  selected_strategy:
    adaptation_mode: <preserve | reflow | resize | collapse | substitute | scroll | disclose | hide>
    component_by_context: []
    substitution_boundaries: []

  shared_contract:
    value_and_selected_state: <contract>
    event_semantics: <contract>
    url_or_query_state: <contract or N/A>
    analytics_identity: <contract>
    accessible_name_and_relationships: <contract>
    focus_and_input_behavior: <contract>

  rejected_alternatives:
    - option: <pattern>
      rejected_because: <reason>

  required_evidence: []
```

## Pattern guidance

These are hypotheses, not device rules:

| Need | Often suitable when constrained | Often suitable with more width |
|---|---|---|
| Few short peer views | segmented control, tabs, visible shortcuts | line tabs |
| Stable primary discovery categories | visible shortcut rail or scrollable labeled rail | line tabs or shortcut grid |
| Numerous, dynamic, searchable options | select, combobox, sheet | searchable select, popover, filter panel |
| Secondary filters | button + sheet/drawer | popover or inline filter bar |
| Dense comparison | prioritized rows, scroll, summary/detail, alternate view | table/grid |
| Multi-step editing | full-screen or step flow | sheet, drawer, dialog, split view |
| Supporting cards | rail with visible continuation | stable grid or supporting column |

A small stable primary category set should not disappear into Select merely because tabs are inconvenient.

## Horizontal rail contract

```text
native swipe or trackpad scrolling
visible continuation when more content exists
right control only when forward movement exists
left control only when backward movement exists
paired controls when both directions exist
controls synchronized with actual scroll position
state refreshed after resize, content change, and selection
keyboard-reachable controls with accessible names
no item permanently covered by controls
approximately one meaningful visible group per control action
```

A permanent right-only chevron is not a complete rail implementation.

## State equivalence

Different component families must preserve:

```text
selected value
available choices and product meaning
change event semantics
URL/query/filter state when applicable
analytics identity
accessible label and relationships
focus return and keyboard expectations
loading, disabled, empty, and error semantics
```

A mobile Select and desktop Tabs are not equivalent when they drift to different labels, values, URLs, analytics events, or focus behavior.

## Boundary verification

Do not require one universal viewport list. Use:

```text
actual product target contexts
widest known failing width
narrowest known passing width
immediately before each adaptation boundary
immediately after each adaptation boundary
intermediate widths when behavior changes non-linearly
```

Stress with applicable cases:

```text
longest realistic labels
highest expected option count
selected, active, disabled, loading, and empty states
localization or text expansion
zoom or text scaling
dynamic content addition and removal
portrait and landscape
touch, pointer, keyboard, and mixed input
```

Common phone, tablet, laptop, and desktop sizes are useful samples, not universal completion criteria. Uploaded image dimensions are artifact metadata, not a substitute for these runtime contexts.

## Handoff

```yaml
adaptive_component_handoff:
  diagnosis: <class>
  selected_component_contract: <record>
  implementation_owner: <owner>
  preserved_behavior: []
  allowed_changes: []
  protected_changes: []
  boundary_acceptance_criteria: []
  rendered_evidence_required: []
  design_review_route:
    review_depth: focused
    selected_gates: [I4, G13, G14]
```

## Completion guard

```text
□ Screenshot artifact dimensions are separated from CSS viewport and available container width.
□ Actual available width is measured.
□ Pattern mismatch and implementation defect are separated.
□ Component choice follows task and realistic content.
□ Intermediate widths are explicitly evaluated.
□ Adaptation boundaries come from observed content behavior.
□ Primary choices remain discoverable.
□ Directional affordances reflect actual scroll availability.
□ Shared state and semantics are preserved across variants.
□ Realistic content and text expansion are tested.
□ Target and boundary contexts have rendered evidence.
□ Implemented output has independent design-review evidence.
```
