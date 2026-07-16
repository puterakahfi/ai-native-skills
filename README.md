# ai-native-skills

Reusable agent skills and workflows for AI-native engineering. Works with any agent that supports the [skills.sh](https://skills.sh) standard — Hermes, Claude Code, Cursor, Codex, Gemini, Windsurf, and 30+ others.

**41 skills · 5 workflows · 2 meta-skills**

---

## Install

```bash
# single skill
npx skills add puterakahfi/ai-native-skills@<skill-name> -g -y

# examples
npx skills add puterakahfi/ai-native-skills@workflow-router -g -y
npx skills add puterakahfi/ai-native-skills@domain-driven-design -g -y
npx skills add puterakahfi/ai-native-skills@systematic-debugging -g -y
```

---

## Skill Type Taxonomy

| Type | Description | Examples |
|---|---|---|
| `skill` | Atomic capability — standalone, single domain | `systematic-debugging`, `security-review` |
| `workflow` | Sequenced phases — composes skills | `bugfix-workflow`, `deployment-workflow` |
| `meta-skill` | Orchestrates other skills dynamically | `role-switcher`, `workflow-router` |
| `skill-adapter` | Extends base skill for product-specific context | `arbiter-git-workflow extends git-workflow` |

---

## Meta-Skills

Load these first — they route and compose everything else.

| Skill | Description |
|---|---|
| `workflow-router` | Detects task type (bug/feature/review/deploy) → loads correct workflow automatically |
| `role-switcher` | Detects intent → composes role lenses (design audit → master-design + ux-psychology + product-manager) |

```bash
npx skills add puterakahfi/ai-native-skills@workflow-router -g -y
npx skills add puterakahfi/ai-native-skills@role-switcher -g -y
```

---

## Workflows (5)

Sequenced multi-phase processes that compose atomic skills.

| Workflow | Phases | Skills Used |
|---|---|---|
| `spec-workflow` | constitution → specify → plan → tasks → implement | plan, product-manager, master-engineer |
| `new-feature-workflow` | plan → design → implement → verify → submit → review | spec-workflow, plan, tdd, master-engineer, architecture-review |
| `bugfix-workflow` | reproduce → investigate → fix → verify → submit → review | systematic-debugging, architecture-review, git-workflow |
| `code-review-workflow` | load-context → architecture-check → design-check → logic-check → verdict | architecture-review, design-review, security-review |
| `deployment-workflow` | pre-deploy → deploy → health-verify → rollback | security-review, architecture-review |

---

## Skills (34)

### Domain Architecture

| Skill | Description |
|---|---|
| `domain-driven-design` | Bounded contexts, aggregates, value objects, domain events, ubiquitous language, repository pattern |
| `ports-and-adapters` | Hexagonal architecture — port definition, adapter implementation, domain isolation, testable domain |
| `design-patterns` | GoF creational/structural/behavioral + CQRS, Saga, Outbox — forces-first selection |
| `service-design` | Service boundary by bounded context, sync vs async justification, data ownership, strangler fig |
| `api-contract` | OpenAPI spec, versioning, breaking change detection, consumer-driven contract testing, deprecation |
| `event-driven-design` | Event schema, producer/consumer contracts, saga patterns, idempotency, DLQ, Outbox, CQRS flow |
| `micro-frontend` | Module federation, MFE boundary by bounded context, shell contract, CSS isolation, independent deploy |
| `adr` | Architecture Decision Records — immutable, status lifecycle, superseding pattern, tradeoff-honest |

### Engineering Quality

| Skill | Description |
|---|---|
| `architecture-review` | Contract compliance — stack violations, layer boundaries, DDD gates, dependency drift |
| `systematic-debugging` | 4-phase root cause — investigate, analyze, hypothesize, fix. Agent thrashing detection |
| `security-review` | OWASP baseline, secrets detection, injection vectors, auth gaps, pre-deploy security gate |
| `refactoring` | Named code smells, green-first, small steps, one type per commit — no behavior change |
| `test-driven-development` | RED-GREEN-REFACTOR cycle — tests before implementation, every time |
| `skill-eval` | APPLIED/PARTIAL/GHOST classification — verify skills are actually applied, not just loaded |

### Experience Design

| Skill | Description |
|---|---|
| `master-design` | Senior Product Designer — UI/UX, wireframes, design systems, interaction design |
| `design-review` | Design system compliance, AI slop detection, accessibility, visual hierarchy gates |
| `ux-psychology` | Cognitive load, habit loops, Fitts's Law, Hick's Law, gestalt, Nielsen heuristics |
| `micro-frontend` | MFE architecture — see Domain Architecture above |

### Observability & Operations

| Skill | Description |
|---|---|
| `observability-design` | Logs + metrics + traces — three pillars, four golden signals, SLO, alerts, cardinality control |
| `deployment-workflow` | See Workflows above |

### Context & Prompt Engineering

| Skill | Description |
|---|---|
| `prompt-optimizer` | Transform vague intent → precise prompt: scope, constraint, output format, stop condition |
| `response-contract` | Persistent output verbosity via AGENTS.md — no filler, answer-first, code exact |
| `context-engineering` | AGENTS.md authoring — encode architecture constraints, guardrails, domain knowledge |
| `context-manager` | Context pack resolution — build precise context before agent execution |

### Process & Workflows

| Skill | Description |
|---|---|
| `spec-workflow` | See Workflows above |
| `plan` | Actionable markdown plan with exact file paths before any implementation |
| `spike` | Throwaway experiment — validate idea, produce verdict, not production code |
| `onboarding` | Bootstrap agent/engineer context — recon codebase, produce AGENTS.md |

### Standards & Governance

| Skill | Description |
|---|---|
| `language-standards` | Consistent declared language across artifacts — code, commits, PRs, skills |
| `rule-manager` | AGENTS.md/.cursorrules authoring, validation, and enforcement |
| `git-workflow` | Branch, commit, PR, merge — generic source control workflow |
| `adr` | See Domain Architecture above |

### Native AI Ecosystem

| Skill | Description |
|---|---|
| `native-ai-engineer` | Layer placement, runtime boundary, contract authoring for ai-native systems |
| `native-ai-runtime-agent` | Runtime agent operations in ai-native-fw product adapters |
| `native-ai-runtime-ops` | Ops for AI-native canonical runtime hosts |

### Roles

| Skill | Description |
|---|---|
| `master-engineer` | Senior Software Engineer — system design, architecture decisions, over-engineering checks |
| `product-manager` | PRD authoring, acceptance criteria, task breakdown, Jira-ready specs |
| `diagram-architect` | Architecture diagrams — SVG, Excalidraw, Mermaid, system/context/component level |

---

## Full Delivery Loop

```
spec-workflow          ← input quality gate (spec before code)
    ↓
new-feature-workflow   ← team process (design → implement → submit)
    ↓
code-review-workflow   ← output quality gate (before merge)
    ↓
deployment-workflow    ← deploy gate (before prod)
```

With meta-skills:
```
workflow-router        ← auto-detect: bug? feature? review? deploy?
role-switcher          ← auto-compose: which lenses for this task?
```

---

## Distributed Systems Coverage

```
Monolith layer:
  domain-driven-design → ports-and-adapters → design-patterns

Distributed layer:
  service-design → api-contract → event-driven-design

Frontend layer:
  micro-frontend (module federation, shell contract, CSS isolation)

Observability layer:
  observability-design (logs + metrics + traces, four golden signals)
```

---

## Inheritance Pattern (Skill Adapters)

Extend public skills for team-specific context:

```yaml
# ~/.hermes/profiles/<team>/skills/<team>/arbiter-git-workflow/SKILL.md
---
name: arbiter-git-workflow
type: skill-adapter
extends: puterakahfi/ai-native-skills@git-workflow
---
# Override only what's team-specific. Base skill handles invariant behavior.
```

---

## Contract Traceability

Every skill implements a contract in [ai-native-core](https://github.com/puterakahfi/ai-native-core):

```
skills/domain-driven-design/SKILL.md
  implements: ai-native-core/contracts/skills/domain-architecture/domain-driven-design.contract.yaml

skills/workflow-router/SKILL.md
  implements: ai-native-core/contracts/skills/domain-architecture/workflow-router.contract.yaml
```

---

## Skill Evaluation

Test whether skills are actually applied vs loaded-and-ignored:

```bash
# run eval against agent output
python ai-native-core/scripts/run-eval.py \
  --skill role-switcher \
  --output-file /tmp/agent-output.txt

# verdict: APPLIED | PARTIAL | GHOST
```

Test cases in `ai-native-core/contracts/tests/*.test.yaml`.

---

## Related

- [ai-native-core](https://github.com/puterakahfi/ai-native-core) — contracts (ports)
- [ai-native-fw](https://github.com/puterakahfi/ai-native-fw) — product runtime adapter
- [skills.sh](https://skills.sh) — open skills ecosystem standard
