# Topology and Classification Reference

Load this reference when deciding whether persistent multi-agent architecture is justified, classifying requested concepts, or selecting a collaboration topology.

## Multi-agent justification

A persistent specialist profile is justified when several of these are true:

- the responsibility is stable and recurring;
- it produces durable artifacts or decisions;
- it needs its own memory scope;
- it needs a materially different model policy;
- it needs distinct tools, credentials, or permissions;
- it receives durable Kanban work;
- it requires an independent evaluation policy;
- it has clear inputs, outputs, and handoffs;
- isolating its blast radius is operationally meaningful.

Multi-agent is normally not justified when:

- the work is occasional or temporary;
- one profile can load a focused skill for the task;
- the requested split is only by framework, library, pattern, or language;
- all proposed agents share the same context, tools, permissions, and outputs;
- the task is too sequential or too small to offset coordination cost;
- reviewer independence cannot be meaningfully improved;
- no durable handoff or ownership boundary exists.

## Coordination-cost assessment

Record at least:

```yaml
coordination_costs:
  context_transfer: LOW | MEDIUM | HIGH | NOT_VERIFIED
  artifact_versioning: LOW | MEDIUM | HIGH | NOT_VERIFIED
  conflicting_decisions: LOW | MEDIUM | HIGH | NOT_VERIFIED
  shared_workspace_collision: LOW | MEDIUM | HIGH | NOT_VERIFIED
  model_and_token_cost: LOW | MEDIUM | HIGH | NOT_VERIFIED
  runtime_operations: LOW | MEDIUM | HIGH | NOT_VERIFIED
```

A larger fleet must show a corresponding durable benefit. Agent count is not a success metric.

## Capability classification

### PROFILE

Use for a durable Hermes identity that owns a stable recurring responsibility, explicit outputs, memory scope, tools/permissions, and handoffs.

Examples:

```text
product-development
solution-architecture
product-design
frontend-engineering
backend-platform
quality-review
platform-operations
```

### SKILL

Use for a reusable method, technique, or expert lens that can be loaded by one or more profiles.

Examples:

```text
React or framework-specific implementation guidance
SOLID
domain-driven-design
design-patterns
test-driven-development
api-contract
accessibility
web-performance
```

### WORKFLOW

Use when ordered phases and gates are the main value.

Examples:

```text
product-development-workflow
new-feature-workflow
bugfix-workflow
code-review-workflow
deployment-workflow
```

### OVERLAY

Use for cross-cutting applicability, assurance, platform, or quality behavior that does not replace the primary lifecycle.

### REVIEWER

Use for an independent verification responsibility with explicit evidence, coverage, and verdict semantics.

### DELEGATED_SUBAGENT

Use for temporary isolated research, comparison, analysis, or bounded parallel work that does not need durable memory or persistent profile ownership.

### PRODUCT_CONTEXT

Use for product identity, repository facts, accepted architecture/design locks, credentials references, local policy, and product acceptance authority.

### NOT_JUSTIFIED

Use when the requested split adds no durable responsibility, security, context, or quality benefit.

## Technology-name normalization

```text
react-agent
→ frontend-engineering profile + React implementation skill/context

ddd-agent
→ solution-architecture profile + domain-driven-design skill

tdd-agent
→ implementation/review profiles + test-driven-development skill

api-agent
→ backend-platform or solution-architecture responsibility depending on output ownership

sdk-agent
→ backend-platform skill initially; split only when SDK has independent users, compatibility policy, versioning, release, and support ownership
```

## Supported topologies

### `single_profile`

```text
user
→ one profile
→ skills/workflows loaded as needed
```

Use for narrow responsibility, low task volume, shared permissions, or an early validation stage.

### `orchestrator_with_specialists`

```text
user/front door
→ orchestrator
→ selected specialists
→ reviewer
→ orchestrator synthesis
```

Default for a durable engineering fleet. The orchestrator owns decomposition, routing, dependency tracking, and synthesis—not every specialist decision.

### `reviewer_loop`

```text
producer
→ reviewer
→ correction route
→ reviewer
```

Use where artifact quality needs explicit iterative verification.

### `parallel_specialists`

```text
orchestrator
├── independent work item A
├── independent work item B
└── independent work item C
```

Use only when tasks have explicit boundaries, separate workspaces or non-conflicting artifacts, and a later integration owner.

### `product_agents_with_shared_engineering_fleet`

```text
product-facing agents
├── pkahfi
├── visualmate
├── docs
└── ai
      ↓ request durable engineering work
shared engineering orchestrator and specialists
```

Use when app-facing agents have distinct identity, audience, gateway, or memory, while engineering capabilities are reusable across products.

### `operations_isolated_fleet`

```text
engineering fleet
→ release authorization
→ isolated platform-operations profile
→ environment health evidence
```

Use where production credentials, blast radius, rollback, incident response, or environment access require a separate security boundary.

## Topology selection rules

1. Select the smallest topology that can own the required outputs and gates.
2. Exactly one default orchestration owner is required for a durable engineering fleet.
3. Product-facing identity does not automatically own engineering methodology.
4. Specialists communicate through task and artifact contracts, not unrestricted conversation.
5. Parallelism requires independence evidence.
6. Review loops must have correction ownership and termination conditions.
7. Operations access requires separate permission and approval policy.
8. Unsupported runtime behavior remains `NOT_VERIFIED`.

## Anti-patterns

- One profile per framework or method.
- Every profile receives the full skill suite.
- Every profile receives a dedicated bot without a separate audience.
- All agents read all conversations and files by default.
- Orchestrator silently implements every task.
- Reviewer is the same sole implementer with a renamed profile.
- Product agents are deleted merely because shared engineering specialists exist.
- Multi-agent is selected before estimating coordination cost.
