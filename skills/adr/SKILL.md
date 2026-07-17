---
name: adr
description: Author and maintain Architecture Decision Records — context, options considered, decision, consequences, and tradeoffs. Immutable once accepted. Superseding pattern for changed decisions.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/architecture/adr.contract.yaml
  ai-native-skills.contract-version: "~0.1"
---

# Architecture Decision Record (ADR)

## When to Write an ADR

Write when the decision:
- Affects multiple teams or services
- Is hard or expensive to reverse
- Involves significant tradeoffs
- Will be questioned in the future

**Trigger words:** "we chose X over Y", "we decided not to use Z", "we will adopt pattern P".

---

## ADR Format

```markdown
# ADR-{NNN}: {Short Title}

**Status:** Proposed | Accepted | Deprecated | Superseded by ADR-{NNN}
**Date:** YYYY-MM-DD
**Deciders:** [names or teams]

## Context

<!-- Why was this decision needed? Specific forces/constraints — not "we wanted X"
     but "we have 50k events/min and our current queue drops messages under load" -->

## Options Considered

### Option A: {Name}
- Pro: ...
- Con: ...

### Option B: {Name}
- Pro: ...
- Con: ...

### Option C: {Name} (chosen)
- Pro: ...
- Con: ...

## Decision

We will use {Option C} because {one sentence rationale tied to context forces}.

## Consequences

### Positive
- ...

### Negative (tradeoffs — be honest)
- ...

### Risks
- ...

## References
- [Link to RFC, spike, or related ADR]
```

---

## Example ADR-001: Use Kafka for Order Events

```markdown
# ADR-001: Use Kafka for Order Events

**Status:** Accepted
**Date:** 2026-07-16
**Deciders:** platform-team, order-team

## Context

OrderService publishes events consumed by InventoryService, ShippingService,
and AnalyticsService. Peak load: 50k orders/hour. We need:
- Message replay (for reprocessing on consumer bug fix)
- Multiple independent consumers per event
- Retention > 7 days for audit trail

RabbitMQ (current) drops messages on consumer lag and has no replay capability.

## Options Considered

### Option A: RabbitMQ (current)
- Pro: team already familiar, low ops overhead
- Con: no replay, no consumer group independence, messages lost on lag

### Option B: AWS SQS + SNS
- Pro: fully managed, no ops
- Con: no replay, 14-day max retention, not multi-region

### Option C: Kafka (chosen)
- Pro: replay, consumer groups, configurable retention, high throughput
- Con: ops complexity, needs schema registry, learning curve

## Decision

We will use Kafka because replay and independent consumer groups are hard
requirements that neither RabbitMQ nor SQS satisfy.

## Consequences

### Positive
- Event replay enables safe consumer bug fixes
- Independent consumer lag — one slow consumer doesn't block others
- 30-day retention satisfies audit requirements

### Negative
- Kafka cluster ops overhead — need dedicated platform team ownership
- Schema registry required to prevent consumer breakage
- Local development setup more complex (docker-compose)

### Risks
- Schema evolution mismanagement → consumer failures. Mitigation: enforce schema registry in CI.
```

---

## Example ADR-002: Reject GraphQL, Use REST + OpenAPI

```markdown
# ADR-002: Reject GraphQL, Use REST + OpenAPI

**Status:** Accepted  **Date:** 2026-07-16

## Context

Frontend team requested GraphQL. Evaluated against team size (8 engineers),
consumer count (2 internal services, 1 mobile app), and backend expertise.

## Decision

REST + OpenAPI — GraphQL flexibility benefits don't justify complexity at our scale.

## Consequences

### Negative
- Less flexible querying — may need multiple endpoints
- N+1 query problem managed manually (no DataLoader)

### Positive
- Standard tooling (oasdiff, Pact, Swagger UI); mature contract testing ecosystem

**Revisit when:** consumer count exceeds 5 or frontend query flexibility becomes blocking.
```

---

## ADR Lifecycle

```
Proposed  → team reviewing, not yet committed
Accepted  → in effect, followed by the team
Deprecated → no longer recommended but not replaced
Superseded by ADR-NNN → replaced by a newer decision
```

**Immutability rule:** Once `Accepted`, never edit the body. Create a new ADR and set status to `Superseded by ADR-NNN`.

## Storage

```
docs/
└── adr/
    ├── ADR-001-kafka-for-order-events.md
    ├── ADR-002-rest-not-graphql.md
    └── README.md  ← index of all ADRs with status
```

---

## ADR Authoring Checklist

- [ ] Status declared explicitly?
- [ ] Context explains the forcing function (not just "we wanted X")?
- [ ] All options considered listed (minimum 2)?
- [ ] Decision stated in one sentence?
- [ ] Consequences include both positive AND negative tradeoffs?
- [ ] Risks identified?
- [ ] If superseding: old ADR updated with `Superseded by ADR-NNN`?
- [ ] Traceable to a real problem or constraint?

> **HARD RULE:** ADRs are immutable facts. Never edit an accepted ADR — supersede it.
