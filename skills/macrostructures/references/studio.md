# Macrostructure 07 · Studio

> Image-led, split 50/50. Portfolio, personal page, creative studio.

```
Layout lead:    image-led, left-aligned, split 50/50
Heading:        Left, stacked — name then descriptor
Body:           Project list — cards on right panel, identity on left
Dividers:       Minimal — 1px border between left/right panels, between cards
Button voice:   Arrow links (↗), not buttons
Image:          Central — full-width project screenshots or photos
Reveal:         Stagger left sequence first, then right cards

When to use:    Portfolio, personal page, creative studio, photographer
When NOT:       Text-heavy content, SaaS product, personal blog
```

## Split-Panel Layout Rules (MANDATORY)

Failing to follow these causes gray void and broken balance — most common Studio bug.

```css
/* Hero wrapper (outer) */
.hero { min-height: 100vh; display: flex; flex-direction: column; padding-top: 80px; }
/* ↑ nav clearance here ONCE — not inside panels */

/* Hero grid */
.hero-grid { flex: 1; display: grid; grid-template-columns: 1fr 1fr; align-items: stretch; }

/* Left panel */
.hero-left {
  display: flex; flex-direction: column; justify-content: center;
  border-right: 1px solid var(--border);
  padding: var(--sp-9) var(--sp-8);
  /* equal top/bottom → justify-content:center works correctly */
  /* DO NOT add extra top padding here — shifts center down */
}

/* Right panel */
.hero-right { display: flex; flex-direction: column; gap: 1px; background: var(--border); padding: 0; }
/* no padding-top — wrapper handles nav clearance */

/* Section label inside right panel */
.work-label { padding: var(--sp-6) var(--sp-6) var(--sp-5); background: var(--bg-alt); }

/* Project cards */
.work-card { flex: 1; padding: var(--sp-8) var(--sp-6); background: var(--bg-alt); }
/* flex:1 = equal height distribution — void inside card is expected, not a bug */
```

**Why nav clearance on wrapper, not panels:**
- Clearance inside left only → asymmetric padding → center shifts down
- Clearance on wrapper → both panels start at same baseline, left truly centered

**Why void inside cards is OK:**
- `flex:1` = equal height distribution
- Gate check: verify card bg fills (not html bg showing), not that content fills card
