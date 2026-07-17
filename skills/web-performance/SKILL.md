---
name: web-performance
description: Web performance skill — Core Web Vitals scoring, LCP/CLS/INP optimization, font loading, critical CSS, image strategy, and JS bundle analysis. Design decisions that directly affect Lighthouse score and user experience.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/engineering/web-performance.contract.yaml
  ai-native-skills.related_skills: '["design-system", "accessibility", "responsiveness"]'
---

# Web Performance Skill

> **HARD RULES**
> - Measure before optimizing — no guessing, run Lighthouse first
> - Core Web Vitals are the gate: LCP ≤ 2.5s, INP ≤ 200ms, CLS ≤ 0.1
> - Never sacrifice readability for micro-optimizations

## Quick Reference

| Phase | What to Do | Reference |
|---|---|---|
| Diagnosis & asset strategy | Core Web Vitals (LCP/CLS/INP), font loading options, image format decisions | [core-vitals-and-assets.md](references/core-vitals-and-assets.md) |
| CSS, JS & scoring gates | Critical CSS, JS defer strategy, Lighthouse audit, performance gates | [css-js-and-gates.md](references/css-js-and-gates.md) |

## When to Use This Skill

- Lighthouse score < 90 on mobile
- LCP, CLS, or INP failing Core Web Vitals thresholds
- Designing a new page/feature with performance requirements
- Reviewing a PR that touches images, fonts, CSS, or JS loading

## Decision Flow

```
Run Lighthouse first → identify failing gate (LCP / CLS / INP / Assets)

LCP failing?
  └─ Is hero image lazy-loaded? → Remove lazy, add fetchpriority="high" + preload
  └─ Is LCP font-blocked? → Use font-display: optional or preload font file

CLS failing?
  └─ Images missing width/height? → Add dimensions
  └─ Font swap causing reflow? → Apply size-adjust fallback metrics

INP failing?
  └─ Long tasks on main thread? → scheduler.yield() or Web Worker
  └─ Third-party scripts? → defer + async, or facade pattern

Asset score low?
  └─ Not WebP? → Convert images
  └─ JS > 150KB gzipped? → Code split, lazy import heavy deps
```

## Metric Targets

| Metric | Target | Common Culprit |
|---|---|---|
| LCP | ≤ 2.5s | Unpreloaded hero, FOIT |
| CLS | ≤ 0.1 | Images without dimensions, font swap |
| INP | ≤ 200ms | JS bundle size, third-party scripts |
| TTFB | ≤ 800ms | Server / CDN |
| JS bundle | < 150KB gzipped | Unoptimized deps |

## Performance Gate Summary (Min score: 8/10 each)

- **P1 LCP** — hero preloaded + fetchpriority="high" + ≤ 2.5s on mobile 4G
- **P2 CLS** — all images sized + no font-swap shifts + ≤ 0.1
- **P3 INP** — no long tasks > 50ms + third-party deferred + ≤ 200ms
- **P4 Assets** — WebP images + font-display optimized + JS < 150KB gzipped

---

Load [core-vitals-and-assets.md](references/core-vitals-and-assets.md) for LCP/CLS/INP deep dives, font loading strategy, size-adjust CSS, and image format decision tree.

Load [css-js-and-gates.md](references/css-js-and-gates.md) for critical CSS extraction, JS defer patterns, Lighthouse audit checklist, and scored performance gates.
