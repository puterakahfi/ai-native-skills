# DDD Strategic Design

## Bounded Context

A bounded context is the explicit boundary within which a domain model applies. Same word, different meaning across contexts = separate bounded contexts.

```
E-commerce example:

  [Sales Context]         [Shipping Context]       [Support Context]
  Product = SKU + price   Product = physical item   Product = what customer bought
  Customer = buyer        Customer = delivery addr  Customer = ticket opener

  Same word "Product" — 3 different models — 3 bounded contexts
```

**Rules:**
- One team owns one bounded context
- Ubiquitous language is consistent WITHIN a context, can differ ACROSS contexts
- Never share domain models across bounded context boundaries — share only via contract

---

## Context Map — Relationships Between Contexts

```yaml
context_relationships:
  - upstream: SalesContext
    downstream: ShippingContext
    pattern: Customer-Supplier   # upstream must meet downstream needs

  - upstream: IdentityContext
    downstream: SalesContext
    pattern: Open-Host-Service   # upstream publishes stable API

  - upstream: LegacyERP
    downstream: InventoryContext
    pattern: Anti-Corruption-Layer  # downstream translates, never lets upstream model leak
```

**Relationship patterns:**
| Pattern | Description |
|---|---|
| Shared Kernel | Two contexts share a small model — changes need coordination |
| Customer-Supplier | Upstream commits to downstream needs |
| Conformist | Downstream conforms to upstream model (no power to negotiate) |
| Anti-Corruption Layer (ACL) | Downstream translates upstream model — prevents model pollution |
| Open-Host Service | Upstream publishes protocol for many downstreams |
| Published Language | Shared well-documented language (OpenAPI, Protobuf) |
