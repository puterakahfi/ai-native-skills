# Collection Diagnosis and Discovery Strategy

Load this reference when the collection shape, retrieval task, or discovery pressure is not yet explicit.

## 1. Collection inventory

Record evidence before selecting a pattern.

```yaml
collection_inventory:
  product_intent: <why the collection exists>
  current_volume: <known count or range>
  expected_growth: <none | slow | medium | rapid | unknown>
  update_frequency: <static | periodic | continuous | unknown>
  item_homogeneity: <homogeneous | mixed | highly heterogeneous>

  item_schema:
    identity_fields: []
    title_fields: []
    descriptive_fields: []
    status_fields: []
    comparable_fields: []
    searchable_fields: []
    filterable_fields: []
    sortable_fields: []
    hierarchy_fields: []

  taxonomy:
    grouping_dimensions: []
    hierarchy: <flat | nested | mixed | unknown>
    stability: <stable | dynamic | unknown>
    owner: information-architecture

  target_contexts: []
  input_modes: []
  constraints:
    backend: []
    performance: []
    accessibility: []
    localization: []
    preservation: []

  evidence_available: []
  unknowns: []
```

Do not infer filterability merely because a field exists. A useful facet must be understandable, selective, and relevant to a user decision.

## 2. Retrieval modes

Name the primary and secondary user modes.

| Mode | User intent | Typical evidence |
|---|---|---|
| `known_item_lookup` | Find a known item or exact match | exact names, IDs, SKUs, titles, frequent direct lookup |
| `exploratory_browse` | Discover what exists | open-ended sessions, inspiration, unfamiliar inventory |
| `narrow_and_refine` | Reduce a broad set to a relevant subset | meaningful dimensions, repeated filtering, query refinement |
| `compare` | Evaluate alternatives systematically | stable comparable fields, shortlist, batch review |
| `monitor_updates` | Consume newly arriving items | chronological or priority updates, continuous ingestion |
| `resume_prior_context` | Return to a prior position or state | repeated sessions, saved query, stable position, back navigation |
| `hierarchical_drill_down` | Navigate a real parent-child structure | folders, org trees, nested taxonomies, dependency trees |

A collection may support several modes. Prioritize them rather than averaging them together.

## 3. Discovery pressures

Use pressures to describe a failing or emerging task, not merely a large number.

| Pressure | Evidence | Common risk |
|---|---|---|
| `LOOKUP_PRESSURE` | Users know what they want but cannot reach it directly | excessive browsing, weak search scope |
| `BROWSE_OVERLOAD` | Default journey exposes too many items or groups before the next decision | scanning fatigue, abandonment |
| `NARROWING_GAP` | Users cannot reduce a broad result set by meaningful dimensions | repeated query reformulation |
| `COMPARISON_PRESSURE` | Users need stable side-by-side or batch evaluation | lost context, poor field alignment |
| `HIERARCHY_PRESSURE` | Parent-child meaning is hard to navigate | flat presentation of nested data |
| `CONTEXT_LOSS_RISK` | Back, refresh, sharing, or adapter substitution loses state or position | repeated work, distrust |
| `GROWTH_PRESSURE` | Current pattern will degrade as inventory grows | future overflow, rendering cost |
| `UPDATE_STREAM_PRESSURE` | New items arrive continuously | stale ordering, uncontrolled loading |
| `PERFORMANCE_PRESSURE` | Rendering or querying exceeds measured budgets | latency, memory, blocked interaction |
| `CROSS_CONTEXT_PRESSURE` | A fit pattern in one context becomes awkward in another | hidden options, long mobile journeys |
| `NO_MATERIAL_DISCOVERY_PRESSURE` | Existing strategy satisfies the tasks | unnecessary redesign |

Rules:

- Item count alone is not a pressure.
- Multiple symptoms may share one pressure.
- Unknown evidence remains unknown.
- `PERFORMANCE_PRESSURE` requires measured or technically grounded evidence.

## 4. Strategy record

Define the model before naming adapters.

```yaml
collection_discovery_strategy:
  primary_retrieval_mode: <mode>
  secondary_retrieval_modes: []
  diagnosed_pressures: []

  default_entry_strategy: <routed browse | search-first | category-first | feed | other>
  organization_strategy: <flat | grouped | hierarchical | comparison-oriented | mixed>
  browse_search_balance: <strategy>
  narrowing_strategy: <strategy or not applicable>
  sorting_strategy: <strategy or not applicable>
  traversal_strategy: <strategy>
  progressive_disclosure_strategy: <strategy>
  detail_access_strategy: <strategy>

  context_and_state_preservation:
    required_state: []
    restoration_behavior: <behavior>
    shareability: <policy>

  constraints: []
  adapter_capability_requirements: []
  rejected_alternatives_and_tradeoffs: []
  verification_plan: []
```

## 5. Example diagnoses

### Capability registry

```text
Evidence:
94 entries, 9 workflows, 6 meta-skills, 79 atomic skills.
Desktop grouped rows scan well. Mobile default journey is too long.
Known-item lookup and routed browsing both matter.

Diagnosis:
LOOKUP_PRESSURE + BROWSE_OVERLOAD + CROSS_CONTEXT_PRESSURE

Strategy:
workflow-first grouped discovery + search/filter path + progressive mobile group preview

Not implied:
pagination, tabs for all items, or hiding the full catalog
```

### Procurement results

```text
Evidence:
About 1,000 results; exact SKU lookup, filtering, comparison, shared URLs,
return to known position, complete review batches.

Diagnosis:
LOOKUP_PRESSURE + NARROWING_GAP + COMPARISON_PRESSURE + CONTEXT_LOSS_RISK

Strategy:
search + meaningful facets + sort + deterministic traversal + persistent URL state
```

### Inspiration feed

```text
Evidence:
Continuous updates, casual exploration, saves, low page-number value,
but position recovery and accessible stopping behavior are required.

Diagnosis:
UPDATE_STREAM_PRESSURE + CONTEXT_LOSS_RISK + PERFORMANCE_PRESSURE

Strategy:
continuous exploration with explicit recovery, stop, loading, and accessibility contracts
```

### Knowledge base

```text
Evidence:
Four stable peer content types, thousands of articles, exact search,
owner/status filters, detail pages.

Diagnosis:
LOOKUP_PRESSURE + NARROWING_GAP

Strategy:
visible stable category switching plus independent search, filters, and detail access
```

## Completion check

Before adapter selection, verify:

- inventory and item schema are explicit;
- primary and secondary retrieval modes are named;
- pressures are causal and evidence-backed;
- taxonomy meaning remains owned by information architecture;
- discovery strategy is described without relying on a component name;
- preservation requirements and unknowns are recorded.
