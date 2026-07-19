---
name: product-development-workflow
description: End-to-end digital product workflow from zero to launch — discovery, PRD, MVP slice, technical specification, feature implementation, product-level acceptance matrix, release, deployment, launch, and learning.
license: MIT
metadata:
  ai-native-skills.version: 2.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.requires: "product-requirements business-value-alignment experiment-design user-research product-manager master-design master-engineer spec-workflow new-feature-workflow code-review-workflow design-review deployment-workflow observability-design"
  ai-native-skills.type: workflow
  ai-native-skills.implements: ai-native-core/contracts/workflows/product-development.contract.yaml
  ai-native-skills.contract-version: "~0.2"
  ai-native-skills.skill_load_order: '[{"phase":"discovery","load":["model-selection","user-research","business-value-alignment","experiment-design","product-manager","decision-making"]},{"phase":"requirements","load":["product-requirements","business-value-alignment","product-manager"]},{"phase":"mvp_slice","load":["business-value-alignment","experiment-design","product-manager","decision-making","spike"]},{"phase":"technical_spec","load":["spec-workflow","native-ai-engineer","master-engineer","api-contract","data-modeling"]},{"phase":"implementation","load":["new-feature-workflow","test-driven-development","master-engineer","systematic-debugging"]},{"phase":"acceptance_verification","load":["skill-eval","code-review-workflow"]},{"phase":"acceptance_domain_review","load_on_demand":["design-review","security-review","threat-modeling","web-performance","accessibility"]},{"phase":"release","load":["git-workflow","deployment-workflow"]},{"phase":"deploy","load":["deployment-workflow","observability-design","resilience-engineering"]},{"phase":"launch","load":["business-value-alignment","product-manager","content-strategy","copywriting","cro","observability-design"]},{"phase":"learn","load":["business-value-alignment","product-manager","observability-design","user-research","decision-making"]}]'
---

# Product Development Workflow

Discovery → PRD → MVP slice → technical spec → implementation → product acceptance → release → deploy → launch → learn.

## Core Rules

```text
1. Use this workflow for a product from zero, not every product-related task.
2. Discovery precedes PRD when the opportunity is still vague.
3. PRD and MVP scope precede technical specification and implementation.
4. Implementation runs through new-feature-workflow boundaries.
5. Feature verification does not automatically prove product-level acceptance.
6. Every in-scope PRD acceptance criterion needs direct evidence and a matrix status.
7. User-facing changes require facade-backed design acceptance with appropriate evidence.
8. code-review-workflow APPROVED is required before release eligibility.
9. NOT_VERIFIED, missing reviewer coverage, and hard-gate failures block release.
10. Release artifacts do not convert NOT_READY into RELEASE_READY.
11. Deployment is not launch; launch includes users, support, analytics, and feedback.
12. Stop at declared approval and external side-effect boundaries.
```

## Route Boundary

Use this workflow when the user is developing a digital product from an idea with no approved PRD/MVP lifecycle yet.

Route elsewhere:

```text
existing PRD/spec + implementation only
  → new-feature-workflow

bug or regression
  → bugfix-workflow

audit an existing design without changing it
  → design-audit

known narrow design failures
  → design-refinement

broad design direction or structure replacement
  → redesign-workflow

code/PR acceptance only
  → code-review-workflow

deployment only
  → deployment-workflow
```

A request containing “audit”, “review”, or “polish” does not automatically belong to product development or redesign. Route by the requested outcome.

## Default Behavior

For a vague idea with no requested stop point:

```text
discovery
→ PRD draft
→ MVP recommendation
→ stop for approval
```

Do not jump directly into architecture or code.

## Phase References

Load references only when entering their phases:

```text
Phases 1–5
  references/phases-1-5.md

Phases 6–10
  references/phases-6-10.md

Product acceptance and release eligibility
  references/acceptance-and-release.md

Formats, stop points, and pitfalls
  references/formats-pitfalls.md
```

## Phase Overview

| # | Phase | Primary capability | Gate |
|---:|---|---|---|
| 1 | Discovery | user research, value alignment, experiment design | Opportunity and value explicit |
| 2 | Requirements / PRD | product requirements | PRD readiness passes |
| 3 | MVP Slice | prioritization and experiment decision | Smallest valuable slice approved |
| 4 | Technical Spec | spec workflow and engineering owners | Tasks trace to PRD criteria |
| 5 | Implementation | `new-feature-workflow` | Feature slices verified and reviewed |
| 6 | Product Acceptance | matrix + required domain reviewers | Every in-scope criterion reconciled |
| 7 | Release | git/release preparation | `RELEASE_READY` + notes/version/rollback |
| 8 | Deploy | deployment and observability | Health verified before launch |
| 9 | Launch | product, content, analytics, support | Users and feedback loop live |
| 10 | Learn | metrics, research, decision making | Next action updates PRD/backlog |

## Product Acceptance Boundary

Phase 5 may produce several approved feature submissions. Phase 6 still must answer:

```text
Does the complete approved MVP satisfy every in-scope PRD acceptance criterion
with direct evidence, complete reviewer coverage, and no release blocker?
```

Phase 6 output:

```yaml
product_acceptance:
  prd: <reference>
  mvp_scope: <reference>
  acceptance_matrix: <reference>
  code_review_verdicts: []
  domain_review_verdicts: []
  hard_gates: <status>
  release_blockers: []
  accepted_risks: []
  release_eligibility: <RELEASE_READY | NOT_READY>
```

Load `references/acceptance-and-release.md` for the complete matrix, evidence, reviewer, and verdict contract.

## Stop Points

```text
after_discovery_recommendation
after_experiment_design
after_prd_draft
after_mvp_plan
after_technical_spec
before_release
after_post_launch_review
```

`before_release` is reached only after Phase 6 returns `RELEASE_READY`. It is not reached merely because implementation or CI completed.

## One-Line Invocation

Planning mode:

```bash
hermes chat -s product-development-workflow -q \
  "Develop a digital product for affiliators from zero. Start with discovery and stop after the PRD/MVP recommendation for approval."
```

Full lifecycle:

```bash
hermes chat -s product-development-workflow -q \
  "Develop a digital product from zero to launch. Respect each approval gate and prove every acceptance criterion before release."
```

## Exit Condition

The workflow is complete only when:

```text
launch occurred with monitoring and feedback
post-launch evidence was reviewed
iterate / pivot / narrow / stop decision is explicit
next PRD or backlog action is recorded
```

A release or deployment alone is not completion.