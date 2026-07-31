---
name: hermes-auto-routing-review-synthesis
description: "Use when agent-orchestrator needs to run the review loop and synthesize worker+review receipts into a final verdict. Dispatches reviewer profiles, records review_receipt per reviewer (independence VERIFIED/LIMITED/NOT_VERIFIED), synthesizes promoted claims, emits synthesis_receipt + origin_return_receipt. Never upgrades unsupported claims. State ladder: executed->reviewed->approved->delivered->merged->accepted, no skipping."
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.runtime: hermes
  ai-native-skills.fleet: native-ai-engineering
  ai-native-skills.requires: "hermes-auto-routing-dispatch"
  ai-native-skills.related_skills: '["hermes-auto-routing-planner","hermes-auto-routing-dispatch","hermes-agent-fleet-bootstrap","task-continuity"]'
  ai-native-skills.implements: '["review-receipt.schema.yaml","synthesis-receipt.schema.yaml","origin-return-receipt.schema.yaml"]'
  ai-native-skills.boundary.covers: '["reviewer_dispatch","review_receipt_emission","independence_determination","synthesis","promoted_claims","origin_return"]'
  ai-native-skills.boundary.delegates: '["plan_authoring","worker_dispatch","skill_sync","catalog_resolution"]'
---

# Hermes Auto-Routing Review + Synthesis

Run the review loop and synthesize all evidence into a final answer.

```
dispatch_receipts + worker_receipts (from hermes-auto-routing-dispatch)
  → hermes-auto-routing-review-synthesis   ← this skill
      → dispatch reviewer profiles
      → collect review_receipts
      → synthesize promoted claims
      → emit synthesis_receipt
      → emit origin_return_receipt
  → user / origin channel
```

## State ladder — strict, no skipping

```
executed      worker completed, artifact produced
  ↓
reviewed      independent reviewer ran, findings recorded
  ↓
approved      reviewer verdict=approved (all findings resolved)
  ↓
delivered     synthesis returned to origin channel
  ↓
merged        PR/artifact accepted into target (external, durable evidence required)
  ↓
accepted      product owner sign-off (external, durable evidence required)
```

**Synthesis MUST NOT jump states.** If review verdict=changes_requested, `final_status` = `reviewed`, not `approved`.

## Procedure

### Step 1 — Collect worker receipts

Load all `worker_receipt` records for the plan. Verify each has `status: executed`.
Any `status: blocked` → synthesis is limited. Document in `unresolved_claims`.

### Step 2 — Determine reviewer assignments

From `task_routing_plan.reviewers`, map each reviewer to the worker receipts they cover.
Apply independence rule:

```
reviewer_profile != any worker_profile in same plan → VERIFIED
reviewer_profile == any worker_profile → LIMITED (must justify) or NOT_VERIFIED
```

### Step 3 — Dispatch reviewers

Use same dispatch modes as #308 (`durable_worker` preferred, `temporary_delegation` fallback).
Bounded context per reviewer:
- worker artifact URI / file path
- expected findings scope (e.g. accessibility, TS correctness, security)
- plan_id + worker_receipt_id for back-reference

### Step 4 — Emit review_receipt per reviewer

```yaml
schema_version: "1.0"
receipt_id: review-receipt-<reviewer_id>-<timestamp>
plan_id: <plan_id>
worker_receipt_id: <worker_receipt_id>
reviewer_profile: <agent-xxx>
independence:
  verdict: VERIFIED | LIMITED | NOT_VERIFIED
  compromises: []         # list reasons if LIMITED/NOT_VERIFIED
reviewed_at: <ISO 8601>
verdict: approved | changes_requested | blocked
findings:
  - id: F-01
    severity: error | warning | info
    location: "<file:line or component>"
    description: "<specific finding>"
    suggested_fix: "<optional>"
```

**Gate:** Independence NOT_VERIFIED with no justification → block synthesis, do not proceed.

### Step 5 — Synthesize

Collect: all worker_receipt_ids, all review_receipt_ids, final verdict.

Final status rules:
- All reviewers verdict=approved → `final_status: approved`
- Any reviewer verdict=changes_requested → `final_status: reviewed`
- Any reviewer verdict=blocked → `final_status: blocked`

Promoted claims:
- `implemented`: asserted if worker_receipts all executed
- `verified`: asserted if tsc/lint/test pass (from worker evidence)
- `reviewed`: asserted if review_receipts exist with findings
- `approved`: asserted only if all review verdicts=approved
- `delivered`/`merged`/`accepted`: external claims — require durable_worker lineage + external_pointer

**NEVER assert `delivered`, `merged`, `accepted` from temporary_delegation evidence.**

Emit:
```yaml
schema_version: "1.0"
receipt_id: synthesis-<plan_id>-<timestamp>
plan_id: <plan_id>
synthesized_at: <ISO 8601>
worker_receipt_ids: [...]
review_receipt_ids: [...]
final_status: approved | reviewed | blocked | not_verified
promoted_claims:
  implemented:
    asserted: true
    supporting_receipt_ids: [worker-receipt-xxx]
  reviewed:
    asserted: true
    supporting_receipt_ids: [review-receipt-xxx]
  approved:
    asserted: true | false
    supporting_receipt_ids: [review-receipt-xxx]
unresolved_claims:
  - claim: "merge to main"
    reason: "requires human PR approval — external action outside fleet scope"
```

### Step 6 — Emit origin_return_receipt

```yaml
schema_version: "1.0"
receipt_id: origin-return-<plan_id>-<timestamp>
plan_id: <plan_id>
origin:
  channel: desktop | gateway_telegram | gateway_slack | cli | cron
  session_id: <session_id>
  user_ref: <user_ref>
delivery_channel: <same as origin.channel>
delivered_at: <ISO 8601>
artifact_uri: "<file path or session URI>"
status: delivered | blocked | not_verified
```

**Known limitation (#312):** `status` enum missing `reviewed` and `changes_requested`.
Until #312 is fixed, use `not_verified` for intermediate review states and document in notes.

### Step 7 — Validate all receipts

```bash
python3 -c "
import yaml, jsonschema
schemas = {
  'review': 'schemas/auto-routing/review-receipt.schema.yaml',
  'synthesis': 'schemas/auto-routing/synthesis-receipt.schema.yaml',
  'origin-return': 'schemas/auto-routing/origin-return-receipt.schema.yaml',
}
"
```

### Step 8 — Return to user

Report:
1. All receipt IDs and validation status
2. Reviewer findings (severity breakdown)
3. Final status (promoted claims)
4. Unresolved claims with next actions
5. Any limitations (independence, durable eligibility)

## Negative patterns — NEVER do these

- ❌ Reviewer profile == worker profile with `independence_target: VERIFIED`
- ❌ `approved` claim without any review_receipt
- ❌ `merged` or `accepted` claim from temporary_delegation evidence
- ❌ Skip `reviewed` state → jump directly to `approved`
- ❌ Synthesize without citing receipt IDs
- ❌ Claim delivery when origin channel not confirmed

## Quality gates

- Every reviewer has a `review_receipt` with `independence.verdict` documented
- `promoted_claims` only asserted when supporting evidence exists
- `delivered`/`merged`/`accepted` require external_pointer + durable lineage
- `unresolved_claims` captures everything synthesis cannot assert
- All 3 receipts validate against their schemas
