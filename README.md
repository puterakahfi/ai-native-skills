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

## Skills

Atomic, reusable capabilities. Load individually or composed inside workflows.

| Skill | Description |
|---|---|
| [`architecture-review`](#architecture-review) | Engineering contract compliance reviewer — stack, layers, dependencies, ADR |
| [`context-manager`](#context-manager) | Build context packs for agents — resolve rules, skills, spec before execution |
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
| [`systematic-debugging`](#systematic-debugging) | 4-phase root cause debugging — investigate before fixing |
| [`test-driven-development`](#test-driven-development) | TDD: RED-GREEN-REFACTOR — tests written before implementation |

### Install a skill

```bash
npx skills add puterakahfi/ai-native-skills@architecture-review -g -y
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

## Workflows

Sequenced processes that compose skills. Load a workflow — it declares which skills to load at each phase.

| Workflow | Phases | Skills Used |
|---|---|---|
| [`bugfix-workflow`](#bugfix-workflow) | reproduce → investigate → fix → verify → submit → review | `systematic-debugging`, `architecture-review` |
| [`code-review-workflow`](#code-review-workflow) | load-context → architecture → design → logic → verdict | `architecture-review`, `design-review`, `master-engineer` |
| [`deployment-workflow`](#deployment-workflow) | pre-deploy → context → deploy → verify → confirm/rollback | `security-review`, `context-manager` |
| [`new-feature-workflow`](#new-feature-workflow) | plan → design → implement → verify → submit → review | `master-engineer`, `architecture-review`, `design-review` |

### Install a workflow

```bash
npx skills add puterakahfi/ai-native-skills@bugfix-workflow -g -y
npx skills add puterakahfi/ai-native-skills@code-review-workflow -g -y
npx skills add puterakahfi/ai-native-skills@deployment-workflow -g -y
npx skills add puterakahfi/ai-native-skills@new-feature-workflow -g -y
```

---

## How Skills and Workflows Relate

```
Workflow: new-feature-workflow
  Phase 1: plan       → load master-engineer
  Phase 2: design     → load master-engineer, diagram-architect, master-design, design-review
  Phase 3: implement  → load master-engineer
  Phase 6: review     → load architecture-review, design-review

Skill: architecture-review
  → standalone — use directly in any review context
  → also composed by: bugfix-workflow, new-feature-workflow, code-review-workflow
```

Skills are standalone. Workflows are orchestrators.

---

## Extending Skills (Inheritance)

Product-specific skills extend public skills via `extends` in frontmatter:

```yaml
# In your private Hermes profile or product repo
name: my-team-git-workflow
extends: puterakahfi/ai-native-skills@git-workflow
```

Override only what's team-specific — branch strategy, issue tracker, approval policy. The base skill handles the invariant parts.

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
