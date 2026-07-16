---
name: hermes-profile-bootstrap
description: Bootstrap the Hermes adapter for the Native AI profile-bootstrap contract. Use when creating, generating, templating, or auditing a Hermes profile that should start with AI-native meta-skills, workflows, foundation skills, runtime skills, and verification policy.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/runtime-profile/profile-bootstrap.contract.yaml
---

# Hermes Profile Bootstrap

## Overview

Use this skill to create or audit the **Hermes adapter implementation** of the Native AI `profile-bootstrap` contract.

The core contract lives in `native-ai-core/contracts/skills/runtime-profile/profile-bootstrap.contract.yaml`. This skill owns the Hermes-specific profile skeleton, commands, paths, install steps, and verification behavior. The profile is a **runtime skeleton**, not a product.

Target command shape:

```bash
hermes-generate profile <profile-name> --preset engineering
```

Until that command exists, use this skill as the canonical Hermes adapter blueprint for manual generation or for implementing the generator.

## When to Use

Use when the user asks to:

- create, generate, bootstrap, install, or audit a Hermes profile based on `ai-native-engineering`
- implement the Hermes adapter for the core `profile-bootstrap` contract
- define the minimum required skills for an AI-native Hermes runtime
- design `hermes-generate profile <name>` or an equivalent profile template command
- create a reusable Hermes profile distribution for Native AI work
- decide which meta-skills, workflows, and foundation skills must ship in a new profile

Do not use for:

- ordinary Hermes setup unrelated to Native AI profile distribution
- product-specific rules that belong in `products/<product-id>/` or a project repo
- live session sync, `state.db`, credentials, memories, or gateway secrets
- replacing Hermes Desktop/CLI/Gateway with a separate dashboard

## Contract Placement

The runtime-agnostic contract belongs in `native-ai-core`. This skill belongs in `ai-native-skills` because it is executable Hermes adapter guidance. If a rule applies to every runtime, move it to the core contract; if it mentions Hermes paths or commands, keep it here.

## Layer Boundary

Keep this split clean:

```text
Hermes profile skeleton = runtime identity, config defaults, installed skills, scripts, docs
ai-native-skills        = portable executable skill source
native-ai-core          = runtime-agnostic profile-bootstrap contract and workflow definitions
native-ai-fw/app        = product/runtime binding and product source-of-truth registry
product instance        = VisualMate or another product's rules, specs, context, and docs
```

A generated profile may reference product projects, but it must not bake product facts into the reusable skeleton.

## Presets

Choose the smallest preset that satisfies the intended runtime.

| Preset | Use when | Includes |
|---|---|---|
| `minimal` | Profile should only route work and understand Native AI boundaries | meta-skills, core workflows, Native AI runtime skills, context/rule skills |
| `engineering` | Default for coding/product engineering | `minimal` + engineering quality + architecture foundation |
| `product` | Profile will design/build product UX and landing/app surfaces | `engineering` + design/product/CRO pack |
| `runtime-ops` | Profile will operate a canonical remote Hermes runtime | `minimal` + runtime ops, deployment, observability, incident skills |
| `full` | Profile should be a complete AI-native engineering workstation | all packs below |

Default to `engineering` unless the user names a narrower or broader preset.

## Required Skill Packs

### Meta-skills

Install in every preset:

```text
workflow-router
role-switcher
```

Purpose: classify the request before execution and compose the right workflow/role lenses.

### Core workflows

Install in every preset:

```text
spec-workflow
new-feature-workflow
bugfix-workflow
code-review-workflow
deployment-workflow
```

Add for product/design presets:

```text
redesign-workflow
```

### Native AI runtime foundation

Install in every preset:

```text
native-ai-engineer
native-ai-runtime-agent
native-ai-runtime-ops
context-engineering
context-manager
rule-manager
response-contract
```

Purpose: keep core/app/runtime/product/profile boundaries explicit and make profile behavior repeatable.

### Engineering quality foundation

Install for `engineering`, `product`, `runtime-ops`, and `full`:

```text
systematic-debugging
test-driven-development
refactoring
architecture-review
security-review
threat-modeling
git-workflow
plan
spike
skill-eval
```

### Architecture foundation

Install for `engineering`, `product`, and `full`:

```text
domain-driven-design
ports-and-adapters
api-contract
event-driven-design
service-design
systems-thinking
adr
```

### Runtime operations pack

Install for `runtime-ops` and `full`:

```text
observability-design
resilience-engineering
incident-response
deployment-workflow
native-ai-runtime-ops
```

### Product/design pack

Install for `product` and `full`:

```text
product-manager
master-design
design-review
design-system
design-genre
information-architecture
accessibility
responsiveness
ui-components
ux-patterns-for-developers
ux-ui-patterns
ux-psychology
visual-hierarchy
composition
macrostructures
motion-design
readability
dark-light-theming
copywriting
content-strategy
cro
web-performance
```

## Profile Skeleton

A generated profile should produce this shape under `~/.hermes/profiles/<profile-name>/`:

```text
~/.hermes/profiles/<profile-name>/
├── SOUL.md                         # runtime identity and operating principles
├── config.yaml                     # safe defaults only; no secrets
├── skills.lock.yaml                # chosen skill preset and source pins
├── scripts/
│   ├── install-skills.sh           # installs declared skills
│   └── verify-profile.sh           # validates profile health
├── docs/
│   ├── profile.md                  # what this profile is for
│   └── skill-preset.md             # installed packs and rationale
└── .gitignore                      # excludes state/secrets/logs if this is a distribution repo
```

Never include these in a reusable profile distribution or generated template:

```text
state.db
state.db-wal
state.db-shm
sessions/
memories/
cron/
auth.json
.env
.env.*
logs/
cache/
secrets/
tokens/
credentials/
```

Hermes itself may create a local `.env` inside a live profile during `hermes profile create`; keep that file local, uncommitted, and free of template-owned secrets.

## Generation Procedure

1. **Name the profile.** Accept `<profile-name>` from the user or command. Completion: name is lowercase/hyphenated and safe as a directory name.
2. **Select preset.** Default to `engineering`. Completion: selected preset and included skill packs are listed.
3. **Create profile.** Prefer Hermes CLI when available:
   ```bash
   hermes profile create <profile-name>
   ```
   Completion: `hermes profile show <profile-name>` succeeds, or the generator reports the exact blocker.
4. **Write skeleton files.** Create `SOUL.md`, `skills.lock.yaml`, `docs/profile.md`, `docs/skill-preset.md`, and scripts. Completion: files exist and contain no secrets or live state.
5. **Install skills.** Use `npx skills add puterakahfi/ai-native-skills@<skill-name> -g -y` or the profile's supported install mechanism. Completion: every selected skill is installed or the missing list is explicit.
6. **Configure safe defaults.** Set only reusable profile defaults: toolset preferences, display/language defaults, and verification policy. Completion: no API keys, tokens, product secrets, or local-only paths are embedded.
7. **Verify profile.** Run:
   ```bash
   hermes -p <profile-name> doctor
   hermes -p <profile-name> skills list
   ```
   Completion: doctor output is captured and selected skills appear in the skill list.
8. **Report handoff.** Return profile path, preset, installed packs, verification output, and next manual steps for model/auth setup.

## `skills.lock.yaml` Shape

Use a simple declarative lock file so the profile is reproducible:

```yaml
profile: ai-native-engineering
preset: engineering
source: puterakahfi/ai-native-skills
skills:
  meta:
    - workflow-router
    - role-switcher
  workflows:
    - spec-workflow
    - new-feature-workflow
    - bugfix-workflow
    - code-review-workflow
    - deployment-workflow
  native_ai:
    - native-ai-engineer
    - native-ai-runtime-agent
    - native-ai-runtime-ops
    - context-engineering
    - context-manager
    - rule-manager
    - response-contract
```

Generators may add version pins later, but the initial skeleton should stay readable and editable.

## SOUL.md Baseline

Generated `SOUL.md` should be short and profile-level:

```markdown
# AI Native Engineering Profile

You are operating as an AI-native engineering runtime.

Default behavior:
- Route ambiguous work through `workflow-router` or `role-switcher` before execution.
- Keep Native AI boundaries explicit: core, app adapter, runtime binding, product instance, profile.
- Use workflows for lifecycle tasks and skills for capability-specific gates.
- Verify with real tool output before claiming completion.
- Store durable reusable procedures as skills; keep task progress out of memory.

Do not store secrets, live session state, product-specific facts, or credentials in this profile distribution.
```

## Implementation Notes for `hermes-generate profile`

A future generator should:

- support `--preset minimal|engineering|product|runtime-ops|full`
- support `--dry-run` and print planned file writes and skill installs
- refuse to overwrite an existing profile unless `--force` is explicit
- write idempotent files where possible
- separate stdout data from stderr diagnostics
- accept `--profile-dir` for testing without touching real `~/.hermes`
- produce a final JSON summary for automation

Minimum JSON summary:

```json
{
  "profile": "my-profile",
  "preset": "engineering",
  "path": "~/.hermes/profiles/my-profile",
  "skills_requested": 31,
  "skills_installed": 31,
  "verification": "passed"
}
```

## Common Pitfalls

1. **Committing live Hermes state.** Profile distributions must not include `state.db`, sessions, memories, auth, cron state, or logs.
2. **Baking in product facts.** VisualMate or other product-specific truths belong in product repos or runtime bindings, not the reusable profile skeleton.
3. **Over-installing by default.** Use `engineering` as the default; reserve `full` for explicit requests.
4. **Skipping meta-skills.** Without `workflow-router` and `role-switcher`, the profile loses its routing behavior and becomes just a skill pile.
5. **Treating auth/model setup as reproducible source.** Model selection can be configured; credentials must remain local and manual.
6. **Trusting install output without verification.** Always run `hermes -p <profile-name> skills list` or equivalent after installation.
7. **Duplicating Hermes runtime surfaces.** The profile guides Hermes; it should not create a second dashboard, session store, or gateway implementation.

## Verification Checklist

- [ ] Profile name is explicit and safe.
- [ ] Preset is selected and documented.
- [ ] Meta-skills are included.
- [ ] Core workflows are included.
- [ ] Native AI runtime foundation is included.
- [ ] Preset-specific packs are included and no unrelated packs are installed by default.
- [ ] `SOUL.md`, `skills.lock.yaml`, docs, and scripts are generated without secrets.
- [ ] Live state and credentials are excluded.
- [ ] `hermes -p <profile-name> doctor` was run or blocker reported.
- [ ] Installed skills were listed and compared against `skills.lock.yaml`.
- [ ] Handoff includes manual model/auth steps.
