# Systems Reasoning

`systems-reasoning` is a foundational `meta-skill` overlay for implementation-independent system modeling.

Use it before product, product-experience design, domain, architecture, delivery, or implementation decisions when boundaries, shared capabilities, cross-component or cross-journey effects, adapter leakage, feedback loops, local optimization, or system-level trade-offs are material.

## Position in the capability system

```text
workflow-router selects one primary workflow
→ systems-reasoning supplies a proportionate shared system model
→ systems-thinking performs deep feedback-loop and emergence analysis when material
→ downstream product, design, domain, architecture, and delivery skills retain ownership
→ experience patterns, mechanisms, adapters, and runtime bindings are selected only after abstraction is stable enough
```

It does not introduce a fourth taxonomy category and does not replace a lifecycle.

## Relationship to systems-thinking

The existing `systems-thinking` atomic skill owns deep analysis of reinforcing and balancing loops, emergence, second-order effects, Conway's Law, Goodhart's Law, unintended consequences, and leverage points under its core contract.

`systems-reasoning` owns the broader orchestration layer: establish the system of interest, boundary, actors, capability/policy/mechanism separation, invariants, uncertainty, proportional depth, and downstream handoff. It delegates deep dynamics analysis instead of duplicating that ownership.

The canonical cross-repository boundary remains tracked by `puterakahfi/ai-native-core#70`. Until that RFC is accepted, the executable capability uses a reviewed core-gap exemption and must not claim core-contract conformance.

## Product-experience and design composition

When design work has material cross-journey, metric, reusable-system, positioning, information-architecture, product-proof, or second-order consequences:

```text
product-development-workflow or redesign-workflow remains primary
→ systems-reasoning creates systemic_design_applicability and a bounded system handoff
→ systems-thinking handles deep dynamics when justified
→ master-design compares and selects the experience and visual direction
→ design specialists resolve narrow concerns
→ implementation-context-discovery verifies repository reality before code
→ design-review controls rendered or implemented acceptance
```

A hero, dashboard, card grid, tabs, split layout, bento, document-led page, workbench, or another macrostructure is a candidate mechanism. None is required merely because the artifact has a familiar name such as landing page or SaaS website.

Bounded visual fixes use REDUCED or NOT_APPLICABLE and must not receive ceremonial deep systems analysis.

## Canonical entry point

- `skills/systems-reasoning/SKILL.md`

## Runtime references

- `skills/systems-reasoning/references/abstraction-model.md`
- `skills/systems-reasoning/references/boundary-capability-analysis.md`
- `skills/systems-reasoning/references/dynamics-leverage-and-tradeoffs.md`
- `skills/systems-reasoning/references/integration-and-handoffs.md`
- `skills/systems-reasoning/references/anti-patterns-and-counterexamples.md`
- `skills/systems-reasoning/references/pilot-cases.md`
- `skills/master-design/references/systemic-design-reasoning.md`

## Behavioral contracts

- `contracts/tests/systems-reasoning.test.yaml`
- `contracts/tests/master-design.test.yaml`

## Activation summary

Activate for:

- ambiguous or contested system boundaries;
- reusable capabilities that must remain adapter-independent;
- cross-repository, cross-service, cross-team, cross-journey, cross-route, or cross-lifecycle effects;
- causal loops, delays, bottlenecks, incentives, metric proxy failure, or failure propagation;
- premature architecture, decomposition, or visual structure selection;
- implementation-heavy or pattern-heavy prompts that risk redefining capability around tools or templates;
- material design-system or component-family consequences.

Use LIGHT depth or do not activate for bounded low-risk work with explicit ownership, contracts, invariants, locks, and consequences.

## Acceptance boundary

Skill-file presence is not completion evidence. Completion requires applicable package validation, behavioral evidence, review, and acceptance. Missing execution evidence remains `NOT_VERIFIED`.
