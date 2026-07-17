---
name: prompt-engineer
description: >
  Image generation prompt engineering expert — craft, refine, and score prompts for text-to-image
  models (DALL-E, Midjourney, Stable Diffusion, Flux). Use when user wants to generate, improve,
  or debug image prompts, or when output quality, token efficiency, or style consistency needs
  to improve. Auto-triggered by: "refine prompt", "generate image prompt", "improve this prompt",
  "why does my image look wrong", "prompt for [subject]".
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
---

# Prompt Engineer

## Core Role

Image generation prompts are a craft — not keyword stuffing. A good prompt is:
- **Specific** — subject, style, lighting, composition, mood, color palette
- **Efficient** — high-signal tokens first, no filler words
- **Model-aware** — syntax and weight conventions differ per model
- **Scoreable** — measurable before generating (saves tokens, avoids retries)

---

## Prompt Anatomy

Every strong image prompt has these layers (in priority order):

```
[Subject]       → who/what is the main focus
[Action/Pose]   → what is happening
[Environment]   → setting, background, context
[Style]         → art style, medium, artist reference
[Lighting]      → key light, mood, time of day
[Color palette] → dominant hues, temperature
[Composition]   → framing, angle, depth of field
[Quality tags]  → resolution, rendering engine, finish
[Negative]      → what to explicitly exclude
```

---

## Model Dialects

### DALL-E 3 (OpenAI)
- Natural language, no weight syntax
- Be descriptive and literal — it follows instructions closely
- Avoid: overly abstract prompts, celebrity names
- Strength: composition, text in image, instruction following

```
A product UI mockup of a mobile app for scheduling sports facilities.
Clean minimal interface, light mode, card-based layout.
Soft shadows, professional photography style, white background.
High resolution, sharp edges.
```

### Midjourney
- Comma-separated keywords work best
- Weight syntax: `(keyword::1.5)` to boost, `(keyword::-1)` to suppress
- Params: `--ar 16:9 --style raw --v 6 --q 2`
- Strength: artistic style, atmosphere, cinematic

```
sports facility scheduler app UI, mobile mockup, minimal design,
card layout, soft blue palette, professional :: clean interface ::2
--ar 9:16 --style raw --v 6
```

### Stable Diffusion / SDXL
- Weight syntax: `(keyword:1.3)` boost, `[keyword]` suppress
- Negative prompt is critical
- LoRA: `<lora:model_name:0.8>`
- Strength: fine-grained control, custom models, NSFW handling

```
Positive:
(mobile app UI mockup:1.4), sports facility scheduler, (minimal design:1.3),
card-based layout, soft colors, (professional photography:1.2),
8k resolution, sharp focus, studio lighting

Negative:
blurry, low quality, watermark, text errors, distorted UI,
extra fingers, bad anatomy, ugly, duplicate
```

### Flux (Black Forest Labs)
- Natural language like DALL-E but more photorealistic
- Supports detailed scene description
- Strength: photorealism, product shots, UI mockups

```
Professional product photograph of a mobile app interface for sports
facility scheduling. Clean white background, soft studio lighting,
minimal UI with card components, blue accent colors.
Shot on Canon R5, 85mm lens, shallow depth of field.
```

---

## Prompt Scoring Gates

Score before generating — a prompt scoring < 6.0 will likely need retries (wastes tokens).

| Gate | Question | Score 0–2 |
|---|---|---|
| **Specificity** | Is the subject unambiguous? | 0=vague, 1=partial, 2=clear |
| **Style clarity** | Is art style/medium declared? | 0=none, 1=genre only, 2=medium+reference |
| **Composition** | Is framing/angle specified? | 0=none, 1=implied, 2=explicit |
| **Lighting** | Is lighting/mood defined? | 0=none, 1=generic, 2=specific |
| **Negative coverage** | Are common failure modes excluded? | 0=none, 1=some, 2=comprehensive |
| **Model fit** | Does syntax match target model? | 0=wrong dialect, 1=partial, 2=correct |

**Minimum score: 8/12 before generating.**

---

## Refinement Loop

```
1. RECEIVE    — user's raw prompt or intent
2. ANALYZE    — score against 6 gates, identify gaps
3. RECONSTRUCT — rewrite using prompt anatomy layers
4. SCORE      — verify ≥ 8/12
5. DELIVER    — formatted for target model + negative prompt
6. ITERATE    — if user provides output feedback, diagnose and patch
```

---

## Token Efficiency Rules

1. **Front-load the subject** — models weight earlier tokens more heavily
2. **No filler** — remove "please", "I want", "a photo of a photo of"
3. **Specifics beat adjectives** — "Canon R5 85mm" > "professional camera"
4. **Style references beat descriptions** — "Gregory Crewdson lighting" > "dark moody cinematic"
5. **DALL-E**: 400 chars optimal. SD: 75 tokens hard limit (CLIP). MJ: no hard limit but diminishing returns after ~60 tokens

---

## Visual Product Use Case (visualmate.id)

For AI-powered image generation in a product:

**User intent classification:**
- "generate X" → build prompt from scratch using anatomy
- "improve this" → score existing, patch failing gates
- "why does it look wrong" → diagnose: check model fit, negative prompts, token order
- "make it more [adj]" → identify which layer to amplify

**Product-level concerns:**
- Consistent style across generations → lock `[Style]` + `[Color palette]` tokens as system prefix
- Token budget per generation → keep prompt < 300 chars for DALL-E cost efficiency
- User-facing prompts → translate user plain language to model-specific syntax invisibly
- Batch consistency → use seed + fixed style tokens for coherent sets

---

## Anti-Patterns

| Anti-Pattern | Fix |
|---|---|
| "a beautiful image of X" | Remove filler — just describe X specifically |
| No negative prompt (SD) | Always add: `blurry, low quality, watermark, distorted` |
| Wrong dialect for model | Check model first, apply correct weight syntax |
| Abstract concepts as subject | Convert to visual concrete: "loneliness" → "person sitting alone at empty cafe table" |
| Over-weighted keywords `(word:3.0)` | Cap at 1.4 — higher breaks model coherence |
| Skipping composition | Always specify angle, framing, focal point |
