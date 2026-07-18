---
name: workflow-router
description: Detect task type from user request and route to the correct workflow automatically — product-from-zero, UI/UX refinement, bug, feature, review, deploy, spike, or verified-case skill evolution. Explicit routing before execution.
license: MIT
metadata:
  ai-native-skills.version: 1.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.requires: "redesign-workflow new-feature-workflow bugfix-workflow code-review-workflow deployment-workflow product-development-workflow design-refinement skill-evolution skill-eval git-workflow skill-doctor spec-workflow"
  ai-native-skills.type: meta-skill
  ai-native-skills.implements: ai-native-core/contracts/skills/meta/workflow-router.contract.yaml
  ai-native-skills.contract-version: "~0.2"
  ai-native-skills.related_skills: '["role-switcher","product-development-workflow","redesign-workflow","design-refinement","skill-evolution","bugfix-workflow","new-feature-workflow","code-review-workflow","deployment-workflow","spec-workflow"]'
---

# Workflow Router

## Core rule

```text
Without workflow-router:
  User: "fix this bug"
  Agent: starts coding immediately — no process, no gates.

With workflow-router:
  User: "fix this bug"
  Agent: classifies → bugfix-workflow → loads systematic-debugging → follows gates.
```

No execution before routing. Routing must be stated explicitly.

Parent workflows may invoke `skill-evolution` automatically after a real fix passes verification. That post-fix invocation does not require a separate user request.

---

## Task classification

### Signal map

| Signals | Workflow | Skills loaded |
|---|---|---|
| "build product from zero", "develop product idea", "MVP from scratch", "idea to launch", "no PRD yet" | `product-development-workflow` | product-development-workflow, product-requirements, user-research, model-selection |
| "refine UI", "redesign", "polish", "landing page", "dashboard UX", "improve hierarchy", "CRO", "visual audit", "UX review" | `redesign-workflow` | redesign-workflow, master-design, design-review, content-strategy, cro |
| "fix gate G21", "failing design gates", "preserve direction", "specific design issue", "targeted UI fix" | `design-refinement` | design-refinement, design-audit, design-review, master-design |
| "learn from this fix", "update the skill from this case", "promote this lesson", "self-improve the skill", "generalize this solution", "add regression learning" | `skill-evolution` | skill-evolution, skill-eval, git-workflow |
| "fix bug", "error", "broken", "crash", "not working", "TICKET-ID" | `bugfix-workflow` | systematic-debugging, architecture-review, git-workflow |
| "add feature", "implement", "build endpoint", "new endpoint", "TICKET-ID (feat)" | `new-feature-workflow` | spec-workflow, plan, master-engineer, tdd |
| "review PR", "review code", "check this", "before merge" | `code-review-workflow` | architecture-review, design-review, security-review |
| "deploy", "release", "ship to", "go to prod" | `deployment-workflow` | security-review, architecture-review |
| "audit design", "UX review", "what's wrong with this UI" | `redesign-workflow` for existing surface, otherwise `role-switcher` → design roles | redesign-workflow, master-design, ux-psychology, product-manager, design-review |
| "refactor", "clean up", "technical debt" | `refactoring` + `bugfix-workflow` | refactoring, systematic-debugging |
| "try this idea", "explore", "validate", "spike" | `spike` | spike, plan |
| "plan this", "break down", "estimate" | `spec-workflow` | spec-workflow, product-manager, plan |
| "design service", "microservice boundary", "how to split" | `service-design` | service-design, domain-driven-design, adr |

### Automatic post-fix route

When another workflow has:

```text
observed real failure
+ applied fix
+ successful verification
+ regression evidence
```

it must route internally to:

```text
skill-evolution
→ skill-eval
→ git-workflow when a shared patch is promotable and writable.
```

This route occurs before final delivery. The parent workflow resumes delivery after the learning verdict is recorded.

---

## Routing output format

Always state routing before acting:

```text
Workflow Router
────────────────────────────────────
Request: "Fix the login bug where users get logged out after 5 minutes"
Classification: BUG FIX
Confidence: HIGH — "fix", "bug", explicit symptom

Workflow: bugfix-workflow
Loading skills: systematic-debugging, architecture-review, git-workflow

Starting Phase 1: Reproduce
```

For explicit learning promotion:

```text
Workflow Router
────────────────────────────────────
Request: "We verified this real fix. Generalize the reason and update the skill."
Classification: VERIFIED-CASE SKILL EVOLUTION
Confidence: HIGH

Workflow: skill-evolution
Loading skills: skill-evolution, skill-eval, git-workflow

Starting Phase 1: Observe
```

---

## Ambiguity resolution

Clarify only when the route materially changes and context is insufficient.

```text
Request: "Update the user profile page"

Ambiguous — could be:
  A) Bug fix — profile update is broken.
  B) Feature — add new profile capability.

Workflow Router
────────────────────────────────────
Classification: AMBIGUOUS

Is this:
  [A] Bug fix
  [B] New feature
```

### Auto-resolve when context is clear

```text
"Users report profile photos are not saving"
→ bugfix-workflow

"Add profile photo upload"
→ new-feature-workflow

"The fix now passes; extract reusable reasoning and update the governing skill"
→ skill-evolution
```

Do not ask whether learning promotion is desired when a parent workflow already requires automatic post-fix learning review. Repository write approval remains governed separately.

---

## Routing decision tree

```text
Request received
    ↓
Explicit verified-case learning signals?
(learn from fix, update skill from case, promote lesson, generalize solution)
    ├─ YES → skill-evolution
    └─ NO → continue
    ↓
Contains Jira/ticket ID?
    ├─ YES → read ticket type → route accordingly
    └─ NO → continue
    ↓
Contains symptom words?
(error, crash, broken, not working, 500, null, undefined)
    ├─ YES → bugfix-workflow
    └─ NO → continue
    ↓
Contains product-from-zero words?
(idea, MVP, digital product, from zero, no PRD, launch)
    ├─ YES → product-development-workflow
    └─ NO → continue
    ↓
Contains targeted design-fix words?
(fix gate, failing design gates, preserve direction, specific design issue)
    ├─ YES → design-refinement
    └─ NO → continue
    ↓
Contains UI/UX refinement words?
(refine, redesign, polish, landing page, dashboard, UX, hierarchy, CTA, CRO)
    ├─ YES → redesign-workflow
    └─ NO → continue
    ↓
Contains build words?
(add, implement, build endpoint, create feature, new endpoint)
    ├─ YES → new-feature-workflow; run spec-workflow first when needed
    └─ NO → continue
    ↓
Contains review words?
(review, check, before merge, PR, audit)
    ├─ YES → code-review-workflow or role-switcher for design audit
    └─ NO → continue
    ↓
Contains deploy words?
(deploy, release, ship, prod, staging)
    ├─ YES → deployment-workflow
    └─ NO → continue
    ↓
Contains explore words?
(try, spike, explore, validate idea, experiment)
    ├─ YES → spike
    └─ NO → continue
    ↓
Contains refactor words?
(refactor, clean, debt, extract, restructure)
    ├─ YES → refactoring
    └─ NO → clarify
```

---

## Fallback

```text
Workflow Router
────────────────────────────────────
Request: "Can you help me with the project?"
Classification: UNCLEAR — insufficient signals

Choose the intended outcome:
  [A] Fix a bug
  [B] Build a feature
  [C] Review before merge
  [D] Plan or break down work
  [E] Improve an existing UI/UX surface
  [F] Promote learning from a verified fix
```

---

## Composition with role-switcher

`workflow-router` selects the process. `role-switcher` selects owner, specialists, and reviewers.

```text
Request: "Audit this checkout design before we ship"

workflow-router:
  existing visual surface → redesign-workflow

role-switcher:
  owner      → master-design
  specialists→ relevant design skills
  reviewer   → design-review

After a verified fix:
  workflow-router → skill-evolution
  reviewer        → skill-eval
```

The final output remains one synthesized workflow result, including the learning-promotion verdict when fixes occurred.
