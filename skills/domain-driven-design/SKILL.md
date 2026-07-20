---
name: domain-driven-design
description: Model complex domains using DDD building blocks — bounded contexts, aggregates, value objects, domain events, ubiquitous language, and repository pattern. Strategic and tactical design.
license: MIT
metadata:
  ai-native-skills.version: 1.0.1
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/architecture/domain-driven-design.contract.yaml
  ai-native-skills.contract-version: "~0.1"
---

# Domain-Driven Design

## Reviewed core contract interface

Source: `ai-native-core/contracts/skills/architecture/domain-driven-design.contract.yaml` · compatible line: `~0.1`

```yaml
required_inputs:
- domain_description
allowed_outputs:
- bounded_context_map
- aggregate_design
- ubiquitous_language_glossary
- domain_event_catalog
- context_map_relationships
- repository_interface_definitions
quality_gates:
- every_aggregate_must_have_a_single_root
- value_objects_must_be_immutable
- domain_events_must_be_named_in_past_tense
- ubiquitous_language_must_be_consistent_across_bounded_context
- repositories_must_only_return_aggregates_not_raw_entities
- no_domain_logic_in_application_or_infrastructure_layer
- bounded_context_boundaries_must_be_explicit
- context_map_must_define_upstream_downstream_relationships
```

Each aggregate has one root, value objects are immutable, domain events use past-tense domain language, and every context map names upstream and downstream relationships. Keep domain logic inside the domain boundary.

Keep this interface synchronized with the pinned core contract. Exact declarations make ownership reviewable; they do not replace runtime, repository, architecture, test, or product evidence.


> **HARD RULES**
> - **Ubiquitous language first** — model reflects domain vocabulary, not technical vocabulary
> - **Bounded context = explicit boundary** — never share domain models across context boundaries; share only via contract
> - **Aggregate root owns consistency** — all invariants enforced through the root; one aggregate = one transaction

## When to Use

- Modeling a new domain or subdomain
- Refactoring a Big Ball of Mud into bounded contexts
- Designing service boundaries for microservices
- When business complexity > technical complexity
- Before writing a single line of domain code

**Do NOT use** for CRUD-only apps, simple scripts, or cases where the domain is trivially thin.

---

## References

| Topic | File |
|---|---|
| Strategic Design — Bounded Contexts, Context Map, Relationship Patterns | [references/strategic-design.md](references/strategic-design.md) |
| Tactical Design — Entities, Value Objects, Aggregates, Domain Events, Repositories, Domain Services, Ubiquitous Language, Layer Architecture, Anti-Patterns, Checklist | [references/tactical-design.md](references/tactical-design.md) |

---

## Quick Decision Guide

```
Defining service boundaries?             → Bounded context + context map, see strategic-design.md
Two contexts need to share data?         → Context relationship patterns (ACL, OHS), see strategic-design.md
Business rule belongs to which object?   → Entity vs Value Object vs Domain Service, see tactical-design.md
Enforcing invariants across related objects? → Aggregate root, see tactical-design.md
Domain uses different words than code?   → Ubiquitous language, see tactical-design.md
Logic leaking into application layer?    → Layer architecture, see tactical-design.md
```
