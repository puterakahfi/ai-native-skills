# MFE Isolation & Deployment

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
