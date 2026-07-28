# Compatibility and responsibility

## Compatibility promises

- **Backward compatible:** newer provider accepts existing consumer expectations.
- **Forward compatible:** older participants tolerate approved newer representations where promised.
- **Exact:** both sides require the same version.
- **Versioned:** multiple explicit versions coexist under lifecycle rules.

## Responsibility split

The provider must honor published required behavior and declared lifecycle rules. Consumers must avoid relying on undocumented fields, ordering, timing, or implementation details. Contract tests should expose violations on either side.

## False compatibility

Reject confidence based only on permissive mocks, incomplete examples, stale snapshots, ignored unknown fields without policy, or a provider test that never executes consumer expectations.

## Evolution cases

Cover required-field removal, type changes, semantic changes, enum growth, optional-field addition, default changes, event ordering, idempotency keys, deprecation windows, and unsupported versions when material.

## Evidence

A passing adapter proves only the consumers, versions, and examples actually exercised. Unknown consumers and unavailable environments remain limitations or `NOT_VERIFIED`.
