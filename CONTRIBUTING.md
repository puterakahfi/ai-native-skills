# Contributing to ai-native-skills

Thank you for improving the executable capability layer of Native AI Engineering.

This repository is not a prompt collection. Contributions must change agent behavior in a reusable, inspectable way through explicit scope, procedure, quality gates, evidence, and failure boundaries.

## Before changing anything

1. Identify the target issue and testable acceptance criteria.
2. Confirm repository ownership and inspect current implementation.
3. Check whether `ai-native-core` already owns the universal contract.
4. Resolve the skill operation and governing lifecycle.
5. Verify branch base, PR target, write policy, and merge authority.
6. Determine affected package rules, tests, behavioral contracts, conformance, docs, and related capabilities.

Repository boundaries:

```text
ai-native-core    canonical domain, contracts, boundaries, terminology, quality standards
ai-native-skills  executable skills, workflows, references, rubrics, behavioral evaluation
native-ai-fw      orchestration, discovery, adapters, context packs, control-plane behavior
product repos     implementation and real-world validation
```

## Skill lifecycle entry points

```text
CREATE | UPDATE | RESTRUCTURE | MIGRATE | DEPRECATE
→ skill-authoring-workflow

Audit, diagnose, or repair unclear skill health
→ skill-doctor

Promote verified reusable learning from a real case
→ skill-evolution

Evaluate whether a saved output applied a skill
→ skill-eval
```

Do not route from the artifact noun alone. “Improve this skill” is ambiguous until intentional authoring, health repair, verified learning, or behavioral evaluation is resolved.

## Canonical package policy

Use:

```text
contracts/skill-package-policy.yaml
docs/skill-package-standard.md
docs/skill-authoring-template.md
scripts/validate-skill-packages.py
```

Package direction:

```text
skills/<name>/SKILL.md              required
skills/<name>/references/           optional runtime knowledge
skills/<name>/scripts/              optional executable resources
skills/<name>/tests/                conditional for bundled scripts
skills/<name>/assets/               optional static resources
skills/<name>/adapter.conformance.yaml optional contract declaration
contracts/tests/<name>.test.yaml    centralized behavioral regression contract
```

Do not create package-local behavioral `evals/` duplicates. Keep generated state outside authored packages. Use explicit exemptions rather than silent violations.

## Capability types

- `skill`: one reusable capability or expert lens;
- `workflow`: ordered phases, gates, ownership, and handoffs;
- `meta-skill`: routes or composes other capabilities.

A workflow owns lifecycle; specialists own domain decisions. Do not mix routing and domain execution in one artifact.

## Authoring requirements

A capability should define:

- when it applies and near misses;
- what it owns and delegates;
- required inputs and allowed outputs;
- ordered procedure or decision rules;
- quality gates and failure signals;
- checkable evidence before completion;
- resource loading conditions;
- repository side effects and approval boundaries.

Keep `SKILL.md` as the lean executable entry point. Move conditional depth into linked `references/`.

## Frontmatter

```yaml
---
name: example-skill
description: Trigger-focused explanation of what the capability does, when to use it, and an important near miss.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
---
```

Rules:

- directory and `name` match;
- use lowercase kebab-case;
- keep repository fields namespaced under `metadata`;
- do not invent a type without updating taxonomy and downstream validation;
- bump version when executable behavior or contract changes.

## Behavioral regression contracts

Store cases at:

```text
contracts/tests/<skill-name>.test.yaml
```

A useful case has a natural trigger, required and prohibited behavior, sequence constraints when needed, and quality gates tested. Assertions must be grounded by the trigger or attributable context.

A green contract validation proves structure and runner compatibility, not live behavioral application. Real per-case outputs are required for `APPLIED`, `PARTIAL`, or `GHOST` evidence.

## Executable resources

Reusable scripts must document inputs, outputs, dependencies, exit codes, error handling, side effects, idempotency, timeout/retry behavior, security assumptions, and evidence produced.

Add package-local `tests/` when required by policy. Use isolated fixtures or dry-run behavior for mutations.

## Validation

Run applicable checks:

```bash
skills-ref validate skills/<skill-name>
python scripts/validate-skill-packages.py --skill <skill-name>
python scripts/validate-eval-contracts.py
AI_NATIVE_CORE_DIR=../ai-native-core bash scripts/run-eval.sh --skill <skill-name> --validate-tests
```

For core-backed adapters also run the pinned conformance validators. Run executable tests, affected related-skill regressions, documentation/link checks, and domain-specific evidence.

A zero exit code from a structural validator does not replace behavioral, runtime, visual, security, architecture, approval, or product evidence.

## Documentation responsibilities

Update authoritative documentation whenever changes affect taxonomy, inventory counts, workflow entry points, skill packs, package policy, adapter patterns, installation instructions, repository boundaries, or public validation commands.

Runtime methodology belongs in skill `references/`. Repository maintainer guidance belongs in root `docs/`.

## Pull request checklist

- [ ] Issue, objective, scope, and acceptance criteria are verified.
- [ ] Correct lifecycle and repository layer are selected.
- [ ] Useful existing behavior is preserved unless replacement is accepted.
- [ ] Package policy and frontmatter pass validation.
- [ ] References, dependencies, links, and catalog entries are valid.
- [ ] Bundled executable behavior has applicable tests.
- [ ] Centralized behavioral contract is updated when behavior changes.
- [ ] Target and affected related regressions are checked.
- [ ] Core conformance is checked when applicable.
- [ ] Package, behavioral, executable-test, and conformance evidence are reported independently.
- [ ] Known gaps use `PARTIAL`, `NOT_VERIFIED`, or `NOT_APPLICABLE` rather than hidden PASS.
- [ ] No secrets, private product context, dependency directories, or generated runtime state are committed.
- [ ] Review, approval, and merge authority remain explicit.
