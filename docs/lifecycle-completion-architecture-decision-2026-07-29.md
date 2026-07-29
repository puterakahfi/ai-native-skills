# AI-Native Engineering Lifecycle Completion — Architecture and Authority Decision

Issue: `puterakahfi/ai-native-skills#247`  
Parent epic: `puterakahfi/ai-native-skills#246`  
Date: 2026-07-29  
Status: `PROPOSED_FOR_OWNER_APPROVAL`

## 1. Decision summary

```yaml
decision:
  product_lifecycle_owner: product-development-workflow
  canonical_product_phases: 12
  operate_and_maintain_model: recurring_cross_workflow_loop
  documentation_assurance:
    capability_id: documentation-assurance
    package_type: skill
    pattern: facade
    lifecycle_role: overlay_and_gate
  maintenance_case:
    capability_id: maintenance-case
    package_type: skill
    pattern: facade
    lifecycle_role: operational_case_overlay
  primary_routing_owner: workflow-router
  role_composition_owner: role-switcher
  runtime_execution_owner: puterakahfi/ai-native-os
  product_policy_owner: product_repositories
  core_rfc_verdict: NO_CORE_CHANGE_FOR_MVP
  review_status: LIMITED_INDEPENDENCE_OWNER_REVIEW_REQUIRED
```

The approved implementation must not create a thirteenth linear product-development phase, a second end-to-end engineering workflow, or a competing maintenance router.

The model is:

```text
product-development-workflow
  remains the product-from-zero lifecycle owner

operate and maintain
  is a recurring composition entered from operational or product signals
  and routed into exactly one existing governing workflow or standalone capability

documentation-assurance
  is a cross-cutting facade skill and completion gate

maintenance-case
  is a cross-cutting facade skill for signal qualification,
  case evidence, bounded closure, and follow-up

workflow-router
  remains the sole primary-route selector

runtime
  stores and enforces execution state and evidence,
  but does not synthesize review, approval, authorization, delivery, or acceptance
```

## 2. Execution context

```yaml
work_item: puterakahfi/ai-native-skills#247
primary_workflow: spec-workflow
owner: product-manager
specialists:
  - native-ai-engineer
  - master-engineer
  - decision-provenance
reviewer:
  - architecture-review
repository: puterakahfi/ai-native-skills
integration_branch: 246-lifecycle-completion
working_branch: 247-lifecycle-semantics-decision
pr_target: 246-lifecycle-completion
source_main_revision: 5cd82bb18bd20a286a1ce4a8224c8dc76e4dd7b6
```

This workstream is an independently reviewable architecture-decision slice. It does not authorize implementation in child issues, merge to the integration branch, final merge to `main`, release, deployment, or product acceptance.

## 3. Evidence inspected

| Repository | Evidence | Effective identity | Finding |
|---|---|---:|---|
| `ai-native-core` | `contracts/workflows/product-development.contract.yaml` | `product-development@0.4.0`, blob `5b63ad08...` | Core already owns a twelve-phase product lifecycle ending in Product Validation and Learning. |
| `ai-native-core` | `contracts/skills/meta/workflow-router.contract.yaml` | `workflow-router@0.2.1`, blob `1133b233...` | Router owns intent classification and exactly one primary route. |
| `ai-native-core` | `contracts/skills/meta/role-switcher.contract.yaml` | `role-switcher@0.1.0`, blob `45b9df48...` | Role composition is separate from lifecycle routing. |
| `ai-native-core` | `contracts/skills/runtime/incident-response.contract.yaml` | `incident-response@0.1.0`, blob `3500ab1b...` | Active incidents already have a focused lifecycle and product-defined severity/on-call policy. |
| `ai-native-skills` | `skills/product-development-workflow/SKILL.md` | `3.1.0`, blob `e9c8c0ad...` | Adapter preserves one product lifecycle owner and distinguishes deploy, launch, and product validation. |
| `ai-native-skills` | `skills/bugfix-workflow/SKILL.md` | `1.2.0`, blob `4d0bfc56...` | Verified non-active defects already have a six-phase governing workflow. |
| `ai-native-skills` | `skills/incident-response/SKILL.md` | `1.0.1`, blob `8ba564df...` | Active incident handling is an atomic executable capability, not a general maintenance router. |
| `ai-native-skills` | `skills/task-continuity/SKILL.md` | `1.0.0`, blob `29860331...` | Continuity owns checkpoint/resume/handoff and explicitly does not execute the governing workflow. |
| `ai-native-skills` | `skills/observability-design/SKILL.md` | `1.0.1`, blob `f55282af...` | Observability owns instrumentation and signals, not maintenance routing or case closure. |
| `ai-native-skills` | `skills/technical-debt-governance/SKILL.md` | `1.0.1`, blob `fb639211...` | Technical debt is one maintenance signal class with its own bounded governance. |
| `ai-native-skills` | `docs/skills.md` | blob `2e5b8b48...` | A skill owns one coherent capability; a workflow owns a lifecycle; a meta-skill routes. |
| `ai-native-skills` | `docs/facade-skill-pattern.md` | blob `e2474bb8...` | A facade may own applicability, shared evidence, normalized verdicts, and specialist delegation without lifecycle ownership. |
| `ai-native-skills` | `catalog/capability-orchestration/manifest.yaml` | `0.1.0 experimental`, blob `4d2c8db6...` | Current orchestration coverage is limited and currently models `REVIEWED` as a capability state. |
| `ai-native-os` | `compose-capability-execution-graph.ts` | blob `7f649470...` | Runtime graph preview is fail-closed and read-only; every selected node is currently only `selected`. |
| `ai-native-os` | merged PR `#94` | merge `e2a02bac...` | Runtime preview deliberately does not execute skills or claim review. |
| `ai-native-os` | draft PR `#92` | head `57868c18...` | Active operating-state work separates plan, execution, claim, evidence, gate, review, approval, delivery, and product acceptance. |

Duplicate searches found no separate open Core RFC or competing implementation outside epic issues `#246`–`#251`.

## 4. Governing constraints

1. `product-development-workflow` must remain the single product-from-zero lifecycle owner.
2. `workflow-router` must remain the sole primary-route selector.
3. A platform, quality, continuity, documentation, or maintenance capability may overlay a primary workflow but must not replace it.
4. Active incident, non-active defect, approved improvement, design correction, deployment, and product validation must remain distinct routes.
5. Core owns universal meaning; Skills owns executable capability composition; Runtime owns concrete state and persistence; product repositories own local policy and acceptance.
6. A new Core contract requires evidence that semantics are stable, universal, and cross-adapter—not merely useful in one epic.
7. Planning, execution, evidence, review, gate result, authority, delivery, and product acceptance must not collapse into one status.

## 5. Decision D-1 — Preserve the twelve-phase product lifecycle

### Decision

`product-development-workflow` remains a twelve-phase lifecycle. No `operate_maintain` phase is added in this epic.

```text
Discovery and Product Brief
→ Requirements / PRD
→ MVP Definition
→ Product Experience Design
→ Solution Design
→ Delivery Planning
→ Implementation
→ Product Acceptance
→ Release
→ Deploy
→ Launch
→ Product Validation and Learning
```

Operate-and-maintain is a recurring loop that may begin after launch, after a confirmed deployment, or whenever a qualified operational/product signal exists.

```text
Observe
→ detect signal
→ qualify evidence
→ normalize maintenance case
→ workflow-router selects one governing route
→ governing workflow executes
→ documentation assurance
→ verification/review/authorization
→ deployment or bounded action when applicable
→ actual health/outcome evidence
→ maintenance case closure and follow-up
→ continue observation
```

### Rationale

- Continuous product operation has no natural terminal point, while a product-development lifecycle and each maintenance case require bounded completion.
- A thirteenth linear phase would make product completion ambiguous or impossible.
- Existing workflows already own feature, bugfix, review, deployment, design, and product-validation lifecycles.
- The missing capability is composition and evidence continuity, not another universal lifecycle.

### Closure rule

Continuous observation does not prevent closure of a bounded maintenance case. A case closes only when its explicit outcome, evidence, remaining gaps, owner, and next action are recorded.

## 6. Decision D-2 — Documentation assurance is a facade skill

### Decision

Create `documentation-assurance` in `ai-native-skills` as:

```yaml
name: documentation-assurance
package_type: skill
pattern: facade
lifecycle_role: overlay_and_completion_gate
core_contract_for_mvp: none
```

### Owned scope

`documentation-assurance` owns:

- documentation-impact applicability classification;
- discovery and mapping of affected documentation domains;
- shared evidence and consistency contract;
- normalized documentation verdict;
- blocking findings and handoff;
- specialist selection for affected documentation domains;
- execution-receipt and continuity integration.

Expected primary outputs:

```text
documentation_impact_report
documentation_update_plan
documentation_verification_report
documentation_verdict
```

Required verdicts:

```text
DOCUMENTATION_REQUIRED
DOCUMENTATION_NOT_APPLICABLE
DOCUMENTATION_NOT_VERIFIED
```

### Delegated scope

It does not own every document's content. Content and review remain with the applicable owner, for example:

- PRD and scope documentation → `product-requirements` / product owner;
- architecture decisions → `adr` / architecture owner;
- API and schema contracts → `api-contract` / API owner;
- user-facing product content → product repository, content owner, or `content-strategy`;
- developer onboarding/setup → product repository and applicable developer-experience capability;
- operational runbook and deployment documentation → product operations owner;
- release notes/changelog → release owner;
- security/privacy documentation → governing security/privacy authority.

### Integration boundary

The facade is loaded conditionally by feature, bugfix, review, release, deployment, maintenance, and continuity compositions. It never becomes the primary product or implementation lifecycle.

### Why not a documentation workflow

The required value is applicability, evidence normalization, consistency, and verdict across many existing lifecycles. A new workflow would compete with those lifecycles and make documentation-only versus implementation work ambiguous.

## 7. Decision D-3 — Maintenance is normalized by a facade skill, not a new workflow

### Decision

Create `maintenance-case` in `ai-native-skills` as:

```yaml
name: maintenance-case
package_type: skill
pattern: facade
lifecycle_role: operational_case_overlay
core_contract_for_mvp: none
```

### Owned scope

`maintenance-case` owns:

- operational/product signal intake and evidence qualification;
- confidence and active-incident classification;
- normalized maintenance-case identity and scope;
- signal-to-route input artifact;
- cross-workflow evidence linkage;
- bounded case completion and recurrence/follow-up record;
- integration with `documentation-assurance` and `task-continuity`.

Expected outputs:

```text
maintenance_signal_assessment
maintenance_routing_input
maintenance_case_record
maintenance_outcome_record
maintenance_followup
```

### Routing boundary

`maintenance-case` may recommend or prepare routing input, but `workflow-router` selects the primary route.

```text
active incident
  → incident-response standalone capability

verified non-active defect or regression
  → bugfix-workflow

approved improvement or new capability
  → new-feature-workflow

existing design deficiency
  → design audit/refinement/redesign route

release/deploy/rollback action
  → deployment-workflow

review-only request
  → code-review-workflow or applicable domain review

product-value uncertainty
  → product-development product-validation/experiment composition

documentation-only correction
  → documentation-assurance as the executor under the applicable governing context
```

### Why not a maintenance workflow

A general maintenance workflow would duplicate several accepted lifecycles and either become a shallow router or absorb incident, bugfix, deployment, security, design, and product-validation responsibilities. The correct composition is a bounded case facade plus one primary governing route.

## 8. Decision D-4 — Runtime state must preserve record-family separation

### Decision

Capability execution state is not the same as review, gate, approval, delivery, or product acceptance.

The runtime capability-node state model for the MVP is:

```text
DISCOVERED
SELECTED
LOADED
EXECUTING
EXECUTED
FAILED
BLOCKED
SKIPPED
```

The following are linked record families, not capability-node states:

```text
review result
quality or completion gate result
risk acceptance
merge/release/deployment authorization
delivery/deployment record
environment health verification
product acceptance
product validation
```

### Required correction

The current experimental orchestration manifest models `REVIEWED` as a transition from `EXECUTED`. WS4 must migrate this into an explicit linked review record or equivalent runtime projection. It must not introduce `ACCEPTED`, `AUTHORIZED`, `DEPLOYED`, or `VERIFIED` as capability execution states.

### Execution evidence

`EXECUTED` requires all of:

- capability source loaded at an immutable revision;
- required procedure steps recorded;
- execution run identity;
- observable output artifact;
- completion evidence;
- no blocking execution failure.

Review requires a separate reviewed artifact, reviewer identity, findings, verdict, and independence status.

### Authority boundary

Runtime records facts and evaluated results. It never synthesizes product-owner approval, accepted risk, merge authorization, release authorization, deployment authorization, or product acceptance.

## 9. Decision D-5 — Repository ownership matrix

| Concern | `ai-native-core` | `ai-native-skills` | `ai-native-os` runtime | Product repository |
|---|---|---|---|---|
| Product lifecycle meaning | Owns canonical semantics | Implements/composes | Projects state only | Supplies product artifacts/policy |
| Primary routing meaning | Owns router contract | Implements routes and fixtures | Consumes routing handoff | Supplies context |
| Documentation assurance | No MVP contract | Owns executable facade and integrations | Records execution/evidence | Owns document locations/content/approval |
| Maintenance case | No MVP contract | Owns facade, taxonomy, routing input, closure procedure | Stores case/execution/evidence state | Owns thresholds, severity, runbooks, action authority |
| Capability graph metadata | Defines only promoted universal semantics | Owns manifests, roles, artifacts, dependencies | Validates/resolves graph | Supplies availability/policy |
| Execution state/persistence | No storage implementation | Declares evidence needs | Owns runtime state, adapters, persistence | Supplies external evidence |
| Review/gates | Defines canonical contracts where present | Executes reviewers/validators | Stores records | Owns product acceptance and policy gates |
| Merge/release/deploy authority | Preserves distinction | Must not infer | Must not synthesize | Owns authority |
| Real-world validation | Defines semantic distinction | Supplies reusable procedure | Supplies runtime evidence | Owns product outcome evidence |

## 10. Decision D-6 — Core RFC verdict

### Verdict

```text
NO_CORE_CHANGE_FOR_MVP
```

### Rationale

1. The twelve-phase product lifecycle is preserved; canonical lifecycle meaning does not change.
2. Documentation and maintenance capabilities have not yet passed independent real-product and real-maintenance validation.
3. The facade shapes are executable adapter-layer decisions, not yet proven universal cross-adapter contracts.
4. Runtime record and persistence behavior belongs in the runtime until stable semantic obligations are proven.
5. Existing Core contracts already preserve routing, lifecycle, incident, authorization, and acceptance boundaries needed for the MVP.

### Promotion rule

After #251, `skill-evolution` must evaluate whether verified repeated evidence justifies:

```text
NO_CHANGE
LOCAL_ONLY
IMPROVEMENT
RFC
DEFERRED_UNVERIFIED
```

A Core RFC is eligible only when a stable universal meaning, required cross-adapter fields, quality gates, compatibility impact, and at least one real product plus one real maintenance source case are available.

## 11. Decision D-7 — Delivery topology

### `ai-native-skills`

```text
main
└── 246-lifecycle-completion                epic integration branch
    ├── 247-lifecycle-semantics-decision    this decision slice
    ├── 248-documentation-assurance         after #247 approval
    ├── 249-maintenance-case-composition    after #247 approval
    └── 250-lifecycle-orchestration         after #248 and #249

final integrated PR
246-lifecycle-completion → main
only after #251 Product Acceptance
```

Child PRs target `246-lifecycle-completion`. Green child CI does not prove epic acceptance.

### Cross-repository work

- `ai-native-core`: no branch or issue is required for the MVP decision.
- `ai-native-os`: #250 must create or reuse a verified runtime issue and dedicated branch after #248/#249 handoffs exist.
- Product repository: #251 selects bounded real product and maintenance cases; product-specific branches and authority remain product-defined.

## 12. Downstream handoffs

### Handoff to #248

```yaml
operation: CREATE
capability: documentation-assurance
type: skill
pattern: facade
core_contract: none_for_mvp
required_integrations:
  - new-feature-workflow
  - bugfix-workflow
  - code-review-workflow
  - product-development-workflow
  - deployment-workflow
  - task-continuity
required_outputs:
  - documentation_impact_report
  - documentation_update_plan
  - documentation_verification_report
  - documentation_verdict
```

### Handoff to #249

```yaml
operation: CREATE_AND_UPDATE_COMPOSITION
new_capability: maintenance-case
new_capability_type: skill
new_capability_pattern: facade
update_targets:
  - workflow-router
  - role-switcher_when_required
  - task-continuity_integration
  - capability orchestration manifest inputs
core_contract: none_for_mvp
routing_owner: workflow-router
```

### Handoff to #250

```yaml
skills_inputs:
  - approved documentation-assurance manifest
  - approved maintenance-case manifest
  - expanded lifecycle intent/artifact registry
runtime_requirements:
  - keep capability execution state separate from review/gate/approval/delivery
  - replace REVIEWED node transition with linked review evidence
  - bind execution runs and observable artifacts before EXECUTED
  - preserve fail-closed graph validation
  - produce deterministic resume and receipt projections
core_change: prohibited_without_new_verified_rfc
```

### Handoff to #251

Validate:

- one real product change;
- one real maintenance case;
- documentation blocking and not-applicable behavior;
- bounded maintenance closure while observation continues;
- runtime state and record separation;
- no duplicate lifecycle/router ownership;
- Core RFC promotion eligibility.

## 13. Rejected alternatives

### Add phase 13: Operate and Maintain

Rejected because continuous operation has no terminal point and would confuse product-lifecycle completion with perpetual observation.

### Create `ai-native-engineering-workflow`

Rejected because it duplicates `product-development-workflow` and the feature/bugfix/review/deployment workflows.

### Create `documentation-workflow`

Rejected because documentation assurance is cross-cutting and must integrate with existing lifecycles rather than replace them.

### Create `maintenance-workflow`

Rejected because it would either duplicate workflow-router or absorb incident, bugfix, feature, design, deployment, and validation ownership.

### Put full state machine in Core now

Rejected because runtime record semantics remain under active development and have not passed cross-adapter validation.

### Keep `REVIEWED` as capability state

Rejected because review is performed by a reviewer over an artifact/output and must remain independently evidenced from capability execution.

## 14. Acceptance assessment for #247

| Criterion | Status | Evidence / gap |
|---|---|---|
| One product lifecycle owner remains explicit | `PASS` | `product-development-workflow` retained. |
| Operate-and-maintain defined as phase, loop, or hybrid | `PASS` | Recurring cross-workflow loop. |
| Documentation assurance has one owner | `PASS` | Proposed `documentation-assurance` facade. |
| Skills/Core/runtime/product ownership separated | `PASS` | Ownership matrix above. |
| Runtime states have identified authority | `PASS_WITH_FLAG` | Capability states decided; WS4 migration still pending. |
| Core RFC decision explicit | `PASS` | `NO_CORE_CHANGE_FOR_MVP`. |
| No lower-authority Core override | `PASS` | No Core edits proposed. |
| WS2–WS5 receive executable handoffs | `PASS` | Handoffs above. |
| Independent architecture review complete | `LIMITED` | Same execution context can perform a structured review, but owner/external approval remains required. |

## 15. Approval and execution boundary

This record is ready for owner and architecture review.

Approval permits #248 and #249 to begin from the declared integration branch. It does not grant:

- merge authorization for this PR;
- final epic merge authorization;
- creation of a Core RFC without new evidence;
- runtime implementation before #248/#249 handoffs;
- release, deployment, accepted-risk, or product-acceptance authority.

## 16. Capability evolution verdict

```text
LOCAL_ONLY
```

This decision improves local composition and provides an implementation hypothesis. Promotion to Core is deferred until #251 produces verified real-product and real-maintenance evidence.
