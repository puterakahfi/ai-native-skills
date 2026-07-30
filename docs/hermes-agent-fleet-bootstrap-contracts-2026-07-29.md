# Hermes Specialist Agent Fleet Bootstrap — Contract Shapes

Issue: `puterakahfi/ai-native-skills#261`  
Parent epic: `puterakahfi/ai-native-skills#260`  
Date: 2026-07-29  
Status: `PROPOSED_FOR_OWNER_REVIEW`

## 1. Purpose

This document defines the normalized, reviewable data shapes required by `hermes-agent-fleet-bootstrap`.

These are adapter-local MVP contracts for `ai-native-skills`. They are not promoted Native AI Core contracts and do not claim runtime execution, profile creation, review, approval, authorization, or product acceptance.

Downstream implementation may encode these shapes as YAML templates, JSON Schema, typed models, or deterministic validators, but must preserve the semantics and evidence boundaries defined here.

## 2. Contract family

```text
normalized_fleet_request
→ existing_profile_inventory
→ multi_agent_verdict
→ capability_classification_report
→ fleet_manifest
→ profile_contracts
→ collaboration_manifest
→ artifact_handoffs
→ profile_bootstrap_handoffs
→ migration_plan
→ verification_report
→ fleet_readiness
→ execution_receipt
```

## 3. Shared conventions

### 3.1 Evidence states

```text
VERIFIED
LIMITED
NOT_VERIFIED
NOT_APPLICABLE
```

### 3.2 Execution and authority states

Do not collapse these record families:

```text
PLANNED
EXECUTED
VERIFIED
REVIEWED
OWNER_APPROVED
AUTHORIZED
DELIVERED
PRODUCT_ACCEPTED
VALIDATED_IN_USE
```

A field may use one of these only when it represents the matching record family and direct evidence exists.

### 3.3 Readiness states

```text
READY
READY_WITH_LIMITATIONS
NEEDS_WORK
BLOCKED
NOT_VERIFIED
```

### 3.4 Identifier rules

- profile IDs are lowercase kebab-case;
- fleet IDs are lowercase kebab-case;
- every durable artifact or decision has one stable ID;
- capability IDs must resolve to the verified capability catalog or be marked unavailable;
- evidence references must be attributable paths, issue/PR refs, commit SHAs, runtime command outputs, or equivalent durable references;
- names do not establish ownership, execution, expertise, or reviewer independence.

## 4. Normalized fleet request

```yaml
normalized_fleet_request:
  request_id: string
  requested_by: string | NOT_VERIFIED
  requested_at: timestamp | NOT_VERIFIED

  runtime:
    target: hermes
    host_ref: string | NOT_VERIFIED
    version: string | NOT_VERIFIED
    profile_root: string | NOT_VERIFIED
    gateway_available: VERIFIED | LIMITED | NOT_VERIFIED
    kanban_available: VERIFIED | LIMITED | NOT_VERIFIED
    dispatcher_available: VERIFIED | LIMITED | NOT_VERIFIED

  desired_outcomes:
    - id: string
      description: string
      recurring: VERIFIED | LIMITED | NOT_VERIFIED
      expected_artifacts: []
      risk_level: low | medium | high | NOT_VERIFIED

  products_or_repositories:
    - id: string
      repository_ref: string | NOT_VERIFIED
      product_context_ref: string | NOT_VERIFIED
      source_of_truth_refs: []
      acceptance_authority: string | NOT_VERIFIED

  requested_responsibilities: []
  named_technologies_or_methods: []

  boundaries:
    permission_boundaries: []
    credential_boundaries: []
    tenant_boundaries: []
    data_boundaries: []
    environment_boundaries: []

  collaboration_expectations:
    front_door: bot | cli | desktop | api | none | NOT_VERIFIED
    durable_coordination: required | optional | unavailable | NOT_VERIFIED
    parallelism: required | optional | not_required | NOT_VERIFIED
    human_approval_points: []

  constraints: []
  assumptions: []
  unknowns: []
  evidence_refs: []
```

### Required gates

- at least one desired outcome exists;
- runtime target is Hermes for MVP;
- product facts and reusable profile requirements remain separable;
- unverified runtime capabilities remain explicit;
- named technologies do not automatically become requested responsibilities.

## 5. Existing profile inventory

```yaml
existing_profile_inventory:
  runtime_ref: string | NOT_VERIFIED
  inspected_at: timestamp | NOT_VERIFIED
  inspection_method: []

  profiles:
    - id: string
      path_ref: string | NOT_VERIFIED
      description: string | NOT_VERIFIED
      soul_ref: string | NOT_VERIFIED
      config_ref: string | NOT_VERIFIED
      skills_lock_ref: string | NOT_VERIFIED

      responsibility:
        mission: string | NOT_VERIFIED
        owns: []
        does_not_own: []

      runtime_state:
        live_profile_exists: VERIFIED | LIMITED | NOT_VERIFIED
        installed_skills: []
        model_policy: object | NOT_VERIFIED
        tool_policy: object | NOT_VERIFIED
        permission_policy: object | NOT_VERIFIED
        memory_scope: string | NOT_VERIFIED
        gateway_policy: none | orchestrator_only | dedicated | NOT_VERIFIED
        cron_responsibilities: []

      product_coupling:
        product_ids: []
        product_facts_in_identity: VERIFIED | LIMITED | NOT_VERIFIED
        reusable_distribution_safe: VERIFIED | LIMITED | NOT_VERIFIED

      evidence_refs: []
      findings: []

  inventory_status: VERIFIED | LIMITED | NOT_VERIFIED
  limitations: []
```

Inventory must never copy live sessions, memory contents, credentials, secret values, state databases, or logs into reusable artifacts.

## 6. Multi-agent verdict

```yaml
multi_agent_verdict:
  status: JUSTIFIED | NOT_JUSTIFIED | LIMITED | NOT_VERIFIED

  outcome_complexity:
    independent_responsibilities: []
    parallelizable_units: []
    independent_review_needed: VERIFIED | LIMITED | NOT_VERIFIED

  persistence_evidence:
    recurring_responsibilities: []
    durable_memory_needs: []
    distinct_skill_compositions: []
    distinct_model_policies: []
    distinct_tool_or_credential_scopes: []
    distinct_permission_boundaries: []
    durable_task_ownership: []

  expected_benefits: []
  coordination_costs: []
  simpler_alternatives: []
  decision_rationale: string
  evidence_refs: []
  findings: []
```

### Decision rules

`JUSTIFIED` requires evidence that one profile plus selected skills/delegation would materially weaken recurring responsibility, isolation, parallel work, or independent verification.

`NOT_JUSTIFIED` must include a simpler recommendation such as:

```text
one profile + selected skills
one profile + temporary delegation
one implementer + independent reviewer
```

## 7. Capability classification report

```yaml
capability_classification_report:
  classifications:
    - concept: string
      verdict: PROFILE | SKILL | WORKFLOW | OVERLAY | REVIEWER | DELEGATED_SUBAGENT | PRODUCT_CONTEXT | NOT_JUSTIFIED
      rationale: string
      responsibility_owner: string | null
      capability_refs: []
      recurring_value: VERIFIED | LIMITED | NOT_VERIFIED
      persistence_need: VERIFIED | LIMITED | NOT_VERIFIED
      permission_boundary: VERIFIED | LIMITED | NOT_VERIFIED | NOT_APPLICABLE
      evidence_refs: []

  unresolved_concepts: []
  findings: []
```

### Classification examples

```yaml
- concept: React
  verdict: SKILL
  rationale: Implementation method inside frontend engineering, not a stable organizational responsibility.

- concept: solution architecture
  verdict: PROFILE
  rationale: Stable recurring responsibility with distinct artifacts, decisions, and independent conformance review.

- concept: temporary market research
  verdict: DELEGATED_SUBAGENT
  rationale: Bounded task with no durable identity or memory requirement.

- concept: VisualMate
  verdict: PRODUCT_CONTEXT
  rationale: Product source of truth and acceptance boundary, not a reusable engineering specialist identity by default.
```

## 8. Fleet manifest

```yaml
fleet_manifest:
  schema_version: 0.1.0
  fleet_id: string
  fleet_name: string
  runtime: hermes
  manifest_version: string
  catalog_version: string | NOT_VERIFIED

  topology:
    pattern: single_profile | orchestrator_with_specialists | reviewer_loop | parallel_specialists | product_agents_with_shared_engineering_fleet | operations_isolated_fleet
    orchestrator_profile: string | null
    topology_rationale: string
    topology_evidence_refs: []

  front_door:
    mode: bot | cli | desktop | api | none
    profile_id: string | null
    gateway_policy: none | orchestrator_only | dedicated
    dedicated_exceptions: []

  profiles:
    - profile_contract_ref: string
      required: boolean
      lifecycle: persistent | conditional | migration_only

  coordination:
    manifest_ref: string
    durable_task_system: hermes_kanban | runtime_adapter | none | NOT_VERIFIED
    worker_mode: kanban_on_demand | direct_invocation | delegation_only | NOT_VERIFIED

  product_bindings:
    - product_id: string
      product_context_ref: string
      profile_access: []
      acceptance_authority: string | NOT_VERIFIED

  policies:
    smallest_effective_fleet: true
    one_orchestration_owner: true
    one_accountable_owner_per_artifact: true
    reviewer_independence_required: true
    product_context_in_reusable_profile: forbidden
    live_state_in_distribution: forbidden
    destructive_migration: explicit_authorization_required
    unbounded_all_to_all_communication: forbidden_by_default

  readiness_ref: string
  findings: []
  evidence_refs: []
```

## 9. Profile contract

```yaml
profile_contract:
  schema_version: 0.1.0
  profile_id: string
  display_name: string
  archetype: string
  runtime: hermes

  mission: string
  responsibility:
    owns: []
    does_not_own: []
    recurring_tasks: []
    accountable_artifacts: []
    supported_decisions: []
    prohibited_decisions: []

  inputs:
    required: []
    optional: []
    product_context_refs: []

  outputs:
    required: []
    optional: []
    completion_evidence: []

  capability_manifest:
    catalog_source: string
    job_profile_refs: []
    required_skills: []
    optional_skills: []
    required_workflows: []
    required_meta_skills: []
    unavailable_capabilities: []

  runtime_policy:
    model_policy: object | NOT_VERIFIED
    tool_policy: object | NOT_VERIFIED
    permission_policy:
      filesystem_scope: string | NOT_VERIFIED
      repository_scope: []
      network_scope: string | NOT_VERIFIED
      credential_scope: string | NOT_VERIFIED
      mutation_authority: read_only | bounded_write | privileged | NOT_VERIFIED
      sandbox_evidence: []
    memory_scope: string | NOT_VERIFIED
    session_scope: string | NOT_VERIFIED
    cron_scope: []
    gateway_policy: none | orchestrator_only | dedicated

  collaboration:
    accepts_tasks_from: []
    handoff_targets: []
    artifact_contract_refs: []
    escalation_targets: []
    retry_policy: string | NOT_VERIFIED

  review:
    required_reviewers: []
    self_review_allowed: true
    self_review_sufficient_for_acceptance: false
    independence_requirement: VERIFIED | LIMITED | NOT_VERIFIED

  bootstrap:
    materializer: hermes-profile-bootstrap
    preset: minimal | engineering | product | runtime-ops | full | custom
    skills_lock_plan_ref: string
    safety_constraints: []
    verification_policy: object

  status: PROPOSED | APPROVED_FOR_BOOTSTRAP | CREATED | AUDITED | NEEDS_WORK | BLOCKED | NOT_VERIFIED
  findings: []
  evidence_refs: []
```

## 10. Default profile archetype templates

### 10.1 Engineering orchestrator

```yaml
profile_archetype:
  id: engineering-orchestrator
  owns:
    - request normalization
    - governing-workflow handoff
    - work decomposition and dependencies
    - specialist task routing
    - evidence aggregation
    - final synthesis
  does_not_own:
    - product requirements content
    - architecture decisions
    - primary implementation
    - independent review
    - product acceptance
    - merge, release, or deployment authorization
  gateway_policy: orchestrator_only
  mutation_authority: read_only_or_coordination_only
```

### 10.2 Product development

```yaml
profile_archetype:
  id: product-development
  owns:
    - product discovery and problem framing
    - Product Brief and PRD composition
    - MVP scope and success metrics
    - product acceptance criteria
    - product-validation handoff
  does_not_own:
    - technical architecture
    - production implementation
    - deployment execution
```

### 10.3 Solution architecture

```yaml
profile_archetype:
  id: solution-architecture
  owns:
    - system and domain boundaries
    - technical specification
    - API, data, integration, and infrastructure direction
    - non-functional requirements and trade-offs
    - architecture decisions
  does_not_own:
    - product priority
    - visual design
    - sole implementation acceptance
```

### 10.4 Product design

```yaml
profile_archetype:
  id: product-design
  owns:
    - information architecture
    - user flows and interaction behavior
    - visual and design-system direction
    - design acceptance criteria
  does_not_own:
    - frontend implementation ownership
    - backend domain decisions
    - release authorization
```

### 10.5 Frontend engineering

```yaml
profile_archetype:
  id: frontend-engineering
  owns:
    - frontend architecture and implementation
    - responsive and accessible implementation
    - browser performance
    - frontend test evidence
  does_not_own:
    - product strategy
    - backend domain authority
    - independent design approval of its own output
```

### 10.6 Backend platform

```yaml
profile_archetype:
  id: backend-platform
  owns:
    - domain and application services
    - APIs, persistence, events, jobs, and integrations
    - backend tests and observability instrumentation
  does_not_own:
    - product scope
    - UI behavior
    - independent architecture approval
    - deployment authorization
```

### 10.7 Quality review

```yaml
profile_archetype:
  id: quality-review
  owns:
    - acceptance verification
    - test and code evidence review
    - architecture conformance
    - regression analysis
    - readiness verdict
  does_not_own:
    - primary implementation
    - product scope changes
    - merge or release authorization
  gateway_policy: none
```

## 11. Collaboration manifest

```yaml
collaboration_manifest:
  schema_version: 0.1.0
  fleet_id: string

  communication_policy:
    default_topology: sparse_orchestrated
    unbounded_all_to_all_allowed: false
    direct_profile_to_profile_allowed_when: []
    human_approval_points: []

  interaction_modes:
    - id: string
      mode: orchestrator_invocation | durable_kanban_task | temporary_delegation | shared_artifact_handoff | review_feedback_loop | human_approval
      producer: string
      consumer: string
      artifact_contract_refs: []
      preconditions: []
      completion_conditions: []
      failure_route: string

  dependency_graph:
    nodes: []
    edges:
      - from: string
        to: string
        reason: string
        required: boolean
    cycles: []

  findings: []
  evidence_refs: []
```

### Required gates

- no required dependency cycle;
- no all-to-all default;
- every required edge has a reason and artifact/task contract;
- orchestrator does not become the hidden producer of specialist artifacts;
- human approval is explicit for privileged or irreversible operations.

## 12. Artifact handoff

```yaml
artifact_handoff:
  handoff_id: string
  task_ref: string
  artifact_id: string
  artifact_type: string

  producer:
    profile_id: string
    responsibility_ref: string
  consumer:
    profile_id: string
    expected_use: string

  artifact:
    location_ref: string | NOT_VERIFIED
    version_or_sha: string | NOT_VERIFIED
    status: DRAFT | READY_FOR_REVIEW | REVIEWED | NEEDS_WORK | BLOCKED | SUPERSEDED
    structure_ref: string | NOT_VERIFIED

  evidence:
    produced_by_run: string | NOT_VERIFIED
    verification_commands: []
    verification_results: []
    evidence_refs: []

  decisions:
    accepted_decisions: []
    assumptions: []
    unknowns: []
    unresolved_risks: []

  correction:
    retry_owner: string | NOT_VERIFIED
    return_conditions: []
    next_action: string
```

## 13. Profile bootstrap handoff

```yaml
profile_bootstrap_handoff:
  fleet_id: string
  profile_contract_ref: string

  runtime_target: hermes
  profile_name: string
  preset: minimal | engineering | product | runtime-ops | full | custom
  skill_catalog_source: string
  safety_constraints: []

  profile_distribution_source: string | null
  core_contract_source: string | null
  runtime_binding_context: string | NOT_VERIFIED
  product_context_reference: string | null

  skills_lock_plan_ref: string
  model_policy: object | NOT_VERIFIED
  toolset_policy: object | NOT_VERIFIED
  verification_policy: object

  dry_run: boolean
  overwrite_policy: refuse | explicit_force_required
  expected_outputs:
    - profile_skeleton_spec
    - skill_preset_manifest
    - profile_distribution_manifest
    - runtime_adapter_requirements
    - install_plan
    - verification_plan
    - safety_exclusion_policy
    - generation_handoff
```

The fleet skill may plan or invoke this handoff. It may not claim profile creation unless `hermes-profile-bootstrap` or the verified runtime action actually completed.

## 14. Migration plan

```yaml
migration_plan:
  schema_version: 0.1.0
  fleet_id: string
  inventory_ref: string

  profile_actions:
    - existing_profile_id: string
      classification: KEEP | KEEP_AS_PRODUCT_AGENT | CONVERT_TO_SPECIALIST | MERGE | SPLIT | REGENERATE | DEPRECATE | NOT_VERIFIED
      target_profile_ids: []
      rationale: string
      evidence_refs: []
      live_state_impact: none | manual_migration_required | destructive | NOT_VERIFIED
      credential_impact: none | manual_reconfiguration_required | NOT_VERIFIED
      product_impact: none | limited | material | NOT_VERIFIED
      required_authority: string | NOT_VERIFIED
      automatic_execution_allowed: false

  preserved_profiles: []
  proposed_profiles: []
  conflicts: []
  manual_actions: []
  findings: []
```

MVP never performs destructive migration automatically.

## 15. Verification report

```yaml
verification_report:
  schema_version: 0.1.0
  fleet_id: string
  manifest_ref: string
  verified_at: timestamp | NOT_VERIFIED
  runtime_ref: string | NOT_VERIFIED

  dimensions:
    multi_agent_justification: PASS | FAIL | LIMITED | NOT_VERIFIED | NOT_APPLICABLE
    topology_sufficiency: PASS | FAIL | LIMITED | NOT_VERIFIED
    profile_responsibility_uniqueness: PASS | FAIL | LIMITED | NOT_VERIFIED
    artifact_ownership: PASS | FAIL | LIMITED | NOT_VERIFIED
    capability_resolution: PASS | FAIL | LIMITED | NOT_VERIFIED
    profile_bootstrap_handoffs: PASS | FAIL | LIMITED | NOT_VERIFIED
    gateway_allocation: PASS | FAIL | LIMITED | NOT_VERIFIED
    collaboration_graph: PASS | FAIL | LIMITED | NOT_VERIFIED
    reviewer_independence: PASS | FAIL | LIMITED | NOT_VERIFIED
    permission_boundaries: PASS | FAIL | LIMITED | NOT_VERIFIED
    product_context_separation: PASS | FAIL | LIMITED | NOT_VERIFIED
    safety_exclusions: PASS | FAIL | LIMITED | NOT_VERIFIED
    dry_run_completeness: PASS | FAIL | LIMITED | NOT_VERIFIED
    idempotency: PASS | FAIL | LIMITED | NOT_VERIFIED
    real_runtime_execution: PASS | FAIL | LIMITED | NOT_VERIFIED | NOT_APPLICABLE

  checks:
    - id: string
      result: PASS | FAIL | LIMITED | NOT_VERIFIED | NOT_APPLICABLE
      expected: string
      observed: string | NOT_VERIFIED
      evidence_refs: []
      findings: []

  blocking_findings: []
  warnings: []
  limitations: []
  manual_actions: []
```

## 16. Fleet readiness

```yaml
fleet_readiness:
  fleet_id: string
  verdict: READY | READY_WITH_LIMITATIONS | NEEDS_WORK | BLOCKED | NOT_VERIFIED

  blocking_findings: []
  limitations: []
  accepted_risks: []
  unresolved_risks: []

  profile_statuses:
    - profile_id: string
      status: PROPOSED | APPROVED_FOR_BOOTSTRAP | CREATED | AUDITED | NEEDS_WORK | BLOCKED | NOT_VERIFIED

  review:
    architecture: PASS | PASS_WITH_FLAGS | REQUEST_CHANGES | BLOCKED | NOT_VERIFIED
    security: PASS | PASS_WITH_FLAGS | REQUEST_CHANGES | BLOCKED | NOT_VERIFIED
    skill_qa: PASS | PASS_WITH_FLAGS | REQUEST_CHANGES | BLOCKED | NOT_VERIFIED
    product_acceptance: PASS | FAIL | LIMITED | NOT_VERIFIED | NOT_APPLICABLE

  authority:
    owner_approval: VERIFIED | ROUTE_FOR_APPROVAL | NOT_VERIFIED
    merge_authorization: GRANTED | NOT_GRANTED | NOT_VERIFIED
    release_authorization: GRANTED | NOT_GRANTED | NOT_APPLICABLE | NOT_VERIFIED
```

### Verdict rules

`READY` requires all release-blocking dimensions to pass with direct evidence and no unresolved blocking finding.

`READY_WITH_LIMITATIONS` is allowed only when limitations do not invalidate the intended use and are explicitly owned.

`NOT_VERIFIED` is required when evidence needed for a readiness claim is unavailable.

## 17. Execution receipt

```yaml
execution_receipt:
  capability: hermes-agent-fleet-bootstrap
  capability_version: string | NOT_VERIFIED
  request_id: string
  fleet_id: string

  mode: PLAN_ONLY | AUDIT | BOOTSTRAP | MIGRATION_PLAN | VERIFY

  outputs:
    normalized_request_ref: string
    multi_agent_verdict_ref: string
    classification_report_ref: string
    fleet_manifest_ref: string | null
    profile_contract_refs: []
    collaboration_manifest_ref: string | null
    bootstrap_handoff_refs: []
    migration_plan_ref: string | null
    verification_report_ref: string | null
    readiness_ref: string

  execution:
    profiles_proposed: []
    profiles_created: []
    profiles_audited: []
    profiles_not_verified: []
    gateways_proposed: []
    gateways_configured: []
    skills_planned: []
    skills_verified_installed: []
    runtime_commands_executed: []
    validators_executed: []

  findings: []
  limitations: []
  manual_actions: []
  evidence_refs: []

  authority:
    owner_approval: VERIFIED | ROUTE_FOR_APPROVAL | NOT_VERIFIED
    destructive_action_authorization: GRANTED | NOT_GRANTED | NOT_APPLICABLE | NOT_VERIFIED
    merge_or_release_authorization: GRANTED | NOT_GRANTED | NOT_APPLICABLE | NOT_VERIFIED
```

## 18. Typed findings

```yaml
typed_finding:
  id: string
  type: string
  severity: info | warning | error | blocker
  subject_ref: string
  message: string
  expected: string
  observed: string | NOT_VERIFIED
  remediation: string
  evidence_refs: []
```

Canonical MVP finding types:

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

## 19. Validation invariants

A conformant implementation must fail closed when any release-blocking invariant fails:

1. Exactly one orchestration owner exists for a durable specialist fleet.
2. Every profile declares `owns` and `does_not_own`.
3. Every durable artifact or decision has one accountable owner.
4. Required handoff dependencies are cycle-free.
5. Required reviewer coverage exists and independence is stated.
6. Technology names do not become profiles without stable responsibility evidence.
7. Specialist bots are not allocated by default.
8. Capability references resolve against the pinned catalog or remain blocked.
9. `hermes-profile-bootstrap` remains the per-profile materializer.
10. Product facts and secrets do not enter reusable distributions.
11. Live memory, sessions, state databases, logs, cron state, and credentials are excluded.
12. Dry-run distinguishes planned actions from executed actions.
13. Repeated identical inputs and catalog version do not create duplicate profiles or uncontrolled drift.
14. Profile separation does not claim OS sandboxing without evidence.
15. Review, approval, authorization, delivery, product acceptance, and real-world validation remain separate.

## 20. Downstream implementation mapping

| Contract | Proposed authored asset |
|---|---|
| Normalized fleet request | `assets/normalized-fleet-request.template.yaml` |
| Profile contract | `assets/profile-contract.template.yaml` |
| Fleet manifest | `assets/fleet-manifest.template.yaml` |
| Collaboration manifest | `assets/collaboration-manifest.template.yaml` |
| Artifact handoff | `assets/artifact-handoff.template.yaml` |
| Profile bootstrap handoff | `assets/profile-bootstrap-handoff.template.yaml` |
| Migration plan | `assets/migration-plan.template.yaml` |
| Verification report | `assets/verification-report.template.yaml` |
| Execution receipt | `assets/execution-receipt.template.yaml` |
| Behavioral requirements | `contracts/tests/hermes-agent-fleet-bootstrap.test.yaml` |

The parent `SKILL.md` must identify when each reference or asset is loaded. Templates must not become an always-loaded context dump.
