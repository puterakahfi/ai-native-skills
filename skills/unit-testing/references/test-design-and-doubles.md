# Unit test design and test doubles

## Boundary selection

Select a unit around one coherent behavior, not around an arbitrary file or class. Record what remains outside the boundary and which risks require broader evidence.

## Assertion style

Use state-based assertions when observable outcomes are sufficient. Use interaction-based assertions only when the collaboration protocol is itself part of the required behavior.

## Test doubles

- **Stub:** provides controlled input or response.
- **Fake:** lightweight working implementation with known limits.
- **Spy:** records interactions for later inspection.
- **Mock:** verifies an expected collaboration protocol.

Prefer no double when the dependency is deterministic, cheap, and local. A double must not be used to claim confidence in persistence, transactions, migrations, serialization, network protocols, framework wiring, or external compatibility.

## Case selection

Include positive, negative, boundary, invariant, and regression cases as justified. Use parameterized or table-driven tests for meaningful input partitions. Use property-based testing when invariants matter more than a small example list.

## Smell review

Flag tests that:

- break after harmless refactoring;
- mirror private implementation structure;
- require excessive mock setup;
- assert incidental call order;
- combine unrelated behaviors;
- hide time, randomness, global state, filesystem, or network access;
- pass while the selected risk remains unobserved.

## Evidence semantics

Skipped, flaky, unavailable, unexecuted, or unsupported tests are not PASS. Mutation testing may strengthen confidence but is never a universal completion requirement.
