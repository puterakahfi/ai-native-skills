# ai-native-skills

Reusable agent skills and workflows for AI-native engineering. Works with any agent that supports the [skills.sh](https://skills.sh) standard — Hermes, Claude Code, Cursor, Codex, Gemini, Windsurf, and 30+ others.

**76 skills · 9 workflows · 6 meta-skills**

See [docs/skills.md](docs/skills.md) for the canonical taxonomy of `skill`, `workflow`, `meta-skill`, and the adapter pattern. See [docs/ai-native-engineering-building-blocks.md](docs/ai-native-engineering-building-blocks.md) for coverage across Agent, Model, Methodology, Spec, and Context. See [docs/skill-packs.md](docs/skill-packs.md) for one-command bundle installs. Skill files follow the [Agent Skills specification](https://agentskills.io/specification); repo-specific fields live under namespaced `metadata` keys.

---

## Install

```bash
# Single skill
npx skills add puterakahfi/ai-native-skills@<skill-name> -g -y

# Examples
npx skills add puterakahfi/ai-native-skills@workflow-router -g -y
npx skills add puterakahfi/ai-native-skills@systems-thinking -g -y
npx skills add puterakahfi/ai-native-skills@ai-system-design -g -y

# Full suite
npx skills add puterakahfi/ai-native-skills -g -y
```

> **Installing a workflow?** Workflows depend on other skills — use the packs in [docs/skill-packs.md](docs/skill-packs.md) to install a workflow + all its dependencies in one command. The Agent Skills spec has no native dependency resolution yet; packs bridge the gap.

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

## Meta-Skills (6)

Load these first — they route and compose everything else.

| Skill | Description |
|---|---|
| `workflow-router` | Detects task type (product-from-zero/refinement/bug/feature/review/deploy) → loads correct workflow automatically |
| `role-switcher` | Detects intent → composes role lenses (design audit → master-design + ux-psychology + product-manager) |
| `design-layout` | Layout & structure port — routes to macrostructures, responsiveness, ui-components |
| `design-visual` | Visual design port — routes to genre, motion, composition, readability |
| `design-strategy` | UX strategy & content port — routes to ux-psychology, information-architecture, cro, copywriting |
| `design-interaction` | Interaction & UX patterns port — routes to ux-ui-patterns, ux-patterns-for-developers |

---

## Workflows (9)

| Workflow | Phases |
|---|---|
| `spec-workflow` | constitution → specify → plan → tasks → implement |
| `new-feature-workflow` | plan → design → implement → verify → submit → review |
| `bugfix-workflow` | reproduce → investigate → fix → verify → submit → review |
| `code-review-workflow` | load-context → architecture-check → design-check → logic-check → verdict |
| `deployment-workflow` | pre-deploy → deploy → health-verify → rollback |
| `redesign-workflow` | existing UI/UX surface refinement — audit → spec → prototype/patch → design-review gates → iterate → deliver |
| `product-development-workflow` | discovery → PRD → MVP → spec → implementation → verification → release → deploy → launch → learn |
| `design-refinement` | targeted design fix — failing-gate triage → patch → re-gate → deliver (no full redesign) |
| `skill-doctor` | skill health — audit → triage → fix monoliths/stubs → verify length + gates |

### Workflow entry points

Use broad lifecycle workflows, not surface-specific workflow variants:

| User intent | Start with |
|---|---|
| Build a product from zero, no PRD yet | `product-development-workflow` |
| Refine/redesign/polish an existing landing page, dashboard, app screen, onboarding flow, pricing page, or portfolio | `redesign-workflow` |
| Fix specific failing design gates without full redesign | `design-refinement` |
| Build a new capability in an existing product | `new-feature-workflow` |
| Fix broken behavior or regression | `bugfix-workflow` |
| Review before merge/ship | `code-review-workflow` |
| Deploy/release/rollback | `deployment-workflow` |
| Audit and fix skill files | `skill-doctor` |

Examples:

```bash
hermes chat -s product-development-workflow -q \
  "Develop a digital product for affiliators from zero. Start with discovery and stop after PRD/MVP recommendation for approval."

hermes chat -s redesign-workflow -q \
  "Refine https://pkahfi.com. Start with audit and redesign spec, then stop for approval before producing code."
```

---

## Skills (76)

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
| `data-modeling` | Schema design, normalization tradeoffs, migration patterns, polyglot persistence |

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
| `technical-debt-governance` | Debt inventory, classification, interest calculation, paydown prioritization |
| `web-performance` | Core Web Vitals scoring, LCP/CLS/INP optimization, font loading, caching |
| `decision-making` | Engineering decision-making frameworks — reversibility classification, pre-mortem, OODA loop |
| `skill-eval` | APPLIED/PARTIAL/GHOST — verify skills are actually applied, not just loaded |

### Experience Design

| Skill | Description |
|---|---|
| `master-design` | Senior Product Designer — Eight Universal Rules, genre, macrostructures, design system |
| `redesign-workflow` | Full redesign loop — Phase 0.5 brief-signal, 35+ gates (G1–G22, R1–R8, C1–C3, H1–H3, CRO1–CRO4), skill-first fix |
| `macrostructures` | Layout archetypes — Marquee Hero, Studio, Editorial; mandatory CSS templates |
| `design-genre` | Editorial dark, minimal light, bold brand — token selection per genre |
| `design-foundation` | Universal design foundation — hierarchy, Ma, Kanso, tokens, a11y |
| `design-brand` | Locked external design systems — brand tokens, constraints, and rules that override genre |
| `design-depth` | Visual depth and layering — multi-layer composition, atmosphere, type interleave, elevation inheritance |
| `design-color` | Color as design structure — palette construction, psychology, harmony rules, genre mapping |
| `design-typography` | Typography as design structure — typeface selection, type scale, pairing, rhythm |
| `design-iconography` | Iconography as design structure — icon style, sizing, optical alignment, usage rules |
| `design-spacing` | Spacing as design structure — visual rhythm, spatial hierarchy, Ma principle |
| `design-system` | Token architecture, component library, design language governance |
| `design-audit` | Standalone design audit — inspect existing UI, produce scored gap report with fix plan |
| `ui-components` | 9 component templates — Navbar, Hero, Section, Work Row, About, Contact, Footer, Scroll Reveal, Verification. Copy-paste, no improvisation |
| `ux-patterns-for-developers` | 74 battle-tested UI patterns from uxpatterns.dev — delegate to `npx skills add` for component behavior + a11y |
| `ux-ui-patterns` | UI/UX pattern library — which hero pattern fits the goal, which layout for content type |
| `composition` | Focal point, optical center (45%), dead space vs breathing room, eye-flow mapping |
| `visual-hierarchy` | Dominant/supporting/accent triad, H2 ≤ 60% H1, heading role taxonomy |
| `readability` | Line length (44ch), contrast, type size, cognitive ease |
| `responsiveness` | Mobile-first, wide/ultrawide breakpoints (1440px, 1920px), max-width containers |
| `motion-design` | Animation tokens, easing, reduced-motion, stagger patterns |
| `dark-light-theming` | Theme switching, token mapping, prefers-color-scheme |
| `design-review` | Design system compliance, AI slop detection, visual hierarchy gates |
| `ux-psychology` | Cognitive load, habit loops, Fitts's Law, Nielsen heuristics |
| `copywriting` | Messaging hierarchy, value prop 1000-person test, bio ≤45 words, buzzword blacklist |
| `content-strategy` | Content strategy — microcopy, tone of voice, content hierarchy, onboarding flows |
| `cro` | Attention flow, trust signals, 8-second window, persuasion sequence |
| `information-architecture` | Content hierarchy, navigation taxonomy, mental models |
| `accessibility` | WCAG 2.1 AA — semantic HTML, ARIA, keyboard nav, screen reader, cognitive |

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
| `experiment-design` | Experiment Design — hypothesis, riskiest assumption, smallest test, success/guardrail criteria, and pass/partial/fail decision rule |
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

Role skills act as **expert personas** — auto-composed by `role-switcher` based on intent detection, no manual activation needed.

| Skill | Persona | Auto-triggers on |
|---|---|---|
| `master-engineer` | Senior Software Engineer | code review, architecture, debugging, refactor |
| `master-design` | Senior Product Designer | UI audit, design system, visual critique |
| `product-manager` | Product Manager | PRD, spec, backlog, gap analysis |
| `ux-psychology` | UX Researcher / Psychologist | user flow, cognitive load, heuristics, retention |
| `user-research` | User Researcher | interviews, usability tests, JTBD, assumption validation |
| `native-ai-engineer` | Native AI Domain Architect | runtime boundary, contract authoring, adapter design |
| `diagram-architect` | Architecture Visualizer | architecture diagrams, flow charts, system maps |
| `prompt-engineer` | Image Prompt Engineer | refine prompt, generate image prompt, why does image look wrong, prompt for [subject] |

---

## Coverage Map

```
Input quality:
  prompt-optimizer → business-value-alignment → experiment-design → response-contract → spec-workflow → threat-modeling

Domain modeling:
  domain-driven-design → ports-and-adapters → design-patterns → adr → data-modeling

Distributed systems:
  service-design → api-contract → event-driven-design

Frontend:
  redesign-workflow → macrostructures → ui-components → ux-patterns-for-developers → accessibility → ux-psychology
  master-design → design-foundation → design-brand → design-depth → design-color → design-typography
  design-layout → design-visual → design-strategy → design-interaction
  composition → visual-hierarchy → copywriting → content-strategy → cro → motion-design

AI systems:
  ai-system-design → ethics-responsible-ai → systems-thinking

Quality gates:
  architecture-review → security-review → code-review-workflow → skill-eval → skill-doctor

Reliability:
  observability-design → resilience-engineering → incident-response → technical-debt-governance

Performance:
  web-performance → design-depth → dark-light-theming → responsiveness

Process:
  product-development-workflow → spec-workflow → new-feature-workflow → bugfix-workflow → deployment-workflow

Philosophy:
  systems-thinking → decision-making → ethics-responsible-ai → adr
```

---

## Full Delivery Loop

```
business-value-alignment ← value: user value, business value, metrics, assumptions, verdict
    ↓
experiment-design      ← learning: hypothesis, riskiest assumption, smallest test, decision rule
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
  ai-native-skills.implements: ai-native-core/contracts/skills/runtime/native-ai-runtime-agent.contract.yaml
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
