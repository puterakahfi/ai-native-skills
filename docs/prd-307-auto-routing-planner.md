# PRD — Auto-Routing Planner (Issue #307)

**Epic:** [#304 — Make Hermes agent auto-routing execute through durable specialist workers](https://github.com/puterakahfi/ai-native-skills/issues/304)
**Slice:** 2 of 6 (blocker for #308 dispatch, depends on #305 contract ✅ merged)
**Status:** Open
**Author:** puterakahfi

---

## Problem Statement

Setelah contract dan schemas auto-routing selesai (#305 merged), orchestrator belum punya mekanisme deterministik untuk menerjemahkan user request menjadi `task_routing_plan` yang valid.

Saat ini:
- Orchestrator bisa classify intent via `workflow-router`
- Orchestrator bisa assign roles via `role-switcher`
- **Tapi tidak ada layer yang meng-compose kedua output tersebut menjadi concrete plan** dengan profile IDs, dependency ordering, dan reviewer assignment yang tervalidasi

Akibatnya: dispatch (#308) tidak punya input yang well-formed, dan setiap orchestrator perlu "reinvent" logic routing manual.

---

## Objective

Build a **deterministic planner** yang meng-compose output `workflow-router` + `role-switcher` + profile availability menjadi `task_routing_plan.yaml` yang validates against `schemas/auto-routing/task-routing-plan.schema.yaml`.

Planner output adalah `PLAN_ONLY` — bukan execution evidence. Dispatch (#308) mengkonsumsi plan ini.

---

## User Stories

### US-1 — Routing tepat per intent
> Sebagai orchestrator, ketika menerima request user, aku ingin planner menghasilkan plan yang memanggil **hanya specialist yang justified**, bukan semua 7 profile.

**Scenarios:**
- `redesign UI halaman X` → plan: agent-design + agent-frontend + agent-review (backend/product tidak ikut)
- `Fix backend bug di endpoint Y` → plan: agent-backend + agent-review only
- `Bikin PRD fitur Z` → plan: agent-product + optional agent-architecture/design
- `Review PR ini` → plan: agent-review only, no implementation workers

### US-2 — Block pada ambiguity
> Sebagai orchestrator, ketika request tidak jelas, aku ingin planner **menolak membuat plan** dan output `BLOCKED` dengan justifikasi, bukan menebak.

**Scenarios:**
- Request tanpa context cukup → `status: blocked`, `blocking_reason` explicit
- Missing required context (repo, stack) → `status: not_verified`

### US-3 — Exactly-one-workflow invariant
> Sebagai consumer downstream (#308), aku ingin setiap plan **punya tepat satu `primary_workflow`**, tidak boleh kosong atau lebih dari satu.

### US-4 — Reviewer independence
> Sebagai orchestrator, aku ingin planner **auto-assign reviewer** dengan `independence_target: VERIFIED` ketika reviewer profile berbeda dari semua worker profiles dalam plan.

---

## Scope

### In scope
- Normalisasi request/product/repository context untuk routing
- Compose `workflow-router` + `role-switcher` output → `task_routing_plan`
- Map owner, specialists, reviewers ke durable profile IDs (`agent-*`)
- Pilih smallest justified profile set (no over-dispatch)
- Block on: ambiguity, stale/missing context, unavailable profiles, duplicate ownership, missing reviewer coverage
- Output `PLAN_ONLY` — tidak trigger durable task mutation
- Planner fixtures: positive (4 happy-path scenarios) + negative (ambiguity + missing context)
- Unit tests validasi plan output against schema
- Behavioral test cases (`.test.yaml`) untuk `skill-eval`

### Out of scope
- Actual dispatch ke specialist profiles (→ #308)
- Review loop dan synthesis (→ #309)
- Runtime acceptance fixtures (→ #310)
- Schema fixes dari dogfood findings (→ #312)

---

## Acceptance Criteria

| # | Criterion | Test |
|---|---|---|
| AC-1 | `redesign UI` request → plan routes to design/frontend/review only | `positive-redesign-ui-plan.yaml` |
| AC-2 | Backend bug request → plan routes to backend/review only | `positive-backend-bug-plan.yaml` |
| AC-3 | PRD request → plan routes to product + optional arch/design | `positive-prd-plan.yaml` |
| AC-4 | Review-only request → plan routes to review, no implementation workers | `positive-review-only-plan.yaml` |
| AC-5 | Not every task invokes every specialist | Verified across all positive fixtures |
| AC-6 | Ambiguous request → `status: blocked` dengan `blocking_reason` | `negative-ambiguous-request.yaml` |
| AC-7 | Missing context → `status: not_verified` | `negative-missing-context.yaml` |
| AC-8 | Plan validates against `task-routing-plan.schema.yaml` | `python3` jsonschema validation |
| AC-9 | Package + unit + behavioral tests pass | CI green |

---

## Technical Design

### Planner location

Skill ini Hermes-specific (fleet profile IDs, dispatch contract) tapi di-publish di `ai-native-skills` repo supaya versioned, reviewable, dan bisa jadi reference buat fleet lain yang adopt pattern yang sama. Parallel ke `hermes-agent-fleet-bootstrap` yang sudah ada.

```
skills/hermes-auto-routing-planner/
  SKILL.md                    ← skill definition, procedure, quality gates
  references/
    planner-procedure.md      ← step-by-step composition logic
  assets/
    plan.template.yaml        ← plan output template
contracts/fixtures/auto-routing/
  positive-redesign-ui-plan.yaml
  positive-backend-bug-plan.yaml
  positive-prd-plan.yaml
  positive-review-only-plan.yaml
  negative-ambiguous-request.yaml
  negative-missing-context.yaml
tests/auto-routing/
  test-planner.test.yaml      ← behavioral test cases
  test_planner_schema.py      ← unit tests (jsonschema validation)
```

### Planner composition steps
```
1. Receive user request + context
2. Run workflow-router → get primary_workflow
3. Run role-switcher → get owner + specialists + reviewers
4. Validate: exactly-one-workflow, no-duplicate-owner, reviewer != worker
5. Map roles to profile IDs (agent-design, agent-frontend, etc.)
6. Apply smallest-set filter — drop unjustified specialists
7. Assign dependency ordering (design → frontend → review)
8. Set independence_target for each reviewer
9. Emit task_routing_plan → validate against schema
10. Return PLAN_ONLY output
```

### Profile ID mapping
| Role | Profile ID |
|---|---|
| Design | `agent-design` |
| Frontend implementation | `agent-frontend` |
| Backend implementation | `agent-backend` |
| Product/PRD | `agent-product` |
| Architecture | `agent-architecture` |
| Independent review | `agent-review` |
| Orchestration | `agent-orchestrator` |

---

## Dependencies

| Dependency | Status |
|---|---|
| #305 — Auto-routing schemas | ✅ Merged (PR #311) |
| `workflow-router` skill | ✅ Available |
| `role-switcher` skill | ✅ Available |
| `task-routing-plan.schema.yaml` | ✅ Available |

## Blocks

| Blocked issue | Why |
|---|---|
| #308 — Durable dispatch | Needs well-formed plan as input |
| #309 — Review + synthesis | Needs plan + dispatch receipts |
| #310 — Fixtures + docs | Needs planner fixtures as examples |

---

## Branch & PR Topology

```
base branch:  main
branch name:  feat/307-auto-routing-planner
PR target:    main
rationale:    Schema+skill-only slice, no runtime code impact,
              independently releasable per #304 policy
```

---

## Definition of Done

- [ ] `skills/auto-routing-planner/SKILL.md` exists dan sesuai skill package standard
- [ ] 4 positive fixtures + 2 negative fixtures valid against schema
- [ ] `test_planner_schema.py` passes
- [ ] `test-planner.test.yaml` behavioral cases defined
- [ ] CI green
- [ ] PR merged ke `main`
- [ ] Issue #307 closed
