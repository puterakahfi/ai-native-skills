---
name: role-switcher
description: Intent detection and automatic role composition — selects a domain owner, relevant specialists, and reviewers so expert skills collaborate without losing decision ownership.
license: MIT
metadata:
  ai-native-skills.version: 1.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.requires: "master-engineer master-design adaptive-component-design product-manager ux-psychology user-research native-ai-engineer diagram-architect design-review systematic-debugging architecture-review security-review plan"
  ai-native-skills.type: meta-skill
  ai-native-skills.implements: ai-native-core/contracts/skills/meta/role-switcher.contract.yaml
  ai-native-skills.contract-version: "~0.1"
---

# Role Switcher

## Core rule

```text
Do not pick one skill and guess.
Detect intent
→ assign one domain owner
→ load only relevant specialists
→ load a reviewer when evidence or acceptance is required
→ synthesize one decision.
```

Roles are not a flat list. Every composition must distinguish:

- **Owner** — holds final decision responsibility and synthesis.
- **Specialist** — contributes narrow expertise.
- **Reviewer** — independently checks gates and evidence.

A specialist must never silently replace the owner.

## Design ownership rule

For product design, UI, or UX work:

```text
Owner:      master-design
Specialist: adaptive-component-design when cross-device component fitness matters
Reviewer:   design-review for audit, refinement, implementation, or final visual acceptance
```

Therefore:

- A broad UI/UX task must not load `adaptive-component-design` without `master-design`.
- A cross-device component task normally loads `master-design + adaptive-component-design`.
- An audit, implemented patch, refinement, or deliverable normally loads `master-design + adaptive-component-design when relevant + design-review`.
- A narrowly scoped advisory question such as “which component should replace Tabs on mobile?” may load `adaptive-component-design` alone, but it must not make unrelated page-level or visual-direction decisions.

## When to Use

- User request spans multiple domains.
- Audit or critique requests need independent review.
- “What is missing?” requires multiple expert perspectives.
- A specialist capability is needed but an owner must preserve coherent decisions.
- The answer requires switching lenses during analysis.
- A workflow needs deterministic skill composition before execution.

---

## Role Map

### Design Domain

| Intent signals | Owner | Specialists | Reviewer |
|---|---|---|---|
| general product design, UI/UX direction, wireframe, mockup, design decision | `master-design` | Load only relevant design ports or expert skills | `design-review` when rendered or implemented |
| audit design, review UI, critique UX, what is wrong with this screen | `master-design` | `ux-psychology` when behavioral analysis matters | `design-review` |
| design system, tokens, components, visual consistency | `master-design` | relevant design-system and visual skills | `design-review` |
| responsive component choice, mobile vs tablet pattern, Tabs overlap, component does not fit viewport | `master-design` | `adaptive-component-design` | `design-review` for implementation or acceptance |
| user flow, onboarding, retention, habit | `master-design` | `ux-psychology` + `product-manager` as relevant | `design-review` when a visual artifact exists |
| accessibility, inclusive design | `master-design` | accessibility and `ux-psychology` as relevant | `design-review` |
| AI slop, template UI, generic design | `master-design` | relevant visual skills | `design-review` |

### Engineering Domain

| Intent signals | Owner | Specialists | Reviewer |
|---|---|---|---|
| review code, PR review, architecture check | `master-engineer` | relevant architecture skills | `architecture-review` |
| bug, error, not working, debugging | `master-engineer` | `systematic-debugging` | relevant review skill after fix |
| security, vulnerability, secrets | `master-engineer` | security domain skills | `security-review` |
| system design, scalability, architecture decision | `master-engineer` | `native-ai-engineer` when AI-native boundaries matter | `architecture-review` when acceptance is required |
| refactor, clean up, simplify | `master-engineer` | refactoring and debugging skills | `architecture-review` when structural boundaries change |
| diagram, visualize architecture, draw flow | `master-engineer` | `diagram-architect` | architecture reviewer when used as a decision artifact |
| AI native, runtime boundary, contract, adapter | `native-ai-engineer` | `master-engineer` and relevant runtime skills | `architecture-review` |

### Research and Product Domain

| Intent signals | Owner | Specialists | Reviewer |
|---|---|---|---|
| what is missing, gap analysis, feature audit | `product-manager` | domain-specific roles | relevant domain reviewer |
| spec, requirements, acceptance criteria | `product-manager` | `plan` and technical/design owners as needed | relevant review workflow |
| prioritize, backlog, roadmap | `product-manager` | decision and value skills as relevant | none unless approval is requested |
| user problem, pain point, why does this fail | `product-manager` | `ux-psychology` | owner synthesizes |
| interview users, research, validate assumption, JTBD | `user-research` | `product-manager` | research evidence review |
| survey, usability test, what do users want | `user-research` | `ux-psychology` | product owner synthesizes implications |

### Creative and AI Tools

| Intent signals | Owner | Specialists | Reviewer |
|---|---|---|---|
| generate image prompt, refine prompt, improve this prompt | `prompt-engineer` | product or brand skills when relevant | output review when acceptance matters |
| why does my image look wrong, fix prompt, bad image output | `prompt-engineer` | visual/product roles as relevant | rendered-output review |
| prompt for a subject or style | `prompt-engineer` | style or domain skills as relevant | none unless quality acceptance is requested |
| AI image product, image generation feature, token efficiency | `product-manager` | `prompt-engineer` + technical/design owners | relevant product/design review |

### Cross-Domain

| Intent signals | Owner | Specialists | Reviewer |
|---|---|---|---|
| audit everything, full review | `product-manager` or explicitly declared lead | `master-engineer` + `master-design` + relevant experts | domain reviewers |
| new feature from scratch | `product-manager` | `master-design` + `master-engineer` | design and engineering review before acceptance |
| why is this failing as a product | `product-manager` | `ux-psychology` + `systematic-debugging` + domain owner | relevant reviewer |
| end-to-end research → design → build | `product-manager` | `user-research` + `master-design` + `master-engineer` | design and engineering review |

---

## How to Apply

### Step 1: Detect intent

Determine:

- domain: design, engineering, product, research, creative, or mixed;
- action: audit, build, fix, plan, review, decide, or advise;
- depth: narrow advisory, actionable specification, implementation, or acceptance;
- evidence state: idea only, source code, rendered artifact, or production behavior.

### Step 2: Assign composition slots

Declare one owner first, then specialists and reviewers.

```text
Owner: master-design
Specialists: adaptive-component-design
Reviewer: design-review
```

Do not call every loaded skill a “role.” State its responsibility.

### Step 3: Enforce owner presence

Before execution:

```text
□ one owner is explicit
□ every specialist has a narrow reason to be loaded
□ no specialist replaces the owner
□ reviewer is independent from the decision when practical
□ rendered or implemented deliverables have a reviewer
```

For UI/UX tasks specifically:

```text
□ master-design is present as owner
□ adaptive-component-design is loaded when viewport changes component fitness
□ design-review is loaded for audit, refinement, implementation, or final acceptance
```

### Step 4: Apply each lens

Each contributor returns findings within its boundary.

```text
## Design owner — master-design
Defines product outcome, evaluates proposed solutions, and holds final synthesis.

## Cross-device specialist — adaptive-component-design
Selects or substitutes components by task, content, viewport, and input modality.

## Reviewer — design-review
Checks the rendered or implemented result against hard gates and evidence.
```

### Step 5: Synthesize

The owner must produce:

- the single recommended decision;
- rationale tied to user and product outcome;
- specialist evidence;
- rejected alternatives and trade-offs;
- implementation implications;
- reviewer verdict or remaining gaps.

Do not return disconnected role reports without a final owner decision.

---

## Example: Cross-device category navigation

**Request:** “Use Tabs for catalogue categories on every device.”

```text
Intent: product UI decision with cross-device risk

Owner: master-design
Specialist: adaptive-component-design
Reviewer: design-review when implemented
```

Expected behavior:

1. `master-design` extracts the real requirement: fast category switching and visible discovery.
2. `adaptive-component-design` evaluates Tabs, segmented controls, shortcut rails, Select, and sheets per viewport.
3. `master-design` chooses and documents the final substitution strategy.
4. `design-review` verifies overflow, paired chevrons, scroll state, touch targets, keyboard access, and shared selected state.

The request to use Tabs is treated as a proposed solution, not as the product requirement.

## Example: Design audit

**Intent detected:** design audit requiring owner plus independent reviewer.

```text
Owner: master-design
Specialists: ux-psychology when relevant
Reviewer: design-review
```

The final response must include one prioritized synthesis from `master-design`, backed by the review evidence.

---

## Adding Custom Roles

Extend the role map for product-specific domains:

```yaml
# In product AGENTS.md or a context file
role_extensions:
  domain_expert_audit:
    owner: product-manager
    specialists: [master-engineer, native-ai-engineer]
    reviewer: architecture-review

  content_review:
    owner: product-manager
    specialists: [ux-psychology]
    reviewer: design-review
```

---

## Anti-Patterns

| Anti-pattern | Why it fails |
|---|---|
| Load a specialist without an owner for broad work | Narrow expertise starts making unrelated decisions |
| Treat all loaded skills as equal owners | Decision responsibility becomes ambiguous |
| Load `adaptive-component-design` alone for a full redesign | It does not own product experience, visual direction, or page structure |
| Skip `design-review` for implemented UI | The decision maker self-certifies without rendered evidence |
| Activate all roles for every request | Noise and conflicting advice |
| Hide which roles were activated | The user cannot see who owns the decision |
| Give a flat list without synthesis | The user must resolve conflicts alone |
| Follow the user's requested component blindly | A proposed solution is mistaken for the actual requirement |
