# GitHub Profile Platform Constraints

Treat GitHub as the rendering platform, not as a blank web canvas. Platform validity and graceful degradation are part of the design.

## Profile README Activation

GitHub displays a profile README when the repository:

```text
has the same name as the GitHub username
is public
contains a non-empty README.md at the repository root
```

Managed user accounts may not support profile READMEs. Verify the actual account and repository state before claiming activation.

## Rendering Model

Use GitHub Flavored Markdown and only GitHub-supported HTML. GitHub sanitizes rendered content and does not provide arbitrary CSS or JavaScript execution.

Therefore:

```text
semantic Markdown is the primary structure
HTML is a bounded layout aid, not an application framework
custom fonts cannot be assumed
scripts and interactive widgets cannot be assumed
render behavior must be inspected on GitHub or an equivalent renderer
```

Do not ship source that only looks correct in a local Markdown editor with different HTML or CSS behavior.

## Source Size and Complexity

GitHub may truncate very large README files. Keep profile source far below platform limits and avoid embedding giant generated SVG/XML payloads directly into the document.

Prefer:

```text
small semantic README
repository-owned image assets
clear relative paths
few external services
human-editable sections
```

Avoid:

```text
base64 image blobs
huge inline SVG
machine-generated HTML tables
hundreds of badges
duplicated light/dark content blocks
```

## Images

Images may use repository-relative paths or stable external URLs.

For every image verify:

```text
source ownership and expected longevity
alt text
intrinsic and displayed size
transparent-background behavior
light and dark contrast
narrow-width scaling
link destination when the image is actionable
```

Critical information must also appear as semantic text. A banner that contains the person's only readable name or role is not sufficient.

## Theme-Aware Assets

GitHub supports theme-aware image patterns in Markdown/HTML. When using separate light and dark assets:

```text
both variants communicate equivalent information
both URLs resolve
both have appropriate contrast
fallback behavior is acceptable
nearby text remains complete without either asset
```

Do not create theme variants merely for decoration when one robust asset works in both themes.

## Links

Verify:

```text
relative links resolve from README.md
external links use the intended canonical destination
repository links point to the correct owner and branch
mail or social links do not expose unintended private data
image links and text links have clear labels
archived or experimental work is labelled honestly
```

A visually polished profile with broken links fails delivery.

## Third-Party Widgets

Generated statistics, streak cards, contribution snakes, trophies, visitor counters, dynamic typing images, and badge services are external dependencies.

Classify each dependency:

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
criticality must not be critical for third-party widgets
unknown privacy or maintenance risk blocks automatic inclusion
one widget should answer one visitor question
similar widgets must not repeat the same information
failure must leave a coherent profile
```

Default `dynamic_widgets: minimal` means zero or one strongly justified widget, not one widget from every popular provider.

## Privacy and Safety

Public profile content is globally visible. Never infer or expose:

```text
private email addresses
private repository names or activity
client identities without permission
precise personal location beyond supplied intent
employment status not explicitly verified
personal schedules, availability, or contact details
analytics/tracking elements without disclosure and purpose
```

When repository or API data is used, distinguish public facts from inference. Do not treat contribution volume as proof of employment, seniority, or expertise.

## Accessibility

GitHub controls the page shell, but README authors still control content accessibility.

Verify:

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

Animated GIFs and contribution animations are not harmless defaults. Avoid them unless requested and ensure the profile still communicates without motion.

## HTML Layout Cautions

HTML alignment, tables, details/summary, picture/source, and image sizing can be useful. They should remain:

```text
semantically understandable
stable under sanitization
readable without custom styling
usable at narrow width
simple enough for the owner to maintain
```

Do not use nested tables as a substitute for a responsive layout system.

## Repository Assets

Prefer repository-owned assets under a clear path such as:

```text
assets/profile/
assets/projects/
assets/brand/
```

Use lowercase predictable filenames, document generated assets, and avoid committing source credentials or private design exports.

## Verification Sources

For current platform behavior, verify against official GitHub documentation:

- Managing your profile README
- About repository README files
- Getting started with writing and formatting on GitHub
- GitHub Flavored Markdown documentation

Platform behavior is external and may change; re-check it when a render differs from expectation.