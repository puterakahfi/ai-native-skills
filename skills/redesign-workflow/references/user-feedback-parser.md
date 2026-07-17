# User Design Feedback Parser

Use when the user gives qualitative design feedback instead of explicit gate names.

## Rule

Do not default to a single diagnosis such as “hierarchy.” Classify the phrase into one or more likely design failures, then choose the active layer and gates.

## Feedback → failure mapping

| User phrase | Likely failure | Layer | Gates / terms |
|---|---|---|---|
| “something feels off” / “not quite there” | Unknown; run quick visual audit | Verification → route | C1/C2/C3, H1/H2/H3, R8, G6/G8 |
| “too busy” / “noisy” | Density / restraint failure | UI | R8 Restraint, G5 Whitespace, visual density |
| “recolored but still busy” | Recolor without reduction | UI / visual language | Minimalism auto-fail: palette changed, density unchanged |
| “floating” / “unanchored” | Weak anchoring or figure/ground | Composition | C3 Alignment, G4 Figure/Ground |
| “feels like an accessory” | Decoration not story | Delight | Accessory drift, narrative integration failure |
| “boxed again” | Unnecessary surface/card | Delight / composition | Cardification, figure-ground mismatch |
| “small but distracting” | Wrong visual weight | Hierarchy / delight | Visual weight under-support, C2 weight distribution |
| “does not support the story” | Narrative mismatch | Strategy / delight | Narrative integration failure, G8 first impression |
| “too templated” | Generic structure/copy | UI / voice | Slop red list, CP3 no slop, macrostructure mismatch |
| “feels like a generic SaaS page” | Genre mismatch | Strategy / UI | Genre detection failure, visual language mismatch |
| “too empty” | Empty space lacks purpose | Composition | Ma failure: emptiness not anchored by focal object |
| “not minimal enough” | Restraint failure | UI / motion | density, accent use, stillness, one focal object |
| “not expressive enough” | Delight/interaction under-expressive | Delight / interaction | named role missing: reward, atmosphere, emphasis |
| “hard to read” | Readability | Voice / UI | G9 line length, G10 contrast, G11 type size |
| “CTA is confusing” | UX action clarity | UX | CTA clarity, route/hash behavior |

## Classification output

When parsing feedback, emit compactly:

```text
Feedback classification:
  Raw phrase: “...”
  Likely issue: [failure name]
  Active layer: [strategy | UI | UX | voice | interaction | delight | verification]
  Gates to inspect: [gate ids/terms]
  Preserve: [approved layers/elements]
```

## Response behavior

If confidence is high, act immediately. Example:

```text
“Feels like an accessory” → Delight failure: accessory drift + narrative integration failure.
Fix: remove card surface, increase/decrease visual weight intentionally, integrate with hero story.
```

If confidence is low, run quick visual audit instead of asking the user to diagnose:

```text
“Something feels off” → run screenshot/DOM + classify top 2 likely failures.
```

## Do not overfit one phrase

A phrase can map to multiple gates. Pick the one that changes the next action.

Example:

```text
“The image is small, boxed, and does not support the story.”
Primary: Delight narrative integration
Secondary: Composition figure-ground
Not primary: raw hierarchy, unless H1/visual competition is the main issue
```
