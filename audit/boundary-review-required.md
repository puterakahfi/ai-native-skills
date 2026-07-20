# Boundary Review Queue

Adapters requiring declaration review: **9**

## adaptive-component-design

- Path: `skills/adaptive-component-design/SKILL.md`
- Contract: `contracts/skills/design/adaptive-component-design.contract.yaml` @ `1.1.0`
- Low-evidence items: `['visual_style_and_brand_expression', 'design_token_definition']`

### Covers

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

### Delegates

- `visual_style_and_brand_expression`
- `page_level_macrostructure_selection`
- `design_token_definition`
- `generic_breakpoint_and_fluid_grid_mechanics`
- `implementation_framework_specific_code`
- `product_specific_component_library_mapping`

### Evidence excerpts

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

## decision-provenance

- Path: `skills/decision-provenance/SKILL.md`
- Contract: `contracts/skills/quality/decision-provenance.contract.yaml` @ `1.0.0`
- Low-evidence items: `['proving_runtime_or_design_quality']`

### Covers

- `material_decision_claim_verification`
- `source_attribution`
- `decision_domain_authority_matching`
- `explicit_supersession_and_conflict_detection`
- `scope_lock_route_approval_status_and_ownership_claims`
- `policy_and_required_approval_preservation`
- `decision_ledger_output`

### Delegates

- `making_product_or_design_decisions_for_the_owner`
- `bypassing_legal_security_repository_or_organizational_policy`
- `proving_runtime_or_design_quality`
- `inventing_missing_decision_sources`
- `treating_agent_authored_text_as_owner_approval`

### Evidence excerpts

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

## design-color

- Path: `skills/design-color/SKILL.md`
- Contract: `contracts/skills/design/color-theory.contract.yaml` @ `1.0.0`
- Low-evidence items: `[]`

### Covers

- `hue_saturation_value_decisions`
- `palette_construction`
- `color_harmony_rules`
- `color_psychology_validation`
- `genre_to_palette_mapping`

### Delegates

- `contrast_ratio_wcag`
- `semantic_token_naming`
- `dark_light_switching`
- `component_level_color`

### Evidence excerpts

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

## design-depth

- Path: `skills/design-depth/SKILL.md`
- Contract: `contracts/skills/design/design-depth.contract.yaml` @ `2.1.0`
- Low-evidence items: `[]`

### Covers

- `depth_need_assessment`
- `surface_and_elevation_relationships`
- `atmosphere_and_imagery_integration`
- `overlap_and_layer_architecture`
- `optional_typography_interleave`
- `responsive_depth_fallback`
- `depth_effect_restraint`

### Delegates

- `illustration_creation`
- `product_specific_elevation_token_values`
- `motion_timing_and_reduced_motion_implementation`
- `page_macrostructure`
- `independent_design_acceptance`

### Evidence excerpts

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

## design-iconography

- Path: `skills/design-iconography/SKILL.md`
- Contract: `contracts/skills/design/iconography.contract.yaml` @ `1.0.0`
- Low-evidence items: `[]`

### Covers

- `icon_family_selection`
- `style_consistency_rules`
- `sizing_optical_alignment`
- `genre_to_icon_mapping`
- `a11y_attribute_rules`

### Delegates

- `svg_component_implementation`
- `icon_animation`
- `token_sizing_values`

### Evidence excerpts

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

## design-spacing

- Path: `skills/design-spacing/SKILL.md`
- Contract: `contracts/skills/design/spacing.contract.yaml` @ `1.0.0`
- Low-evidence items: `[]`

### Covers

- `visual_rhythm_decisions`
- `ma_intentional_space`
- `spatial_hierarchy_logic`
- `breathing_room_vs_dead_space`

### Delegates

- `token_values`
- `8px_grid_rules`
- `css_var_declarations`

### Evidence excerpts

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

## design-typography

- Path: `skills/design-typography/SKILL.md`
- Contract: `contracts/skills/design/typography.contract.yaml` @ `1.0.0`
- Low-evidence items: `['leading_tracking_rhythm']`

### Covers

- `typeface_personality_and_selection`
- `display_body_pairing`
- `modular_scale_selection`
- `hierarchy_h1_to_caption`
- `leading_tracking_rhythm`
- `font_rendering_antialiasing`
- `genre_to_typeface_mapping`

### Delegates

- `contrast_ratio_wcag`
- `characters_per_line`
- `minimum_font_size_px`

### Evidence excerpts

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

## redesign-workflow

- Path: `skills/redesign-workflow/SKILL.md`
- Contract: `contracts/skills/quality/redesign-workflow.contract.yaml` @ `2.2.0`
- Low-evidence items: `['deployment_or_publishing', 'legal_trademark_clearance']`

### Covers

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

### Delegates

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

### Evidence excerpts

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

## skill-evolution

- Path: `skills/skill-evolution/SKILL.md`
- Contract: `contracts/skills/quality/skill-evolution.contract.yaml` @ `1.0.0`
- Low-evidence items: `['promoting_unverified_anecdotes']`

### Covers

- `post_fix_learning_review`
- `reusable_reason_extraction`
- `local_vs_shared_knowledge_classification`
- `target_layer_selection`
- `minimal_skill_or_reference_patch`
- `regression_eval_creation`
- `skill_version_and_promotion_decision`
- `provenance_logging_outside_skill_body`

### Delegates

- `solving_the_original_product_issue`
- `copying_product_implementation_into_shared_skills`
- `storing_product_specific_breakpoints_routes_or_component_names_in_shared_skills`
- `promoting_unverified_anecdotes`
- `bypassing_repository_write_or_approval_policy`
- `replacing_product_design_locks_or_architecture_decisions`

### Evidence excerpts

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
