# Redesign Workflow Dependencies and Installation

> Runtime dependency awareness and package installation are separate concerns.

## Current upstream limitation

The Agent Skills format allows repository-specific metadata, but the upstream `skills` CLI does not currently resolve and install transitive dependencies from `SKILL.md`.

Therefore:

```text
npx skills add puterakahfi/ai-native-skills@redesign-workflow -g -y
```

installs the workflow entrypoint only. It does not guarantee that its owners, ports, adapters, reviewers, correction loop, learning, or repository capabilities are present.

## Canonical source

The canonical installation and dependency model is:

```text
packs/redesign/pack.yaml
```

It owns:

```text
- ordered local dependency inventory
- required, conditional, port, adapter, domain-reviewer, and optional classification
- conditions for contextual capabilities
- compatibility projection for ai-native-skills.requires
- minimum and complete installation profiles
- documentation binding for the public install command
```

`metadata["ai-native-skills.requires"]` remains a backward-compatible runtime hint. It is not the package manifest and must not be interpreted as proof that dependencies were installed.

## Dependency classes

```text
required
  lifecycle capability needed for a normal redesign run

conditional
  capability required only under a declared execution condition
  example: master-engineer for patch production

port
  stable concern-level routing capability
  example: design-visual or design-layout

adapter
  narrow specialist selected from changed layers and acceptance criteria
  example: design-color, responsiveness, or copywriting

domain-reviewer
  acceptance capability selected by the primary design domain
  example: brand-identity-review

optional
  useful capability outside the workflow's direct execution contract
  example: workflow-router before entrypoint selection
```

Do not promote every contextual adapter into a universal hard dependency. Installation may provide the complete pack while runtime composition still loads only the capabilities relevant to the task.

## Installation profiles

### Complete

Use the complete profile for a ready-to-run general redesign environment. The generated command is documented in `docs/skill-packs.md` and validated against the manifest.

```text
python scripts/validate-skill-packs.py \
  --pack redesign \
  --profile complete \
  --print-install-command
```

### Minimum

The minimum profile installs the workflow, required lifecycle capabilities, and concern ports. Contextual adapters must already be installed or added separately before a task that needs them.

The minimum profile is useful for controlled runtimes with their own capability resolver. It is not the recommended manual install path for general users.

## Runtime preflight

Before claiming redesign capability is ready:

```text
1. resolve the selected installation profile
2. verify each required local skill is available
3. inspect output mode and load conditional capabilities
4. resolve changed concerns through ports
5. select only applicable adapters and domain reviewers
6. report missing capabilities as a blocker or explicit limited mode
```

Never claim a complete redesign environment from the presence of `redesign-workflow` alone.

## Validation

Run:

```text
python scripts/validate-skill-packs.py
python -m unittest tests/test_validate_skill_packs.py
```

Validation fails when:

```text
- a referenced local skill is missing
- a dependency is duplicated
- a classification is invalid
- a conditional dependency has no condition
- an adapter references an unknown port
- a domain reviewer has no declared domain
- a pack dependency is unknown or cyclic
- workflow metadata drifts from the compatibility projection
- documented install order or membership drifts from the selected profile
```
