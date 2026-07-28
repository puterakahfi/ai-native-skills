# Anti-patterns and Counterexamples

## Framework-first reasoning

Incorrect:

```text
We use Laravel, so the domain should be organized around controllers, models, and jobs.
```

Corrected:

```text
First identify capabilities, policies, invariants, and boundaries. Then map them to the smallest justified Laravel mechanisms without allowing framework structure to redefine the system.
```

## Tool-shaped capability

Incorrect:

```text
The capability is a Kafka topic.
```

Corrected:

```text
The capability is durable asynchronous transfer with stated ordering, delivery, retry, and observability requirements. Kafka may be one runtime binding.
```

## Adapter leakage

Incorrect:

```text
Use the provider's response object as the canonical identity model.
```

Corrected:

```text
Define the trusted identity context independently. Translate provider claims through an adapter and prove conformance.
```

## Premature decomposition

Incorrect:

```text
Create five services before ownership, transactional boundaries, and failure propagation are understood.
```

Corrected:

```text
Model outcomes, boundaries, dependencies, invariants, and operational forces before selecting service boundaries.
```

## Local optimization

Incorrect:

```text
Increase worker concurrency because the queue is growing.
```

Corrected:

```text
Verify whether downstream rate limits, database contention, retries, or approval delays are the actual system constraint. Higher concurrency may amplify failure and backlog.
```

## Component inventory without relationships

Incorrect:

```text
The system contains API, database, queue, worker, and dashboard.
```

Corrected:

```text
Describe who owns each outcome, dependency direction, exchanged data, failure propagation, delays, and acceptance evidence.
```

## Unsupported universal abstraction

Incorrect:

```text
Every application needs Clean Architecture, DDD, ports, repositories, factories, and domain events.
```

Corrected:

```text
Select abstractions only when verified complexity, change pressure, substitution needs, boundaries, invariants, or recurring forces justify them.
```

## Over-modeling a simple task

Incorrect:

```text
Create a causal-loop diagram and stakeholder map to rename a private local variable.
```

Corrected:

```text
Do not activate, or use LIGHT depth only when a hidden boundary or invariant genuinely matters.
```

## Hidden assumption

Incorrect:

```text
The platform team owns acceptance because it implements the shared package.
```

Corrected:

```text
Mark acceptance ownership `NOT_VERIFIED` until the product or governing source identifies the accountable authority.
```

## Skill declaration as evidence

Incorrect:

```text
Systems reasoning was applied because the plan lists the skill.
```

Corrected:

```text
Claim application only when an observable boundary decision, abstraction map, invariant, dynamic finding, trade-off, gate, or handoff exists.
```