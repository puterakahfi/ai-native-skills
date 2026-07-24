---
name: clean-architecture
description: Repository-aware architecture-style applicability and boundary design — compare Clean, Hexagonal, Onion, Layered, and Modular Monolith approaches; define dependency direction, policy/mechanism separation, boundary data translation, use-case orchestration, and testability without ceremonial layers.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.related_skills: '["master-engineer","implementation-context-discovery","ports-and-adapters","domain-driven-design","solid-design","design-patterns","test-driven-development","refactoring","architecture-review","code-review-workflow"]'
---

# Clean Architecture

Decide whether Clean Architecture principles are justified for the current system or bounded slice, then map stable policy, use cases, boundaries, adapters, data translation, and dependency direction into the actual repository. Prefer the smallest architecture that protects verified product and engineering forces.

## Trigger

Load this skill when:

- business or application policy is coupled to frameworks, providers, persistence, transport, or UI details;
- a feature or subsystem needs explicit policy/mechanism boundaries;
- architecture style is being selected or compared;
- a repository is considering Clean, Hexagonal, Onion, Layered, or Modular Monolith structure;
- use-case orchestration, ports, adapters, boundary DTOs, or dependency direction is unclear;
- framework replacement, integration volatility, testability, or reuse pressure is material;
- a proposed “Clean Architecture” refactor needs an applicability and over-engineering check.

Do not use this skill as:

- a universal requirement for every service, application, script, component, or CRUD surface;
- a fixed folder tree or layer-count generator;
- implementation-context discovery — use `implementation-context-discovery` first for existing repositories;
- port and adapter implementation procedure — use `ports-and-adapters` when that pattern is selected;
- domain-model design — use `domain-driven-design` when domain complexity justifies it;
- architecture ownership or approval — `master-engineer` owns the decision and `architecture-review` independently verifies implementation;
- permission to rewrite the whole system when a bounded correction is sufficient.

## Core Boundary

```text
clean-architecture
  owns:
    architecture-style applicability verdict
    comparison of viable architecture approaches
    policy versus mechanism map
    dependency-rule design
    boundary and owner map
    boundary data translation decision
    use-case orchestration boundary
    repository-aware implementation mapping
    migration slice and stop-condition guidance

  delegates:
    repository canonicality and conventions → implementation-context-discovery
    final architecture ownership and ADR → master-engineer
    port and adapter mechanics → ports-and-adapters
    domain model and aggregate design → domain-driven-design
    object and interface quality → solid-design
    pattern implementation → design-patterns
    behavior-preserving structural execution → refactoring
    independent compliance verdict → architecture-review
    merge-readiness lifecycle → code-review-workflow
```

## Hard Rules

```text
1. Applicability before architecture style.
   Start from verified forces, not the Clean Architecture label.

2. No fixed layer count.
   Entities, use cases, interface adapters, and frameworks are conceptual boundaries,
   not mandatory folders or one-to-one packages.

3. Repository context before mapping.
   Existing contracts, modules, conventions, aliases, frameworks, and migration state
   determine the implementation shape.

4. Dependency direction protects stable policy.
   Source dependencies should point toward stable policy where that policy/detail boundary
   is material; do not invert dependencies merely for symmetry.

5. Framework independence is not framework avoidance.
   Framework code belongs at accepted boundaries; useful framework capabilities need not
   be reimplemented behind pointless wrappers.

6. Boundary data is translated deliberately.
   HTTP, ORM, provider, queue, UI, and transport types must not leak into stable policy
   when they couple policy to volatile detail.

7. Use cases orchestrate application intent.
   They do not absorb domain invariants, provider mechanics, controller formatting,
   or generic transaction ceremony without ownership evidence.

8. Ports exist for meaningful boundaries.
   Do not create one interface per class, one port per method, or adapters around stable
   local code without a proven capability boundary.

9. Testability is a consequence of clear boundaries, not mock abundance.
   Prefer behavior tests at the smallest meaningful boundary.

10. Choose the smallest durable architecture.
    A modular monolith, conventional layered module, or direct implementation may be
    cleaner than ceremonial Clean Architecture.
```

## Required Inputs

```yaml
clean_architecture_context:
  system_or_slice: <required>
  system_goal: <required>
  existing_repository: <reference | greenfield>
  implementation_context_profile: <reference | NOT_VERIFIED>
  engineering_contract: <reference | NOT_VERIFIED>
  architecture_decisions: []
  business_and_application_policy: []
  volatile_details: []
  integrations: []
  data_and_transaction_boundaries: []
  consumers_and_entrypoints: []
  change_pressure: []
  quality_attributes: []
  constraints: []
  migration_state: <none | bounded | active | NOT_VERIFIED>
  verification_plan: []
```

When repository conventions, policy ownership, or change pressure are missing, report `NOT_VERIFIED` for dependent decisions rather than inventing generic folders.

## Procedure

### 1. Frame the architecture decision

Name the exact system or bounded slice, goal, scope, non-goals, forces, constraints, existing architecture, and expected decision.

Separate:

```text
architecture-style decision
boundary correction
migration
review-only request
```

Do not turn a local dependency violation into a system-wide redesign automatically.

### 2. Load repository and authority context

For an existing repository, consume `implementation-context-discovery` evidence:

- canonical framework and runtime;
- accepted module and folder conventions;
- existing domain/application/infrastructure boundaries;
- shared abstractions and integration adapters;
- testing and build conventions;
- migration targets, legacy areas, exceptions, and ADRs;
- approved dependencies and prohibited parallel systems.

If a material architecture change lacks authority, route it through `decision-provenance` and `master-engineer`.

### 3. Identify forces

Record forces such as:

```text
business-rule complexity
provider or framework volatility
multiple entrypoints
multiple persistence or integration adapters
independent testability
reuse across delivery mechanisms
transaction and consistency ownership
team/module ownership
release independence
migration cost
operational simplicity
latency and runtime overhead
```

Do not claim framework independence, replaceability, or testability as goals unless they solve a verified risk.

### 4. Decide applicability

Classify the current system or slice:

```text
RECOMMENDED
  clean inward dependency and policy/mechanism boundaries materially reduce verified risk

ACCEPTABLE
  the approach fits, but simpler alternatives are also viable and trade-offs decide

NOT_JUSTIFIED
  ceremonial layers and indirection would exceed the verified benefit

NOT_VERIFIED
  evidence is insufficient for a responsible architecture-style verdict
```

Load [references/style-applicability-and-comparison.md](references/style-applicability-and-comparison.md) to compare Clean, Hexagonal, Onion, Layered, and Modular Monolith approaches.

### 5. Map policy and mechanism

```yaml
policy_mechanism_map:
  stable_policy: []
  application_orchestration: []
  volatile_mechanisms: []
  entrypoints: []
  external_systems: []
  transaction_owner: <owner | NOT_VERIFIED>
  dependency_violations: []
```

Stable policy includes business or application decisions that should not change merely because a database, framework, provider, transport, or UI changes.

Mechanisms include persistence, HTTP, queues, filesystems, provider SDKs, frameworks, schedulers, and presentation concerns.

### 6. Define boundaries and dependency rule

For each material boundary, record:

```yaml
boundary:
  name: <capability or seam>
  policy_owner: <module>
  outer_detail: <adapter or mechanism>
  allowed_dependency_direction: <direction>
  contract_owner: <consumer or policy>
  boundary_data: <domain/application type or translated DTO>
  failure_contract: <errors and recovery>
  transaction_contract: <scope>
  test_boundary: <evidence>
```

Load [references/boundaries-data-and-migration.md](references/boundaries-data-and-migration.md) for boundary translation, use cases, transaction ownership, migration slicing, and verification.

### 7. Design use-case orchestration

A use case should express one application intention and coordinate domain behavior plus required capabilities.

Keep separate when material:

- domain invariants and calculations;
- application sequencing and authorization intent;
- infrastructure mechanics;
- transport parsing and response formatting;
- persistence mapping;
- event/provider translation.

Do not create use-case classes for trivial pass-through behavior merely to satisfy a diagram.

### 8. Decide ports and adapters selectively

Use a port when stable policy needs a capability supplied by a volatile or external detail, or when multiple adapters must preserve one meaningful behavioral contract.

Do not create a port when:

- dependency is stable and local;
- there is no policy to protect;
- the abstraction only mirrors a provider API;
- the repository already owns an accepted boundary abstraction;
- a direct implementation is easier to test and change.

When selected, hand off port definitions and adapter implementation to `ports-and-adapters`.

### 9. Map the decision to the actual repository

Produce concrete expected paths, owners, imports, contracts, wiring location, and prohibited dependency edges using repository conventions.

Do not return generic directories such as `domain/`, `usecases/`, or `infrastructure/` unless they are accepted or explicitly approved for the target repository.

### 10. Plan bounded migration

For existing code, define the smallest safe sequence:

```text
protect behavior
→ establish boundary test
→ isolate one policy/detail seam
→ translate boundary data
→ move dependency direction
→ verify
→ stop or continue only with accepted evidence
```

Do not combine feature changes, framework migration, domain redesign, and full architecture rewrite in one unbounded slice.

### 11. Verify independently

Define evidence for:

- dependency/import direction;
- policy tests without unnecessary infrastructure;
- adapter integration behavior;
- transaction and failure semantics;
- API/event/data compatibility;
- runtime, performance, and operational consequences;
- independent `architecture-review`.

A diagram, folder layout, compilation result, or mock-heavy unit suite does not prove architecture acceptance.

## Output Contract

```yaml
clean_architecture_decision:
  applicability: RECOMMENDED | ACCEPTABLE | NOT_JUSTIFIED | NOT_VERIFIED
  system_or_slice: <reference>
  goal_and_forces: []
  repository_context: <reference | NOT_VERIFIED>
  selected_architecture_style: <clean | hexagonal | onion | layered | modular-monolith | hybrid | direct>
  alternatives_considered: []
  policy_mechanism_map:
    stable_policy: []
    application_orchestration: []
    volatile_mechanisms: []
  dependency_rule: []
  boundary_and_owner_map: []
  boundary_data_translation: []
  use_case_orchestration: []
  ports_and_adapters_needed: []
  repository_mapping: []
  prohibited_dependency_edges: []
  migration_sequence: []
  stop_conditions: []
  tradeoffs: []
  verification_plan: []
  evidence_gaps: []
  handoffs: []
```

## Quality Gates

- [ ] Exact system/slice, goal, scope, forces, and non-goals are explicit?
- [ ] Existing repository conventions and decisions were inspected or marked `NOT_VERIFIED`?
- [ ] Applicability is `RECOMMENDED`, `ACCEPTABLE`, `NOT_JUSTIFIED`, or `NOT_VERIFIED` with evidence?
- [ ] At least one simpler architecture alternative was considered?
- [ ] Stable policy and volatile mechanisms are distinguished?
- [ ] Dependency direction is defined only for material boundaries?
- [ ] Boundary data translation, failure semantics, and transaction ownership are explicit?
- [ ] Ports and adapters are introduced only for proven boundaries?
- [ ] Framework usage is bounded without pointless reimplementation?
- [ ] Repository mapping uses actual accepted paths and imports?
- [ ] Migration is bounded with preservation locks and stop conditions?
- [ ] Verification and independent architecture acceptance remain separate?

## Failure Signals

```text
CLEAN_ARCHITECTURE_EVERYWHERE
FIXED_LAYER_COUNT
GENERIC_FOLDER_TEMPLATE
FRAMEWORK_BAN
PORT_FOR_EVERY_CLASS
ADAPTER_AROUND_EVERY_DEPENDENCY
USE_CASE_PASS_THROUGH_CEREMONY
ORM_OR_TRANSPORT_TYPE_LEAK
DOMAIN_IMPORTS_INFRASTRUCTURE
MOCK_COUNT_EQUALS_TESTABILITY
FULL_REWRITE_WITHOUT_SLICE
REPOSITORY_CONTEXT_MISSING
DIAGRAM_EQUALS_ACCEPTANCE
SELF_APPROVED_ARCHITECTURE
```

## Handoff

- To `master-engineer`: applicability decision, selected style, forces, alternatives, trade-offs, and ADR requirement.
- To `implementation-context-discovery`: missing canonicality, convention, path, import, dependency, or migration evidence.
- To `ports-and-adapters`: selected ports, contracts, adapters, wiring, and behavioral tests.
- To `domain-driven-design`: verified domain complexity, bounded context, aggregate, value object, or domain-event concerns.
- To `solid-design`: object, responsibility, interface, substitution, or dependency-direction findings below architecture level.
- To `refactoring`: behavior-preserving migration slice with tests, preservation locks, and stop condition.
- To `architecture-review`: implemented boundary map, dependency rules, repository mapping, evidence, and unresolved gaps.
- To `code-review-workflow`: architecture decision reference and independent review inputs.
