---
name: skill-evolution
description: Convert verified lessons from real product work into minimal reusable skill, reference, workflow, eval, or core-contract improvements while preserving package policy, regression evidence, and repository authority.
license: MIT
metadata:
  ai-native-skills.version: 1.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: workflow
  ai-native-skills.requires: "skill-eval git-workflow"
  ai-native-skills.implements: ai-native-core/contracts/workflows/skill-evolution.contract.yaml
  ai-native-skills.contract-version: "^1.0.0"
  ai-native-skills.boundary.covers: '["post_fix_learning_review","reusable_reason_extraction","local_vs_shared_knowledge_classification","target_layer_selection","minimal_skill_or_reference_patch","regression_eval_creation","skill_version_and_promotion_decision","provenance_logging_outside_skill_body"]'
  ai-native-skills.boundary.delegates: '["solving_the_original_product_issue","copying_product_implementation_into_shared_skills","storing_product_specific_breakpoints_routes_or_component_names_in_shared_skills","promoting_unverified_anecdotes","bypassing_repository_write_or_approval_policy","replacing_product_design_locks_or_architecture_decisions"]'
  ai-native-skills.related_skills: '["skill-eval","skill-doctor","skill-authoring-workflow","git-workflow","systematic-debugging"]'
---

# Skill Evolution

## Reviewed core contract interface

Source: `ai-native-core/contracts/workflows/skill-evolution.contract.yaml` · compatible line: `^1.0.0`.

Required inputs include the source case, observed failure, verified fix, before/after evidence, and candidate capability. Outputs include the learning candidate, root reason, generalization report, target layer, minimal patch, regression eval, promotion verdict, commit or no-promotion reason, and provenance record.

## Core rule

```text
verified real case
→ explain why the fix worked
→ classify local versus reusable knowledge
→ test transfer and counterexamples
→ deduplicate against existing ownership
→ patch the smallest correct shared layer
→ add centralized regression evidence
→ validate package, behavior, and conformance
→ promote only with authority and passing gates
```

A resolved product issue always receives a learning review. It is not always promoted.

## Boundary

This workflow owns post-fix learning review and minimal reusable promotion. It does not solve the original product issue, create a capability from an unverified idea, copy product implementation into shared instructions, or bypass repository policy.

Use `skill-authoring-workflow` when the request is intentional creation, accepted redesign, broad migration, or deprecation rather than promotion from a verified case.

## Canonical package sources

Before shaping a promoted patch, load:

```text
contracts/skill-package-policy.yaml
docs/skill-package-standard.md
scripts/validate-skill-packages.py
```

Do not create a second policy or package-local behavioral eval source.

## Automatic invocation

Run before final delivery when:

- a real implementation or design failure was observed;
- a fix was applied;
- relevant runtime, visual, interaction, accessibility, or test verification passed;
- the governing workflow is about to close or deliver.

If no reusable learning exists, return `NO_CHANGE`, `LOCAL_ONLY`, `DUPLICATE`, or `DEFERRED_UNVERIFIED` and continue honest delivery.

## Phase 1 — Record the verified case

Capture:

```yaml
source_case:
  observed_failure: <fact>
  verified_fix: <fact>
  before_after_evidence: []
  candidate_skill_or_workflow: <target or unknown>
  remaining_uncertainty: []
```

Unverified fixes cannot produce shared promotion.

## Phase 2 — Select one target layer

| Defect class | Destination | Shared package change |
|---|---|---:|
| Local implementation defect | product repository | No |
| Product-specific durable decision | product ADR/design lock/context | No |
| Reusable decision rule or gate | target `SKILL.md` | Yes |
| Extended rationale or matrix | target `references/` | Yes |
| Workflow ordering or role gap | workflow `SKILL.md` | Yes |
| Correct rule applied unreliably | `contracts/tests/<skill>.test.yaml` | Eval only |
| Missing cross-adapter obligation | `ai-native-core` | Controlled RFC/contract route |

Product names, routes, class names, exact breakpoints, and local component names remain outside shared instructions unless they are evidence records.

## Phase 3 — Extract and test the reusable reason

The candidate must explain:

1. which assumption failed;
2. why the verified fix worked;
3. decision factors and conditions;
4. counterexamples where the rule should not apply;
5. transfer to at least two materially different contexts;
6. why the candidate target owns the rule.

One successful anecdote is insufficient.

## Phase 4 — Deduplicate

Read the complete target skill, related skills, references, core contract, and existing central behavioral contracts.

Classify:

```text
IMPROVEMENT
EVAL_ONLY
LOCAL_ONLY
DUPLICATE
RFC
DEFERRED_UNVERIFIED
```

Do not append a second wording of an existing principle merely because a new case confirmed it. Add regression coverage or clarify minimally.

## Phase 5 — Apply the minimal patch

When a package change is justified:

- preserve its boundary;
- patch the smallest correct layer;
- bump executable version when behavior changes;
- update dependencies only when they changed;
- keep provenance outside reusable instructions;
- create or update the centralized behavioral contract;
- add tests when bundled scripts or validators change;
- do not create skill-local `evals/` or generated output directories;
- respect branch, write, review, and merge policy.

`EVAL_ONLY` must not create unnecessary package changes.

## Phase 6 — Package and regression gates

A promoted package patch must run:

```bash
skills-ref validate skills/<skill-name>
python scripts/validate-skill-packages.py --skill <skill-name>
python scripts/validate-eval-contracts.py
AI_NATIVE_CORE_DIR=../ai-native-core bash scripts/run-eval.sh --skill <skill-name> --validate-tests
```

Also run applicable:

- bundled executable tests;
- real target behavioral eval using per-case outputs;
- related-skill evals affected by the boundary;
- adapter/core conformance;
- original product verification when feasible;
- documentation and link checks.

Package validation with blocking errors prevents promotion. Missing package evidence returns `DEFERRED_UNVERIFIED`, not `PROMOTED`.

## Phase 7 — Promote

```text
writable branch + authority + all applicable gates pass
→ commit through repository policy

approval-gated
→ prepare exact patch and request approval

read-only or incomplete evidence
→ report not written / deferred
```

## Required report

```yaml
skill_evolution_review:
  verification: PASS | INCOMPLETE
  root_reason: <reason>
  classification: IMPROVEMENT | EVAL_ONLY | LOCAL_ONLY | DUPLICATE | RFC | DEFERRED_UNVERIFIED
  transfer_test: PASS | FAIL | NOT_VERIFIED
  duplicate_check: NEW | EXISTING | OVERLAP
  target: <file or none>
  package_status: COMPLIANT | PARTIAL | EXEMPT | ERROR | NOT_VERIFIED
  behavioral_status: APPLIED | PARTIAL | GHOST | INCOMPLETE | NOT_RUN
  executable_test_status: PASS | FAIL | NOT_APPLICABLE | NOT_VERIFIED
  conformance_status: PASS | FAIL | NOT_APPLICABLE | NOT_VERIFIED
  regression_eval: <file/result or none>
  commit: <sha or not written>
  provenance: <location>
  known_gaps: []
```

## Hard gates

Fail or defer promotion when:

- the original fix is unverified;
- the candidate is product-specific without reusable reasoning;
- transfer or counterexample testing fails;
- another capability already owns the rule;
- no centralized regression evidence exists;
- package validation has blocking errors;
- required executable tests are missing;
- related evals or conformance fail;
- repository authority is missing.
