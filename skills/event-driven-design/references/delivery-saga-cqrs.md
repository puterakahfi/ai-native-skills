# Delivery, Saga, and CQRS Patterns

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
