---
name: contract-testing
description: Verify provider-consumer compatibility across APIs, schemas, messages, events, and versioned interfaces without replacing broader integration testing. Use for compatibility evolution, breaking-change detection, responsibility boundaries, and contract evidence.
license: MIT
metadata:
  ai-native-skills.version: 0.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.requires: "test-strategy decision-provenance implementation-context-discovery"
  ai-native-skills.related_skills: '["api-contract","integration-testing","acceptance-testing","test-driven-development"]'
---

# Contract Testing

## Ownership

This skill owns executable compatibility evidence between a provider and one or more consumers. It covers API, schema, message, event, versioning, lifecycle, deprecation, and negative compatibility cases.

`api-contract` retains ownership of interface design and lifecycle decisions. `integration-testing` retains component/dependency behavior. This skill verifies whether an agreed interface remains compatible; it must not redefine that interface.

## Procedure

```text
verify contract source and authority
→ identify provider, consumers, and versions
→ classify compatibility promises
→ select executable examples and negative cases
→ verify provider and consumer responsibilities
→ execute verified adapter command
→ report compatibility evidence and limitations
```

Load `references/compatibility-and-responsibility.md` for evolution and responsibility rules.

## Required decisions

- authoritative contract source;
- provider and known consumers;
- backward, forward, or exact compatibility promise;
- version and deprecation window;
- positive and negative cases;
- adapter fidelity and verified command;
- unsupported consumers or environments.

## Quality gates

- provider and consumer responsibilities are explicit;
- compatibility promise is named;
- breaking changes are detectable;
- false compatibility from permissive mocks or incomplete fixtures is rejected;
- asynchronous messages include required/optional fields and evolution rules;
- skipped, stale, unavailable, or unexecuted evidence cannot become PASS;
- compatibility evidence does not override product acceptance or release authorization.

## Normalized output

```yaml
contract_testing:
  context_status: VERIFIED | PARTIAL | NOT_VERIFIED
  contract_source: <verified source>
  provider: <provider>
  consumers: []
  compatibility: backward | forward | exact | versioned
  cases:
    compatible: []
    breaking: []
    negative: []
    deprecation: []
  execution:
    command: <verified command or null>
    result: PASS | FAIL | FLAKY | SKIPPED | UNAVAILABLE | NOT_EXECUTED
  limitations: []
  verdict: PASS | NEEDS_WORK | NOT_VERIFIED | NOT_APPLICABLE
```
