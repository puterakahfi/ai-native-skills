# Boundary Declaration Inventory

> Generated evidence for issue #25. This report is not an approval record and does not mutate skill metadata.

- Pinned core: `b60eb2da7d3a31ce0d539f38da58e8a70806c353`
- Contract-backed adapters: **87**
- Missing contract paths: **0**

## Status summary

- `NO_CONTRACT_BOUNDARY`: 78
- `REVIEW_REQUIRED`: 9

## Contract categories

- `architecture`: 10
- `content`: 1
- `context`: 4
- `design`: 25
- `engineering`: 8
- `governance`: 2
- `meta`: 2
- `product`: 6
- `quality`: 12
- `runtime`: 8
- `security`: 2
- `visual-thinking`: 1
- `workflows`: 6

## Adapter audit

### accessibility

- Path: `skills/accessibility/SKILL.md`
- Contract: `contracts/skills/design/accessibility.contract.yaml` @ `0.1.0`
- Type/version: `skill` / `1.1.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

_No boundary-related excerpt detected._

### adaptive-component-design

- Path: `skills/adaptive-component-design/SKILL.md`
- Contract: `contracts/skills/design/adaptive-component-design.contract.yaml` @ `1.1.0`
- Type/version: `skill` / `1.2.1`
- Audit status: `REVIEW_REQUIRED`
- Low-evidence items: `['visual_style_and_brand_expression', 'design_token_definition']`

**Contract covers**

- `component_fitness_diagnosis`
- `context_specific_component_selection`
- `cross_context_component_substitution`
- `responsive_pattern_transformation`
- `navigation_component_adaptation`
- `content_density_adaptation`
- `interaction_mode_adaptation`
- `shared_state_and_semantics_across_variants`
- `overflow_and_disclosure_affordance_behavior`
- `adaptation_boundary_verification`

**Contract delegates**

- `visual_style_and_brand_expression`
- `page_level_macrostructure_selection`
- `design_token_definition`
- `generic_breakpoint_and_fluid_grid_mechanics`
- `implementation_framework_specific_code`
- `product_specific_component_library_mapping`

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L1: # Adaptive Component Design
L3: Select the component pattern that preserves the user task, product meaning, state, semantics, and information priority at the **actual available width**.
L5: Responsive design may change the component family. It must not blindly compress a desktop pattern or replace a fit component merely because its implementation is broken.
L10: narrow cross-context component decision
L11: → adaptive-component-design may advise directly
L13: broad design or redesign
L14: → owner: master-design
L15: → specialist: adaptive-component-design
L16: → implementation: master-engineer when patching
L17: → acceptance: design-review
L20: This skill owns component fitness, adaptation/substitution, shared state semantics, overflow/disclosure affordances, and boundary evidence. It does not own page macrostructure, visual language, product strategy, generic breakpoint mechanics, or final acceptance.
L25: 1. Start from the user task, not the requested component name.
L28: 4. Device labels and common viewport numbers are contexts or samples, not canonical selection rules.
L29: 5. Derive adaptation boundaries from real content failure and passing points.
L30: 6. Separate pattern mismatch from implementation defects.
L31: 7. Preserve a fit component when the issue is local implementation.
L32: 8. Replace an unfit component even when it already exists in the design system.
L33: 9. Keep primary choices discoverable unless a product reason justifies disclosure.
L34: 10. Different component families must preserve product meaning and controlled state.
L35: 11. Verify realistic content, text expansion, states, input modes, and boundary widths.
L36: 12. Screenshots alone do not prove keyboard, dynamic affordances, state equivalence, or the viewport that produced the artifact.
L37: 13. Implemented output requires independent design-review evidence.
L43: PATTERN_MISMATCH
L44: component family does not fit the task, content, or context
L46: IMPLEMENTATION_DEFECT
L47: component family fits but behavior or rendering is broken
L49: CONTENT_PRESSURE
L50: realistic content exceeds the current component contract
L53: available primitive or design system blocks required behavior
L56: A valid rail with a missing left control is an implementation defect. Numerous dynamic searchable choices forced into tabs are a pattern mismatch.
L58: Load `references/component-fitness-and-boundaries.md` for the full decision procedure, component-fitness record, pattern guidance, state-equivalence contract, rail behavior, and boundary verification.
L64: → establish visual-evidence provenance
L66: → inventory realistic content pressure
L67: → identify input/display contexts
L70: → select smallest fit pattern
L71: → identify real adaptation boundary
L72: → define shared state and semantics
L74: → verify target and boundary contexts
L77: ## Component selection principles
L80: - Stable primary discovery categories should remain visibly discoverable.
```

### adr

- Path: `skills/adr/SKILL.md`
- Contract: `contracts/skills/architecture/adr.contract.yaml` @ `0.1.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L110: - Kafka cluster ops overhead — need dedicated platform team ownership
```

### ai-system-design

- Path: `skills/ai-system-design/SKILL.md`
- Contract: `contracts/skills/architecture/ai-system-design.contract.yaml` @ `0.1.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L10: - Trust boundaries (prompt injection vectors)
L25: Covers: RAG architecture and quality gates, chunking strategies, agent memory patterns,
L32: Covers: prompt injection defense, human-in-the-loop design, graceful degradation patterns,
```

### api-contract

- Path: `skills/api-contract/SKILL.md`
- Contract: `contracts/skills/architecture/api-contract.contract.yaml` @ `0.1.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L6: > - Consumer-driven contract testing preferred over provider-defined
L34: └─ Write consumer-driven Pact tests → run in CI against provider
L62: Load [consumer-testing-and-lifecycle.md](references/consumer-testing-and-lifecycle.md) for Pact consumer/provider setup, error response standard, HTTP status codes, deprecation headers, and CI gate setup.
```

### architecture-review

- Path: `skills/architecture-review/SKILL.md`
- Contract: `contracts/skills/quality/architecture-review.contract.yaml` @ `0.1.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L22: 1. Load the product's `engineering-contract.yaml` before starting
L34: - [ ] AI provider follows contract rules?
L48: - [ ] Ports (interfaces) defined in domain layer, adapters in infrastructure?
L85: - [ ] Minimum coverage threshold met?
L86: - [ ] Test type matches layer (unit for domain, integration for adapters)?
L98: - New AI provider
L141: | `import { UserRepo } from '../infrastructure'` in domain layer | Layer boundary violation |
```

### brand-identity-review

- Path: `skills/brand-identity-review/SKILL.md`
- Contract: `contracts/skills/quality/brand-identity-review.contract.yaml` @ `0.1.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L3: Specialist reviewer for the `brand-identity` domain. It plugs into the `design-review` facade and supplies the domain knowledge required to move identity work from `LIMITED REVIEW` to `ADAPTER_COVERED`.
L5: This skill reviews identity systems. It does not generate logos, redesign the mark, or provide legal trademark clearance.
L17: coverage_mode_when_loaded: ADAPTER_COVERED
L27: 5. Large color artwork does not prove small-size, monochrome, inverse, or reproduction quality.
L28: 6. Application mockups do not replace direct inspection of canonical marks and lockups.
L34: 12. Review does not silently become logo generation, redesign, or production.
L75: design-review coverage_mode becomes ADAPTER_COVERED.
L88: Facade normalizes score, coverage, hard gates, verdict, and report.
L90: 7. HANDOFF
L92: identity designer | trademark/legal specialist | ready
L100: no production-ready claim
L110: + monochrome/inverse + lockups + reproduction evidence
L144: coverage_mode: ADAPTER_COVERED
L156: recommended_handoff: <route>
L169: □ Small-size, monochrome, inverse, lockup, and reproduction claims have direct evidence.
```

### bugfix-workflow

- Path: `skills/bugfix-workflow/SKILL.md`
- Contract: `contracts/workflows/bugfix.contract.yaml` @ `None`
- Type/version: `workflow` / `1.1.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L5: A structured bugfix workflow that enforces the right sequence and gates. The phases are invariant across teams — what varies (branch strategy, issue tracker, approval policy) is declared by the product adapter.
L69: Run the full test suite — method is product-defined (local, CI, or both).
L88: Submit code for review — mechanism is product-defined (PR, MR, patch).
```

### business-value-alignment

- Path: `skills/business-value-alignment/SKILL.md`
- Contract: `contracts/skills/product/business-value-alignment.contract.yaml` @ `1.0.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L13: Do not use for: pure syntax/bug fixes; detailed PRD writing (`product-requirements`); architecture records (`adr`).
L41: - Unknown: <needs discovery/experiment>
L89: If the core value claim is mostly `UNKNOWN`, recommend discovery or load `experiment-design` first.
L97: | `EXPERIMENT_FIRST` | Value plausible but key assumptions unverified | `experiment-design` or discovery |
L102: - **Product from zero:** `discovery → business-value-alignment → experiment-design (if needed) → PRD/MVP`
L106: Do not produce a PRD until value hypothesis and success metrics are explicit.
L108: ## Example — Affiliate Product Idea
L112: - User/customer: affiliators managing product recommendations and campaigns
L114: - Value created: less operational overhead and faster campaign production
L118: - Why it matters: validates a possible paid product before full dashboard investment
L124: - Guardrail: generated campaign accuracy/trust does not regress
L142: 4. **Skipping uncertainty.** If important claims are unknown, say so and recommend discovery first.
```

### code-review-workflow

- Path: `skills/code-review-workflow/SKILL.md`
- Contract: `contracts/workflows/code-review.contract.yaml` @ `None`
- Type/version: `workflow` / `2.1.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L5: ## Core boundary
L12: Screenshot ≠ runtime, keyboard, or hidden-state evidence.
L22: + required repository/product/policy approvals are satisfied
L36: 9. LIMITED REVIEW cannot approve a complete specialist-domain claim.
L37: 10. Run security review when trust boundaries or sensitive behavior change.
L39: 12. Agent/author PR text is not owner approval.
L53: product_design_locks: []
L66: runtime: []
L71: approval_policy: <product-defined>
L75: Missing contracts do not automatically block every review. Record the gap and use repository conventions, specifications, architecture, and declared locks. Block when the gap prevents a required domain verdict or authority decision.
L84: repository and product instructions
L86: product design system, locks, and required assets
L92: Claims are not evidence. Submission text such as “responsive tested”, “owner approved”, or “risk accepted” requires the relevant evidence or decision source.
L123: Do not infer “no design change” because only CSS, tokens, props, content data, templates, assets, or generation configuration changed.
L125: Do not infer a claim is authoritative because it appears in the latest commit or PR body.
L137: layer/module boundaries
L138: data ownership and migrations
L142: test strategy and regression coverage
L162: references/design-review-adapter.md
L165: The adapter owns design-change triggers, facade route fields, evidence policy, reviewer coverage, verdict mapping, and design handoff. Do not maintain a duplicate design scorecard here.
L187: edge cases and boundary inputs
L202: Load `security-review` and `threat-modeling` when trust boundaries, authentication/authorization, secrets/tokens, untrusted input, sensitive data, permissions, tenancy, isolation, or high-impact behavior are affected.
L234: missing required specialist reviewer
L264: That is not a contradiction; it preserves the authority boundary.
L286: - Design: [facade verdict, evidence coverage, primary-domain coverage]
L303: - [risk, authority record, owner, mitigation, expiry]
L306: - [missing tests, preview, state, runtime, export, reviewer, or decision source]
L313: Do not approve with “looks good”, “CI passed”, a high partial design score, author self-approval, or missing authority evidence.
L319: | Approve because CI is green | CI does not prove architecture, design, behavior, or authority |
L321: | Treat screenshot as interaction/runtime proof | Hidden behavior remains unverified |
L322: | Run a hardcoded design checklist | Bypasses facade routing and domain ownership |
L323: | Give specialist-domain approval from universal gates | Required reviewer coverage is missing |
L324: | Treat PR body as product-owner approval | Agent/author summary is not authority |
L328: | Merge without explicit final statuses | Responsibility and authority are ambiguous |
```

### content-strategy

- Path: `skills/content-strategy/SKILL.md`
- Contract: `contracts/skills/content/content-strategy.contract.yaml` @ `1.0.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L7: Before writing a single word of copy, declare the Tone Card for the product.
L46: - Tone Card template (declare per product before writing)
```

### context-engineering

- Path: `skills/context-engineering/SKILL.md`
- Contract: `contracts/skills/context/context-engineering.contract.yaml` @ `0.1.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L15: - Setting up a new repo or product for AI agents
L30: product-level:   engineering-contract.yaml, ui-design-system-contract.yaml
L37: 3. Product-level engineering contract
L69: ## Agent Boundaries (must escalate to human)
L75: ## Out of Scope (agent must not touch)
L83: - [ ] Agent boundary rules present — what must escalate to human?
L95: # Product Context
L106: # Agent Boundaries
L129: [ ] Agent boundaries not defined
L166: | No agent boundary rules | Agent makes architecture decisions alone |
L169: | "Be careful with production" as a rule | Not actionable — write the actual constraint |
```

### context-manager

- Path: `skills/context-manager/SKILL.md`
- Contract: `contracts/skills/context/context-manager.contract.yaml` @ `0.1.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L13: - When onboarding an agent to a new product
L26: product:
L27: engineering_contract: products/<product>/engineering-contract.yaml
L28: design_contract: products/<product>/ui-design-system-contract.yaml
L29: blueprint: products/<product>/blueprint.md
L32: agents_md: products/<product>/AGENTS.md
L45: ref: ""           # app/module within product
L50: stale_after: ""   # staleness policy — product_defined
L71: Missing: acceptance_criteria → request from product-manager skill
L79: After resolving, validate before handoff:
L89: **Gate:** Incomplete context = blocked handoff. Not degraded execution.
L100: **Product:** <product>
L111: **Out of scope:**
```

### dark-light-theming

- Path: `skills/dark-light-theming/SKILL.md`
- Contract: `contracts/skills/design/dark-light-theming.contract.yaml` @ `1.0.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L5: 1. **Preserve existing theme infra** — never add a second theme system on top of an existing one. If `data-theme` or CSS custom properties are already in place, extend them; do not create parallel systems.
```

### data-modeling

- Path: `skills/data-modeling/SKILL.md`
- Contract: `contracts/skills/engineering/data-modeling.contract.yaml` @ `1.0.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L37: Renaming/removing a column in production?   → Expand-Contract migration — see normalization-and-migration.md
```

### decision-making

- Path: `skills/decision-making/SKILL.md`
- Contract: `contracts/skills/product/decision-making.contract.yaml` @ `1.0.0`
- Type/version: `skill` / `1.1.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

_No boundary-related excerpt detected._

### decision-provenance

- Path: `skills/decision-provenance/SKILL.md`
- Contract: `contracts/skills/quality/decision-provenance.contract.yaml` @ `1.0.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `REVIEW_REQUIRED`
- Low-evidence items: `['proving_runtime_or_design_quality']`

**Contract covers**

- `material_decision_claim_verification`
- `source_attribution`
- `decision_domain_authority_matching`
- `explicit_supersession_and_conflict_detection`
- `scope_lock_route_approval_status_and_ownership_claims`
- `policy_and_required_approval_preservation`
- `decision_ledger_output`

**Contract delegates**

- `making_product_or_design_decisions_for_the_owner`
- `bypassing_legal_security_repository_or_organizational_policy`
- `proving_runtime_or_design_quality`
- `inventing_missing_decision_sources`
- `treating_agent_authored_text_as_owner_approval`

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L1: # Decision Provenance
L3: Verify decision claims before they change scope, locks, approval state, routing, public status, repository ownership, or delivery behavior.
L7: ```text
L8: claim about a decision
L9: → locate the source
L10: → classify authority
L11: → resolve scope and supersession
L12: → detect conflicts
L13: → emit VERIFIED, NOT_VERIFIED, CONFLICTED, or NON_AUTHORITATIVE
L14: → act only inside the verified decision boundary
L17: An agent must never convert its own summary, inference, PR body, commit message, or previous output into user approval merely because it is recent or confidently worded.
L21: ```text
L22: 1. Every material decision claim must have a source reference.
L23: 2. “The user approved” requires an attributable user or authorized-owner source.
L24: 3. Agent-authored notes, PR bodies, commit messages, and generated specs are not approval by themselves.
L25: 4. Newest does not mean authoritative; authority and explicit supersession control precedence.
L26: 5. Silence, absence of objection, or branch mergeability is not approval.
L27: 6. A direct instruction applies only to the scope it actually names.
L28: 7. Scope expansion, lock removal, destructive action, and approval bypass require verified authority.
L29: 8. Conflicting authoritative decisions remain CONFLICTED until resolved or explicitly superseded.
L30: 9. Missing provenance is NOT_VERIFIED, not inferred consent.
L31: 10. Never invent quotes, timestamps, message IDs, issue comments, or decision owners.
L32: 11. Preserve repository, legal, security, and organizational approval requirements.
L33: 12. Delivery claims must cite the actual decision ledger used by the run.
L38: Load before acting on claims such as:
L40: ```text
L41: “the user explicitly approved this route”
L42: “this feature is now in scope”
L43: “the old lock was removed”
L45: “the PR body says this is production-ready”
L46: “this dependency is required”
L47: “the owner approved deleting this file”
L48: “another agent already decided this”
L51: Use it in redesign, feature, product, review, release, migration, destructive repository, and multi-agent coordination workflows.
L53: ## Decision domains
L55: ```text
L56: scope
L57: preservation lock
L58: route or lifecycle
L59: architecture or product contract
```

### deployment-workflow

- Path: `skills/deployment-workflow/SKILL.md`
- Contract: `contracts/workflows/deployment.contract.yaml` @ `None`
- Type/version: `workflow` / `2.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L5: ## Core boundary
L14: provider deployment success
L21: The workflow owns deployment lifecycle, records, gates, and operational handoffs. Product adapters own provider commands, protected-environment policy, authorization authority, secret management, health checks, verification windows, rollback mechanisms, and emergency procedures.
L33: 8. Authorization must cover the exact candidate, environment, action, scope, and applicable time boundary.
L37: 12. Capture provider deployment ID and actual deployed artifact identity.
L39: 14. Provider success alone cannot confirm application health.
L50: Use for staging, production, preview, canary, regional, internal, customer, data-processing, or other deployment environments when a release candidate will cause an external side effect.
L54: → product-development-workflow release phase or git-workflow
L63: Do not assume staging is always unprotected or production is the only environment requiring authorization.
L79: deployment_provider: <provider/mechanism>
L96: confirmation_owner: <owner/policy>
L97: rollback_owner: <owner/policy>
L104: Unknown required context remains a blocker. Do not fabricate artifact identities, approvals, provider IDs, environment evidence, or rollback outcomes.
L116: resolve environment, provider, config/secrets policy, observability,
L117: verification window, rollback, owners, and change window
L125: execute product-defined mechanism
L190: - emergency rollback boundary;
L197: → return to release/implementation/review/context owner
L211: → route incident/operational recovery as applicable
L256: ❌ CI green → deploy production.
L258: ❌ PR body says owner approved → authorization accepted.
L259: ❌ Approval for staging reused for production.
L262: ❌ Provider says success → app confirmed healthy.
L274: □ Environment, mechanism, health plan, rollback, and owners are explicit.
L275: □ Authorization covers exact candidate, environment, action, scope, and time boundary.
L279: □ Provider success is not confused with application health.
```

### design-brand

- Path: `skills/design-brand/SKILL.md`
- Contract: `contracts/skills/design/design-brand.contract.yaml` @ `1.0.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L4: > 1. Brand file = locked. Do not override brand tokens with genre picks.
L5: > 2. Foundation gates still apply — brand does not exempt from F1–F7.
L16: design-brand        ← locked system (client/product — overrides genre picks)
L42: - Client/product has existing design system
```

### design-color

- Path: `skills/design-color/SKILL.md`
- Contract: `contracts/skills/design/color-theory.contract.yaml` @ `1.0.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `REVIEW_REQUIRED`
- Low-evidence items: `[]`

**Contract covers**

- `hue_saturation_value_decisions`
- `palette_construction`
- `color_harmony_rules`
- `color_psychology_validation`
- `genre_to_palette_mapping`

**Contract delegates**

- `contrast_ratio_wcag`
- `semantic_token_naming`
- `dark_light_switching`
- `component_level_color`

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L1: # Design Color Skill
L3: > **HARD RULES:**
L4: > 1. Genre first — color palette derives from genre, not the reverse.
L5: > 2. Max 3 roles: bg + ink + accent. Every additional color needs a semantic job.
L8: > 5. Never hardcode hex in components — always semantic token (see design-system).
L12: ## Color as Layer 1.5
L15: Layer 1:   Canvas        — background color field (this skill)
L16: Layer 1.5: Color system  — palette + roles (this skill)
L17: Layer 2:   Typography    — type on top of color field
L20: Color is not decoration — it IS the canvas everything else sits on.
L21: Wrong color = wrong temperature = wrong mood = wrong genre.
L26: ## Core Decisions (in order)
L29: 1. TEMPERATURE  → warm / cool / neutral? (follows genre)
L30: 2. VALUE        → light / dark / mid? (follows theme default)
L31: 3. PALETTE      → bg + surface + ink steps (3–5 values)
L32: 4. ACCENT       → one color, one job
L33: 5. HARMONY      → how colors relate (complementary, analogous, monochromatic)
L34: 6. ROLES        → map palette to semantic tokens
L43: | Color theory foundations | `references/theory.md` | Understanding hue/value/saturation |
L44: | Palette construction | `references/palette.md` | Building a palette from scratch |
L45: | Genre-to-palette map | `references/genre-palette-map.md` | Genre-driven color selection |
L46: | Color psychology | `references/psychology.md` | Emotional + cultural color meaning |
L49: skill_view(name='design-color', file_path='references/theory.md')
L50: skill_view(name='design-color', file_path='references/palette.md')
L51: skill_view(name='design-color', file_path='references/genre-palette-map.md')
L52: skill_view(name='design-color', file_path='references/psychology.md')
L57: ## Boundary Map
L60: design-color covers:          others cover:
L61: Hue / saturation / value      Contrast ratio WCAG (readability)
L62: Palette construction          Token architecture (design-system)
L63: Color harmony rules           Dark/light switching (dark-light-theming)
L64: Color psychology + mood       Semantic role naming (design-system)
L65: Genre → palette mapping       Slop gate: no amber (design-genre/zen)
L72: > **REMINDER:** Genre → temperature → palette → accent → roles. In that order.
L73: > Accent = one color, one job. Temperature must be consistent across palette.
```

### design-depth

- Path: `skills/design-depth/SKILL.md`
- Contract: `contracts/skills/design/design-depth.contract.yaml` @ `2.1.0`
- Type/version: `skill` / `1.1.0`
- Audit status: `REVIEW_REQUIRED`
- Low-evidence items: `[]`

**Contract covers**

- `depth_need_assessment`
- `surface_and_elevation_relationships`
- `atmosphere_and_imagery_integration`
- `overlap_and_layer_architecture`
- `optional_typography_interleave`
- `responsive_depth_fallback`
- `depth_effect_restraint`

**Contract delegates**

- `illustration_creation`
- `product_specific_elevation_token_values`
- `motion_timing_and_reduced_motion_implementation`
- `page_macrostructure`
- `independent_design_acceptance`

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L1: # Design Depth
L3: Depth is optional. Use it only when it improves separation, focus, imagery integration, spatial storytelling, interaction state, or emotional meaning.
L8: 1. Assess whether depth is needed before selecting techniques.
L9: 2. Flat, shallow, layered, and deep are all valid.
L11: 4. Every depth technique needs a named role.
L12: 5. Do not require artificial depth metadata for flat components.
L14: 7. Typography interleave is optional and requires readability plus fallback.
L15: 8. Effects must not replace foundation, content, composition, or product proof.
L16: 9. Performance, reduced motion, responsive behavior, and accessibility constrain depth.
L17: 10. Rendered evidence is required before acceptance.
L20: ## Depth need assessment
L23: depth_need_assessment:
L24: target_surface:
L25: selected_design_direction:
L28: available_imagery_or_assets: []
L33: depth_value:
L35: recommended_mode: <flat | shallow | layered | deep>
L40: hierarchy, grouping, and flow are clear without perceptual layering
L43: limited surface separation, focus, or state distinction is needed
L45: LAYERED
L46: meaningful overlap, imagery, atmosphere, or interaction planes are active
L49: spatial storytelling or complex imagery requires several coordinated planes
L52: Do not select layered or deep mode merely because the page feels flat or not premium enough. Diagnose hierarchy, composition, content, and asset quality first.
L54: ## Depth roles
L66: establishes the primary readable/task layer
L68: ATMOSPHERE
L71: IMAGERY_INTEGRATION
L72: combines photography, illustration, or product artifacts with content
L78: expresses modal, popover, drawer, tooltip, or other layered interaction
L91: surface contrast or border
L92: elevation and shadow
L93: overlap and crop
L99: typography interleave
L100: parallax or motion depth
L110: valid when imagery integration or composition benefits
L112: shadow/elevation
L116: valid when it creates a specific light, atmosphere, or separation role
L118: typography interleave
L119: valid only when reading order and responsive fallback remain clear
L125: ## Layer stack
```

### design-foundation

- Path: `skills/design-foundation/SKILL.md`
- Contract: `contracts/skills/design/design-foundation.contract.yaml` @ `1.0.0`
- Type/version: `skill` / `1.5.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L11: design-brand         ← identity, tokens, assets, product rules
L13: design workflows     ← audit, review, refinement, redesign, production
L30: and sequence communicate what belongs together.
L67: Use these 13 principles as cross-cutting composition lenses. They do not create 13 additional release gates; they deepen reasoning and map back to `F1–F10`.
L143: - shadows, blur, glass, borders, and gradients do not replace hierarchy or grouping
L144: - sticky, fixed, floating, or overlapping layers do not hide required content or actions
L145: - interactive layers preserve object/task context and provide a clear continuation or recovery path
L172: A design does not need to support unlimited content. It must honestly define the supported range and provide a meaningful strategy at its boundaries.
L174: Load `references/content-resilience.md` for variable-content products, reusable templates, catalogs, tables, forms, collections, generated/user-authored content, localization, text scaling, or optional media. Load `references/content-resilience-fixtures.md` for cross-surface regression and bias testing.
L205: Exact hues, icon library, component anatomy, motion, radius, and token names belong to the design system, brand, or artifact implementation. The semantic relationship does not.
L229: - content quantity does not automatically require less or more space; evaluate composition and context
L248: - the next intended region is discoverable
L249: - reading order and DOM/task order do not conflict
L251: - content adaptation does not hide or reorder the next valid action without reason
L263: - labels, titles, content, status, and actions do not zig-zag accidentally
L265: - semantic state does not degrade into color-only dots on constrained layouts
L277: | F2 Grouping | Do proximity, common region, figure-ground, containment, and presence show what belongs together? | Related items detach, optional content leaves broken relationships, or foreground/background ownership becomes unclear. |
L287: **A verified foundation failure blocks release approval. A source-only suspicion is `NOT_VERIFIED` until rendered or runtime evidence exists.**
L291: ## Ownership and Handoff
L299: evaluates F1–F10 with evidence and reports coverage/verdict through canonical IDs
L306: content policies, and product-specific rules
L309: load foundation before direction/production and classify the correct fix layer
L312: own runtime announcement, validation behavior, interaction safety,
L320: ## What Foundation Does Not Dictate
L324: Genre/brand/product own expression and declared limits.
L326: FOUNDATION                         GENRE / BRAND / PRODUCT
L347: | Core graphic design principle lenses and F1–F10 mapping | `references/core-graphic-design-principles.md` | Foundation learning, visual direction, production, design review, and principle-specific diagnosis |
L348: | Principles and composition rationale | `references/principles.md` | Direction, planning, production |
L351: | Cross-genre figure-ground regression fixtures | `references/figure-ground-fixtures.md` | Skill evaluation and bias checks across minimal, dense, expressive, product, static, and presentation surfaces |
L352: | Content bounds, stress states, adaptation strategies, and evidence | `references/content-resilience.md` | Variable-content products, reusable templates, catalogs, tables, forms, localization, text scaling, optional media, generated/user content |
L354: | Semantic state taxonomy, channel contract, color/icon/label roles, and ownership | `references/semantic-status-encoding.md` | Validation, health, risk, evidence, progress, maturity, availability, verdict, or destructive consequence |
```

### design-genre

- Path: `skills/design-genre/SKILL.md`
- Contract: `contracts/skills/design/design-genre.contract.yaml` @ `1.1.0`
- Type/version: `skill` / `1.3.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L3: Genre is an expression family, not a product-category shortcut, palette preset, or substitute for design foundation.
L6: resolved foundation + product intent + audience + content + context
L16: 1. Resolve design-foundation and valid brand/product locks first.
L19: 3. Product category is one signal, never an automatic genre.
L24: 8. Do not mix multiple genres as uncontrolled per-section variety.
L25: 9. Insufficient or conflicting evidence remains unresolved; do not silently default.
L35: foundation_handoff: <required>
L36: product_intent: <required>
L61: These are not mutually exclusive product categories. A product may use one primary family with one bounded influence, for example:
L78: audience_and_product_fit:
L96: product positioning and maturity
L102: existing brand/product equity
L114: one candidate clearly best supports product, content, context, and equity
L122: → do not silently choose editorial or modern-minimal
L149: Premium must be translated into specific qualities such as material restraint, confidence, precision, craft, depth, editorial pacing, service detail, or high-fidelity product proof.
L157: brand_and_product_locks: []
L186: wellness product automatically routed to playful or zen
L196: return to foundation, product intent, content, context, and candidate comparison
L216: □ Product category was treated as a signal, not a shortcut.
L220: □ References were transformed through product content and constraints.
```

### design-iconography

- Path: `skills/design-iconography/SKILL.md`
- Contract: `contracts/skills/design/iconography.contract.yaml` @ `1.0.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `REVIEW_REQUIRED`
- Low-evidence items: `[]`

**Contract covers**

- `icon_family_selection`
- `style_consistency_rules`
- `sizing_optical_alignment`
- `genre_to_icon_mapping`
- `a11y_attribute_rules`

**Contract delegates**

- `svg_component_implementation`
- `icon_animation`
- `token_sizing_values`

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L1: # Design Iconography Skill
L3: > **HARD RULES:**
L4: > 1. Icons support text — they do not replace it (exception: universally understood icons only).
L5: > 2. Style consistency — one icon family per product. Never mix Lucide + Heroicons + Material.
L6: > 3. Optical sizing — icons at 16px need different weight than 24px. Not just scale-down.
L7: > 4. Touch targets — minimum 44×44px tap area even if icon visually smaller.
L8: > 5. All icons need aria-label or aria-hidden — never naked SVG without a11y attr.
L12: ## Icons as Layer 4.5
L15: Layer 4:   Components   — buttons, cards, nav
L16: Layer 4.5: Iconography  — icons within components
L17: Layer 5:   Motion       — icon animations (loading, transition)
L19: Icons are micro-communication — they carry meaning at a glance.
L20: Wrong icon style = wrong genre signal. Missing icon = missed affordance.
L21: Decorative icon without text = accessibility failure.
L29: 1. NECESSITY  → does this need an icon, or does text suffice?
L30: 2. STYLE      → which icon family matches the genre?
L31: 3. SIZE       → 16 / 20 / 24 / 32px — contextual sizing
L33: 5. ALIGNMENT  → optical center, not mathematical center
L34: 6. A11Y       → aria-label (interactive) or aria-hidden (decorative)
L43: | Icon family selection + genre map | `references/families.md` | Picking icon style |
L44: | Sizing, weight, optical alignment | `references/sizing-alignment.md` | Using icons in components |
L45: | A11y + usage rules | `references/a11y-usage.md` | Before implementing any icon |
L48: skill_view(name='design-iconography', file_path='references/families.md')
L49: skill_view(name='design-iconography', file_path='references/sizing-alignment.md')
L50: skill_view(name='design-iconography', file_path='references/a11y-usage.md')
L55: ## Boundary
L58: design-iconography covers:     others cover:
L59: Icon family selection          SVG component implementation (ui-components)
L60: Style consistency rules        Icon animation (motion-design)
L61: Sizing + optical alignment     Token sizing values (design-system)
L62: Genre-to-icon mapping          WCAG contrast for icon color (readability)
L63: A11y attribute rules
L69: > **REMINDER:** One family. Text + icon together. aria-label or aria-hidden — always.
```

### design-interaction

- Path: `skills/design-interaction/SKILL.md`
- Contract: `contracts/skills/design/design-interaction.contract.yaml` @ `1.0.0`
- Type/version: `meta-skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L6: > 3. Never hand-roll patterns that ux-patterns-for-developers already covers.
L10: ## What This Port Covers
L15: **Does NOT cover:**
L22: ## Adapter Skills — Load Per Concern
L24: | Concern | Adapter | When to load |
```

### design-layout

- Path: `skills/design-layout/SKILL.md`
- Contract: `contracts/skills/design/design-layout.contract.yaml` @ `2.0.0`
- Type/version: `meta-skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L10: ## What This Port Covers
L15: **Does NOT cover:**
L22: ## Adapter Skills — Load Per Concern
L24: | Concern | Adapter | When to load |
L27: | Breakpoints + fluid grid | `responsiveness` | Phase 4 produce, any responsive concern |\n| Component substitution by viewport | `adaptive-component-design` | When the same component does not fit every width |
L31: ### How to load an adapter
```

### design-patterns

- Path: `skills/design-patterns/SKILL.md`
- Contract: `contracts/skills/architecture/design-patterns.contract.yaml` @ `0.1.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L33: | Need different algorithm at runtime | Strategy |
L34: | Incompatible interface to integrate | Adapter |
L56: | Leaky abstraction | Adapter exposes internal types | Translate to domain types at boundary |
L62: - [Creational & Structural Patterns](references/creational-structural.md) — Factory Method, Builder, Singleton, Adapter, Decorator, Facade
```

### design-refinement

- Path: `skills/design-refinement/SKILL.md`
- Contract: `contracts/skills/quality/design-refinement.contract.yaml` @ `1.2.0`
- Type/version: `workflow` / `2.1.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L5: This workflow owns the refinement boundary, preservation lock, change budget, defect routing, targeted verification, focused re-review, and learning handoff. The design-review facade and governing reviewers own gate meaning and acceptance. Specialist skills own narrow correction reasoning.
L10: 1. Begin from canonical FAIL or PARTIAL findings with sufficient reviewer coverage.
L22: 13. LIMITED or ROUTE_ELSEWHERE coverage cannot certify a specialist correction.
L35: primary-domain coverage is BUILT_IN or ADAPTER_COVERED
L53: → local implementation owner under the same refinement lock
L55: specialist-domain coverage is insufficient
L56: → required domain reviewer/specialist
L82: coverage_mode: <inherited>
L91: canonical findings, evidence, coverage, governing reviewers, accepted direction
L101: system constraint | local visual defect | domain specialist defect
L104: correct owner and layer, inside budget
L117: accepted, residual gap, redesign route, local owner, or specialist
L131: → local implementation owner
L139: → design-system/ui-components + implementation owner
L143: → relevant visual specialist
L145: DOMAIN_SPECIALIST_DEFECT
L146: correction requires specialist-domain knowledge
L147: → governing domain reviewer/specialist
L150: Visible symptoms do not choose the owner. Read the full governing gate and component contract first.
L192: adaptation or substitution boundary
L200: Do not replace a valid rail merely because one arrow is missing. Do not preserve tabs when realistic content proves the component family unfit.
L232: affected target and boundary widths, themes, states, inputs,
L233: focus/semantics, overflow, runtime, realistic content
L242: brand identity or another specialist domain
L270: coverage_mode: <inherited>
L282: only explicit non-blocking gaps outside the required refinement boundary
L288: stop and route to redesign, emergency local fix, or specialist
L302: Promote only generalized reasoning to the correct owner. Product names, paths, accidental breakpoints, local class names, and raw case history remain local.
L309: coverage_mode: <mode>
L321: handoff: <none | verification | local implementation | redesign | specialist>
```

### design-review

- Path: `skills/design-review/SKILL.md`
- Contract: `contracts/skills/quality/design-review.contract.yaml` @ `0.2.0`
- Type/version: `skill` / `3.3.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L3: Unified review entry point for built-in and adapter-covered design domains.
L5: The facade owns classification, reviewer routing, canonical gate resolution, applicability, evidence normalization, scoring, coverage, verdict, and reporting. Specialist reviewers own domain knowledge, full gate definitions, evidence interpretation, and domain hard gates.
L20: 11. Do not turn taste or one style into a universal gate.
L21: 12. High score + low coverage is not release approval.
L23: 14. Unsupported domains require an adapter or an explicitly limited review.
L25: 16. Review does not silently become redesign or implementation.
L41: required_assets   logos, products, people, copy, price, contact, claims, legal content
L43: domain_reviewers  optional specialist reviewers required by the domain
L52: Resolve domain, profile, artifact state, context, depth, and coverage mode.
L54: Load facade-boundary.md only when scope or extension behavior matters.
L80: hard-gate results, evidence coverage, and primary-domain coverage.
L84: Report canonical IDs, governing reviewers, findings, limitations, and handoff.
L91: → score + coverage → report
L94: Do not score until route, domain coverage, selected canonical IDs, and evidence are explicit.
L101: facade-boundary.md only for scope/extension decisions
L126: Never load every reference defensively. A completed phase output is the handoff context for the next phase.
L131: gate-registry.yaml   canonical machine-readable identity and ownership
L134: owner reference      full review question, evidence rules, and correction knowledge
L142: new meaning    → register a new ID and owner
L147: ## Coverage
L152: digital-interface    web, mobile, desktop, and responsive product UI
L157: Available external adapter:
L160: brand-identity       brand-identity-review · namespace BI · ADAPTER_COVERED
L177: Full only with built-in or adapter primary-domain coverage.
L181: inputs, runtime/export/domain evidence, and sufficient primary coverage.
L205: RI1 runtime integrity
L222: A build is not visual verification. A screenshot is not interaction or runtime verification. Universal evidence is not specialist-domain proof.
L230: Evidence coverage: verified applicable weight / all applicable selected weight
L231: Primary-domain coverage: BUILT_IN | ADAPTER_COVERED | LIMITED | ROUTE_ELSEWHERE
L235: PASS             score >= 8, hard gates pass, sufficient coverage
L243: ## Output and Handoff
L250: canonical gate IDs and governing owners
L251: score, evidence coverage, and primary-domain coverage
L254: scope limitations and recommended handoff
L257: Handoff:
L263: domain specialist  unsupported domain knowledge and gates
L264: legal specialist   trademark/legal questions outside design review
L271: □ Built-in or adapter coverage is explicit.
L279: □ Evidence and primary-domain coverage are both shown.
```

### design-spacing

- Path: `skills/design-spacing/SKILL.md`
- Contract: `contracts/skills/design/spacing.contract.yaml` @ `1.0.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `REVIEW_REQUIRED`
- Low-evidence items: `[]`

**Contract covers**

- `visual_rhythm_decisions`
- `ma_intentional_space`
- `spatial_hierarchy_logic`
- `breathing_room_vs_dead_space`

**Contract delegates**

- `token_values`
- `8px_grid_rules`
- `css_var_declarations`

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L3: > **HARD RULES:**
L4: > 1. Spacing is not decoration — it IS the rhythm of the page.
L5: > 2. Ma (間): space must have intent. Dead space ≠ breathing room.
L6: > 3. Vertical rhythm first — section spacing > component spacing > element spacing.
L7: > 4. Never mix token and raw px — all spacing values from design-system tokens.
L8: > 5. Breathing room is earned — sparse content needs LESS space, not more.
L16: Layer 2:   Typography     — type sets voice and rhythm
L17: Layer 3:   Layout         — macrostructure, grid
L18: Layer 3.5: Spacing        — rhythm, breathing room, hierarchy via space
L19: Layer 4:   Components     — elements placed within the spaced layout
L22: Spacing IS the rhythm. Consistent vertical cadence = page feels composed.
L28: ## Core Decisions (in order)
L31: 1. RHYTHM     → section-to-section spacing (largest unit)
L32: 2. BREATHING  → component-to-component spacing (medium unit)
L34: 4. MA         → intentional empty space (not absence — presence)
L35: 5. HIERARCHY  → more space above = new section signal
L44: | Visual rhythm + section spacing | `references/rhythm.md` | Section/layout spacing |
L45: | Ma principle + breathing room | `references/ma.md` | Zen/minimalist spacing |
L46: | Spatial hierarchy rules | `references/hierarchy.md` | Component/element spacing |
L49: skill_view(name='design-spacing', file_path='references/rhythm.md')
L51: skill_view(name='design-spacing', file_path='references/hierarchy.md')
L56: ## Boundary with Design-System
L59: design-spacing covers:        design-system covers:
L60: Why this amount of space?     What token value to use?
L61: Rhythm + cadence decisions    8px grid enforcement
L62: Ma — intentional emptiness    CSS var declarations
L63: Breathing room vs dead space  spacing scale (--sp-1 to --sp-12)
L64: Spatial hierarchy logic       No raw px rule
L69: > **REMINDER:** Rhythm first. Ma is presence, not absence. Token from design-system, decision from here.
```

### design-strategy

- Path: `skills/design-strategy/SKILL.md`
- Contract: `contracts/skills/design/design-strategy.contract.yaml` @ `1.0.0`
- Type/version: `meta-skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L5: > 2. CRO only when business goal is conversion — do not add CTAs to identity/portfolio pages.
L6: > 3. Copy is design — run copywriting adapter before locking layout.
L10: ## What This Port Covers
L15: **Does NOT cover:**
L22: ## Adapter Skills — Load Per Concern
L24: | Concern | Adapter | When to load |
```

### design-system

- Path: `skills/design-system/SKILL.md`
- Contract: `contracts/skills/design/design-system.contract.yaml` @ `1.0.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L5: > Adapter skills: `dark-light-theming`, `accessibility`
L101: □ Border radius declared — 1–2 values for the product
```

### design-typography

- Path: `skills/design-typography/SKILL.md`
- Contract: `contracts/skills/design/typography.contract.yaml` @ `1.0.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `REVIEW_REQUIRED`
- Low-evidence items: `['leading_tracking_rhythm']`

**Contract covers**

- `typeface_personality_and_selection`
- `display_body_pairing`
- `modular_scale_selection`
- `hierarchy_h1_to_caption`
- `leading_tracking_rhythm`
- `font_rendering_antialiasing`
- `genre_to_typeface_mapping`

**Contract delegates**

- `contrast_ratio_wcag`
- `characters_per_line`
- `minimum_font_size_px`

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L5: > 2. Type pair first — decide display + body before any sizing.
L6: > 3. Scale before sizing — pick a modular scale, then derive all sizes from it. No arbitrary px.
L7: > 4. Hierarchy is structural, not decorative — H1/H2/H3 differences must be meaningful.
L8: > 5. Genre governs personality — load design-genre before picking typefaces.
L16: Layer 2: Typography    — type sets the voice, rhythm, and structure of the page
L30: 1. PERSONALITY  → what does this brand/page sound like typographically?
L31: 2. PAIR         → display typeface + body typeface
L32: 3. SCALE        → modular scale ratio (1.250 / 1.333 / 1.414 / 1.618)
L33: 4. HIERARCHY    → H1 / H2 / H3 / body / caption — size + weight mapping
L34: 5. RHYTHM       → line-height, paragraph spacing, letter-spacing
L35: 6. RENDERING    → font-weight, font-variation-settings, antialiasing
L44: | Typeface selection + pairing theory | `references/selection-pairing.md` | Picking typefaces |
L45: | Modular scale + hierarchy rules | `references/scale-hierarchy.md` | Setting type sizes |
L46: | Rhythm, spacing, rendering | `references/rhythm-rendering.md` | Fine-tuning details |
L47: | Genre-to-typeface mapping | `references/genre-typeface-map.md` | Genre-driven selection |
L50: skill_view(name='design-typography', file_path='references/selection-pairing.md')
L51: skill_view(name='design-typography', file_path='references/scale-hierarchy.md')
L52: skill_view(name='design-typography', file_path='references/rhythm-rendering.md')
L53: skill_view(name='design-typography', file_path='references/genre-typeface-map.md')
L58: ## Boundary with Readability Skill
L61: design-typography covers:          readability covers:
L62: Typeface personality               Contrast ratio (WCAG)
L63: Display vs body pairing            Characters per line (CPL)
L64: Modular scale selection            Minimum font size (px)
L65: Hierarchy (H1→H2→H3→body)         Line height for reading comfort
L66: Type rhythm and spacing            Cognitive ease (Flesch-Kincaid)
L67: Font weight + variation            Density scoring
L68: Genre-driven typeface choice
L77: > **REMINDER:** Genre first → pair → scale → hierarchy → rhythm → rendering. In that order.
```

### design-visual

- Path: `skills/design-visual/SKILL.md`
- Contract: `contracts/skills/design/design-visual.contract.yaml` @ `1.1.0`
- Type/version: `meta-skill` / `1.1.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L3: Resolve visual expression from product context and the selected design direction. Do not begin from a fixed genre recipe or load every aesthetic skill by default.
L8: 1. Foundation and valid product/brand locks precede visual expression.
L11: 4. Load only adapters required by active visual concerns.
L17: 10. Repeated visual treatments need a system or product role.
L18: 11. Do not invent proof, content, assets, or product UI.
L27: foundation_handoff: <required>
L28: product_intent: <required>
L46: 2. Apply brand, product, asset, and design-system locks.
L49: 5. Load only the relevant adapters.
L56: ## Adapter selection
L58: | Active concern | Adapter |
L70: Do not load `design-depth` merely because the user says “premium”. Do not load `motion-design` when the direction is intentionally still. Do not defer readability until the end when viewing context already constrains the design.
L106: generic product-independent hero
L113: reference structure copied without product-specific transformation
L123: → preserve coherent system roles and product equity
L127: Do not solve generic design by adding more random effects.
L129: ## Handoff
L132: visual_handoff:
L134: loaded_adapters: []
L135: specialist_decisions: []
L143: The design owner receives one reconciled handoff, not a list of disconnected specialist opinions.
L150: □ Only active adapters were loaded.
```

### diagram-architect

- Path: `skills/diagram-architect/SKILL.md`
- Contract: `contracts/skills/visual-thinking/diagram-architect.contract.yaml` @ `0.1.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L13: Do not jump straight to Mermaid, SVG, Excalidraw, or ASCII until the diagram intent, view, nodes, edges, boundaries, constraints, and verification checklist are clear.
L20: - visualize an architecture, workflow, runtime, profile sync, or session model
L21: - explain a core/app/skill/runtime boundary visually
L22: - create a contract-to-adapter map
L23: - create a responsibility or ownership map
L26: Do not use for pure UI mockups, marketing visuals, or illustration unless a conceptual diagram is needed first.
L31: 2. **Build renderer-agnostic spec.** Define boundaries, nodes, edges, legend, constraints, and verification.
L38: 5. **Verify.** Check required nodes, edges, boundaries, labels, and constraints are visible and not misleading.
L46: type: runtime_topology
L49: boundaries:
L50: - id: boundary_id
L51: label: Boundary Label
L52: meaning: ownership/runtime/trust/product/lifecycle scope
L56: boundary: boundary_id
L57: kind: runtime|repo|database|client|contract|adapter|workflow|service
L64: kind: data|control|ownership|install|sync|execution|verification
L66: - symbol: dashed boundary
L75: ## Renderer Handoff
L80: - boundaries and their meaning
L81: - nodes grouped by boundary
L93: 2. **Wrong source of truth.** Do not show clients or installers as owning live state unless they really do.
L94: 3. **Boundary ambiguity.** Every boundary must say what it means.
L101: - [ ] Nodes, edges, boundaries, legend, constraints, and verification are present.
L102: - [ ] Directionality and source-of-truth ownership are labeled.
```

### domain-driven-design

- Path: `skills/domain-driven-design/SKILL.md`
- Contract: `contracts/skills/architecture/domain-driven-design.contract.yaml` @ `0.1.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L5: > - **Bounded context = explicit boundary** — never share domain models across context boundaries; share only via contract
L12: - Designing service boundaries for microservices
L16: **Do NOT use** for CRUD-only apps, simple scripts, or cases where the domain is trivially thin.
L32: Defining service boundaries?             → Bounded context + context map, see strategic-design.md
L34: Business rule belongs to which object?   → Entity vs Value Object vs Domain Service, see tactical-design.md
```

### ethics-responsible-ai

- Path: `skills/ethics-responsible-ai/SKILL.md`
- Contract: `contracts/skills/quality/ethics-responsible-ai.contract.yaml` @ `0.1.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L25: Covers: stakeholder impact mapping, identifying sensitive attributes, fairness metrics,
L32: Covers: accountability mapping, pre-launch harm assessment (direct, indirect, distributional),
L52: **Gate:** Run fairness audit and harm assessment before any AI feature ships to production.
```

### event-driven-design

- Path: `skills/event-driven-design/SKILL.md`
- Contract: `contracts/skills/architecture/event-driven-design.contract.yaml` @ `0.1.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L16: **Do NOT use** when caller needs immediate response, or when eventual consistency is not acceptable.
```

### experiment-design

- Path: `skills/experiment-design/SKILL.md`
- Contract: `contracts/skills/product/experiment-design.contract.yaml` @ `1.0.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L8: Do not build the product when a smaller experiment can answer the riskiest assumption.
L14: - A product idea has plausible value but weak evidence
L17: Do not use for: full PRD writing (`product-requirements`); production implementation (`new-feature-workflow`); generic research synthesis (`user-research`).
L40: - What we will not build yet: <explicit non-build boundary>
L65: - PARTIAL → <follow-up discovery/narrowing>
L91: - Smallest test is smaller than building the product.
L93: - Guardrails cover privacy, trust, safety, or brand risk.
```

### git-workflow

- Path: `skills/git-workflow/SKILL.md`
- Contract: `contracts/skills/engineering/git-workflow.contract.yaml` @ `0.1.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L14: - What is the base branch? (product_defined)
L15: - What is the branch naming convention? (product_defined)
L16: - What is the commit message convention? (product_defined)
L33: Branch naming convention is product_defined. Common patterns:
L43: Commit message convention is product_defined. Common patterns:
L79: Mechanism is product_defined (GitHub PR, GitLab MR, Gerrit patch, etc).
L86: - [ ] CI/lint passing (if product_defined as required)
L92: Merge strategy is product_defined (merge commit, squash, rebase).
L95: # via CLI if product allows
L119: Product-specific implementations should declare `extends` in their frontmatter:
L126: Then override only what's product-specific: base branch, naming convention, issue tracker, merge strategy.
```

### hermes-profile-bootstrap

- Path: `skills/hermes-profile-bootstrap/SKILL.md`
- Contract: `contracts/skills/runtime/profile-bootstrap.contract.yaml` @ `0.1.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L7: Use this skill to create or audit the **Hermes adapter implementation** of the Native AI `profile-bootstrap` contract.
L9: The core contract lives in `native-ai-core/contracts/skills/runtime/profile-bootstrap.contract.yaml`. This skill owns the Hermes-specific profile skeleton, commands, paths, install steps, and verification behavior. The profile is a **runtime skeleton**, not a product.
L17: Until that command exists, use this skill as the canonical Hermes adapter blueprint for manual generation or for implementing the generator.
L24: - implement the Hermes adapter for the core `profile-bootstrap` contract
L25: - define the minimum required skills for an AI-native Hermes runtime
L30: Do not use for:
L33: - product-specific rules that belong in `products/<product-id>/` or a project repo
L39: The runtime-agnostic contract belongs in `native-ai-core`. This skill belongs in `ai-native-skills` because it is executable Hermes adapter guidance. If a rule applies to every runtime, move it to the core contract; if it mentions Hermes paths or commands, keep it here.
L41: ## Layer Boundary
L46: Hermes profile skeleton = runtime identity, config defaults, installed skills, scripts, docs
L48: native-ai-core          = runtime-agnostic profile-bootstrap contract and workflow definitions
L49: native-ai-fw/app        = product/runtime binding and product source-of-truth registry
L50: product instance        = VisualMate or another product's rules, specs, context, and docs
L53: A generated profile may reference product projects, but it must not bake product facts into the reusable skeleton.
L75: ### Phase 3 — Verification & Handoff
L77: Run doctor, list installed skills, compare against `skills.lock.yaml`, report handoff.
```

### incident-response

- Path: `skills/incident-response/SKILL.md`
- Contract: `contracts/skills/runtime/incident-response.contract.yaml` @ `0.1.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L30: Phase 2 → Triage            — scope blast radius, DO NOT fix yet
```

### information-architecture

- Path: `skills/information-architecture/SKILL.md`
- Contract: `contracts/skills/design/information-architecture.contract.yaml` @ `1.0.0`
- Type/version: `skill` / `1.1.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

_No boundary-related excerpt detected._

### language-standards

- Path: `skills/language-standards/SKILL.md`
- Contract: `contracts/skills/governance/language-standards.contract.yaml` @ `0.1.0`
- Type/version: `skill` / `1.1.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L6: Artifact language      = product_defined (declare it explicitly)
L8: Team chat language     = product_defined (unconstrained)
L10: This skill does NOT mandate English.
L32: language: product_defined
L81: ✅ // validate ownership before update — prevents IDOR
L86: ❌ // validate ownership before update ← mixing
```

### macrostructures

- Path: `skills/macrostructures/SKILL.md`
- Contract: `contracts/skills/design/macrostructures.contract.yaml` @ `1.0.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L49: | 03 | **Bento** | grid-led | left | SaaS features, product overview | references/other-structures.md |
L58: | 12 | **Sport** | image-led | left | Bold, kinetic, product launch | references/other-structures.md |
L62: | 16 | **Aurora** | image-led | center | AI product, creative tool | references/other-structures.md |
```

### master-design

- Path: `skills/master-design/SKILL.md`
- Contract: `contracts/skills/design/master-design.contract.yaml` @ `0.2.0`
- Type/version: `skill` / `1.2.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L3: Operate as the active product-design owner, not a passive screen generator or style-recipe executor.
L6: product intent + user task + content + context + existing equity + locks
L9: → delegate narrow specialist concerns
L17: 1. Separate the real user/product requirement from the proposed UI or visual solution.
L19: 3. Preserve valid brand, product, content, asset, behavior, and design-system locks.
L23: 6. Product category is a signal, not an automatic genre or layout.
L25: 8. Delegate specialist concerns, but keep final synthesis and trade-off ownership.
L26: 9. Do not treat one font pairing, color percentage, spacing grid, composition axis,
L28: 10. Every repeated visual treatment needs a product, semantic, system,
L30: 11. Distinctiveness must come from coherent product-specific grammar, not randomness.
L31: 12. Do not invent metrics, testimonials, proof, product UI, imagery, or claims.
L36: ## Ownership
L41: product experience direction
L45: specialist delegation and reconciliation
L46: preservation of valid product and brand equity
L47: design-to-engineering handoff
L50: It does not own:
L53: specialist gate definitions
L56: product scope approval
L69: Design-owner response:
L72: → delegate cross-context fitness to adaptive-component-design
L83: Product experience and final synthesis
L87: → design-strategy + narrow adapters
L90: → design-visual + narrow adapters
L93: → design-layout + narrow adapters
L99: → design-interaction + narrow adapters
L102: → design-system + narrow adapters
L108: Specialists return evidence, trade-offs, and boundaries. They do not emit disconnected decisions for the implementation agent to reconcile.
L132: brand identity and product character
L135: real product artifacts and proof
L141: Do not erase useful equity merely to make a redesign look more dramatic.
L170: product_and_user_fit:
L217: ### 6. Delegate active concerns
L219: Load only skills required by the direction and changed layers. Reconcile specialist recommendations under one selected direction.
L237: ### 8. Produce engineering-ready handoff
L256: Load `design-review` for rendered, exported, or implemented artifacts. Code inspection, design intent, and a high-level mockup do not prove the final experience passes.
L265: Accent quantity and role follow product semantics, brand, content, and channel.
L283: Remove treatments with no named role. Restraint does not require sparse output.
L291: generic product-independent hero
L298: reference structure copied without product transformation
```

### master-engineer

- Path: `skills/master-engineer/SKILL.md`
- Contract: `contracts/skills/engineering/master-engineer.contract.yaml` @ `0.1.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L13: Design Patterns Specialist
L17: In the Native AI architecture, this skill helps distinguish core contracts, app/product instances, runtime bindings, runtime adapters, and platform implementation. It should improve over time when repeated architecture lessons emerge.
L26: - Core/product/runtime/adapter boundaries
L28: - Module, package, service, or API boundaries
L32: Do not use it to justify complexity. Default to the smallest durable design that solves the real problem.
L36: 1. **Purpose before pattern.** Start from the product/system problem, not from a favorite architecture.
L37: 2. **Boundaries before code.** Define ownership and seams before implementation.
L41: 6. **Runtime is not domain.** Hermes/Codex/CI implement capabilities; they do not own product truth.
L42: 7. **Agent-ready handoff.** Good design includes source references, constraints, approval gates, and verification commands.
L44: 8. **Core/app/skill split.** When a framework repo starts mixing core contracts, product context, and runtime skills, prefer a domain-driven split: public core contracts, app adapters that may be public or private, and runtime skill adapters. See `references/native-ai-core-app-skills-split.md`.
L52: 3. **Identify forces.** Name competing pressures: simplicity vs extensibility, runtime-specific vs runtime-agnostic, private vs public, speed vs maintainability. Done when trade-offs are explicit.
L56: 5. **Map to layers.** Place artifacts in core framework, product instance, runtime binding, runtime adapter, or platform code. Done when file placement and boundary risks are clear.
L58: 6. **Produce a handoff.** Return an ADR, design critique, system design, refactor strategy, engineering contract update, or implementation task. Done when verification criteria are included.
L87: ## Boundary Check
L98: ## Boundaries
L124: - Boundaries are explicit.
L127: - Runtime-specific behavior does not leak into core.
L133: 1. **Pattern worship.** Do not introduce DDD, CQRS, event sourcing, hexagonal architecture, microservices, or plugin systems unless the forces justify them.
L134: 2. **Dashboard duplication.** If Hermes already provides the runtime surface, do not build another runtime dashboard without a clear separate purpose.
L135: 3. **Vague architecture approval.** Never approve by vibes; tie approval to contracts, boundaries, and verification.
L136: 4. **Leaking product facts into core.** Keep product-specific decisions local unless generalized.
L138: 6. **Publishing private history.** Do not convert a private product/app repo to public by flipping visibility if it may contain product context in git history. Create a fresh public core repo and copy only sanitized contract artifacts.
L139: 7. **Visibility-boundary confusion.** Do not define architecture by public/private status. App adapters implement core contracts and may be public or private; classify by responsibility first.
```

### micro-frontend

- Path: `skills/micro-frontend/SKILL.md`
- Contract: `contracts/skills/architecture/micro-frontend.contract.yaml` @ `0.1.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L6: 1. Domain boundary = MFE boundary (bounded context → MFE, never per-page or per-feature)
L7: 2. No direct imports across MFE boundaries — use event bus or shell contract
L28: ## MFE Boundary — Align with Bounded Context
L30: Same rule as microservices: MFE boundary = bounded context boundary.
L36: [Catalog Context]    → ProductCatalogMFE
L60: MFE fails to load?   → ErrorBoundary fallback per mount point
```

### model-selection

- Path: `skills/model-selection/SKILL.md`
- Contract: `contracts/skills/runtime/model-selection.contract.yaml` @ `0.1.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L7: The model is the **brain** in the AI-native engineering stack. Do not pick a model from habit, price, hype, or the current default. Pick it from the task's intent, risk, required capabilities, context constraints, fallback path, and verification burden.
L9: This skill implements the runtime-agnostic contract:
L12: ai-native-core/contracts/skills/runtime/model-selection.contract.yaml
L19: - selecting a model/provider/agent for coding, review, design, QA, security, architecture, or summarization
L26: Do not use for:
L29: - product feature design where the model is already mandated by a higher-level spec
L64: Use `reasoning` for architecture tradeoffs, boundary decisions, contracts, and migration plans. Use `fast_general` only for formatting or summarizing already-decided architecture.
L102: For long tasks, include this as a short preflight before execution. Do not let the preflight replace the actual work.
L106: A Hermes profile should map these abstract classes to concrete configured providers/models or external coding agents. Keep provider names in profile config, not in the core contract.
L119: Do not commit API keys, tokens, or local-only credentials in the policy.
L129: 7. **Claiming unsupported capability.** Do not say a model can see images, edit repos, or use tools unless the runtime actually provides that capability.
L141: - [ ] Provider-specific names are kept in runtime/profile config, not the core contract.
```

### motion-design

- Path: `skills/motion-design/SKILL.md`
- Contract: `contracts/skills/design/motion-design.contract.yaml` @ `1.0.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L19: | `references/subtle-interactions.md` | Mode 1 SUBTLE: hover lift, link underline, button press, focus ring, skeleton loading, scroll entrance, stagger (1A–1G) | Building micro-interactions, product UI, personal pages |
L44: Product app / dashboard    → SUBTLE only (subtle-interactions.md)
```

### native-ai-engineer

- Path: `skills/native-ai-engineer/SKILL.md`
- Contract: `contracts/skills/runtime/native-ai-engineer.contract.yaml` @ `0.1.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L5: Use this skill when Hermes should reason as a Native AI Framework Engineer: a domain-contract architect for AI-native products, agents, runtimes, skills, workflows, verification loops, and learning policy.
L10: native-ai-core    = product-agnostic domain, contracts, workflows, rules, skills, philosophy
L11: native-ai-app     = app/product adapter implementing core contracts; public or private by implementer choice
L12: native-ai-skills  = runtime skill adapters implementing core skill contracts
L13: runtime           = Hermes, Codex, Claude, CI, cron, gateway, or another execution surface
L14: product instance  = product-specific source of truth under products/<product-id>/
L21: - Where does this concept belong: core, app adapter, skill adapter, product instance, or runtime binding?
L22: - Is this a domain contract, runtime implementation, product-specific rule, or executable skill?
L24: - What should become memory, skill, rule, product doc, core contract, or session-only progress?
L25: - What contract should exist before building an adapter, runner, skill, or automation?
L28: Do not use this skill for ordinary bug fixing, UI work, deployment, or generic software architecture unless the Native AI layer boundary is the actual question.
L30: ## Responsibilities
L32: 1. **Layer placement.** Classify artifacts by responsibility, not visibility. Done when every artifact has a target layer and a reason.
L33: 2. **Contract design.** Define skill, workflow, runtime binding, product config, adapter compatibility, approval, verification, and learning contracts. Done when inputs, outputs, ownership, quality gates, and adapter requirements are explicit.
L34: 3. **Runtime mapping.** Map abstract concepts to runtime capabilities without making the runtime the domain. Done when runtime-specific files are isolated in bindings/adapters.
L35: 4. **Promotion governance.** Decide whether knowledge belongs in memory, skill, product docs, core contracts, native-ai-skills, or session progress. Done when durable learning is captured in the smallest correct layer.
L36: 5. **Anti-pattern detection.** Block runtime leakage into core, product facts in public core, mixed contract/implementation, visibility-boundary confusion, and dashboard/controller duplication. Done when the safer layer and non-goal are named.
L42: In core, use runtime-agnostic terms:
L45: Runtime
L46: Runtime Adapter
L59: Runtime = Hermes Agent
L60: Runtime Adapter = Hermes runtime binding + Hermes profile skills
L61: Skill Adapter = native-ai-skills/adapters/hermes/*
L67: Therefore `native-ai-core` may mention Hermes only as an example runtime or example adapter mapping. Required Hermes behavior belongs in app/runtime binding or `native-ai-skills` Hermes adapters.
L71: 1. **Name the decision.** State the exact layer/boundary question. Done when it fits in one sentence.
L72: 2. **Inspect artifacts.** Read relevant contracts, app binding, skill adapter, product config, or runtime docs. Done when existing ownership is known.
L73: 3. **Classify by responsibility.** Pick core, app adapter, skill adapter, product instance, runtime binding, platform code, memory, or session. Done when the layer map is explicit.
L74: 4. **Design the contract first.** If implementation is needed, define the minimal contract/compat shape before adapter code. Done when inputs, outputs, quality gates, and adapter requirements are named.
L75: 5. **Map runtime implementation.** Show how Hermes or another runtime satisfies abstract ports without leaking into core. Done when runtime-specific files are identified.
L76: 6. **Give a reversible handoff.** Include file placement, verification, risks, and what not to build yet. Done when an agent can execute without guessing.
L86: ## Contract/Adapter Impact
L97: ## Ownership
L99: ## Adapter Requirements
L103: ### Runtime Mapping
L107: ## Runtime Implementation
L109: ## Adapter Files
L111: ## Boundary Risks
L116: 1. **Visibility-boundary confusion.** Public/private is not the architecture boundary; responsibility is.
L117: 2. **Runtime leakage.** Do not make Hermes-specific behavior mandatory in core.
L118: 3. **Product leakage.** Keep VisualMate or other product-specific facts out of reusable core.
```

### native-ai-runtime-agent

- Path: `skills/native-ai-runtime-agent/SKILL.md`
- Contract: `contracts/skills/runtime/native-ai-runtime-agent.contract.yaml` @ `0.1.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L1: # Native AI Runtime Agent
L5: Use this skill to operate Hermes as the runtime adapter for `native-ai-fw`.
L10: Hermes Agent     = runtime, dashboard, tool execution surface
L12: native-ai-app/fw = app/product/runtime adapter implementing native-ai-core contracts; public or private by implementer choice
L13: native-ai-skills = runtime skill adapters implementing native-ai-core skill contracts
L14: Product instance = product-specific source of truth, e.g. VisualMate
L17: Do not turn `native-ai-fw` into a replacement Hermes dashboard. Use Hermes Desktop/CLI/Gateway as the execution surface. Use `native-ai-fw`/app adapters to bind product context, runtime policy, core contracts, and installed runtime skills.
L24: - The task mentions Native AI Framework, VisualMate, runtime binding, product instance, product contract, workflow, or Hermes runtime adapter.
L25: - The user asks Hermes to plan, design, engineer, verify, deploy, review, or capture learning for a product instance.
L29: Do not use this skill for:
L31: - Generic Hermes configuration not related to `native-ai-fw` or product runtime binding.
L35: ## Runtime Boot Sequence
L37: Before product work, do this compact boot sequence:
L39: 1. **Identify product id.**
L42: - Completion: product id is known or you ask the user only if the task cannot proceed without it.
L46: - Completion: core/product/runtime boundary is clear.
L48: 3. **Load product config.**
L49: - Read `products/<product-id>/project.config.yaml`.
L51: - Completion: product authority files for the task are known.
L53: 4. **Load runtime binding.**
L54: - Read `products/<product-id>/runtime.binding.yaml`.
L55: - Confirm `runtime_binding.runtime` is `hermes`.
L57: - Resolve `hermes.skills.runtime_adapters` for executable runtime skills; `installed_as` should match an entry in `hermes.skills.hermes_profile_skills`.
L58: - Completion: profile, toolsets, workflows, approval policy, verification policy, learning policy, core source, and runtime skill adapter sources are known.
L69: - Use product-specific workflows when listed in the binding; otherwise use framework workflows.
L81: - Put reusable procedures into skills; stable product facts into the right product docs or memory; task progress stays in session/kanban.
L91: VisualMate provides product truth.
L96: - A separate native-ai-fw runtime dashboard.
L99: - Product OS UI work when the user is still clarifying runtime behavior.
L101: ## File Responsibilities
L103: | File or folder | Responsibility |
L105: | `.hermes.md` | Hermes-specific repo entrypoint and boundary rules |
L106: | `docs/hermes-runtime-agent.md` | Runtime operating protocol |
L107: | `docs/hermes-runtime-binding.md` | Binding contract explanation |
L109: | `products/<id>/project.config.yaml` | Product source-of-truth registry |
L110: | `products/<id>/runtime.binding.yaml` | Product-to-Hermes runtime policy, core source, and runtime skill adapter declarations |
L111: | `context-packs/<id>.yaml` | Condensed product context |
L112: | `products/<id>/...` | Product-specific contracts, workflows, rules, and skills |
L113: | `core/workflows/`, `core/rules/`, `core/skills/` | Product-agnostic core methodology artifacts |
L114: | `hermes.skills.runtime_adapters` | Source-of-truth links to runtime skill implementations such as `native-ai-skills` |
```

### native-ai-runtime-ops

- Path: `skills/native-ai-runtime-ops/SKILL.md`
- Contract: `contracts/skills/runtime/native-ai-runtime-ops.contract.yaml` @ `0.1.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L1: # Native AI Runtime Ops
L5: Use this skill when Hermes should act as a runtime operations engineer for a Native AI workspace.
L13: It does not decide domain architecture. Use `native-ai-engineer` for layer boundaries and contracts.
L21: - turning a remote host into the canonical Hermes runtime
L25: - setting up tmux, gateway, cron, or systemd for persistent runtime use
L52: For shared sessions, prefer one canonical runtime host with clients connecting remotely. Do not active-active sync live Hermes SQLite state.
L69: Host native-ai-runtime
L81: ssh native-ai-runtime 'hostname && whoami && uname -a'
L96: ## Canonical Runtime Bootstrap
L117: ssh native-ai-runtime
L136: - [ ] Hermes profile is installed under the canonical runtime host.
L140: - [ ] Users connect as clients; they do not sync live state.
```

### new-feature-workflow

- Path: `skills/new-feature-workflow/SKILL.md`
- Contract: `contracts/workflows/new-feature.contract.yaml` @ `None`
- Type/version: `workflow` / `2.1.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L3: Plan verified scope → approve decisions → implement → verify → submit decision/evidence handoff → technical review and merge authorization.
L5: ## Core boundary
L15: A wireframe or specification decides what to build. It does not prove the implemented result. A technical review verdict does not automatically prove the responsible authority permits merge.
L22: 3. Agent-authored issue/spec/PR text is not owner approval by itself.
L26: 7. A new route, product dependency, data boundary, permission behavior, or material lock change requires explicit bounded approval.
L30: 11. LIMITED REVIEW cannot authorize complete specialist-domain acceptance.
L34: 15. Do not bundle unrelated or unapproved changes.
L39: Use when adding a new capability to an existing product or codebase.
L42: product from zero        → product-development-workflow
L67: preserved_routes_or_boundaries: []
L79: approval_policy: <product-defined>
L113: system boundaries, contracts, integration, or data model
L120: Load only relevant owners and specialists:
L127: specialized owner     domains outside built-in product UI/visual communication
L130: Load `references/design-decision-and-acceptance.md` for the decision schema, evidence boundary, risk provenance, and handoff.
L132: **Done when:** the verified approval boundary, required states/contexts, locks, assumptions, and implementation-ready criteria are explicit.
L142: write tests at the relevant boundary
L158: Existing implementation does not retroactively approve the expansion.
L171: contract, migration, runtime, or integration evidence
L182: Evidence boundary:
L185: rendered interactive → affected contexts, states, inputs, runtime, accessibility
L192: For `CONDITIONAL PASS` or another non-blocking exception, run `decision-provenance` against the product's accepted-risk authority. Missing authority is not an accepted risk.
L211: accepted risks with authority, owner, mitigation, and expiry when required
L215: Use the handoff schema in `references/design-decision-and-acceptance.md`.
L217: Do not submit as design-complete while rendered evidence remains `NOT_VERIFIED`. Do not claim “owner approved” without an attributable decision source.
L225: Pass the complete feature handoff to `code-review-workflow`. It returns:
L237: → eligible to merge under product policy
L240: → technically ready, but do not merge yet
L248: **Done when:** technical reviewers approve, merge authority is verified, and the submission is merged according to product policy.
L255: | Design decision | Decision authority | Boundary, contexts, states, locks, and owner records explicit |
L258: | Submit | Complete decision/evidence handoff | Submission is traceable and reviewable |
L265: | Agent-generated issue means scope approved | Verify attributable owner/system-of-record acceptance |
L266: | Existing route means it belongs to the feature | Existing state does not establish current scope |
L270: | Specialist visual accepted with universal gates | Load domain reviewer or block complete acceptance |
L274: | Scope grows during implementation | Stop, verify provenance, and reapprove the boundary |
```

### observability-design

- Path: `skills/observability-design/SKILL.md`
- Contract: `contracts/skills/runtime/observability-design.contract.yaml` @ `0.1.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L41: - [ ] Dashboard covers four golden signals?
```

### onboarding

- Path: `skills/onboarding/SKILL.md`
- Contract: `contracts/skills/runtime/onboarding.contract.yaml` @ `0.1.0`
- Type/version: `skill` / `1.1.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L8: Onboarding output = AGENTS.md that encodes what you discovered,
L9: so the next agent (or engineer) does not have to rediscover it.
L38: | 3 | Test Command Discovery | `references/phases-1-3.md` |
L40: | 5 | Gotcha Discovery | `references/phases-4-6.md` |
```

### plan

- Path: `skills/plan/SKILL.md`
- Contract: `contracts/skills/engineering/plan.contract.yaml` @ `0.1.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L19: - Do not implement code.
L20: - Do not edit project files except the plan markdown file.
L21: - Do not run mutating terminal commands, commit, push, or perform external actions.
L47: If the runtime provides a specific target path, use that exact path.
L64: - [`references/writing-process.md`](references/writing-process.md) — Step-by-step writing process, principles (DRY/YAGNI/TDD), common mistakes, and execution handoff
L68: ## Execution Handoff
L75: - Fresh `delegate_task` per task with full context
```

### ports-and-adapters

- Path: `skills/ports-and-adapters/SKILL.md`
- Contract: `contracts/skills/architecture/ports-and-adapters.contract.yaml` @ `0.1.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L1: # Ports and Adapters (Hexagonal Architecture)
L4: > - Ports = input boundaries only — defined in Domain layer, never in Infrastructure
L5: > - Adapters implement ports, never call each other directly
L12: | Architecture & Ports | Understand the 3 layers, define port interfaces, implement infrastructure + primary adapters | [architecture-and-adapters.md](references/architecture-and-adapters.md) |
L13: | App Service, DI & Testing | Wire application service, bind adapters via DI, use in-memory adapters for tests | [application-service-and-testing.md](references/application-service-and-testing.md) |
L27: ├─ YES → Define port in Domain/Port/, implement adapter in Infrastructure/
L31: └─ Create primary adapter in Interface/ that drives domain via Application Service
L39: Dependency direction: Adapters → Ports ← Domain
L40: NEVER: Domain → Adapter (direct)
L46: - [ ] Adapters in Infrastructure/ or Interface/ only?
L48: - [ ] Domain tests use in-memory adapters (no real DB/HTTP)?
L55: | `use Illuminate\...` in Domain/ | Extract to adapter |
L57: | `DB::table()` in entity method | Define port, inject adapter |
L63: Load [architecture-and-adapters.md](references/architecture-and-adapters.md) for layer diagram, port definitions, and adapter implementation examples.
L65: Load [application-service-and-testing.md](references/application-service-and-testing.md) for orchestration layer, DI wiring, in-memory adapters, folder structure, and violation table.
```

### product-development-workflow

- Path: `skills/product-development-workflow/SKILL.md`
- Contract: `contracts/workflows/product-development.contract.yaml` @ `None`
- Type/version: `workflow` / `2.1.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L1: # Product Development Workflow
L3: Discovery → verified PRD → authorized MVP slice → technical spec → feature implementation → product acceptance → release readiness and approval → deploy → launch → learn.
L8: 1. Use this workflow for a product from zero, not every product-related task.
L9: 2. Discovery precedes PRD when the opportunity is still vague.
L12: 5. Agent-authored PRD, issue, or status text is not owner approval by itself.
L13: 6. Implementation runs through new-feature-workflow boundaries.
L14: 7. Feature verification does not automatically prove product-level acceptance.
L18: 11. NOT_VERIFIED, missing reviewer coverage, provenance gaps, and hard-gate failures block release readiness.
L20: 13. Release, deploy, and launch actions require the approvals defined by product policy.
L21: 14. Release artifacts do not convert NOT_READY into RELEASE_READY.
L25: ## Route boundary
L44: discovery
L62: Acceptance, accepted-risk authority, and release boundary
L75: | 1 | Discovery | research, value, experiment | Opportunity, value, assumptions, decision owners explicit |
L76: | 2 | Requirements / PRD | product requirements + provenance | PRD readiness and scope authority pass |
L78: | 4 | Technical Spec | spec workflow and engineering owners | Tasks trace to verified PRD/MVP criteria |
L80: | 6 | Product Acceptance | matrix + reviewers + provenance | Every in-scope criterion and risk reconciled |
L83: | 9 | Launch | product, content, analytics, support | Launch approval and feedback loop live |
L86: ## Decision provenance boundary
L93: “the owner accepted this product risk”
L94: “all merged features mean the product is ready”
L100: verified authoritative source covers the exact scope/action
L105: → do not treat as approval
L116: ## Product acceptance boundary
L122: with direct evidence, complete reviewer coverage, verified risk authority,
L127: product_acceptance:
L143: ## Release boundary
L167: after_discovery_recommendation
L187: iterate / pivot / narrow / stop decision has an attributable owner
```

### product-manager

- Path: `skills/product-manager/SKILL.md`
- Contract: `contracts/skills/product/product-manager.contract.yaml` @ `0.1.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L1: # Product Manager
L23: ## 1. Product Intent
L28: product_intent:
L34: non_goals: []         # explicitly what this does NOT solve
L46: intent_ref: ""        # links back to product intent
L75: estimate: ""              # product_defined unit (SP, hours, etc)
L127: **Out of scope:**
```

### product-requirements

- Path: `skills/product-requirements/SKILL.md`
- Contract: `contracts/skills/product/product-requirements.contract.yaml` @ `0.2.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L1: # Product Requirements
L5: Use when the user asks to write a PRD, turn discovery notes into product requirements, define goals/metrics/scope/acceptance criteria, or review feature readiness before technical spec.
L7: Do not use for: technical architecture specs (`spec-workflow`, `api-contract`); release execution; implementation task breakdown only (`product-manager`).
L12: # PRD: <Product or Feature Name>
L15: <What user or business problem needs solving? Do not start with the solution.>
L20: - Excluded users: <who this does not optimize for>
L36: - NG1: <explicitly out of scope>
L47: ### Out of Scope
L56: - REQ-1: <testable product behavior>
L76: - Q1: <question> → owner: <owner> → due: <date or milestone>
L84: 1. **Frame the problem.** Problem statement names a user/business outcome, does not prescribe implementation.
L87: 4. **Define goals and non-goals.** Success and boundaries both documented.
L89: 6. **Set scope boundaries.** Scope-in and scope-out both exist.
L108: - Open questions have owners or next-step decisions.
L121: Scope boundary: PASS|FAIL — <note>
L149: - [ ] Non-functional requirements cover relevant quality attributes.
```

### prompt-optimizer

- Path: `skills/prompt-optimizer/SKILL.md`
- Contract: `contracts/skills/context/prompt-optimizer.contract.yaml` @ `0.1.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L19: - When scope boundaries are ambiguous
L49: Scope out: do not touch callers, do not rename the function
L52: Stop: after one refactored version — do not offer alternatives
L67: Stop: after verdict APPROVED or REQUEST CHANGES — do not suggest unrelated improvements
L80: Scope out: do not test private methods, do not add integration tests
L83: Stop: after the 4 test cases — do not add more without asking
L96: Scope out: do not refactor unrelated code
L97: Constraint: do not propose fix until root cause is confirmed
L99: Stop: after phase 3 — do not suggest architectural improvements
L114: Output: structured by lens — Product / Design / Psychology — then Synthesis with P1/P2/P3
L115: Stop: after Synthesis — do not suggest implementation solutions
L116: Skills: role-switcher → master-design, ux-psychology, product-manager
L136: - "do not rename", "do not add dependencies", "do not refactor callers"
L148: | No scope_out | Agent refactors 5 files instead of 1 | Explicitly name what's out of scope |
L149: | No stop condition | Agent adds "bonus" suggestions after task | "Stop after X — do not add more" |
```

### readability

- Path: `skills/readability/SKILL.md`
- Contract: `contracts/skills/design/readability.contract.yaml` @ `1.0.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

_No boundary-related excerpt detected._

### redesign-workflow

- Path: `skills/redesign-workflow/SKILL.md`
- Contract: `contracts/skills/quality/redesign-workflow.contract.yaml` @ `2.2.0`
- Type/version: `workflow` / `3.4.0`
- Audit status: `REVIEW_REQUIRED`
- Low-evidence items: `['deployment_or_publishing', 'legal_trademark_clearance']`

**Contract covers**

- `existing_visual_surface_redesign`
- `redesign_vs_refinement_vs_audit_routing`
- `explicit_design_implementation_and_repository_write_ownership`
- `confirmed_scope_and_baseline_capture`
- `final_effective_diff_integrity`
- `concurrent_branch_write_detection_and_coordination`
- `brand_content_asset_behavior_route_and_path_preservation`
- `direction_macrostructure_and_layered_change_planning`
- `user_and_business_value_alignment`
- `delegated_design_and_implementation_work`
- `prototype_or_repository_patch_production`
- `domain_appropriate_verification`
- `design_review_facade_acceptance`
- `bounded_fix_iterations_and_learning_promotion`
- `passing_delivery_or_honest_blocker_reporting`

**Contract delegates**

- `net_new_product_definition`
- `audit_only_work_after_route_handoff`
- `known_narrow_refinement_after_route_handoff`
- `non_visual_feature_development`
- `unrelated_product_route_auth_data_or_infrastructure_changes`
- `general_bugfix_workflow`
- `deployment_or_publishing`
- `legal_trademark_clearance`
- `force_overwrite_of_uninspected_concurrent_work`
- `destructive_repository_operations_without_approval`

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L1: # Redesign Workflow
L3: Redesign an existing visual surface through explicit ownership, verified decision provenance, bounded specialist delegation, clean final-diff scope, concurrency-safe writes, domain-appropriate evidence, independent facade review, and a verified correction loop.
L5: The workflow owns lifecycle, state transitions, approvals, preservation, integrity gates, iteration, and handoffs. Specialist skills own narrow design decisions. `master-engineer` owns repository implementation when required. `design-review` and the governing domain reviewer own acceptance.
L9: Runtime composition and package installation are separate concerns.
L13: → backward-compatible runtime capability hint
L14: → does not prove that dependencies are installed
L17: → bind this workflow version to one canonical manifest contract
L19: packs/redesign/pack.yaml
L21: → classifies required, conditional, port, adapter, domain-reviewer, and optional skills
L23: → governs the documented Redesign Pack command
L26: Installing `redesign-workflow` alone installs only the entrypoint because the upstream `skills` CLI does not currently resolve transitive dependencies from `SKILL.md`. Before execution, verify required capability availability, resolve conditional capabilities from the run context, and select adapters only from changed concerns and acceptance criteria.
L28: Load `references/dependencies-and-installation.md` for the complete dependency contract, installation profiles, runtime preflight, and validation commands.
L33: 1. Route redesign, refinement, and audit-only before production.
L34: 2. Declare exactly one design owner.
L35: 3. Patch mode requires an implementation owner and one active repository write owner.
L36: 4. Material scope, lock, approval, override, status, and ownership claims require decision provenance.
L37: 5. Agent summaries, PR bodies, commits, recency, and inference are not owner approval.
L38: 6. Capture baseline, confirmed scope, preservation locks, and decision records before patch production.
L39: 7. Select specialists from changed layers and acceptance criteria; never load everything by default.
L40: 8. Product, audience, content, trust, complexity, context, and existing equity drive direction—not taste labels.
L41: 9. Port/profile defaults are not universal workflow rules.
L42: 10. Structural copy and content decisions precede layout lock.
L43: 11. Every repository write uses an expected-head lease.
L44: 12. Inspect head drift before retry; newest commit is not automatically authoritative.
L45: 13. Two reversals of the same decision/path stop automatic writes; never ping-pong or force-push.
L46: 14. Classify every effective changed path against verified scope.
L47: 15. OUT_OF_SCOPE, UNKNOWN, or provenance-blocked changes block passing review and delivery.
L48: 16. Verification evidence must match domain, artifact state, changed layers, and delivery boundary.
L49: 17. Build success is not design proof; screenshot evidence is not runtime or interaction proof.
L50: 18. Acceptance runs only through design-review and the governing domain reviewer.
L52: 20. Contextual hard gates come from loaded reviewers, not a global UI checklist.
L53: 21. Provenance, scope, concurrency, evidence, coverage, and facade verdict all control delivery.
L54: 22. Classify root cause and correction ownership before fixing.
L55: 23. Maximum design iterations default to 5; after two failed patches in one region, re-read and replan.
L57: 25. Blocked or bounded attempts are never labeled PASS.
L58: 26. Never claim a complete redesign environment from the workflow entrypoint alone.
L61: ## Route
L64: audit only, no production requested
L65: → design-audit
L67: accepted direction + known narrow verified findings
```

### refactoring

- Path: `skills/refactoring/SKILL.md`
- Contract: `contracts/skills/engineering/refactoring.contract.yaml` @ `0.1.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L26: ├─ NO  → Fix tests first. Do not refactor broken code.
L39: | God Class | > 300 lines, 10+ responsibilities | Extract Class |
```

### resilience-engineering

- Path: `skills/resilience-engineering/SKILL.md`
- Contract: `contracts/skills/quality/resilience-engineering.contract.yaml` @ `0.1.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L3: > **Design for failure, not just success. Test failure modes with chaos before production. Graceful degradation beats hard failure.**
L12: Resilience = ability to absorb disturbance and adapt, not just recover.
L68: - [Chaos Engineering & Recovery Design](references/chaos-and-recovery.md) — Graceful Degradation, Chaos Engineering, RTO/RPO
```

### response-contract

- Path: `skills/response-contract/SKILL.md`
- Contract: `contracts/skills/context/response-contract.contract.yaml` @ `0.1.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L27: - No unsolicited alternatives: do not offer "Option A / Option B" unless asked
L33: - Verbosity level: [concise|normal|verbose] ← product_defined
```

### responsiveness

- Path: `skills/responsiveness/SKILL.md`
- Contract: `contracts/skills/design/responsiveness.contract.yaml` @ `1.0.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

_No boundary-related excerpt detected._

### role-switcher

- Path: `skills/role-switcher/SKILL.md`
- Contract: `contracts/skills/meta/role-switcher.contract.yaml` @ `0.1.0`
- Type/version: `meta-skill` / `1.3.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L7: → assign one owner
L8: → load only narrow specialists
L17: Owner            final decision responsibility and synthesis
L18: Specialist       narrow expertise contributing within a boundary
L20: Domain reviewer  specialist-domain gates, evidence, and hard-gate policy
L23: A specialist or reviewer never silently replaces the owner.
L32: evidence normalization, score, coverage, verdict, report
L36: specialist hard gates, correction knowledge
L41: | Design domain | Owner | Specialists | Reviewer facade | Domain reviewer |
L43: | Digital product UI, responsive web, mobile, desktop | `master-design` | relevant design ports; `adaptive-component-design` when needed | `design-review` | built-in interactive/profile strategy |
L44: | Static marketing, social, ad, poster, banner, thumbnail | `master-design` | typography, color, composition, brand/content specialists | `design-review` | built-in static-visual strategy |
L45: | Presentation slides or decks | `master-design` or presentation owner | narrative, data, visual specialists | `design-review` | built-in presentation strategy |
L47: ### External adapter domains
L49: | Design domain | Owner | Reviewer facade | Domain reviewer | Coverage when loaded |
L51: | Logo and brand identity systems | declared brand/identity owner | `design-review` | `brand-identity-review` (`BI`) | `ADAPTER_COVERED` |
L52: | Packaging and specialist print production | declared packaging/print owner | `design-review` | packaging/print reviewer | adapter-defined |
L53: | Motion graphics, film, video editing | declared motion/video owner | `design-review` | motion/video reviewer | adapter-defined |
L54: | Industrial or physical product design | declared industrial-design owner | `design-review` | industrial-design reviewer | adapter-defined |
L55: | Architecture, interior, or spatial design | declared spatial-design owner | `design-review` | spatial-domain reviewer | adapter-defined |
L56: | Fashion design | declared fashion-design owner | `design-review` | fashion-domain reviewer | adapter-defined |
L57: | Service-design systems | product/service owner | `design-review` only for visual artifacts | service-design reviewer | adapter-defined |
L62: coverage_mode: LIMITED
L64: handoff: install/load domain reviewer or route to domain specialist
L67: Universal visual review remains supplementary and cannot certify complete specialist-domain quality.
L69: ## Design Ownership Rules
L72: broad product UI/UX
L73: owner: master-design
L78: owner: master-design
L79: specialist: adaptive-component-design
L83: owner: declared brand/identity owner
L87: coverage: ADAPTER_COVERED when loaded
L99: A narrow advisory question may use a specialist without a reviewer when no artifact is being accepted.
L105: | Intent | Owner | Specialists | Reviewer |
L111: | Native AI runtime, adapter, contract | `native-ai-engineer` | `master-engineer`, runtime skills | `architecture-review` |
L113: ### Product and Research
L115: | Intent | Owner | Specialists | Reviewer |
L117: | Product gap analysis | `product-manager` | domain owners and experts | relevant domain reviewer |
L118: | Requirements and acceptance criteria | `product-manager` | technical/design owners | relevant review workflow |
L119: | Interviews, JTBD, assumption validation | `user-research` | `product-manager` | research evidence review |
L120: | Survey or usability test | `user-research` | `ux-psychology` | product owner synthesizes implications |
```

### rule-manager

- Path: `skills/rule-manager/SKILL.md`
- Contract: `contracts/skills/governance/rule-manager.contract.yaml` @ `0.1.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L10: Rules live in `AGENTS.md`, `.cursorrules`, or product rule files.
L13: **Do not put procedures in rules. Do not put constraints in skills.**
L17: - Writing or updating `AGENTS.md` for a product
L20: - Onboarding a new agent to a product context
L38: - Be careful with production
L55: - Engineering contract: products/<product>/engineering-contract.yaml
L56: - Design contract: products/<product>/ui-design-system-contract.yaml
L70: - Do not modify files outside the assigned task scope
L71: - Do not refactor code unrelated to the current task
L72: - Do not create new abstractions without an ADR
L74: ## Agent Boundaries
L75: - Do not make architecture decisions — raise a flag instead
L76: - Do not approve your own generated output
L77: - Do not merge without human approval
L104: - [ ] Every rule is traceable to engineering contract or product decision?
L108: - [ ] Agent boundary rules explicit — what agent must NOT decide alone?
L109: - [ ] Rules have been reviewed by product owner or tech lead?
L119: - [ ] Source control boundaries
L123: - [ ] Scope boundaries per task
L128: For each gap → write a rule or confirm it's covered by engineering contract.
L150: | No scope boundary rules | Agent modifies files outside task scope |
```

### security-review

- Path: `skills/security-review/SKILL.md`
- Contract: `contracts/skills/security/security-review.contract.yaml` @ `0.1.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L6: No deploy to production without security gate.
L13: - Before deploying to staging or production
```

### service-design

- Path: `skills/service-design/SKILL.md`
- Contract: `contracts/skills/architecture/service-design.contract.yaml` @ `0.1.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L13: - Conway's Law — team structure requires service boundary
L20: ## Step 1: Identify Service Boundaries via Bounded Context
L22: Service boundaries must align with bounded contexts (DDD). One bounded context = one service candidate.
L34: **Wrong signal:** Service boundary crosses bounded context = distributed monolith.
L44: ## Step 2: Data Ownership — Each Service Owns Its Data
L96: HALF-OPEN → probe requests to test recovery
L133: New bounded context = new service from day one — do not add to existing monolith.
L141: | Distributed Monolith | Services share DB, or sync call chains 3+ deep | Redesign boundaries, introduce async |
L172: Before finalizing service boundaries:
```

### skill-eval

- Path: `skills/skill-eval/SKILL.md`
- Contract: `contracts/skills/quality/skill-eval.contract.yaml` @ `0.1.0`
- Type/version: `skill` / `1.1.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L3: `skill loaded` does not mean `skill applied`.
L34: positive and negative rules do not directly contradict
L38: Contract validation does not prove an agent applied the skill.
L70: description: Cross-device acceptance needs owner, specialist, and reviewer.
L82: - pattern: "Owner"
L83: must_come_before: "Specialist|Reviewer"
L85: - one_owner
L104: │   ├── screenshot-dashboard-runtime-not-verified.txt
L111: Do not evaluate several different triggers against one shared output. Each case requires its own generated response.
L151: --case screenshot-dashboard-runtime-not-verified \
L152: --output-file eval-outputs/design-review/screenshot-dashboard-runtime-not-verified.txt
L202: model/runtime/context version
L209: Do not patch a skill from a failed eval until the failure is classified as:
L217: local product override
L229: | Ignore missing outputs | Evaluation coverage is overstated |
```

### skill-evolution

- Path: `skills/skill-evolution/SKILL.md`
- Contract: `contracts/skills/quality/skill-evolution.contract.yaml` @ `1.0.0`
- Type/version: `workflow` / `1.0.0`
- Audit status: `REVIEW_REQUIRED`
- Low-evidence items: `['promoting_unverified_anecdotes']`

**Contract covers**

- `post_fix_learning_review`
- `reusable_reason_extraction`
- `local_vs_shared_knowledge_classification`
- `target_layer_selection`
- `minimal_skill_or_reference_patch`
- `regression_eval_creation`
- `skill_version_and_promotion_decision`
- `provenance_logging_outside_skill_body`

**Contract delegates**

- `solving_the_original_product_issue`
- `copying_product_implementation_into_shared_skills`
- `storing_product_specific_breakpoints_routes_or_component_names_in_shared_skills`
- `promoting_unverified_anecdotes`
- `bypassing_repository_write_or_approval_policy`
- `replacing_product_design_locks_or_architecture_decisions`

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L1: # Skill Evolution
L8: → classify the knowledge scope
L9: → generalize the reusable reason
L10: → patch the smallest correct shared layer
L11: → add a regression eval
L13: → commit when repository policy permits.
L16: A resolved product issue is always reviewed for learning, but it is **not always promoted**.
L18: Do not copy the implementation story into `SKILL.md`. Shared skills store reusable decision logic. Product repositories store product-specific decisions and implementation details. Tests store concrete regression cases.
L24: - a real implementation or design issue was observed;
L26: - the fix passed relevant runtime, visual, interaction, accessibility, or test verification;
L27: - the workflow is about to deliver or close the issue.
L29: The parent workflow must not wait for the user to say “update the skill.” The learning review is a required post-fix phase.
L31: If no reusable learning exists, produce an explicit `NO PROMOTION` verdict and continue delivery.
L39: product: <product or project name>
L42: verified_fix: <what changed locally>
L44: candidate_skill_or_workflow: <likely owner of the missing reasoning>
L45: implementation_diff: <optional>
L48: Product names and implementation details are valid evidence here. They are not automatically valid shared-skill content.
L52: Write the factual case record:
L56: Why the previous decision failed:
L57: Verified local fix:
L62: Fail closed when the fix is only assumed, visually unverified, or not regression-tested. Unverified ideas are learning candidates, not promotable knowledge.
L64: ## Phase 2 — Classify the target layer
L68: | Classification | Destination | Shared skill patch |
L70: | Local implementation defect | Product repository code | No |
L71: | Product-specific durable decision | Product `DESIGN.md`, design lock, ADR, or context | No |
L72: | Reusable decision rule or quality gate | Target `SKILL.md` | Yes |
L73: | Extended reusable rationale or matrix | Target `references/` | Yes |
L74: | Workflow ordering or role-loading gap | Workflow `SKILL.md` | Yes |
L75: | Correct rule applied unreliably | Regression eval/test | Eval only |
L76: | Missing public cross-adapter obligation | `ai-native-core` contract | Controlled |
L78: Examples of local-only details:
L80: - route names;
L81: - repository paths;
L82: - exact project breakpoints;
L83: - component names unique to one product;
L85: - a specific card height;
L86: - brand-specific decisions.
L88: Examples of reusable learning:
L90: - decision factors omitted by the skill;
```

### spec-workflow

- Path: `skills/spec-workflow/SKILL.md`
- Contract: `contracts/workflows/spec-driven.contract.yaml` @ `None`
- Type/version: `workflow` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L7: Precise specs → agent-executable tasks → production-grade output.
L28: Define the non-negotiables for this product/repo:
L41: - ""                       # e.g. "do not introduce new dependencies without ADR"
L53: Load `product-manager`.
L117: **Gate:** Tasks must have context pack before agent handoff.
L136: **Out of scope:**
L172: | **2. Specify** | `product-manager` | Testable ACs, explicit scope |
```

### spike

- Path: `skills/spike/SKILL.md`
- Contract: `contracts/skills/engineering/spike.contract.yaml` @ `0.1.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L10: - The work is production path — use the `plan` skill instead
L112: **Parallel comparison spikes (002a / 002b) — delegate.** When two approaches can run in parallel and both need real engineering (not 10-line prototypes), fan out with `delegate_task`:
L115: delegate_task(tasks=[
L169: - **Data handoffs** — spike A's output was assumed compatible with spike B's input; never proven
L180: - Keep the code throwaway — a spike that takes 2 days to "clean up for production" was a bad spike
```

### systematic-debugging

- Path: `skills/systematic-debugging/SKILL.md`
- Contract: `contracts/skills/quality/systematic-debugging.contract.yaml` @ `0.1.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L27: - Bugs in production
L77: For each component boundary: log what enters, log what exits, verify config propagation. Run once to gather evidence showing WHERE it breaks, THEN investigate that specific component.
L85: - [ ] Loop is deterministic (or flaky bug has high enough reproduction rate)
L89: **STOP:** Do not proceed to Phase 2 until you understand WHY it's happening.
L95: ### 1. Minimize the Reproduction
L127: Simplest possible reproduction. Automated test if possible. MUST exist before fixing.
L162: 4. Do NOT look at previous fix attempts — start clean
L163: 5. If still stuck after Phase 1-3: escalate to human — this is an architecture boundary
L165: **Rule:** If an agent has attempted the same class of fix 3 times, it does not need another attempt. It needs better diagnosis.
```

### systems-thinking

- Path: `skills/systems-thinking/SKILL.md`
- Contract: `contracts/skills/architecture/systems-thinking.contract.yaml` @ `0.1.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

_No boundary-related excerpt detected._

### technical-debt-governance

- Path: `skills/technical-debt-governance/SKILL.md`
- Contract: `contracts/skills/engineering/technical-debt-governance.contract.yaml` @ `1.0.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L5: > 2. **Never pay debt without tests.** No test coverage = can't safely refactor.
L6: > 3. **Debt register must be visible to the product team.** Engineering-only registers drift into irrelevance.
L46: > **Reminder:** classify before paying · no paydown without tests · register visible to product team.
```

### test-driven-development

- Path: `skills/test-driven-development/SKILL.md`
- Contract: `contracts/skills/engineering/test-driven-development.contract.yaml` @ `0.1.0`
- Type/version: `skill` / `1.1.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L31: NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST
L96: NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST
L107: Production code → test exists and failed first
```

### threat-modeling

- Path: `skills/threat-modeling/SKILL.md`
- Contract: `contracts/skills/security/threat-modeling.contract.yaml` @ `0.1.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L9: Design phase: $1 | Implementation: $10 | Testing: $100 | Production: $1000+
L14: Run threat modeling for: every new API endpoint, auth/authz change, new service/integration, or trust boundary change.
L32: ## Step 2: Identify Trust Boundaries
L34: A trust boundary = anywhere data crosses from one trust level to another.
L42: Mark every arrow that crosses a trust boundary.
L47: ## Step 3: STRIDE Per Trust Boundary
L59: Example — Trust boundary: Internet → Login API
L75: Damage potential / Reproducibility / Exploitability / Affected users / Discoverability (1-3 each)
L98: trust_boundaries:
L99: - boundary: internet_to_login_api
L132: [ ] Trust boundaries identified
L133: [ ] STRIDE applied per boundary
L144: - [ ] All trust boundaries identified?
L145: - [ ] STRIDE applied at every trust boundary?
```

### ui-components

- Path: `skills/ui-components/SKILL.md`
- Contract: `contracts/skills/design/ux-ui-patterns.contract.yaml` @ `1.0.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L7: 3. **After 2 failed patches → `write_file` full rewrite.** Do not keep patching broken CSS.
```

### user-research

- Path: `skills/user-research/SKILL.md`
- Contract: `contracts/skills/product/user-research.contract.yaml` @ `1.0.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L14: DISCOVERY (what problem to solve):  User interviews (generative), diary studies, contextual inquiry
L46: ❌ Never show your product before exploring the problem space
L66: Users don't buy products — they hire them to do a job.
```

### ux-psychology

- Path: `skills/ux-psychology/SKILL.md`
- Contract: `contracts/skills/design/ux-psychology.contract.yaml` @ `0.1.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L65: | 9 | **Help users recognize, diagnose, recover from errors** | Error message says "Error 500" not what happened + what to do |
```

### ux-ui-patterns

- Path: `skills/ux-ui-patterns/SKILL.md`
- Contract: `contracts/skills/design/ux-ui-patterns.contract.yaml` @ `1.0.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L73: > Missing interactive states (focus, error, loading) = incomplete design — do not ship.
```

### web-performance

- Path: `skills/web-performance/SKILL.md`
- Contract: `contracts/skills/quality/web-performance.contract.yaml` @ `1.0.0`
- Type/version: `skill` / `1.0.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

_No boundary-related excerpt detected._

### workflow-router

- Path: `skills/workflow-router/SKILL.md`
- Contract: `contracts/skills/meta/workflow-router.contract.yaml` @ `0.2.1`
- Type/version: `meta-skill` / `1.3.0`
- Audit status: `NO_CONTRACT_BOUNDARY`
- Low-evidence items: `[]`

**Contract covers**

- _None_

**Contract delegates**

- _None_

**Current declarations**

- Covers: `None`
- Delegates: `None`

**Evidence excerpts**

```text
L13: No execution before routing. The artifact noun does not determine the lifecycle: a dashboard or logo may be audited, refined, redesigned, implemented, or reviewed for release.
L19: | Build a product from zero | `product-development-workflow` | research, requirements, design, engineering |
L22: | Change design direction, structure, or multiple layers | `redesign-workflow` | owner, specialists, `design-review` |
L24: | Add a capability to an existing product | `new-feature-workflow` | spec, product/design/engineering owners |
L27: | Plan or specify | `spec-workflow` | product-manager, plan, relevant owners |
L36: lifecycle: audit | refinement | redesign | production | advisory
L44: audit, critique, score, evaluate, gap report, production-readiness review
L50: Audit ends with findings unless production was explicitly requested.
L57: sufficient domain coverage
L71: A narrow known problem does not become redesign merely because the user says “polish”.
L77: → role-switcher + relevant owner/specialists
L82: ## Domain Coverage
L87: coverage: BUILT_IN
L91: coverage: BUILT_IN
L95: coverage: BUILT_IN
L100: coverage: ADAPTER_COVERED when adapter is available
L109: Never represent universal visual gates as complete specialist-domain coverage.
L118: | “replace the logo concept and identity direction” | `redesign-workflow` + identity owner; review with `brand-identity-review` |
L125: | “build product from zero” | `product-development-workflow` |
L137: Product from zero / no PRD? → product-development-workflow
L146: then resolve domain reviewer and coverage
L159: ### Identity adapter available
L164: Request: "Review whether this logo system is production-ready"
L172: Coverage: ADAPTER_COVERED
L173: Execution boundary: report only; no redesign
L176: ### Identity adapter unavailable
L182: Coverage: LIMITED
L184: Handoff: install/load adapter or route to identity specialist
L189: `workflow-router` chooses lifecycle. `role-switcher` assigns owner, specialists, facade, and domain reviewer.
L194: owner: declared brand/identity owner
L215: | Average score chooses lifecycle | Use intent, direction, root cause, coverage, hard gates |
L217: | Identity adapter exists but router ignores it | Route to `brand-identity-review` with BI namespace |
L218: | One request executes competing primary workflows | Select one lifecycle and explicit handoffs |
```
