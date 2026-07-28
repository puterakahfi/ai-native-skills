# Anti-Patterns and Counterexamples

Load this reference before finalizing a substantial production test strategy.

## Coverage-number substitution

Bad:

```text
Target 90% coverage, therefore the strategy is complete.
```

Why it fails: coverage does not prove meaningful assertions, boundary behavior, compatibility, failure paths, or acceptance outcomes.

Required response: map tests to risks and confidence claims; retain coverage only as supporting evidence where useful.

## Unit-only cross-boundary claim

Bad:

```text
All service methods are unit tested, therefore database transactions and external integrations are safe.
```

Why it fails: mocks and isolated units cannot prove the real boundary.

Required response: add justified integration or contract evidence, or mark the claim `NOT_VERIFIED`.

## Ceremonial test pyramid

Bad:

```text
Every change must have unit, integration, and E2E tests because the pyramid says so.
```

Why it fails: it creates cost and duplication without distinct risk coverage.

Required response: select only levels mapped to material risks and record rejected levels.

## UI implies E2E

Bad:

```text
The feature has a page, so Playwright is mandatory.
```

Why it fails: UI presence does not prove that a browser journey is the narrowest credible evidence.

Required response: identify the critical outcome and choose the narrowest sufficient test level.

## Framework-first strategy

Bad:

```text
Use Vitest and Playwright, then decide what to test.
```

Why it fails: adapters are selected before objective, risk, boundary, and repository context.

Required response: complete strategy selection first, then hand adapter choice to verified implementation context.

## Mocking away the risk

Bad:

```text
Mock the database or provider in the only test for a persistence or compatibility risk.
```

Why it fails: the test removes the exact behavior requiring evidence.

Required response: use the real boundary, a contract harness, or explicitly preserve `NOT_VERIFIED`.

## Duplicate E2E assertions

Bad:

```text
Repeat every unit and integration assertion through browser journeys.
```

Why it fails: the suite becomes slow and flaky without adding distinct confidence.

Required response: keep E2E focused on critical cross-boundary outcomes and diagnostics.

## Missing evidence normalized as PASS

Bad:

```text
The environment was unavailable, tests were skipped, or retries eventually passed; mark the gate PASS.
```

Why it fails: unavailable, skipped, flaky, and retried results have different confidence semantics.

Required response: report the actual state and use `NOT_VERIFIED`, `NEEDS_WORK`, or another non-PASS verdict where confidence is insufficient.

## Counterexample: simple deterministic utility

A pure deterministic utility with no meaningful external boundary may justify unit tests only. Adding contract, acceptance, and E2E layers is `NOT_JUSTIFIED` unless a distinct risk is demonstrated.

## Counterexample: compatibility-sensitive API change

A provider schema change with active consumers cannot be accepted from unit tests alone. Contract evidence is required; integration or acceptance evidence may also be justified by the affected outcome.
