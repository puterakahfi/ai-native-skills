# Motion Design — Mode 1: SUBTLE Micro-Interactions

> **HARD RULES (non-negotiable)**
> - `prefers-reduced-motion` is a HARD GATE — Gate M7 score 0 = automatic full fail
> - Every animation must have a reduced-motion override
> - `transform` + `opacity` only — no layout-triggering properties

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
