# PRD — Durable Specialist Worker Dispatch (Issue #308)

**Epic:** [#304](https://github.com/puterakahfi/ai-native-skills/issues/304)
**Slice:** 3 of 6 (depends on #307 planner ✅ PR #313, blocks #309 review+synthesis)
**Status:** Open

---

## Problem Statement

Setelah planner (#307) menghasilkan `task_routing_plan` yang valid, orchestrator belum punya
execution bridge untuk mengirim task ke specialist profiles. Tanpa dispatcher:
- Plan tetap `PLAN_ONLY` selamanya — tidak ada worker yang jalan
- Tidak ada `dispatch_receipt` → #309 review loop tidak bisa mulai
- Tidak ada idempotent resume → kalau interrupted, semua diulang dari nol

## Objective

Implement `hermes-auto-routing-dispatch` skill yang mengkonsumsi `task_routing_plan`,
dispatch setiap worker slot ke Hermes specialist profile, dan produce `dispatch_receipt`
per worker. Support dua mode: `durable_worker` (Kanban/persistent session) dan
`temporary_delegation` (subprocess `hermes -p ... chat -q`). Completed workers tidak
di-dispatch ulang pada resume.

---

## Dispatch Modes

| Mode | Mechanism | Durable? | Can promote to `merged`/`accepted`? |
|---|---|---|---|
| `durable_worker` | Hermes Kanban + persistent profile session | ✅ | ✅ |
| `temporary_delegation` | `hermes -p <profile> chat -q "..."` subprocess | ❌ | ❌ |

`temporary_delegation` harus di-label explicitly as non-durable di receipt. Synthesis (#309)
dilarang upgrade temporary evidence ke external claims.

---

## Acceptance Criteria

| # | Criterion |
|---|---|
| AC-1 | Selected profiles receive bounded context + expected output contracts |
| AC-2 | Each worker produces `dispatch_receipt` validating against schema |
| AC-3 | Completed workers (status: dispatched/executed) not re-dispatched on resume |
| AC-4 | Failed/blocked workers preserve actionable error evidence in receipt |
| AC-5 | `temporary_delegation` receipts labeled non-durable, excluded from durable acceptance |
| AC-6 | Dispatch respects `depends_on` ordering from plan |
| AC-7 | All fixtures validate against `dispatch-receipt.schema.yaml` |
| AC-8 | Unit + behavioral tests pass, or limitations documented as `READY_WITH_LIMITATIONS` |

---

## Technical Design

```
skills/hermes-auto-routing-dispatch/
  SKILL.md
  references/
    dispatch-procedure.md
contracts/fixtures/auto-routing/
  positive-dispatch-durable.yaml
  positive-dispatch-temporary.yaml
  negative-dispatch-blocked.yaml
tests/auto-routing/
  test_dispatch_schema.py
```

### Dispatch procedure (per worker slot)
```
1. Load plan, check worker status (skip if already dispatched/executed)
2. Resolve depends_on — wait for upstream worker receipt before dispatching
3. Select dispatch mode:
   a. durable_worker  → hermes kanban create-task + hermes -p <profile> (persistent)
   b. temporary_delegation → hermes -p <profile> chat -q "..." (subprocess)
4. Emit dispatch_receipt with proof (session_id / delegate_task_id)
5. Validate receipt against schema
6. On failure → set status: blocked, preserve error evidence
```

---

## Branch & PR Topology

```
base:   main
branch: feat/308-auto-routing-dispatch
PR:     main
```

## Definition of Done

- [ ] `skills/hermes-auto-routing-dispatch/SKILL.md`
- [ ] 2 positive + 1 negative dispatch fixtures, all schema-valid
- [ ] `test_dispatch_schema.py` passing
- [ ] Hermes runtime limitations documented if durable Kanban not yet available
- [ ] PR merged, #308 closed
