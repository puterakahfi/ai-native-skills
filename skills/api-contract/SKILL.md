---
name: api-contract
description: Design, enforce, and version API contracts between services — OpenAPI spec, consumer-driven contract testing, breaking change detection, versioning strategy, and deprecation lifecycle.
license: MIT
metadata:
  ai-native-skills.version: 1.0.1
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/architecture/api-contract.contract.yaml
  ai-native-skills.contract-version: "~0.1"
  ai-native-skills.related_skills: '["service-design", "event-driven-design", "security-review"]'
---

# API Contract

## Core contract interface

```yaml
required_inputs:
  - api_description_or_spec
allowed_outputs:
  - openapi_spec
  - contract_test_suite
  - versioning_decision
  - breaking_change_report
  - consumer_impact_analysis
quality_gates:
  - api_must_have_explicit_versioning_strategy
  - breaking_changes_must_be_detected_before_deploy
  - contract_tests_must_exist_for_every_consumer
  - no_undocumented_endpoints_in_production
  - error_responses_must_follow_consistent_schema
  - backward_compatibility_must_be_preserved_within_major_version
  - api_design_must_be_consumer_driven
  - deprecation_must_be_announced_before_removal
```

Start from the `api_description_or_spec`; missing source material is `NOT_VERIFIED`, not permission to invent an API. Return only the applicable declared outputs. Preserve backward compatibility within one major version, detect breaking changes before deploy, reject undocumented production endpoints, and announce deprecation before removal.

> **HARD RULES**
> - Contract before implementation — write the OpenAPI spec first, then code
> - Breaking changes require a version bump — never silently break consumers
> - Consumer-driven contract testing preferred over provider-defined

## Quick Reference

| Phase | What to Do | Reference |
|---|---|---|
| Design & versioning | Write OpenAPI spec, declare versioning strategy, identify breaking vs non-breaking changes | [contract-first-and-versioning.md](references/contract-first-and-versioning.md) |
| Testing, errors & lifecycle | Consumer-driven Pact tests, error schema standard, deprecation lifecycle, CI gate | [consumer-testing-and-lifecycle.md](references/consumer-testing-and-lifecycle.md) |

## When to Use This Skill

- Designing a new API endpoint or service
- Changing an existing API (adding/removing fields, endpoints)
- Setting up CI to catch breaking changes
- Deprecating an old API version

## Decision Flow

```
New API?
  └─ Write OpenAPI spec FIRST → generate tests → implement against tests

Changing existing API?
  └─ Is it a breaking change? (remove field, rename, type change, make required)
       ├─ YES → MAJOR version bump required (v1 → v2)
       └─ NO  → MINOR bump (new optional field, new endpoint)

Known consumers?
  └─ Write consumer-driven Pact tests → run in CI against provider
```

## Breaking vs Non-Breaking

| ❌ Breaking (needs version bump) | ✅ Non-Breaking (safe) |
|---|---|
| Remove field from response | Add new optional field |
| Rename field | Add new endpoint |
| Change field type | Add new enum value |
| Make optional field required | Loosen validation |
| Remove endpoint | — |
| Change HTTP method | — |

## Gates

- [ ] OpenAPI spec written before first line of implementation?
- [ ] Versioning strategy declared in spec?
- [ ] All endpoints: request + response + errors documented?
- [ ] Error responses follow consistent schema (code, message, details)?
- [ ] Consumer-driven contract tests exist for known consumers?
- [ ] `oasdiff` (or equivalent) in CI — fails on breaking change in same major version?
- [ ] Deprecation policy documented with sunset date + headers?

---

Load [contract-first-and-versioning.md](references/contract-first-and-versioning.md) for OpenAPI spec example, versioning strategies, and breaking vs non-breaking change catalogue.

Load [consumer-testing-and-lifecycle.md](references/consumer-testing-and-lifecycle.md) for Pact consumer/provider setup, error response standard, HTTP status codes, deprecation headers, and CI gate setup.
