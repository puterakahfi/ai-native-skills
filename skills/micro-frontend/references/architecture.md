# MFE Architecture — Module Federation

## Shell App (Host)

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

## MFE (Remote)

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
