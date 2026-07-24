# Architecture Style Applicability and Comparison

Use this reference to compare architecture approaches from verified forces rather than labels. The same system may use different approaches in different bounded slices.

## Start with forces

```yaml
architecture_forces:
  policy_complexity: <low | medium | high>
  integration_volatility: <low | medium | high>
  entrypoints: []
  persistence_variants: []
  provider_variants: []
  reuse_requirements: []
  independent_testability_need: <bounded | material | critical>
  transaction_complexity: <low | medium | high>
  team_and_module_ownership: []
  operational_constraints: []
  migration_constraints: []
```

Do not select an architecture because it is popular, modern, diagram-friendly, or associated with senior engineering.

## Direct or conventional implementation

### Fits when

- behavior is simple and local;
- one delivery mechanism and one stable dependency exist;
- no stable policy/detail boundary is materially at risk;
- repository conventions already make ownership clear;
- abstraction and translation would add more cost than change protection.

### Risks

- can become coupled when policy and integration complexity grow;
- may need a later bounded extraction if provider or delivery variation appears.

### Warning

Direct code is not automatically unclean. It is often the smallest durable design.

## Layered architecture

Typical conceptual flow:

```text
presentation → application/service → data/infrastructure
```

### Fits when

- the system has clear responsibility tiers;
- dependencies mostly flow one direction;
- domain complexity is moderate;
- repository/framework conventions already support layered modules;
- a small number of integrations can remain at outer layers.

### Strengths

- familiar and easy to navigate;
- low ceremony;
- good fit for many business applications;
- incremental adoption is straightforward.

### Risks

- business policy can drift into controllers or services;
- application services can become transaction scripts or god services;
- domain and data models may collapse into one framework representation;
- layers can become global technical silos rather than product capabilities.

A well-designed layered module can satisfy the dependency rule without adopting Clean Architecture vocabulary.

## Modular monolith

### Fits when

- one deployable product contains multiple cohesive business capabilities;
- module ownership and internal contracts matter;
- independent service deployment is not justified;
- operational simplicity is valuable;
- modules need bounded data and dependency rules.

### Strengths

- strong capability ownership with one operational unit;
- local transactions remain possible;
- lower network and deployment complexity than microservices;
- supports incremental extraction only when proven.

### Risks

- modules can become naming-only boundaries;
- shared database and utility areas can reintroduce coupling;
- internal APIs may be bypassed through direct imports;
- a “shared” module can absorb product-specific policy.

Modular monolith and Clean Architecture can be combined: each material module may have inward policy/detail boundaries without requiring identical internal layers.

## Hexagonal architecture

Core idea:

```text
primary adapters → application/domain ports ← secondary adapters
```

### Fits when

- multiple entrypoints drive the same application capability;
- external integrations are volatile or replaceable;
- policy must be tested independently from infrastructure;
- one behavioral capability has multiple adapters;
- adapter contracts are meaningful and owned by policy/consumers.

### Strengths

- clear external boundaries;
- adapter replacement and contract testing;
- domain/application logic can remain technology-independent;
- good integration vocabulary.

### Risks

- port proliferation;
- generic interfaces that mirror provider APIs;
- adapters around stable local code;
- extra mapping and wiring for trivial behavior.

Use `ports-and-adapters` for implementation mechanics after selection.

## Onion architecture

Core idea:

```text
infrastructure → application services → domain services/model
```

Dependencies point inward toward the domain model.

### Fits when

- a rich domain model is the most stable system center;
- domain rules and invariants carry high product value;
- application and infrastructure concerns can remain outside;
- DDD patterns are already justified.

### Strengths

- protects domain policy;
- emphasizes inward dependency;
- supports domain-focused testing.

### Risks

- domain-centric ceremony for transaction-oriented systems;
- artificial domain services and entities;
- unclear placement for cross-cutting application policy;
- anemic or over-modeled domain when complexity is low.

Do not select Onion solely because the project uses entities and repositories.

## Clean Architecture

Core idea:

```text
frameworks and drivers
→ interface adapters
→ application use cases
→ enterprise/domain policy
```

Conceptual dependency points inward toward stable policy.

### Fits when

- stable business/application policy must outlive delivery and infrastructure details;
- several entrypoints or providers share use cases;
- boundary translation and testability are material;
- policy, orchestration, and mechanisms have distinct change pressure;
- repository scale and team ownership justify explicit seams.

### Strengths

- explicit policy/mechanism separation;
- clear use-case intent;
- controlled framework/provider coupling;
- supports multiple delivery and infrastructure adapters;
- architecture decisions become reviewable.

### Risks

- ceremonial entities/use-cases/adapters for simple CRUD;
- fixed folder templates detached from repository conventions;
- mapping explosion;
- pass-through use cases;
- duplicated framework capabilities;
- overuse of interfaces and mocks.

Clean Architecture is a set of dependency and boundary principles, not a required four-folder tree.

## Hybrid architecture

Most real products are hybrid.

Examples:

- modular monolith at system level, layered modules by default, hexagonal boundaries for volatile integrations;
- conventional framework application with clean application policy around payments or authorization;
- rich domain module using Onion principles beside simple CRUD modules;
- direct implementation for stable utilities, explicit ports for providers.

A hybrid is valid when boundaries are intentional and reviewable, not accidental inconsistency.

## Comparison matrix

| Pressure | Direct | Layered | Modular monolith | Hexagonal | Onion | Clean |
|---|---|---|---|---|---|---|
| Simple local behavior | Strong fit | Strong fit | Usually unnecessary | Usually unnecessary | Poor fit | Poor fit |
| Multiple product capabilities | Weak | Medium | Strong | Per-module | Per-domain module | Strong when policy boundaries matter |
| Volatile integrations | Weak | Medium | Medium | Strong | Medium | Strong |
| Rich domain invariants | Medium | Medium | Strong | Strong | Strong | Strong |
| Multiple entrypoints | Weak | Medium | Medium | Strong | Medium | Strong |
| Operational simplicity | Strong | Strong | Strong | Medium | Medium | Medium |
| Low ceremony | Strong | Strong | Medium | Medium | Medium | Weak-to-medium |
| Incremental migration | Strong | Strong | Strong | Strong at seams | Bounded | Bounded |

The matrix is guidance, not scoring automation.

## Applicability decision

### RECOMMENDED

Use when multiple verified forces align and simpler approaches leave material policy/detail, adapter, testability, or ownership risk unresolved.

### ACCEPTABLE

Use when Clean Architecture fits but layered, modular, or hexagonal alternatives also satisfy the forces. Select based on repository conventions and total cost.

### NOT_JUSTIFIED

Use when:

- policy is simple and local;
- dependencies are stable;
- only one implementation/entrypoint exists;
- architecture would add pass-through layers and mapping ceremony;
- the repository already has a simpler accepted structure;
- the request is driven by fashion or folder appearance.

### NOT_VERIFIED

Use when change pressure, ownership, integration volatility, repository conventions, or quality attributes are unknown.

## Decision record

```yaml
architecture_style_comparison:
  forces: []
  candidates:
  - style: <style>
    strengths_for_current_forces: []
    unresolved_risks: []
    ceremony_and_runtime_cost: []
    migration_cost: []
    repository_fit: <high | medium | low | NOT_VERIFIED>
  selected: <style>
  applicability: RECOMMENDED | ACCEPTABLE | NOT_JUSTIFIED | NOT_VERIFIED
  rationale: <reviewable reason>
  reversal_path: <path>
```
