# Behavioral Patterns

## Strategy
**Forces:** Multiple algorithms for the same operation, switchable at runtime.

```php
// Forces: different shipping rate calculators — flat, weight-based, zone-based
interface ShippingCalculator {
    public function calculate(Shipment $shipment): Money;
}

class FlatRateCalculator implements ShippingCalculator { /* ... */ }
class WeightBasedCalculator implements ShippingCalculator { /* ... */ }
class ZoneBasedCalculator implements ShippingCalculator { /* ... */ }

class ShippingService {
    public function __construct(private ShippingCalculator $calculator) {}

    public function getRate(Shipment $shipment): Money {
        return $this->calculator->calculate($shipment);
    }
}
```

---

## Observer / Event
**Forces:** One-to-many notification, decoupled reactions to domain events.

```php
// Forces: OrderPlaced must trigger inventory reserve, email, analytics — decoupled
class OrderPlacedListener {
    public function handle(OrderPlaced $event): void {
        $this->inventory->reserve($event->orderId);
        $this->mailer->sendConfirmation($event->customerId);
    }
}

// Dispatcher fires event — listeners are unknown to domain
$dispatcher->dispatch(new OrderPlaced($order->id(), $order->customerId()));
```

---

## Command
**Forces:** Encapsulate requests as objects — queue, log, undo support needed.

```php
// Forces: operations need to be queued, logged, retried
class PlaceOrderCommand {
    public function __construct(
        public readonly CustomerId $customerId,
        public readonly array $items,
        public readonly PaymentToken $paymentToken,
    ) {}
}

class PlaceOrderHandler {
    public function handle(PlaceOrderCommand $cmd): OrderId { /* ... */ }
}
```

---

## Specification
**Forces:** Complex, composable business rules that must be named and reused.

```php
// Forces: "eligible for discount" is complex and reused in multiple places
class EligibleForDiscountSpec {
    public function isSatisfiedBy(Customer $customer): bool {
        return $customer->isActive()
            && $customer->totalSpend()->isGreaterThan(Money::of(500, 'USD'))
            && !$customer->hasActiveDiscount();
    }
}

// Composable
$spec = new EligibleForDiscountSpec()
    ->and(new NotBlockedSpec())
    ->or(new LoyaltyMemberSpec());
```

---

## Architectural Patterns

### CQRS (Command Query Responsibility Segregation)
**Forces:** Read and write models have different scaling/complexity needs.

```
Write side:  Command → Handler → Aggregate → Domain Event → Write DB
Read side:   Query  → Read Model (denormalized) → Read DB (or cache)

When to use:
  ✅ Read/write ratio heavily skewed
  ✅ Read model needs different shape than write model
  ✅ Event sourcing
  ❌ Simple CRUD — massive over-engineering
```

### Saga (Distributed Transactions)
**Forces:** Multi-service transaction without 2PC — compensating transactions on failure.

```
Choreography Saga (event-driven):
  OrderService   → emits OrderCreated
  PaymentService → listens OrderCreated → charges → emits PaymentProcessed
  InventoryService → listens PaymentProcessed → reserves → emits ItemsReserved
  (on failure: each service emits failure event → previous steps compensate)

Orchestration Saga (command-driven):
  SagaOrchestrator → commands each service in sequence
  → handles failures → issues compensating commands
```

### Outbox Pattern
**Forces:** Database write + event publish must be atomic — no lost events.

```
Problem: save Order to DB ✓ → publish OrderPlaced to queue ✗ → event lost
Fix:     save Order + save OutboxEvent in SAME transaction
         Background worker reads OutboxEvent → publishes → marks delivered
```
