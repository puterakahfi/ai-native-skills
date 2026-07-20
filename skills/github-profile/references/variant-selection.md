# GitHub Profile Variant Selection

Select a variant after verified content, audience, goal, proof strength, and brand grammar are known.

## Decision Precedence

```text
1. explicit user variant request
2. established brand grammar and prohibited treatments
3. primary audience and desired action
4. strongest available proof
5. content quantity and maintenance capacity
6. available stable assets
7. low-risk presentation preference
```

An explicit variant request does not override factual integrity, foundation, accessibility, platform constraints, or an explicit brand prohibition.

## Selection Matrix

| Signal | Strong candidate | Avoid by default |
|---|---|---|
| Calm personal brand, authored thesis, limited visual assets | `zen-minimalist` | card-heavy modern treatment |
| Hiring, consulting, broad professional credibility | `modern-professional` | vague manifesto-only profile |
| Designer-engineer, creative technologist, strong authored voice | `creative-editorial` | random decoration or animation wall |
| Strong public repositories and maintainer proof | `modern-professional` or future technical-index | creative treatment that obscures contribution routes |
| Product builder with visual evidence | `modern-professional` with showcase support | minimalist profile that hides shipped work |
| Missing brand and weak proof | restrained `modern-professional` or text-first | fabricated creative identity |

## Auto-Selection Heuristic

Use qualitative evidence, not a fake universal score. Resolve each candidate against:

```yaml
variant_candidate:
  name:
  audience_fit: strong | moderate | weak
  desired_action_fit: strong | moderate | weak
  proof_fit: strong | moderate | weak
  content_fit: strong | moderate | weak
  brand_fit: strong | moderate | conflict
  maintenance_fit: strong | moderate | weak
  foundation_risks: []
  platform_risks: []
```

Reject any candidate with `brand_fit: conflict` unless the user explicitly authorizes a brand redesign through the correct workflow.

## `zen-minimalist`

Select when:

```text
identity and thesis are stronger than visual assets
the brand values calmness, restraint, Ma, or editorial silence
selected work can be understood through concise semantic text
no-lines or no-card constraints are intentional
```

Do not select when:

```text
the content needs dense comparison or many parallel facts
critical proof would become hidden by excessive restraint
“minimalist” is being used to avoid resolving hierarchy
```

## `modern-professional`

Select when:

```text
visitors need fast professional comprehension
selected projects and capabilities are strong proof
a balanced density improves scanning
the profile needs clear destinations for hiring, consulting, or collaboration
```

Do not interpret modern as:

```text
card dashboard
badge grid
gradient hero
stats wall
multiple third-party widgets
generic SaaS copy
```

## `creative-editorial`

Select when:

```text
authored voice is part of the person's real identity
engineering, design, product, writing, or creative technology intersect
the brand permits more expressive hierarchy and section language
one coherent editorial device can carry the expression
```

Reject when:

```text
creative means changing style every section
proof becomes secondary to atmosphere
critical text is baked into art
mixed emoji, ASCII, badges, GIFs, and decorative assets create noise
```

## Explicit Multi-Variant Request

When the user asks for minimalist, modern, and creative variants:

```text
- produce all requested variants unless one conflicts with a hard brand lock
- keep verified facts, links, and core proof stable
- state each variant's audience and trade-off
- render with the same content baseline and comparable viewports
- recommend one only after comparison against the declared goal and brand
```

A user may request intentionally divergent concepts. Record which concepts are brand-aligned, exploratory, or rejected for publication.

## Variant Recommendation Output

```yaml
variant_recommendation:
  requested_variants: []
  selected_for_publication:
  alternatives:
    - name:
      role:
      audience_fit:
      brand_fit:
      key_tradeoff:
      publication_status: aligned | exploratory | rejected
  comparison_evidence: []
```

## Refinement Boundary

A local rendering problem does not automatically require changing the variant. Correct the smallest failing layer first.

Change variant only when evidence shows the current expression contract is wrong for the audience, goal, proof, or brand—not because one spacing interval, sentence, or project module failed.