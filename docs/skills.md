# Skills Taxonomy

This document defines the official skill categories used in `ai-native-skills` while staying compatible with the [Agent Skills specification](https://agentskills.io/specification).

The goal is to keep authoring decisions consistent: when to create an atomic skill, when to create a workflow, and when to create a meta-skill that routes or composes other capabilities.

Current repository inventory:

- `skill`: 87
- `workflow`: 10
- `meta-skill`: 6
- Total executable skills: 103

---

## Official Types

Agent Skills frontmatter allows standard fields such as `name`, `description`, `license`, `compatibility`, `allowed-tools`, and `metadata`. Repository-specific classification therefore lives in namespaced metadata such as `metadata["ai-native-skills.type"]`.

`ai-native-skills` uses three official category values:

| Type | Primary job | Answers | Examples |
|---|---|---|---|
| `skill` | Provide one reusable capability | “What capability or expert lens is needed?” | `delivery-work-breakdown`, `implementation-context-discovery`, `systematic-debugging`, `collection-discovery-design`, `decision-provenance`, `project-instruction-generator`, `accessibility`, `chatgpt-app-development` |
| `workflow` | Run a sequenced lifecycle | “What phases and gates must this task follow?” | `bugfix-workflow`, `new-feature-workflow`, `redesign-workflow` |
| `meta-skill` | Route or compose capabilities | “Which workflow and specialists should be loaded?” | `workflow-router`, `role-switcher`, `design-layout` |

Do not introduce another category value unless README, this document, validation, examples, and downstream consumers are updated together.

---

## `skill`

A `skill` is an atomic, reusable capability or expert lens.

Use `metadata["ai-native-skills.type"]: skill` when the artifact teaches the agent how to perform one coherent capability with scope, procedure, quality gates, failure boundaries, and verification.

### Use when

- behavior is reusable across workflows;
- the domain is specific enough to have principles and evidence rules;
- it can be loaded directly or composed by a workflow;
- output is a decision, review, artifact, implementation guidance, or gate result.

### Do not use when

- the main value is a multi-phase lifecycle → use `workflow`;
- the artifact primarily chooses other capabilities → use `meta-skill`;
- the content is product-specific configuration → product/app adapter layer;
- it is a temporary project note → keep it out of `skills/`.

### Required behavior

A good skill defines:

1. trigger;
2. owned and delegated scope;
3. procedure and decision rules;
4. allowed outputs;
5. quality gates;
6. failure signals and evidence boundaries;
7. verification and workflow handoff.

### Examples

- `delivery-work-breakdown` — classify release units, work hierarchy, branch bases, PR targets, and epic acceptance before Git execution.
- `implementation-context-discovery` — inspect an existing repository before code, classify canonical framework/component/styling/icon/tooling systems, lock conventions, decide reuse/extension/composition/native/dependency, and hand off to implementation plus independent architecture review.
- `collection-discovery-design` — diagnose retrieval and discovery strategy before pagination, tabs, filtering, traversal, or disclosure adapters are selected.
- `project-instruction-generator` — generate or audit concise project-scoped bootstrap instructions that bind project identity and resources to reusable routing, disclosure, repository, completion, and capability-evolution policy.
- `systematic-debugging` — root-cause investigation discipline.
- `decision-provenance` — verify authority, source, scope, supersession, and conflict behind material decisions.
- `accessibility` — WCAG-oriented UI quality gate.
- `master-design` — senior product-design ownership.
- `business-value-alignment` — value and metric alignment before execution.
- `experiment-design` — minimum viable experiment before PRD/MVP/build.
- `copywriting` — product messaging capability.
- `native-ai-engineer` — Native AI layer and contract reasoning.
- `chatgpt-app-development` — Apps SDK/MCP product boundary, cost ownership, tool/widget/auth/security, and release discipline.

### Stable domain versus adapters

A skill should own a stable decision domain, not one replaceable implementation name.

```text
implementation-context-discovery
  stable domain:
    repository evidence, canonicality, convention locks,
    reuse/extension/dependency decisions

  discovered product adapters:
    Next.js, React, shadcn/ui, Tailwind CSS, Lucide,
    or any other actual repository choices
```

Do not create a universal `shadcn-skill`, `lucide-skill`, or framework-specific redesign workflow merely to preserve product conventions. Product libraries are evidence inside implementation-context discovery unless platform-specific knowledge itself is the stable reusable capability.

---

## `workflow`

A `workflow` is a sequenced execution process for a task class.

Use `metadata["ai-native-skills.type"]: workflow` when the main value is the ordering of phases, gates, evidence, and handoffs. A workflow may compose many skills, but owns the lifecycle.

### Use when

- order matters and skipping phases creates risk;
- phase gates control progress;
- evidence and exit conditions are explicit;
- output is a completed lifecycle: feature, fix, review, deployment, redesign, refinement, product delivery, or spec.

### Required behavior

A good workflow defines:

1. entry condition and routing boundary;
2. ordered phases;
3. loaded capabilities per phase;
4. blocking gates;
5. evidence and authority requirements;
6. state transitions and correction routes;
7. exit and delivery conditions.

### Current workflows

| Workflow | Lifecycle |
|---|---|
| `spec-workflow` | constitution → specify → plan → tasks → implement |
| `new-feature-workflow` | plan → delivery topology → architecture/design decision → implementation-context discovery → implement → verify → submit → review |
| `bugfix-workflow` | reproduce → investigate → fix → verify → submit → review |
| `code-review-workflow` | load context → architecture → design → logic → security → verdict/authorization |
| `deployment-workflow` | pre-deploy → context-load → deploy → health-verify → confirm/rollback |
| `redesign-workflow` | route → owners → inspect → direction → layered plan → implementation-context mapping → produce → verify → architecture/design review → fix → deliver |
| `product-development-workflow` | discovery → PRD → MVP/release-unit decomposition → spec → implementation → verification → release → deploy → launch → learn |
| `design-refinement` | verified finding → lock/budget → implementation-context mapping → smallest patch → verify → focused review → deliver |
| `skill-doctor` | audit → triage → repair → verify |
| `skill-evolution` | observe verified product learning → diagnose reusable gap → apply minimal skill/workflow/eval/core patch → validate → promote |

A workflow should load `implementation-context-discovery` only when existing-repository code production or material implementation mapping is in scope. Pure static visual artifacts may mark it `NOT_APPLICABLE`.

---

## `meta-skill`

A `meta-skill` routes, selects, or composes other skills and workflows.

Use `metadata["ai-native-skills.type"]: meta-skill` when the artifact’s job is to decide which capabilities should be loaded and how they combine, rather than perform the domain work directly.

### Required behavior

A good meta-skill defines:

1. intent and domain detection;
2. routing map;
3. composition and ownership rules;
4. conflict handling;
5. handoff contract;
6. non-execution boundary.

### Current meta-skills

| Meta-skill | Responsibility |
|---|---|
| `workflow-router` | Select one primary lifecycle and applicable platform/domain overlays. |
| `role-switcher` | Assign one owner, narrow specialists, independent reviewers, and domain reviewers. |
| `design-layout` | Route macrostructure, component strategy, responsiveness, and spacing. |
| `design-visual` | Route visual direction, composition, hierarchy, type, color, depth, iconography, motion, and readability. |
| `design-strategy` | Route psychology, information architecture, collection discovery, CRO, copy, and content. |
| `design-interaction` | Route interaction patterns, states, behavior, and accessibility semantics. |

A platform or repository specialist normally overlays an existing lifecycle rather than replacing it.

```text
ChatGPT App product from zero
  primary lifecycle: product-development-workflow
  platform specialist: chatgpt-app-development

Existing product adds ChatGPT integration
  primary lifecycle: new-feature-workflow
  platform specialist: chatgpt-app-development

Repository-backed redesign or feature
  lifecycle remains redesign/new-feature/refinement
  pre-code specialist: implementation-context-discovery
```

---

## Adapter Pattern

`skill-adapter` is a pattern, not an official type value.

Adapter behavior is represented through:

- `metadata["ai-native-skills.implements"]`, linking to a Native AI Core contract;
- `metadata["ai-native-skills.contract-version"]`;
- reviewed boundary declarations when the contract boundary is non-empty;
- `compat/*.compat.yaml` when explicit compatibility evidence is required;
- product/runtime bindings that install or compose the skill.

Contract-backed adapters remain an ordinary `skill`, `workflow`, or `meta-skill`.

Examples:

- `delivery-work-breakdown`;
- `implementation-context-discovery`;
- `collection-discovery-design`;
- `native-ai-engineer`;
- `native-ai-runtime-agent`;
- `native-ai-runtime-ops`;
- `decision-provenance`.

A platform-specific reusable capability such as `chatgpt-app-development` may remain a normal skill without `implements` metadata when no stable runtime-agnostic contract exists. Do not invent a core contract only for classification.

### Adapter boundary example

```text
implementation-context-discovery
  owns:
    repository ecosystem discovery
    canonicality and convention locks
    reuse/extension/composition/native/dependency decisions
    evidence-backed implementation mapping

  delegates:
    actual feature implementation
    architecture acceptance
    product-specific approval
```
