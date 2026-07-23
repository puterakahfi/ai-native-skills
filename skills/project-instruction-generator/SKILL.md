---
name: project-instruction-generator
description: Generate or audit concise, standardized Project Instructions for ChatGPT Projects and equivalent project-scoped agent workspaces. Use when a project needs reusable routing, source-of-truth, execution disclosure, repository, completion, and capability-evolution rules while changing mainly project identity and resource links.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.requires: "workflow-router role-switcher skill-evolution"
  ai-native-skills.related_skills: '["product-manager","delivery-work-breakdown","decision-provenance","implementation-context-discovery","git-workflow","skill-eval"]'
---

# Project Instruction Generator

## Purpose

Generate a lean project-level bootstrap that tells an agent:

- what the project is;
- which sources govern decisions;
- how work is routed and disclosed;
- which repository and delivery safeguards apply;
- when work may be called complete;
- how verified execution lessons are reviewed for reusable evolution.

The generated Project Instructions must reference executable skills rather than copy their complete methodology.

## When to Use

Use this skill when the user asks to:

- create Project Instructions for ChatGPT Projects or a similar scoped workspace;
- standardize instructions across multiple projects;
- convert a long project prompt into a reusable template;
- add workflow, role, skill, evidence, and learning disclosure to every project thread;
- audit whether existing Project Instructions duplicate too much skill methodology.

Do not use this skill to:

- author the complete product specification;
- replace repository `AGENTS.md`, architecture docs, ADRs, design locks, or acceptance criteria;
- persist execution state or runtime observability;
- invent project resources, repository contents, issues, branches, or delivery status;
- automatically refine shared skills without verified evidence and repository authorization.

## Inputs

Resolve these fields before generation when available:

```yaml
project_name: <required>
project_purpose: <required>
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
```

Do not block generation for optional missing fields. Omit unused resource lines or preserve an explicit placeholder. Never fabricate a value.

## Output

Produce:

```text
1. completed Project Instructions artifact;
2. unresolved-placeholder report;
3. omitted optional sections;
4. instruction-size or duplication warnings;
5. source-of-truth and ownership review;
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
canonical core, skill, runtime, and product layers
write and approval boundary
```

A ChatGPT Project instruction is a runtime bootstrap. It is not the source of truth for every procedure or product fact.

### 2. Resolve source ownership

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

Change this mapping only when verified project sources define a different valid ownership model.

### 3. Populate only project variables

Replace template variables such as:

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

Keep the reusable execution policy stable unless the user explicitly requests a policy change.

### 4. Enforce the execution loop

Every generated template must preserve:

```text
route
→ execute
→ verify
→ deliver
→ learn
→ evolve when justified
```

The loop does not mean every run modifies a skill. It means every substantive run closes with a capability-learning review.

### 5. Keep disclosure observable

The template must require:

- one primary workflow;
- one owner;
- only relevant specialists and reviewers;
- concise activation disclosure before substantive work;
- material phase-transition updates for long tasks;
- a final execution receipt;
- observable evidence for any claim that a skill was applied.

Do not require private chain-of-thought. Require reviewable routing rationale, evidence, decisions, outputs, gate results, limitations, and handoffs.

### 6. Add capability evolution

The generated template must route post-execution findings through `skill-evolution` and distinguish:

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

Route the issue to:

- `ai-native-skills` for executable behavior, workflow ordering, role composition, references, or evals;
- `ai-native-core` for canonical meaning, universal contracts, boundaries, or cross-adapter obligations;
- `ai-native-fw` for runtime orchestration, persistence, bindings, state, or observability;
- the product repository for local implementation, product policy, architecture decisions, or design locks.

Issue creation requires verified evidence, duplicate checking, clear ownership, and write authorization. Otherwise produce a draft or `DEFERRED_UNVERIFIED` result.

### 7. Remove duplicated methodology

Replace copied procedure detail with a mandate to load the owning skill.

Example:

```text
Too much:
  complete epic classification matrix, branch topology algorithm,
  evidence taxonomy, and all git steps copied into Project Instructions

Correct:
  Use delivery-work-breakdown for release-unit and topology decisions.
  Use git-workflow only after topology is resolved.
```

Keep project-specific constraints only when they genuinely govern that project.

### 8. Verify the generated artifact

Confirm:

```text
□ project identity and purpose are explicit
□ all URLs are supplied or clearly unresolved
□ source-of-truth priority is explicit
□ workflow-router and role-switcher are mandated
□ disclosure precedes substantive work
□ completion uses evidence and acceptance criteria
□ repository inspection precedes modification
□ capability-learning review is present
□ skill evolution is evidence-gated, not automatic
□ core versus skills versus runtime versus product ownership is preserved
□ no full skill methodology was copied unnecessarily
□ no repository state, issue, branch, or result was invented
```

## Quality Gates

The result is `PASS` only when:

- project-specific values are traceable to user input or verified sources;
- reusable policy and project-specific configuration remain separated;
- instructions are concise enough to function as a bootstrap;
- routing, role composition, execution disclosure, evidence, completion, and evolution are covered;
- missing information is explicit rather than guessed;
- the generated artifact can be reused by replacing primarily project identity and links.

Use `NEEDS_WORK` when the artifact is complete but bloated, duplicated, or ambiguous.

Use `BLOCKED` when required project identity or governing sources cannot be resolved.

## Completion Report

```text
PROJECT INSTRUCTION GENERATION
────────────────────────────────────
Project:
Runtime target:
Template version: 1.0.0
Resolved resources:
Unresolved placeholders:
Omitted optional sections:
Routing policy: PASS | NEEDS_WORK | BLOCKED
Disclosure policy: PASS | NEEDS_WORK | BLOCKED
Repository policy: PASS | NEEDS_WORK | BLOCKED
Evolution loop: PASS | NEEDS_WORK | BLOCKED
Duplication review: PASS | NEEDS_WORK
Final verdict: PASS | NEEDS_WORK | BLOCKED
```
