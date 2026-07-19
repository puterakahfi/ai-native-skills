---
name: new-feature-workflow
description: Evidence-backed new feature workflow — specify scope, approve design decisions, implement with tests, verify technical and rendered outcomes, submit complete evidence, and merge only through code-review-workflow approval.
license: MIT
metadata:
  ai-native-skills.version: 2.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.requires: "master-engineer master-design spec-workflow test-driven-development code-review-workflow design-review"
  ai-native-skills.type: workflow
  ai-native-skills.implements: ai-native-core/contracts/workflows/new-feature.contract.yaml
  ai-native-skills.contract-version: "~0.3"
  ai-native-skills.skill_load_order: '[{''phase'': ''plan'', ''load'': [''master-engineer'']}, {''phase'': ''design-decision'', ''load'': [''master-engineer'', ''diagram-architect'', ''master-design'']}, {''phase'': ''implement'', ''load'': [''master-engineer'', ''test-driven-development'']}, {''phase'': ''verify'', ''load'': [''design-review'']}, {''phase'': ''review'', ''load'': [''code-review-workflow'']}]'
  ai-native-skills.skills: '{''required'': [''master-engineer'', ''test-driven-development'', ''code-review-workflow''], ''optional'': [''diagram-architect'', ''master-design'', ''design-review'']}'
---

# New Feature Workflow

Plan → design decision → implement → verify → submit → code review.

## Core Rule

```text
Spec before implementation.
Design decision before implementation when affected.
Rendered acceptance after implementation when user-facing output changes.
Code-review-workflow approval before merge.
```

A wireframe or specification decides what to build. It does not prove the implemented result.

## Hard Rules

```text
1. Define the problem, scope, acceptance criteria, and affected domains before coding.
2. Separate pre-implementation design decision from post-implementation acceptance.
3. Never claim implemented PASS from a wireframe, diagram, or source-only artifact.
4. Implementation must trace to approved scope and decisions.
5. Write tests as part of implementation.
6. User-facing or generated visual changes require fresh rendered/exported evidence.
7. Source-only evidence cannot approve changed visual or interaction behavior.
8. LIMITED REVIEW cannot authorize complete specialist-domain acceptance.
9. Submit spec, issue, technical evidence, and applicable design evidence together.
10. Final merge approval belongs to code-review-workflow.
11. Do not bundle unrelated changes or silently expand scope.
```

## When to Use

Use when adding a new capability to an existing product or codebase.

```text
product from zero        → product-development-workflow
bug or regression        → bugfix-workflow
broad design replacement → redesign-workflow
known narrow design fix  → design-refinement
review-only request      → code-review-workflow or design-audit
```

## Workflow Context

Record before implementation:

```yaml
feature:
  title: <title>
  problem: <problem>
  issue_ref: <issue or task>
  scope_in: []
  scope_out: []
  acceptance_criteria: []
  affected_domains:
    architecture: <true | false>
    logic: <true | false>
    data: <true | false>
    security: <true | false>
    user_facing_design: <true | false>
    generated_or_exported_visual: <true | false>
  technical_approach: <summary>
  verification_plan: []
  approval_policy: <product-defined>
```

## Phase 1 — Plan

**Gate:** spec and affected domains exist before implementation.

Define:

```text
problem and intended outcome
scope in and scope out
observable acceptance criteria
technical approach
architecture, logic, data, security, and design impact
issue tracker reference
verification and evidence plan
```

Replace vague criteria such as “works correctly” with behavior, context, and expected result.

**Done when:** scope, affected domains, criteria, issue, and verification plan are explicit.

## Phase 2 — Design Decision

**Gate:** applicable design decisions are approved before implementation.

Required when the feature changes:

```text
system boundaries, contracts, integration, or data model
user flow, information architecture, component model, or interaction
responsive/adaptive behavior or visual direction
required states, content, assets, or fidelity locks
specialized generated/exported visual behavior
```

Load only relevant owners and specialists:

```text
master-engineer   architecture, contracts, data, integration
master-design     task flow, component model, responsive behavior, visual direction
diagram-architect decision-bearing diagrams when useful
specialized owner domains outside built-in product UI/visual communication
```

Load `references/design-decision-and-acceptance.md` for the decision schema, gate checklist, and forbidden claims.

**Done when:** the approved boundary, required states/contexts, locks, assumptions, and implementation-ready criteria are explicit.

## Phase 3 — Implement

**Gate:** implementation traces to approved scope and design decisions.

Load `master-engineer` and `test-driven-development`.

```text
implement one approved slice at a time
write tests at the relevant boundary
trace changes to acceptance criteria
preserve declared design, content, and asset locks
update and reapprove the spec when scope materially changes
keep unrelated cleanup outside the submission
```

**Done when:** scoped criteria are implemented, tests exist, and no unapproved change is bundled.

## Phase 4 — Verify

**Gate:** technical and applicable design-acceptance evidence exist before submission.

Technical evidence may include:

```text
tests and regression tests
type, lint, and build output
contract, migration, runtime, or integration evidence
security evidence when affected
```

For user-facing or generated/exported visual changes, load:

```text
design-review
references/design-decision-and-acceptance.md
```

The adapter defines:

```text
acceptance trigger
design-review facade route
evidence by artifact state
specialized-domain coverage
verdict → workflow-state mapping
```

Key boundary:

```text
rendered interactive → exercise affected contexts, states, inputs, runtime, accessibility
rendered static      → inspect final size, crop, fidelity, content, and export
source-only          → rendered behavior remains NOT_VERIFIED
specialized domain   → load domain reviewer or block complete acceptance
backend-only         → Design acceptance: NOT_APPLICABLE
```

**Done when:** technical evidence exists and every applicable design verdict is resolved for the declared feature scope.

## Phase 5 — Submit

**Gate:** submission references spec, issue, decisions, and evidence.

Include:

```text
what changed and why
spec and issue reference
acceptance-criteria checklist
approved decision artifacts and locks when applicable
technical evidence
design-review route, verdict, findings, and gaps when applicable
known limitations and accepted risks
confirmation that unrelated changes are absent
```

Use the handoff schema in `references/design-decision-and-acceptance.md`.

Do not submit as design-complete while required rendered evidence remains `NOT_VERIFIED`.

**Done when:** the submission is traceable, evidence-backed, and ready for independent review.

## Phase 6 — Review

**Gate:** explicit `code-review-workflow` approval before merge.

Pass the complete feature handoff to `code-review-workflow`. It evaluates affected architecture, design, logic, and security domains and returns:

```text
APPROVED        → eligible to merge under product policy
REQUEST CHANGES → return to implementation or verification
BLOCKED         → resolve missing evidence, hard failure, or reviewer coverage
```

A feature-level `NEEDS WORK`, `CRITICAL`, `LIMITED REVIEW`, or `ROUTE ELSEWHERE` cannot be downgraded to a non-blocking merge flag.

**Done when:** required reviewers approve and the submission is merged according to product policy.

## Quick Reference

| Phase | Primary gate | Done when |
|---|---|---|
| Plan | Spec + affected domains | Scope, criteria, issue, verification plan explicit |
| Design decision | Decisions approved | Boundary, contexts, states, and locks explicit |
| Implement | Traces to scope | Criteria implemented with tests |
| Verify | Acceptance evidence | Technical and applicable design evidence resolved |
| Submit | Complete handoff | Submission is traceable and reviewable |
| Review | Code-review approval | Explicit merge verdict issued |

## Common Pitfalls

| Anti-pattern | Correct behavior |
|---|---|
| Wireframe reviewed, therefore UI passed | Treat it as a decision; verify implementation later |
| CI green, therefore feature complete | Collect all required technical and design evidence |
| CSS/source inspection used as visual acceptance | Render the output or mark NOT_VERIFIED |
| Design-review loaded for backend-only change | Record design as NOT_APPLICABLE |
| Specialist visual accepted with universal gates | Load domain reviewer or block complete acceptance |
| Submit first, collect evidence during review | Resolve verification before submission |
| Peer review bypasses code-review-workflow | Use the evidence-backed merge workflow |
| Scope grows during implementation | Update and reapprove spec and decisions |
