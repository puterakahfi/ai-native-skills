# Skill Authoring Template

Use this guide with [`skill-package-standard.md`](skill-package-standard.md) and the `skill-authoring-workflow` lifecycle.

## Choose the correct lifecycle first

```text
Create, intentionally update, restructure, migrate, or deprecate
→ skill-authoring-workflow

Audit or repair unclear health problems
→ skill-doctor

Promote verified reusable learning
→ skill-evolution

Evaluate whether saved output applied a skill
→ skill-eval
```

Do not start writing files until the operation, target, issue, acceptance criteria, repository, branch base, and authority are resolved.

## Canonical package sources

```text
contracts/skill-package-policy.yaml
docs/skill-package-standard.md
scripts/validate-skill-packages.py
```

Do not duplicate the package policy inside a skill or workflow.

## Minimal `SKILL.md`

```yaml
---
name: example-skill
description: Use this skill when the user needs <specific intent>. Also use it when <implicit intent>. Do not use it for <near miss owned elsewhere>.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
---
```

The body must define:

1. applicability and exclusions;
2. ownership and handoffs;
3. required inputs and allowed outputs;
4. ordered procedure or decision rules;
5. quality gates;
6. evidence required before completion;
7. failure and limitation behavior;
8. exact conditions for loading references or invoking scripts;
9. repository side effects and approval boundaries when applicable.

## Description review

A description is acceptable only when reviewers can derive:

- explicit triggers;
- implicit triggers;
- at least one near miss;
- the capability boundary;
- wording suitable for catalog-only discovery.

Do not describe implementation internals while leaving user intent ambiguous.

## Runtime references

Place conditional execution knowledge in:

```text
skills/<name>/references/
```

Link it from `SKILL.md` with a loading condition, for example:

```text
Read `references/api-errors.md` when a non-2xx response must be classified.
```

Do not use vague instructions such as “see references for more information.” Skill-local `docs/` is discouraged for runtime knowledge.

## Behavioral regression contract

Create or update the centralized source:

```text
contracts/tests/<name>.test.yaml
```

A useful case includes a natural trigger, required behavior, prohibited behavior, sequence constraints when applicable, and quality gates tested.

Include positive behavior and realistic near-miss or forbidden behavior. Do not hint to the model that it must use the target skill. Do not create a package-local `evals/` duplicate.

## Executable resources

When a skill bundles reusable scripts, document inputs, outputs, dependencies, exit codes, side effects, idempotency, timeout/retry behavior, security assumptions, and evidence produced.

Add package-local `tests/` for applicable executable behavior. Keep generated results outside the skill directory.

## Operation-specific requirements

### CREATE

Create the smallest complete package, metadata, centralized behavioral contract, and applicable tests.

### UPDATE

Preserve accepted behavior, bump version for executable changes, and update target and related regression evidence.

### RESTRUCTURE

Prove behavior preservation. Structural validation alone is insufficient.

### MIGRATE

Record current compliance, target compliance, exemptions, warnings, and deferred debt. File presence alone does not prove compliance.

### DEPRECATE

Document replacement, dependency and catalog impact, migration path, compatibility expectations, and removal authority.

## Validation order

```bash
skills-ref validate skills/<skill-name>
python scripts/validate-skill-packages.py --skill <skill-name>
python scripts/validate-eval-contracts.py
AI_NATIVE_CORE_DIR=../ai-native-core bash scripts/run-eval.sh --skill <skill-name> --validate-tests
```

Also run applicable executable tests, related-skill contracts, adapter/core conformance, documentation/link checks, and live behavioral evaluation when real outputs exist.

## Pull request evidence

A skill change is not complete until applicable package validation, executable tests, behavioral-contract validation, related regressions, conformance, independent review, and acceptance are reported.

Report package, behavioral, executable-test, and conformance status independently. Missing evidence remains `NOT_VERIFIED`; structural CI does not prove live behavioral application.
