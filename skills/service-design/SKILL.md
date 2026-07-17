---
name: service-design
description: Design service boundaries and inter-service communication — decompose by bounded context, justify sync vs async, own your data, avoid distributed monolith. Forces-first decomposition.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/architecture/service-design.contract.yaml
  ai-native-skills.contract-version: "~0.1"
  ai-native-skills.related_skills: '[''domain-driven-design'', ''api-contract'', ''event-driven-design'', ''ports-and-adapters'']'
---

# Service Design

## The Core Rule

```
Microservices are a solution to an organizational and scaling problem.
They are not a starting point.

Forces that justify decomposition:
  - Independent deployability needed per team
  - Radically different scaling requirements
  - Different technology requirements per domain
  - Conway's Law — team structure requires service boundary

Without these forces → monolith first, extract later.
```

---

## Step 1: Identify Service Boundaries via Bounded Context

Service boundaries must align with bounded contexts (DDD). One bounded context = one service candidate.

```
E-commerce — context map → service map:

  [Sales Context]      → OrderService
  [Inventory Context]  → InventoryService
  [Shipping Context]   → ShippingService
  [Identity Context]   → IdentityService
  [Payment Context]    → PaymentService
```

**Wrong signal:** Service boundary crosses bounded context = distributed monolith.

```
❌ UserOrderService  — mixes User (Identity) + Order (Sales)
✅ OrderService      — owns Sales context only
✅ IdentityService   — owns Identity context only
```

---

## Step 2: Data Ownership — Each Service Owns Its Data

```
✅ Each service has its own database/schema
   OrderService   → orders_db
   PaymentService → payments_db
   UserService    → users_db

❌ Shared database — services read each other's tables directly
   → tight coupling, schema changes break multiple services
   → kills independent deployability
```

**Enforcement:** Cross-service data access via API or event only — never direct DB query.

---

## Step 3: Communication Pattern — Sync vs Async

| Factor | Sync (REST/gRPC) | Async (Events/Queue) |
|---|---|---|
| Response needed immediately | ✅ | ❌ |
| Caller can proceed without response | ❌ | ✅ |
| Failure isolation needed | ❌ | ✅ |
| Temporal decoupling needed | ❌ | ✅ |
| Simple request-response | ✅ | ❌ |
| Long-running process | ❌ | ✅ |

```
Sync examples:
  GET /orders/{id}           — caller needs data now
  POST /payments/charge      — caller needs success/failure now

Async examples:
  OrderPlaced event          — inventory reserves, email sends, analytics records
  PaymentProcessed event     — shipping triggered, order confirmed
```

**Rule:** If caller can tolerate eventual consistency → async. If not → sync.

---

## Step 4: Failure Modes Per Communication Pattern

### Sync failures
```
Problem: ServiceA calls ServiceB — ServiceB is down
Solution: Circuit breaker + fallback

States:
  CLOSED   → requests pass through normally
  OPEN     → requests fail fast (no waiting) after threshold
  HALF-OPEN → probe requests to test recovery

// Pseudocode
$circuitBreaker->call(
    fn() => $paymentService->charge($amount),
    fallback: fn() => new PaymentResult('PENDING_RETRY')
);
```

### Async failures
```
Problem: Consumer crashes mid-processing — message lost
Solution: At-least-once delivery + idempotent consumer

Consumer must handle duplicate messages:
  - Check if event already processed (idempotency key)
  - Process is safe to repeat
  - Or use transactional outbox pattern
```

---

## Decomposition Patterns

### Strangler Fig (Preferred)
Incrementally extract from monolith — route traffic to new service, strangle old code.

```
Phase 1: Route /orders/* to new OrderService — monolith still handles everything else
Phase 2: Verify OrderService handles load
Phase 3: Remove order code from monolith
Phase 4: Repeat for next bounded context
```

**Never:** Big bang rewrite — rewrite entire system at once.

### Extract by Feature (for new capability)
New bounded context = new service from day one — do not add to existing monolith.

---

## Anti-Patterns

| Anti-Pattern | Signal | Fix |
|---|---|---|
| Distributed Monolith | Services share DB, or sync call chains 3+ deep | Redesign boundaries, introduce async |
| Nano-services | Service per function (UserGetService, UserUpdateService) | Merge by bounded context |
| Chatty Services | 10+ sync calls per user request | Introduce API gateway aggregation or async |
| Shared DB | Two services read/write same table | Each service owns its data |
| Circular Dependency | A calls B calls A | Introduce event — break cycle |
| Big Bang Rewrite | Rewrite all services at once | Strangler fig — extract incrementally |
| Service per Layer | "DataService", "BusinessService" | Service per domain/context, not technical layer |

---

## Data Consistency Across Services

```
Strong consistency → synchronous, 2PC (avoid — distributed deadlock risk)
Eventual consistency → async events, saga pattern

Saga: multi-service transaction via compensating transactions
  Forward: A → B → C  (each step publishes event)
  Rollback: if C fails → C compensates → B compensates → A compensates

Example:
  PlaceOrder → ReserveInventory → ChargePayment → ScheduleShipping
  If ChargePayment fails:
    → ReleaseInventory compensation
    → CancelOrder compensation
```

---

## Service Design Checklist

Before finalizing service boundaries:
- [ ] Each service maps to a bounded context?
- [ ] Each service owns its own data?
- [ ] No shared database across services?
- [ ] Sync vs async decision justified per communication path?
- [ ] Circular dependencies between services checked?
- [ ] Failure modes defined per communication pattern?
- [ ] Decomposition justified by forces (team, scale, tech)?
- [ ] Strangler fig planned if extracting from monolith?
- [ ] Data consistency strategy declared (eventual vs strong)?
