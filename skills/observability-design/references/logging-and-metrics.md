# Observability: Structured Logging & Metrics

## Pillar 1: Structured Logging

### Always structured — never plaintext

```php
// ❌ Plaintext — unsearchable, unparseable
error_log("User 123 failed to login at 2026-07-16");

// ✅ Structured JSON
$logger->error('login.failed', [
    'userId'      => $userId,
    'reason'      => 'invalid_credentials',
    'ip'          => $request->ip(),
    'userAgent'   => $request->userAgent(),
    'requestId'   => $request->header('X-Request-ID'),
    'timestamp'   => now()->toIso8601String(),
]);
```

### Log Levels — Use Correctly

| Level | When |
|---|---|
| `DEBUG` | Developer info, never in production default |
| `INFO` | Normal operations, business events |
| `WARNING` | Unexpected but handled — degraded behavior |
| `ERROR` | Failed operation, requires attention |
| `CRITICAL` | Service down, data loss risk |

### Required Fields in Every Log

```json
{
  "level": "error",
  "message": "payment.charge_failed",
  "requestId": "req_abc123",
  "correlationId": "corr_xyz789",
  "service": "payment-service",
  "timestamp": "2026-07-16T10:00:00Z",
  "context": {
    "orderId": "ord_001",
    "amount": 9998,
    "reason": "card_declined"
  }
}
```

### No PII in Logs

```php
// ❌ PII — never log
$logger->info('user.registered', ['email' => $user->email, 'password' => $hash]);

// ✅ Safe
$logger->info('user.registered', ['userId' => $user->id(), 'method' => 'email']);
```

---

## Pillar 2: Metrics + Four Golden Signals

Every service must instrument the four golden signals (Google SRE):

| Signal | What | Metric Type |
|---|---|---|
| **Latency** | Time to serve request (p50, p95, p99) | Histogram |
| **Traffic** | Request rate (req/sec) | Counter |
| **Errors** | Error rate (4xx, 5xx) | Counter |
| **Saturation** | Resource utilization (CPU, memory, queue depth) | Gauge |

```php
// Laravel + Prometheus example
$histogram->observe(
    $request->duration(),
    ['route' => $route, 'method' => $method, 'status' => $status]
);

$counter->inc(['route' => $route, 'status' => '5xx']);
```

### SLO Definition

```yaml
# SLO — Service Level Objectives
slos:
  - name: api_availability
    target: 99.9%
    window: 30d
    metric: sum(rate(http_requests_total{status!~"5.."}[5m])) / sum(rate(http_requests_total[5m]))

  - name: api_latency_p99
    target: 500ms
    window: 30d
    metric: histogram_quantile(0.99, rate(http_request_duration_seconds_bucket[5m]))
```

### Cardinality Control

High-cardinality labels destroy metrics backends:

```php
// ❌ Cardinality explosion — userId is unique per user
$counter->inc(['userId' => $userId, 'route' => '/orders']);

// ✅ Low cardinality — route is bounded set
$counter->inc(['route' => '/orders', 'method' => 'POST', 'status' => '201']);
```

Rule: label values must be from a bounded set (< 1000 unique values).

---

## Observability Stack Options

| Layer | Open Source | Managed |
|---|---|---|
| Logs | Loki + Grafana | Datadog, CloudWatch |
| Metrics | Prometheus + Grafana | Datadog, CloudWatch |
| Traces | Jaeger / Tempo | Datadog APM, X-Ray |
| Alerting | Alertmanager | PagerDuty, OpsGenie |
| All-in-one | Grafana Stack (Loki+Mimir+Tempo) | Datadog, Honeycomb |
