# Event Schema and Contracts

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
