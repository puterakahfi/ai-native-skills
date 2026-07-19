---
name: new-feature-workflow
description: Evidence-backed new feature workflow — verify scope and decision authority, approve design decisions, implement with tests, verify technical and rendered outcomes, submit a decision ledger, and merge only through code-review-workflow approval plus merge authorization.
license: MIT
metadata:
  ai-native-skills.version: 2.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.requires: "master-engineer master-design decision-provenance spec-workflow test-driven-development code-review-workflow design-review"
  ai-native-skills.type: workflow
  ai-native-skills.implements: ai-native-core/contracts/workflows/new-feature.contract.yaml
  ai-native-skills.contract-version: "~0.4"
  ai-native-skills.skill_load_order: '[{"phase":"plan","load":["master-engineer","decision-provenance"]},{"phase":"design-decision","load":["master-engineer","diagram-architect","master-design","decision-provenance"]},{"phase":"implement","load":["master-engineer","test-driven-development"]},{"phase":"verify","load":["design-review","decision-provenance"]},{"phase":"submit","load":["decision-provenance"]},{"phase":"review","load":["code-review-workflow"]}]'
  ai-native-skills.skills: '{"required":["master-engineer","decision-provenance","test-driven-development","code-review-workflow"],"optional":["diagram-architect","master-design","design-review"]}'
---

# New Feature Workflow

Plan verified scope → approve decisions → implement → verify → submit decision/evidence handoff → technical review and merge authorization.

## Core boundary

```text
Spec before implementation.
Decision authority before material scope or lock changes.
Design decision before implementation when affected.
Rendered acceptance after implementation when user-facing output changes.
Code-review technical approval + merge authorization before merge.
```

A wireframe or specification decides what to build. It does not prove the implemented result. A technical review verdict does not automatically prove the responsible authority permits merge.

## Hard rules

```text
1. Define the problem, effective verified scope, acceptance criteria, and affected domains before coding.
2. Material scope, lock, dependency, exception, and approval claims require decision provenance.
3. Agent-authored issue/spec/PR text is not owner approval by itself.
4. Separate pre-implementation design decision from post-implementation acceptance.
5. Never claim implemented PASS from a wireframe, diagram, or source-only artifact.
6. Implementation must trace to verified scope and decisions.
7. A new route, product dependency, data boundary, permission behavior, or material lock change requires explicit bounded approval.
8. Write tests as part of implementation.
9. User-facing or generated visual changes require fresh rendered/exported evidence.
10. Source-only evidence cannot approve changed visual or interaction behavior.
11. LIMITED REVIEW cannot authorize complete specialist-domain acceptance.
12. Conditional acceptance requires verified non-blocking risk authority.
13. Submit spec, issue, decision ledger, technical evidence, and applicable design evidence together.
14. Final technical review and merge authorization belong to code-review-workflow.
15. Do not bundle unrelated or unapproved changes.
```

## When to use

Use when adding a new capability to an existing product or codebase.

```text
product from zero        → product-development-workflow
bug or regression        → bugfix-workflow
broad design replacement → redesign-workflow
known narrow design fix  → design-refinement
review-only request      → code-review-workflow or design-audit
```

## Workflow context

Record before implementation:

```yaml
feature:
  title: <title>
  problem: <problem>
  issue_ref: <issue or task>

  decision_sources: []
  required_authorities: []
  previous_decision_records: []

  effective_verified_scope:
    scope_in: []
    scope_out: []
    approved_dependencies: []
    preserved_routes_or_boundaries: []

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
  merge_authority: <role or policy>
```

## Phase 1 — Plan

**Gate:** spec, affected domains, scope provenance, and verification plan exist before implementation.

Define:

```text
problem and intended outcome
scope in and scope out
observable acceptance criteria
technical approach
architecture, logic, data, security, and design impact
issue tracker reference
verification and evidence plan
decision sources and required authorities
```

Run `decision-provenance` for the initial feature scope and any claimed approval. An agent-authored issue or generated spec is not automatically an approved system of record.

Replace vague criteria such as “works correctly” with behavior, context, and expected result.

**Done when:** scope, affected domains, criteria, issue, verification plan, and authoritative decision records are explicit.

## Phase 2 — Design decision

**Gate:** applicable architecture/design decisions have verified authority before implementation.

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
master-engineer       architecture, contracts, data, integration
master-design         task flow, component model, responsive behavior, visual direction
diagram-architect     decision-bearing diagrams when useful
decision-provenance   authority, scope, supersession, unresolved approval
specialized owner     domains outside built-in product UI/visual communication
```

Load `references/design-decision-and-acceptance.md` for the decision schema, evidence boundary, risk provenance, and handoff.

**Done when:** the verified approval boundary, required states/contexts, locks, assumptions, and implementation-ready criteria are explicit.

## Phase 3 — Implement

**Gate:** implementation traces to effective verified scope and approved decisions.

Load `master-engineer` and `test-driven-development`.

```text
implement one approved slice at a time
write tests at the relevant boundary
trace changed paths/behavior to acceptance criteria
preserve declared design, content, route, and asset locks
keep unrelated cleanup outside the submission
```

When implementation needs material scope or decision change:

```text
stop the affected slice
→ run decision-provenance
→ reapprove or route for approval
→ update spec, evidence plan, and traceability
→ continue only after the relevant authority gate passes
```

Existing implementation does not retroactively approve the expansion.

**Done when:** scoped criteria are implemented with tests and no unapproved change is bundled.

## Phase 4 — Verify

**Gate:** technical evidence, applicable rendered acceptance, and accepted-risk provenance exist before submission.

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

Evidence boundary:

```text
rendered interactive → affected contexts, states, inputs, runtime, accessibility
rendered static      → final size, crop, fidelity, content, export
source-only          → rendered behavior remains NOT_VERIFIED
specialized domain   → load domain reviewer or block complete acceptance
backend-only         → Design acceptance: NOT_APPLICABLE
```

For `CONDITIONAL PASS` or another non-blocking exception, run `decision-provenance` against the product's accepted-risk authority. Missing authority is not an accepted risk.

**Done when:** technical evidence exists and every applicable design/risk verdict is resolved for the verified feature scope.

## Phase 5 — Submit

**Gate:** submission references spec, issue, decision ledger, scope, and evidence.

Include:

```text
what changed and why
spec and issue reference
effective verified scope and excluded scope
authoritative decision-record IDs
acceptance-criteria checklist
approved decision artifacts and locks when applicable
implementation diff and technical evidence
design-review route, verdict, findings, and gaps when applicable
accepted risks with authority, owner, mitigation, and expiry when required
confirmation that unrelated/unapproved changes are absent
```

Use the handoff schema in `references/design-decision-and-acceptance.md`.

Do not submit as design-complete while rendered evidence remains `NOT_VERIFIED`. Do not claim “owner approved” without an attributable decision source.

**Done when:** the submission is traceable, provenance-backed, evidence-backed, and ready for independent review.

## Phase 6 — Review

**Gate:** explicit `code-review-workflow` technical approval and merge authorization before merge.

Pass the complete feature handoff to `code-review-workflow`. It returns:

```text
Technical review:
  APPROVED | REQUEST CHANGES | BLOCKED

Merge authorization:
  AUTHORIZED | NOT_AUTHORIZED | ROUTE_FOR_APPROVAL
```

```text
APPROVED + AUTHORIZED
  → eligible to merge under product policy

APPROVED + ROUTE_FOR_APPROVAL
  → technically ready, but do not merge yet

REQUEST CHANGES / BLOCKED / NOT_AUTHORIZED
  → return to implementation, verification, or authority resolution
```

A feature-level `NEEDS WORK`, `CRITICAL`, `LIMITED REVIEW`, `ROUTE ELSEWHERE`, or provenance blocker cannot be downgraded to a non-blocking merge flag.

**Done when:** technical reviewers approve, merge authority is verified, and the submission is merged according to product policy.

## Quick reference

| Phase | Primary gate | Done when |
|---|---|---|
| Plan | Spec + scope provenance | Scope, criteria, issue, authorities, verification plan explicit |
| Design decision | Decision authority | Boundary, contexts, states, locks, and owner records explicit |
| Implement | Traces to verified scope | Criteria implemented with tests and no silent expansion |
| Verify | Evidence + risk authority | Technical/design evidence and conditional risks resolved |
| Submit | Complete decision/evidence handoff | Submission is traceable and reviewable |
| Review | Technical + authority gates | Explicit merge authorization issued |

## Common pitfalls

| Anti-pattern | Correct behavior |
|---|---|
| Agent-generated issue means scope approved | Verify attributable owner/system-of-record acceptance |
| Existing route means it belongs to the feature | Existing state does not establish current scope |
| Wireframe reviewed, therefore UI passed | Treat it as a decision; verify implementation later |
| CI green, therefore feature complete | Collect all required technical and design evidence |
| CSS/source inspection used as visual acceptance | Render the output or mark NOT_VERIFIED |
| Specialist visual accepted with universal gates | Load domain reviewer or block complete acceptance |
| Conditional PASS without risk authority | Route to accepted-risk authority |
| Submit first, collect evidence during review | Resolve verification before submission |
| Technical approval means merge now | Wait for explicit merge authorization |
| Scope grows during implementation | Stop, verify provenance, and reapprove the boundary |
