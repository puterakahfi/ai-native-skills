# Web Performance — Critical CSS, JS Strategy, Lighthouse & Gates

## Critical CSS

```
What: inline the CSS needed for above-fold render.
Why: external CSS = render-blocking. Critical CSS inline = no block.

Strategy:
  1. Identify above-fold elements (hero, nav)
  2. Extract their CSS rules
  3. Inline in <head> as <style>
  4. Load full CSS as non-blocking:
     <link rel="preload" href="/styles.css" as="style"
           onload="this.onload=null;this.rel='stylesheet'">
     <noscript><link rel="stylesheet" href="/styles.css"></noscript>

Tools:
  critical (npm) — extracts critical CSS automatically
  Critters (webpack plugin) — same, build-time

For personal sites: if total CSS < 15KB, just inline everything.
```

---

## JS Loading Strategy

```
Scripts that should be DEFERRED:
  - Analytics (GA, Plausible)
  - Chat widgets
  - Social embeds
  - Non-critical UI enhancements (theme toggle, smooth scroll)

Pattern:
  <script src="/analytics.js" defer></script>
  <script src="/main.js"      type="module"></script>
  <!-- type="module" is deferred by default -->

Scripts that must NOT be deferred:
  - Theme detection (FOUC prevention — must be inline, sync)
  - Critical polyfills

Bundle analysis:
  Run: npx vite build --report (Vite)
       npx webpack-bundle-analyzer (Webpack)
  Target: initial JS bundle < 100KB (gzipped)
  Red flag: any single dep > 50KB (find a smaller alternative)
```

---

## Lighthouse Audit Checklist

```
Run: npx lighthouse https://yoursite.com --output html

Performance targets:
  LCP:           ≤ 2.5s    ← hero is the bottleneck
  CLS:           ≤ 0.1     ← images/fonts are the culprit
  INP:           ≤ 200ms   ← JS bundle size + third-party
  TTFB:          ≤ 800ms   ← server / CDN issue
  Total size:    < 500KB   ← everything compressed
  JS bundle:     < 150KB   ← gzipped

Common Lighthouse kills:
  □ Render-blocking resources (defer CSS/JS)
  □ Images not sized (add width/height)
  □ Images not WebP (convert)
  □ Unused CSS (tree-shake or PurgeCSS)
  □ Unused JS (code split, lazy import)
  □ No caching headers (add Cache-Control)
  □ No gzip/brotli (enable on server)
```

---

## Performance Gates (Scored 0–10, Min 8)

```
Gate P1: LCP
  □ Hero image/text is preloaded?
  □ fetchpriority="high" on LCP element?
  □ LCP measured ≤ 2.5s on mobile 4G sim?
  Score: __ / 10

Gate P2: CLS
  □ All images have width + height attributes?
  □ No layout shifts from font swap?
  □ CLS score ≤ 0.1 in Lighthouse?
  Score: __ / 10

Gate P3: INP
  □ No long tasks > 50ms in main thread?
  □ Third-party scripts deferred?
  □ INP ≤ 200ms?
  Score: __ / 10

Gate P4: Asset Strategy
  □ Images served as WebP?
  □ Font-display: optional or swap with size-adjust?
  □ JS bundle < 150KB gzipped?
  Score: __ / 10

OVERALL: __ / 10   MINIMUM: 8.0
Lighthouse mobile score < 90 = automatic flag for all gates
```
