# Motion Design — Mode 2: CINEMATIC & Composing

> **HARD RULES (non-negotiable)**
> - `prefers-reduced-motion` is a HARD GATE — Gate M7 score 0 = automatic full fail
> - Every animation must have a reduced-motion override
> - `transform` + `opacity` only — no layout-triggering properties

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
