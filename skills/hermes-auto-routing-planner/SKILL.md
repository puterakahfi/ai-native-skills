---
name: hermes-auto-routing-planner
description: Use when agent-orchestrator needs to translate a user request into a validated task_routing_plan for the native-ai-engineering fleet. Composes workflow-router + role-switcher outputs into a concrete plan with durable profile IDs, dependency ordering, and reviewer assignment. Output is PLAN_ONLY — does not dispatch workers.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.runtime: hermes
  ai-native-skills.fleet: native-ai-engineering
  ai-native-skills.requires: "workflow-router role-switcher"
  ai-native-skills.related_skills: '["hermes-agent-fleet-bootstrap","workflow-router","role-switcher","delivery-work-breakdown","task-continuity"]'
  ai-native-skills.boundary.covers: '["request_context_normalization","workflow_classification","role_to_profile_mapping","smallest_justified_profile_selection","dependency_ordering","reviewer_independence_assignment","plan_validation","plan_only_output"]'
  ai-native-skills.boundary.delegates: '["worker_dispatch","review_loop","synthesis","origin_return","skill_sync","catalog_resolution"]'
---

# Hermes Auto-Routing Planner

Translate a user request into a validated `task_routing_plan` for the `native-ai-engineering` Hermes fleet.

This skill is the **planner** step in the auto-routing pipeline:

```
user request
  → hermes-auto-routing-planner   ← this skill
      → workflow-router (classify)
      → role-switcher (assign)
      → profile mapping + validation
      → task_routing_plan (PLAN_ONLY)
  → hermes-auto-routing-dispatch  (#308, consumes plan)
  → hermes-auto-routing-review    (#309, consumes receipts)
```

> **Note on skill sync:** Profile skills are installed copies from `puterakahfi/ai-native-skills`. Dynamic catalog resolution and version locking are tracked in Epic #285. Until then, profile ID mapping in this skill is static and must be updated manually when fleet profiles change.

## Boundary

```text
hermes-auto-routing-planner
  request normalization, workflow classification, role assignment,
  profile ID mapping, smallest-set filtering, dependency ordering,
  reviewer independence, plan validation, PLAN_ONLY output

workflow-router
  exactly one primary workflow per task

role-switcher
  one owner, bounded specialists, reviewers per task

hermes-auto-routing-dispatch (#308)
  durable worker dispatch — consumes the plan

hermes-agent-fleet-bootstrap
  fleet setup and profile identity — not task-time routing
```

## Fleet profile ID map

| Role | Durable Profile ID |
|---|---|
| Orchestration | `agent-orchestrator` |
| Product / PRD | `agent-product` |
| Architecture | `agent-architecture` |
| Design (UI/UX/tokens) | `agent-design` |
| Frontend implementation | `agent-frontend` |
| Backend implementation | `agent-backend` |
| Independent review | `agent-review` |

## Procedure

Run steps in order. Block on any unresolved gate.

### Step 1 — Normalize request context

Collect and verify:

```yaml
request_context:
  user_request: <verbatim request>
  product_context: <repo, stack, or NOT_VERIFIED>
  repository_context: <branch policy or NOT_VERIFIED>
  priority: <high | normal | NOT_VERIFIED>
```

If `user_request` is empty or purely social → emit `orchestrator_action_receipt` (self-handle, category: acknowledgment/clarification). Do not produce a routing plan.

### Step 2 — Classify workflow via workflow-router

Run `workflow-router` on the normalized request. Capture:

```yaml
workflow_classification:
  primary_workflow: <exactly one>
  routing_rationale: <evidence>
  ambiguity_resolution: resolved | clarification_required | not_applicable
```

**Gate:** `ambiguity_resolution` must be `resolved`. If `clarification_required` → emit `BLOCKED`, ask user, stop.

### Step 3 — Assign roles via role-switcher

Run `role-switcher` on the classified workflow. Capture:

```yaml
role_assignment:
  owner: <role>
  specialists: []
  reviewers: []
  justification: <why these roles>
```

**Gate:** Exactly one owner. No reviewer = same profile as any worker.

### Step 4 — Map roles to profile IDs

Apply fleet profile ID map. Use smallest justified set:

```text
DO include: profiles whose responsibility directly covers the task scope
DO NOT include: profiles not justified by the workflow + role assignment
```

Routing examples:

| Request type | Workers | Reviewer |
|---|---|---|
| Redesign UI | agent-design → agent-frontend | agent-review |
| Backend bug | agent-backend | agent-review |
| PRD / product planning | agent-product (+ agent-architecture if justified) | agent-review |
| Review-only | _(no implementation workers)_ | agent-review |
| New feature (full stack) | agent-design → agent-frontend → agent-backend | agent-review |

**Gate:** No worker profile duplicated. Reviewer profile ≠ any worker profile.

### Step 5 — Build dependency ordering

Assign `depends_on` per worker slot based on artifact handoff:

```text
design output → frontend input   → agent-frontend depends_on agent-design
frontend output → review input   → agent-review depends_on agent-frontend
```

Cycle check: dependency graph must be a DAG.

**Gate:** No cycles. Every `depends_on` ref resolves to a `worker_id` in the same plan.

### Step 6 — Assign reviewer independence

For each reviewer:

- If reviewer profile ∉ worker profiles → `independence_target: VERIFIED`
- If reviewer profile ∈ worker profiles → `independence_target: LIMITED` + justification required
- `agent-review` reviewing any `agent-design`/`agent-frontend`/`agent-backend` work → always `VERIFIED`

### Step 7 — Emit and validate plan

Produce `task_routing_plan` conforming to `schemas/auto-routing/task-routing-plan.schema.yaml`:

```yaml
schema_version: "1.0"
plan_id: plan-<slug>-<timestamp>
created_at: <ISO 8601>
origin:
  channel: desktop | gateway_telegram | gateway_slack | cli | cron
orchestrator_action:
  kind: delegated_to_specialist
primary_workflow: <from step 2>
workers:
  - worker_id: worker-<role>-01
    profile: agent-<role>
    responsibility: <clear scope>
    inputs: []
    expected_outputs: []
    depends_on: []
reviewers:
  - reviewer_id: reviewer-<role>-01
    profile: agent-review
    scope: []
    independence_target: VERIFIED
    reviews_worker_ids: []
review_policy:
  allow_limited_independence: false
  require_reviewer_per_worker: true
status: planned
```

Validate: `python3 -c "import yaml,jsonschema; jsonschema.validate(yaml.safe_load(open('plan.yaml')), yaml.safe_load(open('schemas/auto-routing/task-routing-plan.schema.yaml'))); print('VALID')"`

**Gate:** Schema validation must pass. Fix and retry (max 2 iterations) before reporting BLOCKED.

## Blocking conditions

Return `status: blocked` when:

- `ambiguity_resolution: clarification_required` — request is unclear
- No `primary_workflow` can be determined
- Worker profile duplicated (two workers same profile)
- Reviewer = worker (same profile)
- Dependency cycle detected
- Required context is `NOT_VERIFIED` and cannot be inferred
- Schema validation fails after 2 fix iterations

## Output

```yaml
plan: <task_routing_plan>           # always present
validation: VALID | BLOCKED         # schema check result
blocking_reason: <if BLOCKED>       # explicit reason
plan_only: true                     # dispatch is a separate step (#308)
```

## Quality gates

- Exactly one `primary_workflow` per plan
- One accountable `profile` per worker slot
- No duplicate worker profiles
- Reviewer profile ≠ any worker profile (or LIMITED with justification)
- Smallest justified profile set — no over-dispatch
- All `depends_on` refs resolve within the plan
- No dependency cycles
- Plan validates against schema before output
- `PLAN_ONLY` — no dispatch, no mutation, no receipt beyond plan itself
