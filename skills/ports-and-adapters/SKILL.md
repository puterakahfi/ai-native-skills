---
name: ports-and-adapters
description: Design hexagonal architecture with explicit ports and adapters — domain isolation, dependency inversion, testable domain without infrastructure. Foundation pattern for DDD, microservices, and clean architecture.
license: MIT
metadata:
  ai-native-skills.version: 1.0.1
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/architecture/ports-and-adapters.contract.yaml
  ai-native-skills.contract-version: "~0.1"
---

# Ports and Adapters (Hexagonal Architecture)

## Reviewed core contract interface

Source: `ai-native-core/contracts/skills/architecture/ports-and-adapters.contract.yaml` · compatible line: `~0.1`

```yaml
required_inputs:
- component_or_feature
allowed_outputs:
- port_definitions
- adapter_implementations
- dependency_graph
- architecture_decision_record
quality_gates:
- domain_must_not_depend_on_infrastructure
- ports_must_be_defined_as_interfaces_in_domain_layer
- adapters_must_implement_ports_not_the_other_way
- all_external_dependencies_must_cross_via_port
- domain_logic_must_be_testable_without_infrastructure
- no_framework_imports_in_domain_layer
- primary_ports_drive_the_domain_secondary_ports_are_driven_by_domain
- dependency_inversion_principle_enforced_at_every_boundary
```

Every external dependency crosses a named port, adapters implement ports, and dependency inversion is enforced at every boundary. Framework and infrastructure imports do not enter the domain.

Keep this interface synchronized with the pinned core contract. Exact declarations make ownership reviewable; they do not replace runtime, repository, architecture, test, or product evidence.


> **HARD RULES**
> - Ports = input boundaries only — defined in Domain layer, never in Infrastructure
> - Adapters implement ports, never call each other directly
> - Domain never imports infrastructure — dependency flows inward only

## Quick Reference

| Phase | What to Do | Reference |
|---|---|---|
| Architecture & Ports | Understand the 3 layers, define port interfaces, implement infrastructure + primary adapters | [architecture-and-adapters.md](references/architecture-and-adapters.md) |
| App Service, DI & Testing | Wire application service, bind adapters via DI, use in-memory adapters for tests | [application-service-and-testing.md](references/application-service-and-testing.md) |

## When to Use This Skill

- Starting a new service or bounded context
- Adding a new integration (DB, payment, email, queue)
- Writing domain tests that run fast without infrastructure
- Reviewing a PR for architectural violations

## Decision Flow

```
New feature required?
  └─ Does it touch infrastructure (DB, email, payment, queue)?
       ├─ YES → Define port in Domain/Port/, implement adapter in Infrastructure/
       └─ NO  → Pure domain logic, no port needed

Adding a new external consumer (REST, CLI, queue)?
  └─ Create primary adapter in Interface/ that drives domain via Application Service
```

## Architecture Summary

```
[REST/CLI/Queue] → PRIMARY PORTS → [DOMAIN] → SECONDARY PORTS → [DB/Email/Bus]

Dependency direction: Adapters → Ports ← Domain
NEVER: Domain → Adapter (direct)
```

## Gates

- [ ] Port interfaces in Domain/Port/ only (no framework imports)?
- [ ] Adapters in Infrastructure/ or Interface/ only?
- [ ] Application service orchestrates — zero domain logic in UseCase?
- [ ] Domain tests use in-memory adapters (no real DB/HTTP)?
- [ ] No `use Illuminate\...` (or framework equivalent) in Domain/?

## Common Violations

| Violation | Fix |
|---|---|
| `use Illuminate\...` in Domain/ | Extract to adapter |
| `EloquentModel` in Domain/Order/ | Move to Infrastructure/ |
| `DB::table()` in entity method | Define port, inject adapter |
| Business rule in UseCase | Move to domain object |
| Interface defined in Infrastructure/ | Move to Domain/Port/ |

---

Load [architecture-and-adapters.md](references/architecture-and-adapters.md) for layer diagram, port definitions, and adapter implementation examples.

Load [application-service-and-testing.md](references/application-service-and-testing.md) for orchestration layer, DI wiring, in-memory adapters, folder structure, and violation table.
