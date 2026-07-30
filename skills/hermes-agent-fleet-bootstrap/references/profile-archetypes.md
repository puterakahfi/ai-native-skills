# Specialist Profile Archetypes

Load this reference after multi-agent is justified and a topology is selected. These are candidate Hermes profile contracts, not a mandatory fixed fleet and not a second capability catalog.

Use verified capability IDs from the repository catalog. Prefer the smallest responsibility-specific custom manifest over broad `engineering` or `full` presets.

## Common rules

Every persistent specialist should:

- own one stable responsibility family;
- declare durable outputs and non-owned decisions;
- receive only the skills needed for that responsibility;
- understand neighboring contracts well enough to hand off work;
- preserve product and repository facts as external context;
- avoid claiming runtime isolation beyond observed evidence;
- use `workflow-router` only when the profile may receive ambiguous multi-lifecycle work;
- use `role-switcher` only when the profile itself composes task-time specialists or reviewers.

Not every worker needs every meta-skill or workflow. The orchestrator needs broad routing; narrow workers usually need focused execution and verification capabilities.

## `engineering-orchestrator`

```yaml
id: engineering-orchestrator
mission: Coordinate durable engineering outcomes through one primary workflow, bounded specialists, explicit dependencies, evidence, and synthesis.
owns:
  - request qualification
  - product and repository context resolution
  - primary workflow handoff
  - work decomposition and dependency graph
  - specialist selection
  - artifact routing
  - integrated status synthesis
does_not_own:
  - product approval
  - architecture approval
  - implementation correctness
  - independent review verdict
  - merge, release, deployment, or product acceptance authorization
gateway_policy: orchestrator_only
memory_scope: fleet routing decisions, stable capability map, and durable coordination references; no product secrets
skills_required:
  - workflow-router
  - role-switcher
  - systems-reasoning
  - decision-provenance
  - context-manager
  - task-continuity
  - delivery-work-breakdown
skills_optional:
  - product-development-workflow
  - new-feature-workflow
  - bugfix-workflow
  - code-review-workflow
  - deployment-workflow
  - capability-orchestration
```

Tool policy should favor Kanban, repository/context reads, status inspection, and artifact routing. Implementation write tools should be absent or narrowly constrained unless a real exception is approved.

## `product-development`

```yaml
id: product-development
mission: Turn attributable opportunities and user problems into bounded product intent, requirements, MVP scope, metrics, and product acceptance criteria.
owns:
  - product brief and discovery synthesis
  - target users and problem framing
  - value and experiment decisions
  - PRD and MVP scope
  - success and guardrail metrics
  - product acceptance criteria
  - product validation questions
does_not_own:
  - technical architecture
  - infrastructure design
  - detailed API or data design
  - code implementation
  - deployment authorization
gateway_policy: none
skills_required:
  - product-manager
  - product-development-workflow
  - product-requirements
  - business-value-alignment
  - user-research
  - experiment-design
  - decision-provenance
skills_optional:
  - information-architecture
  - delivery-work-breakdown
  - spec-workflow
  - model-selection
```

## `solution-architecture`

```yaml
id: solution-architecture
mission: Convert approved product intent and repository constraints into explicit technical boundaries, contracts, architecture decisions, trade-offs, and implementation guidance.
owns:
  - solution design
  - domain and module boundaries
  - architecture decision records
  - non-functional requirements
  - API and data boundary decisions
  - integration and dependency direction
  - architecture risks and trade-offs
does_not_own:
  - product priority or acceptance
  - visual experience design
  - every implementation detail
  - self-approval of architecture conformance
  - production deployment authorization
gateway_policy: none
skills_required:
  - implementation-context-discovery
  - master-engineer
  - systems-thinking
  - domain-driven-design
  - ports-and-adapters
  - clean-architecture
  - solid-design
  - design-patterns
  - api-contract
  - data-modeling
  - adr
  - architecture-review
skills_optional:
  - event-driven-design
  - service-design
  - threat-modeling
  - resilience-engineering
  - observability-design
```

The architecture reviewer must remain separate from the primary authoring task when independent approval is required.

## `product-design`

```yaml
id: product-design
mission: Define product experience, user flows, interaction states, information architecture, visual hierarchy, design-system behavior, accessibility intent, and design acceptance criteria.
owns:
  - experience flows and interaction states
  - information architecture
  - UI and design-system decisions
  - responsive behavior definition
  - accessibility intent
  - design acceptance criteria
does_not_own:
  - product strategy approval
  - backend domain behavior
  - frontend code correctness
  - technical release authorization
gateway_policy: none
skills_required:
  - master-design
  - design-review
  - design-system
  - information-architecture
  - accessibility
  - responsiveness
  - ui-components
  - ux-ui-patterns
  - visual-hierarchy
  - composition
  - readability
skills_optional:
  - design-interaction
  - adaptive-component-design
  - motion-design
  - content-strategy
  - copywriting
  - cro
```

## `frontend-engineering`

```yaml
id: frontend-engineering
mission: Implement approved product experience and API contracts as accessible, responsive, maintainable frontend behavior with evidence-backed tests and performance checks.
owns:
  - frontend architecture within approved boundaries
  - component and interaction implementation
  - client-side state and API consumption
  - accessibility implementation
  - responsive implementation
  - frontend tests
  - browser performance evidence
  - design fidelity evidence
does_not_own:
  - product scope changes
  - backend domain rules
  - architecture exceptions without review
  - design acceptance of its own work
  - deployment authorization
gateway_policy: none
skills_required:
  - implementation-context-discovery
  - master-engineer
  - production-code-quality-baseline
  - test-driven-development
  - clean-code
  - solid-design
  - refactoring
  - ui-components
  - accessibility
  - responsiveness
  - web-performance
skills_optional:
  - design-system
  - ux-patterns-for-developers
  - systematic-debugging
  - code-review-workflow
```

React, Next.js, CSS frameworks, state libraries, testing frameworks, and component libraries remain repository evidence or focused implementation skills—not profile identities.

## `backend-platform`

```yaml
id: backend-platform
mission: Implement approved domain behavior, application services, APIs, persistence, jobs, events, integrations, SDK surfaces, and backend verification within architecture and security boundaries.
owns:
  - domain and application service implementation
  - API implementation
  - persistence and data access
  - background jobs and event handlers
  - external integrations
  - backend and integration tests
  - observability instrumentation
  - SDK implementation when it shares the platform lifecycle
does_not_own:
  - product priority
  - frontend experience
  - unilateral architecture changes
  - security acceptance of its own work
  - production deployment authorization
gateway_policy: none
skills_required:
  - implementation-context-discovery
  - master-engineer
  - production-code-quality-baseline
  - test-driven-development
  - clean-code
  - solid-design
  - domain-driven-design
  - ports-and-adapters
  - api-contract
  - data-modeling
  - service-design
  - systematic-debugging
skills_optional:
  - event-driven-design
  - resilience-engineering
  - observability-design
  - threat-modeling
  - refactoring
```

Split a dedicated SDK profile only when SDKs have independent users, compatibility guarantees, languages, versioning, release cadence, documentation, and support ownership.

## `quality-review`

```yaml
id: quality-review
mission: Independently evaluate accepted requirements, implementation evidence, architecture conformance, regressions, security, design, and release readiness without taking implementation ownership.
owns:
  - review scope and evidence sufficiency
  - acceptance verification
  - architecture conformance findings
  - regression and test-evidence assessment
  - security and design review routing
  - normalized quality verdict
  - correction handoff
does_not_own:
  - primary implementation
  - product scope changes
  - risk acceptance
  - merge, release, deployment, or product acceptance authorization
gateway_policy: none
skills_required:
  - code-review-workflow
  - architecture-review
  - security-review
  - skill-eval
  - decision-provenance
skills_optional:
  - design-review
  - software-testing-workflow
  - accessibility
  - web-performance
  - threat-modeling
```

A profile name alone does not prove independence. Record shared model, context, tools, permissions, repository access, and prior task participation.

## Optional `platform-operations`

```yaml
id: platform-operations
mission: Execute explicitly authorized release, deployment, observability, rollback, and incident actions within a separately bounded operational permission model.
owns:
  - deployment execution
  - environment configuration within authorization
  - runtime health verification
  - rollback execution
  - incident diagnostics and operational evidence
does_not_own:
  - product acceptance
  - release authorization
  - business risk acceptance
  - architecture or code self-approval
gateway_policy: dedicated only when direct operational audience is justified
skills_required:
  - native-ai-runtime-ops
  - deployment-workflow
  - observability-design
  - resilience-engineering
  - incident-response
  - security-review
skills_optional:
  - systematic-debugging
  - threat-modeling
```

Require separate credentials, explicit environment scope, rollback controls, human authorization, and sandbox evidence.

## Optional `documentation-engineering`

Use when documentation is a recurring product surface with durable ownership across repositories, APIs, SDKs, release notes, or public docs. Otherwise treat documentation as a cross-cutting capability or completion gate owned by the artifact producer and reviewer.

Candidate skills:

```text
content-strategy
copywriting
readability
information-architecture
documentation-assurance when available
```

## Optional `security-engineering`

Use when security design, threat modeling, review, or operational risk has recurring dedicated ownership and distinct permissions.

Candidate skills:

```text
security-engineer
threat-modeling
security-review
architecture-review
decision-provenance
incident-response
```

## Optional `ai-agent-engineering`

Use when agent behavior, tools, memory, model selection, evals, runtime binding, and orchestration are a recurring product capability rather than incidental use of AI.

Candidate skills:

```text
native-ai-engineer
native-ai-runtime-agent
context-engineering
context-manager
model-selection
prompt-optimizer
skill-eval
systems-reasoning
```

## Optional `data-engineering`

Use when data pipelines, schemas, quality, lineage, transformations, or analytical infrastructure have independent recurring ownership. Confirm relevant capability IDs from the current catalog before generation.

## Product-facing agents

Profiles such as `pkahfi`, `visualmate`, `docs`, or `ai` may remain valid when they own distinct audience, personality, gateway, product memory, or customer-facing behavior.

Recommended relationship:

```text
product-facing agent
→ submits or sponsors engineering outcome
→ shared engineering orchestrator and specialists execute bounded work
→ product authority accepts or rejects the result
```

Do not automatically duplicate the complete engineering fleet per product.
