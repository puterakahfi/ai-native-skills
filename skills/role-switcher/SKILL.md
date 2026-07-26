---
name: role-switcher
description: Intent and domain detection with explicit, evidenced role composition — selects one owner, narrow specialists, an independent reviewer facade, and a domain reviewer when specialized acceptance is required, then verifies that every activated role produced its distinct output.
license: MIT
metadata:
  ai-native-skills.version: 1.6.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.requires: "commercial-creative-production product-image-production prompt-engineer master-engineer master-design design-visual adaptive-component-design product-manager ux-psychology user-research native-ai-engineer chatgpt-app-development diagram-architect design-review brand-identity-review systematic-debugging architecture-review security-review plan"
  ai-native-skills.type: meta-skill
  ai-native-skills.implements: ai-native-core/contracts/skills/meta/role-switcher.contract.yaml
  ai-native-skills.contract-version: "~0.1"
---

# Role Switcher

## Core contract interface

```yaml
required_inputs:
  - user_request
allowed_outputs:
  - detected_intent
  - role_composition
  - skills_to_load
  - analysis_with_multi_lens
quality_gates:
  - intent_must_be_detected_before_role_selection
  - role_composition_must_be_explicit_not_implicit
  - each_role_must_contribute_a_distinct_lens
  - no_role_loaded_without_clear_relevance_to_intent
  - multi_role_output_must_be_structured_by_lens
  - agent_must_state_which_roles_were_activated
```

State detected intent and activated roles explicitly. Each role contributes one distinct lens before the owner synthesizes one decision. Never load a role merely because it is generally useful.

Role names are not execution evidence. Production or acceptance work requires an observable evidence ledger.

## Core rule

```text
detect intent, lifecycle, platform, domain, and artifact state
→ preserve the governing workflow selected by workflow-router
→ assign exactly one decision owner
→ load only narrow specialists
→ assign execution/implementation ownership when binary or repository work occurs
→ add reviewer facade when acceptance is required
→ add applicable built-in or external domain reviewer
→ declare expected output for every activated role
→ verify evidence and status
→ owner synthesizes one result
```

Roles are not a flat list.

```text
Lifecycle workflow  phase order, state transitions, and handoff integrity
Owner               final decision responsibility and synthesis inside the lifecycle
Specialist          narrow expertise within a declared boundary
Execution owner     provider, runtime, or repository implementation
Reviewer facade     common review entry, evidence normalization, score, verdict, report
Domain reviewer     specialist-domain gates, evidence interpretation, hard-gate policy
Authority owner     factual, legal, brand, product, or approval decision source
```

A workflow, platform specialist, domain specialist, prompt specialist, or reviewer never silently replaces the owner.

## Role execution evidence

Place evidence inside the contract-approved `role_composition` output:

```yaml
role_composition:
  lifecycle: <workflow or standalone capability>
  owner: <role>
  specialists: []
  implementation_or_execution_owner: <role or null>
  reviewer_facade: <role or null>
  domain_reviewer: <role or null>
  authority_owners: []
  role_execution_evidence:
    - role: <activated role>
      slot: owner | specialist | reviewer_facade | domain_reviewer | implementation_owner | authority_owner
      required: true | false
      expected_output: <distinct artifact or decision>
      evidence_ref: <observable output reference or null>
      status: PRODUCED | PARTIAL | NOT_VERIFIED | BLOCKED | NOT_APPLICABLE
      limitation: <reason or null>
  production_readiness: READY | PARTIAL | BLOCKED | NOT_VERIFIED
```

Evidence rules:

1. Every activated role has exactly one narrow expected output.
2. `evidence_ref` points to an observable artifact, decision, mapping, review, test, export, or runtime evidence.
3. A role name or activation statement is never enough.
4. Required role evidence with `PARTIAL`, `NOT_VERIFIED`, or `BLOCKED` prevents production or acceptance PASS.
5. `NOT_APPLICABLE` requires rationale.
6. Owner synthesis cites actual role outputs and preserves their statuses.
7. Reviewer evidence remains independent from producer or implementation evidence when practical.
8. Lifecycle presence does not count as owner evidence; the lifecycle coordinates, the owner decides.

## Commercial creative composition

### Net-new commercial static production

```yaml
role_composition:
  lifecycle: commercial-creative-production
  owner: master-design
  specialists:
    - design-visual
    - product-image-production # required when raw/unverified product imagery needs preparation
    - prompt-engineer          # conditional provider-translation specialist
    - <selected copy/content/brand/type/color/composition specialists>
  implementation_or_execution_owner: <product/runtime/provider adapter>
  reviewer_facade: design-review
  domain_reviewer: built-in static-visual strategy
  authority_owners:
    - <brand/content/product/legal owner when applicable>
```

Distinct outputs:

| Role | Expected output | Must not own |
|---|---|---|
| `commercial-creative-production` | lifecycle state, phase order, asset-readiness gate, handoff integrity, return route | visual taste, pixel execution, final verdict |
| `master-design` | commercial direction, hierarchy, composition synthesis, destination variants | product-source truth, provider execution, self-acceptance |
| `product-image-production` | source suitability, fidelity locks, transformation decisions, Product Asset Master | final advertising message or composition |
| `design-visual` | bounded visual direction under brief and asset locks | product reinterpretation or acceptance |
| `prompt-engineer` | provider-specific translation of a locked plan | fidelity, lifecycle, transformation authority, final verdict |
| provider/runtime adapter | binary execution and export evidence | shared workflow ownership, product truth policy |
| `design-review` | gate applicability, evidence normalization, score, verdict, report | production or silent correction |
| built-in static strategy | static visual evidence interpretation and hard-gate policy | production ownership |

Hard role rule:

```text
raw product source that requires preparation
→ product-image-production evidence must be PRODUCED
→ approved Product Asset Master variant must cover destination
→ only then may master-design consume it
```

### Prepared Product Asset Master

When a verified master covers the destination:

```text
lifecycle: commercial-creative-production
owner: master-design
product-image-production: NOT_APPLICABLE for reprocessing, with master evidence reference
specialist handoff: approved variant + preservation locks + allowed/prohibited uses
```

Do not load Product Image Production merely to repeat completed work.

### Standalone product image preparation

```yaml
role_composition:
  lifecycle: standalone product-image-production
  owner: product-image-production
  specialists:
    - prompt-engineer # only when provider translation is requested
  implementation_or_execution_owner: <provider adapter or null>
  reviewer_facade: design-review # only when acceptance is requested
  domain_reviewer: built-in static-visual strategy # when reviewed
```

`master-design` is not required when no final commercial composition is requested.

### Targeted product-asset correction

For a known halo, clipping, edge, color, crop, or mask defect in an accepted existing direction:

```text
lifecycle: design-refinement
owner: master-design or declared existing-artifact owner
causal specialist: product-image-production
reviewer: design-review + built-in static strategy
preservation: unaffected layout, copy, brand, product truth, and approved direction
```

### Existing broad commercial redesign

```text
lifecycle: redesign-workflow
owner: master-design
specialists: product-image-production only when asset/source layers change
reviewer: design-review + built-in static strategy
```

The commercial-production workflow does not replace redesign ownership for an existing artifact.

### Audit or acceptance only

```text
audit findings only
→ lifecycle: design-audit
→ owner: declared review owner
→ reviewer facade: design-review
→ domain reviewer: built-in static strategy

acceptance of existing export
→ design-review owns verdict
→ producer roles are evidence sources, not acceptance owners
```

## Design review composition

For design acceptance, `design-review` is the reviewer facade. It is not automatically the expert for every discipline.

```text
design-review owns
  classification, reviewer routing, gate identity, applicability,
  evidence normalization, score, coverage, verdict, report

domain reviewer owns
  domain principles, canonical gate definitions, evidence interpretation,
  specialist hard gates, correction knowledge
```

### Built-in domains

| Design domain | Decision owner | Specialists | Reviewer facade | Domain reviewer |
|---|---|---|---|---|
| Digital product UI, responsive web, mobile, desktop | `master-design` | relevant design ports; `adaptive-component-design` when needed | `design-review` | built-in interactive strategy |
| Net-new static marketing, social, ad, poster, banner, thumbnail | `master-design` under `commercial-creative-production` | `design-visual`, selected visual/content specialists, `product-image-production` when needed | `design-review` | built-in static-visual strategy |
| Existing static marketing redesign | `master-design` under `redesign-workflow` | selected changed-layer specialists | `design-review` | built-in static-visual strategy |
| Presentation slides or decks | `master-design` or presentation owner | narrative, data, visual specialists | `design-review` | built-in presentation strategy |

### External adapter domains

| Design domain | Owner | Reviewer facade | Domain reviewer | Coverage when loaded |
|---|---|---|---|---|
| Logo and brand identity systems | declared brand/identity owner | `design-review` | `brand-identity-review` (`BI`) | `ADAPTER_COVERED` |
| Packaging and specialist print production | declared packaging/print owner | `design-review` | packaging/print reviewer | adapter-defined |
| Motion graphics, film, video editing | declared motion/video owner | `design-review` | motion/video reviewer | adapter-defined |
| Industrial or physical product design | declared industrial-design owner | `design-review` | industrial-design reviewer | adapter-defined |
| Architecture, interior, or spatial design | declared spatial-design owner | `design-review` | spatial-domain reviewer | adapter-defined |
| Fashion design | declared fashion-design owner | `design-review` | fashion-domain reviewer | adapter-defined |
| Service-design systems | product/service owner | `design-review` only for visual artifacts | service-design reviewer | adapter-defined |

When a required reviewer is unavailable:

```text
coverage_mode: LIMITED
verdict ceiling: LIMITED REVIEW
handoff: install/load domain reviewer or route to domain specialist
```

Universal visual review remains supplementary and cannot certify complete specialist-domain quality.

## Design ownership rules

```text
broad product UI/UX
  owner: master-design
  reviewer facade: design-review
  domain reviewer: built-in interactive

cross-device component choice
  owner: master-design
  specialist: adaptive-component-design
  reviewer facade: design-review after implementation

net-new commercial static production
  lifecycle: commercial-creative-production
  owner: master-design
  asset specialist: product-image-production when required
  reviewer: design-review + built-in static

brand identity audit or acceptance
  owner: declared brand/identity owner
  facade: design-review
  domain reviewer: brand-identity-review
  namespace: BI
  coverage: ADAPTER_COVERED when loaded

audit only
  lifecycle: design-audit

targeted verified design findings
  lifecycle: design-refinement

broad existing direction replacement
  lifecycle: redesign-workflow
```

A narrow advisory question may use a specialist without a reviewer when no artifact is being accepted.

## General role map

### Engineering

| Intent | Owner | Specialists | Reviewer |
|---|---|---|---|
| Review code, PR, architecture | `master-engineer` | relevant architecture skills | `architecture-review` |
| Bug, error, crash, debugging | `master-engineer` | `systematic-debugging` | relevant reviewer after fix |
| Security, vulnerability, secrets | `master-engineer` | security skills | `security-review` |
| System design or structural refactor | `master-engineer` | `native-ai-engineer` when relevant | `architecture-review` |
| Native AI runtime, adapter, contract | `native-ai-engineer` | `master-engineer`, runtime skills | `architecture-review` |
| Existing-product ChatGPT App integration | `master-engineer` | `chatgpt-app-development`, `native-ai-engineer`, product/design specialists as needed | architecture, security, and design reviewers as applicable |

### Product and research

| Intent | Owner | Specialists | Reviewer |
|---|---|---|---|
| Product gap analysis | `product-manager` | domain owners and experts | relevant domain reviewer |
| Requirements and acceptance criteria | `product-manager` | technical/design owners | relevant review workflow |
| Interviews, JTBD, assumption validation | `user-research` | `product-manager` | research evidence review |
| Survey or usability test | `user-research` | `ux-psychology` | product owner synthesizes implications |
| ChatGPT App product from zero | `product-manager` | `chatgpt-app-development`, `native-ai-engineer`, `master-design`, `master-engineer` | product acceptance plus architecture, security, and design reviewers |

### Creative and AI tools

| Intent | Owner | Specialists | Reviewer |
|---|---|---|---|
| Generate/refine provider-specific image prompt | `prompt-engineer` | brand/product/design specialists supplying locks | rendered-output review when accepted |
| Prepare truthful reusable product image asset | `product-image-production` | `prompt-engineer` only for translation; provider adapter for execution | `design-review` when acceptance requested |
| Produce a net-new commercial static creative | `master-design` under `commercial-creative-production` | `design-visual`, `product-image-production` when required, selected visual/content specialists, `prompt-engineer` conditionally | `design-review` + built-in static strategy |
| Diagnose generated identity output | identity owner or `prompt-engineer` for prompt-only diagnosis | `brand-identity-review` as reviewer, not generator | `design-review` + `brand-identity-review` |
| AI image product or generation feature | `product-manager` | prompt + design + engineering owners | applicable product/design/engineering reviewers |
| ChatGPT App tool, widget, native-capability handoff, or publication boundary | lifecycle owner | `chatgpt-app-development`; add `native-ai-engineer` for contract/runtime boundaries | applicable architecture, security, accessibility, and design reviewers |

## ChatGPT App composition rules

`chatgpt-app-development` is a platform specialist, not a product owner and not a replacement workflow.

```text
product from zero
  lifecycle owner: product-manager
  platform specialist: chatgpt-app-development
  architecture specialist: native-ai-engineer
  UI owner: master-design when user-facing widget/UI is in scope
  implementation owner: master-engineer during delivery
  reviewers: architecture-review + security-review + design-review/accessibility as applicable

existing product integration
  lifecycle owner: master-engineer for implementation synthesis
  product authority: product-manager for scope/value decisions
  platform specialist: chatgpt-app-development
  architecture specialist: native-ai-engineer when boundaries change
```

The platform specialist owns Apps SDK/MCP expertise, not product value, domain ownership, or approval.

## Application steps

### 1. Detect intent and lifecycle

```text
domain
action: audit | advise | prepare | produce | build | fix | redesign | accept
depth: narrow | specification | production | release
evidence state: idea | source | prepared_master | rendered | exported | runtime_behavior
platform: generic | chatgpt-app | other-specialized-surface
```

For design tasks also classify:

```text
design_domain
surface_profile
existing_or_net_new
raw_or_verified_assets
reviewer availability
built-in or adapter coverage
```

For commercial production also classify:

```text
standalone_asset_or_final_creative
Product_Asset_Master_requirement
provider_translation_required
binary_execution_owner
destination_and_export_requirements
```

### 2. Assign composition slots

```yaml
roles:
  lifecycle:
  owner:
  specialists: []
  implementation_or_execution_owner:
  reviewer_facade:
  domain_reviewer:
  authority_owners: []
```

For each slot, declare one `expected_output`, whether required, and evidence that satisfies it.

### 3. Enforce composition gates

```text
□ governing lifecycle or standalone capability is explicit
□ exactly one decision owner is explicit
□ every specialist has a narrow reason
□ every activated role has one distinct expected output
□ every required role has produced evidence or a preserved non-pass status
□ role names or activation statements are not evidence
□ lifecycle, platform, prompt, and domain specialists do not replace the owner
□ execution ownership is explicit when binary or repository work occurs
□ raw product sources cannot bypass Product Image Production when preparation is required
□ verified Product Asset Masters are reused without unnecessary reprocessing
□ prompt-engineer does not own fidelity or transformation authority
□ reviewer is independent when practical
□ design domain and coverage are explicit when reviewed
□ specialized acceptance has the correct domain reviewer
□ missing reviewer limits the verdict
□ rendered/implemented deliverables have evidence-backed review
□ owner synthesis references actual role outputs
```

### 4. Synthesize one result

The owner returns one decision with rationale, specialist evidence, trade-offs, production implications, reviewer verdict, coverage mode, and remaining gaps.

The synthesis includes `role_execution_evidence` and `production_readiness`. Do not return disconnected role reports or normalize missing evidence into PASS.

## Examples

### New product ad from raw photo

```text
Lifecycle: commercial-creative-production
Owner: master-design
Asset specialist: product-image-production
Visual specialist: design-visual
Prompt specialist: prompt-engineer only if provider translation is needed
Execution owner: selected provider adapter
Reviewer: design-review + built-in static
Gate: Product Asset Master must cover the destination before composition
```

### Product Asset Master already approved

```text
Lifecycle: commercial-creative-production
Owner: master-design
Product Image Production: NOT_APPLICABLE for reprocessing
Evidence: approved variant and preservation-lock handoff
Reviewer: design-review + built-in static
```

### Repository UI work blocked by label-only roles

```yaml
role_execution_evidence:
  - role: master-design
    slot: owner
    expected_output: visual_direction_contract
    evidence_ref: issue-comment:direction-lock
    status: PRODUCED
  - role: implementation-context-discovery
    slot: specialist
    expected_output: repository_implementation_mapping
    evidence_ref: null
    status: NOT_VERIFIED
  - role: master-engineer
    slot: implementation_owner
    expected_output: repository_patch
    evidence_ref: null
    status: BLOCKED
production_readiness: BLOCKED
```

Roles are listed, but production may not proceed because required outputs are missing.

### ChatGPT App product from zero

```text
Owner: product-manager
Platform specialist: chatgpt-app-development
Architecture specialist: native-ai-engineer
Design owner: master-design for widget UX
Implementation owner: master-engineer
Reviewers: architecture-review, security-review, design-review, accessibility
Primary lifecycle: product-development-workflow
```

## Anti-patterns

```text
❌ Use `prompt-engineer` as product-fidelity or commercial-production owner.
❌ Use `master-design` to certify its own final export.
❌ Route raw product sources directly to composition when preparation is required.
❌ Load Product Image Production to repeat an approved destination-compatible master.
❌ List roles without expected outputs and evidence.
❌ Treat a workflow name as proof that owner work was produced.
❌ Load every design skill by default.
❌ Fall back to interactive UI gates for a missing identity specialist.
❌ Allow platform specialists to replace product or engineering owners.
❌ Normalize `PARTIAL`, `NOT_VERIFIED`, or `BLOCKED` into PASS.
```

## Final guard

```text
□ Intent, lifecycle, platform, domain, and artifact state are explicit.
□ Exactly one owner is explicit.
□ Every specialist is narrow and necessary.
□ Execution ownership is explicit when applicable.
□ Raw product-source preparation ownership is explicit.
□ Product Asset Master handoff and reprocessing status are explicit.
□ Prompt translation does not absorb fidelity or lifecycle ownership.
□ Every activated role has one expected output and evidence status.
□ Reviewer facade and domain reviewer are correct for acceptance.
□ Missing evidence or reviewer coverage limits readiness honestly.
□ Owner synthesis cites actual outputs and preserves non-pass states.
```
