---
name: role-switcher
description: Intent detection and automatic role composition — reads a user request, detects the task type, and loads the right combination of role skills to respond from multiple expert lenses simultaneously.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.requires: "master-engineer master-design product-manager ux-psychology user-research native-ai-engineer diagram-architect design-review systematic-debugging architecture-review security-review plan"
  ai-native-skills.type: meta-skill
  ai-native-skills.implements: ai-native-core/contracts/skills/domain-architecture/role-switcher.contract.yaml
---

# Role Switcher

## The Core Rule

```
Don't pick one role and guess.
Detect the intent → activate the right roles → respond from all relevant lenses.
State which roles are active at the start of every response.
```

## When to Use

- User request spans multiple domains (design + psychology + product)
- "Audit" or "critique" requests — needs multi-lens analysis
- "What's missing?" — needs multiple expert perspectives
- Ambiguous requests where one role would give a partial answer
- Any time the right answer requires switching hats mid-analysis

---

## Role Map

### Design Domain

| Intent Signals | Roles to Activate |
|---|---|
| audit design, review UI, critique UX, what's wrong with this screen | `master-design` + `ux-psychology` + `design-review` |
| design system, tokens, components, visual consistency | `master-design` + `design-review` |
| user flow, onboarding, retention, habit | `master-design` + `ux-psychology` + `product-manager` |
| accessibility, inclusive design | `master-design` + `ux-psychology` |
| AI slop, template UI, generic design | `design-review` + `master-design` |

### Engineering Domain

| Intent Signals | Roles to Activate |
|---|---|
| review code, PR review, architecture check | `master-engineer` + `architecture-review` |
| bug, error, not working, debugging | `systematic-debugging` + `master-engineer` |
| security, vulnerability, secrets | `security-review` + `master-engineer` |
| system design, scalability, architecture decision | `master-engineer` + `native-ai-engineer` |
| refactor, clean up, simplify | `master-engineer` + `systematic-debugging` |
| diagram, visualize architecture, draw flow | `diagram-architect` + `master-engineer` |
| AI native, runtime boundary, contract, adapter | `native-ai-engineer` + `master-engineer` |

### Research & Product Domain

| Intent Signals | Roles to Activate |
|---|---|
| what's missing, gap analysis, feature audit | `product-manager` + domain-specific roles |
| spec, requirements, acceptance criteria | `product-manager` + `plan` |
| prioritize, backlog, roadmap | `product-manager` |
| user problem, pain point, why does this fail | `product-manager` + `ux-psychology` |
| interview users, research, validate assumption, JTBD | `user-research` + `product-manager` |
| survey, usability test, what do users want | `user-research` + `ux-psychology` |

### Creative & AI Tools

| Intent Signals | Roles to Activate |
|---|---|
| generate image prompt, refine prompt, improve this prompt | `prompt-engineer` |
| why does my image look wrong, fix prompt, bad image output | `prompt-engineer` |
| prompt for [subject], create prompt for [style] | `prompt-engineer` |
| AI image product, image generation feature, token efficiency | `prompt-engineer` + `product-manager` |

### Cross-Domain (Full Stack)

| Intent Signals | Roles to Activate |
|---|---|
| audit everything, full review | `master-engineer` + `master-design` + `ux-psychology` + `product-manager` |
| new feature from scratch | `product-manager` + `master-design` + `master-engineer` |
| why is this failing (product) | `product-manager` + `ux-psychology` + `systematic-debugging` |
| end-to-end: research → design → build | `user-research` + `master-design` + `master-engineer` |

---

## How to Apply

### Step 1: Detect Intent

Read the request. Ask:
- What domain? (design / engineering / product / mixed)
- What action? (audit / build / fix / plan / review)
- What depth? (quick gut check / deep analysis / actionable spec)

### Step 2: State Active Roles

Always declare at the start of a response:

```
Roles active: master-design, ux-psychology, product-manager
```

### Step 3: Apply Each Lens

Structure the response by role lens — not a flat dump:

```
## Product Lens (product-manager)
<findings from product perspective — user problem, scope, metrics>

## Design Lens (master-design)
<findings from design perspective — system, hierarchy, patterns>

## Psychology Lens (ux-psychology)
<findings from psychology perspective — cognitive load, habit, heuristics>

## Synthesis
<cross-lens priority list — what matters most overall>
```

### Step 4: Synthesize

Don't just list findings per role. At the end, synthesize:
- What is the single highest-impact change?
- Are there conflicts between lenses? (design wants X, engineering says Y)
- What order should fixes happen in?

---

## Example: "Audit this design — what's missing?"

**Intent detected:** design audit → multi-lens analysis needed

**Roles activated:** `master-design` + `ux-psychology` + `product-manager` + `design-review`

**Response structure:**
```
Roles active: master-design, ux-psychology, product-manager, design-review

## Product Lens
- Is the user problem clear from the UI?
- Does the primary action match the user's goal?
- What's missing to complete the core user journey?

## Design Lens
- Visual hierarchy — is the primary action obvious?
- Design system compliance — tokens, spacing, components
- Information architecture — grouped by user mental model?

## Psychology Lens
- Cognitive load per screen
- Habit loop — does the flow build a return trigger?
- Heuristic violations — top 3

## AI Slop Check (design-review)
- Generic template patterns?
- Missing brand character?
- Inconsistent visual language?

## Synthesis
P1: <highest impact fix across all lenses>
P2: <next>
P3: <next>
```

---

## Adding Custom Roles

Extend the role map for product-specific roles:

```yaml
# In your product AGENTS.md or context file
role_extensions:
  domain_expert_audit:
    triggers: [audit domain logic, review business rules]
    load: [master-engineer, native-ai-engineer, product-manager]

  content_review:
    triggers: [review copy, audit content, check messaging]
    load: [product-manager, ux-psychology]
```

---

## Anti-Patterns

| Anti-Pattern | Why It Fails |
|---|---|
| Pick one role, answer narrowly | Misses cross-domain issues |
| Activate all roles for every request | Noise — `master-engineer` in a copy review is irrelevant |
| Don't declare active roles | User doesn't know what perspective they're getting |
| Give flat list of findings without lens structure | Cross-domain findings get lost |
| Skip synthesis | User left to prioritize across lenses alone |
