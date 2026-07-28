---
name: unit-testing
description: Design and verify focused unit tests for deliberately selected behavior boundaries without hiding material integration risk. Use for deterministic logic, isolated components, regression seams, test-double decisions, and unit-test quality review.
license: MIT
metadata:
  ai-native-skills.version: 0.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.requires: "test-strategy decision-provenance implementation-context-discovery"
  ai-native-skills.related_skills: '["test-driven-development","integration-testing","clean-code","refactoring"]'
---

# Unit Testing

## Ownership

This skill owns unit-boundary selection, unit-test design, test-double justification, deterministic evidence, and unit-test smell detection.

It does not own RED-GREEN-REFACTOR sequencing; that remains with `test-driven-development`. It must not use mocks to erase a material integration risk selected by `test-strategy`.

## Operating rule

```text
verify behavior and context
→ select the smallest meaningful unit boundary
→ choose observable outcomes
→ select state- or interaction-based style
→ justify doubles
→ cover positive, negative, boundary, and regression cases
→ execute verified command
→ report evidence and limitations
```

## Required decisions

- unit under test and excluded boundaries;
- observable behavior and invariants;
- state-based versus interaction-based assertions;
- need for stub, fake, spy, mock, fixture, generator, or no double;
- deterministic setup and cleanup;
- parameterized, table-driven, example-based, or property-based approach;
- evidence command and confidence limit.

## Test-double rules

Use the simplest double that preserves the claim:

- stub: supplies controlled input;
- fake: lightweight working implementation;
- spy: records interaction for later assertion;
- mock: verifies a required collaboration protocol.

Do not mock value objects, pure calculations, or every collaborator by default. A mock cannot prove persistence, serialization, transactions, network behavior, migrations, or real framework wiring.

## Quality gates

- selected boundary is explicit;
- assertions verify behavior rather than private implementation details;
- tests are deterministic and isolated;
- doubles are justified and do not hide selected integration risk;
- failure messages localize the violated behavior;
- regression tests reproduce the prior failure when applicable;
- mutation testing is optional evidence, never a universal completion gate;
- skipped, flaky, unavailable, or unexecuted tests are not PASS.

## Failure signals

- excessive mock setup relative to behavior;
- tests break on harmless refactoring;
- private methods or internal call order are overspecified;
- one test covers many unrelated behaviors;
- hidden time, randomness, global state, filesystem, or network dependency;
- unit-only evidence is used for a cross-boundary claim.

## Normalized output

```yaml
unit_testing:
  context_status: VERIFIED | PARTIAL | NOT_VERIFIED
  boundary: <unit and exclusions>
  behaviors: []
  style: state_based | interaction_based | mixed
  doubles: []
  cases:
    positive: []
    negative: []
    boundaries: []
    regression: []
  execution:
    command: <verified command or null>
    result: PASS | FAIL | FLAKY | SKIPPED | UNAVAILABLE | NOT_EXECUTED
  limitations: []
  verdict: PASS | NEEDS_WORK | NOT_VERIFIED | NOT_APPLICABLE
```

## Handoff

Return integration risks to `integration-testing`; return lifecycle sequencing to `test-driven-development`; return portfolio changes to `test-strategy`.