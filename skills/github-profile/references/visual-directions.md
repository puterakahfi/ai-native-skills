# GitHub Profile Visual Directions

Load after audience, narrative, content roles, and preservation locks are known. Direction expresses the profile strategy; it must not replace it.

## Text-First

Best for technical authority, maintainers, writers, and profiles with strong written proof.

```text
semantic headings
short lead paragraph
few or no decorative badges
project descriptions with direct links
small capability groups
```

Strength: robust, accessible, maintainable.
Risk: generic output when positioning and evidence are weak.

## Editorial

Best for personal brands combining engineering, product, design, or writing.

```text
strong thesis-driven opening
intentional section titles
alternating concise narrative and proof modules
one restrained accent graphic or wordmark
```

Strength: distinctive through voice and hierarchy.
Risk: vague manifesto content overwhelming proof.

## Showcase

Best for product builders and portfolios with strong visual assets.

```text
compact hero
selected project visuals
short project context and outcome
clear repository/product destinations
minimal supporting stack
```

Strength: immediate shipped-work proof.
Risk: screenshots becoming an unlabelled image gallery.

## Branded

Best when a mature personal identity system already exists.

```text
verified wordmark or banner
consistent asset style
brand vocabulary in section labels
restrained badge and icon treatment
```

Strength: recognition and continuity.
Risk: over-branding reducing technical readability and theme compatibility.

## Selection Matrix

```text
technical authority    → text-first by default
multi-disciplinary     → editorial with one unifying thesis
product portfolio      → showcase when visual proof is strong
mature personal brand  → branded while preserving GitHub readability
weak or missing assets → text-first; do not fabricate a visual identity
mixed goal             → one primary direction, one supporting treatment
```

Compare at least two plausible directions when `visual_direction: auto` and the choice materially affects hierarchy or asset production.

## Direction Lock

Record:

```yaml
visual_direction_decision:
  selected: text-first | editorial | showcase | branded
  audience_fit: <reason>
  proof_fit: <reason>
  content_fit: <reason>
  asset_requirements: []
  rejected_alternatives: []
  preservation_locks: []
```

Do not silently change direction during refinement. A failed widget, link, or project module usually requires a local correction, not a new visual concept.