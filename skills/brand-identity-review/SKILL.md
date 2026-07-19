---
name: brand-identity-review
description: Specialist domain reviewer for logo and brand-identity systems — evaluate brand logic, concept-to-symbol translation, distinctiveness, construction, optical balance, recognition, scalability, reproduction, lockups, variants, typography, color, application fidelity, and similarity risk through the design-review facade.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.pattern: domain-reviewer
  ai-native-skills.requires: "design-review design-brand composition visual-hierarchy design-typography design-color"
  ai-native-skills.implements: ai-native-core/contracts/skills/quality/brand-identity-review.contract.yaml
  ai-native-skills.contract-version: "^0.1.0"
  ai-native-skills.related_skills: '["design-review","design-audit","design-refinement","redesign-workflow","design-brand","composition","visual-hierarchy","design-typography","design-color"]'
---

# Brand Identity Review

Specialist reviewer for the `brand-identity` domain. It plugs into the `design-review` facade and supplies the domain knowledge required to move identity work from `LIMITED REVIEW` to `ADAPTER_COVERED`.

This skill reviews identity systems. It does not generate logos, redesign the mark, or provide legal trademark clearance.

## Domain Reviewer Declaration

```yaml
domain_reviewer:
  domain: brand-identity
  gate_namespace: BI
  gate_registry_entries: design-review/references/gate-registry.yaml
  gates: references/identity-gates.md
  required_evidence: references/evidence-and-hard-gates.md
  finding_contract: design-review/finding
  coverage_mode_when_loaded: ADAPTER_COVERED
```

## Hard Rules

```text
1. Resolve brand context and intended use before judging relevance.
2. Separate brand logic, symbol translation, construction, and optical quality.
3. Review the identity system, not only one attractive mockup.
4. Use only canonical BI gate IDs registered by design-review.
5. Large color artwork does not prove small-size, monochrome, inverse, or reproduction quality.
6. Application mockups do not replace direct inspection of canonical marks and lockups.
7. Missing evidence is NOT_VERIFIED, never zero or PASS.
8. Variant diversity must preserve one recognizable construction system.
9. Distinctiveness is not novelty for novelty's sake; relevance and recognition still matter.
10. Similarity screening flags risk and routes legal review; it is not trademark clearance.
11. Every failed or partial gate maps to the design-review finding contract.
12. Review does not silently become logo generation, redesign, or production.
```

## Inputs

```text
target                 required — mark, identity board, PDF, vector source, exports, applications
brand_name             required
brand_context          required — audience, positioning, category, personality, values, use case
identity_state         concept-only | primary-mark | identity-system | application-set | source-only | mixed
intended_use_contexts  required — favicon, app icon, signage, print, social, packaging, UI, etc.
review_depth           quick | focused | full | release
semantic_intent        optional — name meaning, symbol meaning, verbal concept
primary_mark           optional
secondary_marks        optional
wordmark               optional
lockups                optional
monochrome_inverse     optional
construction_source    optional — vector paths, grid, geometry, master artwork
minimum_size_tests     optional
clear_space_rules      optional
typography_system      optional
color_system           optional
application_examples   optional
comparison_set         optional — relevant category/competitor/reference marks
approved_references    optional
```

Infer only when evidence is strong and record assumptions.

## Review Flow

```text
1. CLASSIFY
   Confirm design_domain=brand-identity and identity_state.

2. CONTEXT
   Resolve brand logic, semantic intent, audience, category, personality,
   intended uses, required variants, and delivery claims.

3. ROUTE THROUGH FACADE
   design-review coverage_mode becomes ADAPTER_COVERED.
   Load universal gates only when they add cross-domain evidence.

4. SELECT BI GATES
   Load references/identity-gates.md.
   Select all applicable gates for full/release review or a focused subset.

5. COLLECT EVIDENCE
   Load references/evidence-and-hard-gates.md.
   Inspect canonical marks before mockups.

6. SCORE + VERDICT
   Return BI gate statuses and evidence to design-review.
   Facade normalizes score, coverage, hard gates, verdict, and report.

7. HANDOFF
   local asset fix | design-refinement | redesign-workflow |
   identity designer | trademark/legal specialist | ready
```

## Review Depth

```text
quick
  BI1, BI2, BI3, BI4, BI6, BI7 plus any triggered hard gate
  no production-ready claim

focused
  declared failing BI gates + adjacent construction/variant regressions

full
  all applicable BI gates with explicit evidence gaps

release
  full review + canonical source + required variants + minimum-size tests
  + monochrome/inverse + lockups + reproduction evidence
  + comparison screening when originality claims matter
```

## Domain Verdict Rules

The reviewer returns gate results to `design-review`; the facade issues the final common verdict.

```text
PASS
  applicable BI gates pass, contextual hard gates pass, evidence is sufficient

CONDITIONAL PASS
  no hard-gate failure; bounded non-blocking evidence gaps or risks remain

NEEDS WORK
  important BI gates fail or system consistency is incomplete

CRITICAL
  a contextual BI hard gate fails materially

NOT_VERIFIED
  required identity evidence is missing
```

No identity release claim is allowed when canonical source, required variants, or triggered hard-gate evidence remains unavailable.

## Output Mapping

```yaml
domain_review_result:
  reviewer: brand-identity-review
  design_domain: brand-identity
  namespace: BI
  coverage_mode: ADAPTER_COVERED
  identity_state: <state>
  selected_gate_ids: []
  gate_results: []
  contextual_hard_gates: []
  evidence_available: []
  evidence_gaps: []
  similarity_risk:
    level: low | medium | high | not-verified
    evidence: []
    legal_clearance: not-provided
  scope_limitations: []
  recommended_handoff: <route>
```

Every finding uses canonical `BI*` ID, governing reviewer `brand-identity-review`, direct evidence, impact, correction direction, confidence, and effort.

## Final Guard

```text
□ Brand context and intended uses are explicit.
□ Identity state and review depth are explicit.
□ Canonical marks were inspected before mockups.
□ Every selected BI gate is registered and applicable.
□ Construction and optical findings remain separate.
□ Small-size, monochrome, inverse, lockup, and reproduction claims have direct evidence.
□ Variant consistency was checked across the complete supplied set.
□ Similarity screening is not presented as legal clearance.
□ Findings map back through design-review.
□ No redesign or generation occurred unless a calling workflow owns it.
```