<!-- HARD RULES reminder -->
<!-- Copy template verbatim. Zero improvisation. -->

## 05 · ABOUT SECTION (split 2-col)

### Spec
```
Layout:     2-col grid 1fr 1fr, gap var(--sp-9)
Left:       H2 (STATEMENT role — ≤60% H1), short manifesto heading
Right:      body prose + meta groups (location, stack, focus)
Mobile:     single column at ≤900px
```

### Template
```css
.about-inner {
  max-width: 1280px; margin: 0 auto;
  display: grid; grid-template-columns: 1fr 1fr; gap: var(--sp-9);
}
.about-heading {
  font-size: clamp(1.4rem, 1rem + 2vw, 2rem); /* max 2rem = ≤60% of H1 3.5rem */
  font-weight: 700; letter-spacing: -0.02em; line-height: 1.15;
  color: var(--bright); margin-top: var(--sp-6);
}
.about-body { font-size: var(--text-base); color: var(--subtle); line-height: 1.8; }
.about-body p + p { margin-top: var(--sp-5); }
.about-meta { display: flex; flex-direction: column; gap: var(--sp-6); padding-top: var(--sp-6); }
.meta-group { display: flex; flex-direction: column; gap: var(--sp-2); }
.meta-label {
  font-family: var(--font-mono); font-size: var(--text-xs);
  letter-spacing: 0.12em; text-transform: uppercase; color: var(--muted);
}
.meta-value { font-size: var(--text-sm); color: var(--ink); }
.stack-list { display: flex; flex-wrap: wrap; gap: var(--sp-2); list-style: none; }
.stack-list li {
  font-family: var(--font-mono); font-size: var(--text-xs); color: var(--subtle);
  border: 1px solid var(--border); padding: 3px 10px; border-radius: 2px;
}
@media (max-width: 900px) { .about-inner { grid-template-columns: 1fr; } }
```

---

## 06 · CONTACT SECTION

### Spec
```
Layout:     flex row, space-between
Left:       H2 "Let's talk." (SECTION role)
Right:      flex row of links, height 44px each
Border:     border-bottom
```

### Template
```css
#contact { padding: var(--sp-8) var(--sp-8); border-bottom: 1px solid var(--border); }
.contact-inner {
  max-width: 1280px; margin: 0 auto;
  display: flex; align-items: center; justify-content: space-between;
}
.contact-heading {
  font-size: var(--text-2xl); font-weight: 700;
  letter-spacing: -0.03em; color: var(--bright);
}
.contact-links { display: flex; gap: var(--sp-6); align-items: stretch; height: 44px; }
.contact-links a {
  font-family: var(--font-mono); font-size: var(--text-xs);
  letter-spacing: 0.1em; text-transform: uppercase;
  color: var(--subtle); text-decoration: none;
  display: flex; align-items: center; padding: 0 var(--sp-2);
  transition: color 120ms ease;
}
.contact-links a:hover { color: var(--bright); }
@media (max-width: 640px) {
  .contact-inner { flex-direction: column; align-items: flex-start; gap: var(--sp-6); }
}
```

---

## 07 · FOOTER

### Spec
```
Height:     auto, padding var(--sp-6) horizontal
Content:    logo left, copyright right
Border:     border-top
Font:       mono xs muted
Max-width:  1280px inner
```

### Template
```css
footer { padding: var(--sp-6) var(--sp-8); border-top: 1px solid var(--border); }
.footer-inner {
  max-width: 1280px; margin: 0 auto;
  display: flex; justify-content: space-between; align-items: center;
}
footer span {
  font-family: var(--font-mono); font-size: var(--text-xs);
  letter-spacing: 0.06em; color: var(--muted);
}
```
