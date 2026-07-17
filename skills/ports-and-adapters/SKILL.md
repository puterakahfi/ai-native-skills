---
name: ports-and-adapters
description: Design hexagonal architecture with explicit ports and adapters — domain isolation, dependency inversion, testable domain without infrastructure. Foundation pattern for DDD, microservices, and clean architecture.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/domain-architecture/ports-and-adapters.contract.yaml
---

# Ports and Adapters (Hexagonal Architecture)

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
