# Eval — Preserve visual personality during structural redesign

## Source case

- Application issue: `puterakahfi/pkahfi#8`
- Skill refinement issue: `puterakahfi/ai-native-skills#21`
- Target: existing `/ai-skills` page in the pkahfi surface family
- Canonical genre reference: `skills/design-genre/references/zen.md`

## Prompt fixture

```text
Redesign an existing capability directory so users start from job intent,
route into the correct lifecycle workflow, and disclose atomic skills progressively.

The broader site has an established zen, spacious, low-containment visual personality.
Preserve valid brand and product equity while improving IA and interaction.
Do not ban lines mechanically: retain a line when it performs necessary control,
orientation, data, diagram, or structural-boundary work supported by the Zen contract.
```

## Evidence available

```yaml
baseline:
  target_source: available
  target_rendered_dom: available
  adjacent_surface_family: owner-confirmed zen, spacious, low-containment
  selected_or_inherited_genre: zen-minimalist
  canonical_genre_reference: skills/design-genre/references/zen.md
  pixel_screenshots_at_initial_direction: unavailable
```

## Expected workflow behavior

```text
1. classify the change as broad redesign because IA, hierarchy, components,
   and interaction change together;
2. capture the target plus adjacent canonical surface-family traits;
3. route genre expression through design-genre and load references/zen.md;
4. inherit Kanso, Seijaku, Ma, the structural-line budget, and allowed exceptions;
5. preserve existing expression while pixel evidence is incomplete;
6. recognize that adding repeated borders, dividers, cards, panels, or density
   changes makes expression an active layer even when IA is the primary task;
7. route design-brand, design-genre, design-visual, and applicable
   layout/spacing/composition specialists;
8. run a repeated-treatment audit before acceptance;
9. preserve a genuinely necessary line when its functional exception is explicit;
10. keep workflow-first IA, intent routing, progressive disclosure, canonical metrics,
    mobile component substitution, and visible feedback when correcting expression drift;
11. require local rendered evidence before PASS.
```

## Passing output characteristics

```yaml
surface_family_baseline:
  shared_visual_traits:
    - calm pacing
    - generous relational space
    - low containment
    - low visual interruption

visual_personality_handoff:
  selected_or_inherited_genre: zen-minimalist
  canonical_genre_reference: skills/design-genre/references/zen.md
  supported_traits:
    - Kanso: remove before adding
    - Seijaku: space is the divider, not lines
    - Ma: intentional intervals with a visual anchor

visual_personality_locks:
  containment_grammar: open composition by default; rare anchor surfaces only when interaction or comparison requires them
  separator_grammar: Ma and Seijaku by default; structural lines are exceptional, not universally forbidden
  line_exception_contract:
    allowed_when:
      - form control or focus affordance
      - required data-table or diagram grid
      - one list-boundary hairline needed for orientation
      - another evidenced structural boundary that space cannot communicate clearly
    requires: explicit functional reason
  repeated_treatment_rules:
    - no treatment becomes the default grammar without a named role

layered_plan:
  structure: refine or replace
  components: refine
  expression: preserve or narrowly refine

verification:
  repeated_treatment_audit: present
  functional_exceptions: recorded
  visual_continuity_report: NOT_VERIFIED until rendered locally
```

## Failure conditions

```text
FAIL if the workflow:
- treats zen, minimal, editorial, or another personality label as sufficient specification;
- restates a new Zen philosophy instead of loading design-genre/references/zen.md;
- inspects only the target page when adjacent canonical surfaces establish the shared language;
- adds repeated borders or cards while classifying expression as unchanged;
- uses borders, dividers, or panels as default hierarchy without named roles;
- declares all lines forbidden and removes a required control, orientation, data, or diagram line;
- accepts a line exception without a functional reason;
- removes accepted IA improvements while correcting only visual drift;
- claims personality continuity from source inspection without rendered evidence;
- marks PASS before visual-continuity and repeated-treatment evidence exist.
```

## Regression assertion

The workflow must be able to return:

```text
accepted IA and interaction changes
+ visual-continuity FAIL/PARTIAL
→ smallest expression-only correction
→ preserve justified functional line exceptions
→ rendered verification
```

It must not force an all-or-nothing redesign rollback or an all-lines-forbidden interpretation.

## Current validation status

```yaml
skill_eval:
  status: PARTIAL
  reason:
    - canonical design-genre Zen reference is now the authority
    - contract and regression fixture cover line proliferation and functional exceptions
    - application expression patch implemented
    - local rendered evidence and independent design-review still pending
  forbidden_claim: improved/PASS before the local retest is completed
```
