# Observability: Tracing, Alerting & Dashboard Blueprint

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

## Alert Strategy — Actionable Only

> **HARD RULE: Alert on symptoms, not causes. Every alert must have a runbook link.**

```yaml
# ✅ Actionable alert — symptom-based
alert: HighErrorRate
expr: rate(http_requests_total{status=~"5.."}[5m]) > 0.05
for: 2m
annotations:
  summary: "Error rate > 5% for 2 minutes"
  runbook: "https://wiki/runbooks/high-error-rate"
  severity: critical

# ❌ Noise alert — not actionable (cause, not symptom)
alert: CPUAbove50Percent
expr: cpu_usage > 0.5
# "CPU is high" — so what? No action defined.
```

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
