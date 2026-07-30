# Architecture Review — Hermes Specialist Agent Fleet Bootstrap

Issue: `puterakahfi/ai-native-skills#261`  
Parent epic: `puterakahfi/ai-native-skills#260`  
Reviewed artifacts:

- `docs/hermes-agent-fleet-bootstrap-architecture-decision-2026-07-29.md`
- `docs/hermes-agent-fleet-bootstrap-contracts-2026-07-29.md`

Base: `260-hermes-agent-fleet-bootstrap@7e629ceed27b6764119a89453ddf40041e15e50a`  
Reviewed head after contract commits: `261-fleet-architecture-contracts@d100092d0699eca92323d52106f1a9c7aa9efcd6`  
Date: 2026-07-29

## 1. Review context

```yaml
review_capability: architecture-review
review_scope: hermes_multi_agent_fleet_boundary_contracts_authority_and_downstream_constraints

repository_contracts:
  - docs/skills.md
  - docs/facade-skill-pattern.md
  - docs/skill-package-standard.md
  - skills/hermes-profile-bootstrap/SKILL.md
  - skills/hermes-profile-bootstrap/references/generation.md
  - skills/hermes-profile-bootstrap/references/skill-packs.md
  - catalog/capability-discovery/job-profiles.json
  - skills/workflow-router/SKILL.md
  - skills/role-switcher/SKILL.md

implementation_context:
  changed_files:
    - docs/hermes-agent-fleet-bootstrap-architecture-decision-2026-07-29.md
    - docs/hermes-agent-fleet-bootstrap-contracts-2026-07-29.md
  code_or_dependency_change: false
  executable_behavior_change: false

review_independence: LIMITED_SAME_EXECUTION_CONTEXT
owner_approval: ROUTE_FOR_APPROVAL
merge_authorization: NOT_GRANTED
```

## 2. Verdict

```text
ARCHITECTURE REVIEW VERDICT
───────────────────────────
Status: PASS WITH FLAGS

Capability taxonomy: PASS
Existing router/workflow ownership: PASS
Single-profile bootstrap boundary: PASS
One-bot/orchestrator topology: PASS WITH RUNTIME VALIDATION REQUIRED
Specialist profile boundaries: PASS
Artifact and handoff contracts: PASS
Reviewer independence semantics: PASS WITH LIMITATION
Product-context and live-state boundaries: PASS
Core RFC required now: NO
New dependency or framework: none
Blocking architecture violations: none
Review independence: LIMITED
Owner approval: ROUTE_FOR_APPROVAL
Merge authorization: NOT_GRANTED
```

The artifacts are sufficient to unblock implementation planning in #262 after owner review. They do not prove Hermes runtime support, skill behavior, profile creation, idempotency, or real cross-agent execution.

## 3. Contract checks

### 3.1 Capability taxonomy

**PASS**

`hermes-agent-fleet-bootstrap` is correctly classified as a `skill` using the facade/composer pattern.

It performs real coherent work beyond routing:

- multi-agent applicability and justification;
- topology selection;
- responsibility design;
- profile and fleet artifact assembly;
- conflict and safety validation;
- migration planning;
- normalized readiness and handoff.

It does not create a fourth official package type. It does not qualify as a workflow because it does not own a delivery lifecycle. It does not qualify as a pure meta-skill because it does not stop after selecting capabilities.

### 3.2 Workflow router and role composition ownership

**PASS**

The decision preserves:

```text
workflow-router
  → exactly one governing workflow for the actual task

role-switcher
  → one task owner, narrow specialists, and reviewers

hermes-agent-fleet-bootstrap
  → reusable persistent fleet design and bootstrap plan
```

No competing primary router, product lifecycle, feature lifecycle, or review lifecycle is introduced.

### 3.3 Single-profile bootstrap boundary

**PASS WITH REQUIRED IMPLEMENTATION CONSTRAINT**

The decision correctly leaves concrete profile paths, Hermes creation commands, profile skeletons, skill installation, and per-profile verification with `hermes-profile-bootstrap`.

Required downstream action `AR-01`: #262 and #263 must compose one explicit `profile_bootstrap_handoff` per approved profile. They must not copy the single-profile generation procedure or claim profile creation from a fleet plan alone.

### 3.4 Generalist preset versus specialist manifests

**PASS WITH REQUIRED IMPLEMENTATION CONSTRAINT**

The current `engineering` preset is a broad workstation bundle containing routing, workflows, Native AI foundations, engineering quality, and architecture capabilities. Installing it into every specialist would recreate multiple generalists with overlapping tools and responsibility.

Required downstream action `AR-02`: specialist profiles must use responsibility-specific `custom` skill manifests or equivalent smallest packs. Mandatory common foundations must be justified; broad presets may be used only when the profile genuinely owns that breadth.

### 3.5 One bot/front door and headless workers

**PASS WITH RUNTIME VALIDATION REQUIRED**

The architecture correctly separates:

```text
Hermes profile = durable agent identity and state boundary
bot/gateway = optional user-facing communication surface
worker process = bounded execution of a profile
Kanban/runtime work item = durable coordination state
```

The orchestrator-only gateway default minimizes credential, routing, audience, and notification complexity.

Flag `AR-03`: official runtime behavior, gateway commands, Kanban dispatcher availability, worker spawning, retry behavior, and profile addressing must be verified against the actual Hermes installation in #265. The architecture record must not be interpreted as runtime execution evidence.

### 3.6 Specialist granularity and T-shaped roles

**PASS**

The candidate archetypes are based on stable responsibilities and durable outputs rather than implementation names. The architecture correctly keeps React, SOLID, DDD, TDD, design patterns, API design, and equivalent methods as skills or adapters unless independent organizational responsibility is proven.

The `NOT_JUSTIFIED` path prevents multi-agent from becoming a default regardless of workload.

### 3.7 Product, architecture, design, frontend, backend, and review boundaries

**PASS WITH DOWNSTREAM TRACEABILITY REQUIREMENT**

The `owns` and `does_not_own` boundaries are coherent and preserve one accountable owner per durable artifact or decision.

Required downstream action `AR-04`: #262 must map every required output and decision to one profile contract, then #264 must fail duplicate ownership and missing-owner fixtures deterministically.

### 3.8 Sparse coordination and artifact handoffs

**PASS**

The decision rejects uncontrolled all-to-all messaging and defines accepted interaction modes:

- orchestrator invocation;
- durable Kanban task;
- temporary delegation;
- shared artifact handoff;
- review feedback loop;
- human approval.

The artifact handoff contract preserves producer, consumer, version, evidence, assumptions, risks, and correction route. This is proportionate for durable engineering work.

### 3.9 Reviewer independence

**PASS WITH EVIDENCE LIMITATION**

The contracts explicitly distinguish reviewer identity from actual independence and allow:

```text
VERIFIED
LIMITED_SHARED_MODEL
LIMITED_SHARED_CONTEXT
LIMITED_SHARED_TOOLS
NOT_VERIFIED
```

Flag `AR-05`: separate profile names are insufficient proof. #264 and #265 must report the actual shared model, context, tools, repository permissions, and task history that affect independence. Limited review must not become full product acceptance.

### 3.10 Profile isolation and security boundary

**PASS WITH REQUIRED RUNTIME DISCLOSURE**

The decision correctly states that Hermes profile isolation does not automatically prove OS sandboxing, filesystem restriction, network restriction, or credential isolation.

Required downstream action `AR-06`: every profile template and runtime acceptance case must declare permission scope and sandbox evidence. Privileged operations profiles require separate credentials, blast-radius controls, and human authorization.

### 3.11 Product agents and non-destructive migration

**PASS**

Existing `pkahfi`, `visualmate`, `docs`, and `ai` profiles are not assumed to be defective. They may remain valid product-facing agents while shared engineering specialists serve multiple products.

The migration taxonomy is explicit and automatic destructive actions are prohibited in MVP.

### 3.12 Catalog and job-profile ownership

**PASS WITH EXTENSIBILITY FLAG**

The architecture correctly uses capability discovery, job profiles, and capability metadata instead of creating a second capability universe.

Current job profiles do not cover every specialist archetype.

Flag `AR-07`: #262 may add Hermes-specific archetype templates referencing canonical capability IDs, but must not represent those templates as universal job-profile authority. A future catalog extension requires its own discovery/catalog review and validation.

### 3.13 Runtime/control-plane boundary

**PASS WITH NAMING FLAG**

The architecture intentionally leaves control-plane selection out of scope and refers to Hermes/runtime adapters generically.

Flag `AR-08`: current repository materials contain both `native-ai-fw` and newer `ai-native-os` ownership language. #262 must not silently choose or redefine the canonical runtime control plane. Runtime bindings remain external until governing repository decisions are reconciled.

### 3.14 Execution, review, authority, and acceptance separation

**PASS**

The contracts preserve distinct records for:

- specification and plan;
- runtime execution;
- verification evidence;
- review verdict;
- owner approval;
- merge/release/deployment authorization;
- product acceptance;
- validation in use.

A dry-run cannot claim profile creation. Installed skills cannot claim behavioral expertise. Worker completion cannot claim independent acceptance.

### 3.15 Core RFC verdict

**PASS WITH PROMOTION GATE**

`NO_CORE_CHANGE_FOR_MVP` is proportionate because the capability is Hermes-specific and has no cross-runtime proof.

Promotion gate `AR-09`: #265 must run `skill-evolution`. A future Core RFC requires stable runtime-agnostic semantics, at least one additional adapter or strong cross-runtime evidence, compatibility analysis, and verified source cases.

### 3.16 Documentation and package placement

**PASS**

Repository-level architecture and contracts belong under `docs/`. Downstream runtime references and templates belong in `skills/hermes-agent-fleet-bootstrap/references/` and `assets/`. Behavioral cases remain in `contracts/tests/`.

No unreferenced package-local `docs/` or duplicate eval authority is proposed.

### 3.17 Validation depth for this slice

**NOT_APPLICABLE for executable tests**

This workstream changes architecture documentation only. It adds no executable script, schema parser, package metadata, dependency, or runtime mutation.

Required before merge:

- inspect rendered Markdown and code blocks;
- verify all changed paths exist on the working branch;
- verify branch base and PR target;
- verify the PR references #261 and #260;
- confirm owner approval of material decisions;
- preserve limited reviewer independence;
- ensure downstream issues retain `AR-01` through `AR-09`.

## 4. Findings

| ID | Severity | Finding | Required action |
|---|---|---|---|
| `AR-01` | Required downstream | Fleet planning could duplicate single-profile generation. | Compose one `hermes-profile-bootstrap` handoff per profile; do not copy or falsely claim materialization. |
| `AR-02` | Required downstream | Broad `engineering` presets would recreate generalists. | Generate responsibility-specific custom manifests and justify shared foundations. |
| `AR-03` | Runtime validation | One-bot/headless-worker semantics are architecture assumptions until executed. | Verify Hermes gateway, Kanban, dispatcher, profile addressing, retries, and worker lifecycle in #265. |
| `AR-04` | Required downstream | Artifact ownership could become ambiguous in implementation. | Encode one owner per artifact/decision and add deterministic duplicate/missing-owner fixtures. |
| `AR-05` | Review limitation | Different profile names do not prove reviewer independence. | Record shared model/context/tools/permissions and limit verdict where necessary. |
| `AR-06` | Security | Hermes profiles are not automatic OS sandboxes. | Require permission policy, sandbox evidence, privileged separation, and human approval. |
| `AR-07` | Extensibility | Current job profiles do not cover every proposed specialist. | Use local Hermes archetypes referencing canonical capabilities; do not create a hidden second catalog. |
| `AR-08` | Ownership naming | `native-ai-fw` and `ai-native-os` runtime ownership language is not fully reconciled. | Keep runtime control-plane choice outside this skill until a governing decision resolves it. |
| `AR-09` | Promotion gate | Universal Core semantics lack cross-runtime evidence. | Run real Hermes validation and skill-evolution before any Core RFC. |
| `AR-10` | Authority | Architecture review does not approve merge, release, or production actions. | Obtain owner review and separate merge authorization. |
| `AR-11` | Review limitation | Author and reviewer share one execution context. | Treat verdict as `LIMITED`; owner or separate reviewer must confirm before acceptance. |

## 5. Auto-fail checks

| Check | Result |
|---|---|
| Competing product/engineering lifecycle introduced | PASS — none |
| Competing primary router introduced | PASS — none |
| New unsupported package type introduced | PASS — none |
| Single-profile bootstrap duplicated | PASS in architecture; downstream constraint recorded |
| Technology/framework agents normalized as default | PASS — rejected |
| One bot per specialist normalized as default | PASS — rejected |
| Uncontrolled all-to-all topology normalized | PASS — rejected |
| Product-specific facts leaked into reusable profile | PASS — prohibited |
| Live state or secrets included in distribution | PASS — prohibited |
| Profile isolation represented as proven OS sandbox | PASS — explicitly rejected |
| Review/approval/authorization conflated | PASS — separated |
| Core contract invented without evidence | PASS — no Core change for MVP |
| Executable behavior changed without tests | NOT_APPLICABLE |

## 6. Recommendation

Proceed with a draft PR targeting `260-hermes-agent-fleet-bootstrap` and route the decision and contract shapes to owner review.

#262 may begin package implementation after:

1. owner approval of the capability type, one-bot topology, archetype boundaries, and no-Core-change verdict;
2. PR target and branch topology are confirmed;
3. `AR-01` through `AR-11` are preserved as implementation and acceptance constraints.

#263, #264, and #265 remain responsible for integration, validation, real runtime evidence, and learning. This review does not establish that the proposed fleet works in Hermes.

## 7. Review receipt

```yaml
architecture_review:
  verdict: PASS_WITH_FLAGS
  blocking_violations: []
  required_downstream_actions:
    - AR-01
    - AR-02
    - AR-04
    - AR-06
  runtime_validation:
    - AR-03
  limitations:
    - AR-05
    - AR-08
    - AR-11
  extensibility_and_promotion_gates:
    - AR-07
    - AR-09
  authority_flags:
    - AR-10
  independence: LIMITED
  owner_approval: ROUTE_FOR_APPROVAL
  merge_authorization: NOT_GRANTED
```
