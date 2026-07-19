---
name: design-foundation
description: Universal design foundation — the non-negotiable composition contract every design genre, brand, surface, and workflow must satisfy. Covers hierarchy, grouping, alignment, spacing rhythm, balance, flow, legibility, consistency, accessibility, and responsive continuity.
license: MIT
metadata:
  ai-native-skills.version: 1.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/design/design-foundation.contract.yaml
  ai-native-skills.contract-version: "^1.0.0"
  ai-native-skills.related_skills: '["design-visual","design-layout","design-system","design-genre","design-brand","design-review","redesign-workflow"]'
---

# Design Foundation Skill

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
    Importance levels and semantic roles are distinguishable at a glance.

F2  GROUPING
    Proximity, similarity, enclosure, and sequence communicate what belongs together.

F3  ALIGNMENT
    Elements share meaningful structural or optical anchors; exceptions are intentional.

F4  SPACE + RHYTHM
    Spacing expresses relationship, sequence, and emphasis instead of repeating one gap.

F5  BALANCE
    Visual mass, contrast, density, direction, imagery, and empty space are distributed intentionally.

F6  FLOW
    The eye and the user can follow the intended reading, task, or narrative order.

F7  LEGIBILITY
    Type, contrast, measure, scale, and information density suit the real viewing context.

F8  SYSTEM CONSISTENCY
    Repeated roles use coherent tokens, treatments, states, and component behavior.

F9  ACCESSIBILITY + AFFORDANCE
    Interaction remains perceivable, operable, understandable, and keyboard/touch safe.

F10 RESPONSIVE CONTINUITY
    Hierarchy, grouping, reading order, and interaction meaning survive format or viewport changes.
```

---

## Universal Composition Contract

### 1. Hierarchy is relational

Hierarchy is not proven by one large H1. Review the full relationship:

```text
page → section → group → item → metadata/action
parent → child group → sibling items → supporting details
```

Rules:

```text
- primary, supporting, and tertiary roles must be recognizable without reading every word
- parent and child levels must not collapse into equal visual weight
- nested hierarchy should use at least two cues when one cue is ambiguous:
  scale, weight, measure, contrast, placement, spacing, or repetition
- sibling items should feel related to one another while remaining subordinate to their parent
- numeric type ratios are diagnostic evidence, not universal laws
```

### 2. Grouping follows relationship

```text
- related elements cluster more strongly than unrelated elements
- within-group spacing is usually tighter than between-group spacing
- parent → child-group separation is stronger than child → child separation
- enclosure is optional; cards and borders are not required for grouping
- similarity must not erase meaningful differences in status, priority, or role
```

A practical starting point is a between-group interval around `1.25×–2×` the within-group interval, then verify visually in context.

### 3. Alignment uses shared anchors

```text
- repeated roles reuse stable start, center, baseline, or end anchors
- alignment may be geometric or optical
- near-alignment without intent is a defect
- asymmetry is valid when the balancing logic is visible
- local nudges must not replace a shared grid or alignment system
```

Box alignment is not always optical alignment. Mixed font sizes, icons, and irregular shapes may need one reusable optical correction.

### 4. Space communicates structure

```text
- space must answer: what relationship does this interval communicate?
- one repeated gap everywhere usually flattens hierarchy
- large empty intervals need an anchor and a structural purpose
- sparse content does not automatically require less or more space; evaluate composition and context
- whitespace may group, separate, pause, emphasize, or resolve
```

### 5. Balance is visual weight, not symmetry

Evaluate together:

```text
scale + contrast + density + position + direction + color + imagery + empty space
```

A composition may be symmetrical, asymmetrical, centered, dense, or open. It passes when the weight distribution feels intentional and supports the message or task.

### 6. Flow is an ordered experience

```text
- the first focal point is clear
- the next intended region is discoverable
- reading order and DOM/task order do not conflict
- transitions between sections or states preserve context
- CTAs and actions appear after sufficient meaning, not before it
- decorative motion must not hijack the intended flow
```

### 7. Responsive continuity preserves meaning

```text
- hierarchy survives scale reduction
- grouped content stays grouped after stacking
- desktop rails collapse into predictable mobile order
- labels, titles, content, and actions do not zig-zag accidentally
- touch targets, overflow, localization, and text scaling remain safe
```

---

## Foundation Gates

| Gate | Universal question | Failure signal |
|---|---|---|
| F1 Hierarchy | Are importance levels and semantic roles unambiguous? | Parent and child compete; headings, labels, and metadata collapse into one level. |
| F2 Grouping | Do proximity and visual relationships show what belongs together? | Related items feel detached or unrelated items read as one group. |
| F3 Alignment | Do repeated elements use meaningful structural or optical anchors? | Accidental drift, almost-aligned edges, or per-item nudging. |
| F4 Spatial Rhythm | Does spacing encode grouping, sequence, and emphasis? | One gap everywhere; parent-to-group and sibling gaps feel equal. |
| F5 Balance | Is visual weight distributed intentionally? | One region feels stranded, overloaded, or accidentally dominant. |
| F6 Flow | Is the intended reading/task sequence clear? | Competing focal points, unclear next step, broken order. |
| F7 Legibility | Is content readable in the real context? | Weak contrast, poor measure, tiny metadata, dense or orphaned text. |
| F8 Consistency | Are repeated roles governed coherently? | Same role changes treatment without reason; duplicate token vocabularies. |
| F9 Accessibility | Are interaction and information accessible? | Missing labels, focus, contrast, touch size, reduced motion, or semantic order. |
| F10 Responsive Continuity | Do relationships and behavior survive viewport/format change? | Grouping breaks, order changes incorrectly, overflow, mobile zig-zag. |

**A verified foundation failure blocks release approval. A source-only suspicion is `NOT_VERIFIED` until rendered or runtime evidence exists.**

---

## What Foundation Does Not Dictate

```text
Foundation owns relationship and quality.
Genre/brand own expression.

FOUNDATION                         GENRE / BRAND
clear grouping                     cards, borders, whitespace, or color fields
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
| Principles and composition rationale | `references/principles.md` | Direction, planning, production |
| Foundation gates and evidence | `references/gates.md` | Review, refinement, release verification |

```text
skill_view(name='design-foundation', file_path='references/principles.md')
skill_view(name='design-foundation', file_path='references/gates.md')
```

---

> **REMINDER:** Foundation is not a theme. It is the universal quality contract underneath every theme.