---
name: role-switcher
description: Intent and domain detection with explicit role composition — selects one owner, narrow specialists, an independent reviewer facade, and a domain reviewer when specialized acceptance is required.
license: MIT
metadata:
  ai-native-skills.version: 1.3.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.requires: "master-engineer master-design adaptive-component-design product-manager ux-psychology user-research native-ai-engineer diagram-architect design-review brand-identity-review systematic-debugging architecture-review security-review plan"
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
→ add the applicable built-in or external domain reviewer
→ synthesize one decision
```

Roles are not a flat list.

```text
Owner            final decision responsibility and synthesis
Specialist       narrow expertise contributing within a boundary
Reviewer facade  common review entry point, evidence, score, verdict, report
Domain reviewer  specialist-domain gates, evidence, and hard-gate policy
```

A specialist or reviewer never silently replaces the owner.

## Design Review Composition

For design acceptance, `design-review` is the reviewer facade. It is not automatically the expert for every discipline.

```text
design-review owns
  classification, reviewer routing, gate identity, applicability,
  evidence normalization, score, coverage, verdict, report

domain reviewer owns
  domain principles, canonical gate definitions, evidence interpretation,
  specialist hard gates, correction knowledge
```

### Built-in domains

| Design domain | Owner | Specialists | Reviewer facade | Domain reviewer |
|---|---|---|---|---|
| Digital product UI, responsive web, mobile, desktop | `master-design` | relevant design ports; `adaptive-component-design` when needed | `design-review` | built-in interactive/profile strategy |
| Static marketing, social, ad, poster, banner, thumbnail | `master-design` | typography, color, composition, brand/content specialists | `design-review` | built-in static-visual strategy |
| Presentation slides or decks | `master-design` or presentation owner | narrative, data, visual specialists | `design-review` | built-in presentation strategy |

### External adapter domains

| Design domain | Owner | Reviewer facade | Domain reviewer | Coverage when loaded |
|---|---|---|---|---|
| Logo and brand identity systems | declared brand/identity owner | `design-review` | `brand-identity-review` (`BI`) | `ADAPTER_COVERED` |
| Packaging and specialist print production | declared packaging/print owner | `design-review` | packaging/print reviewer | adapter-defined |
| Motion graphics, film, video editing | declared motion/video owner | `design-review` | motion/video reviewer | adapter-defined |
| Industrial or physical product design | declared industrial-design owner | `design-review` | industrial-design reviewer | adapter-defined |
| Architecture, interior, or spatial design | declared spatial-design owner | `design-review` | spatial-domain reviewer | adapter-defined |
| Fashion design | declared fashion-design owner | `design-review` | fashion-domain reviewer | adapter-defined |
| Service-design systems | product/service owner | `design-review` only for visual artifacts | service-design reviewer | adapter-defined |

When a required reviewer is unavailable:

```text
coverage_mode: LIMITED
verdict ceiling: LIMITED REVIEW
handoff: install/load domain reviewer or route to domain specialist
```

Universal visual review remains supplementary and cannot certify complete specialist-domain quality.

## Design Ownership Rules

```text
broad product UI/UX
  owner: master-design
  facade: design-review
  domain reviewer: built-in interactive

cross-device component choice
  owner: master-design
  specialist: adaptive-component-design
  facade: design-review after implementation/acceptance

brand identity audit or acceptance
  owner: declared brand/identity owner
  facade: design-review
  domain reviewer: brand-identity-review
  namespace: BI
  coverage: ADAPTER_COVERED when loaded

audit only
  lifecycle: design-audit

targeted verified design findings
  lifecycle: design-refinement

broad direction or structure replacement
  lifecycle: redesign-workflow
```

A narrow advisory question may use a specialist without a reviewer when no artifact is being accepted.

## General Role Map

### Engineering

| Intent | Owner | Specialists | Reviewer |
|---|---|---|---|
| Review code, PR, architecture | `master-engineer` | relevant architecture skills | `architecture-review` |
| Bug, error, crash, debugging | `master-engineer` | `systematic-debugging` | relevant reviewer after fix |
| Security, vulnerability, secrets | `master-engineer` | security skills | `security-review` |
| System design or structural refactor | `master-engineer` | `native-ai-engineer` when relevant | `architecture-review` |
| Native AI runtime, adapter, contract | `native-ai-engineer` | `master-engineer`, runtime skills | `architecture-review` |

### Product and Research

| Intent | Owner | Specialists | Reviewer |
|---|---|---|---|
| Product gap analysis | `product-manager` | domain owners and experts | relevant domain reviewer |
| Requirements and acceptance criteria | `product-manager` | technical/design owners | relevant review workflow |
| Interviews, JTBD, assumption validation | `user-research` | `product-manager` | research evidence review |
| Survey or usability test | `user-research` | `ux-psychology` | product owner synthesizes implications |

### Creative and AI Tools

| Intent | Owner | Specialists | Reviewer |
|---|---|---|---|
| Generate/refine image prompt | `prompt-engineer` | brand/product/design specialists | rendered-output review when accepted |
| Diagnose generated identity output | `prompt-engineer` or identity owner | `brand-identity-review` as reviewer, not generator | `design-review` + `brand-identity-review` |
| AI image product or generation feature | `product-manager` | prompt + design + engineering owners | applicable product/design/engineering reviewers |

## Application Steps

### 1. Detect intent and lifecycle

```text
domain
action: audit | advise | build | fix | redesign | accept
depth: narrow | specification | production | release
evidence state: idea | source | rendered | production behavior
```

For design tasks also classify:

```text
design_domain
surface_profile
reviewer availability
built-in or adapter coverage
```

### 2. Assign composition slots

```yaml
roles:
  owner: brand-identity-owner
  specialists:
    - design-typography
    - design-color
  reviewer_facade: design-review
  domain_reviewers:
    - brand-identity-review
  gate_namespace: BI
  coverage_mode: ADAPTER_COVERED
```

### 3. Enforce composition gates

```text
□ exactly one owner is explicit
□ every specialist has a narrow reason
□ reviewer is independent when practical
□ design domain and coverage are explicit
□ specialized acceptance has the correct domain reviewer
□ missing reviewer limits the verdict
□ rendered/implemented deliverables have evidence-backed review
```

### 4. Synthesize one result

The owner returns one decision with rationale, specialist evidence, trade-offs, implementation/production implications, reviewer verdict, coverage mode, and remaining gaps.

Do not return disconnected role reports.

## Examples

### Cross-device category navigation

```text
Owner: master-design
Specialist: adaptive-component-design
Reviewer facade: design-review
Domain reviewer: built-in interactive
Coverage: BUILT_IN
```

### Logo-system audit

```text
Owner: declared brand/identity owner
Reviewer facade: design-review
Domain reviewer: brand-identity-review
Gate namespace: BI
Coverage: ADAPTER_COVERED
```

If `brand-identity-review` is not installed, the same request falls back to `LIMITED REVIEW`; it does not fall back to UI gates.

## Anti-Patterns

| Anti-pattern | Why it fails |
|---|---|
| Flat list of roles | Ownership and boundaries disappear |
| Specialist replaces owner | Narrow expertise controls unrelated decisions |
| `design-review` treated as expert in every discipline | Facade coverage is overstated |
| Identity review uses universal/static gates only | Domain construction and system quality remain uncovered |
| Missing domain reviewer still receives PASS | Missing knowledge is hidden |
| Activate all skills for every request | Context and advice become noisy |
| Skip reviewer for implemented acceptance | Decision maker self-certifies |
| Return separate reports without synthesis | User must resolve conflicts manually |