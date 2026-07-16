---
name: redesign-workflow
description: Autonomous landing page redesign loop — audit site, confirm spec, produce HTML prototype, run design-review gates, fix failures, deliver only when all gates pass. Self-correcting loop, max 3 iterations.
version: 1.0.0
author: puterakahfi
license: MIT
type: workflow
implements: ai-native-core/contracts/workflows/redesign.contract.yaml
related_skills: [master-design, ux-psychology, design-review, design-system, ux-ui-patterns, readability, responsiveness, accessibility, motion-design, design-genre, macrostructures, content-strategy, web-performance]
skill_load_order:
  - phase: preflight
    skills: [design-genre, macrostructures, information-architecture]
  - phase: audit
    skills: [ux-psychology, accessibility, readability, responsiveness, web-performance]
  - phase: spec
    skills: [product-manager, master-design, content-strategy]
  - phase: produce
    skills: [design-genre, macrostructures, design-system, ux-ui-patterns, master-design, motion-design, composition, visual-hierarchy, copywriting, cro]
  - phase: pre-emit-critique
    skills: [master-design, ux-psychology, composition, visual-hierarchy, copywriting, cro]
  - phase: review
    skills: [design-review, readability, responsiveness, accessibility, motion-design, web-performance, content-strategy, composition, visual-hierarchy, copywriting, cro]
  - phase: fix
    skills: [design-genre, macrostructures, design-system, ux-ui-patterns, master-design, readability, responsiveness, motion-design, content-strategy, composition, visual-hierarchy, copywriting, cro]
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

## Phase 0: PRE-FLIGHT

Before anything — scan the target for existing design context:

```
Pre-flight scan (in order):
  1. design.md / DESIGN.md at project root → locked design system, overrides all picks
  2. CSS custom properties (:root vars) → existing palette + type scale
  3. package.json deps → framework, motion libs, font packages
  4. Existing macrostructure stamp: /* macrostructure: <name> */ in any CSS
  5. Deployed site: browser_navigate → browser_vision → capture palette, fonts, layout

Output (emit once):
  Pre-flight findings:
  · Existing palette: [found | not found]
  · Existing font stack: [found | not found]
  · Motion stance: [motion-on | motion-cut] (based on deps)
  · Macrostructure in use: [name | none]
  · Design system locked: [yes (design.md) | no]

  Hallmark will preserve: [list]
  Will introduce: [list]
  If wrong: correct me before I proceed.

If no signals found: "No pre-flight signals — proceeding with full stack."
```

## Phase 0.5: GENRE + MACROSTRUCTURE PICK

This phase has two gates. Both must pass before Phase 1.

---

### Gate A: Genre Detection (from `design-genre` skill)

Read signals from brief + pre-flight. Assign one genre.

```
Signal → Genre mapping:
  personal page + no CTA + showcase only     → editorial
  SaaS product + pricing + CTAs              → modern-minimal
  creative portfolio + visual work           → atmospheric
  game / toy / consumer app                  → playful
```

State explicitly:
```
Genre: [name]
Signals matched: [list signals from brief that confirm this genre]
```

---

### Gate B: Macrostructure Pick (from `macrostructures` skill)

**Step 1 — Extract brief signals:**
```
□ Primary goal:      [convert | showcase | inform | entertain]
□ Identity weight:   [high = person/brand leads | low = work leads]
□ Content volume:    [N products / N sections / N words]
□ Audience:          [hiring manager | client | developer | general]
□ CTA present:       [yes | no]
□ Visual assets:     [yes = images/screenshots | no = text only]
```

**Step 2 — Match signals to pattern:**

| Goal | Identity | Content vol | Audience | Best macrostructure |
|---|---|---|---|---|
| showcase | high | low (≤3) | hiring manager | Marquee Hero or Specimen |
| showcase | high | low (≤3) | creative client | Studio or Atelier |
| showcase | low | high (4+) | any | Bento or Workbench |
| inform | low | high | developer | Long Document or Almanac |
| convert | low | medium | general | Newsprint or Manifesto |
| brand | high | low | general | Manifesto or Lumen |

**Step 3 — Diversification check (secondary, not primary):**
```
Previous macrostructure: [name from last iteration or "none"]
Candidate macrostructure: [name]
Axes that differ: [list — layout lead / heading / divider / button / image / reveal]
Must differ on ≥2 axes IF previous exists.
If brief-match and diversification conflict → brief-match WINS.
```

**Step 4 — State your pick with justification:**
```
Macrostructure: [name]
Genre: [name]

Justified by brief signals:
  - [signal 1] → [why this supports the pick]
  - [signal 2] → [why this supports the pick]
  - [signal N] → ...

NOT chosen [alternative] because:
  - [reason 1]
  - [reason 2]

Diversification: differs from [previous] on [N] axes: [list axes]
```

**Justification is mandatory.** "Differs from previous" alone is NOT sufficient.
If you cannot justify from brief signals, revisit Step 2 before proceeding.

---

### pkahfi.com example (reference)

```
Brief signals:
  Primary goal:   showcase
  Identity:       high — personal landing page, person leads
  Content vol:    low — 2 LIVE products only
  Audience:       hiring manager / fellow engineer
  CTA:            none
  Visual assets:  none (text-led)

Signal → pattern match:
  showcase + identity high + content low + hiring manager → Marquee Hero or Specimen

Pick: Marquee Hero
  - Identity high: full-width name above fold, work below
  - 2 products: stacked list, not grid (low volume = list beats grid)
  - No CTA: hero does not need action urgency layout
  - Hiring manager: credibility via copy, not visual flair

NOT Studio:
  - Studio = 50/50 split → identity and work equal weight
  - pkahfi.com identity should lead, work is secondary
  - Studio better for creative agency where work IS the identity
```

Load `design-genre` skill. Detect genre from brief signals.
Load `macrostructures` skill. Pick ONE macrostructure.

```
State out loud before writing any code:

Genre: [editorial | modern-minimal | atmospheric | playful]
Signal: [what triggered it | default]
Macrostructure: [name]
Layout lead: [type-led | image-led | grid-led | document-led]
Differs from last on: [axes | first build]

If unsure between 2 macrostructures: offer 3 from categorically different groups,
let user pick, or pick the most distant from default (not Specimen, not Marquee Hero).
```



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

Produce HTML prototype. Apply design in this order:
1. Genre tokens (from `design-genre` skill — voice, color family, motion stance)
2. Macrostructure structure (from `macrostructures` skill — layout, heading, dividers)
3. Design system tokens (from `design-system` skill — spacing, type scale, color semantic)
4. Motion (from `motion-design` skill — only if motion-on)
5. Content (from `content-strategy` skill — microcopy, button labels, empty states)

Stamp at top of CSS (mandatory):
```css
/*
 * macrostructure: [name]
 * genre: [genre]
 * theme: [theme name | custom]
 * iteration: [N]
 */
```

### Pre-Emit Self-Critique (run BEFORE delivering output)

Score 1–5 on six axes. Anything < 3 = revision pass before emit.

```
Pre-emit critique:
  P (Philosophy):  Does every element have a reason to exist?        __ / 5
  H (Hierarchy):   Is the visual hierarchy immediately readable?     __ / 5
  E (Execution):   Are spacing, scale, alignment consistent?         __ / 5
  S (Specificity): Is copy specific, not generic? No AI slop?        __ / 5
  R (Restraint):   Is anything decorative that could be removed?     __ / 5
  V (Variety):     Does this differ structurally from last output?   __ / 5

Revision trigger: any axis < 3
Fix the lowest axis before delivering.

Stamp in CSS: /* pre-emit: P_ H_ E_ S_ R_ V_ */
```

### Slop Red List (auto-revision if any present)

```
❌ "Get started for free" as primary CTA (unless product requires it)
❌ Hero with H1 + 3 bullet features + CTA button (template pattern)
❌ "Trusted by X companies" with logo row in hero
❌ Testimonial grid with star ratings
❌ Gradient mesh background behind text
❌ Generic stock photo of diverse people in office
❌ "Seamless", "leverage", "world-class", "cutting-edge" in copy
❌ 6+ feature cards in equal-size grid
❌ Login button in hero for first-time visitor page
❌ All-caps nav with 5+ items
```


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
Gate 2: Typographic Scale   (1.333 modular, H1/body ≤ 3.5x DESKTOP, ≤ 3.0x MOBILE)
  Common violation: clamp hero to 7rem (112px) with 21px body = 5.3x → FAIL
  Fix: clamp max ≤ 4.5rem for hero, or raise body size proportionally
  Score: __ / 10
Gate 3: Color Semantic      (one token = one role, no collapse)        Score: __ / 10
Gate 4: Figure/Ground       (bg depth: texture/gradient/alt)           Score: __ / 10
Gate 5: Whitespace Rhythm   (hero ≠ content ≠ contact padding)        Score: __ / 10

── UX/UI PATTERNS ─────────────────────────────────
Gate 6: Hero Pattern        (correct pattern for page goal, spec met)  Score: __ / 10
Gate 7: Layout Grid         (column count matches content count)       Score: __ / 10
Gate 8: First Impression    (50ms: stance not job description)         Score: __ / 10

── READABILITY ─────────────────────────────────────
Gate 9:  Line Length
  □ Hero stance/bio: max-width 44ch (NOT px — px exceeds 65 CPL at large viewport)
  □ Body prose: max-width 65ch
  Common violation: max-width:553px → 72 CPL at 21px font → FAIL
  Score: __ / 10
Gate 10: Contrast Ratio     (primary ≥ 4.5:1, secondary ≥ 3:1)       Score: __ / 10
Gate 11: Type Size          (body ≥ 16px, smallest ≥ 12px)           Score: __ / 10
Gate 12: Cognitive Ease     (H1 ≤ 8 words, ≤ 4 sentences/para)       Score: __ / 10

── RESPONSIVENESS ──────────────────────────────────
Gate 13: Mobile Layout      (1-col, no overflow)                       Score: __ / 10
Gate 14: Touch Targets      (interactive ≥ 44×44px)                   Score: __ / 10
Gate 15: Type Scaling       (clamp() or mobile cap, ratio ≤ 3.5x)    Score: __ / 10

── ACCESSIBILITY ───────────────────────────────────
Gate 16: Semantic Structure
  □ main, nav[aria-label], footer, sections with aria-labelledby
  □ H1→H2→H3 — no heading level skips
  □ Work/product list: must have H2 even if visually-hidden
  Common violation: work section uses div+div, no H2 → heading outline broken
  Fix: .sr-only { position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0,0,0,0); }
       Add <h2 class="sr-only">Selected work</h2> inside section
  Score: __ / 10
Gate 17: Interactive A11y   (descriptive links, focus states visible)  Score: __ / 10

── COMPOSITION + VISUAL HIERARCHY ──────────────
Gate C1: Focal Point Above-Fold
  □ H1/name visible within first 100vh
  □ Sits at ≤ 50% from top (optical center)
  □ No unframed dead space above focal point
  Common violation: justify-content:flex-end on 100vh → H1 at 80% → void above → FAIL
  Score: __ / 10

Gate C2: Visual Weight Distribution
  □ One heavy (H1), one supporting (H2), one accent (label) — identifiable
  □ No two elements compete for dominance
  Score: __ / 10

Gate C3: Alignment & Anchoring
  □ Every element aligned to grid column, sibling edge, or center axis
  □ No magic-number positioning
  □ Spacing multiples of 8px base unit
  □ No floating/unanchored elements ("ngambang")
  Score: __ / 10

Gate H1: Dominant/Supporting Ratio
  □ Supporting H2 ≤ 60% of H1 size
  □ No H2 larger than H1
  Score: __ / 10

Gate H2: Inter-Section Weight Decay
  □ No section heading carries more visual weight than hero H1
  □ About/manifesto H2 sized as STATEMENT (< H1), not ANCHOR
  Score: __ / 10


Gate 18: Motion Purpose     (every animation = user signal)            Score: __ / 10
Gate 19: Duration + Easing  (hover≤200ms, ease-out enter, ease-in exit) Score: __ / 10
Gate 20: GPU Performance    (transform+opacity only, will-change)      Score: __ / 10
Gate 21: Reduced Motion     (HARD GATE — 0 or 10)                     Score: __ / 10
Gate 22: Cinematic Ratio    (hero=max, contact=min, decreasing)        Score: __ / 10

════════════════════════════════════════════════════
CLUSTER SCORES:
  Design System:    G1         = __ / 10
  Visual Design:    G2–5  avg  = __ / 10
  UX/UI Patterns:   G6–8  avg  = __ / 10
  Readability:      G9–12 avg  = __ / 10
  Responsiveness:   G13–15 avg = __ / 10
  Accessibility:    G16–17 avg = __ / 10
  Motion Design:    G18–22 avg = __ / 10  (G21 hard gate)

OVERALL: __ / 10   MINIMUM: 8.0
Gate 21 (Reduced Motion) = non-negotiable: score 0 = automatic full fail
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

Gate 5: Whitespace Rhythm
  □ Section label to first content item: minimum 24px gap (not 0)
  □ Label must have internal padding — never padding:0 when adjacent to cards
  □ No gray void: flex panels use flex:1 on children, not justify-content:center
  □ Split-panel: right panel padding=0, spacing via internal card padding only
  □ Section padding: each section has differentiated top/bottom — no two sections same weight
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

## Phase 5: FIX (Skill-First Mandatory)

When any gate scores < 8.0, run this sequence IN ORDER. Skipping step A is NOT allowed.

```
Step A — Root cause classification (mandatory before any fix):

  For each failing gate, answer:
    1. Which skill encodes the rule for this gate?
    2. Is the rule present in that skill? (yes/no)
    3. If no → the skill is the root cause → patch skill first
    4. If yes → was the rule followed in the output? (yes/no)
    5. If no → the output violated an existing rule → still patch skill
       (add a "common violation" or "pitfall" note to the relevant rule)
    6. Document: SKILL: [name] | RULE: [quoted] | GAP: [what was missing]

Step B — Patch the skill:

  For each root cause identified in Step A:
    - Open the relevant skill file
    - Add/strengthen the missing rule, example, or pitfall
    - Be specific: not "use proper spacing" but "section-label padding must be
      var(--sp-6) var(--sp-6) var(--sp-5) — never 0 when adjacent to cards"
    - Commit the patch to skill before producing new output

Step C — Reproduce from patched skill:

  Re-run Phase 3 (PRODUCE) with the patched skill loaded.
  Do NOT patch the HTML output directly — reproduce from skill.
  This is the only way to verify the skill fix actually works.

Step D — Re-score:

  Re-run Phase 4 (REVIEW) on the new output.
  Compare scores iteration-to-iteration.
  If a gate that previously passed now fails → skill patch introduced regression → fix.
```

## Phase 6: AUTONOMOUS LOOP

Run Phases 3→4→5 autonomously until exit condition.

```
LOOP STATE:
  iteration:     1
  max:           5 (default, configurable)
  skill_patches: []   ← log every skill patched this session
  score_history: []   ← [iter1_score, iter2_score, ...]

LOOP BODY (repeat):
  1. Phase 3: PRODUCE
     → Write HTML from current skill state
     → Stamp: macrostructure, genre, iteration N, pre-emit scores

  2. Phase 4: REVIEW
     → Score all 22 gates
     → Compute overall average
     → Log: score_history.append(avg)

  3. Check exit:
     IF avg >= 8.0 → EXIT → Phase 7: DELIVER
     IF iteration >= max → EXIT → Phase 7: DELIVER (with gap report)

  4. Phase 5: FIX (skill-first mandatory)
     → Root cause → patch skill → log skill_patches
     → iteration++
     → go to step 1

LOOP REPORT (emit at exit):
  ════════════════════════════════
  Autonomous loop complete: N iterations
  Score progression: [8.0 → 8.4 → 9.1 → 9.6]
  Skills patched this session:
    - macrostructures: Studio split-panel rules
    - redesign-workflow: Gate 5 whitespace proximity
    - master-design: section label padding
  Final score: 9.6 / 10
  Status: ✅ PASS (>= 8.0)

  Residual gaps (if max reached before 8.0):
    Gate N: [description] — [score] — [why not fixed in N iterations]
    Recommendation: extend loop or manual review
  ════════════════════════════════

EXTENSION PROMPT (if max reached, score < 8.0):
  "Loop reached max N iterations. Score: X.X / 10.
   Residual gaps: [list]. Extend loop? (Y = 3 more iterations)"
```

### Why skill-first loop beats output-first loop

```
Output-first loop (wrong):           Skill-first loop (correct):
  Iter 1: produce bad output           Iter 1: produce → review → gap found
  Iter 1: fix HTML directly            Iter 1: patch SKILL → reproduce
  Iter 2: produce from same skill      Iter 2: produce from BETTER skill
  Iter 2: same mistake, fix again      Iter 2: mistake doesn't recur
  Iter 3: same mistake, fix again      Iter 3: new gap → patch skill
  → skill never improves               → skill accumulates knowledge
  → mistakes repeat across sessions    → mistakes do not repeat across sessions
``` (if gates fail)

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
