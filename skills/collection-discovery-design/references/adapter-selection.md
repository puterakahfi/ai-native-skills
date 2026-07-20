# Collection Adapter Selection

Load this reference only after a collection diagnosis and discovery strategy exist.

Adapter names are replaceable implementation choices. Select capability families first, then delegate behavior to `design-interaction` and context-specific component fitness to `adaptive-component-design`.

## Selection sequence

```text
retrieval modes
→ diagnosed pressures
→ strategy requirements
→ candidate capability families
→ constraints and tradeoffs
→ selected adapter capabilities
→ context substitutions
→ verification
```

Do not reverse this sequence because the user asked for pagination, tabs, or a filter panel.

## Organization capabilities

| Capability | Stronger when | Reject or reconsider when | Requirements |
|---|---|---|---|
| `flat_list` | collection is small or already narrowed; items share a simple schema | grouping or hierarchy materially improves retrieval | clear ordering and scan rhythm |
| `grouped_sections` | stable meaningful groups support browsing | groups are arbitrary, numerous, or mostly empty | group labels, counts where useful, predictable order |
| `tabs` | few stable peer views are switched frequently | options are numerous, dynamic, long, searchable, nested, or not true peers | persistent selected state, reachable options, content-panel relationship |
| `accordion` | users need selective disclosure within meaningful groups | comparison across groups must remain visible | clear expanded state, keyboard behavior, preserved content access |
| `tree_navigation` | data has a real parent-child hierarchy | taxonomy is flat or multi-faceted rather than hierarchical | expansion state, path context, keyboard tree semantics |
| `category_navigation` | categories are stable primary discovery paths | categories are secondary filters or highly dynamic | visible current location and reachable alternatives |
| `table_or_matrix` | comparison across consistent fields is primary | items are heterogeneous or narrative | column priority, sorting/filtering contract, small-width strategy |

Tabs organize peer views. They do not solve lookup, narrowing, traversal, or rendering scale by themselves.

## Narrowing capabilities

| Capability | Stronger when | Reject or reconsider when | Requirements |
|---|---|---|---|
| `search` | known-item lookup is material and indexable fields exist | users cannot form meaningful queries or backend cannot support expected scope | visible scope, query persistence, loading/no-result/error behavior |
| `autocomplete` | vocabulary is learnable and suggestions reduce query effort | suggestions are misleading, incomplete, or slower than direct entry | keyboard navigation, announcement, exact-query path |
| `facets` | dimensions are understandable, selective, and tied to decisions | fields are merely available metadata or create low-value choices | counts where useful, multi-select semantics, active state, reset |
| `filter_panel` | several secondary dimensions need bounded space | primary dimensions become hidden or mobile interaction cost is excessive | active-filter summary, apply/reset policy, context preservation |
| `filter_chips` | a few high-frequency active dimensions need visible toggling | the set grows, wraps excessively, or becomes the only discovery path | selected state, removal, overflow strategy |
| `sort` | order changes a real decision, comparison, or monitoring task | ordering is cosmetic or users cannot predict its meaning | default rationale, direction, persistence |
| `command_palette` | expert users need fast cross-domain lookup/actions | it hides primary discovery from unfamiliar users | discoverable trigger, scope, keyboard/focus contract |

A facet is not justified by field existence. It must reduce meaningful uncertainty.

## Traversal capabilities

| Capability | Stronger when | Reject or reconsider when | Requirements |
|---|---|---|---|
| `pagination` | deterministic location, shareable pages, comparison batches, exhaustive review, or reliable return matters | exploration is continuous and page boundaries have little meaning | page state, URL policy, total/unknown-total behavior, focus and scroll restoration |
| `load_more` | progressive exploration benefits from explicit user control without page navigation | users need direct page access or exhaustive completion semantics | loading state, retained position, end state, retry |
| `infinite_scroll` | continuous exploration is primary and positional precision is low | stable reference, exhaustive completion, comparison batches, or accessible stopping cannot be satisfied | recovery, stop/end behavior, position restoration, loading announcements, footer access |
| `cursor_navigation` | backend data is mutable or large and stable offsets are unreliable | users require arbitrary page jumps or visible page numbers | opaque cursor state, next/previous semantics, restoration policy |
| `virtualized_collection` | measured rendering pressure exists for large visible collections | it is being used as a substitute for search, filtering, or grouping | keyboard/focus continuity, item measurement, screen-reader strategy, restoration |

Virtualization is a rendering adapter. It does not define how users discover items.

## Disclosure capabilities

| Capability | Stronger when | Risks | Requirements |
|---|---|---|---|
| `preview_limit` | default browse path is too long but representative primary choices can remain visible | hiding important or misleadingly ordered items | rationale, count, accessible reveal path |
| `show_all` | users should explicitly expand a finite hidden remainder | expansion creates an unmanageable page | visible total, reversible action when useful, preserved position |
| `expandable_group` | group-level pressure varies and users can choose relevant groups | repeated controls become noisy or group meaning is weak | per-group state, label/count, keyboard operation |
| `staged_drill_down` | users make sequential narrowing decisions | backtracking loses context or hierarchy is invented | breadcrumb/back behavior, retained parent state |

## Detail access capabilities

| Capability | Stronger when | Reject or reconsider when | Requirements |
|---|---|---|---|
| `inline_expansion` | detail is compact and comparison context should stay visible | rows become unstable or long | one/many-open policy, focus and scroll behavior |
| `detail_drawer` | underlying collection context is valuable and detail fits | deep content, nested navigation, or narrow viewport makes overlay awkward | focus containment/restoration, URL/back policy, mobile substitution |
| `modal_detail` | short interruptive detail or confirmation is appropriate | content is browsable, linkable, or long | dismissal and focus contract |
| `drill_down_page` | detail is deep, linkable, shareable, or task-rich | frequent comparison requires constant return friction | back/return state, canonical URL, preserved query/filter/position |

## Anti-threshold rules

Never use rules such as:

```text
more than 20 items → pagination
more than 5 categories → tabs
mobile → dropdown
large data → infinite scroll
```

Count is evidence, not a verdict. Combine it with:

```text
retrieval task
item heterogeneity
growth and update model
comparison needs
position and shareability needs
meaningful dimensions
backend capability
performance evidence
actual context and input mode
accessibility
```

## Candidate comparison record

```yaml
adapter_candidate:
  capability_family: <organization | narrowing | traversal | disclosure | detail_access>
  candidate: <adapter capability>
  supports_tasks: []
  resolves_pressures: []
  required_constraints: []
  state_requirements: []
  accessibility_requirements: []
  context_fit: []
  costs_and_risks: []
  evidence: []
  verdict: <select | reject | defer | not_applicable>
```

Compare at least one plausible alternative for every material selection.

## Cross-context example

```yaml
strategy:
  default_entry: workflow-first grouped discovery
  known_item_path: search
  narrowing: type and domain filters
  full_inventory: progressive disclosure

adapter_mapping:
  desktop:
    organization: grouped_sections
    disclosure: full routing groups
  mobile:
    organization: grouped_sections
    disclosure: preview_limit + expandable_group

preserved_state:
  - query
  - active filters
  - selected or expanded item
  - group expansion where applicable
  - URL policy
```

The strategy is stable. The disclosure adapter changes because the context pressure changes.

## Handoff rules

After capability selection:

- `design-interaction` defines behavior, states, keyboard, announcements, loading, recovery, and accessibility details;
- `adaptive-component-design` chooses the fit component family and substitution boundary for actual widths/contexts;
- `responsiveness` defines layout mechanics;
- engineering/product adapters map to libraries, APIs, query/index infrastructure, virtualization, and analytics;
- `design-review` verifies the implemented result.
