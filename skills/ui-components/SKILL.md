---
name: ui-components
version: 1.0.0
type: skill
description: >
  UI component patterns — exact CSS templates, behavior specs, interaction states,
  and composition rules for Navbar, Hero, Section, Work/List rows, About, Contact, Footer.
  Template-based: copy-paste, do NOT improvise.
tags: [ui, components, patterns, templates, css, behavior]
implements: ai-native-core/contracts/skills/experience-design/ui-components.contract.yaml
---

# UI Components

**RULE: Every component below has a mandatory CSS template. Copy it. Do NOT improvise.**
Improvisation = bugs. Template = correct behavior on all viewports.

---

## 01 · NAVBAR

### Spec
```
Height:         64px fixed
Position:       fixed top-0 left-0 right-0 z-100
Scrolled state: bg rgba(9,9,8,0.92) + blur(16px) + border-bottom
Default state:  transparent, no border
Logo:           left, mono font, 44px touch target
Links:          right, mono font xs uppercase, 44px touch target
Mobile break:   ≤640px → hamburger, links hidden
```

### Template
```css
nav#site-nav {
  position: fixed; top: 0; left: 0; right: 0; z-index: 100;
  height: 64px;
  border-bottom: 1px solid transparent;
  transition: background 200ms ease, border-color 200ms ease;
}
nav#site-nav.scrolled {
  background: rgba(9,9,8,0.92);
  backdrop-filter: blur(16px);
  border-color: var(--border);
}
.nav-inner {
  max-width: 1280px; margin: 0 auto;
  padding: 0 var(--sp-8); height: 100%;
  display: flex; align-items: center; justify-content: space-between;
}
.nav-logo {
  font-family: var(--font-mono); font-size: var(--text-sm);
  letter-spacing: 0.04em; color: var(--bright); text-decoration: none;
  min-height: 44px; display: flex; align-items: center;
}
.nav-links { display: flex; gap: var(--sp-7); list-style: none; }
.nav-links a {
  font-family: var(--font-mono); font-size: var(--text-xs);
  letter-spacing: 0.12em; text-transform: uppercase;
  color: var(--muted); text-decoration: none;
  min-height: 44px; display: flex; align-items: center;
  transition: color 120ms ease;
}
.nav-links a:hover { color: var(--bright); }
.nav-hamburger {
  display: none; flex-direction: column; gap: 5px;
  background: none; border: none; cursor: pointer;
  min-height: 44px; min-width: 44px;
  justify-content: center; align-items: center;
}
.nav-hamburger span { display: block; width: 20px; height: 1px; background: var(--subtle); }
@media (max-width: 640px) {
  .nav-links { display: none; }
  .nav-hamburger { display: flex; }
}
```

### Behavior
```
scroll > 40px  → add .scrolled to nav
hamburger click → toggle #nav-mobile .open
mobile nav link click → close mobile nav
```

### JS
```js
const nav = document.getElementById('site-nav');
window.addEventListener('scroll', () => {
  nav.classList.toggle('scrolled', window.scrollY > 40);
}, { passive: true });

const btn = document.querySelector('.nav-hamburger');
const mobileNav = document.getElementById('nav-mobile');
btn.addEventListener('click', () => {
  const open = mobileNav.classList.toggle('open');
  btn.setAttribute('aria-expanded', open);
});
```

### Mobile Nav Drawer
```css
#nav-mobile {
  position: fixed; top: 64px; left: 0; right: 0; z-index: 99;
  background: rgba(9,9,8,0.98); backdrop-filter: blur(24px);
  padding: var(--sp-6) var(--sp-8) var(--sp-8);
  border-bottom: 1px solid var(--border);
  transform: translateY(-8px); opacity: 0; pointer-events: none;
  transition: all 200ms cubic-bezier(0,0,0.2,1);
}
#nav-mobile.open { transform: none; opacity: 1; pointer-events: auto; }
#nav-mobile a {
  display: flex; align-items: center;
  min-height: 44px; padding: var(--sp-4) 0;
  font-family: var(--font-mono); font-size: var(--text-sm);
  letter-spacing: 0.08em; text-transform: uppercase;
  color: var(--subtle); text-decoration: none;
  border-bottom: 1px solid var(--border);
  transition: color 120ms ease;
}
#nav-mobile a:hover { color: var(--bright); }
```

---

## 02 · HERO — Marquee Hero (personal landing)

### Spec
```
Pattern:        TOP-ANCHORED — name near top, void below = intentional
min-height:     100vh
padding-top:    clamp(120px, 16vh, 180px) — nav clearance + breathing
Layout:         display:block — NOT grid, NOT flex-center
Content width:  max-width 1280px centered
Scroll cue:     position:absolute bottom — out of document flow

Slots (in order, top to bottom):
  1. eyebrow    — mono xs uppercase, muted color, decorative line before
  2. H1 name    — display font, large, dominant
  3. hero-bottom — flex row: stance (left) + meta links (right)
  4. scroll-cue — absolute, bottom center
```

### Template
```css
.hero {
  /* NO min-height:100vh — forces void when content is sparse */
  display: block;
  padding-top: clamp(120px, 16vh, 180px);     /* nav(64px) + breathing above name */
  padding-bottom: clamp(80px, 14vh, 140px);   /* breathing room — NOT full viewport */
  padding-left: var(--sp-8);
  padding-right: var(--sp-8);
  position: relative;
  border-bottom: 1px solid var(--border);
}
/* HARD RULE: min-height:100vh + sparse content = huge void below = FAIL */
/* HARD RULE: display:grid/flex-center = content floats in void at tall viewports = FAIL */
/* CORRECT: display:block + padding = content anchored, void only as breathing room */
.hero-content { max-width: 1280px; margin: 0 auto; width: 100%; }

.hero-eyebrow {
  font-family: var(--font-mono); font-size: var(--text-xs);
  letter-spacing: 0.14em; text-transform: uppercase; color: var(--muted);
  margin-bottom: var(--sp-5);
  display: flex; align-items: center; gap: var(--sp-4);
}
.hero-eyebrow::before { content: ''; width: 24px; height: 1px; background: var(--muted); }

.hero-name {
  font-family: var(--font-display);        /* R1: display face, NOT body font */
  font-size: clamp(2.2rem, 1.3rem + 3.8vw, 3.5rem); /* ratio ≤3.5x body */
  font-weight: 800; letter-spacing: -0.02em; line-height: 0.95;
  color: var(--bright); margin-bottom: var(--sp-7);
}

.hero-bottom {
  display: flex; align-items: flex-end;
  justify-content: space-between; gap: var(--sp-8);
}
.hero-stance {
  font-size: var(--text-lg); color: var(--subtle);
  line-height: 1.6; max-width: 44ch;      /* ~57 CPL optimal */
}
.hero-meta { display: flex; flex-direction: column; gap: var(--sp-3); flex-shrink: 0; }
.hero-meta a {
  font-family: var(--font-mono); font-size: var(--text-xs);
  letter-spacing: 0.08em; color: var(--muted); text-decoration: none;
  display: flex; align-items: center; gap: var(--sp-3);
  min-height: 44px; padding: 0 var(--sp-2);
  transition: color 120ms ease;
}
.hero-meta a:hover { color: var(--bright); }
.hero-meta-label { font-size: 0.65rem; letter-spacing: 0.12em; text-transform: uppercase; }

.scroll-cue {
  position: absolute; bottom: var(--sp-7); left: 50%;
  transform: translateX(-50%);
  display: flex; flex-direction: column; align-items: center; gap: var(--sp-3);
}
.scroll-cue-line {
  width: 1px; height: 40px; background: var(--border);
  animation: scroll-line 2s ease-in-out infinite;
}
@keyframes scroll-line {
  0%,100% { transform: scaleY(1); opacity: .4; }
  50%      { transform: scaleY(1.4); opacity: 1; }
}
.scroll-cue-label {
  font-family: var(--font-mono); font-size: 0.625rem;
  letter-spacing: 0.16em; text-transform: uppercase; color: var(--muted);
}
@media (max-width: 640px) {
  .hero-bottom { flex-direction: column; align-items: flex-start; gap: var(--sp-6); }
  .hero-meta { flex-direction: row; flex-wrap: wrap; }
}
```

### HTML
```html
<div class="hero">
  <div class="hero-content">
    <div class="hero-eyebrow" aria-hidden="true">Engineer — Yogyakarta</div>
    <h1 class="hero-name">Putera<br>Kahfi.</h1>
    <div class="hero-bottom">
      <p class="hero-stance">One sentence stance. Direct. No hedging.</p>
      <nav class="hero-meta" aria-label="Contact">
        <a href="mailto:hi@pkahfi.com">
          <span class="hero-meta-label">Email</span> hi@pkahfi.com
        </a>
      </nav>
    </div>
  </div>
  <div class="scroll-cue" aria-hidden="true">
    <div class="scroll-cue-line"></div>
    <span class="scroll-cue-label">Scroll</span>
  </div>
</div>
```

### Behavior
```
On load:     eyebrow → name → hero-bottom stagger animate in (100ms, 250ms, 400ms)
scroll > 60: scroll-cue fades out
```

### JS
```js
// Stagger entrance
['.hero-eyebrow','.hero-name','.hero-bottom'].forEach((sel, i) => {
  const el = document.querySelector(sel);
  if (el) setTimeout(() => el.classList.add('visible'), 100 + i * 150);
});
// Scroll cue fade
window.addEventListener('scroll', () => {
  const cue = document.querySelector('.scroll-cue');
  if (cue) cue.style.opacity = window.scrollY > 60 ? '0' : '1';
}, { passive: true });
```

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

---

## 08 · SCROLL REVEAL (section entrance)

### Spec
```
Trigger:    IntersectionObserver threshold 0.1, rootMargin 0px 0px -40px 0px
Effect:     opacity 0→1 + translateY(20px)→0
Duration:   350ms ease-enter
Class:      .reveal → add .visible on enter
```

### Template
```css
.reveal {
  opacity: 0; transform: translateY(20px);
  transition: opacity 350ms cubic-bezier(0,0,0.2,1),
              transform 350ms cubic-bezier(0,0,0.2,1);
}
.reveal.visible { opacity: 1; transform: none; }
@media (prefers-reduced-motion: reduce) {
  .reveal { opacity: 1 !important; transform: none !important; transition: none !important; }
}
```

### JS
```js
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });
document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
```

---

## 09 · VERIFICATION CHECKLIST (run after every component change)

```js
// Paste in browser console — all must pass before deliver
const ok = {
  bg:        getComputedStyle(document.body).backgroundColor, // ≠ rgba(0,0,0,0)
  sheets:    document.styleSheets.length,                     // > 0
  touchFail: [...document.querySelectorAll('a,button')]
               .filter(el=>{const b=el.getBoundingClientRect();
                 return b.width>0&&b.height<44;}).length,     // === 0
  h1TopPct:  Math.round(document.querySelector('h1')
               .getBoundingClientRect().top/window.innerHeight*100), // < 45
  maxWidth:  getComputedStyle(document.querySelector('.hero-content')||
               document.querySelector('.nav-inner')).maxWidth,       // 1280px
};
console.table(ok);
```

---

## PITFALLS

```
□ Improvising component CSS → always copy template above, never write from scratch
□ Missing max-width on sections → content bleeds to viewport edge on ultrawide
□ Hero display:grid + 1fr row → content floats in void at tall viewports → use display:block
□ Touch targets: min-height alone doesn't work if parent is flex with align-items:center
  → use height:44px + display:flex + align-items:center on the link itself
□ CSS patch corruption: 3+ patches on same block → nested rules → white page
  → after 2 patches fail, rewrite full file with write_file
□ self-closing divs used as grid rows → don't, use display:none or remove
```
