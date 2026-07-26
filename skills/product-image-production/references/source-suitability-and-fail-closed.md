# Source Suitability and Fail-Closed Decisions

Load this reference when source quality, destination fitness, difficult edges, restoration, recovery, or reshoot guidance is material.

## Destination-specific suitability

A source is never suitable in the abstract. Assess it against the declared output profile, size, crop, viewing context, and truth requirements.

```yaml
source_assessment:
  suitability: <suitable | suitable_with_limits | unsuitable | not_verified>
  declared_output_profile:
  destination_context:
    target_channels: []
    required_dimensions: []
    expected_viewing_size:
    required_crop_or_angles: []
    required_alpha: <true | false | conditional>
  source_strengths: []
  source_defects: []
  product_truth_visibility:
    verified_details: []
    uncertain_details: []
    missing_or_obstructed_details: []
  edge_complexity: <rigid | irregular | reflective | translucent | soft | mixed | unknown>
  effective_resolution_status: <sufficient | marginal | insufficient | not_verified>
  correction_risks: []
  required_operations: []
  prohibited_operations: []
  better_source_or_reshoot_required: <true | false | conditional>
  limitations: []
```

## Assessment sequence

### 1. Confirm source identity and provenance

Record whether the source is:

- a direct photograph of the declared product;
- a scan or render with known origin;
- a generated image;
- user-provided but not independently verified;
- unknown or contradictory.

A user-provided source may be accepted as the working source while remaining distinct from independently verified product truth.

### 2. Inspect product-truth visibility

Check whether the source visibly supports:

- full silhouette and distinctive geometry;
- packaging seams, caps, handles, openings, controls, or other functional details;
- required labels, logos, symbols, legal marks, and text;
- product color and material characteristics;
- transparent, reflective, glossy, metallic, fibrous, furry, liquid, or soft-edge regions;
- natural contact shadows and grounding cues;
- all required angles or surfaces for the intended output.

Do not treat inference as visibility.

### 3. Inspect source defects

Classify defects without immediately assuming they should be fixed:

```text
capture defects
  exposure, white balance, focus, motion blur, noise, compression,
  lens distortion, perspective, chromatic aberration, flare

scene defects
  background clutter, occlusion, unwanted support, inconsistent lighting,
  color spill, cast shadow, reflection contamination

product-state observations
  dust, damage, dents, scratches, stains, folds, wrinkles, fingerprints,
  condensation, crumbs, manufacturing variation

information defects
  missing angle, cropped geometry, unreadable text, hidden logo,
  contradictory reference, unknown product variant
```

A visible mark on the product is not automatically a removable defect. It may be permanent product truth, damage requiring explicit authorization, or a state that should be preserved.

### 4. Inspect destination risk

Examples:

- small thumbnail: minor source noise may be acceptable, but logo legibility can still be critical;
- transparent master: edge complexity and occlusion become hard constraints;
- large campaign crop: resolution, texture, reflection, and reconstruction risk increase;
- marketplace listing: platform dimensions, background rules, truthful representation, and label clarity matter;
- compositing: perspective, lighting direction, contact/ambient shadow, and color profile affect downstream readiness.

### 5. Select a suitability result

```text
SUITABLE
  Required product truth is visible and the destination can be met
  using authorized, evidence-preserving operations.

SUITABLE_WITH_LIMITS
  The destination can be met within declared constraints, but bounded
  quality, crop, angle, edge, resolution, or fidelity limitations remain.

UNSUITABLE
  The declared result cannot be produced truthfully or to the required
  destination quality from this source.

NOT_VERIFIED
  Required source, destination, authority, or evidence information is missing.
```

## Fail-closed matrix

| Condition | Default result | Safer route |
|---|---|---|
| Required label is unreadable and no approved reference exists | Block reconstruction | Request better source or authoritative artwork |
| Product geometry is cropped or hidden | Block complete-master claim | Use bounded crop or request another angle/source |
| Source is too small for declared final size | `SUITABLE_WITH_LIMITS` or `UNSUITABLE` | Reduce destination size, reshoot, or conditionally upscale with review |
| Reflective edge merges with background | Conditional | Request controlled source or use specialist masking with explicit limits |
| Translucent product contains background color contamination | Conditional/high risk | Controlled reshoot or destination-specific compositing plan |
| Soft/fibrous edge is compressed or blurred | Limit or block transparent master | Better source with contrast and resolution |
| Permanent product mark may be mistaken for dust | `NOT_VERIFIED` | Resolve authority before removal |
| Multiple references show different packaging variants | Route for authority | Select authoritative variant and record decision |
| Requested color change alters sold product identity | Block by default | Require explicit authorized variant/change scope |
| Only model preview exists | `NOT_VERIFIED` for production | Require exported artifact and actual-size review |

## Restoration and recovery language

Use precise terms:

```text
observable correction
  A source-supported adjustment such as exposure balancing or removing
  background dust without changing product truth.

bounded reconstruction
  A conditional operation supported by authoritative reference evidence.
  It must disclose what was reconstructed and how it was verified.

generative completion
  Model-created content not directly supported by the source.
  It is prohibited for required product identifiers unless explicitly
  authorized and independently verified against authoritative references.

unrecoverable
  The missing detail cannot be faithfully established from available evidence.
```

Never say a missing detail was recovered when it was invented or approximated.

## Better-source guidance

When blocking, provide actionable source requirements rather than a generic refusal:

- higher native resolution and lower compression;
- full product silhouette with safe margin;
- controlled, contrasting background;
- even lighting that preserves material and edges;
- sharp focus on required labels and distinguishing details;
- multiple angles for hidden geometry;
- polarization or reflection control where appropriate;
- authoritative packaging artwork or approved reference variant;
- color reference or calibrated capture when product color is critical.

## Evidence statuses

```text
PASS
  Direct evidence supports the assessment claim.

PARTIAL
  Some evidence exists but a bounded gap remains.

FAIL
  Available evidence contradicts the required condition.

NOT_VERIFIED
  Evidence is unavailable or insufficient.

NOT_APPLICABLE
  The condition does not apply to the declared output.
```

Missing evidence is not zero quality and not automatic failure. It blocks the unsupported claim.

## Guard

```text
□ Suitability is tied to an explicit destination.
□ Product truth and uncertainty are separated.
□ Product-state observations are not automatically removed.
□ Edge complexity is classified.
□ Effective resolution is assessed for final use, not source dimensions alone.
□ Better-source guidance is concrete.
□ Generative completion is never described as recovery.
□ Unsupported production claims remain NOT_VERIFIED.
```
