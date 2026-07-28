---
name: acceptance-testing
description: Turn approved acceptance criteria and examples into executable checks of business-observable outcomes without taking product acceptance authority. Use for UI-free or journey-scoped acceptance evidence traceable to explicit criteria.
license: MIT
metadata:
  ai-native-skills.version: 0.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.requires: "test-strategy decision-provenance implementation-context-discovery"
  ai-native-skills.related_skills: '["contract-testing","integration-testing","test-driven-development","product-requirements"]'
---

# Acceptance Testing

## Ownership

This skill owns executable checks that trace approved acceptance criteria or examples to business-observable outcomes. It does not approve the criteria, declare product acceptance, or require a browser or Gherkin.

## Procedure

```text
verify criterion and approval source
→ express observable preconditions, action, and outcome
→ choose the narrowest executable surface
→ remove implementation-detail assertions
→ execute verified command
→ trace result to the criterion
→ preserve product acceptance authority
```

Load `references/criteria-to-executable-examples.md` for traceability and scenario-design rules.

## Required decisions

- criterion or approved example identifier;
- observable actor, preconditions, action, and result;
- non-UI, API, component, or E2E execution surface;
- data and environment assumptions;
- verified command and evidence location;
- limitations and authority boundary.

## Quality gates

- every result traces to a criterion or approved example;
- assertions describe business outcomes, not private methods or incidental UI structure;
- a browser is used only when the criterion requires a real user journey;
- scenarios do not duplicate lower-level evidence without distinct value;
- over-specified scripts are rejected;
- failing, skipped, unavailable, flaky, or unexecuted checks cannot become PASS;
- product owner or governing product source retains acceptance authority.

## Normalized output

```yaml
acceptance_testing:
  context_status: VERIFIED | PARTIAL | NOT_VERIFIED
  criteria:
    - id: <criterion id>
      source: <approved source>
      example: <observable example>
      execution_surface: non_ui | api | component | e2e
      result: PASS | FAIL | FLAKY | SKIPPED | UNAVAILABLE | NOT_EXECUTED
      evidence: []
  limitations: []
  product_acceptance_authority: <owner or NOT_VERIFIED>
  verdict: PASS | NEEDS_WORK | NOT_VERIFIED | NOT_APPLICABLE
```
