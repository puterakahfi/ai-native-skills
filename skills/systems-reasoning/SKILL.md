---
name: systems-reasoning
description: Establish an implementation-independent model of a system before product, experience-design, domain, architecture, delivery, or implementation decisions. Use for ambiguous boundaries, shared capabilities, cross-component or cross-journey effects, abstraction design, adapter leakage risk, feedback loops, local optimization, and system-level trade-offs. Do not use deep modeling for bounded low-risk work with explicit consequences.
license: MIT
metadata:
  ai-native-skills.version: 0.2.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.requires: "decision-provenance systems-thinking"
  ai-native-skills.type: meta-skill
  ai-native-skills.role: foundational-overlay
  ai-native-skills.related_skills: '["workflow-router","product-manager","master-design","information-architecture","design-review","delivery-work-breakdown","implementation-context-discovery","architecture-review","test-strategy","production-code-quality-baseline","skill-eval","skill-evolution"]'
---

# Systems Reasoning

## Purpose

Model the system before designing the solution. Establish purpose, boundaries, actors, capabilities, relationships, invariants, dynamics, leverage points, trade-offs, evidence, and uncertainty before selecting mechanisms, experience patterns, adapters, frameworks, vendors, or tools.

`systems-reasoning` is a foundational overlay. It does not replace the one primary lifecycle selected by `workflow-router`, and it does not take ownership from product, experience design, domain, architecture, delivery, implementation, testing, review, or acceptance capabilities.

## Core rule

```text
system purpose and outcomes
→ environment, actors, and ownership
→ boundaries and dependencies
→ capabilities, policies, and invariants
→ relationships and system dynamics
→ leverage points, failure modes, and trade-offs
→ downstream lifecycle decisions
→ design or implementation mechanisms
→ adapter profiles
→ runtime and tool bindings
```

Never reason backward from an available framework, tool, UI pattern, reference-site structure, adapter, vendor, repository layout, or current implementation and present that mechanism as the canonical system definition.

A landing page, dashboard, hero, card grid, tabs, split layout, design system, architecture pattern, or provider schema is not automatically the capability or requirement. Treat it as a proposed mechanism until the governing downstream owner evaluates it against verified system and product context.

## Activate when

Use this skill when one or more apply:

- the system of interest or ownership boundary is ambiguous;
- a reusable capability must remain independent from adapters or products;
- a change crosses actors, journey stages, routes, products, components, repositories, services, teams, or lifecycle phases;
- local optimization may create system-level regressions;
- feedback loops, delays, bottlenecks, incentives, metric proxy failure, or emergent effects matter;
- product-experience or redesign work may alter positioning, information architecture, product proof, conversion strategy, reusable page shells, component families, design-system behavior, or downstream outcomes;
- architecture, decomposition, or visual structure is being selected before capabilities, invariants, tasks, content reality, and consequences are clear;
- the prompt is implementation- or pattern-heavy and risks tool-shaped or template-shaped reasoning;
- downstream skills need a shared normalized system model.

Do not activate for a bounded, low-risk task whose system, owner, invariants, locks, and consequences are already explicit. Use the LIGHT path when only one or two missing decisions require clarification.

## Required inputs

```yaml
user_request: required
objective_or_desired_outcome: required_or_discovered
governing_sources: required_when_available
known_context: optional
candidate_system_of_interest: optional
constraints: optional
evidence_refs: optional
```

Missing evidence is `NOT_VERIFIED`, not permission to invent boundaries, actors, dependencies, invariants, design proof, approvals, or completion state.

## Procedure

### 1. Establish execution depth

Classify the task:

```text
LIGHT      bounded task; one local decision; low consequence
STANDARD   multiple actors, boundaries, journey stages, or reusable abstraction
DEEP       cross-repository or cross-system change, high risk, strong dynamics, or conflicting authority
```

Use only the depth justified by complexity, reversibility, blast radius, uncertainty, and acceptance risk.

For product-experience or design work, also classify:

```yaml
systemic_design_applicability:
  status: REQUIRED | REDUCED | NOT_APPLICABLE | NOT_VERIFIED
  rationale: string
  activation_signals: []
  omitted_analysis_risk: []
```

`REQUIRED` and `REDUCED` do not make systems reasoning the primary workflow. They only determine whether the downstream design owner receives a system model.

### 2. Define the system of interest

State:

- the system name;
- intended purpose and observable outcomes;
- environment and external systems;
- owner and decision authority;
- what is explicitly outside the analysis.

If the system cannot be bounded from verified evidence, stop implementation or structural selection and return `NOT_VERIFIED` with the missing decisions.

### 3. Identify actors and relationships

Identify materially relevant actors, stakeholders, users, components, journey stages, external systems, and their relationships. Record ownership, dependency direction, exchanged value or information, and failure propagation where relevant.

Do not produce a component, page-section, or stakeholder inventory without explaining the important relationships.

### 4. Separate abstraction layers

Classify each material concept:

```text
capability      outcome the system must be able to produce
policy          rule governing permitted or required behavior
mechanism       one way to realize a capability or policy
adapter         translation between a canonical boundary and an external mechanism
runtime_binding concrete tool, provider, framework, process, or deployment binding
```

Experience patterns and visual structures are mechanisms. They may satisfy product and system constraints, but they must not redefine the canonical capability merely because they are common or requested.

Capabilities and policies may constrain downstream mechanisms. Mechanisms, adapters, and runtime bindings must not redefine the canonical capability unless higher-authority evidence explicitly changes the system contract.

### 5. Discover invariants, constraints, assumptions, and uncertainty

Record separately:

- invariants that must remain true across implementations or experience directions;
- constraints imposed by authority, environment, compatibility, safety, accessibility, brand, product, or delivery;
- assumptions that have not been verified;
- unresolved uncertainty and its effect on decisions.

### 6. Analyze dynamics proportionately

When material, trace:

- causal relationships;
- reinforcing and balancing feedback loops;
- delays and accumulation;
- bottlenecks and constraints;
- incentives and local optimizations;
- metric proxy failure and Goodhart risk;
- failure modes, unintended consequences, and emergent behavior.

Do not manufacture loops for a simple bounded task. For deep work, omission of material dynamics is a blocking gap.

Delegate deep dynamics to `systems-thinking` when reinforcing or balancing loops, emergence, second-order effects, Conway alignment, Goodhart risk, unintended consequences, or leverage-point analysis are material. Naming the skill is not execution evidence; an observable finding or decision is required.

### 7. Identify leverage points and trade-offs

Identify the smallest system-level interventions likely to improve the desired outcome. Record benefits, costs, reversibility, second-order effects, rejected alternatives, and residual risks.

Do not equate the most technically sophisticated or visually familiar intervention with the highest-leverage intervention.

For design work, test whether the leverage point is actually layout, positioning, content, proof, information architecture, interaction, onboarding, component-system reuse, or another journey intervention before selecting page structure.

### 8. Produce the normalized system model

Return the output contract below. Keep evidence, inference, assumption, review, approval, and acceptance distinct.

### 9. Produce a bounded design handoff when applicable

When the downstream consumer is `master-design`, `information-architecture`, a product-experience phase, or a redesign lifecycle, load `references/integration-and-handoffs.md` and produce only the material `systemic_design_context` fields.

The handoff may constrain or inform design. It must not select a hero, macrostructure, card system, component, visual genre, or interaction pattern on behalf of the design owner.

### 10. Hand off without taking lifecycle ownership

Provide only the fields needed by the selected downstream workflow or skill. Preserve one primary workflow. Experience direction, architecture, technology, and adapter selection occur downstream after the abstraction is stable enough for the decision being made.

## Output contract

```yaml
systems_reasoning:
  depth: LIGHT | STANDARD | DEEP
  status: PASS | NEEDS_WORK | PARTIALLY_COMPLETED | BLOCKED | NOT_VERIFIED | LIMITED | HANDED_OFF
  system_of_interest:
    name: string
    purpose: string
    desired_outcomes: []
    environment: []
    inside_boundary: []
    outside_boundary: []
    owner: string | NOT_VERIFIED
  actors_and_relationships:
    actors: []
    relationships: []
    dependency_direction: []
  abstraction_map:
    capabilities: []
    policies: []
    mechanisms: []
    adapters: []
    runtime_bindings: []
  invariants: []
  constraints: []
  dynamics:
    causal_relationships: []
    feedback_loops: []
    delays_or_accumulations: []
    bottlenecks: []
    failure_modes: []
    unintended_consequences: []
  leverage_points: []
  trade_offs: []
  rejected_alternatives: []
  evidence_refs: []
  inferences: []
  assumptions: []
  unresolved_uncertainty: []
  blocking_gaps: []
  downstream_handoff:
    primary_workflow: string | NOT_VERIFIED
    consumers: []
    required_next_decisions: []
    systemic_design_applicability: optional
    systemic_design_context: optional
```

LIGHT outputs may omit empty dynamics and design-handoff fields, but must still state the system, boundary, relevant invariant or constraint, decision, evidence state, and handoff.

## Product-experience and design boundary

When design context is material:

- `systems-reasoning` establishes the system, journey role, boundaries, actors, relationships, consequences, leverage, trade-offs, and evidence gaps;
- `systems-thinking` performs deep dynamics analysis when justified;
- `master-design` owns experience direction, candidate comparison, final synthesis, component strategy, interaction contracts, and engineering handoff;
- `information-architecture` owns structure, taxonomy, navigation, and findability;
- design specialists own their narrow domains;
- `implementation-context-discovery` verifies actual repository components, families, paths, imports, tokens, and conventions;
- `design-review` owns independent rendered or implemented acceptance.

A hero or conventional landing-page sequence may be correct. It is never mandatory merely because the artifact is a landing page.

## Quality gates

- The system of interest and desired outcome are explicit.
- Inside/outside boundaries and decision ownership are explicit or `NOT_VERIFIED`.
- Capabilities, policies, mechanisms, adapters, runtime bindings, and design patterns are not conflated.
- Material relationships and dependency directions are visible.
- Invariants, constraints, assumptions, and uncertainty are distinct.
- Dynamics analysis is proportionate to complexity and risk.
- Deep feedback-loop, emergence, second-order, Conway, Goodhart, unintended-consequence, and leverage analysis is delegated to `systems-thinking` when material.
- Leverage points and trade-offs precede implementation or structural selection.
- Framework-first, adapter-leakage, and template-shaped reasoning are rejected.
- Product-experience work does not force a universal hero or page recipe.
- Simple tasks are not inflated into ceremonial modeling.
- Complex tasks cannot bypass material boundary, invariant, relationship, and trade-off analysis.
- The output preserves one primary workflow and does not self-authorize design, implementation, merge, release, or product acceptance.
- A capability is claimed as applied only when it produces an observable system decision, model, finding, gate, or handoff.

## Stop and escalation conditions

Return `BLOCKED` or `NOT_VERIFIED` when:

- higher-authority sources conflict and decision provenance cannot resolve them;
- the system boundary or owner is required but cannot be established;
- a canonical capability change is being inferred from one adapter, implementation, UI pattern, or reference site;
- required evidence is unavailable;
- the task requires an RFC or approval outside the current authority;
- downstream implementation or design direction would prematurely lock an unverified abstraction;
- a requested metric cannot be connected to the intended user or system outcome without material proxy risk.

## Reference loading

Load only what the current concern requires:

- `references/abstraction-model.md` for terminology and abstraction hierarchy;
- `references/boundary-capability-analysis.md` for boundaries, actors, capabilities, invariants, and normalized examples;
- `references/dynamics-leverage-and-tradeoffs.md` for causal loops, delays, bottlenecks, failure modes, leverage points, and trade-offs;
- `references/integration-and-handoffs.md` for downstream composition, including product-experience and design handoffs;
- `references/anti-patterns-and-counterexamples.md` when detecting or correcting reasoning failures.

When product-experience or broad redesign work is active, the downstream design owner may also load `master-design/references/systemic-design-reasoning.md`.

## Completion

The skill is complete for a task only when its proportionate gates pass, blocking gaps are disclosed, the normalized output is reviewable, and downstream ownership is explicit. Missing evidence remains `NOT_VERIFIED`.
