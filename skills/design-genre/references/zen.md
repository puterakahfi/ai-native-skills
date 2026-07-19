# Genre: Zen / Minimalist

> Still, deliberate, unhurried — every element earns its place, and empty space performs real structural work.

## Signal Words

```text
zen, minimalist, ma, stillness, restraint, breathe, quiet, monk,
sparse, wabi-sabi, negative space, personal portfolio (senior/expert level),
space-led, calm, low interruption
```

## Voice & Copy

```text
Voice:     Still, deliberate, unhurried
Copy tone: Short sentences, no filler. Specificity over warmth.
           "I build systems meant to last." NOT "passionate engineer".
           No superlatives. No buzzwords.
```

## Typography

```text
Pair:      Light-weight display serif or restrained display sans + light sans
           Recommended starting point: Fraunces 300 + Inter 300

HIERARCHY RULE: restraint = no decoration, NOT no size
  H1: weight 300–500 + LARGE size — dominant focal object
  H2: lighter or smaller — clearly subordinate
  body: weight 300–400 + quiet readable measure
  ❌ light weight + small size everywhere → hierarchy collapses
  ✅ one large calm focal statement → zen dominance without loudness

Leading: generous; body line-height usually 1.65–1.8
Hero bio: max 44–52ch
Repeated ALL-CAPS labels: avoid; sentence case or quiet tracked labels are preferred
```

## Color

```text
Dark mode:
  bg: warm dark, not cold absolute black
  ink: muted / subtle / ink / bright — limited steps
  accent: one purpose-only sage/stone role

Light mode:
  pure white or a deliberately approved paper tone
  work rows remain transparent; no card is needed

Border color, when an allowed exception exists:
  barely visible, never a recurring page motif

FORBIDDEN:
  startup-blue takeover, amber/orange/yellow drift, neon, gradient mesh,
  multiple decorative accents, contrast used to compensate for weak spacing
```

## Layout — Wabi-Sabi Principles Applied

```text
Fukinsei (不均斉): asymmetry — balance without mirrored grids
Kanso (簡素):     remove before adding
Seijaku (静寂):   silence — space is the divider, not lines
Ma (間):          intentional intervals with a visual anchor
Shibui (渋い):    quiet depth; no spectacle
```

### Structural line contract

This is a hard genre constraint.

```text
SECTION DIVIDERS
  allowed: 0
  section border-top / border-bottom / border-y → FAIL

REPEATED ROW SEPARATORS
  default: 0
  do not remove cards and replace every card boundary with a hairline

DENSE LIST EXCEPTION
  one list system may use ONE leading or trailing hairline for orientation
  do not place a border between every item
  prefer spacing, indentation, numbering, alignment, and typographic weight

VISIBLE LINE BUDGET
  target: 0 structural lines in most viewports
  maximum: 1 visible structural hairline in a viewport, excluding controls,
           form fields, focus rings, and necessary data-table grids
```

Hairlines are not automatically zen. Repeated faint lines still fragment the page and increase visual interruption.

```text
❌ hero border-bottom
❌ border-y around every section
❌ border-top on every project, principle, capability, or contact row
❌ card removal followed by divider proliferation
✅ larger gap between sections
✅ asymmetric indentation
✅ numbered rows separated by rhythm only
✅ changes in measure, alignment, and typographic emphasis
```

### Void rule

```text
Every large empty interval needs a visual anchor before or after it.
Hero should resolve into a CTA, contact cue, work preview, or quiet illustration.
Empty space without relationship reads abandoned; intentional space reads composed.

Section rhythm starting point:
  clamp(64px, 8vh, 96px)
Adapt from content length and viewport; do not fill space with containers.
```

### Containment grammar

```text
PRIMARY CONTAINERS
  whitespace
  alignment
  text measure
  asymmetric grid position
  grouping by proximity

SECONDARY CONTAINERS
  a quiet image field
  one rare anchor surface when interaction or comparison requires it

NOT DEFAULT CONTAINERS
  cards
  borders
  pills
  section backgrounds
  boxed CTA panels
```

## Motion

```text
Stance: STILLNESS
Only permitted by default: color transition and restrained fade/translateY 6–8px
No hover lift, bounce, glow, scale choreography, or motion on every row
prefers-reduced-motion: hard gate
```

## Macrostructures

```text
Marquee Hero (zen variant), Specimen, Studio, Atelier, Lumen
```

A compatible macrostructure is still invalid when implemented with repeated section borders, equal cards, or dense metadata chrome.

## Nav & Footer

```text
Nav: minimal, low contrast, transparent until scrolling only when needed
Footer: minimal and open; whitespace may separate it from contact
```

## Zen Review Questions

```text
1. What was removed rather than restyled?
2. Where does empty space perform grouping or separation?
3. What is the single focal object in this viewport?
4. How many structural lines are visible?
5. Could any remaining border become spacing instead?
6. Did card removal merely become hairline-divider repetition?
7. With color removed, does the composition remain calm and legible?
```

## Hard Failures

```text
❌ structural section borders
❌ repeated border-separated rows across multiple sections
❌ more than one visible structural line in a typical viewport without domain need
❌ card-to-hairline substitution
❌ background color swap between ordinary sections
❌ hover lift or shadow glow
❌ repeated badges/pills for plain metadata
❌ bold body copy and multiple competing focal objects
❌ more than one decorative accent
❌ empty space filled because it feels "unfinished"
```

## Allowed Exceptions

```text
✅ form controls and focus rings
✅ required data-table or diagram lines
✅ one rare list boundary hairline
✅ one strong focal object per viewport
✅ near-invisible texture when it does not create another surface
```

Every exception needs a functional reason in the run state. "It looked too empty" is not a functional reason.