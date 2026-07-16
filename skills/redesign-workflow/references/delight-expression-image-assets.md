# Delight / Expression Image Assets

Use this reference when a redesign loop reaches the Delight / Expression layer and the user wants illustration, static images, video, or graphic embellishments.

## Layer rule

Illustration/video/graphics belong to **Delight / Expression**, after strategy, UI, UX, voice, and interaction are coherent. They should create memory and atmosphere, not hide weak structure.

## Capability boundary

Before promising an asset, name the medium and whether the current runtime can produce it:

| Medium | Agent can produce directly? | Notes |
|---|---:|---|
| SVG/CSS/canvas/vector | yes | Best for lightweight motifs, diagrams, marks, and system maps. |
| Raster AI image via GPT Image/DALL·E/Midjourney | only if tool/API is available | Do not imply access unless the runtime exposes it or the user provides it. |
| ComfyUI/Stable Diffusion | only if ComfyUI/cloud/local model is available | Check server/tool availability before promising generation. |
| User-supplied generated image | yes, for review/integration | Optimize, crop, convert, and integrate. |
| Video/ambient motion | depends on tooling | Always provide static/reduced-motion fallback. |

## Software-related zen/minimalist direction

For a software engineering portfolio, generic zen imagery is usually too vague. Prefer:

```text
✓ abstract software architecture map
✓ modular boundaries / domain boxes
✓ interface blueprint / wireframe system
✓ prompt → design spec → UI review flow
✓ dependency lines, agents, review gates, product modules
✓ ink wash / paper texture / grayscale restraint
```

Avoid:

```text
✗ temple/roofline as the main subject without software relation
✗ stones, tea, bamboo, mountains, lotus, generic meditation objects
✗ dashboards/screenshots that look like SaaS product mockups
✗ circuit boards, neon, blue tech gradients, cyberpunk meshes
✗ icon sets or many small decorations per section
```

## Prompt pattern for generated images

Use a prompt that makes the software artifact the subject and zen only the rendering style:

```text
Create a quiet zen minimalist editorial illustration for a personal software engineering portfolio.

Subject:
An abstract software architecture map: modular blocks, nested domain boundaries, thin dependency lines, and a calm flow of decisions. It should suggest clean architecture, reusable modules, and long-lived product systems.

Style:
Japanese sumi-e ink wash meets precise software architecture linework. Soft grayscale ink, off-white paper texture, restrained, calm, editorial.

Composition:
Wide 16:9 landscape. Large negative space. One focal cluster only. The visual should support website hero text without becoming a busy dashboard.

Avoid:
traditional roof, temple, building, landscape, mountains, people, text, logo, UI screenshots, readable code, laptop, server rack, circuit board, colorful gradients, neon, cyberpunk, 3D render, generic SaaS vector art.
```

## Candidate review questions

Before integrating an image, answer:

```text
1. What software/product idea does the image communicate?
2. Does it support the H1/subcopy story, or is it just decorative?
3. Is the visual metaphor domain-related enough for the surface?
4. Is there too much density, contrast, or small detail?
5. Does it need to be a semantic image, or should it be decorative alt=""?
6. Does it work in both light and dark themes?
7. Will it hurt LCP/CLS? Is it optimized and dimensioned?
```

## Common failure names

Use these terms when diagnosing why an image feels off:

- **Narrative integration failure** — the visual does not advance the hero/story.
- **Accessory drift** — the visual is present but reads like a detached ornament.
- **Cardification** — the image is placed inside a bordered card/box that separates it from the story.
- **Figure-ground mismatch** — the asset creates an isolated surface instead of belonging to the composition.
- **Visual weight under-support** — the visual is too small to support the H1 but too visible to ignore.
- **Generic motif drift** — the motif fits the aesthetic but not the product/domain.

## Integration patterns

### Hero supporting figure

Use when the image should support the H1.

```text
✓ larger supporting visual mass
✓ no unnecessary card/border/background unless the card is the concept
✓ fade/mask/crop edges into the page background
✓ caption connects visual to H1/subcopy
✓ image can be decorative alt="" if caption carries the meaning
```

### Atmospheric ghost

Use when the image should only create mood.

```text
✓ low opacity / masked / behind content
✓ no caption required
✓ decorative alt=""
✓ should disappear on mobile if it adds density
```

### Product evidence image

Use when the image is a screenshot or proof.

```text
✓ semantic alt text
✓ real dimensions to avoid CLS
✓ clear relation to product claim
✓ card/frame allowed because the surface itself is evidence
```

## Performance rules

```text
✓ convert PNG/JPEG candidates to WebP or AVIF
✓ set width/height attributes
✓ use Next/Image or equivalent optimized image component when available
✓ use priority/fetchpriority only for above-fold LCP images
✓ keep final decorative hero asset small (<100KB target when possible)
✗ do not lazy-load the above-fold hero image if it is LCP
```
