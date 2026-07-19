# Concurrent Write Integrity

Load this reference for repository-backed redesign runs when more than one agent, automation, user session, or integration may update the same branch.

Load `decision-provenance` whenever head drift changes or disputes scope, locks, route, ownership, content, acceptance, or approval decisions.

## Purpose

A correct scope decision can still be corrupted when another writer changes the branch between inspection and patch application.

```text
capture expected head
→ prepare patch from that head
→ verify branch still matches expected head
→ write by compare-and-swap / fast-forward
→ if head moved, inspect delta and decision provenance before any retry
```

Never enter a ping-pong loop in which agents repeatedly add and remove the same file, route, content, or behavior.

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
  decision_record_ids: []
  write_owner: <single active writer or coordination owner>
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
  Concurrent changes are in scope and do not conflict with the current verified decision.

DECISION_CONFLICT
  Concurrent changes reverse or materially alter a verified scope, lock,
  route, component, content, ownership, or acceptance decision.

SCOPE_EXPANSION
  Concurrent changes introduce paths, products, routes, or dependencies
  outside verified scope.

OVERLAPPING_IMPLEMENTATION
  Both writers changed the same file/region for compatible verified goals,
  but the patch must be reconciled rather than replayed blindly.

UNKNOWN
  Intent, ownership, causal need, or decision provenance cannot be established.
```

## Decision authority on drift

Do not choose a winner from commit recency, confidence, PR prose, or agent identity.

```text
newest commit exists
  → proves branch state only
  → does not prove authority

PR body or commit message says “user approved”
  → AGENT_AUTHORED_SUMMARY unless an attributable owner source is linked

current direct owner instruction explicitly supersedes old agent inference
  → verified newer decision may control the next lease

multiple authoritative sources conflict without supersession
  → DECISION_CONFLICT
  → PROVENANCE_BLOCKED
  → stop writes

source is understood but policy/another owner approval remains
  → ROUTE_FOR_APPROVAL
  → preserve current safe state
```

Every decision-sensitive drift report must include the decision record IDs used to classify it.

## Required behavior

```text
COMPATIBLE
  → absorb delta
  → re-run scope, provenance, and preservation checks
  → create a new expected-head lease

OVERLAPPING_IMPLEMENTATION
  → inspect both variants
  → confirm one governing decision and owner
  → synthesize one patch on current head
  → verify affected behavior

DECISION_CONFLICT
  → stop repository writes
  → emit decision provenance report
  → coordinate explicit supersession or split lifecycle

SCOPE_EXPANSION
  → stop repository writes
  → route new product/feature work separately or obtain bounded approval

UNKNOWN
  → stop and hand off
```

Do not discard a concurrent commit merely because it conflicts. Preserve valid work in its rightful lifecycle while preventing it from silently changing the current delivery.

## Anti-ping-pong rule

Track repeated contention by decision and path:

```yaml
contention:
  key: <decision + path set>
  observed_cycles: 0
  writers_or_sources: []
  decision_record_ids: []
  head_sequence: []
```

```text
same decision/path reversed twice
  → stop automatic writes
  → CONCURRENT_WRITE_BLOCKED
  → require one declared owner, explicit authoritative decision,
    or isolated lifecycle branch
```

A third automated reversal is forbidden. This limit is independent from the two-patch-per-region design correction limit.

## Prohibited behavior

```text
❌ force-push over an uninspected concurrent commit
❌ retry the same stale Contents API update with a refreshed blob SHA only
❌ keep updating a parent submodule pointer while the child branch is moving
❌ treat a PR body written by an agent as owner approval
❌ choose the latest commit as authoritative without decision provenance
❌ overwrite PR descriptions to hide an active conflict
❌ call the branch clean using a manifest from an older head
❌ treat a fast-forward failure as a transport error and blindly retry
❌ keep running acceptance review against an unstable artifact
```

## Isolation options

Choose the smallest safe coordination action:

```text
one writer and one verified decision are authoritative
  → declare owner and pause other writers

both changes are valid but belong to separate lifecycle decisions
  → preserve and split into separate branches/PRs/tickets

one change is a new feature or product route
  → route through new-feature-workflow or product-development-workflow

parent pointer follows moving child
  → stop pointer updates until the child head and decision ledger are frozen

unclear authority or conflicting owner decisions
  → leave draft, report PROVENANCE_BLOCKED, request explicit supersession
```

Do not create a new branch solely to conceal unresolved ownership. A split must represent a real lifecycle or scope boundary.

## Output contract

```yaml
concurrency_report:
  repository: <repo>
  branch: <branch>
  expected_head: <sha>
  actual_head: <sha>
  drift_detected: true
  decision_provenance:
    record_ids: []
    verdict: <PASS | PROVENANCE_BLOCKED | ROUTE_FOR_APPROVAL>
    effective_decision: <decision or null>
    conflicts: []
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

`PASS` means the final write was based on the inspected current head and verified governing decision. It does not mean design, scope, or release acceptance passed.

## Workflow placement

```text
INITIALIZE
  capture branch, initial head, write owner, and decision records

SPEC CONFIRMATION
  verify decision provenance for scope, locks, and ownership

BEFORE EVERY WRITE
  acquire and validate expected-head lease

ON DRIFT
  classify code delta and decision authority before retry

VERIFICATION
  prove final artifact, scope report, provenance report, and manifest
  refer to the actual stable head

DELIVERY
  block when head is moving, provenance is unresolved, or manifest is stale
```

## Final guard

```text
□ Every write names the expected head it was prepared from.
□ Current head was re-resolved immediately before mutation.
□ Head drift was inspected, not blindly overwritten.
□ Decision-sensitive drift references verified provenance records.
□ Agent-authored summaries were not treated as approval.
□ Newest commit was not confused with authoritative intent.
□ Scope and preservation were rechecked after compatible drift.
□ Decision conflicts stopped automatic writes.
□ Two reversals triggered anti-ping-pong stop.
□ Parent pointers were not chased while the child head remained unstable.
□ Delivery artifacts and PR text reference the actual stable head and decision ledger.
```
