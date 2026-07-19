---
name: github-profile
description: Generate or redesign a GitHub Profile README as an evidence-backed personal brand and technical portfolio — resolve audience and positioning, build a clear content hierarchy, compose a distinctive GitHub-native visual system, produce maintainable GFM/HTML, render it, and verify it through the design-review facade.
license: MIT
metadata:
  ai-native-skills.version: 1.1.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.requires: "design-foundation design-strategy design-visual composition visual-hierarchy readability content-strategy copywriting accessibility design-review skill-eval"
  ai-native-skills.related_skills: '["design-brand","design-typography","design-color","design-iconography","information-architecture","dark-light-theming","redesign-workflow","design-refinement","git-workflow"]'
---

# GitHub Profile

```text
HARD RULES
1. Start from audience, goal, identity, and evidence—not badges or decoration.
2. Never invent employers, projects, metrics, contribution claims, skills, or personal data.
3. The opening viewport must answer: who, what value, for whom, and why believe it.
4. Build one profile narrative; do not paste a résumé, portfolio, link tree, and dashboard together.
5. Use GitHub-native Markdown/HTML that remains readable when images or widgets fail.
6. External cards, counters, and generated SVGs are optional dependencies, never critical content.
7. Default to restrained visual density; badge walls, animation walls, and stat walls are failures.
8. Clean and readable is the baseline—not a sufficient visual direction. Create one recognizable thesis, module treatment, or brand cue.
9. Verify light/dark rendering, narrow screens, alt text, links, and source maintainability.
10. Review the rendered artifact; raw README source is not visual evidence.
11. Repository mutation, approval, and write ownership belong to the calling workflow.
```

## Purpose and Boundary

Use this skill to create, redesign, or refine the `README.md` shown on a personal GitHub profile.

It owns profile strategy, content architecture, GitHub-native visual composition, README generation, dependency choices, and domain verification. It composes existing design skills rather than redefining hierarchy, composition, readability, copywriting, accessibility, or review rules.

It does not own repository authorization, private-data discovery, custom illustration production, employment verification, or general GitHub account configuration.

## Inputs

```yaml
github_profile_input:
  username: <required for repository-backed work>
  mode: create | redesign | refine
  output_mode: readme-only | spec-and-readme | patch
  goal: hiring | consulting | freelance | open-source | founder | personal-brand | community | mixed
  primary_audience: <who should understand and act>
  desired_action: <view projects | contact | hire | collaborate | sponsor | follow | other>
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
  brand_assets: []
  brand_tokens: <optional>
  existing_readme: <optional>
  preservation_locks: []
  prohibited_content: []
  density: concise | balanced | rich
  visual_direction: auto | text-first | editorial | showcase | branded
  dynamic_widgets: none | minimal | selective
```

Infer only low-risk presentation choices. Mark missing factual content as a gap; never fill it with plausible biography.

## Procedure

```text
1. INVENTORY
   Resolve verified identity, audience, action, proof, links, existing equity,
   preservation locks, and missing information.

2. POSITION
   Select one primary narrative and dominant value proposition.
   Load references/strategy-and-content.md.

3. STRUCTURE
   Order content by visitor decision needs; keep identity and proof before detail.
   Merge sections that repeat the same idea in different words.

4. DIRECT
   Apply design-foundation, then choose a GitHub-appropriate direction.
   Declare one differentiation device: thesis, project-module treatment,
   diagram, visual asset, or distinctive editorial rhythm.
   Load references/visual-system.md only after content roles are known.

5. COMPOSE
   Produce semantic GFM/HTML with restrained assets, contrasting module roles,
   graceful fallback, and a scannable first viewport.
   Load references/platform-constraints.md and references/templates.md.

6. RENDER
   Render through GitHub or equivalent GFM at desktop and narrow width.
   Inspect both themes when theme-dependent assets are used.

7. REVIEW
   Load references/verification.md and route the rendered-static artifact through
   design-review using only universal/static gates applicable to this medium.

8. REFINE
   Correct the smallest failing layer while preserving accepted narrative,
   verified facts, links, and visual direction.
```

## Reference Loading

| Need | Load |
|---|---|
| Audience, positioning, evidence, content order | `references/strategy-and-content.md` |
| Hierarchy, density, modules, visual directions | `references/visual-system.md` |
| GFM/HTML, images, themes, links, privacy, dependencies | `references/platform-constraints.md` |
| Starting structures without cloning a generic template | `references/templates.md` |
| Render evidence, acceptance checks, design-review handoff | `references/verification.md` |

Load only the references required by the current mode and uncertainty.

## Composition Contract

```text
required roles: identity → positioning → proof → selected work → current focus → action
optional roles: capabilities → principles → writing → community → personal interests
default budget: one hero treatment, one differentiation device, one accent system,
                zero–two dynamic widgets
```

A technology list supports positioning; it is not the positioning. Statistics support proof; they do not replace project context, role, or impact.

A sequence of headings plus paragraphs may be semantically correct while still failing visually. At least one major content role must receive a distinct GitHub-native treatment—such as a thesis block, compact proof module, diagram, repository-owned visual, or intentionally different editorial cadence. Do not give every section equal visual weight.

## Output Contract

For `readme-only`, return a complete `README.md` plus a short dependency note when external assets are used.

For `spec-and-readme`, return:

```yaml
github_profile_result:
  profile_goal: <resolved>
  primary_audience: <resolved>
  desired_action: <resolved>
  narrative: <one sentence>
  verified_facts: []
  assumptions: []
  content_gaps: []
  preservation_locks: []
  selected_direction: <direction and reason>
  differentiation_device: <declared visual or editorial device>
  section_order: []
  external_dependencies: []
  readme: <complete markdown>
  render_evidence: []
  design_review_result: <verdict or NOT_VERIFIED>
```

For `patch`, hand the proposed content and file boundary to the repository write owner. Do not claim a branch changed without tool evidence.

## Acceptance Checks

```text
□ Identity, audience, desired action, and profile narrative are explicit.
□ Every factual claim is supplied, repository-verifiable, or marked unverified.
□ The first screen communicates identity, value, and proof before decoration.
□ A recognizable thesis, module treatment, or brand cue differentiates the profile.
□ Section order follows visitor questions and one dominant hierarchy.
□ Repetitive sections are merged rather than restating the same positioning.
□ Selected work explains context, role, outcome/current state, and a useful destination.
□ Major content roles do not all use identical heading-plus-paragraph treatment.
□ Badges and widgets support meaning rather than dominate it.
□ Critical information survives blocked images and unavailable services.
□ Alt text, links, themes, narrow width, and source maintainability are verified.
□ Rendered output received design-review or is honestly NOT_VERIFIED.
```

Common failures: generic greeting + badge/stat wall; clean but anonymous documentation layout; claims without project evidence; cards without role or outcome; repeated thesis across multiple sections; essential text only inside a hero image; mixed visual styles; broken theme contrast; counters/trophies as credibility substitutes; critical third-party widgets; fabricated current work; or copied identity.

```text
FINAL REMINDER
Purpose before decoration. Proof before badges. One narrative before many modules.
Readable is mandatory; recognizable is the next gate.
Use verified facts, GitHub-native structure, graceful fallback, and maintainable source.
Render before review. Preserve NOT_VERIFIED when evidence is missing.
Repository writes require an explicit calling workflow and verified tool evidence.
```
