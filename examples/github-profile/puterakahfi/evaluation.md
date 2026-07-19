# Putera Kahfi GitHub Profile Evaluation

## Fixture

```yaml
profile_repository: puterakahfi/puterakahfi
profile_url: https://github.com/puterakahfi
initial_commit: c1a3f65b6138093e8a817019425aca23c681f0c7
first_refinement_commit: d5ebd185a1d78f7ce11cfba87e24c3c30092b9ff
line_free_but_foundation_failed_commit: 4319b26c20b51e1a23e350a65bf29ec01788c775
foundation_corrected_commit: 8b09299ad169221ec2daf1a3b05110d2af229c53
skill: github-profile@1.2.0
workflow: redesign-workflow@3.3.0
mode: create_then_redesign_then_correct
output_mode: patch
```

## Behavioral Result

```text
classification: APPLIED_REVIEWED_CORRECTED
rendered_delivery_verdict: NOT_VERIFIED
```

The fixture exercises a real correction loop rather than accepting valid Markdown or a stylistic label as finished design:

1. generate a proof-first profile
2. publish to the real GitHub Profile README surface
3. inspect a user-provided desktop screenshot
4. identify generic hierarchy and brand-differentiation failures
5. apply a local visual refinement
6. inspect another user-provided screenshot
7. detect that the refinement violated design foundation and brand alignment
8. reload `redesign-workflow`, compose one design owner and selected specialists
9. compare two valid direction candidates
10. select and patch a foundation-led zen composition
11. convert both failures into permanent skill rules and regression tests

## Preserved Equity and Locks

```yaml
preservation_locks:
  identity:
    - Putera Kahfi
    - Native AI Engineering
    - Product and design systems
  proof:
    - AI Native Skills
    - Native AI Core
    - VisualMate
  brand_grammar:
    mood: zen and calm editorial
    density: sparse but information-bearing
    spacing: purposeful and relational
    separators: no decorative lines
    containment: no cards or blockquote project containers
    expression: restrained, readable, personal
```

## Version 1.0 · Source Success, Render Failure

The initial version passed important behavioral checks:

- positioning before technologies
- selected work before capability inventory
- explicit role, contribution, and state
- public proof without exposing private repositories
- no fabricated employer, metric, client, or achievement claims
- no badge wall, statistics wall, counters, animations, or third-party widgets

The first screenshot produced this rendered verdict:

```text
PASS     factual integrity
PASS     proof before badges
PASS     GitHub-native readability
PASS     anti-clutter
PARTIAL  first-viewport memorability
PARTIAL  information hierarchy
PARTIAL  visual composition
FAIL     brand differentiation
```

Observed failures:

- generic name + role + paragraph + links opening
- nearly every section used equal heading-plus-paragraph treatment
- projects read like documentation entries
- multiple sections repeated related ideas
- the document was clean but visually anonymous

## Version 1.1 · Distinctive but Brand-Conflicting

The next refinement introduced:

- thesis-led opening
- blockquote proof modules
- code-box process flow
- reduced content overlap

This improved differentiation but introduced a new root-cause defect:

```text
FAIL  brand continuity
```

The proof blocks and code container used a technical-documentation grammar that conflicted with the established `pkahfi.com` direction: zen, more space, and no lines.

Learning:

```text
distinctive ≠ brand-aligned
GitHub-native ≠ automatically appropriate
```

## Version 1.2 Attempt · Line-Free but Foundation Failure

A line-free refinement removed borders, blockquotes, code boxes, and horizontal rules. The second screenshot showed that the correction was too literal.

Foundation findings:

```text
F1 HIERARCHY   FAIL     page anchor, section label, item, and metadata were too close in weight
F2 GROUPING    FAIL     projects were visually detached by oversized gaps
F3 ALIGNMENT   PARTIAL  centered identity worked, but the body lacked strong role anchors
F4 RHYTHM      FAIL     large spacing repeated across unrelated transitions
F5 BALANCE     FAIL     small content mass floated inside a tall empty canvas
F6 FLOW        PARTIAL  order was logical, but long voids weakened continuation
F7 LEGIBILITY  FAIL     small labels carried critical section identity
F8 CONSISTENCY PASS     repeated roles were treated consistently
F9 ACCESS      PASS     semantic text and links remained available
F10 RESPONSIVE NOT_VERIFIED
```

Root cause:

> “More space” was translated into more `<br>` elements instead of relational spacing. The result contained dead space rather than Ma.

This directly violated `design-spacing`:

```text
sparse content needs less space, not more
vertical rhythm first
Ma is intentional presence, not absence
```

## Workflow Correction

The correction was rerouted through `redesign-workflow`.

### Role composition

```yaml
lifecycle_owner: redesign-workflow
design_owner: master-design
implementation_owner: master-engineer-equivalent repository patch owner
repository_write_owner: GitHub connector
specialists:
  - design-foundation
  - design-brand
  - composition
  - visual-hierarchy
  - design-spacing
  - readability
  - content-strategy
reviewer: design-review rendered-static facade
```

### Direction candidates

```text
A  Centered Zen Manifesto
   centered identity opening → left-aligned proof and detail
   hierarchy through H3/H4, weight, measure, proximity, and cadence

B  Zen Technical Index
   fully left-aligned, compact, highly utilitarian
   faster scanning but weaker continuity with the personal-brand opening
```

Selected: **Centered Zen Manifesto**.

Reason: it preserves the calm personal-brand identity while restoring a clear editorial focal sequence.

### Corrected hierarchy

```text
page anchor     H3 centered name
positioning     bold supporting role
thesis          H4 authored proposition
section parent  H3 left-aligned
project item    H4 linked title
metadata        italic supporting line
body            concise explanatory copy
action          bounded profile links
```

### Corrected spatial rhythm

```text
element gap < item gap < section gap
```

- related project anatomy stays attached
- projects have stronger separation than their internal details
- sections have the strongest pause
- only one bounded centered opening is used
- no decorative lines, cards, blockquotes, or visual boxes

## Contract Mapping

```text
PASS  positioning before decoration
PASS  proof before badges
PASS  no fabricated identity or metrics
PASS  product/founder narrative
PASS  anti-clutter
PASS  generic-documentation failure converted to a regression case
PASS  brand preservation now precedes genre expression
PASS  foundation now precedes zen styling
PASS  dead-space failure converted to a regression case
```

## GitHub Activation and Source Checks

```text
PASS  repository name matches username
PASS  repository is public
PASS  non-empty README.md exists at repository root
PASS  default branch is main
PASS  semantic source order
PASS  project proof before capability inventory
PASS  no external image or widget dependency
PASS  no private email or repository details exposed
PASS  source remains human-editable
PASS  current statements are dated
```

## Render Acceptance

```text
PASS          initial desktop render captured and reviewed
PASS          line-free foundation-failed desktop render captured and reviewed
NOT_VERIFIED  foundation-corrected desktop render not yet captured
NOT_VERIFIED  foundation-corrected narrow-width render not captured
NOT_VERIFIED  light/dark visual comparison not captured
```

The screenshots are valid evidence for rejecting the earlier attempts. The current foundation-corrected source still requires direct rendering before a `READY` or full `PASS` verdict.

## Learning Result

```text
universal design principles are portable
brand grammar constrains genre expression
clean is a baseline, not differentiation
distinctive is insufficient when brand-conflicting
whitespace is relational structure, not quantity
zen does not exempt hierarchy, grouping, balance, or legibility
source validity does not prove rendered composition
GitHub Profile README needs document-specific translation
```

Potential next evolution: register a dedicated `developer-profile` or `document-portfolio` reviewer after comparing additional engineer, founder, maintainer, and designer fixtures.
