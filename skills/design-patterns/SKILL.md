---
name: design-patterns
description: Identify and apply appropriate design patterns — GoF creational, structural, behavioral, and modern architectural patterns (CQRS, Saga, Outbox). Pattern selection justified by forces, not preference.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/architecture/design-patterns.contract.yaml
  ai-native-skills.contract-version: "~0.1"
---

# Design Patterns

> **Patterns solve communication problems, not just code problems. Name the pattern explicitly so teammates share the vocabulary. Don't force a pattern where no forces exist.**

## The Core Rule

```
Pattern selection must be justified by forces, not preference.

Forces = the problem pressures that make a pattern the right fit.
Without forces → no pattern. Impose a pattern without forces = over-engineering.
```

---

## Pattern Selection Process

```
1. Name the problem in one sentence
2. Identify the forces (why naive solution fails)
3. Consider 2-3 candidate patterns
4. Pick the one whose forces match closest
5. State the trade-offs explicitly
6. Implement — name the pattern in code
```

---

## Pattern Selection Cheat Sheet

| Problem | Candidate Patterns |
|---|---|
| Need different algorithm at runtime | Strategy |
| Incompatible interface to integrate | Adapter |
| Add behavior without subclassing | Decorator |
| Complex object construction | Builder |
| Notify multiple objects on change | Observer / Event |
| Encapsulate request as object | Command |
| Simplify complex subsystem | Facade |
| Complex composable business rules | Specification |
| Multi-service transaction | Saga |
| Atomic DB write + event publish | Outbox |
| Different read/write complexity | CQRS |

---

## Anti-Patterns to Catch

| Anti-Pattern | Signal | Correct Pattern |
|---|---|---|
| Pattern worship | "Let's use CQRS" without stating forces | Justify by forces first |
| God Object | One class does everything | SRP + Strategy/Facade decomposition |
| Anemic Model | Entities with only getters/setters, logic in services | Move logic to entities |
| Premature abstraction | Interface with one implementation | Wait for second implementation |
| Singleton abuse | Singleton for non-singleton concern | DI container binding |
| Leaky abstraction | Adapter exposes internal types | Translate to domain types at boundary |

---

## References

- [Creational & Structural Patterns](references/creational-structural.md) — Factory Method, Builder, Singleton, Adapter, Decorator, Facade
- [Behavioral Patterns](references/behavioral.md) — Strategy, Observer/Event, Command, Specification
- [Architectural Patterns](references/architectural.md) — CQRS, Saga, Outbox
