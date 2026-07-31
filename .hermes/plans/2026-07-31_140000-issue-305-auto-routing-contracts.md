# Issue #305 — Auto-Routing Contract and Evidence Receipts

> **For Hermes:** Slice 1 of Epic #304. Define schemas + fixtures + docs for task-time auto-routing. No runtime code yet — this is contract-first.

**Goal:** Publish canonical schemas and receipts that later slices (audit, planner, dispatch, review, docs) will reference and validate against. Positive + negative fixtures must be present so #307–#310 can wire assertions.

**Architecture:** STAR topology (orchestrator hub, specialists spoke). Orchestrator is **coordination-first with classification gate** — trivial acks/clarifications/read-only-lookups may be self-handled with structured justification; anything domain-heavy must delegate. Extend the existing `hermes-agent-fleet-bootstrap` skill package with a new `references/auto-routing-contract.md` document, YAML schema files under `schemas/auto-routing/`, and behavioral fixtures under `contracts/tests/`. Preserve exactly-one-primary-workflow + one-owner invariants; separate durable dispatch from `delegate_task` explicitly.

**Tech Stack:** YAML schemas, markdown reference docs, Python assertion helpers reused from existing test suite pattern.

---

## Current context

- Epic #304 defines 6 slices; this is Slice 1 (blocker for #306–#310).
- Existing skill `skills/hermes-agent-fleet-bootstrap/` owns the fleet identity contract; auto-routing is the runtime companion.
- Existing tests use `contracts/tests/*.test.yaml` schema with `skill_test.cases[]` — reuse this shape.
- No existing routing/dispatch schema exists in ai-native-skills — greenfield.
- Base branch: `main` (verified via `arbiter-issue-fix-cycle` rule for ai-native-skills).
- PR target: `main`. No epic integration branch created yet; #304 says "target an epic/integration branch unless repository policy allows independent release" — for a schema-only slice with no runtime code impact, direct-to-main is defensible. Confirm with user before push.

## Files likely to change

### Create
- `schemas/auto-routing/task-routing-plan.schema.yaml` — planner output.
- `schemas/auto-routing/orchestrator-action-receipt.schema.yaml` — self-handled trivial-scope evidence.
- `schemas/auto-routing/dispatch-receipt.schema.yaml` — orchestrator dispatch record.
- `schemas/auto-routing/worker-receipt.schema.yaml` — specialist worker outcome.
- `schemas/auto-routing/review-receipt.schema.yaml` — independent-reviewer outcome.
- `schemas/auto-routing/synthesis-receipt.schema.yaml` — orchestrator synthesis of workers.
- `schemas/auto-routing/origin-return-receipt.schema.yaml` — return path evidence (desktop, gateway).
- `skills/hermes-agent-fleet-bootstrap/references/auto-routing-contract.md` — human-readable contract, load-order, status vocab.
- `contracts/tests/hermes-auto-routing.test.yaml` — positive + negative behavioral fixtures.
- `contracts/fixtures/auto-routing/positive-redesign-ui.yaml` — happy path: redesign → design+frontend+review workers.
- `contracts/fixtures/auto-routing/positive-backend-bug.yaml` — bugfix → backend+review.
- `contracts/fixtures/auto-routing/negative-orchestrator-shortcut.yaml` — orchestrator implements specialist work silently.
- `contracts/fixtures/auto-routing/negative-delegate-task-claim.yaml` — temp delegate claimed as durable.
- `contracts/fixtures/auto-routing/negative-reviewer-independence.yaml` — reviewer = implementer.
- `contracts/fixtures/auto-routing/negative-missing-worker-evidence.yaml` — dispatch success without receipt.
- `skills/hermes-agent-fleet-bootstrap/tests/test_auto_routing_schema.py` — schema-load + shape assertions.
- `skills/hermes-agent-fleet-bootstrap/tests/test_auto_routing_fixtures.py` — fixtures parse and honor invariants.

### Modify
- `skills/hermes-agent-fleet-bootstrap/SKILL.md` — add auto-routing reference to "Load references" list.
- `docs/capability-inventory.json` — regenerated via `scripts/verify-capability-inventory.py --write-snapshot`.
- `docs/contract-coverage-discovery.yaml` — regenerated.
- `README.md` — skill count badge only if new top-level skill added (probably not; this extends existing).
- `docs/skills.md` — same.

## Status vocabulary (defines return of every receipt)

```yaml
status:
  planned         # planner emitted plan, nothing dispatched
  attempted       # dispatch started, no worker receipt yet
  dispatched      # worker acknowledged, no completion
  executed        # worker completed with output
  reviewed        # independent reviewer signed off
  approved        # user/authority approved
  delivered       # return-path returned artifact to origin
  merged          # code merged (external verification)
  accepted        # product acceptance (external)
  blocked         # invariant violated, hard stop
  cancelled       # user or system cancelled
  not_verified    # attempted but evidence missing
```

## Invariants (schemas must enforce structurally)

1. Exactly one `primary_workflow` per plan.
2. Each worker slot has exactly one accountable specialist profile.
3. `reviewer_independence` is one of `VERIFIED | LIMITED_SHARED_MODEL | LIMITED_SHARED_CONTEXT | LIMITED_SHARED_TOOLS | NOT_VERIFIED`.
4. `dispatch_mode` is `durable_worker` or `temporary_delegation` — synthesis cannot upgrade temp to durable.
5. `origin.channel` ∈ `desktop | gateway_telegram | gateway_slack | cli | cron`. Return path receipt must reference the same channel.
6. `worker_receipt.evidence` MUST contain either `receipt_uri` (retrievable) or `receipt_inline` (bounded content) — synthesis without either → `blocked` or `not_verified`.

## Proposed approach

Schema-first, YAML JSON-schema (draft-07). Author each receipt as an independent doc that composes:

```
task_routing_plan
  ├── plan_id, origin, primary_workflow, workers[], reviewers[], review_policy
dispatch_receipt
  ├── plan_id, worker_id, dispatch_mode, dispatched_at, evidence_pointer
worker_receipt
  ├── worker_id, profile, status, evidence, started_at, completed_at
review_receipt
  ├── review_id, worker_id, reviewer_profile, independence, findings, verdict
synthesis_receipt
  ├── plan_id, worker_receipts[], review_receipts[], final_status, promoted_claims
origin_return_receipt
  ├── plan_id, origin, delivered_at, delivery_channel, artifact_uri
```

Docs mirror this structure with load order + hard stops (mirrors existing `runtime-gateway-and-security.md` style).

## Step-by-step plan

### Task 1: Author status vocabulary + invariants doc
- Create `skills/hermes-agent-fleet-bootstrap/references/auto-routing-contract.md`.
- Include: purpose, load context, status vocab, invariants (1–6 above), hard stops.
- Verify: `read_file` back, cross-check with #304 acceptance criteria.
- Commit: `docs(hermes): add auto-routing contract reference [#305]`.

### Task 2: Schema — task_routing_plan
- Create `schemas/auto-routing/task-routing-plan.schema.yaml` (JSON-schema draft-07 as YAML).
- Fields: `plan_id`, `created_at`, `origin{channel, session_id, thread_id?}`, `primary_workflow`, `workers[]{worker_id, profile, responsibility, inputs, expected_outputs}`, `reviewers[]{reviewer_id, profile, independence_target, scope}`, `review_policy`, `status`.
- Constraint: `primary_workflow` required + non-empty; `workers` minItems 1; each `profile` matches `^agent-[a-z]+$`.
- Verify: `python -c "import yaml, jsonschema; jsonschema.Draft7Validator.check_schema(yaml.safe_load(open('schemas/auto-routing/task-routing-plan.schema.yaml')))"`.

### Task 3: Schema — dispatch_receipt
- Fields: `receipt_id`, `plan_id`, `worker_id`, `dispatch_mode` (enum: `durable_worker`, `temporary_delegation`), `dispatched_at`, `evidence_pointer`, `status`.
- Verify: schema self-check.

### Task 4: Schema — worker_receipt
- Fields: `receipt_id`, `worker_id`, `plan_id`, `profile`, `status`, `started_at`, `completed_at`, `evidence{ receipt_uri?, receipt_inline?, evidence_type }`, `failures[]`, `retries`.
- Constraint: `oneOf: [ {required: [receipt_uri]}, {required: [receipt_inline]} ]`.
- Verify: schema self-check + negative example fails.

### Task 5: Schema — review_receipt
- Fields: `receipt_id`, `plan_id`, `worker_receipt_id`, `reviewer_profile`, `independence` (enum), `findings[]{severity, evidence, message}`, `verdict` (enum: `approved`, `changes_requested`, `blocked`), `not_upgraded_claims[]`.
- Verify: schema self-check.

### Task 6: Schema — synthesis_receipt
- Fields: `receipt_id`, `plan_id`, `worker_receipts[]`, `review_receipts[]`, `final_status`, `promoted_claims{implemented, verified, reviewed, approved, delivered, merged, accepted}`, `unresolved_claims[]`.
- Constraint: `promoted_claims` values ∈ status vocab; `merged`/`accepted` cannot be true unless external evidence pointer present.
- Verify: schema + negative example.

### Task 7: Schema — origin_return_receipt
- Fields: `receipt_id`, `plan_id`, `origin{channel, session_id, thread_id?}`, `delivery_channel`, `delivered_at`, `artifact_uri`, `status`.
- Constraint: `delivery_channel == origin.channel` (structural).
- Verify: schema self-check.

### Task 8: Positive fixtures (2)
- `contracts/fixtures/auto-routing/positive-redesign-ui.yaml`: 4 receipts (plan → dispatch × 3 workers → worker receipts → 3 reviews → synthesis → origin return).
- `contracts/fixtures/auto-routing/positive-backend-bug.yaml`: 2 workers path.
- Verify: fixtures validate against all 6 schemas.

### Task 9: Negative fixtures (4)
- `negative-orchestrator-shortcut.yaml`: plan has 0 specialist workers, orchestrator synthesizes without delegation — must map to `blocked`.
- `negative-delegate-task-claim.yaml`: dispatch_mode=`temporary_delegation` but synthesis promoted `merged` claim — must fail invariant.
- `negative-reviewer-independence.yaml`: reviewer_profile == worker profile, independence=`NOT_VERIFIED`, but verdict=`approved` — must fail.
- `negative-missing-worker-evidence.yaml`: worker_receipt.status=`executed` but no evidence pointer — schema rejects.

### Task 10: Behavioral test yaml (`contracts/tests/hermes-auto-routing.test.yaml`)
- 6 cases minimum: 2 positive path, 4 negative from Task 9.
- Follow existing `skill_test` shape (see `hermes-agent-fleet-bootstrap.test.yaml`).
- Each case: `must_contain` + `must_not_contain` + `quality_gates_tested`.

### Task 11: Python tests (`tests/test_auto_routing_schema.py`, `test_auto_routing_fixtures.py`)
- Schema tests: load all 6 schemas, `Draft7Validator.check_schema`.
- Fixture tests: load each fixture, resolve schema, validate; positive → PASS, negative → raises jsonschema.ValidationError.
- Verify: `python3 -m pytest skills/hermes-agent-fleet-bootstrap/tests/test_auto_routing_*.py -v` — all pass.

### Task 12: SKILL.md — add reference load line
- Patch line under "Load references" to include `auto-routing-contract.md` in the union merge.

### Task 13: Regenerate snapshots
```bash
python3 scripts/verify-capability-inventory.py --write-snapshot
python3 -c "import sys,yaml,importlib.util; from pathlib import Path; ...  # from ai-native-core-contribution skill Step 5"
```

### Task 14: Local verify
```bash
python3 scripts/verify-capability-inventory.py --skip-docs
python3 scripts/validate-contract-coverage.py --root . --core-root /data/www/native-ai-engineering/ai-native-core
python3 scripts/validate-skill-packages.py
python3 -m pytest skills/hermes-agent-fleet-bootstrap/tests/ -v
```

### Task 15: Branch + PR
```bash
git checkout -b feature/305-auto-routing-contracts
git add -A
git commit -m "feat(hermes): define auto-routing contract and receipts [#305]"
git push -u origin feature/305-auto-routing-contracts
gh pr create --repo puterakahfi/ai-native-skills \
  --title "feat(hermes): define auto-routing contract and receipts (#305)" \
  --body "Closes #305. Slice 1 of Epic #304. Schemas + fixtures + docs only; no runtime code." \
  --base main
```

### Task 16: Wait CI + iterate
```bash
sleep 60
gh pr checks <N> --repo puterakahfi/ai-native-skills
```
Fix any drift; wait for user merge authorization.

## Risks + open questions

1. **PR target — main vs epic integration branch?** #304 says integration branch unless policy allows independent release. Schema-only slice with no runtime impact → arguably independent. **Confirm with user before Task 15.**
2. **Schema draft — YAML embedding JSON-schema draft-07 vs custom DSL?** Existing repo has no schema convention. Draft-07 is broadly readable; go with that unless user prefers something else.
3. **Fixture format — YAML vs JSON?** Existing pattern uses YAML. Stick with YAML.
4. **Do we need contracts in ai-native-core companion?** Epic runs at repository scope; #305 mentions "Applicable package, schema, and behavioral validation commands pass" — no explicit ai-native-core contract requirement. Skip unless CI complains.
5. **Effort estimate:** ~15–20 hours solo. Tasks 2–7 (schemas) ~4h; Tasks 8–9 (fixtures) ~4h; Tasks 10–11 (tests) ~3h; Task 13–16 (snapshots + PR) ~2h; buffer ~3–5h.

## Verification

Local gates (must PASS before push):
- `verify-capability-inventory.py --skip-docs` → PASS
- `validate-contract-coverage.py --core-root ...` → PASS (pre-existing 3 violations acceptable; must not add new)
- `validate-skill-packages.py` → 0 errors
- `pytest skills/hermes-agent-fleet-bootstrap/tests/test_auto_routing_*.py` → all pass
- Positive fixtures validate against schemas; negative fixtures raise `jsonschema.ValidationError`

CI gates (must PASS in PR):
- Contract Coverage validate
- Published Capability Catalog validate
- Skill Pack Contracts validate
- Skill Package Validation validate
- Skill and Gate Contracts validate
- inventory-drift validate

## Handoff

Plan complete. Awaiting user decision on Risk #1 (PR target). Once confirmed, execute Task 1 → 16 linearly.
