<!-- HARD RULES reminder -->
<!-- Copy template verbatim. Check ux-patterns-for-developers for behavior. -->

# UI Components — Sections Reference

> **CRITICAL RULE: Copy template verbatim — zero improvisation. Check ux-patterns-for-developers before writing component behavior.**

---

## 03 · SECTION (generic content section)

### Spec
```
Padding:       var(--sp-9) var(--sp-8) — vertical large, horizontal standard
Max-width:     1280px centered inner
Border:        border-bottom 1px solid var(--border)
Label:         section-label (mono xs uppercase, muted, decorative line)
Heading:       H2, sized per visual-hierarchy rule (≤60% of H1)
```

### Template
```css
section {
  border-bottom: 1px solid var(--border);
  padding: var(--sp-9) var(--sp-8);
}
.section-inner { max-width: 1280px; margin: 0 auto; width: 100%; }
.section-label {
  font-family: var(--font-mono); font-size: var(--text-xs);
  letter-spacing: 0.14em; text-transform: uppercase; color: var(--muted);
  display: flex; align-items: center; gap: var(--sp-4);
  margin-bottom: var(--sp-6);
}
.section-label::before { content: ''; width: 16px; height: 1px; background: var(--muted); }
.section-heading {
  font-size: clamp(1.4rem, 1rem + 2vw, 2rem); /* max ≤60% of H1 */
  font-weight: 700; letter-spacing: -0.02em; line-height: 1.15;
  color: var(--bright);
}
```

### A11y (from W3C APG + WCAG 2.1)
```
Container:  <ul> or <ol> native — NOT role="list" redundantly
Each row:   <li> with <a> wrapping entire row (preferred over role="link" on div)
Status dot: <span aria-label="Status: Live"> — color alone = WCAG 1.4.1 FAIL
Hover:      Must NOT be sole focus indicator — :focus-visible required separately
Keyboard:   Tab → first interactive element in row → next row
            Enter/Space → activate row
            Escape → dismiss open action menu
Nested btn: stopPropagation() on child buttons — row click must not fire
Event:      Full row clickable, min 44×44px touch target (WCAG 2.5.5)
```

### Behavior
```
Row hover:   background: var(--surface) + arrow translate(4px,-4px)
Row click:   navigate to URL (entire <a> wraps row)
Child click: stopPropagation — tag clicks, action buttons don't trigger row nav
Status:      aria-label="Status: Live" on dot — not color alone
Empty state: role="status" + message — "No work yet"
Loading:     aria-busy="true" on container + skeleton rows
```

---

## 04 · WORK ROW (product/project list item)

### Spec
```
Layout:     4-col grid: [index 80px] [main 1fr] [status 200px] [arrow auto]
Hover:      background surface, arrow translates(4px,-4px)
Tags:       mono xs uppercase, border pill
Status dot: 6px accent circle + label
Mobile:     3-col (hide status col at ≤900px)
Touch:      entire row is clickable — min-height 80px
```

### Template
```css
.product-list { display: flex; flex-direction: column; }
.product-row {
  max-width: 1280px; margin: 0 auto; width: 100%;
  display: grid;
  grid-template-columns: 80px 1fr 200px auto;
  align-items: start; gap: var(--sp-6);
  padding: var(--sp-7) var(--sp-8);
  border-bottom: 1px solid var(--border);
  text-decoration: none;
  transition: background 120ms ease;
}
.product-row:hover { background: var(--surface); }
.product-row:hover .row-arrow { transform: translate(4px,-4px); color: var(--bright); }

.row-index {
  font-family: var(--font-mono); font-size: var(--text-xs);
  letter-spacing: 0.08em; color: var(--muted); padding-top: 4px;
}
.row-main { display: flex; flex-direction: column; gap: var(--sp-4); }
.row-name { font-size: var(--text-xl); font-weight: 700; letter-spacing: -0.02em; color: var(--bright); }
.row-desc { font-size: var(--text-sm); color: var(--subtle); line-height: 1.6; }
.row-tags { display: flex; flex-wrap: wrap; gap: var(--sp-2); }
.tag {
  font-family: var(--font-mono); font-size: 0.65rem;
  letter-spacing: 0.08em; text-transform: uppercase;
  color: var(--muted); border: 1px solid var(--border);
  padding: 2px 8px; border-radius: 2px;
}
.row-status { display: flex; align-items: flex-start; gap: var(--sp-2); padding-top: 4px; }
.status-dot { width: 6px; height: 6px; border-radius: 50%; background: var(--accent); margin-top: 6px; flex-shrink: 0; }
.status-label {
  font-family: var(--font-mono); font-size: var(--text-xs);
  letter-spacing: 0.1em; text-transform: uppercase; color: var(--accent);
}
.row-arrow {
  color: var(--muted); font-size: 1.25rem; padding-top: 2px;
  transition: transform 120ms ease, color 120ms ease;
}
@media (max-width: 900px) {
  .product-row { grid-template-columns: 48px 1fr auto; }
  .row-status { display: none; }
}
@media (max-width: 640px) {
  .product-row { grid-template-columns: 40px 1fr auto; gap: var(--sp-4); }
}
```

---

