# Component Review Registry

Load this reference only for interactive surfaces and only for components that exist or are required by the user task.

This is a registry, not a requirement that every surface contain every component. A missing component fails only when the task, information architecture, or product contract requires it.

## Component selection rule

For each selected component, review:

```text
purpose and task fit
content contract and density
states
input methods
responsive/adaptive behavior
accessibility
shared state and semantics across variants
relationship to adjacent components
failure and edge conditions
```

Do not judge a component only by visual similarity to a reference. Judge whether it is the correct component for the task and constraints.

## Component diagnosis

Before recommending a correction, classify the problem:

```text
PATTERN_MISMATCH
  The component family does not fit the task, content, or context.
  Correction owner: adaptive-component-design + design owner.

IMPLEMENTATION_DEFECT
  The selected component contract is fit, but behavior or rendering is broken.
  Correction owner: local implementation owner.

CONTENT_PRESSURE
  Realistic content exceeds the component contract.
  Correction owner: adaptive-component-design and possibly design-strategy.

SYSTEM_CONSTRAINT
  The design-system primitive cannot satisfy the required behavior.
  Correction owner: design-system/ui-components + implementation owner.

LOCAL_VISUAL_DEFECT
  The component is structurally fit but has bounded hierarchy, readability,
  spacing, composition, or expression problems.
  Correction owner: relevant visual specialist.
```

Visible overflow does not automatically mean the component family is wrong. A valid rail with stale directional controls is an implementation defect. Numerous dynamic searchable choices forced into tabs are a pattern mismatch.

## Adaptive component contract

When a component changes across contexts, review:

```text
actual available width, not viewport label alone
realistic option count and label lengths
adaptation mode in each relevant context
observed passing/failure or substitution boundary
selected value and available choices
change event semantics
URL/query/filter state when applicable
analytics identity
accessible name and relationships
focus and keyboard behavior
loading, disabled, empty, and error semantics
```

Different component families may be valid across widths, but their product meaning and state must remain equivalent.

Common phone/tablet/desktop sizes are samples. Acceptance must include actual target contexts and points immediately before and after adaptation boundaries.

## Navigation

Review:

- information scent and label clarity;
- current-location and active-state visibility;
- hierarchy between global, local, contextual, and utility navigation;
- overflow and narrow-width strategy;
- keyboard, pointer, touch, and back behavior;
- preservation of context during navigation;
- whether hidden navigation remains discoverable.

Common failures:

```text
compressing desktop navigation into an unusable mobile row
hiding primary destinations only to avoid overflow
active state communicated by color alone
multiple navigation systems competing at equal weight
back action returning to an unexpected context
```

## Hero or page header

Review:

- primary message or task identity;
- relationship between title, supporting copy, proof, media, and action;
- first-viewport composition;
- focal point and excess empty space;
- whether the pattern matches marketing, application, editorial, or utility intent;
- responsive reflow and text scaling;
- action prominence and honesty.

Do not require every page to have a cinematic hero. Application surfaces often need a compact task header instead.

## Tabs, segmented controls, and category rails

Review:

- whether the pattern represents peer views, navigation, discovery categories, or filters;
- selected-state clarity;
- realistic label length and option count;
- actual available width after shell and adjacent controls;
- overflow behavior and previous/next affordances;
- touch, keyboard, swipe, and scroll behavior;
- content-panel relationship and preserved state;
- suitability versus dropdown, filters, chips, sidebar, rail, carousel, or another component;
- state and semantic equivalence when variants differ by context.

A primary discovery set should not be hidden solely because the chosen tabs overflow. Evaluate visible overflow, scrolling affordances, wrapping risk, label length, option count, available width, and component substitution.

For a rail:

```text
right control appears only when forward movement exists
left control appears only when backward movement exists
both controls appear when both directions exist
controls update from actual scroll state after scroll, resize, selection, and content change
no control permanently covers an item
```

## Cards and lists

Review:

- grouping and repeated structure;
- scanability and comparison;
- content hierarchy inside each item;
- action placement and target size;
- selected, hover, disabled, loading, and empty states;
- image ratio and content variability;
- list versus grid choice at each context;
- whether equal-size cards falsely imply equal priority.

Avoid turning every content type into a card. Rows, tables, grouped lists, timelines, and editorial blocks may fit better.

## Forms, filters, and controls

Review:

- label and instruction clarity;
- field grouping and sequence;
- required and optional distinction;
- validation timing and recovery;
- input type, default, placeholder, and formatting;
- keyboard and mobile input behavior;
- filter application, reset, and active-filter visibility;
- destructive or irreversible action protection;
- loading and submission feedback.

Placeholders are not substitutes for persistent labels when the value can obscure the instruction.

## Tables and data views

Review:

- column priority and comparison task;
- density, alignment, truncation, and wrapping;
- sorting, filtering, selection, pagination, and bulk actions;
- empty, loading, error, partial, and stale states;
- sticky headers or columns where justified;
- responsive strategy: scroll, prioritize, transform, or alternate view;
- keyboard and screen-reader relationships;
- numeric, date, currency, and status formatting.

Do not automatically convert every table into stacked cards on mobile. Preserve the comparison task through horizontal scroll, column priority, compact modes, or alternate views as appropriate.

## Dialogs, drawers, popovers, and overlays

Review:

- whether the overlay is the correct containment model;
- context preservation and background relationship;
- open/close triggers and dismissal;
- focus entry, containment, and restoration;
- viewport and keyboard fit;
- scroll ownership;
- action hierarchy and destructive confirmation;
- nested-overlay risk;
- mobile substitution between dialog, sheet, full screen, and inline flow;
- shared values, actions, validation, and recovery across variants.

Avoid using a drawer merely because the implementation already has one. Choose it when preserving the underlying context is valuable and the content fits the available width.

## Search and command surfaces

Review:

- search scope and query expectations;
- input visibility and shortcut discoverability;
- suggestions, recent items, filters, and result grouping;
- loading, no-result, error, and partial-result states;
- keyboard navigation and focus management;
- query persistence and clear/reset behavior;
- result action clarity;
- mobile keyboard and viewport behavior.

A search icon without visible scope or discoverable expansion may be insufficient for a primary discovery task.

## Empty, loading, error, success, and permission states

Review:

- whether the state explains what happened;
- whether it distinguishes no data, no results, no access, offline, failure, and first use;
- available recovery or next action;
- preservation of user input and context;
- visual weight proportional to state importance;
- truthful language;
- skeleton and placeholder resemblance to final content;
- prevention of layout shift or false completion.

A decorative empty illustration does not replace explanation and recovery.

## Footer and closing regions

Review:

- whether the surface needs a closing or utility region;
- hierarchy relative to primary content;
- legal, support, account, and secondary navigation accuracy;
- repeated CTA necessity;
- density and grouping;
- mobile stacking and target reachability;
- contrast and transition from the preceding region.

Applications may not need a marketing footer. Do not add one by convention.

## Component finding format

```yaml
component_finding:
  component: category-navigation
  region: creative-gallery-category-navigation
  governing_gate: I4
  diagnosis: IMPLEMENTATION_DEFECT

  observation: previous direction is not discoverable after horizontal scroll
  evidence:
    - actual available-width capture
    - tablet interaction recording
    - scroll-state observation
  impact: users can move forward but cannot reliably return to hidden earlier categories

  component_contract:
    role: primary discovery
    selected_pattern: horizontal rail
    adaptation_mode: scroll
    substitution_boundary: <value or N/A>
    shared_state_and_semantics: <reference>

  correction_owner: local implementation owner
  correction_direction: expose bidirectional edge controls synchronized with actual scroll state
  target_region: category navigation only
  protected_regions: [hero, cards, typography, desktop grid]
  adjacent_regression_gates: [G13, G14]
  required_evidence:
    - before and after boundary contexts
    - touch and keyboard operation
    - state after resize and content change
```

When the same issue affects multiple components, report the underlying system or interaction rule once and list affected regions. Do not duplicate the same finding per instance.

## Refinement handoff

A finding routed to `design-refinement` should provide:

```yaml
refinement_handoff:
  accepted_direction: <reference>
  target_findings: []
  target_regions: []
  preserved_gate_ids: []
  preserved_regions: []
  preserved_component_contracts: []
  diagnosis: <class>
  correction_owner: <owner>
  adjacent_regression_gates: []
  required_evidence: []
```

Do not send a vague “make it better” finding into refinement. The handoff must be precise enough to declare a lock and change budget before editing.
