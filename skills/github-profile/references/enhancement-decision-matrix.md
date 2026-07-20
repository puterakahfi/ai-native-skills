# Enhancement Decision Matrix

Enhancements are optional profile components such as banners, badges, icons, counters, stats, generated cards, certification marks, and contribution animations.

Their job is to improve comprehension, proof, trust, or brand recognition. “Looks cool” is not enough.

## Decision Axes

Evaluate every enhancement:

```yaml
enhancement_decision:
  component:
  intended_job:
  decision_value: 0..3
  evidence_value: 0..3
  brand_fit: 0..3
  visual_cost: 0..3
  maintenance_risk: 0..3
  external_dependency_risk: 0..3
  narrow_width_risk: 0..3
  accessibility_risk: 0..3
  semantic_fallback:
  status: APPROVED | RECOMMENDED | REJECTED | NOT_VERIFIED | NOT_APPLICABLE
  reason:
```

Higher visual cost or risk is worse. Approval requires a useful job, acceptable risks, and semantic fallback.

## Default Policy

| Enhancement | Default | Approve when | Common rejection reason |
|---|---|---|---|
| Owned banner | conditional | stable brand asset, correct aspect behavior, useful identity cue, semantic text nearby | dominates first viewport, conflicts with brand, poor mobile crop |
| Project/build badge | conditional-useful | accurately communicates build, release, license, or support state for a relevant project | badge wallpaper or stale state |
| Skill icons | restrained | improves scanning of a small capability set after positioning and proof | replaces evidence or becomes logo inventory |
| Social badges | usually plain links | badge treatment adds real recognition without noise | repeated brand-colored buttons dominate action hierarchy |
| GitHub stats card | usually reject | audience and decision need are explicit, interpretation is bounded, service is stable | activity presented as expertise or impact |
| Streak card | reject by default | rare community or habit context explicitly requires it | gamifies activity without proof value |
| Top languages | reject as expertise proof | only as descriptive repository-usage context with caveat | misread as proficiency or professional depth |
| Visitor counter | reject | exceptional campaign measurement with verified need and privacy/dependency review | no visitor decision value |
| Typing animation | reject by default | animation is an established identity motif and motion remains accessible | delays comprehension, generic novelty, dependency risk |
| Contribution snake | reject by default | explicitly playful/creative goal, brand fit, non-critical placement, maintained workflow | animation noise, workflow maintenance, contribution theatre |
| Certification badge | conditional | verified, relevant to target positioning, destination proves credential | unrelated or unverified credential wall |
| Competitive-programming stats | conditional | problem-solving competition is relevant to audience and verified | unrelated to actual role or project proof |
| Personal fun fact | optional | humanizes identity without displacing proof or exposing unwanted personal data | filler, privacy risk, or off-brand tone |

These defaults are not prohibitions. They establish the burden of proof.

## Evidence Interpretation

```text
activity ≠ impact
frequency ≠ quality
language usage ≠ expertise
stars ≠ ownership
followers ≠ product value
visitor count ≠ trust
certification ≠ applied capability
```

When a metric is included, label what it actually measures and avoid implied conclusions.

## Banner Contract

An approved banner must:

```text
□ be owned or properly licensed
□ support the established brand grammar
□ preserve a readable first viewport
□ crop or scale acceptably on narrow screens
□ avoid critical text that disappears with the image
□ include meaningful alt text
□ have a stable repository-owned path when possible
□ work in light and dark contexts or declare its limitation
```

## External Dependency Contract

For every third-party image, SVG, card, or generated service:

```yaml
external_dependency:
  service:
  purpose:
  critical: false
  failure_behavior:
  privacy_or_tracking_note:
  theme_behavior:
  narrow_behavior:
  maintenance_owner:
  fallback_text:
```

Critical identity, proof, and actions must remain usable when the dependency fails.

## Enhancement Budget

Default budget:

```text
one identity treatment
one differentiation device
zero to two non-critical dynamic enhancements
one coherent icon or badge family when approved
```

The budget may be lower for zen, editorial, accessibility-sensitive, or maintenance-sensitive profiles.

## Review Questions

```text
Does this help a visitor decide or verify something?
Would the profile lose meaning if it disappeared?
Does it compete with stronger project proof?
Does it introduce a new visual language?
Will it wrap, crop, animate, or fail poorly?
Who maintains it?
What false conclusion could a visitor draw from it?
```

Reject enhancements whose main value is novelty while their cost is hierarchy, accessibility, maintenance, or evidence integrity.
