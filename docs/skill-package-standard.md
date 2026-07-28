# Skill Package, Documentation, Testing, and Evaluation Standard

Status: proposed repository standard for Epic #169.

## Purpose

This standard defines which files belong inside a skill package, which verification artifacts remain repository-level, and which generated evidence must stay outside authored sources.

It preserves the repository's existing canonical behavioral-evaluation architecture at `contracts/tests/` instead of duplicating equivalent cases under every skill.

## Canonical layout

```text
skills/<skill-name>/
├── SKILL.md                 # required executable entry point
├── references/             # optional runtime knowledge, loaded conditionally
├── scripts/                # optional bundled executable resources
├── tests/                  # conditional tests for bundled executable resources
├── assets/                 # optional templates, schemas, and static resources
└── adapter.conformance.yaml # conditional contract-adapter declaration

contracts/tests/<skill-name>.test.yaml
  canonical repository behavioral regression contract

.tmp/ or external artifact storage
  generated eval output, reports, inventories, and temporary state
```

## Directory policy

| Path | Policy | Responsibility |
|---|---|---|
| `SKILL.md` | Required | Discovery metadata, executable procedure, gates, evidence, failures, and handoffs. |
| `references/` | Optional and recommended for deep guidance | Runtime knowledge loaded only when the current phase or concern requires it. |
| `scripts/` | Optional | Reusable deterministic behavior bundled with the skill. |
| `tests/` | Conditional | Automated tests for skill-local scripts, parsers, validators, generators, or mutations. |
| `assets/` | Optional | Templates, schemas, fixtures intended as runtime inputs, and static resources. |
| `adapter.conformance.yaml` | Conditional | Structured implementation evidence for a Native AI Core contract. |
| `docs/` inside a skill | Discouraged | Use `references/` for runtime knowledge and repository `docs/` for maintainer guidance. |
| `evals/` inside a skill | Optional compatibility surface, not canonical here | Do not duplicate cases already owned by `contracts/tests/`. |
| `workspace/`, `results/`, `outputs/`, `.tmp/` | Prohibited as authored skill content | Generated state belongs outside the skill package. |
| dependency directories | Prohibited | Do not commit `.venv/`, `node_modules/`, `dist/`, caches, or downloaded dependencies. |

## Why behavioral evals remain centralized

This repository already has a canonical evaluator, core-runner integration, version matching, schema validation, smoke fixtures, and CI enforcement around:

```text
contracts/tests/<skill-name>.test.yaml
```

Moving or copying those cases into `skills/<name>/evals/` would create two authorities for:

- skill version alignment;
- trigger wording;
- required and prohibited behavior;
- gate coverage;
- evaluation runner discovery;
- regression maintenance.

Therefore:

1. repository behavioral cases remain in `contracts/tests/`;
2. package-local `evals/` is not required;
3. an external interoperability adapter may project centralized cases into another runtime format, but generated projections must not become a second authored source of truth;
4. missing behavioral evidence is `NOT_VERIFIED`, never automatic `PASS`.

## Substantive skills

A skill is substantive when one or more of these apply:

- it changes or produces engineering, product, design, security, or delivery artifacts;
- it routes or composes other capabilities;
- it runs tools or mutations;
- it owns a quality gate, review verdict, acceptance decision, or compliance claim;
- it is required by a workflow;
- a behavioral regression could materially change delivery outcomes.

Substantive skills require a canonical behavioral contract unless an explicit, reviewed exemption exists.

## Executable-resource testing

A skill-local `tests/` directory is required when `scripts/` contains non-trivial reusable behavior, including:

- parsers or schema validators;
- generators or graders;
- file or repository mutations;
- gate-producing commands;
- behavior with dependencies, retries, timeouts, or security boundaries.

Tests must cover applicable success, malformed input, missing input, failure, and isolated side-effect behavior. Test fixtures are verification sources and must not be loaded as runtime knowledge by default.

Tiny declarative wrappers may be exempted only when the reason is explicit and the executable behavior is already tested through a higher-authority repository runner.

## Documentation boundaries

Use `references/` when the agent may need the material during execution. The parent `SKILL.md` must say when to load each reference.

Use repository-level `docs/` for:

- contributor and maintainer guidance;
- taxonomy and architecture decisions;
- migration procedures;
- CI and release documentation;
- standards shared by multiple skills.

Do not create unreferenced documentation islands.

## Progressive disclosure

`SKILL.md` must remain the lean executable entry point. Deep matrices, examples, domain methods, and checklists belong in references.

Repository validation should report:

- ambiguous or missing reference-loading conditions;
- unreachable references;
- nested reference chains that obscure execution;
- excessive entry-point size where configured.

Size budgets are quality signals, not permission to remove necessary safety, evidence, or failure boundaries.

## Generated evidence

Generated outputs must be stored outside authored skill directories, for example:

```text
.tmp/skill-package-validation/
.tmp/eval-reports/
eval-outputs/
CI artifact storage
```

Generated evidence must identify the skill, case, repository revision, tool/runtime version when observable, verdict, failures, and raw-output location.

## Enforcement phases

### Phase 1: pilot blocking

The validator blocks structural and behavioral-contract failures for:

- `test-driven-development`;
- `workflow-router`;
- `skill-evolution`.

Repository-wide findings are inventoried without silently claiming compliance.

### Phase 2: changed-skill enforcement

New or materially changed substantive skills must satisfy the standard before merge.

### Phase 3: repository migration

Existing skills are migrated by verified risk and dependency priority. Grandfathering is not compliance; unresolved evidence remains `PARTIALLY_COMPLIANT`, `NEEDS_MIGRATION`, `BLOCKED`, or `NOT_VERIFIED`.

## Completion rules

A skill package is not complete merely because `SKILL.md` exists or CI syntax passes. Completion requires applicable structural validation, executable tests, behavioral evidence, domain evidence, review, and acceptance.

Allowed non-pass verdicts are:

```text
NEEDS_WORK
PARTIALLY_COMPLETED
BLOCKED
NOT_VERIFIED
LIMITED
HANDED_OFF
```
