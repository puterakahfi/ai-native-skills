---
name: role-switcher
description: Intent and domain detection with explicit role composition — selects one owner, narrow specialists, an independent reviewer facade, and a domain reviewer when specialized acceptance is required.
license: MIT
metadata:
  ai-native-skills.version: 1.4.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.requires: "master-engineer master-design adaptive-component-design product-manager ux-psychology user-research native-ai-engineer chatgpt-app-development diagram-architect design-review brand-identity-review systematic-debugging architecture-review security-review plan"
  ai-native-skills.type: meta-skill
  ai-native-skills.implements: ai-native-core/contracts/skills/meta/role-switcher.contract.yaml
  ai-native-skills.contract-version: "~0.1"
---

# Role Switcher

## Core contract interface

```yaml
required_inputs:
  - user_request
allowed_outputs:
  - detected_intent
  - role_composition
  - skills_to_load
  - analysis_with_multi_lens
quality_gates:
  - intent_must_be_detected_before_role_selection
  - role_composition_must_be_explicit_not_implicit
  - each_role_must_contribute_a_distinct_lens
  - no_role_loaded_without_clear_relevance_to_intent
  - multi_role_output_must_be_structured_by_lens
  - agent_must_state_which_roles_were_activated
```

State the detected intent and activated roles explicitly. Each role must contribute a distinct lens, and multi-role evidence must remain structured by lens before the owner synthesizes one decision. Never load a role without clear relevance to the user request.

## Core Rule

```text
detect intent, lifecycle, platform, and domain
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

A platform specialist, domain specialist, or reviewer never silently replaces the owner.

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
| Existing-product ChatGPT App integration | `master-engineer` | `chatgpt-app-development`, `native-ai-engineer`, product/design specialists as needed | `architecture-review`, `security-review`, `design-review` when UI ships |

### Product and Research

| Intent | Owner | Specialists | Reviewer |
|---|---|---|---|
| Product gap analysis | `product-manager` | domain owners and experts | relevant domain reviewer |
| Requirements and acceptance criteria | `product-manager` | technical/design owners | relevant review workflow |
| Interviews, JTBD, assumption validation | `user-research` | `product-manager` | research evidence review |
| Survey or usability test | `user-research` | `ux-psychology` | product owner synthesizes implications |
| ChatGPT App product from zero | `product-manager` | `chatgpt-app-development`, `native-ai-engineer`, `master-design`, `master-engineer` | product acceptance plus architecture, security, and design reviewers |

### Creative and AI Tools

| Intent | Owner | Specialists | Reviewer |
|---|---|---|---|
| Generate/refine image prompt | `prompt-engineer` | brand/product/design specialists | rendered-output review when accepted |
| Diagnose generated identity output | `prompt-engineer` or identity owner | `brand-identity-review` as reviewer, not generator | `design-review` + `brand-identity-review` |
| AI image product or generation feature | `product-manager` | prompt + design + engineering owners | applicable product/design/engineering reviewers |
| ChatGPT App tool, widget, native-capability handoff, or publication boundary | lifecycle owner | `chatgpt-app-development`; add `native-ai-engineer` for contract/runtime boundaries | applicable architecture, security, accessibility, and design reviewers |

## ChatGPT App Composition Rules

`chatgpt-app-development` is a platform specialist, not a product owner and not a replacement workflow.

```text
product from zero
  lifecycle owner: product-manager
  platform specialist: chatgpt-app-development
  architecture specialist: native-ai-engineer
  UI owner: master-design when user-facing widget/UI is in scope
  implementation owner: master-engineer during delivery
  reviewers: architecture-review + security-review + design-review/accessibility as applicable

existing product integration
  lifecycle owner: master-engineer for implementation synthesis
  product authority: product-manager for scope/value decisions
  platform specialist: chatgpt-app-development
  architecture specialist: native-ai-engineer when boundaries change
```

The specialist owns Apps SDK/MCP product-boundary expertise, including cost ownership, tool contracts, widget behavior, native ChatGPT handoff, auth, state, security, testing, and publication requirements. Product-specific rules remain with the owning product modules.

## Application Steps

### 1. Detect intent and lifecycle

```text
domain
action: audit | advise | build | fix | redesign | accept
depth: narrow | specification | production | release
evidence state: idea | source | rendered | production behavior
platform: generic | chatgpt-app | other-specialized-surface
```

For design tasks also classify:

```text
design_domain
surface_profile
reviewer availability
built-in or adapter coverage
```

For ChatGPT App work also classify:

```text
generation_surface
cost_owner
data_scope
ui_mode
distribution
```

### 2. Assign composition slots

```yaml
roles:
  owner: product-manager
  specialists:
    - chatgpt-app-development
    - native-ai-engineer
    - master-design
    - master-engineer
  reviewers:
    - architecture-review
    - security-review
    - design-review
  platform: chatgpt-app
```

### 3. Enforce composition gates

```text
□ exactly one owner is explicit
□ every specialist has a narrow reason
□ platform specialist does not replace lifecycle owner
□ reviewer is independent when practical
□ design domain and coverage are explicit when design is reviewed
□ specialized acceptance has the correct domain reviewer
□ missing reviewer limits the verdict
□ rendered/implemented deliverables have evidence-backed review
□ ChatGPT App cost owner and generation surface are explicit
```

### 4. Synthesize one result

The owner returns one decision with rationale, specialist evidence, trade-offs, implementation/production implications, reviewer verdict, coverage mode, and remaining gaps.

Do not return disconnected role reports.

## Examples

### ChatGPT App product from zero

```text
Owner: product-manager
Platform specialist: chatgpt-app-development
Architecture specialist: native-ai-engineer
Design owner: master-design for widget UX
Implementation owner: master-engineer during feature delivery
Reviewers: architecture-review, security-review, design-review, accessibility
Primary lifecycle: product-development-workflow
```

### Existing product adds ChatGPT App adapter

```text
Owner: master-engineer for implementation synthesis
Product authority: product-manager for scope decisions
Platform specialist: chatgpt-app-development
Architecture specialist: native-ai-engineer
Primary lifecycle: new-feature-workflow
```

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
| ChatGPT App specialist becomes a new lifecycle owner | Platform knowledge overrides product/feature lifecycle |
| `design-review` treated as expert in every discipline | Facade coverage is overstated |
| Identity review uses universal/static gates only | Domain construction and system quality remain uncovered |
| Missing domain reviewer still receives PASS | Missing knowledge is hidden |
| Activate all skills for every request | Context and advice become noisy |
| Skip reviewer for implemented acceptance | Decision maker self-certifies |
| Return separate reports without synthesis | User must resolve conflicts manually |
