---
name: hermes-agent-fleet-bootstrap
description: Design, bootstrap, audit, and verify the smallest justified fleet of persistent Hermes specialist profiles. Use when a Hermes engineering setup needs one orchestrator plus bounded specialists; when deciding whether capabilities should become profiles, skills, workflows, reviewers, delegated subagents, or product context; or when migrating existing app-based profiles into a shared specialist fleet. Do not use for ordinary single-profile creation, task-time workflow routing, product delivery itself, bot-token provisioning, destructive migration, or unsupported runtime claims.
license: MIT
metadata:
  ai-native-skills.version: 0.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.pattern: facade
  ai-native-skills.requires: "workflow-router role-switcher hermes-profile-bootstrap decision-provenance skill-eval"
  ai-native-skills.related_skills: '["hermes-profile-bootstrap","workflow-router","role-switcher","implementation-context-discovery","product-manager","master-engineer","architecture-review","security-review","skill-eval"]'
  ai-native-skills.boundary.covers: '["fleet_request_normalization","multi_agent_justification","topology_selection","profile_responsibility_contracts","profile_skill_manifest_composition","gateway_and_bot_policy","collaboration_and_artifact_handoff_contracts","ownership_and_cycle_validation","non_destructive_profile_migration_planning","per_profile_bootstrap_handoffs","fleet_readiness_and_receipt"]'
  ai-native-skills.boundary.delegates: '["single_profile_materialization","task_time_primary_workflow_selection","task_time_role_assignment","product_or_repository_truth","kanban_dispatcher_execution","bot_token_or_secret_provisioning","operating_system_sandboxing","implementation_delivery","merge_release_deployment_or_product_acceptance_authorization"]'
---

# Hermes Agent Fleet Bootstrap

Design the smallest effective Hermes specialist fleet, then delegate each approved profile to `hermes-profile-bootstrap` for concrete creation or audit.

## Boundary

```text
hermes-agent-fleet-bootstrap
  fleet applicability, topology, specialist contracts,
  shared handoffs, conflict checks, migration plan,
  profile-bootstrap handoffs, fleet verification, readiness

hermes-profile-bootstrap
  one concrete profile skeleton, skill installation plan,
  safe defaults, and profile verification

workflow-router
  exactly one primary workflow for an actual task

role-switcher
  one task owner, narrow specialists, and reviewers

Hermes runtime
  durable tasks, worker execution, retry, gateway, and state

product repositories
  product truth, policy, authorization, and acceptance
```

This is a facade/composer, not a new engineering lifecycle or second primary router.

## Default operating model

```text
user
→ one bot/front door
→ engineering-orchestrator profile
→ Hermes Kanban or verified durable coordination
→ headless specialist profiles as on-demand workers
→ independent reviewer
→ orchestrator synthesis
```

A profile is a durable agent identity. A bot is an optional communication surface. Only the orchestrator receives a bot by default.

## Load references

- Load `references/topology-and-classification.md` for multi-agent justification, capability classification, and topology selection.
- Load `references/profile-archetypes.md` for candidate specialist boundaries and responsibility-specific skill manifests.
- Load `references/runtime-gateway-and-security.md` for bots, workers, permissions, sandbox evidence, and runtime limitations.
- Load `assets/*.template.yaml` only when producing machine-readable manifests.

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

Resolve every field from evidence or mark it `NOT_VERIFIED`. Never infer credentials, profile state, runtime commands, filesystem isolation, product facts, or authorization.

## Procedure

Run phases in order. A later phase cannot normalize an earlier blocker into `PASS`.

### 1. Verify intent and authority

- Distinguish plan, audit, and create/update intent.
- Verify runtime host, profile source, product/repository references, and mutation authority.
- Preserve missing evidence as `NOT_VERIFIED`.

Gate: intent and evidence posture are explicit.

### 2. Normalize requested capabilities

Convert implementation names into stable responsibilities.

```text
React, Next.js, CSS, component tests
→ frontend implementation capability

SOLID, DDD, patterns
→ architecture and engineering-quality skills

PRD, MVP, metrics
→ product-development responsibility

API, service, database, SDK
→ backend/platform responsibility unless SDK has an independent lifecycle
```

Gate: each concept has a stable capability description or explicit unknown status.

### 3. Decide whether multi-agent is justified

Use `references/topology-and-classification.md` and return:

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

### 4. Classify each concept

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

Stable recurring responsibility may become a profile. Methods and frameworks remain skills or product adapters. Ordered lifecycles remain workflows. Temporary analysis remains delegation. Product identity and accepted local facts remain product context.

Gate: no concept has duplicate primary classifications.

### 5. Select topology

Supported identities:

```text
single_profile
orchestrator_with_specialists
reviewer_loop
parallel_specialists
product_agents_with_shared_engineering_fleet
operations_isolated_fleet
```

Use the simplest sufficient topology. Reject uncontrolled all-to-all messaging. Parallel work requires independent tasks, workspace ownership, artifact contracts, and an integration owner.

Gate: orchestrator, interaction modes, and coordination costs are explicit.

### 6. Define profile contracts

Use `assets/profile-contract.template.yaml` and `references/profile-archetypes.md`.

Every profile declares mission, owned and non-owned artifacts/decisions, inputs, outputs, recurring work, skill manifest, model/tools/permissions, memory, gateway, handoffs, reviewers, and completion evidence.

Use responsibility-specific `custom` skill manifests. Do not clone broad `engineering` or `full` presets into every worker.

Gate: every durable artifact and decision has one accountable owner.

### 7. Validate boundaries and safety

Fail closed on:

- duplicate or missing artifact owners;
- circular required handoffs;
- reviewer as sole implementer;
- default bot per specialist without independent audience;
- profiles defined only by frameworks or methods;
- product facts, secrets, or live state in reusable distributions;
- assumed OS, filesystem, network, or credential isolation;
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

### 8. Define collaboration

Use `assets/collaboration-manifest.template.yaml` and only explicit modes:

```text
orchestrator_invocation
durable_kanban_task
temporary_delegation
shared_artifact_handoff
review_feedback_loop
human_approval
```

Every handoff records producer, consumer, artifact version, evidence, assumptions, risks, and correction route.

Gate: communication is sparse, directional, and auditable.

### 9. Compose one profile-bootstrap handoff per profile

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

Gate: every persistent profile has one materialization or audit handoff.

### 10. Plan migration

Classify existing profiles:

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

MVP migration is non-destructive. Preserve live memory, sessions, credentials, gateway state, and accepted product identity.

Gate: recommendations are evidence-backed and distinct from executed mutations.

### 11. Plan, audit, or execute

- `PLAN_ONLY`: list intended profiles, files, skills, policies, gateways, and migration actions without mutation.
- `AUDIT_ONLY`: compare observed profiles against approved contracts without mutation.
- `CREATE_OR_UPDATE`: execute only with verified runtime tools and authority; otherwise emit an exact handoff.

Gate: planned and executed states remain separate.

### 12. Verify fleet readiness

Use `assets/fleet-manifest.template.yaml` and verify topology, unique identifiers, artifact ownership, custom skill manifests, profile-bootstrap handoffs, gateway policy, collaboration cycles, reviewer independence, safety exclusions, permissions, runtime assumptions, migration safety, and deterministic inputs.

Verdicts:

```text
READY
READY_WITH_LIMITATIONS
NEEDS_WORK
BLOCKED
NOT_VERIFIED
```

`READY` covers the fleet contract only. It does not prove product work, runtime execution, merge, release, deployment, or product acceptance.

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
- The smallest sufficient topology is selected.
- One default orchestration owner exists unless an exception is justified.
- Only the orchestrator receives a default bot.
- Profiles own stable responsibilities, not framework names.
- Every durable artifact has one owner.
- Skill manifests are responsibility-specific.
- `hermes-profile-bootstrap` remains the per-profile executor.
- Collaboration is sparse and handoffs are structured.
- Review independence is evidenced or limited honestly.
- Product facts and live state remain outside distributions.
- Profile isolation is not represented as OS sandboxing.
- Plan, execution, review, approval, delivery, and acceptance remain distinct.

## Hard stops

Return `BLOCKED`, `NOT_VERIFIED`, or `READY_WITH_LIMITATIONS` when current profiles cannot be inspected for requested migration; duplicate ownership or cycles remain; required skills cannot be resolved; reviewer independence is required but unavailable; runtime behavior is assumed; secret-free output cannot be proven; authority is missing; or a privileged profile lacks bounded permissions and human approval.

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
