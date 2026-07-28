# Decision: Keep behavioral eval contracts centralized

Date: 2026-07-28
Status: Accepted for Epic #169 implementation

## Context

Agent Skills examples may place evaluation material near a skill. This repository already has an established canonical architecture at `contracts/tests/<skill>.test.yaml`, integrated with version validation, the pinned `ai-native-core` runner, smoke compatibility, and CI.

## Decision

- `contracts/tests/` remains the authored source of truth for behavioral regression contracts.
- `skills/<name>/evals/` is not required and is discouraged when it duplicates centralized cases.
- `skills/<name>/tests/` is conditional and owns tests for skill-local executable resources only.
- external runtime formats may be generated from centralized contracts, but generated projections are not committed as a second authority.

## Consequences

This preserves working evaluation infrastructure and avoids version, trigger, and assertion drift. Interoperability adapters must translate from the canonical contract rather than fork it.

## Supersession

Changing this decision requires evidence that centralized ownership prevents a required runtime capability and a migration plan that preserves one authoritative behavioral contract.
