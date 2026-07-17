# Phase 0.5 / 0.6 / 0.75 — Genre, Macrostructure, Visual Language, Layered Plan

## Phase 0.5: GENRE + MACROSTRUCTURE PICK

### Gate A: Genre Detection

```
Signal → Genre:
  personal page + no CTA + showcase only     → editorial
  SaaS product + pricing + CTAs              → modern-minimal
  creative portfolio + visual work           → atmospheric
  game / toy / consumer app                  → playful

State:
  Genre: [name]
  Signals matched: [list]
```

### Gate B: Macrostructure Pick

**Step 1 — Extract brief signals:**
```
□ Primary goal:    [convert | showcase | inform | entertain]
□ Identity weight: [high = person leads | low = work leads]
□ Content volume:  [N products / N sections]
□ Audience:        [hiring manager | client | developer | general]
□ CTA present:     [yes | no]
□ Visual assets:   [yes | no]
```

**Step 2 — Signal → Pattern:**

| Goal | Identity | Volume | Audience | Best macrostructure |
|---|---|---|---|---|
| showcase | high | ≤3 | hiring manager | Marquee Hero or Specimen |
| showcase | high | ≤3 | creative client | Studio or Atelier |
| showcase | low | 4+ | any | Bento or Workbench |
| inform | low | high | developer | Long Document or Almanac |
| convert | low | medium | general | Newsprint or Manifesto |
| brand | high | low | general | Manifesto or Lumen |

**Step 3 — Diversification check (secondary — brief-match WINS if conflict):**
```
Previous macrostructure: [name | none]
Candidate: [name]
Must differ on ≥2 axes IF previous exists.
Axes: layout-lead / heading / divider / button / image / reveal
```

**Step 4 — State pick with justification (mandatory):**
```
Macrostructure: [name]
Genre: [name]

Justified by:
  - [signal] → [why it supports this pick]

NOT chosen [alt] because:
  - [reason]
```

**pkahfi.com reference example:**
```
showcase + identity high + ≤2 products + hiring manager → Marquee Hero
NOT Studio: Studio = 50/50 split; pkahfi.com identity must lead
```

---

## Phase 0.6: VISUAL LANGUAGE DEFINITION

Translate theme word → concrete rules BEFORE touching UI.
"Minimalist" ≠ color swap. Define values first.

### Zen / Minimalist

**Core values:**
```
Ma / emptiness     → negative space IS content, not unused area
Restraint          → remove elements before styling them
Stillness          → no hover lift, bounce, glow, decorative urgency
One focal object   → one strong anchor per viewport
Low density        → few cards, few badges, few borders
Muted contrast     → ink/stone/paper/sage; accent is rare
```

**Palette:** paper white, warm ivory, mist gray, charcoal, ink black, stone, sage  
**NOT:** bright startup blue, neon, gradient mesh, glassmorphism  

**Layout:** large asymmetrical whitespace, narrow columns, intentional empty areas  
**NOT:** equal-weight card catalogs, filling grid space because it exists  

**Typography:** fewer sizes, lighter weights, larger line-height, one display moment per viewport  
**NOT:** font-black everywhere, H1/H2/H3 all shouting  

**Motion:** fade, slow reveal, opacity, tiny translate for orientation only  
**NOT:** hover lift on every card, springy/bouncy motion  

**Auto-fail if any after zen request:**
```
❌ Palette changed to brown/warm but density stays high
❌ Many cards + many badges + many tags = catalog, not zen
❌ Every section has bold headline + bordered card cluster
❌ Accent on labels, icons, badges, CTA, logo, bullets all at once
❌ Dark mode = heavy charcoal panel inversion only
❌ Motion added before silence and spacing are solved
```

**Zen check before calling pass:**
```
1. What did we remove?
2. Where is the intentional emptiness?
3. What is the single focal object per viewport?
4. Which elements became quieter, not just recolored?
5. With color removed — does composition still feel calm?
```

---

## Phase 0.75: LAYERED REDESIGN PLAN

Classify work into layers. Each iteration names ONE primary layer.

```
Layer 0: Strategy   — why the surface exists, what is remembered first
Layer 1: UI         — visual structure, typography, color, spacing, hierarchy
Layer 2: UX         — navigation, CTA clarity, hover/focus/tap, a11y behavior
Layer 3: Voice      — copy specificity, H1 stance, status language, no buzzwords
Layer 4: Interaction— hover, focus, scroll, theme transition, reduced motion
Layer 5: Delight    — motion detail, illustration, texture, visual metaphor
Layer 6: Verification—browser checks, DOM probes, theme QA, git diff
```

**Layer dependency — do not skip:**
```
Strategy failure   → blocks UI polish
UI failure         → blocks Delight
UX failure         → blocks final Verification
Voice failure      → blocks motion/illustration polish
```

**Iteration Declaration (emit at start of each iteration):**
```
Iteration N focus:
  Primary layer: [name]
  Secondary: [optional]
  Not touching: [deferred]
  Success criteria: [specific checks]
```

### Layer 5 — Delight asset classification:
```
□ code/vector (SVG/CSS/canvas)     → generatable by coding agent
□ raster AI image (DALL·E/ComfyUI) → requires available generator
□ user-supplied                     → optimize + integrate
□ video/ambient motion              → requires video tooling or fallback
```

**Do not imply access to raster generators unless runtime exposes the tool.**

**Delight gates:**
```
□ Enhancement clarifies character, meaning, or memory
□ Not hiding weak copy or missing content
□ Has named role: orientation / affordance / emphasis / atmosphere / reward
□ Removable without breaking comprehension
□ Lightweight — no a11y or performance cost
```

**Common Delight failures:**
```
❌ Accessory drift: image present but does not advance the story
❌ Cardification: generated image boxed like product card
❌ Figure/ground mismatch: asset creates its own surface
❌ Generic motif: zen rocks on a software portfolio
```
