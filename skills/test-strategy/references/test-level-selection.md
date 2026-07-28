# Test-Level Selection

Select the narrowest level that can observe the risk and support the intended claim.

## Unit

Select when confidence depends on isolated rules, calculations, state transitions, or deterministic behavior within one deliberate unit boundary.

Reject or supplement when the risk depends on persistence, serialization, framework wiring, network behavior, consumer compatibility, or a real journey.

## Integration

Select when confidence depends on collaboration between components or a real boundary such as a database, adapter, external service sandbox, message broker, or framework integration.

Do not use mocks to erase the exact boundary whose behavior must be proven.

## Contract

Select when confidence depends on compatibility between provider and consumer, API/schema evolution, event/message shape, versioning, or conformance obligations.

A generic integration test is not automatically contract evidence.

## Acceptance

Select when an approved criterion or example must be proven through a business-observable outcome. Acceptance testing may be below the browser and need not cross every production boundary.

Do not assert internal calls or implementation structure as acceptance outcomes.

## End-to-end

Select when a critical user or system journey must be proven across the real material boundaries and narrower tests cannot provide equivalent confidence.

Reject when the same risk is already credibly covered by faster and narrower tests, or when the environment cannot produce trustworthy evidence.

## Status semantics for rejected levels

- `NOT_APPLICABLE`: the level does not match any material risk or boundary.
- `NOT_JUSTIFIED`: the level could apply, but its cost or duplication is not warranted by distinct risk coverage.
- `NOT_VERIFIED`: available context is insufficient to decide.

Never use `PASS` for a test level that was not executed.

## Selection checks

For each selected level, record:

```yaml
level: <test level>
risks: []
purpose: <distinct confidence provided>
evidence_required: []
```

A selected level with no mapped risk is ceremonial and must be removed or justified.