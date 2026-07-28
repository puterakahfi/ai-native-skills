# Risk Classification

Load this reference after the objective and affected behavior are known.

## Risk dimensions

Assess only materially relevant dimensions:

| Dimension | Questions |
|---|---|
| Domain behavior | Can business rules produce an incorrect state or decision? |
| Data integrity | Can data be lost, duplicated, corrupted, leaked, or migrated incompatibly? |
| Component integration | Can collaborating modules disagree on state, timing, or failure behavior? |
| Contract compatibility | Can an API, schema, event, or consumer expectation break? |
| User journey | Can a critical observable outcome fail across real system boundaries? |
| Operational behavior | Can timeout, retry, race, partial failure, or unavailable infrastructure change correctness? |
| Regression exposure | Has this behavior failed before, or is it easy to reintroduce? |

Security, performance, resilience, accessibility, and similar concerns may affect portfolio selection, but their specialist methods remain delegated to the appropriate capabilities.

## Boundary map

Classify the narrowest material boundary:

```text
pure domain or algorithm
process/component boundary
persistence boundary
external service boundary
API/schema boundary
message/event boundary
user/system journey boundary
deployment/runtime boundary
```

Do not infer a boundary from filenames alone. Use verified architecture, call paths, data flow, consumers, and runtime behavior.

## Impact assessment

Use impact as a decision aid, not a numeric scoring ritual.

- `LOW`: localized, easily detected, reversible, and low consequence.
- `MEDIUM`: meaningful user or developer impact with bounded recovery.
- `HIGH`: material business, data, compatibility, or operational impact.
- `CRITICAL`: severe integrity, safety, security, financial, or broad availability impact.

Record likelihood only when supported by evidence such as prior incidents, change complexity, coupling, or unstable dependencies.

## Evidence gap

For every risk, state what is not yet proven. Examples:

- rule correctness under edge cases;
- transaction behavior with a real database;
- provider-consumer compatibility;
- observable acceptance outcome;
- cross-service journey continuity;
- timeout and retry behavior;
- regression prevention.

A risk without an evidence gap does not automatically need another test level.

## Stop conditions

Return `NOT_VERIFIED` when material architecture, consumer, environment, or behavior information is unavailable. Do not invent a risk matrix to create the appearance of rigor.
