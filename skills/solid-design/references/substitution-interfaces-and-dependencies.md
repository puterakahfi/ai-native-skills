# Substitution, Interfaces, and Dependencies

Use this reference for LSP, ISP, and DIP analysis. These principles require behavioral, client, and dependency evidence; syntax and framework mechanisms are not enough.

## LSP — behavioral substitutability

A substitute is valid when a client relying on the declared contract can use it without surprising behavior, weakened guarantees, or special-case knowledge.

Compilation, inheritance, shared method names, and interface implementation prove only structural compatibility.

### Behavioral contract dimensions

```yaml
behavior_contract:
  accepted_inputs: []
  preconditions: []
  outputs: []
  postconditions: []
  invariants: []
  state_transitions: []
  errors: []
  side_effects: []
  ordering: []
  idempotency: <true | false | conditional>
  timing_or_resource_expectations: []
  cancellation_and_retry: []
```

Review each substitute against the promises clients actually use.

### Common LSP violations

- a subtype rejects valid inputs accepted by the base contract;
- a substitute returns weaker or ambiguous results;
- an operation becomes unsupported, silently ignored, or throws a new surprise error;
- state invariants change so clients need subtype checks;
- ordering, atomicity, retry, or idempotency differs materially;
- a read substitute performs unexpected writes or network calls;
- one implementation requires initialization or sequencing not declared by the contract;
- performance or resource behavior violates an explicit contract clients rely on.

### Unsupported operations

A base contract that exposes operations some substitutes cannot support is usually a contract-design problem.

Do not solve it with:

```text
throw NotSupportedException
return null
silently no-op
check concrete type in every client
```

Possible corrections:

- narrow the contract;
- separate capabilities by client need;
- use composition instead of inheritance;
- expose capability discovery explicitly when the domain truly supports optional behavior;
- move the operation to a more specific contract.

### Contract tests

Use shared behavioral tests when multiple implementations claim one contract.

```text
contract test suite
  runs against implementation A
  runs against implementation B
  verifies the same observable promises
```

Contract tests should cover inputs, outputs, errors, side effects, ordering, and state transitions—not implementation details.

### Inheritance review

Inheritance is appropriate only when the subtype genuinely preserves the base behavioral contract and the taxonomy is stable enough to justify coupling.

Prefer composition when:

- behavior varies independently from identity;
- clients need selectable capabilities;
- subclasses override many methods or disable behavior;
- lifecycle and state invariants diverge;
- reuse is the only reason for inheritance.

## ISP — interfaces shaped by clients

ISP asks whether a client depends only on the operations and guarantees it needs.

Begin from consumers, not from a desired number of methods.

### Client-operation matrix

```yaml
client_interface_matrix:
  interface: <name>
  operations: []
  clients:
  - client: <name>
    required_operations: []
    required_guarantees: []
    unused_operations: []
    fake_or_unsupported_operations: []
    change_coupling: []
```

### Evidence that an interface is too broad

- implementations provide fake or unsupported methods;
- clients receive permissions or capabilities they should not have;
- unrelated operations change for different consumer groups;
- mocks and test doubles must implement irrelevant behavior;
- broad changes force many unrelated consumers to recompile, retest, or migrate;
- one contract mixes command, query, administration, and operational concerns without a cohesive client need.

### Evidence against splitting

- all clients use the operations as one cohesive transaction;
- guarantees and invariants span the full interface;
- splitting creates ordering knowledge or partial invalid states;
- one-method fragments make discovery and ownership worse;
- the repository intentionally exposes a stable cohesive capability.

### Correction options

```text
keep cohesive interface
provide a narrower client-facing view
split read/write or user/admin capability when domain evidence supports it
compose small cohesive interfaces
move optional operation to a specific capability
```

Avoid interface fragmentation by method count alone.

## DIP — stable policy and volatile detail

DIP asks whether high-value policy is insulated from details that change for unrelated technical or provider reasons.

It does not require every dependency to be abstract. Direct dependency is valid when it is stable, local, accepted, and not creating meaningful coupling risk.

### Dependency map

```yaml
dependency_decision:
  policy_owner: <module or capability>
  stable_policy: <business or application rule>
  volatile_detail: <database, provider, framework, clock, filesystem, queue, transport>
  current_direction: <policy -> detail | detail -> policy abstraction>
  boundary_owner: <consumer or policy module>
  abstraction_needed: <yes | no | not_verified>
  wiring_location: <composition root>
  test_consequence: <effect>
```

### Valid DIP pressure

- business policy imports provider SDK types;
- application rules cannot be tested without network, database, clock, filesystem, or framework runtime;
- changing a provider requires modifying stable policy;
- infrastructure owns the interface and leaks its vocabulary inward;
- reusable policy depends on product-specific or runtime-specific detail;
- multiple details implement one stable capability contract.

### When direct dependency is acceptable

- dependency is a stable standard-library or accepted core primitive;
- the code is already in the infrastructure adapter that owns the detail;
- there is no stable policy to protect;
- abstraction would merely mirror the dependency API;
- tests can verify the behavior at the correct boundary without harmful coupling;
- repository architecture explicitly accepts the dependency in this layer.

### Abstraction ownership

The abstraction should normally be named and owned by the policy or consumer capability.

Bad direction:

```text
policy → provider-owned interface and provider types
```

Preferred when DIP applies:

```text
provider adapter → policy-owned capability contract ← stable policy
```

The contract should express domain/application meaning rather than reproduce the provider SDK.

### Dependency injection is wiring, not proof

Constructor injection can improve visibility and testing, but it does not prove DIP when:

- the injected type is still a volatile provider class;
- the interface is owned by infrastructure and leaks detail semantics;
- stable policy still knows transport, ORM, framework, or vendor types;
- the DI container hides global service location;
- the abstraction has no bounded behavioral contract.

Conversely, manual composition can satisfy DIP without a container.

### Composition root

Keep concrete wiring at an accepted outer boundary:

```text
application bootstrap
framework adapter
runtime assembly
product composition root
```

Do not turn domain/application code into a service locator.

## Combined review examples

### Payment processing

```text
LSP
  every payment provider must preserve declared authorization/capture/refund semantics

ISP
  a reporting client should not depend on refund or credential-rotation operations

DIP
  checkout policy depends on a policy-owned payment capability, not provider SDK types
```

This does not imply every provider operation belongs in one universal interface. Separate contracts by cohesive client need and behavioral guarantee.

### Storage abstraction

A generic `Repository<T>` is not automatically SOLID.

Review whether:

- domain consumers share one meaningful persistence capability;
- operations express domain intent;
- implementations can preserve the same transaction and error behavior;
- broad CRUD methods force unsupported or unsafe behavior;
- abstraction hides important query, consistency, or ownership semantics.

A direct repository specialized for an aggregate may be clearer than a generic base interface.

## Verification evidence

Possible evidence:

- shared contract tests across implementations;
- client-specific compile/type checks;
- tests showing unsupported operations are removed;
- dependency graph or import checks;
- policy tests using in-memory/fake adapters;
- provider adapter integration tests;
- architecture review confirming layer and owner boundaries.

Keep design recommendation separate from post-implementation acceptance.
