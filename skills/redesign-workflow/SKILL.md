---
name: redesign-workflow
description: Autonomous landing page redesign loop — audit site, confirm spec, produce HTML prototype, run design-review gates, fix failures, deliver only when all gates pass. Self-correcting loop, max 3 iterations.
version: 1.0.0
author: puterakahfi
license: MIT
type: workflow
implements: ai-native-core/contracts/workflows/redesign.contract.yaml
related_skills: [master-design, ux-psychology, design-review, design-system, ux-ui-patterns, readability, responsiveness, accessibility]
skill_load_order:
  - phase: audit
    skills: [ux-psychology, accessibility, readability, responsiveness]
  - phase: spec
    skills: [product-manager, master-design, ux-ui-patterns]
  - phase: produce
    skills: [design-system, ux-ui-patterns, master-design]
  - phase: review
    skills: [design-review, readability, responsiveness, accessibility]
  - phase: fix
    skills: [design-system, ux-ui-patterns, master-design, readability, responsiveness]
---

# Redesign Workflow

## The Core Rule

```
This workflow runs autonomously until ALL design-review gates pass.
No delivery before gates are green.

Loop:
  audit → spec → produce → review → fix (if fail) → review → ... → deliver

Exit condition: all gates pass OR max_iterations (3) reached
On max_iterations: deliver best attempt + explicit gate failure report
```

---

## Parameters

| Param | Required | Description |
|---|---|---|
| `url` | YES | URL to audit and redesign |
| `goal` | YES | What the page should achieve |
| `products` | NO | List of LIVE products to show (skip DEV) |
| `cta` | NO | Primary CTA — default: none |
| `audience` | NO | Target audience — default: general |
| `output_path` | NO | Where to save HTML — default: /tmp/{domain}-redesign.html |

---

## Phase 1: AUDIT

```
1. browser_navigate(url)
2. browser_snapshot(full=true) — capture DOM structure
3. browser_vision("Full visual audit: hierarchy, CTA, typography, colors, whitespace, first impression")
4. Scroll and capture multiple sections if needed

Audit checklist:
  □ Current H1 and value proposition — what does it say?
  □ CTA count and placement — how many, where?
  □ Navigation items — count and labels
  □ Products/sections shown — which are LIVE vs DEV?
  □ Typography — feels proportional or arbitrary?
  □ Color usage — accent used for multiple meanings?
  □ Whitespace — uniform or rhythmic?
  □ First impression 50ms — what does user capture?
  □ Accessibility signals — semantic HTML present?
```

Output: `audit_report` object with findings per gate.

---

## Phase 2: SPEC CONFIRM

Before producing — align on constraints. Extract from params or ask:

```
spec = {
  goal:      "personal landing page" | "portfolio" | "SaaS marketing" | ...,
  products:  [list of LIVE products only — no DEV],
  cta:       "hire me" | "contact" | null,
  audience:  "hiring manager" | "client" | "developer" | "general",
  nav_items: derived from goal (3 max for personal),
  hero_copy: must pass 50ms test — stance, not job description
}
```

If `products` not provided → extract from audit, keep LIVE only.
If `cta` not provided → default null (showcase only).

State spec explicitly before proceeding:
```
SPEC CONFIRMED
──────────────
Goal:     personal landing page — showcase only
Products: Blog (LIVE), Blueprint (LIVE)
CTA:      none
Audience: general / developer community
Nav:      Work · About · Contact
```

---

## Phase 3: PRODUCE

Generate complete, self-contained HTML file.

### Mandatory Design System (apply every time)

**Typographic Scale — 1.333 Perfect Fourth:**
```css
--text-xs:   0.563rem;
--text-sm:   0.75rem;
--text-base: 1rem;
--text-lg:   1.333rem;
--text-xl:   1.777rem;
--text-2xl:  2.369rem;
--text-3xl:  3.157rem;
--text-4xl:  4.209rem;
/* Mobile: cap H1 at --text-3xl to keep H1/body ratio ≤ 3.5x */
```

**Color Semantic (declare before using):**
```css
/* Each var = ONE semantic role ONLY */
--live:             /* LIVE status indicator — nowhere else */
--interactive-hover:/* hover state — nowhere else */
--bg:               /* base background */
--bg-alt:           /* alternate section background (figure/ground) */
--surface:          /* card/elevated surface */
--border:           /* dividers */
--bright:           /* headings, primary content */
--text:             /* body text */
--subtle:           /* supporting info */
--muted:            /* decorative, disabled */
```

**Figure/Ground:**
```css
/* Always add depth to background — never flat single color */
background-image: radial-gradient(circle, #1e1e1e 1px, transparent 1px);
background-size: 32px 32px;
/* OR: linear-gradient(180deg, #0f0f0f 0%, #0a0a0a 100%) */
/* OR: alternating section backgrounds */
```

**Whitespace Rhythm:**
```
Hero section:    min-height: 100vh — maximum space, this is a statement
Content sections: 80–96px padding — tighter, reading mode
Contact section:  48–64px padding — minimal, closing quietly
Footer:           24–32px padding — functional only
```

**Empty State Rule:**
```
Count products before choosing layout:
  1 product  → full width
  2 products → full-width stacked (NOT 2-col grid)
  3 products → 3-col grid or stacked
  4+ products → grid
```

**First Impression (50ms):**
```
Hero copy must be a stance, not a job description.
Test: read H1 in 50ms — what ONE idea survives?
FAIL: "Full Stack Engineer specializing in scalable architecture"
PASS: "One codebase. Five products." / "I build systems meant to last."
```

**Accessibility:**
```html
<!-- Semantic structure required -->
<nav>, <main>, <section>, <footer>
<!-- Heading hierarchy: H1 → H2 → H3 — no skipping -->
<!-- Live badge: aria-hidden on decorative elements -->
<!-- Links: descriptive text, rel="noopener" for external -->
<!-- Images: meaningful alt or alt="" if decorative -->
```

---

## Phase 4: REVIEW (Scored Gate Check)

Run ALL 17 gates across 6 skill dimensions. Every gate scored 0–10. Minimum **8.0 average** to pass.

```
DESIGN REVIEW — Iteration N
════════════════════════════════════════════════════

── DESIGN SYSTEM ──────────────────────────────────
Gate 1: Token Completeness
  □ All colors from declared semantic token table?
  □ All spacing from 8px grid tokens?
  □ All font-sizes from modular scale?
  □ No hardcoded hex/px outside token table?
  Score: __ / 10

── VISUAL DESIGN ──────────────────────────────────
Gate 2: Typographic Scale   (1.333 modular, H1/body ≤ 3.5x mobile)   Score: __ / 10
Gate 3: Color Semantic      (one token = one role, no collapse)        Score: __ / 10
Gate 4: Figure/Ground       (bg depth: texture/gradient/alt)           Score: __ / 10
Gate 5: Whitespace Rhythm   (hero ≠ content ≠ contact padding)        Score: __ / 10

── UX/UI PATTERNS ─────────────────────────────────
Gate 6: Hero Pattern        (correct pattern for page goal, spec met)  Score: __ / 10
Gate 7: Layout Grid         (column count matches content count)       Score: __ / 10
Gate 8: First Impression    (50ms: stance not job description)         Score: __ / 10

── READABILITY ─────────────────────────────────────
Gate 9:  Line Length        (body ≤ 65ch, no full-width prose)        Score: __ / 10
Gate 10: Contrast Ratio     (primary ≥ 4.5:1, secondary ≥ 3:1)       Score: __ / 10
Gate 11: Type Size          (body ≥ 16px, smallest ≥ 12px)           Score: __ / 10
Gate 12: Cognitive Ease     (H1 ≤ 8 words, ≤ 4 sentences/para)       Score: __ / 10

── RESPONSIVENESS ──────────────────────────────────
Gate 13: Mobile Layout      (1-col, no overflow)                       Score: __ / 10
Gate 14: Touch Targets      (interactive ≥ 44×44px)                   Score: __ / 10
Gate 15: Type Scaling       (clamp() or mobile cap, ratio ≤ 3.5x)    Score: __ / 10

── ACCESSIBILITY ───────────────────────────────────
Gate 16: Semantic Structure (nav/main/section/footer, H1→H2→H3)      Score: __ / 10
Gate 17: Interactive A11y   (descriptive links, focus states visible)  Score: __ / 10

════════════════════════════════════════════════════
CLUSTER SCORES:
  Design System:    G1         = __ / 10
  Visual Design:    G2–5  avg  = __ / 10
  UX/UI Patterns:   G6–8  avg  = __ / 10
  Readability:      G9–12 avg  = __ / 10
  Responsiveness:   G13–15 avg = __ / 10
  Accessibility:    G16–17 avg = __ / 10

OVERALL: __ / 10   MINIMUM: 8.0
STATUS: ✅ PASS → deliver  |  ❌ FAIL → fix lowest scoring gates → re-review
════════════════════════════════════════════════════
Failing gates (< 8):
  Gate __ [name]: score __ — fix: [specific action]
```

Run all gates before any other action:

```
DESIGN REVIEW — Iteration N
────────────────────────────

Gate 1: Typographic Scale
  □ All font sizes from declared scale?
  □ H1/body ratio ≤ 3.5x on mobile?
  Result: PASS | FAIL (reason)

Gate 2: Color Semantic
  □ Each color var has exactly ONE semantic role?
  □ No accent used for multiple meanings?
  Result: PASS | FAIL (reason)

Gate 3: Figure/Ground
  □ Background has depth (texture/gradient/alternating)?
  □ Squint test: foreground separates from background?
  Result: PASS | FAIL (reason)

Gate 4: Whitespace Rhythm
  □ Sections have different padding weights?
  □ Hero ≠ content section padding?
  Result: PASS | FAIL (reason)

Gate 5: First Impression (50ms)
  □ H1 communicates ONE memorable idea?
  □ Not a job description or generic tagline?
  Result: PASS | FAIL (reason)

Gate 6: Empty State
  □ Grid layout matches product count?
  □ No 2 items in 4-column grid?
  Result: PASS | FAIL (reason)

Gate 7: Accessibility
  □ Semantic HTML: nav/main/section/footer?
  □ Heading hierarchy correct?
  □ External links have rel="noopener"?
  □ No button-in-anchor?
  Result: PASS | FAIL (reason)

Gate 8: CTA Clarity
  □ If CTA defined: single, prominent, clear action?
  □ If no CTA: no confusing pseudo-CTAs present?
  Result: PASS | FAIL (reason)

──────────────────────────────
TOTAL: N/8 gates passing
STATUS: PASS (deliver) | FAIL (fix → re-review)
```

---

## Phase 5: FIX (if gates fail)

For each failed gate — apply specific fix, do not rewrite from scratch:

| Gate Failure | Fix |
|---|---|
| Typographic scale | Replace all font-size values with scale vars |
| Color semantic | Rename vars, ensure each has one role |
| Figure/ground | Add dot-grid or gradient to body background |
| Whitespace rhythm | Adjust section padding to vary by weight |
| First impression | Rewrite H1 to stance — test 50ms |
| Empty state | Switch layout to match product count |
| Accessibility | Add missing semantic elements, fix hierarchy |
| CTA clarity | Remove duplicate CTAs, strengthen or remove |

After fix: goto Phase 4 (review). Do NOT skip review after fix.

---

## Phase 6: DELIVER

Only when: all 8 gates PASS (or max_iterations=3 reached).

```
Output:
1. Save HTML to output_path
2. MEDIA: output_path → deliver as file to user
3. Gate report summary
4. Key changes from original (table: before → after)
5. If max_iterations reached: honest report of remaining failures
```

Delivery format:
```
REDESIGN COMPLETE — pkahfi.com
──────────────────────────────
Gates: 8/8 passing
Iterations: N

Key changes:
  Before: [original issue]   After: [fix applied]
  ...

MEDIA: /tmp/pkahfi-redesign-v3.html
```

---

## Anti-Loop Protection

```
iteration_count = 0
max_iterations  = 3

before each produce/fix:
  iteration_count++
  if iteration_count > max_iterations:
    deliver current best
    report remaining failures
    STOP — do not loop again
```

If same gate fails 2 iterations in a row:
→ Try different approach for that gate specifically
→ Do not keep applying same fix that is not working
