---
name: product-development-workflow
description: End-to-end digital product workflow from zero to launch. Use when a user wants to develop a product idea through discovery, PRD, MVP slice, technical spec, implementation, acceptance verification, release, deployment, launch, and learning without manually composing many skills.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: workflow
  ai-native-skills.implements: ai-native-core/contracts/workflows/product-development.contract.yaml
  ai-native-skills.skill_load_order: '[{''phase'': ''discovery'', ''load'': [''model-selection'', ''user-research'', ''product-manager'', ''decision-making'']}, {''phase'': ''requirements'', ''load'': [''product-requirements'', ''product-manager'']}, {''phase'': ''mvp_slice'', ''load'': [''product-manager'', ''decision-making'', ''spike'']}, {''phase'': ''technical_spec'', ''load'': [''spec-workflow'', ''native-ai-engineer'', ''master-engineer'', ''api-contract'', ''data-modeling'']}, {''phase'': ''implementation'', ''load'': [''new-feature-workflow'', ''test-driven-development'', ''master-engineer'', ''systematic-debugging'']}, {''phase'': ''acceptance_verification'', ''load'': [''skill-eval'', ''code-review-workflow'', ''security-review'', ''design-review'', ''web-performance'']}, {''phase'': ''release'', ''load'': [''git-workflow'', ''deployment-workflow'']}, {''phase'': ''deploy'', ''load'': [''deployment-workflow'', ''observability-design'', ''resilience-engineering'']}, {''phase'': ''launch'', ''load'': [''product-manager'', ''content-strategy'', ''copywriting'', ''cro'', ''observability-design'']}, {''phase'': ''learn'', ''load'': [''product-manager'', ''observability-design'', ''user-research'', ''decision-making'']}]'
---

# Product Development Workflow

## Overview

Use this workflow as the **single entry point** for developing a digital product from an initial idea to launch.

The user should not need to manually load `user-research`, `product-requirements`, `product-manager`, `spec-workflow`, `new-feature-workflow`, `deployment-workflow`, and release/launch skills one by one. This workflow wraps them into a staged product lifecycle with clear stop points.

Implements:

```text
ai-native-core/contracts/workflows/product-development.contract.yaml
```

## When to Use

Use when the user says things like:

- “I want to build a digital product for X.”
- “Develop this product idea from zero.”
- “Plan and build an MVP.”
- “Take this from idea to launch.”
- “What workflow should I execute for a new product?”
- “I have an idea but no PRD/spec yet.”

Do not use when:

- the PRD/spec already exists and the user only wants implementation; use `spec-workflow` or `new-feature-workflow`
- the task is only a bugfix; use `bugfix-workflow`
- the task is only deployment; use `deployment-workflow`
- the task is refinement/redesign of an existing UI surface; use `redesign-workflow`
- the task is only design iteration, landing page polish, dashboard UX improvement, copy/CTA/CRO refinement, or visual audit; use `redesign-workflow`

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

## Default Behavior

If the user does not specify a stop point, default to:

```text
discovery → PRD draft → MVP recommendation → stop for approval
```

Do **not** jump straight into technical spec or implementation when the product idea is vague.

## Phases

### Phase 1 — Discovery

**Goal:** Understand the product opportunity.

Load conceptually:

```text
model-selection
user-research
product-manager
decision-making
```

Produce:

```text
- target user segments
- jobs-to-be-done
- pain points
- existing alternatives/workarounds
- opportunity list
- ranked recommendation
```

**Gate:** Opportunity must be ranked before PRD.

**Done when:** one MVP direction is recommended with rationale and open assumptions.

### Phase 2 — Requirements / PRD

**Goal:** Convert opportunity into a PRD.

Load conceptually:

```text
product-requirements
product-manager
```

Produce:

```text
- problem statement
- target users
- goals and non-goals
- success metrics
- scope in/out
- user stories or JTBD
- functional requirements
- non-functional requirements
- acceptance criteria
- constraints, dependencies, risks, open questions
- launch criteria
```

**Gate:** PRD readiness must pass before MVP planning or technical spec.

**Done when:** `PRD READINESS` verdict is `READY` or explicit blockers are listed.

### Phase 3 — MVP Slice

**Goal:** Choose the smallest valuable release slice.

Load conceptually:

```text
product-manager
decision-making
spike
```

Produce:

```text
- MVP scope
- non-MVP deferred scope
- highest-risk assumptions
- validation plan
- build sequence
```

**Gate:** MVP scope must be smaller than the full product and must map to success metrics.

**Done when:** the user can approve one MVP slice.

### Phase 4 — Technical Spec

**Goal:** Translate PRD/MVP into agent-executable technical work.

Load conceptually:

```text
spec-workflow
native-ai-engineer
master-engineer
api-contract
data-modeling
```

Produce:

```text
- architecture constraints
- technical spec
- task plan
- context packs
- acceptance criterion mapping
```

**Gate:** technical spec must trace to PRD requirements.

**Done when:** every task traces to an acceptance criterion.

### Phase 5 — Implementation

**Goal:** Build the MVP slice.

Load conceptually:

```text
new-feature-workflow
test-driven-development
master-engineer
systematic-debugging
```

Produce:

```text
- implementation changes
- test evidence
- scope drift check
```

**Gate:** implementation must trace to acceptance criteria.

**Done when:** code changes are verified with real tool output.

### Phase 6 — Acceptance Verification

**Goal:** Prove the product satisfies the PRD acceptance criteria.

Load conceptually:

```text
skill-eval
code-review-workflow
security-review
design-review
web-performance
accessibility
```

Produce:

```text
- acceptance evidence matrix
- review findings
- release blockers
```

**Gate:** acceptance criteria must have evidence.

**Done when:** release blockers are resolved or explicitly accepted.

### Phase 7 — Release

**Goal:** Prepare release artifacts.

Load conceptually:

```text
git-workflow
deployment-workflow
```

Produce:

```text
- release notes
- version/tag plan
- changelog
- rollback note
- release signoff
```

**Gate:** release has notes, version/tag, and rollback plan.

**Done when:** release is approved for deployment.

### Phase 8 — Deploy

**Goal:** Deploy safely and verify health.

Load conceptually:

```text
deployment-workflow
observability-design
resilience-engineering
incident-response
```

Produce:

```text
- deployment evidence
- health check output
- rollback readiness
```

**Gate:** deployment health must be verified before launch.

**Done when:** deployment is healthy or rollback/blocker is reported.

### Phase 9 — Launch

**Goal:** Release to users with support, analytics, and feedback loop.

Load conceptually:

```text
product-manager
content-strategy
copywriting
cro
observability-design
```

Produce:

```text
- launch message
- support handoff
- analytics checklist
- feedback channel
- monitoring plan
```

**Gate:** launch includes monitoring and feedback loop.

**Done when:** users can access the product and feedback/metrics collection is live.

### Phase 10 — Learn

**Goal:** Convert launch data into next decisions.

Load conceptually:

```text
product-manager
observability-design
user-research
decision-making
```

Produce:

```text
- metric readout
- feedback synthesis
- incident/bug summary
- iterate / pivot / stop recommendation
- next PRD or backlog update
```

**Gate:** post-launch learning feeds next PRD or backlog.

**Done when:** next action is explicit.

## Stop Points

Default stop points:

```text
after_discovery_recommendation
after_prd_draft
after_mvp_plan
after_technical_spec
before_release
after_post_launch_review
```

If the user asks for planning only, stop after PRD/MVP. If the user asks for full execution, ask for approval at each destructive or external side-effect boundary.

## Output Format for Planning Mode

Use this format when the user is still exploring the product:

```text
PRODUCT DEVELOPMENT WORKFLOW
Mode: planning
Current phase: discovery | requirements | mvp_slice
Stop point: <stop point>

Target users:
- ...

Top opportunities:
1. ...
2. ...
3. ...

Recommended MVP:
- ...

PRD readiness:
Verdict: READY | NEEDS REVISION | BLOCKED
Blocking gaps:
- ...

Next approval needed:
- ...
```

## Output Format for Execution Mode

Use this format when the user wants actual implementation/deploy:

```text
PRODUCT DEVELOPMENT WORKFLOW
Mode: execution
Current phase: <phase>
Gate status: PASS | FAIL | BLOCKED
Evidence:
- <tool output, test result, URL, commit, or artifact path>
Next phase:
- <phase or approval request>
```

## Common Pitfalls

1. **Starting with code.** New products start with discovery and PRD unless the user already provides validated requirements.
2. **Skipping non-goals.** Without non-goals, MVP scope expands into full-product fantasy.
3. **Treating deploy as launch.** Deployment is technical availability; launch is user-facing release with messaging, support, analytics, and feedback.
4. **No acceptance evidence.** A checklist without proof is not release readiness.
5. **No stop point.** For vague product ideas, stop after PRD/MVP recommendation for approval before technical spec.
6. **Overloading one response.** For large products, phase output should be concise and gated, not a giant all-in-one document.

## Verification Checklist

- [ ] Discovery happened before PRD when idea was vague.
- [ ] PRD exists before technical spec.
- [ ] MVP slice is smaller than full product.
- [ ] Technical spec traces to PRD requirements.
- [ ] Implementation tasks trace to acceptance criteria.
- [ ] Acceptance criteria have evidence before release.
- [ ] Release has notes/version/rollback plan.
- [ ] Deployment health is verified before launch.
- [ ] Launch has support, analytics, and feedback loop.
- [ ] Post-launch learning feeds next PRD or backlog.
