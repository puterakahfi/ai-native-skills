---
name: visual-hierarchy
version: 1.0.0
type: skill
description: >
  Visual hierarchy system — dominant/supporting/accent triad, inter-section
  weight decay, heading competition prevention.
tags: [design, hierarchy, typography, weight, contrast]
---

# Visual Hierarchy

## When to Load

Load when:
- Multiple sections each have a large heading (competition risk)
- H1 and H2 feel similar in weight
- Page feels "noisy" or lacks clear reading priority
- User eye doesn't know where to go next after hero

---

## The Triad: Dominant / Supporting / Accent

Every page has exactly one dominant element. One. Not one per section — one per page.

```
Dominant (1×):   H1 hero name — largest, highest contrast, most weight
Supporting (N×): Section headings (H2) — clearly subordinate to dominant
Accent (N×):     Labels, tags, meta — decorative, never competes

Scale law: Supporting must be ≤ 60% of dominant size
           Accent must be ≤ 40% of dominant size

Example:
  Dominant H1:  56px (3.5rem)
  Supporting H2: 32px (2rem)   → 32/56 = 57% ✅
  Accent label: 11px (0.69rem) → 11/56 = 20% ✅

VIOLATION: H2 "One codebase. Five products." at 64px with H1 at 56px
  → H2 > H1 → hierarchy inverted → FAIL
```

---

## Inter-Section Weight Decay

As user scrolls down, section headings must progressively carry less weight than the hero.

```
Section 1 (Hero):    H1 — maximum weight — page anchor
Section 2 (Work):    H2 — ≤ 60% of H1 weight — clearly subordinate
Section 3 (About):   H2 — same or less than section 2 — no escalation
Section 4 (Contact): H2 — minimal — directional, not declarative

Weight = f(size, contrast, spacing above)
  More space above = more weight (isolation effect)
  Less space above = less weight (context absorbed by prior section)

VIOLATION: About H2 "One codebase. Five products." = large, bold, lots of space above
  → reads as second hero → user confused about page structure
FIX: reduce size OR reduce isolation spacing OR make it a supporting statement, not a heading
```

---

## Heading Role Taxonomy

Before writing any heading, declare its role:

```
Role: ANCHOR      → H1 only. Full weight. Establishes identity.
Role: SECTION     → H2. Navigational. "What this section is about."
                     Should be short (≤ 4 words) and directional.
Role: STATEMENT   → H2 styled differently. Bold claim. Used in About/manifesto.
                     DANGER: competes with H1 if same size. Must be smaller.
Role: LABEL       → Not a heading. Use <div class="section-label">. Decorative.
```
pkahfi.com heading map:
  Hero:     "Putera Kahfi."        → ANCHOR    (H1, clamp max 3.5rem)
  Work:     "Selected work"        → LABEL     (sr-only H2, visible div)
  About:    "One codebase..."      → STATEMENT (H2, clamp max 2rem — MUST be < H1 max)
  Contact:  "Let's talk."          → SECTION   (H2, clamp max 2.5rem, directional)

VIOLATION: About H2 clamp(2.5rem,...,4rem) > H1 clamp max → hierarchy inverted → FAIL
FIX: About STATEMENT H2 max = 60% of H1 max. If H1 max = 3.5rem → About H2 max = 2.1rem
```

---

## Contrast as Hierarchy Signal

Size alone is not enough — contrast differentiates hierarchy levels.

```
Level 1 (Dominant):   color: var(--bright)   — #f2f2ea — near white
Level 2 (Supporting): color: var(--text)     — #d0d0c5 — off-white
Level 3 (Body):       color: var(--subtle)   — #78786f — warm gray
Level 4 (Accent):     color: var(--muted)    — #565652 — dark gray

Rule: each level must have visually distinct contrast from adjacent levels.
      ΔL* (CIELAB lightness delta) ≥ 15 between adjacent levels.

VIOLATION: heading and body text same color → hierarchy collapse → FAIL
```

---

## Gate: Visual Hierarchy (for redesign-workflow integration)

```
Gate H1: Dominant/Supporting Ratio
  □ Supporting H2 ≤ 60% of H1 size
  □ No H2 larger than H1 — ever
  □ Accent elements ≤ 40% of H1 size
  Score: __ / 10

Gate H2: Inter-Section Weight Decay
  □ No section heading carries more visual weight than hero H1
  □ About/manifesto headings are sized as STATEMENT (< H1), not ANCHOR
  □ Contact heading is directional and minimal
  Score: __ / 10

Gate H3: Contrast Levels
  □ At least 3 distinct contrast levels visible on page
  □ Adjacent hierarchy levels have ΔL* ≥ 15
  Score: __ / 10
```
