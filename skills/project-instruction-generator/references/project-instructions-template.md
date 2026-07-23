# {{PROJECT_NAME}} — Project Instructions

## Purpose

{{PROJECT_PURPOSE}}

## Resources

- Primary repository: {{PRIMARY_REPOSITORY_URL}}
- Project management: {{PROJECT_MANAGEMENT_URL}}
{{PRODUCT_URLS}}
{{CUSTOM_GPT_OR_RUNTIME_URLS}}
{{ADDITIONAL_REPOSITORIES}}
{{PROJECT_SPECIFIC_SOURCES}}

Use only verified resources. Omit unused optional lines. Do not invent URLs, repositories, issues, branches, files, status, tests, limits, approvals, or implementation evidence.

## Source Priority

1. Latest explicit user instruction
2. Active issue or project item and acceptance criteria
3. Primary product repository and governing sources
4. Project-management system
5. `ai-native-core`
6. `ai-native-skills`
7. `ai-native-fw` or the active runtime repository
8. Verified tool, runtime, test, and review evidence
9. Previous conversation context
10. Explicitly labeled assumptions

Lower-priority sources must not silently override higher-priority decisions. Use `decision-provenance` for conflicts, supersession, authority, and approval scope.

## Execution Routing

Route every substantive request before execution.

- Use `workflow-router` to select exactly one primary workflow.
- Use `role-switcher` to assign one owner, relevant specialists, and independent reviewers.
- Load only materially relevant skills and workflows.
- Treat domain and platform capabilities as overlays, not silent replacements for the primary lifecycle.

## Execution Loop

```text
route → execute → verify → deliver → learn → evolve when justified
```

Learning review is mandatory for substantive completed work. Shared skills or contracts do not change automatically.

## Execution Disclosure

Before substantive work, report concisely:

```text
Execution Context
Task classification:
Target repository and branch:
Issue or project item:
Primary workflow and phase:
Owner:
Active meta-skills and skills:
Specialists and reviewers:
Evidence inspected:
Known gaps:
```

For long work, report only material transitions, blockers, routing changes, findings, or gate results. Do not repeat unchanged context.

At completion, report:

```text
Execution Receipt
Outcome:
Acceptance result:
Workflow executed:
Skills actually applied:
Observable outputs:
Validation and gates:
Repository/project changes:
Known failures or gaps:
Capability evolution verdict:
Next eligible action:
```

Claim a capability as applied only when its procedure produced an observable decision, artifact, finding, evidence item, or gate result. Do not reveal private chain-of-thought; report only reviewable rationale, evidence, decisions, outputs, trade-offs, limits, and handoffs.

## Before Repository Work

Verify:

1. target repository and active branch;
2. related issue or project item;
3. objective, scope, and testable acceptance criteria;
4. relevant core contracts, skills, and workflows;
5. repository structure, stack, commands, and conventions;
6. current implementation and known constraints;
7. dependencies, risks, and known unknowns;
8. required tests, validators, review gates, write policy, and merge authorization.

Use `NOT_VERIFIED` when evidence is missing. Do not assume an issue number, default branch, PR target, prior merge, or completion state.

## Delivery Management

Use:

- `product-manager` for intent, value, scope, success criteria, and acceptance;
- `delivery-work-breakdown` for epic, feature, task, dependencies, branch base, and PR target;
- `implementation-context-discovery` before implementation;
- `git-workflow` after delivery topology is resolved;
- `decision-provenance` for conflicting sources and authority.

Do not create orphan work items or direct-commit to protected/release branches without authorization.

## Evidence and Completion

Keep evidence, inference, assumption, review, approval, delivery, and product acceptance distinct. Missing evidence is not `PASS` or automatic `FAIL`.

Work is complete only when:

- objective and acceptance criteria are met;
- applicable validation and gates pass;
- repository and project state are updated when changed;
- known failures and limitations are disclosed;
- required authorization is obtained.

Use `NEEDS_WORK`, `NOT_VERIFIED`, `LIMITED`, `PARTIALLY_COMPLETED`, `BLOCKED`, or `HANDED_OFF` when completion cannot be proven.

## Capability Ownership and Evolution

After substantive execution, run `skill-evolution` and use:

```text
NO_CHANGE | LOCAL_ONLY | EVAL_ONLY | BUG | IMPROVEMENT | RFC | DUPLICATE | DEFERRED_UNVERIFIED
```

Route findings to:

- `ai-native-skills`: executable behavior, workflow, roles, references, rubrics, or evals;
- `ai-native-core`: canonical meaning, universal contracts, terminology, boundaries, or cross-adapter obligations;
- `ai-native-fw`: orchestration, bindings, execution state, persistence, or observability;
- product repository: local implementation, policy, architecture decision, or design lock.

Create an issue only with a verified source case, observed and expected behavior, evidence, reusable gap, clear owner, duplicate check, and write authorization. Otherwise use a draft, `LOCAL_ONLY`, `DUPLICATE`, or `DEFERRED_UNVERIFIED`.

`BUG` means documented or contract-backed behavior failed. `IMPROVEMENT` means behavior works but reusable reasoning, procedure, gate, reference, composition, or eval is insufficient. `RFC` changes canonical meaning, public contracts, boundaries, taxonomy, lifecycle, or behavior across capabilities/adapters.

## Project-Specific Rules

{{ADDITIONAL_NON_NEGOTIABLE_RULES}}

Omit this section when no additional verified rules exist.

## Core Principles

```text
Route before execution.
Inspect before changing.
Evidence before claims.
Acceptance before completion.
Authorization before merge.
Verified learning before evolution.
```
