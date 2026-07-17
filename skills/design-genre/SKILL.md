---
name: design-genre
description: Design genre classification — editorial, modern-minimal, atmospheric, playful. Determines theme cluster, voice fixtures, nav/footer defaults, and which slop gates apply. Run before any design decision. Borrowed concept from Hallmark (Nutlope), adapted for ai-native-skills ecosystem.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.implements: ai-native-core/contracts/skills/design/design-genre.contract.yaml
  ai-native-skills.contract-version: "^1.0.0"
  ai-native-skills.related_skills: '["ux-ui-patterns", "design-system", "master-design", "redesign-workflow"]'
---

# Design Genre Skill

> **HARD RULES — apply always, top and bottom of every engagement:**
> 1. **Genre = voice + color + motion stance, not just color palette.** Picking colors without genre = misaligned output.
> 2. **Declare genre token card before any design decisions.** Emit the genre output block first; everything else follows.
> 3. **Genre must match audience mental model.** Wrong genre = everything downstream is misaligned.

---

## Core Principle

```
Genre scopes everything downstream:
  - Which macrostructures fit
  - Which theme cluster to rotate
  - Which nav/footer archetypes are appropriate
  - What voice/copy fixtures to use
  - Which slop gates apply most strictly

Pick genre BEFORE picking layout, colors, or fonts.
Wrong genre = everything downstream is misaligned.

Default: editorial (silent, no signal needed)
```

---

## Genre Detection (Signal-Based)

```
ATMOSPHERIC: AI tool, generative, music, video, voice, audio, late-night,
  dark mode, creative tool, artist tool, ambient, cinematic

MODERN-MINIMAL: SaaS, enterprise, API, platform, developer tool, infra,
  B2B, dev experience, dashboard, analytics, productivity

PLAYFUL: fun, consumer, casual, friendly, onboarding, family,
  community, kids, social, lifestyle, wellness

ZEN/MINIMALIST: zen, minimalist, stillness, restraint, ma, sparse, wabi-sabi,
  senior personal portfolio, quiet, monk-mode

EDITORIAL (default): portfolio, personal, blog, magazine, agency, studio,
  foundry, publication, art direction

Conflict (2+ non-default signals): ask once:
  "This brief fits [genre A] and [genre B] — which feels closer?"
```

---

## Genre Output Format

After detecting genre, emit ONCE before design starts:

```
Genre: [editorial | modern-minimal | atmospheric | playful]
Signal: [what triggered this — or "default" if editorial]
Voice: [one-line description]
Motion stance: [motion-on | motion-cut]
Theme cluster: [list of applicable themes]
Nav range: [N-codes]
Footer range: [Ft-codes]
Macrostructure range: [applicable macrostructures]

If wrong: say "genre: [X]" and I'll redirect.
```

---

## References — Genre Catalog

Each genre is a standalone file. Load only the one you need.

| Genre | File | Default? |
|---|---|---|
| Zen / Minimalist | [references/zen.md](references/zen.md) | |
| Editorial | [references/editorial.md](references/editorial.md) | ✅ |
| Modern Minimal | [references/modern-minimal.md](references/modern-minimal.md) | |
| Atmospheric | [references/atmospheric.md](references/atmospheric.md) | |
| Playful | [references/playful.md](references/playful.md) | |
| Genre × Macrostructure compatibility | [references/genre-compatibility.md](references/genre-compatibility.md) | |

> **Reminder:** genre = voice+color+motion stance · declare genre token card first · must match audience mental model.
