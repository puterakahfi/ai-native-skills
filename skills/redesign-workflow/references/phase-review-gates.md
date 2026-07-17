# Phase 5 — REVIEW (Scored Gate Check)

Minimum **8.0 average** to pass. Gate 21 (Reduced Motion) = hard gate: 0 = full fail.

---

## Lightweight Iteration Checks (during active visual loops)

Do NOT run full build/lint/typecheck on every iteration. Keep loops fast:
```
□ browser visual check — all sections
□ browser visual check in every theme mode (light/dark)
□ theme toggle: light → dark → light, aria-label updates
□ DOM probes: overflow, sheets > 0, touch targets, H1 position
□ hash/link click checks on changed CTAs
□ git diff --check on changed files
```

Full build/lint only when: user approves, preparing PR/commit, or deploy-ready.

---

## DOM Verification Snippet (run after EVERY CSS change)

```js
JSON.stringify({
  sheets:    document.styleSheets.length,          // > 0
  bg:        getComputedStyle(document.body).backgroundColor, // not rgba(0,0,0,0)
  overflow:  document.documentElement.scrollWidth > innerWidth, // false
  touchFail: [...document.querySelectorAll('a,button')]
    .filter(el=>{const b=el.getBoundingClientRect();
      return b.width>0&&b.height>0&&(b.width<44||b.height<44);}).length, // 0
  h1TopPct:  Math.round(document.querySelector('h1')
    ?.getBoundingClientRect().top/window.innerHeight*100), // < 50
});
```

---

## Full Scorecard

```
DESIGN REVIEW — Iteration N
════════════════════════════════════════════════════

── DESIGN SYSTEM ──────────────────────────────────
G1:  Token Completeness
  □ All colors from semantic token table?
  □ All spacing from 8px grid tokens?
  □ All font-sizes from modular scale?
  □ No hardcoded hex/px outside token table?
  Score: __ / 10

── VISUAL DESIGN ──────────────────────────────────
G2:  Typographic Scale   (1.333 modular, H1/body ≤ 3.5x desktop, ≤ 3.0x mobile)
  Common violation: clamp hero 7rem + 21px body = 5.3x → FAIL
  Score: __ / 10
G3:  Color Semantic      (one token = one role, no collapse)           Score: __ /10
G4:  Figure/Ground       (bg depth: texture/gradient/alt sections)     Score: __ /10
G5:  Whitespace Rhythm   (hero ≠ content ≠ contact ≠ footer padding)  Score: __ /10

── THEME SYSTEM ───────────────────────────────────
T1:  Token Architecture  (semantic tokens, no mode-specific hex)       Score: __ /10
T2:  Toggle A11y         (≥44px, aria-label = next action)             Score: __ /10
T3:  Dual-Theme QA       (light + dark DOM/screenshot verified)        Score: __ /10
T4:  Contrast + Inversion(primary ≥ 4.5:1 both modes)                 Score: __ /10

── UX/UI PATTERNS ─────────────────────────────────
G6:  Hero Pattern        (correct pattern for page goal)               Score: __ /10
G7:  Layout Grid         (column count matches content count)          Score: __ /10
G8:  First Impression    (50ms: stance not job description)            Score: __ /10

── READABILITY ─────────────────────────────────────
G9:  Line Length         (hero bio ≤44ch, body prose ≤65ch)           Score: __ /10
G10: Contrast Ratio      (primary ≥4.5:1, secondary ≥3:1)             Score: __ /10
G11: Type Size           (body ≥16px, smallest ≥12px)                 Score: __ /10
G12: Cognitive Ease      (H1 ≤8 words, ≤4 sentences/para)             Score: __ /10

── RESPONSIVENESS ──────────────────────────────────
G13: Mobile Layout       (1-col, no overflow)                          Score: __ /10
G14: Touch Targets       (interactive ≥44×44px)                       Score: __ /10
G15: Type Scaling        (clamp() or mobile cap, ratio ≤3.0x mobile)  Score: __ /10

── ACCESSIBILITY ───────────────────────────────────
G16: Semantic Structure
  □ main / nav[aria-label] / footer / section[aria-labelledby]
  □ H1→H2→H3 — no skips
  □ Work section: sr-only H2 if visually hidden
  □ Skip link as first focusable element
  Score: __ /10
G17: Interactive A11y    (descriptive links, focus:visible, aria-*)   Score: __ /10

── EIGHT UNIVERSAL RULES ──────────────────────────
R1:  Type       H1 font ≠ body font role (not just weight diff)       Score: __ /10
R2:  Colour     Accent < 5% surface area, max 1 accent hue            Score: __ /10
R3:  Space      All spacing = named token on 4px grid                 Score: __ /10
R4:  Motion     Every animation has prefers-reduced-motion override   Score: __ /10
R5:  Voice      No buzzwords, distinct register, not neutral middle   Score: __ /10
R6:  Layout     At least one axis intentionally asymmetric            Score: __ /10
R7:  Hierarchy  H2 ≤ 60% H1, max 3 visual weight levels              Score: __ /10
R8:  Restraint  Every element has named role, nothing fills blindly   Score: __ /10

── COMPOSITION ─────────────────────────────────────
C1:  Focal Point       (H1 visible ≤50% from top, no dead space above)Score: __ /10
C2:  Weight Distrib    (one heavy, one supporting, one accent)         Score: __ /10
C3:  Alignment         (grid-anchored, no magic-number, no ngambang)   Score: __ /10

── VISUAL HIERARCHY ────────────────────────────────
H1:  Dominant/Supporting ratio (supporting H2 ≤60% of H1)            Score: __ /10
H2:  Inter-Section Decay (no section H2 heavier than hero H1)         Score: __ /10
H3:  Heading Taxonomy  (ANCHOR/SECTION/STATEMENT/LABEL roles clear)   Score: __ /10

── MOTION ──────────────────────────────────────────
G18: Motion Purpose    (every animation = user signal)                 Score: __ /10
G19: Duration+Easing   (hover≤200ms, ease-out enter, ease-in exit)    Score: __ /10
G20: GPU Performance   (transform+opacity only, will-change)          Score: __ /10
G21: Reduced Motion    *** HARD GATE — 0 = FULL FAIL ***              Score: __ /10
G22: Cinematic Ratio   (hero=max, contact=min, decreasing)            Score: __ /10

── CRO ─────────────────────────────────────────────
CRO1: Attention Flow   (F-pattern or Z-pattern respected)             Score: __ /10
CRO2: Trust Signals    (credibility anchors present, not fake)        Score: __ /10
CRO3: 8-Second Window  (value prop clear in 8s)                       Score: __ /10
CRO4: Persuasion Seq   (awareness → interest → desire → action)       Score: __ /10

── COPY / CONTENT ──────────────────────────────────
CP1: Value Prop        (passes 1000-person test — specific enough)    Score: __ /10
CP2: Bio Length        (≤45 words)                                    Score: __ /10
CP3: No Slop           (no buzzwords from red list)                   Score: __ /10
CP4: Status Honesty    (live/planned/lab/private/archived — accurate) Score: __ /10

════════════════════════════════════════════════════
CLUSTER SCORES:
  Design System:   G1          = __ /10
  Visual Design:   G2–G5  avg  = __ /10
  Theme System:    T1–T4  avg  = __ /10
  UX/UI Patterns:  G6–G8  avg  = __ /10
  Readability:     G9–G12 avg  = __ /10
  Responsiveness:  G13–G15 avg = __ /10
  Accessibility:   G16–G17 avg = __ /10
  Universal Rules: R1–R8  avg  = __ /10
  Composition:     C1–C3  avg  = __ /10
  Hierarchy:       H1–H3  avg  = __ /10
  Motion:          G18–G22 avg = __ /10  ← G21 hard gate
  CRO:             CRO1–4 avg  = __ /10
  Copy:            CP1–4  avg  = __ /10

OVERALL: __ / 10   MINIMUM: 8.0
G21 (Reduced Motion) — score 0 = automatic full fail regardless of average
════════════════════════════════════════════════════
Failing gates (< 8):
  Gate [id] [name]: score __ — fix: [specific action]
```
