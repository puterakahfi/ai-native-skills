---
name: ai-system-design
description: Design AI-powered systems — RAG architecture, agent memory patterns, LLM eval framework, prompt injection defense, human-in-the-loop, graceful degradation, and context window budget management.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/domain-architecture/ai-system-design.contract.yaml
  ai-native-skills.related_skills: "['native-ai-engineer', 'service-design', 'observability-design', 'ethics-responsible-ai', 'threat-modeling']"
---

# AI System Design

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
