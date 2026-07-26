# Fidelity Locks and Transformation Authorization

Load this reference whenever an operation can affect product identity, geometry, packaging, labels, color, material, texture, reflections, shadows, or distinguishing details.

## Product truth before aesthetics

A product image is not a generic visual subject. Its identifying truth can affect purchasing, brand trust, catalog accuracy, marketplace policy, and downstream reuse.

```text
product truth
→ preservation locks
→ explicit transformation authority
→ smallest justified operation
→ evidence-backed verification
```

A style request such as “premium,” “cleaner,” “more dramatic,” or “more professional” is not sufficient authorization to alter product truth.

## Fidelity lock record

```yaml
fidelity_lock_record:
  product_identity:
    declared_identity:
    authoritative_refs: []
    variant_status: <resolved | conflicted | unknown>

  locks:
    preserve_shape: <true | false | conditional>
    preserve_packaging: <true | false | conditional>
    preserve_logo: <true | false | conditional>
    preserve_label_text: <true | false | conditional>
    preserve_material: <true | false | conditional>
    preserve_product_color: <true | false | conditional>
    preserve_distinguishing_details: <true | false | conditional>
    preserve_functional_parts: <true | false | conditional>
    preserve_required_surface_state: <true | false | conditional>
    additional_locks: []

  authorized_exceptions:
    - lock:
      allowed_change:
      authority_ref:
      verification_required: []

  unresolved_truth_risks: []
```

The default is preservation. A lock changes only with attributable authority for the named scope.

## Transformation decision contract

Classify every operation separately:

```yaml
transformation_decision:
  operation: <stable operation id>
  target_region: <background | product | edge | shadow | canvas | full-image>
  purpose: <named production role>
  authorization: <allowed | conditional | prohibited | not_verified>
  product_truth_impact: <none | low | material | unknown>
  affected_locks: []
  authority_refs: []
  evidence_required: []
  provider_constraints: []
  rollback_or_alternative:
  rationale:
```

Do not authorize a whole “retouch” bundle. Each meaningful operation remains reviewable.

## Authorization levels

### Allowed

Use when the operation has a named production purpose, does not materially alter locked truth, and has sufficient evidence.

Common examples:

- remove dust or clutter from the background;
- correct global exposure within verified color/material limits;
- neutralize a documented capture color cast;
- remove sensor spots outside the product;
- refine a mask without changing the silhouette;
- normalize canvas and padding for a declared destination;
- export with the required color profile and alpha settings.

### Conditional

Use when the operation may affect truth or requires destination/provider verification.

Common examples:

- remove a mark located on the product;
- reduce wrinkles or dents;
- change reflection intensity;
- correct perspective;
- reconstruct a small occluded area from authoritative reference evidence;
- upscale beyond native effective resolution;
- regenerate a shadow;
- replace a background through generative editing near difficult edges;
- adjust product color to match an authoritative reference.

The condition must name authority, evidence, provider limitation, and rollback.

### Prohibited

Use when the operation would create unsupported product truth or violate an active lock.

Common examples:

- invent unreadable label text;
- replace a real logo with a similar generated mark;
- change packaging shape or cap geometry;
- add controls, seams, ingredients, texture, or accessories absent from authoritative evidence;
- smooth away functional details;
- silently create a different product variant;
- fabricate transparency, material, or reflection behavior;
- claim a generated substitute is the photographed product.

### Not verified

Use when authority, source evidence, provider behavior, or destination constraints are insufficient to classify safely.

`NOT_VERIFIED` is a blocking state for the proposed operation, not permission to proceed.

## Operation guidance

### Cleanup and retouching

```text
background cleanup
  usually low truth impact

product-surface cleanup
  conditional when the mark may be permanent, manufactured, damaged,
  textured, printed, reflective, or otherwise identifying

beautification
  never a valid operation category by itself
```

Record what is being corrected and why it is not product truth.

### Exposure, white balance, and color

- Preserve relative tonal relationships and material cues.
- Avoid clipping highlights that define glossy, metallic, transparent, or reflective materials.
- Do not neutralize intentional product color.
- Use authoritative references when exact sold-product color matters.
- Distinguish capture correction from a requested product color change.
- Record display/profile uncertainty when calibrated evidence is unavailable.

### Noise reduction and sharpening

- Apply only for the declared output and viewing size.
- Protect printed text, micro-texture, edge transitions, and material grain.
- Reject waxy smoothing, halos, ringing, false texture, and invented detail.
- Do not use one numeric amount for all sources.

### Perspective and geometry

Perspective correction is conditional when it may change product proportions.

```text
allowed intent
  correct capture distortion so observed geometry is represented more faithfully

not allowed by default
  reshape the product to look slimmer, taller, wider, more symmetrical,
  or more appealing than the authoritative object
```

Verify silhouette, parallelism, circular features, label placement, and functional geometry after correction.

### Restoration and reconstruction

- Restoration can correct supported degradation.
- Reconstruction requires authoritative reference evidence.
- Generative completion cannot establish missing product truth.
- Disclose reconstructed regions and evidence.
- When verification is impossible, request a better source or preserve the limitation.

### Upscale

Upscale is conditional on destination need and actual artifact review.

Record:

- source effective resolution;
- target dimensions and viewing context;
- provider/model used by the product adapter;
- introduced or amplified artifacts;
- label/logo and material comparison;
- whether the result remains suitable only at a bounded size.

Upscale does not convert an unreadable label into verified text.

### Background separation and masking

- Preserve the authoritative silhouette.
- Treat reflective, translucent, soft, fibrous, perforated, motion-blurred, and mixed edges as specialist cases.
- Do not cut through handles, holes, straps, transparent walls, steam, crumbs, fibers, or thin structures merely to create a clean contour.
- Separate color spill correction from shape masking.
- Require actual-size edge evidence before claiming a clean asset.

The detailed transparent profile belongs to `transparent-product-catalog`; this specialist defines the fidelity boundary used by that profile.

### Shadows and grounding

Classify the existing shadow before editing:

```text
contact shadow
ambient/form shadow
cast shadow
reflection
drop shadow added by design
unknown or mixed
```

- Preserve natural grounding when needed.
- Remove or separate a shadow only for a named downstream role.
- Regeneration must preserve plausible contact, direction, softness, scale, and scene logic.
- Dramatic advertising shadows belong to commercial compositing, not the neutral Product Asset Master by default.

### Crop, canvas, scale, and padding

- Normalize for destination, product geometry, family consistency, and safe area.
- Protect protrusions, handles, caps, labels, shadows, and irregular silhouettes.
- Use relational rules, not universal percentages.
- Record the actual crop and padding decision in the master variant.

### Export

Export preparation can include:

- format and alpha mode;
- dimensions and pixel density;
- color profile;
- bit depth where material gradients require it;
- compression constraints;
- background and shadow mode;
- naming/version reference;
- intended channels.

A correct preview does not prove export integrity.

## Decision examples

### Example: background dust

```yaml
operation: remove_background_dust
purpose: clean neutral catalog background
authorization: allowed
product_truth_impact: none
evidence_required:
  - source/export comparison outside product silhouette
```

### Example: unreadable label

```yaml
operation: reconstruct_label_text
purpose: make label readable
authorization: prohibited
product_truth_impact: material
rollback_or_alternative: request authoritative packaging artwork or better source
rationale: source does not establish the required text
```

### Example: dent removal

```yaml
operation: remove_product_dent
purpose: represent approved undamaged sellable state
authorization: conditional
product_truth_impact: material
authority_refs:
  - approved product-owner statement or authoritative undamaged reference
evidence_required:
  - before/after geometry review
  - packaging-detail fidelity review
```

### Example: perspective correction

```yaml
operation: correct_capture_perspective
purpose: restore faithful frontal presentation
authorization: conditional
product_truth_impact: low
verification_required:
  - silhouette comparison
  - label and circular-feature geometry comparison
```

## Authority rules

Use `decision-provenance` when:

- a requested edit changes a preservation lock;
- references show different product variants;
- a defect may be a real product feature or state;
- an earlier approval conflicts with the current request;
- destructive or irreversible source treatment is proposed;
- a provider limitation requires accepting fidelity risk.

Agent summaries, provider prompts, model defaults, and aesthetic preference are not product-owner authority.

## Guard

```text
□ Product truth is documented before aesthetic changes.
□ Every operation has one named purpose.
□ Every affected lock is visible.
□ Material changes have attributable authority.
□ Conditional operations name evidence and safer alternatives.
□ Restoration is not confused with generative completion.
□ Upscale is destination-driven and artifact-reviewed.
□ Masking preserves difficult but truthful edges.
□ Shadows are classified before removal or regeneration.
□ Export claims are based on the exported artifact.
```
