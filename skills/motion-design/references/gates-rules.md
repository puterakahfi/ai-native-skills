# Motion Design — Gates, Reduced Motion & Anti-Patterns

> **HARD RULES (non-negotiable)**
> - `prefers-reduced-motion` is a HARD GATE — Gate M7 score 0 = automatic full fail
> - Every animation must have a reduced-motion override
> - `transform` + `opacity` only — no layout-triggering properties

---

## Motion Gates (Scoring Rubric)

Every gate scored 0–10. Minimum 8.0 to pass.

```
MOTION REVIEW
════════════════════════════════════════════════════

Gate M1: Purpose Test
  For each animation: can you state what it communicates?
  Fail: animation exists because "it looks cool"
  Pass: every animation = clear user signal
  Score: __ / 10

Gate M2: Duration Appropriateness
  Micro-interactions ≤ 200ms?
  Standard transitions ≤ 400ms?
  Entrances ≤ 600ms?
  Cinematic ≤ 1200ms?
  Score: __ / 10

Gate M3: Easing Correctness
  Entering elements: ease-out (decelerate) — not linear, not ease-in
  Exiting elements: ease-in (accelerate)
  Standard UI: ease-standard (symmetric)
  Score: __ / 10

Gate M4: Performance (GPU composited only)
  Animated properties: transform + opacity ONLY?
  No animation of: width, height, top, left, margin, padding
  will-change declared on frequently-animated elements?
  Score: __ / 10

Gate M5: Stagger Timing
  Stagger delay ≤ 120ms per item?
  Total stagger duration (n × delay) ≤ 600ms?
  Last item visible before user gets impatient?
  Score: __ / 10

Gate M6: Cinematic → Subtle Ratio (landing pages)
  Hero: max motion ✓
  Content sections: medium motion ✓
  Contact/footer: minimal/no motion ✓
  Ratio decreases toward page bottom?
  Score: __ / 10

Gate M7: Reduced Motion Compliance (HARD GATE)
  prefers-reduced-motion: reduce → all animations disabled?
  Transitions replaced with instant state changes?
  Content still readable/accessible without motion?
  Score: 0 (fail, must fix) OR 10 (pass, non-negotiable)

Gate M8: No Motion Distraction
  Motion does not pull attention from primary content?
  Animations complete before user needs to interact?
  No looping animations competing with reading?
  (pulse/nudge = ok; spinning/flashing = fail)
  Score: __ / 10

════════════════════════════════════════════════════
OVERALL: __ / 10   MINIMUM: 8.0
Gate M7 is non-negotiable — score 0 = automatic full fail
════════════════════════════════════════════════════
```

---

## Reduced Motion (Non-Negotiable)

```css
@media (prefers-reduced-motion: reduce) {
  /* Kill ALL transitions and animations */
  *, *::before, *::after {
    animation-duration:        0.01ms !important;
    animation-iteration-count: 1      !important;
    transition-duration:       0.01ms !important;
    scroll-behavior:           auto   !important;
  }

  /* Restore essential non-motion transitions */
  :focus-visible {
    transition: none;
    outline: 2px solid var(--interactive-hover);
  }
}
```

```js
// Check in JS before applying motion
const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

if (!prefersReduced) {
  initHeroEntrance();
  initScrollReveal();
  initParallax('.hero-eyebrow', 0.15);
} else {
  // Make everything visible immediately
  document.querySelectorAll('.reveal').forEach(el => el.classList.add('visible'));
  document.querySelectorAll('[style*="opacity: 0"]').forEach(el => el.style.opacity = '1');
  document.querySelectorAll('[style*="transform"]').forEach(el => el.style.transform = 'none');
}
```

---

## Anti-Patterns

| Anti-Pattern | Why It Fails | Fix |
|---|---|---|
| `transition: all 0.3s` | Animates non-composited props (layout thrash) | List specific props: `transform, opacity` |
| Duration > 500ms on hover | User feels lag, not delight | Max 200ms for hover |
| Bounce/spring on entrance | Draws attention, not purpose | Spring only for playful confirmations |
| Stagger > 120ms per item | Last item takes forever | Cap at 80–100ms |
| Infinite spin/flash | Competes with content, epilepsy risk | Remove or add `prefers-reduced-motion` |
| Parallax on mobile | Causes jank, battery drain | `@media (hover: none) { parallax = off }` |
| Animation on scroll without `passive: true` | Blocks scroll thread | Always `{ passive: true }` |
| Animating width/height/top/left | Layout thrash → jank | Use `transform: scale/translate` instead |
| `will-change: transform` on everything | Wastes GPU memory | Only on actively animated elements |
| Cinematic entrance on dashboard | Slows task completion | Subtle or none on functional UI |
| Motion before content is ready | Reveals empty state | Animate in only after data is available |
