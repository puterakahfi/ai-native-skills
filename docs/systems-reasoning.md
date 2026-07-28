# Systems Reasoning

`systems-reasoning` is a foundational `meta-skill` overlay for implementation-independent system modeling.

Use it before product, domain, architecture, delivery, or implementation decisions when boundaries, shared capabilities, cross-component effects, adapter leakage, feedback loops, or system-level trade-offs are material.

## Position in the capability system

```text
workflow-router selects one primary workflow
→ systems-reasoning supplies a proportionate shared system model
→ systems-thinking performs deep feedback-loop and emergence analysis when material
→ downstream product/domain/architecture/delivery skills retain ownership
→ mechanisms, adapters, and runtime bindings are selected only after abstraction is stable enough
```

It does not introduce a fourth taxonomy category and does not replace a lifecycle.

## Relationship to systems-thinking

The existing `systems-thinking` atomic skill owns deep analysis of reinforcing and balancing loops, emergence, second-order effects, Conway's Law, Goodhart's Law, unintended consequences, and leverage points under its core contract.

`systems-reasoning` owns the broader orchestration layer: establish the system of interest, boundary, actors, capability/policy/mechanism separation, invariants, uncertainty, proportional depth, and downstream handoff. It delegates deep dynamics analysis instead of duplicating that ownership.

## Canonical entry point

- `skills/systems-reasoning/SKILL.md`

## Runtime references

- `skills/systems-reasoning/references/abstraction-model.md`
- `skills/systems-reasoning/references/boundary-capability-analysis.md`
- `skills/systems-reasoning/references/dynamics-leverage-and-tradeoffs.md`
- `skills/systems-reasoning/references/integration-and-handoffs.md`
- `skills/systems-reasoning/references/anti-patterns-and-counterexamples.md`
- `skills/systems-reasoning/references/pilot-cases.md`

## Behavioral contract

- `contracts/tests/systems-reasoning.test.yaml`

## Activation summary

Activate for:

- ambiguous or contested system boundaries;
- reusable capabilities that must remain adapter-independent;
- cross-repository, cross-service, cross-team, or cross-lifecycle effects;
- causal loops, delays, bottlenecks, incentives, or failure propagation;
- premature architecture or decomposition;
- implementation-heavy prompts that risk redefining capability around tools.

Use LIGHT depth or do not activate for bounded low-risk work with explicit ownership, contracts, invariants, and consequences.

## Acceptance boundary

Skill-file presence is not completion evidence. Completion requires applicable package validation, behavioral evidence, review, and acceptance. Missing execution evidence remains `NOT_VERIFIED`.