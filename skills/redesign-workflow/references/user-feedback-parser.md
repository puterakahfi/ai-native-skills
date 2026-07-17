# User Design Feedback Parser

Use when the user gives qualitative design feedback instead of explicit gate names.

## Rule

Do not answer “yes, hierarchy” by default. Classify the phrase into one or more likely design failures, then choose the active layer and gates.

## Feedback → failure mapping

| User phrase | Likely failure | Layer | Gates / terms |
|---|---|---|---|
| “kureng” / “something is off” | Unknown; run quick visual audit | Verification → route | C1/C2/C3, H1/H2/H3, R8, G6/G8 |
| “rame” | Density / restraint failure | UI | R8 Restraint, G5 Whitespace, visual density |
| “coklat rame” | Recolor without reduction | UI / visual language | Zen auto-fail: palette changed, density unchanged |
| “ngambang” | Weak anchoring or figure/ground | Composition | C3 Alignment, G4 Figure/Ground |
| “kayak aksesoris” | Decoration not story | Delight | Accessory drift, narrative integration failure |
| “ada kotaknya lagi” | Unnecessary surface/card | Delight / composition | Cardification, figure-ground mismatch |
| “kecil banget tapi ganggu” | Wrong visual weight | Hierarchy / delight | Visual weight under-support, C2 weight distribution |
| “nggak mendukung story” | Narrative mismatch | Strategy / delight | Narrative integration failure, G8 first impression |
| “template banget” | Generic structure/copy | UI / voice | Slop red list, CP3 no slop, macrostructure mismatch |
| “SaaS banget” | Genre mismatch | Strategy / UI | Genre detection failure, visual language mismatch |
| “terlalu kosong” | Empty space lacks purpose | Composition | Ma failure: emptiness not anchored by focal object |
| “kurang zen” | Restraint failure | UI / motion | density, accent use, stillness, one focal object |
| “kurang hidup” | Delight/interaction under-expressive | Delight / interaction | named role missing: reward, atmosphere, emphasis |
| “susah dibaca” | Readability | Voice / UI | G9 line length, G10 contrast, G11 type size |
| “CTA bingung” | UX action clarity | UX | CTA clarity, route/hash behavior |

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
“Kayak aksesoris” → Delight failure: accessory drift + narrative integration failure.
Fix: remove card surface, increase/decrease visual weight intentionally, integrate with hero story.
```

If confidence is low, run quick visual audit instead of asking the user to diagnose:

```text
“Kureng” → run screenshot/DOM + classify top 2 likely failures.
```

## Do not overfit one phrase

A phrase can map to multiple gates. Pick the one that changes the next action.

Example:

```text
“Gambarnya kecil, ada kotaknya, nggak support story”
Primary: Delight narrative integration
Secondary: Composition figure-ground
Not primary: raw hierarchy, unless H1/visual competition is the main issue
```
