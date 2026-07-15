# Native AI Skills

Native AI Skills is the public runtime-adapter skill library for Native AI Core contracts.

```text
native-ai-core    = public core/domain/contracts/philosophy
native-ai-app     = app/product adapter that consumes core contracts
native-ai-skills  = runtime skill adapters that implement core skill contracts
```

This repo owns **how a runtime performs a skill**. It does not own product-specific context and it does not redefine the core contract.

## Current Adapters

```text
adapters/hermes/master-design/SKILL.md
adapters/hermes/master-engineer/SKILL.md
adapters/hermes/diagram-architect/SKILL.md
adapters/hermes/native-ai-engineer/SKILL.md
adapters/hermes/native-ai-runtime-ops/SKILL.md
adapters/hermes/native-ai-runtime-agent/SKILL.md
compat/master-design.compat.yaml
compat/master-engineer.compat.yaml
compat/diagram-architect.compat.yaml
compat/native-ai-engineer.compat.yaml
compat/native-ai-runtime-ops.compat.yaml
compat/native-ai-runtime-agent.compat.yaml
```

## Contract Relationship

Each adapter declares compatibility with a skill contract from `native-ai-core`:

```text
native-ai-core/contracts/skills/.../*.contract.yaml
  -> native-ai-skills/adapters/<runtime>/<skill>/SKILL.md
  -> app adapter runtime.binding.yaml
  -> installed runtime skill
```

## Installation Pattern

For Hermes, copy or sync the adapter directory into a Hermes profile skill directory, then list the installed skill in the app adapter runtime binding.

Example:

```text
~/.hermes/profiles/<profile>/skills/creative/master-design/SKILL.md
~/.hermes/profiles/<profile>/skills/creative/diagram-architect/SKILL.md
~/.hermes/profiles/<profile>/skills/software-development/master-engineer/SKILL.md
~/.hermes/profiles/<profile>/skills/software-development/native-ai-runtime-ops/SKILL.md
~/.hermes/profiles/<profile>/skills/software-development/native-ai-runtime-agent/SKILL.md
```

The app adapter should bind both contract and adapter source:

```yaml
skills:
  contracts:
    - id: master-engineer
      source: native-ai-core/contracts/skills/software-engineering/master-engineer.contract.yaml
  runtime_adapters:
    hermes:
      - id: master-engineer
        source: https://github.com/puterakahfi/native-ai-skills/adapters/hermes/master-engineer
        installed_as: master-engineer
```

## What Belongs Here

- Generic runtime skill implementations
- Compatibility manifests
- Runtime-specific install notes
- Generic examples with fake/non-private context

## What Does Not Belong Here

- Product-specific rules
- Private customer/product context
- Deployment secrets
- App-specific runtime bindings
- Core contract definitions
