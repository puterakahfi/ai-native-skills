---
name: resilience-engineering
description: Design for failure before failure happens — failure mode analysis, chaos engineering, circuit breakers, graceful degradation, blast radius minimization, RTO/RPO design, and load shedding.
license: MIT
metadata:
  ai-native-skills.version: 1.0.1
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/quality/resilience-engineering.contract.yaml
  ai-native-skills.contract-version: "~0.1"
  ai-native-skills.related_skills: '["observability-design", "incident-response", "service-design", "deployment-workflow"]'
---

# Resilience Engineering

## Reviewed core contract interface

Source: `ai-native-core/contracts/skills/quality/resilience-engineering.contract.yaml` · compatible line: `~0.1`

```yaml
required_inputs:
- system_or_service_description
allowed_outputs:
- failure_mode_analysis
- chaos_experiment_plan
- circuit_breaker_design
- graceful_degradation_strategy
- blast_radius_map
- rto_rpo_design
quality_gates:
- failure_modes_must_be_identified_before_chaos_testing
- circuit_breaker_must_have_fallback_defined
- graceful_degradation_preferred_over_total_failure
- blast_radius_must_be_minimized_by_design
- chaos_experiments_must_have_hypothesis_and_abort_condition
- rto_and_rpo_must_be_explicitly_defined
- load_shedding_strategy_must_exist_for_saturation
- resilience_tests_must_run_in_staging_before_prod
```

Begin with system_or_service_description, identify failure modes before chaos work, then produce failure analysis, chaos plan, circuit-breaker design, graceful-degradation strategy, blast-radius map, and RTO/RPO design. Every chaos experiment needs a hypothesis and abort condition; resilience is verified in staging before production.

Keep this interface synchronized with the pinned core contract. Exact declarations make ownership reviewable; they do not replace runtime, repository, security, incident, resilience, or product evidence.


> **Design for failure, not just success. Test failure modes with chaos before production. Graceful degradation beats hard failure.**

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

---

## References

- [Failure Isolation Patterns](references/failure-isolation.md) — Circuit Breaker, Bulkhead, Timeout + Retry, Load Shedding
- [Chaos Engineering & Recovery Design](references/chaos-and-recovery.md) — Graceful Degradation, Chaos Engineering, RTO/RPO
