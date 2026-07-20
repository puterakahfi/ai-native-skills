---
name: context-manager
description: Context resolution and validation skill — build context packs for agents before task execution. Ensures agents never execute with missing, stale, or incomplete context.
license: MIT
metadata:
  ai-native-skills.version: 1.0.1
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/context/context-manager.contract.yaml
  ai-native-skills.contract-version: "~0.1"
---

# Context Manager

## Reviewed core contract interface

Source: `ai-native-core/contracts/skills/context/context-manager.contract.yaml` · compatible line: `~0.1`

```yaml
required_inputs:
- task_or_workflow_ref
- product_ref
allowed_outputs:
- context_pack
- missing_context_report
- stale_context_flag
- context_validation_verdict
quality_gates:
- context_must_be_resolved_before_agent_handoff
- missing_context_must_be_flagged_not_assumed
- stale_context_must_be_refreshed_before_use
- context_pack_must_include_rules_and_skills
- agent_must_not_execute_with_incomplete_context
- context_source_must_be_traceable
```

Resolve task_or_workflow_ref together with product_ref before handoff. Return a context_pack, missing_context_report, stale_context_flag, and context_validation_verdict. Every included rule, skill, contract, and product fact must retain a traceable source; missing or stale context is reported rather than assumed.

Keep this interface synchronized with the pinned core contract. Exact declarations make ownership reviewable; they do not replace repository, runtime, workflow, review, approval, or product evidence.


## The Core Rule

```
Agents must not execute with missing or stale context.
Assume nothing — resolve everything.
```

## When to Use

- Before handing off a task to an agent
- When onboarding an agent to a new product
- When context feels "off" — agent making wrong assumptions
- Before executing any multi-step workflow
- When building a context pack for a team

---

## 1. Context Resolution

Resolve in this order:

```yaml
context_pack:
  product:
    engineering_contract: products/<product>/engineering-contract.yaml
    design_contract: products/<product>/ui-design-system-contract.yaml
    blueprint: products/<product>/blueprint.md

  rules:
    agents_md: products/<product>/AGENTS.md
    cursorrules: .cursorrules

  skills:
    required: []      # skills the task needs — load before execution
    optional: []

  task:
    ref: ""           # issue/ticket ref
    spec: ""          # feature spec or bug description
    acceptance_criteria: []

  app:
    ref: ""           # app/module within product
    stack: ""         # from engineering contract

  state:
    resolved_at: ""   # timestamp
    stale_after: ""   # staleness policy — product_defined
```

---

## 2. Missing Context Detection

Before handing off to agent, check:

- [ ] Engineering contract exists and is not stale?
- [ ] AGENTS.md exists and is current?
- [ ] Task has acceptance criteria?
- [ ] Required skills identified?
- [ ] Relevant rules loaded?

**Gate:** Flag missing context — never assume defaults silently.

```
MISSING CONTEXT REPORT
──────────────────────
Missing: engineering-contract.yaml → block execution
Missing: acceptance_criteria → request from product-manager skill
Stale:   AGENTS.md (last updated >30d) → flag for review
```

---

## 3. Context Validation

After resolving, validate before handoff:

| Context Item | Validation |
|---|---|
| Engineering contract | File exists + required fields present |
| Rules (AGENTS.md) | File exists + not empty |
| Task spec | Has acceptance criteria |
| Skills | All required skills exist in skills registry |
| Stack info | Matches engineering contract |

**Gate:** Incomplete context = blocked handoff. Not degraded execution.

---

## 4. Context Pack Output

Deliver context pack to agent as structured reference:

```markdown
## Context Pack — <task-ref>

**Product:** <product>
**Task:** <task-ref> — <title>
**Stack:** <from engineering contract>

**Rules:** AGENTS.md loaded
**Skills to load:** [skill-1, skill-2]
**Engineering contract:** <path>

**Acceptance criteria:**
- AC-1: Given..., When..., Then...

**Out of scope:**
- item A

**Resolved at:** <timestamp>
```

---

## Common Anti-Patterns

| Anti-Pattern | Why It Fails |
|---|---|
| Agent executes without loading AGENTS.md | Rules not enforced |
| Assume engineering contract from memory | Stale context causes drift |
| Skip acceptance criteria for "quick tasks" | No definition of done |
| Context pack built once, reused forever | Stale context — check freshness |
| Missing context filled with assumptions | Gate exists to prevent this |
