---
name: commercial-creative-production
description: Govern net-new commercial static visual production from authorized brief and raw or prepared assets through truthful asset preparation, claim-locked provider execution, independent review, destination delivery, and bounded return routes.
license: MIT
metadata:
  ai-native-skills.version: 1.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: workflow
  ai-native-skills.requires: "workflow-router role-switcher decision-provenance product-image-production master-design design-visual prompt-engineer design-review skill-evolution skill-eval"
  ai-native-skills.related_skills: '["design-audit","design-refinement","redesign-workflow","copywriting","content-strategy","composition","design-brand","design-color","design-typography"]'
  ai-native-skills.boundary.covers: '["net_new_commercial_static_visual_production","brief_and_required_content_intake","authorized_content_ledger","source_asset_inventory_and_preparation_decision","product_asset_master_verification","commercial_direction_and_composition_handoff","provider_execution_handoff","post_provider_claim_and_fidelity_comparison","exported_artifact_review","destination_scoped_delivery","defect_ownership_and_return_routing"]'
  ai-native-skills.boundary.delegates: '["single_product_asset_preparation_without_commercial_composition","audit_only_existing_artifact_review","known_narrow_existing_artifact_refinement","broad_existing_artifact_redesign","provider_specific_prompt_syntax","binary_provider_execution","product_repository_storage_ui_and_provider_configuration","legal_and_regulated_claim_approval"]'
---

# Commercial Creative Production

Own the ordered lifecycle for a **new commercial static visual** such as a catalog image, marketplace creative, flyer, poster, banner, social advertisement, campaign key visual, or related channel asset.

This workflow prevents a polished artifact from being built on an unverified raw source or unsupported commercial content. It coordinates existing owners; it does not absorb their expertise.

## Core rule

```text
route and classify
→ lock brief, content, destination, and authority
→ build an exact authorized-content ledger
→ inventory source assets
→ prepare required assets or verify reusable masters
→ block raw-source bypass
→ lock commercial direction
→ translate only the locked plan and ledger to the provider
→ execute through the selected adapter
→ compare actual output with source, locks, and ledger
→ independent static-visual review
→ deliver only when hard gates pass
→ route defects to their causal owner
→ run learning review when a reusable verified fix occurred
```

A plausible preview is not a delivered commercial asset. Visual polish cannot compensate for invented claims, altered product truth, unsupported marks, or missing evidence.

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
Build a flyer from an approved Product Asset Master and supplied prices.
Create a campaign key visual using verified product and brand assets.
```

## Route elsewhere

```text
prepare one product photo, cutout, transparent master, retouch, restoration
→ product-image-production

provider-specific prompt translation only
→ prompt-engineer

existing artifact audit with no changes
→ design-audit

known narrow defect with accepted direction
→ design-refinement + causal specialist

broad change to an existing commercial artifact
→ redesign-workflow

acceptance review only
→ design-review + built-in static-visual strategy

product feature that adds a creative engine or UI
→ new-feature-workflow + this workflow as a domain overlay
```

The artifact noun does not override lifecycle. A banner may be new production, redesign, refinement, or audit.

## Ownership

### Workflow ownership

`commercial-creative-production` owns:

- lifecycle state and phase order;
- brief, content, destination, and source-asset completeness gates;
- the authorized-content ledger and unknown-content policy;
- the decision to prepare, reuse, limit, or block each source asset;
- handoff integrity between asset, design, provider, and review owners;
- prevention of raw-source and unsupported-content bypass;
- evidence-state preservation;
- post-provider claim, mark, text, and product comparison;
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
  authority_owners:
    - <brand/content/product/legal owner when applicable>
```

Role rules:

1. `master-design` owns final commercial direction and synthesis.
2. `product-image-production` owns source suitability, product truth, transformations, and Product Asset Master status.
3. `design-visual` owns bounded visual direction under the accepted brief and locks.
4. `prompt-engineer` translates the locked plan, ledger, and preservation constraints into provider syntax. It does not own claims, fidelity, lifecycle, or acceptance.
5. Product/runtime adapters own provider selection, binary execution, and export evidence.
6. `design-review` owns gate applicability, evidence normalization, score, verdict, and report.
7. Producer evidence and reviewer evidence remain distinct.
8. Authority owners decide whether facts, claims, specifications, prices, contacts, legal text, and marks are approved.

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
    call_to_action: <authorized value or null>
    tone_and_direction_constraints: []

  authority:
    decision_sources: []
    approved_brand_rules: []
    approved_content_sources: []
    inferred_constraints: []
    unverified_claims: []

  authorized_content_ledger:
    ledger_id: <required before provider execution>
    authority_refs: []
    unknown_content_policy: prohibit
    authorized_items:
      - content_id: <stable identifier>
        kind: <rendered_text | factual_claim | specification | price | contact | legal_text | brand_mark>
        value: <exact authorized value>
        authority_ref: <required>
        render_policy: <required | allowed | metadata_only>
    prohibited_items: []
    unresolved_items: []

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

Missing destination, product identity, authority, or required content remains unresolved. Unknown commercial content defaults to `prohibit`; it is never creative-completion space.

Load [Authorized Content and Provider Handoff](references/authorized-content-and-provider-handoff.md) before any provider translation or binary execution.

## Lifecycle states

```text
ROUTED
INTAKE_BLOCKED
INTAKE_READY
ASSET_REVIEW
ASSET_BLOCKED
ASSET_READY
DIRECTION_LOCKED
PRODUCTION_READY
PRODUCED
COMPARISON_BLOCKED
REVIEW_BLOCKED
ACCEPTED
DELIVERED
NOT_VERIFIED
```

State transitions require observable evidence. A role name, prompt, plausible preview, or producer approval is not evidence that a later state was reached.

## Canonical flow

### 0. Route

Classify exactly one primary lifecycle:

```text
new commercial production | standalone asset preparation | prompt-only |
audit | targeted refinement | redesign | acceptance-only | product feature
```

Stop before execution when lifecycle is ambiguous.

### 1. Compose roles

Use `role-switcher` to declare one design owner, narrow specialists, execution owner, reviewer facade, domain reviewer, and authority owners.

Every activated role receives one distinct expected output and evidence status.

### 2. Intake, authority, and claim lock

Verify:

- objective and audience;
- required content and factual sources;
- target channels, ratios, and exports;
- brand and product preservation locks;
- approval and transformation authority;
- explicit exclusions and unsupported claims.

Build the authorized-content ledger before direction lock or provider translation.

The ledger must:

- use exact values, not broad topics;
- classify names, claims, specifications, prices, contacts, legal text, and brand marks;
- link each authorized item to an authority reference;
- mark items `required`, `allowed`, or `metadata_only`;
- place unresolved content outside the renderable set;
- use `unknown_content_policy: prohibit`.

A style request such as “premium”, “bold”, “luxury”, or “high-converting” authorizes visual direction only. It does not authorize factual claims, benefits, ingredients, fragrance notes, quality assertions, awards, prices, logos, badges, or specifications.

Missing critical facts produce `INTAKE_BLOCKED` or `NOT_VERIFIED`, not invented copy.

### 3. Asset inventory

Classify every source:

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
- reuse an approved Product Asset Master without reprocessing when its destination is covered;
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

- message hierarchy and attention flow;
- relationship between authorized copy, product, approved marks, and supporting assets;
- visual language appropriate to audience, brand, and channel;
- destination variants;
- design preservation locks and prohibited reinterpretations.

`design-visual` and selected specialists contribute bounded decisions. They may not broaden the authorized-content ledger or reinterpret locked product truth.

### 6. Provider handoff

```yaml
provider_execution_handoff:
  handoff_id: <stable identifier>
  locked_brief_ref: <required>
  authorized_content_ledger_ref: <required>
  authorized_content_ids: []
  exact_rendered_text: []
  approved_mark_refs: []
  approved_asset_refs: []
  approved_product_variant_ids: []
  product_reference_refs: []
  preservation_locks: []
  operation_or_design_plan_ref: <required>
  provider_specific_translation_owner: <prompt-engineer or adapter>
  binary_execution_owner: <adapter or repository owner>
  requested_exports: []
  prohibited_transformations: []
  prohibited_content: []
  negative_constraints: []
  comparison_required:
    authorized_content: true
    brand_fidelity: true
    product_fidelity: true
    content_accuracy: true
  required_evidence: []
  provider_limitations: []
```

The handoff fails closed when:

- the ledger is absent or unresolved;
- `unknown_content_policy` is not `prohibit`;
- exact rendered text is not traceable to authorized IDs;
- product reference and preservation locks are absent when a specific product is used;
- the provider cannot return reviewable output evidence.

Shared workflow logic never embeds volatile provider recipes as canonical rules.

### 7. Production

The execution owner produces only within the locked brief, approved assets, authorized ledger, destination constraints, and provider handoff.

Provider freedom covers visual realization inside the locked plan. It does not cover new commercial facts, marks, specifications, or product reinterpretation.

A specification-only run may produce a production specification but must retain `specified_only` or `NOT_VERIFIED` artifact status.

### 8. Post-provider comparison

Before independent review, compare the actual output with the ledger and source references.

```yaml
post_provider_comparison:
  output_ref: <actual export>
  ledger_ref: <required>
  product_reference_refs: []
  detected_content:
    - kind: <rendered_text | factual_claim | specification | price | contact | legal_text | brand_mark>
      value: <observed value>
      authorized_content_id: <matching id or null>
      status: <PASS | FAIL | NOT_VERIFIED>
  unmatched_content: []
  altered_authorized_content: []
  omitted_required_content: []
  fidelity_gates:
    SV8: <PASS | FAIL | NOT_VERIFIED | NOT_APPLICABLE>
    SV9: <PASS | FAIL | NOT_VERIFIED | NOT_APPLICABLE>
    SV11: <PASS | FAIL | NOT_VERIFIED | NOT_APPLICABLE>
  result: <PASS | FAIL | PARTIAL | NOT_VERIFIED>
```

Any unmatched claim, specification, price, contact, legal text, or mark is a content hard-gate failure. Any material product geometry, packaging, label, logo, color, or material drift is a product-fidelity hard-gate failure.

`PRODUCED` may transition to `ACCEPTED` only when this comparison passes and independent review passes.

### 9. Export evidence

When production is claimed, require:

- actual exported artifact references;
- declared dimensions and format;
- destination previews at relevant size;
- source/master-to-export fidelity comparison;
- authorized-content comparison;
- effective-resolution and export-integrity checks;
- provider limitations and operation record.

Screenshots may support evidence but do not replace export files.

### 10. Independent review

Route through `design-review` using built-in static-visual gates, including:

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

For commercial delivery, verified non-PASS `SV8`, `SV9`, or `SV11` blocks `ACCEPTED` and `DELIVERED`. The producer cannot issue its own final PASS.

### 11. Defect classification and return routing

```yaml
commercial_creative_defect:
  defect_id: <stable identifier>
  evidence_ref: <required>
  defect_class: <brief | content | product_asset | commercial_design | provider_translation | provider_execution | export | review_coverage | authority>
  causal_owner: <required>
  correction_owner: <required>
  preservation_scope: []
  return_route: <required>
  status: <OPEN | BLOCKED | CORRECTED | NOT_VERIFIED>
```

Return map:

```text
wrong/missing product truth, geometry, packaging, label, mask, edge, or asset resolution
→ design-refinement + product-image-production

ledger omitted or incorrectly translated
→ prompt-engineer

provider invented content despite a correct handoff
→ product/runtime adapter, then repeat comparison

unsupported price, claim, specification, contact, legal text, or mark
→ authoritative content owner + design-refinement

message, hierarchy, composition, type, color, or integration defect
→ master-design + relevant design specialists

missing review evidence or wrong gate coverage
→ design-review

conflicted authority or superseded decision
→ decision-provenance + governing owner
```

Do not restart every phase when the defect is narrow and upstream locks remain valid.

### 12. Delivery

```yaml
commercial_creative_delivery:
  request_id: <stable identifier>
  accepted_artifact_refs: []
  declared_channels: []
  final_dimensions: []
  asset_master_refs: []
  authorized_content_ledger_ref: <required>
  post_provider_comparison_ref: <required>
  preservation_locks: []
  reviewer_report_refs: []
  limitations: []
  prohibited_uses: []
  reprocessing_conditions: []
  status: <DELIVERED | DELIVERED_WITH_LIMITS | BLOCKED | NOT_VERIFIED>
```

`DELIVERED` requires:

- post-provider comparison `PASS`;
- all applicable hard static-visual gates `PASS`;
- reviewed destinations covered by the export evidence;
- no unresolved unauthorized content or product drift.

### 13. Learning review

A verified reusable correction routes to `skill-evolution` with regression evidence. A documented contract-backed behavior failure is classified `BUG`. Product-only exceptions and unverified provider quirks remain local.

## Quality gates

```text
lifecycle_is_classified_before_execution
net_new_commercial_production_routes_to_this_workflow
standalone_asset_prompt_audit_refinement_and_redesign_boundaries_are_preserved
exactly_one_design_owner_is_explicit
specialists_have_narrow_outputs_and_evidence_states
brief_content_destination_and_authority_are_locked_before_production
authorized_content_ledger_exists_before_provider_translation
unknown_commercial_content_defaults_to_prohibited
source_assets_are_inventoried_before_composition
raw_product_source_does_not_bypass_required_product_image_production
Product_Asset_Master_destination_and_variant_are_verified_before_handoff
prepared_master_is_not_reprocessed_without_a_valid_condition
prompt_engineer_translates_but_does_not_own_fidelity_or_lifecycle
provider_handoff_carries_exact_authorized_content_and_preservation_locks
provider_execution_remains_adapter_owned
commercial_direction_does_not_reinterpret_product_truth
post_provider_comparison_detects_unauthorized_content_and_product_drift
production_claims_require_actual_export_evidence
review_is_independent_and_uses_static_visual_gates
SV8_SV9_SV11_non_pass_blocks_acceptance_and_delivery
failure_states_preserve_FAIL_PARTIAL_NOT_VERIFIED_and_NOT_APPLICABLE
causal_defect_owner_is_identified_before_fix
valid_upstream_locks_survive_narrow_correction
final_delivery_is_destination_scoped
verified_reusable_fixes_receive_learning_review
```

## Fail-closed conditions

Block or limit production when:

- required brief or content facts are unresolved;
- the authorized-content ledger is absent, conflicted, or uses a permissive unknown-content policy;
- product identity or variant is conflicted;
- a raw product source requires preparation but no Product Asset Master is available;
- the approved master does not cover the destination;
- a requested transformation violates preservation locks;
- provider limitations prevent checkable fidelity or export evidence;
- only a preview exists but delivery is claimed;
- post-provider comparison finds unauthorized or altered content;
- post-provider comparison finds product or brand drift;
- required reviewer coverage or evidence is absent;
- a hard static-visual gate fails.

Allowed non-pass outcomes:

```text
REQUEST_MISSING_BRIEF_OR_CONTENT
REQUEST_AUTHORIZED_COPY_OR_CLAIM_SOURCE
REQUEST_BETTER_SOURCE_OR_REFERENCE
RETURN_TO_PRODUCT_IMAGE_PRODUCTION
RETURN_TO_PROMPT_ENGINEER
ROUTE_FOR_AUTHORITY
BLOCK_UNSAFE_TRANSFORMATION
BLOCK_UNAUTHORIZED_CONTENT
RETURN_TO_DESIGN_OWNER
RETURN_TO_PROVIDER_ADAPTER
LIMITED_REVIEW
NOT_VERIFIED
```

## Anti-patterns

```text
❌ Send raw product photos straight into final ad composition.
❌ Treat “premium”, “bold”, or “high-converting” as authority to invent benefits or specifications.
❌ Add badges, crowns, certifications, notes, ingredients, prices, or claims without ledger authority.
❌ Let prompt-engineer decide logo, packaging, product color, material, or commercial facts.
❌ Reprocess a verified Product Asset Master for every new banner.
❌ Treat a model preview as exported evidence.
❌ Accept a polished output without comparing it to source and ledger.
❌ Merge asset, design, execution, and acceptance ownership into one role.
❌ Route a known product or claim defect into broad redesign.
❌ Normalize missing evidence into PASS.
❌ Claim readiness for channels outside the reviewed destination.
```

## Final guard

```text
□ One primary lifecycle is explicit.
□ One design owner and narrow specialists are explicit.
□ Brief, content, channels, authority, and locks are recorded.
□ Exact authorized content and marks are recorded in a ledger.
□ Unknown commercial content defaults to prohibited.
□ Every required source has an evidence-backed readiness state.
□ Raw-source bypass is absent.
□ Approved Product Asset Master variants cover the destination.
□ Provider handoff contains ledger, exact content, references, and locks.
□ Actual exports and destination previews exist when production is claimed.
□ Output was compared against ledger and source references.
□ Static-visual review is independent and evidence-backed.
□ SV8, SV9, and SV11 block acceptance when non-PASS.
□ Defects return to causal owners without breaking valid locks.
□ Delivery status and limitations are honest and destination-scoped.
□ Reusable verified lessons receive learning review.
```
