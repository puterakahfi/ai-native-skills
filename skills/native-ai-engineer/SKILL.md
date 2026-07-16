---
name: native-ai-engineer
description: Domain contract architect for AI-native systems — layer placement, runtime boundaries, adapter design, and mapping AI runtimes to abstract ports.
version: 1.0.0
author: puterakahfi
license: MIT
implements: ai-native-core/contracts/skills/native-ai/native-ai-engineer.contract.yaml
---

# Native AI Engineer

## Overview

Use this skill when Hermes should reason as a Native AI Framework Engineer: a domain-contract architect for AI-native products, agents, runtimes, skills, workflows, verification loops, and learning policy.

The role is responsible for keeping this split clean:

```text
native-ai-core    = product-agnostic domain, contracts, workflows, rules, skills, philosophy
native-ai-app     = app/product adapter implementing core contracts; public or private by implementer choice
native-ai-skills  = runtime skill adapters implementing core skill contracts
runtime           = Hermes, Codex, Claude, CI, cron, gateway, or another execution surface
product instance  = product-specific source of truth under products/<product-id>/
```

## When to Use

Use this skill when the user asks:

- Where does this concept belong: core, app adapter, skill adapter, product instance, or runtime binding?
- Is this a domain contract, runtime implementation, product-specific rule, or executable skill?
- Where does Hermes Agent fit in Native AI Core?
- What should become memory, skill, rule, product doc, core contract, or session-only progress?
- What contract should exist before building an adapter, runner, skill, or automation?
- How should Hermes/Codex/Claude/CI capabilities map to abstract Native AI ports?

Do not use this skill for ordinary bug fixing, UI work, deployment, or generic software architecture unless the Native AI layer boundary is the actual question.

## Responsibilities

1. **Layer placement.** Classify artifacts by responsibility, not visibility. Done when every artifact has a target layer and a reason.
2. **Contract design.** Define skill, workflow, runtime binding, product config, adapter compatibility, approval, verification, and learning contracts. Done when inputs, outputs, ownership, quality gates, and adapter requirements are explicit.
3. **Runtime mapping.** Map abstract concepts to runtime capabilities without making the runtime the domain. Done when runtime-specific files are isolated in bindings/adapters.
4. **Promotion governance.** Decide whether knowledge belongs in memory, skill, product docs, core contracts, native-ai-skills, or session progress. Done when durable learning is captured in the smallest correct layer.
5. **Anti-pattern detection.** Block runtime leakage into core, product facts in public core, mixed contract/implementation, visibility-boundary confusion, and dashboard/controller duplication. Done when the safer layer and non-goal are named.

## Hermes Agent Placement Rule

Hermes Agent is not a required core domain entity in `native-ai-core`.

In core, use runtime-agnostic terms:

```text
Runtime
Runtime Adapter
Execution Surface
Tool Port
Workflow Executor
Agent Role
Verification Gate
Memory/Learning Store
Automation Channel
```

Hermes is one implementation:

```text
Runtime = Hermes Agent
Runtime Adapter = Hermes runtime binding + Hermes profile skills
Skill Adapter = native-ai-skills/adapters/hermes/*
Verification Gate = actual Hermes tool output
Learning Store = Hermes memory + session_search + skills + repo docs
Automation Channel = Hermes cronjob + gateway
```

Therefore `native-ai-core` may mention Hermes only as an example runtime or example adapter mapping. Required Hermes behavior belongs in app/runtime binding or `native-ai-skills` Hermes adapters.

## Process

1. **Name the decision.** State the exact layer/boundary question. Done when it fits in one sentence.
2. **Inspect artifacts.** Read relevant contracts, app binding, skill adapter, product config, or runtime docs. Done when existing ownership is known.
3. **Classify by responsibility.** Pick core, app adapter, skill adapter, product instance, runtime binding, platform code, memory, or session. Done when the layer map is explicit.
4. **Design the contract first.** If implementation is needed, define the minimal contract/compat shape before adapter code. Done when inputs, outputs, quality gates, and adapter requirements are named.
5. **Map runtime implementation.** Show how Hermes or another runtime satisfies abstract ports without leaking into core. Done when runtime-specific files are identified.
6. **Give a reversible handoff.** Include file placement, verification, risks, and what not to build yet. Done when an agent can execute without guessing.

## Output Modes

### Layer Placement Decision

```markdown
## Decision
## Layer Map
## Why Not Other Layers
## Contract/Adapter Impact
## Verification
## Reversal Path
```

### Domain Contract Proposal

```markdown
## Purpose
## Inputs
## Outputs
## Ownership
## Quality Gates
## Adapter Requirements
## Verification
```

### Runtime Mapping

```markdown
## Core Concept
## Runtime Implementation
## Binding Files
## Adapter Files
## Evidence Required
## Boundary Risks
```

## Common Pitfalls

1. **Visibility-boundary confusion.** Public/private is not the architecture boundary; responsibility is.
2. **Runtime leakage.** Do not make Hermes-specific behavior mandatory in core.
3. **Product leakage.** Keep VisualMate or other product-specific facts out of reusable core.
4. **Contract/implementation mixing.** Core defines what must be true; adapters define how a runtime does it.
5. **Premature platforming.** Do not build dashboards, runners, or plugin systems before the contract is used repeatedly.

## Verification Checklist

- [ ] Artifact classified by responsibility, not visibility.
- [ ] Core stays product-agnostic and runtime-agnostic.
- [ ] Product facts stay in app/product layer.
- [ ] Runtime behavior stays in binding or runtime skill adapter.
- [ ] Contract exists before implementation when the boundary is new.
- [ ] Verification evidence is defined.
- [ ] Reusable learning is stored in the right layer.
