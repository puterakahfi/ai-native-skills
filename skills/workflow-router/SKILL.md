---
name: workflow-router
description: Detect task intent and route to the correct workflow or standalone capability — product-from-zero, design audit, design refinement, redesign, bug, feature, review, deploy, spike, or verified-case skill evolution. Route before execution.
license: MIT
metadata:
  ai-native-skills.version: 1.2.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.requires: "redesign-workflow design-audit design-refinement design-review new-feature-workflow bugfix-workflow code-review-workflow deployment-workflow product-development-workflow skill-evolution skill-eval git-workflow skill-doctor spec-workflow"
  ai-native-skills.type: meta-skill
  ai-native-skills.implements: ai-native-core/contracts/skills/meta/workflow-router.contract.yaml
  ai-native-skills.contract-version: "~0.2"
  ai-native-skills.related_skills: '["role-switcher","product-development-workflow","redesign-workflow","design-audit","design-refinement","design-review","skill-evolution","bugfix-workflow","new-feature-workflow","code-review-workflow","deployment-workflow","spec-workflow"]'
---

# Workflow Router

## Core Rule

```text
classify requested outcome
→ select one primary lifecycle or capability
→ resolve design domain when design is involved
→ load only required skills/reviewers
→ execute
```

No execution before routing. Do not confuse the artifact noun with the requested action: a dashboard can be audited, refined, redesigned, debugged, or extended.

## Route Classes

| Intent | Primary route | Supporting capabilities |
|---|---|---|
| Build a product from zero | `product-development-workflow` | research, requirements, design, engineering |
| Audit/critique an existing design without changing it | `design-audit` | `design-review` facade + applicable domain reviewer |
| Fix known specific design findings while preserving direction | `design-refinement` | prior review, governing reviewer, skill-evolution |
| Change design direction, structure, or multiple layers | `redesign-workflow` | design owner, specialists, design-review facade |
| Fix broken implementation behavior | `bugfix-workflow` | systematic-debugging, relevant reviewers |
| Add a capability to an existing product | `new-feature-workflow` | spec-workflow, product/design/engineering owners |
| Review code or PR before merge | `code-review-workflow` | architecture/security/design reviewers as applicable |
| Deploy or release | `deployment-workflow` | security and architecture checks |
| Plan or specify | `spec-workflow` | product-manager, plan, relevant owners |
| Explore a reversible idea | `spike` | plan, experiment skills |
| Promote a verified lesson | `skill-evolution` | skill-eval, git-workflow |
| Refactor code without new behavior | `refactoring` or appropriate engineering workflow | architecture-review when structural |

## Design Intent Routing

Design requests require two classifications:

```text
1. Requested lifecycle
   audit | refinement | redesign | production | advisory

2. Design domain
   digital-interface | visual-communication | presentation | specialized/other
```

### Audit only

Signals:

```text
audit, critique, review this design, what is wrong, score this,
quality check, evaluate, gap report, before redesign
```

Route:

```text
design-audit
→ design-review facade
→ built-in or external domain reviewer
```

Do not route to `redesign-workflow` merely because the target is an existing UI. Audit ends with findings unless the user also requests production.

### Targeted refinement

Signals:

```text
fix these gates, preserve the direction, specific design issue,
only repair tabs overflow, improve this known problem, re-score after fix
```

Route:

```text
design-refinement
```

Requirements:

```text
known verified findings
accepted direction
sufficient primary-domain reviewer coverage
explicit preservation scope
```

When findings are unknown, run `design-audit` first.

### Redesign

Signals:

```text
redesign, rethink direction, replace layout, change visual language,
restructure page, current approach is wrong, broad multi-layer improvement
```

Route:

```text
redesign-workflow
```

Do not route every request containing “polish” to redesign. A narrow known issue belongs to refinement.

### Advisory design question

Signals:

```text
which component fits, explain hierarchy, should mobile use tabs,
what design principle applies
```

Route through `role-switcher` to the owner and relevant specialists. Load `design-review` only when an artifact must be accepted or scored.

## Design Domain Coverage

After choosing the lifecycle, resolve reviewer coverage:

```text
digital-interface
  design-review built-in interactive strategy

visual-communication
  design-review built-in static strategy

presentation
  design-review built-in presentation strategy

identity, packaging, motion/video, industrial, spatial, fashion,
service-design, or another specialized discipline
  load a declared domain reviewer
  without one: LIMITED REVIEW or route to domain specialist
```

Never represent universal visual gates as complete specialist-domain coverage.

## Signal Map

| User signals | Route |
|---|---|
| “audit this landing page”, “review this dashboard UX”, “what is wrong with this poster?” | `design-audit` |
| “fix G14”, “preserve everything except mobile tabs”, “repair these review findings” | `design-refinement` |
| “redesign this landing page”, “replace the dashboard structure”, “new visual direction” | `redesign-workflow` |
| “review this logo concept” | `design-audit` + identity reviewer; otherwise `LIMITED REVIEW` |
| “fix login bug”, “crash”, “not working”, explicit error | `bugfix-workflow` |
| “add upload feature”, “new endpoint”, “implement capability” | `new-feature-workflow` |
| “review PR”, “review code”, “before merge” | `code-review-workflow` |
| “deploy”, “release”, “ship to production” | `deployment-workflow` |
| “build product from zero”, “MVP from scratch”, “no PRD” | `product-development-workflow` |
| “learn from this verified fix”, “update the skill from this case” | `skill-evolution` |
| “plan”, “break down”, “write spec” | `spec-workflow` |

Symptom words such as error, crash, broken, null, 500, or not working take precedence over visual-polish words when the requested outcome is a functional fix.

## Decision Tree

```text
Request received
  ↓
Verified-case learning explicitly requested or required by parent workflow?
  YES → skill-evolution
  NO  → continue
  ↓
Product from zero / no PRD?
  YES → product-development-workflow
  NO  → continue
  ↓
Functional symptom or regression?
  YES → bugfix-workflow
  NO  → continue
  ↓
Design-related request?
  YES → classify lifecycle:
          audit only?          → design-audit
          known targeted fix?  → design-refinement
          broad direction/structure change? → redesign-workflow
          advisory only?       → role-switcher + relevant design skills
        then resolve design domain and reviewer coverage
  NO  → continue
  ↓
New capability requested?
  YES → new-feature-workflow
  NO  → continue
  ↓
Code/PR acceptance review?
  YES → code-review-workflow
  NO  → continue
  ↓
Deploy/release?
  YES → deployment-workflow
  NO  → continue
  ↓
Plan/spec?
  YES → spec-workflow
  NO  → continue
  ↓
Explore/spike/refactor?
  YES → corresponding capability/workflow
  NO  → clarify only when the route materially changes
```

## Routing Output

State the route before acting:

```text
Workflow Router
────────────────────────────────────
Request: "Audit this mobile checkout before redesigning it"
Classification: DESIGN AUDIT
Design domain: digital-interface
Surface profile: mobile-application
Confidence: HIGH

Primary route: design-audit
Reviewer facade: design-review
Domain reviewer: built-in interactive/mobile strategy
Execution boundary: report only; no redesign or patch
```

For a specialized domain without coverage:

```text
Workflow Router
────────────────────────────────────
Request: "Review whether this logo system is production-ready"
Classification: SPECIALIZED DESIGN AUDIT
Design domain: brand-identity
Coverage: reviewer not available

Primary route: design-audit
Facade verdict ceiling: LIMITED REVIEW
Required next route: brand-identity domain reviewer or specialist
```

## Automatic Post-Fix Learning

When a parent workflow has a real failure, verified fix, and regression evidence, it must internally route before delivery:

```text
skill-evolution
→ skill-eval
→ git-workflow when a shared patch is promotable and writable
```

Do not ask again whether learning promotion is desired when the parent workflow already requires it. Repository write approval remains separate.

## Composition with Role Switcher

`workflow-router` chooses the lifecycle. `role-switcher` assigns owner, specialists, facade reviewer, and domain reviewer.

```text
workflow-router:
  audit-only → design-audit

role-switcher:
  owner: master-design or domain owner
  specialists: only what the target needs
  reviewer facade: design-review
  domain reviewer: built-in or declared specialist reviewer
```

The final result is one synthesized lifecycle output, not disconnected reports.

## Anti-Patterns

| Anti-pattern | Correct behavior |
|---|---|
| “UX review” automatically routes to redesign | Audit-only routes to design-audit |
| Every existing UI improvement routes to redesign | Known narrow failures route to design-refinement |
| Average score chooses the lifecycle | Use intent, direction, root cause, coverage, and hard gates |
| Logo audit uses only UI gates | Load identity reviewer or return LIMITED REVIEW |
| One request executes multiple competing primary workflows | Select one primary route and explicit handoffs |
| Reviewer selection happens before domain classification | Resolve lifecycle and domain first |