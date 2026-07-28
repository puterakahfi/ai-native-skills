---
name: end-to-end-testing
description: Design and verify critical user or system journeys across the real system boundary using risk-based scope, explicit environment readiness, stable assertions, diagnostics, cleanup, and fail-closed evidence. Browser automation is optional.
license: MIT
metadata:
  ai-native-skills.version: 0.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.requires: "test-strategy acceptance-testing integration-testing decision-provenance implementation-context-discovery"
  ai-native-skills.related_skills: '["behavior-driven-development","contract-testing","resilience-engineering","observability-design"]'
---

# End-to-End Testing

## Ownership

This skill owns evidence for a selected critical journey crossing the real system boundary. It does not define product acceptance, require a browser, or replace lower-level tests.

## Applicability

Use only when a material risk depends on composition across multiple deployed components, services, protocols, or a real user journey. Return `NOT_JUSTIFIED` when lower-level evidence is sufficient.

## Procedure

```text
verify risk and journey
→ define system boundary and environment readiness
→ select browser or non-browser execution surface
→ establish authentication, state, data isolation, observability, and cleanup
→ execute positive and material failure paths
→ classify deterministic, environmental, and flaky outcomes
→ preserve diagnostics and evidence
```

Load `references/critical-journey-design.md` for detailed selection and stability rules.

## Quality gates

- journey maps to an explicit risk;
- the minimum credible E2E surface is selected;
- environment, authentication, data, and cleanup contracts are explicit;
- assertions target observable outcomes, not incidental selectors or timing;
- diagnostics identify the failing boundary;
- bounded retry diagnoses flakiness but never converts uncertain evidence to PASS;
- browser automation is selected only when the journey requires it;
- failing, flaky, skipped, unavailable, or unexecuted evidence remains non-PASS.

## Normalized output

```yaml
end_to_end_testing:
  applicability: APPLICABLE | NOT_JUSTIFIED | NOT_APPLICABLE
  context_status: VERIFIED | PARTIAL | NOT_VERIFIED
  journey: <risk-linked journey>
  boundary: []
  execution_surface: browser | api | protocol | cross_service | other
  environment_readiness: READY | PARTIAL | UNAVAILABLE
  commands: []
  results: []
  failures: []
  flaky_results: []
  diagnostics: []
  limitations: []
  verdict: PASS | FAIL | FLAKY | NEEDS_WORK | NOT_VERIFIED
```

## Stop conditions

Stop and return non-PASS when the environment cannot represent the claimed boundary, test data cannot be isolated, cleanup is unsafe, or flakiness prevents confidence.

## Adapter boundary

Playwright, Cypress, Selenium, browser drivers, API clients, and orchestration tools are adapters. Replacing an adapter must not change canonical journey-selection or evidence semantics.