---
name: project-instruction-generator
description: Generate or audit concise, runtime-valid Project Instructions for ChatGPT Projects and equivalent project-scoped agent workspaces. Use when a project needs reusable routing, source-of-truth, execution disclosure, repository, scope-containment, feature-sized delivery, completion, capability-evolution, and platform-capacity rules while changing mainly project identity and resource links.
license: MIT
metadata:
  ai-native-skills.version: 1.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.requires: "workflow-router role-switcher skill-evolution"
  ai-native-skills.related_skills: '["product-manager","delivery-work-breakdown","decision-provenance","implementation-context-discovery","git-workflow","readability","skill-eval"]'
---

# Project Instruction Generator

## Purpose

Generate a lean project bootstrap covering project identity, source priority, routing, disclosure, repository safeguards, scope containment, feature-sized execution, completion, learning, and runtime capacity.

Reference executable skills instead of copying their full methodology.

## When to Use

Use for creating, standardizing, or auditing Project Instructions for ChatGPT Projects and equivalent workspaces.

Do not use it to replace specifications or acceptance criteria, invent repository/runtime evidence, activate optional ideas without approval, prescribe one branch/PR/CI run per tiny fragment, or automatically refine shared capabilities.

## Inputs

```yaml
project_name: <required>
project_purpose: <required>
workspace_runtime: <required for paste-ready output>
primary_repository_url: <required when repository-backed>
project_management_url: <required when managed externally>
product_urls: []
custom_gpt_or_runtime_urls: []
additional_repository_urls: []
project_specific_sources: []
repository_write_policy: <optional>
additional_non_negotiable_rules: []
instruction_character_limit: <verified value or null>
instruction_limit_provenance: <source or validator>
instruction_target_budget: <limit minus safety margin>
```

Default shared sources:

```text
core:    https://github.com/puterakahfi/ai-native-core
skills:  https://github.com/puterakahfi/ai-native-skills
runtime: https://github.com/puterakahfi/ai-native-fw
```

Do not block on optional fields. Never fabricate values or limits.

Use [`references/runtime-instruction-limits.md`](references/runtime-instruction-limits.md) and [`references/project-instructions-template.md`](references/project-instructions-template.md).

## Output

Produce the completed artifact, unresolved/omitted report, ownership review, scope and delivery-granularity review, exact capacity report, duplication warnings, and verification verdict.

## Procedure

### 1. Resolve workspace and ownership

Identify runtime, project identity, repository mode, project-management source, write/approval boundary, and source ownership.

```text
ai-native-core   canonical meaning, contracts, boundaries, standards
ai-native-skills executable skills, workflows, references, evals
ai-native-fw     orchestration, state, integration, observability
product repo     product intent, implementation, policy, acceptance
project system   roadmap, priority, hierarchy, dependencies, status
```

Project Instructions are a runtime bootstrap, not the source of truth for every procedure or product fact.

### 2. Resolve runtime capacity

For ChatGPT Projects:

```text
hard maximum: 8,000 characters
target budget: 7,200 characters
safety margin: 800 characters
```

Record provenance. The UI validator remains authoritative. Use `NOT_VERIFIED` for unknown limits and never transfer one provider's limit to another without evidence.

### 3. Populate project variables

Replace project identity, purpose, URLs, sources, and explicit non-negotiable rules. Keep reusable policy stable unless an explicit policy change is requested.

### 4. Enforce routing and disclosure

Preserve:

```text
route → execute → verify → deliver → learn → evolve when justified
```

Require exactly one primary workflow, one owner, relevant specialists/reviewers, concise execution disclosure, material transition updates, and a final execution receipt.

A claimed skill application must produce an observable decision, artifact, finding, evidence item, or gate result. Require reviewable rationale and evidence, not private chain-of-thought.

### 5. Enforce scope containment

Define:

```text
active scope
= explicit objective
+ acceptance criteria
+ approved dependencies
+ required validation
```

Require:

- execute only work traceable to the active issue, project item, or explicit user instruction;
- keep useful but unrequested ideas as deferred recommendations;
- require explicit approval before adding sibling features or redesigning adjacent systems;
- do not use quality, cleanup, or architecture enthusiasm as permission to expand scope;
- admit a new security, correctness, data-loss, or release blocker only when disclosed and necessary to complete the active outcome.

### 6. Enforce feature-sized execution

`delivery-work-breakdown` owns formal classification and topology. Generated instructions must preserve this operational shorthand:

```text
epic
  combined outcome requiring dependent features

feature
  coherent, independently reviewable capability or complete flow slice

task
  implementation work contributing to a feature;
  not a delivery outcome unless independently releasable
```

Require:

- plan tasks separately when useful, but execute and validate a coherent batch that completes an observable feature slice;
- examples include a complete landing page, detail page, settings flow, API capability, or another end-to-end outcome;
- avoid separate branches, PRs, commits, or GitHub Actions runs for trivial fragments that can be safely completed and reviewed together;
- choose boundaries from acceptance, risk, ownership, reversibility, and independent releasability—not file count;
- complete the requested flow and parent acceptance criteria before optional polish, speculative cleanup, broad refactoring, or refinement;
- refine earlier only when explicitly required or proven to block flow completion.

### 7. Preserve repository, completion, and evolution safeguards

Require repository inspection before modification, explicit branch/PR topology, acceptance evidence, authorization before merge, and honest incomplete states.

Route learning through `skill-evolution`:

```text
NO_CHANGE | LOCAL_ONLY | EVAL_ONLY | BUG | IMPROVEMENT | RFC | DUPLICATE | DEFERRED_UNVERIFIED
```

Route executable behavior to `ai-native-skills`, canonical contracts to `ai-native-core`, runtime orchestration/state to `ai-native-fw`, and local implementation/policy to the product repository.

Create an issue only with a verified case, observed/expected behavior, evidence, reusable gap, duplicate check, owner, and write authorization.

### 8. Remove duplication

Replace copied delivery matrices, git algorithms, evidence taxonomies, and evolution procedures with mandates to load the owning skills. Preserve only project-governing constraints.

### 9. Validate capacity

Count only the paste-ready artifact.

```text
count <= target budget            PASS
target budget < count <= maximum  NEEDS_WORK
count > maximum                   FAIL
unknown limit                     NOT_VERIFIED
```

When filesystem execution is available:

```bash
python3 skills/project-instruction-generator/scripts/validate-instruction-size.py \
  <project-instructions-file> \
  --runtime chatgpt-projects \
  --hard-maximum 8000 \
  --target-budget 7200 \
  --provenance runtime-profile
```

Report actual count, maximum, target, margin, and remaining hard budget. Remove duplication before governing rules.

### 10. Verify

```text
□ identity, purpose, resources, and source priority are explicit
□ workflow-router and role-switcher are mandated
□ disclosure precedes substantive work
□ repository inspection precedes modification
□ active scope is acceptance-traceable
□ out-of-scope ideas are deferred unless approved
□ epic, feature, and task boundaries are explicit
□ coherent feature slices replace avoidable micro-task and CI churn
□ requested flow completes before optional refinement
□ completion uses acceptance and evidence
□ capability learning is evidence-gated
□ ownership boundaries are preserved
□ capacity is verified or NOT_VERIFIED
□ no state, limit, approval, or result was invented
```

## Quality Gates

`PASS` requires traceable values, routing and disclosure, scope containment, coherent feature-sized delivery, flow completion before refinement, evidence-backed completion, ownership preservation, and a final artifact within target budget.

Use `NEEDS_WORK` for bloated, ambiguous, over-budget, scope-permissive, micro-fragmented, or refinement-first output. Use `NOT_VERIFIED` for unknown capacity/evidence and `BLOCKED` when required identity or governing sources cannot be resolved.

## Completion Report

```text
PROJECT INSTRUCTION GENERATION
────────────────────────────────────
Project:
Runtime target:
Template version: 1.1.0
Resolved resources:
Unresolved placeholders:
Character count:
Hard maximum:
Target budget:
Safety margin:
Remaining hard budget:
Limit provenance:
Runtime capacity: PASS | NEEDS_WORK | FAIL | NOT_VERIFIED
Routing policy: PASS | NEEDS_WORK | BLOCKED
Repository policy: PASS | NEEDS_WORK | BLOCKED
Scope containment: PASS | NEEDS_WORK | BLOCKED
Delivery granularity: PASS | NEEDS_WORK | BLOCKED
Flow before refinement: PASS | NEEDS_WORK | BLOCKED
Evolution loop: PASS | NEEDS_WORK | BLOCKED
Final verdict: PASS | NEEDS_WORK | BLOCKED
```
