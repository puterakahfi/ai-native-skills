---
name: design-foundation
description: Universal design foundation — the non-negotiable composition contract every design genre, brand, surface, and workflow must satisfy. Covers 13 core graphic design principles, hierarchy, grouping, figure-ground, semantic layering, content resilience, semantic status encoding, alignment, spacing rhythm, balance, flow, legibility, consistency, accessibility, and responsive continuity.
license: MIT
metadata:
  ai-native-skills.version: 1.5.1
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/design/design-foundation.contract.yaml
  ai-native-skills.contract-version: "^1.0.0"
  ai-native-skills.related_skills: '["design-visual","design-layout","design-system","design-genre","design-brand","design-review","redesign-workflow"]'
---

# Design Foundation Skill

## Reviewed core contract interface

Source: `ai-native-core/contracts/skills/design/design-foundation.contract.yaml` · compatible line: `^1.0.0`

```yaml
required_inputs: []
allowed_outputs: []
quality_gates:
- F1_hierarchy_h1_body_ratio_min_2_5x
- F2_contrast_primary_min_4_5_1
- F3_touch_target_min_44px
- F4_no_hardcoded_values_in_components
- F5_no_dead_space_no_min_height_100vh
- F6_no_decoration_without_function
- F7_aria_keyboard_accessible
```

F5 explicitly rejects dead space and min-height:100vh as a composition shortcut. Empty space must communicate grouping, pacing, emphasis, or balance rather than delaying the focal point.

Keep this interface synchronized with the pinned core contract. Exact declarations make ownership reviewable; they do not replace rendered, runtime, accessibility, or product evidence.

> **THIS IS THE BASE. Every genre and brand expresses it differently; none may remove it.**

```text
LAYER MODEL:
  design-foundation    ← universal composition + usability contract
      ↑ expressed by
  design-genre         ← density, voice, containment, color, motion
      ↑ constrained by
  design-brand         ← identity, tokens, assets, product rules
      ↑ consumed by
  design workflows     ← audit, review, refinement, redesign, production
```

Foundation defines **relationships and quality**, not a visual style.

---

## Universal Foundation Axes

Every design engagement must resolve these axes before genre-specific styling is accepted.

```text
F1  HIERARCHY
    Importance levels, semantic roles, maturity, severity, and state are distinguishable at a glance.

F2  GROUPING
    Proximity, similarity, common region, figure-ground, containment, presence,
    and sequence communicate what belongs together.

F3  ALIGNMENT
    Elements share meaningful structural or optical anchors; exceptions are intentional.

F4  SPACE + RHYTHM
    Spacing and density express relationship, content state, sequence, and emphasis
    instead of repeating one gap or composition.

F5  BALANCE
    Visual mass, contrast, density, direction, imagery, depth, overlap, semantic color,
    and empty space are distributed intentionally.

F6  FLOW
    The eye and the user can follow the intended reading, task, narrative, and state-change order.

F7  LEGIBILITY
    Type, symbols, contrast, measure, scale, content length, value shape, and information density
    suit the real viewing context.

F8  SYSTEM CONSISTENCY
    Repeated roles use coherent tokens, treatments, states, components, fallbacks,
    semantic meanings, and content-adaptation behavior.

F9  ACCESSIBILITY + AFFORDANCE
    Information and interaction remain perceivable, operable, understandable,
    non-color-dependent, and keyboard/touch safe.

F10 RESPONSIVE CONTINUITY
    Hierarchy, grouping, reading order, layer meaning, content meaning, status meaning,
    and interaction meaning survive format, viewport, theme, and supported-content changes.
```

---

## Core Graphic Design Principle Lenses

Use these 13 principles as cross-cutting composition lenses. They do not create 13 additional release gates; they deepen reasoning and map back to `F1–F10`.

```text
1.  ALIGNMENT     shared structural and optical anchors create order
2.  CONTRAST      meaningful difference creates distinction and legibility
3.  BALANCE       visual weight is distributed intentionally
4.  HIERARCHY     importance and semantic order are recognizable
5.  COLOR         hue, value, and saturation communicate identity and meaning
6.  WHITE SPACE   negative space groups, separates, pauses, and emphasizes
7.  PROPORTION    relative scale supports hierarchy, balance, and usability
8.  REPETITION    coherent reuse builds recognition and consistency
9.  RHYTHM        recurrence and spacing create cadence
10. MOVEMENT      visual and actual motion guide attention and sequence
11. EMPHASIS      a deliberate focal point communicates priority
12. PROXIMITY     spatial closeness communicates relationship
13. UNITY         all elements work as one coherent composition
```

Principle relationships matter more than isolated compliance:

```text
contrast without emphasis discipline   → everything competes
repetition without rhythm              → mechanical monotony
rhythm without hierarchy               → movement without meaning
alignment without optical correction   → technically aligned, visually wrong
white space without grouping purpose   → decorative emptiness
variation without unity                → expressive but fragmented
```

Load `references/core-graphic-design-principles.md` for definitions, applications, review questions, failure signals, combined-use guidance, and principle-to-gate mapping.

---

## Universal Composition Contract

### 1. Hierarchy is relational

Hierarchy is not proven by one large H1. Review the full relationship:

```text
page → section → group → item → metadata/action
parent → child group → sibling items → supporting details
state category → state value → consequence/action
```

Rules:

```text
- primary, supporting, and tertiary roles must be recognizable without reading every word
- parent and child levels must not collapse into equal visual weight
- nested hierarchy should use at least two cues when one cue is ambiguous:
  scale, weight, measure, contrast, placement, spacing, repetition, symbol, or semantic color
- sibling items should feel related to one another while remaining subordinate to their parent
- status, severity, maturity, progress, and evidence must not collapse into one visual role
- numeric type ratios are diagnostic evidence, not universal laws
```

### 2. Grouping follows relationship

```text
- related elements cluster more strongly than unrelated elements
- within-group spacing is usually tighter than between-group spacing
- parent → child-group separation is stronger than child → child separation
- enclosure is optional; cards and borders are not required for grouping
- similarity must not erase meaningful differences in status, priority, maturity, or role
- foreground, background, and containment relationships must remain understandable
- optional content may appear or disappear without detaching the remaining relationships
```

A practical starting point is a between-group interval around `1.25×–2×` the within-group interval, then verify visually in context.

### 2b. Figure-ground and semantic layers preserve relationships

```text
- the intended foreground remains distinguishable from its background
- surfaces and elevation communicate containment, priority, transience, focus, or state
- shadows, blur, glass, borders, and gradients do not replace hierarchy or grouping
- sticky, fixed, floating, or overlapping layers do not hide required content or actions
- interactive layers preserve object/task context and provide a clear continuation or recovery path
- layer meaning survives crop, theme, viewport, orientation, localization, and text scaling changes
```

Use semantic layer roles before arbitrary z-index values:

```text
canvas → content → containment → floating → modal → system/critical
```

Not every artifact needs every layer. A flat design can pass; a highly layered design can pass. Review the relationship, not the quantity of depth effects.

Load `references/figure-ground-layering.md` when the artifact includes surfaces, imagery behind text, overlap, sticky/fixed UI, popovers, drawers, dialogs, layered compositions, or depth effects.

### 2c. Content resilience preserves relationships under variation

```text
- supported content bounds are declared instead of assumed from ideal placeholders
- empty, minimum, normal, maximum, and applicable variant states are considered
- optional text, media, metadata, and items may change without collapsing hierarchy or grouping
- wrapping, clamping, truncation, scrolling, pagination, summarization, disclosure,
  prioritization, or component substitution is deliberate and preserves critical meaning
- repeated roles use coherent content-adaptation and fallback policies
- realistic long content is combined with constrained viewport, localization,
  text scaling, and missing-media conditions where applicable
```

A design does not need to support unlimited content. It must honestly define the supported range and provide a meaningful strategy at its boundaries.

Load `references/content-resilience.md` for variable-content products, reusable templates, catalogs, tables, forms, collections, generated/user-authored content, localization, text scaling, or optional media. Load `references/content-resilience-fixtures.md` for cross-surface regression and bias testing.

### 2d. Semantic status encoding preserves meaning

```text
- state meaning is declared before visual styling
- success/pass uses a stable success family and affirmative symbol
- warning/risk/conditional uses an attention family without implying failure
- fail/error uses a failure family and explicit failure label
- danger/destructive is stronger than ordinary error and reserved for serious consequence
- information remains distinct from success, warning, selection, and decoration
- pending/in-progress remains distinct from warning
- not verified remains distinct from fail because missing evidence is not negative evidence
- not applicable remains visible and neutral rather than silently omitted
- color reinforces meaning but never acts as the only essential carrier
- label, icon/shape, hierarchy, and color remain aligned across repeated surfaces
```

Default conventional families are semantic starting points, not fixed brand tokens:

```text
success / pass        → green family + affirmative symbol + explicit label
warning / conditional → amber family + alert symbol + explicit label
fail / error          → red family + failure symbol + explicit label
danger / destructive  → stronger red + consequence wording + danger symbol
information           → blue/cyan family + information symbol + explicit label
pending / progress    → cool blue/slate + progress/clock/dashed symbol + label
not verified          → cool evidence-gap family + unknown/dashed symbol + label
not applicable        → neutral family + minus symbol + label
```

Exact hues, icon library, component anatomy, motion, radius, and token names belong to the design system, brand, or artifact implementation. The semantic relationship does not.

Load `references/semantic-status-encoding.md` whenever an artifact communicates validation, health, risk, evidence, progress, maturity, availability, review verdict, or destructive consequence. Load `references/semantic-status-fixtures.md` for cross-surface regression.

### 3. Alignment uses shared anchors

```text
- repeated roles reuse stable start, center, baseline, or end anchors
- alignment may be geometric or optical
- near-alignment without intent is a defect
- asymmetry is valid when the balancing logic is visible
- local nudges must not replace a shared grid or alignment system
- icons, labels, values, and wrapped status text preserve one reusable optical relationship
```

Box alignment is not always optical alignment. Mixed font sizes, icons, and irregular shapes may need one reusable optical correction.

### 4. Space communicates structure

```text
- space must answer: what relationship does this interval communicate?
- one repeated gap everywhere usually flattens hierarchy
- large empty intervals need an anchor and a structural purpose
- empty, sparse, normal, and dense content states must not reuse one composition blindly
- content quantity does not automatically require less or more space; evaluate composition and context
- status label, icon, value, explanation, and action remain visibly associated
- whitespace may group, separate, pause, emphasize, or resolve
```

### 5. Balance is visual weight, not symmetry

Evaluate together:

```text
scale + contrast + density + position + direction + color + imagery + depth + overlap + empty space
```

A composition may be symmetrical, asymmetrical, centered, dense, open, flat, or layered. It passes when weight distribution is intentional and supports the message or task. Semantic color must not become accidental decoration or overpower the primary narrative.

### 6. Flow is an ordered experience

```text
- the first focal point is clear
- the next intended region is discoverable
- reading order and DOM/task order do not conflict
- transitions between sections, states, or layers preserve context
- content adaptation does not hide or reorder the next valid action without reason
- state change communicates what happened, why it matters, and what can happen next
- CTAs and actions appear after sufficient meaning, not before it
- decorative motion must not hijack the intended flow
```

### 7. Responsive continuity preserves meaning

```text
- hierarchy survives scale reduction
- grouped content stays grouped after stacking or optional-content changes
- desktop rails collapse into predictable mobile order
- labels, titles, content, status, and actions do not zig-zag accidentally
- touch targets, overflow, localization, content variation, and text scaling remain safe
- semantic state does not degrade into color-only dots on constrained layouts
- floating, sticky, modal, and overlapping relationships remain safe and understandable
- realistic content stress is tested together with constrained space, not separately only
```

---

## Foundation Gates

| Gate | Universal question | Failure signal |
|---|---|---|
| F1 Hierarchy | Are importance levels, roles, maturity, severity, and state unambiguous? | Parent and child compete; status, labels, metadata, and content collapse into one level. |
| F2 Grouping | Do proximity, common region, figure-ground, containment, and presence show what belongs together? | Related items detach, optional content leaves broken relationships, or foreground/background ownership becomes unclear. |
| F3 Alignment | Do repeated elements use meaningful structural or optical anchors? | Accidental drift, almost-aligned edges, or per-item nudging. |
| F4 Spatial Rhythm | Does spacing and density encode grouping, content state, sequence, and emphasis? | One gap/composition everywhere; empty or dense states feel stranded, collapsed, or flattened. |
| F5 Balance | Are visual mass, semantic color, depth, overlap, and empty space distributed intentionally? | One region, layer, or status treatment is overloaded, obscured, or accidentally dominant. |
| F6 Flow | Is the intended reading/task/state sequence clear? | Competing focal points, unclear next step, broken order, or lost context after a layer/state/content change. |
| F7 Legibility | Are text, values, symbols, and state distinctions readable in the real context? | Weak contrast, tiny metadata, ambiguous icons, clipping, unstable wrapping, or background interference. |
| F8 Consistency | Are repeated roles, semantic meanings, and adaptation policies governed coherently? | Same state changes color/icon/label meaning; unrelated states reuse one treatment. |
| F9 Accessibility | Are interaction and information accessible without depending on color alone? | Missing labels, focus, contrast, non-color cues, touch size, semantic order, or layer operability. |
| F10 Responsive Continuity | Do relationships, status meaning, and behavior survive viewport, theme, format, and supported-content changes? | Grouping breaks, status becomes color-only, order changes, overflow is unsafe, content disappears, or layer occlusion occurs. |

**A verified foundation failure blocks release approval. A source-only suspicion is `NOT_VERIFIED` until rendered or runtime evidence exists.**

---

## Ownership and Handoff

```text
design-foundation
  owns reusable universal relationship knowledge, the 13 principle lenses,
  semantic-state meaning, multi-channel encoding, and F1–F10 definitions

design-review
  evaluates F1–F10 with evidence and reports coverage/verdict through canonical IDs

design-genre
  adds stricter expression constraints without redefining semantic meaning

design-system / brand
  implements exact semantic tokens, icon set, component anatomy, variants,
  content policies, and product-specific rules

design workflows
  load foundation before direction/production and classify the correct fix layer

surface/domain reviewers
  own runtime announcement, validation behavior, interaction safety,
  platform thresholds, and domain-specific consequence rules
```

A local visual defect should not automatically patch this skill. Promote it here only when the missing or misleading rule is reusable across genres and surfaces.

---

## What Foundation Does Not Dictate

```text
Foundation owns relationship, meaning, and quality.
Genre/brand/product own expression and declared limits.

FOUNDATION                         GENRE / BRAND / PRODUCT
clear grouping                     cards, borders, whitespace, or color fields
clear figure-ground                flat, outlined, elevated, glass, textured, cinematic
content resilience                 exact item limits, copy limits, pagination, or fallback UI
semantic state meaning             exact HEX, icon library, radius, badge/toast/table anatomy
stable hierarchy                   exact typeface, weights, and scale magnitude
intentional alignment              symmetric, asymmetric, centered, editorial grid
readable contrast                  exact palette and accent behavior
coherent rhythm                    compact, spacious, dense, or dramatic cadence
clear flow                         stillness, motion, playfulness, cinematic pacing
usable interaction                 component styling and brand voice
```

Genre-specific rules may be stricter, but may not erase foundation requirements.

---

## Reference Files

| Topic | File | When to load |
|---|---|---|
| Core graphic design principle lenses and F1–F10 mapping | `references/core-graphic-design-principles.md` | Foundation learning, visual direction, production, design review, and principle-specific diagnosis |
| Principles and composition rationale | `references/principles.md` | Direction, planning, production |
| Foundation gates and evidence | `references/gates.md` | Review, refinement, release verification |
| Figure-ground, containment, layering, overlap, and evidence | `references/figure-ground-layering.md` | Surfaces, imagery behind text, sticky/fixed UI, overlays, modal/floating layers, layered static composition |
| Cross-genre figure-ground regression fixtures | `references/figure-ground-fixtures.md` | Skill evaluation and bias checks across minimal, dense, expressive, product, static, and presentation surfaces |
| Content bounds, stress states, adaptation strategies, and evidence | `references/content-resilience.md` | Variable-content products, reusable templates, catalogs, tables, forms, localization, text scaling, optional media, generated/user content |
| Cross-surface content resilience regression fixtures | `references/content-resilience-fixtures.md` | Skill evaluation and PASS/FAIL discrimination across empty/minimum/normal/maximum/variant content states |
| Semantic state taxonomy, channel contract, color/icon/label roles, and ownership | `references/semantic-status-encoding.md` | Validation, health, risk, evidence, progress, maturity, availability, verdict, or destructive consequence |
| Cross-surface semantic status regression fixtures | `references/semantic-status-fixtures.md` | Review scorecards, forms, alerts, dashboards, workflows, reports, themes, and non-color checks |

```text
skill_view(name='design-foundation', file_path='references/core-graphic-design-principles.md')
skill_view(name='design-foundation', file_path='references/principles.md')
skill_view(name='design-foundation', file_path='references/gates.md')
skill_view(name='design-foundation', file_path='references/figure-ground-layering.md')
skill_view(name='design-foundation', file_path='references/figure-ground-fixtures.md')
skill_view(name='design-foundation', file_path='references/content-resilience.md')
skill_view(name='design-foundation', file_path='references/content-resilience-fixtures.md')
skill_view(name='design-foundation', file_path='references/semantic-status-encoding.md')
skill_view(name='design-foundation', file_path='references/semantic-status-fixtures.md')
```

---

> **REMINDER:** Foundation is not a theme. It is the universal quality contract underneath every theme.
