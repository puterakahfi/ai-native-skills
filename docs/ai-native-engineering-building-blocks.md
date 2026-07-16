# AI-Native Engineering Building Blocks Coverage

This document maps the repository to the five AI-native engineering building blocks:

```text
Agent + Model + Methodology + Spec + Context
```

Use it to decide which capabilities are already covered, which gaps are intentional, and which contracts/skills should be implemented next.

## Summary

| Block | Meaning | Current coverage | Status | Main gap |
|---|---|---|---|---|
| Agent | The hand: active participant that uses tools and changes systems | `native-ai-runtime-agent`, `native-ai-runtime-ops`, `hermes-profile-bootstrap`, `workflow-router`, `role-switcher` | Partial | execution/tool governance |
| Model | The brain: cognitive capability and reasoning resource | `model-selection`, `ai-system-design`, `skill-eval`, `prompt-optimizer` | Emerging | routing/capability matrix/evals |
| Methodology | The path: lifecycle and quality process | `product-development-workflow`, workflows, `business-value-alignment`, TDD, debugging, review, deployment, refactoring | Strong | compliance gates and human review policy |
| Spec | The what: intent, contracts, architecture constraints | `business-value-alignment`, `product-requirements`, `spec-workflow`, contracts, `api-contract`, ADR, product/design skills | Strong | traceability and acceptance verification |
| Context | The how: instructions, knowledge, guardrails | `context-engineering`, `context-manager`, `rule-manager`, `response-contract` | Partial | hierarchy, freshness, security |

## Agent

### Covered

- `native-ai-runtime-agent` — runtime agent behavior and product adapter boundary.
- `native-ai-runtime-ops` — canonical runtime host operations.
- `hermes-profile-bootstrap` — Hermes profile skeleton and skill preset adapter.
- `workflow-router` / `role-switcher` — request routing and role composition, including product-from-zero versus existing UI/UX refinement routing.

### Gaps

- agent execution contract: plan/act/verify/report loop
- tool permission policy: safe/risky/forbidden tools and approval boundaries
- multi-agent handoff protocol: delegate, verify, merge, report
- runtime capability manifest: which tools/capabilities this profile actually has

### Candidate additions

- `agent-execution-contract`
- `tool-permission-policy`
- `agent-capability-manifest`
- `multi-agent-orchestration`

## Model

### Covered

- `model-selection` — selects abstract model class by task intent, risk, capabilities, context, fallback, and verification.
- `ai-system-design` — designs AI systems with evals/fallbacks/context budgets.
- `skill-eval` — verifies whether a skill was actually applied.
- `prompt-optimizer` / `response-contract` — improves prompt and response structure.

### Gaps

- concrete model routing policy per Hermes profile
- model capability matrix and model registry
- model eval suites per task class
- cost/latency telemetry and routing feedback
- privacy-aware hosted-vs-local policy

### Candidate additions

- `model-routing-policy`
- `model-capability-matrix`
- `model-evaluation`
- `model-risk-governance`

## Methodology

### Covered

- `spec-workflow`
- `product-development-workflow`
- `new-feature-workflow`
- `bugfix-workflow`
- `code-review-workflow`
- `deployment-workflow`
- `redesign-workflow`
- `test-driven-development`
- `systematic-debugging`
- `refactoring`
- `plan`
- `spike`

### Gaps

- workflow compliance checking: prove phases were followed
- human review gate: when approval is mandatory
- methodology selection matrix beyond current router behavior; current router now covers product-from-zero and existing UI/UX refinement, but compliance evidence is still separate

### Candidate additions

- `workflow-compliance-check`
- `human-review-gate`
- `methodology-router-contract`

## Spec

### Covered

- `spec-workflow`
- `business-value-alignment` — aligns work to user/business value, metrics, assumptions, risks, and a continue/narrow/experiment/stop verdict before execution.
- `product-requirements`
- `api-contract`
- `adr`
- `product-manager`
- `decision-making`
- `data-modeling`
- `domain-driven-design`
- `ports-and-adapters`
- Native AI Core `.contract.yaml` files

### Gaps

- spec traceability: requirement → task → code → test → verification
- acceptance criteria verification: what evidence proves acceptance criteria
- spec versioning and migration
- spec-to-context bridge: what enters context vs stays as source docs

### Candidate additions

- `acceptance-criteria-verification`
- `spec-traceability`
- `spec-versioning`
- `spec-context-bridge`

## Context

### Covered

- `context-engineering`
- `context-manager`
- `rule-manager`
- `response-contract`
- `language-standards`
- `onboarding`
- `security-review`
- `threat-modeling`

### Gaps

- context source hierarchy: SOUL.md vs AGENTS.md vs README vs memory vs session vs external docs
- context freshness policy: when source must be re-read
- context security guardrails: untrusted context, prompt injection, secrets redaction
- context packaging: profile context vs product context vs repo context
- institutional knowledge lifecycle: memory vs skill vs docs vs rules

### Candidate additions

- `context-source-hierarchy`
- `context-freshness-policy`
- `context-security-guardrails`
- `context-packaging`
- `institutional-knowledge-management`

## Priority Roadmap

1. **P0 — Model block**
   - Implemented first: `model-selection` contract + skill.
   - Next: `model-routing-policy` for concrete profile routing.
2. **P1 — Agent control block**
   - Add `agent-execution-contract` and `tool-permission-policy`.
3. **P2 — Spec verification**
   - Add `acceptance-criteria-verification` and `spec-traceability`.
4. **P3 — Context governance**
   - Add `context-source-hierarchy`, `context-security-guardrails`, and `context-freshness-policy`.

## Maintenance Rule

When adding a skill or contract, update this map if it changes coverage for one of the five blocks.
