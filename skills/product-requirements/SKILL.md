---
name: product-requirements
description: Create, revise, review, and verify Product Requirements Documents (PRDs) for AI-native product development. Use when turning verified discovery, feature intent, user needs, constraints, and success metrics into a testable PRD, product scope, acceptance criteria, evidence plan, and readiness verdict. Do not use for conceptual PRD explanations, pre-PRD Product Brief ownership, technical architecture specifications, implementation planning alone, or release execution.
license: MIT
metadata:
  ai-native-skills.version: 1.2.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/product/product-requirements.contract.yaml
  ai-native-skills.contract-version: "~0.2"
  ai-native-skills.related_skills: '["business-value-alignment", "experiment-design", "product-manager", "user-research", "spec-workflow", "decision-provenance", "delivery-work-breakdown", "acceptance-testing", "observability-design"]'
---

# Product Requirements / PRD

Turn attributable product intent and sufficient upstream evidence into a bounded, testable product contract. `PRD` is the user-facing artifact; `product-requirements` is the single executable capability identity.

## Boundary and composition

```text
product-development-workflow Discovery
→ Product Brief from discovery/value/research composition
→ product-manager owns intent, value, scope authority, and product decisions
→ product-requirements authors/revises/reviews the PRD artifact
→ decision-provenance verifies approval and supersession claims
```

Do not create or prefer a second `prd` skill. Do not absorb Product Brief ownership from Discovery. Do not treat an agent-authored document as product-owner approval.

Use this capability for:

- PRD authoring from sufficient verified discovery or bounded feature intent;
- PRD revision with change and authority preservation;
- PRD readiness review;
- requirements, metrics, scope, acceptance criteria, evidence plan, and launch-criteria definition.

Do not use it for:

- explanation-only questions such as “Apa itu PRD?”;
- vague opportunity discovery or Product Brief production;
- technical architecture or API specifications (`spec-workflow`, `api-contract`);
- delivery topology or task decomposition alone (`delivery-work-breakdown`);
- release/deployment execution;
- approval claims unsupported by attributable authority.

## Required inputs and evidence classes

Required inputs remain:

```text
product or feature intent
target users
problem statement
```

Before authoring, classify every material input as one of:

```text
VERIFIED_EVIDENCE       attributable observation, research, decision, or result
INFERENCE               reasoned conclusion linked to evidence
ASSUMPTION              unverified belief being used temporarily
UNKNOWN                 unresolved information not safe to infer
DECISION                attributable choice with scope and authority
OBSERVED_IMPLEMENTATION current system state, not automatic product approval
```

Missing evidence is `NOT_VERIFIED`; never fill it with invented facts, metrics, deadlines, effort, demand, or approval.

## Intent, upstream readiness, and PRD profile

Classify the request before producing an artifact:

```text
AUTHOR       create a new product requirements artifact
REVISE       update an existing effective PRD
REVIEW       evaluate readiness without silently replacing the PRD
EXPLAIN      conceptual answer only; do not claim an artifact was produced
```

For `AUTHOR`, verify upstream readiness before selecting a PRD profile:

```text
vague opportunity, missing target user/problem, or materially weak discovery
  → route to product-development-workflow Discovery
  → produce/complete Product Brief through its governing composition
  → do not claim a PRD artifact or implementation authority

FEATURE_PRD
  bounded change inside an existing product with attributable parent context

FULL_PRODUCT_PRD
  new product, material MVP, or broad product contract with sufficient upstream intent
```

Load [prd-modes-and-lifecycle.md](references/prd-modes-and-lifecycle.md) for profile requirements, upstream handoff, document control, status semantics, and templates.

## Allowed outputs

Depending on intent and profile, produce one or more of:

```text
Feature PRD
Full Product PRD
requirements summary
scope boundary
acceptance criteria
success and guardrail metrics
risk and dependency list
open questions
analytics and evidence plan
launch-readiness criteria
revision change report
PRD readiness verdict
```

A Product Brief may be referenced as an upstream input, but is not an output of this capability.

## Authoring procedure

1. **Verify the source and upstream readiness.** Identify attributable intent, effective discovery/Product Brief inputs, evidence quality, and whether PRD authoring may begin. Route weak opportunities upstream instead of manufacturing readiness.
2. **Select the PRD profile.** Use Feature PRD for a bounded change with effective parent context; use Full Product PRD for a new product, material MVP, or broad contract.
3. **Frame the problem before the solution.** State the user or business outcome, affected users, current alternatives, and evidence. Move implementation ideas to constraints or downstream handoffs.
4. **Make value explicit.** State user value, business value, confidence, and unsupported assumptions.
5. **Define goals and non-goals.** Goals describe measurable outcomes; non-goals create explicit scope protection.
6. **Define measurable success.** Include a primary outcome metric, relevant activation/adoption metrics, guardrails, target/threshold, measurement method, and window when known.
7. **Bound scope.** Record scope-in and scope-out; include deferral or reconsideration triggers when useful.
8. **Describe the product journey.** Use user stories or jobs-to-be-done to connect situation, motivation, capability, and desired progress.
9. **Write stable requirements.** Assign IDs, state observable product behavior, and avoid technical implementation unless it is an attributable constraint.
10. **Classify non-functional requirements.** Address relevant quality domains or record an attributable `NOT_APPLICABLE` rationale. Load [non-functional-requirements.md](references/non-functional-requirements.md).
11. **Write acceptance criteria.** Use Given/When/Then or equivalent observable conditions and trace every criterion to requirements.
12. **Plan evidence.** Map goals, metrics, scope, requirements, acceptance criteria, verification method, and expected evidence. Load [requirements-and-evidence-traceability.md](references/requirements-and-evidence-traceability.md).
13. **Capture constraints, dependencies, risks, and unknowns.** Give open questions an owner or next decision when attributable; mark blockers explicitly.
14. **Define launch criteria.** Include product acceptance, analytics, observability, support, rollout/rollback, and applicable domain review—not only code completion.
15. **Run readiness gates.** Load [readiness-rubric.md](references/readiness-rubric.md) and return a reproducible verdict.
16. **Route authority.** Use `decision-provenance` for claims that the PRD, scope, deferral, risk, or downstream execution is approved.

## Minimum traceability contract

A ready Feature or Full Product PRD must support:

```text
source evidence / decision
→ goal
→ success or guardrail metric
→ scope item
→ requirement
→ acceptance criterion
→ verification method
→ expected or observed evidence
```

A missing link is either a named gap or a readiness failure. Do not represent an unverified future evidence item as observed proof.

## Revision procedure

When revising an existing PRD:

1. Identify the effective version and decision sources.
2. Separate requested edits from already accepted decisions.
3. Preserve accepted scope unless verified authority supersedes it.
4. Report content as `ADDED`, `CHANGED`, `REMOVED`, or `DEFERRED` with affected IDs.
5. Re-run value, metric, scope, NFR, traceability, risk, evidence, and launch-readiness gates.
6. Record the new artifact status and `supersedes` reference when applicable.
7. Keep the revised draft `NOT_APPROVED` until approval is attributable.

## Readiness review procedure

When reviewing rather than authoring:

1. Inspect the supplied or verified effective PRD.
2. Evaluate every applicable rubric dimension.
3. Separate `FAIL`, missing evidence, `NOT_APPLICABLE`, and approval status.
4. Return `READY`, `NEEDS REVISION`, or `BLOCKED` with concrete findings and one next action per blocker.
5. Do not silently rewrite unless revision is also requested.

## Readiness and approval states

```text
DRAFT          artifact is being authored
READY          applicable PRD quality gates pass
NEEDS_REVISION quality gaps exist but can be corrected in the artifact
BLOCKED        missing evidence, authority, or dependency prevents a valid contract
APPROVED       attributable product authority approved the exact scope/version
SUPERSEDED     a verified later decision or artifact replaced this version
```

`READY` is not `APPROVED`. `APPROVED` is not automatic implementation, release, deployment, or launch authorization.

## Handoffs

```text
weak opportunity evidence or incomplete Product Brief
  → product-development-workflow Discovery
  → user-research / experiment-design / business-value-alignment / product-manager

ready PRD, MVP scope unresolved
  → product-manager + product-development-workflow MVP Definition

technical solution or architecture required
  → implementation-context-discovery + spec-workflow

engineering slices, branches, or PR targets required
  → delivery-work-breakdown + git-workflow

acceptance evidence required
  → acceptance-testing / product acceptance reviewers
```

## Quality gates

- Request intent and PRD profile are explicit.
- Upstream discovery is sufficient for PRD authoring or the request is routed upstream without producing a false PRD.
- Problem statement is not a disguised solution.
- Target users and excluded users are explicit when relevant.
- User value, business value, evidence, assumptions, unknowns, and confidence are separated.
- Goals and non-goals both exist.
- Success and guardrail metrics are measurable or missing targets are named blockers.
- Scope-in and scope-out both exist.
- Requirements are stable-ID, observable, and testable.
- Relevant NFR domains are addressed or explicitly `NOT_APPLICABLE` with rationale.
- Acceptance criteria trace to requirements.
- Analytics and verification evidence are planned when metrics or runtime behavior require measurement.
- Constraints, dependencies, risks, and open questions are explicit.
- Launch criteria define readiness beyond implementation completion.
- Effective version, changes, authority, and supersession are explicit when revising durable artifacts.
- Implementation detail is excluded unless it is a verified constraint.
- Capability identity remains `product-requirements`; `PRD` remains the artifact alias.

## PRD readiness output

```yaml
prd_readiness:
  artifact_ref: ""
  profile: FEATURE_PRD | FULL_PRODUCT_PRD
  verdict: READY | NEEDS_REVISION | BLOCKED
  dimensions:
    problem_and_evidence: PASS | FAIL | NOT_VERIFIED | NOT_APPLICABLE
    users_and_value: PASS | FAIL | NOT_VERIFIED | NOT_APPLICABLE
    goals_metrics_and_scope: PASS | FAIL | NOT_VERIFIED | NOT_APPLICABLE
    functional_requirements: PASS | FAIL | NOT_VERIFIED | NOT_APPLICABLE
    non_functional_requirements: PASS | FAIL | NOT_VERIFIED | NOT_APPLICABLE
    acceptance_and_traceability: PASS | FAIL | NOT_VERIFIED | NOT_APPLICABLE
    risks_dependencies_and_unknowns: PASS | FAIL | NOT_VERIFIED | NOT_APPLICABLE
    analytics_and_evidence_plan: PASS | FAIL | NOT_VERIFIED | NOT_APPLICABLE
    launch_readiness: PASS | FAIL | NOT_VERIFIED | NOT_APPLICABLE
    lifecycle_and_provenance: PASS | FAIL | NOT_VERIFIED | NOT_APPLICABLE
  blockers: []
  next_actions: []
  approval:
    status: VERIFIED | NOT_VERIFIED | ROUTE_FOR_APPROVAL
    authority_ref: ""
```

## Hard stops

Return `BLOCKED`, preserve `NOT_VERIFIED`, or route upstream when:

- problem, target user, or attributable intent is missing;
- discovery/Product Brief evidence is too weak to support a product contract;
- high-risk assumptions are treated as facts;
- scope authority or supersession is claimed without provenance;
- measurable success cannot be defined and no evidence-gathering step is accepted;
- requirements or acceptance criteria cannot be observed or verified;
- a relevant safety, security, privacy, reliability, accessibility, or compliance domain is silently omitted;
- downstream implementation is requested while product intent remains materially ambiguous.

## Verification checklist

- [ ] Intent, upstream readiness, and PRD profile are classified.
- [ ] Weak opportunities are routed to Discovery/Product Brief ownership without producing a false PRD.
- [ ] Evidence, inference, assumptions, unknowns, and decisions are distinct.
- [ ] Document control and lifecycle are present when a durable PRD is requested.
- [ ] Problem, users, value, goals, non-goals, metrics, and scope are explicit.
- [ ] Functional requirements use stable IDs and observable behavior.
- [ ] Relevant NFRs are covered or explicitly not applicable.
- [ ] Acceptance criteria trace to requirements and verification evidence.
- [ ] Analytics/evidence plan supports claimed metrics and runtime acceptance.
- [ ] Risks, dependencies, unknowns, and launch criteria are explicit.
- [ ] Revision changes and authority are preserved.
- [ ] Readiness is not represented as approval.
- [ ] Technical specification and delivery topology are handed to their owners.
