---
name: role-switcher
description: Intent and domain detection with explicit role composition — selects one owner, narrow specialists, an independent reviewer facade, and a domain reviewer when specialized acceptance is required.
license: MIT
metadata:
  ai-native-skills.version: 1.2.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.requires: "master-engineer master-design adaptive-component-design product-manager ux-psychology user-research native-ai-engineer diagram-architect design-review systematic-debugging architecture-review security-review plan"
  ai-native-skills.type: meta-skill
  ai-native-skills.implements: ai-native-core/contracts/skills/meta/role-switcher.contract.yaml
  ai-native-skills.contract-version: "~0.1"
---

# Role Switcher

## Core Rule

```text
detect intent and domain
→ assign one owner
→ load only narrow specialists
→ add a reviewer facade when acceptance is required
→ add a domain reviewer when the facade has no complete built-in coverage
→ synthesize one decision
```

Roles are not a flat list.

```text
Owner            final decision responsibility and synthesis
Specialist       narrow expertise contributing within a boundary
Reviewer facade  common review entry point, evidence, score, verdict, report
Domain reviewer  specialized domain gates and evidence requirements
```

A specialist or reviewer must never silently replace the owner.

## Design Review Composition

For design acceptance, `design-review` is the reviewer facade. It is not automatically the specialist for every design discipline.

```text
design-review facade owns
  domain/surface classification
  reviewer selection
  applicability and evidence normalization
  score, coverage, verdict, report

built-in or external domain reviewer owns
  domain principles
  specialist thresholds
  domain hard gates
  correction knowledge
```

### Built-in facade coverage

| Design domain | Owner | Specialists | Reviewer facade | Domain reviewer |
|---|---|---|---|---|
| Digital product UI, responsive web, mobile, desktop | `master-design` | relevant design ports; `adaptive-component-design` when component fitness changes by viewport | `design-review` | built-in interactive/profile strategy |
| Static marketing, social, ad, poster, banner, thumbnail | `master-design` | typography, color, composition, brand/content specialists as relevant | `design-review` | built-in static-visual strategy |
| Presentation slides or decks | `master-design` or declared presentation owner | narrative, data, visual specialists as relevant | `design-review` | built-in presentation strategy |

### Specialized design domains

| Design domain | Owner | Reviewer facade | Required domain reviewer |
|---|---|---|---|
| Logo and brand identity systems | declared brand/identity owner | `design-review` | brand-identity reviewer |
| Packaging and specialist print production | declared packaging/print owner | `design-review` | packaging/print reviewer |
| Motion graphics, film, video editing | declared motion/video owner | `design-review` | motion/video reviewer |
| Industrial or physical product design | declared industrial-design owner | `design-review` | industrial-design reviewer |
| Architecture, interior, or spatial design | declared spatial-design owner | `design-review` | spatial-domain reviewer |
| Fashion design | declared fashion-design owner | `design-review` | fashion-domain reviewer |
| Service-design research and organizational systems | product/service owner | `design-review` only for visual artifacts | service-design reviewer |

When no required domain reviewer is available:

```text
coverage_mode: LIMITED
verdict ceiling: LIMITED REVIEW
handoff: domain specialist or reviewer
```

Universal visual review may still be useful, but it cannot certify complete specialist-domain quality.

## Design Ownership Rules

For product design, UI, or UX work:

```text
Owner: master-design
Specialist: only skills required by the task
Reviewer facade: design-review for audit, implementation, refinement, or acceptance
Domain reviewer: selected from the classified design domain
```

Therefore:

- broad UI/UX work must retain `master-design` as owner;
- cross-device component work normally loads `adaptive-component-design` as specialist;
- audit-only work uses `design-audit` as lifecycle/capability and `design-review` as reviewer facade;
- targeted verified failures use `design-refinement`;
- broad direction or structure replacement uses `redesign-workflow`;
- a narrow advisory question may load one specialist without a reviewer when no artifact is being accepted;
- specialized domains must not be approved using built-in UI/static gates alone.

## When to Use

- A request spans multiple expertise areas.
- Audit or acceptance needs independent review.
- A specialist capability is needed while ownership must remain coherent.
- The design domain determines which reviewer can issue a complete verdict.
- A workflow needs deterministic role composition.
- “What is missing?” requires evidence from multiple bounded lenses.

## Role Map

### Design and Experience

| Intent | Owner | Specialists | Reviewer composition |
|---|---|---|---|
| General product UI/UX direction, wireframe, mockup, design decision | `master-design` | relevant design ports/skills | `design-review` when rendered or accepted + built-in interactive reviewer |
| Audit UI/UX or visual artifact | `master-design` or declared domain owner | behavioral/content specialists when relevant | `design-review` + applicable domain reviewer |
| Design system, tokens, components, consistency | `master-design` | design-system and relevant visual/component skills | `design-review` + built-in interactive reviewer |
| Responsive component choice, tabs overflow, viewport substitution | `master-design` | `adaptive-component-design` | `design-review` for implemented acceptance |
| User flow, onboarding, retention, habit | `master-design` | `ux-psychology`, product skills | `design-review` when a visual artifact exists |
| Accessibility and inclusive design | `master-design` | accessibility specialists | `design-review` for evidence-backed acceptance |
| Static campaign/poster/social visual | `master-design` | typography, color, composition, copy/brand | `design-review` + built-in static reviewer |
| Presentation/deck | declared presentation owner | narrative, data, design specialists | `design-review` + built-in presentation reviewer |
| Identity, packaging, motion/video, industrial, spatial, fashion | declared domain owner | domain specialists | `design-review` + declared external domain reviewer; otherwise LIMITED REVIEW |

### Engineering

| Intent | Owner | Specialists | Reviewer |
|---|---|---|---|
| Review code, PR, architecture | `master-engineer` | relevant architecture skills | `architecture-review` |
| Bug, error, crash, debugging | `master-engineer` | `systematic-debugging` | relevant reviewer after fix |
| Security, vulnerability, secrets | `master-engineer` | security skills | `security-review` |
| System design, scalability, architecture decision | `master-engineer` | `native-ai-engineer` when relevant | `architecture-review` for acceptance |
| Refactor, simplify, debt | `master-engineer` | refactoring/debugging skills | `architecture-review` when boundaries change |
| Diagram or architecture visualization | `master-engineer` | `diagram-architect` | architecture reviewer when decision-bearing |
| Native AI runtime, adapter, contract | `native-ai-engineer` | `master-engineer`, runtime skills | `architecture-review` |

### Product and Research

| Intent | Owner | Specialists | Reviewer |
|---|---|---|---|
| Gap analysis, product feature audit | `product-manager` | domain owners and experts | relevant domain reviewer |
| Requirements and acceptance criteria | `product-manager` | plan + technical/design owners | relevant review workflow |
| Prioritization, backlog, roadmap | `product-manager` | decision/value skills | none unless approval requested |
| User problem or behavioral failure | `product-manager` | `ux-psychology` | owner synthesizes |
| Interviews, JTBD, assumption validation | `user-research` | `product-manager` | research evidence review |
| Survey or usability test | `user-research` | `ux-psychology` | product owner synthesizes implications |

### Creative and AI Tools

| Intent | Owner | Specialists | Reviewer |
|---|---|---|---|
| Generate/refine image prompt | `prompt-engineer` | brand/product/design specialists as relevant | rendered-output review when acceptance matters |
| Diagnose bad image output | `prompt-engineer` | visual/domain specialists | `design-review` with applicable static or specialized reviewer |
| AI image product or generation feature | `product-manager` | prompt + design + engineering owners | product/design/engineering reviewers |

### Cross-Domain

| Intent | Owner | Specialists | Reviewer |
|---|---|---|---|
| Full product audit | `product-manager` or declared lead | engineering, design, product specialists | independent domain reviewers |
| New feature from scratch | `product-manager` | design + engineering owners | design and engineering review |
| End-to-end research → design → build | `product-manager` | research + design + engineering | design and engineering review |

## Application Steps

### 1. Detect intent and requested lifecycle

Determine:

```text
domain
action: audit | advise | build | fix | redesign | accept
depth: narrow | specification | production | release
evidence state: idea | source | rendered | production behavior
```

For design tasks, also classify:

```text
design_domain
surface_profile
built-in or external reviewer coverage
```

### 2. Assign composition slots

```yaml
roles:
  owner: master-design
  specialists:
    - adaptive-component-design
  reviewer_facade: design-review
  domain_reviewers:
    - built-in-interactive
  coverage_mode: BUILT_IN
```

Do not call every loaded skill a role without declaring its responsibility.

### 3. Enforce composition gates

```text
□ exactly one owner is explicit
□ every specialist has a narrow reason
□ reviewer is independent when practical
□ design domain and reviewer coverage are explicit
□ specialized acceptance has a domain reviewer
□ missing domain reviewer limits the verdict
□ rendered or implemented deliverables have evidence-backed review
```

### 4. Apply bounded contributions

```text
Owner
  defines outcome, constraints, and final synthesis

Specialist
  contributes decisions only within its expertise

Reviewer facade
  classifies, normalizes evidence, scores, and reports

Domain reviewer
  applies specialist-domain gates and hard-gate policy
```

### 5. Synthesize one result

The owner returns:

- one recommended decision;
- rationale tied to user/product/message outcome;
- specialist evidence;
- alternatives and trade-offs;
- implementation or production implications;
- reviewer verdict, coverage mode, and remaining gaps.

Do not return disconnected role reports.

## Examples

### Cross-device category navigation

```text
Intent: product UI decision with cross-device risk
Owner: master-design
Specialist: adaptive-component-design
Reviewer facade: design-review
Domain reviewer: built-in interactive strategy
```

The specialist evaluates Tabs, rails, Select, sheets, and other patterns. The owner chooses. The reviewer verifies overflow, paired affordances, shared state, target reachability, and input behavior.

### Logo-system audit without identity reviewer

```text
Intent: specialist design audit
Owner: declared brand/identity owner
Reviewer facade: design-review
Domain reviewer: unavailable
Coverage: LIMITED
```

The result may contain universal composition/type/color observations, but it cannot claim the identity system is production-ready.

## Adding Product-Specific Roles

Extend in product context:

```yaml
role_extensions:
  identity_audit:
    owner: product-brand-owner
    specialists: [design-typography, design-color]
    reviewer_facade: design-review
    domain_reviewers: [brand-identity-review]

  ai_output_review:
    owner: product-manager
    specialists: [prompt-engineer, master-design]
    reviewer_facade: design-review
    domain_reviewers: [built-in-static]
```

## Anti-Patterns

| Anti-pattern | Why it fails |
|---|---|
| Flat list of roles | Ownership and boundaries disappear |
| Specialist replaces owner | Narrow expertise controls unrelated decisions |
| `design-review` treated as expert in every design discipline | Facade coverage is overstated |
| Specialized design has no domain reviewer but receives PASS | Missing knowledge is hidden |
| Activate all skills for every request | Context and advice become noisy |
| Skip reviewer for implemented acceptance | Decision maker self-certifies |
| Follow requested component blindly | Proposed solution replaces actual requirement |
| Return separate reports without synthesis | User must resolve conflicts manually |