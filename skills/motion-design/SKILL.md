---
name: motion-design
description: Motion design system — micro-interactions, state transitions, scroll-driven animation, staggered entrance, and cinematic narrative motion. Decision tree for choosing the right motion type. Scores motion quality 0–10. Minimum 8 to pass. Always respects prefers-reduced-motion.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/experience-design/motion-design.contract.yaml
  ai-native-skills.related_skills: '[''design-system'', ''ux-psychology'', ''ux-ui-patterns'', ''accessibility'', ''master-design'']'
---

# Motion Design Skill

## Core Principle

```
Motion is not decoration — it is communication.
Every animation must answer: what does this tell the user?

The two laws:
  1. Motion must earn its place — if removing it loses nothing, remove it.
  2. Motion must respect the user — always honor prefers-reduced-motion.

Two modes:
  SUBTLE    → micro-interactions, purposeful feedback, clean entrance
  CINEMATIC → scroll-driven narrative, stagger, text reveal, parallax

Choose mode based on page intent:
  Personal landing, portfolio  → subtle first, cinematic if it serves the story
  Editorial, case study        → cinematic, narrative-driven
  Product app, dashboard       → subtle only, never cinematic
  Marketing, campaign          → cinematic acceptable, conversion-focused
```

---

## Motion Token System

Declare before animating — never hardcode durations or easings.

```css
:root {
  /* ── DURATION ── */
  --dur-instant:  50ms;   /* imperceptible — state flags */
  --dur-micro:   150ms;   /* hover, focus, small feedback */
  --dur-fast:    250ms;   /* standard UI transitions */
  --dur-normal:  350ms;   /* element entrance, modal open */
  --dur-slow:    500ms;   /* page section entrance */
  --dur-cinematic: 800ms; /* narrative reveal, hero entrance */
  --dur-dramatic: 1200ms; /* scroll-driven, full section wipe */

  /* ── EASING ── */
  --ease-standard:   cubic-bezier(0.4, 0, 0.2, 1);   /* most UI transitions */
  --ease-enter:      cubic-bezier(0, 0, 0.2, 1);     /* elements entering screen */
  --ease-exit:       cubic-bezier(0.4, 0, 1, 1);     /* elements leaving */
  --ease-spring:     cubic-bezier(0.175, 0.885, 0.32, 1.275); /* bouncy, playful */
  --ease-editorial:  cubic-bezier(0.76, 0, 0.24, 1); /* sharp, cinematic */
  --ease-smooth:     cubic-bezier(0.65, 0, 0.35, 1); /* smooth, editorial */

  /* ── STAGGER ── */
  --stagger-sm:  40ms;   /* tight list items */
  --stagger-md:  80ms;   /* card grids */
  --stagger-lg: 120ms;   /* section children */
}
```

### Easing Selection Guide

```
Standard UI (hover, click, toggle)  → --ease-standard
Element entering viewport           → --ease-enter
Element leaving (dismiss, close)    → --ease-exit
Playful confirmation (success, like)→ --ease-spring
Editorial text reveal, hero         → --ease-editorial
Scroll-driven parallax              → --ease-smooth
```

---

## Decision Tree — Which Motion Type?

```
What is the user trigger?

├── User ACTION (hover, click, focus)
│   → MICRO-INTERACTION
│   └── Examples: button hover, card lift, link underline grow
│
├── STATE CHANGE (loading, success, error, empty→populated)
│   → STATE TRANSITION
│   └── Examples: skeleton→content, form submit, toggle switch
│
├── ELEMENT ENTERING VIEWPORT (scroll)
│   ├── Subtle page → SCROLL ENTRANCE (fade + translate)
│   └── Editorial page → CINEMATIC REVEAL (clip, stagger, text split)
│
├── PAGE LOAD (first render)
│   ├── App/dashboard → no entrance animation (too slow)
│   └── Landing/portfolio → HERO ENTRANCE (stagger children)
│
└── USER SCROLLS (parallax, progress)
    ├── Subtle → SCROLL PROGRESS (opacity fade)
    └── Cinematic → SCROLL NARRATIVE (parallax, sticky sections)
```

---

## Mode 1: SUBTLE — Micro-Interactions

For: personal pages, product apps, anywhere motion must not distract.

### 1A. Hover Lift (cards, links)

```css
.card {
  transition:
    transform var(--dur-micro) var(--ease-standard),
    background var(--dur-micro) var(--ease-standard),
    box-shadow var(--dur-micro) var(--ease-standard);
  will-change: transform;
}
.card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(0,0,0,0.4);
}

/* Rule: translateY max ±4px for subtle. ±8px+ is cinematic. */
```

### 1B. Link Underline Grow

```css
.link {
  text-decoration: none;
  background-image: linear-gradient(currentColor, currentColor);
  background-size: 0% 1px;
  background-repeat: no-repeat;
  background-position: left bottom;
  transition: background-size var(--dur-fast) var(--ease-standard);
}
.link:hover { background-size: 100% 1px; }
```

### 1C. Button Press Feedback

```css
.btn {
  transition:
    transform var(--dur-micro) var(--ease-standard),
    background var(--dur-micro) var(--ease-standard);
}
.btn:hover  { transform: translateY(-1px); }
.btn:active { transform: translateY(0) scale(0.98); }
```

### 1D. Focus Ring Reveal

```css
/* Animate focus ring appearing — not jarring */
:focus-visible {
  outline: 2px solid var(--interactive-hover);
  outline-offset: 3px;
  transition: outline-offset var(--dur-micro) var(--ease-standard);
}
:focus-visible:not(:focus-visible) { outline-offset: 0; }
```

### 1E. Skeleton Loading → Content

```css
.skeleton {
  background: linear-gradient(
    90deg,
    var(--surface) 25%,
    var(--border) 50%,
    var(--surface) 75%
  );
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
  border-radius: 4px;
}
@keyframes shimmer {
  0%   { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}

.skeleton.loaded {
  animation: none;
  background: none;
  transition: opacity var(--dur-fast) var(--ease-enter);
}
```

### 1F. Scroll Entrance (Subtle)

```css
.reveal {
  opacity: 0;
  transform: translateY(16px);
  transition:
    opacity var(--dur-slow) var(--ease-enter),
    transform var(--dur-slow) var(--ease-enter);
}
.reveal.visible {
  opacity: 1;
  transform: translateY(0);
}
```

```js
const observer = new IntersectionObserver(
  (entries) => entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add('visible');
      observer.unobserve(e.target); // fire once
    }
  }),
  { threshold: 0.15, rootMargin: '0px 0px -48px 0px' }
);
document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
```

### 1G. Stagger (list/grid entrance)

```js
// Stagger children on parent reveal
function staggerReveal(parent, childSelector, staggerMs = 80) {
  const children = parent.querySelectorAll(childSelector);
  children.forEach((child, i) => {
    child.style.transitionDelay = `${i * staggerMs}ms`;
    child.classList.add('reveal');
  });
}
// Call after observer fires on parent
```

---

## Mode 2: CINEMATIC — Editorial & Narrative

For: personal landing pages, portfolios, editorial sites, campaigns.
Never for: dashboards, product apps, data-heavy UI.

### 2A. Hero Entrance (stagger children)

```js
// On DOMContentLoaded — stagger hero elements in sequence
const heroSequence = [
  { el: '.hero-eyebrow', delay: 0 },
  { el: '.hero h1 .name',   delay: 120 },
  { el: '.hero h1 .stance', delay: 240 },
  { el: '.hero-bio',        delay: 380 },
  { el: '.hero-meta',       delay: 500 },
];

heroSequence.forEach(({ el, delay }) => {
  const node = document.querySelector(el);
  if (!node) return;
  node.style.opacity = '0';
  node.style.transform = 'translateY(24px)';
  node.style.transition = `opacity var(--dur-cinematic) var(--ease-enter),
                            transform var(--dur-cinematic) var(--ease-enter)`;
  setTimeout(() => {
    node.style.opacity = '1';
    node.style.transform = 'translateY(0)';
  }, delay + 100); // +100ms for paint
});
```

### 2B. Text Split Reveal (word by word)

```js
function splitWords(el, staggerMs = 60, delay = 0) {
  const words = el.textContent.trim().split(' ');
  el.innerHTML = words.map(w =>
    `<span class="word" style="display:inline-block; overflow:hidden; vertical-align:bottom;">
       <span class="word-inner" style="display:inline-block; transform:translateY(110%); opacity:0;">${w}</span>
     </span>`
  ).join(' ');

  el.querySelectorAll('.word-inner').forEach((w, i) => {
    w.style.transition = `transform var(--dur-cinematic) var(--ease-editorial),
                           opacity var(--dur-fast) var(--ease-enter)`;
    setTimeout(() => {
      w.style.transform = 'translateY(0)';
      w.style.opacity = '1';
    }, delay + i * staggerMs);
  });
}

// Usage: splitWords(document.querySelector('.hero h1'), 60, 200);
```

### 2C. Clip Reveal (section headings)

```css
.clip-reveal {
  clip-path: inset(0 100% 0 0);
  transition: clip-path var(--dur-dramatic) var(--ease-editorial);
}
.clip-reveal.visible { clip-path: inset(0 0% 0 0); }
```

### 2D. Scroll-Driven Parallax

```js
// Lightweight parallax — no library needed
function initParallax(selector, speed = 0.3) {
  const els = document.querySelectorAll(selector);
  let ticking = false;

  window.addEventListener('scroll', () => {
    if (ticking) return;
    requestAnimationFrame(() => {
      els.forEach(el => {
        const rect = el.getBoundingClientRect();
        const centerY = rect.top + rect.height / 2 - window.innerHeight / 2;
        el.style.transform = `translateY(${centerY * speed}px)`;
      });
      ticking = false;
    });
    ticking = true;
  }, { passive: true });
}

// Usage: initParallax('.hero-eyebrow', 0.15);
// Rule: speed ≤ 0.3 for subtle, 0.3–0.6 for cinematic
```

### 2E. Scroll Progress Fade (sections)

```js
// Section fades based on scroll position — narrative pacing
function initScrollFade(sectionSelector) {
  const sections = document.querySelectorAll(sectionSelector);

  const obs = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      const ratio = e.intersectionRatio;
      e.target.style.opacity = Math.min(1, ratio * 3).toFixed(2);
    });
  }, { threshold: Array.from({ length: 20 }, (_, i) => i / 20) });

  sections.forEach(s => {
    s.style.transition = `opacity var(--dur-fast) linear`;
    obs.observe(s);
  });
}
```

### 2F. Number Counter (stats, metrics)

```js
function countUp(el, target, duration = 1200, suffix = '') {
  const start = performance.now();
  const update = (now) => {
    const progress = Math.min((now - start) / duration, 1);
    const ease = 1 - Math.pow(1 - progress, 3); // ease-out cubic
    el.textContent = Math.round(ease * target) + suffix;
    if (progress < 1) requestAnimationFrame(update);
  };
  requestAnimationFrame(update);
}
// Trigger on IntersectionObserver, not on load
```

---

## Composing Subtle + Cinematic

For a personal landing page — layer both:

```
Hero section:      CINEMATIC entrance (hero sequence stagger)
                   + SUBTLE micro-interactions (meta links hover)

Work section:      SUBTLE scroll entrance (reveal + stagger cards)
                   + SUBTLE hover (card lift, arrow animate)

About section:     SUBTLE scroll entrance (fade in)
                   + Optional: CINEMATIC heading clip-reveal

Contact section:   SUBTLE only — closing quietly, no drama
```

Rule: **cinematic motion decreases as page progresses**.
Hero = max motion. Contact = min motion. Never reverse.

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
