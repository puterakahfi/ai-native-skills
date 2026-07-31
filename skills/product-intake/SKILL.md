---
name: product-intake
description: "Investigation-first gate before engineering routing. Use when an agent receives a feature request, bug report, or change request and must determine scope, PRD depth, and task structure before any engineering work begins. Never skip to implementation."
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/product/product-intake.contract.yaml
  ai-native-skills.contract-version: "~1.0"
  ai-native-skills.requires: "product-requirements delivery-work-breakdown decision-provenance"
  ai-native-skills.related_skills: '["workflow-router","role-switcher","product-requirements","delivery-work-breakdown","decision-provenance","task-continuity"]'
  ai-native-skills.boundary.covers: '["intake_investigation","prd_depth_determination","task_structure_sizing","multi_component_detection","artifact_target_resolution","intake_artifacts_emission"]'
  ai-native-skills.boundary.delegates: '["prd_authoring","delivery_decomposition","jira_execution","kanban_execution","engineering_routing","implementation"]'
---

# Product Intake

Investigation-first gate that runs **before** `workflow-router` routes to engineering. Findings drive everything — PRD depth, task structure, and artifact target are outputs of investigation, not inputs.

## Core rule

```text
request masuk
  → INVESTIGATE: understand problem, scope, affected components
  → FINDINGS determine:
      PRD depth      → minimal brief | partial PRD | full PRD
      Task structure → hotfix | single task | multi-task | epic
      Artifact target → Jira | local/kanban | markdown
  → CREATE appropriate artifacts
  → THEN emit intake_artifacts
  → THEN route to engineering
```

**Never assume scope. Never produce PRD before findings. Never route to engineering without intake_artifacts.**

## Phase 1: Investigate

Before producing any artifact, establish answers to:

- **Problem**: What is broken or missing? Why does it matter?
- **Scope**: Which components are affected? (UI, backend, security, infra, DB, auth, etc.)
- **Existing state**: Is there prior work, open issues, related decisions, or existing context?
- **Risk**: What breaks if this is wrong? Is it user-facing, security-sensitive, or data-critical?
- **Ambiguity**: What is unclear that would block delivery if assumed?

Sources to consult:
- User input and request
- Codebase exploration (search, read affected files)
- Existing issue tracker (Jira, GitHub)
- Error logs, monitoring, or prior session context
- Related skills: `task-continuity` for prior session context, `decision-provenance` for authority claims

### Investigation completeness gate

Do NOT advance to Phase 2 until:
- [ ] Problem is stated in one sentence (not assumed)
- [ ] Affected components are listed (even if "unknown" for some)
- [ ] Existing related work is checked
- [ ] Risk level is classified: LOW | MEDIUM | HIGH | NOT_VERIFIED

If investigation reveals the request is too vague to scope, **ask for clarification** — do not proceed with assumptions.

## Phase 2: Determine PRD depth

Let findings drive depth. Never apply a fixed template.

| Signal | PRD Depth | Content |
|---|---|---|
| Single component, clear problem, low risk, < 1 day | **Minimal brief** | Problem statement + acceptance criteria + scope boundary |
| 2+ components OR moderate ambiguity OR user-facing | **Partial PRD** | + user journey, non-goals, open questions, component impact |
| Cross-team, regulatory, high risk, new product surface | **Full PRD** | + background, metrics, rollout plan, launch criteria |
| Ambiguous, discovery needed | **Defer** | Route to product-development-workflow Discovery first |

Delegate PRD authoring to `product-requirements` for Partial and Full PRD. Minimal brief may be produced inline.

### PRD depth anti-patterns

- ❌ Full formal PRD for a hotfix → wastes velocity
- ❌ One-liner brief for a multi-component feature → missing acceptance criteria
- ❌ Producing PRD before investigation is complete → assumptions become requirements

## Phase 3: Size and structure tasks

Let component count, dependency depth, and risk drive structure.

| Signal | Task Structure |
|---|---|
| Single component, isolated, < 1 day | **Single task / issue** |
| Single component, > 1 day OR sequential steps | **Multi-task, flat list** |
| 2+ distinct components (e.g. UI + backend + security) | **Epic with child tasks per component** |
| Unknown scope after investigation | Re-investigate; do not guess |

**Multi-component rule**: if the change requires work in 2 or more distinct areas (frontend, backend, security, infra, DB schema, auth, analytics, etc.), classify as Epic. One engineer touching two files is not multi-component — two distinct capability boundaries is.

**Dependency rule**: if task B cannot start until task A is merged/deployed, they must be linked. An epic is required when dependent tasks span components.

Delegate task decomposition and dependency graph to `delivery-work-breakdown`.

### Sizing anti-patterns

- ❌ Creating an Epic for every request → overhead on hotfixes
- ❌ Creating a single task for multi-component work → invisible dependencies, integration failures
- ❌ Sizing before investigation → wrong structure locked in early

## Phase 4: Determine artifact target

Check project configuration before creating any tracker items.

```text
Jira MCP connected (project has jira config) → create Epic/Story/Task in Jira
GitHub issues reachable → create issue/milestone in GitHub
Hermes Kanban available → create task in local Kanban
None / unknown → output as structured markdown task list
```

**Never assume Jira is always the target.** Check first. If unknown, ask the user or inspect project config.

Execution of tracker item creation is **delegated** — this skill emits the intake_artifacts contract; the adapter (e.g. `hermes-product-intake`) handles execution.

## Output contract: intake_artifacts

Emit this before any engineering routing. All fields required unless marked optional.

```yaml
intake_artifacts:
  schema_version: "1.0"
  request_summary: "<one sentence>"
  investigation:
    problem_statement: "<verified, not assumed>"
    affected_components: []        # list: ui | backend | security | infra | db | auth | analytics | other
    existing_related_work: []      # issue IDs, PR links, or "none found"
    risk_level: LOW | MEDIUM | HIGH | NOT_VERIFIED
    ambiguities_resolved: []
    ambiguities_open: []           # must be empty or explicitly deferred before routing
  prd:
    depth: minimal_brief | partial_prd | full_prd | deferred
    status: DRAFT | READY | BLOCKED | DEFERRED
    artifact_ref: "<inline or link>"   # inline for minimal brief, link for partial/full
  tasks:
    structure: hotfix | single_task | multi_task | epic
    artifact_target: jira | github | kanban | markdown
    items: []                      # list of task titles with type and component
    epic_ref: "<issue ID or null>" # required when structure = epic
  gate:
    investigation_complete: true | false
    prd_artifact_exists: true | false
    tasks_created: true | false
    engineering_routing_allowed: true | false  # true only when all above = true
```

`engineering_routing_allowed: false` **blocks** engineering routing in `workflow-router`.

## Gate before engineering

Engineering routing is **BLOCKED** until:

- [ ] `investigation_complete: true` — problem, components, risk verified
- [ ] `prd_artifact_exists: true` — PRD at appropriate depth exists
- [ ] `tasks_created: true` — task structure created in appropriate target
- [ ] `ambiguities_open` is empty or all items are explicitly deferred with owner

If any gate fails, return `engineering_routing_allowed: false` and state the blocker explicitly.

## Composition

```text
product-intake
  → product-requirements    (PRD authoring for partial/full depth)
  → delivery-work-breakdown (task decomposition and dependency graph)
  → decision-provenance     (verify authority claims in scope or requirements)
  → [adapter]               (execution: Jira / GitHub / Kanban creation)
  → workflow-router         (engineering routing, only after gate passes)
```

This skill owns the investigation and gate logic. It does not author full PRDs, execute tracker API calls, or implement code.

## Quality gates

```yaml
quality_gates:
  - investigation_required_before_prd_or_sizing
  - prd_depth_must_be_driven_by_findings_not_template
  - task_structure_must_be_driven_by_component_count_and_dependencies
  - artifact_target_must_be_detected_not_assumed
  - intake_artifacts_required_before_engineering_routing
  - open_ambiguities_must_be_resolved_or_deferred_before_gate_pass
  - multi_component_detection_must_reference_distinct_capability_boundaries
  - do_not_produce_full_prd_for_hotfix
  - do_not_produce_single_task_for_multi_component_work
```

## Anti-patterns

| Anti-pattern | Consequence |
|---|---|
| Skip investigation, assume scope | Wrong components touched, wasted engineering effort |
| Always produce full PRD | Kills velocity on hotfixes and small fixes |
| Always produce single task | Epic-worthy work underestimated, integration failures |
| Assume Jira is always the target | Fails silently when project not configured |
| Route to engineering without intake_artifacts | No acceptance criteria to verify against |
| Treat user's feature name as problem statement | Skips root cause, wrong solution built |
| Size tasks before investigation complete | Wrong structure locked in, rework required |

## Handoffs

```text
weak discovery / vague opportunity
  → product-development-workflow Discovery (do not proceed with intake)

investigation complete, partial/full PRD needed
  → product-requirements (delegate PRD authoring)

investigation complete, task sizing needed
  → delivery-work-breakdown (delegate decomposition and dependency graph)

intake_artifacts gate passed
  → workflow-router (engineering routing permitted)
  → adapter executes tracker item creation (Jira / GitHub / Kanban)

prior session context needed
  → task-continuity
```
