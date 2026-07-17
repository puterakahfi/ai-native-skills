# Section Patterns + Form Patterns + State Patterns + Anti-Pattern Catalog

## Section Patterns

### Section Flow for Personal Pages

```
Optimal flow (proven by eye-tracking studies):

  1. HERO          → who are you + stance (100vh)
  2. WORK          → what have you built (LIVE only)
  3. ABOUT         → who you are in depth
  4. CONTACT        → how to reach you

  Between each: visual break (alternating bg, border, or space)
  Each section: different padding weight (hero > content > contact)
```

### Section Break Patterns

```
Option A: Alternating background
  Hero:    --bg
  Work:    --bg-alt (subtle difference)
  About:   --bg
  Contact: --bg-alt (or --bg with top border)

Option B: Border separators only
  All sections: same --bg
  Separated by: border-top: 1px solid var(--border)

Option C: Whitespace only
  All sections: same --bg
  Separated by: larger padding (--space-11 between sections)

Choose ONE and apply consistently.
```

---

## Form Patterns

### Input Field Spec

```
Height:      40–48px (desktop), 48–56px (mobile — Fitts's Law)
Padding:     12–16px horizontal
Border:      1px solid var(--border) → focus: var(--accent)
Label:       above input (never placeholder-only — a11y fail)
Error:       below input, var(--danger), icon + text
Required:    asterisk next to label, explain in form description

Anti-patterns:
  ❌ Placeholder as label — disappears on focus, a11y fail
  ❌ Input height < 44px — touch target too small
  ❌ Error only on submit — validate on blur
```

---

## State Patterns

Every interactive component needs ALL states designed:

```
States required for every interactive element:
  Default   → what it looks like normally
  Hover     → subtle feedback (background, color change)
  Focus     → visible outline for keyboard nav (2px, offset)
  Active    → pressed/clicked state
  Disabled  → opacity 0.4, cursor not-allowed, no interaction
  Loading   → skeleton or spinner in-place
  Error     → red border + message
  Success   → green confirmation

Missing ANY state = incomplete design.
Common mistake: design default + hover, ship without focus/error/loading.
```

---

## Anti-Pattern Catalog

| Anti-Pattern | Problem | Fix |
|---|---|---|
| Hamburger on desktop | Forces extra click, hides navigation | Horizontal nav for ≥ 5 items |
| Card grid with 2 items in 4 cols | Looks broken/unfinished | Stack or use 2-col |
| Infinite scroll on portfolio | User loses position | Paginate or load-more button |
| Full-width text lines | > 75 chars = hard to track | max-width: 65ch on prose |
| Primary nav > 6 items flat | Cognitive overload | Group into dropdowns |
| Hover-only state | Inaccessible on touch, keyboard | Add focus + active state |
| Icon-only buttons | No label = confusion | Icon + visible label or tooltip |
| Carousel auto-advance | User loses control | Manual only, or pause on hover |
| Modal on page load | Intrudes before user has context | Trigger only on explicit action |
| Nested cards (card in card) | Visual confusion, unclear clickable area | Flatten or use different component |
| Placeholder as label | Disappears on focus, a11y fail | Always use visible label above input |
| Input height < 44px | Touch target too small | 40–48px desktop, 48–56px mobile |
| Error only on submit | User finds out too late | Validate on blur |
