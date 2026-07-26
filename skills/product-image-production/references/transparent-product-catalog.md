# Transparent Product Catalog Profile

Load this reference when `product-image-production` selects `intended_output.profile: transparent-product-catalog`.

## Purpose

This profile prepares a source-linked product asset with truthful transparency for catalog, marketplace, layout, and commercial-compositing reuse.

A transparent product catalog asset is not merely an image with a removed background. It is a destination-scoped Product Asset Master variant with verified silhouette, alpha semantics, edge fidelity, normalization, effective resolution, and export integrity.

```text
source truth
→ destination-specific eligibility
→ edge-region classification
→ authorized background separation
→ alpha and shadow treatment
→ canvas and scale normalization
→ actual-export verification
→ Product Asset Master variant
```

A plausible cutout preview is insufficient.

## Profile declaration

```yaml
transparent_product_catalog_profile:
  profile_id: transparent-product-catalog
  profile_version: 1.0.0
  source_assessment_ref:
  product_identity_ref:
  fidelity_lock_ref:

  destination:
    channels: []
    final_dimensions: []
    intended_backgrounds: []
    viewing_context:
    minimum_effective_resolution:

  subject_class:
    primary: <rigid_opaque | irregular_opaque | reflective | translucent | soft_fibrous | mixed>
    edge_regions: []
    internal_openings: []
    detached_or_thin_parts: []
    uncertainty_regions: []

  separation_plan:
    method_class: <manual_mask | path_plus_mask | channel_or_luminance | color_decontamination | mixed | adapter_selected>
    protected_regions: []
    partial_alpha_regions: []
    forbidden_reconstruction_regions: []
    provider_constraints: []

  shadow_policy:
    master_mode: <none | preserve | remove | separate>
    grounded_variant: <not_requested | preserve | separate | controlled_regeneration>
    authority_refs: []
    limitations: []

  normalization:
    canvas_dimensions:
    subject_scale_rule:
    alignment_rule:
    padding_rule:
    family_consistency_ref:
    crop_safe_regions: []

  export_contract:
    format: png
    alpha_required: true
    bit_depth:
    color_profile:
    premultiplication_handling:
    compression_policy:
    metadata_policy:

  evidence_requirements: []
  limitations: []
```

The profile does not select a provider or prescribe one editor technique universally.

## Eligibility

Return exactly one profile eligibility status:

```text
ELIGIBLE
ELIGIBLE_WITH_LIMITS
INELIGIBLE
NOT_VERIFIED
```

### `ELIGIBLE`

Use only when the supplied source and references can support all required product truth and edge regions for the declared destination.

Typical evidence:

- the complete silhouette is visible;
- required labels, logos, geometry, material, and color are verifiable;
- critical edges are sufficiently resolved;
- intended output dimensions are declared;
- difficult transparent, reflective, fibrous, or thin regions have enough evidence;
- the requested transformation is authorized.

### `ELIGIBLE_WITH_LIMITS`

Use when a truthful transparent asset can be produced only for bounded uses.

Examples:

- adequate for small marketplace display but not large campaign composition;
- clean on light and neutral backgrounds but not verified on deep black;
- one approved crop and scale only;
- a grounded-shadow variant is unavailable;
- one translucent region remains partial or destination-constrained.

### `INELIGIBLE`

Use when the source cannot support truthful separation or destination readiness.

Examples:

- essential product geometry is cropped outside the frame;
- required edges are motion-blurred beyond reliable separation;
- a translucent product is photographed against an inseparable same-tone background without references;
- a handle, cable, strap, vapor, fine fiber, or perforation is missing or unrecoverable;
- generative reconstruction would be required to complete product truth;
- effective resolution cannot meet the declared destination.

### `NOT_VERIFIED`

Use when required source, authority, destination, or export evidence is absent.

A provider preview without the exported PNG is `NOT_VERIFIED`.

## Edge-region classification

Do not apply one mask rule to an entire product. Classify materially different regions separately.

### Rigid opaque

Examples: box edges, bottle caps, appliances, solid packaging.

Required behavior:

- preserve authoritative geometry;
- avoid stair-stepping, over-feathering, corner rounding, and clipped protrusions;
- keep small functional details and openings;
- use restrained edge transition appropriate to capture focus and final size.

### Irregular opaque

Examples: food, foliage, textured fabric, rough materials, crumbs, perforations.

Required behavior:

- preserve irregular silhouette without artificial smoothing;
- keep meaningful holes, cutouts, crumbs, fibers, and texture boundaries;
- distinguish real detached detail from removable background debris;
- do not simplify the edge merely to look cleaner.

### Reflective

Examples: polished metal, glossy bottles, chrome, mirrors, dark lacquer.

Required behavior:

- separate background reflections from product geometry only when evidence supports it;
- preserve reflections that communicate material and form;
- avoid flattening reflective surfaces into generic gradients;
- record unresolved environment reflections as limitations when they cannot be removed truthfully.

Reflection cleanup does not authorize material redesign.

### Translucent

Examples: clear glass, transparent plastic, liquid, frosted packaging, thin film.

Required behavior:

- preserve partial alpha where the product transmits background light;
- preserve internal refraction, tint, highlights, thickness, and material cues;
- avoid binary cutouts that turn transparent material opaque;
- avoid deleting transparent regions because they resemble background;
- require destination-background testing because appearance is compositing-dependent.

A translucent product cannot receive a universal `ready` verdict without declared background conditions.

### Soft or fibrous

Examples: fur, hair, textile fibers, soft brush edges, steam, powder, mist.

Required behavior:

- preserve meaningful soft transitions and fine structures;
- prevent hard clipping, excessive choking, bright fringe, and background-color contamination;
- separate low-confidence wisps from invented or model-generated replacement detail;
- fail closed when required fine structure is not recoverable.

### Mixed

Most commercial products contain multiple edge classes. Use a region map and apply the correct rule per region.

```yaml
edge_region:
  region_id:
  location:
  class:
  product_truth_role:
  alpha_behavior: <opaque | transparent | partial | mixed | unknown>
  preservation_requirement:
  source_confidence: <high | medium | low | unknown>
  operation_authorization:
  evidence_required: []
  status: <resolved | limited | blocked | not_verified>
```

## Alpha semantics

The alpha channel represents visibility and material transmission, not merely selection confidence.

Required rules:

1. Fully opaque verified product regions remain opaque.
2. Fully removed background regions become transparent.
3. Translucent and soft regions retain justified partial alpha.
4. Internal holes and openings remain open when source truth proves them.
5. Unknown regions are not silently filled, erased, or regenerated.
6. Feather, choke, expand, contract, denoise, and decontamination values are region- and destination-specific.
7. Premultiplied-alpha handling must not create bright or dark fringes.
8. Color decontamination must not recolor the product edge or material.

Prohibited shortcuts:

```text
binary alpha for all product classes
one feather radius for the full subject
one-click background removal accepted without inspection
painting missing detail into alpha to hide uncertainty
flattening transparency against white and calling it transparent
```

## Mask and edge inspection

Inspect the actual exported asset at delivery size and at meaningful zoom for diagnosis.

Required backgrounds:

```text
white
black or deep neutral
mid-gray
checkerboard
at least one declared destination background when compositing is intended
```

Inspect for:

- halo or fringe visible only on light or dark backgrounds;
- jagged, chattering, stair-stepped, or over-smoothed edges;
- missing thin parts, protrusions, holes, handles, cables, fibers, crumbs, steam, or perforations;
- accidental semi-transparent haze or rectangular alpha boxes;
- residual background pixels;
- edge color spill;
- clipped highlights or shadows that belong to product material;
- inconsistent sharpness between product body and edge;
- generative deformation or duplicated detail.

A mask passes only when all required edge classes pass for the declared destinations.

## Clipping and completeness

Before normalization, compare the complete silhouette against source and authoritative references.

Hard failures:

- any required product protrusion touches or crosses the export boundary;
- a handle, lid, cap, foot, cable, strap, label, or distinguishing feature is cut;
- internal openings are filled;
- detached product parts are removed as background;
- a source-cropped region is reconstructed without authoritative evidence;
- alpha removes material highlights or transparent body regions.

When the source itself is cropped, the profile must not infer the missing shape. Request a better source or emit a bounded crop-specific variant.

## Shadow policy

Shadow treatment is explicit and variant-specific.

### Transparent master

Default production role:

```text
product isolated for reuse
no invented advertising environment
no hidden grounding baked in without declaration
```

Allowed shadow modes:

- `none` when no truthful product-attached shadow is required;
- `preserve` when a shadow is part of the captured product presentation and compatible with declared use;
- `remove` when removal is authorized and does not erase product material or contact cues;
- `separate` when a reusable independent shadow component is needed and can be extracted truthfully.

### Transparent grounded variant

A separate optional variant may add or preserve grounding.

Controlled regeneration requires:

- declared destination and perspective;
- product contact geometry;
- light direction and softness constraints;
- separation from the product-truth master;
- explicit record that the shadow is generated or reconstructed;
- destination comparison evidence.

Prohibited behavior:

- adding a dramatic shadow merely to make the product look premium;
- baking a shadow into every transparent master;
- removing glass, reflective highlights, or soft product edges as if they were shadow;
- claiming a generated shadow is captured source truth.

## Canvas, scale, alignment, and padding

Normalization supports repeatable downstream use without imposing arbitrary universal percentages.

### Canvas

Declare canvas dimensions from the destination profile, family system, or explicit downstream contract.

Do not choose a canvas merely because it is common in one marketplace.

### Scale

Scale is based on:

- destination legibility;
- product family consistency;
- shape and aspect ratio;
- required breathing room;
- protrusions and soft regions;
- shadow mode;
- safe crop requirements.

A tall bottle, wide pan, irregular food plate, and cable-based device should not share one fill percentage by default.

### Alignment

Choose and record one alignment rule:

```text
geometric_bounds_center
visual_mass_center
baseline_or_contact_alignment
family_anchor_alignment
custom_destination_alignment
```

Visual centering may differ from geometric centering, but it must remain explainable and repeatable.

### Padding

Padding is derived from destination, subject shape, family consistency, and crop safety.

```yaml
padding_record:
  unit:
  top:
  right:
  bottom:
  left:
  rationale:
  protected_protrusions: []
  shadow_allowance:
  family_consistency_ref:
```

Prohibited behavior:

- universal 5%, 10%, or 15% padding rules;
- edge crowding to maximize product size;
- excess empty space that destroys catalog consistency;
- cropping protrusions to maintain a fixed fill ratio.

## Effective resolution

Resolution is judged at the declared final dimensions and viewing context.

Required checks:

- product detail remains credible at final size;
- labels and required marks remain legible when the destination requires them;
- thin structures and edge transitions survive resampling;
- sharpening does not invent text, texture, or edge detail;
- upscale artifacts do not distort geometry or material;
- destination crops do not exceed verified source coverage.

Large pixel dimensions alone do not prove effective resolution.

A bounded small-size variant may pass while a large campaign variant fails.

## PNG export contract

The actual exported file must be inspected.

Required checks:

```text
file decodes successfully
format is PNG when alpha is required
expected pixel dimensions are correct
alpha channel exists and behaves as declared
no accidental flattened background
no unintended matte color or fringe
bit depth is appropriate for the destination
color profile is declared or intentionally normalized
compression is lossless and file is not corrupted
metadata handling follows product policy
preview and exported file are the same approved version
```

Do not infer alpha from a checkerboard screenshot. Inspect the exported file or a trustworthy alpha-channel representation tied to it.

## Destination readiness

Profile readiness is scoped to named uses.

```yaml
transparent_catalog_variant:
  variant_id:
  profile: transparent-product-catalog
  production_role: <transparent_master | transparent_grounded>
  artifact_ref:
  source_refs: []
  edge_region_refs: []
  dimensions:
  alpha_status: <pass | fail | partial | not_verified>
  shadow_status: <none | preserved | removed | separated | regenerated | not_verified>
  normalization_record:
  effective_resolution_status: <pass | fail | partial | not_verified>
  export_integrity_status: <pass | fail | partial | not_verified>
  intended_channels: []
  intended_backgrounds: []
  limitations: []
  status: <produced | specified_only | blocked | not_verified>
```

Map the variant into `product_asset_master.variants[]`. Add its evidence and limitations to the shared quality report and downstream handoff.

## Evidence bundle

A produced profile requires:

```yaml
transparent_profile_evidence:
  source_refs: []
  authoritative_reference_refs: []
  exported_png_ref:
  alpha_channel_evidence_ref:
  source_export_comparison_refs: []
  edge_region_inspection_refs: []
  light_background_test_ref:
  dark_background_test_ref:
  checker_background_test_ref:
  destination_background_test_refs: []
  clipping_and_completeness_ref:
  normalization_ref:
  effective_resolution_ref:
  export_integrity_ref:
  reviewer_result_refs: []
```

Screenshots support review but do not replace the exported PNG.

## Profile gates

```text
TPC1 profile destination and eligibility are explicit
TPC2 complete product silhouette and required internal openings are preserved
TPC3 edge regions are classified before mask treatment
TPC4 opaque, translucent, reflective, soft, and mixed regions use truthful alpha semantics
TPC5 no required detail is invented, erased, or reconstructed without authority
TPC6 halo, fringe, spill, residue, haze, and matte contamination are absent at declared backgrounds
TPC7 thin parts, protrusions, holes, and detached product details are not clipped
TPC8 shadow mode is explicit, evidence-backed, and variant-specific
TPC9 canvas, scale, alignment, and padding are destination- and family-aware
TPC10 effective resolution passes for each declared destination
TPC11 exported PNG alpha, color, dimensions, readability, and integrity are verified
TPC12 Product Asset Master records uses, limits, evidence, and reprocessing conditions
TPC13 independent review remains required for final acceptance
```

`TPC2`, `TPC4`, `TPC5`, `TPC7`, `TPC10`, and `TPC11` are hard gates for a `ready` transparent catalog variant.

## Design-review mapping

The producer reports profile evidence. Independent acceptance maps applicable findings through `design-review`:

```text
SV9  Product Fidelity
SV12 Crop Safety
SV15 Subject Separation
SV17 Resolution
SV18 Edge and Mask Quality
SV19 Lighting and Perspective when a grounded variant is used
SV20 Compression and Color
SV21 Generative Artifact Control when generative operations are involved
```

A producer-side TPC result does not replace the reviewer verdict.

## PASS example

```text
Rigid opaque bottle; full silhouette and sharp packaging are supplied.
Destination: 1200×1200 marketplace and layout reuse.
Background removal is authorized.
The exported PNG preserves exact geometry, logo, label, color, cap, embossing,
and internal handle opening. Alpha passes white, black, gray, checker, and
approved destination-background tests. No clipping, halo, spill, or residue is
found. Effective resolution and export integrity pass.

Profile result: ready for the declared destinations, pending independent review.
```

## PASS WITH LIMITS example

```text
Transparent glass bottle passes on white, light neutral, and declared warm-beige
backgrounds. Deep-black compositing exposes unresolved edge contamination.

Profile result: ready_with_limits for declared light backgrounds; prohibited on
deep-dark backgrounds until reprocessed and re-reviewed.
```

## FAIL examples

```text
FAIL: binary cutout makes a clear bottle fully opaque.
FAIL: white fringe is invisible on the editor checker but visible on black.
FAIL: a pan handle is clipped to maintain a fixed 90% fill ratio.
FAIL: fine food crumbs are removed as noise without product-truth classification.
FAIL: one universal 10% padding rule is applied across unrelated product shapes.
FAIL: a checkerboard screenshot is presented without the exported PNG.
FAIL: generated label detail is used to hide motion blur.
```

## Fail-closed routes

```text
missing required silhouette or edge truth
→ REQUEST_BETTER_SOURCE_OR_REFERENCE

material transformation would be required
→ ROUTE_FOR_AUTHORITY or BLOCK_UNSAFE_TRANSFORMATION

source supports only bounded destination
→ PROCEED_WITH_LIMITS

exported PNG or alpha evidence missing
→ NOT_VERIFIED

profile hard gate fails
→ BLOCKED or NEEDS_REPROCESSING
```

## Guard

```text
□ Profile eligibility is destination-specific.
□ All material edge regions are classified.
□ Transparent and soft regions preserve justified partial alpha.
□ Internal openings, thin parts, protrusions, and detached details remain intact.
□ Alpha is tested on light, dark, neutral, checker, and declared destination backgrounds.
□ Shadow treatment is explicit and variant-specific.
□ Canvas, scale, alignment, and padding have a repeatable rationale.
□ Effective resolution is verified at final size.
□ The actual exported PNG and alpha behavior are inspected.
□ Product Asset Master records evidence, limitations, and approved uses.
□ Final acceptance is independent.
```
