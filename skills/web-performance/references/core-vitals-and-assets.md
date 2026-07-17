# Web Performance — Core Web Vitals, Fonts & Images

## Core Principle

```
Performance is a design decision, not a post-launch patch.

Every design choice has a performance cost:
  Custom fonts:       +200–800ms if loaded wrong
  Hero image:         +1–3s to LCP if not preloaded
  Unnecessary JS:     +100–500ms to INP
  Dynamic imports:    +50ms per chunk

The goal: Lighthouse 90+ on mobile. Not 90 on desktop.
```

---

## Core Web Vitals

### LCP — Largest Contentful Paint (target: ≤ 2.5s)

```
What: Time until the largest visible element is rendered
Usually: hero image, H1, or above-fold banner

Common failures:
  ❌ Hero image loaded lazily (lazy loading = never preload)
  ❌ Font blocking render (H1 uses custom font, FOIT)
  ❌ Server slow to respond (TTFB > 800ms)
  ❌ Image too large (no WebP, no srcset)

Fixes:
  ✅ <link rel="preload" as="image" href="/hero.webp">
  ✅ font-display: optional (or swap with fallback size match)
  ✅ srcset + sizes for responsive images
  ✅ Priority hint: <img fetchpriority="high" src="/hero.webp">
  ✅ If LCP = text: preload the font file, not just the CSS
```

### CLS — Cumulative Layout Shift (target: ≤ 0.1)

```
What: Sum of all unexpected layout shifts during page life
Caused by: content inserted above existing content, images without dimensions

Common failures:
  ❌ <img> without width/height attributes → shifts when loads
  ❌ Font swap causes text reflow (FOUT)
  ❌ Dynamic content inserted above fold (banners, cookie notices)
  ❌ CSS animations that move elements (not just transform)

Fixes:
  ✅ Always set width + height on <img> (or aspect-ratio in CSS)
  ✅ Reserve space for dynamic content (min-height on containers)
  ✅ Use transform for animations — never top/left/width
  ✅ Size-adjust font metric: make fallback font same size as custom font
  ✅ Cookie/consent banners: fixed position at bottom, not top
```

### INP — Interaction to Next Paint (target: ≤ 200ms)

```
What: Slowest interaction response time (click, tap, keypress)
Caused by: long JS tasks blocking main thread

Common failures:
  ❌ Synchronous heavy computation in event handler
  ❌ Unoptimized third-party scripts (analytics, chat widgets)
  ❌ Too much JS on main thread (large bundles)

Fixes:
  ✅ Break long tasks with scheduler.yield() or setTimeout(fn, 0)
  ✅ Load third-party scripts async + defer, or via facade
  ✅ Use Web Workers for heavy computation
  ✅ Virtualize long lists (only render visible items)
```

---

## Font Loading Strategy

```
Option 1: font-display: swap (fast but FOUT)
  - Text shows immediately in fallback font
  - Swaps when custom font loads
  - CLS risk: if fallback ≠ custom font metrics
  - Fix CLS: use size-adjust + ascent-override to match metrics

Option 2: font-display: optional (best for LCP, no FOUT)
  - Gives font 0ms to load (uses cache only)
  - If not cached, uses fallback — no swap ever
  - Best for: returning users, performance-critical pages
  - Downside: first-time users always see fallback

Option 3: font-display: block (avoid unless icon fonts)
  - Blocks render until font loads (FOIT)
  - Invisible text for up to 3 seconds
  - Only use for icon fonts where fallback = wrong character

Recommended for personal sites: optional with size-adjust
```

### Size-Adjust Fallback (eliminate CLS from font swap)

```css
@font-face {
  font-family: 'Inter Fallback';
  src: local('Arial');
  size-adjust: 107%;          /* adjust until metrics match */
  ascent-override: 90%;
  descent-override: 22%;
  line-gap-override: 0%;
}

body {
  font-family: 'Inter', 'Inter Fallback', system-ui, sans-serif;
}
```

---

## Image Strategy

```
Format decision tree:
  Photo/complex image?   → WebP (with JPEG fallback)
  Simple illustration?   → SVG
  Icon?                  → SVG (inline if < 1KB, external if reused)
  Animation?             → CSS animation > GIF (60% smaller)
  Video loop?            → <video autoplay muted loop> (not GIF)

<picture> pattern for modern formats:
  <picture>
    <source srcset="/hero.avif" type="image/avif">
    <source srcset="/hero.webp" type="image/webp">
    <img src="/hero.jpg" alt="..." width="1200" height="630"
         fetchpriority="high">  <!-- hero = high priority -->
  </picture>

Lazy loading — safe to use on below-fold images:
  <img src="/product.webp" loading="lazy" alt="..."
       width="800" height="600">

Never lazy load:
  - Hero image (LCP)
  - Above-fold images
  - Images in first two viewport heights
```
