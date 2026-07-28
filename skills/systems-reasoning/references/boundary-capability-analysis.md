# Boundary and Capability Analysis

## Boundary procedure

1. State the intended outcome and decision being supported.
2. Name the system of interest.
3. List what the current owner can change directly.
4. List external actors, systems, authorities, and constraints.
5. Mark unknown ownership or responsibility as `NOT_VERIFIED`.
6. Identify dependency direction and exchanged information, value, or control.
7. Test whether moving the boundary changes the meaning of the decision.

## Boundary questions

- What outcome is this system responsible for producing?
- Which actor owns that outcome and its acceptance?
- Which decisions are internal, and which require external authority?
- Which dependencies can fail independently?
- Where can implementation details leak into canonical contracts?
- What must remain stable if an adapter, provider, or framework changes?

## Capability discovery

Describe capabilities as observable outcomes, not components or technologies.

Weak:

```text
Use Redis, Kafka, and a worker service.
```

Stronger:

```text
Accept work without blocking the caller, preserve delivery intent,
retry recoverable failures, prevent unacceptable duplication, and expose status.
```

Only after those outcomes and constraints are stable should downstream architecture select queues, brokers, databases, workers, or providers.

## Invariant discovery

Look for truths that must hold across implementation choices:

- safety and authorization boundaries;
- consistency and ordering guarantees;
- identity and ownership rules;
- compatibility obligations;
- no-loss or bounded-loss requirements;
- acceptance and evidence rules.

Do not rewrite temporary implementation limitations as permanent invariants.

## Normalized light example

```yaml
systems_reasoning:
  depth: LIGHT
  status: PASS
  system_of_interest:
    name: shared authentication capability
    purpose: provide trusted identity context to product applications
    inside_boundary: [canonical identity contract, authentication use cases]
    outside_boundary: [identity provider, UI framework, persistence vendor]
    owner: platform capability owner
  abstraction_map:
    capabilities: [establish trusted identity context]
    policies: [unverified identities are never authenticated]
    mechanisms: [password, oauth, passkey]
    adapters: [provider adapters]
    runtime_bindings: []
  invariants:
    - provider-specific claims do not leak into the canonical identity model
  trade_offs:
    - broader provider support increases adapter and conformance cost
  evidence_refs: []
  assumptions: []
  blocking_gaps: []
  downstream_handoff:
    primary_workflow: spec-workflow
    consumers: [domain modeling, architecture]
    required_next_decisions: [canonical identity contract]
```

## Boundary failure signals

- a component list exists but no ownership or dependency direction;
- the repository structure is treated as the system boundary by default;
- one provider API determines the domain model;
- an implementation team is assumed to own product acceptance;
- external approval or authority is omitted;
- cross-system consequences are labeled out of scope merely because they are difficult.