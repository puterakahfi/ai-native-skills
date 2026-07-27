---
name: prompt-engineer
description: Translate an approved visual or image-operation plan into provider-specific instructions without inventing product truth, commercial claims, rendered text, brand marks, transformation authority, lifecycle state, or acceptance.
license: MIT
metadata:
  ai-native-skills.version: 1.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.pattern: specialist
  ai-native-skills.requires: "decision-provenance"
  ai-native-skills.related_skills: '["commercial-creative-production","product-image-production","master-design","design-visual","design-review"]'
---

# Prompt Engineer

Translate a locked visual, image-production, or commercial plan into the syntax and constraints of a selected provider.

This skill improves provider instruction quality. It does not decide what is true, approved, commercially claimable, visually accepted, or production-ready.

## Core rule

```text
receive locked plan + authority + assets + constraints
→ identify provider dialect and capability limits
→ preserve exact content and product locks
→ translate positive instructions
→ translate negative and fail-closed constraints
→ validate completeness
→ emit provider handoff or refuse translation
```

Provider fluency is subordinate to authority, fidelity, and workflow state.

## When to use

Load this skill for:

- provider-specific text-to-image instructions;
- provider-specific image-edit or generation instructions;
- refinement of an existing provider prompt;
- diagnosis of a provider output or prompt failure;
- translation of an approved product-image operation plan;
- translation of a locked commercial creative plan.

Do not use it as the owner of:

- product fidelity or Product Asset Master status;
- commercial claims, prices, specifications, legal text, or brand approval;
- final visual direction;
- binary execution;
- review or acceptance;
- lifecycle routing.

## Required input

```yaml
prompt_engineering_input:
  request_id: <stable identifier>
  mode: <draft | translate_locked_plan | diagnose | refine>
  target_provider: <provider/model/version or unresolved>

  governing_workflow: <workflow or standalone capability>
  locked_plan_ref: <required for translation>
  authority_refs: []

  subject_and_asset_refs: []
  product_reference_refs: []
  approved_mark_refs: []
  preservation_locks: []
  allowed_transformations: []
  prohibited_transformations: []

  authorized_content_ledger:
    ledger_id: <required for commercial rendered content>
    authority_refs: []
    unknown_content_policy: prohibit
    authorized_items: []
    prohibited_items: []
    unresolved_items: []

  requested_exports: []
  provider_limitations: []
```

A commercial translation is blocked when the locked plan, authority, or authorized-content ledger is missing. A product-specific translation is blocked when required product references or preservation locks are missing.

For commercial production, load `../commercial-creative-production/references/authorized-content-and-provider-handoff.md`.

## Ownership boundary

### Owns

```text
provider dialect selection and syntax
prompt structure and instruction ordering
provider-supported positive and negative constraints
translation completeness
provider limitation disclosure
prompt-level diagnosis
```

### Delegates

```text
commercial lifecycle and claim lock → commercial-creative-production
product truth and transformation authority → product-image-production
design direction and hierarchy → master-design + design-visual
binary execution and export evidence → provider/runtime adapter
final visual verdict → design-review
factual, brand, legal, and approval decisions → authority owner
```

### Prohibits

```text
inventing copy, claims, specifications, prices, contacts, legal text, or marks
repairing unreadable labels with plausible content
changing product geometry, packaging, logo, color, material, or distinguishing details
weakening locks to improve aesthetics
claiming provider execution or acceptance
turning style adjectives into factual authority
```

## Translation procedure

### 1. Classify request

```text
prompt draft only
locked plan translation
prompt diagnosis
bounded prompt refinement
```

If the request actually asks for asset preparation, final commercial production, redesign, audit, or acceptance, preserve that lifecycle and use this skill only as a specialist.

### 2. Verify authority and locks

Before writing provider syntax, verify:

- one governing workflow or capability;
- one locked plan reference;
- all required source and approved asset references;
- exact authorized rendered content and marks;
- product-fidelity and preservation locks;
- allowed and prohibited transformations;
- provider target and known limitations.

Missing material input produces `BLOCKED` or `NOT_VERIFIED`, not a guessed prompt.

### 3. Separate direction from facts

Classify each instruction:

```text
visual direction
authorized rendered content
authorized mark
product fidelity lock
allowed transformation
prohibited transformation
provider execution requirement
evidence requirement
```

Examples:

```text
"premium editorial lighting" → visual direction
"premium quality"            → factual/quality claim requiring authority
"bold composition"           → visual direction
"bold & masculine"           → positioning claim requiring authority
"100 ml"                     → specification requiring authority
crown or award seal           → mark requiring authority
```

### 4. Build provider-neutral translation plan

```yaml
provider_translation_plan:
  plan_ref: <locked plan>
  subject_refs: []
  product_reference_refs: []
  approved_mark_refs: []
  authorized_content_ids: []
  exact_rendered_text: []
  visual_direction: []
  preservation_locks: []
  allowed_transformations: []
  prohibited_transformations: []
  required_evidence: []
```

Do not mix unsupported prose into `visual_direction`.

### 5. Translate to provider dialect

Provider syntax may vary, but the following meanings remain invariant:

```text
use only supplied product and approved assets
render only exact authorized text
use only approved brand marks
add no captions, labels, badges, seals, watermarks, or symbols
infer no claims, benefits, ingredients, notes, specifications, prices, sizes, or use cases
preserve product shape, packaging, cap, label placement, logo, color, material, and details
return an export suitable for source and content comparison
```

### 6. Provider-aware guidance

#### Natural-language image providers

Use direct, ordered instructions:

```text
1. Identify exact source assets.
2. State preservation and content locks before style.
3. State visual direction and composition.
4. Repeat exact rendered text and approved marks.
5. State explicit exclusions.
6. Request export and evidence conditions.
```

#### Weighted or negative-prompt providers

Use the provider's supported syntax while preserving the same semantics. A negative prompt supplements the exact allowlist; it never authorizes generated filler.

#### Providers with weak text or identity control

Declare the limitation before execution. Route exact text or mark compositing to a deterministic downstream tool when available. Do not claim fidelity from a provider known to be unable to preserve it.

### 7. Validate translation

```yaml
prompt_translation_validation:
  locked_plan_preserved: <true | false>
  authority_preserved: <true | false>
  authorized_content_ids_complete: <true | false | not_applicable>
  unknown_content_policy_prohibit: <true | false | not_applicable>
  exact_text_preserved: <true | false | not_applicable>
  approved_marks_preserved: <true | false | not_applicable>
  product_references_present: <true | false | not_applicable>
  preservation_locks_complete: <true | false | not_applicable>
  prohibited_transformations_complete: <true | false>
  provider_limitations_disclosed: <true | false>
  result: <PASS | FAIL | NOT_VERIFIED>
```

Only `PASS` may hand off to binary execution.

### 8. Output

```yaml
prompt_engineering_output:
  request_id: <stable identifier>
  provider: <provider/model/version>
  governing_workflow: <ref>
  locked_plan_ref: <ref>
  authorized_content_ledger_ref: <ref or not_applicable>
  provider_translation_plan: <structured plan>
  positive_instructions: <provider syntax>
  negative_instructions: <provider syntax>
  provider_limitations: []
  required_output_evidence: []
  translation_validation: <record>
  status: <READY_FOR_EXECUTION | BLOCKED | NOT_VERIFIED>
```

This output is translation evidence, not provider execution or acceptance evidence.

## Diagnosis loop

When a provider output is supplied:

```text
compare observed failure with locked plan
→ classify translation omission vs provider execution defect
→ preserve valid locks
→ patch only the causal instruction layer
→ route product/content/review defects to their owners
```

Examples:

```text
ledger omitted from prompt                      → prompt-engineer defect
correct prompt, provider adds unsupported badge → provider adapter defect
product geometry changed                        → product-image-production + refinement
unsupported claim passed from brief             → authority owner + workflow intake
final artifact looks good but lacks comparison  → design-review / NOT_VERIFIED
```

## Prompt quality gates

```text
provider_target_is_explicit
locked_plan_is_preserved
commercial_content_is_allowlisted_and_authorized
unknown_commercial_content_is_prohibited
exact_text_and_marks_are_not_broadened
product_references_and_fidelity_locks_are_present_when_required
allowed_and_prohibited_transformations_are_explicit
provider_limitations_are_disclosed
positive_and_negative_instructions_preserve_shared_meaning
translation_does_not_claim_execution_or_acceptance
```

## Anti-patterns

```text
❌ Add persuasive copy because the layout has empty space.
❌ Infer product benefits from appearance or category.
❌ Convert “premium” into “premium quality”.
❌ Add a crown, seal, certification, or official mark without an approved asset.
❌ Repair unreadable source text with plausible words.
❌ Describe a product loosely enough that the provider substitutes it.
❌ Remove fidelity constraints to improve image quality.
❌ Treat prompt score as production readiness.
❌ Treat a generated preview as accepted evidence.
```

## Final guard

```text
□ Governing workflow and locked plan are explicit.
□ Authority and exact authorized content are present.
□ Unknown commercial content defaults to prohibited.
□ Product references and preservation locks are complete when required.
□ Provider positive and negative instructions preserve the same constraints.
□ Provider limitations are disclosed.
□ Translation validation is PASS before execution.
□ Output claims translation only, not execution or acceptance.
```
