---
name: project-instruction-generator
description: Generate or audit concise, runtime-valid Project Instructions for ChatGPT Projects and equivalent project-scoped agent workspaces. Use when a project needs reusable routing, source-of-truth, execution disclosure, repository, completion, capability-evolution, and platform-capacity rules while changing mainly project identity and resource links.
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

Generate a lean project-level bootstrap that tells an agent:

- what the project is;
- which sources govern decisions;
- how work is routed and disclosed;
- which repository and delivery safeguards apply;
- when work may be called complete;
- how verified lessons are reviewed for reusable evolution;
- whether the artifact fits the target runtime.

Project Instructions must reference executable skills rather than copy their full methodology.

## When to Use

Use this skill to:

- create Project Instructions for ChatGPT Projects or a similar scoped workspace;
- standardize instructions across projects;
- convert a long project prompt into a reusable template;
- add workflow, role, skill, evidence, and learning disclosure;
- audit duplicated methodology or runtime-size violations.

Do not use it to:

- replace product specifications, `AGENTS.md`, ADRs, architecture docs, design locks, or acceptance criteria;
- persist execution state or runtime observability;
- invent resources, repository state, issues, branches, limits, or test results;
- automatically refine shared skills without verified evidence and authorization.

## Inputs

Resolve these fields when available:

```yaml
project_name: <required>
project_purpose: <required>
workspace_runtime: <required for paste-ready output>
primary_repository_url: <required when repository-backed>
project_management_url: <required when managed externally>
product_urls: []
custom_gpt_or_runtime_urls: []
additional_repository_urls: []
core_repository_url: https://github.com/puterakahfi/ai-native-core
skills_repository_url: https://github.com/puterakahfi/ai-native-skills
runtime_repository_url: https://github.com/puterakahfi/ai-native-fw
project_specific_sources: []
repository_write_policy: <optional>
additional_non_negotiable_rules: []
instruction_character_limit: <verified runtime value or null>
instruction_limit_provenance: <source or observed validator>
instruction_target_budget: <limit minus safety margin>
```

Do not block on optional fields. Omit unused lines or preserve explicit placeholders. Never fabricate a value or platform limit.

Use [`references/runtime-instruction-limits.md`](references/runtime-instruction-limits.md) to resolve runtime capacity. A supplied limit overrides the profile only when its provenance is explicit and credible.

## Output

Produce:

```text
1. completed Project Instructions artifact;
2. unresolved-placeholder and omitted-section report;
3. source-of-truth and ownership review;
4. exact character-count and runtime-budget report;
5. duplication warnings;
6. generation verification result.
```

Use [`references/project-instructions-template.md`](references/project-instructions-template.md) as the canonical starting template.

## Generation Procedure

### 1. Classify the workspace

Identify:

```text
workspace runtime
project or product identity
repository-backed or advisory-only work
project-management source
canonical core, skills, runtime, and product layers
write and approval boundary
```

Project Instructions are a runtime bootstrap, not the source of truth for every procedure or product fact.

### 2. Resolve runtime capacity

Before drafting:

1. identify the target runtime;
2. load a verified runtime profile when available;
3. record the hard maximum, target budget, safety margin, and provenance;
4. use `NOT_VERIFIED` when the limit is unknown;
5. never reuse ChatGPT's limit for another platform without evidence.

For ChatGPT Projects, use the maintained profile:

```text
hard maximum: 8,000 characters
target budget: 7,200 characters
safety margin: 800 characters
```

The UI validator remains authoritative. Normalize line endings to LF and count Unicode characters for preflight. Keep a margin because provider counting behavior may differ for some Unicode sequences.

### 3. Resolve source ownership

Preserve this default boundary:

```text
ai-native-core
  canonical domain, contracts, terminology, boundaries, quality standards

ai-native-skills
  executable skills, workflows, meta-skills, references, rubrics, evals

ai-native-fw
  orchestration, execution state, runtime integration, observability

product repository
  product intent, implementation, policy, private context, acceptance

project-management system
  roadmap, priority, work hierarchy, dependencies, delivery status
```

Change the mapping only when verified project sources define another valid ownership model.

### 4. Populate project variables

Replace only project variables such as:

```text
{{PROJECT_NAME}}
{{PROJECT_PURPOSE}}
{{PRIMARY_REPOSITORY_URL}}
{{PROJECT_MANAGEMENT_URL}}
{{PRODUCT_URLS}}
{{CUSTOM_GPT_OR_RUNTIME_URLS}}
{{ADDITIONAL_REPOSITORIES}}
{{PROJECT_SPECIFIC_SOURCES}}
{{ADDITIONAL_NON_NEGOTIABLE_RULES}}
```

Keep reusable execution policy stable unless an explicit policy change is requested.

### 5. Enforce the execution loop

Every generated artifact must preserve:

```text
route
→ execute
→ verify
→ deliver
→ learn
→ evolve when justified
```

The loop requires a learning review, not automatic skill modification.

### 6. Keep disclosure observable

Require:

- one primary workflow;
- one owner;
- only relevant specialists and reviewers;
- concise activation disclosure;
- material phase-transition updates for long work;
- a final execution receipt;
- observable evidence for every claim that a skill was applied.

Do not require private chain-of-thought. Require reviewable routing rationale, evidence, decisions, outputs, gate results, limitations, and handoffs.

### 7. Add capability evolution

Route post-execution findings through `skill-evolution` using:

```text
NO_CHANGE
LOCAL_ONLY
EVAL_ONLY
BUG
IMPROVEMENT
RFC
DUPLICATE
DEFERRED_UNVERIFIED
```

Route issues to:

- `ai-native-skills` for executable behavior, workflow ordering, role composition, references, rubrics, or evals;
- `ai-native-core` for canonical meaning, universal contracts, boundaries, or cross-adapter obligations;
- `ai-native-fw` for runtime orchestration, bindings, state, persistence, or observability;
- the product repository for local implementation, policy, architecture decisions, or design locks.

Issue creation requires evidence, duplicate checking, clear ownership, and write authorization.

### 8. Remove duplicated methodology

Replace copied procedures with mandates to load the owning skill.

```text
Too much:
  complete epic matrices, branch algorithms, evidence taxonomies,
  every git command, and the full skill-evolution procedure

Correct:
  Use delivery-work-breakdown for release-unit and topology decisions.
  Use git-workflow after topology is resolved.
  Use skill-evolution after verified execution.
```

Preserve only constraints that genuinely govern the project.

### 9. Validate character capacity

Count the final artifact, excluding commentary and reports outside the text to be pasted.

For a verified runtime profile:

```text
count <= target budget
  capacity gate: PASS

target budget < count <= hard maximum
  capacity gate: NEEDS_WORK
  artifact may fit, but safety margin is insufficient

count > hard maximum
  capacity gate: FAIL
  final verdict cannot be PASS
```

For an unknown limit:

```text
capacity gate: NOT_VERIFIED
platform acceptance: unproven
```

When filesystem execution is available, run:

```bash
python3 skills/project-instruction-generator/scripts/validate-instruction-size.py \
  <project-instructions-file> \
  --runtime chatgpt-projects \
  --hard-maximum 8000 \
  --target-budget 7200 \
  --provenance runtime-profile
```

Report actual count, maximum, target, safety margin, and remaining hard-budget characters. Shorten by removing duplication, optional prose, repeated warnings, and explanatory detail before removing governing rules.

### 10. Verify the artifact

Confirm:

```text
□ project identity and purpose are explicit
□ URLs are supplied or clearly unresolved
□ runtime limit and provenance are resolved or NOT_VERIFIED
□ exact character count and remaining budget are reported
□ output does not exceed a verified hard maximum
□ source-of-truth priority is explicit
□ workflow-router and role-switcher are mandated
□ disclosure precedes substantive work
□ completion uses evidence and acceptance criteria
□ repository inspection precedes modification
□ capability-learning review is present
□ skill evolution is evidence-gated
□ core, skills, runtime, and product ownership is preserved
□ no full skill methodology was copied unnecessarily
□ no repository state, issue, branch, limit, or result was invented
```

## Quality Gates

`PASS` requires:

- project values trace to user input or verified sources;
- reusable policy and project configuration remain separated;
- runtime capacity is verified and the artifact is within the target budget;
- routing, role composition, disclosure, evidence, completion, and evolution are covered;
- missing information is explicit;
- the artifact remains reusable by changing mainly project identity and links.

Use `NEEDS_WORK` when the artifact is complete but bloated, ambiguous, over target budget, or over the hard maximum.

Use `NOT_VERIFIED` for runtime capacity when the platform limit is unknown.

Use `BLOCKED` when required project identity or governing sources cannot be resolved.

## Completion Report

```text
PROJECT INSTRUCTION GENERATION
────────────────────────────────────
Project:
Runtime target:
Template version: 1.1.0
Resolved resources:
Unresolved placeholders:
Omitted optional sections:
Character count:
Hard maximum:
Target budget:
Safety margin:
Remaining hard budget:
Limit provenance:
Runtime capacity: PASS | NEEDS_WORK | FAIL | NOT_VERIFIED
Routing policy: PASS | NEEDS_WORK | BLOCKED
Disclosure policy: PASS | NEEDS_WORK | BLOCKED
Repository policy: PASS | NEEDS_WORK | BLOCKED
Evolution loop: PASS | NEEDS_WORK | BLOCKED
Duplication review: PASS | NEEDS_WORK
Final verdict: PASS | NEEDS_WORK | BLOCKED
```
