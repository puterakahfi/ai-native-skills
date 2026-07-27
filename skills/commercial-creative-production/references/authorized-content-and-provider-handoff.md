# Authorized Content and Provider Handoff

Use this reference for every commercial static visual that will be translated to or executed by an image provider.

## Purpose

Prevent a provider, prompt translator, design owner, or reviewer from turning missing commercial facts into plausible-looking copy, claims, specifications, prices, contacts, legal text, or brand marks.

The contract separates four concerns:

```text
authority decides what is true and approved
→ workflow records the exact authorized set
→ prompt-engineer translates without broadening it
→ provider executes within that set
→ independent comparison and review decide acceptance
```

## Default policy

```text
unknown content → prohibited
unverified claim → prohibited
unreadable source text → do not reconstruct
style adjective → visual direction only
provider-added text or mark → unauthorized until proven otherwise
```

“Premium”, “luxury”, “bold”, “viral”, “high-converting”, “professional”, or similar direction never authorizes a product benefit, quality claim, ingredient, note, award, certification, size, price, discount, usage, or logo.

## Authorized-content ledger

```yaml
authorized_content_ledger:
  ledger_id: ACL-<stable-id>
  authority_refs:
    - <brief, product page, approved copy deck, price sheet, legal approval, brand asset>
  unknown_content_policy: prohibit

  authorized_items:
    - content_id: CONTENT-001
      kind: rendered_text
      value: <exact string>
      authority_ref: <required>
      render_policy: required | allowed | metadata_only
      normalization: exact | whitespace_only | case_insensitive

  prohibited_items:
    - <explicit value, category, or pattern>

  unresolved_items:
    - proposed_value: <value>
      reason: <missing authority, contradiction, unreadable source, pending approval>
      status: NOT_VERIFIED
```

### Supported kinds

```text
rendered_text
factual_claim
specification
price
contact
legal_text
brand_mark
```

A sentence that contains both visual copy and a factual claim must be classified as a claim.

## Authority rules

1. Every authorized item has one traceable authority reference.
2. User-provided text is authorized only for the declared use; it is not proof of a broader factual claim.
3. Source-image text may be recorded only when readable enough to transcribe without reconstruction.
4. Brand marks require supplied or explicitly approved assets.
5. Prices, discounts, quantities, dates, contacts, ingredients, notes, benefits, comparisons, certifications, and legal text require explicit authority.
6. Unresolved or contradictory items remain outside the provider-renderable set.
7. The workflow may request approval for proposed copy, but proposed copy is not executable content until accepted.

## Provider handoff contract

```yaml
provider_execution_handoff:
  handoff_id: PEH-<stable-id>
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
  provider_specific_translation_owner: prompt-engineer | adapter
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

### Required negative constraints

Use provider-appropriate syntax, but preserve these meanings:

```text
no additional words, captions, labels, badges, icons, logos, seals, or watermarks
no inferred claims, benefits, ingredients, notes, specifications, prices, sizes, or use cases
no altered product geometry, packaging, cap, label placement, logo construction, color, or material
no replacement product, plausible substitute, or brand-like mark
render only exact authorized text and approved marks
```

Negative constraints supplement the allowlist; they never replace it.

## Prompt-engineer translation boundary

`prompt-engineer` must:

- receive a locked brief, ledger, source references, preservation locks, and provider target;
- preserve exact authorized content IDs and values;
- distinguish visual direction from factual content;
- emit provider-specific positive and negative instructions;
- report unsupported provider features and expected text/fidelity limitations;
- refuse translation when the ledger or required locks are absent.

`prompt-engineer` must not:

- invent marketing copy to make a layout feel complete;
- infer benefits or specifications from appearance;
- repair unreadable labels with plausible text;
- create a mark because a premium composition appears visually empty;
- weaken exact-content or product-truth constraints for aesthetic quality.

## Output comparison

Inspect the actual export, not only the prompt or preview.

```yaml
post_provider_comparison:
  output_ref: <required>
  ledger_ref: <required>
  product_reference_refs: []

  detected_content:
    - kind: <supported kind>
      value: <observed output value>
      authorized_content_id: <matching id or null>
      status: PASS | FAIL | NOT_VERIFIED

  unmatched_content: []
  altered_authorized_content: []
  omitted_required_content: []

  fidelity_gates:
    SV8: PASS | FAIL | NOT_VERIFIED | NOT_APPLICABLE
    SV9: PASS | FAIL | NOT_VERIFIED | NOT_APPLICABLE
    SV11: PASS | FAIL | NOT_VERIFIED | NOT_APPLICABLE

  result: PASS | FAIL | PARTIAL | NOT_VERIFIED
```

### Matching policy

- `exact`: value must match exactly.
- `whitespace_only`: whitespace may normalize; wording and punctuation remain unchanged.
- `case_insensitive`: case may differ only when authority permits.
- Brand marks match approved asset identity, not a textual description.
- A paraphrase of a factual claim is still a claim and needs authority.

## Hard-gate policy

```text
unmatched claim, specification, price, contact, legal text, or mark → FAIL SV11 and block
altered or invented logo/mark                                     → FAIL SV8 and block
product geometry, packaging, label, color, or material drift       → FAIL SV9 and block
unreadable required text                                            → FAIL SV5/SV6 and block
missing comparison evidence                                         → NOT_VERIFIED and block
```

Aesthetic score cannot override these failures.

## Return routing

```text
ledger missing, broadened, or mistranslated
→ prompt-engineer

provider invented content despite correct handoff
→ provider adapter

unsupported claim, specification, price, contact, legal text, or mark
→ authority owner + design-refinement

product geometry, packaging, label, logo, color, or material drift
→ design-refinement + product-image-production

composition defect with content and product truth intact
→ master-design + relevant design specialists

missing or incorrect review evidence
→ design-review
```

Preserve valid upstream decisions during narrow correction.

## Counterexamples

### Unsupported fragrance claims

Source shows a perfume and product name only. Output adds “long lasting”, “premium quality”, gender positioning, or note lists.

```text
result: FAIL
reason: unsupported factual and marketing claims
route: authority owner + design-refinement
```

### Unsupported packaging use cases

Source shows clear jars and capacities. Output adds “ideal for candles, skincare, gifts & storage”.

```text
result: FAIL
reason: inferred use-case claims
route: authority owner + design-refinement
```

### Unsupported premium mark

Output adds a crown, seal, award, certification, or official-store mark not supplied by authority.

```text
result: FAIL
reason: unauthorized brand-like mark
route: provider adapter or prompt-engineer, depending on handoff evidence
```

### Product drift

Output changes cap geometry, label placement, package proportions, logo construction, color, or material while preserving a plausible category appearance.

```text
result: FAIL
reason: product fidelity drift
route: design-refinement + product-image-production
```

## Final checklist

```text
□ Exact authorized values and authority refs exist.
□ Unknown content policy is prohibit.
□ Unresolved items are excluded from renderable content.
□ Exact text and approved marks are carried into provider translation.
□ Product references and preservation locks are carried into provider translation.
□ Provider-specific negative constraints preserve the shared meanings.
□ Actual export is compared against the ledger and references.
□ SV8, SV9, and SV11 statuses are explicit.
□ Any non-PASS hard gate blocks acceptance and delivery.
□ Defects route to the narrow causal owner.
```
