# Phases 1–6: Discovery → Delivery Planning

## Phase 1 — Discovery and Product Brief

**Goal:** Understand the problem, target users, evidence quality, expected outcome, value, and likely decision owners before defining a solution.

Load: `user-research`, `business-value-alignment`, `experiment-design`, `product-manager`; add `model-selection` or `decision-making` when relevant.

Produce a lightweight Product Brief containing:

```text
problem and opportunity evidence
target users and jobs-to-be-done
pains, alternatives, and workarounds
expected outcome and user/business value
success signals
assumptions and evidence gaps
early non-goals
decision domains and likely owners
experiment recommendation when evidence is weak
```

**Gate:** the Product Brief makes the problem, target user, outcome, value, evidence quality, non-goals, and decision owners explicit before PRD.

An `EXPERIMENT_FIRST` verdict produces an experiment design before PRD or build.

---

## Phase 2 — Requirements / PRD

**Goal:** Convert the recommended opportunity into a testable product contract with verified scope authority.

Load: `product-requirements`, `product-manager`, `business-value-alignment`, `decision-provenance`.

Produce problem, users, value, goals/non-goals, metrics, scope, functional and non-functional requirements, stable acceptance-criterion IDs, constraints, risks, dependencies, open questions, launch criteria, evidence plan, and decision sources.

A PRD readiness verdict is not owner approval. Run `decision-provenance` before downstream execution.

**Gate:** PRD readiness and scope provenance pass before MVP Definition or downstream design.

---

## Phase 3 — MVP Definition

**Goal:** Select the smallest valuable end-to-end outcome or experiment and verify who approved it.

Produce:

```text
primary user/problem where applicable
core end-to-end workflow
MVP scope in/out
included and deferred acceptance criteria
success metric mapping
risks and assumptions
scope decision record IDs
```

Do not define detailed branch, PR, or task topology here. That belongs to Phase 6 after sufficient Solution Design.

**Gate:** the MVP is smaller than the full product, value-aligned, end-to-end usable/testable, and approved by the required authority.

---

## Phase 4 — Product Experience Design

**Goal:** Make the core user or consumer experience understandable and evaluable before technical solution design.

Compose existing design capabilities; do not create a duplicate design lifecycle. Scale outputs by product type, risk, and complexity.

Produce when applicable:

```text
user journey
core user flows
information architecture
screen or interaction map
wireframes, interaction specification, or prototype
default/loading/empty/error/success/permission states
responsive behavior
accessibility expectations
experience decisions and design locks
criterion-to-experience traceability
review/evidence route
```

API-only or non-visual products may mark visual artifacts `NOT_APPLICABLE`, but must still define consumer interaction and contract expectations.

**Gate:** the core MVP experience is understandable, testable, traceable, and reviewed or explicitly not applicable before Solution Design.

---

## Phase 5 — Solution Design and Technical Specification

**Goal:** Translate verified PRD, MVP, and experience decisions into an executable technical solution without guessing repository context.

Required flow:

```text
implementation-context discovery
→ domain/module boundaries
→ frontend/backend/data/API design
→ security, deployment, observability, and testing design
→ material technology decisions
→ executable technical specification
```

Load `implementation-context-discovery` before material architecture, dependency, stack, or repository-mapping decisions.

Produce architecture constraints, solution design, technology trade-offs, tasks/context packs, criterion traceability, evidence/runtime plan, reviewer plan, and approved dependency/exception records.

**Gate:** every material boundary and technology decision traces to verified product inputs, repository context, constraints, risks, alternatives, and authority.

---

## Phase 6 — Delivery Planning

**Goal:** Convert the approved MVP and sufficient Solution Design into independently testable delivery slices and authorized repository topology.

Load `delivery-work-breakdown` and `decision-provenance`.

Produce:

```text
release-unit classification
product / epic / feature / task hierarchy
vertical slices with observable outcomes
dependencies and critical path
branch base, integration branch, and PR targets
criterion-to-slice/task traceability
activation and rollback plan
verification and reviewer plan
```

Default slice:

```text
interface/UI + application/domain behavior + data/integration
+ tests + observability + acceptance evidence
```

Horizontal enabling work is valid only when tied to a consuming outcome and explicit dependency.

**Gate:** each slice produces an independently testable outcome, traces to verified criteria and solution decisions, and has approved delivery topology.
