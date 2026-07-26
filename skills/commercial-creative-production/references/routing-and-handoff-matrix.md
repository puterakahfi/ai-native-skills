# Commercial Creative Routing and Handoff Matrix

Load this reference when a request could be confused between product-image preparation, prompt translation, commercial production, audit, refinement, redesign, or acceptance.

## Primary route matrix

| Requested outcome | Primary lifecycle or capability | Conditional specialist | Reviewer |
|---|---|---|---|
| Prepare one product image, cutout, retouch, restore, normalize, or create a reusable master | `product-image-production` | `prompt-engineer` only for provider translation | `design-review` when acceptance is requested |
| Create a net-new catalog, marketplace image, flyer, poster, banner, social ad, or campaign creative | `commercial-creative-production` | `product-image-production` when source preparation is required | `design-review` + built-in static-visual strategy |
| Translate an approved plan into provider-specific prompt or edit syntax | `prompt-engineer` | supplied brand/product/design authorities | rendered-output review only when acceptance is requested |
| Audit an existing artifact without changing it | `design-audit` | applicable domain specialist | `design-review` + domain strategy |
| Fix a known narrow defect while preserving accepted direction | `design-refinement` | causal specialist such as `product-image-production` | governing reviewer |
| Replace direction, structure, concept, or multiple layers of an existing artifact | `redesign-workflow` | changed-layer specialists | `design-review` + domain strategy |
| Decide whether an existing export passes | `design-review` | applicable domain reviewer | reviewer owns verdict |

## Asset-state routing

```text
raw product source
  → assess through product-image-production
  → prepare or fail closed
  → approved Product Asset Master variant
  → commercial composition

verified Product Asset Master covering destination
  → reuse approved variant
  → do not repeat background removal, retouching, or regeneration

verified master does not cover destination
  → return to product-image-production
  → create or approve a destination-compatible variant
```

## Handoff ownership

| Handoff | Producer | Consumer | Required evidence |
|---|---|---|---|
| Raw source → product-image preparation | intake/workflow owner | `product-image-production` | source refs, destination, product identity, authority, locks |
| Product Asset Master → commercial design | `product-image-production` | `master-design` and `design-visual` | approved variant, allowed uses, preservation locks, limitations, reprocessing conditions |
| Locked plan → provider translation | production/design owner | `prompt-engineer` | locked plan, prohibited transformations, provider context |
| Provider translation → binary execution | `prompt-engineer` or workflow owner | product/runtime adapter | provider instructions, approved assets, export requirements, limitations |
| Export → acceptance | execution owner | `design-review` | actual artifact, destination preview, fidelity/content/resolution/export evidence |
| Review finding → correction | `design-review` | causal owner | gate ID, evidence, defect class, preservation scope, return route |

## Non-transferable ownership

```text
product truth and Product Asset Master status
  remain with product-image-production

commercial direction and composition synthesis
  remain with master-design under the governing workflow

provider syntax translation
  remains with prompt-engineer

binary execution and provider configuration
  remain with product/runtime adapters

final acceptance
  remains with design-review and applicable domain strategy
```

A handoff transfers an approved artifact and constraints. It does not transfer permission to reinterpret product truth, expand authority, self-certify acceptance, or claim readiness outside the reviewed destination.

## Guard

```text
□ Exactly one primary lifecycle or standalone capability is selected.
□ Raw product sources cannot bypass required image production.
□ Approved masters are reused instead of reprocessed without cause.
□ Every handoff names producer, consumer, evidence, locks, and limitations.
□ Prompt translation and provider execution do not absorb lifecycle or fidelity ownership.
□ Acceptance remains independent.
□ Defects return to their causal owner while valid upstream locks remain intact.
```
