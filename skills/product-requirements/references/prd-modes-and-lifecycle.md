# PRD Profiles, Upstream Readiness, and Lifecycle

Load this reference after the request is classified as PRD authoring or revision.

## Upstream readiness boundary

A Product Brief is an upstream Discovery artifact, not a PRD profile and not an output of `product-requirements`.

```text
vague opportunity or weak problem/user evidence
  → product-development-workflow Discovery
  → user-research + business-value-alignment + experiment-design + product-manager
  → Product Brief
  → READY_FOR_PRD or EXPERIMENT_FIRST

sufficient upstream intent and evidence
  → product-requirements
  → Feature PRD or Full Product PRD
```

Do not use a thin PRD as a substitute for missing Discovery. Do not repeat a verified Product Brief when its effective source and decisions can be referenced.

## PRD profile selection

| Condition | Profile | Purpose |
|---|---|---|
| A bounded capability changes an existing product and effective parent context exists | `FEATURE_PRD` | Define a testable feature contract without repeating the whole product |
| A new product, material MVP, or broad product boundary is being defined with sufficient upstream intent | `FULL_PRODUCT_PRD` | Define the complete evidence, requirements, traceability, and readiness contract |

Use the smallest profile that preserves the decision. Do not inflate a narrow feature into a full-product document.

## Minimum sections by profile

### Feature PRD

```text
document control
attributable feature intent and parent references
affected users and current behavior
problem and evidence
user and business value
goals and non-goals
success, activation, and guardrail metrics
scope in and scope out
user journey or JTBD
functional requirements
relevant non-functional requirements
acceptance criteria
analytics and verification evidence plan
constraints, dependencies, risks, and unknowns
rollout or launch criteria
readiness and approval state
```

Inherited product decisions must reference an effective source. Do not silently duplicate or reinterpret them.

### Full Product PRD

Use all Feature PRD sections plus:

```text
product-level identity and version history
primary, secondary, and excluded users
current alternatives or market context when attributable
complete product journey and core workflows
MVP boundary inputs without deciding delivery topology
broader NFR applicability review
operational, support, and rollback readiness
end-to-end traceability matrix
supersession and decision-provenance references
```

## Document control

Durable Feature and Full Product PRDs should include:

```yaml
prd_control:
  id: PRD-<PRODUCT>-<SCOPE>-<NUMBER>
  title: ""
  profile: FEATURE_PRD | FULL_PRODUCT_PRD
  version: ""
  status: DRAFT | READY | NEEDS_REVISION | BLOCKED | APPROVED | SUPERSEDED
  product_owner: ""
  authors: []
  created_at: ""
  updated_at: ""
  source_intent_refs: []
  product_brief_refs: []
  parent_prd_refs: []
  decision_refs: []
  supersedes: ""
```

A missing owner, source, or date may remain `NOT_VERIFIED`; do not invent it.

## Lifecycle semantics

```text
DRAFT
  → READY when applicable quality gates pass
  → NEEDS_REVISION when artifact quality gaps remain
  → BLOCKED when evidence, dependency, or authority prevents a valid contract

READY
  → APPROVED only through attributable product authority
  → NEEDS_REVISION when review exposes quality gaps

APPROVED
  → SUPERSEDED only through an attributable later decision or approved artifact
  → remains effective until superseded, withdrawn, or invalidated by policy
```

The newest timestamp does not automatically define the effective PRD. Use `decision-provenance` when versions or authorities conflict.

## Feature PRD skeleton

```markdown
# PRD: <Feature>

## Document Control
<identity, version, status, owners, Product Brief/parent PRD/decision sources>

## Problem and Evidence
<problem, verified evidence, assumptions, unknowns, confidence>

## Target Users and Value
<affected users, user value, business value>

## Goals and Non-Goals
<measurable outcomes and protected exclusions>

## Success Metrics
<primary, activation/adoption, guardrails, measurement method/window>

## Scope
### In Scope
### Out of Scope

## User Journey / JTBD

## Functional Requirements
- REQ-1: <observable behavior>

## Non-Functional Requirements
- NFR-1: <quality behavior or NOT_APPLICABLE rationale>

## Acceptance Criteria
- AC-1: Given ... When ... Then ... [traces: REQ-1]

## Analytics and Evidence Plan
<metric events, verification methods, expected evidence>

## Constraints, Dependencies, Risks, and Unknowns

## Rollout / Launch Criteria

## Readiness and Approval
```

## Full Product PRD skeleton

Use the Feature PRD skeleton and add product-level users, alternatives, journey/workflow map, complete NFR review, MVP-boundary inputs, support/operations readiness, and an end-to-end traceability matrix.

## Revision change report

```yaml
prd_revision:
  effective_source: ""
  proposed_version: ""
  changes:
    added: []
    changed: []
    removed: []
    deferred: []
  affected_requirements: []
  affected_acceptance_criteria: []
  decision_refs: []
  approval_status: NOT_VERIFIED | ROUTE_FOR_APPROVAL | VERIFIED
```

A revision report describes change; it does not authorize it.
