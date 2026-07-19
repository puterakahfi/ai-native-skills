# Genre: Zen / Minimalist

> Still, deliberate, unhurried — every element earns its place, and empty space performs real structural work.

## Foundation Inheritance

Zen is an expression layer, not the owner of universal composition quality.

```text
Inherited from design-foundation:
  hierarchy
  grouping
  structural + optical alignment
  spatial rhythm
  balance
  reading/task flow
  legibility
  system consistency
  accessibility
  responsive continuity

Zen adds stricter expression constraints:
  low interruption
  space-led containment
  near-zero structural lines
  rare surfaces
  restrained color and motion
  one calm focal object
```

A hierarchy, grouping, balance, alignment, or flow defect must be fixed in the foundation relationship first. Do not label the defect “zen asymmetry” or repair it with more empty space.

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

FOUNDATION HIERARCHY, ZEN EXPRESSION:
  one large calm focal statement
  child and supporting roles remain unmistakably subordinate
  fewer visible type steps, but no role collapse
  restraint = no decoration, NOT no hierarchy

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
✅ numbered rows separated by rhythm only
✅ changes in measure, alignment, and typographic emphasis
```

### Alignment rail contract

Foundation requires meaningful alignment. Zen makes the hidden order quieter and stricter.

```text
PAGE SHELL
  use one persistent content width across nav, hero, sections, contact, and footer
  do not alternate container widths without a declared focal reason

PRIMARY RAILS
  define 2–4 reusable vertical start positions before composing sections
  section labels, major headings, titles, body copy, and actions should reuse them
  adjacent sections must feel related even when their spans differ

ASYMMETRY
  create asymmetry by span, whitespace, measure, or one deliberate focal offset
  do not shift individual rows with arbitrary margin-left, padding-left, or translate-x
  repeated per-item nudging is drift, not Fukinsei

OFFSET BUDGET
  default arbitrary offsets: 0
  allowed exception: one documented focal object or illustration offset per viewport
  never alternate row offsets merely to make a list feel organic

RESPONSIVE COLLAPSE
  desktop rails must collapse predictably to one or two mobile rails
  mobile order must remain label → title → content/action without visual zig-zag
```

Common failure pattern:

```text
section header begins on rail A
project title begins on rail B
principle title begins on a manually shifted rail C
contact links use another percentage indentation
result: every local composition looks plausible, but the full page feels crooked
verdict: alignment continuity failure
```

```text
❌ repeated translate-x on alternating rows
❌ md:ml-[N%] or arbitrary padding used as section-level layout
❌ different heading start positions without hierarchy reason
❌ nav/footer shell wider or narrower than the page body by accident
✅ one shared grid with different column spans
✅ consistent label rail and main-content rail
✅ one intentional offset used sparingly as a focal exception
```

### Spacing expression

Foundation owns relational spacing. Zen expresses it with quiet, visible intervals rather than boundaries.

```text
parent → child group must remain distinct
sibling items form a tighter repeated rhythm
within-item details cluster closely
between-section intervals provide a calm pause
```

Do not increase every gap equally. Equal large gaps flatten grouping just as equal small gaps do.

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
  shared alignment rails
  text measure
  grouping by proximity
  restrained asymmetrical spans

SECONDARY CONTAINERS
  a quiet image field
  one rare anchor surface when interaction or comparison requires it

NOT DEFAULT CONTAINERS
  cards
  borders
  pills
  section backgrounds
  boxed CTA panels
  arbitrary per-item offsets
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

A compatible macrostructure is still invalid when implemented with repeated section borders, equal cards, dense metadata chrome, broken hierarchy, or broken alignment continuity.

## Nav & Footer

```text
Nav: minimal, low contrast, transparent until scrolling only when needed
Footer: minimal and open; whitespace may separate it from contact
Nav, content, and footer should share the same page shell and outer rails
```

## Zen Review Questions

```text
1. Did the design-foundation gates pass before zen conformance was evaluated?
2. What was removed rather than restyled?
3. Where does empty space perform grouping or separation?
4. What is the single focal object in this viewport?
5. How many structural lines are visible?
6. Could any remaining border become spacing instead?
7. Did card removal merely become hairline-divider repetition?
8. What are the persistent alignment rails across the page?
9. Are any rows manually nudged off those rails without a functional reason?
10. Does mobile collapse preserve a calm reading order?
11. With color removed, does the composition remain calm and legible?
```

## Hard Failures

```text
❌ treating a foundation defect as a zen style choice
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
❌ multiple container widths with no declared reason
❌ repeated arbitrary margin, padding, or translate offsets used to fake asymmetry
❌ section labels, headings, and content drifting across unrelated start positions
❌ parent, child group, and siblings using equal visual weight
❌ mobile content zig-zag caused by desktop offset rules
```

## Allowed Exceptions

```text
✅ form controls and focus rings
✅ required data-table or diagram lines
✅ one rare list boundary hairline
✅ one strong focal object per viewport
✅ one documented focal offset for an illustration or singular composition
✅ near-invisible texture when it does not create another surface
```

Every exception needs a functional reason in the run state. "It looked too empty" or "it felt more dynamic" is not a functional reason.