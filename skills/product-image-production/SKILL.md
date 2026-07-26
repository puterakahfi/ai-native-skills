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
→ load the selected production profile
→ plan the smallest safe production operations
→ execute through a product/provider adapter when requested
→ verify exported evidence
→ emit Product Asset Master or fail closed
```

A plausible-looking result is not sufficient. Product truth, exported evidence, declared limitations, and destination-specific profile gates control the result.

## When to use

Load this skill for:

- product-photo cleanup or restrained professional retouching;
- background removal, cutout, masking, or transparent PNG preparation;
- clean-white, grounded, or neutral-studio product assets;
- restoration, perspective correction, or destination-aware upscale;
- crop, canvas, scale, padding, shadow, or export normalization;
- reusable product preparation before catalog, marketplace, flyer, banner, social-ad, or compositing work;
- source-suitability review for a declared product-output profile.

Do not load it merely because a final design contains a product. Consume an already verified Product Asset Master without reprocessing.

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
profile-specific production gates
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
brand policy, UI, storage, versioning, and operations → product repository
legal, trademark, regulated-content, and approval decisions → governing specialist
```

### Prohibits

```text
inventing missing labels, logos, packaging, geometry, texture, or controls
silently redrawing a specific product as a plausible substitute
generic beautification that changes product truth
claiming restoration recovered details that were not verifiable
accepting a preview without exported evidence when production is claimed
universal crop, padding, fill-ratio, feather, sharpening, denoise, or upscale values
hiding provider uncertainty behind premium, realistic, clean, or enhanced
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
    intended_backgrounds: []
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

Missing destination, product identity, preservation, or authority information is unresolved. Do not silently guess material decisions.

## Execution procedure

### 1. Classify the request

Classify as exactly one primary concern:

```text
specification only
source suitability assessment
single asset preparation
existing asset refinement
final commercial creative production
acceptance review
```

This skill owns the first four only within its declared boundary. Route final composition or acceptance to the governing workflow/reviewer.

### 2. Inventory source truth

Record what the source and authoritative references directly prove:

- geometry, silhouette, openings, thin parts, and detached product parts;
- readable labels, logo marks, packaging construction, and variant identity;
- color, material, transparency, reflection, texture, and shadow evidence;
- missing, blurred, obstructed, contradictory, cropped, or low-confidence details;
- source dimensions, compression, noise, focus, and color-profile limits.

Load [source suitability and fail-closed decisions](references/source-suitability-and-fail-closed.md) when source quality, difficult edges, restoration, reshoot, or recovery claims matter.

### 3. Resolve fidelity locks and authority

Preserve identifying truth by default. A requested edit does not automatically authorize material change.

Load [fidelity locks and transformation authorization](references/fidelity-locks-and-transformations.md) for cleanup, geometry correction, label/logo treatment, restoration, generative completion, recoloring, shadow changes, or any product-truth impact.

Use `decision-provenance` when authority is material, disputed, missing, or superseded.

### 4. Select and load the production profile

Profile selection makes destination-specific rules executable; it does not create a second owner.

For `intended_output.profile: transparent-product-catalog`, load [Transparent Product Catalog Profile](references/transparent-product-catalog.md) before choosing mask, alpha, shadow, crop, normalization, resolution, or export operations.

That profile adds:

- eligibility and unsuitable-source conditions;
- edge-region classification for rigid, irregular, reflective, translucent, soft/fibrous, and mixed subjects;
- truthful opaque, transparent, and partial-alpha semantics;
- clipping, residue, halo, spill, haze, and fringe checks;
- explicit transparent-master and grounded-shadow variants;
- destination- and family-aware canvas, scale, alignment, and padding rules;
- effective-resolution and actual PNG-export requirements;
- `TPC*` profile gates and mapping to independent static visual review.

Other profiles must provide equivalent destination, transformation, evidence, and failure boundaries before production claims are allowed.

### 5. Assess suitability

Return exactly one source status:

```text
SUITABLE
SUITABLE_WITH_LIMITS
UNSUITABLE
NOT_VERIFIED
```

Assessment is destination-specific. A source may support a small marketplace thumbnail but fail a large print, transparent master, difficult dark-background composite, or precise edge requirement.

When a profile defines stricter eligibility states, record both the shared source status and the profile result.

### 6. Classify every operation

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

### 7. Produce an adapter-neutral operation plan

The plan may contain only justified operations, such as:

- non-product dust or background cleanup;
- exposure and white-balance correction within verified product-color constraints;
- restrained noise reduction and sharpening for the declared destination;
- safe perspective correction that preserves geometry;
- region-aware background separation and mask refinement;
- natural-shadow preservation, separation, authorized removal, or controlled regeneration;
- crop, canvas, scale, alignment, and padding normalization;
- destination-aware restoration or upscale with artifact review;
- alpha, color-profile, format, and export preparation.

Provider selection and execution remain outside this skill. `prompt-engineer` may translate the locked plan into provider-specific instructions without becoming the fidelity owner.

### 8. Verify execution evidence

When execution is claimed, require the actual exported artifact and applicable comparison evidence. Inspect at actual delivery size and destination context, not only a reduced preview.

Minimum evidence can include:

- source, authoritative references, and exported artifact;
- product, label/logo, color, and material comparison;
- mask, alpha, edge, clipping, residue, spill, haze, and halo inspection;
- light, dark, checker, neutral, and declared destination-background tests when alpha is used;
- shadow-mode and normalization records;
- effective-resolution and export-integrity checks;
- operation record, provider limitations, and unresolved claims.

Missing exported evidence produces `NOT_VERIFIED`, not PASS.

### 9. Emit Product Asset Master or fail closed

Load [Product Asset Master](references/product-asset-master.md) to construct variants, quality report, limitations, downstream locks, reprocessing conditions, and handoff.

A selected profile maps its variant record, evidence, gates, and limitations into the shared Product Asset Master. A specification-only run may emit `specified_only`; it must not claim that an image was produced or accepted.

## Quality gates

```text
request_and_destination_are_explicit
source_truth_is_inventoried_before_transformation
fidelity_locks_are_explicit_and_authorized
required_unknowns_are_not_silently_filled
source_suitability_is_destination_specific
every_operation_has_purpose_authorization_impact_and_evidence
smallest_safe_operation_set_is_selected
selected_profile_is_loaded_before_profile_sensitive_operations
provider_execution_does_not_absorb_shared_skill_ownership
product_identity_is_preserved_unless_authoritatively_changed
restoration_and_upscale_claims_match_observable_evidence
mask_shadow_crop_and_export_claims_require_actual_artifact_evidence
transparent_profile_edge_regions_use_truthful_alpha_semantics
transparent_profile_normalization_has_no_universal_padding_or_fill_ratio
transparent_profile_ready_claim_requires_exported_png_and_background_tests
specification_only_output_is_not_reported_as_produced
Product_Asset_Master_records_limits_and_downstream_locks
final_acceptance_remains_independent
```

Profile hard gates are additive. A shared gate cannot override a failed `TPC*` hard gate.

## Fail-closed conditions

Stop, limit, or route for a better source when:

- required identifying text, geometry, silhouette, opening, or thin part is absent or unrecoverable;
- sources contradict one another without an authority decision;
- a requested edit materially alters locked product truth;
- generative completion would invent required product detail;
- source or effective resolution cannot support the declared destination;
- reflective, translucent, soft, fibrous, perforated, or mixed edges cannot be separated truthfully;
- the profile requires background or alpha tests that cannot be performed;
- provider limitations prevent checkable fidelity or export claims;
- only a preview exists but a production-ready asset is claimed.

Allowed outcomes:

```text
PROCEED
PROCEED_WITH_LIMITS
REQUEST_BETTER_SOURCE_OR_REFERENCE
ROUTE_FOR_AUTHORITY
BLOCK_UNSAFE_TRANSFORMATION
NEEDS_REPROCESSING
NOT_VERIFIED
```

## Handoff

```yaml
product_image_production_result:
  request_id:
  source_assessment:
  selected_profile:
  profile_result:
  fidelity_lock_record:
  transformation_decisions: []
  operation_plan: []
  execution_status: <not_requested | specified_only | produced | blocked | not_verified>
  product_asset_master: <record or null>
  evidence_refs: []
  limitations: []
  next_route: <provider_adapter | prompt-engineer | master-design | design-visual | design-review | better_source | authority_owner | reprocessing | ready>
```

Downstream design receives only approved variants, preservation locks, allowed/prohibited uses, evidence status, destination constraints, and reprocessing conditions. It does not receive permission to reinterpret product truth.

## Anti-patterns

```text
❌ “Make it more premium” without naming authorized changes.
❌ Rebuilding unreadable label text from model guesses.
❌ Whitening, smoothing, sharpening, or recoloring every source by default.
❌ Treating photorealism or one-click removal as fidelity evidence.
❌ Applying binary alpha to translucent or soft material.
❌ Removing all shadows before deciding the production role.
❌ Baking a generated grounding shadow into every transparent master.
❌ Applying one padding or fill percentage to unrelated product shapes.
❌ Calling a cutout clean without actual-size light/dark/background inspection.
❌ Inferring alpha from a checkerboard screenshot without the PNG.
❌ Reprocessing a verified master for every downstream design.
❌ Letting the producer issue its own final acceptance verdict.
```

## Final guard

```text
□ Request, product identity, output profile, destination, and source references are explicit.
□ Source truth and uncertainty were recorded before edits were planned.
□ Fidelity locks and authority references are explicit.
□ The selected profile was loaded before profile-sensitive decisions.
□ Every material transformation is authorized or blocked.
□ The operation set is minimal and provider-neutral.
□ Unrecoverable details were not invented.
□ Execution claims have actual exported evidence.
□ Profile hard gates and destination tests were applied.
□ Product Asset Master status and limitations are honest.
□ Downstream locks, allowed uses, and reprocessing conditions are recorded.
□ Final visual acceptance is routed independently.
```
