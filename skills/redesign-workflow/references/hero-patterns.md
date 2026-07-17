# Hero Patterns

Use when touching above-fold composition, hero image, hero CTA/story, or first-impression gates.

## Hero decision rule

The hero must have one primary job. Choose the pattern from the job, not from decoration preference.

| Pattern | Use when | Primary focal object | Image role |
|---|---|---|---|
| Type-led manifesto | Identity/stance is the product | H1 | absent or atmospheric echo |
| Image-supported statement | Visual helps explain the claim | H1 + supporting figure | integrated, not boxed |
| Product evidence hero | Screenshot/proof is the claim | product surface | framed/card allowed |
| Split studio hero | Person/work are equal identity | text + visual equal | visual can be semantic |
| Editorial long-form hero | Reading/context first | headline + dek | minimal ornament |
| Atmospheric hero | Mood/brand memory first | composition field | low-opacity/behind/fade |

## Pattern selection

For a personal software portfolio:

```text
showcase + identity high + low live-product count → Type-led manifesto or Image-supported statement
NOT product screenshot hero unless showing a real product surface
NOT generic atmospheric hero unless visual metaphor is domain-specific
```

## Type-led manifesto

Use when H1 is the thing to remember.

```text
✓ H1 dominates within first 100vh
✓ visual, if present, is a supporting echo
✓ CTA is secondary to stance
✓ empty space reinforces confidence
✗ no competing card cluster beside H1
✗ no product-dashboard mockup unless evidence is needed
```

## Image-supported statement

Use when the visual clarifies the claim.

```text
✓ image is large enough to carry supporting visual weight
✓ image edge blends into page via crop/mask/fade/overlap
✓ caption bridges image to H1/subcopy
✓ alt="" if nearby text carries meaning and image is decorative
✗ avoid small bordered card unless the card itself is the story
✗ avoid image that is merely aesthetic but not domain-related
```

## Product evidence hero

Use when a product screenshot is proof.

```text
✓ card/frame allowed because the product surface is the evidence
✓ semantic alt text required
✓ clear dimensions to avoid CLS
✓ should connect directly to CTA/product claim
✗ do not use fake screenshots as credibility proof
```

## Hero anti-pattern names

```text
❌ Split without equality — visual takes 50% layout but does not deserve 50% narrative weight
❌ Accessory drift — image exists beside hero but can be removed with no loss
❌ Cardification — visual is boxed even though it should be atmosphere/supporting figure
❌ Hero void — min-height/centering creates dead space without intentional focal tension
❌ CTA urgency mismatch — buttons shout louder than a quiet/showcase page needs
❌ Section leakage — next section appears too early and competes with hero focus
```

## Hero review questions

```text
1. What is the one idea remembered after 50ms?
2. Is the H1 a stance or a job description?
3. If image is removed, what meaning is lost?
4. If image stays, does it deserve its visual weight?
5. Is the visual semantic evidence, supporting figure, or atmospheric ghost?
6. Does the next section enter at the right moment, or leak into the hero?
7. Does mobile preserve the same story without crowding?
```

## Safe hero refinement moves

When direction is already approved, prefer these before changing macrostructure:

```text
- adjust visual weight, opacity, crop, or mask
- move caption closer/farther to clarify relation
- reduce border/card surface around decorative assets
- change hero section padding before changing layout family
- simplify CTA/button contrast before rewriting copy
- hide atmospheric asset on mobile if density rises
```
