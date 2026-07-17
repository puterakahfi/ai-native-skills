---
name: product-development-workflow
description: End-to-end digital product workflow from zero to launch. Use when a user wants to develop a product idea through discovery, PRD, MVP slice, technical spec, implementation, acceptance verification, release, deployment, launch, and learning without manually composing many skills.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.requires: "product-requirements business-value-alignment experiment-design user-research master-design master-engineer spec-workflow threat-modeling code-review-workflow deployment-workflow observability-design"
  ai-native-skills.type: workflow
  ai-native-skills.implements: ai-native-core/contracts/workflows/product-development.contract.yaml
  ai-native-skills.contract-version: "~0.1"
  ai-native-skills.skill_load_order: '[{''phase'': ''discovery'', ''load'': [''model-selection'', ''user-research'', ''business-value-alignment'', ''experiment-design'', ''product-manager'', ''decision-making'']}, {''phase'': ''requirements'', ''load'': [''product-requirements'', ''business-value-alignment'', ''experiment-design'', ''product-manager'']}, {''phase'': ''mvp_slice'', ''load'': [''business-value-alignment'', ''experiment-design'', ''product-manager'', ''decision-making'', ''spike'']}, {''phase'': ''technical_spec'', ''load'': [''spec-workflow'', ''native-ai-engineer'', ''master-engineer'', ''api-contract'', ''data-modeling'']}, {''phase'': ''implementation'', ''load'': [''new-feature-workflow'', ''test-driven-development'', ''master-engineer'', ''systematic-debugging'']}, {''phase'': ''acceptance_verification'', ''load'': [''skill-eval'', ''code-review-workflow'', ''security-review'', ''design-review'', ''web-performance'']}, {''phase'': ''release'', ''load'': [''git-workflow'', ''deployment-workflow'']}, {''phase'': ''deploy'', ''load'': [''deployment-workflow'', ''observability-design'', ''resilience-engineering'']}, {''phase'': ''launch'', ''load'': [''business-value-alignment'', ''product-manager'', ''content-strategy'', ''copywriting'', ''cro'', ''observability-design'']}, {''phase'': ''learn'', ''load'': [''business-value-alignment'', ''product-manager'', ''observability-design'', ''user-research'', ''decision-making'']}]'
---

# Product Development Workflow

> **HARD RULES (read first)**
> 1. **One-line invocation** — use the patterns below; they are the most common entry point.
> 2. **Never skip phases** — discovery before spec, spec before implementation. No exceptions.
> 3. **Stop at every stop point** — do not auto-proceed past a gate without explicit user approval.

## One-Line Invocation

For a vague product idea:

```bash
hermes chat -s product-development-workflow -q \
  "Develop a digital product for affiliators from zero. Start with discovery and stop after PRD/MVP recommendation for approval."
```

For full lifecycle:

```bash
hermes chat -s product-development-workflow -q \
  "Develop a digital product for affiliators from zero to launch. Ask for approval at each major gate."
```

## Overview

Use this workflow as the **single entry point** for developing a digital product from an initial idea to launch.

The user should not need to manually load `user-research`, `product-requirements`, `product-manager`, `spec-workflow`, `new-feature-workflow`, `deployment-workflow`, and release/launch skills one by one. This workflow wraps them into a staged product lifecycle with clear stop points.

Implements:

```text
ai-native-core/contracts/workflows/product-development.contract.yaml
```

## When to Use

Use when the user says things like:

- "I want to build a digital product for X."
- "Develop this product idea from zero."
- "Plan and build an MVP."
- "Take this from idea to launch."
- "What workflow should I execute for a new product?"
- "I have an idea but no PRD/spec yet."

Do not use when:

- the PRD/spec already exists and the user only wants implementation; use `spec-workflow` or `new-feature-workflow`
- the task is only a bugfix; use `bugfix-workflow`
- the task is only deployment; use `deployment-workflow`
- the task is refinement/redesign of an existing UI surface; use `redesign-workflow`
- the task is only design iteration, landing page polish, dashboard UX improvement, copy/CTA/CRO refinement, or visual audit; use `redesign-workflow`

## Default Behavior

If the user does not specify a stop point, default to:

```text
discovery → PRD draft → MVP recommendation → stop for approval
```

Do **not** jump straight into technical spec or implementation when the product idea is vague.

## Phase Overview

Load `references/phases-1-5.md` for full details on Phases 1–5.
Load `references/phases-6-10.md` for full details on Phases 6–10.
Load `references/formats-pitfalls.md` for stop points, output formats, pitfalls, and verification checklist.

| # | Phase | Key skills to load | Gate |
|---|-------|--------------------|------|
| 1 | Discovery | model-selection, user-research, business-value-alignment, experiment-design, product-manager, decision-making | Opportunity + business value explicit |
| 2 | Requirements / PRD | product-requirements, business-value-alignment, experiment-design, product-manager | PRD READINESS = READY |
| 3 | MVP Slice | business-value-alignment, experiment-design, product-manager, decision-making, spike | MVP scope approved |
| 4 | Technical Spec | spec-workflow, native-ai-engineer, master-engineer, api-contract, data-modeling | Spec traces to PRD |
| 5 | Implementation | new-feature-workflow, test-driven-development, master-engineer, systematic-debugging | Code verified with real tool output |
| 6 | Acceptance Verification | skill-eval, code-review-workflow, security-review, design-review, web-performance | Acceptance criteria have evidence |
| 7 | Release | git-workflow, deployment-workflow | Notes + version + rollback plan |
| 8 | Deploy | deployment-workflow, observability-design, resilience-engineering, incident-response | Health verified before launch |
| 9 | Launch | product-manager, content-strategy, copywriting, cro, observability-design | Monitoring + feedback loop live |
| 10 | Learn | product-manager, observability-design, user-research, decision-making | Next action explicit |

### Stop Points Summary

Default stop points (see `references/formats-pitfalls.md` for full detail):

```text
after_discovery_recommendation
after_prd_draft
after_mvp_plan
after_technical_spec
before_release
after_post_launch_review
```

---

> **HARD RULES (reminder)**
> 1. **Never skip phases** — discovery before spec, spec before implementation.
> 2. **Stop at every stop point** — do not auto-proceed. Ask for explicit approval at each gate.
> 3. **No acceptance evidence = not release-ready.** A checklist without proof does not pass.
