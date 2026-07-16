# ai-native-skills

Reusable agent skills and workflows for AI-native engineering. Works with any agent that supports the [skills.sh](https://skills.sh) standard — Hermes, Claude Code, Cursor, Codex, Gemini, Windsurf, and 30+ others.

**66 skills · 7 workflows · 2 meta-skills**

See [docs/skills.md](docs/skills.md) for the canonical taxonomy of `skill`, `workflow`, `meta-skill`, and the adapter pattern. See [docs/ai-native-engineering-building-blocks.md](docs/ai-native-engineering-building-blocks.md) for coverage across Agent, Model, Methodology, Spec, and Context. Skill files follow the [Agent Skills specification](https://agentskills.io/specification); repo-specific fields live under namespaced `metadata` keys.

---

## Install

```bash
npx skills add puterakahfi/ai-native-skills@<skill-name> -g -y

# examples
npx skills add puterakahfi/ai-native-skills@workflow-router -g -y
npx skills add puterakahfi/ai-native-skills@systems-thinking -g -y
npx skills add puterakahfi/ai-native-skills@ai-system-design -g -y
```

---

## Hermes Profile Bootstrap

Use `hermes-profile-bootstrap` when Hermes is already installed and you want to create a ready-to-use AI-native engineering profile skeleton.

Install the bootstrap skill into Hermes:

```bash
npx --yes skills add puterakahfi/ai-native-skills \
  --skill hermes-profile-bootstrap \
  --agent hermes-agent \
  --global \
  --yes
```

Then ask Hermes to bootstrap the profile:

```bash
hermes chat -s hermes-profile-bootstrap -q \
  "Bootstrap the ai-native-engineering profile using the engineering preset. Create the complete skeleton and verify that required skills, workflows, and meta-skills exist."
```

What it creates/checks:

- `SOUL.md`, `skills.lock.yaml`, bootstrap docs, install/verify scripts, and `.gitignore`
- required meta-skills: `workflow-router`, `role-switcher`
- required workflows: `product-development-workflow`, `spec-workflow`, `new-feature-workflow`, `bugfix-workflow`, `code-review-workflow`, `deployment-workflow`
- required Native AI, engineering quality, and architecture foundation skills
- correct `metadata["ai-native-skills.type"]` for meta-skills and workflows
- no secrets, credentials, or live Hermes state in the reusable skeleton

One-shot mode without installing the skill permanently:

```bash
hermes chat -q "$(npx --yes skills use puterakahfi/ai-native-skills@hermes-profile-bootstrap)

Bootstrap the ai-native-engineering profile using the engineering preset. Verify required skill packs before claiming done."
```

This is a Hermes adapter skill for the runtime-agnostic profile-bootstrap contract in [`ai-native-core`](https://github.com/puterakahfi/ai-native-core). It is not a standalone `hermes-generate` binary yet.

---

## Skill Type Taxonomy

`ai-native-skills` uses three official category values under `metadata["ai-native-skills.type"]`. See [docs/skills.md](docs/skills.md) for definitions, decision rules, and the adapter pattern.

| Type | Description | Examples |
|---|---|---|
| `skill` | Atomic capability — standalone, reusable domain capability or expert lens | `systematic-debugging`, `threat-modeling` |
| `workflow` | Sequenced phases — lifecycle with gates, often composing skills | `bugfix-workflow`, `redesign-workflow` |
| `meta-skill` | Router/composer — selects workflows or skill combinations before execution | `role-switcher`, `workflow-router` |

---

## Meta-Skills (2)

Load these first — they route and compose everything else.

| Skill | Description |
|---|---|
| `workflow-router` | Detects task type (product-from-zero/refinement/bug/feature/review/deploy) → loads correct workflow automatically |
| `role-switcher` | Detects intent → composes role lenses (design audit → master-design + ux-psychology + product-manager) |

---

## Workflows (7)

| Workflow | Phases |
|---|---|
| `spec-workflow` | constitution → specify → plan → tasks → implement |
| `new-feature-workflow` | plan → design → implement → verify → submit → review |
| `bugfix-workflow` | reproduce → investigate → fix → verify → submit → review |
| `code-review-workflow` | load-context → architecture-check → design-check → logic-check → verdict |
| `deployment-workflow` | pre-deploy → deploy → health-verify → rollback |
| `redesign-workflow` | existing UI/UX surface refinement — audit → spec → prototype/patch → design-review gates → iterate → deliver |
| `product-development-workflow` | discovery → PRD → MVP → spec → implementation → verification → release → deploy → launch → learn |

### Workflow entry points

Use broad lifecycle workflows, not surface-specific workflow variants:

| User intent | Start with |
|---|---|
| Build a product from zero, no PRD yet | `product-development-workflow` |
| Refine/redesign/polish an existing landing page, dashboard, app screen, onboarding flow, pricing page, or portfolio | `redesign-workflow` |
| Build a new capability in an existing product | `new-feature-workflow` |
| Fix broken behavior or regression | `bugfix-workflow` |
| Review before merge/ship | `code-review-workflow` |
| Deploy/release/rollback | `deployment-workflow` |

Examples:

```bash
hermes chat -s product-development-workflow -q \
  "Develop a digital product for affiliators from zero. Start with discovery and stop after PRD/MVP recommendation for approval."

hermes chat -s redesign-workflow -q \
  "Refine https://pkahfi.com. Start with audit and redesign spec, then stop for approval before producing code."
```

---

## Skills (66)

### Domain Architecture

| Skill | Description |
|---|---|
| `domain-driven-design` | Bounded contexts, aggregates, value objects, domain events, ubiquitous language |
| `ports-and-adapters` | Hexagonal architecture — port definition, adapter implementation, domain isolation |
| `design-patterns` | GoF creational/structural/behavioral + CQRS, Saga, Outbox |
| `service-design` | Service boundary by bounded context, sync vs async, data ownership |
| `api-contract` | OpenAPI, versioning, breaking change detection, consumer-driven contract testing |
| `event-driven-design` | Event schema, saga, idempotency, DLQ, Outbox, CQRS flow |
| `micro-frontend` | Module federation, MFE boundary, shell contract, CSS isolation |
| `adr` | Architecture Decision Records — immutable, superseding pattern, tradeoff-honest |
| `ai-system-design` | RAG, agent memory, LLM evals, prompt injection defense, graceful degradation |
| `systems-thinking` | Feedback loops, second-order effects, Conway's Law, Goodhart's Law, leverage points |

### Engineering Quality

| Skill | Description |
|---|---|
| `architecture-review` | Contract compliance — layer violations, DDD gates, dependency drift |
| `systematic-debugging` | 4-phase root cause — investigate, analyze, hypothesize, fix |
| `security-review` | OWASP baseline, secrets detection, injection vectors, auth gaps |
| `threat-modeling` | STRIDE per trust boundary, data flow mapping, risk rating, proactive security |
| `resilience-engineering` | Failure mode analysis, circuit breakers, chaos engineering, RTO/RPO |
| `incident-response` | Structured incident lifecycle, blameless postmortem, 5 Whys to systemic cause |
| `refactoring` | Named code smells, green-first, small steps, one type per commit |
| `test-driven-development` | RED-GREEN-REFACTOR — tests before implementation, every time |
| `skill-eval` | APPLIED/PARTIAL/GHOST — verify skills are actually applied, not just loaded |

### Experience Design

| Skill | Description |
|---|---|
| `master-design` | Senior Product Designer — UI/UX, wireframes, design systems |
| `design-review` | Design system compliance, AI slop detection, visual hierarchy gates |
| `ux-psychology` | Cognitive load, habit loops, Fitts's Law, Nielsen heuristics |
| `accessibility` | WCAG 2.1 AA — semantic HTML, ARIA, keyboard nav, screen reader, cognitive |
| `micro-frontend` | MFE architecture — see Domain Architecture |

### Observability & Operations

| Skill | Description |
|---|---|
| `observability-design` | Logs + metrics + traces — three pillars, four golden signals, SLO, alerts |
| `incident-response` | See Engineering Quality |

### Context & Prompt Engineering

| Skill | Description |
|---|---|
| `prompt-optimizer` | Vague intent → precise prompt: scope, constraint, output format, stop condition |
| `model-selection` | Select model class by task intent, risk, capabilities, context, fallback, and verification needs |
| `response-contract` | Persistent output verbosity via AGENTS.md — no filler, answer-first, code exact |
| `context-engineering` | AGENTS.md authoring — encode constraints, guardrails, domain knowledge |
| `context-manager` | Context pack resolution — build precise context before agent execution |

### Process & Developer Experience

| Skill | Description |
|---|---|
| `spec-workflow` | See Workflows |
| `plan` | Actionable markdown plan with exact file paths |
| `spike` | Throwaway experiment — validate idea, produce verdict |
| `onboarding` | Bootstrap agent/engineer context — recon codebase, produce AGENTS.md |

### Product Management

| Skill | Description |
|---|---|
| `product-requirements` | PRD authoring — goals, non-goals, scope, metrics, requirements, acceptance criteria, launch readiness |
| `business-value-alignment` | Business Value Alignment — user value, business value, metrics, assumptions, risks, and continue/narrow/experiment/stop verdict |
| `product-manager` | PRD authoring, acceptance criteria, task breakdown, scope, and prioritization |
| `user-research` | User interviews, synthesis, insights, personas, JTBD, and research-backed decisions |

### Governance & Standards

| Skill | Description |
|---|---|
| `ethics-responsible-ai` | Fairness audit, harm assessment, transparency, consent, accountability, power asymmetry |
| `threat-modeling` | See Engineering Quality |
| `language-standards` | Consistent declared language across artifacts |
| `rule-manager` | AGENTS.md/.cursorrules authoring and enforcement |
| `git-workflow` | Branch, commit, PR, merge — generic source control |
| `adr` | See Domain Architecture |

### Native AI Ecosystem

| Skill | Description |
|---|---|
| `native-ai-engineer` | Layer placement, runtime boundary, contract authoring |
| `native-ai-runtime-agent` | Runtime agent in ai-native-fw product adapters |
| `native-ai-runtime-ops` | Ops for AI-native canonical runtime hosts |
| `hermes-profile-bootstrap` | Hermes adapter for the Native AI profile-bootstrap contract: profile skeleton, skill presets, install plan, and verification policy |

### Roles

| Skill | Description |
|---|---|
| `master-engineer` | Senior Software Engineer — system design, architecture decisions |
| `product-manager` | PRD authoring, acceptance criteria, task breakdown |
| `diagram-architect` | Architecture diagrams — SVG, Excalidraw, Mermaid |

---

## Coverage Map

```
Input quality:
  prompt-optimizer → business-value-alignment → response-contract → spec-workflow → threat-modeling

Domain modeling:
  domain-driven-design → ports-and-adapters → design-patterns → adr

Distributed systems:
  service-design → api-contract → event-driven-design

Frontend:
  redesign-workflow → micro-frontend → accessibility → ux-psychology

AI systems:
  ai-system-design → ethics-responsible-ai → systems-thinking

Quality gates:
  architecture-review → security-review → code-review-workflow → skill-eval

Reliability:
  observability-design → resilience-engineering → incident-response

Process:
  product-development-workflow → spec-workflow → new-feature-workflow → bugfix-workflow → deployment-workflow

Philosophy:
  systems-thinking → ethics-responsible-ai → adr
```

---

## Full Delivery Loop

```
business-value-alignment ← value: user value, business value, metrics, assumptions, verdict
    ↓
product-requirements    ← PRD: goals, non-goals, scope, metrics, acceptance criteria
    ↓
product-development-workflow ← umbrella flow from discovery to launch
    ↓
spec-workflow          ← spec before code
    ↓
threat-modeling        ← security before implementation
    ↓
new-feature-workflow   ← team process
    ↓
code-review-workflow   ← gate before merge
    ↓
deployment-workflow    ← gate before prod
    ↓
observability-design   ← monitor after deploy
    ↓
incident-response      ← when things go wrong
```

With meta-skills routing:
```
workflow-router → detect: product-from-zero? refinement? bug? feature? review? deploy?
role-switcher   → compose: which lenses for this task?
```

---

## Adapter Pattern

Adapter behavior is a pattern, not a separate official category value today. Use `metadata["ai-native-skills.type"]: skill` plus `metadata["ai-native-skills.implements"]` and `compat/*.compat.yaml` when a skill implements a Native AI Core contract.

```yaml
name: native-ai-runtime-agent
metadata:
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/runtime-agent/native-ai-runtime-agent.contract.yaml
```

See [docs/skills.md](docs/skills.md#adapter-pattern) for details.

---

## Skill Evaluation

```bash
python ai-native-core/scripts/run-eval.py \
  --skill role-switcher \
  --output-file /tmp/agent-output.txt
# verdict: APPLIED | PARTIAL | GHOST
```

---

## Related

- [ai-native-core](https://github.com/puterakahfi/ai-native-core) — contracts (ports)
- [ai-native-fw](https://github.com/puterakahfi/ai-native-fw) — product runtime adapter
- [skills.sh](https://skills.sh) — open skills ecosystem standard
