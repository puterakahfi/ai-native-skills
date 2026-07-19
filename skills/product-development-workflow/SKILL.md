---
name: product-development-workflow
description: End-to-end digital product workflow from zero to launch — discovery, provenance-backed PRD and MVP decisions, technical specification, feature implementation, product acceptance, release readiness, delivery approval, launch, and learning.
license: MIT
metadata:
  ai-native-skills.version: 2.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.requires: "product-requirements business-value-alignment experiment-design user-research product-manager decision-provenance master-design master-engineer spec-workflow new-feature-workflow code-review-workflow design-review deployment-workflow observability-design"
  ai-native-skills.type: workflow
  ai-native-skills.implements: ai-native-core/contracts/workflows/product-development.contract.yaml
  ai-native-skills.contract-version: "~0.3"
  ai-native-skills.skill_load_order: '[{"phase":"discovery","load":["model-selection","user-research","business-value-alignment","experiment-design","product-manager","decision-making"]},{"phase":"requirements","load":["product-requirements","business-value-alignment","product-manager","decision-provenance"]},{"phase":"mvp_slice","load":["business-value-alignment","experiment-design","product-manager","decision-making","spike","decision-provenance"]},{"phase":"technical_spec","load":["spec-workflow","native-ai-engineer","master-engineer","api-contract","data-modeling","decision-provenance"]},{"phase":"implementation","load":["new-feature-workflow","test-driven-development","master-engineer","systematic-debugging"]},{"phase":"acceptance_verification","load":["skill-eval","code-review-workflow","decision-provenance"]},{"phase":"acceptance_domain_review","load":["design-review","security-review","threat-modeling","web-performance","accessibility"]},{"phase":"release","load":["git-workflow","deployment-workflow","decision-provenance"]},{"phase":"deploy","load":["deployment-workflow","observability-design","resilience-engineering","decision-provenance"]},{"phase":"launch","load":["business-value-alignment","product-manager","content-strategy","copywriting","cro","observability-design","decision-provenance"]},{"phase":"learn","load":["business-value-alignment","product-manager","observability-design","user-research","decision-making","decision-provenance"]}]'
---

# Product Development Workflow

Discovery → verified PRD → authorized MVP slice → technical spec → feature implementation → product acceptance → release readiness and approval → deploy → launch → learn.

## Core rules

```text
1. Use this workflow for a product from zero, not every product-related task.
2. Discovery precedes PRD when the opportunity is still vague.
3. PRD and MVP scope precede technical specification and implementation.
4. PRD readiness, MVP scope, scope removal, and accepted-risk claims require decision provenance.
5. Agent-authored PRD, issue, or status text is not owner approval by itself.
6. Implementation runs through new-feature-workflow boundaries.
7. Feature verification does not automatically prove product-level acceptance.
8. Every in-scope PRD criterion needs direct evidence and a matrix status.
9. User-facing changes require facade-backed design acceptance.
10. code-review-workflow technical APPROVED is required before release eligibility.
11. NOT_VERIFIED, missing reviewer coverage, provenance gaps, and hard-gate failures block release readiness.
12. RELEASE_READY is a quality state, not automatic permission to release.
13. Release, deploy, and launch actions require the approvals defined by product policy.
14. Release artifacts do not convert NOT_READY into RELEASE_READY.
15. Deployment is not launch; launch includes users, support, analytics, and feedback.
```

## Route boundary

```text
existing PRD/spec + implementation only → new-feature-workflow
bug or regression                       → bugfix-workflow
audit existing design only              → design-audit
known narrow design failures            → design-refinement
broad design replacement                → redesign-workflow
code/PR acceptance only                 → code-review-workflow
deployment only                         → deployment-workflow
```

Route by requested outcome, not merely words such as “audit”, “review”, or “polish”.

## Default behavior

For a vague idea with no requested stop point:

```text
discovery
→ PRD draft
→ MVP recommendation
→ decision-provenance check
→ stop for required approval
```

A generated PRD draft is not an approved PRD.

## Phase references

```text
Phases 1–5
  references/phases-1-5.md

Phases 6–10
  references/phases-6-10.md

Acceptance, accepted-risk authority, and release boundary
  references/acceptance-and-release.md

Formats, stop points, and pitfalls
  references/formats-pitfalls.md
```

Load `decision-provenance` whenever a PRD/MVP scope, scope removal, accepted risk, release, deployment, launch, or post-launch direction decision is asserted or changed.

## Phase overview

| # | Phase | Primary capability | Gate |
|---:|---|---|---|
| 1 | Discovery | research, value, experiment | Opportunity, value, assumptions, decision owners explicit |
| 2 | Requirements / PRD | product requirements + provenance | PRD readiness and scope authority pass |
| 3 | MVP Slice | prioritization + provenance | Smallest valuable slice explicitly approved |
| 4 | Technical Spec | spec workflow and engineering owners | Tasks trace to verified PRD/MVP criteria |
| 5 | Implementation | `new-feature-workflow` | Feature slices verified and inside scope |
| 6 | Product Acceptance | matrix + reviewers + provenance | Every in-scope criterion and risk reconciled |
| 7 | Release | release preparation | `RELEASE_READY` plus required release approval |
| 8 | Deploy | deployment and observability | Delivery approval and health verified |
| 9 | Launch | product, content, analytics, support | Launch approval and feedback loop live |
| 10 | Learn | metrics, research, decision making | Owned next action updates PRD/backlog |

## Decision provenance boundary

Verify claims such as:

```text
“the PRD is approved”
“this criterion is no longer in the MVP”
“the owner accepted this product risk”
“all merged features mean the product is ready”
“RELEASE_READY means release now”
“the latest report supersedes the previous decision”
```

```text
verified authoritative source covers the exact scope/action
  → decision may control the lifecycle

agent-authored artifact, merged code, or newest status is the only support
  → NON_AUTHORITATIVE or OBSERVED_IMPLEMENTATION_STATE
  → do not treat as approval

another required authority remains
  → ROUTE_FOR_APPROVAL

conflicting authoritative decisions lack explicit supersession
  → PROVENANCE_BLOCKED
```

Required policy approvals remain enforceable.

## Product acceptance boundary

Phase 5 may produce several technically approved feature submissions. Phase 6 still asks:

```text
Does the complete verified MVP satisfy every in-scope PRD criterion
with direct evidence, complete reviewer coverage, verified risk authority,
and no release blocker?
```

```yaml
product_acceptance:
  prd: <effective verified version>
  mvp_scope: <effective verified scope>
  decision_provenance_report: <reference>
  acceptance_matrix: <reference>
  code_review_verdicts: []
  domain_review_verdicts: []
  hard_gates: <status>
  release_blockers: []
  accepted_risks: []
  release_eligibility: <RELEASE_READY | NOT_READY>
  release_approval: <APPROVED | NOT_APPROVED | ROUTE_FOR_APPROVAL>
```

Load `references/acceptance-and-release.md` for the complete evidence, reviewer, risk, decision, and release contract.

## Release boundary

```text
RELEASE_READY
  quality state: verified MVP satisfies release criteria

release approval APPROVED
  permission state: required authority permits the release action

RELEASE_READY + APPROVED
  → release preparation may proceed

RELEASE_READY + ROUTE_FOR_APPROVAL
  → technically ready; stop before release action

NOT_READY or NOT_APPROVED
  → return to acceptance, implementation, verification, or decision resolution
```

Use the same separation for deployment and launch.

## Stop points

```text
after_discovery_recommendation
after_experiment_design
after_prd_draft
after_mvp_plan
after_technical_spec
before_release
before_deploy
before_launch
after_post_launch_review
```

`before_release` is reached only after Phase 6 returns `RELEASE_READY`; execution still requires the defined approval.

## Exit condition

The workflow is complete only when:

```text
launch occurred with required approval, monitoring, and feedback
post-launch evidence was reviewed
iterate / pivot / narrow / stop decision has an attributable owner
next PRD or backlog action is recorded
```

A release or deployment alone is not completion.
