---
name: micro-frontend
description: Design micro-frontend architecture with module federation — MFE boundary by bounded context, shell app contract, CSS isolation, shared dependency strategy, independent deployability, and fallback strategy.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/experience-design/micro-frontend.contract.yaml
  ai-native-skills.related_skills: '[''service-design'', ''domain-driven-design'', ''design-patterns'', ''api-contract'']'
---

# Micro-Frontend (MFE)

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

## Architecture: Module Federation

### Shell App (Host)

```javascript
// webpack.config.js — Shell (Host)
const { ModuleFederationPlugin } = require('webpack').container;

module.exports = {
  plugins: [
    new ModuleFederationPlugin({
      name: 'shell',
      remotes: {
        checkout:  'checkout@https://checkout.app.com/remoteEntry.js',
        catalog:   'catalog@https://catalog.app.com/remoteEntry.js',
        account:   'account@https://account.app.com/remoteEntry.js',
      },
      shared: {
        react:     { singleton: true, requiredVersion: '^18.0.0' },
        'react-dom': { singleton: true, requiredVersion: '^18.0.0' },
      },
    }),
  ],
};
```

### MFE (Remote)

```javascript
// webpack.config.js — CheckoutMFE (Remote)
module.exports = {
  plugins: [
    new ModuleFederationPlugin({
      name: 'checkout',
      filename: 'remoteEntry.js',
      exposes: {
        './CheckoutApp': './src/bootstrap',  // expose entry point only
      },
      shared: {
        react:     { singleton: true, requiredVersion: '^18.0.0' },
        'react-dom': { singleton: true, requiredVersion: '^18.0.0' },
      },
    }),
  ],
};
```

---

## Shell App Contract

The shell must define a stable contract for all MFEs:

```typescript
// shell-contract.ts — published to all MFE teams
export interface ShellContract {
  // Auth context — MFE reads, never owns
  auth: {
    user: User | null;
    token: string | null;
    logout: () => void;
  };

  // Navigation — MFE calls shell to navigate
  navigate: (path: string) => void;

  // Event bus — MFE-to-MFE communication (no direct import)
  eventBus: {
    emit: (event: string, payload: unknown) => void;
    on:   (event: string, handler: (payload: unknown) => void) => void;
    off:  (event: string, handler: (payload: unknown) => void) => void;
  };

  // Design tokens — shared, never duplicated
  theme: DesignTokens;
}
```

**Rule:** MFEs receive shell contract via props or context — never import from each other directly.

---

## No Direct Import Across MFE Boundaries

```typescript
// ❌ Wrong — CheckoutMFE importing from CatalogMFE
import { ProductCard } from 'catalog/ProductCard';

// ✅ Correct — shell provides shared UI via design system package
import { ProductCard } from '@company/design-system';

// ✅ Correct — communicate via event bus
shellContract.eventBus.emit('product.selected', { productId: 'prd-001' });
```

---

## Shared Dependencies Strategy

```
Singleton dependencies (one version across all MFEs):
  - react, react-dom         → version must match exactly
  - routing library           → shell owns routing
  - auth library              → shell owns auth

Versioned dependencies (each MFE owns its version):
  - business logic libraries  → MFE-specific
  - UI component library      → from shared design system package

Design system:
  @company/design-system      → published NPM package, versioned
  Tokens, base components     → shared, each MFE imports same version
```

---

## CSS Isolation

```typescript
// Option A: CSS Modules (recommended for React)
import styles from './CheckoutApp.module.css';
// Generates: .CheckoutApp_button__abc123 — scoped automatically

// Option B: Shadow DOM (Web Components)
class CheckoutElement extends HTMLElement {
  connectedCallback() {
    const shadow = this.attachShadow({ mode: 'open' });
    // styles here are fully isolated
  }
}

// Option C: BEM with MFE prefix namespace
.checkout-mfe__button { }
.checkout-mfe__form { }

// ❌ Never: global CSS from MFE
body { font-size: 14px; }  // leaks to entire page
```

---

## Fallback Strategy

What happens when an MFE fails to load:

```typescript
// Shell — lazy load with fallback
const CheckoutApp = React.lazy(() =>
  import('checkout/CheckoutApp').catch(() => ({
    default: () => <ErrorBoundary message="Checkout is temporarily unavailable" />
  }))
);

// ErrorBoundary per MFE mount point
<Suspense fallback={<LoadingSpinner />}>
  <ErrorBoundary fallback={<MFEErrorFallback name="checkout" />}>
    <CheckoutApp contract={shellContract} />
  </ErrorBoundary>
</Suspense>
```

**Rule:** One MFE failing must not crash the shell or other MFEs.

---

## Independent Deployment

```
Each MFE deploys independently — shell does not redeploy when MFE changes.

Deployment flow per MFE:
  1. MFE CI passes → build → upload remoteEntry.js to CDN
  2. Shell reads remoteEntry.js at runtime (not build time)
  3. No shell rebuild needed

Version pinning (optional):
  remotes: {
    checkout: 'checkout@https://cdn.app.com/checkout/1.2.3/remoteEntry.js'
  }
  → explicit version — shell controls which MFE version to use
```

---

## MFE Design Checklist

Before designing MFE architecture:
- [ ] Forces justify MFE (team independence, release cadence, tech migration)?
- [ ] MFE boundaries align with bounded contexts?
- [ ] Shell contract defined and published to all MFE teams?
- [ ] No direct imports across MFE boundaries?
- [ ] Shared dependencies strategy declared (singleton vs versioned)?
- [ ] CSS isolated per MFE — no global style leakage?
- [ ] Design tokens from shared package, not duplicated?
- [ ] Fallback strategy for MFE load failure?
- [ ] Each MFE independently deployable?
- [ ] Event bus for cross-MFE communication (not direct import)?
