---
name: hermes-agent-fleet-bootstrap
description: Design, bootstrap, audit, and verify the smallest justified fleet of persistent Hermes specialist profiles. Use when a Hermes engineering setup needs one orchestrator plus bounded product, architecture, design, frontend, backend, quality, operations, security, documentation, AI-agent, or data specialists; when deciding whether requested capabilities should be profiles, skills, workflows, reviewers, delegated subagents, or product context; or when migrating existing app-based profiles into a shared specialist fleet. Do not use for ordinary single-profile creation, task-time workflow routing, product delivery itself, bot-token provisioning, destructive profile migration, or unsupported runtime claims.
license: MIT
metadata:
  ai-native-skills.version: 0.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.pattern: facade
  ai-native-skills.requires: "workflow-router role-switcher hermes-profile-bootstrap decision-provenance skill-eval"
  ai-native-skills.related_skills: '["hermes-profile-bootstrap","workflow-router","role-switcher","capability-orchestration","implementation-context-discovery","product-manager","master-engineer","architecture-review","security-review","skill-eval"]'
  ai-native-skills.boundary.covers: '["fleet_request_normalization","multi_agent_justification","topology_selection","profile_responsibility_contracts","profile_skill_manifest_composition","gateway_and_bot_policy","collaboration_and_artifact_handoff_contracts","ownership_and_cycle_validation","non_destructive_profile_migration_planning","per_profile_bootstrap_handoffs","fleet_readiness_and_receipt"]'
  ai-native-skills.boundary.delegates: '["single_profile_materialization","task_time_primary_workflow_selection","task_time_role_assignment","product_or_repository_truth","kanban_dispatcher_execution","bot_token_or_secret_provisioning","operating_system_sandboxing","implementation_delivery","merge_release_deployment_or_product_acceptance_authorization"]'
---

# Hermes Agent Fleet Bootstrap

Design the smallest effective Hermes specialist fleet, then delegate each approved profile to `hermes-profile-bootstrap` for concrete creation or audit.

## Capability boundary

```text
hermes-agent-fleet-bootstrap
  owns fleet applicability, topology, specialist boundaries,
  shared contracts, conflict checks, migration planning,
  profile-bootstrap handoffs, fleet verification, and readiness.

hermes-profile-bootstrap
  owns one concrete Hermes profile skeleton, files,
  skill installation plan, safe defaults, and profile verification.

workflow-router
  owns exactly one primary workflow for an actual task.

role-switcher
  owns one task owner, narrow specialists, and reviewers at execution time.

Hermes Kanban / dispatcher
  owns durable work items, dependencies, worker execution, retry, and status.

product repositories
  own product truth, local policy, authorization, and acceptance.
```

This skill is a facade/composer. It performs real fleet-design and verification work, but it does not become a new engineering lifecycle or a second primary router.

## Default operating model

```text
user
→ one bot or front door
→ engineering-orchestrator profile
→ Hermes Kanban or verified durable coordination
→ headless specialist profiles as on-demand workers
→ independent reviewer
→ orchestrator synthesis
```

A profile is a durable agent identity and capability boundary. A bot or messaging gateway is optional. Only the orchestrator receives a bot by default.

## When to load references

- Load `references/topology-and-classification.md` when deciding whether multi-agent is justified, selecting topology, or classifying a requested concept.
- Load `references/profile-archetypes.md` when proposing specialist profiles or composing responsibility-specific skill manifests.
- Load `references/runtime-gateway-and-security.md` when defining gateways, Kanban/worker assumptions, permissions, sandbox evidence, or runtime limitations.
- Load assets only when producing machine-readable fleet, profile, collaboration, or handoff manifests.

## Required inputs

Resolve or mark `NOT_VERIFIED`:

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

Do not infer credentials, bot tokens, profile contents, product facts, filesystem isolation, runtime commands, or authorization.

## Execution procedure

Run phases in order. A later phase may not normalize an earlier blocker into `PASS`.

### Phase 1 — Verify intent and authority

1. Confirm the request concerns persistent Hermes profiles or an existing fleet.
2. Distinguish plan, audit, and create/update intent.
3. Verify target host, profile source, repository/product context, and write authority when mutation is requested.
4. Preserve missing runtime or profile evidence as `NOT_VERIFIED`.

Completion: intent, evidence posture, and mutation authority are explicit.

### Phase 2 — Normalize requested outcomes

Convert technology-shaped or lifecycle-shaped language into stable responsibilities and outputs.

Examples:

```text
React, Next.js, CSS, component tests
→ frontend implementation capability

SOLID, DDD, patterns, architecture
→ solution architecture and engineering-quality skills

PRD, MVP, product metrics
→ product-development responsibility

API, service, database, SDK
→ backend/platform responsibility unless SDK has an independent lifecycle
```

Completion: every requested concept has a stable capability description or an explicit unresolved status.

### Phase 3 — Decide whether multi-agent is justified

Use `references/topology-and-classification.md`.

Return:

```yaml
multi_agent_verdict:
  status: JUSTIFIED | NOT_JUSTIFIED | LIMITED | NOT_VERIFIED
  reasons: []
  expected_benefits: []
  coordination_costs: []
  simpler_alternative: ""
```

Prefer one profile plus skills when responsibilities are narrow, occasional, share the same permissions and context, and do not require independent review or durable ownership.

Completion: multi-agent is justified by recurring responsibility and evidence, not by the number of technologies named.

### Phase 4 — Classify every requested concept

Classify as exactly one primary form:

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

Rules:

- Stable recurring responsibility with durable outputs may become a profile.
- A method, framework, pattern, or tool normally remains a skill or product adapter.
- Ordered lifecycle remains a workflow.
- Temporary isolated analysis remains a delegated subagent.
- Product/app identity, repository facts, and accepted local policy remain product context.
- Independent verification responsibility may become a reviewer profile.

Completion: no requested concept is duplicated across primary classifications.

### Phase 5 — Select the simplest sufficient topology

Supported topology identities:

```text
single_profile
orchestrator_with_specialists
reviewer_loop
parallel_specialists
product_agents_with_shared_engineering_fleet
operations_isolated_fleet
```

The default for a durable engineering fleet is `orchestrator_with_specialists` with sparse communication.

Reject uncontrolled all-to-all messaging as the default. Parallel execution is allowed only for independent tasks with explicit artifact contracts and workspace ownership.

Completion: topology, orchestrator, communication modes, and coordination costs are explicit.

### Phase 6 — Define profile contracts

For every proposed profile, produce the shape in `assets/profile-contract.template.yaml`.

Each profile must declare:

```text
mission
owns
does_not_own
required inputs
required outputs
recurring tasks
required and optional skills
model policy
tool policy
permission policy
memory scope
gateway policy
collaboration modes
handoff targets
reviewers
completion evidence
```

Use `references/profile-archetypes.md` as candidate guidance, not as a mandatory fixed fleet.

Use responsibility-specific custom skill manifests. Do not install the broad `engineering` or `full` preset into every specialist unless that breadth is itself justified.

Completion: every durable artifact and decision has one accountable profile owner.

### Phase 7 — Validate boundaries and safety

Fail closed on:

- duplicate primary artifact ownership;
- missing owner for a required output;
- circular required handoffs;
- reviewer as sole implementer of the reviewed artifact;
- multiple default gateways without independent audience or operational justification;
- profile defined only by framework or method names;
- product-specific facts or secrets embedded in a reusable profile;
- live sessions, memories, cron state, runtime databases, logs, caches, tokens, or credentials in a distribution;
- assumed OS sandbox, network isolation, or filesystem restriction without evidence;
- privileged operations without separate permission policy and human authorization.

Reviewer independence must be reported as one of:

```text
VERIFIED
LIMITED_SHARED_MODEL
LIMITED_SHARED_CONTEXT
LIMITED_SHARED_TOOLS
NOT_VERIFIED
```

Completion: no unresolved blocking conflict is hidden.

### Phase 8 — Define collaboration and handoffs

Use only explicit interaction modes:

```text
orchestrator_invocation
durable_kanban_task
temporary_delegation
shared_artifact_handoff
review_feedback_loop
human_approval
```

Every artifact handoff records producer, consumer, version, evidence, assumptions, unresolved risks, and correction route. Use `assets/collaboration-manifest.template.yaml`.

Completion: required communication is sparse, directional, and auditable.

### Phase 9 — Compose profile bootstrap handoffs

For each approved persistent profile, create one `hermes-profile-bootstrap` handoff:

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

Do not copy the single-profile generation procedure into this skill. A fleet plan cannot claim that profiles were created.

Completion: every proposed profile has one explicit materialization or audit handoff.

### Phase 10 — Plan migration of existing profiles

Classify each existing profile:

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

MVP behavior is non-destructive. Preserve live memory, sessions, credentials, gateway state, and accepted product identity. A recommendation is not an executed migration.

Completion: current profiles have evidence-backed recommendations and no destructive action is implicit.

### Phase 11 — Dry-run, execute, or hand off

- `PLAN_ONLY`: produce intended profile, file, skill, policy, gateway, and migration actions without mutation.
- `AUDIT_ONLY`: compare current evidence against approved contracts without mutation.
- `CREATE_OR_UPDATE`: invoke supported runtime actions only when tool availability and authorization are verified; otherwise produce an exact handoff.

Completion: actual execution state is distinct from planned state.

### Phase 12 — Verify the fleet

Use `assets/fleet-manifest.template.yaml` and verify:

- selected topology and one orchestration owner;
- unique profile identifiers;
- one owner per durable artifact;
- responsibility-specific skill manifests;
- per-profile bootstrap handoffs;
- gateway policy;
- collaboration graph and cycle checks;
- reviewer independence status;
- safety exclusions and permission boundaries;
- runtime evidence versus assumptions;
- migration non-destructiveness;
- deterministic output inputs and catalog version.

Return:

```text
READY
READY_WITH_LIMITATIONS
NEEDS_WORK
BLOCKED
NOT_VERIFIED
```

`READY` means the planned or audited fleet contract passes applicable gates. It does not mean product work, profile runtime execution, merge, release, deployment, or product acceptance has occurred.

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
migration_plan
verification_report
fleet_readiness_verdict
execution_receipt
```

## Quality gates

- Multi-agent is explicitly justified or rejected.
- The simplest sufficient topology is selected.
- Exactly one default orchestration owner exists unless an exception is justified.
- Only the orchestrator receives a default bot/gateway.
- Each profile owns a stable recurring responsibility rather than a framework name.
- Each durable artifact and decision has one accountable owner.
- Specialist skill manifests are responsibility-specific.
- `hermes-profile-bootstrap` remains the per-profile executor.
- Collaboration is sparse and handoffs are structured.
- Reviewer independence is evidenced or limited honestly.
- Product facts and live runtime state remain outside reusable distributions.
- Profile isolation is not misrepresented as OS sandboxing.
- Planned, executed, reviewed, approved, delivered, and accepted states remain distinct.
- Missing runtime evidence remains `NOT_VERIFIED`.

## Hard stops

Return `BLOCKED`, `NOT_VERIFIED`, or `READY_WITH_LIMITATIONS` when:

- current profiles cannot be inspected but migration or overwrite is requested;
- duplicate ownership or required handoff cycles remain;
- required capability IDs cannot be resolved from verified catalogs;
- reviewer independence is required but cannot be established;
- runtime commands, Kanban, dispatcher, profile addressing, or gateway behavior are assumed rather than verified;
- secret-free distribution cannot be proven;
- write authorization or product/repository authority is missing;
- a privileged profile lacks bounded permissions and human authorization.

## Receipt

```yaml
fleet_bootstrap_receipt:
  request_mode: PLAN_ONLY | AUDIT_ONLY | CREATE_OR_UPDATE
  multi_agent_verdict: ""
  topology: ""
  profiles_proposed: []
  profiles_created_or_updated: []
  profiles_audited: []
  profile_bootstrap_handoffs: []
  gateways_planned_or_verified: []
  validations_executed: []
  findings: []
  readiness: READY | READY_WITH_LIMITATIONS | NEEDS_WORK | BLOCKED | NOT_VERIFIED
  runtime_execution: EXECUTED | PARTIAL | NOT_RUN | BLOCKED | NOT_VERIFIED
  review_independence: VERIFIED | LIMITED_SHARED_MODEL | LIMITED_SHARED_CONTEXT | LIMITED_SHARED_TOOLS | NOT_VERIFIED
  approval: VERIFIED | ROUTE_FOR_APPROVAL | NOT_VERIFIED
  merge_release_deploy_authorization: NOT_GRANTED | VERIFIED
  known_gaps: []
  next_action: ""
```
