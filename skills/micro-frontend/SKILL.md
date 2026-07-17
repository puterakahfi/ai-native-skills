---
name: micro-frontend
description: Design micro-frontend architecture with module federation — MFE boundary by bounded context, shell app contract, CSS isolation, shared dependency strategy, independent deployability, and fallback strategy.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/architecture/micro-frontend.contract.yaml
  ai-native-skills.related_skills: "['service-design', 'domain-driven-design', 'design-patterns', 'api-contract']"
---

# Micro-Frontend (MFE)

## HARD RULES

```
1. Domain boundary = MFE boundary (bounded context → MFE, never per-page or per-feature)
2. No direct imports across MFE boundaries — use event bus or shell contract
3. Shared dependencies via singleton scope only — one version, enforced in webpack config
4. One MFE failing must not crash the shell or other MFEs
```

---

## When to Use

```
Forces that justify MFE:
  - Multiple teams independently develop and deploy frontend features
  - Different parts of the UI have different release cadences
  - Tech stack migration needed (e.g. Angular → React) without full rewrite
  - Frontend is as complex as the backend and needs same decomposition

Without these forces → single SPA. MFE is complexity. Justify it.
```

---

## MFE Boundary — Align with Bounded Context

Same rule as microservices: MFE boundary = bounded context boundary.

```
E-commerce — bounded context → MFE map:

  [Sales Context]      → CheckoutMFE
  [Catalog Context]    → ProductCatalogMFE
  [Account Context]    → AccountMFE
  [Order Context]      → OrderHistoryMFE
  [Shell]              → ShellApp (routing, auth, shared layout)
```

**Wrong:** MFE per page or per feature within a context — too granular.
**Wrong:** MFE that crosses bounded context — same mistake as distributed monolith.

---

## References

- **[Architecture](references/architecture.md)** — Module Federation config (Shell + MFE), Shell Contract, No Direct Import rule, Shared Dependencies strategy
- **[Isolation & Deployment](references/isolation-deployment.md)** — CSS Isolation options, Fallback Strategy, Independent Deployment, MFE Design Checklist

---

## Quick Decision

```
New frontend feature → bounded context exists? → new MFE or extend existing MFE in that context
Cross-context UI?    → shell contract + event bus, never direct import
Shared component?    → @company/design-system package, not copy-paste
MFE fails to load?   → ErrorBoundary fallback per mount point
```
