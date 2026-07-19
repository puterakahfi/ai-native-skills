# GitHub-Native Visual System

Translate design principles into controls GitHub Profile README actually provides. Do not imitate a normal website with fragile HTML. Load `visual-directions.md` when direction selection or comparison is required.

## Foundation Before Direction

A GitHub Profile README must first satisfy the relational foundation:

```text
page anchor → section parent → item → metadata → action
related content groups more tightly than unrelated content
repeated roles share stable alignment and treatment
spacing communicates hierarchy instead of repeating one gap
the visual mass fits the available canvas
the reading path remains obvious at desktop and narrow width
```

Genre and brand decide how these relationships are expressed. They may not remove them.

## Brand Grammar Lock

Before choosing a module treatment, inspect supplied or established brand references. Record stable grammar rather than copying surface decoration.

```text
mood
content density
spacing rhythm
separator behavior
alignment behavior
typography behavior
asset language
prohibited treatments
```

Examples:

```text
zen, generous spacing, no lines    → whitespace and cadence create grouping
technical, compact, structured     → bounded labels and denser proof anatomy may fit
editorial, expressive type         → thesis and scale contrast carry identity
visual portfolio                   → owned imagery carries proof; text remains semantic
```

A GitHub-native pattern is not automatically brand-compatible. Blockquotes, tables, code boxes, badge rows, and horizontal rules may be valid platform controls while still being wrong for a line-free or calm identity.

## Medium Translation

| Design concern | GitHub-native control |
|---|---|
| Hierarchy | opening order, semantic heading levels, weight, measure, placement, spacing |
| Typography | H3/H4 roles when H1/H2 rules conflict with a line-free brand; restrained bold/italic roles |
| Spacing | blank lines, bounded `<br>` spacing, heading margins, concise modules |
| Composition | mixed alignment, project grouping, content measure, visual-mass distribution |
| Color | links and owned assets; never color alone |
| Depth | optional containment; flat composition is valid |
| Rhythm | parent/item/metadata cadence and sentence-length variation |
| Responsiveness | single-column priority and semantic source order |

GitHub already supplies navigation, avatar, bio, contribution graph, pinned repositories, and activity. The README should complement rather than duplicate them.

## Opening Viewport

The opening should usually contain:

```text
page anchor: name or recognizable identity
supporting role: specific positioning
statement: one value proposition or thesis
proof bridge: selected-work destination
bounded secondary action
```

Use at least two cues for important role differences when scale alone is weak:

```text
scale + weight
scale + placement
weight + measure
placement + isolation
spacing + repetition
```

Do not spend the entire opening on a decorative banner, typing animation, icon grid, statistic cards, long autobiography, or unanchored empty space.

A centered opening may be appropriate for identity and still return to left alignment for detailed reading. Centering the entire document is a safe-default failure.

## Differentiation Gate

Clean composition is the baseline. A profile becomes recognizable through one deliberate device, not through more decoration.

Choose one primary device:

```text
thesis-led opening       a concise belief or system statement
proof-module treatment   repeated project anatomy
system diagram           a small semantic flow or architecture map
owned visual asset       brand mark or theme-aware project visual
editorial rhythm         deliberate contrast between identity, proof, detail, and action
```

The device passes only when it supports actual positioning and the established brand grammar. A conflicting device fails even when it looks distinctive in isolation.

## Spatial Rhythm

Spacing is structure. Start with three relational levels:

```text
element gap       within one statement or metadata group
item gap          between comparable projects or principles
section gap       between different content roles
```

Verify:

```text
within-group spacing is tighter than between-group spacing
parent-to-item transition is clear
section gaps are visibly stronger than sibling gaps
large intervals have a named grouping, pacing, framing, or narrative role
sparse content does not receive exaggerated spacing merely to look premium
```

A practical starting relation is:

```text
element < item < section
```

Do not translate this into a fixed pixel ratio without rendering. GitHub heading margins and line wrapping affect the final rhythm.

### Zen / Ma correction

```text
Ma = purposeful pause
Ma ≠ maximum empty area
```

For zen profiles:

```text
use a small number of meaningful pauses
keep related project anatomy visually attached
avoid repeating `<br><br><br>` at every transition
let precise copy and hierarchy earn the space
reduce space when visual mass becomes stranded
```

## Section Rhythm

Use a repeatable cadence while varying role weight:

```text
section parent
optional one-sentence frame
item title
purpose
metadata
contribution or outcome
item gap
```

Project proof, engineering thesis, capability inventory, current focus, and contact action should not all look identical.

## Project Module Patterns

### Line-free narrative project

Best for zen, editorial, or no-card brands:

```markdown
#### [Project Name →](...)

Specific purpose or audience value.

*Role · evidence type · current state*

Meaningful ownership, contribution, or verified outcome.
```

Keep the title, purpose, metadata, and contribution closer to one another than to the next project.

### Narrative project with labels

```markdown
#### Project Name
One sentence describing the problem and audience.

**Role:** What was owned  
**Contribution:** The meaningful work or decision  
**Outcome:** Verified result or current state
```

### Compact selected-work list

```markdown
- **Project Name** — problem, contribution, and outcome. [Explore →](...)
```

### Contained proof block

Blockquotes or tables are optional, not preferred defaults. Use only when the brand permits containment and the content genuinely needs stronger common-region grouping.

### Visual showcase

Place the visual near the project name and provide adjacent semantic text. Keep image aspect ratios consistent across the selected set.

## Capability Presentation

Prefer capability groups over unbounded logo grids.

```markdown
- **Architecture** — DDD, ports-and-adapters, event-driven systems
- **Product engineering** — Go, PHP, Next.js, Docker
- **AI-native systems** — agents, skills, context, evaluation
```

Bullets may improve scanning without violating a line-free brand. Restraint does not require removing every structural cue.

## Typography Roles

```text
page anchor     strongest identity role
positioning     supporting role below the anchor
thesis          authored statement; locally dominant
section parent  H3 or equivalent GitHub-native role
item title      H4 or strong linked title
body            explanatory prose
metadata        italic or short supporting detail
```

Do not make critical labels tiny merely to appear refined. Small muted text carrying section identity is a legibility and hierarchy failure.

## Alignment and Balance

Use stable anchors:

```text
center anchor for a bounded identity opening when brand-appropriate
left content edge for project narratives and detailed reading
consistent project-title and metadata starts
```

Evaluate visual mass across the whole README. A narrow cluster floating inside a very tall empty canvas is not automatically balanced or zen.

HTML tables can simulate columns, but they compress poorly on narrow screens and introduce containment. Avoid them for line-free brands.

## Color and Theme

```text
semantic text remains readable in both themes
links remain distinguishable
transparent images work on light and dark backgrounds
light/dark variants communicate equivalent information
brand color is an accent, not the sole hierarchy mechanism
```

Without a reliable brand system, GitHub-native neutral styling is better than an arbitrary palette.

## Narrow-Screen Test

```text
opening remains concise
forced line breaks do not create awkward fragments
project anatomy stays grouped
section gaps do not become excessive scrolling
metadata remains readable
links remain distinguishable
reading order stays semantic
no essential text is baked only into an image
```

A desktop-only README is not finished.
