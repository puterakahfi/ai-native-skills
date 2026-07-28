# Systems Reasoning Abstraction Model

## Working definitions

- **System**: interacting elements whose relationships produce outcomes within an environment.
- **System of interest**: the bounded system currently being analyzed for a stated purpose.
- **Environment**: external conditions, actors, systems, and constraints that affect the system of interest.
- **Boundary**: the explicit separation between what the analysis owns and what it treats as external.
- **Actor**: a person, team, organization, service, component, or external system that participates in or is affected by the system.
- **Capability**: an implementation-independent outcome the system must be able to produce.
- **Policy**: a governing rule that constrains allowed, required, or prohibited behavior.
- **Mechanism**: one way to realize a capability or enforce a policy.
- **Adapter**: a translation layer between a canonical boundary and an external mechanism or protocol.
- **Runtime binding**: a concrete provider, framework, tool, process, deployment, or library selected for execution.
- **Invariant**: a truth that must remain valid across permitted states and implementations.
- **Constraint**: a limiting condition imposed by authority, environment, compatibility, safety, cost, or delivery.
- **Assumption**: an unverified proposition temporarily used for reasoning.
- **Feedback loop**: a causal cycle whose effects reinforce or balance future behavior.
- **Leverage point**: a place where a bounded intervention can materially change system behavior.
- **Trade-off**: an explicit exchange between competing outcomes, risks, costs, or qualities.

## Allowed dependency direction

```text
purpose and outcomes
  ↓
capabilities and policies
  ↓
invariants and boundary contracts
  ↓
mechanisms
  ↓
adapters
  ↓
runtime bindings
```

A lower layer may satisfy or implement a higher layer. It must not silently redefine it.

## Classification examples

### Authentication

```yaml
capability: establish trusted identity context
policy: unverified identity cannot be treated as authenticated
mechanisms: [password, passkey, oauth, magic-link]
adapters: [oauth-provider-adapter, password-hash-adapter]
runtime_bindings: [Auth0, Keycloak, framework middleware]
```

Incorrect: `OAuth is the authentication domain.`

Correct: OAuth is one mechanism or protocol binding used to realize part of the authentication capability.

### Shared notifications

```yaml
capability: deliver a user-relevant notification through permitted channels
policy: user consent and delivery preference must be respected
mechanisms: [email, push, sms, in-app]
adapters: [smtp-adapter, push-provider-adapter]
runtime_bindings: [SES, Firebase Cloud Messaging]
```

Incorrect: define the shared capability around one provider's payload schema.

Correct: keep provider payloads downstream from a canonical notification contract.

### Persistence

```yaml
capability: preserve and retrieve domain state with required consistency
policy: writes must preserve aggregate invariants
mechanisms: [relational-store, document-store, event-log]
adapters: [repository-adapter, event-store-adapter]
runtime_bindings: [PostgreSQL, MongoDB, EventStoreDB]
```

Incorrect: `Repository pattern is the capability.`

Correct: persistence semantics are the capability; a repository can be a justified mechanism or boundary abstraction.

## Authority rule

When implementation evidence conflicts with a higher-authority canonical contract, record the conflict through decision provenance. Do not promote the implementation into canonical meaning without approval.