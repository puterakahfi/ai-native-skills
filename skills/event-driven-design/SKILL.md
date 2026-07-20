---
name: event-driven-design
description: Design event schema, producer/consumer contracts, saga patterns, and idempotency strategy for event-driven and async systems. Covers at-least-once delivery, dead letter queues, schema evolution, and CQRS flow.
license: MIT
metadata:
  ai-native-skills.version: 1.0.1
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/architecture/event-driven-design.contract.yaml
  ai-native-skills.contract-version: "~0.1"
  ai-native-skills.related_skills: '["domain-driven-design", "service-design", "design-patterns", "api-contract"]'
---

# Event-Driven Design

## Reviewed core contract interface

Source: `ai-native-core/contracts/skills/architecture/event-driven-design.contract.yaml` · compatible line: `~0.1`

```yaml
required_inputs:
- business_flow_or_domain_event
allowed_outputs:
- event_schema
- event_catalog_entry
- producer_consumer_contract
- saga_design
- dead_letter_queue_strategy
- idempotency_strategy
quality_gates:
- event_names_must_be_past_tense_and_domain_meaningful
- event_schema_must_be_versioned
- consumers_must_be_idempotent
- delivery_guarantee_must_be_explicit
- saga_must_define_compensating_transactions
- no_direct_db_sharing_between_producer_and_consumer
- dead_letter_queue_strategy_must_be_defined
- schema_evolution_must_be_backward_compatible
```

A saga is incomplete without compensating transactions. Producer and consumer may share a contract but must not share a database; delivery, idempotency, DLQ behavior, and schema evolution remain explicit.

Keep this interface synchronized with the pinned core contract. Exact declarations make ownership reviewable; they do not replace runtime, repository, architecture, test, or product evidence.


> **HARD RULES**
> - Events are immutable facts — always named in **past tense**
> - Event schema **must be versioned** — every envelope carries `eventVersion`
> - Consumers **must be idempotent** — at-least-once delivery means duplicates will arrive

## When to Use

- Decoupling services that should not know about each other
- Long-running processes that span multiple services
- High-throughput write paths that need async processing
- Audit trail / event sourcing requirements
- Fan-out: one event triggers multiple downstream reactions

**Do NOT use** when caller needs immediate response, or when eventual consistency is not acceptable.

---

## References

| Topic | File |
|---|---|
| Event Schema Design, Schema Versioning, Producer Contract, Consumer Contract + Idempotency | [references/event-schema-and-contracts.md](references/event-schema-and-contracts.md) |
| Delivery Guarantees, Outbox Pattern, DLQ, Saga Patterns, CQRS + Event Flow, Checklist | [references/delivery-saga-cqrs.md](references/delivery-saga-cqrs.md) |

---

## Quick Decision Guide

```
Need to decouple two services?        → Event-driven, see event-schema-and-contracts.md
Multi-service transaction?            → Saga (choreography or orchestration), see delivery-saga-cqrs.md
Exactly-once guarantee needed?        → Outbox pattern, see delivery-saga-cqrs.md
Consumer failing on duplicates?       → Idempotency strategies, see event-schema-and-contracts.md
Schema change in existing event?      → Schema versioning + registry, see event-schema-and-contracts.md
```
