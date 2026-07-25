---
name: bugfix-workflow
description: Guided bugfix workflow — reproduce, investigate, classify repository-convention impact, discover implementation context when material, fix, verify, submit, and review. Stack-sensitive fixes must map canonical repository systems before code; isolated fixes remain lightweight.
license: MIT
metadata:
  ai-native-skills.version: 1.2.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.requires: "systematic-debugging implementation-context-discovery master-engineer security-review test-driven-development architecture-review"
  ai-native-skills.type: workflow
  ai-native-skills.implements: ai-native-core/contracts/workflows/bugfix.contract.yaml
  ai-native-skills.contract-version: "~0.3"
  ai-native-skills.skill_load_order: '[{"phase":"investigate","load":["systematic-debugging"]},{"phase":"pre-fix-context","load":["implementation-context-discovery"],"condition":"material_repository_conventions_affected"},{"phase":"fix","load":["systematic-debugging"]},{"phase":"review","load":["architecture-review"]}]'
  ai-native-skills.skills: '{"required":["systematic-debugging","architecture-review"],"optional":["implementation-context-discovery","master-engineer"]}'
  ai-native-skills.related_skills: '["implementation-context-discovery","architecture-review","test-driven-development","decision-provenance"]'
---

# Bugfix Workflow

## Reviewed core contract interface

Source: `ai-native-core/contracts/workflows/bugfix.contract.yaml` · compatible line: `~0.3`

```yaml
required_phases:
  - reproduce
  - investigate
  - fix
  - verify
  - submit
  - review
quality_gates:
  - red_loop_must_exist_before_fix
  - root_cause_must_be_stated_before_fix
  - verification_evidence_required_before_submission
  - submission_must_reference_issue_tracker_item
  - no_merge_without_approval
  - fix_must_not_bundle_unrelated_changes
```

This adapter preserves the canonical six-phase lifecycle. The pre-fix repository-context gate is a conditional adapter refinement inside the investigate-to-fix transition; it does not add a universal discovery burden to isolated fixes.

## Overview

```text
reproduce
→ investigate root cause
→ classify implementation-context impact
→ discover and lock repository conventions when material
→ regression test and smallest root-cause fix
→ verify
→ submit
→ independent architecture review and approval
```

Branch strategy, issue tracker, verification method, and approval policy remain product-defined.

## Hard rules

1. Reproduce before fixing.
2. State the root cause before fixing.
3. Before code, classify whether the fix materially affects repository implementation conventions.
4. When material, run `implementation-context-discovery` and produce convention locks plus implementation mapping before Phase 3.
5. Package presence alone does not establish canonicality.
6. Reuse, existing variants, bounded extension, composition, canonical registry, or semantic-native implementation precedes local duplication or a dependency proposal.
7. Unknown material stack context is `NOT_VERIFIED` or `BLOCKED`; do not guess.
8. When implementation context is not material, record `NOT_APPLICABLE` with evidence and keep the workflow lightweight.
9. One root-cause fix at a time; no unrelated cleanup, migration, redesign, or dependency change.
10. Architecture review remains independent after implementation.

## Required skills

| Phase | Skill | Applicability |
|---|---|---|
| Investigate | `systematic-debugging` | required |
| Pre-fix context | `implementation-context-discovery` | conditional when material repository conventions are affected |
| Fix | `systematic-debugging`; `master-engineer` when needed | required / conditional |
| Review | `architecture-review` | required |

## Phase 1 — Reproduce

**Gate:** a deterministic red loop exists before any fix.

1. Read the issue and governing acceptance criteria completely.
2. Build one tight command or interaction that reproduces the exact symptom.
3. Confirm the loop fails for the expected reason.
4. Record affected surface, environment, inputs, and observed output.

```bash
pytest tests/test_module.py::test_name -v
curl -X POST http://localhost:8000/endpoint -d '{"payload":"..."}'
```

**Done when:** the bug can be triggered on demand and the failure boundary is explicit.

## Phase 2 — Investigate

**Gate:** root cause is stated before fix.

Load and follow `systematic-debugging`. Separate symptom, triggering condition, owning layer, and root cause.

```text
The root cause is <X> because <evidence Y>, in owner/layer <Z>.
```

Do not use visible UI symptoms alone to choose a component, styling, or dependency correction.

**Done when:** root cause, affected layer, and candidate correction boundary are evidence-backed.

## Pre-fix implementation-context gate

Classify the change before entering Phase 3.

### Material context triggers

Run `implementation-context-discovery` when the correction can affect any of:

```text
framework or runtime usage
shared components, primitives, variants, organisms, or templates
styling, CSS strategy, themes, semantic tokens, typography, or iconography
state, forms, query/cache, validation, table, animation, or data tooling
aliases, wrappers, shared utilities, module placement, build, tests, or stories
dependencies, vendored source, canonical registry additions, or migration targets
```

A small diff is still material when it bypasses or changes a shared system.

### Required mapping when material

```yaml
bugfix_implementation_context:
  applicability: MATERIAL
  repository_ref: <ref>
  affected_capability_families: []
  implementation_context_profile_ref: <ref>
  canonicality_decisions: []
  convention_locks: []
  component_and_variant_coverage: []
  canonical_tokens_styles_icons: []
  state_form_query_data_conventions: []
  selected_decision: <reuse | reuse_variant | extend | compose | registry | product_specific | semantic_native>
  expected_paths_and_imports: []
  prohibited_parallel_systems: []
  dependency_decisions: []
  evidence_gaps: []
  verification_plan: []
```

The selected decision must follow:

```text
existing canonical implementation
→ existing variant
→ bounded extension
→ canonical primitive composition
→ canonical registry component
→ product-specific adapter using canonical primitives
→ semantic native element when sufficient
→ dependency only after a proven capability gap and authority
```

If canonicality, coverage, or authority is unknown, stop the affected fix slice with `NOT_VERIFIED` or `BLOCKED`.

### Lightweight path

When the bug is isolated from material repository conventions, record:

```yaml
bugfix_implementation_context:
  applicability: NOT_APPLICABLE
  evidence:
    - <why framework/component/styling/icon/state/form/query/data conventions are unaffected>
  protected_systems: []
```

Examples include a bounded pure-domain calculation defect or an isolated parser branch whose correction does not change shared implementation systems. `NOT_APPLICABLE` is a reasoned classification, not a skipped check.

**Gate:** material fixes cannot enter Phase 3 without the mapping; non-material fixes cannot enter Phase 3 without the `NOT_APPLICABLE` evidence.

## Phase 3 — Fix

**Gate:** one mapped root-cause change at a time.

1. Write a regression test that reproduces the bug (`RED`).
2. Implement the smallest fix targeting the stated root cause.
3. When context is material, reuse/extend/compose only through the approved mapping.
4. Confirm the regression test passes (`GREEN`).
5. Audit changed paths, imports, dependencies, and shared-system effects.

If the fix requires a different component, dependency, token system, path, or scope than the mapping allows:

```text
stop
→ return to implementation-context-discovery and decision provenance
→ update mapping and authority
→ continue only after the gate passes
```

**Done when:** regression test is green, the root cause is addressed, and no unapproved convention or scope drift exists.

## Phase 4 — Verify

**Gate:** verification evidence exists before submission.

Run the product-defined full suite plus checks appropriate to the affected boundary:

```text
regression and full tests
lint, typecheck, build
changed import/path/dependency audit
canonical component/token/icon/state/form/query/data conformance
rendered/runtime/accessibility evidence when behavior is user-facing
absence of prohibited parallel systems
```

Source/import alignment does not prove runtime, visual, interaction, or accessibility acceptance.

**Done when:** technical evidence and implementation-context conformance are recorded honestly.

## Phase 5 — Submit

**Gate:** submission references the issue and the approved delivery topology.

Include:

- symptom and deterministic reproduction;
- root cause;
- context applicability verdict;
- implementation-context mapping or `NOT_APPLICABLE` evidence;
- fix summary and regression test;
- verification evidence;
- scope and dependency changes;
- known gaps.

**Done when:** submission is open against the approved target with complete evidence.

## Phase 6 — Review

**Gate:** independent approval before merge.

Load `architecture-review`. Verify the actual diff against the engineering contract and discovered implementation context. Compilation or a green regression test is not architecture approval.

- [ ] root-cause correction is bounded;
- [ ] canonical systems were preserved;
- [ ] no unauthorized dependency or parallel system exists;
- [ ] tests and evidence match the affected boundary;
- [ ] feedback is addressed;
- [ ] required approval and merge authorization exist.

## Quick reference

| Phase | Gate | Done when |
|---|---|---|
| Reproduce | Red loop | Exact symptom is deterministic |
| Investigate | Root cause | Root cause and owner are stated |
| Context gate | Material mapping or reasoned `NOT_APPLICABLE` | Fix path is repository-safe |
| Fix | One mapped change | Regression green; no drift |
| Verify | Evidence | Technical and convention checks resolved |
| Submit | Issue and topology traceability | Reviewable submission open |
| Review | Independent approval | Approved and authorized for merge |

## Common pitfalls

1. Fixing before reproduction.
2. Treating the visible symptom as root cause.
3. Assuming an installed package is canonical.
4. Building a local component or CSS workaround before inspecting shared systems.
5. Marking context `NOT_APPLICABLE` without evidence.
6. Allowing a new dependency because it is convenient or familiar.
7. Bundling cleanup, redesign, migration, or framework changes.
8. Treating green tests or compilation as architecture approval.
