# Errors, Comments, Duplication, and Side Effects

Use this reference for findings involving failure semantics, comments, duplicated knowledge, mutation, side effects, or superficial quality signals.

## Error meaning

Error handling should make the failed operation, actionable context, ownership, and recovery path understandable without exposing sensitive data.

Inspect:

- swallowed exceptions or ignored return values;
- broad catches that collapse materially different failures;
- log-and-continue behavior that leaves invalid state;
- duplicate logging at several layers;
- vague messages such as “something went wrong” at an internal boundary;
- infrastructure/provider errors leaking directly into domain or public contracts;
- retries without idempotency, limits, backoff, or terminal failure behavior;
- success return values after partial failure;
- cleanup or rollback failures that replace the primary error without preserving both.

A good correction preserves causal meaning:

```yaml
error_contract:
  operation: <what failed>
  category: <validation | conflict | unavailable | timeout | unauthorized | internal>
  safe_context: <identifiers or state useful for diagnosis>
  cause: <preserved internal cause when applicable>
  retryability: <yes | no | conditional>
  owner: <caller | module | adapter | operator>
```

Do not add logs everywhere. Logging, returning, translating, retrying, compensating, and alerting are separate responsibilities.

## Comments and documentation

Keep comments that preserve information the code cannot express safely:

- rationale behind a non-obvious decision;
- compatibility or migration constraint;
- invariant spanning several operations;
- external protocol or provider behavior;
- security, performance, or concurrency hazard;
- intentional trade-off and reversal condition;
- public API contract not represented by types.

Review or remove comments that:

- restate the next line;
- describe behavior that no longer exists;
- excuse unclear code without naming the constraint;
- contain an unowned TODO;
- duplicate documentation that should have one canonical owner;
- conceal a required test or validation rule.

A TODO is actionable only when it has bounded work, reason, owner or tracking reference, and an acceptable deferral boundary.

## Duplication

Distinguish three cases.

### Duplicated syntax

Code looks similar but represents different concepts or may change independently. Do not abstract automatically.

### Duplicated behavior

Several implementations are expected to produce the same observable result. Shared tests or a common policy may be justified.

### Duplicated knowledge

A business rule, protocol rule, conversion, validation, or decision is encoded in several places. This is the strongest extraction signal because one change can leave inconsistent truth.

Review questions:

1. What concept is duplicated?
2. Must all copies change for the same reason?
3. Is there one legitimate owner?
4. Can consumers depend on that owner without creating a worse boundary?
5. Would an abstraction clarify the concept or merely centralize syntax?
6. What migration and test evidence protects consolidation?

Prefer a small explicit duplication over a misleading universal abstraction when shared ownership is not proven.

## Side effects and mutation

A side effect is not inherently unclean. Hidden, unordered, or weakly owned side effects are risky.

Make material effects visible through names, boundaries, or contracts:

```text
persist
publish
send
charge
invalidate
schedule
mutate shared state
read current time
read randomness
perform network or filesystem I/O
```

Inspect:

- a query-like name that writes;
- constructors or getters that perform external I/O;
- mutation of arguments or shared collections without an explicit contract;
- partially completed multi-step effects;
- side-effect ordering that is required but undocumented or untested;
- time/random/global state that makes tests nondeterministic;
- retries that repeat a non-idempotent effect.

Route distributed consistency, transactions, event publication, or integration-boundary decisions to the relevant architecture capability.

## Superficial quality signals

These are useful evidence but cannot independently prove internal quality:

```text
formatter clean
linter clean
compiler/type checker clean
unit tests green
coverage increased
complexity metric decreased
file or function became shorter
fewer classes or more classes
```

Ask what concrete risk changed. A shorter function can hide behavior in vague helpers. Increased coverage can assert implementation details. A new abstraction can lower duplication metrics while increasing coupling and navigation cost.

## Correction and refactoring boundary

`clean-code` can recommend a correction and may provide a small implementation sketch. Use `refactoring` when structural code changes are to be executed under behavior preservation.

A refactoring handoff should contain:

```yaml
refactoring_handoff:
  named_smell: <smell>
  evidence: <locations and consequence>
  intended_behavior: <reference>
  preservation_locks: []
  green_test_evidence: []
  smallest_transformation: <rename | extract | move | inline | simplify | introduce value object | other>
  verification: []
  stop_condition: <bounded completion>
```

Do not mix unrelated bug fixes or feature behavior into the cleanup commit.

## Finding examples

```yaml
- location: src/payment/charge.ts:chargeCustomer
  category: errors
  evidence: provider timeout is caught and returned as successful pending charge without persisted retry state
  consequence: caller cannot distinguish accepted work from lost work
  severity: BLOCKING

- location: src/member/member-service.ts:update
  category: duplication
  evidence: membership expiry rule is encoded differently in update and import paths
  consequence: the same member can receive conflicting status depending on entry path
  severity: HIGH

- location: src/report/build.ts
  category: comments
  evidence: comment repeats the loop operation and contains no rationale or constraint
  consequence: noise only; no behavior or maintenance risk
  severity: LOW
```

The third example may justify removal, but it should not dominate a review over material behavior or maintenance risks.
