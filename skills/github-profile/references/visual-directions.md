# GitHub Profile Visual Directions

Load after audience, narrative, content roles, brand references, and preservation locks are known. Direction expresses the profile strategy; it must not replace it or contradict an established personal identity.

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

## Zen Editorial

Best when the existing brand uses calm rhythm, generous whitespace, low visual noise, and minimal separators.

```text
space creates grouping
short labels instead of heavy section chrome
few heading levels
no decorative horizontal rules
no card simulation by default
no blockquote borders as project containers
no code fences used only as visual boxes
proof separated through cadence, not outlines
one quiet thesis as the recognition device
```

GitHub-native controls:

```text
blank lines and bounded <br> spacing
<sub> labels or restrained bold labels
short paragraphs
plain links with ample separation
left-aligned reading body after a calm centered opening
semantic anchors when line-free labels replace H2 headings
```

Strength: aligned, calm, durable, and highly compatible with personal brands based on Ma, restraint, or editorial minimalism.  
Risk: becoming empty or weak when whitespace is not supported by precise writing and clear content roles.

Whitespace is not decoration. Every large gap must separate a meaningful role: identity, proof, thesis, capability, focus, or action.

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
brand-consistent density and spacing
restrained badge and icon treatment
```

Strength: recognition and continuity.  
Risk: over-branding reducing technical readability and theme compatibility.

`branded` does not automatically mean more visual elements. A mature brand may require fewer elements, no lines, no cards, and more whitespace.

## Selection Matrix

```text
technical authority       → text-first by default
multi-disciplinary        → editorial with one unifying thesis
zen / Ma-led brand        → zen-editorial with spacing as hierarchy
product portfolio         → showcase when visual proof is strong
mature personal brand     → branded while preserving GitHub readability
weak or missing assets    → text-first; do not fabricate a visual identity
mixed goal                → one primary direction, one supporting treatment
```

When a brand reference exists, first derive:

```yaml
brand_grammar:
  mood: calm | energetic | technical | expressive | other
  density: sparse | balanced | dense
  spacing: compact | rhythmic | generous
  separators: none | subtle | structural
  alignment: centered | left | mixed
  typography_behavior: quiet | editorial | expressive | technical
  prohibited_treatments: []
```

Compare at least two plausible directions when `visual_direction: auto` and the choice materially affects hierarchy or asset production. Reject any otherwise-plausible direction that conflicts with the brand grammar.

## Direction Lock

Record:

```yaml
visual_direction_decision:
  selected: text-first | editorial | zen-editorial | showcase | branded
  audience_fit: <reason>
  proof_fit: <reason>
  content_fit: <reason>
  brand_fit: <reason>
  asset_requirements: []
  rejected_alternatives: []
  preservation_locks: []
  prohibited_treatments: []
```

Do not silently change direction during refinement. A failed widget, link, or project module usually requires a local correction, not a new visual concept. A rendered treatment that violates the established brand grammar is not a local success; revert the conflicting treatment and refine within the locked direction.
