---
name: systems-reasoning
description: Establish an implementation-independent model of a system before product, domain, architecture, delivery, or implementation decisions. Use for ambiguous boundaries, shared capabilities, cross-component effects, abstraction design, adapter leakage risk, feedback loops, and system-level trade-offs.
license: MIT
metadata:
  ai-native-skills.version: 0.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.requires: "decision-provenance"
  ai-native-skills.type: foundational-meta-skill
  ai-native-skills.related_skills: '["workflow-router","product-manager","delivery-work-breakdown","implementation-context-discovery","architecture-review","test-strategy","production-code-quality-baseline","skill-eval","skill-evolution"]'
---

# Systems Reasoning

## Purpose

Model the system before designing the solution. Establish purpose, boundaries, actors, capabilities, relationships, invariants, dynamics, leverage points, trade-offs, evidence, and uncertainty before selecting mechanisms, adapters, frameworks, vendors, or tools.

`systems-reasoning` is a foundational overlay. It does not replace the one primary lifecycle selected by `workflow-router`, and it does not take ownership from product, domain, architecture, delivery, implementation, testing, review, or acceptance capabilities.

## Core rule

```text
system purpose and outcomes
→ environment, actors, and ownership
→ boundaries and dependencies
→ capabilities, policies, and invariants
→ relationships and system dynamics
→ leverage points, failure modes, and trade-offs
→ downstream lifecycle decisions
→ mechanisms and adapter profiles
→ runtime and tool bindings
```

Never reason backward from an available framework, tool, adapter, vendor, repository structure, or current implementation and present that mechanism as the canonical system definition.

## Activate when

Use this skill when one or more apply:

- the system of interest or ownership boundary is ambiguous;
- a reusable capability must remain independent from adapters or products;
- a change crosses actors, components, repositories, services, teams, or lifecycle phases;
- local optimization may create system-level regressions;
- feedback loops, delays, bottlenecks, incentives, or emergent effects matter;
- architecture or decomposition is being selected before capabilities and invariants are clear;
- the prompt is implementation-heavy and risks tool-shaped reasoning;
- downstream skills need a shared normalized system model.

Do not activate for a bounded, low-risk task whose system, owner, invariants, and consequences are already explicit. Use the light path when only one or two missing decisions require clarification.

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

Missing evidence is `NOT_VERIFIED`, not permission to invent boundaries, actors, dependencies, invariants, approvals, or completion state.

## Procedure

### 1. Establish execution depth

Classify the task:

```text
LIGHT      bounded task; one local decision; low consequence
STANDARD   multiple actors/boundaries or reusable abstraction
DEEP       cross-repository/system change, high risk, strong dynamics, or conflicting authority
```

Use only the depth justified by complexity, reversibility, blast radius, uncertainty, and acceptance risk.

### 2. Define the system of interest

State:

- the system name;
- intended purpose and observable outcomes;
- environment and external systems;
- owner and decision authority;
- what is explicitly outside the analysis.

If the system cannot be bounded from verified evidence, stop implementation selection and return `NOT_VERIFIED` with the missing decisions.

### 3. Identify actors and relationships

Identify materially relevant actors, stakeholders, components, external systems, and their relationships. Record ownership, dependency direction, exchanged value or information, and failure propagation where relevant.

Do not produce a component inventory without explaining the important relationships.

### 4. Separate abstraction layers

Classify each material concept:

```text
capability      outcome the system must be able to produce
policy          rule governing permitted or required behavior
mechanism       one way to realize a capability or policy
adapter         translation between a canonical boundary and an external mechanism
runtime_binding concrete tool, provider, framework, process, or deployment binding
```

Capabilities and policies may constrain downstream mechanisms. Mechanisms, adapters, and runtime bindings must not redefine the canonical capability unless higher-authority evidence explicitly changes the system contract.

### 5. Discover invariants, constraints, assumptions, and uncertainty

Record separately:

- invariants that must remain true across implementations;
- constraints imposed by authority, environment, compatibility, safety, or delivery;
- assumptions that have not been verified;
- unresolved uncertainty and its effect on decisions.

### 6. Analyze dynamics proportionately

When material, trace:

- causal relationships;
- reinforcing and balancing feedback loops;
- delays and accumulation;
- bottlenecks and constraints;
- incentives and local optimizations;
- failure modes, unintended consequences, and emergent behavior.

Do not manufacture loops for a simple bounded task. For deep work, omission of material dynamics is a blocking gap.

### 7. Identify leverage points and trade-offs

Identify the smallest system-level interventions likely to improve the desired outcome. Record benefits, costs, reversibility, second-order effects, rejected alternatives, and residual risks.

Do not equate the most technically sophisticated intervention with the highest-leverage intervention.

### 8. Produce the normalized system model

Return the output contract below. Keep evidence, inference, assumption, review, approval, and acceptance distinct.

### 9. Hand off without taking lifecycle ownership

Provide only the fields needed by the selected downstream workflow or skill. Preserve one primary workflow. Technology and adapter selection occurs downstream after the abstraction is stable enough for the decision being made.

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
```

LIGHT outputs may omit empty dynamics fields, but must still state the system, boundary, relevant invariant or constraint, decision, evidence state, and handoff.

## Quality gates

- The system of interest and desired outcome are explicit.
- Inside/outside boundaries and decision ownership are explicit or `NOT_VERIFIED`.
- Capabilities, policies, mechanisms, adapters, and runtime bindings are not conflated.
- Material relationships and dependency directions are visible.
- Invariants, constraints, assumptions, and uncertainty are distinct.
- Dynamics analysis is proportionate to complexity and risk.
- Leverage points and trade-offs precede implementation selection.
- Framework-first reasoning and adapter leakage are rejected.
- Simple tasks are not inflated into ceremonial modeling.
- Complex tasks cannot bypass material boundary, invariant, relationship, and trade-off analysis.
- The output preserves one primary workflow and does not self-authorize implementation, merge, release, or product acceptance.
- A capability is claimed as applied only when it produces an observable system decision, model, finding, gate, or handoff.

## Stop and escalation conditions

Return `BLOCKED` or `NOT_VERIFIED` when:

- higher-authority sources conflict and decision provenance cannot resolve them;
- the system boundary or owner is required but cannot be established;
- a canonical capability change is being inferred from one adapter or implementation;
- required evidence is unavailable;
- the task requires an RFC or approval outside the current authority;
- downstream implementation would prematurely lock an unverified abstraction.

## Reference loading

Load only what the current concern requires:

- `references/abstraction-model.md` for terminology and abstraction hierarchy;
- `references/boundary-capability-analysis.md` for boundaries, actors, capabilities, invariants, and normalized examples;
- `references/dynamics-leverage-and-tradeoffs.md` for causal loops, delays, bottlenecks, failure modes, leverage points, and trade-offs;
- `references/integration-and-handoffs.md` for downstream composition and ownership;
- `references/anti-patterns-and-counterexamples.md` when detecting or correcting reasoning failures.

## Completion

The skill is complete for a task only when its proportionate gates pass, blocking gaps are disclosed, the normalized output is reviewable, and downstream ownership is explicit. Missing evidence remains `NOT_VERIFIED`.