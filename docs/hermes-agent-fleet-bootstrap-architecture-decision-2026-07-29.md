# Hermes Specialist Agent Fleet Bootstrap — Architecture and Authority Decision

Issue: `puterakahfi/ai-native-skills#261`  
Parent epic: `puterakahfi/ai-native-skills#260`  
Date: 2026-07-29  
Status: `PROPOSED_FOR_OWNER_REVIEW`

## 1. Decision summary

```yaml
decision:
  capability_id: hermes-agent-fleet-bootstrap
  public_name: Hermes Specialist Agent Fleet Bootstrap
  repository: puterakahfi/ai-native-skills
  package_type: skill
  pattern: facade_composer
  runtime_target: hermes

  default_topology: orchestrator_with_specialists
  default_gateway_policy: orchestrator_only
  specialist_runtime_mode: kanban_on_demand
  persistent_identity_unit: hermes_profile

  fleet_composition_owner: hermes-agent-fleet-bootstrap
  single_profile_materialization_owner: hermes-profile-bootstrap
  primary_workflow_owner: workflow-router
  task_role_composition_owner: role-switcher
  capability_composition_sources:
    - capability-discovery catalog
    - job-profile catalog
    - skill metadata and dependencies
  durable_coordination_owner: hermes_kanban_or_runtime_adapter
  product_context_owner: product_repositories
  product_acceptance_owner: product_authority

  core_rfc_verdict: NO_CORE_CHANGE_FOR_MVP
  runtime_control_plane_choice: OUT_OF_SCOPE
  architecture_review: REQUIRED
  owner_approval: ROUTE_FOR_APPROVAL
```

The approved implementation must not create:

- a second primary workflow router;
- a competing end-to-end product or engineering lifecycle;
- one persistent profile for every framework, method, or lifecycle phase;
- one bot for every specialist by default;
- a duplicate single-profile generator;
- an autonomous swarm with uncontrolled all-to-all communication;
- a reusable profile distribution containing product facts, secrets, or live runtime state.

The operating model is:

```text
user
→ one bot, CLI, Desktop, or other front door
→ engineering-orchestrator profile
→ one governing workflow selected by workflow-router
→ bounded durable tasks and shared artifacts
→ specialist Hermes profiles executed as on-demand workers
→ independent reviewer profile
→ orchestrator synthesis
→ product authority for acceptance or authorization
```

## 2. Execution context

```yaml
work_item: puterakahfi/ai-native-skills#261
parent_epic: puterakahfi/ai-native-skills#260
primary_workflow: spec-workflow
owner: native-ai-engineer
specialists:
  - systems-reasoning
  - master-engineer
  - decision-provenance
reviewer:
  - architecture-review
repository: puterakahfi/ai-native-skills
integration_branch: 260-hermes-agent-fleet-bootstrap
working_branch: 261-fleet-architecture-contracts
pr_target: 260-hermes-agent-fleet-bootstrap
source_main_revision: 7e629ceed27b6764119a89453ddf40041e15e50a
```

This slice owns architecture, authority, schemas, and downstream constraints. It does not implement the executable skill, provision Hermes profiles, create credentials, run a real fleet, approve merge, or authorize release.

## 3. Evidence inspected

| Evidence | Effective finding |
|---|---|
| `skills/hermes-profile-bootstrap/SKILL.md` | Existing capability owns one Hermes profile skeleton, skill preset, installation plan, verification plan, and safety exclusion policy. It is not a fleet composer. |
| `skills/hermes-profile-bootstrap/references/generation.md` | A reusable profile contains identity/config defaults, skill lock, scripts, and documentation; live sessions, memory, state databases, credentials, logs, and secrets are excluded. |
| `skills/hermes-profile-bootstrap/references/skill-packs.md` | Current presets are broad workstation bundles. Fleet composition needs responsibility-specific manifests rather than installing the complete engineering preset into every specialist. |
| `catalog/capability-discovery/job-profiles.json` | Job profiles are workflow/capability compositions and do not replace executable procedures or routing. Current published profiles cover Product Planning, Engineering Quality, and Security Engineering. |
| `docs/skills.md` | A skill performs one reusable capability; a workflow owns a lifecycle; a meta-skill only routes or composes and then hands off. Product/framework facts are not universal skill identities. |
| `docs/facade-skill-pattern.md` | A facade remains a skill when it performs applicability decisions, evidence normalization, artifact assembly, conflict handling, and a shared verdict instead of only routing. |
| `docs/skill-package-standard.md` | Architecture decisions belong in repository `docs/`; runtime templates and schemas belong in the skill package `assets/`; behavioral contracts remain in `contracts/tests/`. |
| `skills/workflow-router/SKILL.md` | Exactly one primary workflow is selected from requested outcome; platform/domain nouns do not create competing lifecycles. |
| `skills/role-switcher/SKILL.md` | One owner, narrow specialists, and independent reviewers are composed per task; role names alone are not execution evidence. |
| Epic `#260` | Owner-approved product direction is one bot/front door, one orchestrator, specialist worker profiles, independent review, dry-run, idempotency, and non-destructive migration. |

## 4. System model

### 4.1 Purpose

Convert an engineering-organization request into the smallest justified, reproducible, safe, and verifiable Hermes specialist fleet.

### 4.2 Actors

```text
user or product authority
engineering-orchestrator profile
specialist profiles
reviewer profiles
Hermes gateway/front door
Hermes Kanban or durable coordination adapter
hermes-profile-bootstrap
capability/job-profile catalogs
product repositories
runtime host and operating system
```

### 4.3 Core capabilities

```text
normalize fleet intent
inspect existing profiles
justify or reject multi-agent
select the simplest sufficient topology
classify profile vs skill vs workflow vs delegation
produce profile responsibility contracts
resolve skills from verified catalogs
plan gateways, tools, models, permissions, and memory
plan per-profile bootstrap
plan safe migration
validate ownership and communication topology
produce readiness and execution receipts
```

### 4.4 Invariants

1. One substantive task has one governing workflow.
2. One fleet has one orchestration owner unless an explicit topology exception is justified.
3. One artifact or decision has one accountable owner.
4. Persistent profiles are created for stable responsibility, not for technology names alone.
5. Specialists may be broad enough to collaborate but must have one deep bounded responsibility.
6. The orchestrator coordinates and synthesizes; it does not silently absorb specialist or acceptance authority.
7. Review evidence is separate from implementation evidence.
8. A Hermes profile is an identity/state boundary, not automatic operating-system sandboxing.
9. A bot or gateway is an optional communication surface, not the agent identity itself.
10. Product truth, approval, credentials, and live runtime state do not enter reusable profile distributions.
11. Missing evidence remains `NOT_VERIFIED`; it is not guessed or converted into `PASS`.
12. Runtime execution, review, approval, authorization, delivery, and product acceptance remain separate records.

## 5. Decision D-1 — Implement a facade/composer skill

Create `hermes-agent-fleet-bootstrap` as:

```yaml
metadata:
  ai-native-skills.type: skill
  ai-native-skills.pattern: facade
```

It remains a `skill` because it performs coherent fleet-design work beyond routing:

- multi-agent applicability and justification;
- topology selection;
- responsibility and artifact ownership design;
- capability-versus-agent classification;
- profile contract and manifest assembly;
- conflict and safety validation;
- migration planning;
- normalized readiness verdict and execution handoff.

It is not a workflow because it does not own product, feature, bugfix, review, deployment, or agent-development lifecycle execution. It is not a meta-skill because it does more than choose capabilities and stop after handoff.

## 6. Decision D-2 — One front door is the default, not one bot per profile

Default gateway policy:

```yaml
gateway_policy:
  engineering-orchestrator: messaging_front_door
  specialist_profiles: none
  dedicated_gateway_exception:
    allowed_when:
      - independently_product_facing
      - independently_operational
      - distinct_audience_or_tenant
      - distinct_security_or_permission_boundary
    evidence_required: true
```

A profile remains a durable agent identity without a dedicated bot. Specialist profiles are addressable by the orchestrator or durable task dispatcher.

Dedicated bots are exceptions, not a convenience default. The fleet report must disclose their cost, audience, permission boundary, and routing implications.

## 7. Decision D-3 — Persistent specialist identities, on-demand worker processes

The persistence model is:

```text
Hermes profile
  durable identity, SOUL, config defaults, skills, memory scope,
  session namespace, cron responsibility, and runtime state

worker process
  a bounded execution of that profile for an assigned task

Kanban task or runtime work item
  durable coordination state, dependencies, handoff, retry, and evidence
```

A specialist profile may exist continuously while its worker process starts only when assigned work is ready.

The fleet bootstrap skill specifies this topology. Actual worker spawning, retries, scheduling, and durable task persistence remain runtime-owned.

## 8. Decision D-4 — Use the smallest effective T-shaped fleet

A persistent profile is justified only when several of these are evidenced:

- stable recurring responsibility;
- distinct durable memory scope;
- materially different skill composition;
- materially different model policy;
- materially different tools or credentials;
- meaningful permission or blast-radius boundary;
- independent evaluation requirement;
- durable task ownership;
- clear recurring inputs, outputs, and handoffs.

Otherwise classify the request as a skill, workflow, overlay, reviewer, delegated subagent, or product context.

The skill must return `NOT_JUSTIFIED` when one profile plus selected capabilities is sufficient.

Specialists are T-shaped:

```text
deep expertise in one responsibility
+ enough adjacent understanding for contracts and handoffs
- no authority to absorb unrelated product or lifecycle decisions
```

## 9. Decision D-5 — Responsibility archetypes, not framework agents

Default candidate archetypes:

| Profile | Owns | Does not own |
|---|---|---|
| `engineering-orchestrator` | intake normalization, workflow/role handoff, decomposition, dependency coordination, evidence aggregation, synthesis | PRD content, architecture decisions, implementation, self-review, product acceptance, deployment authorization |
| `product-development` | product discovery, Product Brief/PRD composition, MVP scope, success metrics, product acceptance criteria, product validation handoff | technical architecture, framework choice, production implementation, deployment |
| `solution-architecture` | system boundaries, technical specification, domain/API/data/integration architecture, NFR trade-offs, ADRs | product priority, visual design, sole implementation acceptance |
| `product-design` | information architecture, user flows, interaction behavior, visual/design-system direction, design acceptance criteria | frontend implementation ownership, backend domain rules, release authority |
| `frontend-engineering` | frontend architecture and implementation, accessibility implementation, responsive behavior, browser performance, frontend tests | product strategy, backend domain authority, design approval of its own work |
| `backend-platform` | domain/application services, APIs, persistence, integrations, jobs/events, backend tests and observability instrumentation | product scope, UI behavior, architecture approval of its own work, deployment authorization |
| `quality-review` | independent acceptance verification, code/test evidence review, architecture conformance, regression and readiness verdict | primary implementation, product scope changes, merge or release authorization |

Conditional archetypes:

```text
platform-operations
documentation-engineering
security-engineering
ai-agent-engineering
data-engineering
```

React, Next.js, Tailwind, SOLID, DDD, design patterns, TDD, API design, and equivalent methods are skills, repository adapters, or evidence—not persistent profile identities by default.

## 10. Decision D-6 — Explicit classification contract

Every requested concept receives one classification:

```text
PROFILE
SKILL
WORKFLOW
OVERLAY
REVIEWER
DELEGATED_SUBAGENT
PRODUCT_CONTEXT
NOT_JUSTIFIED
```

Required fields:

```yaml
classification:
  concept: string
  verdict: PROFILE | SKILL | WORKFLOW | OVERLAY | REVIEWER | DELEGATED_SUBAGENT | PRODUCT_CONTEXT | NOT_JUSTIFIED
  rationale: string
  evidence_refs: []
  owner: string | null
  recurring_value: VERIFIED | LIMITED | NOT_VERIFIED
  persistence_need: VERIFIED | LIMITED | NOT_VERIFIED
```

A technology-shaped profile request without recurring responsibility evidence fails the persistent-profile gate.

## 11. Decision D-7 — Sparse coordination through an orchestrator and shared artifacts

Default interaction modes:

```text
orchestrator invocation
durable Kanban task
temporary delegation
shared artifact handoff
review feedback loop
human approval
```

Unbounded all-to-all profile communication is rejected by default because it obscures authority, multiplies context, propagates errors, and weakens provenance.

Every handoff identifies:

- producer;
- consumer;
- artifact or decision;
- accepted structure;
- status;
- evidence;
- unresolved risks;
- retry or correction route.

The orchestrator may route artifacts but must not rewrite specialist decisions silently.

## 12. Decision D-8 — Ownership and reviewer independence

Every fleet manifest must prove:

```text
one orchestration owner
one accountable owner per durable artifact or decision
no circular required handoffs
no duplicate primary responsibility
required reviewer differs from primary implementer
review coverage and independence are explicit
```

Reviewer independence states:

```text
VERIFIED
LIMITED_SHARED_MODEL
LIMITED_SHARED_CONTEXT
LIMITED_SHARED_TOOLS
NOT_VERIFIED
```

A different profile name alone does not prove independence. Missing independence may produce a limited review but cannot be normalized into fully independent acceptance.

## 13. Decision D-9 — Catalog-driven skill composition

Profile skill selection authority is:

```text
capability-discovery classifications
→ job-profile compositions when available
→ capability metadata and dependencies
→ Hermes-specific archetype template
→ product/runtime availability and policy
```

The fleet skill must not maintain a second unrelated catalog of all capabilities.

Current job profiles do not cover every proposed specialist. Downstream implementation therefore uses them where applicable and supplements them with explicit, reviewable Hermes archetype templates that reference canonical capability IDs.

The existing broad `engineering` preset is not copied into every specialist. Each profile receives the smallest responsibility-specific manifest plus mandatory routing/runtime foundations justified by its job.

## 14. Decision D-10 — Compose, do not duplicate, single-profile bootstrap

For each approved profile contract, `hermes-agent-fleet-bootstrap` produces one handoff to `hermes-profile-bootstrap` containing:

```yaml
profile_bootstrap_handoff:
  runtime_target: hermes
  profile_name: string
  preset: minimal | engineering | product | runtime-ops | full | custom
  skill_catalog_source: string
  safety_constraints: []
  profile_contract_ref: string
  skills_lock_plan: string
  model_policy: {}
  toolset_policy: {}
  verification_policy: {}
  dry_run: boolean
```

`hermes-profile-bootstrap` remains the owner of profile skeleton paths, creation commands, safe defaults, installation, and per-profile verification.

The fleet skill owns cross-profile uniqueness, topology, ownership, gateway allocation, handoffs, and integrated readiness.

## 15. Decision D-11 — Preserve product agents and migrate non-destructively

Existing profiles such as `pkahfi`, `visualmate`, `docs`, and `ai` may be valid product-facing agents.

They are not automatically replaced by engineering specialists. Each existing profile is classified as:

```text
KEEP
KEEP_AS_PRODUCT_AGENT
CONVERT_TO_SPECIALIST
MERGE
SPLIT
REGENERATE
DEPRECATE
NOT_VERIFIED
```

MVP produces recommendations and intended actions only. It must not delete, overwrite, merge, move memory, copy credentials, or mutate live state without a separately authorized runtime action.

Product-specific truth remains in product repositories or product bindings. Reusable specialist profiles may reference a product context but may not bake it into identity or distribution.

## 16. Decision D-12 — Permissions are explicit; profiles are not automatic sandboxes

Profile separation provides Hermes identity and state separation. It does not prove filesystem, process, network, repository, or credential isolation at the operating-system layer.

Every profile contract declares:

```yaml
permission_policy:
  filesystem_scope: string | NOT_VERIFIED
  repository_scope: []
  network_scope: string | NOT_VERIFIED
  credential_scope: string | NOT_VERIFIED
  mutation_authority: read_only | bounded_write | privileged | NOT_VERIFIED
  sandbox_evidence: []
```

Privileged profiles such as `platform-operations` require a distinct permission boundary and explicit human authorization for destructive or production actions.

## 17. Decision D-13 — Separate execution, review, authority, and acceptance

Fleet bootstrap records must not collapse these states:

```text
profile specification
generation plan
profile creation or audit execution
verification evidence
review verdict
owner approval
merge/release/deployment authorization
product acceptance
real-world validation
```

A dry-run or generated manifest does not prove profiles exist. Profile existence does not prove skills are installed. Installed skills do not prove behavioral expertise. Worker completion does not prove independent review. Review does not authorize release.

## 18. Decision D-14 — No Core contract for MVP

```text
NO_CORE_CHANGE_FOR_MVP
```

The immediate capability is Hermes-specific and has not been validated across multiple runtimes. Stable runtime-agnostic semantics may be proposed to `ai-native-core` only after the real Hermes case in #265 and cross-adapter evidence justify promotion.

The repository-level skill may define local schemas and typed findings without representing them as universal Core contracts.

## 19. Contract assets required from downstream implementation

Issue #262 must create or equivalent:

```text
skills/hermes-agent-fleet-bootstrap/
├── SKILL.md
├── references/
│   ├── topology-selection.md
│   ├── specialist-archetypes.md
│   ├── collaboration-and-handoffs.md
│   ├── migration-planning.md
│   └── verification.md
└── assets/
    ├── normalized-fleet-request.template.yaml
    ├── profile-contract.template.yaml
    ├── fleet-manifest.template.yaml
    ├── collaboration-manifest.template.yaml
    ├── artifact-handoff.template.yaml
    ├── migration-plan.template.yaml
    ├── verification-report.template.yaml
    └── execution-receipt.template.yaml

contracts/tests/hermes-agent-fleet-bootstrap.test.yaml
```

If deterministic schema validation is implemented through scripts, #264 must add corresponding package-local tests.

The normative data shapes are defined in:

```text
docs/hermes-agent-fleet-bootstrap-contracts-2026-07-29.md
```

## 20. Readiness and typed findings

Fleet readiness states:

```text
READY
READY_WITH_LIMITATIONS
NEEDS_WORK
BLOCKED
NOT_VERIFIED
```

Minimum typed findings:

```text
MULTI_AGENT_NOT_JUSTIFIED
ORCHESTRATOR_MISSING
MULTIPLE_ORCHESTRATORS
PROFILE_RESPONSIBILITY_OVERLAP
DUPLICATE_ARTIFACT_OWNER
TECHNOLOGY_ONLY_PROFILE
CIRCULAR_HANDOFF
REQUIRED_REVIEWER_MISSING
REVIEWER_NOT_INDEPENDENT
UNBOUNDED_COMMUNICATION_TOPOLOGY
EXCESSIVE_GATEWAY_ALLOCATION
CAPABILITY_NOT_FOUND
CAPABILITY_VERSION_INCOMPATIBLE
PROFILE_STATE_NOT_INSPECTABLE
PRODUCT_CONTEXT_LEAKAGE
PROHIBITED_LIVE_STATE
PERMISSION_BOUNDARY_NOT_VERIFIED
RUNTIME_COMMAND_UNAVAILABLE
PROFILE_BOOTSTRAP_FAILED
FLEET_VERIFICATION_FAILED
EVIDENCE_MISSING
```

## 21. Repository ownership matrix

| Concern | `ai-native-core` | `ai-native-skills` | Hermes/runtime adapter | Product repository |
|---|---|---|---|---|
| Multi-agent universal semantics | Future RFC only after evidence | Local MVP decision and executable skill | Consumes local contracts | Supplies real cases |
| Fleet applicability/topology | No MVP contract | Owns procedure and normalized artifacts | Executes supported topology | Supplies requirements and constraints |
| Profile skeleton/materialization | No new contract | `hermes-profile-bootstrap` adapter guidance | Executes Hermes commands/paths | Supplies authorization only |
| Workflow routing | Owns canonical contract | `workflow-router` implementation | Consumes routing output | Supplies context |
| Task role composition | Owns canonical contract | `role-switcher` implementation | Executes selected profiles | Supplies local policy |
| Durable tasks/worker scheduling | No storage implementation | Declares required handoff/evidence | Owns Kanban/dispatcher/state | Supplies repositories and runtime access |
| Product identity and acceptance | Preserves distinction | Must not infer | Stores or projects records only | Owns truth and authority |
| Credentials, bots, production access | No secrets | Excludes from distributions | Owns live configuration and isolation | Owns authorization policy |

## 22. Delivery topology

```text
main
└── 260-hermes-agent-fleet-bootstrap
    ├── 261-fleet-architecture-contracts
    ├── 262-fleet-bootstrap-skill
    ├── 263-fleet-integrations-migration
    ├── 264-fleet-validators-evals
    └── 265-fleet-real-runtime-acceptance
```

Child PRs target `260-hermes-agent-fleet-bootstrap`. Green child CI or architecture review does not prove Epic acceptance or grant merge/release authority.

## 23. Downstream handoffs

### #262 — Skill implementation

Implement the facade procedure and authored package assets without duplicating profile generation or capability catalogs.

### #263 — Integrations and migration

Bind to existing catalogs and `hermes-profile-bootstrap`; prove dry-run, idempotency, safety exclusions, and non-destructive migration behavior.

### #264 — Validators and behavioral evals

Implement positive/negative fixtures, schema or template validation, deterministic replay, safety gates, and independent skill QA.

### #265 — Real Hermes acceptance

Verify one-bot/orchestrator plus specialist workers on an actual Hermes runtime. Missing runtime access is a valid blocker, not a simulated pass.

## 24. Rejected alternatives

- One full generalist profile for all engineering work: rejected as the only default because it weakens depth, independent review, permission separation, and durable responsibility.
- One agent per framework or method: rejected as unstable and excessively granular.
- One bot per specialist: rejected as default because it exposes internal topology, fragments conversation, and increases routing and credential overhead.
- A new multi-agent workflow: rejected because product/feature/bugfix/review/deployment workflows already own lifecycles.
- A new global meta-router: rejected because `workflow-router` and `role-switcher` already own task routing and role composition.
- Copy the full engineering preset into every worker: rejected because it recreates generalists and increases context/tool overlap.
- Replace app profiles with engineering specialists automatically: rejected because product-facing identities and memories may be valid.
- Put live Hermes state in reusable distributions: rejected for safety and reproducibility.
- Promote a universal Core contract now: rejected pending real runtime and cross-adapter evidence.

## 25. Acceptance assessment

| Criterion | Status | Evidence or gap |
|---|---|---|
| Capability boundary versus router/workflow/profile bootstrap is explicit | `PASS` | Decisions D-1, D-9, and D-10. |
| One-bot/orchestrator plus headless worker semantics are explicit | `PASS` | Decisions D-2 and D-3. |
| Agent versus skill classification is explicit | `PASS` | Decisions D-4 through D-6. |
| Ownership, sparse communication, and reviewer independence are explicit | `PASS` | Decisions D-7 and D-8. |
| Product context and migration boundaries are explicit | `PASS` | Decision D-11. |
| Permission/sandbox boundary is explicit | `PASS` | Decision D-12. |
| Runtime record families remain separated | `PASS` | Decision D-13. |
| Downstream templates and findings are specified | `PASS` | Sections 19 and 20 plus contracts document. |
| Core RFC decision is explicit | `PASS` | `NO_CORE_CHANGE_FOR_MVP`. |
| Real Hermes runtime proof | `NOT_VERIFIED` | Deferred to #265. |
| Independent external architecture review | `LIMITED` | Same execution context; owner/separate review required. |
| Owner approval of exact decision record | `ROUTE_FOR_APPROVAL` | Pending review of this artifact. |

## 26. Capability evolution verdict

```text
LOCAL_ONLY
```

This decision defines an adapter-local reusable capability and downstream validation hypothesis. Promotion or broader evolution is deferred until #265 produces real Hermes evidence and `skill-evolution` review.
