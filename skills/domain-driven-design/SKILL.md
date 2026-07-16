---
name: domain-driven-design
description: Model complex domains using DDD building blocks — bounded contexts, aggregates, value objects, domain events, ubiquitous language, and repository pattern. Strategic and tactical design.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/domain-architecture/domain-driven-design.contract.yaml
---

# Domain-Driven Design

## When to Use

- Modeling a new domain or subdomain
- Refactoring a Big Ball of Mud into bounded contexts
- Designing service boundaries for microservices
- When business complexity > technical complexity
- Before writing a single line of domain code

**Do NOT use** for CRUD-only apps, simple scripts, or cases where the domain is trivially thin.

---

## Strategic Design — The Big Picture

### Bounded Context

A bounded context is the explicit boundary within which a domain model applies. Same word, different meaning across contexts = separate bounded contexts.

```
E-commerce example:

  [Sales Context]         [Shipping Context]       [Support Context]
  Product = SKU + price   Product = physical item   Product = what customer bought
  Customer = buyer        Customer = delivery addr  Customer = ticket opener

  Same word "Product" — 3 different models — 3 bounded contexts
```

**Rules:**
- One team owns one bounded context
- Ubiquitous language is consistent WITHIN a context, can differ ACROSS contexts
- Never share domain models across bounded context boundaries — share only via contract

### Context Map — Relationships Between Contexts

```yaml
context_relationships:
  - upstream: SalesContext
    downstream: ShippingContext
    pattern: Customer-Supplier   # upstream must meet downstream needs

  - upstream: IdentityContext
    downstream: SalesContext
    pattern: Open-Host-Service   # upstream publishes stable API

  - upstream: LegacyERP
    downstream: InventoryContext
    pattern: Anti-Corruption-Layer  # downstream translates, never lets upstream model leak
```

**Relationship patterns:**
| Pattern | Description |
|---|---|
| Shared Kernel | Two contexts share a small model — changes need coordination |
| Customer-Supplier | Upstream commits to downstream needs |
| Conformist | Downstream conforms to upstream model (no power to negotiate) |
| Anti-Corruption Layer (ACL) | Downstream translates upstream model — prevents model pollution |
| Open-Host Service | Upstream publishes protocol for many downstreams |
| Published Language | Shared well-documented language (OpenAPI, Protobuf) |

---

## Tactical Design — Building Blocks

### Entity

Has identity that persists across state changes.

```php
// Entity — identity = $id, state can change
class Order {
    private OrderId $id;
    private OrderStatus $status;
    private Money $total;

    public function confirm(): void {
        if (!$this->status->isPending()) {
            throw new InvalidOrderStateException();
        }
        $this->status = OrderStatus::CONFIRMED;
        $this->record(new OrderConfirmed($this->id));
    }
}
```

### Value Object

No identity. Defined by its attributes. **Always immutable.**

```php
// Value Object — no id, immutable, equality by value
final class Money {
    public function __construct(
        private readonly int $amount,      // in cents
        private readonly Currency $currency
    ) {}

    public function add(Money $other): self {
        if (!$this->currency->equals($other->currency)) {
            throw new CurrencyMismatchException();
        }
        return new self($this->amount + $other->amount, $this->currency);
    }

    public function equals(Money $other): bool {
        return $this->amount === $other->amount
            && $this->currency->equals($other->currency);
    }
}
```

**Gate:** Value objects are immutable — any "change" returns a new instance.

### Aggregate

A cluster of domain objects treated as a single unit. Has one **Aggregate Root** — the only entry point.

```php
// Aggregate Root = Order
// Aggregate = Order + OrderLine(s)
class Order {
    private OrderId $id;
    private array $lines = [];   // OrderLine — internal, not accessible directly
    private array $events = [];

    public function addLine(ProductId $productId, int $qty, Money $price): void {
        // all invariants enforced HERE — not in application service
        if ($this->status !== OrderStatus::DRAFT) {
            throw new OrderAlreadySubmittedException();
        }
        $this->lines[] = new OrderLine($productId, $qty, $price);
    }

    // Only Aggregate Root is returned from repository
    // Never: $orderLineRepository->find($lineId)
}
```

**Rules:**
- Only one Aggregate Root per aggregate
- External objects reference aggregate by Root ID only
- Transactions must not span aggregate boundaries
- One aggregate = one transaction

### Domain Event

Something that happened in the domain — named in **past tense**.

```php
// Past tense: OrderPlaced, PaymentProcessed, ShipmentDispatched
final class OrderPlaced {
    public function __construct(
        public readonly OrderId $orderId,
        public readonly CustomerId $customerId,
        public readonly Money $total,
        public readonly DateTimeImmutable $occurredAt
    ) {}
}
```

**Gate:** Event names always past tense. Events are immutable facts.

### Repository

Abstracts persistence for aggregates. Domain defines the interface — infrastructure implements it.

```php
// DOMAIN LAYER — interface only
interface OrderRepository {
    public function findById(OrderId $id): ?Order;
    public function save(Order $order): void;
    public function nextIdentity(): OrderId;
}

// INFRASTRUCTURE LAYER — implementation
class EloquentOrderRepository implements OrderRepository {
    public function findById(OrderId $id): ?Order { /* ... */ }
    public function save(Order $order): void { /* ... */ }
}
```

**Gate:** Repositories return aggregates, never raw entities or DTOs.

### Domain Service

Logic that doesn't naturally belong to a single entity or value object.

```php
// Domain service — stateless, uses domain objects
class TransferService {
    public function transfer(Account $from, Account $to, Money $amount): void {
        $from->debit($amount);
        $to->credit($amount);
    }
}
```

---

## Ubiquitous Language

The shared language between domain experts and developers — used in code, conversations, and documentation.

```
# Glossary — Sales Context
Order:      A customer's request to purchase one or more products
OrderLine:  A single product + quantity within an Order
Confirm:    Transition an Order from PENDING to CONFIRMED state
Place:      Submit a Draft Order for processing

# These exact words must appear in:
# - Class names, method names, variable names
# - Jira tickets, PR descriptions
# - Team conversations with domain experts
```

**Anti-pattern:** Code says `UserRequest`, business says `Order` → model drift.

---

## Layer Architecture

```
┌─────────────────────────────────┐
│      Interface Layer            │  HTTP, CLI, queues — thin, no logic
├─────────────────────────────────┤
│      Application Layer          │  Use cases, orchestration, no domain logic
├─────────────────────────────────┤
│      Domain Layer               │  Entities, VOs, Aggregates, Domain Events
│      (pure, no dependencies)    │  Repository interfaces, Domain Services
├─────────────────────────────────┤
│      Infrastructure Layer       │  DB, email, queue, external APIs
│                                 │  Repository implementations
└─────────────────────────────────┘

Rule: dependencies point INWARD only — domain has no outward dependencies
```

---

## DDD Anti-Patterns

| Anti-Pattern | Signal | Fix |
|---|---|---|
| Anemic Domain Model | Entities are data bags, all logic in services | Move logic into entities/VOs |
| Big Ball of Mud | No bounded contexts, one giant model | Identify seams, extract contexts |
| Shared Database | Two contexts read/write same tables | Each context owns its data |
| God Aggregate | One aggregate with 20+ fields and 15 methods | Decompose — find sub-aggregates |
| Primitive Obsession | `string $email`, `int $price` everywhere | Wrap in Value Objects |
| Repository returns entities not aggregates | `$lineRepo->find($lineId)` from outside | Return only from Aggregate Root |

---

## Checklist Before Modeling

- [ ] Bounded context boundary is explicit — documented in context map?
- [ ] Ubiquitous language glossary exists for this context?
- [ ] Every aggregate has exactly one root?
- [ ] Value objects are immutable?
- [ ] Domain events named in past tense?
- [ ] Repositories return aggregates, not raw entities?
- [ ] No domain logic in application or infrastructure layer?
- [ ] Context map defines upstream/downstream relationships?
