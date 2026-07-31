---
name: hermes-auto-routing-dispatch
description: Use when agent-orchestrator needs to execute a verified task_routing_plan by dispatching each worker slot to a Hermes specialist profile. Supports durable_worker (Kanban) and temporary_delegation (subprocess) modes. Records dispatch_receipt per worker. Respects depends_on ordering and skips already-completed workers on resume.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.runtime: hermes
  ai-native-skills.fleet: native-ai-engineering
  ai-native-skills.requires: "hermes-auto-routing-planner"
  ai-native-skills.related_skills: '["hermes-auto-routing-planner","hermes-agent-fleet-bootstrap","task-continuity"]'
  ai-native-skills.implements: "contracts/schemas/auto-routing/dispatch-receipt.schema.yaml"
  ai-native-skills.boundary.covers: '["plan_consumption","worker_slot_iteration","dispatch_mode_selection","bounded_context_delivery","dispatch_receipt_emission","depends_on_ordering","resume_idempotency","failure_evidence_preservation"]'
  ai-native-skills.boundary.delegates: '["plan_authoring","review_loop","synthesis","origin_return","skill_sync"]'
---

# Hermes Auto-Routing Dispatch

Execute a verified `task_routing_plan` by dispatching each worker slot to a durable
Hermes specialist profile or a temporary delegation subprocess.

```
task_routing_plan (from hermes-auto-routing-planner)
  → hermes-auto-routing-dispatch   ← this skill
      → dispatch each worker slot
      → emit dispatch_receipt per worker
      → validate receipts
  → hermes-auto-routing-review (#309, consumes receipts)
```

## Dispatch modes

### durable_worker
Dispatches to a persistent Hermes specialist profile via Kanban task queue.

```bash
hermes kanban create-task --profile <agent-xxx> --title "<task>" --context "<bounded context>"
# profile picks up task from queue, produces worker_receipt
```

Proof required: `profile_id` + `worker_session_id` (+ optional `kanban_card_uri`).
Can be promoted to `merged`/`accepted` at synthesis.

### temporary_delegation
Dispatches via subprocess — no persistent session, no Kanban.

```bash
hermes -p <agent-xxx> chat -q "<bounded task prompt with output contract>"
```

Proof required: `delegate_task_id` + `parent_session_id`.
**MUST be labeled non-durable.** Synthesis MUST NOT promote temporary evidence to
`merged` or `accepted`. Downgrade to `not_verified` for external claims.

## Procedure

### Step 1 — Load and validate plan

Load `task_routing_plan`. Verify:
- `status: planned` or `attempted` (not already `executed`/`delivered`)
- All `worker_id` slots present
- Schema valid

**Gate:** Plan must exist and reference valid worker slots.

### Step 2 — Build dispatch order

Topological sort of workers by `depends_on`. Workers with no deps go first.
Workers with deps wait until upstream `dispatch_receipt.status == dispatched`
and upstream `worker_receipt.status == executed`.

**Gate:** No cycles (inherited from planner). Blocked upstream = block downstream.

### Step 3 — Check resume state

For each worker slot, check if a `dispatch_receipt` already exists:
- `status: dispatched` or `executed` → **skip, do not re-dispatch**
- `status: attempted` → re-dispatch (previous attempt incomplete)
- No receipt → dispatch fresh

### Step 4 — Select dispatch mode

Default preference order:
1. `durable_worker` — if Hermes Kanban is available and profile is active
2. `temporary_delegation` — fallback when Kanban unavailable or for short-lived tasks

Document which mode was used and why in `dispatch_mode.kind`.

### Step 5 — Build bounded context

Per worker slot, construct:
```
- task scope (from worker.responsibility)
- inputs (from worker.inputs or upstream worker artifacts)
- expected_outputs (from worker.expected_outputs)
- output contract (schema or format expected)
- plan_id (for receipt back-reference)
- worker_id (for receipt back-reference)
```

Keep context bounded — do not pass entire plan or unrelated artifacts.

### Step 6 — Dispatch and emit receipt

#### durable_worker
```bash
hermes -p <profile_id> chat -q "<bounded context prompt>"
# capture session_id from output
```

Emit:
```yaml
schema_version: "1.0"
receipt_id: dispatch-<worker_id>-<timestamp>
plan_id: <plan_id>
worker_id: <worker_id>
dispatched_at: <ISO 8601>
status: dispatched
dispatch_mode:
  kind: durable_worker
  proof:
    profile_id: <agent-xxx>
    worker_session_id: <session_id>
    kanban_card_uri: <uri if available>
```

#### temporary_delegation
```yaml
schema_version: "1.0"
receipt_id: dispatch-<worker_id>-<timestamp>
plan_id: <plan_id>
worker_id: <worker_id>
dispatched_at: <ISO 8601>
status: dispatched
dispatch_mode:
  kind: temporary_delegation
  proof:
    delegate_task_id: <id>
    parent_session_id: <session_id>
    max_turns: 20
```

### Step 7 — Validate receipt

```bash
python3 -c "import yaml,jsonschema; jsonschema.validate(
  yaml.safe_load(open('receipt.yaml')),
  yaml.safe_load(open('schemas/auto-routing/dispatch-receipt.schema.yaml'))
); print('VALID')"
```

**Gate:** Schema must pass. Fix and retry (max 2 iterations) before reporting BLOCKED.

### Step 8 — Handle failure

If dispatch fails (profile unavailable, timeout, error):
```yaml
status: blocked
# include error evidence in a separate worker_receipt with status: blocked
```

Preserve actionable error: what failed, why, what to retry.
Do NOT silently skip failed workers.

## Resume semantics

On interruption:
1. Load plan by `plan_id`
2. Load all existing `dispatch_receipt` records
3. Workers with `dispatched`/`executed` receipts → skip
4. Workers with `attempted` or no receipt → re-dispatch
5. Preserve all previous receipts for audit

## Hermes runtime limitations

> **Current state (as of 2026-07-31):** Hermes Kanban-based `durable_worker` dispatch
> is not yet fully wired for automated task pickup by specialist profiles.
> `temporary_delegation` via `hermes -p <profile> chat -q "..."` subprocess is the
> verified working mode (confirmed in Epic #304 dogfood run).
>
> Until #285 (catalog-backed capability resolution) and Kanban auto-pickup are complete,
> `durable_worker` receipts that lack a real `worker_session_id` from an actual profile
> run MUST be marked `READY_WITH_LIMITATIONS`, not `READY`.
>
> Do not claim durable routing from simulations only.

## Quality gates

- Every dispatched worker has a `dispatch_receipt` with schema-valid proof
- Completed workers are not re-dispatched on resume
- `temporary_delegation` receipts never promoted to `merged`/`accepted`
- `depends_on` ordering respected — no worker dispatched before upstream completes
- Failed workers: `status: blocked` with actionable error evidence
- Runtime limitations documented honestly — no false `durable_worker` claims
