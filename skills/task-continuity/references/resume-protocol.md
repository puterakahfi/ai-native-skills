# Verified Resume Protocol

Resume validates a checkpoint against current sources before execution.

## Ordered protocol

1. Load the latest candidate checkpoint and its supersession chain.
2. Resolve the current governing instruction, issue, acceptance criteria, repository, branch, PR, artifacts, and gates.
3. Compare task identity, objective, scope, revisions, and status claims.
4. Classify each mismatch as missing, stale, superseded, conflicting, or non-blocking warning.
5. Refresh the context pack from current authoritative sources.
6. Produce a continuity validation verdict.
7. Hand off to the governing workflow only when required context is sufficient.

## Comparison matrix

| Checkpoint claim | Current evidence | Classification | Action |
|---|---|---|---|
| PR open | PR merged | `SUPERSEDED_CHECKPOINT` | record merged state; do not repeat merge |
| branch exists | branch absent and no successor | `IDENTITY_MISSING` | `MISSING_CONTEXT`; block |
| full redesign | issue limits hierarchy refinement | `SCOPE_CONFLICT` | governing issue wins; re-plan |
| build passed | review/approval absent | `FALSE_COMPLETION_RISK` | preserve build result; keep later gates pending |
| official decision only in chat | no durable record | `DURABLE_KNOWLEDGE_GAP` | create promotion request |

## Verdict rules

```text
VALID
  required sources agree and next action is supported

VALID_WITH_WARNINGS
  non-blocking stale or unavailable evidence is disclosed

STALE_REFRESH_REQUIRED
  source revisions changed but authority and scope remain resolvable

CONFLICT_RESOLUTION_REQUIRED
  governing sources disagree materially

MISSING_CONTEXT
  required task identity or evidence cannot be resolved

BLOCKED
  execution would require invention, unauthorized override, or skipped gate
```

## Non-negotiable protections

- Current authoritative sources override an older checkpoint.
- A newer timestamp does not override a higher-authority source.
- Missing branch, PR, commit, artifact, or command evidence remains `NOT_VERIFIED`.
- Completed verified actions are not repeated.
- Pending validation, review, approval, delivery, and acceptance are not skipped.
- Conversation memory cannot broaden issue scope.
- Resume ends with one exact next action and expected evidence.

## Output

```yaml
continuity_validation:
  verdict: VALID
  checkpoint_ref: "checkpoint-id@version"
  verified_sources: []
  stale_sources: []
  superseded_sources: []
  conflicts: []
  missing_context: []
  warnings: []
  refreshed_state: {}
  next_exact_action: ""
  expected_evidence: []
```
