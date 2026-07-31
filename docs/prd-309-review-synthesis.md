# PRD — Review + Synthesis Loop (Issue #309)

**Epic:** [#304](https://github.com/puterakahfi/ai-native-skills/issues/304)
**Slice:** 4 of 6 (depends on #308 dispatch ✅ PR #314, blocks #310 fixtures+docs)
**Status:** Open

---

## Problem Statement

After workers execute (#308), orchestrator needs a structured loop to:
1. Invoke required reviewer profiles
2. Collect `review_receipt` with independence verdict + findings
3. Synthesize all worker + review receipts into a single `synthesis_receipt`
4. Return the synthesized answer to the origin channel via `origin_return_receipt`

Without this, the pipeline terminates at dispatch with no final verdict or delivery.

## Objective

Implement `hermes-auto-routing-review-synthesis` skill that:
- Dispatches reviewer profiles against worker receipts
- Records `review_receipt` per reviewer (independence: VERIFIED/LIMITED/NOT_VERIFIED)
- Synthesizes promoted claims without upgrading unsupported evidence
- Emits `synthesis_receipt` + `origin_return_receipt`
- Keeps implementation/review/approval/delivery/merge/acceptance states strictly separate

## State ladder (strict — no skipping)

```
executed → reviewed → approved → delivered → merged → accepted
```

Each state requires explicit evidence. Synthesis MUST NOT jump over states.

## Independence rules (§6)

| Reviewer profile == Worker profile? | independence_target |
|---|---|
| Different profile | VERIFIED |
| Same profile | LIMITED (must justify) or NOT_VERIFIED |

## Acceptance Criteria

| # | Criterion |
|---|---|
| AC-1 | Required review runs or readiness is limited/blocked honestly |
| AC-2 | Independence is VERIFIED, LIMITED with justification, or NOT_VERIFIED |
| AC-3 | Final synthesis cites all worker + reviewer receipt IDs |
| AC-4 | Final answer does not imply approval/merge/release/deployment unless state is reached |
| AC-5 | Negative fixtures catch reviewer-as-implementer and unsupported completion claims |
| AC-6 | All fixtures validate against review-receipt + synthesis-receipt + origin-return-receipt schemas |
| AC-7 | Behavioral tests pass |

## Known schema gap (#312)

`origin-return-receipt.status` enum: `[delivered, blocked, cancelled, not_verified]`
Missing: `reviewed`, `changes_requested` for intermediate review states.
Workaround for now: use `not_verified` for intermediate states, document as limitation.
Fix tracked in #312.

## Branch & PR Topology

```
base:   main
branch: feat/309-review-synthesis
```
