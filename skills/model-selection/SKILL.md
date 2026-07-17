---
name: model-selection
description: Select model class for AI-native engineering tasks. Use when choosing between fast, reasoning, coding-agent, vision, or local/private models based on task intent, risk, capabilities, context, cost, latency, fallback, and verification needs.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/runtime/model-selection.contract.yaml
  ai-native-skills.contract-version: "~0.1"
  ai-native-skills.related_skills: '[''ai-system-design'', ''skill-eval'', ''threat-modeling'', ''architecture-review'', ''native-ai-runtime-agent'']'
---

# Model Selection

## Overview

Use this skill to choose the right **model class** before doing AI-native engineering work.

The model is the **brain** in the AI-native engineering stack. Do not pick a model from habit, price, hype, or the current default. Pick it from the task's intent, risk, required capabilities, context constraints, fallback path, and verification burden.

This skill implements the runtime-agnostic contract:

```text
ai-native-core/contracts/skills/runtime/model-selection.contract.yaml
```

## When to Use

Use when the task involves:

- selecting a model/provider/agent for coding, review, design, QA, security, architecture, or summarization
- routing subtasks to different model classes
- defining a Hermes profile's model policy or fallback policy
- deciding whether a task needs a reasoning model, coding agent, vision model, or local/private model
- checking whether the current model is strong enough for the requested risk level
- explaining cost/latency/quality tradeoffs

Do not use for:

- purely deterministic shell/file operations with no model choice
- product feature design where the model is already mandated by a higher-level spec
- benchmarking a concrete model in depth; use eval tooling plus `skill-eval` for that

## Decision Order

Always decide in this order:

1. **Classify task intent.** Completion: one of `chat`, `summarization`, `coding`, `architecture`, `security`, `design`, `debugging`, `review`, `vision`, `ops`, or `research` is named.
2. **Classify task risk.** Completion: risk is `low`, `medium`, `high`, or `critical` with one sentence explaining impact if wrong.
3. **List required capabilities.** Completion: capabilities are explicit: `tool-use`, `repo-editing`, `long-context`, `vision`, `reasoning`, `privacy`, `speed`, `low-cost`, `structured-output`, or `multi-agent`.
4. **Check context constraints.** Completion: sensitive data, untrusted context, freshness, and context-window pressure are noted.
5. **Pick a model class.** Completion: one primary class and one fallback class are selected.
6. **Define verification.** Completion: verification depth matches risk; high-risk work has tests/review/evals, not just answer plausibility.
7. **State tradeoff.** Completion: cost/latency/quality/privacy tradeoff is explicit.

## Model Classes

| Class | Use when | Avoid when |
|---|---|---|
| `fast_general` | Low-risk chat, small summaries, routing, classification | Architecture, security, repo edits, irreversible actions |
| `reasoning` | Architecture, root cause debugging, security, cross-file planning, high-stakes decisions | Cheap bulk transforms or latency-critical chat |
| `coding_agent` | Multi-file repo edits, TDD, refactors, PR review, tool-heavy implementation | No repo/tool context or no write permission |
| `vision` | Screenshots, UI review, diagram analysis, image-grounded QA | Text-only tasks |
| `local_private` | Sensitive/offline context, private code, low external-data tolerance | Tasks where local model cannot satisfy reasoning/quality requirements |

## Routing Rules

### Coding and repo edits

Use `coding_agent` when the agent must inspect files, edit code, run tests, or commit/push. If the coding change is architecturally risky, pair it with `reasoning` for planning/review.

Completion criterion: repo-changing work has real tool verification, not just model explanation.

### Architecture and system design

Use `reasoning` for architecture tradeoffs, boundary decisions, contracts, and migration plans. Use `fast_general` only for formatting or summarizing already-decided architecture.

Completion criterion: output includes alternatives, tradeoffs, constraints, and verification gates.

### Security and privacy

Use `reasoning` or specialized security review for auth, secrets, threat modeling, prompt injection, data exposure, and destructive operations. If sensitive context is present, prefer `local_private` unless its capability is insufficient.

Completion criterion: privacy constraints override cost/latency preferences.

### Visual/UI work

Use `vision` when the source of truth is a screenshot, mockup, diagram, image, or visual QA output. Pair with design/reasoning if the task requires redesign decisions.

Completion criterion: visual claims are grounded in inspected pixels or provided image context.

### Bulk low-risk work

Use `fast_general` for low-risk extraction, classification, formatting, and summaries when mistakes are easy to detect and cheap to fix.

Completion criterion: user-facing result is still checked for formatting and stated constraints.

## Output Format

When applying this skill explicitly, respond with:

```text
MODEL SELECTION
Task intent: <intent>
Risk: <low|medium|high|critical> — <why>
Required capabilities: <list>
Context constraints: <list>
Selected class: <fast_general|reasoning|coding_agent|vision|local_private>
Fallback class: <class or human escalation>
Tradeoff: <cost/latency/quality/privacy>
Verification: <what proves the answer/work is correct>
```

For long tasks, include this as a short preflight before execution. Do not let the preflight replace the actual work.

## Hermes Profile Mapping

A Hermes profile should map these abstract classes to concrete configured providers/models or external coding agents. Keep provider names in profile config, not in the core contract.

Example policy shape:

```yaml
model_policy:
  fast_general: <profile-defined>
  reasoning: <profile-defined>
  coding_agent: <codex|claude-code|opencode|profile-defined>
  vision: <profile-defined>
  local_private: <profile-defined>
```

Do not commit API keys, tokens, or local-only credentials in the policy.

## Common Pitfalls

1. **Default-model bias.** Using the current default for every task ignores risk and capability mismatch.
2. **Cheap model on expensive mistake.** Saving cents on model cost can create hours of debugging or unsafe changes.
3. **Reasoning model for everything.** Strong models are not always the best for cheap, low-risk transforms.
4. **No fallback.** If the selected model is unavailable, overloaded, or lacks a tool/vision capability, the run must fail closed or route to fallback.
5. **Ignoring privacy.** Sensitive context changes the model class decision even if a hosted model is stronger.
6. **Skipping verification.** Model selection is incomplete until the verification burden is explicit.
7. **Claiming unsupported capability.** Do not say a model can see images, edit repos, or use tools unless the runtime actually provides that capability.

## Verification Checklist

- [ ] Task intent is classified.
- [ ] Task risk is stated.
- [ ] Required capabilities are explicit.
- [ ] Context sensitivity and freshness are considered.
- [ ] Selected model class matches task risk and capability needs.
- [ ] Fallback class or human escalation exists.
- [ ] Cost/latency/quality/privacy tradeoff is stated.
- [ ] Verification depth matches risk.
- [ ] Provider-specific names are kept in runtime/profile config, not the core contract.
