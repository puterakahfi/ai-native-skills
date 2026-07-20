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
- manifest schema and pack version
- ordered local or explicitly pinned external dependency inventory
- required, conditional, port, adapter, domain-reviewer, and optional classification
- conditions for contextual capabilities
- exact compatibility projection for ai-native-skills.requires
- minimum and complete installation profiles
- exact documentation binding for the public install command
```

The workflow binds the manifest with:

```text
ai-native-skills.pack
ai-native-skills.pack-version
```

`metadata["ai-native-skills.requires"]` remains a backward-compatible runtime hint. It is not the package manifest and must not be interpreted as proof that dependencies were installed. Its order and membership are generated from the manifest compatibility projection and validated exactly.

## Dependency classes

```text
required
  universal lifecycle capability needed for a normal redesign run

conditional
  capability required only under a declared execution condition
  examples: master-engineer for patch production,
            design-brand when brand locks are in scope,
            git-workflow for repository-backed delivery

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

Do not promote every contextual capability into a universal hard dependency. Installation may provide the complete pack while runtime composition still loads only the capabilities relevant to the task.

## Installation profiles

### Complete

Use the complete profile for a ready-to-run general redesign environment. The generated command is documented in `docs/skill-packs.md` and validated byte-for-byte after surrounding whitespace normalization.

```text
python scripts/validate-skill-packs.py \
  --pack redesign \
  --profile complete \
  --print-install-command
```

### Minimum

The minimum profile installs the workflow, universal lifecycle capabilities, and concern ports. Conditional capabilities and adapters must already be installed or added separately before a task that needs them.

The minimum profile is useful for controlled runtimes with their own capability resolver. It is not the recommended manual install path for general users.

## Runtime preflight

Before claiming redesign capability is ready:

```text
1. resolve the selected installation profile
2. verify each universal required skill is available
3. inspect output mode, domain, brand locks, evidence needs, and delivery boundary
4. load conditional capabilities whose activation conditions are true
5. resolve changed concerns through ports
6. select only applicable adapters and domain reviewers
7. report missing capabilities as a blocker or explicit limited mode
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
- the manifest schema version is unsupported
- a pack, profile, skill, concern, port, or domain identifier is invalid
- the repository coordinate is invalid
- a referenced local skill is missing or has a mismatched name
- an external dependency lacks an explicit repository and ref
- a dependency is duplicated
- a classification is invalid
- a conditional dependency or domain reviewer has no activation condition
- an adapter references an unknown port
- a domain reviewer has no declared domain
- a pack dependency is unknown or cyclic
- workflow manifest path or pack-version metadata drifts
- ai-native-skills.requires membership, order, or uniqueness drifts
- the documented repository, skills, order, flags, or full command drifts
```
