# Criteria to executable examples

## Traceability

Each check must reference an approved criterion or example. Missing authority remains `NOT_VERIFIED`; a test author must not invent product acceptance criteria.

## Scenario design

Describe actor, preconditions, action, and observable outcome in domain language. Keep implementation choices, private methods, CSS selectors, database rows, and internal event names out unless they are explicitly part of the accepted behavior.

## Execution surface

Choose the narrowest surface that proves the outcome:

- domain or application API for UI-free behavior;
- component boundary when observable behavior is local;
- external API when the criterion is interface-visible;
- E2E only when the real journey is material.

## Over-specification

Reject scenarios that prescribe every click, internal call order, incidental copy, or layout detail when the criterion only requires an outcome. Split unrelated behaviors and avoid duplicating lower-level assertions.

## Verdict boundary

A passing acceptance test is evidence for a criterion. It is not product acceptance, release authorization, or proof of unrelated quality attributes.
