# Motion Design — Tokens, Easing & Decision Tree

> **HARD RULES (non-negotiable)**
> - `prefers-reduced-motion` is a HARD GATE — Gate M7 score 0 = automatic full fail
> - Every animation must have a reduced-motion override
> - `transform` + `opacity` only — no layout-triggering properties

---

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
