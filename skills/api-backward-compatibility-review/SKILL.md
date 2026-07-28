---
name: api-backward-compatibility-review
description: Review a proposed API change against an explicit prior contract, classify compatibility impact, and require migration, deprecation, consumer, versioning, and release evidence. Use before changing a published or consumed API; do not use as the primary skill for greenfield API design or implementation-only debugging.
license: MIT
metadata:
  ai-native-skills.version: 1.0.1
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.requires: "api-contract decision-provenance"
  ai-native-skills.related_skills: '["api-contract","architecture-review","contract-testing","decision-provenance","deployment-workflow"]'
---

# API Backward Compatibility Review

Determine whether a proposed API change can be released without silently breaking existing consumers.

## Boundary

This skill owns:

- comparison of an explicit previous and proposed API contract;
- compatibility classification and review rationale;
- consumer-impact and migration requirements;
- deprecation, versioning, rollout, and rollback evidence requirements;
- a release recommendation constrained by available evidence and authority.

It does not own:

- greenfield API design (`api-contract`);
- implementation of the change;
- provider-specific diff tooling;
- product-specific release approval;
- automatic semantic-version publication.

## Required inputs

```yaml
compatibility_review:
  previous_contract: <immutable contract or NOT_VERIFIED>
  proposed_contract: <candidate contract or NOT_VERIFIED>
  consumers: []
  compatibility_dimensions: []
  deprecation_policy: <verified policy or NOT_VERIFIED>
  versioning_policy: <verified policy or NOT_VERIFIED>
  rollout_constraints: []
  approval_authority: <verified or NOT_VERIFIED>
```

Do not infer compatibility from implementation intent alone. Missing previous contract means the compatibility verdict is `NOT_VERIFIED`.

## Compatibility dimensions

Review only dimensions relevant to the API, and state which were not applicable:

- source compatibility;
- binary compatibility;
- wire or schema compatibility;
- behavioral compatibility;
- operational compatibility, including limits, latency, ordering, retries, and failure behavior;
- security and authorization compatibility.

## Classification

Use exactly one primary compatibility result:

```text
ADDITIVE                 existing consumers remain valid; new behavior is opt-in
COMPATIBLE               observable contract remains compatible for supported consumers
CONDITIONALLY_COMPATIBLE compatible only after declared migration, rollout, or consumer conditions
BREAKING                 at least one supported consumer contract is invalidated
NOT_VERIFIED             evidence is insufficient for a defensible classification
```

A syntactically additive field can still be behaviorally or operationally breaking. A version-number change does not prove compatibility.

Report approval independently as `APPROVED`, `REJECTED`, or `NOT_VERIFIED`. Never downgrade or upgrade the compatibility classification merely because approval authority is absent.

## Procedure

1. Verify repository, issue, baseline revision, proposed revision, consumers, and review scope.
2. Normalize previous and proposed contracts into comparable operations, inputs, outputs, errors, invariants, and operational promises.
3. List changes without assigning compatibility yet.
4. For each change, inspect affected compatibility dimensions and known consumers.
5. Classify each change as additive, compatible, conditional, breaking, or not verified.
6. Aggregate the strictest supported result; do not average away a breaking consumer impact.
7. Define required migration, deprecation, versioning, rollout, monitoring, and rollback actions.
8. Separate evidence, inference, assumptions, compatibility classification, and approval.
9. Issue a review report and explicit next gate.

## Breaking-change signals

Treat these as breaking unless verified evidence proves otherwise:

- removing or renaming an operation, field, event, error, or enum value;
- making an optional input required;
- narrowing accepted values or increasing validation strictness;
- changing units, defaults, ordering, idempotency, retry, pagination, or timeout behavior;
- changing authentication, authorization, scopes, tenancy, or data visibility;
- changing response semantics while preserving the same shape;
- lowering limits or support guarantees used by existing consumers;
- changing event delivery, duplication, or ordering guarantees.

## Required output

```yaml
api_backward_compatibility_review:
  baseline: <revision or NOT_VERIFIED>
  proposal: <revision or NOT_VERIFIED>
  classification: ADDITIVE | COMPATIBLE | CONDITIONALLY_COMPATIBLE | BREAKING | NOT_VERIFIED
  dimensions_reviewed: []
  changes:
    - change: <description>
      affected_consumers: []
      classification: <result>
      evidence: []
      assumptions: []
  migration_requirements: []
  deprecation_requirements: []
  versioning_requirements: []
  rollout_and_rollback: []
  approval_status: APPROVED | REJECTED | NOT_VERIFIED
  approval_evidence: []
  known_gaps: []
  next_gate: <one exact action>
```

## Hard gates

Return compatibility classification `NOT_VERIFIED` or `BREAKING` rather than a positive compatibility result when:

- the previous contract or proposed contract is missing;
- consumer impact is unknown for a destructive or semantic change;
- a migration is required but no migration path exists;
- deprecation timing violates verified policy;
- rollout or rollback evidence is missing for a conditional change.

Return approval status `NOT_VERIFIED` when the reviewer lacks verified release authority. Compatibility evidence may still support a classification, but release approval remains blocked.

## Evidence rules

- Contract files, schemas, generated specifications, consumer tests, and production traces are evidence.
- Issue descriptions and author intent are context, not proof of compatibility.
- Structural contract tests do not prove behavioral or operational compatibility.
- Unknown consumers remain a disclosed risk; do not silently classify them as unaffected.

## Completion report

Report independently:

- compatibility classification;
- package status;
- behavioral-evaluation status;
- executable-test status;
- core conformance status;
- approval status;
- unresolved consumer and rollout gaps.
