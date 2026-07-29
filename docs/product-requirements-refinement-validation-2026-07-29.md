# Product Requirements Refinement Validation — 2026-07-29

## Scope

This record validates the adapter-level refinement tracked by issue #244 and draft pull request #245.

```yaml
repository: puterakahfi/ai-native-skills
branch: 244-refine-product-requirements
capability: product-requirements
operation: UPDATE
adapter_version: 1.2.0
core_contract: product-requirements@~0.2
primary_workflow: skill-authoring-workflow
validation_evidence_head: 12b1fb0d7b3aa62c32cb96eadbcb0201b743cbcc
```

This record does not change canonical Core ownership and does not claim merge, product approval, release readiness, or real-user product validation.

## Structural implementation

The refined capability adds:

- explicit upstream-readiness routing to Discovery/Product Brief ownership;
- Feature PRD and Full Product PRD profile selection;
- evidence, inference, assumption, unknown, decision, and implementation-state separation;
- document lifecycle and provenance semantics;
- stable requirement and acceptance-criterion traceability;
- analytics and verification evidence planning;
- conditional non-functional-requirement applicability;
- deterministic PRD readiness dimensions and blocking rules;
- centralized positive, negative, near-miss, revision, review, upstream-handoff, and downstream-handoff fixtures.

## Boundary correction found during self-review

The initial epic draft treated Product Brief as a PRD mode. Review against the canonical contract and product-development phase ordering showed that this would duplicate Discovery ownership.

```yaml
corrected_boundary:
  product_brief:
    owner: product-development-workflow Discovery composition
    status: upstream input to PRD
  product_requirements:
    profiles:
      - FEATURE_PRD
      - FULL_PRODUCT_PRD
    does_not_output:
      - Product Brief
```

The skill, reference, readiness rubric, tests, and epic decision record were corrected before acceptance. This is an observed self-review finding and fix, not a silent scope change.

## Realistic transfer case — LandingMate

### Provided product context

```yaml
product: LandingMate
original_idea: landing-page generator
problem: creating a good landing page is difficult for non-technical users
primary_user: non-technical users
expected_outcome: users can manage a website more easily
initial_mvp_scope: landing-page generator
constraints:
  - TDD
  - SOLID
  - modular monolith
  - Domain-Driven Design
research_evidence: NOT_VERIFIED
market_evidence: NOT_VERIFIED
success_metric_target: NOT_VERIFIED
approval_source: user product intent only
```

### Upstream and profile classification

```yaml
intent: AUTHOR
upstream_readiness: LIMITED
profile: FULL_PRODUCT_PRD
reason: >-
  LandingMate is a new product/material MVP rather than a bounded change to an
  effective existing product. The supplied intent, problem, and target user support
  a draft Full Product PRD, while missing research, metric targets, and platform/cost
  evidence remain explicit blockers to READY/APPROVED downstream execution.
```

A weaker request without problem or target-user context would route to Discovery/Product Brief instead of producing a PRD.

### Evidence classification

| Item | Classification | Rationale |
|---|---|---|
| Non-technical users struggle to create good landing pages | `ASSUMPTION` | Product intent states the problem, but attributable research is not provided |
| LandingMate should generate a landing page | `DECISION` | Explicit product direction from the owner |
| Users will manage websites more easily | `EXPECTED_OUTCOME` | Desired outcome, not observed evidence |
| TDD, SOLID, modular monolith, DDD | `CONSTRAINT` | Explicitly supplied engineering constraints; detailed design remains downstream |
| Activation target | `NOT_VERIFIED` | No baseline or approved target exists |
| Demand and willingness to use/pay | `UNKNOWN` | No market or user evidence supplied |

### Example traceability slice

```yaml
traceability:
  - source:
      type: product_intent
      ref: LandingMate supplied context
    goal: G-1
    metric: MET-1
    scope: S-IN-1
    requirement: REQ-1
    acceptance_criterion: AC-1
    verification:
      method: moderated_user_test_and_runtime_evidence
      expected_evidence: EV-1
      observed_evidence: NOT_RUN
```

```text
G-1
Non-technical users can obtain an editable landing-page draft without writing code.

MET-1
Activation/completion target: NOT_VERIFIED.
Next evidence action: establish a baseline and approved target through a prototype test.

S-IN-1
Generate one editable landing-page draft from supplied profile/business information.

REQ-1
The product provides an observable end-to-end flow from supplied information to an editable draft.

AC-1
Given a non-technical user has supplied the required information,
when they request a draft,
then the product returns an editable landing page containing the product-defined required sections
or an actionable recoverable error.

EV-1
Expected: runtime recording plus moderated-user-test evidence.
Observed: NOT_RUN.
```

### NFR applicability sample

| Domain | Status | Finding |
|---|---|---|
| Accessibility | `REQUIRED` | Primary users include non-technical users; interaction accessibility cannot be silently omitted |
| Reliability/recovery | `REQUIRED` | Generation failure must not discard supplied input |
| Performance | `NOT_VERIFIED` | No approved threshold or baseline exists |
| Privacy | `REQUIRED` | User-supplied profile/business information requires explicit handling expectations |
| Security | `REQUIRED` | Publication, editing, and user data boundaries require downstream review |
| Observability | `REQUIRED` | Activation and failure metrics need measurement evidence |
| AI provider cost/limits | `NOT_VERIFIED` | Generation surface and cost owner are not established in the supplied context |

### Readiness result

```yaml
prd_readiness:
  profile: FULL_PRODUCT_PRD
  verdict: BLOCKED
  dimensions:
    problem_and_evidence: NOT_VERIFIED
    users_and_value: PASS
    goals_metrics_and_scope: NOT_VERIFIED
    functional_requirements: PASS
    non_functional_requirements: NOT_VERIFIED
    acceptance_and_traceability: PASS
    risks_dependencies_and_unknowns: PASS
    analytics_and_evidence_plan: PASS
    launch_readiness: NOT_VERIFIED
    lifecycle_and_provenance: PASS
  blockers:
    - attributable user/problem evidence is missing
    - activation and success targets are not approved
    - generation surface, provider limits, and cost ownership are unresolved
    - product-owner approval covers direction but not a complete effective PRD version
  next_actions:
    - run the smallest prototype/user-evidence step before implementation authorization
    - define the generation/cost boundary during product and platform discovery
    - revise and route the effective PRD for attributable approval
  approval:
    status: ROUTE_FOR_APPROVAL
    authority_ref: NOT_VERIFIED
```

### Transfer verdict

```yaml
transfer_validation:
  capability_application: APPLIED
  semantic_improvement:
    upstream_boundary: OBSERVED
    profile_selection: OBSERVED
    evidence_discipline: OBSERVED
    traceability: OBSERVED
    nfr_applicability: OBSERVED
    false_approval_prevention: OBSERVED
  real_user_product_validation: NOT_VERIFIED
  interpretation: >-
    The refined procedure materially changes the PRD result by preserving weak
    evidence and unresolved product/platform boundaries instead of inventing
    targets or authorizing implementation. It also prevents product-requirements
    from taking over Product Brief ownership. This is a reviewed transfer example,
    not live runtime or real-user success proof.
```

## Acceptance reconciliation

| Criterion | Result | Evidence |
|---|---|---|
| AC-1 Upstream/profile classification | PASS | Skill procedure and centralized weak-opportunity, Feature PRD, and Full Product PRD fixtures |
| AC-2 Evidence discipline | PASS | Evidence classes, hard stops, LandingMate transfer classification |
| AC-3 Lifecycle and provenance | PASS | Document control, status/supersession guidance, revision fixture |
| AC-4 Testable product contract | PASS | Stable IDs, metrics, scope, requirements, acceptance procedure and fixtures |
| AC-5 NFR applicability | PASS | Conditional NFR reference and omission negative fixture |
| AC-6 Traceability and evidence plan | PASS | Dedicated reference, full-PRD fixture, transfer traceability slice |
| AC-7 Revision safety | PASS | Added/changed/removed/deferred procedure and authority regression fixture |
| AC-8 Review safety | PASS | Deterministic readiness rubric and no-silent-rewrite fixture |
| AC-9 Correct handoffs | PASS | Discovery/Product Brief upstream and spec/delivery downstream handoff fixtures |
| AC-10 Regression and conformance | PASS | Six required GitHub Actions workflows succeeded on evidence head |
| AC-11 Realistic transfer case | PASS | LandingMate transfer record preserves unsupported evidence as `NOT_VERIFIED` |

## Automated validation evidence

All pull-request workflows completed successfully on `12b1fb0d7b3aa62c32cb96eadbcb0201b743cbcc`:

```yaml
validation:
  skill_package_validation: PASS
  skill_pack_contracts: PASS
  skill_and_gate_contracts: PASS
  contract_coverage: PASS
  capability_inventory: PASS
  published_capability_catalog: PASS
```

Initial failures were inspected and corrected:

```yaml
fixed_failures:
  - fixture YAML parse failure caused by an unquoted colon-bearing trigger
  - stale contract-coverage inventory after adapter version bump
```

No failure was hidden or reclassified as PASS without a succeeding rerun.

## Review result

```yaml
review:
  contract_boundary_review: PASS
  architecture_ownership_review: PASS_AFTER_CORRECTION
  qa_and_eval_review: PASS
  documentation_review: PASS
  human_or_external_reviewer_approval: NOT_VERIFIED
  merge_authorization: NOT_VERIFIED
```

The architecture review correction preserved Product Brief ownership in Discovery. The canonical `product-manager` overlap remains a separate Core-level finding and was not silently changed.

## Capability evolution

```yaml
product_requirements_refinement:
  verdict: IMPROVEMENT
  target: ai-native-skills
  rationale: >-
    The existing capability remains valid, but its reusable executable methodology,
    upstream-readiness routing, profile selection, evidence discipline, NFR guidance,
    traceability, and semantic regression coverage were insufficient.

product_manager_prd_ownership_overlap:
  verdict: RFC
  target: ai-native-core
  action: HANDOFF_ONLY
  rationale: >-
    Canonical product-manager still declares PRD-authoring role/output. Changing
    that universal ownership boundary requires Core authority and is not silently
    implemented by this adapter patch.
```

## Final adapter verdict

```yaml
adapter_acceptance: PASS
pull_request_state: DRAFT_PENDING_FINAL_REVIEW_TRANSITION
merge_state: NOT_AUTHORIZED
real_product_validation: NOT_VERIFIED
```

The adapter implementation and automated gates are complete. Pull-request readiness and merge remain separate authorization states.
