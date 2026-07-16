---
name: workflow-router
description: Detect task type from user request and route to the correct workflow automatically — bug vs feature vs review vs deploy vs spike. Explicit routing before execution. Meta-skill that composes workflow skills.
version: 1.0.0
author: puterakahfi
license: MIT
type: meta-skill
implements: ai-native-core/contracts/skills/domain-architecture/workflow-router.contract.yaml
related_skills: [role-switcher, bugfix-workflow, new-feature-workflow, code-review-workflow, deployment-workflow, spec-workflow]
---

# Workflow Router

## The Core Rule

```
Without workflow-router:
  User: "fix this bug"
  Agent: starts coding immediately — no process, no gates

With workflow-router:
  User: "fix this bug"
  Agent: classifies → bugfix-workflow → loads systematic-debugging → follows gates
```

No execution before routing. Routing must be stated explicitly.

---

## Task Classification

### Signal Map

| Signals | Workflow | Skills Loaded |
|---|---|---|
| "fix bug", "error", "broken", "crash", "not working", "TICKET-ID" | `bugfix-workflow` | systematic-debugging, architecture-review, git-workflow |
| "add feature", "implement", "build", "new endpoint", "TICKET-ID (feat)" | `new-feature-workflow` | spec-workflow, plan, master-engineer, tdd |
| "review PR", "review code", "check this", "before merge" | `code-review-workflow` | architecture-review, design-review, security-review |
| "deploy", "release", "ship to", "go to prod" | `deployment-workflow` | security-review, architecture-review |
| "audit design", "UX review", "what's wrong with this UI" | `role-switcher` → design roles | master-design, ux-psychology, product-manager, design-review |
| "refactor", "clean up", "technical debt" | `refactoring` + `bugfix-workflow` | refactoring, systematic-debugging |
| "try this idea", "explore", "validate", "spike" | `spike` | spike, plan |
| "plan this", "break down", "estimate" | `spec-workflow` | spec-workflow, product-manager, plan |
| "design service", "microservice boundary", "how to split" | `service-design` | service-design, domain-driven-design, adr |

---

## Routing Output Format

Always state routing before acting:

```
Workflow Router
───────────────
Request: "Fix the login bug where users get logged out after 5 minutes"
Classification: BUG FIX
Confidence: HIGH — "fix", "bug", explicit symptom

Workflow: bugfix-workflow
Loading skills: systematic-debugging, architecture-review, git-workflow

Starting Phase 1: Reproduce
```

---

## Ambiguity Resolution

When signals are mixed, clarify — do not assume:

```
Request: "Update the user profile page"

Ambiguous — could be:
  A) Bug fix — "update" meaning "fix broken update"
  B) Feature — "update" meaning "add new fields to profile page"

Routing Router
───────────────
Request: "Update the user profile page"
Classification: AMBIGUOUS

Is this:
  [A] Bug fix — profile update is broken/incorrect
  [B] New feature — add new capability to profile page
```

### Auto-resolve when context is clear:

```
Request: "Users are reporting their profile photos aren't saving"
→ AUTO: bugfix-workflow — symptom is clearly a bug, no clarification needed

Request: "Add profile photo upload to the user profile page"
→ AUTO: new-feature-workflow — "add" + new capability, clearly a feature
```

---

## Routing Decision Tree

```
Request received
    ↓
Contains Jira/ticket ID?
    ├─ YES → read ticket type (Bug/Task/Story) → route accordingly
    └─ NO → continue
    ↓
Contains symptom words? (error, crash, broken, not working, 500, null, undefined)
    ├─ YES → bugfix-workflow
    └─ NO → continue
    ↓
Contains build words? (add, implement, build, create, new)
    ├─ YES → new-feature-workflow (check: needs spec? → spec-workflow first)
    └─ NO → continue
    ↓
Contains review words? (review, check, before merge, PR, audit)
    ├─ YES → code-review-workflow OR role-switcher (design audit)
    └─ NO → continue
    ↓
Contains deploy words? (deploy, release, ship, prod, staging)
    ├─ YES → deployment-workflow
    └─ NO → continue
    ↓
Contains explore words? (try, spike, explore, validate idea, experiment)
    ├─ YES → spike
    └─ NO → continue
    ↓
Contains refactor words? (refactor, clean, debt, extract, restructure)
    ├─ YES → refactoring skill
    └─ NO → FALLBACK → clarify with user
```

---

## Fallback

When no workflow matches:

```
Workflow Router
───────────────
Request: "Can you help me with the project?"
Classification: UNCLEAR — insufficient signals

I need more context to route correctly:
  [A] Fix a bug
  [B] Build a new feature
  [C] Review code before merge
  [D] Plan / break down a task
  [E] Something else → describe
```

---

## Composed With role-switcher

`workflow-router` handles process routing (which workflow).
`role-switcher` handles role routing (which skills/lenses).

They compose:

```
Request: "Audit this checkout design before we ship"

workflow-router: review + design + before ship → code-review-workflow
role-switcher:   design audit → master-design + ux-psychology + product-manager

Combined:
  Workflow: code-review-workflow
  Roles: master-design, ux-psychology, product-manager, design-review
  Phases: load-context → design-check → logic-check → verdict
```
