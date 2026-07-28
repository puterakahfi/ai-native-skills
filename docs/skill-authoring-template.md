# Skill Authoring Template

Use this guide together with [`skill-package-standard.md`](skill-package-standard.md).

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
8. exact conditions for loading each reference or invoking each script.

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

Do not use vague instructions such as “see references for more information.”

## Behavioral regression contract

Create or update:

```text
contracts/tests/<name>.test.yaml
```

A useful case includes a natural trigger, required behavior, prohibited behavior, sequence constraints when applicable, and quality gates tested.

Include positive behavior and realistic near-miss or forbidden behavior. Do not hint to the model that it must use the target skill.

## Executable resources

When a skill bundles reusable scripts, document inputs, outputs, dependencies, exit codes, side effects, idempotency, timeout/retry behavior, security assumptions, and evidence produced.

Add package-local `tests/` for non-trivial executable behavior. Keep generated results outside the skill directory.

## Pull request evidence

A skill change is not complete until applicable package validation, executable tests, behavioral-contract validation, domain evidence, independent review, and acceptance are reported. Missing evidence remains `NOT_VERIFIED`.
