# Ports and Adapters — Architecture, Ports & Adapter Implementation

## Core Idea

```
The domain is the center. Everything else is a plugin.

        [REST API]  [CLI]  [Queue Consumer]
              ↓        ↓         ↓
         PRIMARY PORTS (driving ports)
              ↓
         [ D O M A I N ]
              ↓
         SECONDARY PORTS (driven ports)
              ↓        ↓         ↓
           [DB]    [Email]   [Message Bus]
```

**Primary ports** — driven BY external actors (REST, CLI, tests)
**Secondary ports** — driven BY the domain (DB, email, queue)

The domain defines both. Infrastructure implements secondary ports. Framework implements primary ports.

---

## Why This Matters

```
Without hexagonal:
  Domain → Laravel → MySQL
  Test requires DB, test requires HTTP, test requires queue — slow, fragile

With hexagonal:
  Domain → interface only
  Test uses in-memory adapter — fast, isolated, no infrastructure
  Swap MySQL for Postgres: change one adapter, zero domain changes
  Swap REST for GraphQL: change one adapter, zero domain changes
```

---

## The 3 Layers

```
┌──────────────────────────────────────────────┐
│  ADAPTERS (Infrastructure + Framework)        │
│  EloquentOrderRepo, StripePaymentAdapter,     │
│  LaravelController, SQSConsumer               │
├──────────────────────────────────────────────┤
│  PORTS (Interfaces defined by Domain)         │
│  OrderRepository, PaymentGateway,             │
│  EmailSender, EventPublisher                  │
├──────────────────────────────────────────────┤
│  DOMAIN (Pure, no external dependencies)      │
│  Order, Money, OrderService, OrderPlaced      │
└──────────────────────────────────────────────┘

Dependency direction: Adapters → Ports ← Domain
NEVER: Domain → Adapter (direct)
```

---

## Port Definition — Always in Domain Layer

```php
// src/Domain/Order/Port/OrderRepository.php
// DOMAIN owns this interface — infrastructure implements it

namespace App\Domain\Order\Port;

interface OrderRepository
{
    public function findById(OrderId $id): ?Order;
    public function save(Order $order): void;
    public function nextIdentity(): OrderId;
}
```

```php
// src/Domain/Payment/Port/PaymentGateway.php
namespace App\Domain\Payment\Port;

interface PaymentGateway
{
    public function charge(Money $amount, PaymentToken $token): PaymentResult;
    public function refund(PaymentId $id, Money $amount): RefundResult;
}
```

**Gate:** Port interfaces live in domain layer. No framework imports allowed.

---

## Adapter Implementation — Always in Infrastructure Layer

```php
// src/Infrastructure/Persistence/EloquentOrderRepository.php
// INFRASTRUCTURE implements the domain port

namespace App\Infrastructure\Persistence;

use App\Domain\Order\Port\OrderRepository;

class EloquentOrderRepository implements OrderRepository
{
    public function findById(OrderId $id): ?Order
    {
        $record = OrderModel::find($id->toString());
        return $record ? $this->toDomain($record) : null;
    }

    public function save(Order $order): void
    {
        OrderModel::updateOrCreate(
            ['id' => $order->id()->toString()],
            $this->toRecord($order)
        );
    }

    private function toDomain(OrderModel $model): Order { /* mapping */ }
    private function toRecord(Order $order): array { /* mapping */ }
}
```

```php
// src/Infrastructure/Payment/StripePaymentGateway.php
namespace App\Infrastructure\Payment;

use App\Domain\Payment\Port\PaymentGateway;

class StripePaymentGateway implements PaymentGateway
{
    public function charge(Money $amount, PaymentToken $token): PaymentResult
    {
        // Stripe SDK calls here
    }
}
```

---

## Primary Adapter — Driving the Domain

```php
// src/Interface/Http/OrderController.php
// HTTP adapter drives the domain via application service

class OrderController
{
    public function __construct(
        private PlaceOrderUseCase $placeOrder  // application service, not domain directly
    ) {}

    public function store(PlaceOrderRequest $request): JsonResponse
    {
        $result = $this->placeOrder->execute(
            new PlaceOrderCommand(
                customerId: CustomerId::from($request->customer_id),
                items: $request->items,
            )
        );
        return response()->json($result);
    }
}
```
