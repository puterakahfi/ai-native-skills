# Contributing to ai-native-skills

Thank you for improving the executable capability layer of Native AI Engineering.

This repository is not a general prompt collection. Contributions should change agent behavior in a reusable, inspectable way through explicit scope, procedure, quality gates, evidence, and failure boundaries.

## Before you change anything

1. Identify the target issue and acceptance criteria.
2. Confirm that the change belongs in this repository.
3. Inspect the current implementation and preserve good existing work.
4. Check whether a canonical contract already exists in [`ai-native-core`](https://github.com/puterakahfi/ai-native-core).
5. Classify the artifact using [`docs/skills.md`](docs/skills.md): `skill`, `workflow`, or `meta-skill`.
6. Determine which tests, compatibility records, references, and documentation must change with it.

Repository boundaries:

```text
ai-native-core    canonical domain, contracts, boundaries, terminology, and quality standards
ai-native-skills  executable skills, workflows, references, rubrics, and behavioral evaluation
native-ai-fw      orchestration, discovery, adapters, context packs, and control-plane behavior
product repos     implementation and real-world validation
```

Update the correct repository instead of copying universal contracts into runtime or product-specific files.

## Contribution paths

### Add or refine a skill

Use `skills/<skill-name>/SKILL.md` for one reusable capability or expert lens.

A skill should define:

- when it applies;
- what it owns and does not own;
- the procedure or decision rules;
- quality gates and failure signals;
- checkable evidence before completion.

Keep the main `SKILL.md` as the executable entry point. Move deep methodology, matrices, examples, and checklists into `skills/<skill-name>/references/` when they are loaded conditionally.

### Add or refine a workflow

Use a workflow when ordered phases, gates, ownership, and handoffs are the main value. A workflow may compose many skills, but it owns the lifecycle rather than the specialist decisions.

When workflow dependencies change, also inspect:

- `metadata["ai-native-skills.requires"]`;
- [`docs/skill-packs.md`](docs/skill-packs.md);
- routing and role-composition behavior;
- affected behavioral cases.

### Add or refine a meta-skill

Use a meta-skill only when the artifact routes or composes other skills and workflows. It must make the routing decision and then hand execution to the selected capability.

Do not mix routing and domain execution in one artifact.

### Add a reference

Place supporting material under `skills/<skill-name>/references/` when it is part of that skill's executable method but does not need to load for every invocation.

The parent `SKILL.md` must state when the reference should be loaded. Do not create unreferenced documentation islands.

### Add a behavioral evaluation case

Regression contracts live under:

```text
contracts/tests/<skill-name>.test.yaml
```

A useful case contains:

- a realistic trigger;
- required and prohibited behavior;
- sequence constraints when order matters;
- the quality gates being exercised.

Prefer cases that prevent a known failure mode or preserve a verified reusable learning. Do not add cases that only restate the skill description.

### Implement a Native AI Core contract

A contract-compatible adapter remains an official `skill`, `workflow`, or `meta-skill` and declares the contract through namespaced metadata:

```yaml
metadata:
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/<category>/<contract>.contract.yaml
  ai-native-skills.contract-version: "^1.0.0"
```

When the universal capability contract, terminology, boundary, or quality standard changes, update `ai-native-core` first. Update this repository when executable agent behavior changes.

Use `compat/*.compat.yaml` when compatibility evidence is required. Do not present a missing or partial contract implementation as complete.

## Frontmatter rules

Every `SKILL.md` must use valid Agent Skills frontmatter.

```yaml
---
name: example-skill
description: Trigger-focused explanation of what the skill does and when to use it.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
---
```

Rules:

- the directory name and `name` must match;
- use lowercase kebab-case;
- keep repository-specific fields under namespaced `metadata` keys;
- do not invent a new official type without updating taxonomy, validation, examples, and downstream consumers;
- increase the skill version when executable behavior or its contract changes.

The canonical type and adapter rules live in [`docs/skills.md`](docs/skills.md).

## Validation

Validate the individual skill package:

```bash
skills-ref validate skills/<skill-name>
```

Run behavioral evaluation with a checked-out `ai-native-core` runner available at `ai-native-core/`:

```bash
python ai-native-core/scripts/run-eval.py \
  --skill <skill-name> \
  --output-dir eval-outputs
```

Changes to executable skills, contracts, compatibility records, or behavioral evals must pass the repository's **Skill and Gate Contracts** workflow. The workflow currently checks:

- local validator and runner syntax;
- the canonical design-gate registry;
- repository evaluation contracts;
- validation through the pinned `ai-native-core` runner;
- wrapper integration;
- per-case runner compatibility smoke.

Documentation-only changes may not trigger every executable-contract check. For those changes, inspect rendered Markdown, local links, commands, terminology, and source-of-truth references directly.

A green workflow is required when applicable, but it does not replace domain evidence. Visual, interaction, runtime, security, or architecture claims still require evidence appropriate to that domain.

## Documentation responsibilities

Update documentation whenever a change affects:

- the official type taxonomy or inventory counts;
- workflow entry points or skill packs;
- facade, adapter, or domain-reviewer patterns;
- installation instructions;
- repository boundaries or terminology;
- public examples and evaluation commands.

Keep [`docs/skills.md`](docs/skills.md) authoritative for taxonomy and the complete inventory. Keep [`docs/skill-packs.md`](docs/skill-packs.md) authoritative for workflow bundle installation.

## Pull request checklist

Before requesting review:

- [ ] The issue objective and acceptance criteria are satisfied.
- [ ] The change is in the correct repository and layer.
- [ ] Existing useful behavior is preserved unless the issue explicitly replaces it.
- [ ] Frontmatter, paths, links, and declared dependencies are valid.
- [ ] Required references are linked from the executable skill.
- [ ] Behavioral regressions are covered when reusable behavior changed.
- [ ] Local validation has been run where available.
- [ ] Applicable Skill and Gate Contracts checks are green.
- [ ] Documentation-only changes were reviewed for rendered structure and link integrity.
- [ ] Known gaps are reported as `PARTIAL`, `NOT_VERIFIED`, or `NOT_APPLICABLE` rather than hidden.
- [ ] No secrets, credentials, private product context, or generated runtime state were committed.

Use focused commits and a PR description that explains the objective, changed behavior, validation evidence, and known limitations.