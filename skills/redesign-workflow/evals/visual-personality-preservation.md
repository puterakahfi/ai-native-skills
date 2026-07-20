# Eval — Preserve visual personality during structural redesign

## Source case

- Application issue: `puterakahfi/pkahfi#8`
- Skill refinement issue: `puterakahfi/ai-native-skills#21`
- Target: existing `/ai-skills` page in the pkahfi surface family

## Prompt fixture

```text
Redesign an existing capability directory so users start from job intent,
route into the correct lifecycle workflow, and disclose atomic skills progressively.

The broader site has an established zen, spacious, low-containment visual personality.
Preserve valid brand and product equity while improving IA and interaction.
```

## Evidence available

```yaml
baseline:
  target_source: available
  target_rendered_dom: available
  adjacent_surface_family: owner-confirmed zen, spacious, low-containment
  pixel_screenshots_at_initial_direction: unavailable
```

## Expected workflow behavior

```text
1. classify the change as broad redesign because IA, hierarchy, components,
   and interaction change together;
2. capture the target plus adjacent canonical surface-family traits;
3. translate `zen` into observable, evidence-bounded rules rather than a style keyword;
4. preserve existing expression while pixel evidence is incomplete;
5. recognize that adding repeated borders, dividers, cards, panels, or density
   changes makes expression an active layer even when IA is the primary task;
6. route design-brand, design-visual, and applicable layout/spacing/composition specialists;
7. run a repeated-treatment audit before acceptance;
8. keep workflow-first IA, intent routing, progressive disclosure, canonical metrics,
   mobile component substitution, and visible feedback when correcting expression drift;
9. require local rendered evidence before PASS.
```

## Passing output characteristics

```yaml
surface_family_baseline:
  shared_visual_traits:
    - calm pacing
    - generous relational space
    - low containment
    - separators reserved for real boundaries

visual_personality_locks:
  containment_grammar: open composition by default; framed surfaces only for meaningful interactive focal regions
  separator_grammar: prefer space, alignment, type, and tonal contrast; use lines only at structural or control boundaries
  repeated_treatment_rules:
    - no treatment becomes the default grammar without a named role

layered_plan:
  structure: refine or replace
  components: refine
  expression: preserve or narrowly refine

verification:
  repeated_treatment_audit: present
  visual_continuity_report: NOT_VERIFIED until rendered locally
```

## Failure conditions

```text
FAIL if the workflow:
- treats zen, minimal, editorial, or another personality label as sufficient specification;
- inspects only the target page when adjacent canonical surfaces establish the shared language;
- adds repeated borders or cards while classifying expression as unchanged;
- uses borders, dividers, or panels as default hierarchy without named roles;
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
→ rendered verification
```

It must not force an all-or-nothing redesign rollback.

## Current validation status

```yaml
skill_eval:
  status: PARTIAL
  reason:
    - contract and regression fixture added
    - application expression patch implemented
    - local rendered evidence and independent design-review still pending
  forbidden_claim: improved/PASS before the local retest is completed
```
