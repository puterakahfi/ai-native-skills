---
name: design-audit
description: Standalone design audit — inspect an existing UI surface and produce a scored gap report without redesigning. Use before redesign-workflow to understand what needs fixing, or as a periodic health check on shipped surfaces.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.related_skills: '["redesign-workflow","design-review","design-refinement","master-design","accessibility","readability","responsiveness"]'
---

# Design Audit

Inspect → score → report. No redesign output. Produces an actionable gap report.

## When to Use

- Before starting a redesign (understand the current state first)
- Periodic health check on a shipped surface
- Stakeholder audit — "what's actually wrong and why"
- Deciding between `design-refinement` (targeted fix) vs `redesign-workflow` (full rebuild)

**Output**: scored gap report + prioritized fix list, not new HTML.

---

## Audit Process

### Step 1 — Capture current state

```
browser_navigate(target)
browser_vision("Full visual audit: hierarchy, CTA, typography, spacing, first impression")
browser_snapshot(full=true)

DOM probes:
  document.styleSheets.length          → > 0
  getComputedStyle(body).backgroundColor → not rgba(0,0,0,0)
  document.documentElement.scrollWidth > innerWidth → false (no overflow)
  [...querySelectorAll('a,button')].filter(el => {
    const b = el.getBoundingClientRect();
    return b.width > 0 && b.height > 0 && (b.width < 44 || b.height < 44);
  }).length  → 0 (no small touch targets)
  document.querySelector('h1')?.getBoundingClientRect().top / innerHeight * 100 → < 50%
```

### Step 2 — Score against gates

Load `design-review` skill. Score each gate 0–10.

Fast audit (subset) — score these 8 critical gates first:
```
□ G2:  Typographic scale — H1/body ratio ≤ 3.5x?
□ G8:  First impression  — H1 = stance in 50ms?
□ G9:  Line length       — prose ≤ 65ch, bio ≤ 44ch?
□ G14: Touch targets     — interactive ≥ 44×44px?
□ G16: Semantic HTML     — nav/main/section/footer + heading hierarchy?
□ G21: Reduced motion    — @media(prefers-reduced-motion) present?
□ R1:  Type pairing      — display face ≠ body face?
□ C1:  Focal point       — H1 visible ≤ 50% from top, no void above?
```

Full audit — score all gates from `design-review` skill (35+ gates).

### Step 3 — Classify each failure

For each failing gate (< 8.0):
```
Gate:    [id + name]
Score:   [n] / 10
Finding: [what is actually wrong — specific, not generic]
Skill:   [which skill encodes the fix rule]
Fix:     [specific action — e.g. "add @media(prefers-reduced-motion:reduce) to .hero-name transition"]
Effort:  [low | medium | high]
```

### Step 4 — Prioritize

Cluster findings into:
```
CRITICAL (score < 5):  fix before any visual polish
  → usually: G21 reduced motion, G16 semantic HTML, G14 touch targets

IMPORTANT (score 5–7): fix in next iteration
  → usually: G2 type scale, G8 first impression, G9 line length

POLISH (score 7–8):    fix when other gates pass
  → usually: C2 weight distribution, G5 whitespace rhythm
```

---

## Audit Report Format

```
DESIGN AUDIT — [target]
════════════════════════
Date: [date]
Surface: [type]
Overall avg: X.X / 10
Status: PASS (≥8.0) | NEEDS WORK | CRITICAL

CRITICAL (< 5):
  Gate G21 Reduced Motion: 0/10
  Finding: No @media(prefers-reduced-motion:reduce) on any animation
  Fix: Add reduced-motion override to all transitions/animations
  Effort: low

IMPORTANT (5–7):
  Gate G2 Typographic Scale: 6/10
  Finding: Hero H1 = 7rem, body = 18px → ratio 6.2x (max 3.5x)
  Fix: Clamp hero to clamp(3rem, 2rem+4vw, 4.5rem)
  Effort: low

POLISH (7–8):
  Gate C2 Weight Distrib: 7/10
  Finding: Two elements competing for H1 weight in hero
  Fix: Reduce about-heading to font-weight:500, font-size:1.6rem
  Effort: low

RECOMMENDED ACTION:
  [ ] Use design-refinement for targeted gate fixes (IMPORTANT + POLISH)
  [ ] Use redesign-workflow for full rebuild (if CRITICAL count ≥ 3)
════════════════════════
```
