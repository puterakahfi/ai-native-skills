# Collection State and Verification

Load this reference after the discovery strategy and adapter capability requirements are known.

A context-specific adapter is acceptable only when it preserves the collection meaning and the user context required by the product task.

## Collection state contract

Record only applicable fields, but justify every omission.

```yaml
collection_state_contract:
  query_state:
    value: <state or not_applicable>
    persistence: <none | session | url | stored>

  active_filters:
    values: []
    application_mode: <instant | explicit_apply | mixed>
    reset_behavior: <behavior>

  sort_state:
    value: <state or not_applicable>
    default_rationale: <reason>

  selected_group_or_view:
    value: <state or not_applicable>

  current_position_or_cursor:
    value: <page | offset | cursor | item anchor | not_applicable>
    restoration: <behavior>

  expanded_or_selected_item:
    value: <state or not_applicable>
    one_or_many_open: <policy>

  return_and_restore_behavior:
    browser_back: <behavior>
    refresh: <behavior>
    revisit: <behavior>

  url_or_shareable_state_policy:
    query: <included | excluded | not_applicable>
    filters: <included | excluded | not_applicable>
    sort: <included | excluded | not_applicable>
    group_or_view: <included | excluded | not_applicable>
    position: <included | excluded | not_applicable>
    selected_item: <included | excluded | not_applicable>

  analytics_identity:
    collection: <stable identity>
    adapters: []
    events: []

  accessibility_relationships:
    controls_to_results: <relationship>
    result_count_announcement: <policy>
    loading_announcement: <policy>
    focus_after_change: <policy>
```

## State equivalence across adapters

Different adapters may represent the same strategy.

```text
desktop tabs → mobile select
full desktop grouped registry → mobile group preview
page-based results → compact next/previous controls
side filter panel → mobile filter sheet
inline detail → mobile full-screen detail
```

The substitution passes only when applicable state remains equivalent:

- same available choices and taxonomy meaning;
- same query/filter/sort semantics;
- same selected value or view;
- same item identity and action meaning;
- truthful result count and loading state;
- preserved URL/history policy;
- stable analytics identity;
- equivalent accessible names and relationships;
- predictable focus and return behavior.

Do not preserve visual shape at the cost of product meaning. Do not preserve product meaning only in theory while losing state in implementation.

## URL and history policy

URL addressability is stronger when users need:

- sharing or bookmarking;
- deterministic return;
- browser back/forward behavior;
- multi-step comparison;
- support/debug reproduction;
- saved searches or views.

Not every transient disclosure state belongs in the URL. Decide deliberately.

```yaml
url_state_decision:
  field: <query | filter | sort | group | position | item | expansion>
  user_value: <reason>
  cost_or_risk: <reason>
  policy: <include | exclude | product_defined>
```

## Verification matrix

### Realistic data

Verify:

- current and highest expected item counts;
- expected growth and update frequency;
- longest titles and labels;
- ambiguous or duplicate names;
- sparse and dense groups;
- zero, one, and many results;
- heterogeneous item descriptions and actions;
- localization/text expansion when supported.

### Discovery tasks

Verify each declared mode:

- lookup reaches a known item efficiently;
- browse communicates what exists without an excessive default journey;
- narrowing visibly changes and explains the result set;
- comparison preserves relevant fields and context;
- monitoring handles incoming items truthfully;
- resume restores the required state and position;
- hierarchy preserves parent-child context.

### Interaction states

Verify applicable states:

```text
initial
loading
partial or incremental loading
success
empty collection
no matching result
error
retry
stale or refreshed data
selected
expanded
end of collection
permission or unavailable state
```

### Context boundaries

Use actual product contexts and evidence around transition points:

- widest failing and narrowest passing context;
- immediately before and after component substitution;
- intermediate widths where behavior changes non-linearly;
- touch, pointer, keyboard, and assistive-technology paths;
- browser back, refresh, deep link, and return from detail;
- zoom/text scaling and orientation where applicable.

Device names are samples, not canonical breakpoints.

### Performance

Do not claim performance from item count or source structure.

Measured evidence may include:

- query latency and result timing;
- render and interaction responsiveness;
- memory/DOM pressure;
- incremental loading behavior;
- cancellation and retry;
- virtualization behavior;
- cache/staleness policy.

Virtualization can pass performance while discovery still fails. Search and facets can pass discovery while backend performance still fails. Report them separately.

## Evidence statuses

```text
PASS
  applicable task and state are verified with appropriate evidence

FAIL
  evidence shows the strategy or adapter breaks an applicable requirement

PARTIAL
  some applicable contexts or states pass while others fail or remain incomplete

NOT_VERIFIED
  evidence is unavailable or cannot prove the claim

NOT_APPLICABLE
  the requirement does not apply to the declared strategy and task
```

A screenshot can support visual hierarchy and static discoverability. It cannot prove keyboard operation, state restoration, dynamic loading, history behavior, or measured performance.

## Acceptance handoff

```yaml
collection_discovery_acceptance:
  strategy_reference: <artifact>
  retrieval_modes_verified: []
  pressures_resolved: []

  adapter_mapping:
    contexts: []
    substitutions: []
    boundaries: []

  state_equivalence:
    query: <status>
    filters: <status>
    sort: <status>
    group_or_view: <status>
    position_or_cursor: <status>
    selected_item: <status>
    url_and_history: <status>
    analytics: <status>
    accessibility: <status>

  realistic_data_results: []
  interaction_results: []
  performance_results: []
  evidence_gaps: []
  design_review_route:
    review_depth: focused
    target_regions: []
    adjacent_regressions: []
```

## Stop conditions

Do not approve when:

- a primary retrieval mode has no verified path;
- filters or categories are unreachable in a required context;
- adapter substitution resets required query/filter/sort/selection state;
- back or detail return loses required position;
- infinite loading has no stop, recovery, end, or accessibility behavior;
- pagination breaks filter/query URL state or restoration;
- result count, loading, empty, and error states are misleading;
- a performance or runtime claim lacks measured evidence;
- acceptance relies only on source inspection.
