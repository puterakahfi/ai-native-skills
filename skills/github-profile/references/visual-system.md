# GitHub-Native Visual System

Translate design principles into controls GitHub Profile README actually provides. Do not imitate a normal website with fragile HTML. Load `visual-directions.md` when direction selection or comparison is required.

## Medium Translation

| Design concern | GitHub-native control |
|---|---|
| Hierarchy | heading levels, opening order, concise lead, emphasis, section grouping |
| Typography | semantic headings, bold/italic/code roles, restrained image display type |
| Spacing | section breaks, blank lines, dividers, concise modules, table density |
| Composition | section order, alignment, image scale, project grouping, whitespace |
| Color | brand assets, badges, diagrams, theme-aware images; never color alone |
| Depth | grouping, contrast between text and visual modules, selective visuals |
| Rhythm | repeatable section pattern, project anatomy, heading cadence |
| Responsiveness | single-column priority, flexible images, minimal fixed-width tables |

GitHub already supplies navigation, avatar, bio, contribution graph, pinned repositories, and activity. The README should complement rather than duplicate them.

## Opening Viewport

The opening should usually contain:

```text
name or recognizable identity
specific role/positioning
one sentence explaining value or focus
one proof cue or selected-work bridge
one primary action, optionally one secondary action
```

Do not spend the entire opening on:

```text
a decorative banner with no semantic text
typing animations or visitor counters
large technology icon grids
multiple statistics cards
long autobiography
```

## Visual Budget

Default limits are heuristics, not universal gates:

```text
hero visual systems:       1
accent styles:             1 primary + 1 supporting
badge rows above projects: 0–1
third-party widgets:       0–2
animated assets:           0 by default
project modules:           3–6 selected items
social/contact actions:    1 primary + bounded secondary links
```

Increase density only when content and audience genuinely require it.

## Section Rhythm

Use a repeatable cadence:

```text
section heading
one-sentence framing when needed
proof or content module
short action or transition
breathing space
```

Avoid consecutive walls of badges → icons → stats → trophies → activity → counters. They have similar visual weight and produce no focal hierarchy.

## Project Module Patterns

### Narrative project

```markdown
### Project Name
One sentence describing the problem and audience.

**Role:** What was owned  
**Contribution:** The meaningful work or decision  
**Outcome:** Verified result or current state  
[Repository](...) · [Product](...) · [Case study](...)
```

### Compact selected-work list

```markdown
- **Project Name** — problem, contribution, and outcome. [Explore →](...)
```

### Visual showcase

Place the visual near the project name and provide adjacent semantic text. Keep image aspect ratios consistent across the selected set.

## Capability Presentation

Prefer capability groups over unbounded logo grids.

```markdown
**Architecture:** DDD, ports and adapters, event-driven systems  
**Product engineering:** Go, PHP, Next.js, Docker  
**AI-native systems:** agents, skills, context, evals
```

Use badges only when they improve scanning or recognition. Keep style, height, capitalization, and ordering consistent.

## Typography Roles

```text
H1       identity only; normally one
H2       primary profile sections
H3       projects, products, or bounded subsections
bold     labels and short emphasis
italic   occasional nuance, not body styling
code     technologies, commands, repository names, file paths
quote    a meaningful principle or testimonial with provenance
```

Do not use heading levels solely to change visual size. Keep semantic order intact.

## Alignment and Grids

Centered alignment works for a short hero, but long centered body text is difficult to scan. Return to left alignment for project narratives and detailed content.

HTML tables can simulate columns, but they compress poorly on narrow screens. Use them only for short modules with a readable single-column fallback. Never hide essential reading order inside a grid.

## Color and Theme

```text
semantic text remains readable in both themes
transparent images work on light and dark backgrounds
light/dark variants communicate equivalent information
brand color is an accent, not the sole hierarchy mechanism
mixed badge vendors do not create accidental rainbow noise
```

Without a reliable brand system, GitHub-native neutral styling is better than an arbitrary palette.

## Iconography and Images

Use a coherent icon family or native text labels. Mixed emoji, vendor logos, and custom illustrations create fragmentation.

Every meaningful image needs:

```text
useful alt text
stable source or repository-owned asset
appropriate dimensions
clear role in the hierarchy
fallback meaning in nearby text
```

## Narrow-Screen Test

```text
hero remains concise
images scale without horizontal scrolling
project order remains logical
HTML tables do not crush text
badge rows wrap without becoming dominant
links remain distinguishable
no essential text is baked only into a wide image
```

A desktop-only README is not finished.