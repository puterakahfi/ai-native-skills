# Task Continuity Checkpoint Schema

Load this reference when a full, portable checkpoint is required.

## Canonical shape

```yaml
continuity_checkpoint:
  schema_version: "0.1"
  checkpoint_id: ""
  checkpoint_version: 1
  mode: checkpoint
  observed_at: ""
  supersedes_ref: null

  identity:
    product_ref: ""
    app_ref: null
    task_or_workflow_ref: ""
    repository_ref: null
    issue_or_task_tracker_ref: null
    branch_ref: null
    pull_request_ref: null

  objective:
    statement: ""
    source_ref: ""
    authority: ""

  acceptance_criteria:
    - criterion: ""
      status: pending | satisfied_with_evidence | blocked | removed | not_verified
      source_ref: ""
      evidence_refs: []

  work_state:
    planned: []
    attempted: []
    implemented: []
    verified: []
    pending: []
    blocked: []
    abandoned: []

  decisions:
    accepted: []
    provisional: []
    rejected: []
    conflicts: []

  implementation_and_artifacts:
    changed_files: []
    commits: []
    artifact_refs: []
    execution_refs: []

  validation:
    commands_run: []
    test_results: []
    gate_result_refs: []
    review_result_refs: []
    approval_refs: []
    delivery_refs: []

  blockers_and_risks:
    blockers: []
    known_failures: []
    risks: []
    unavailable_sources: []

  next_exact_action:
    action: ""
    required_sources: []
    files_or_surfaces: []
    command_or_operation: null
    expected_evidence: []
    completion_condition: ""

  provenance:
    source_priority_rule: ""
    verified_sources: []
    not_verified_claims: []
    assumptions: []

  freshness_and_version:
    source_revisions: []
    staleness_policy: ""
    stale_conditions: []
    continuity_verdict: VALID | VALID_WITH_WARNINGS | STALE_REFRESH_REQUIRED | CONFLICT_RESOLUTION_REQUIRED | MISSING_CONTEXT | BLOCKED
```

## Work-state item

Each material work item should use:

```yaml
- item: ""
  status: planned | attempted | implemented | verified | pending | blocked | abandoned
  source_ref: ""
  evidence_refs: []
  observed_at: ""
  notes: ""
```

Do not put `reviewed`, `approved`, `delivered`, `merged`, or `accepted` inside the implementation status. Link their owning records separately.

## Decision item

```yaml
- decision: ""
  status: accepted | provisional | rejected | superseded | conflicted
  authority: ""
  source_ref: ""
  supersedes_ref: null
  durable_knowledge_ref: null
  promotion_required: false
```

An accepted decision that exists only in chat must set `promotion_required: true` until it is written to a governing repository artifact.

## Source record

```yaml
- source_ref: ""
  source_type: issue | repository | branch | commit | pull_request | contract | adr | artifact | test | gate | review | approval | delivery | checkpoint | chat_memory | other
  authority: governing | authoritative_runtime | accepted_document | evidence | derived | retrieval_hint | unknown
  revision: null
  observed_at: ""
  verification_method: ""
  status: verified | stale | unavailable | conflicted | not_verified
```

`chat_memory` may be a `retrieval_hint`; it must not be marked governing or authoritative.

## Next exact action test

A next action is acceptable only when another agent can answer all of these:

1. What exact operation happens first?
2. Which source, file, issue, branch, PR, or surface is involved?
3. Which prerequisite must be loaded or checked?
4. What evidence proves the action completed?
5. What must not be inferred from that evidence?

Reject:

```text
continue implementation
finish the remaining work
check everything
proceed as discussed
```

Prefer:

```text
Open PR #49 and inspect the Contract integrity workflow. If it failed,
record the exact failing validator and patch only the contract or test
responsible. Evidence: workflow run, failing step, and updated validation result.
```

## Minimum checkpoint gate

A checkpoint is incomplete when any required item is absent:

- task identity;
- governing objective;
- acceptance criteria or an explicit missing-context finding;
- evidence-supported work state;
- pending and blocked work;
- known failures;
- one next exact action;
- expected evidence;
- checkpoint version and observed time;
- continuity verdict.
