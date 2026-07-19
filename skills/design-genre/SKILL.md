---
name: design-genre
description: Design genre classification — zen-minimalist, editorial, modern-minimal, atmospheric, and playful. Determines voice, density, structure, color, motion stance, and which slop gates apply. Run before any design decision.
license: MIT
metadata:
  ai-native-skills.version: 1.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/design/design-genre.contract.yaml
  ai-native-skills.contract-version: "^1.0.0"
  ai-native-skills.related_skills: '["ux-ui-patterns", "design-system", "master-design", "redesign-workflow"]'
---

# Design Genre Skill

> **HARD RULES — apply always, top and bottom of every engagement:**
> 1. **Genre = composition + density + voice + color + motion stance, not just palette.**
> 2. **Declare the genre token before any design decision.** Everything downstream follows it.
> 3. **Load the selected genre reference before selecting macrostructure or components.**
> 4. **Genre-specific constraints override generic workflow, macrostructure, and component defaults.**
> 5. **Genre must match the audience mental model and explicit user direction.** Wrong genre means downstream misalignment.

---

## Core Principle

```text
Genre scopes everything downstream:
  - Which macrostructures fit
  - Which density and containment grammar is valid
  - Which theme cluster to rotate
  - Which nav/footer archetypes are appropriate
  - What voice/copy fixtures to use
  - Which slop gates and hard constraints apply

Pick genre BEFORE picking layout, colors, fonts, cards, borders, or motion.
Wrong genre = everything downstream is misaligned.

Default only when no stronger signal exists: editorial.
Explicit user genre direction overrides inferred product-category defaults.
```

---

## Genre Detection (Signal-Based)

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

### Conflict policy

```text
Explicit user direction exists
  → use it unless it conflicts with a locked brand/design system

Two or more inferred non-default genres remain plausible
  → ask once which feels closer

No strong signal
  → editorial
```

Do not silently route a personal engineering site to `modern-minimal` merely because it mentions SaaS, agents, APIs, or developer tools when the user explicitly requests zen or space-led minimalism.

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
  genre: <name>
  reference: <loaded file>
  composition_rules: []
  containment_rules: []
  density_rules: []
  color_rules: []
  motion_rules: []
  hard_failures: []
```

A genre label without its loaded constraint set is unresolved and must not proceed to production.

---

## Genre Output Format

Emit once before design starts:

```text
Genre: [zen-minimalist | editorial | modern-minimal | atmospheric | playful]
Signal: [what triggered this — or "default" if editorial]
Reference loaded: [path]
Voice: [one-line description]
Density: [sparse | moderate | dense]
Containment grammar: [space-led | editorial rows | surfaces | mixed]
Motion stance: [motion-on | motion-cut | stillness]
Theme cluster: [list of applicable themes]
Nav range: [N-codes]
Footer range: [Ft-codes]
Macrostructure range: [applicable macrostructures]
Hard genre constraints: [short list]

If wrong: say "genre: [X]" and redirect before production.
```

---

## References — Genre Catalog

Each genre is a standalone file. Load only the selected one.

| Genre | File | Default? |
|---|---|---|
| Zen / Minimalist | [references/zen.md](references/zen.md) | |
| Editorial | [references/editorial.md](references/editorial.md) | ✅ |
| Modern Minimal | [references/modern-minimal.md](references/modern-minimal.md) | |
| Atmospheric | [references/atmospheric.md](references/atmospheric.md) | |
| Playful | [references/playful.md](references/playful.md) | |
| Genre × Macrostructure compatibility | [references/genre-compatibility.md](references/genre-compatibility.md) | |

> **Reminder:** the selected reference is a constraint contract, not inspiration. Generic workflow defaults cannot override it.