---
name: design-genre
description: Design genre classification — zen-minimalist, editorial, modern-minimal, atmospheric, and playful. Runs after design-foundation and determines voice, density, containment, color, motion stance, and genre-specific slop gates without overriding universal composition quality.
license: MIT
metadata:
  ai-native-skills.version: 1.2.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/design/design-genre.contract.yaml
  ai-native-skills.contract-version: "^1.0.0"
  ai-native-skills.related_skills: '["design-foundation","ux-ui-patterns","design-system","master-design","redesign-workflow"]'
---

# Design Genre Skill

> **HARD RULES — apply always:**
> 1. **Resolve `design-foundation` first.** Genre expresses hierarchy, grouping, alignment, spacing, balance, flow, legibility, and responsiveness; it does not replace them.
> 2. **Genre = composition expression + density + voice + color + motion stance, not just palette.**
> 3. **Declare the genre token before genre-specific design decisions.**
> 4. **Load the selected genre reference before selecting macrostructure or components.**
> 5. **Genre-specific constraints override generic workflow, macrostructure, and component defaults — but never foundation requirements.**
> 6. **Genre must match the audience mental model and explicit user direction.** Wrong genre means downstream misalignment.

---

## Layer Relationship

```text
design-foundation
  owns: hierarchy, grouping, alignment, space rhythm, balance, flow,
        legibility, consistency, accessibility, responsive continuity

          ↓ expressed through

design-genre
  owns: density, containment grammar, visual voice, color stance,
        motion stance, texture, stylistic restraint/expression

          ↓ constrained by

design-brand / DESIGN.md
  owns: identity, assets, semantic tokens, product-specific locks
```

A genre may make a foundation rule stricter. It may not remove it.

---

## Core Principle

```text
Genre scopes downstream expression:
  - Which macrostructures fit
  - Which density and containment grammar is valid
  - Which theme cluster to rotate
  - Which nav/footer archetypes are appropriate
  - What voice/copy fixtures to use
  - Which additional slop gates and hard constraints apply

Foundation remains active underneath:
  - parent/child/sibling hierarchy
  - grouping by relationship
  - structural and optical alignment
  - intentional spatial rhythm
  - balance and focal order
  - reading/task flow
  - legibility, accessibility, responsive continuity
```

Pick genre **after foundation resolution** and before layout, colors, fonts, cards, borders, or motion.

```text
No strong genre signal → editorial default
Explicit user genre direction → overrides inferred product-category defaults
Foundation failure → fix foundation; do not switch genre as a workaround
```

---

## Required Foundation Handoff

Before genre detection, foundation state must include:

```yaml
foundation_handoff:
  hierarchy_roles: []
  parent_child_groups: []
  sibling_sets: []
  structural_anchors: []
  optical_corrections: []
  spatial_rhythm_rules: []
  balance_strategy: <value | unresolved>
  flow_sequence: []
  legibility_requirements: []
  responsive_continuity_rules: []
  unresolved_foundation_gaps: []
```

If foundation is unresolved, genre selection may be exploratory but production must not begin.

---

## Genre Detection — Signal Based

```text
ZEN / MINIMALIST:
  zen, minimalist, stillness, restraint, ma, sparse, wabi-sabi,
  negative space, senior personal portfolio, quiet, monk-mode,
  focus on space, calm, few visual interruptions

ATMOSPHERIC:
  AI tool, generative, music, video, voice, audio, late-night,
  dark mode, creative tool, artist tool, ambient, cinematic

MODERN-MINIMAL:
  SaaS, enterprise, API, platform, developer tool, infra,
  B2B, dev experience, dashboard, analytics, productivity

PLAYFUL:
  fun, consumer, casual, friendly, onboarding, family,
  community, kids, social, lifestyle, wellness

EDITORIAL:
  portfolio, personal, blog, magazine, agency, studio,
  foundry, publication, art direction
```

### Conflict Policy

```text
Explicit user direction exists
  → use it unless it conflicts with a locked brand/design system

Two or more inferred non-default genres remain plausible
  → ask once which feels closer

No strong signal
  → editorial
```

Do not silently route a personal engineering site to `modern-minimal` merely because it mentions SaaS, agents, APIs, or developer tools when the user explicitly requests zen or space-led minimalism.

Do not use a genre change to hide a foundation problem:

```text
flat hierarchy        ≠ “modern minimal”
misalignment          ≠ “editorial asymmetry”
excessive empty space ≠ “zen”
random color          ≠ “playful”
weak contrast         ≠ “atmospheric”
```

---

## Mandatory Reference Load

After selecting a genre, load exactly its catalog file before macrostructure selection:

```text
zen-minimalist → references/zen.md
editorial       → references/editorial.md
modern-minimal  → references/modern-minimal.md
atmospheric     → references/atmospheric.md
playful         → references/playful.md
```

Record the loaded constraints in run state:

```yaml
genre_contract:
  foundation_reference: <design-foundation path>
  inherited_foundation_rules: []
  genre: <name>
  reference: <loaded file>
  composition_expression: []
  containment_rules: []
  density_rules: []
  color_rules: []
  motion_rules: []
  hard_failures: []
```

A genre label without its loaded constraint set is unresolved and must not proceed to production.

---

## Genre Output Format

Emit once before genre-specific production starts:

```text
Foundation: [resolved | unresolved]
Foundation reference: [path]
Foundation gaps: [list]
Genre: [zen-minimalist | editorial | modern-minimal | atmospheric | playful]
Signal: [what triggered this — or "default" if editorial]
Genre reference loaded: [path]
Voice: [one-line description]
Density: [sparse | moderate | dense]
Containment grammar: [space-led | editorial rows | surfaces | mixed]
Motion stance: [motion-on | motion-cut | stillness]
Theme cluster: [list of applicable themes]
Nav range: [N-codes]
Footer range: [Ft-codes]
Macrostructure range: [applicable macrostructures]
Inherited foundation rules: [short list]
Hard genre constraints: [short list]
```

If wrong, say `genre: [X]` and redirect before production.

---

## References — Genre Catalog

Each genre is a standalone expression contract. Load only the selected one.

| Genre | File | Default? |
|---|---|---|
| Zen / Minimalist | [references/zen.md](references/zen.md) | |
| Editorial | [references/editorial.md](references/editorial.md) | ✅ |
| Modern Minimal | [references/modern-minimal.md](references/modern-minimal.md) | |
| Atmospheric | [references/atmospheric.md](references/atmospheric.md) | |
| Playful | [references/playful.md](references/playful.md) | |
| Genre × Macrostructure compatibility | [references/genre-compatibility.md](references/genre-compatibility.md) | |

> **Reminder:** genre is an extension contract, not the universal base. Generic defaults cannot override genre; genre cannot override foundation.