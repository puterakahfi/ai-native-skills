# Normalized testing evidence

Every evidence record includes:

- test level and applicability status;
- risk, boundary, contract, criterion, example, or journey identifier;
- verified repository command and execution environment;
- result status and relevant counts;
- failure, retry, skip, flaky, timeout, and unavailable details;
- evidence location and limitations;
- confidence contribution and acceptance impact.

## Status rules

`PASS` requires executed, deterministic evidence for the claimed scope. `FAIL`, `FLAKY`, `SKIPPED`, `UNAVAILABLE`, `NOT_VERIFIED`, `NEEDS_WORK`, `BLOCKED`, `NOT_APPLICABLE`, and `NOT_JUSTIFIED` remain distinct.

A retry can diagnose but cannot erase prior uncertainty. Coverage numbers are supporting evidence, never completion by themselves. A lower-level pass cannot prove an untested higher-level boundary.

## Traceability

Use stable identifiers so a reviewer can move from risk or criterion to test selection, command, result, failure analysis, and acceptance handoff without inference.