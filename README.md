# ai-native-skills

Executable skills, workflows, and routers for AI-native engineering.

This repository turns engineering methods and Native AI contracts into reusable agent behavior. It is not a prompt collection: each capability should define its scope, procedure, quality gates, evidence requirements, and failure boundaries.

Works with agents that support the [Agent Skills specification](https://agentskills.io/specification) or the [skills.sh](https://skills.sh) ecosystem, including Hermes, Claude Code, Cursor, Codex, Gemini, Windsurf, and other compatible runtimes.

**87 skills · 10 workflows · 6 meta-skills**

## Start here

| Goal | Start with |
|---|---|
| Install one reusable capability | [Single skill](#install-one-skill) |
| Install a complete workflow and its documented dependencies | [Skill packs](docs/skill-packs.md) |
| Let the agent choose the correct workflow | `workflow-router` |
| Compose engineering, design, product, and review roles | `role-switcher` |
| Generate concise standardized Project Instructions | `project-instruction-generator` |
| Classify feature vs epic and define issue/branch/PR topology | `delivery-work-breakdown` |
| Discover repository frameworks, components, styling, icons, tooling, and reuse constraints before code | `implementation-context-discovery` |
| Diagnose discovery for a catalog, registry, directory, feed, or result set | `collection-discovery-design` |
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
- [`native-ai-fw`](https://github.com/puterakahfi/native-ai-fw) provides orchestration, discovery, adapters, context packs, and product-control behavior.
- Product repositories apply and validate the capabilities in real systems.

## Install

### Install one skill

```bash
npx skills add puterakahfi/ai-native-skills@<skill-name> -g -y
```

Examples:

```bash
npx skills add puterakahfi/ai-native-skills@workflow-router -g -y
npx skills add puterakahfi/ai-native-skills@project-instruction-generator -g -y
npx skills add puterakahfi/ai-native-skills@delivery-work-breakdown -g -y
npx skills add puterakahfi/ai-native-skills@implementation-context-discovery -g -y
npx skills add puterakahfi/ai-native-skills@decision-provenance -g -y
npx skills add puterakahfi/ai-native-skills@ai-system-design -g -y
npx skills add puterakahfi/ai-native-skills@chatgpt-app-development -g -y
npx skills add puterakahfi/ai-native-skills@collection-discovery-design -g -y
npx skills add puterakahfi/ai-native-skills@brand-identity-review -g -y
```

### Install a workflow pack

Workflows compose other capabilities. The Agent Skills specification does not currently provide native transitive dependency installation, so [`docs/skill-packs.md`](docs/skill-packs.md) provides verified bundle commands for redesign, product delivery, ChatGPT App product delivery, engineering quality, identity review, deployment, and other common flows.

### Install the full suite

```bash
npx skills add puterakahfi/ai-native-skills -g -y
```

## Capability model

`ai-native-skills` uses three official category values under `metadata["ai-native-skills.type"]`.

| Type | Primary job | Examples |
|---|---|---|
| `skill` | One reusable capability or expert lens | `delivery-work-breakdown`, `implementation-context-discovery`, `systematic-debugging`, `collection-discovery-design`, `decision-provenance`, `project-instruction-generator`, `chatgpt-app-development`, `brand-identity-review` |
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
| Build a ChatGPT App from zero | `product-development-workflow` + `chatgpt-app-development` |
| Add ChatGPT App integration to an existing product | `new-feature-workflow` + `chatgpt-app-development` |
| Generate or audit project-scoped agent instructions | `project-instruction-generator` |
| Decompose a release into epic/feature/task work and define branch/PR topology | `delivery-work-breakdown` |
| Map an accepted feature/design into an existing repository stack before implementation | `implementation-context-discovery` |
| Specify requirements before implementation | `spec-workflow` |
| Build a new capability in an existing product | `new-feature-workflow` |
| Investigate and fix a regression | `bugfix-workflow` |
| Review code before merge or release | `code-review-workflow` |
| Deploy, verify health, and confirm or roll back | `deployment-workflow` |
| Audit an existing design without changing it | `design-audit` |
| Fix known design findings while preserving direction and repository conventions | `design-refinement` |
| Replace design direction, structure, or multiple layers | `redesign-workflow` |
| Verify scope, approval, ownership, dependency, or override authority | `decision-provenance` |
| Audit and repair skill quality | `skill-doctor` |

Use [`workflow-router`](skills/workflow-router/SKILL.md) when the request has not yet been classified.

## How the system composes

```text
broad request
  → workflow-router selects the lifecycle and platform/domain overlays
  → role-switcher assigns one owner and narrow specialists
  → workflow runs ordered phases and gates
  → skills provide reusable domain behavior
  → facade and domain reviewers evaluate evidence
  → behavioral evals protect reusable learning
```

Examples:

```text
Repository-backed redesign or feature
  design/feature decision
  → implementation-context-discovery
      repository evidence
      canonicality and convention locks
      reuse / extend / compose / semantic-native / dependency decision
      implementation mapping
  → master-engineer implementation
  → architecture-review
  → design-review when user-facing

Design work
  workflow-router → design-audit | design-refinement | redesign-workflow
  role-switcher → design owner + specialists + design-review + domain reviewer
  collection-heavy surface → information-architecture → collection-discovery-design
  → design-interaction + adaptive-component-design

Engineering quality
  implementation-context-discovery when convention evidence is material
  → architecture-review → security-review → code-review-workflow → skill-eval

Product delivery
  product-development-workflow → spec-workflow → delivery-work-breakdown
  → new-feature-workflow
  → implementation-context-discovery → code-review-workflow
  → deployment-workflow → observability-design

ChatGPT App product delivery
  product-development-workflow | new-feature-workflow
  → delivery-work-breakdown for dependent P0 slices
  → chatgpt-app-development + native-ai-engineer
  → implementation-context-discovery for the product repository
  → architecture/security/design verification
  → deployment-workflow and actual ChatGPT integration evidence
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

Run behavioral regression cases:

```bash
bash scripts/run-eval.sh
```

Repository CI also validates:

- skill frontmatter and taxonomy;
- contract-backed adapter path/version conformance;
- structured boundary declarations;
- behavioral evaluation contracts;
- canonical design gate identity;
- machine-readable skill-pack manifests and documented commands;
- compatibility with the pinned `ai-native-core` runner.

## Related repositories

- [`ai-native-core`](https://github.com/puterakahfi/ai-native-core) — canonical domain, contracts, ports, and quality standards
- [`native-ai-fw`](https://github.com/puterakahfi/native-ai-fw) — orchestration and product runtime adapter
- [`skills.sh`](https://skills.sh) — compatible skill discovery and installation ecosystem
