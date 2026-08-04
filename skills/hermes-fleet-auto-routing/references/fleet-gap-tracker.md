# Fleet ADLC Readiness Gap Tracker

Last reviewed: 2026-07-31

## Gap status

| ID | Gap | Severity | Status |
|---|---|---|---|
| #307 | `hermes-auto-routing-planner` not installed | 🔴 Critical | ✅ Fixed 2026-07-31 — installed via `npx skills add` |
| #308 | Durable worker mode not wired (`durable_worker` via Kanban) | 🔴 Critical | ⚠️ Open — `temporary_delegation` only |
| #309 | `hermes-auto-routing-review-synthesis` YAML parse error (description colon) | 🔴 Blocks install | ⚠️ Open — cannot be installed until SKILL.md description is quoted |
| #310 | Fixtures & docs missing | 🟡 Medium | ⚠️ Open |
| #312 | `origin-return-receipt` status enum missing `reviewed` state | 🟡 Medium | ⚠️ Open — workaround: use `not_verified` |
| #285 | No automatic skill sync across profiles | 🟡 Medium | ⚠️ Open — manual reinstall required after repo merges |

## Specialist profile skills — NOT AUDITED

Skills installed on `agent-design`, `agent-frontend`, `agent-backend`, `agent-architecture`,
`agent-product`, `agent-review` have **not been audited**. Unknown whether they carry
task-relevant skills for their assigned responsibilities.

**Next action**: run `hermes -p <profile> skills list` for each specialist and compare
against expected skills from `hermes-agent-fleet-bootstrap/assets/presets/native-ai-engineering.json`.

## Current fleet topology

```
agent-orchestrator (gateway-eligible, active)
  → agent-product     (headless, on-demand)
  → agent-architecture (headless, on-demand)
  → agent-design      (headless, on-demand)
  → agent-frontend    (headless, on-demand)
  → agent-backend     (headless, on-demand)
  → agent-review      (headless, on-demand)
```

STAR topology confirmed. No direct specialist-to-specialist dispatch.

## Dispatch mode (as of 2026-07-31)

- `temporary_delegation` via `hermes -p <profile> chat -q "..."` = **VERIFIED WORKING**
- `durable_worker` via Kanban + persistent session = **NOT VERIFIED** (#308)
