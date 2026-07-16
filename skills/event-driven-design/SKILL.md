---
name: event-driven-design
description: Design event schema, producer/consumer contracts, saga patterns, and idempotency strategy for event-driven and async systems. Covers at-least-once delivery, dead letter queues, schema evolution, and CQRS flow.
version: 1.0.0
author: puterakahfi
license: MIT
type: skill
implements: ai-native-core/contracts/skills/domain-architecture/event-driven-design.contract.yaml
related_skills: [domain-driven-design, service-design, design-patterns, api-contract]
---

# Event-Driven Design

## When to Use

- Decoupling services that should not know about each other
- Long-running processes that span multiple services
- High-throughput write paths that need async processing
- Audit trail / event sourcing requirements
- Fan-out: one event triggers multiple downstream reactions

**Do NOT use** when caller needs immediate response, or when eventual consistency is not acceptable.

---

## Event Schema Design

### Naming Convention — Past Tense, Domain Meaningful

```
✅ OrderPlaced         ← something happened in Sales context
✅ PaymentProcessed    ← something happened in Payment context
✅ ItemsReserved       ← something happened in Inventory context
✅ ShipmentDispatched  ← something happened in Shipping context

❌ PlaceOrder          ← command, not event
❌ OrderUpdate         ← vague, not past tense
❌ UserEvent           ← meaningless, not domain-specific
```

### Event Envelope — Standard Schema

Every event must carry:

```json
{
  "eventId": "evt_01J5X...",
  "eventType": "order.placed",
  "eventVersion": "1.0",
  "occurredAt": "2026-07-16T10:00:00Z",
  "aggregateId": "ord_abc123",
  "aggregateType": "Order",
  "correlationId": "req_xyz789",
  "causationId": "cmd_place_order_456",
  "payload": {
    "orderId": "ord_abc123",
    "customerId": "cust_789",
    "items": [
      { "productId": "prd_001", "quantity": 2, "price": 4999 }
    ],
    "total": 9998,
    "currency": "USD"
  }
}
```

**Required fields:**
- `eventId` — globally unique, for idempotency
- `eventType` — dotted namespace: `{context}.{event_name}`
- `eventVersion` — schema version
- `occurredAt` — when it happened (not when published)
- `aggregateId` + `aggregateType` — what entity this is about
- `correlationId` — trace ID across service calls

---

## Schema Versioning + Evolution

### Backward Compatible Changes (safe)
```json
// v1.0
{ "orderId": "...", "total": 9998 }

// v1.1 — added optional field — backward compatible
{ "orderId": "...", "total": 9998, "currency": "USD" }
```

### Breaking Changes (require new version)
```
❌ Remove field consumers use
❌ Rename field
❌ Change field type
❌ Make optional field required
```

### Strategy: Schema Registry
- Register every event schema version
- Validate on publish, validate on consume
- Consumers declare which version(s) they support

---

## Producer Contract

Producer publishes — commits to schema stability within a version.

```yaml
# producer-contract: OrderService
produces:
  - event: order.placed
    version: "1.0"
    schema: schemas/order.placed.v1.0.json
    delivery: at-least-once
    broker: kafka/orders-topic

  - event: order.cancelled
    version: "1.0"
    schema: schemas/order.cancelled.v1.0.json
    delivery: at-least-once
    broker: kafka/orders-topic
```

---

## Consumer Contract + Idempotency

Consumers MUST be idempotent — at-least-once delivery means duplicates will arrive.

```php
class OrderPlacedConsumer
{
    public function handle(OrderPlaced $event): void
    {
        // Idempotency check — skip if already processed
        if ($this->processedEvents->contains($event->eventId)) {
            return;  // duplicate — safe to ignore
        }

        // Process
        $this->inventory->reserve($event->aggregateId, $event->payload['items']);

        // Mark as processed (in same transaction as business logic)
        $this->processedEvents->record($event->eventId);
    }
}
```

**Idempotency strategies:**
| Strategy | How |
|---|---|
| Processed event log | Store eventId in DB, check before processing |
| Natural key dedup | Business key (orderId + action) is unique constraint |
| Conditional update | `UPDATE ... WHERE status = 'PENDING'` — only applies once |

---

## Delivery Guarantees

| Guarantee | Meaning | Use When |
|---|---|---|
| At-most-once | May lose messages, never duplicate | Telemetry, non-critical notifications |
| At-least-once | May duplicate, never lose | Most business events — combine with idempotency |
| Exactly-once | Never lose, never duplicate | Financial transactions — expensive, use Outbox pattern |

---

## Outbox Pattern — Atomic Publish

**Problem:** Save to DB + publish to broker — what if broker fails after DB commit?

```
❌ Wrong:
  BEGIN TRANSACTION
  INSERT INTO orders ...
  COMMIT
  → publish OrderPlaced to Kafka  ← fails here → event lost forever
```

```
✅ Outbox:
  BEGIN TRANSACTION
  INSERT INTO orders ...
  INSERT INTO outbox (event_type, payload, status='PENDING') ...
  COMMIT
  ← background worker reads outbox → publishes → marks DELIVERED
  ← retry on broker failure — idempotent because eventId is stable
```

---

## Dead Letter Queue (DLQ)

Every consumer must define what happens when processing fails repeatedly.

```yaml
consumer:
  queue: inventory.order-placed
  max_retries: 3
  retry_delay: [5s, 30s, 5m]   # exponential backoff
  dlq: inventory.order-placed.dlq

# DLQ handler — alert + manual review
dlq_handler:
  alert: pagerduty/inventory-team
  retention: 7d
  replay_command: bin/replay-dlq.sh inventory.order-placed.dlq
```

---

## Saga Patterns

### Choreography Saga (event-driven, decentralized)

```
OrderService      → emits OrderPlaced
InventoryService  → listens OrderPlaced → reserves → emits ItemsReserved
PaymentService    → listens ItemsReserved → charges → emits PaymentProcessed
ShippingService   → listens PaymentProcessed → schedules → emits ShipmentScheduled

Failure: PaymentService fails
  → emits PaymentFailed
  → InventoryService listens PaymentFailed → emits ItemsReleased (compensation)
  → OrderService listens ItemsReleased → emits OrderCancelled (compensation)
```

**Use when:** Services are truly independent, choreography is simple enough to trace.

### Orchestration Saga (command-driven, centralized)

```
SagaOrchestrator:
  1. command ReserveItems → InventoryService
  2. on ItemsReserved: command ChargePayment → PaymentService
  3. on PaymentProcessed: command ScheduleShipment → ShippingService
  4. on failure: issue compensating commands in reverse order

State machine — tracks saga progress, handles timeouts
```

**Use when:** Complex flow with many services, need explicit saga state tracking.

---

## CQRS + Event Flow

```
Write side:
  Command → Handler → Aggregate → Domain Event → Event Store → Publish

Read side:
  Event → Projector → Read Model (denormalized view) → Query

Example:
  PlaceOrderCommand
    → OrderAggregate.place()
    → emits OrderPlaced
    → stored in EventStore
    → published to broker
    → OrderProjector handles OrderPlaced
    → updates orders_read_model table
    → GET /orders/{id} queries orders_read_model (fast)
```

---

## Event-Driven Design Checklist

Before publishing a new event:
- [ ] Event name is past tense and domain meaningful?
- [ ] Event envelope has all required fields (eventId, eventType, eventVersion, occurredAt)?
- [ ] Schema registered in schema registry?
- [ ] Producer contract documented?
- [ ] Consumer is idempotent (handles duplicate delivery)?
- [ ] Delivery guarantee declared?
- [ ] DLQ defined with retry + alert strategy?
- [ ] Saga compensation transactions defined (if multi-service transaction)?
- [ ] Outbox pattern used if exactly-once needed?
- [ ] Schema evolution strategy documented (backward compatible)?
