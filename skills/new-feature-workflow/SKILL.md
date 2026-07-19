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

A pre-implementation wireframe or specification decides what to build. It does not prove the implemented result.

## Hard Rules

```text
1. Define the user problem, scope, acceptance criteria, and affected domains before coding.
2. Separate design decision approval from post-implementation design acceptance.
3. Do not use design-review to claim implemented PASS from a wireframe or source-only artifact.
4. Implementation must trace to approved scope and design decisions.
5. Write tests as part of implementation, not after the feature is declared complete.
6. User-facing changes require fresh rendered or exported evidence before submission.
7. Source-only evidence cannot approve changed visual or interaction behavior.
8. LIMITED REVIEW cannot authorize a complete specialist-domain submission claim.
9. Submission must include spec, issue, technical evidence, and applicable design evidence.
10. Final merge approval belongs to code-review-workflow.
11. Do not bundle unrelated changes.
12. Do not silently expand scope; update and reapprove the spec first.
```

## When to Use

Use when adding a new capability to an existing product or codebase.

Do not use for:

```text
product from zero       → product-development-workflow
bug or regression       → bugfix-workflow
broad design replacement → redesign-workflow
known narrow design fix → design-refinement
review-only request     → code-review-workflow or design-audit
```

## Workflow State

Record before implementation:

```yaml
feature:
  title: <title>
  problem: <user or system problem>
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
  design_decision_required: <true | false>
  design_acceptance_required: <true | false>
  approval_policy: <product-defined>
```

## Phase 1 — Plan

**Gate:** spec and affected domains exist before implementation.

Define:

```text
what problem is solved
who or what is affected
scope in and scope out
acceptance criteria
technical approach
changed architecture, logic, data, security, and user-facing domains
issue tracker reference
verification and evidence plan
```

Minimum spec:

```yaml
feature_spec:
  title: ""
  problem: ""
  scope_in: []
  scope_out: []
  acceptance_criteria: []
  affected_domains: []
  technical_approach: ""
  verification_plan: []
  issue_ref: ""
```

Acceptance criteria must be observable. Replace “works correctly” with concrete behavior, context, and expected result.

**Done when:** scope, affected domains, acceptance criteria, issue, and verification plan are explicit.

## Phase 2 — Design Decision

**Gate:** applicable design decisions are approved before implementation.

Required when the feature changes any of:

```text
system boundaries, contracts, integration, or data model
user flow, information architecture, component model, or interaction
responsive/adaptive behavior
visual direction or design-system constraints
required states, content, assets, or fidelity locks
specialized generated/exported visual behavior
```

Load only relevant owners and specialists:

```text
master-engineer   architecture, contracts, data, integration
master-design     user flow, component model, responsive behavior, visual direction
diagram-architect decision-bearing diagrams when useful
specialized owner primary domains outside built-in product UI/visual communication
```

For full procedure, load:

```text
references/design-decision-and-acceptance.md
→ section: Pre-Implementation Design Decision
```

The output must declare:

```text
decision owner
artifacts and approved boundary
required states/viewports/inputs
locked assets and content
unresolved assumptions
implementation-ready acceptance criteria
```

Do not claim runtime, accessibility, responsive, visual, export, or release PASS here.

**Done when:** affected decisions are approved and implementation boundaries are clear.

## Phase 3 — Implement

**Gate:** implementation traces to approved scope and design decisions.

Load `master-engineer` and `test-driven-development`.

```text
1. Implement one approved slice at a time.
2. Write unit, integration, contract, UI, or regression tests at the relevant boundary.
3. Trace commits and changed files to acceptance criteria.
4. Preserve declared design/content/asset locks.
5. Stop and update the spec when implementation reveals a material scope change.
6. Keep unrelated cleanup out of the feature submission.
```

**Done when:** all scoped criteria are implemented, tests exist, and no unapproved scope is bundled.

## Phase 4 — Verify

**Gate:** technical and applicable rendered acceptance evidence exist before submission.

### Technical verification

Collect real outputs appropriate to the change:

```text
tests
type/lint/build
contract or migration verification
runtime or integration evidence
security evidence when affected
```

A green suite proves only the tested technical scope.

### Design acceptance

When user-facing or generated/exported visual output changes, load:

```text
design-review
references/design-decision-and-acceptance.md
→ sections: Post-Implementation Acceptance Trigger through Verdict
```

Required route:

```yaml
design_acceptance:
  design_domain: <domain>
  surface_profile: <profile>
  artifact_state: <state>
  review_depth: focused
  coverage_mode: <mode>
  domain_reviewers: []
  evidence_available: []
  evidence_gaps: []
```

Evidence must match the changed outcome:

```text
rendered interactive → changed viewports, states, inputs, runtime, accessibility
rendered static      → final size, crop, fidelity, content, export
source-only          → rendered behavior remains NOT_VERIFIED
specialized domain   → required domain reviewer or LIMITED/ROUTE ELSEWHERE
```

Workflow mapping:

```text
PASS             → submission eligible
CONDITIONAL PASS → eligible only with explicit accepted non-blocking risks
NEEDS WORK       → return to implementation
CRITICAL         → block submission
LIMITED REVIEW   → block complete-domain acceptance
ROUTE ELSEWHERE  → load required reviewer before submission
```

For backend-only changes with no user-facing or visual-output impact:

```text
Design acceptance: NOT_APPLICABLE
```

**Done when:** technical evidence exists and all applicable design acceptance is resolved for the declared feature scope.

## Phase 5 — Submit

**Gate:** submission references spec, issue, decisions, and verification evidence.

Submission must include:

```text
what changed and why
spec and issue reference
acceptance-criteria checklist
approved design-decision artifacts when applicable
technical verification evidence
facade design-review route and verdict when applicable
known limitations and accepted risks
no unrelated changes
```

Use the handoff format in `references/design-decision-and-acceptance.md`.

Do not submit as design-complete when required rendered evidence is still `NOT_VERIFIED`.

**Done when:** a reviewable submission exists with complete traceability and evidence.

## Phase 6 — Review

**Gate:** explicit `code-review-workflow` approval before merge.

Load `code-review-workflow` and pass:

```text
feature spec and accepted scope
approved design decisions and locks
implementation diff
technical evidence
design-review evidence and verdict when applicable
known limitations and accepted risks
```

The reviewer evaluates architecture, design, logic, and security according to affected domains.

```text
APPROVED        → eligible to merge under product policy
REQUEST CHANGES → return to implementation/verification
BLOCKED         → resolve missing evidence, hard failure, or reviewer coverage
```

A feature-level `NEEDS WORK`, `CRITICAL`, `LIMITED REVIEW`, or `ROUTE ELSEWHERE` cannot be downgraded to a non-blocking merge flag.

**Done when:** required reviewers approve and the submission is merged according to product policy.

## Quick Reference

| Phase | Primary gate | Done when |
|---|---|---|
| Plan | Spec + affected domains | Scope, criteria, issue, verification plan explicit |
| Design decision | Decisions approved | Implementation boundary and locks explicit |
| Implement | Traces to scope | Criteria implemented with tests |
| Verify | Acceptance evidence | Technical and rendered/static evidence resolved |
| Submit | Traceable evidence package | Submission is complete and reviewable |
| Review | Code-review approval | Explicit merge verdict issued |

## Common Pitfalls

| Anti-pattern | Correct behavior |
|---|---|
| Wireframe reviewed, therefore UI passed | Treat it as decision approval; verify implementation later |
| CI green, therefore feature complete | Collect all required technical and design evidence |
| CSS/source inspection used as visual acceptance | Render affected output or mark NOT_VERIFIED |
| Design-review loaded for backend-only change | Record design as NOT_APPLICABLE |
| Specialized visual accepted with universal gates only | Load domain reviewer or block complete claim |
| Submit first and collect evidence during review | Resolve verification before submission |
| Peer review bypasses code-review-workflow | Use the evidence-backed workflow for merge verdict |
| Scope grows during implementation | Update and reapprove spec/design decision |
