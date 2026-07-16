---
name: observability-design
description: Design logs, metrics, and traces stack for distributed systems — three pillars, four golden signals, SLO definitions, alert strategy, structured logging, trace propagation, and cardinality control.
version: 1.0.0
author: puterakahfi
license: MIT
type: skill
implements: ai-native-core/contracts/skills/runtime-ops/observability-design.contract.yaml
related_skills: [service-design, deployment-workflow, systematic-debugging]
---

# Observability Design

## Three Pillars

```
Logs    → what happened (events, errors, audit trail)
Metrics → how the system is performing (counters, gauges, histograms)
Traces  → where time was spent (request journey across services)

All three required. One missing = blind spot.
```

---

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

### Alert Strategy — Actionable Only

```yaml
# ✅ Actionable alert
alert: HighErrorRate
expr: rate(http_requests_total{status=~"5.."}[5m]) > 0.05
for: 2m
annotations:
  summary: "Error rate > 5% for 2 minutes"
  runbook: "https://wiki/runbooks/high-error-rate"
  severity: critical

# ❌ Noise alert — not actionable
alert: CPUAbove50Percent
expr: cpu_usage > 0.5
# "CPU is high" — so what? No action defined.
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

## Pillar 3: Distributed Tracing

### Correlation ID Propagation

Every request gets a correlation ID — must propagate across all service calls:

```php
// Middleware — generate or extract correlation ID
class CorrelationIdMiddleware
{
    public function handle(Request $request, Closure $next): Response
    {
        $correlationId = $request->header('X-Correlation-ID') ?? Str::uuid();
        Context::set('correlationId', $correlationId);

        $response = $next($request);
        $response->header('X-Correlation-ID', $correlationId);
        return $response;
    }
}

// Outgoing HTTP call — propagate
$client->post('/inventory/reserve', [
    'headers' => ['X-Correlation-ID' => Context::get('correlationId')],
    'json'    => $payload,
]);
```

### Trace Spans

```php
// OpenTelemetry
$tracer = Globals::tracerProvider()->getTracer('order-service');

$span = $tracer->spanBuilder('place-order')
    ->setSpanKind(SpanKind::KIND_SERVER)
    ->startSpan();

try {
    $span->setAttribute('order.id', $orderId);
    $span->setAttribute('order.total', $total);

    // child span for DB call
    $dbSpan = $tracer->spanBuilder('db.insert-order')->startSpan();
    $this->orderRepo->save($order);
    $dbSpan->end();

} catch (\Throwable $e) {
    $span->recordException($e);
    $span->setStatus(StatusCode::STATUS_ERROR);
    throw $e;
} finally {
    $span->end();
}
```

---

## Observability Stack Options

| Layer | Open Source | Managed |
|---|---|---|
| Logs | Loki + Grafana | Datadog, CloudWatch |
| Metrics | Prometheus + Grafana | Datadog, CloudWatch |
| Traces | Jaeger / Tempo | Datadog APM, X-Ray |
| Alerting | Alertmanager | PagerDuty, OpsGenie |
| All-in-one | Grafana Stack (Loki+Mimir+Tempo) | Datadog, Honeycomb |

---

## Dashboard Blueprint — Four Golden Signals

Every service gets a dashboard with:

```
Row 1: Traffic
  - Request rate (req/sec) — by route
  - Traffic source breakdown

Row 2: Errors
  - Error rate % — by route + status code
  - Error count — by type

Row 3: Latency
  - p50, p95, p99 latency — by route
  - Latency heatmap

Row 4: Saturation
  - CPU usage %
  - Memory usage %
  - Queue depth (if applicable)
  - DB connection pool utilization
```

---

## Observability Design Checklist

- [ ] Three pillars addressed: logs, metrics, traces?
- [ ] Logs are structured JSON with required fields?
- [ ] No PII in logs or traces?
- [ ] Four golden signals instrumented per service?
- [ ] SLOs defined with target + measurement query?
- [ ] Alerts are actionable (have runbook link)?
- [ ] Correlation ID propagated across all service calls?
- [ ] Cardinality controlled — no high-cardinality labels?
- [ ] Dashboard covers four golden signals?
- [ ] Alert noise threshold calibrated (not alerting on every blip)?
