# Work-Item Identity and Deduplication

Use this reference before an `issue_plan` is executed against a tracker.

## Purpose

A proposed task name is not proof that the work is new. Establish one canonical work-item owner before creating another issue, ticket, or draft.

The goal is not to eliminate every similar item. The goal is to distinguish:

```text
same owner
related but separate scope
superseded history
truly new work
unverified uniqueness
```

## Required identity input

```yaml
proposed_work_item:
  canonical_task_id: ""
  work_item_type: feature | task | spike | bug
  parent_ref: ""
  objective: ""
  acceptance_criteria: []
  repository_or_tracker_scope: ""
  primary_entities: []
  symptoms_or_outcomes: []
  known_related_refs: []
```

Missing identity, objective, parent, or acceptance scope is a planning gap. Do not compensate with title-only search.

## Search matrix

Use multiple independent search angles:

```text
1. exact canonical task ID or proposed identifier
2. primary capability, product, component, or provider names
3. observed symptom or requested outcome
4. synonyms, legacy terms, abbreviations, and alternate wording
5. parent epic, feature, incident, migration, or workstream references
6. known related issues, PRs, decisions, and supersession records
7. recent tracker items when search indexing or recall is uncertain
8. open and closed items when historical work may still be authoritative
```

An empty result from one query is not evidence that the work item is unique.

When tracker search is known to be incomplete, supplement it with recent-item listing, parent-thread inspection, project-board inspection, or another verified source. Record the limitation.

## Candidate comparison

Open plausible candidates and compare:

```text
canonical identity
objective
scope boundary
acceptance criteria
source case or observed failure
parent and dependency position
current authority
status, supersession, and closure reason
unique evidence owned by each item
```

Title similarity alone cannot prove duplication. Different titles cannot prove independence.

## Identity verdicts

### `NEW`

No existing item owns the same objective and acceptance boundary after adequate search coverage.

Action:

```text
create the planned item
record duplicate-search evidence
link related but non-owning work
```

### `EXISTING_OWNER`

An existing item owns the same objective and acceptance boundary.

Action:

```text
reuse, update, or link the existing owner
do not create parallel canonical ownership
add new evidence to the existing item when authorized
```

### `OVERLAP_REQUIRES_SCOPE_SPLIT`

Items share a source case or capability, but each needs a distinct acceptance boundary.

Action:

```text
define parent/child or sibling boundaries
state non-overlapping acceptance criteria
record dependencies
then create only the missing scope
```

### `SUPERSEDED_OWNER`

A historical item covered the work but no longer has current authority because a newer contract, architecture, or explicit decision superseded it.

Action:

```text
identify the current owner
preserve historical provenance
record why the older item does not block new work
```

### `DUPLICATE`

A parallel item was proposed or created for scope already owned elsewhere.

Action before creation:

```text
do not create it
route work to the canonical owner
```

Recovery after accidental creation:

```text
transfer unique evidence
update dependent references
record canonical owner and supersession
close the duplicate only with tracker authority
preserve any diagnostic artifact that remains useful
```

### `NOT_VERIFIED`

Search access, indexing, tracker scope, or authority is insufficient to determine uniqueness.

Action:

```text
block write execution
or create only a clearly provisional draft when product policy explicitly allows it
state the missing evidence and next exact verification action
```

Do not silently convert `NOT_VERIFIED` into `NEW`.

## Decision record

```yaml
work_item_identity_decision:
  proposed_canonical_task_id: ""
  verdict: NEW | EXISTING_OWNER | OVERLAP_REQUIRES_SCOPE_SPLIT | SUPERSEDED_OWNER | DUPLICATE | NOT_VERIFIED
  canonical_owner_ref: null
  candidate_refs: []
  search_queries: []
  tracker_states_inspected: []
  comparison_summary: []
  search_limitations: []
  scope_split: []
  evidence_transfer_required: []
  next_exact_action: ""
```

## Quality gates

```text
work_item_identity_is_explicit_before_issue_plan_execution
multi_query_duplicate_search_covers_identity_entities_symptoms_synonyms_and_parent_refs
open_and_closed_tracker_state_is_considered_when_relevant
candidate_matches_are_inspected_by_scope_and_acceptance_not_title_only
empty_single_query_result_does_not_prove_uniqueness
existing_canonical_owner_is_reused_or_extended_instead_of_duplicated
scope_split_is_explicit_when_related_work_is_not_fully_duplicate
accidental_duplicate_recovery_transfers_unique_evidence_and_preserves_provenance
duplicate_search_limitations_are_disclosed_as_not_verified
```

## Counterexamples

### Same symptom, different scope

A monitoring issue and a root-cause remediation issue may share an incident but have different independently testable acceptance criteria. Use `OVERLAP_REQUIRES_SCOPE_SPLIT`, not automatic duplication.

### Same title, superseded architecture

A closed issue under an obsolete architecture may be historical rather than current authority. Use `SUPERSEDED_OWNER` or `NEW` with explicit provenance.

### Different title, same owner

“Upload API returns 503” and “Object storage saturation makes uploads unavailable” may describe the same canonical incident/remediation. Inspect the body and acceptance criteria before deciding.

## Handoff rule

The issue-tracker adapter executes the approved identity decision. It does not invent uniqueness, close duplicates without authority, or choose a canonical owner from title similarity alone.
