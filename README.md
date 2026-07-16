# ai-native-skills

Reusable agent skills and workflows for AI-native engineering. Works with any agent that supports the [skills.sh](https://skills.sh) standard — Hermes, Claude Code, Cursor, Codex, and more.

Part of the [AI-Native Engineering](https://github.com/puterakahfi/ai-native-core) ecosystem.

```
ai-native-core        → domain contracts (what)
ai-native-skills      → agent implementations (how)  ← you are here
ai-native-fw          → product adapters (where)
```

---

## Install

```bash
# single skill
npx skills add puterakahfi/ai-native-skills@<skill-name> -g -y

# all skills
npx skills add puterakahfi/ai-native-skills -g -y
```

---

## Skills (18)

Atomic, reusable capabilities. Load individually or composed inside workflows.

| Skill | Description |
|---|---|
| [`architecture-review`](#architecture-review) | Engineering contract compliance reviewer — stack, layers, dependencies, ADR |
| [`context-engineering`](#context-engineering) | Author AGENTS.md, .cursorrules, and context packs that encode architecture constraints into the AI workspace |
| [`context-manager`](#context-manager) | Resolve and validate context packs before agent execution — rules, skills, spec |
| [`design-review`](#design-review) | Design system compliance + AI slop detector — token, layout, visual direction |
| [`diagram-architect`](#diagram-architect) | Architecture, workflow, and contract diagrams — renderer-agnostic |
| [`git-workflow`](#git-workflow) | Source control — branching, commits, PR/MR, merge. All conventions product-defined |
| [`master-design`](#master-design) | Senior Product Designer — wireframes, mockups, interaction contracts, design systems |
| [`master-engineer`](#master-engineer) | Senior Software Engineer — architecture decisions, system design, patterns |
| [`native-ai-engineer`](#native-ai-engineer) | AI-native domain contract architect — layer placement, runtime boundaries |
| [`native-ai-runtime-agent`](#native-ai-runtime-agent) | Runtime agent for ai-native-fw product adapters |
| [`native-ai-runtime-ops`](#native-ai-runtime-ops) | Ops for AI-native runtime hosts — SSH, bootstrap, gateway, backup |
| [`plan`](#plan) | Write actionable markdown plans with exact file paths before execution |
| [`product-manager`](#product-manager) | PRDs, acceptance criteria, task breakdown, prioritization |
| [`rule-manager`](#rule-manager) | Author and validate AGENTS.md, .cursorrules, per-product rules |
| [`security-review`](#security-review) | Security baseline validation — secrets, injection, auth, dependencies |
| [`spike`](#spike) | Throwaway experiments to validate an idea — verdict, not production code |
| [`systematic-debugging`](#systematic-debugging) | 4-phase root cause debugging — investigate before fixing. Includes agent thrashing detection |
| [`test-driven-development`](#test-driven-development) | TDD: RED-GREEN-REFACTOR — tests written before implementation |

```bash
npx skills add puterakahfi/ai-native-skills@architecture-review -g -y
npx skills add puterakahfi/ai-native-skills@context-engineering -g -y
npx skills add puterakahfi/ai-native-skills@context-manager -g -y
npx skills add puterakahfi/ai-native-skills@design-review -g -y
npx skills add puterakahfi/ai-native-skills@diagram-architect -g -y
npx skills add puterakahfi/ai-native-skills@git-workflow -g -y
npx skills add puterakahfi/ai-native-skills@master-design -g -y
npx skills add puterakahfi/ai-native-skills@master-engineer -g -y
npx skills add puterakahfi/ai-native-skills@native-ai-engineer -g -y
npx skills add puterakahfi/ai-native-skills@native-ai-runtime-agent -g -y
npx skills add puterakahfi/ai-native-skills@native-ai-runtime-ops -g -y
npx skills add puterakahfi/ai-native-skills@plan -g -y
npx skills add puterakahfi/ai-native-skills@product-manager -g -y
npx skills add puterakahfi/ai-native-skills@rule-manager -g -y
npx skills add puterakahfi/ai-native-skills@security-review -g -y
npx skills add puterakahfi/ai-native-skills@spike -g -y
npx skills add puterakahfi/ai-native-skills@systematic-debugging -g -y
npx skills add puterakahfi/ai-native-skills@test-driven-development -g -y
```

---

## Workflows (5)

Sequenced processes that compose skills. Load a workflow — it declares which skills to load at each phase.

| Workflow | Phases | Skills Used |
|---|---|---|
| [`spec-workflow`](#spec-workflow) | constitution → specify → plan → tasks → implement | `native-ai-engineer`, `master-engineer`, `product-manager`, `plan`, `context-manager`, `rule-manager` |
| [`new-feature-workflow`](#new-feature-workflow) | plan → design → implement → verify → submit → review | `master-engineer`, `master-design`, `architecture-review`, `design-review` |
| [`bugfix-workflow`](#bugfix-workflow) | reproduce → investigate → fix → verify → submit → review | `systematic-debugging`, `architecture-review` |
| [`code-review-workflow`](#code-review-workflow) | load-context → architecture → design → logic → verdict | `architecture-review`, `design-review`, `master-engineer` |
| [`deployment-workflow`](#deployment-workflow) | pre-deploy → context → deploy → verify → confirm/rollback | `security-review`, `context-manager` |

```bash
npx skills add puterakahfi/ai-native-skills@spec-workflow -g -y
npx skills add puterakahfi/ai-native-skills@new-feature-workflow -g -y
npx skills add puterakahfi/ai-native-skills@bugfix-workflow -g -y
npx skills add puterakahfi/ai-native-skills@code-review-workflow -g -y
npx skills add puterakahfi/ai-native-skills@deployment-workflow -g -y
```

---

## Full Delivery Loop

These workflows compose into a complete spec-to-production pipeline:

```
spec-workflow            ← input quality: no vague prompts, no implementation without spec
  ↓
new-feature-workflow     ← team process: design → implement → submit
  ↓
code-review-workflow     ← output quality: architecture + design + logic gates
  ↓
deployment-workflow      ← deploy gate: security → context → deploy → verify
```

Each workflow is independent — use any subset that fits your team's process.

---

## Context Engineering vs Context Manager

Two related but distinct skills:

| | `context-manager` | `context-engineering` |
|---|---|---|
| **What** | Resolves context before a task runs | Authors context that persists across all tasks |
| **When** | Per-task, just-in-time | One-time setup, updated on contract changes |
| **Output** | Context pack for agent | AGENTS.md, .cursorrules, context templates |
| **Analogy** | Pull the right files from the shelf | Design and organize the shelf |

---

## Extending Skills (Inheritance)

Product-specific skills extend public skills via `extends` in frontmatter:

```yaml
# In your Hermes profile or product repo
name: my-team-git-workflow
extends: puterakahfi/ai-native-skills@git-workflow
```

Override only what's team-specific — branch strategy, issue tracker, approval policy.

---

## Contract Traceability

Every skill and workflow traces to a contract in [ai-native-core](https://github.com/puterakahfi/ai-native-core):

```yaml
# In every SKILL.md frontmatter
implements: ai-native-core/contracts/skills/quality-control/architecture-review.contract.yaml
```

Contracts define: capability, quality gates, required inputs/outputs, adapter requirements.
Skills define: how to fulfill the contract as an executable agent procedure.

---

## Related

- [ai-native-core](https://github.com/puterakahfi/ai-native-core) — domain contracts
- [ai-native-fw](https://github.com/puterakahfi/ai-native-fw) — product adapters
- [skills.sh](https://skills.sh) — open agent skills registry
