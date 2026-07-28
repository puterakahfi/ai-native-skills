---
name: integration-testing
description: Design and verify tests across real component, persistence, adapter, API, messaging, and service boundaries using proportionate dependencies and explicit isolation. Use when confidence depends on behavior that unit tests cannot observe.
license: MIT
metadata:
  ai-native-skills.version: 0.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.requires: "test-strategy decision-provenance implementation-context-discovery"
  ai-native-skills.related_skills: '["unit-testing","test-driven-development","api-contract","resilience-engineering"]'
---

# Integration Testing

## Ownership

This skill owns test design and evidence for material boundaries between components and dependencies: persistence, repositories, adapters, framework wiring, APIs, external services, messaging, migrations, transactions, retries, timeouts, races, and eventual consistency.

It does not own full user journeys, product acceptance, or RED-GREEN-REFACTOR sequencing. It must not expand into E2E without a distinct risk that requires journey-level evidence.

## Operating rule

```text
verify selected risk and repository context
→ identify the real boundary
→ choose the minimum credible dependency fidelity
→ define isolation, data, environment, and cleanup
→ cover success, failure, timeout, retry, and compatibility behavior
→ execute verified command
→ preserve failures, flakiness, and limitations
```

## Dependency-fidelity decision

Choose deliberately among:

- real local dependency;
- ephemeral container;
- approved sandbox;
- in-process fake;
- protocol stub;
- unavailable dependency with `NOT_VERIFIED` outcome.

Use a fake only when it preserves the behavior under claim. Do not use it to claim confidence in real transactions, migrations, serialization, network protocols, broker semantics, or vendor compatibility.

## Environment contract

Record:

- required services and versions;
- migrations and seed state;
- transaction/isolation strategy;
- fixture ownership;
- port, credential, and sandbox assumptions;
- cleanup and idempotency behavior;
- concurrency and eventual-consistency timing;
- verified execution command.

## Quality gates

- the tested boundary maps to a risk selected by `test-strategy`;
- dependency fidelity is justified;
- setup and cleanup are repeatable;
- tests do not depend on production services;
- failure, timeout, retry, race, and compatibility paths are covered when material;
- asynchronous assertions use bounded polling or observable completion, not arbitrary sleeps;
- integration scope remains below full E2E unless separately justified;
- failing, flaky, skipped, unavailable, or unexecuted evidence cannot become PASS.

## Failure signals

- mocks replace the exact boundary whose behavior matters;
- test environment assumptions are implicit;
- shared state creates order dependence;
- cleanup leaks data, ports, processes, containers, or messages;
- arbitrary sleeps hide eventual-consistency uncertainty;
- tests require live production credentials;
- a browser journey is used where boundary-level evidence is sufficient;
- a unit test is used to claim real persistence or protocol confidence.

## Normalized output

```yaml
integration_testing:
  context_status: VERIFIED | PARTIAL | NOT_VERIFIED
  boundary: <components or dependency>
  risk_ids: []
  dependency_fidelity: real_local | container | sandbox | fake | stub | unavailable
  environment:
    services: []
    migrations: []
    fixtures: []
    isolation: <strategy>
    cleanup: <strategy>
  cases:
    positive: []
    failure: []
    timeout_retry: []
    concurrency: []
    compatibility: []
  execution:
    command: <verified command or null>
    result: PASS | FAIL | FLAKY | SKIPPED | UNAVAILABLE | NOT_EXECUTED
  limitations: []
  verdict: PASS | NEEDS_WORK | NOT_VERIFIED | NOT_APPLICABLE
```

## Handoff

Return narrow logic to `unit-testing`, portfolio changes to `test-strategy`, contract compatibility to `api-contract` or future contract-testing capability, and full journeys to the E2E capability only when justified.