# Integration and Handoffs

`systems-reasoning` is a foundational overlay. It supplies a normalized system model while preserving exactly one primary workflow.

## Workflow router

Consumed:

- user request;
- requested outcome;
- ambiguity and cross-system signals.

Produced:

- system classification;
- boundary and risk findings;
- recommended depth;
- materially relevant downstream consumers.

`workflow-router` still owns primary workflow selection.

## Product framing

Provide actors, desired outcomes, environment, constraints, incentives, and system-level trade-offs. Product capabilities still own value, scope, success criteria, and product acceptance.

## Domain modeling

Provide system boundary candidates, capabilities, policies, invariants, actors, relationships, and unresolved semantic conflicts. Domain modeling owns domain language, aggregates, events, and model design.

## Architecture

Provide capability boundaries, dependency direction, invariants, dynamics, failure propagation, leverage points, constraints, and trade-offs. Architecture owns architectural decisions and mechanism selection.

## Delivery breakdown

Provide independently valuable outcomes, dependency graph, ownership boundaries, risky integration points, and acceptance dependencies. Delivery breakdown owns epic/feature/task topology, branch base, and PR targets.

## Implementation context discovery

Provide the questions that must be verified against the live repository: current boundaries, adapters, runtime bindings, conventions, constraints, and known failure points. Discovery owns verification of actual implementation state.

## Test strategy

Provide system risks, boundaries, invariants, failure propagation, feedback delays, and acceptance consequences. Test strategy owns portfolio and test-level selection.

## Quality review

Provide intended system model and trade-offs as review context. Reviewers determine whether implementation evidence preserves the model and accepted decisions.

## Handoff rules

- Include only fields materially needed by the consumer.
- Preserve evidence, inference, assumption, review, approval, and acceptance as separate states.
- Do not convert an unresolved system decision into an implementation default.
- Do not claim downstream capability execution merely because it is named in a handoff.
- Return to systems reasoning only when new evidence materially changes the system boundary, purpose, invariant, relationship, dynamic, or trade-off.

## Composition example

```text
workflow-router selects new-feature-workflow
→ systems-reasoning models shared notification capability
→ product-manager confirms user value and channel policy
→ domain modeling defines canonical notification semantics
→ architecture selects ports and adapter boundaries
→ delivery-work-breakdown defines slices and integration order
→ implementation-context-discovery verifies repository reality
→ implementation and validation proceed
```

The overlay ends when the normalized system decisions are sufficient for the downstream owner. It must not remain active as a ceremonial duplicate of every later step.