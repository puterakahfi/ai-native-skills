---
name: commercial-creative-production
description: Govern net-new commercial static visual production from brief and raw or prepared assets through truthful asset preparation, commercial direction, provider execution, independent review, destination delivery, and bounded return routes.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: workflow
  ai-native-skills.requires: "workflow-router role-switcher decision-provenance product-image-production master-design design-visual prompt-engineer design-review skill-evolution skill-eval"
  ai-native-skills.related_skills: '["design-audit","design-refinement","redesign-workflow","copywriting","content-strategy","composition","design-brand","design-color","design-typography"]'
  ai-native-skills.boundary.covers: '["net_new_commercial_static_visual_production","brief_and_required_content_intake","source_asset_inventory_and_preparation_decision","product_asset_master_verification","commercial_direction_and_composition_handoff","provider_execution_handoff","exported_artifact_review","destination_scoped_delivery","defect_ownership_and_return_routing"]'
  ai-native-skills.boundary.delegates: '["single_product_asset_preparation_without_commercial_composition","audit_only_existing_artifact_review","known_narrow_existing_artifact_refinement","broad_existing_artifact_redesign","provider_specific_prompt_syntax","binary_provider_execution","product_repository_storage_ui_and_provider_configuration","legal_and_regulated_claim_approval"]'
---

# Commercial Creative Production

Own the ordered lifecycle for a **new commercial static visual** such as a catalog image, marketplace creative, flyer, poster, banner, social advertisement, campaign key visual, or related channel asset.

This workflow prevents a polished design from being built on an unverified raw source. It coordinates existing owners; it does not absorb their expertise.

## Core rule

```text
route and classify
→ lock brief, content, destination, and authority
→ inventory source assets
→ prepare required assets or verify reusable masters
→ block raw-source bypass
→ lock commercial direction
→ execute through selected adapters
→ inspect actual exports
→ independent static-visual review
→ deliver for declared channels
→ route defects to their causal owner
→ run learning review when a reusable verified fix occurred
```

A plausible preview is not a delivered commercial asset.

## When to use

Use this workflow when all are true:

- the requested artifact is net-new commercial static visual production;
- the result requires coordinated brief, asset, design, execution, and review stages;
- at least one exported or rendered deliverable is expected;
- the request is broader than preparing one standalone product asset.

Representative requests:

```text
Create a new Instagram product ad from these raw bottle photos.
Produce a marketplace catalog set and promotional banner.
Build a flyer from the approved Product Asset Master and supplied prices.
Create a campaign key visual using verified product and brand assets.
```

## Route elsewhere

```text
prepare one product photo, cutout, transparent master, retouch, restoration
→ product-image-production

prompt generation or provider-specific edit instructions only
→ prompt-engineer

existing artifact audit with no changes
→ design-audit

known narrow defect with accepted direction
→ design-refinement + causal specialist

broad change to an existing poster, campaign, or static artifact
→ redesign-workflow

acceptance review only
→ design-review + built-in static-visual strategy

product feature that adds a commercial-creative engine or UI
→ new-feature-workflow; this workflow may be an executable domain overlay
```

The artifact noun does not override lifecycle. “Banner” can be new production, redesign, refinement, or audit.

## Ownership

### Workflow ownership

`commercial-creative-production` owns:

- lifecycle state and phase order;
- brief, content, destination, and source-asset completeness gates;
- the decision to prepare, reuse, limit, or block each source asset;
- handoff integrity between asset, design, provider, and review owners;
- prevention of raw-source bypass;
- evidence-state preservation;
- destination-scoped delivery and return routes.

### Role composition

```yaml
commercial_creative_roles:
  lifecycle: commercial-creative-production
  design_owner: master-design
  required_specialists:
    - design-visual
  conditional_specialists:
    - product-image-production
    - prompt-engineer
    - copywriting
    - content-strategy
    - composition
    - design-brand
    - design-color
    - design-typography
  implementation_or_execution_owner: <product/provider adapter or repository owner>
  reviewer_facade: design-review
  domain_reviewer: built-in static-visual strategy
```

Role rules:

1. `master-design` owns final commercial direction and synthesis.
2. `product-image-production` owns source suitability, product truth, transformations, and Product Asset Master status.
3. `design-visual` owns visual direction decisions within the accepted brief and asset locks.
4. `prompt-engineer` translates locked plans into provider syntax; it does not own fidelity, lifecycle, or acceptance.
5. Product/runtime adapters own provider selection and binary execution.
6. `design-review` owns gate applicability, evidence normalization, score, verdict, and report.
7. Producer evidence and reviewer evidence remain distinct.

## Required input

```yaml
commercial_creative_production_input:
  request_id: <stable identifier>
  intent:
    artifact_types: []
    target_channels: []
    output_dimensions: []
    production_mode: <specification_only | execute | review_existing_export>

  brief:
    objective: <required>
    audience: <required or unresolved>
    primary_message: <required or unresolved>
    required_content: []
    prohibited_claims: []
    call_to_action: <value or null>
    tone_and_direction_constraints: []

  authority:
    decision_sources: []
    approved_brand_rules: []
    approved_content_sources: []
    inferred_constraints: []
    unverified_claims: []

  source_assets:
    - asset_ref: <required>
      role: <product | logo | brand | talent | background | illustration | other>
      status: <raw | verified_master | approved_asset | unknown>
      provenance: <verified | user_provided | unknown>
      intended_uses: []

  product_asset_masters: []
  preservation_locks: []
  provider_context:
    execution_requested: <true | false>
    available_adapters: []
    selected_adapter: <ref or null>
    limitations: []

  delivery_constraints:
    formats: []
    dimensions: []
    safe_areas: []
    minimum_effective_resolution: <declared or unresolved>
    color_and_compression_constraints: []
    channel_policies: []
```

Unresolved required content, destination, product identity, authority, or delivery constraints remain explicit. Do not fill them with model guesses.

## Lifecycle states

```text
ROUTED
INTAKE_READY
ASSET_REVIEW
ASSET_BLOCKED
ASSET_READY
DIRECTION_LOCKED
PRODUCTION_READY
PRODUCED
REVIEW_BLOCKED
ACCEPTED
DELIVERED
NOT_VERIFIED
```

State transitions require observable evidence. A role name, prompt, or reduced preview is not evidence that a later state was reached.

## Canonical flow

### 0. Route

Classify:

```text
new commercial production | standalone asset preparation | prompt-only |
audit | targeted refinement | redesign | acceptance-only | product feature
```

Stop before execution when the lifecycle is ambiguous.

### 1. Compose roles

Use `role-switcher` to declare one design owner, narrow specialists, execution owner, reviewer facade, and built-in static domain strategy.

Every activated role receives one distinct expected output and evidence status.

### 2. Intake and authority

Verify:

- objective and audience;
- required content and factual sources;
- target channels, ratios, and exports;
- brand and product preservation locks;
- approval and transformation authority;
- explicit exclusions and unsupported claims.

Missing critical facts produce `INTAKE_BLOCKED` or `NOT_VERIFIED`, not invented copy.

### 3. Asset inventory

Classify each source:

```text
VERIFIED_REUSABLE_MASTER
APPROVED_ASSET
RAW_REQUIRES_ASSESSMENT
UNSUITABLE
CONFLICTED
NOT_VERIFIED
```

For product imagery:

- load `product-image-production` when a raw image needs diagnosis, retouching, separation, normalization, restoration, upscale, shadow treatment, or Product Asset Master creation;
- reuse an approved Product Asset Master without reprocessing when the destination is within its allowed uses;
- return to Product Image Production when crop, size, background, variant, edge, or shadow requirements exceed the approved master.

### 4. Asset readiness gate

```yaml
asset_readiness_gate:
  source_inventory_complete: <true | false | unknown>
  required_product_asset_master_status: <ready | ready_with_limits | blocked | specified_only | not_verified | not_applicable>
  approved_variant_ids: []
  destination_covered: <true | false | partial | unknown>
  preservation_locks_loaded: <true | false>
  raw_source_bypass_detected: <true | false>
  unresolved_asset_risks: []
  result: <PASS | FAIL | PARTIAL | NOT_VERIFIED>
```

Hard rule:

```text
raw or unverified product source + preparation required
≠ valid handoff to final commercial composition
```

`PASS` requires an approved variant or a justified `NOT_APPLICABLE` product-image path.

### 5. Commercial direction

`master-design` synthesizes:

- message hierarchy;
- composition and attention flow;
- relationship between copy, product, logo, and supporting assets;
- visual language appropriate to audience, brand, and channel;
- variants required by destination;
- design preservation locks and prohibited reinterpretations.

`design-visual` and selected specialists contribute bounded decisions. They may not edit locked product truth or broaden asset readiness.

### 6. Provider handoff

```yaml
provider_execution_handoff:
  locked_brief_ref:
  approved_asset_refs: []
  approved_product_variant_ids: []
  preservation_locks: []
  operation_or_design_plan_ref:
  provider_specific_translation_owner: <prompt-engineer or adapter>
  binary_execution_owner: <adapter or repository owner>
  requested_exports: []
  prohibited_transformations: []
  required_evidence: []
  provider_limitations: []
```

Shared workflow logic never embeds volatile provider recipes as canonical rules.

### 7. Production

The execution owner produces only within the locked brief, approved assets, destination constraints, and provider handoff.

A specification-only run may produce a production specification but must retain `specified_only` or `NOT_VERIFIED` artifact status.

### 8. Export evidence

When production is claimed, require:

- actual exported artifact references;
- declared dimensions and format;
- destination previews at relevant size;
- source/master-to-export fidelity comparison;
- required content accuracy evidence;
- effective-resolution and export-integrity checks;
- provider limitations and operation record.

Screenshots may support evidence but do not replace export files.

### 9. Independent review

Route through `design-review` using the built-in static-visual strategy and applicable gates, including:

```text
SV5  actual-size legibility
SV8  brand fidelity
SV9  product fidelity
SV11 content accuracy
SV12 crop safety
SV13 safe areas and overlays
SV15 subject separation
SV17 effective resolution
SV18 edge and mask quality
SV19 lighting and perspective
SV20 compression and color
SV21 generative artifact control
```

Applicable fidelity, content, crop, and resolution failures block commercial delivery. The producer cannot issue its own final PASS.

### 10. Defect classification and return routing

```yaml
commercial_creative_defect:
  defect_id:
  evidence_ref:
  defect_class: <brief | content | product_asset | commercial_design | provider_execution | export | review_coverage | authority>
  causal_owner:
  correction_owner:
  preservation_scope: []
  return_route:
  status: <OPEN | BLOCKED | CORRECTED | NOT_VERIFIED>
```

Return map:

```text
wrong/missing product truth, mask, edge, asset resolution
→ product-image-production

provider syntax or translation defect
→ prompt-engineer

provider execution/export defect with correct locked plan
→ product/runtime adapter

message, hierarchy, composition, type, color, integration defect
→ master-design + relevant design specialists

wrong price, claim, date, or required content
→ authoritative content owner; then design owner

missing review evidence or wrong gate coverage
→ design-review

conflicted authority or superseded decision
→ decision-provenance + governing owner
```

Do not restart every phase when the defect is narrow and upstream locks remain valid.

### 11. Delivery

```yaml
commercial_creative_delivery:
  request_id:
  accepted_artifact_refs: []
  declared_channels: []
  final_dimensions: []
  asset_master_refs: []
  preservation_locks: []
  reviewer_report_refs: []
  limitations: []
  prohibited_uses: []
  reprocessing_conditions: []
  status: <DELIVERED | DELIVERED_WITH_LIMITS | BLOCKED | NOT_VERIFIED>
```

Delivery readiness is destination-scoped, never universal.

### 12. Learning review

A verified reusable correction may route to `skill-evolution` with regression evidence. Product-only exceptions, provider quirks without stable obligation, and unverified workarounds remain local.

## Quality gates

```text
lifecycle_is_classified_before_execution
net_new_commercial_production_routes_to_this_workflow
standalone_asset_prompt_audit_refinement_and_redesign_boundaries_are_preserved
exactly_one_design_owner_is_explicit
specialists_have_narrow_outputs_and_evidence_states
brief_content_destination_and_authority_are_locked_before_production
source_assets_are_inventoried_before_composition
raw_product_source_does_not_bypass_required_product_image_production
Product_Asset_Master_destination_and_variant_are_verified_before_handoff
prepared_master_is_not_reprocessed_without_a_valid_condition
prompt_engineer_translates_but_does_not_own_fidelity_or_lifecycle
provider_execution_remains_adapter_owned
commercial_direction_does_not_reinterpret_product_truth
production_claims_require_actual_export_evidence
review_is_independent_and_uses_static_visual_gates
failure_states_preserve_FAIL_PARTIAL_NOT_VERIFIED_and_NOT_APPLICABLE
causal_defect_owner_is_identified_before_fix
final_delivery_is_destination_scoped
verified_reusable_fixes_receive_learning_review
```

## Fail-closed conditions

Block or limit production when:

- required brief or content facts are unresolved;
- product identity or variant is conflicted;
- a raw product source requires preparation but no Product Asset Master is available;
- the approved master does not cover the destination;
- a requested transformation violates preservation locks;
- provider limitations prevent checkable fidelity or export evidence;
- only a preview exists but delivery is claimed;
- required reviewer coverage or evidence is absent;
- a hard static-visual gate fails.

Allowed non-pass outcomes:

```text
REQUEST_MISSING_BRIEF_OR_CONTENT
REQUEST_BETTER_SOURCE_OR_REFERENCE
RETURN_TO_PRODUCT_IMAGE_PRODUCTION
ROUTE_FOR_AUTHORITY
BLOCK_UNSAFE_TRANSFORMATION
RETURN_TO_DESIGN_OWNER
RETURN_TO_PROVIDER_ADAPTER
LIMITED_REVIEW
NOT_VERIFIED
```

## Anti-patterns

```text
❌ Send raw product photos straight into final ad composition.
❌ Let prompt-engineer decide logo, packaging, product color, or material changes.
❌ Reprocess a verified Product Asset Master for every new banner.
❌ Treat a model preview as exported evidence.
❌ Use “make it premium” as transformation authority.
❌ Merge asset, design, execution, and acceptance ownership into one role.
❌ Route an existing broad redesign into net-new production merely because it is an ad.
❌ Route a known halo or copy defect into a full redesign.
❌ Normalize missing evidence into PASS.
❌ Claim readiness for channels outside the reviewed destination.
```

## Final guard

```text
□ One primary lifecycle is explicit.
□ One design owner and narrow specialists are explicit.
□ Brief, content, channels, authority, and locks are recorded.
□ Every required source has an evidence-backed readiness state.
□ Raw-source bypass is absent.
□ Approved Product Asset Master variants cover the destination.
□ Provider translation and binary execution ownership are explicit.
□ Actual exports and destination previews exist when production is claimed.
□ Static-visual review is independent and evidence-backed.
□ Defects return to causal owners without breaking valid locks.
□ Delivery status and limitations are honest and destination-scoped.
□ Reusable verified lessons receive learning review.
```
