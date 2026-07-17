# Touch Targets, Viewport Checklist, Scoring Rubric & Common Failures

---

## Touch Targets

**WCAG 2.5.5 (Level AAA) — minimum 44×44px**
**Apple HIG — minimum 44pt**
**Material Design — minimum 48dp**

```
All interactive elements on mobile must be ≥ 44×44px.
This includes: buttons, links, nav items, checkboxes, radio buttons, tags.

Common failures:
  ❌ Nav links with font-size: 0.7rem and no padding → 20px touch target
  ❌ Icon buttons with only the icon size as target → 16×16px
  ❌ Tag chips with 2px vertical padding → 24px touch target
```

**Touch target fix patterns:**

```css
/* Small visual, large touch target */
.tag {
  font-size: var(--text-xs);
  padding: var(--space-2) var(--space-3);   /* minimum vertical: 8px */
  min-height: 32px;                          /* acceptable for non-primary actions */
}

/* Primary actions — full 44px */
.nav-link {
  display: flex;
  align-items: center;
  min-height: 44px;
  padding: 0 var(--space-4);
}

/* Icon buttons — expand hit area without changing visual */
.icon-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  min-width: 44px;
  min-height: 44px;
}
```

---

## Viewport Adaptation Checklist

### Navigation

```
Mobile (< 768px):
  □ Hamburger menu OR bottom tab bar
  □ Full-screen overlay or slide-in drawer
  □ Close button visible
  □ Tap outside to close

Tablet (768–1024px):
  □ Decide: show desktop nav OR keep mobile nav
  □ If desktop nav: verify items still fit (no overflow)

Desktop (≥ 1024px):
  □ Full horizontal nav visible
  □ Hamburger gone
  □ Active state visible
```

### Hero

```
Mobile:
  □ H1 font-size ≤ --text-3xl (50px)
  □ H1 max 3–4 words per line
  □ Subtitle max-width: 90% (not full bleed)
  □ If SPLIT HERO: visual below text, not beside

Tablet:
  □ H1 between mobile and desktop size
  □ Split hero: evaluate if side-by-side fits

Desktop:
  □ Full H1 scale
  □ Text max-width: 60% for split hero
  □ Visual complements, doesn't overpower text
```

### Product Cards

```
Mobile:
  □ 1 column, full width
  □ Card padding: --space-5 to --space-6

Tablet:
  □ 2 column if cards ≥ 3, else 1 column
  □ Card heights equal (use align-items: stretch)

Desktop:
  □ Layout from ux-ui-patterns grid decision (count-based)
  □ Hover states work (not just click)
```

### Images

```css
img {
  max-width: 100%;
  height: auto;
  display: block;
}

/* Responsive images with different crops */
picture source[media="(max-width: 640px)"] → mobile crop (portrait/square)
picture source[media="(min-width: 641px)"] → desktop crop (landscape)
```

---

## Responsiveness Scoring Rubric

```
RESPONSIVENESS AUDIT — [page name]
────────────────────────────────────────────────
Dimension 1: Mobile Layout
  □ Single column on mobile?
  □ No horizontal overflow?
  □ Text not overflowing container?
  Score: __ / 10

Dimension 2: Touch Targets
  □ All interactive elements ≥ 44×44px on mobile?
  □ Nav links have adequate tap area?
  □ Cards fully clickable?
  Score: __ / 10

Dimension 3: Typography Scaling
  □ H1/body ratio ≤ 3.5x on mobile?
  □ No text smaller than 12px on mobile?
  □ Type scales fluidly between viewpoints?
  Score: __ / 10

Dimension 4: Navigation
  □ Mobile nav present and functional?
  □ Desktop nav hidden on mobile?
  □ Active state visible on both?
  Score: __ / 10

Dimension 5: Images & Media
  □ No image overflow?
  □ Images have width:100%, height:auto?
  □ No fixed-pixel widths on images?
  Score: __ / 10

Dimension 6: Spacing Rhythm
  □ Mobile padding reduced from desktop?
  □ No excess whitespace on mobile?
  □ Sections still have visual separation?
  Score: __ / 10

────────────────────────────────────────────────
TOTAL SCORE: __ / 10  (average of 6 dimensions)
STATUS: PASS (≥ 8.0) | FAIL (< 8.0)

Failing dimensions:
  [list each < 8 with specific fix]
────────────────────────────────────────────────
```

---

## Common Responsiveness Failures

| Failure | Score Impact | Fix |
|---|---|---|
| Horizontal scroll on mobile | D1: -8 | `overflow-x: hidden` on body, find overflow source |
| Touch targets < 44px | D2: -6 | Add min-height: 44px + padding |
| H1 too large on mobile (ratio > 4x) | D3: -4 | Cap at --text-3xl on mobile |
| Desktop nav visible on mobile | D4: -6 | `display: none` on mobile, add hamburger |
| Fixed-width image | D5: -6 | `max-width: 100%; height: auto` |
| Desktop padding unchanged on mobile | D6: -4 | Reduce from --space-8 to --space-5 |
| Two-column grid on 360px viewport | D1: -5 | `grid-template-columns: 1fr` on mobile |
| Text set in vw only (no min) | D3: -4 | Use `clamp()` with minimum size |
| Hover-only interaction (no touch) | D2: -3 | Add click/tap equivalent for all hover actions |
