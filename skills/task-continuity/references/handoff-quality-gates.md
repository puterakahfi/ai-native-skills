# Task Continuity Handoff Quality Gates

Load this reference when work moves to another chat, agent, runtime, model, machine, or teammate.

## Handoff objective

A valid handoff allows the receiver to recover the verified task state and perform the first correct action without access to the prior transcript.

## Required package

```yaml
session_handoff:
  handoff_id: ""
  created_at: ""
  checkpoint_ref: ""
  checkpoint_version: 1

  identity:
    product_ref: ""
    task_or_workflow_ref: ""
    repository_ref: null
    issue_or_task_tracker_ref: null
    active_branch_ref: null
    pull_request_ref: null

  governing_sources:
    - source_ref: ""
      purpose: ""
      revision: null
      required: true

  objective: ""
  acceptance_criteria: []

  verified_state:
    implemented: []
    verified: []
    reviewed: []
    approved: []
    delivered: []
    merged: []
    accepted: []

  remaining_state:
    in_progress: []
    pending: []
    blocked: []
    not_verified: []

  decisions:
    accepted: []
    provisional: []
    conflicted: []

  artifacts_and_evidence: []
  known_failures_and_risks: []
  warnings: []

  next_exact_action:
    action: ""
    required_sources: []
    target_files_or_surfaces: []
    command_or_operation: null
    expected_evidence: []
    completion_condition: ""

  continuity_verdict: ""
```

## Gate 1 — Independent usability

The receiver must not need:

- the previous chat transcript;
- hidden model memory;
- an unexplained person or project nickname;
- an unstated branch, issue, or PR;
- implicit knowledge of what “continue,” “fix it,” or “as discussed” means.

Fail as `HANDOFF_INCOMPLETE` when the package depends on any of these.

## Gate 2 — Verified identity

The package must identify the actual:

- product;
- task or workflow;
- repository when applicable;
- issue or project item when applicable;
- active branch when applicable;
- PR and base branch when applicable.

Use `NOT_VERIFIED` rather than guessing a missing number or branch name.

## Gate 3 — Governing objective

Objective and acceptance criteria must be copied or summarized from current governing sources, not reconstructed from memory.

Include explicit exclusions and non-goals when they prevent scope drift.

## Gate 4 — Evidence-supported state

Every material claim must link to a source or evidence record.

Acceptable examples:

```text
implemented → changed file/commit evidence
verified → named command and exact result
reviewed → review-result reference
approved → authorized approval reference
merged → PR merge evidence
accepted → explicit product-acceptance evidence
```

Do not write “done” as a substitute for these states.

## Gate 5 — Pending work is preserved

The package must disclose:

- unrun tests;
- pending screenshots or rendered checks;
- missing reviews;
- required approvals;
- merge or deployment pending;
- known failures;
- inaccessible sources;
- unresolved decisions;
- blockers and risks.

A handoff that preserves only positive progress creates false completion risk.

## Gate 6 — One next exact action

The first action must be singular, concrete, and checkable.

It should name:

```text
operation
target source/file/surface
required prerequisite
expected evidence
completion condition
```

### Invalid

```text
continue the implementation
finish testing
review the PR
proceed based on previous discussion
```

### Valid

```text
Open PR #49 and inspect the latest Contract integrity workflow run.
If it failed, capture the failing step and exact validator message before
changing files. Expected evidence: run ID, job/step, and failure output.
```

## Gate 7 — Freshness and supersession

Include:

- checkpoint version;
- observed time;
- source revisions when available;
- known stale conditions;
- superseded checkpoint reference;
- continuity verdict.

Do not choose a checkpoint solely because it has the newest timestamp.

## Gate 8 — Authority separation

Keep these independently reported:

```text
execution
validation
gate evaluation
review
approval
delivery
merge
product acceptance
```

A handoff may compose them for readability but must not normalize them into one `approved` or `complete` status.

## Gate 9 — Durable decisions

When an official decision exists only in chat:

1. mark `DURABLE_KNOWLEDGE_GAP`;
2. identify the correct repository artifact, ADR, contract, rule, or blueprint;
3. create or request a promotion action;
4. do not describe the decision as durably established until the artifact exists and is accepted.

## Gate 10 — Receiver verification

The receiver must begin by verifying required sources when:

- the handoff crosses runtime or machine boundaries;
- issue, branch, PR, or artifact state can change;
- the checkpoint is older than the product staleness policy;
- known warnings or conflicts exist;
- current access differs from the sender’s access.

## Compact quality checklist

- [ ] Usable without previous transcript.
- [ ] Product and task identity are explicit.
- [ ] Repository, issue, branch, and PR refs are verified or `NOT_VERIFIED`.
- [ ] Objective and acceptance criteria trace to governing sources.
- [ ] Work state uses evidence-supported semantic states.
- [ ] Pending gates, failures, blockers, and risks are preserved.
- [ ] Decisions include authority and provenance.
- [ ] One exact next action is present.
- [ ] Expected evidence and completion condition are present.
- [ ] Freshness, version, and supersession are explicit.
- [ ] Review, approval, delivery, merge, and acceptance remain separate.
- [ ] Official chat-only decisions have a durable promotion route.
