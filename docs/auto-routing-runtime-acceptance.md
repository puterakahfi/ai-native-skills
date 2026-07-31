# Auto-Routing Runtime Acceptance Guide

**Epic #304 — Hermes native-ai-engineering fleet**
**Slice 5 of 6 (Issue #310)**

This document explains how to validate the full auto-routing path end-to-end,
documents known limitations, and answers "who actually ran this?"

---

## Who actually ran this?

Every step in the auto-routing pipeline has a named, verifiable actor:

| Step | Actor | Evidence |
|---|---|---|
| Plan authored | `agent-orchestrator` | `task_routing_plan.yaml` + `plan_id` |
| Worker dispatched | `agent-orchestrator` | `dispatch_receipt.receipt_id` |
| Work executed | Specialist profile (e.g. `agent-design`) | `worker_receipt.receipt_id` |
| Review run | Independent reviewer (e.g. `agent-review`) | `review_receipt.receipt_id` |
| Synthesized | `agent-orchestrator` | `synthesis_receipt.receipt_id` |
| Returned to user | `agent-orchestrator` | `origin_return_receipt.receipt_id` |

All actors are explicit in their receipts. An auditor can reconstruct the full
chain from `plan_id` alone.

---

## Four operating modes

### 1. PLAN mode
Orchestrator emits `task_routing_plan` only. No dispatch, no workers.
Use for: dry runs, human review of routing before execution.

```bash
hermes -p agent-orchestrator chat -q "Plan: <request> — emit plan only, do not dispatch"
```

### 2. EXECUTE mode
Full pipeline: plan → dispatch → worker → review → synthesis → return.
Use for: normal operation.

### 3. AUDIT mode
Load an existing plan by `plan_id` and verify all receipts.
Use for: post-run verification, CI integration.

```bash
python3 -m pytest tests/auto-routing/ -v
```

### 4. RESUME mode
Load plan + existing receipts. Skip completed workers. Re-dispatch incomplete.
Use for: recovering from interruptions.

See `hermes-auto-routing-dispatch` skill §resume semantics.

---

## Durable workers vs temporary subagents

| | Durable worker | Temporary subagent |
|---|---|---|
| Mechanism | `hermes -p <profile> chat` (persistent session) | `delegate_task` (spawned subagent) |
| Dispatch receipt kind | `durable_worker` | `temporary_delegation` |
| Session persists? | ✅ Yes — session ID retrievable | ❌ No — ephemeral |
| Can promote to `merged`/`accepted`? | ✅ Yes (with external pointer) | ❌ No |
| Synthesis promotes to? | `approved` / `delivered` | `reviewed` max |
| Resume safe? | ✅ Yes | ❌ No — must re-dispatch |
| Current status | ✅ Working (`hermes -p` subprocess) | ✅ Working (`delegate_task`) |

**When to use `delegate_task`:** short-lived isolated research, bounded subtasks where
durability is not required. Document as `temporary_delegation` and do not assert
`merged`/`accepted` from this evidence.

**When to use `hermes -p <profile> chat`:** specialist work where you need a real
session ID, a persistent profile context (skills, memory), and durable receipt evidence.
This is the verified working mode for Epic #304 (confirmed 2026-07-31 dogfood).

---

## Acceptance: all 6 receipt types must be present

A fully accepted auto-routing run produces:

```
✅ task_routing_plan        plan-*.yaml — validated against schema
✅ dispatch_receipt(s)      per worker — validated
✅ worker_receipt(s)        per worker — validated
✅ review_receipt(s)        per reviewer — validated
✅ synthesis_receipt        one per plan — validated
✅ origin_return_receipt    one per plan — validated
```

Minimum to reach `final_status: approved`:
- All workers `executed`
- All reviewers `verdict: approved` with `independence: VERIFIED` or permitted `LIMITED`
- Synthesis `promoted_claims.approved.asserted: true`
- `origin_return_receipt.status: delivered`

---

## Known limitations

### Desktop-origin path
`origin.channel: desktop` is **VERIFIED** — confirmed working in #304 dogfood.
`origin_return_receipt.delivery_channel: desktop` is supported.

### Gateway-origin paths
`gateway_telegram`, `gateway_slack` are **NOT_VERIFIED** — not tested in current fleet.
Limitation: Hermes gateway profiles and routing would need to be configured.
Receipts can declare these channels, but end-to-end delivery is not validated.

### Provider credentials
Workers run with the credentials of the specialist profile. If a profile's LLM
provider differs from the orchestrator's, credential isolation is per-profile.
Limitation: shared provider credentials across profiles are not isolated at the
receipt level.

### Reviewer independence
`VERIFIED` independence requires `reviewer.profile != any worker.profile` in the
same plan. When `agent-review` appears as both a worker and a reviewer, independence
is `LIMITED (shared_profile)`. Synthesis cannot assert `approved` under this condition
unless `review_policy.allow_limited_independence: true`.

### Kanban auto-pickup
Durable Kanban task pickup (specialist profile auto-consuming from queue) is not yet
fully wired. Current verified path: `hermes -p <profile> chat -q "..."` subprocess.
Until #285 (catalog-backed resolution) is resolved, `durable_worker` receipts that
rely on Kanban queue pickup should be marked `READY_WITH_LIMITATIONS`.

---

## Validation commands

```bash
# Validate all plan fixtures
python3 -m pytest tests/auto-routing/test_planner_schema.py -v

# Validate all dispatch fixtures
python3 -m pytest tests/auto-routing/test_dispatch_schema.py -v

# Validate all review + synthesis fixtures
python3 -m pytest tests/auto-routing/test_review_synthesis_schema.py -v

# Full suite
python3 -m pytest tests/auto-routing/ -v
```

---

## Epic #304 completion gate

Epic #304 is complete when:

- [x] PR #311 — contract + 7 schemas + 8 fixtures + reference doc
- [x] PR #313 — planner skill + 4 positive + 2 negative fixtures + 28 tests
- [x] PR #314 — dispatch skill + 3 fixtures + 14 tests
- [x] PR #315 — review+synthesis skill + 4 fixtures + 27 tests
- [x] PR #316 — 7 schema+doc+cli fixes from dogfood
- [ ] PR #310 (this) — runtime acceptance doc + negative fixtures
- [ ] All open PRs merged to main
- [ ] 69+ tests passing on main
- [ ] This doc present and reviewed
