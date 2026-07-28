# Workflow composition

## One primary lifecycle

`workflow-router` selects exactly one primary lifecycle such as feature, bugfix, refactoring, specification, review, or deployment. `software-testing-workflow` is a composed verification workflow, not a second delivery owner.

## Role assignment

`role-switcher` assigns one owner accountable for the primary lifecycle. Testing specialists may own strategy, unit, integration, contract, acceptance, E2E, or BDD evidence. An independent reviewer checks test-level justification, evidence integrity, and acceptance boundaries.

## Typical handoffs

- feature: requirements and risks → strategy → selected test levels → acceptance evidence;
- bugfix: reproduction and regression risk → minimum failing level → broader regression only when justified;
- refactoring: characterization and contract preservation → focused unit/integration/contract evidence;
- specification: examples and ambiguity → BDD or acceptance formulation → automation handoff;
- code review: inspect changed risks, missing evidence, flakiness, and unsupported PASS claims;
- deployment: consume immutable evidence and add environment/release checks without redesigning the portfolio.

## Inspection matrix

For each engineering workflow, record `UPDATED`, `ALREADY_COMPOSES`, or `NOT_MODIFIED`, plus evidence and rationale. Avoid mechanical edits where existing contracts already provide the handoff.