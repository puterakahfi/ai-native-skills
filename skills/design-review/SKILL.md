---
name: design-review
description: Scored design gate check — load this skill during Phase 5 of redesign-workflow, or standalone to score any UI surface. Contains the complete 35+ gate scorecard. Load on-demand, not always-on.
license: MIT
metadata:
  ai-native-skills.version: 2.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.related_skills: '["design-audit","design-refinement","redesign-workflow","master-design","accessibility","readability","responsiveness","motion-design","composition","visual-hierarchy","copywriting","cro"]'
---

# Design Review

Scored gate check. Minimum **8.0 average** to pass. Gate G21 = hard gate.

<!-- LOAD ON-DEMAND — not always-on. Load in Phase 5 of redesign-workflow or standalone audit. -->

## Quick Score (8 critical gates — run first)

```
□ G2:  Typographic scale — H1/body ratio ≤ 3.5x desktop, ≤ 3.0x mobile?
□ G8:  First impression  — H1 stance readable in 50ms?
□ G9:  Line length       — prose ≤ 65ch, hero bio ≤ 44ch?
□ G14: Touch targets     — all interactive ≥ 44×44px?
□ G16: Semantic HTML     — nav/main/section/footer + H1→H2→H3?
□ G21: Reduced motion    — HARD GATE — @media(prefers-reduced-motion) present?
□ R1:  Type pairing      — display face ≠ body face?
□ C1:  Focal point       — H1 ≤ 50% from top, no void above?

If any score < 5 → CRITICAL → fix before full review.
```

---

## DOM Verification (run before scoring)

```js
JSON.stringify({
  sheets:    document.styleSheets.length,           // > 0
  bg:        getComputedStyle(document.body).backgroundColor, // not rgba(0,0,0,0)
  overflow:  document.documentElement.scrollWidth > innerWidth, // false
  touchFail: [...document.querySelectorAll('a,button')]
    .filter(el=>{const b=el.getBoundingClientRect();
      return b.width>0&&b.height>0&&(b.width<44||b.height<44);}).length, // 0
  h1TopPct:  Math.round(document.querySelector('h1')
    ?.getBoundingClientRect().top / window.innerHeight * 100), // < 50
});
```

---

## Full Scorecard (35+ gates)

### Design System
| Gate | Check | Min |
|---|---|---|
| G1 Token Completeness | All colors/spacing/type from declared tokens, no hardcoded hex/px | 8 |

### Visual Design
| Gate | Check | Min |
|---|---|---|
| G2 Typographic Scale | 1.333 modular, H1/body ≤ 3.5x desktop / ≤ 3.0x mobile | 8 |
| G3 Color Semantic | One token = one role, no collapse | 8 |
| G4 Figure/Ground | Bg has depth: texture/gradient/alternating sections | 8 |
| G5 Whitespace Rhythm | Hero ≠ content ≠ contact ≠ footer padding | 8 |

### Theme System
| Gate | Check | Min |
|---|---|---|
| T1 Token Architecture | Semantic tokens, no mode-specific hardcoded hex | 8 |
| T2 Toggle A11y | ≥44px target, aria-label = next action | 8 |
| T3 Dual-Theme QA | Light + dark DOM/screenshot both verified | 8 |
| T4 Contrast + Inversion | Primary ≥ 4.5:1 both modes | 8 |

### UX/UI Patterns
| Gate | Check | Min |
|---|---|---|
| G6 Hero Pattern | Correct pattern for page goal | 8 |
| G7 Layout Grid | Column count matches content count | 8 |
| G8 First Impression | H1 = stance in 50ms, not job description | 8 |

### Readability
| Gate | Check | Min |
|---|---|---|
| G9 Line Length | Hero bio ≤ 44ch, body prose ≤ 65ch | 8 |
| G10 Contrast Ratio | Primary ≥ 4.5:1, secondary ≥ 3:1 | 8 |
| G11 Type Size | Body ≥ 16px, smallest ≥ 12px | 8 |
| G12 Cognitive Ease | H1 ≤ 8 words, ≤ 4 sentences/para | 8 |

### Responsiveness
| Gate | Check | Min |
|---|---|---|
| G13 Mobile Layout | 1-col, no overflow at 375px | 8 |
| G14 Touch Targets | All interactive ≥ 44×44px | 8 |
| G15 Type Scaling | clamp() or mobile cap, ratio ≤ 3.0x mobile | 8 |

### Accessibility
| Gate | Check | Min |
|---|---|---|
| G16 Semantic Structure | nav/main/section/footer, H1→H2→H3, sr-only H2, skip link | 8 |
| G17 Interactive A11y | Descriptive links, focus:visible, aria-* attributes correct | 8 |

### Eight Universal Rules (from master-design)
| Gate | Check | Min |
|---|---|---|
| R1 Type | H1 font ≠ body font role (not just weight) | 8 |
| R2 Colour | Accent < 5% surface area, max 1 accent hue | 8 |
| R3 Space | All spacing = named token on 4px grid | 8 |
| R4 Motion | Every animation has prefers-reduced-motion override | 8 |
| R5 Voice | No buzzwords, distinct register | 8 |
| R6 Layout | At least one axis intentionally asymmetric | 8 |
| R7 Hierarchy | H2 ≤ 60% H1, max 3 visual weight levels | 8 |
| R8 Restraint | Every element has named role | 8 |

### Composition
| Gate | Check | Min |
|---|---|---|
| C1 Focal Point | H1 visible ≤ 50% from top, no dead space above | 8 |
| C2 Weight Distribution | One heavy (H1), one supporting (H2), one accent (label) | 8 |
| C3 Alignment | Grid-anchored, no magic-number px, no floating elements | 8 |

### Visual Hierarchy
| Gate | Check | Min |
|---|---|---|
| H1 Dominant/Supporting | H2 ≤ 60% of H1 size | 8 |
| H2 Inter-Section Decay | No section H2 heavier than hero H1 | 8 |
| H3 Heading Taxonomy | ANCHOR/SECTION/STATEMENT/LABEL roles identifiable | 8 |

### Motion
| Gate | Check | Min |
|---|---|---|
| G18 Motion Purpose | Every animation = user signal, not decoration | 8 |
| G19 Duration+Easing | Hover ≤ 200ms, ease-out enter, ease-in exit | 8 |
| G20 GPU Performance | transform+opacity only, will-change where needed | 8 |
| **G21 Reduced Motion** | **HARD GATE** — @media(prefers-reduced-motion) on ALL animations | **10** |
| G22 Cinematic Ratio | Hero=max, contact=min, decreasing through sections | 8 |

### CRO
| Gate | Check | Min |
|---|---|---|
| CRO1 Attention Flow | F-pattern or Z-pattern respected | 8 |
| CRO2 Trust Signals | Credibility anchors present, not fake social proof | 8 |
| CRO3 8-Second Window | Value prop clear in 8 seconds | 8 |
| CRO4 Persuasion Seq | Awareness → interest → desire → action flow | 8 |

### Copy / Content
| Gate | Check | Min |
|---|---|---|
| CP1 Value Prop | Passes 1000-person test — specific enough | 8 |
| CP2 Bio Length | ≤ 45 words | 8 |
| CP3 No Slop | No buzzwords from red list | 8 |
| CP4 Status Honesty | live/planned/lab/private/archived — accurate labels | 8 |

---

## Cluster Summary

```
Design System:   G1           = __ /10
Visual Design:   G2–G5  avg   = __ /10
Theme System:    T1–T4  avg   = __ /10
UX/UI Patterns:  G6–G8  avg   = __ /10
Readability:     G9–G12 avg   = __ /10
Responsiveness:  G13–G15 avg  = __ /10
Accessibility:   G16–G17 avg  = __ /10
Universal Rules: R1–R8  avg   = __ /10
Composition:     C1–C3  avg   = __ /10
Hierarchy:       H1–H3  avg   = __ /10
Motion:          G18–G22 avg  = __ /10  ← G21 hard gate
CRO:             CRO1–4 avg   = __ /10
Copy:            CP1–4  avg   = __ /10

OVERALL: __ / 10   PASS: ≥ 8.0
G21 = 0 → automatic full fail
```

---

## AI Slop Red List (auto-flag if present)

```
❌ "Seamless", "leverage", "world-class", "cutting-edge", "modern solution"
❌ H1 + 3 bullet features + CTA (template pattern)
❌ "Trusted by X companies" logo row
❌ 6+ equal-size feature cards
❌ Gradient mesh background behind text
❌ Color-only status signal (missing aria-label)
❌ All-caps nav with 5+ items
```
