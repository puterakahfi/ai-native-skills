# Test Portfolio Patterns

These are decision examples, not fixed pyramids.

## Pure domain behavior

Typical portfolio:

```text
unit tests for rules and edge cases
acceptance examples when business approval needs executable evidence
integration/E2E: NOT_APPLICABLE unless a real boundary is involved
```

## CRUD service with persistence

Typical portfolio:

```text
unit tests for non-trivial domain behavior
integration tests for repository, transactions, constraints, and migrations
acceptance tests for approved observable outcomes
E2E only for critical cross-boundary journeys
```

## API provider and consumer

Typical portfolio:

```text
unit tests for local transformations and rules
integration tests for adapter and serialization behavior
contract tests for provider-consumer compatibility
acceptance or E2E only when a broader outcome requires it
```

## Event-driven workflow

Typical portfolio:

```text
unit tests for state transitions and policies
integration tests for broker, persistence, retry, and idempotency behavior
contract tests for event compatibility
acceptance/E2E for a critical eventually consistent outcome when justified
```

## Frontend critical journey

Typical portfolio:

```text
unit/component tests for isolated behavior
integration tests for data and framework boundaries
acceptance tests for approved outcomes
small E2E set for critical journeys that require the real stack
```

## Bugfix regression

The portfolio must include the narrowest test that reproduces the defect and any broader level required to prove the material boundary that allowed it.

## Portfolio review

A proportionate portfolio:

- maps every selected level to a distinct risk;
- minimizes duplicated assertions;
- keeps fast feedback near the behavior;
- preserves boundary and compatibility confidence;
- uses E2E sparingly for irreplaceable journey evidence;
- states what remains unverified.

Do not add layers merely to match a diagram or coverage target.