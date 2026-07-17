---
name: observability-design
description: Design logs, metrics, and traces stack for distributed systems — three pillars, four golden signals, SLO definitions, alert strategy, structured logging, trace propagation, and cardinality control.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/runtime/observability-design.contract.yaml
  ai-native-skills.related_skills: '["service-design", "deployment-workflow", "systematic-debugging"]'
---

# Observability Design

> **HARD RULES — apply always, top and bottom of every engagement:**
> 1. **Logs + Metrics + Traces = three pillars. All three required.** One missing = blind spot.
> 2. **Structured logging only.** Never string concatenation / plaintext log calls.
> 3. **Alert on symptoms, not causes.** Alerts must be actionable with a runbook link.

---

## Three Pillars

```
Logs    → what happened (events, errors, audit trail)
Metrics → how the system is performing (counters, gauges, histograms)
Traces  → where time was spent (request journey across services)

All three required. One missing = blind spot.
```

---

## References

| Topic | File |
|---|---|
| Structured Logging · Metrics · Four Golden Signals · SLOs · Cardinality · Stack options | [references/logging-and-metrics.md](references/logging-and-metrics.md) |
| Distributed Tracing · Correlation IDs · Spans · Alert strategy · Dashboard blueprint · Checklist | [references/tracing-and-alerting.md](references/tracing-and-alerting.md) |

---

## Quick Checklist

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

> **Reminder:** structured logging only · alert on symptoms not causes · all three pillars required.
