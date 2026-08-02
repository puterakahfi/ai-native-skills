---
name: hermes-agent-fleet-bootstrap
description: Design, bootstrap, audit, reconcile, and verify the smallest justified fleet of persistent Hermes agents. Use when a Hermes setup needs one orchestrator plus bounded product, architecture, design, implementation, or review specialists; when deciding whether a capability should be a profile, skill, workflow, reviewer, delegated subagent, or product context; or when planning a non-destructive migration from legacy profiles. Do not use for ordinary single-profile creation, task-time product delivery, secret provisioning, destructive migration, or unsupported runtime claims.
license: MIT
metadata:
  ai-native-skills.version: 0.2.1
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.pattern: facade
  ai-native-skills.requires: "workflow-router role-switcher hermes-profile-bootstrap decision-provenance skill-eval"
  ai-native-skills.related_skills: '["hermes-profile-bootstrap","workflow-router","role-switcher","implementation-context-discovery","product-manager","master-engineer","architecture-review","security-review","skill-eval"]'
  ai-native-skills.boundary.covers: '["fleet_request_normalization","multi_agent_justification","topology_selection","profile_responsibility_contracts","profile_skill_manifest_composition","gateway_and_bot_policy","collaboration_and_artifact_handoff_contracts","ownership_and_cycle_validation","non_destructive_profile_migration_planning","per_profile_bootstrap_handoffs","deterministic_preset_execution","fleet_readiness_and_receipt"]'
  ai-native-skills.boundary.delegates: '["single_profile_materialization","task_time_primary_workflow_selection","task_time_role_assignment","product_or_repository_truth","kanban_dispatcher_execution","bot_token_or_secret_provisioning","operating_system_sandboxing","implementation_delivery","merge_release_deployment_or_product_acceptance_authorization"]'
---

# Hermes Agent Fleet Bootstrap

Design the smallest effective Hermes agent fleet, then delegate each approved concrete profile to `hermes-profile-bootstrap` for creation or audit.

## Boundary

```text
hermes-agent-fleet-bootstrap
  fleet applicability, topology, agent identities,
  profile contracts, skill composition, gateway policy,
  identity-state audit, migration planning,
  deterministic preset execution, verification, receipts

hermes-profile-bootstrap
  one concrete profile skeleton, safe defaults,
  skill installation plan, and profile verification

workflow-router
  exactly one primary workflow for an actual task

role-switcher
  one task owner, bounded specialists, and reviewers

Hermes runtime
  durable tasks, worker execution, retry, gateway, and runtime state

product repositories
  product truth, local architecture, authorization, implementation, and acceptance
```

This capability is a facade/composer. It is not a second engineering lifecycle or a replacement for task-time routing.

## Default operating model

```text
user
→ one bot or front door
→ agent-orchestrator
→ one primary workflow
→ Hermes Kanban or verified durable coordination
→ smallest relevant set of headless agent-* specialists
→ agent-review when independent verification is required
→ agent-orchestrator synthesis
→ response through the originating gateway
```

The reusable fleet ID remains:

```text
native-ai-engineering
```

The approved v2 target identities are:

```text
agent-orchestrator
agent-product
agent-architecture
agent-design
agent-frontend
agent-backend
agent-review
```

Only `agent-orchestrator` is gateway-eligible by default. All six specialists use:

```yaml
gateway: none
worker_mode: headless_on_demand
```

A profile is a durable runtime identity. A bot is an optional communication surface. Product and repository identities remain task context rather than reusable fleet profile names.

## Product and environment boundary

The fleet is product-neutral and local to a verified trust environment. It is not tied to VisualMate, pkahfi, an employer, a repository, a client, or any other named product.

A product or repository does not automatically require a persistent product profile. Small or occasional work may pass bounded product and repository context directly to `engineering-orchestrator`. Create a durable product or domain profile only when recurring product intent, terminology, accepted decisions, stakeholders, approval flow, or product-facing interaction justify persistent context.

Product profiles remain product-context custodians and product-facing authorities. They do not automatically receive the full engineering skill suite or own architecture, frontend, backend, testing, security review, or deployment.

Personal, office, client, tenant, and confidentiality environments must not silently share profiles, memory, sessions, credentials, Kanban state, or product context. Prefer separate hosts or separate `HERMES_HOME` roots. Separate Hermes homes isolate Hermes-managed application state but do not prove operating-system or credential sandboxing.

Load `references/product-context-and-environments.md` before deciding product-profile granularity, sharing one fleet across products, or separating personal and office environments.

## Primary invocation

The installed Hermes slash command is the normal user interface:

```text
/hermes-agent-fleet-bootstrap bootstrap native-ai-engineering
/hermes-agent-fleet-bootstrap bootstrap native-ai-engineering --apply
/hermes-agent-fleet-bootstrap audit native-ai-engineering
/hermes-agent-fleet-bootstrap reconcile native-ai-engineering
/hermes-agent-fleet-bootstrap reconcile native-ai-engineering --apply
/hermes-agent-fleet-bootstrap sync-models native-ai-engineering
/hermes-agent-fleet-bootstrap sync-models native-ai-engineering --apply
```

Interpret arguments as:

```text
/hermes-agent-fleet-bootstrap <operation> <preset> [--apply] [supported executor flags]
```

Fleet bootstrap, reconcile, and audit execute through:

```bash
bash "${HERMES_SKILL_DIR}/scripts/hermes-fleet" \
  <operation> <preset> [--apply] [supported executor flags]
```

Model-policy synchronization executes through:

```bash
bash "${HERMES_SKILL_DIR}/scripts/hermes-fleet-model-sync" \
  <preset> [--apply] [supported model-sync flags]
```

Do not manually reproduce deterministic profile, skill, Kanban, model-policy, audit, or receipt mutations when the bundled runner is available. Preserve the executor exit code and return its receipt and limitations.

Without `--apply`, `bootstrap`, `reconcile`, and `sync-models` are plan-only. `audit` is always read-only. Mutation requires verified create/update authority.

## Deterministic operations

```text
bootstrap    create missing target profiles, synchronize managed skills and SOUL files, initialize Kanban
reconcile    compare and synchronize an approved target preset idempotently, including SOUL drift
audit        classify observed fleet identity state and inspect conformance without mutation
sync-models  synchronize approved non-secret model policy from the preset orchestrator
```

The executors do not invent topology, provision credentials, start gateways, delete profiles, or copy memory, sessions, cron, gateway state, Kanban databases, or runtime databases.

## Load references

- Load `references/topology-and-classification.md` for multi-agent justification, capability classification, and topology selection.
- Load `references/profile-archetypes.md` for the approved agent identity, responsibility contracts, and candidate specialist boundaries.
- Load `references/runtime-gateway-and-security.md` for the `agent-orchestrator` front door, headless worker policy, permissions, sandbox evidence, and runtime limitations.
- Load `references/product-context-and-environments.md` for product-neutral fleets, optional product profiles, domain profiles, and personal/office trust separation.
- Load `references/catalog-migration-and-idempotency.md` for capability resolution, existing-profile audit, migration planning, dry-run, and idempotency checks.
- Load `references/one-command-cli.md` before deterministic bootstrap, reconcile, or audit execution.
- Load `references/model-policy-sync.md` before model-policy synchronization.
- Load `references/auto-routing-contract.md` before planning task-time auto-routing, dispatching durable specialist workers, or auditing routing/dispatch/review/synthesis evidence.
- Load `assets/profile-identity-maps/native-ai-engineering-v1-to-v2.json` when planning legacy identity migration.
- Load `assets/*.template.yaml` only when producing machine-readable manifests.
- Load `assets/presets/native-ai-engineering.json` and other `assets/presets/*.json` only after the selected preset and mutation authority are explicit.

## Required input

```yaml
fleet_request:
  runtime_target: hermes
  desired_outcomes: []
  recurring_responsibilities: []
  products_or_repositories: []
  current_profiles: []
  requested_capabilities: []
  expected_users_or_audiences: []
  model_constraints: []
  tool_constraints: []
  permission_boundaries: []
  memory_requirements: []
  collaboration_constraints: []
  safety_constraints: []
  write_authorization: PLAN_ONLY | AUDIT_ONLY | CREATE_OR_UPDATE
```

Resolve fields from evidence or mark them `NOT_VERIFIED`. Never infer credentials, runtime state, product truth, isolation, or authorization.

## Procedure

Run phases in order. A later phase cannot normalize an earlier blocker into `PASS`.

### 1. Verify intent and authority

- Distinguish planning, audit, and create/update intent.
- Verify runtime target, selected preset, product/repository references, and write policy.
- Preserve missing evidence as `NOT_VERIFIED`.

Gate: intent, evidence posture, and authority are explicit.

### 2. Normalize requested capabilities

Convert implementation or methodology names into stable responsibility families.

```text
React, Next.js, CSS, component tests
→ frontend implementation capability

SOLID, DDD, patterns
→ architecture and engineering-quality skills

PRD, MVP, metrics
→ product responsibility

API, service, database, SDK
→ backend responsibility unless an independent SDK lifecycle is proven
```

Gate: every concept has a stable description or explicit unknown status.

### 3. Decide whether multiple persistent agents are justified

Return:

```yaml
multi_agent_verdict:
  status: JUSTIFIED | NOT_JUSTIFIED | LIMITED | NOT_VERIFIED
  reasons: []
  expected_benefits: []
  coordination_costs: []
  simpler_alternative: ""
```

Prefer one profile plus focused skills for narrow, occasional work sharing the same context, tools, permissions, and outputs.

Gate: profile count is justified by durable responsibility, not technology count.

### 4. Classify every concept

Choose exactly one primary form:

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

Stable recurring responsibility may become a profile. Frameworks and methods remain skills. Ordered lifecycles remain workflows. Temporary analysis remains delegation. Product facts remain product context.

Gate: no concept has duplicate primary classifications.

### 5. Select the simplest sufficient topology

Supported topology identities include:

```text
single_profile
orchestrator_with_specialists
reviewer_loop
parallel_specialists
product_agents_with_shared_engineering_fleet
operations_isolated_fleet
```

Reject uncontrolled all-to-all messaging. Parallel work requires independent tasks, workspace ownership, artifact contracts, and an integration owner.

Gate: one coordination owner, interaction modes, and coordination costs are explicit.

### 6. Define agent responsibility contracts

Use `references/profile-archetypes.md` and `assets/profile-contract.template.yaml`.

Every persistent agent declares:

- mission;
- owned and non-owned decisions/artifacts;
- required inputs and outputs;
- recurring responsibility;
- required and optional skills;
- model, tool, permission, and memory boundaries;
- gateway and worker mode;
- handoffs, reviewers, and completion evidence.

Use responsibility-specific custom skill manifests. Do not clone broad full-catalog presets into every worker.

Gate: every durable artifact and decision has one accountable owner.

### 7. Validate authority, safety, and independence

Fail closed on:

- duplicate or missing artifact owners;
- circular required handoffs;
- reviewer as sole implementer;
- default gateway per specialist without an independent audience;
- profiles defined by frameworks, methods, products, or repositories;
- product facts, secrets, or live state in reusable distributions;
- personal, office, client, tenant, or confidentiality contexts sharing one fleet without verified trust boundaries;
- assumed OS, filesystem, process, network, or credential isolation;
- privileged operations without bounded permissions and human approval.

Reviewer independence states:

```text
VERIFIED
LIMITED_SHARED_MODEL
LIMITED_SHARED_CONTEXT
LIMITED_SHARED_TOOLS
NOT_VERIFIED
```

Gate: no blocking conflict is hidden.

### 8. Define sparse, auditable collaboration

Use only explicit modes:

```text
orchestrator_invocation
durable_kanban_task
temporary_delegation
shared_artifact_handoff
review_feedback_loop
human_approval
```

Every handoff identifies producer, consumer, artifact/version, status, evidence, assumptions, risks, and correction route.

Gate: communication is directional and auditable.

### 9. Compose one profile-bootstrap handoff per target agent

```yaml
profile_bootstrap_handoff:
  capability: hermes-profile-bootstrap
  runtime_target: hermes
  profile_name: ""
  preset: custom
  skill_catalog_source: ""
  skills_required: []
  skills_optional: []
  model_policy: {}
  toolset_policy: {}
  verification_policy: {}
  safety_constraints: []
  product_context_reference: ""
  mutation_status: PLANNED | EXECUTED | BLOCKED | NOT_VERIFIED
```

Do not copy the single-profile generation procedure. A plan cannot claim profiles were created.

Gate: every persistent target agent has one materialization or audit handoff.

### 10. Classify observed fleet identity state

For versioned presets, classify profile directories before normal bootstrap or reconcile:

```text
EMPTY
TARGET_ONLY_COMPLETE
TARGET_ONLY_PARTIAL
LEGACY_ONLY_COMPLETE
LEGACY_ONLY_PARTIAL
MIXED
UNVERSIONED
```

Policy:

- `EMPTY`: fresh bootstrap may proceed.
- `TARGET_ONLY_COMPLETE`: audit or idempotent reconcile may proceed.
- `TARGET_ONLY_PARTIAL`: audit reports `NEEDS_WORK`; reconcile may create missing target profiles.
- `LEGACY_ONLY_COMPLETE` or `LEGACY_ONLY_PARTIAL`: audit reports migration required; bootstrap/reconcile are `BLOCKED`.
- `MIXED`: audit reports ambiguous migration state; bootstrap/reconcile are `BLOCKED`.

Ordinary bootstrap and reconcile must not rename, delete, reinterpret, or copy legacy profiles. Use the approved migration operation for legacy or mixed fleets.

Gate: identity generation and migration state are explicit before mutation.

### 11. Plan non-destructive migration separately

Legacy mapping is deterministic:

```text
engineering-orchestrator → agent-orchestrator
product-development      → agent-product
solution-architecture    → agent-architecture
product-design           → agent-design
frontend-engineering     → agent-frontend
backend-platform         → agent-backend
quality-review           → agent-review
```

Preserve legacy profiles and runtime-owned state. Never automatically copy `.env`, `auth.json`, tokens, credentials, memory, sessions, cron, gateway state, Kanban databases, or runtime databases.

Gate: migration recommendations remain distinct from executed bootstrap/reconcile actions.

### 12. Execute or audit deterministically

- `PLAN_ONLY`: list intended target profiles, skills, Kanban actions, identity state, and findings without mutation.
- `AUDIT_ONLY`: compare observed target/legacy identities and managed skills without mutation.
- `CREATE_OR_UPDATE`: execute only with an approved preset, verified runtime tools, and write authority.
- Preserve bundled executor receipts and exit codes.
- Do not use deterministic execution to bypass multi-agent justification, responsibility contracts, safety review, or authorization.

Gate: planned and executed states remain separate.

### 13. Verify readiness

Verify:

- preset version and identity generation;
- exact target profile IDs and one gateway owner;
- responsibility-specific skill packages;
- unique ownership and reviewer boundaries;
- observed identity state;
- plan/apply distinction and idempotency;
- secret and live-state exclusions;
- product/environment trust boundaries;
- runtime limitations;
- receipt completeness.

Use `assets/fleet-manifest.template.yaml` to record topology, unique identifiers, artifact ownership, custom skill manifests, profile-bootstrap handoffs, gateway policy, collaboration cycles, reviewer independence, safety exclusions, permissions, product/environment trust boundaries, runtime assumptions, migration safety, deterministic inputs, executable receipt, and idempotent replay.

Verdicts:

```text
READY
READY_WITH_LIMITATIONS
NEEDS_WORK
BLOCKED
NOT_VERIFIED
```

`READY` covers the fleet contract and managed preset state only. It does not prove Telegram dispatch, worker execution, product delivery, merge, release, deployment, or product acceptance.

## Allowed outputs

```text
normalized_fleet_request
multi_agent_verdict
capability_classification
fleet_topology
profile_contracts
fleet_manifest
collaboration_manifest
artifact_handoff_contracts
profile_bootstrap_handoffs
fleet_identity_state
migration_plan
verification_report
fleet_readiness_verdict
execution_receipt
```

## Quality gates

- Multi-agent is explicitly justified or rejected.
- The smallest sufficient topology is selected.
- One default orchestration owner exists unless an exception is justified.
- Only `agent-orchestrator` receives the default gateway.
- Specialists remain headless by default.
- Profiles own stable responsibilities, not framework, method, product, or repository names.
- A product or repository does not automatically require a product profile.
- A shared fleet is product-neutral and scoped to one verified trust environment.
- Personal, office, client, tenant, and confidentiality boundaries are separated or explicitly evidenced.
- Every durable artifact has one accountable owner.
- Skill manifests are responsibility-specific and catalog-resolvable.
- `agent-review` has no primary feature or bugfix implementation ownership.
- `hermes-profile-bootstrap` remains the per-profile executor.
- Deterministic execution uses an approved versioned preset.
- Legacy and mixed identity states fail closed outside migration.
- Plan-only, audit, and apply remain distinguishable.
- Repeated apply is idempotent and preserves unmanaged state.
- Review independence is evidenced or limited honestly.
- Product facts, credentials, and live state remain outside reusable distributions.
- Profile separation is not represented as OS sandboxing.
- Execution, review, approval, delivery, and acceptance remain distinct.

## Hard stops

Return `BLOCKED`, `NOT_VERIFIED`, or `READY_WITH_LIMITATIONS` when:

- current profiles cannot be inspected for requested migration;
- a legacy-only or mixed fleet is passed to ordinary bootstrap/reconcile;
- duplicate ownership or required cycles remain;
- required skills cannot be resolved;
- reviewer independence is required but unavailable;
- runtime behavior is assumed rather than observed;
- secret-free output cannot be proven;
- product/environment trust boundaries are missing;
- authority is missing;
- an approved preset is unavailable;
- Hermes preflight fails;
- the bundled executor cannot be resolved through `${HERMES_SKILL_DIR}`;
- a privileged profile lacks bounded permissions and human approval.

## Receipt

```yaml
fleet_bootstrap_receipt:
  schema_version: "2.0.0"
  request_mode: PLAN_ONLY | AUDIT_ONLY | CREATE_OR_UPDATE
  multi_agent_verdict: ""
  topology: ""
  preset_id: ""
  preset_version: ""
  identity_generation: 0
  orchestrator_profile: ""
  target_profile_ids: []
  fleet_identity_state: ""
  legacy_profiles_present: []
  profiles_proposed: []
  profiles_created_or_updated: []
  profiles_audited: []
  profile_bootstrap_handoffs: []
  gateways_planned_or_verified: []
  credentials_copied: false
  live_state_copied: false
  validations_executed: []
  actions: []
  findings: []
  readiness: READY | READY_WITH_LIMITATIONS | NEEDS_WORK | BLOCKED | NOT_VERIFIED
  runtime_execution: EXECUTED | PARTIAL | NOT_RUN | BLOCKED | NOT_VERIFIED
  review_independence: VERIFIED | LIMITED_SHARED_MODEL | LIMITED_SHARED_CONTEXT | LIMITED_SHARED_TOOLS | NOT_VERIFIED
  approval: VERIFIED | ROUTE_FOR_APPROVAL | NOT_VERIFIED
  merge_release_deploy_authorization: NOT_GRANTED | VERIFIED
  known_gaps: []
  next_action: ""
```
