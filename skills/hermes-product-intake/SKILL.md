---
name: hermes-product-intake
description: "Hermes adapter for product-intake. Use when agent-orchestrator receives a feature request, bug report, or change request and must run investigation, create Jira/GitHub/Kanban items, and enforce the intake gate before routing to engineering. Wraps product-intake with Hermes-specific execution: Jira MCP detection, Kanban fallback, and engineering handoff format."
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.runtime: hermes
  ai-native-skills.fleet: native-ai-engineering
  ai-native-skills.requires: "product-intake product-requirements delivery-work-breakdown jira-issue-query"
  ai-native-skills.related_skills: '["product-intake","workflow-router","hermes-auto-routing-planner","jira-issue-query","task-continuity","delivery-work-breakdown"]'
  ai-native-skills.boundary.covers: '["jira_config_detection","jira_epic_story_task_creation","github_issue_creation","hermes_kanban_fallback","intake_gate_enforcement","engineering_handoff_emission"]'
  ai-native-skills.boundary.delegates: '["investigation_logic","prd_depth_determination","task_sizing","prd_authoring","delivery_decomposition","engineering_execution"]'
---

# Hermes Product Intake

Hermes-specific execution adapter for `product-intake`. Runs investigation via `product-intake`, then executes artifact creation in the correct target (Jira, GitHub, or Hermes Kanban), and enforces the gate before emitting the engineering handoff.

## Composition boundary

```text
product-intake          owns investigation, PRD depth logic, task sizing, intake_artifacts contract
hermes-product-intake   owns execution: config detection, tracker item creation, gate enforcement, handoff
workflow-router         owns engineering routing — only permitted after gate passes
```

This skill does not re-implement investigation logic. It consumes `intake_artifacts` from `product-intake` and executes the Hermes-specific steps.

## Load order

```text
1. product-intake       → run investigation, produce intake_artifacts
2. hermes-product-intake → detect target, create items, enforce gate, emit handoff
```

## Step 1 — Verify intake_artifacts from product-intake

Require all fields before proceeding:

```yaml
intake_artifacts:
  gate:
    investigation_complete: true
    prd_artifact_exists: true
    tasks_created: false          # this skill will set to true
    engineering_routing_allowed: false  # this skill will set to true on success
```

If `investigation_complete: false` or `prd_artifact_exists: false` → **BLOCKED**. Do not proceed to tracker creation.

## Step 2 — Detect artifact target

Check in order:

### 2a. Jira detection

Jira is available when ALL of:
- Jira MCP tools are reachable (`mcp__atlassian_mcp_server__getVisibleJiraProjects` responds)
- Project has a Jira project key in config or user confirms

```text
Jira reachable + project key known → target: jira
Jira reachable + project key unknown → ask user for project key
Jira not reachable → skip to 2b
```

### 2b. GitHub detection

GitHub is available when:
- `gh auth status` succeeds
- Project has a GitHub repo (check `git remote get-url origin`)

```text
gh auth ok + repo known → target: github
```

### 2c. Hermes Kanban fallback

If neither Jira nor GitHub available:
```text
target: kanban  (hermes kanban create-task)
```

### 2d. Markdown fallback

If Kanban unavailable or not configured:
```text
target: markdown  (structured task list in response)
```

Never assume Jira. Always detect.

## Step 3 — Create tracker items

Based on `intake_artifacts.tasks.structure` and detected target:

### Epic structure (multi-component)

**Jira:**
```text
1. Create Epic: title = request summary, description = PRD brief, labels = intake
2. Create Story/Task per component with epic link
3. Set depends_on links where applicable
```

Use `mcp__atlassian_mcp_server__createJiraIssue` for each item.

**GitHub:**
```text
1. Create milestone or Epic issue (labeled 'epic')
2. Create child issues per component, reference parent in body
3. Set depends_on in body ("Depends on #N")
```

Use `gh issue create` for each item.

**Kanban:**
```text
hermes kanban create-task --title "<epic title>" --body "<prd brief>"
hermes kanban create-task --title "<component task>" --parent <epic-id>
```

### Single task / hotfix structure

**Jira:**
```text
Create one Task/Bug issue with acceptance criteria in description
```

**GitHub:**
```text
gh issue create --title "<title>" --body "<problem + acceptance criteria>"
```

**Kanban / Markdown:**
```text
Single task entry with problem statement and acceptance criteria
```

### Record created items

After creation, record all item IDs/URLs in `execution_artifacts`.

## Step 4 — Enforce gate

After tracker items are created, update gate:

```yaml
intake_gate_result:
  investigation_complete: true
  prd_artifact_exists: true
  tasks_created: true
  artifact_target: jira | github | kanban | markdown
  created_items: []    # list of IDs or URLs
  engineering_routing_allowed: true
```

If tracker creation fails for any item → `engineering_routing_allowed: false`, state blocker explicitly.

## Step 5 — Emit engineering handoff

When gate passes, emit:

```yaml
engineering_handoff:
  schema_version: "1.0"
  request_summary: "<from intake_artifacts>"
  problem_statement: "<verified>"
  affected_components: []
  risk_level: LOW | MEDIUM | HIGH
  prd:
    depth: minimal_brief | partial_prd | full_prd
    artifact_ref: "<inline or link>"
  tasks:
    structure: hotfix | single_task | multi_task | epic
    artifact_target: jira | github | kanban | markdown
    items: []           # titles + IDs/URLs
    epic_ref: "<ID or null>"
  routing_permitted: true
  next_workflow: "<workflow-router selection>"
  open_ambiguities: []  # must be empty for routing_permitted: true
```

This handoff is the input to `workflow-router` for engineering routing.

## Step 6 — Route to engineering

Pass `engineering_handoff` to `workflow-router`. Route class is determined by task structure and intake findings:

```text
hotfix / single bug     → bugfix-workflow
single feature task     → new-feature-workflow
multi-task / epic       → new-feature-workflow + delivery-work-breakdown
new product / greenfield → product-development-workflow
```

`workflow-router` selects the exact primary lifecycle. This skill does not override that selection.

## Gate enforcement rules

- `engineering_routing_allowed: false` → `workflow-router` is BLOCKED from engineering routes
- Agent must surface the blocker explicitly and wait — do NOT route silently
- Partial tracker creation (some items failed) → `engineering_routing_allowed: false` until resolved
- Open ambiguities remaining → `engineering_routing_allowed: false`

## Anti-patterns

| Anti-pattern | Consequence |
|---|---|
| Skip Jira detection, assume connected | Silent failure when project not configured |
| Create tracker items before gate passes | Orphan items with no verified scope |
| Route to engineering before handoff emitted | No acceptance criteria in engineering context |
| Create Epic for every request | Overhead on hotfixes |
| Use `target: jira` when gh CLI available but Jira is not | Items created in wrong tracker |
| Skip fallback chain | Fails silently when primary target unavailable |

## Pitfalls

- **Jira MCP not always loaded**: check tool availability before assuming MCP is active. Use `tool_search("jira")` or attempt a lightweight call to verify.
- **gh auth state**: `gh auth status` may fail in Hermes profile sessions if symlink not set. If it fails, fall through to kanban/markdown.
- **Epic link in Jira**: requires Epic issue type to exist in the project. Some Jira projects use different hierarchy (e.g. Initiative → Story). Check `getJiraProjectIssueTypesMetadata` first.
- **Kanban commands**: verify `hermes kanban` is available in the current profile before using it. If not available, use markdown fallback.

## Quality gates

```yaml
quality_gates:
  - intake_artifacts_must_be_complete_before_execution
  - artifact_target_must_be_detected_not_assumed
  - jira_project_key_must_be_known_before_jira_creation
  - all_tracker_items_must_be_created_before_gate_passes
  - engineering_handoff_must_reference_created_item_ids
  - engineering_routing_allowed_false_must_surface_blocker
  - open_ambiguities_must_be_empty_before_routing_permitted
```
