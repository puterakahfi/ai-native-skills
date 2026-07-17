# Failure Isolation Patterns

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
