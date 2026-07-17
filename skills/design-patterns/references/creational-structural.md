# Creational & Structural Patterns

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

---

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

---

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

---

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

---

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
