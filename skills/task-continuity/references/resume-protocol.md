# Task Continuity Resume Protocol

Load this reference when a prior checkpoint must be compared with current repositories, issues, branches, pull requests, artifacts, validation, review, approval, or delivery state.

## Principle

```text
candidate checkpoint
  ≠ current task truth

candidate checkpoint
  + current authoritative sources
  + conflict and freshness analysis
  = verified resume context
```

## Ordered protocol

### 1. Identify the candidate checkpoint

Record:

- checkpoint ID and version;
- observed time;
- product and task identity;
- claimed repository, issue, branch, and PR refs;
- source revisions captured by the checkpoint;
- supersession reference, if any.

When multiple checkpoints exist, do not select only by timestamp. Prefer the latest non-superseded checkpoint whose authority and identity match the governing task.

### 2. Resolve current governing sources

Inspect all applicable sources:

```text
latest explicit task instruction
active issue or project item
current acceptance criteria
repository default and active branch
commit and changed-file evidence
pull request state and base branch
artifact and execution records
validation and gate results
review results
approval records
delivery and merge records
product decisions, ADRs, and contracts
```

Unavailable sources must be named explicitly.

### 3. Compare identity

Verify:

- same product;
- same task or workflow;
- same target repository;
- branch and PR still exist when required;
- active base branch is still valid;
- task was not cancelled, superseded, split, or merged into another work item.

An unresolved material identity mismatch returns `BLOCKED`.

### 4. Compare objective and scope

Compare checkpoint objective and acceptance criteria with the current governing task.

Classify each difference:

| Classification | Meaning |
|---|---|
| `UNCHANGED` | Same meaning and authority |
| `ADDITIVE` | New accepted criterion or constraint |
| `REDUCED` | Scope was explicitly narrowed |
| `REMOVED` | Criterion no longer applies |
| `SUPERSEDED` | New task/decision replaces old scope |
| `CONFLICTED` | Sources disagree and authority is unresolved |

`CONFLICTED` objective or acceptance criteria blocks execution.

### 5. Compare task state

For each claimed work item, verify the strongest supported status:

```text
planned
attempted
implemented
verified
gate passed
reviewed
approved
delivered
merged
accepted
```

Downgrade unsupported claims rather than preserving optimistic wording.

Examples:

- branch exists with changed files, no tests → `implemented`, validation pending;
- test command succeeded → named validation result only;
- PR merged → `merged`, release and acceptance unresolved unless separately evidenced;
- review comment says acceptable → review result only, unless an authorized approval record exists.

### 6. Detect freshness and supersession

A checkpoint is stale when any material source changed after observation:

- issue objective or acceptance criteria changed;
- branch head changed;
- PR state or base changed;
- referenced artifact or validation was replaced;
- review or approval state changed;
- task moved to a successor issue;
- required source is no longer resolvable.

A stale checkpoint may be refreshed. A superseded checkpoint remains in history and must not be rewritten as current.

### 7. Detect conflicts and gaps

Produce explicit findings:

```yaml
findings:
  - type: IDENTITY_MISSING | SOURCE_UNAVAILABLE | STALE_CHECKPOINT | SUPERSEDED_CHECKPOINT | STATUS_CONFLICT | SCOPE_CONFLICT | FALSE_COMPLETION_RISK | HANDOFF_INCOMPLETE | DURABLE_KNOWLEDGE_GAP
    subject_ref: ""
    checkpoint_claim: ""
    current_source_state: ""
    authority_analysis: ""
    impact: ""
    correction_route: ""
```

Never repair missing source state by silently creating a branch, issue, commit, PR, decision, artifact, test, review, or approval.

### 8. Refresh context

When the verified state differs from the checkpoint:

1. create a successor checkpoint;
2. mark the old checkpoint superseded or stale;
3. update the active context pack through `context-manager`;
4. preserve unresolved warnings;
5. define the next exact action from current state.

### 9. Issue verdict

#### `VALID`

All required sources resolve, identity matches, no material stale or conflicting state exists, and the next action is current.

#### `VALID_WITH_WARNINGS`

Execution can continue, but non-blocking warnings or unavailable optional sources remain.

#### `STALE_REFRESH_REQUIRED`

Material sources changed, but authority is clear and a refreshed checkpoint can be produced.

#### `CONFLICT_RESOLUTION_REQUIRED`

Governing sources disagree about scope, state, or authority.

#### `MISSING_CONTEXT`

Required task context is absent or inaccessible.

#### `BLOCKED`

Execution must not continue because identity, authority, required acceptance criteria, or safety-critical state cannot be resolved.

## Resume output

```yaml
resume_context:
  checkpoint_ref: ""
  verdict: ""
  verified_identity: {}
  governing_objective: {}
  current_acceptance_criteria: []
  verified_work_state: {}
  source_comparison: []
  findings: []
  refreshed_context_refs: []
  next_exact_action: ""
  expected_evidence: []
  prohibited_inferences: []
```

## Stop conditions

Do not hand off to execution when:

- issue or task identity is unresolved;
- objective or acceptance criteria conflict materially;
- the claimed branch/PR/commit cannot be verified and is required;
- the next action depends on unverified completion;
- a pending review, approval, migration, deployment, or destructive action requires authority;
- source access is insufficient to establish safe state.
