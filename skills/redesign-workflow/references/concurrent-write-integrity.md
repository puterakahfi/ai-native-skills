# Concurrent Write Integrity

Load this reference for repository-backed redesign runs when more than one agent, automation, user session, or integration may update the same branch.

## Purpose

A correct scope decision can still be corrupted when another writer changes the branch between inspection and patch application.

```text
capture expected head
→ prepare patch from that head
→ verify branch still matches expected head
→ write by compare-and-swap / fast-forward
→ if head moved, inspect delta before any retry
```

Never enter a ping-pong loop in which agents repeatedly add and remove the same file or behavior.

## Lease model

Before each repository mutation, record:

```yaml
write_lease:
  repository: <owner/repo>
  branch: <branch>
  expected_head: <sha inspected by this agent>
  baseline_ref: <delivery baseline>
  intended_paths: []
  decision_or_defect: <why this write is needed>
  acquired_at_phase: <phase>
```

Immediately before writing, resolve the current branch head again.

```text
current_head == expected_head
  → patch or fast-forward is eligible

current_head != expected_head
  → lease invalid
  → do not write from stale assumptions
```

Contents API writes, Git ref updates, full-tree commits, submodule pointer updates, and generated artifact uploads all require this guard.

## Head drift classification

When the lease is invalid, compare `expected_head...current_head` and classify the delta:

```text
COMPATIBLE
  Concurrent changes are in scope and do not conflict with the current decision.
  Re-read affected files, rebuild the patch on current head, and obtain a new lease.

DECISION_CONFLICT
  Concurrent changes reverse or materially alter an approved scope, lock,
  route, component, content, or acceptance decision.

SCOPE_EXPANSION
  Concurrent changes introduce paths, products, routes, or dependencies
  outside confirmed scope.

OVERLAPPING_IMPLEMENTATION
  Both writers changed the same file/region for compatible goals,
  but the patch must be reconciled rather than replayed blindly.

UNKNOWN
  Intent or ownership cannot be established.
```

## Required behavior

```text
COMPATIBLE
  → absorb delta
  → re-run relevant scope and preservation checks
  → create a new expected-head lease

OVERLAPPING_IMPLEMENTATION
  → inspect both variants
  → synthesize one patch under the governing owner
  → verify affected behavior

DECISION_CONFLICT / SCOPE_EXPANSION / UNKNOWN
  → stop repository writes
  → report expected and actual heads
  → identify conflicting paths and decisions
  → route to owner or orchestration coordination
  → state CONCURRENT_WRITE_BLOCKED
```

Do not assume the newest commit is correct merely because it is newer. Do not discard it merely because it conflicts. Re-evaluate it against baseline, confirmed scope, locks, and owner decisions.

## Anti-ping-pong rule

Track repeated contention by decision and path:

```yaml
contention:
  key: <decision + path set>
  observed_cycles: 0
  writers_or_sources: []
  head_sequence: []
```

```text
same decision/path reversed twice
  → stop automatic writes
  → CONCURRENT_WRITE_BLOCKED
  → require one declared owner or isolated branch
```

A third automated reversal is forbidden. This limit is independent from the two-patch-per-region design correction limit.

## Prohibited behavior

```text
❌ force-push over an uninspected concurrent commit
❌ retry the same stale Contents API update with a new blob SHA only
❌ keep updating a parent submodule pointer while the child branch is moving
❌ overwrite PR descriptions to hide the active decision conflict
❌ call the branch clean using a manifest from an older head
❌ treat a fast-forward failure as a transport error and blindly retry
❌ keep running design review against an artifact whose head is not stable
```

## Isolation options

Choose the smallest safe coordination action:

```text
one writer is authoritative
  → declare owner and pause other writers

both changes are valid but separate
  → split into separate branches/PRs

one change is a new feature
  → route through new-feature-workflow

parent pointer follows moving child
  → stop pointer updates until child head is frozen for verification

unclear ownership
  → leave draft, report blocker, request owner decision
```

Do not create a new branch solely to conceal unresolved product ownership. The branch split must represent a real lifecycle or scope boundary.

## Output contract

```yaml
concurrency_report:
  repository: <repo>
  branch: <branch>
  expected_head: <sha>
  actual_head: <sha>
  drift_detected: true
  delta:
    changed_paths: []
    classification: <COMPATIBLE | DECISION_CONFLICT | SCOPE_EXPANSION |
                     OVERLAPPING_IMPLEMENTATION | UNKNOWN>
    decision_conflicts: []
  contention:
    observed_cycles: <N>
    head_sequence: []
  action: <rebase_and_retry | reconcile | split | handoff | stop>
  status: PASS | CONCURRENT_WRITE_BLOCKED
```

`PASS` means the final write was based on the inspected current head. It does not mean design or scope acceptance passed.

## Workflow placement

```text
INITIALIZE
  capture branch and initial head

SPEC CONFIRMATION
  declare ownership and expected scope

BEFORE EVERY WRITE
  acquire/validate expected-head lease

ON DRIFT
  classify concurrent delta before retry

VERIFICATION
  prove final artifact and scope report refer to actual current head

DELIVERY
  block when head is moving or manifest is stale
```

## Final guard

```text
□ Every write names the expected head it was prepared from.
□ Current head was re-resolved immediately before mutation.
□ Head drift was inspected, not blindly overwritten.
□ Scope and preservation were rechecked after compatible drift.
□ Decision conflicts stopped automatic writes.
□ Two reversals triggered anti-ping-pong stop.
□ Parent pointers were not chased while the child head remained unstable.
□ Delivery artifacts and PR text reference the actual stable head.
```
