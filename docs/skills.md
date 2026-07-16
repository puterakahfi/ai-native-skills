# Skills Taxonomy

This document defines the official skill categories used in `ai-native-skills` while staying compatible with the [Agent Skills specification](https://agentskills.io/specification).

The goal is to keep skill authoring decisions consistent: when to create an atomic skill, when to create a workflow, and when to create a meta-skill that routes or composes other skills.

Current repository inventory:

- `skill`: 65
- `workflow`: 6
- `meta-skill`: 2
- Total executable skills: 73

---

## Official Types

Agent Skills standard frontmatter only allows `name`, `description`, `license`, `compatibility`, `allowed-tools`, and `metadata`. Repository-specific classification therefore lives in namespaced metadata keys such as `ai-native-skills.type` rather than a top-level `type:` field.

`ai-native-skills` currently uses three official category values:

| Type | Primary job | Answers | Examples |
|---|---|---|---|
| `skill` | Provide a reusable capability | “What capability or expert lens is needed?” | `systematic-debugging`, `accessibility`, `master-design` |
| `workflow` | Run a sequenced task lifecycle | “What phases must this task follow?” | `bugfix-workflow`, `deployment-workflow`, `redesign-workflow` |
| `meta-skill` | Route or compose other skills/workflows | “Which skills/workflows should be loaded?” | `workflow-router`, `role-switcher` |

Do not introduce a new category value unless the README, this document, and existing tooling are updated together.

---

## `skill`

A `skill` is an atomic, reusable capability or expert lens.

Use `metadata["ai-native-skills.type"]: skill` when the artifact teaches the agent how to perform one coherent capability with quality gates, examples, pitfalls, and verification criteria.

### Use when

- The behavior is reusable across multiple workflows.
- The domain is specific enough to have its own principles, checks, and failure modes.
- The skill can be loaded directly by a user or composed by a workflow.
- The output is a decision, review, artifact, implementation guidance, or quality gate result.

### Do not use when

- The artifact primarily defines a multi-phase lifecycle. Use `workflow`.
- The artifact primarily chooses which other skills to load. Use `meta-skill`.
- The artifact is product-specific configuration. Put it in the product/app adapter layer.
- The artifact is only a temporary project note. Keep it out of `skills/`.

### Required behavior

A good `skill` should define:

1. **Trigger.** When the agent should load it.
2. **Scope.** What it does and does not own.
3. **Procedure.** Steps, heuristics, or decision rules.
4. **Quality gates.** How the agent knows the skill was applied correctly.
5. **Pitfalls.** The common ways agents misuse the capability.
6. **Verification.** Checkable evidence before claiming completion.

### Examples

- `systematic-debugging` — root-cause investigation discipline.
- `accessibility` — WCAG-oriented UI quality gate.
- `master-design` — senior product design lens.
- `copywriting` — product messaging capability.
- `native-ai-engineer` — Native AI layer-boundary and contract reasoning.

---

## `workflow`

A `workflow` is a sequenced execution process for a task class.

Use `metadata["ai-native-skills.type"]: workflow` when the main value is the ordering of phases, gates, and handoffs. A workflow may compose many skills, but the workflow itself owns the lifecycle.

### Use when

- The task has a required order of operations.
- Skipping or reordering phases creates quality risk.
- The workflow has explicit phase gates before moving forward.
- The output is a completed lifecycle: fix, feature, review, deployment, redesign, or spec.

### Do not use when

- The artifact is just one capability or expert lens. Use `skill`.
- The artifact only routes to other workflows. Use `meta-skill`.
- The phases are optional notes rather than enforced gates.
- The process is product-specific and not reusable.

### Required behavior

A good `workflow` should define:

1. **Entry condition.** When this workflow applies.
2. **Phases.** Ordered steps with completion criteria.
3. **Composed skills.** Which skills are loaded or consulted in each phase.
4. **Gates.** What blocks progress to the next phase.
5. **Evidence.** Tool output, files, tests, screenshots, or review artifacts required before completion.
6. **Exit condition.** What “done” means for the whole lifecycle.

### Current workflows

| Workflow | Lifecycle |
|---|---|
| `spec-workflow` | constitution → specify → plan → tasks → implement |
| `new-feature-workflow` | plan → design → implement → verify → submit → review |
| `bugfix-workflow` | reproduce → investigate → fix → verify → submit → review |
| `code-review-workflow` | load-context → architecture-check → design-check → logic-check → verdict |
| `deployment-workflow` | pre-deploy → context-load → deploy → health-verify → confirm/rollback |
| `redesign-workflow` | audit → spec → prototype → design-review gates → iterate → deliver |

---

## `meta-skill`

A `meta-skill` routes, selects, or composes other skills and workflows.

Use `metadata["ai-native-skills.type"]: meta-skill` when the artifact’s job is not to perform the domain work directly, but to decide which capabilities should be loaded and in what combination.

### Use when

- The input is a broad user request and the correct workflow is not yet known.
- The agent must classify intent before execution.
- The artifact composes multiple role lenses or workflows.
- The output is a routing decision, loading plan, or execution path.

### Do not use when

- The artifact performs the actual task lifecycle. Use `workflow`.
- The artifact teaches one domain capability. Use `skill`.
- The routing logic is product-specific configuration rather than reusable repo logic.

### Required behavior

A good `meta-skill` should define:

1. **Detection rules.** How to classify the user request.
2. **Routing map.** Which workflow or skills correspond to each intent.
3. **Composition rules.** Which skills can be combined safely.
4. **Conflict handling.** What to do when multiple routes match.
5. **Handoff.** What the selected workflow/skills should receive as context.
6. **Non-execution boundary.** Where routing ends and task execution begins.

### Current meta-skills

| Meta-skill | Responsibility |
|---|---|
| `workflow-router` | Detect task type — bug, feature, review, deploy, spike — and route to the correct workflow. |
| `role-switcher` | Detect user intent and compose expert role lenses, such as design + UX psychology + product management. |

---

## Adapter Pattern

`skill-adapter` is currently a pattern, not an official category value in this repository.

The README previously described `skill-adapter` as a taxonomy item, but no current `SKILL.md` uses `metadata["ai-native-skills.type"]: skill-adapter`. Adapter behavior is represented through:

- `metadata["ai-native-skills.implements"]`, linking a skill to a Native AI Core contract.
- `compat/*.compat.yaml`, describing compatibility between runtime skill implementations and core contracts.
- Product or runtime bindings that install or load the skill in a specific execution context.

### Definition

A skill adapter is a skill that implements, extends, or binds an external/core contract for a specific runtime, product, or execution context.

In practice, it remains executable as a normal `skill` unless the repo formally introduces `type: skill-adapter` later.

### Examples

These are adapter-like skills because they implement Native AI Core contracts while remaining `metadata["ai-native-skills.type"]: skill`:

- `native-ai-engineer`
- `native-ai-runtime-agent`
- `native-ai-runtime-ops`

### When to use the adapter pattern

Use `metadata["ai-native-skills.type"]: skill` plus adapter metadata when:

- The skill implements a Native AI Core contract.
- A runtime binding needs to reference the executable skill.
- Compatibility needs to be validated through `compat/*.compat.yaml`.
- The behavior is still a concrete capability, not a router or lifecycle workflow.

---

## Decision Guide

| If you are creating... | Use |
|---|---|
| One reusable capability or expert lens | `metadata["ai-native-skills.type"]: skill` |
| A multi-phase lifecycle with gates | `metadata["ai-native-skills.type"]: workflow` |
| An intent router or skill composer | `metadata["ai-native-skills.type"]: meta-skill` |
| A runtime/product implementation of a core contract | `metadata["ai-native-skills.type"]: skill` + adapter pattern |
| A product-specific override | Product/app adapter layer, not this repo by default |
| A temporary idea or scratch note | Do not put it in `skills/` |

---

## Frontmatter Contract

Every `SKILL.md` must be valid Agent Skills frontmatter. Keep standard fields at the top level and put repo-specific fields under namespaced `metadata` keys.

Top-level fields allowed by the Agent Skills spec:

- `name` — required, max 64 chars, lowercase/hyphenated, must match the skill directory name.
- `description` — required, max 1024 chars, explains what the skill does and when to use it.
- `license` — optional.
- `compatibility` — optional, max 500 chars, for environment requirements.
- `allowed-tools` — optional experimental field.
- `metadata` — optional extension map.

Basic skill example:

```yaml
---
name: example-skill
description: Short trigger-focused description.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
---
```

For Native AI contract-backed skills, include `metadata["ai-native-skills.implements"]`:

```yaml
---
name: native-ai-runtime-agent
description: Runtime agent skill for ai-native-fw product adapters.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/runtime-agent/native-ai-runtime-agent.contract.yaml
---
```

Validate compatibility with the Agent Skills reference validator:

```bash
skills-ref validate skills/<skill-name>
```

---

## Anti-patterns

1. **Calling everything a skill.** If phase order matters, create a workflow.
2. **Calling a router a workflow.** If it only selects another process, create a meta-skill.
3. **Creating product-specific base skills.** Product-specific behavior belongs in product/app adapters unless it is broadly reusable.
4. **Inventing a new category casually.** A new category value affects README, docs, validation, examples, and downstream consumers.
5. **Using adapter as a type before tooling supports it.** Keep adapter semantics in `metadata["ai-native-skills.implements"]` and `compat/` until the repo formally adopts `skill-adapter`.
6. **Writing no-op skills.** If the document does not change agent behavior or quality gates, it should not be a skill.
7. **Mixing routing and execution.** Meta-skills decide the route; workflows and skills perform the work.
