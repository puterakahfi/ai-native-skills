---
name: context-manager
description: Context resolution and validation skill — build context packs for agents before task execution. Ensures agents never execute with missing, stale, or incomplete context.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/context/context-manager.contract.yaml
---

# Context Manager

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
