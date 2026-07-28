# Dynamics, Leverage Points, and Trade-offs

## When deeper dynamics analysis is justified

Use deeper analysis when the task includes repeated behavior, queues or accumulation, incentives, multiple owners, delayed effects, scaling pressure, operational feedback, or a history of local fixes causing new problems.

## Causal analysis

Express important causal relationships in plain language:

```text
more adapter-specific logic in canonical skills
→ faster local implementation
→ higher coupling
→ harder reuse and testing
→ more exceptions
→ more pressure to add adapter-specific logic
```

Classify loops:

- **reinforcing**: change amplifies future change;
- **balancing**: change creates pressure toward a limit or target.

Record delays because delayed effects often make a harmful intervention appear successful at first.

## Bottlenecks and constraints

Distinguish the system constraint from visible local symptoms. Improving a non-constraint may increase work-in-progress without improving throughput.

Questions:

- Where does work, information, approval, or failure accumulate?
- Which dependency determines end-to-end throughput or confidence?
- Which local metric can improve while the system outcome worsens?
- What delayed consequence is currently invisible?

## Failure modes and unintended consequences

For each material intervention, consider:

- how it fails;
- how failure propagates;
- whether retry, compensation, fallback, or human intervention exists;
- who detects the failure and with what evidence;
- whether the intervention changes incentives or moves risk elsewhere.

## Leverage-point selection

Prefer interventions that change system behavior at the smallest justified cost and scope. Common leverage points include:

- clarifying ownership and acceptance;
- stabilizing an invariant or canonical boundary;
- changing information flow or feedback visibility;
- reducing a harmful delay;
- constraining adapter leakage;
- adding conformance evidence at a boundary;
- removing a repeated source of work rather than accelerating rework.

## Trade-off record

```yaml
trade_off:
  decision: stabilize canonical notification contract before adding providers
  benefits: [provider independence, consistent policy enforcement]
  costs: [initial modeling and conformance work]
  second_order_effects: [simpler future provider additions]
  reversibility: medium
  rejected_alternatives:
    - alternative: expose provider payloads directly
      reason: couples products to one runtime binding
  residual_risks: [canonical contract may initially omit provider-specific edge cases]
```

A trade-off is incomplete when it lists only benefits or treats one quality attribute as universally dominant.