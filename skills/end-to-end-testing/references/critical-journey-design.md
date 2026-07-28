# Critical journey design

## Select from risk

Choose journeys whose failure would materially harm value, safety, compatibility, money movement, authorization, or release confidence. UI availability is not a selection criterion.

## Boundary and surface

Name every participating component and external boundary. Use a browser only when browser behavior is part of the claim; cross-service API, messaging, CLI, or protocol journeys are valid E2E surfaces.

## Readiness contract

Record environment identity, deployed versions, authentication, test accounts, seed data, feature flags, external dependencies, observability access, isolation, and cleanup.

## Stable evidence

Assert durable business or system outcomes. Prefer stable identifiers and observable state over CSS structure, arbitrary sleeps, or exact timing.

## Diagnostics

Capture correlation identifiers, logs, traces, screenshots when relevant, response payloads, service versions, and the first known failing boundary.

## Retry and flakiness

Retries are bounded diagnostic probes. A pass after retry is `FLAKY` until the cause is resolved and confidence restored.

## Counterexamples

Do not add E2E when a unit, integration, contract, or acceptance check proves the selected risk more cheaply and precisely. Do not duplicate every lower-level case at journey scope.