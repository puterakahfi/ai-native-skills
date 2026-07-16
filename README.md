# ai-native-skills

Reusable agent skills and workflows for AI-native engineering. Works with any agent that supports the [skills.sh](https://skills.sh) standard — Hermes, Claude Code, Cursor, Codex, Gemini, Windsurf, and 30+ others.

**48 skills · 5 workflows · 2 meta-skills**

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

## Skill Type Taxonomy

| Type | Description | Examples |
|---|---|---|
| `skill` | Atomic capability — standalone, single domain | `systematic-debugging`, `threat-modeling` |
| `workflow` | Sequenced phases — composes skills | `bugfix-workflow`, `deployment-workflow` |
| `meta-skill` | Orchestrates other skills dynamically | `role-switcher`, `workflow-router` |
| `skill-adapter` | Extends base skill for product-specific context | `arbiter-git-workflow extends git-workflow` |

---

## Meta-Skills (2)

Load these first — they route and compose everything else.

| Skill | Description |
|---|---|
| `workflow-router` | Detects task type (bug/feature/review/deploy) → loads correct workflow automatically |
| `role-switcher` | Detects intent → composes role lenses (design audit → master-design + ux-psychology + product-manager) |

---

## Workflows (5)

| Workflow | Phases |
|---|---|
| `spec-workflow` | constitution → specify → plan → tasks → implement |
| `new-feature-workflow` | plan → design → implement → verify → submit → review |
| `bugfix-workflow` | reproduce → investigate → fix → verify → submit → review |
| `code-review-workflow` | load-context → architecture-check → design-check → logic-check → verdict |
| `deployment-workflow` | pre-deploy → deploy → health-verify → rollback |

---

## Skills (48)

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
  prompt-optimizer → response-contract → spec-workflow → threat-modeling

Domain modeling:
  domain-driven-design → ports-and-adapters → design-patterns → adr

Distributed systems:
  service-design → api-contract → event-driven-design

Frontend:
  micro-frontend → accessibility → ux-psychology

AI systems:
  ai-system-design → ethics-responsible-ai → systems-thinking

Quality gates:
  architecture-review → security-review → code-review-workflow → skill-eval

Reliability:
  observability-design → resilience-engineering → incident-response

Process:
  spec-workflow → new-feature-workflow → bugfix-workflow → deployment-workflow

Philosophy:
  systems-thinking → ethics-responsible-ai → adr
```

---

## Full Delivery Loop

```
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
workflow-router → detect: bug? feature? review? deploy?
role-switcher   → compose: which lenses for this task?
```

---

## Inheritance Pattern

```yaml
# skill-adapter extends public base skill
name: arbiter-git-workflow
type: skill-adapter
extends: puterakahfi/ai-native-skills@git-workflow
# Override only what's product-specific
```

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
