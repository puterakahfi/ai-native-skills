# Auto-routing Schema Friction — Dogfood Findings

Source: Epic #304 dogfood run (2026-07-31) + #312 schema iteration.
Task: DarkModeToggle React component — design → frontend → review pipeline.
All 6 receipts validated successfully once the patterns below were applied.

## F1 — worker-receipt: started_at + completed_at are REQUIRED

**Schema**: `worker-receipt.schema.yaml`
**Problem**: Both fields are in `required[]` but easy to omit.
**Fix**: Always include both timestamps. Capture wall-clock time around the subprocess call:

```bash
START=$(date +%s)
hermes -p agent-design chat -q "..."
# inject started_at = wall clock before, completed_at = after
```

## F2 — synthesis-receipt: omit unasserted claims entirely

**Schema**: `synthesis-receipt.schema.yaml`
**Problem**: Setting `asserted: false` with `supporting_receipt_ids: []` fails validation.
The schema enforces `minItems: 1` on `supporting_receipt_ids` regardless of `asserted` value.

```yaml
# WRONG — fails schema validation
promoted_claims:
  approved:
    asserted: false
    supporting_receipt_ids: []   # ValidationError: [] should be non-empty

# CORRECT — omit the key entirely
promoted_claims:
  implemented:
    asserted: true
    supporting_receipt_ids: ["worker-receipt-frontend-01"]
  # 'approved' key not present = not asserted
```

## F3 — origin-return-receipt: `reviewed` + `changes_requested` ✅ FIXED in PR #316

~~Status enum was `['delivered', 'blocked', 'cancelled', 'not_verified']` — missing `reviewed`.~~
**Fixed:** enum now `[delivered, reviewed, changes_requested, blocked, cancelled, not_verified]`.
Use the correct status — `not_verified` workaround no longer needed.

## F4 — review-receipt: findings items have restricted shape

**Schema**: `review-receipt.schema.yaml`
**Problem**: `findings` items only allow `severity`, `message`, `evidence`.
Fields `id`, `location`, `description`, `suggested_fix` cause `additionalProperties` errors.

```yaml
# WRONG
findings:
  - id: F-01
    severity: error
    location: "DarkModeToggle.tsx:89"
    description: "Space key double-fires"
    suggested_fix: "Remove onKeyDown"

# CORRECT — pack location + description into message
findings:
  - severity: error
    message: "DarkModeToggle.tsx:89 — Space key double-fires (onClick+onKeyDown both call toggle)"
    evidence: "Remove onKeyDown handler; button onClick handles Space/Enter natively"
```

## F5 — review-receipt: compromises enum + NOT_VERIFIED verdict constraint

**Problem 1**: `independence.compromises` items must be exact enum values:
```
shared_model | shared_context | shared_tools | shared_repo_access | shared_profile
```
Free-text strings like `"agent-review self-reviewed"` are schema-invalid.
Use `shared_profile` when reviewer profile == any worker profile in the same plan.

**Problem 2**: Schema `allOf`: `NOT_VERIFIED` + `verdict: approved` is forbidden.
Use `changes_requested` in test fixtures; document synthesis blocking separately.

## F6 — reviewer as both worker AND reviewer: independence_target must be LIMITED

When `agent-review` (or any profile) appears as a **worker** in `plan.workers[]`
AND as a **reviewer** in `plan.reviewers[]`, `independence_target: VERIFIED` is wrong.

```yaml
# WRONG
reviewers:
  - profile: agent-review
    independence_target: VERIFIED  # ← agent-review is also a worker in this plan

# CORRECT
reviewers:
  - profile: agent-review
    independence_target: LIMITED   # shared_profile compromise applies
```

## F7 — task-routing-plan: new optional fields (PR #316)

`origin.request_summary` (max 500 chars) — auditor context, now valid.
`reviewers[].note` (max 500 chars) — per-reviewer justification, now valid.

## F8 — hermes_fleet.py sandbox HOME detection (PR #316)

Default `Path("~/.hermes").expanduser()` resolves to agent sandbox when running
from inside an agent session. Fixed via `_resolve_hermes_home()`.
When running bootstrap from agent session: pass `--hermes-home /home/<user>/.hermes`
or set `HERMES_REAL_HOME=/home/<user>/.hermes`.

---

## Schema state after PR #316 (current canonical)

| Schema | Status |
|---|---|
| `task-routing-plan` | ✅ + `origin.request_summary`, `reviewers[].note` |
| `orchestrator-action-receipt` | ✅ |
| `dispatch-receipt` | ✅ |
| `worker-receipt` | ✅ |
| `review-receipt` | ✅ |
| `synthesis-receipt` | ✅ |
| `origin-return-receipt` | ✅ + `reviewed`, `changes_requested` in status enum |

## F9 — SKILL.md description field: YAML compact mapping parse error on install

**Scope**: Any skill's YAML frontmatter `description` field.
**Problem**: A long unquoted `description` containing `:`, `→` (Unicode arrow), or `—` (em-dash)
causes `npx skills add` to silently skip the skill:
```
⚠ Skipped .../SKILL.md — YAML parse error: Nested mappings are not allowed in compact mappings
```
YAML parser treats the unquoted value with `:` as a nested mapping attempt.

**Fix**: Always quote the description. Replace `→` with `->`, replace `—` with `,` or `-`.

```yaml
# WRONG — fails install
description: Use when X: step A → B — no skipping.

# CORRECT
description: "Use when X: step A -> B, no skipping."
```

**Verified fix**: `hermes-auto-routing-review-synthesis` commit 564ab78, 2026-07-31.
**Lint before publish**: `python3 -c "import yaml; yaml.safe_load(open('SKILL.md').read().split('---')[1]); print('OK')"`

---

## Verified dogfood session IDs (reference)

- agent-design: `20260731_144459_1b026f` (81s, 2 tool calls)
- agent-frontend: `20260731_144650_ae132c` (131s, 10 tool calls)
- agent-review: `20260731_144936_34fed8` (161s, 6 tool calls)
