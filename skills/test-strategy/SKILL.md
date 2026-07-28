---
name: test-strategy
description: Design a risk-based, tool-agnostic software test portfolio before selecting frameworks. Use when a feature, bugfix, refactor, integration, release, or architecture change needs justified unit, integration, contract, acceptance, or end-to-end coverage with explicit evidence and confidence limits.
license: MIT
metadata:
  ai-native-skills.version: 0.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.requires: "decision-provenance implementation-context-discovery"
  ai-native-skills.related_skills: '["test-driven-development","api-contract","production-code-quality-baseline","architecture-review","code-review-workflow"]'
---

# Test Strategy

## Status and ownership

This is a provisional executable capability tracked by `puterakahfi/ai-native-skills#161` under Epic `#160`.

No accepted `ai-native-core` contract for `test-strategy` has been verified. Use the adjacent `contract.exemption.yaml` as the static ownership record. Do not claim core contract conformance until an accepted canonical contract exists and reviewed adapter conformance is added.

This skill owns risk-based test portfolio selection. It does not own:

- RED-GREEN-REFACTOR execution, which belongs to `test-driven-development`;
- product acceptance authority;
- implementation details of unit, integration, contract, acceptance, or E2E testing;
- framework selection before repository context is verified;
- security, performance, or resilience testing methods owned by their specialist capabilities.

## Core operating rule

```text
verify objective and repository context
→ identify changed behavior and system boundaries
→ classify risks and failure impact
→ select only justified test levels
→ record rejected levels and rationale
→ define negative-path and regression scope
→ define evidence and confidence limits
→ hand off a normalized test plan
```

Frameworks such as Vitest, Playwright, Cucumber, PHPUnit, Go `testing`, Testcontainers, and Pact are adapters. They must not determine the canonical strategy.

## Required inputs

- objective and acceptance criteria;
- changed or proposed behavior;
- verified repository stack, architecture, and test commands when available;
- affected boundaries, consumers, data, journeys, and failure modes;
- existing tests and known gaps;
- product-defined checks and release constraints.

Missing material context must remain `NOT_VERIFIED`; do not invent boundaries, commands, environments, or coverage.

## Procedure

### 1. Establish the test objective

State what confidence is needed and which claim the tests must support. Examples include behavior correctness, compatibility, persistence integrity, critical journey continuity, or regression prevention.

### 2. Discover boundaries

Identify domain logic, process/component, persistence, external service, API/schema, message/event, user journey, and deployment/runtime boundaries affected by the change.

Load `references/risk-classification.md` for the risk and boundary matrix.

### 3. Classify risks

For each material risk, record:

- affected behavior or asset;
- boundary crossed;
- failure impact and likelihood;
- observability of failure;
- reversibility and blast radius;
- existing evidence and confidence gap.

### 4. Select test levels

Choose the narrowest test level that can provide credible evidence for each risk. Add broader levels only when narrower tests cannot observe the relevant boundary or outcome.

Load `references/test-level-selection.md` for selection and rejection rules.

### 5. Compose a proportionate portfolio

Balance fast local feedback, boundary confidence, compatibility evidence, and critical journey coverage. Avoid ceremonial layers and duplicated assertions.

Load `references/test-portfolio-patterns.md` for representative portfolios.

### 6. Define negative and regression scope

Include material failure paths, invalid inputs, incompatible changes, timeout/retry behavior, data corruption risks, authorization boundaries, and the specific regression being prevented where applicable.

### 7. Define evidence and confidence limits

Specify commands or harnesses only after verification. State what counts as PASS, what remains unsupported, and how skipped, flaky, unavailable, or partial results affect the verdict.

### 8. Review anti-patterns

Load `references/anti-patterns-and-counterexamples.md` before finalizing strategy for substantial production work.

## Normalized output

```yaml
test_strategy:
  objective: <claim requiring evidence>
  context_status: VERIFIED | PARTIAL | NOT_VERIFIED
  risks:
    - id: <stable risk id>
      behavior: <affected behavior>
      boundary: <boundary>
      impact: LOW | MEDIUM | HIGH | CRITICAL
      evidence_gap: <missing confidence>
  portfolio:
    selected:
      - level: unit | integration | contract | acceptance | e2e
        risks: []
        purpose: <why this level is needed>
        evidence_required: []
    rejected:
      - level: unit | integration | contract | acceptance | e2e
        status: NOT_APPLICABLE | NOT_JUSTIFIED | NOT_VERIFIED
        rationale: <why it is not selected>
  negative_paths: []
  regression_scope: []
  environment_assumptions: []
  confidence_limits: []
  handoffs: []
  verdict: READY | NEEDS_WORK | BLOCKED | NOT_VERIFIED
```

## Quality gates

A strategy is `READY` only when:

- objective and affected behavior are explicit;
- material boundaries and risks are reviewable;
- every selected test level maps to at least one risk;
- rejected levels include rationale and correct status semantics;
- adapter selection has not preceded verified stack context;
- negative-path and regression scope are proportionate;
- evidence requirements and confidence limits are explicit;
- product acceptance and merge/release authority remain separate.

## Failure behavior

Return `NEEDS_WORK`, `BLOCKED`, or `NOT_VERIFIED` when:

- acceptance criteria or changed behavior are materially ambiguous;
- repository boundaries or commands are unknown and required;
- the proposed portfolio relies on coverage percentage alone;
- unit tests are used to claim cross-boundary confidence;
- E2E is selected merely because a UI exists;
- BDD or Gherkin is treated as mandatory;
- duplicated E2E assertions add cost without distinct risk coverage;
- flaky, skipped, or unavailable evidence is normalized as PASS.

## Completion evidence

Report:

- verified inputs and known gaps;
- risk and boundary map;
- selected and rejected test levels;
- negative and regression scope;
- evidence requirements and confidence limits;
- applicable handoffs;
- final strategy verdict.

A declared test framework, test file, or coverage number is not strategy evidence by itself.
