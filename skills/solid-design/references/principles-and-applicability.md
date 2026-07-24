# Principles and Applicability

Use this reference to decide whether SRP or OCP materially applies, identify real change forces, and reject SOLID ceremony that adds more indirection than value.

## Review sequence

```text
behavior and ownership
→ consumers and change pressure
→ principle applicability
→ current risk
→ direct and abstract alternatives
→ smallest justified correction
→ verification
```

A principle name is not evidence. Begin from observable system pressure.

## Applicability classification

### APPLICABLE

Use when concrete evidence shows the principle affects safe change or behavior.

Examples:

- unrelated policies change independently inside one owner;
- multiple accepted variants repeatedly modify the same stable decision path;
- clients rely on substitutes with materially different behavior;
- consumers are forced to implement operations they cannot support;
- stable policy imports volatile provider or framework details.

### PARTIAL

Use when only a bounded portion of the subject has the relevant force.

A module can have an SRP issue in one sub-area without requiring total decomposition. A single integration boundary can need DIP while the rest of the module remains direct.

### NOT_APPLICABLE

Use when no relevant ownership, variation, substitution, client-interface, or dependency-direction force exists.

`NOT_APPLICABLE` is a valid finding. It protects the codebase from speculative abstraction.

### NOT_VERIFIED

Use when behavior, consumers, variants, change history, repository conventions, or tests are missing.

Do not replace missing evidence with textbook assumptions.

## Force map

```yaml
force_map:
  subject: <class, module, component, service, or API>
  owned_concept: <concept>
  behavior_contracts: []
  consumers: []
  existing_variants: []
  observed_change_reasons: []
  volatile_dependencies: []
  repository_constraints: []
  evidence_gaps: []
```

Useful evidence includes specifications, issue history, git changes, tests, client usage, error contracts, provider boundaries, and repository architecture decisions.

## SRP — cohesive responsibility and change ownership

SRP asks whether behavior and state that belong to one coherent owner change together for related reasons.

It does not require:

- one method per class;
- one actor word per class;
- tiny files;
- separating every read from every write;
- moving logic into generic services merely to reduce class size.

### Review questions

- What concept does this subject own?
- Which invariants must remain consistent together?
- Which changes happen for the same product or domain reason?
- Which changes are driven by unrelated policies, teams, providers, or release cadence?
- Are stable business rules interleaved with volatile delivery or infrastructure details?
- Do consumers use coherent or disjoint subsets of behavior?
- Would decomposition create clearer ownership, or only more navigation and data movement?

### Valid SRP evidence

```text
One module owns pricing policy and SMTP delivery.
Pricing changes with commercial rules; SMTP changes with provider behavior.
The concerns have different tests, dependencies, and failure semantics.
```

This is stronger than:

```text
The file has 350 lines, therefore SRP is violated.
```

### Correction ladder

```text
clarify name and ownership
→ group related behavior
→ isolate volatile detail
→ extract one cohesive policy or capability
→ split module only when owner and contracts are clear
```

Do not create an anemic coordinator plus many wrappers when the current subject owns one cohesive transaction or invariant.

## OCP — protect proven variation pressure

OCP asks whether stable behavior can accept a proven family of changes without repeatedly editing the same risky decision core.

It does not mean all code must be extensible. Most code can remain directly modifiable until variation pressure is real.

### Evidence that OCP may apply

- two or more accepted variants already exist;
- new variants repeatedly change the same conditional or switch;
- extension comes from separately deployed or owned modules;
- a stable contract must support provider, policy, or strategy replacement;
- changes repeatedly risk regressions in unrelated variants;
- repository architecture already defines an accepted extension seam.

### Evidence that direct modification may remain better

- the rule set is finite and intentionally closed;
- there is one implementation and no credible second force;
- variants share no stable contract beyond superficial syntax;
- abstraction would expose more internals than it protects;
- the change is rare, local, and safely tested;
- the repository intentionally favors explicit conditionals for this domain.

### Conditional analysis

A conditional is not automatically an OCP violation.

Prefer an explicit conditional when it expresses:

- a small closed business rule;
- ordered validation;
- protocol state transitions;
- a finite exhaustive type set;
- behavior clearer together than distributed across objects.

Consider an extension seam when the conditional repeatedly grows from independently changing variants whose behavior can be expressed through one stable contract.

### Candidate options

```text
direct conditional
named decision function
lookup or data table
composition
strategy
registry or plugin
policy object
repository-accepted pattern
```

Select based on actual forces, not pattern prestige.

## Cross-principle interactions

SOLID principles can pull in different directions.

- Splitting for SRP may increase interface and navigation burden.
- OCP abstractions can violate ISP when every client receives a broad extension contract.
- DIP can create unnecessary indirection when the detail is stable and local.
- LSP may show that inheritance is wrong even though OCP pressure is real; composition can be safer.

Record trade-offs rather than claiming one principle automatically dominates.

## Abstraction risk review

```yaml
abstraction_risk:
  proposed_abstraction: <interface, base class, strategy, port, registry, wrapper>
  proven_force: <evidence | missing>
  expected_variants: []
  owner: <consumer, policy, provider, shared core>
  new_indirection: <cost>
  migration_cost: <cost>
  test_consequence: <effect>
  reversal_path: <path>
  verdict: JUSTIFIED | PREMATURE | NOT_VERIFIED
```

### Premature abstraction signals

- interface with one implementation and no credible change force;
- generic repository hiding useful domain operations;
- base class created only to share a few lines;
- strategy for one fixed algorithm;
- adapter around a stable local module with no boundary need;
- event or plugin system used to avoid a direct call;
- class split caused only by a metric target.

## Severity guidance

```text
BLOCKING
  behavioral incompatibility, unsafe substitution, policy/detail inversion causing material risk,
  or ownership confusion that prevents responsible implementation

HIGH
  verified design coupling with strong regression or change risk

MEDIUM
  concrete maintainability or client-coupling cost with bounded impact

LOW
  localized improvement that does not block safe change

NOTE
  principle not applicable, trade-off observation, or evidence gap
```

A book-rule mismatch is never blocking by itself. Severity follows system consequence.
