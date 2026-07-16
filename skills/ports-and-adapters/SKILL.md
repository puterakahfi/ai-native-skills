---
name: ports-and-adapters
description: Design hexagonal architecture with explicit ports and adapters — domain isolation, dependency inversion, testable domain without infrastructure. Foundation pattern for DDD, microservices, and clean architecture.
version: 1.0.0
author: puterakahfi
license: MIT
type: skill
implements: ai-native-core/contracts/skills/domain-architecture/ports-and-adapters.contract.yaml
---

# Ports and Adapters (Hexagonal Architecture)

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

---

## Application Service — Orchestration Layer

```php
// src/Application/Order/PlaceOrderUseCase.php
// Orchestrates domain + ports — no domain logic here

class PlaceOrderUseCase
{
    public function __construct(
        private OrderRepository $orders,       // port — injected
        private PaymentGateway $payments,      // port — injected
        private EventPublisher $events,        // port — injected
    ) {}

    public function execute(PlaceOrderCommand $cmd): OrderId
    {
        $order = Order::place($cmd->customerId, $cmd->items);
        $this->payments->charge($order->total(), $cmd->paymentToken);
        $this->orders->save($order);
        $this->events->publish($order->releaseEvents());
        return $order->id();
    }
}
```

**Gate:** Application service has no domain logic. Domain has no infrastructure calls.

---

## Dependency Injection — Wiring Adapters to Ports

```php
// src/Infrastructure/Provider/AppServiceProvider.php

$this->app->bind(OrderRepository::class, EloquentOrderRepository::class);
$this->app->bind(PaymentGateway::class, StripePaymentGateway::class);
$this->app->bind(EventPublisher::class, SQSEventPublisher::class);
```

For testing — swap to in-memory adapters:

```php
// tests — no real DB, no real Stripe, no real SQS
$this->app->bind(OrderRepository::class, InMemoryOrderRepository::class);
$this->app->bind(PaymentGateway::class, FakePaymentGateway::class);
$this->app->bind(EventPublisher::class, FakeEventPublisher::class);
```

---

## In-Memory Adapters for Testing

```php
// tests/Infrastructure/InMemoryOrderRepository.php
class InMemoryOrderRepository implements OrderRepository
{
    private array $store = [];

    public function findById(OrderId $id): ?Order
    {
        return $this->store[$id->toString()] ?? null;
    }

    public function save(Order $order): void
    {
        $this->store[$order->id()->toString()] = $order;
    }

    public function nextIdentity(): OrderId
    {
        return OrderId::generate();
    }
}
```

**Gate:** Domain tests run in milliseconds — no DB, no HTTP, no queue.

---

## Folder Structure

```
src/
├── Domain/
│   ├── Order/
│   │   ├── Order.php              ← aggregate root
│   │   ├── OrderLine.php          ← entity
│   │   ├── OrderId.php            ← value object
│   │   ├── OrderStatus.php        ← value object
│   │   ├── Event/
│   │   │   └── OrderPlaced.php    ← domain event
│   │   └── Port/
│   │       └── OrderRepository.php ← port (interface)
│   └── Payment/
│       └── Port/
│           └── PaymentGateway.php  ← port (interface)
├── Application/
│   └── Order/
│       └── PlaceOrderUseCase.php   ← orchestration
├── Infrastructure/
│   ├── Persistence/
│   │   └── EloquentOrderRepository.php ← adapter
│   └── Payment/
│       └── StripePaymentGateway.php    ← adapter
└── Interface/
    └── Http/
        └── OrderController.php         ← primary adapter
```

---

## Violations — What to Catch in Review

| Violation | Signal | Fix |
|---|---|---|
| Domain imports framework | `use Illuminate\...` in Domain/ | Extract to adapter |
| Adapter in Domain/ | `EloquentModel` in Domain/Order/ | Move to Infrastructure/ |
| Domain calls infrastructure directly | `DB::table()` in entity method | Define port, inject adapter |
| Application service has domain logic | Business rule in UseCase | Move to domain object |
| Port defined in Infrastructure | Interface in Infrastructure/ | Move to Domain/Port/ |
| Test requires real DB | Slow, fragile test | Use in-memory adapter |

---

## Relation to ai-native-core

```
ai-native-core itself uses this pattern:
  contracts/  = ports    (what must be true — interfaces)
  ai-native-skills/ = adapters (how — public implementations)
  ai-native-fw/     = adapters (how — product-specific implementations)

The pattern is fractal — applies at code level and at ecosystem level.
```
