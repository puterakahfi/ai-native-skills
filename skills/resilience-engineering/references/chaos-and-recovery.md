# Chaos Engineering & Recovery Design

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
