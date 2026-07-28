---
name: product-development-workflow
description: End-to-end digital product workflow from idea to validated product — Product Brief, PRD, MVP, experience and solution design, vertical-slice delivery, implementation, evidence-backed acceptance, release, deploy, launch, and real-user validation.
license: MIT
metadata:
  ai-native-skills.version: 3.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.requires: "product-requirements business-value-alignment experiment-design user-research product-manager delivery-work-breakdown decision-provenance master-design master-engineer native-ai-engineer chatgpt-app-development spec-workflow new-feature-workflow code-review-workflow design-review deployment-workflow observability-design"
  ai-native-skills.type: workflow
  ai-native-skills.implements: ai-native-core/contracts/workflows/product-development.contract.yaml
  ai-native-skills.contract-version: "~0.4"
  ai-native-skills.skill_load_order: '[{"phase":"discovery","load":["model-selection","user-research","business-value-alignment","experiment-design","product-manager","decision-making"]},{"phase":"requirements","load":["product-requirements","business-value-alignment","product-manager","decision-provenance"]},{"phase":"mvp_definition","load":["business-value-alignment","experiment-design","product-manager","delivery-work-breakdown","decision-making","spike","decision-provenance"]},{"phase":"product_experience_design","load":["information-architecture","master-design","design-foundation","accessibility","decision-provenance"]},{"phase":"solution_design","load":["implementation-context-discovery","spec-workflow","native-ai-engineer","master-engineer","api-contract","data-modeling","decision-provenance"]},{"phase":"delivery_planning","load":["delivery-work-breakdown","product-manager","decision-provenance"]},{"phase":"implementation","load":["new-feature-workflow","test-driven-development","master-engineer","systematic-debugging"]},{"phase":"acceptance_verification","load":["skill-eval","code-review-workflow","decision-provenance"]},{"phase":"acceptance_domain_review","load":["design-review","security-review","threat-modeling","web-performance","accessibility"]},{"phase":"release","load":["git-workflow","deployment-workflow","decision-provenance"]},{"phase":"deploy","load":["deployment-workflow","observability-design","resilience-engineering","decision-provenance"]},{"phase":"launch","load":["business-value-alignment","product-manager","content-strategy","copywriting","cro","observability-design","decision-provenance"]},{"phase":"product_validation_learning","load":["business-value-alignment","product-manager","observability-design","user-research","experiment-design","decision-making","decision-provenance"]}]'
---

# Product Development Workflow

Discovery and Product Brief → verified PRD → authorized MVP Definition → Product Experience Design → Solution Design → Delivery Planning → feature implementation → Product Acceptance → release readiness and approval → deploy → launch → Product Validation and Learning.

## Core rules

```text
1. Use this workflow for a product from zero, not every product-related task.
2. Discovery precedes PRD when the opportunity is still vague.
3. PRD and MVP scope precede technical specification and implementation.
4. PRD readiness, MVP scope, experience/design locks, material solution boundaries, scope removal, and accepted-risk claims require decision provenance.
5. Agent-authored PRD, issue, or status text is not owner approval by itself.
6. Define the core product experience before Solution Design when user or consumer interaction is material.
7. Inspect implementation context before material architecture or technology choices.
8. Run detailed Delivery Planning after sufficient Solution Design; prefer independently testable vertical outcomes.
9. Classify the release unit and approve hierarchy, base branches, and PR targets before implementation branches.
10. Implementation runs through new-feature-workflow boundaries.
11. Feature verification does not automatically prove product-level acceptance.
12. Every in-scope PRD criterion needs direct evidence and a matrix status.
13. User-facing changes require facade-backed design acceptance.
14. code-review-workflow technical APPROVED is required before release eligibility.
15. NOT_VERIFIED, missing reviewer coverage, provenance gaps, and hard-gate failures block release readiness.
16. RELEASE_READY is a quality state, not automatic permission to release.
17. Release, deploy, and launch actions require the approvals defined by product policy.
18. Release artifacts do not convert NOT_READY into RELEASE_READY.
19. Deployment is not launch; launch includes users, support, analytics, and feedback.
20. Specialized delivery platforms load their specialist capability without replacing this lifecycle.
21. Engineering verification, Product Acceptance, and real-user Product Validation are distinct evidence states.
22. The workflow is complete only after reviewed usage evidence produces an owned next action.
23. Specialized delivery platforms load their specialist capability without replacing this lifecycle.
24. For ChatGPT Apps, generation surface and cost ownership are product acceptance criteria when pricing or quota claims depend on them.
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
→ lightweight Product Brief
→ PRD draft
→ MVP recommendation
→ decision-provenance check
→ stop for required approval
```

A generated Product Brief or PRD draft is useful evidence, not owner approval.

For requests with sufficient verified upstream artifacts, enter the earliest incomplete phase rather than repeating completed work:

```text
verified PRD + approved MVP, no experience evidence
  → Product Experience Design

verified experience + solution design, no delivery topology
  → Delivery Planning

verified PRD/MVP/experience/solution/delivery plan
  → Implementation through new-feature-workflow
```

Direct entry never bypasses missing provenance, acceptance criteria, required design decisions, implementation context, or authorization.

## Phase references

```text
Phases 1–6
  references/phases-1-6.md

Phases 7–12
  references/phases-7-12.md

Acceptance, accepted-risk authority, and release boundary
  references/acceptance-and-release.md

Product Experience Design composition
  references/product-experience-design.md

Solution Design and technology selection composition
  references/solution-design-and-technology-selection.md

Delivery Planning and vertical-slice composition
  references/delivery-planning-and-vertical-slices.md

Product Validation and Learning composition
  references/product-validation-and-learning.md

Formats, stop points, and pitfalls
  references/formats-pitfalls.md
```

Load `decision-provenance` whenever a PRD/MVP scope, scope removal, accepted risk, release, deployment, launch, or post-launch direction decision is asserted or changed.

## Phase overview

| # | Phase | Primary capability | Gate |
|---:|---|---|---|
| 1 | Discovery and Product Brief | research, value, experiment | Problem, target user, outcome, value, signals, assumptions, evidence gaps, non-goals, and owners explicit |
| 2 | Requirements / PRD | product requirements + provenance | PRD readiness and scope authority pass |
| 3 | MVP Definition | prioritization + provenance | Smallest valuable end-to-end outcome and scope explicitly approved |
| 4 | Product Experience Design | information architecture + design composition | Core experience is understandable/evaluable or explicitly not applicable |
| 5 | Solution Design and Technical Specification | context discovery + spec and engineering owners | Material boundaries and technology decisions trace to verified inputs |
| 6 | Delivery Planning | `delivery-work-breakdown` + provenance | Vertical slices, dependencies, branches, PR targets, rollback, and evidence plan approved |
| 7 | Implementation | `new-feature-workflow` | Feature slices verified and inside scope |
| 8 | Product Acceptance | matrix + reviewers + provenance | Every in-scope criterion and risk reconciled |
| 9 | Release | release preparation | `RELEASE_READY` plus required release approval |
| 10 | Deploy | deployment and observability | Delivery approval and health verified |
| 11 | Launch | product, content, analytics, support | Launch approval and feedback loop live |
| 12 | Product Validation and Learning | usage evidence, research, decision making | Real-user evidence produces an owned next action |

## Delivery decomposition boundary

After sufficient Solution Design and before implementation, load `delivery-work-breakdown`. MVP Definition owns product scope; Delivery Planning owns engineering topology.

```text
single independently releasable slice
  → feature or standalone release unit may be valid

multiple dependent slices forming one MVP outcome
  → epic release unit
  → child PRs target the epic/integration branch
  → final epic PR targets the release branch after product acceptance
```

Equivalent trunk-based delivery is valid only with attributable default-safe activation, traceability, integrated acceptance, rollback, and release authorization. Child CI does not prove epic or product acceptance.

## Conditional platform specialists

Load platform specialists only when the product target requires them.

### ChatGPT App

When the product includes a ChatGPT App, Apps SDK integration, MCP-backed tools, or ChatGPT widget, load `chatgpt-app-development` during:

```text
Discovery / Requirements
  verify primary value, target ChatGPT surface, plan/workspace assumptions,
  generation surface, cost owner, data scope, and distribution intent

Technical Spec
  define MCP tools/resources, product-core boundary, widget/state model,
  native capability handoff, auth, security, deployment, and observability

Implementation
  execute through new-feature-workflow while keeping MCP/widget code as adapters

Product Acceptance
  verify actual ChatGPT runtime behavior, cost boundary, tool routing,
  auth/authorization, widget interaction, accessibility, privacy, and security

Release / Deploy / Launch
  re-check current official platform requirements, production endpoint health,
  publication metadata, pricing disclosures, support, and feedback loop
```

Use `native-ai-engineer` with it when domain contracts, runtime binding, adapter placement, or cross-module ownership are in scope.

The ChatGPT App specialist does not create a competing workflow and does not carry product-specific rules into reusable skills.

## Decision provenance boundary

Verify claims such as:

```text
“the PRD is approved”
“this criterion is no longer in the MVP”
“the owner accepted this product risk”
“all merged features mean the product is ready”
“RELEASE_READY means release now”
“the latest report supersedes the previous decision”
“native ChatGPT generation means the developer cannot be billed”
“this ChatGPT capability is available to every target user”
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

Phase 5 may produce several technically approved feature submissions on an epic/integration branch. Phase 6 still asks:

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

For a ChatGPT App whose pricing or product promise depends on user-owned native generation, the matrix must include direct evidence that:

```text
generation_surface = chatgpt-native
cost_owner = end-user-chatgpt or declared workspace
native handoff path does not call the developer model/image API client
pricing copy separates product subscription from ChatGPT plan requirements
capability availability and limits are not overclaimed
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
after_mvp_definition
after_product_experience_design
after_solution_design
after_delivery_plan
before_release
before_deploy
before_launch
after_product_validation_review
```

`before_release` is reached only after Phase 8 returns `RELEASE_READY`; execution still requires the defined approval.

## Exit condition

The workflow is complete only when:

```text
launch occurred with required approval, monitoring, and feedback
real-user Product Validation evidence was reviewed
iterate / pivot / narrow / stop decision has an attributable owner
next PRD or backlog action is recorded
```

A release or deployment alone is not completion.
