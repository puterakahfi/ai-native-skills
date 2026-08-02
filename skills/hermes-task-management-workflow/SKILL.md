---
name: hermes-task-management-workflow
description: Use when chat work must become durable project-board execution with orchestrator routing and evidence-backed acceptance. Do not use it as a replacement for product, implementation, review, deployment, or external-tracker workflows.
license: MIT
metadata:
  ai-native-skills.version: 1.7.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.pattern: facade
  ai-native-skills.requires: "workflow-router role-switcher delivery-work-breakdown git-workflow product-development-workflow new-feature-workflow bugfix-workflow code-review-workflow deployment-workflow"
  ai-native-skills.related_skills: '["hermes-kanban-orchestration","workflow-router","role-switcher","delivery-work-breakdown","git-workflow","product-development-workflow","new-feature-workflow","bugfix-workflow","code-review-workflow","deployment-workflow","spike","documentation-assurance"]'
  ai-native-skills.boundary.covers: '["project_board_selection","parent_outcome_card_contract","visible_card_identity_contract","task_routing_record","agent_assignment_decision","assignment_readiness_separation","repository_mutation_gate","gateway_dispatch_readiness","idempotent_dependency_pipeline","duplicate_overlap_control","scope_change_control","cancel_supersede_followup","agent_to_agent_progression","external_approver_notification","execution_observability","failure_recovery","board_lifecycle_gates","evidence_backed_parent_completion","external_tracker_sync_gate","fleet_portability_contract","role_bootstrap_contract"]'
  ai-native-skills.boundary.delegates: '["hermes_runtime_mutation","primary_lifecycle_execution","product_scope_and_acceptance_definition","delivery_decomposition","implementation","domain_review","deployment","external_tracker_mutation"]'
---

# Hermes Task Management Workflow

Turn chat requests into durable, routed, reviewable project-board work while preserving the authority of existing product and delivery workflows.

## Boundary

This facade owns the project-board operating model, parent-card routing contract, board-stage gates, assignment decision, evidence aggregation, and parent completion verdict.

It delegates:

- Hermes board/card mutations and dispatcher mechanics to `hermes-kanban-orchestration` and the available Hermes runtime tools;
- exactly-one-primary-workflow selection to `workflow-router`;
- owner, specialist, and reviewer composition to `role-switcher`;
- epic/feature/task hierarchy and repository topology to `delivery-work-breakdown`;
- branch/worktree execution and source-control safety to `git-workflow`;
- product, feature, bugfix, review, deployment, spike, and documentation execution to their existing capabilities.

It does not create a second product or engineering lifecycle. It never treats board status, child completion, green CI, a sample, or a prototype as sufficient product acceptance.

## Operating model

```text
chat request
→ select the durable board for the project
→ create or update one parent outcome card owned by agent-orchestrator
→ classify and record routing before dispatch
→ select one primary workflow
→ assign one execution owner plus bounded specialists and reviewers
→ materialize one idempotent dependency graph
→ let the gateway dispatcher run Plan → Sample/Decision when needed → Design/Product → Build → Test → Verify → Review → Accept
→ run explicitly required, authorized merge/deploy lanes and capture execution receipts
→ wake agent-orchestrator for end-to-end synthesis → Done or READY_FOR_ACCEPTANCE_OR_RELEASE
→ optionally sync an external tracker only after separate explicit approval
```

Use one durable Hermes Kanban board per project, product, repository, or independently governed workstream. Do not mix unrelated products on one board merely because they share an agent fleet. If the project board is unknown or unavailable, stop with `BLOCKED` or `NOT_VERIFIED`; do not silently use a default board.

Every new parent outcome card defaults to `agent-orchestrator`. A specialist may own a child card or execution lane, but does not replace parent synthesis and acceptance-gate ownership. Routine lane completion and review handoffs proceed through dependency promotion and the dispatcher; they do not require the user to send another chat message.

## Required inputs

```yaml
task_management_request:
  user_request: string
  project_or_workstream: string
  board_ref: string | NOT_VERIFIED
  source_artifact_refs: []
  requested_outcome: string
  acceptance_criteria: []
  profile_inventory_ref: string | NOT_VERIFIED
  dispatcher_evidence_ref: string | NOT_VERIFIED
  repository_or_runtime_context: []
  repository_work_gate_ref: string | NOT_VERIFIED
  approval_policy_refs: []
  external_sync_requested: false
```

Missing board identity, requested outcome, or acceptance basis blocks dispatch. Missing profile inventory blocks assignment to an unverified assignee. Repository mutation also requires an explicit, verified branch/worktree gate before the card becomes executable. Automatic-mode claims require observable gateway/dispatcher evidence; a written pipeline alone is not evidence that ready work will run.

## Parent card contract

Every parent card must contain this `routing:` block before specialist dispatch:

```yaml
routing:
  project: <project-or-board-slug>
  board_ref: <verified Hermes board reference>
  task_type: <product_idea | prd_spec | feature | bug | design | review | deployment | spike_sample | documentation | unknown>
  source_artifact:
    type: <user_request | prd | spec | screenshot | error_log | issue | code_diff | deploy_url | document | other>
    refs: []
  hierarchy:
    kind: <epic | subtask | single_task>
    parent_task_id: <task id | null>
    parent_external_ref: <issue, PRD, epic, or other authority ref | null>
    owns_overall_dod: <true | false>
    requires_decomposition: <true | false>
    lane_role: <plan | design | engineering | test | verify | review | product_acceptance | release | sync | null>
    terminal_state_policy:
      done_requires: <full_delivery_chain | lane_local_dod | single_task_dod>
  lifecycle_stage: <plan | sample | decision | build | verify | accept | done>
  primary_workflow: <selected capability | NOT_VERIFIED>
  parent_owner: agent-orchestrator
  execution_owner: <verified profile id | NOT_VERIFIED>
  specialists: []
  reviewers: []
  role_evidence_expectations: []
  readiness_gate:
    status: <READY | NEEDS_PLANNING | NEEDS_DISCOVERY | NEEDS_DECISION | BLOCKED | NOT_VERIFIED>
    missing_inputs: []
    allowed_next_action: <plan | inspect | diagnose | decide | dispatch_execution | block>
    mutation_allowed: <true | false>
  repository_work_gate:
    mutation_intended: <true | false>
    repository_ref: <path or project reference | null>
    protected_branch_policy_ref: <reference | unknown | null>
    release_unit_ref: <epic, feature, task, bug, spike, or single-task reference | null>
    base_branch: <explicit branch | NOT_VERIFIED | null>
    working_branch: <explicit branch | NOT_VERIFIED | null>
    pr_target: <explicit branch | NOT_VERIFIED | null>
    workspace_kind: <worktree | branch | dir_readonly | scratch | null>
    direct_main_checkout_mutation_allowed: false
    topology_source: <delivery-work-breakdown | explicit_user_authority | NOT_VERIFIED | null>
    git_workflow_required: <true | false>
  approval_required_before_build: <true | false | NOT_VERIFIED>
  approval_required_before_done: <true | false | NOT_VERIFIED>
  acceptance_criteria_refs: []
  required_evidence: []
  dependencies: []
  automation:
    mode: <gateway_dispatcher | manual_dispatch | NOT_VERIFIED>
    dispatcher_evidence_ref: <gateway/config/runtime receipt | null>
    pipeline_key: <stable project-and-outcome key>
    graph_revision: <integer>
    lane_key_rule: <pipeline_key plus stable lane identity>
  release_scope:
    merge_required: <true | false | NOT_VERIFIED>
    deploy_required: <true | false | NOT_VERIFIED>
    external_sync_required: <true | false>
    authorization_refs: []
    execution_receipt_refs: []
  human_gates:
    - type: <product_owner_acceptance | merge | deploy | external_sync | ambiguous_decision>
      authority_ref: <reference | null>
      status: <NOT_REQUIRED | PENDING | APPROVED | REJECTED | NOT_VERIFIED>
  external_sync:
    requested: false
    target: null
    approval_ref: null
```

Rules:

1. `primary_workflow` contains exactly one governing workflow or standalone capability.
2. `parent_owner` remains `agent-orchestrator` until parent synthesis is complete.
3. `execution_owner`, specialists, and reviewers must resolve to profiles proven by `profile_inventory_ref`; role labels are not assignee IDs.
4. Every activated role has a distinct expected output and evidence reference.
5. Every child traces to parent acceptance criteria and explicit dependencies.
6. `unknown` or `NOT_VERIFIED` routing fails closed; it is not permission to dispatch.
7. External synchronization remains false unless separately requested and approved.
8. `pipeline_key` and graph revision identify one canonical decomposition; every lane receives a deterministic idempotency key derived from that pipeline and stable lane identity, and retries reuse or reconcile it instead of creating parallel lanes.
9. A generic `review-required` state routes to a verified agent reviewer lane when one exists. It is not automatically a human gate.
10. Human gates are enumerated and limited to product-owner acceptance, merge, deploy, external sync, or a genuinely ambiguous decision that no authorized agent can resolve.
11. Release scope is explicit before decomposition. Required merge or deploy work is represented by a final authorized lane, not inferred from acceptance or CI.
12. `hierarchy.kind` is classified before dispatch. Ambiguity routes to orchestrator triage or blocks; it never silently defaults to `single_task`.
13. Assignment records responsibility only. It never changes `readiness_gate.status`, grants mutation authority, or proves that the dispatcher may execute the card.
14. A repository-mutating lane is executable only when its branch/worktree topology is explicit and verified; direct mutation on the main/default checkout remains forbidden.

## Work-item hierarchy classification

Classify every work item before dispatch because hierarchy determines ownership, decomposition, terminal-state meaning, and the evidence needed for Done.

| Kind | Classification rule | Ownership and terminal policy |
|---|---|---|
| `epic` | The requested outcome spans multiple lifecycle stages or roles, requires dependent lanes, or owns product/release acceptance. | `agent-orchestrator` owns the parent and overall DoD; `requires_decomposition: true`; Done requires the full delivery chain, acceptance, terminal release/sync lanes when in scope, and synthesis. |
| `subtask` | The work has a parent task/external parent or represents one bounded role/lane of a broader outcome. | A verified specialist owns only `lane_local_dod`; `owns_overall_dod: false`; completion writes a structured handoff and promotes/delegates the next known lane. |
| `single_task` | One verified owner can complete the entire requested outcome and all applicable verification/acceptance gates without child lanes. | That owner completes `single_task_dod`; merge, deploy, or external sync still require explicit scope and authority when applicable. |

Decision order:

```text
has parent or is one lane of a broader outcome
  → subtask

otherwise spans multiple roles/stages, dependent work, product acceptance, or release acceptance
  → epic

otherwise one verified owner can satisfy the complete requested DoD without decomposition
  → single_task

otherwise
  → BLOCKED / orchestrator triage
```

Do not use title size, file count, estimated duration, or the word “task” as classification evidence. A small release-authority outcome may still be an epic; a large but truly bounded one-owner analysis may be a `single_task`. Parent external references preserve provenance but do not replace the Hermes `parent_task_id` when an internal parent exists.

## Visible card identity and title rules

Because Hermes Kanban cards are intentionally simple, every created or reconciled card must expose its hierarchy in the visible title and durable routing metadata. Do not rely on prose descriptions, chat history, column position, or assignee names to distinguish epic parents from subtasks.

Use exactly one of these title families:

| Hierarchy kind | Required visible title format | Required relationship fields | Initial owner and status |
|---|---|---|---|
| `epic` | `[EPIC] <project-or-product>: <outcome>` | `parent_task_id: null`, `owns_overall_dod: true`, `requires_decomposition: true`, `lane_role: null`, `terminal_state_policy.done_requires: full_delivery_chain` | `agent-orchestrator`; `triage` until decomposition and gates pass |
| `subtask` | `[SUBTASK][<parent_task_id>][<lane_role>] <bounded lane result>` | `parent_task_id: <epic task id>`, `owns_overall_dod: false`, `requires_decomposition: false`, `lane_role: <plan|design|engineering|test|verify|review|product_acceptance|release|sync>`, `terminal_state_policy.done_requires: lane_local_dod` | verified lane owner; `todo` or `blocked` until dependencies pass |
| `single_task` | `[TASK] <project-or-product>: <bounded complete outcome>` | `parent_task_id: null`, `owns_overall_dod: true`, `requires_decomposition: false`, `lane_role: null`, `terminal_state_policy.done_requires: single_task_dod` | one verified owner; status follows readiness gate |

Every card must also carry a compact identity block in metadata, labels, or the task body according to the active Kanban protocol:

```yaml
card_identity:
  kind: <epic | subtask | single_task>
  parent_task_id: <task id | null>
  parent_title: <parent title | null>
  lane_role: <plan | design | engineering | test | verify | review | product_acceptance | release | sync | null>
  pipeline_key: <stable project-and-outcome key>
  lane_identity: <stable lane identity | null>
  idempotency_key: <pipeline key, or pipeline_key:lane:lane_identity>
  title_prefix: <[EPIC] | [SUBTASK][parent][lane] | [TASK]>
```

Creation gates:

1. When classification yields `epic`, first create or reuse the `[EPIC]` parent card, then create or reconcile dependency-linked `[SUBTASK]` cards. Do not create lane cards without the returned parent task ID.
2. A `[SUBTASK]` without a valid `parent_task_id`, `lane_role`, and deterministic lane idempotency key is malformed and must remain `BLOCKED`/`NOT_VERIFIED`; do not dispatch it.
3. A child card title must identify both the parent and lane. A title such as `Implement onboarding`, `Review needed`, or `Frontend task` is not acceptable for an epic child.
4. A parent epic title must not masquerade as executable lane work. If the card owns overall DoD, its title starts with `[EPIC]` and it remains orchestrator-owned until synthesis.
5. A `single_task` may not use `[EPIC]` or `[SUBTASK]`; if follow-on lanes become necessary, supersede or revise it into an epic graph instead of silently adding ambiguous children.
6. Board views should be filterable by `kind`, `parent_task_id`, `lane_role`, and `pipeline_key`; if the active runtime lacks native fields, encode these values in the task body and labels before dispatch.

## Task classification and primary route

Classify intent before assigning an agent. Use `workflow-router` for the authoritative route and preserve exactly one primary selection.

| Task type | Evidence signal | Primary route |
|---|---|---|
| `product_idea` | value, audience, positioning, or solution direction is unresolved | `product-development-workflow` |
| `prd_spec` | create/revise requirements or specification without build authority | `product-development-workflow` plus the applicable artifact producer, or `spec-workflow` when technical specification is the actual intent |
| `feature` | accepted capability for an existing product | `new-feature-workflow` |
| `bug` | broken expected behavior, reproducible regression, failure evidence | `bugfix-workflow` |
| `design` | audit, narrow correction, or broad redesign | `design-audit`, `design-refinement`, or `redesign-workflow` according to scope |
| `review` | code, architecture, security, design, or readiness verdict | `code-review-workflow` or the applicable review facade |
| `deployment` | release, deploy, rollback, DNS, environment, or runtime promotion | `deployment-workflow` |
| `spike_sample` | reversible feasibility test, prototype, or sample requested before commitment | `spike` |
| `documentation` | documentation-only correction under verified governing context | `documentation-assurance` |
| `unknown` | intent, authority, source, or outcome is unresolved | orchestrator triage; no execution dispatch |

The artifact noun does not decide the route. A PRD can be authored, reviewed, revised, or implemented; a screenshot can evidence a bug, design finding, or acceptance result.

## Agent assignment decision tree

First use `role-switcher` to distinguish:

```text
parent owner     durable outcome coordination and final synthesis
execution owner one accountable producer for the current child or lane
specialist      narrow contribution with a distinct expected output
reviewer        independent evidence and verdict; not the sole implementer
```

Then assign only to a verified available profile:

| Classified responsibility | Preferred verified assignment | Fallback when profile is absent |
|---|---|---|
| product intent, PRD, acceptance | `agent-product` | `agent-orchestrator` with product capability; record limitation |
| design direction or UX evidence | `agent-design` | `agent-orchestrator` with design capability; record limitation |
| frontend implementation | `agent-frontend` | verified engineering profile with frontend scope, otherwise `BLOCKED` |
| backend/general engineering | `agent-backend` or another verified engineering profile | `agent-orchestrator` only for triage; implementation remains `BLOCKED` without capability evidence |
| deployment/operations | verified profile whose contract owns DevOps/operations | `agent-orchestrator` for coordination only; privileged execution requires a verified operations owner |
| security analysis | verified profile whose contract owns security work | use security specialist/reviewer capability under an eligible owner; do not invent `agent-security` |
| architecture decision or review | `agent-architecture` | eligible engineering owner plus architecture reviewer, with independence limitation recorded |
| independent review | `agent-review` | verified domain reviewer; otherwise acceptance is `LIMITED` or `BLOCKED` |
| unknown or cross-domain coordination | `agent-orchestrator` | remain in triage until routing evidence resolves |

Do not infer that `agent-devops`, `agent-security`, or any other profile exists from a capability name. Unknown assignees can leave cards undispatched and are a blocking routing defect.

For multi-domain work, keep the parent with `agent-orchestrator` and create dependency-linked child cards. Load `delivery-work-breakdown` before broad decomposition or repository topology decisions.

## Assignment, readiness, and repository mutation gates

Assignment answers **who is responsible if the card becomes executable**. Readiness answers **whether execution is permitted now**. Keep these decisions separate in both card data and board status.

```text
assigned + READY + all authority/topology gates pass
  → executable `ready`

assigned + planning/discovery/decision still required
  → `triage`; only the declared non-mutating next action is allowed

assigned + missing human authority or repository topology
  → `blocked`; record the exact unblock condition

assigned + unknown readiness
  → not executable; never default to `ready`
```

Create intake cards with `triage: true` when specification or decomposition is still required. Create them with `initial_status: blocked` when a known authority, capability, or repository gate is missing. Promote a card to `ready` only after hierarchy, primary workflow, verified execution owner, acceptance basis, `readiness_gate.status: READY`, and every applicable authority and repository gate pass. A running gateway may claim a `ready` card immediately, so placing it there is an execution decision, not clerical organization.

For every repository-mutating lane:

1. consume the release-unit and topology decision from `delivery-work-breakdown`, or record explicit user authority;
2. record repository, protected-branch policy, release unit, explicit base branch, working branch, PR target, and workspace strategy;
3. verify live branch/worktree evidence before the first edit;
4. execute branch/worktree operations through `git-workflow`;
5. forbid direct mutation in the main/default checkout or protected branch;
6. attach the verified workspace and branch evidence to the lane handoff and parent synthesis.

Unknown base branch, working branch, PR target, protected-branch policy, release topology, or workspace strategy yields `BLOCKED`/`NOT_VERIFIED` with `mutation_allowed: false`. Do not infer `main` from the repository default, and do not treat a `dir` workspace on the default checkout as writable without a bounded, explicitly authorized exception.

## Automatic dispatch and lane progression

Automatic operation uses the gateway-embedded Hermes dispatcher. Verify current behavior against the installed runtime and official Hermes Kanban documentation before recording the command or configuration as evidence.

```text
default operating mode
  hermes gateway start
  config: kanban.dispatch_in_gateway: true

deprecated fallback
  hermes kanban daemon --force
  only when the gateway cannot run and only when the installed runtime exposes it
```

Do not run a standalone daemon alongside the gateway dispatcher against the same board. `hermes kanban watch` only streams events and does not dispatch work. A one-shot `hermes kanban dispatch` is a diagnostic/manual nudge, not proof of continuous automatic mode.

The dispatcher sweeps all active boards. A board does not need its own daemon process, but each task is board-pinned and every project pipeline records its board reference. Automatic progression is dependency-driven:

```text
Plan lane Done
→ dispatcher promotes dependency-unblocked Sample or Decision lane todo → ready
→ assigned profile executes it
→ Build Done promotes Verify or independent Review
→ review PASS promotes product/owner Accept
→ all required lanes Done/accepted promotes orchestrator synthesis
```

Use Hermes dependency edges only for execution order. Do not make the parent outcome card a blocking predecessor of its first child, which would deadlock parent completion against child completion. Preserve child-to-outcome membership through the routing block, acceptance references, and synthesis record; make the final orchestrator synthesis depend on all terminal required lanes.

When a running reviewer finds remediable defects, it creates or identifies a bounded remediation lane, links that lane as its dependency, and blocks with dependency semantics so it auto-resumes after remediation. When a verified reviewer profile exists, implementation completion must route to `agent-review`, `agent-product`, `agent-architecture`, or the applicable domain reviewer instead of surfacing a generic `review-required` request to the user.

### Fleet portability and role bootstrap contract

This workflow is a fleet-level operating model, not a local chat convention. A runtime fix, local board repair, or one successful project-board run is not enough to claim durable rollout. The model must be available through the reusable skill package and through the profile or fleet-bootstrap mechanism used to create other Hermes agents.

Required distribution evidence before claiming global or reusable workflow readiness:

1. `hermes-task-management-workflow` records the current lane, handoff, review, remediation, synthesis, and authority semantics.
2. The behavioral contract in `contracts/tests/hermes-task-management-workflow.test.yaml` contains regression cases for those semantics.
3. Fleet bootstrap/profile assets that create or update `agent-orchestrator`, implementation specialists, and review profiles include the smallest role-specific operating rules needed for Kanban-dispatched work.
4. Kanban-dispatched tasks can receive the model without a manual slash command or ad hoc chat reminder.
5. Runtime-local fixes and ai-native-skills package changes cross-reference each other through task comments, release notes, or another durable evidence handle.

Role-specific minimums:

| Profile class | Must carry without manual prompting |
|---|---|
| `agent-orchestrator` | Board selection, explicit epic/subtask/single classification, canonical graph reconciliation, parent hold/synthesis, status summary, and authority-gate reporting. |
| Implementation specialists | Lane-local scope only, exact commit or immutable artifact evidence, clean worktree evidence for repository mutation, structured `lane_handoff`, and no generic human `review-required` block when a reviewer lane exists. |
| Review profiles | Canonical verdicts, latest-evidence review target, bounded remediation/re-review routing, and no parent/release approval beyond the review lane. |

If a target Hermes installation lacks those skills or profile assets, report `NOT_PORTABLE` or `NOT_VERIFIED` rather than saying the workflow is permanent. Local runtime validation remains useful evidence, but the portable deliverable lives in the ai-native-skills package plus the installed Hermes runtime behavior.

### Lane-local completion and structured handoff

Each child owns only its lane-local DoD. Child Done is a graph milestone, never proof that the parent outcome is Done. Before completing a lane, write a durable structured handoff that the next assignee and parent synthesizer can consume without reconstructing chat history:

```yaml
lane_handoff:
  lane_ref: <task id>
  lane_identity: <stable semantic identity>
  lane_local_result: <PASS | NEEDS_WORK | BLOCKED | REJECTED | NOT_VERIFIED>
  operational_status: <DONE | NEEDS_WORK | BLOCKED | REVIEW_REQUIRED_AGENT | AWAITING_HUMAN_AUTHORITY | FAILED>
  exact_reason: <attributable reason for the status>
  next_action: <one exact action>
  decisions: []
  artifacts: []
  changed_files: []
  exact_commit: <commit sha | null>
  worktree_status: <clean | dirty | not_applicable | not_verified>
  commands_and_results: []
  evidence_refs: []
  risks: []
  blockers: []
  acceptance_mapping:
    - criterion_ref: <parent criterion>
      contribution: <what this lane established>
      verdict: <PASS | FAIL | PARTIAL | NOT_VERIFIED>
  next_lane:
    ref: <existing task id | null>
    identity: <stable lane identity | null>
    assignee: <verified profile | null>
    promotion_condition: <dependency completion or explicit authority gate>
```

If the next lane is known, create or reuse it and record its task ID before completing the current lane. Do not replace `next_lane` with “ask the user to continue” or a vague human review request. If no next lane is applicable, say why and identify the parent synthesis dependency. Store human-readable synthesis in the lane summary and machine-readable handoff facts in durable result metadata or a task comment according to the active Kanban protocol.

For repository-mutating implementation lanes, `DONE` requires an attributable immutable source of truth. Prefer a local commit on the lane branch/worktree plus a clean worktree. If policy explicitly forbids committing, the lane must state the approved alternative immutable artifact; otherwise it remains `BLOCKED`/`FAILED` as a protocol issue and must not ask review to infer changes from a dirty checkout. `REVIEW_REQUIRED_AGENT` may appear inside the handoff as the next operational state, but it is not a reason to leave a completed implementation card blocked when the reviewer lane is known and linked.

`operational_status` is mandatory and has one meaning:

- `DONE`: lane-local DoD and structured handoff are complete;
- `NEEDS_WORK`: bounded remediation is known and routes to an agent lane;
- `BLOCKED`: a dependency or capability prerequisite prevents progress;
- `REVIEW_REQUIRED_AGENT`: an eligible reviewer lane is required and known;
- `AWAITING_HUMAN_AUTHORITY`: a named product, merge, deploy, risk, or sync authority gate is the only blocker;
- `FAILED`: execution crashed, timed out, violated protocol, or ended without trustworthy completion evidence.

Every non-Done status records the exact reason, evidence reference, and next action. A status label without those fields is `NOT_VERIFIED`, not progress.

### Idempotent decomposition and reconciliation

Before creating any lane:

1. derive a stable `pipeline_key` from board, canonical outcome identity, and accepted scope;
2. define one stable semantic `lane_identity` per node, such as `plan`, `design`, `frontend-build`, `runtime-verify`, `independent-review`, `product-accept`, `merge-main`, or `deploy-production`;
3. derive each `idempotency_key` deterministically as `<pipeline_key>:lane:<lane_identity>`; a graph revision does not change this key unless accepted scope changes the lane's canonical identity;
4. inspect existing non-archived cards and links for that key, task type, acceptance refs, and source artifact;
5. pass the derived `idempotency_key` to `kanban_create`, retain the returned task ID, and reuse that ID for handoffs and dependency links on every retry;
6. reuse the canonical card, add only missing lanes or edges, and reject cycles;
7. compare the desired graph to the live graph and record `REUSED`, `CREATED`, `REPAIRED`, `SUPERSEDED`, or `NOT_VERIFIED` per node and edge;
8. never create a second active pipeline to recover a stalled first pipeline;
9. archive or unlink stale duplicates only with attributable cleanup authority and preserved evidence.

After decomposition, verify that every assignee exists, every non-initial lane has the intended dependency, terminal review/acceptance lanes feed synthesis, and no duplicate active card or edge remains. Failed reconciliation blocks dispatch rather than producing an ambiguous graph.

### Duplicate, overlap, scope, cancellation, and follow-up control

Treat lifecycle changes as governed graph revisions, not ad hoc card creation or silent edits.

**Duplicate or overlap:** Before creating or promoting work, compare board, canonical outcome, source refs, accepted scope, acceptance criteria, repository/release unit, and active lane identities. Exact duplicates reuse the canonical card. Partial overlaps either consolidate under one owner with an explicit acceptance mapping or remain separate with a documented non-overlap boundary. If ownership cannot be reconciled, block both mutation paths. Mark stale work `SUPERSEDED / DO NOT EXECUTE`, detach obsolete dependency edges, preserve provenance, and verify that only one canonical active mutation owner remains.

**Scope change:** Classify new information as one of:

```text
clarification       preserves outcome and acceptance basis; update the canonical card
bounded remediation fixes a finding under the same active parent; create/reuse a remediation lane
material change     changes outcome, audience, architecture, release unit, acceptance criteria, or authority; stop affected lanes and require a new approved graph revision or successor parent
scope creep         unrelated or unapproved work; reject from the active lane and record a follow-up candidate
```

Never let an implementation lane absorb unapproved work because it appears nearby in the repository. A material change invalidates stale readiness and mutation authority until impact, acceptance, dependencies, topology, and ownership are re-approved.

**Cancel and supersede:** Cancellation requires an attributable authority reference, reason, affected lanes, side effects already performed, retained artifacts/evidence, dependency cleanup, and downstream notification. Cancelled work is not Done and does not satisfy acceptance criteria. Superseding creates or identifies the successor, links provenance, marks the old graph non-executable, and prevents both graphs from mutating the same scope concurrently.

**After Done:** Never reopen or silently rewrite completed evidence. New defects, improvements, or changed requirements become a follow-up `single_task` or `epic` according to complete current scope. Link the original parent as provenance, run fresh readiness and repository gates, and preserve the original Done receipt. If a release-blocking finding proves the prior acceptance invalid, record the original as superseded for release purposes and route a successor remediation plus independent review; do not pretend the earlier evidence never existed.

## Observability and failure recovery

Automatic execution must be inspectable from the board without asking the user to poll chat or read every worker transcript. Maintain this compact status on every `epic` and `single_task` parent after each material event:

```yaml
status_summary:
  current_lane: <lane identity | null>
  current_assignee: <verified profile | null>
  current_state: <running | dependency_wait | agent_review_running | human_gate | release_authorization_gate | external_sync_gate | completed | failed | not_verified>
  last_completed_lane: <lane identity | null>
  next_lane: <lane identity | null>
  blocked_reason: <exact reason | null>
  required_human_gate: <gate type and authority | null>
  verification_evidence_refs: []
  updated_at_ref: <board event, run, or comment reference>
```

Distinguish active work from passive waiting. `running` and `agent_review_running` require a live run/worker receipt; `dependency_wait` requires an unresolved dependency; human, release-authorization, and external-sync gates identify the authority and exact unblock condition. Do not report `running` merely because the parent is open or a worker was once spawned.

Treat crashes, protocol violations, timeouts, stale workers, duplicate-graph detection, and missing structured handoffs as observable failures:

1. collect the task, run, event/log, error, timeout, worker-liveness, and graph evidence available to the runtime;
2. set the lane to `FAILED` or `BLOCKED` with exact reason and next action; never leave it looking active;
3. route the incident to `agent-orchestrator` remediation/triage;
4. create or reuse a bounded remediation/retry lane with the existing deterministic `idempotency_key`; do not duplicate the canonical lane or pipeline;
5. repair dependencies or handoff metadata, then retry only when the failure condition is resolved and the active runtime allows retry;
6. record the recovery attempt and outcome in the parent status summary and final lane timeline.

A missing handoff prevents downstream promotion even when a process exited zero. A stale worker or expired run is not active work. Duplicate detection blocks graph advancement until canonical ownership and edges are reconciled.

### User-external approver and notification model

The user/product owner is external to routine Plan → Build → Verify → Review execution. Do not model the user as an internal Kanban lane, assignee, dependency node, or the “continue” button between agents. Internal reviewers own routine correctness and quality findings; they must route `NEEDS_WORK` to bounded agent remediation and re-review until PASS, BLOCKED, or a genuine authority decision remains.

Only surface work to the user for a named authority gate reserved by policy, such as final product acceptance, material scope/priority choice, merge, deploy, risk acceptance, or external sync. A sample or preview does not silently wait for the user: first route it to the applicable agent reviewer, then either auto-promote the next known lane or publish an explicit authority request.

Every human-facing gate or terminal notification must carry this evidence packet:

```yaml
notification_evidence_packet:
  parent_ref: <task id>
  requested_decision: <one exact decision or null>
  authority_type: <product_owner_acceptance | scope | priority | merge | deploy | risk | external_sync | null>
  current_state: <human_gate | completed | failed | superseded>
  completed_lanes: []
  reviewer_verdicts: []
  acceptance_matrix_ref: <reference | null>
  artifacts_and_runtime_evidence_refs: []
  unresolved_risks: []
  exact_unblock_or_next_action: <one action>
  notification_receipt_ref: <subscription, delivery, watcher, or runtime receipt | NOT_VERIFIED>
```

At workflow start, verify a completion/authority-gate notification subscription or another bounded delivery mechanism supported by the runtime. Notifications are observability only; dependencies and the gateway continue internal progression without a human subscriber. If delivery cannot be configured, record `notification_receipt_ref: NOT_VERIFIED`, disclose the observability gap in parent status, and install a bounded watcher when the environment supports one. Never leave a preview, review result, failure, supersede event, or final acceptance gate in a silent passive wait.

## Review and human-gate routing

Review is an agent lane by default when an eligible independent profile exists:

| Review claim | Default lane | Human involvement |
|---|---|---|
| code quality or implementation correctness | `agent-review` or verified domain reviewer | not required for routine findings/remediation |
| architecture boundary | `agent-architecture` | only for an unresolved authority decision |
| product-fit and acceptance evidence | `agent-product` | product owner/user only when policy reserves final acceptance |
| design acceptance | `agent-design` or verified design reviewer | only when product-owner acceptance is reserved |
| security or operations | verified security/operations reviewer | privileged deploy or risk acceptance remains human-authorized when policy requires |

An agent reviewer returns PASS, NEEDS_WORK, BLOCKED, LIMITED, or NOT_VERIFIED with evidence. NEEDS_WORK creates or reuses remediation dependencies; it does not become a chat interruption. Use a human-blocking gate only when its type, required authority, missing decision, and exact unblock condition are explicit.

Reviewer lanes normalize their verdict into this canonical progression contract:

| Verdict | Meaning | Required routing |
|---|---|---|
| `PASS_FOR_NEXT_LANE` | The latest non-superseded handoff evidence satisfies the lane review scope. | Complete the review lane and promote the next known lane or synthesis dependency. |
| `NEEDS_SPECIALIST_REMEDIATION` | A blocking, in-scope finding maps to acceptance criteria, policy, regression, security, accessibility, architecture, or explicit requirements. | Create/reuse a bounded remediation lane owned by the responsible specialist and a re-review lane targeting the remediation evidence. |
| `BLOCKED_AUTHORITY` | The reviewer cannot decide because a named human/product/merge/deploy/risk authority is required. | Block with authority type, exact missing decision, and evidence packet. |
| `FAILED_REVIEW_PROTOCOL` | The reviewed evidence is missing, stale, dirty, unauthenticated, or not reviewable. | Route to orchestrator remediation/triage; do not PASS or promote downstream lanes. |

Legacy labels such as `APPROVED`, `REQUEST_CHANGES`, or prose “review required” may be reported as human-readable aliases, but the durable handoff/verdict must include one canonical verdict above for downstream automation.

## Board lifecycle gates

Stages are evidence gates, not labels that may be skipped by moving a card.

### Plan

Required:

- outcome, scope, source, acceptance criteria, board, and authority are attributable;
- `routing:` is complete;
- exactly one primary workflow and one parent owner are explicit;
- dependencies and expected evidence are mapped.

Exit: `PLAN_READY`. Missing routing or acceptance basis yields `BLOCKED` or `NOT_VERIFIED`.

### Sample

Use only when a reversible example, spike, prototype, or feasibility proof reduces a named uncertainty.

Required:

- hypothesis or decision question;
- bounded sample scope and disposal/promotion rule;
- observable result and limitations.

Exit: `SAMPLE_EVIDENCE_READY`. A sample is never feature completion and must not be relabeled as production build evidence.

### Decision

Required when direction, scope, architecture, design, cost, risk, or build authority must be approved.

Required:

- decision, rationale, evidence refs, authority, rejected alternatives, and consequences;
- explicit outcome: `APPROVED`, `REVISE`, `REJECTED`, or `NOT_VERIFIED`.

Only `APPROVED`, or a policy-backed no-approval-needed decision, can unlock Build.

### Build

The selected lower-level workflow owns implementation. This facade only checks that:

- build authority and repository/runtime context are verified;
- child work is assigned to real profiles;
- workspaces, dependencies, acceptance refs, and expected artifacts are explicit.

Exit: implementation artifacts exist. Existence alone does not prove correctness.

### Verify

Required evidence depends on the claim and may include tests, lint/build results, runtime output, rendered evidence, security checks, deployment receipts, or document consistency checks.

Exit: each acceptance criterion has attributable evidence or an explicit non-pass status. Green CI alone does not prove product acceptance.

### Accept

Required:

- owner or user/product authority evaluates the requested outcome against acceptance criteria;
- reviewer findings and unresolved risks are resolved, accepted by authority, or remain blocking;
- sample evidence is not substituted for shipped behavior.

Exit: `ACCEPTED`, `REJECTED`, `NEEDS_WORK`, or `NOT_VERIFIED` with an authority reference.

### Done

The orchestrator synthesizes the parent only after the Done gate below passes. Moving a card to Done does not create evidence. The parent remains not-Done while any required child, reviewer, acceptance lane, or synthesis obligation is open; an implementation lane cannot close the outcome by itself.

For a project or epic, evaluate the requested end-to-end chain in this order and mark inapplicable lanes explicitly rather than silently skipping them:

```text
Plan / scope / acceptance criteria
→ Design or Product direction when applicable
→ Engineering implementation
→ Test / source validation
→ Verify with runtime, rendered, or other claim-appropriate evidence
→ Independent technical and product review when applicable
→ Product-owner acceptance
→ merge to main and/or production deployment only when required, explicitly authorized, and evidenced by execution receipts
→ external tracker sync only when requested, after internal delivery completion, and separately approved
→ orchestrator synthesis
```

If merge or deployment is required by the accepted parent DoD but authorization or execution evidence is missing, the parent remains open with `READY_FOR_ACCEPTANCE_OR_RELEASE`; it is not `DONE` and does not imply authority. If merge/deploy is explicitly out of scope, record `NOT_REQUIRED` with the governing scope reference and do not invent a release lane. When external sync is part of the requested parent outcome, internal delivery must pass first, then the approved sync lane must execute before final parent `DONE`; otherwise external sync remains a separately gated post-Done action.

## Evidence-backed parent Done gate

A parent may be marked Done only when all are true:

```text
□ routing block is complete and reflects the executed route
□ assignment and executable readiness were recorded separately; no lane ran merely because it had an assignee
□ every repository-mutating lane used a verified non-default branch/worktree topology and reports workspace evidence
□ every required child is Done or explicitly cancelled with rationale and authority
□ every child traces to a parent acceptance criterion
□ acceptance matrix maps each criterion to observable evidence and verdict
□ required role outputs and independent review verdicts are present
□ verification reflects the actual artifact/runtime/document claim
□ unresolved risks are absent or explicitly accepted by authorized ownership
□ required product/user acceptance is recorded
□ every child completion has a structured lane-local handoff with result, evidence, acceptance mapping, risks/blockers, and next known lane
□ merge/deploy requirements are explicit; every required release lane has authorization and execution receipts, or the parent remains READY_FOR_ACCEPTANCE_OR_RELEASE
□ parent orchestrator synthesis records outcome, evidence, limitations, and next state
□ the canonical dependency graph is cycle-free, reconciled, and free of duplicate active pipelines
□ overlap, scope-change, cancellation, and supersede decisions preserve one canonical mutation owner and attributable provenance
□ automatic progression evidence identifies the gateway dispatcher or records manual mode honestly
□ human-gate or terminal notifications include the evidence packet and an attributable delivery receipt or explicit observability limitation
□ external tracker sync is NOT_REQUESTED/NOT_REQUIRED, or an in-scope sync is separately approved, EXECUTED, and backed by an attributable evidence receipt
```

Allowed parent verdicts:

```text
DONE
READY_FOR_ACCEPTANCE_OR_RELEASE
NEEDS_WORK
BLOCKED
REJECTED
NOT_VERIFIED
```

`DONE` is unavailable when required evidence, review, acceptance, release execution, or an in-scope sync's approval, execution, or receipt is missing. `READY_FOR_ACCEPTANCE_OR_RELEASE` means all currently authorized internal work is verified but one or more required authority-gated acceptance, merge, deploy, or sync actions remain; it is a non-Done readiness verdict. A separately approved external sync may occur after internal delivery is Done; when it belongs to the requested parent outcome, its `EXECUTED` status and evidence receipt are required before final parent `DONE`. Sync completion is not evidence that the product outcome passed.

## Output contract

```yaml
task_management_result:
  board_ref: string
  parent_card_ref: string
  card_identity:
    kind: epic | subtask | single_task
    parent_task_id: string | null
    lane_role: plan | design | engineering | test | verify | review | product_acceptance | release | sync | null
    title_prefix: string
    visible_title: string
    pipeline_key: string
    lane_identity: string | null
    idempotency_key: string
  routing: {}
  readiness_gate:
    status: READY | NEEDS_PLANNING | NEEDS_DISCOVERY | NEEDS_DECISION | BLOCKED | NOT_VERIFIED
    mutation_allowed: boolean
    evidence_refs: []
  repository_work_gate:
    mutation_intended: boolean
    base_branch: string | null
    working_branch: string | null
    pr_target: string | null
    workspace_kind: worktree | branch | dir_readonly | scratch | null
    direct_main_checkout_mutation_allowed: false
    evidence_refs: []
  hierarchy:
    kind: epic | subtask | single_task
    parent_task_id: string | null
    parent_external_ref: string | null
    owns_overall_dod: boolean
    requires_decomposition: boolean
    lane_role: plan | design | engineering | test | verify | review | product_acceptance | release | sync | null
    terminal_state_policy:
      done_requires: full_delivery_chain | lane_local_dod | single_task_dod
  status_summary:
    current_lane: string | null
    current_assignee: string | null
    current_state: running | dependency_wait | agent_review_running | human_gate | release_authorization_gate | external_sync_gate | completed | failed | not_verified
    last_completed_lane: string | null
    next_lane: string | null
    blocked_reason: string | null
    required_human_gate: string | null
    verification_evidence_refs: []
    updated_at_ref: string
  child_refs: []
  pipeline:
    key: string
    graph_revision: integer
    reconciliation: REUSED | CREATED | REPAIRED | SUPERSEDED | NOT_VERIFIED
    dispatcher_mode: GATEWAY_DISPATCHER | MANUAL_DISPATCH | NOT_VERIFIED
    dispatcher_evidence_ref: string | null
    lane_keys: []
  lane_handoffs: []
  reviewer_verdicts:
    - lane_ref: string
      verdict: PASS_FOR_NEXT_LANE | NEEDS_SPECIALIST_REMEDIATION | BLOCKED_AUTHORITY | FAILED_REVIEW_PROTOCOL
      reviewed_handoff_ref: string
      reviewed_commit: string | null
      remediation_ref: string | null
      re_review_ref: string | null
  lane_timeline:
    - lane_ref: string
      assignee: string
      operational_status: DONE | NEEDS_WORK | BLOCKED | REVIEW_REQUIRED_AGENT | AWAITING_HUMAN_AUTHORITY | FAILED
      started_at_ref: string | null
      completed_at_ref: string | null
      evidence_refs: []
      recovery_refs: []
  lifecycle_stage: plan | sample | decision | build | verify | accept | done
  acceptance_matrix:
    - criterion_ref: string
      evidence_refs: []
      verdict: PASS | FAIL | PARTIAL | NOT_VERIFIED
  role_evidence: []
  unresolved_risks: []
  acceptance:
    verdict: ACCEPTED | REJECTED | NEEDS_WORK | NOT_VERIFIED
    authority_ref: string | null
  release:
    merge_status: NOT_REQUIRED | AWAITING_AUTHORIZATION | AUTHORIZED | EXECUTED | BLOCKED | NOT_VERIFIED
    deploy_status: NOT_REQUIRED | AWAITING_AUTHORIZATION | AUTHORIZED | EXECUTED | BLOCKED | NOT_VERIFIED
    authorization_refs: []
    execution_receipt_refs: []
  internal_delivery_verdict: DONE | READY_FOR_ACCEPTANCE_OR_RELEASE | NEEDS_WORK | BLOCKED | REJECTED | NOT_VERIFIED
  parent_verdict: DONE | READY_FOR_ACCEPTANCE_OR_RELEASE | NEEDS_WORK | BLOCKED | REJECTED | NOT_VERIFIED
  human_gates: []
  lifecycle_control:
    canonical_ref: string
    overlap_verdict: REUSED | CONSOLIDATED | SEPARATE | SUPERSEDED | BLOCKED | NOT_VERIFIED
    scope_change: NONE | CLARIFICATION | BOUNDED_REMEDIATION | MATERIAL_CHANGE | SCOPE_CREEP | NOT_VERIFIED
    cancellation_or_supersede_refs: []
    follow_up_refs: []
  notification_evidence_packet: {}
  external_sync:
    status: NOT_REQUESTED | AWAITING_APPROVAL | APPROVED | EXECUTED | BLOCKED | NOT_VERIFIED
    evidence_ref: string | null
  next_exact_action: string | null
```

## Anti-patterns and hard stops

- Do not use an assistant-local todo list as durable project execution state.
- Do not create visually ambiguous Kanban cards; every card title and metadata must identify `[EPIC]`, `[SUBTASK][parent][lane]`, or `[TASK]` before dispatch.
- Do not dispatch before board identity, routing, and assignee existence are verified.
- Do not equate assignment with readiness or place intake work in executable `ready`; use `triage` or `blocked` until all gates pass.
- Do not mutate a repository before verifying explicit base, working branch, PR target, and workspace evidence; never edit directly on the main/default checkout.
- Do not dispatch before hierarchy is explicit or silently classify ambiguous work as `single_task`.
- Do not assign a cross-domain parent directly to one specialist and lose synthesis ownership.
- Do not flatten owner, specialist, and reviewer into one role list.
- Do not let an implementer self-certify independent review when independence is required.
- Do not mark a sample, mock, screenshot, prototype, plan, PR, or green CI run as feature Done.
- Do not mark a parent Done because child implementation finished while acceptance is missing.
- Do not let a lane finish with only prose such as “review required”; preserve its result, artifacts/evidence, acceptance mapping, risks, blockers, and exact next lane.
- Do not leave a repository-mutating implementation lane blocked as `review-required` after it has valid lane-local evidence and a known reviewer lane; complete the lane-local handoff and promote review.
- Do not claim a workflow is permanent or fleet-ready from local board repair alone; update the ai-native-skills skill/contract/profile distribution surfaces or report `NOT_PORTABLE`.
- Do not declare an epic Done while a required but unauthorized or unexecuted merge/deploy lane remains; use `READY_FOR_ACCEPTANCE_OR_RELEASE`.
- Do not ask the user to manually advance routine lanes that can progress through dependency completion and the dispatcher.
- Do not make the user manually poll chat to learn whether work is active, waiting, failed, or authority-gated; maintain the compact parent status summary and final lane timeline.
- Do not leave crashes, timeouts, stale workers, protocol violations, duplicate graphs, or missing handoffs looking `running`; route them to orchestrator remediation with evidence and an exact next action.
- Do not turn generic `review-required` into a human block when a verified agent reviewer can produce the verdict.
- Do not run the deprecated standalone daemon beside the gateway dispatcher or mistake `watch` for dispatch.
- Do not retry decomposition by cloning the pipeline; derive and pass a deterministic per-lane `idempotency_key`, reuse returned task IDs, and reconcile the canonical graph and its stable keys.
- Do not run overlapping mutation owners, absorb scope creep, call cancellation Done, or reopen completed evidence; reconcile, revise, supersede, or create a freshly gated follow-up.
- Do not model the user as an internal lane or leave previews and authority gates silently waiting; complete agent review/remediation first and send an evidence-backed notification with an exact decision or next action.
- Do not copy lower-level product, bugfix, review, deployment, or testing procedures into this facade; load and execute the owning skill.
- Do not create GitHub, Jira, Linear, or other tracker artifacts without a separate explicit sync request and target approval.
- Do not treat external sync, merge, release, or deployment as self-authorized by board completion.

Return `BLOCKED` or `NOT_VERIFIED` rather than guessing when board selection, routing, assignee inventory, authority, required evidence, acceptance, or external-sync approval is unresolved.
