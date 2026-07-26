# Product Asset Master

Load this reference when a Product Image Production run must emit, verify, or hand off a reusable product asset.

## Purpose

A Product Asset Master is not merely a final PNG. It is a source-linked production record that keeps product truth, transformations, variants, quality evidence, limitations, and downstream use constraints together.

```text
raw source
→ assessed source
→ locked product truth
→ authorized operation record
→ exported variant(s)
→ quality report
→ controlled downstream handoff
```

This prevents each flyer, banner, marketplace image, or campaign creative from reinterpreting or reprocessing the raw source independently.

## Master contract

```yaml
product_asset_master:
  master_id: <stable identifier>
  product_identity:
    declared_identity:
    authoritative_refs: []
    variant_status: <resolved | conflicted | unknown>

  source_refs: []
  source_assessment_ref:

  fidelity_lock_record:
    applied_locks: []
    authorized_exceptions: []
    unresolved_truth_risks: []

  operation_record:
    planned_operations: []
    executed_operations: []
    skipped_operations: []
    prohibited_operations: []
    provider_adapter_ref: <ref or null>
    provider_limitations: []
    execution_evidence_refs: []

  variants:
    - variant_id:
      profile:
      artifact_ref: <exported artifact or null>
      dimensions:
      effective_resolution_status: <pass | fail | partial | not_verified | not_applicable>
      alpha_status: <present | absent | partial | not_verified | not_applicable>
      shadow_status: <preserved | removed | separated | regenerated | absent | not_verified | not_applicable>
      crop_and_padding_record:
      color_profile:
      export_format:
      compression_record:
      intended_channels: []
      status: <produced | specified_only | blocked | not_verified>

  quality_report:
    product_fidelity: <pass | fail | partial | not_verified | not_applicable>
    label_and_logo_fidelity: <pass | fail | partial | not_verified | not_applicable>
    color_and_material_fidelity: <pass | fail | partial | not_verified | not_applicable>
    mask_and_edge_quality: <pass | fail | partial | not_verified | not_applicable>
    clipping_and_residue: <pass | fail | partial | not_verified | not_applicable>
    shadow_and_grounding: <pass | fail | partial | not_verified | not_applicable>
    effective_resolution: <pass | fail | partial | not_verified | not_applicable>
    export_integrity: <pass | fail | partial | not_verified | not_applicable>
    compositing_readiness: <pass | fail | partial | not_verified | not_applicable>
    evidence_refs: []
    limitations: []

  downstream_handoff:
    approved_variant_ids: []
    allowed_uses: []
    prohibited_uses: []
    preservation_locks: []
    required_review_gates: []
    destination_constraints: []
    reprocessing_conditions: []
    next_owner:

  status: <ready | ready_with_limits | blocked | specified_only | not_verified>
```

## Master states

### `specified_only`

A plan and schema exist, but no binary asset has been produced.

Allowed claims:

- source assessment completed;
- operations planned;
- locks and destination requirements defined.

Prohibited claims:

- asset produced;
- mask clean;
- color faithful;
- export valid;
- ready for production.

### `not_verified`

An artifact or claim exists but required evidence is missing.

Examples:

- provider preview exists but exported file is absent;
- alpha cannot be inspected;
- source reference is missing;
- target resolution is unknown;
- label comparison cannot be performed.

### `blocked`

A hard condition prevents a truthful or destination-ready asset.

Examples:

- required product detail is unrecoverable;
- requested transformation violates a lock;
- source resolution cannot support the declared use;
- variant authority is conflicted;
- provider output materially changes product identity.

### `ready_with_limits`

All blocking conditions are resolved, but bounded limitations remain and are acceptable for named uses.

Examples:

- suitable for small marketplace display but not large print;
- suitable on light backgrounds but edge contamination remains on dark backgrounds;
- one approved crop only;
- shadow-separated variant not available.

### `ready`

All required gates for the declared variant and destination have evidence-backed PASS or valid NOT_APPLICABLE status, and no blocking limitation remains.

`ready` is destination-scoped, not universal.

## Variant design

A master may contain several variants, but each must have one production role.

Common roles:

```text
transparent master
  product isolated with alpha, without an invented advertising scene

transparent grounded
  transparent product with a controlled grounding/contact-shadow treatment

clean white catalog
  destination-compliant white background and normalized presentation

neutral studio
  restrained neutral environment suitable for approved catalog or composition use

custom destination variant
  named channel/profile with explicit dimensions, background, crop, and constraints
```

Do not create variants only for visual novelty.

## Quality-report rules

### Product fidelity

Compare source/reference evidence against the exported variant for:

- silhouette and geometry;
- packaging construction;
- functional parts;
- distinguishing details;
- product variant identity.

### Label and logo fidelity

Inspect:

- exact visible text and symbol shape;
- letterform integrity;
- placement and proportions;
- no invented, replaced, or corrupted marks;
- no sharpening or upscale artifacts that create false text.

### Color and material fidelity

Inspect:

- product color relationships;
- highlight and shadow behavior;
- transparency, reflectivity, gloss, matte, metallic, fabric, food, liquid, or textured cues;
- profile/conversion uncertainty;
- no generic beautification that changes the sold-product appearance.

### Mask and edge quality

Inspect at actual size and against relevant light/dark/checker backgrounds:

- authoritative silhouette;
- thin structures and holes;
- reflective/translucent/soft/fibrous regions;
- hair, fibers, straps, handles, steam, crumbs, or perforations where applicable;
- no stair-stepping, chatter, hard cut, fringe, halo, color spill, missing edge, or background residue.

### Clipping and residue

Check:

- no cropped product protrusions;
- no accidental cut through shadow/handle/cap/detail;
- no hidden background fragments;
- no alpha values producing unintended boxes or haze.

### Shadow and grounding

Check whether the declared shadow mode was implemented truthfully and consistently with the intended use.

### Effective resolution

Judge resolution at final dimensions and intended viewing distance. Source pixel dimensions alone do not prove effective resolution.

### Export integrity

Verify the actual export:

- correct format;
- dimensions;
- alpha behavior;
- color profile;
- compression;
- file readability;
- no flattened background when alpha is required;
- no unintended metadata or conversion damage when applicable.

### Compositing readiness

Verify that the asset can enter downstream design without forcing hidden reprocessing or violating perspective, light, edge, color, crop, or preservation locks.

## Evidence bundle

A production-ready master should reference:

```yaml
evidence_bundle:
  source_refs: []
  authoritative_reference_refs: []
  exported_artifact_refs: []
  source_export_comparisons: []
  actual_size_edge_inspection_refs: []
  destination_preview_refs: []
  operation_record_ref:
  provider_limitations_ref:
  reviewer_result_refs: []
```

Screenshots can support evidence but do not replace the exported artifact.

## Downstream handoff

The receiving design or compositing owner gets:

- approved variant IDs;
- exact artifact references;
- allowed and prohibited uses;
- active preservation locks;
- destination constraints;
- required review gates;
- known limitations;
- conditions that require returning to Product Image Production.

The handoff does not grant permission to:

- edit labels or logos;
- alter product geometry;
- recolor the product;
- regenerate difficult edges;
- replace the asset with a plausible model-created product;
- claim broader destination readiness than the master records.

## Reprocessing conditions

Return to Product Image Production when:

- the destination needs materially larger size or a different crop/angle;
- the background exposes edge problems not covered by the approved use;
- a different shadow mode is required;
- product variant or packaging changes;
- authoritative references change;
- a downstream edit touches preservation locks;
- provider export or color conversion damages fidelity;
- the existing master is only `ready_with_limits` for another destination.

## Acceptance boundary

The producer assembles the master and evidence. Final visual acceptance remains with `design-review` and any applicable domain reviewer.

```text
producer report
≠ independent acceptance

exported evidence + applicable gates + independent verdict
→ accepted for the declared destination
```

## Guard

```text
□ The master has a stable identity and source chain.
□ Product variant authority is explicit.
□ Operations and provider limitations are recorded.
□ Every produced variant references the actual export.
□ Specification-only variants do not claim production.
□ Quality statuses preserve PASS, FAIL, PARTIAL, NOT_VERIFIED, and NOT_APPLICABLE.
□ `ready` is scoped to declared destinations.
□ Downstream uses and preservation locks are explicit.
□ Reprocessing conditions are explicit.
□ Final acceptance remains independent.
```
