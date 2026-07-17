# 02 · Marquee Hero

**Layout lead:** image-led (or full-bleed video/color)
**Best for:** Personal landing, campaign landing, atmospheric brand, product launch
**When NOT:** Documentation, complex product with many features

```
Layout lead:    image-led (or full-bleed video/color)
Heading:        Left-aligned, very large, optical center of viewport
Body:           Brief — 1–2 sentences below headline
Dividers:       Section breaks via background color change
Button voice:   Ghost or outline on dark, solid on light
Image:          Full-bleed background, or large centered image below headline
Reveal:         Hero entrance stagger (cinematic), scroll reveal below
```

---

## Mandatory CSS Pattern — NEVER improvise

```css
/* Marquee Hero = TOP-ANCHORED, not centered */
/* Void below content = intentional breathing room. Void above = dead space = FAIL. */
.hero {
  /* NO min-height: 100vh — forces void when content is sparse */
  display: block;
  padding-top: clamp(120px, 16vh, 180px);
  padding-bottom: clamp(80px, 14vh, 140px); /* generous but not full viewport */
  padding-left: var(--sp-8);
  padding-right: var(--sp-8);
  position: relative;
  border-bottom: 1px solid var(--border);
}
/* HARD RULE: min-height:100vh + sparse content = void = FAIL */
/* Use generous padding-bottom instead — breathing room without dead space */
/* HARD RULE: justify-content:center → content floats in tall 1fr row → void above AND below → FAIL */
/* HARD RULE: grid-template-rows with 1fr → same problem at tall viewports → FAIL */
/* HARD RULE: flex-end → name at 75%+ → dead space above → FAIL */
/* CORRECT: block + padding-top:clamp() → name anchored near top, void only below */

.scroll-cue {
  position: absolute;
  bottom: var(--sp-7);
  left: 50%;
  transform: translateX(-50%);
}
```

---

## Eye Flow

```
eyebrow (top of flex) → name (dominant) → stance (below) → meta (right) → scroll cue (bottom)
```

---

## Example Structure

```
┌──────────────────────────────────┐
│  — ENGINEER · YOGYAKARTA         │  eyebrow — first child of flex
│                                  │
│  Very Large                      │  H1 — dominant anchor
│  Name.                           │
│                                  │
│  Stance sentence. One sentence.  │  supporting
│                            Meta  │  accent
│                                  │
│              ↓ scroll            │  cue — absolute
└──────────────────────────────────┘
[work section below]
```

---

## Wide Screen Behavior

At wide viewports (1440px+), Marquee Hero can suffer void if using min-height:100vh.
Always use clamp-based padding instead:

```css
/* Scales with viewport height — no fixed void */
padding-top: clamp(120px, 16vh, 180px);
padding-bottom: clamp(80px, 14vh, 140px);
```

At 768px viewport height → name near top, breathing room below ✅
At 1440px viewport height → same ratio, still anchored near top ✅

---

## Checklist Before Shipping

```
□ No min-height:100vh on .hero
□ No justify-content:flex-end anywhere in hero
□ padding-top uses clamp()
□ Scroll cue is absolutely positioned (not in flow)
□ H1 dominates — eyebrow and stance are visually subordinate
□ Full-bleed background (if used) doesn't obscure text
□ Hero entrance animation: cinematic stagger (eyebrow → H1 → stance → meta → cue)
```
