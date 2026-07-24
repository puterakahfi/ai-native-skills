# Boundaries, Data Translation, and Migration

Use this reference after architecture applicability is established. It turns conceptual inward dependency into repository-aware boundary decisions, data translation, orchestration, transactions, migration slices, and verification.

## Boundary identification

A boundary is justified when behavior, ownership, volatility, or failure semantics differ materially.

Potential boundaries:

- domain policy versus application orchestration;
- application policy versus persistence;
- application policy versus provider SDK;
- transport parsing versus use-case input;
- use-case output versus presentation formatting;
- bounded module versus another product capability;
- reusable core versus product/runtime adapter;
- synchronous application flow versus asynchronous delivery.

Do not create a boundary merely because two folders can be named.

## Boundary record

```yaml
boundary_record:
  name: <capability or seam>
  purpose: <risk or ownership protected>
  inner_owner: <stable policy module>
  outer_owner: <adapter, framework, provider, or product module>
  incoming_contract: <input contract>
  outgoing_contract: <required capability contract>
  allowed_dependencies: []
  prohibited_dependencies: []
  data_translation: []
  failure_translation: []
  transaction_scope: <scope>
  tests: []
  evidence_gaps: []
```

## Dependency direction

The dependency rule applies to source and semantic ownership, not only runtime calls.

Runtime control may flow outward:

```text
use case → payment capability → payment adapter → provider
```

Source ownership should preserve inward policy:

```text
provider adapter imports policy-owned payment contract
policy does not import provider SDK types
```

Inspect:

- imports and package references;
- type ownership;
- configuration and annotation leakage;
- inheritance and interface ownership;
- error and DTO types;
- event schemas and provider payloads;
- callbacks and framework base classes;
- static/global access to infrastructure.

## Boundary data translation

Translate data when outer representation would couple stable policy to a volatile detail.

Common outer types:

- HTTP request/response models;
- GraphQL resolver inputs;
- ORM entities and query builders;
- provider SDK objects;
- queue or event envelopes;
- framework validation errors;
- UI/view models;
- filesystem, serialization, or transport structures.

### Translation options

```text
transport input → use-case command/query
ORM record ↔ domain/application state
provider response → policy-owned result
use-case result → presenter/view model
external event → application message
```

### Do not translate mechanically

Translation is not automatically required for every field or every layer.

Keep a type direct when:

- it is already policy-owned and stable;
- no volatile detail leaks through it;
- repository convention accepts it at the current boundary;
- another mapping would duplicate data without protecting a real seam.

Translate when:

- provider or framework vocabulary enters policy decisions;
- persistence shape differs from business invariants;
- transport optionality, validation, or naming differs from use-case intent;
- external schema evolution should not force policy changes;
- errors or partial states need a stable application contract.

## Error and failure translation

Each boundary should preserve meaningful failure semantics.

```yaml
failure_contract:
  outer_failures: []
  inner_meaning: []
  retryable: []
  permanent: []
  partial_success: []
  idempotency: <contract>
  observability_owner: <owner>
```

Do not leak provider exceptions or framework error objects into stable policy when clients need a durable application meaning.

Avoid collapsing every failure into one generic error. Preserve decisions clients need for retry, compensation, user messaging, or incident handling.

## Use-case orchestration

A use case owns one application intention.

Typical responsibilities:

- authorize or establish application preconditions;
- load required state through accepted capabilities;
- invoke domain policy;
- coordinate one transaction or consistency boundary;
- call external capabilities in an explicit sequence;
- publish application outcomes;
- return a stable result.

A use case should not automatically own:

- domain invariants that belong to entities/value objects/domain services;
- SQL, ORM, HTTP, queue, or provider mechanics;
- controller/view formatting;
- generic logging wrappers;
- one class per CRUD call when direct framework behavior is already accepted and sufficient.

### Pass-through ceremony signal

```text
controller → use case → service → repository
```

is not valuable when every layer forwards the same data with no policy, translation, ownership, or test seam.

Possible correction:

- remove a meaningless layer;
- merge orchestration into the accepted application owner;
- keep a boundary only around material policy or volatile detail;
- retain direct framework flow for trivial accepted behavior.

## Transaction ownership

Declare where atomicity and consistency belong.

Questions:

- Which state changes must commit together?
- Does the domain enforce invariants inside the transaction?
- Does the use case define transaction scope?
- Is persistence implementation responsible only for mechanics?
- Are external side effects inside or outside the transaction?
- Is an outbox, saga, retry, or compensation actually justified?
- Can an adapter open hidden nested transactions?

Do not scatter transaction control across controllers, domain objects, repositories, and provider adapters.

## Ports and adapters decision

Create a port when:

- stable policy needs a capability from a volatile detail;
- multiple adapters must preserve a meaningful contract;
- testing requires a policy boundary independent from infrastructure;
- a separately owned module exposes a bounded capability;
- provider changes should not alter policy vocabulary.

A port should include:

```yaml
port:
  owner: <policy or consumer module>
  capability: <meaningful job>
  operations: []
  behavior_guarantees: []
  error_contract: []
  transaction_expectations: []
  implementations: []
  contract_tests: []
```

Do not create:

- an interface that mirrors every provider SDK method;
- a repository with generic CRUD unrelated to domain intent;
- a port around stable standard-library utilities;
- one adapter per class merely to increase mockability;
- an interface with no policy consumer or credible implementation pressure.

## Repository mapping

Map conceptual decisions to actual accepted repository structures.

```yaml
repository_mapping:
  policy_module:
    path: <actual path>
    imports_allowed: []
    imports_prohibited: []
  application_orchestration:
    path: <actual path>
  adapters:
  - capability: <capability>
    path: <actual path>
    accepted_frameworks_or_providers: []
  wiring:
    path: <composition root>
  boundary_types:
  - type: <type>
    owner: <owner>
    path: <path>
```

Use aliases, package conventions, framework modules, and existing component systems discovered in the repository. Do not introduce parallel “clean” roots without approval.

## Migration strategy

### Preservation locks

Before structural changes, record:

- observable behavior and acceptance criteria;
- public API/event/data contracts;
- persistence and migration compatibility;
- transaction and failure behavior;
- performance and operational constraints;
- repository convention locks;
- tests that protect the slice.

### Safe sequence

```text
1. Select one verified policy/detail seam.
2. Add or strengthen behavior evidence.
3. Define the inner contract only if the boundary is justified.
4. Translate one outer representation at the seam.
5. Move one dependency direction.
6. Wire the concrete adapter at the accepted composition root.
7. Run technical and runtime verification.
8. Run independent architecture review.
9. Stop unless the next slice has separate evidence and acceptance.
```

### Stop conditions

Stop when:

- the verified risk is resolved;
- further movement would be cosmetic;
- the next slice lacks tests or authority;
- migration expands into unrelated modules;
- framework capabilities are being duplicated;
- indirection increases without policy protection;
- runtime or performance cost exceeds accepted limits.

## Testing strategy

Use the smallest meaningful evidence:

### Policy or domain tests

Verify business/application decisions without unnecessary infrastructure.

### Use-case tests

Verify orchestration, failure handling, state transitions, and capability interaction. Fakes should preserve meaningful contracts, not simply return convenient values.

### Contract tests

Run shared behavioral expectations against multiple adapters implementing one port.

### Adapter integration tests

Verify provider/framework mapping, persistence behavior, serialization, transactions, and external error translation.

### Boundary and dependency checks

Verify prohibited imports, package/module dependencies, type leakage, and architecture rules where tooling exists.

### Runtime evidence

Verify actual wiring, configuration, transactions, latency, failure modes, and observability. Unit tests alone do not prove the composed system.

## Review checklist

- Is every boundary protecting a named risk or owner?
- Does source dependency point toward stable policy where applicable?
- Are contracts owned by policy/consumers rather than volatile details?
- Are outer data and errors translated only when needed?
- Is use-case orchestration meaningful rather than pass-through ceremony?
- Is transaction ownership explicit?
- Are ports bounded by capability and behavior?
- Does repository mapping use actual accepted paths?
- Is migration incremental and reversible?
- Are behavior, integration, dependency, runtime, and acceptance evidence distinct?
