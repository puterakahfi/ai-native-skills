# A11y & Usage Rules

> Icons without accessibility attributes are invisible to screen readers.

## Functional vs Decorative

```
FUNCTIONAL ICON (carries meaning, no text label):
  → aria-label required on the element OR title inside SVG
  → Example: icon-only close button, standalone nav icon

  <button aria-label="Close dialog">
    <svg aria-hidden="true">...</svg>
  </button>

DECORATIVE ICON (icon + visible text label):
  → aria-hidden="true" on SVG — screen reader reads text, not icon
  → Example: icon next to "Settings" text label

  <button>
    <svg aria-hidden="true" focusable="false">...</svg>
    Settings
  </button>

RULE: Never naked SVG without one of these two patterns.
```

## Touch Target Rule

```
Minimum touch target: 44 × 44px (Apple HIG + WCAG 2.5.5)
Visual icon can be smaller — padding makes up the difference:

  /* 20px icon, 44px touch target */
  .icon-btn {
    width: 44px;
    height: 44px;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 12px;
  }
```

## Usage Rules

```
RULE 1 — Icon + text preferred over icon alone
  Exception: universally understood (✕ close, ☰ menu, ← back)
  Even then: add aria-label

RULE 2 — Consistent icon for consistent action
  Search always = magnifier. Never swap icons for same action across pages.

RULE 3 — No icon for decoration in body text
  Icons in body prose = visual noise. Reserve for navigation, buttons, status.

RULE 4 — Color contrast applies to icons too
  Icon on bg ≥ 3:1 contrast (WCAG 1.4.11 non-text contrast)
  Use readability skill for contrast check

RULE 5 — Loading/animated icons need prefers-reduced-motion
  @media (prefers-reduced-motion: reduce) { animation: none; }
```

## Icon + Status Pattern

```html
<!-- Live status dot (zen site pattern) -->
<span class="status-dot" aria-label="Status: Live" role="img"></span>

<!-- Status with icon -->
<span aria-label="Error">
  <svg aria-hidden="true"><!-- error icon --></svg>
  <span>Failed to load</span>
</span>
```
