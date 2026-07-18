# Component Review Registry

Load this reference only for interactive surfaces and only for components that exist or are required by the user task.

This is a registry, not a requirement that every surface contain every component. A missing component fails only when the task, information architecture, or product contract requires it.

## Component selection rule

For each selected component, review:

```text
purpose and task fit
content fit and density
states
input methods
responsive/adaptive behavior
accessibility
relationship to adjacent components
failure and edge conditions
```

Do not judge a component only by visual similarity to a reference. Judge whether it is the correct component for the task and constraints.

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

## Tabs and segmented controls

Review:

- whether tabs represent peer views of the same context;
- selected-state clarity;
- label length and option count;
- overflow behavior and previous/next affordances;
- touch, keyboard, swipe, and scroll behavior;
- content-panel relationship and preserved state;
- suitability versus dropdown, filters, chips, sidebar, carousel, or another component.

A primary discovery set should not be hidden solely because the chosen tabs overflow. Evaluate visible overflow, scrolling affordances, wrapping risk, label length, option count, available width, and component substitution.

## Cards and lists

Review:

- grouping and repeated structure;
- scanability and comparison;
- content hierarchy inside each item;
- action placement and target size;
- selected, hover, disabled, loading, and empty states;
- image ratio and content variability;
- list versus grid choice at each viewport;
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
- mobile substitution between dialog, sheet, full screen, and inline flow.

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
  component: tabs
  region: creative-gallery-category-navigation
  issue: previous direction is not discoverable after horizontal scroll
  governing_gate: I4
  evidence: tablet viewport screenshot and touch interaction
  impact: users can move forward but cannot reliably return to hidden earlier categories
  recommendation: expose bidirectional edge affordances and keep them synchronized with scroll position
  scope: component
```

When the same issue affects multiple components, report the underlying system or interaction rule once and list affected regions. Do not duplicate the same finding per instance.