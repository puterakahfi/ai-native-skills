# Creative Production Capability Boundary Decision

**Parent epic:** #140  
**Spike:** #141  
**Status:** PROPOSED FOR REVIEW  
**Working branch:** `140-141-creative-production-boundaries`  
**Decision scope:** executable capability ownership in `ai-native-skills`; no provider implementation and no canonical core mutation.

## 1. Source case

A raw product photograph must sometimes be diagnosed, cleaned, retouched, separated from its background, normalized, and exported as a reusable product asset before it can safely be used in a catalog, marketplace listing, flyer, banner, social advertisement, or composed key visual.

Existing capabilities cover prompt engineering, visual direction, design production, routing, and review, but no capability owns the truth-preserving production boundary between a raw source image and a verified Product Asset Master.

## 2. Decision summary

```yaml
capability_decision:
  product_image_production:
    create: true
    type: skill
    role: specialist
    core_contract: deferred

  creative_asset_production:
    create: false
    type: not_applicable
    reason: one proven specialist does not justify a routing-only wrapper

  commercial_creative_production:
    create: true
    type: workflow
    role: primary lifecycle for net-new commercial visual production
    core_contract: deferred

  ai_native_core:
    verdict: NO_CHANGE
    reason: executable boundaries require multi-case validation before a public cross-adapter obligation is promoted
```

## 3. Why `product-image-production` is a skill

Repository taxonomy defines a skill as one reusable capability with a coherent domain, procedure, outputs, quality gates, failure boundaries, verification, and workflow handoff.

`product-image-production` has a stable domain independent of any provider:

- assess whether a source image is suitable for the declared output;
- identify product truth and preservation requirements;
- define authorized and prohibited transformations;
- plan safe cleanup, retouching, separation, restoration, normalization, and export;
- fail closed when fidelity cannot be established;
- emit a reviewable Product Asset Master and quality report;
- hand verified assets to downstream design or compositing.

It does not select the primary lifecycle, own final advertising composition, or implement one particular editing tool.

## 4. Why `creative-asset-production` is not created

A meta-skill is justified when it must select or compose multiple established specialist capabilities. At this stage only Product Image Production is sufficiently evidenced.

Creating `creative-asset-production` now would produce a wrapper that:

- routes to only one specialist;
- duplicates `role-switcher` specialist composition;
- duplicates `workflow-router` lifecycle selection;
- creates a directory and vocabulary without an observable additional decision.

Reconsider only after at least two materially distinct sibling specialists exist, such as talent-image production, illustration asset production, video asset preparation, or another validated asset-production capability requiring shared selection logic.

## 5. Why `commercial-creative-production` is a workflow

The complete commercial-creative outcome has ordered phases and blocking gates:

```text
route and classify
→ brief and required-content intake
→ source-asset inventory
→ source suitability and fidelity locks
→ asset preparation or verified reuse
→ Product Asset Master verification
→ commercial direction and composition
→ production through the selected provider/tool adapter
→ rendered/exported review
→ channel-specific delivery
→ learning review when a verified reusable fix occurred
```

Skipping or reordering these phases can produce materially unsafe output: altered products, fabricated labels, unusable masks, invalid export resolution, or a polished campaign built from an unverified source.

The workflow fills a lifecycle gap:

- `redesign-workflow` owns broad change to an **existing** visual surface or artifact;
- `design-refinement` owns known narrow fixes to an accepted existing direction;
- `design-audit` owns audit-only work;
- `product-image-production` owns a narrow specialist capability, not the entire commercial lifecycle;
- no current workflow owns net-new commercial static production from brief/raw assets through export acceptance.

## 6. Lifecycle routing boundary

| User intent | Primary lifecycle/capability | Composition |
|---|---|---|
| Prepare one product image, cut out background, create reusable asset master | standalone `product-image-production` capability | provider adapter when execution is requested; `design-review` when acceptance is requested |
| Create a new catalog, flyer, banner, marketplace image, social ad, or campaign creative from raw or prepared assets | `commercial-creative-production` | `product-image-production` when needed, `master-design`, `design-visual`, provider adapter, `design-review` |
| Redesign an existing campaign, poster, banner, or static artifact across multiple layers | `redesign-workflow` | relevant design and image-production specialists |
| Fix a verified narrow defect in an existing creative while preserving direction | `design-refinement` | governing specialists and reviewer |
| Audit an existing asset or commercial creative without changing it | `design-audit` | `design-review` and applicable domain strategy |
| Improve or translate provider-specific image prompts/edit instructions | `prompt-engineer` | product/design locks supplied by the owning production capability |

A raw source must not be routed directly to final commercial design when source diagnosis determines that preparation is required.

## 7. Ownership matrix

| Responsibility | Primary owner | Explicitly not owned by |
|---|---|---|
| Source suitability for declared output | `product-image-production` | `prompt-engineer`, `master-design` |
| Product fidelity and preservation locks | `product-image-production` | provider adapter, final design workflow |
| Authorized/prohibited image transformations | `product-image-production` | generative model defaults |
| Provider/model/API/tool selection and binary execution | product/runtime adapter | shared skill instructions |
| Provider-specific prompt or edit-instruction translation | `prompt-engineer` | `product-image-production` lifecycle ownership |
| Product Asset Master contract and quality report | `product-image-production` | `design-visual` |
| Final commercial message, hierarchy, composition, type, color, imagery integration | `master-design` + `design-visual` under the governing workflow | product-image specialist |
| Ordered net-new commercial production lifecycle | `commercial-creative-production` | `redesign-workflow`, standalone specialist |
| Existing artifact redesign | `redesign-workflow` | commercial-production workflow for net-new work |
| Static visual gate identity, evidence normalization, and verdict | `design-review` | producer or prompt specialist |
| Product-specific brand locks, UI, storage, model/provider configuration, and operational implementation | product repository | `ai-native-skills` shared instructions |
| Lifecycle selection | `workflow-router` | specialist capability |
| Owner/specialist/reviewer composition | `role-switcher` | workflow-specific wrapper meta-skill |
| Canonical cross-adapter public obligation | `ai-native-core`, only after evidence-backed promotion | unvalidated first implementation |

## 8. `product-image-production` boundary

### Covers

```text
source quality and suitability diagnosis
product truth inventory
fidelity and preservation locks
transformation authorization
retouch restraint and safe cleanup decisions
background separation and masking strategy
color/material preservation decisions
perspective correction constraints
restoration and upscale suitability
shadow preservation/removal/regeneration constraints
crop, canvas, scale, and padding normalization strategy
export profile preparation
Product Asset Master declaration
limitations and fail-closed guidance
downstream handoff requirements
```

### Delegates

```text
actual pixel/model/tool execution
provider-specific syntax and API calls
final advertising message and composition
brand strategy and identity creation
legal claim or trademark approval
final static visual acceptance
storage, versioning UI, and product runtime behavior
```

### Prohibits

```text
inventing missing labels, logos, packaging, geometry, texture, or controls
silently redrawing a specific product as a plausible substitute
generic beautification that changes product truth
claiming restoration recovered details that were not verifiable
accepting a plausible preview without exported evidence
universal crop, padding, sharpening, or upscale percentages
hiding provider uncertainty behind quality adjectives
```

## 9. Finalized input contract

```yaml
product_image_production_input:
  request_id: <stable run identifier>
  source_assets:
    - asset_ref: <required>
      source_type: <photograph | scan | render | generated | unknown>
      declared_product_identity: <provided value or null>
      provenance_status: <verified | user_provided | unknown>
      dimensions: <known dimensions or unknown>
      color_profile: <known profile or unknown>

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

## 10. Source assessment contract

```yaml
source_assessment:
  suitability: <suitable | suitable_with_limits | unsuitable | not_verified>
  declared_output_profile:
  source_strengths: []
  source_defects: []
  product_truth_visibility:
    verified_details: []
    uncertain_details: []
    missing_or_obstructed_details: []
  edge_complexity: <rigid | irregular | reflective | translucent | soft | mixed | unknown>
  correction_risks: []
  required_operations: []
  prohibited_operations: []
  better_source_or_reshoot_required: <true | false | conditional>
  limitations: []
```

Fail closed when required identifying details are missing, obscured, blurred beyond reliable recovery, contradicted by references, or likely to be replaced through generative completion.

## 11. Transformation authorization contract

Each operation is classified before execution:

```yaml
transformation_decision:
  operation: <operation id>
  purpose: <named production role>
  authorization: <allowed | conditional | prohibited | not_verified>
  product_truth_impact: <none | low | material | unknown>
  evidence_required: []
  provider_constraints: []
  rollback_or_alternative: <safer option or null>
  rationale:
```

Examples:

- removing dust on the background can be allowed;
- removing a permanent mark on the product is conditional on verified intent;
- reconstructing unreadable label text is prohibited without an authoritative reference;
- correcting lens perspective is conditional on preserving geometry;
- upscaling is conditional on destination need and artifact review;
- creating a new dramatic reflection is outside product-master preparation and belongs to controlled commercial compositing.

## 12. Product Asset Master contract

```yaml
product_asset_master:
  master_id:
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
    provider_adapter_ref: <ref or null>
    execution_evidence_refs: []

  variants:
    - variant_id:
      profile:
      artifact_ref: <exported artifact or null>
      dimensions:
      alpha_status:
      shadow_status:
      crop_and_padding_record:
      color_profile:
      export_format:
      intended_channels: []
      status: <produced | specified_only | blocked | not_verified>

  quality_report:
    product_fidelity: <pass | fail | partial | not_verified | not_applicable>
    label_and_logo_fidelity: <pass | fail | partial | not_verified | not_applicable>
    color_and_material_fidelity: <pass | fail | partial | not_verified | not_applicable>
    mask_and_edge_quality: <pass | fail | partial | not_verified | not_applicable>
    clipping_and_residue: <pass | fail | partial | not_verified | not_applicable>
    effective_resolution: <pass | fail | partial | not_verified | not_applicable>
    export_integrity: <pass | fail | partial | not_verified | not_applicable>
    compositing_readiness: <pass | fail | partial | not_verified | not_applicable>
    evidence_refs: []
    limitations: []

  downstream_handoff:
    allowed_uses: []
    prohibited_uses: []
    preservation_locks: []
    required_review_gates: []
    reprocessing_conditions: []
```

A specification-only output must not claim that a binary asset was produced or reviewed.

## 13. Commercial Creative Production workflow boundary

### Entry conditions

- net-new commercial visual artifact or campaign output is requested;
- required content and asset sources can be identified;
- the requested result is not primarily an audit, narrow refinement, or redesign of an existing artifact.

### Required phases

```text
1. route and classify lifecycle/domain
2. resolve owner, specialists, reviewer, and provider adapter
3. verify brief, content, claims, brand locks, and target channel
4. inventory source assets and determine preparation needs
5. run Product Image Production when required
6. verify Product Asset Master or record an explicit preparation bypass with evidence
7. resolve commercial design direction and production specification
8. execute through product/provider adapters
9. inspect rendered/exported output through design-review static gates
10. correct bounded defects or report blockers
11. export and deliver channel-specific variants
12. run learning review after verified reusable fixes
```

### Hard gates

```text
unresolved required product truth blocks fidelity claims
required asset preparation cannot be silently skipped
unverified Product Asset Master cannot be treated as production-ready
a provider preview cannot substitute for final exported evidence
wrong product, label, logo, price, claim, contact, or required content fails commercial acceptance
final design polish cannot compensate for failed product fidelity or export integrity
```

### Bypass rule

Product Image Production may be `NOT_APPLICABLE` only when an already prepared asset has attributable evidence for the required profile and destination. The workflow records the asset reference, evidence, locks, and review status.

## 14. Provider and runtime adapter boundary

Provider adapters may implement:

- background-removal APIs;
- generative image editing;
- deterministic image-processing pipelines;
- Photoshop or design-tool automation;
- local segmentation, restoration, or upscale models;
- export and storage integration.

Shared skills specify intent, decisions, truth constraints, handoffs, and evidence. They must not embed one vendor as the universal implementation, imply unsupported model guarantees, or claim binary execution when only a plan was produced.

## 15. Design and review handoff

`master-design` and `design-visual` receive:

```yaml
commercial_design_asset_handoff:
  asset_master_ref:
  approved_variant_refs: []
  product_truth_summary:
  preservation_locks: []
  authorized_compositing_transformations: []
  prohibited_transformations: []
  intended_channels: []
  crop_and_safe_area_constraints: []
  unresolved_limitations: []
  required_final_review_gates: []
```

`prompt-engineer` receives the same locks when translating instructions for a provider. It may optimize provider syntax but may not weaken the locks or reinterpret unknown product details.

`design-review` retains canonical acceptance ownership. Applicable static gates include product fidelity, subject separation, resolution, edge/mask quality, lighting and perspective when composited, compression/color, crop safety, content accuracy, and generative artifact control.

## 16. Minimal repository topology

Phase #142 may create:

```text
skills/product-image-production/
├── SKILL.md
└── references/
    ├── fidelity-and-transformation-authorization.md
    ├── source-suitability-and-fail-closed.md
    └── product-asset-master.md
```

Phase #143 may add:

```text
skills/product-image-production/references/transparent-product-catalog.md
```

After the specialist and profile pass validation, phase #144 may create:

```text
skills/commercial-creative-production/
├── SKILL.md
└── references/
    ├── lifecycle-and-routing.md
    └── asset-design-review-handoffs.md
```

Do not create `skills/creative-asset-production/` in this epic unless later evidence supersedes this decision.

## 17. Core-contract verdict

```yaml
ai_native_core_decision:
  verdict: NO_CHANGE
  status: deferred_until_validation
  blocked_changes:
    - product-image-production core contract
    - commercial-creative-production core workflow contract
    - new universal creative-production taxonomy
  promotion_requirements:
    - successful executable skill implementation
    - regression evals
    - at least three materially different product categories
    - fail-closed counterexamples
    - provider-independent transfer evidence
    - demonstrated cross-adapter public obligation
```

The first executable version may be a repository-native skill/workflow without `metadata.ai-native-skills.implements`. Lack of a core contract does not prevent a reusable specialist; inventing a public contract before validation would create premature canonical meaning.

## 18. Acceptance traceability

| Epic criterion | Spike evidence |
|---|---|
| AC-1 Boundary clarity | Sections 2–8 and 13 establish non-overlapping owners |
| AC-6 Handoff integrity | Sections 6, 7, and 15 define lifecycle and handoff boundaries |
| AC-10 Contract and eval integrity | Sections 9–17 define contracts, topology, validation, and core deferral |

## 19. Remaining validation gaps

- Actual provider/tool behavior is not yet tested.
- No binary image artifact has been produced by this spike.
- Mask, alpha, fidelity, and export quality remain `NOT_VERIFIED` until #143/#145.
- Workflow routing evals remain pending #144/#145.
- This decision record is agent-authored and requires review through the child PR; it is not release approval by itself.
