---
name: ai-system-design
description: Design AI-powered systems — RAG architecture, agent memory patterns, LLM eval framework, prompt injection defense, human-in-the-loop, graceful degradation, and context window budget management.
license: MIT
metadata:
  ai-native-skills.version: 1.0.1
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/architecture/ai-system-design.contract.yaml
  ai-native-skills.contract-version: "~0.1"
  ai-native-skills.related_skills: "['native-ai-engineer', 'service-design', 'observability-design', 'ethics-responsible-ai', 'threat-modeling']"
---

# AI System Design

## Reviewed core contract interface

Source: `ai-native-core/contracts/skills/architecture/ai-system-design.contract.yaml` · compatible line: `~0.1`

```yaml
required_inputs:
- ai_feature_description
allowed_outputs:
- ai_system_architecture
- rag_design
- agent_memory_design
- eval_framework
- fallback_strategy
- prompt_injection_defense
- human_in_the_loop_design
quality_gates:
- fallback_must_be_designed_for_model_failure_or_hallucination
- prompt_injection_defense_must_be_explicit
- eval_framework_must_exist_before_production_deploy
- human_in_the_loop_must_be_defined_for_high_stakes_decisions
- context_window_budget_must_be_planned
- rag_retrieval_quality_must_be_measurable
- ai_feature_must_degrade_gracefully_not_fail_silently
- data_privacy_in_llm_context_must_be_audited
```

Production approval requires an eval_framework before deploy, measurable RAG retrieval quality, an explicit fallback_strategy, and graceful degradation instead of silent failure. High-stakes paths must define human-in-the-loop ownership.

Keep this interface synchronized with the pinned core contract. Exact declarations make ownership reviewable; they do not replace runtime, repository, architecture, test, or product evidence.


> **HARD RULES:** Define failure modes before architecture. LLM is unreliable by default — design for graceful degradation. Every AI decision needs a non-AI fallback path.

## The Core Rule

```
An AI component is not a magic box. It is a service with:
  - Failure modes (hallucination, context overflow, latency spikes)
  - Trust boundaries (prompt injection vectors)
  - Quality metrics (eval scores, not just uptime)
  - Degradation paths (what happens when model is down or wrong?)

Design it like any other critical service — with fallbacks, evals, and observability.
```

---

## Design Areas

This skill is split across two reference files:

### Part 1 — RAG, Memory & Evals

Covers: RAG architecture and quality gates, chunking strategies, agent memory patterns,
LLM eval framework, and CI eval gates.

→ See `references/rag-and-eval.md`

### Part 2 — Safety, Operations & Checklist

Covers: prompt injection defense, human-in-the-loop design, graceful degradation patterns,
context window budget management, data privacy in LLM context, and the full pre-ship checklist.

→ See `references/safety-and-ops.md`

---

## Quick Reference

| Concern | Pattern | Reference |
|---|---|---|
| Domain knowledge drift | RAG | rag-and-eval.md |
| Agent persistence | Memory patterns | rag-and-eval.md |
| Behavioral regression | Eval suite + CI gate | rag-and-eval.md |
| Adversarial input | Prompt injection defense | safety-and-ops.md |
| High-stakes automation | Human-in-the-loop | safety-and-ops.md |
| Model failure | Graceful degradation | safety-and-ops.md |
| Token overrun | Context window budget | safety-and-ops.md |
| Data leakage | PII scrubbing | safety-and-ops.md |

**Gate:** Every AI call must have at least one fallback path before merging.
