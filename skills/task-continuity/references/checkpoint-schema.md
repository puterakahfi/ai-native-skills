# Task Continuity Checkpoint Schema

Use this schema when the checkpoint must survive a new chat, agent, runtime, or machine.

```yaml
checkpoint:
  checkpoint_id: ""
  checkpoint_version: 1
  observed_at: ""
  supersedes: null

  identity:
    product_ref: ""
    task_or_workflow_ref: ""
    repository_ref: ""
    issue_ref: ""
    branch_ref: ""
    pull_request_ref: ""

  objective: ""
  acceptance_criteria: []

  work_state:
    planned: []
    attempted: []
    implemented: []
    verified: []
    pending: []
    blocked: []
    abandoned: []

  decisions:
    - decision: ""
      status: accepted | provisional | superseded | NOT_VERIFIED
      source_ref: ""
      authority: ""

  implementation_and_artifacts:
    changed_files: []
    commits: []
    artifacts: []

  validation:
    - command_or_gate: ""
      exact_result: ""
      status: PASS | FAIL | NOT_EXECUTED | NOT_VERIFIED
      evidence_ref: ""

  blockers_and_risks: []
  known_failures: []

  next_exact_action: ""
  expected_evidence: []

  provenance:
    source_refs: []
    unavailable_sources: []
    assumptions: []

  freshness:
    source_revisions: {}
    staleness_rule: ""
```

## Rules

- Every material claim has a source or `NOT_VERIFIED`.
- Record only the strongest status supported by evidence.
- `implemented`, `verified`, `reviewed`, `approved`, `merged`, and `accepted` are separate.
- One checkpoint names exactly one next action.
- The next action states the evidence it must produce.
- Missing source access is explicit.
- Supersession preserves old checkpoint identity; it never rewrites history.

## Invalid checkpoint signals

Reject or downgrade a checkpoint when:

- task identity or acceptance criteria are absent;
- repository or issue claims cannot be resolved;
- memory is presented as authority;
- `done` is used without a supported state;
- known failures or pending gates are hidden;
- the next action is vague;
- freshness and revision data are missing.
