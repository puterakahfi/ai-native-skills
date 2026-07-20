---
name: github-profile
description: Generate, redesign, or audit a GitHub profile as an evidence-backed personal brand and technical portfolio — resolve audience and positioning, curate the full profile surface, preserve established brand grammar, select or compare profile variants, compose maintainable GFM/HTML, evaluate repositories and enhancements, render the result, and verify it through the design-review facade.
license: MIT
metadata:
  ai-native-skills.version: 1.4.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.requires: "design-foundation design-brand design-genre design-spacing design-strategy design-visual composition visual-hierarchy readability content-strategy copywriting information-architecture accessibility design-review skill-eval"
  ai-native-skills.related_skills: '["design-typography","design-color","design-iconography","dark-light-theming","redesign-workflow","design-refinement","git-workflow"]'
---

# GitHub Profile

```text
HARD RULES
1. Start from audience, goal, identity, and evidence—not badges or decoration.
2. Never invent employers, projects, metrics, contribution claims, skills, clients, or personal data.
3. Declare scope: readme-only, profile-surface, or full-profile-ecosystem.
4. The opening viewport must answer: who, what value, for whom, and why believe it.
5. Build one profile narrative; do not paste a résumé, portfolio, link tree, repository dump, and dashboard together.
6. Use GitHub-native Markdown/HTML that remains readable when images or widgets fail.
7. External cards, counters, and generated SVGs are optional dependencies, never critical content.
8. Default to restrained visual density; badge walls, animation walls, stat walls, and repository walls are failures.
9. An established personal-brand grammar is a preservation lock.
10. A variant changes expression—not facts, evidence strength, approved strategy, or repository truth.
11. Clean and readable is the baseline, not a sufficient visual direction.
12. README quality cannot hide contradictory pins, inaccessible proof, or weak repository presentation.
13. Pinned repositories must have explicit proof roles; do not fill every available slot by default.
14. Archive, pin, profile-metadata, privacy, and repository-setting changes require explicit approval and capable write ownership.
15. Activity, top languages, stars, followers, streaks, and visitor counts are not expertise or impact by themselves.
16. Verify rendering, links, dependencies, repository state, narrow width, and source maintainability.
17. Review rendered artifacts and observed profile state; source Markdown alone is not visual evidence.
18. Repository mutation and approval belong to the calling workflow.
```

## Purpose and Boundary

Use this skill to create, redesign, refine, compare, or audit a personal GitHub profile.

It owns:

```text
profile strategy and narrative
profile-surface inventory
content architecture
brand translation and preservation locks
variant selection and comparison
README composition
pinned-repository recommendations
selected repository hygiene review
CTA and destination alignment
enhancement decisions and dependency policy
GitHub-specific verification and design-review handoff
```

It composes existing design skills rather than redefining hierarchy, composition, spacing, readability, accessibility, or review rules.

It does not own:

```text
repository authorization
private-data discovery
employment verification
custom illustration production
GitHub account or repository mutations without a capable write owner
automatic pinning, archiving, privacy changes, or settings changes
```

## Scope Modes

```text
readme-only
  compose and verify the profile README
  report adjacent profile-surface contradictions when observed

profile-surface
  audit identity metadata, README, pinned items, selected proof repositories,
  CTA paths, and cross-surface consistency

full-profile-ecosystem
  audit the complete public repository portfolio, repository hygiene,
  discoverability metadata, lifecycle recommendations, contribution paths,
  and optional enhancements
```

Load `references/profile-ecosystem.md` whenever scope is broader than `readme-only`.

## Inputs

```yaml
github_profile_input:
  username: <required for repository-backed work>
  mode: create | redesign | refine | audit | compare-variants
  scope: readme-only | profile-surface | full-profile-ecosystem
  output_mode: readme-only | spec-and-readme | profile-surface-report | ecosystem-report | variant-set | patch
  goal: hiring | consulting | freelance | open-source | founder | personal-brand | community | mixed
  primary_audience: <who should understand and act>
  desired_action: <view projects | contact | hire | collaborate | contribute | sponsor | follow | other>
  identity:
    name: <verified or supplied>
    role_or_positioning: <verified or supplied>
    location: <optional>
    languages: []
    short_bio: <optional>
  evidence:
    selected_projects: []
    products: []
    open_source: []
    achievements: []
    metrics: []
    testimonials_or_clients: []
  capabilities: []
  current_focus: []
  contact_links: []
  profile_surface:
    observed_metadata: {}
    current_pins: []
    public_repositories: []
    contribution_context: []
    external_destinations: []
  repository_curation:
    requested: false
    preferred_proof_roles: []
    protected_repositories: []
    archive_prohibited: []
  enhancements:
    requested: []
    prohibited: []
    dependency_tolerance: low | medium | high
  brand_assets: []
  brand_reference_urls: []
  brand_tokens: <optional>
  brand_grammar:
    mood: <optional>
    density: <optional>
    spacing: <optional>
    separators: <optional>
    alignment: <optional>
    typography_behavior: <optional>
    prohibited_treatments: []
  existing_readme: <optional>
  preservation_locks: []
  prohibited_content: []
  content_archetype: auto | technical-authority | editorial-personal-brand | product-builder | open-source-maintainer | custom
  variant: auto | zen-minimalist | modern-professional | creative-editorial | custom
  requested_variants: []
  comparison_mode: none | concept | rendered
  density: concise | balanced | rich
  visual_direction: auto | text-first | editorial | zen-editorial | showcase | branded
  dynamic_widgets: none | minimal | selective
```

Infer only low-risk presentation choices. Mark missing factual or platform state as `NOT_VERIFIED`; never fill gaps with plausible biography, assumed pins, guessed repository health, or inferred expertise.

## Procedure

```text
1. INVENTORY
   Resolve scope, verified identity, audience, desired action, proof, links,
   existing equity, brand references, preservation locks, profile surfaces,
   repository visibility/state, dependencies, privacy constraints, and gaps.
   Load references/profile-ecosystem.md when scope is broader than README-only.

2. POSITION
   Select one primary narrative and dominant value proposition.
   Load references/strategy-and-content.md.

3. CURATE
   When scope includes profile surface or ecosystem:
   - map selected proof to public repositories and destinations
   - evaluate current pins when observable
   - recommend a complementary pin set with explicit proof roles
   - review selected repository descriptions, topics, READMEs, and lifecycle state
   - mark archive, unpin, or metadata actions as recommendations only
   Load references/repository-curation.md.

4. STRUCTURE
   Select a content archetype and order content by visitor decision needs.
   Keep identity and proof before detail. Merge repeated ideas.
   Content archetype decides information roles; it does not decide visual style.

5. DIRECT
   Apply design-foundation.
   When an established brand exists, apply design-brand and lock its mood,
   density, spacing, separator behavior, alignment, and prohibited treatments.
   Select or compare profile variants through references/variant-selection.md.
   Resolve variant axes through references/variant-system.md.
   Choose a GitHub-appropriate direction and one differentiation device.

6. COMPOSE
   Produce semantic GFM/HTML with restrained assets, contrasting content roles,
   graceful fallback, brand-consistent spacing, and a scannable first viewport.
   Ensure README claims and actions match observed repository and destination state.
   Load the selected file under references/variants/.
   Load references/platform-constraints.md and references/templates.md.

7. ENHANCE
   Evaluate every requested or proposed banner, badge, icon, counter, stat card,
   generated SVG, certification mark, animation, or contribution visualization.
   Approve only when decision value, evidence value, brand fit, accessibility,
   responsive behavior, dependency risk, and maintenance ownership are acceptable.
   Load references/enhancement-decision-matrix.md.

8. RENDER
   Render through GitHub or equivalent GFM at desktop and narrow width.
   For variant comparison, lock facts, completeness, and viewports.
   Inspect both themes when theme-dependent assets are used.
   When scope is broader than README-only, inspect the surrounding profile surface.

9. REVIEW
   Load references/verification.md and route the rendered-static artifact through
   design-review using only universal/static gates applicable to this medium.
   Review README, pins, public proof destinations, CTA consistency, dependency
   behavior, and the declared variant contract within available evidence.

10. REFINE
    Correct the smallest failing layer while preserving accepted narrative,
    facts, links, selected variant, brand grammar, and approved proof roles.
    Change variant only when audience, goal, proof, or brand evidence disproves it.
    Never solve weak repositories by adding more decoration to the README.
```

## Reference Loading

| Need | Load |
|---|---|
| Audience, positioning, evidence, content order | `references/strategy-and-content.md` |
| Full surface, scope, state labels, CTA mapping | `references/profile-ecosystem.md` |
| Pins, proof roles, repository hygiene, lifecycle | `references/repository-curation.md` |
| Banners, badges, stats, counters, icons, animations | `references/enhancement-decision-matrix.md` |
| Variant architecture and invariant facts | `references/variant-system.md` |
| Variant selection or comparison | `references/variant-selection.md` |
| Zen minimalist expression | `references/variants/zen-minimalist.md` |
| Modern professional expression | `references/variants/modern-professional.md` |
| Creative editorial expression | `references/variants/creative-editorial.md` |
| Hierarchy, density, modules, brand translation | `references/visual-system.md` |
| GFM/HTML, images, themes, links, privacy | `references/platform-constraints.md` |
| Content archetype starting structures | `references/templates.md` |
| Render, ecosystem, and design-review checks | `references/verification.md` |

Load only the references required by scope, mode, selected variant, and uncertainty.

## Profile Ecosystem Contract

```text
identity metadata → README → pinned proof → repository presentation
→ contribution context → external destination → desired action
```

These surfaces must tell one compatible story. A README passes only its own scope; it does not automatically validate the surrounding profile.

Use observation states consistently:

```text
OBSERVED | RECOMMENDED | APPROVED | REJECTED | NOT_VERIFIED | NOT_APPLICABLE
```

## Composition Contract

```text
required roles: identity → positioning → proof → selected work → current focus → action
optional roles: capabilities → principles → writing → community → personal interests
profile-surface roles: pins → repository proof → contribution path → external destination
default budget: one hero treatment, one differentiation device,
                zero–two non-critical dynamic enhancements
brand constraint: differentiation uses the established brand grammar
variant constraint: expression may change; facts and proof strength may not
```

A technology list supports positioning; it is not positioning. Statistics may support context; they do not replace project contribution, repository evidence, or verified outcomes.

A sequence of headings and paragraphs may be semantically valid while visually anonymous. At least one major role must receive a distinct GitHub-native treatment. Distinct treatment does not imply cards, borders, dividers, or widgets.

## Variant Contract

```text
zen-minimalist
  calm thesis-led identity, purposeful Ma, no containment by default

modern-professional
  balanced density, crisp proof hierarchy, clear actions, contemporary restraint

creative-editorial
  authored voice, intentional editorial rhythm, one coherent expressive device
```

Record density, alignment, expression, proof emphasis, thesis emphasis, containment, separators, assets, widget policy, and brand overrides. Multi-variant outputs must lock one fact set and equal proof completeness.

## Repository Curation Contract

```text
pins are navigation and proof, not awards
fewer strong complementary pins are acceptable
private implementation is not public source proof
repository age alone does not justify archive
archive and unpin are recommendations until explicitly approved and applied
repository descriptions, topics, and READMEs must support the assigned proof role
```

Every recommended pin requires a primary proof role and visitor question answered.

## Enhancement Contract

Evaluate enhancements by:

```text
decision value
evidence value
brand fit
visual cost
maintenance risk
external dependency risk
narrow-width risk
accessibility risk
semantic fallback
```

Activity, top-language, follower, star, streak, and visitor metrics must be labelled by what they actually measure. Never imply expertise or impact without stronger evidence.

## Output Contract

For `readme-only`, return a complete `README.md` plus declared external dependencies.

For `spec-and-readme`, return:

```yaml
github_profile_result:
  scope:
  profile_goal:
  primary_audience: []
  desired_action:
  narrative:
  content_archetype:
  selected_variant:
  variant_axes: {}
  verified_facts: []
  assumptions: []
  content_gaps: []
  preservation_locks: []
  brand_alignment: {}
  selected_direction:
  differentiation_device:
  section_order: []
  external_dependencies: []
  readme:
  render_evidence: []
  design_review_result:
```

For `profile-surface-report` or `ecosystem-report`, return:

```yaml
github_profile_ecosystem_result:
  scope:
  observed_surface:
    identity: {}
    readme: {}
    pinned_items: {}
    repositories: []
    contribution_context: {}
    destinations: []
  cross_surface_consistency:
  repository_curation:
    current_pins: {}
    recommended_pin_set: []
    recommended_order: []
    unpin_recommendations: []
    archive_candidates: []
    metadata_gaps: []
  enhancement_decisions: []
  cta_alignment:
  privacy_constraints: []
  mutations:
    applied: []
    recommended: []
    rejected: []
    not_verified: []
  render_evidence: []
  github_profile_acceptance:
```

For `variant-set`, return one locked fact set, alternatives, brand fit, trade-offs, publication status, complete READMEs, and comparable render evidence.

For `patch`, hand proposed content and file boundaries to the write owner. Do not claim profile, pin, metadata, topic, or archive changes without tool evidence.

## Acceptance Checks

```text
□ scope is explicit
□ identity, audience, desired action, and narrative are explicit
□ every factual claim is supplied, repository-verifiable, or marked NOT_VERIFIED
□ observed state and recommendations are not conflated
□ existing brand references were inventoried before variant selection
□ content archetype and visual variant are not confused
□ first viewport communicates identity, value, and proof before decoration
□ selected work explains context, ownership, state/outcome, and destination
□ README claims match accessible repository or product evidence
□ current pins are observed or explicitly NOT_VERIFIED
□ each recommended pin has a complementary proof role
□ repository descriptions, topics, READMEs, and lifecycle gaps are explicit
□ archive and unpin actions remain recommendations until approved and applied
□ CTA follows audience and goal
□ enhancements have documented job, risks, fallback, and decision state
□ top languages, activity, stars, followers, streaks, and counters are not expertise proof
□ critical information survives blocked images and unavailable services
□ links, themes, narrow width, accessibility, and maintainability are verified
□ rendered output and surrounding profile surface received review within available scope
□ unavailable evidence remains honestly NOT_VERIFIED
```

Common failures:

```text
generic greeting plus badge/stat wall
clean but anonymous documentation layout
strong README with weak or contradictory pins
six pins filled without six strong complementary proof roles
private repositories presented as public source proof
archive recommendations based only on age
empty descriptions and project READMEs that make visitors guess
modern interpreted as card dashboard
creative interpreted as random emoji, ASCII, or animation
minimalist interpreted as tiny text and maximum emptiness
visitor counter treated as trust
streak or green graph treated as quality
top languages treated as expertise
stars or followers treated as ownership or impact
essential text inside images
critical third-party widgets
fabricated current work or repository state
claimed mutations without write evidence
```

```text
FINAL REMINDER
Purpose before decoration. Proof before badges. One narrative across all surfaces.
Content archetype decides what belongs; variant decides how it is expressed.
Pins route visitors to proof; they are not trophies.
Enhancements require a job, evidence, fallback, and maintenance owner.
Readable is mandatory; recognizable is the next gate; brand continuity constrains both.
Render before review. Preserve NOT_VERIFIED when evidence is missing.
Repository and profile writes require explicit approval and verified tool evidence.
```
