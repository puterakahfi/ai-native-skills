<!-- HARD RULES reminder -->
<!-- NO min-height:100vh — void. Use padding-top:clamp(120px,16vh,180px) -->

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
