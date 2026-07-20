# ai-native-skills

Executable skills, workflows, and routers for AI-native engineering.

This repository turns engineering methods and Native AI contracts into reusable agent behavior. It is not a prompt collection: each capability should define its scope, procedure, quality gates, evidence requirements, and failure boundaries.

Works with agents that support the [Agent Skills specification](https://agentskills.io/specification) or the [skills.sh](https://skills.sh) ecosystem, including Hermes, Claude Code, Cursor, Codex, Gemini, Windsurf, and other compatible runtimes.

**81 skills · 9 workflows · 6 meta-skills**

## Start here

| Goal | Start with |
|---|---|
| Install one reusable capability | [Single skill](#install-one-skill) |
| Install a complete workflow and its documented dependencies | [Skill packs](docs/skill-packs.md) |
| Let the agent choose the correct workflow | `workflow-router` |
| Compose engineering, design, product, and review roles | `role-switcher` |
| Bootstrap an AI-native Hermes profile | [`hermes-profile-bootstrap`](#hermes-profile-bootstrap) |
| Browse the complete capability taxonomy | [docs/skills.md](docs/skills.md) |
| Contribute a skill, workflow, reference, or eval case | [CONTRIBUTING.md](CONTRIBUTING.md) |

## Where this repository fits

```text
ai-native-core
  canonical domain, contracts, boundaries, terminology, and quality standards
        ↓ implemented as executable behavior
ai-native-skills
  skills, workflows, meta-skills, references, rubrics, and behavioral evaluation
        ↓ installed directly or orchestrated through adapters
agents, native-ai-fw, and product repositories
  runtime execution, control-plane behavior, product implementation, and validation
```

- [`ai-native-core`](https://github.com/puterakahfi/ai-native-core) defines the public, runtime-agnostic contracts.
- `ai-native-skills` implements reusable capabilities that agents can load and execute.
- [`native-ai-fw`](https://github.com/puterakahfi/ai-native-fw) provides orchestration, discovery, adapters, context packs, and product-control behavior.
- Product repositories apply and validate the capabilities in real systems.

## Install

### Install one skill

```bash
npx skills add puterakahfi/ai-native-skills@<skill-name> -g -y
```

Examples:

```bash
npx skills add puterakahfi/ai-native-skills@workflow-router -g -y
npx skills add puterakahfi/ai-native-skills@decision-provenance -g -y
npx skills add puterakahfi/ai-native-skills@ai-system-design -g -y
npx skills add puterakahfi/ai-native-skills@brand-identity-review -g -y
```

### Install a workflow pack

Workflows compose other capabilities. The Agent Skills specification does not currently provide native transitive dependency installation, so [`docs/skill-packs.md`](docs/skill-packs.md) provides verified bundle commands for redesign, product delivery, engineering quality, identity review, deployment, and other common flows.

### Install the full suite

```bash
npx skills add puterakahfi/ai-native-skills -g -y
```

## Capability model

`ai-native-skills` uses three official category values under `metadata["ai-native-skills.type"]`.

| Type | Primary job | Examples |
|---|---|---|
| `skill` | One reusable capability or expert lens | `systematic-debugging`, `decision-provenance`, `brand-identity-review` |
| `workflow` | An ordered lifecycle with phases and gates | `bugfix-workflow`, `redesign-workflow`, `deployment-workflow` |
| `meta-skill` | Route or compose other capabilities | `workflow-router`, `role-switcher` |

`facade`, `domain-reviewer`, and adapter are patterns rather than additional official types. Contract-backed implementations remain a `skill`, `workflow`, or `meta-skill` and declare their relationship through namespaced metadata.

The canonical definitions, decision rules, frontmatter contract, and complete inventory live in [`docs/skills.md`](docs/skills.md).

## Repository map

```text
skills/<name>/SKILL.md
  executable entry point for one skill, workflow, or meta-skill

skills/<name>/references/
  deep methodology, matrices, examples, checklists, and conditional guidance

contracts/tests/<name>.test.yaml
  behavioral regression cases and quality-gate expectations

compat/*.compat.yaml
  compatibility evidence for contract-backed adapters when required

docs/
  canonical taxonomy, architecture patterns, skill packs, and repository guidance
```

A `SKILL.md` should remain the lean executable entry point. Load references only when the current phase or concern requires them.

## Common workflow entry points

| User intent | Start with |
|---|---|
| Build a product from discovery through launch | `product-development-workflow` |
| Specify requirements before implementation | `spec-workflow` |
| Build a new capability in an existing product | `new-feature-workflow` |
| Investigate and fix a regression | `bugfix-workflow` |
| Review code before merge or release | `code-review-workflow` |
| Deploy, verify health, and confirm or roll back | `deployment-workflow` |
| Audit an existing design without changing it | `design-audit` |
| Fix known design findings while preserving direction | `design-refinement` |
| Replace design direction, structure, or multiple layers | `redesign-workflow` |
| Verify scope, approval, ownership, or override authority | `decision-provenance` |
| Audit and repair skill quality | `skill-doctor` |

Use [`workflow-router`](skills/workflow-router/SKILL.md) when the request has not yet been classified.

## How the system composes

```text
broad request
  → workflow-router selects the lifecycle
  → role-switcher assigns one owner and narrow specialists
  → workflow runs ordered phases and gates
  → skills provide reusable domain behavior
  → facade and domain reviewers evaluate evidence
  → behavioral evals protect reusable learning
```

Examples:

```text
Design work
  workflow-router → design-audit | design-refinement | redesign-workflow
  role-switcher → design owner + specialists + design-review + domain reviewer

Engineering quality
  architecture-review → security-review → code-review-workflow → skill-eval

Product delivery
  product-development-workflow → spec-workflow → new-feature-workflow
  → code-review-workflow → deployment-workflow → observability-design
```

## Hermes Profile Bootstrap

Use `hermes-profile-bootstrap` when Hermes is already installed and you want a reusable AI-native engineering profile skeleton.

Install the bootstrap skill:

```bash
npx --yes skills add puterakahfi/ai-native-skills \
  --skill hermes-profile-bootstrap \
  --agent hermes-agent \
  --global \
  --yes
```

Then run it through Hermes:

```bash
hermes chat -s hermes-profile-bootstrap -q \
  "Bootstrap the ai-native-engineering profile using the engineering preset. Create the complete skeleton and verify that required skills, workflows, and meta-skills exist."
```

The bootstrap checks the reusable profile structure, required meta-skills and workflows, Native AI foundations, metadata classification, and secret-free output. It implements the runtime-agnostic profile-bootstrap contract from [`ai-native-core`](https://github.com/puterakahfi/ai-native-core).

## Evaluation and quality gates

Validate one skill package with the Agent Skills reference validator:

```bash
skills-ref validate skills/<skill-name>
```

Behavioral cases live under `contracts/tests/<skill-name>.test.yaml` and can be run through a checked-out `ai-native-core` runner:

```bash
python ai-native-core/scripts/run-eval.py \
  --skill <skill-name> \
  --output-dir eval-outputs
```

Executable capability and contract changes are validated by the **Skill and Gate Contracts** workflow. It verifies validator and runner syntax, canonical gate identity, repository eval contracts, the pinned core runner, wrapper integration, and per-case compatibility smoke.

A green workflow is necessary for affected paths but not sufficient by itself. Visual, runtime, interaction, security, architecture, and product claims still require evidence appropriate to their domain.

## Contributing

Read [`CONTRIBUTING.md`](CONTRIBUTING.md) before adding or refining a capability.

The guide covers:

- repository and contract boundaries;
- skill, workflow, and meta-skill authoring;
- references and behavioral eval cases;
- contract-compatible adapter metadata;
- validation commands and quality gates;
- documentation and pull-request responsibilities.

## Canonical documentation

- [Skills taxonomy and complete inventory](docs/skills.md)
- [Skill packs](docs/skill-packs.md)
- [Facade skill pattern](docs/facade-skill-pattern.md)
- [AI-native engineering building blocks](docs/ai-native-engineering-building-blocks.md)
- [Contributing](CONTRIBUTING.md)

## Related repositories

- [`ai-native-core`](https://github.com/puterakahfi/ai-native-core) — canonical domain, contracts, ports, and quality standards
- [`native-ai-fw`](https://github.com/puterakahfi/ai-native-fw) — orchestration and product runtime adapter
- [`skills.sh`](https://skills.sh) — compatible skill discovery and installation ecosystem
