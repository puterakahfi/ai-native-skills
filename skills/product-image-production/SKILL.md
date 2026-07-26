---
name: product-image-production
description: Prepare product-source images into truthful, reusable Product Asset Masters by diagnosing source suitability, locking product fidelity, authorizing safe transformations, planning retouching and separation, failing closed on unverifiable detail, and handing verified assets to commercial design or compositing.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.pattern: specialist
  ai-native-skills.requires: "decision-provenance"
  ai-native-skills.related_skills: '["prompt-engineer","master-design","design-visual","design-review","workflow-router","role-switcher","redesign-workflow","design-refinement"]'
---

# Product Image Production

Prepare a source image for faithful reuse as a product asset. This skill owns the decision boundary between a raw product source and a documented Product Asset Master.

It may be loaded directly for one-asset preparation or by a governing commercial-production, redesign, or refinement workflow. It does not own provider execution, final advertising composition, product UI, storage, or final acceptance.

## Core rule

```text
source image + declared destination
→ assess what is visible and trustworthy
→ lock product truth
→ authorize each transformation
→ plan the smallest safe production operations
→ execute through a product/provider adapter when requested
→ verify exported evidence
→ emit Product Asset Master or fail closed
```

A plausible-looking result is not sufficient. Product truth, exported evidence, and declared limitations control the result.

## When to use

Load this skill when the request includes one or more of:

- product-photo cleanup or professional retouching;
- background removal, cutout, masking, or transparent PNG preparation;
- clean-white or neutral-studio product assets;
- product image restoration, perspective correction, or destination-aware upscale;
- crop, canvas, scale, padding, shadow, or export normalization;
- creation of a reusable product asset before catalog, marketplace, flyer, banner, social-ad, or compositing work;
- review of whether a source image is suitable for a declared product-output profile.

Do not load it merely because a final design contains a product. A verified reusable Product Asset Master can be consumed directly without reprocessing.

## Boundary

### Owns

```text
source suitability for the declared output
product truth inventory
fidelity and preservation locks
authorized, conditional, prohibited, and unverified transformations
retouch restraint and safe cleanup decisions
background separation and masking strategy
color and material preservation decisions
perspective, restoration, upscale, and shadow constraints
crop, canvas, scale, padding, and export preparation
Product Asset Master declaration
limitations and fail-closed guidance
downstream asset handoff
```

### Delegates

```text
provider/model/API/tool selection and binary execution → product/runtime adapter
provider-specific prompt or edit syntax → prompt-engineer
final commercial message and composition → master-design + design-visual
audit normalization and final visual verdict → design-review
existing broad artifact redesign → redesign-workflow
known narrow existing-artifact correction → design-refinement
brand policy, UI, storage, versioning, and operational implementation → product repository
legal claims, trademark approval, and regulated-content approval → governing specialist
```

### Prohibits

```text
inventing missing labels, logos, packaging, geometry, texture, or controls
silently redrawing a specific product as a plausible substitute
generic beautification that changes product truth
claiming restoration recovered details that were not verifiable
accepting a preview without exported evidence when production is claimed
universal crop, padding, sharpening, denoise, or upscale percentages
hiding provider uncertainty behind words such as premium, realistic, or enhanced
routing an unverified raw source directly into final commercial design when preparation is required
```

## Required input

```yaml
product_image_production_input:
  request_id: <stable identifier>
  source_assets:
    - asset_ref: <required>
      source_type: <photograph | scan | render | generated | unknown>
      declared_product_identity: <provided value or null>
      provenance_status: <verified | user_provided | unknown>
      dimensions: <known or unknown>
      color_profile: <known or unknown>

  intended_output:
    profile: <transparent-product-catalog | clean-white-catalog | grounded-product-asset | neutral-studio-asset | custom>
    target_channels: []
    final_dimensions: []
    required_alpha: <true | false | conditional>
    required_shadow_mode: <preserve | remove | separate | controlled_regeneration | not_applicable>

  product_truth:
    required_identifiers: []
    distinguishing_geometry: []
    packaging_details: []
    required_text_and_labels: []
    logo_and_brand_marks: []
    material_and_surface_properties: []
    approved_reference_assets: []
    unknown_or_unverifiable_details: []

  fidelity_locks:
    preserve_shape: true
    preserve_packaging: true
    preserve_logo: true
    preserve_label_text: true
    preserve_material: true
    preserve_product_color: true
    preserve_distinguishing_details: true
    additional_locks: []

  transformation_authorization:
    allowed: []
    conditional: []
    prohibited: []
    authority_refs: []

  delivery_constraints:
    minimum_effective_resolution: <declared or unresolved>
    crop_and_safe_area_constraints: []
    transparency_constraints: []
    export_formats: []
    compression_constraints: []
    color_constraints: []

  provider_context:
    execution_requested: <true | false>
    available_adapters: []
    selected_adapter: <adapter ref or null>
    provider_limitations: []
```

Missing destination, product-identity, preservation, or authority information is recorded as unresolved. Do not silently guess material decisions.

## Execution procedure

### 1. Classify the request

Determine whether the requested result is:

```text
specification only
source suitability assessment
single asset preparation
existing asset refinement
final commercial creative production
acceptance review
```

This skill can own the first four only within its declared boundary. Route final commercial composition or acceptance to the governing workflow/reviewer.

### 2. Inventory source truth

Record what the source directly proves:

- product geometry and silhouette;
- readable labels and logo marks;
- packaging construction;
- color and material evidence;
- reflections, transparency, texture, fine edges, and shadows;
- missing, blurred, obstructed, contradictory, or cropped details;
- source dimensions, compression, noise, and color-profile limitations.

Load [source suitability and fail-closed decisions](references/source-suitability-and-fail-closed.md) when source quality, difficult edges, restoration, reshoot, or recovery claims matter.

### 3. Resolve fidelity locks and authority

Preserve identifying truth by default. A requested edit does not automatically authorize a material change.

Load [fidelity locks and transformation authorization](references/fidelity-locks-and-transformations.md) when the request includes cleanup, geometry correction, label/logo treatment, restoration, generative completion, color change, shadow changes, or any transformation with product-truth impact.

Use `decision-provenance` when authority is material, disputed, missing, or superseded.

### 4. Assess suitability

Return exactly one source status:

```text
SUITABLE
SUITABLE_WITH_LIMITS
UNSUITABLE
NOT_VERIFIED
```

Assessment is destination-specific. A source may be suitable for a small marketplace thumbnail but unsuitable for a large campaign crop or precise transparent master.

### 5. Classify every operation

For each proposed operation, record:

```yaml
transformation_decision:
  operation: <operation id>
  purpose: <named production role>
  authorization: <allowed | conditional | prohibited | not_verified>
  product_truth_impact: <none | low | material | unknown>
  evidence_required: []
  provider_constraints: []
  rollback_or_alternative: <safer option or null>
  rationale: <why this is justified>
```

Prefer the smallest causal operation. Do not apply generic enhancement stacks.

### 6. Produce an adapter-neutral operation plan

The plan may include only justified operations such as:

- non-product dust/background cleanup;
- exposure and white-balance correction within verified product color constraints;
- restrained noise reduction and sharpening for the declared destination;
- safe perspective correction that preserves geometry;
- background separation and mask refinement;
- natural-shadow preservation, separation, or controlled removal;
- crop, canvas, scale, and padding normalization;
- destination-aware restoration or upscale with explicit artifact review;
- export and color-profile preparation.

Provider selection and execution remain outside this skill. `prompt-engineer` may translate the locked plan into provider-specific instructions without becoming the fidelity owner.

### 7. Verify execution evidence

When execution is claimed, require the actual exported artifact and applicable comparison evidence. Inspect at actual size and destination context, not only a reduced preview.

Minimum evidence can include:

- source and exported artifact references;
- product-fidelity comparison;
- label/logo and color/material comparison;
- mask, edge, clipping, residue, and halo inspection;
- effective-resolution and export-integrity checks;
- operation record and provider limitations;
- declared unsupported or unverified claims.

Missing exported evidence produces `NOT_VERIFIED`, not PASS.

### 8. Emit Product Asset Master or fail closed

Load [Product Asset Master](references/product-asset-master.md) to construct the final output, quality report, variants, limitations, and downstream handoff.

A specification-only run may emit a planned master with `specified_only` status. It must not claim that an image was produced or accepted.

## Quality gates

```text
request_and_destination_are_explicit
source_truth_is_inventoried_before_transformation
fidelity_locks_are_explicit_and_authorized
required_unknowns_are_not_silently_filled
source_suitability_is_destination_specific
every_operation_has_purpose_authorization_impact_and_evidence
smallest_safe_operation_set_is_selected
provider_execution_does_not_absorb_shared_skill_ownership
product_identity_is_preserved_unless_authoritatively_changed
restoration_and_upscale_claims_match_observable_evidence
mask_shadow_crop_and_export_claims_require actual artifact evidence
specification_only_output_is_not_reported_as_produced
Product_Asset_Master_records_limits_and_downstream_locks
final_acceptance_remains_independent
```

## Fail-closed conditions

Stop, limit, or route for a better source when:

- required identifying text or geometry is absent, obstructed, or unrecoverably blurred;
- source/reference assets contradict each other without an authority decision;
- a requested edit would materially alter locked product truth;
- generative completion would invent required product details;
- the source lacks sufficient effective resolution for the declared destination;
- reflective, translucent, soft, or mixed edges cannot be separated truthfully with the available evidence;
- provider limitations prevent a checkable fidelity or export claim;
- only a preview exists but a production-ready asset is being claimed.

Allowed outcomes are:

```text
PROCEED
PROCEED_WITH_LIMITS
REQUEST_BETTER_SOURCE_OR_REFERENCE
ROUTE_FOR_AUTHORITY
BLOCK_UNSAFE_TRANSFORMATION
NOT_VERIFIED
```

## Handoff

```yaml
product_image_production_result:
  request_id:
  source_assessment:
  fidelity_lock_record:
  transformation_decisions: []
  operation_plan: []
  execution_status: <not_requested | specified_only | produced | blocked | not_verified>
  product_asset_master: <record or null>
  evidence_refs: []
  limitations: []
  next_route: <provider_adapter | prompt-engineer | master-design | design-visual | design-review | better_source | authority_owner | ready>
```

Downstream design receives only the approved asset variant, preservation locks, allowed/prohibited uses, evidence status, and reprocessing conditions. It does not receive permission to reinterpret product truth.

## Anti-patterns

```text
❌ “Make it more premium” without specifying what may change.
❌ Rebuilding unreadable label text from model guesses.
❌ Whitening, smoothing, sharpening, or recoloring every source by default.
❌ Treating a provider's photorealism setting as product-fidelity evidence.
❌ Removing all natural shadows before deciding whether grounding is required.
❌ Applying one padding percentage to every product shape and destination.
❌ Upscaling because a tool supports it rather than because the destination needs it.
❌ Calling a cutout clean without actual-size alpha-edge inspection.
❌ Reprocessing a verified master for every downstream design.
❌ Letting the producer issue its own final acceptance verdict.
```

## Final guard

```text
□ The request, product identity, output profile, destination, and source references are explicit.
□ Source truth and uncertainty were recorded before edits were planned.
□ Fidelity locks and authority references are explicit.
□ Every material transformation is authorized or blocked.
□ The operation set is minimal and provider-neutral.
□ Unrecoverable details were not invented.
□ Execution claims have exported evidence.
□ Product Asset Master status and limitations are honest.
□ Downstream locks, allowed uses, and reprocessing conditions are recorded.
□ Final visual acceptance is routed independently.
```
