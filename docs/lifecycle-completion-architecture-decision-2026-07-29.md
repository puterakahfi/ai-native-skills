# AI-Native Engineering Lifecycle Completion — Architecture and Authority Decision

Issue: `puterakahfi/ai-native-skills#247`  
Parent epic: `puterakahfi/ai-native-skills#246`  
Date: 2026-07-29  
Status: `OWNER_APPROVED`

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
  owner_approval: APPROVED
  approval_source: explicit_user_instruction_2026-07-29
  review_status: LIMITED_INDEPENDENCE
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

This workstream is an independently reviewable architecture-decision slice. It authorizes downstream implementation under #248 and #249, while merge, release, deployment, and product acceptance remain separately evidenced.

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

Continuous observation does not prevent closure of a bounded maintenance case. A case closes only when its explicit outcome, evidence, remaining gaps, owner, and next action are recorded.

## 6. Decision D-2 — Documentation assurance is a facade skill

Create `documentation-assurance` in `ai-native-skills` as:

```yaml
name: documentation-assurance
package_type: skill
pattern: facade
lifecycle_role: overlay_and_completion_gate
core_contract_for_mvp: none
```

It owns documentation-impact applicability classification, affected-document discovery and mapping, shared evidence and consistency rules, a normalized verdict, blocking findings, specialist selection, and receipt/handoff integration. It does not own every document's content or product-specific approval.

Expected outputs:

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

The facade is loaded conditionally by feature, bugfix, review, release, deployment, maintenance, and continuity compositions. It never becomes the primary product or implementation lifecycle.

## 7. Decision D-3 — Maintenance is normalized by a facade skill, not a new workflow

Create `maintenance-case` in `ai-native-skills` as:

```yaml
name: maintenance-case
package_type: skill
pattern: facade
lifecycle_role: operational_case_overlay
core_contract_for_mvp: none
```

It owns operational/product signal intake, evidence qualification, active-incident classification, normalized maintenance-case identity and scope, routing input, cross-workflow evidence linkage, bounded closure, and recurrence/follow-up. `workflow-router` still selects exactly one primary route.

Expected outputs:

```text
maintenance_signal_assessment
maintenance_routing_input
maintenance_case_record
maintenance_outcome_record
maintenance_followup
```

## 8. Decision D-4 — Runtime state must preserve record-family separation

Capability execution state is not the same as review, gate, approval, delivery, or product acceptance.

MVP capability-node states:

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

Linked record families, not capability-node states:

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

WS4 must migrate the current experimental `EXECUTED → REVIEWED` transition into a linked review record or equivalent runtime projection. `ACCEPTED`, `AUTHORIZED`, `DEPLOYED`, and `VERIFIED` must not be introduced as capability execution states.

`EXECUTED` requires an immutable loaded capability source, recorded procedure steps, execution-run identity, observable output, completion evidence, and no blocking execution failure.

## 9. Repository ownership matrix

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

## 10. Core RFC verdict

```text
NO_CORE_CHANGE_FOR_MVP
```

The twelve-phase product lifecycle is preserved, the new facade shapes are not yet proven universal, and runtime record/persistence behavior remains runtime-owned. After #251, `skill-evolution` evaluates whether evidence justifies `NO_CHANGE`, `LOCAL_ONLY`, `IMPROVEMENT`, `RFC`, or `DEFERRED_UNVERIFIED`.

## 11. Delivery topology

```text
main
└── 246-lifecycle-completion
    ├── 247-lifecycle-semantics-decision
    ├── 248-documentation-assurance
    ├── 249-maintenance-case-composition
    └── 250-lifecycle-orchestration

final integrated PR
246-lifecycle-completion → main
after #251 Product Acceptance
```

Child PRs target `246-lifecycle-completion`. Green child CI does not prove epic acceptance.

## 12. Downstream handoffs

### #248

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
```

### #249

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

### #250

```yaml
runtime_requirements:
  - keep capability execution state separate from review/gate/approval/delivery
  - replace REVIEWED node transition with linked review evidence
  - bind execution runs and observable artifacts before EXECUTED
  - preserve fail-closed graph validation
  - produce deterministic resume and receipt projections
core_change: prohibited_without_new_verified_rfc
```

## 13. Rejected alternatives

- Add phase 13: rejected because continuous operation has no terminal point.
- Create `ai-native-engineering-workflow`: rejected as duplicate lifecycle ownership.
- Create `documentation-workflow`: rejected because assurance is cross-cutting.
- Create `maintenance-workflow`: rejected because it would duplicate routing or absorb existing lifecycles.
- Put the full runtime state machine in Core now: rejected pending real transfer evidence.
- Keep `REVIEWED` as capability state: rejected because review is independently evidenced.

## 14. Acceptance assessment

| Criterion | Status | Evidence / gap |
|---|---|---|
| One product lifecycle owner remains explicit | `PASS` | `product-development-workflow` retained. |
| Operate-and-maintain model explicit | `PASS` | Recurring cross-workflow loop. |
| Documentation assurance owner explicit | `PASS` | `documentation-assurance` facade. |
| Skills/Core/runtime/product ownership separated | `PASS` | Ownership matrix. |
| Runtime execution/review separation | `PASS_WITH_FOLLOWUP` | #250 implementation pending. |
| Core RFC decision explicit | `PASS` | `NO_CORE_CHANGE_FOR_MVP`. |
| Owner approval | `PASS` | Explicit approval on 2026-07-29. |
| Independent external review | `LIMITED` | Same execution context; disclosed. |

## 15. Capability evolution verdict

```text
LOCAL_ONLY
```

This decision improves local composition and provides an implementation hypothesis. Promotion to Core is deferred until #251 produces verified real-product and real-maintenance evidence.
