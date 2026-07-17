# Card Patterns + Layout Grid Patterns

## Card Patterns

### Card Type Selection

```
Content type → card pattern:

Product/project showcase   → FEATURE CARD
Blog post list             → EDITORIAL CARD
Team/person                → PROFILE CARD
Metric/stat                → STAT CARD
Tool/service comparison    → COMPARISON CARD
Process/timeline           → TIMELINE CARD
```

### Card Pattern Specs

**FEATURE CARD** — products, projects
```
Structure:
  [status badge — LIVE/DEV]
  [title — --text-xl]
  [description — --text-base, max 2–3 lines]
  [tags/tech stack]
  [arrow or link indicator]

Width:   full-width stacked (1–2 items) OR equal-height grid (3+)
Hover:   background lightens, arrow animates
Click:   entire card is clickable (not just title)
```

**EDITORIAL CARD** — blog, articles
```
Structure:
  [cover image — 16:9]
  [category + date]
  [title — --text-xl, max 2 lines]
  [excerpt — --text-base, max 3 lines]
  [author + read time]

Grid:    2-col desktop, 1-col mobile
Image:   required — text-only editorial cards feel unfinished
```

**STAT CARD** — metrics, numbers
```
Structure:
  [label — --text-sm, muted]
  [value — --text-3xl, bold]
  [delta — +/- change, colored]

Grid:    3–4 col desktop, 2-col mobile, 1-col phone
Minimal: no border-radius on stat cards — sharp = precision
```

---

## Layout Grid Patterns

### Grid Selection Rule

```
Content count → grid choice:

1 item          → full-width (100%)
2 items         → stacked (1 col) OR side-by-side (2 col if ≥ 600px width)
3 items         → 3-col grid
4 items         → 2x2 grid OR 4-col
5 items         → 2+3 split OR masonry
6+ items        → equal grid, 2–4 col depending on card width

WARNING — 2 items in 4-col grid = FAIL (looks broken, not minimal)
```

### Responsive Grid Breakpoints

```css
/* Mobile first — add columns as screen grows */

.grid {
  display: grid;
  gap: var(--space-4);
  grid-template-columns: 1fr;                          /* mobile: 1 col */
}

@media (min-width: 640px) {
  .grid { grid-template-columns: repeat(2, 1fr); }    /* tablet: 2 col */
}

@media (min-width: 960px) {
  .grid { grid-template-columns: repeat(3, 1fr); }    /* desktop: 3 col */
}

/* For stacked (intentional 1-col):
   No breakpoints needed — stays 1 col but wider */
.grid-stacked {
  display: flex;
  flex-direction: column;
  gap: 1px; /* hairline separator between cards */
  background: var(--border); /* gap shows as divider */
}
```

---

## Anti-Patterns (Cards/Grid)

| Anti-Pattern | Problem | Fix |
|---|---|---|
| Card grid with 2 items in 4 cols | Looks broken/unfinished | Stack or use 2-col |
| Nested cards (card in card) | Visual confusion, unclear clickable area | Flatten or use different component |
| Infinite scroll on portfolio | User loses position | Paginate or load-more button |
| Full-width text lines | > 75 chars = hard to track | max-width: 65ch on prose |
