---
name: resilience-engineering
description: Design for failure before failure happens — failure mode analysis, chaos engineering, circuit breakers, graceful degradation, blast radius minimization, RTO/RPO design, and load shedding.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/quality-control/resilience-engineering.contract.yaml
  ai-native-skills.related_skills: '[''observability-design'', ''incident-response'', ''service-design'', ''deployment-workflow'']'
---

# Resilience Engineering

## The Core Rule

```
Failure is not an exception. Failure is a guarantee.

The question is not "will it fail?" but "how gracefully does it fail?"

Resilience = ability to absorb disturbance and adapt, not just recover.
```

---

## Step 1: Failure Mode Analysis

Before any chaos experiment — identify failure modes systematically.

```
For each service dependency, ask:
  1. What happens if this dependency is slow? (latency spike)
  2. What happens if this dependency is down? (total failure)
  3. What happens if this dependency returns wrong data? (corruption)
  4. What happens if this dependency is intermittently failing? (flapping)

Example — Order Service depends on:
  - Payment Service
  - Inventory Service
  - Notification Service
  - Order DB

Failure Mode Matrix:
  | Dependency         | Slow       | Down           | Wrong data    |
  |--------------------|------------|----------------|---------------|
  | Payment Service    | Order hangs| Order fails    | Double charge |
  | Inventory Service  | Order hangs| Order fails    | Oversell      |
  | Notification Service| Slow confirm| Silent success| Duplicate email|
  | Order DB           | Everything | Total outage   | Data corruption|
```

---

## Circuit Breaker

Prevent cascade failure — stop calling a failing dependency.

```python
from enum import Enum
from datetime import datetime, timedelta

class CircuitState(Enum):
    CLOSED    = "closed"    # normal — calls pass through
    OPEN      = "open"      # failing — calls blocked, return fallback
    HALF_OPEN = "half_open" # testing — one call allowed to probe

class CircuitBreaker:
    def __init__(self, failure_threshold=5, recovery_timeout=60):
        self.state = CircuitState.CLOSED
        self.failure_count = 0
        self.failure_threshold = failure_threshold
        self.last_failure_time = None
        self.recovery_timeout = recovery_timeout

    def call(self, fn, fallback):
        if self.state == CircuitState.OPEN:
            if datetime.now() > self.last_failure_time + timedelta(seconds=self.recovery_timeout):
                self.state = CircuitState.HALF_OPEN
            else:
                return fallback()   # ← return fallback, don't call failing service

        try:
            result = fn()
            self._on_success()
            return result
        except Exception:
            self._on_failure()
            return fallback()

    def _on_success(self):
        self.failure_count = 0
        self.state = CircuitState.CLOSED

    def _on_failure(self):
        self.failure_count += 1
        self.last_failure_time = datetime.now()
        if self.failure_count >= self.failure_threshold:
            self.state = CircuitState.OPEN

# Usage
payment_breaker = CircuitBreaker(failure_threshold=5, recovery_timeout=30)

def charge_order(order):
    return payment_breaker.call(
        fn=lambda: payment_service.charge(order),
        fallback=lambda: queue_for_retry(order)   # ← fallback must be defined
    )
```

---

## Graceful Degradation

Core hierarchy: **full experience → degraded experience → empty → error (last resort)**

```python
class ProductRecommendations:
    def get(self, user_id: str) -> list:
        # Full: personalized AI recommendations
        try:
            return self.ai_engine.recommend(user_id, limit=10)
        except (Timeout, ServiceUnavailable):
            pass

        # Degraded: cached popular items
        try:
            return self.cache.get("popular_products", default=[])
        except CacheUnavailable:
            pass

        # Minimal: static top sellers from config
        try:
            return self.config.get("default_featured_products")
        except Exception:
            pass

        # Last resort: empty (never crash the page)
        return []
```

---

## Bulkhead Pattern

Isolate failures — one subsystem's failure must not drain resources from others.

```python
from concurrent.futures import ThreadPoolExecutor

# ❌ Shared thread pool — slow payment drains threads for all services
shared_pool = ThreadPoolExecutor(max_workers=50)

# ✅ Separate pools — payment slowdown only affects payment calls
payment_pool   = ThreadPoolExecutor(max_workers=10, thread_name_prefix="payment")
inventory_pool = ThreadPoolExecutor(max_workers=10, thread_name_prefix="inventory")
email_pool     = ThreadPoolExecutor(max_workers=5,  thread_name_prefix="email")
```

---

## Timeout + Retry Strategy

```python
import httpx
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

# Timeouts — always set, never rely on default (often infinite)
client = httpx.Client(
    timeout=httpx.Timeout(
        connect=2.0,   # time to establish connection
        read=5.0,      # time to read response
        write=2.0,     # time to write request
        pool=1.0,      # time to acquire connection from pool
    )
)

# Retry — only for idempotent operations, with backoff
@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=1, max=10),
    retry=retry_if_exception_type((httpx.TimeoutException, httpx.ConnectError)),
)
def get_inventory(product_id: str):
    return client.get(f"/inventory/{product_id}").json()

# ⚠️ Never retry non-idempotent operations (POST payment) without idempotency key
```

---

## Load Shedding

When saturated — shed load deliberately rather than degrading for everyone.

```python
from asyncio import Semaphore

class LoadShedder:
    def __init__(self, max_concurrent: int):
        self.semaphore = Semaphore(max_concurrent)

    async def execute(self, fn, priority: str = "normal"):
        if not self.semaphore._value and priority != "critical":
            # Shed non-critical load immediately
            raise ServiceUnavailableError("Service at capacity — retry later")

        async with self.semaphore:
            return await fn()

# Priority tiers
order_processor = LoadShedder(max_concurrent=100)

# Critical: checkout — always processed
async def checkout(order):
    return await order_processor.execute(lambda: process_order(order), priority="critical")

# Normal: report generation — shed when busy
async def generate_report(params):
    return await order_processor.execute(lambda: build_report(params), priority="normal")
```

---

## Chaos Engineering

**Hypothesis-driven experiments** — not random destruction.

```yaml
# Chaos experiment template
experiment:
  id: payment-service-latency-spike
  hypothesis: "When payment service latency exceeds 3s, order service circuit breaker opens and returns error to user within 5s, without affecting other endpoints"

  method:
    target: payment-service
    fault: latency
    parameters:
      latency_ms: 3500
      percentage: 100

  steady_state:
    before:
      - metric: order_success_rate > 0.99
      - metric: p99_latency < 500ms

  abort_conditions:
    - order_success_rate < 0.50    # ← stop if more than 50% of orders fail
    - database_error_rate > 0.01   # ← stop if DB starts failing too

  expected_result:
    - circuit_breaker: OPEN within 30s
    - user_experience: error message within 5s (not hanging)
    - other_endpoints: unaffected
    - recovery: circuit HALF-OPEN after 60s timeout
```

**Abort conditions are mandatory** — chaos without abort condition is not engineering, it's gambling.

---

## RTO and RPO

```
RTO — Recovery Time Objective
  How long can the system be down before business impact is unacceptable?
  → Design backup + failover to meet this

RPO — Recovery Point Objective
  How much data loss is acceptable in a disaster scenario?
  → Design backup frequency to meet this

Example:
  Payments:    RTO = 5 min,  RPO = 0 (no data loss ever)
  Analytics:   RTO = 4 hr,   RPO = 1 hr (lose some events)
  Audit logs:  RTO = 24 hr,  RPO = 0 (must not lose, can be slow)

RTO → drives: multi-region, failover automation, runbook completeness
RPO → drives: backup frequency, write-ahead logs, replication strategy
```

---

## Resilience Checklist

Design:
- [ ] Failure modes identified per dependency?
- [ ] Circuit breaker with fallback defined for each external call?
- [ ] Graceful degradation path defined (full → degraded → empty)?
- [ ] Bulkhead isolation per subsystem?
- [ ] All timeouts explicitly set (no default/infinite)?
- [ ] Retry only on idempotent operations?
- [ ] Load shedding strategy defined for saturation?
- [ ] RTO and RPO defined per service tier?

Testing:
- [ ] Chaos experiments have hypothesis + abort conditions?
- [ ] Experiments run in staging before prod?
- [ ] Circuit breaker behavior verified under load?
- [ ] Fallback paths tested (not just happy path)?
