---
name: micro-frontend
description: Design micro-frontend architecture with module federation — MFE boundary by bounded context, shell app contract, CSS isolation, shared dependency strategy, independent deployability, and fallback strategy.
license: MIT
metadata:
  ai-native-skills.version: 1.0.1
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/architecture/micro-frontend.contract.yaml
  ai-native-skills.contract-version: "~0.1"
  ai-native-skills.related_skills: "['service-design', 'domain-driven-design', 'design-patterns', 'api-contract']"
---

# Micro-Frontend (MFE)

## Reviewed core contract interface

Source: `ai-native-core/contracts/skills/architecture/micro-frontend.contract.yaml` · compatible line: `~0.1`

```yaml
required_inputs:
- application_description
allowed_outputs:
- mfe_boundary_map
- shell_app_contract
- module_federation_config
- shared_dependency_strategy
- css_isolation_strategy
- independent_deployment_plan
quality_gates:
- mfe_boundary_must_align_with_bounded_context
- each_mfe_must_be_independently_deployable
- shell_contract_must_define_routing_and_shared_state
- css_must_be_isolated_per_mfe
- shared_dependencies_must_be_explicitly_declared
- no_direct_import_across_mfe_boundaries
- design_token_sharing_strategy_must_be_defined
- fallback_strategy_must_exist_when_mfe_fails_to_load
```

A proposed MFE boundary must support independent deployment, isolated CSS, an explicit design-token sharing strategy, declared shared dependencies, and a fallback when a remote fails to load.

Keep this interface synchronized with the pinned core contract. Exact declarations make ownership reviewable; they do not replace runtime, repository, architecture, test, or product evidence.


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
