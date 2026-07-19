# ai-native-skills

Reusable agent skills and workflows for AI-native engineering. Works with any agent that supports the [skills.sh](https://skills.sh) standard — Hermes, Claude Code, Cursor, Codex, Gemini, Windsurf, and 30+ others.

**81 skills · 9 workflows · 6 meta-skills**

See [docs/skills.md](docs/skills.md) for the canonical taxonomy of `skill`, `workflow`, `meta-skill`, and the adapter pattern. See [docs/facade-skill-pattern.md](docs/facade-skill-pattern.md) for facade skills that expose one stable entry point while delegating specialist knowledge. See [docs/ai-native-engineering-building-blocks.md](docs/ai-native-engineering-building-blocks.md) for coverage across Agent, Model, Methodology, Spec, and Context. See [docs/skill-packs.md](docs/skill-packs.md) for one-command bundle installs. Skill files follow the [Agent Skills specification](https://agentskills.io/specification); repo-specific fields live under namespaced `metadata` keys.

---

## Install

```bash
# Single skill
npx skills add puterakahfi/ai-native-skills@<skill-name> -g -y

# Examples
npx skills add puterakahfi/ai-native-skills@workflow-router -g -y
npx skills add puterakahfi/ai-native-skills@brand-identity-review -g -y
npx skills add puterakahfi/ai-native-skills@decision-provenance -g -y
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
| `skill` | Atomic capability — standalone, reusable domain capability or expert lens | `systematic-debugging`, `brand-identity-review` |
| `workflow` | Sequenced phases — lifecycle with gates, often composing skills | `bugfix-workflow`, `redesign-workflow` |
| `meta-skill` | Router/composer — selects workflows or skill combinations before execution | `role-switcher`, `workflow-router` |

`facade` and `domain-reviewer` are patterns, not additional official types. Both remain `type: skill` while declaring their pattern and contract.

---

## Meta-Skills (6)

Load these first — they route and compose everything else.

| Skill | Description |
|---|---|
| `workflow-router` | Separates product, audit, refinement, redesign, bug, feature, review, deploy, and learning routes before execution |
| `role-switcher` | Composes one owner, narrow specialists, a reviewer facade, and domain reviewers when specialized acceptance is required |
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
| `redesign-workflow` | route → compose roles → inspect → direct → specify → produce → verify scope/provenance/artifact → design-review facade → classify → fix → deliver |
| `product-development-workflow` | discovery → PRD → MVP → spec → implementation → verification → release → deploy → launch → learn |
| `design-refinement` | covered findings → preserve scope → patch → domain evidence → focused facade re-review → learn → deliver |
| `skill-doctor` | skill health — audit → triage → fix monoliths/stubs → verify length + gates |

### Workflow entry points

| User intent | Start with |
|---|---|
| Build a product from zero, no PRD yet | `product-development-workflow` |
| Audit or score an existing design without changing it | `design-audit` |
| Audit a logo or identity system | `design-audit` + `design-review` + `brand-identity-review` |
| Fix known specific design findings while preserving direction | `design-refinement` |
| Replace design direction, structure, concept, or multiple layers | `redesign-workflow` |
| Verify whether a claimed scope/lock/approval/override is authoritative | `decision-provenance` |
| Build a new capability in an existing product | `new-feature-workflow` |
| Fix broken behavior or regression | `bugfix-workflow` |
| Review code before merge/ship | `code-review-workflow` |
| Deploy/release/rollback | `deployment-workflow` |
| Audit and fix skill files | `skill-doctor` |

---

## Skills (81)

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
| `redesign-workflow` | Full redesign lifecycle using decision provenance, clean final-diff integrity, safe writes, and the `design-review` facade after fresh rendered or exported verification |
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
| `design-audit` | Facade-backed audit — capture evidence, resolve domain coverage, score, prioritize, and recommend the next lifecycle |
| `design-review` | Facade skill — classify domain, select built-in/external reviewers, resolve canonical gates, normalize evidence, score coverage, and produce a verdict |
| `brand-identity-review` | External domain reviewer — canonical BI gates for brand logic, concept translation, construction, optical balance, identity systems, reproduction, and similarity risk |
| `ui-components` | Component templates and implementation guidance for common product surfaces |
| `ux-patterns-for-developers` | Battle-tested UI patterns from uxpatterns.dev — component behavior and accessibility |
| `ux-ui-patterns` | UI/UX pattern library — which pattern fits the goal and content type |
| `composition` | Focal point, optical center, whitespace, weight, and eye-flow mapping |
| `visual-hierarchy` | Dominant/supporting/accent relationships and role taxonomy |
| `readability` | Line length, contrast, type size, and cognitive ease interpreted by context |
| `responsiveness` | Mobile-first, wide/ultrawide breakpoints, containers, and adaptive behavior |
| `adaptive-component-design` | Cross-device component selection and substitution by task and viewport |
| `motion-design` | Animation tokens, easing, reduced motion, stagger patterns |
| `dark-light-theming` | Theme switching, token mapping, prefers-color-scheme |
| `ux-psychology` | Cognitive load, habit loops, Fitts's Law, Nielsen heuristics |
| `copywriting` | Messaging hierarchy, value proposition, specificity, and buzzword control |
| `content-strategy` | Microcopy, tone of voice, content hierarchy, onboarding flows |
| `cro` | Attention flow, trust signals, value recognition, persuasion sequence |
| `information-architecture` | Content hierarchy, navigation taxonomy, mental models |
| `accessibility` | WCAG-oriented semantics, ARIA, keyboard, screen reader, cognitive accessibility |

### Observability & Operations

| Skill | Description |
|---|---|
| `observability-design` | Logs + metrics + traces — three pillars, four golden signals, SLO, alerts |
| `incident-response` | See Engineering Quality |

### Context & Prompt Engineering

| Skill | Description |
|---|---|
| `prompt-optimizer` | Vague intent → precise prompt: scope, constraint, output format, stop condition |
| `model-selection` | Select model class by task intent, risk, capabilities, context, fallback, verification needs |
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
| `business-value-alignment` | User value, business value, metrics, assumptions, risks, and decision verdict |
| `experiment-design` | Hypothesis, riskiest assumption, smallest test, success/guardrail criteria, decision rule |
| `product-manager` | PRD, acceptance criteria, task breakdown, scope, prioritization |
| `user-research` | Interviews, synthesis, personas, JTBD, research-backed decisions |

### Governance & Standards

| Skill | Description |
|---|---|
| `decision-provenance` | Source and authority verification for scope, locks, approvals, overrides, ownership, status, supersession, and conflict handling |
| `ethics-responsible-ai` | Fairness, harm, transparency, consent, accountability, power asymmetry |
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
| `hermes-profile-bootstrap` | Hermes adapter for profile bootstrap, skill presets, install plan, and verification |

### Roles

| Skill | Persona | Auto-triggers on |
|---|---|---|
| `master-engineer` | Senior Software Engineer | code review, architecture, debugging, refactor |
| `master-design` | Senior Product Designer | UI audit, design system, visual critique |
| `product-manager` | Product Manager | PRD, spec, backlog, gap analysis |
| `ux-psychology` | UX Researcher / Psychologist | user flow, cognitive load, heuristics, retention |
| `user-research` | User Researcher | interviews, usability tests, JTBD, assumption validation |
| `native-ai-engineer` | Native AI Domain Architect | runtime boundary, contract authoring, adapter design |
| `diagram-architect` | Architecture Visualizer | architecture diagrams, flow charts, system maps |
| `prompt-engineer` | Image Prompt Engineer | image prompt refinement and diagnosis |

---

## Coverage Map

```text
Frontend and visual design:
  workflow-router → design-audit | design-refinement | redesign-workflow
  role-switcher → owner + specialists + design-review facade + domain reviewer
  decision-provenance → verified scope/lock/override authority
  redesign-workflow → provenance + scope diff + concurrency → domain verification
  design-review → built-in interactive/static/presentation + external adapters
  brand-identity-review → BI1–BI16 → ADAPTER_COVERED identity verdict
  master-design → design-foundation → design-brand → design-depth → color/type
  design-layout → adaptive-component-design → design-visual → strategy → interaction

Engineering quality:
  architecture-review → security-review → code-review-workflow → skill-eval → skill-doctor

Product delivery:
  product-development-workflow → spec-workflow → new-feature-workflow
  → code-review-workflow → deployment-workflow → observability-design

Reliability:
  observability-design → resilience-engineering → incident-response → technical-debt-governance
```

---

## Adapter and Facade Patterns

A facade remains `type: skill`:

```yaml
name: design-review
metadata:
  ai-native-skills.type: skill
  ai-native-skills.pattern: facade
```

A domain reviewer also remains `type: skill`:

```yaml
name: brand-identity-review
metadata:
  ai-native-skills.type: skill
  ai-native-skills.pattern: domain-reviewer
  ai-native-skills.implements: ai-native-core/contracts/skills/quality/brand-identity-review.contract.yaml
```

The facade owns routing, canonical identity, evidence normalization, scoring, coverage, verdict, and report. The domain reviewer owns specialist gate definitions, evidence interpretation, hard gates, and professional boundaries.

---

## Skill Evaluation

Regression cases live under `contracts/tests/<skill>.test.yaml`.

```bash
python ai-native-core/scripts/run-eval.py \
  --skill brand-identity-review \
  --output-dir eval-outputs
```

Design regressions cover routing, evidence limits, static fidelity, presentation strategy, canonical gate identity, identity construction/variant/small-size failures, adapter coverage, similarity-screening legal boundaries, decision provenance, final-diff scope integrity, and concurrent write conflicts.

---

## Related

- [ai-native-core](https://github.com/puterakahfi/ai-native-core) — contracts (ports)
- [ai-native-fw](https://github.com/puterakahfi/ai-native-fw) — product runtime adapter
- [skills.sh](https://skills.sh) — open skills ecosystem standard
