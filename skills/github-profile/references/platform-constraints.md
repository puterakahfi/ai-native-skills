# GitHub Profile Platform Constraints

Treat GitHub as the rendering platform, not a blank web canvas. Platform validity and graceful degradation are part of the design.

## Profile README Activation

GitHub displays a profile README when the repository:

```text
has the same name as the GitHub username
is public
contains a non-empty README.md at the repository root
```

Managed user accounts may not support profile READMEs. Verify account and repository state before claiming activation.

## Rendering Model

Use GitHub Flavored Markdown and GitHub-supported HTML. GitHub sanitizes rendered content and does not provide arbitrary CSS or JavaScript execution.

```text
semantic Markdown is the primary structure
HTML is a bounded layout aid, not an application framework
custom fonts cannot be assumed
scripts and interactive widgets cannot be assumed
render behavior must be inspected on GitHub or an equivalent renderer
```

Do not ship source that only works in a local editor with different HTML or CSS behavior.

## Source Size and Complexity

Keep profile source far below platform limits and avoid giant generated SVG/XML payloads.

Prefer:

```text
small semantic README
repository-owned image assets
clear relative paths
few external services
human-editable sections
```

Avoid base64 images, huge inline SVG, machine-generated tables, hundreds of badges, and duplicated theme content.

## Images

Images may use repository-relative paths or stable external URLs. Verify:

```text
source ownership and expected longevity
alt text
intrinsic and displayed size
transparent-background behavior
light and dark contrast
narrow-width scaling
link destination when actionable
```

Critical information must also appear as semantic text. A banner containing the only readable name or role is insufficient.

## Theme-Aware Assets

When using separate light and dark assets:

```text
both variants communicate equivalent information
both URLs resolve and retain contrast
fallback behavior is acceptable
nearby text remains complete without either asset
```

Do not create theme variants merely for decoration when one robust asset works in both themes.

## Links

```text
relative links resolve from README.md
external links use the intended canonical destination
repository links point to the correct owner and branch
contact links expose only intended information
image and text links have clear labels
archived or experimental work is labelled honestly
```

A visually polished profile with broken links fails delivery.

## Third-Party Widgets

Statistics, streak cards, contribution snakes, trophies, counters, typing images, and badge services are external dependencies.

```yaml
external_dependency:
  purpose: <what visitor need it serves>
  provider: <service>
  criticality: decorative | supporting | critical
  data_exposed: <username, repository, request metadata, other>
  theme_support: <verified | partial | none | unknown>
  failure_fallback: <what remains when unavailable>
  maintenance_risk: low | medium | high | unknown
```

Rules:

```text
third-party widgets must never be critical
unknown data or maintenance risk blocks automatic inclusion
one widget should answer one visitor question
similar widgets must not repeat the same information
failure must leave a coherent profile
```

`dynamic_widgets: minimal` means zero or one justified widget, not one from every provider.

## Privacy and Data Boundaries

Public profile content is broadly visible. Never infer or expose:

```text
non-public contact details
non-public repository names or activity
client identities without permission
precise location beyond supplied intent
unverified role or work status
personal schedules or availability
tracking elements without purpose and disclosure
```

Distinguish public facts from inference. Contribution volume does not prove employment, seniority, or expertise.

## Accessibility

```text
semantic heading order
meaningful link labels
alt text for meaningful images
no color-only distinctions
no essential text only inside images
reasonable animation restraint
readable body copy and lists
logical source order
```

Avoid animated GIFs and contribution animations by default. The profile must communicate without motion.

## HTML Layout Cautions

HTML alignment, tables, details/summary, picture/source, and image sizing may help, but must remain:

```text
semantically understandable
stable under sanitization
readable without custom styling
usable at narrow width
simple enough for the owner to maintain
```

Do not use nested tables as a substitute for responsive layout.

## Repository Assets

Prefer clear repository-owned paths:

```text
assets/profile/
assets/projects/
assets/brand/
```

Use predictable lowercase filenames, document generated assets, and exclude credentials or restricted design exports.

## Verification Sources

For current behavior, verify official GitHub documentation for profile READMEs, repository READMEs, writing/formatting, and GitHub Flavored Markdown. Platform behavior may change; re-check it when rendering differs from expectation.