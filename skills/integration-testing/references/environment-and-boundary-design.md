# Integration environment and boundary design

## Boundary first

Name the material boundary before choosing infrastructure: persistence, repository adapter, framework wiring, API, external service, message broker, migration, transaction, or cross-component behavior.

## Dependency fidelity

Choose the minimum credible fidelity:

- real local dependency;
- ephemeral container;
- approved sandbox;
- in-process fake;
- protocol stub;
- unavailable dependency with a `NOT_VERIFIED` result.

A fake or stub is acceptable only when it preserves the behavior being claimed. It cannot prove real transaction, migration, serialization, broker, network, or vendor semantics.

## Environment contract

Document service versions, migrations, seeds, fixtures, credentials, ports, isolation, cleanup, idempotency, concurrency assumptions, and the verified command.

## Nondeterminism

Use bounded polling or observable completion for asynchronous behavior. Do not use arbitrary sleeps as evidence. Record timeout, retry, race, eventual-consistency, and flaky outcomes explicitly.

## Scope control

Integration testing stops at the selected component or dependency boundary. A full user journey belongs to E2E only when a distinct risk requires journey-level evidence.

When the selected claim is provider-consumer compatibility rather than component behavior, hand off to contract testing. When the claim is product-defined behavior, hand off to acceptance testing without transferring product acceptance authority.

## Cleanup gate

A credible test restores or disposes of data, messages, processes, ports, containers, and external sandbox state. Leaked or order-dependent state is `NEEDS_WORK`, not PASS.
