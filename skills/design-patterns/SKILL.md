---
name: design-patterns
description: Identify and apply appropriate design patterns — GoF creational, structural, behavioral, and modern architectural patterns (CQRS, Saga, Outbox). Pattern selection justified by forces, not preference.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/domain-architecture/design-patterns.contract.yaml
---

# Design Patterns

## The Core Rule

```
Pattern selection must be justified by forces, not preference.

Forces = the problem pressures that make a pattern the right fit.
Without forces → no pattern. Impose a pattern without forces = over-engineering.
```

---

## Pattern Selection Process

```
1. Name the problem in one sentence
2. Identify the forces (why naive solution fails)
3. Consider 2-3 candidate patterns
4. Pick the one whose forces match closest
5. State the trade-offs explicitly
6. Implement — name the pattern in code
```

---

## Creational Patterns

### Factory Method
**Forces:** Object creation logic is complex, or caller should not know the concrete type.

```php
// Forces: different notification types, caller should not decide which class
interface Notification {
    public function send(string $message): void;
}

abstract class NotificationFactory {
    abstract public function create(): Notification;

    public function notify(string $message): void {
        $this->create()->send($message);
    }
}

class EmailNotificationFactory extends NotificationFactory {
    public function create(): Notification {
        return new EmailNotification($this->config);
    }
}
```

**When NOT to use:** Single concrete type, creation is trivial → just `new`.

### Builder
**Forces:** Object construction requires many optional parameters, or order matters.

```php
// Forces: QueryBuilder — many optional clauses, order matters, fluent API needed
$query = QueryBuilder::for(User::class)
    ->where('active', true)
    ->with(['orders'])
    ->orderBy('created_at', 'desc')
    ->paginate(25);
```

**When NOT to use:** < 4 constructor parameters → just use constructor.

### Singleton
**Forces:** Exactly one instance must exist (config, connection pool).

⚠️ **Use sparingly.** Singletons make testing hard. Prefer dependency injection container.

---

## Structural Patterns

### Adapter
**Forces:** Incompatible interfaces must work together — legacy system, third-party lib.

```php
// Forces: legacy payment processor has different interface than our PaymentGateway port
class LegacyPaymentAdapter implements PaymentGateway
{
    public function __construct(private LegacyPaymentProcessor $legacy) {}

    public function charge(Money $amount, PaymentToken $token): PaymentResult
    {
        // translate our domain types to legacy types
        $legacyResult = $this->legacy->processPayment(
            amount: $amount->toCents(),
            token: $token->toString(),
            currency: $amount->currency()->code()
        );
        return PaymentResult::fromLegacy($legacyResult);
    }
}
```

### Decorator
**Forces:** Add responsibilities to objects without subclassing, composable behaviors.

```php
// Forces: add logging, caching, retry to repository without modifying it
class CachingOrderRepository implements OrderRepository
{
    public function __construct(
        private OrderRepository $inner,
        private Cache $cache
    ) {}

    public function findById(OrderId $id): ?Order
    {
        return $this->cache->remember(
            key: "order:{$id}",
            ttl: 300,
            callback: fn() => $this->inner->findById($id)
        );
    }
}

// Compose: Caching(Logging(Eloquent())) — each adds one responsibility
```

### Facade
**Forces:** Simplify a complex subsystem for common use cases.

```php
// Forces: checkout involves payment, inventory, notification, order — hide complexity
class CheckoutFacade
{
    public function checkout(Cart $cart, PaymentToken $token): OrderId
    {
        $order = $this->orderService->createFromCart($cart);
        $this->paymentService->charge($order->total(), $token);
        $this->inventoryService->reserve($order->items());
        $this->notificationService->confirmOrder($order);
        return $order->id();
    }
}
```

---

## Behavioral Patterns

### Strategy
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

### Observer / Event
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

### Command
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

### Specification
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

---

## Anti-Patterns to Catch

| Anti-Pattern | Signal | Correct Pattern |
|---|---|---|
| Pattern worship | "Let's use CQRS" without stating forces | Justify by forces first |
| God Object | One class does everything | SRP + Strategy/Facade decomposition |
| Anemic Model | Entities with only getters/setters, logic in services | Move logic to entities |
| Premature abstraction | Interface with one implementation | Wait for second implementation |
| Singleton abuse | Singleton for non-singleton concern | DI container binding |
| Leaky abstraction | Adapter exposes internal types | Translate to domain types at boundary |

---

## Pattern Selection Cheat Sheet

| Problem | Candidate Patterns |
|---|---|
| Need different algorithm at runtime | Strategy |
| Incompatible interface to integrate | Adapter |
| Add behavior without subclassing | Decorator |
| Complex object construction | Builder |
| Notify multiple objects on change | Observer / Event |
| Encapsulate request as object | Command |
| Simplify complex subsystem | Facade |
| Complex composable business rules | Specification |
| Multi-service transaction | Saga |
| Atomic DB write + event publish | Outbox |
| Different read/write complexity | CQRS |
