# Phase 12 — DELIVER + PITFALLS + ANTI-LOOP

Load `quality-levels.md` before choosing delivery language or declaring the redesign complete.

## File management — hard rule

```text
ONE canonical file/path per project surface. PATCH/WRITE in-place.
NEVER create versioned output files merely to preserve iterations.

❌ pkahfi-v2.html, pkahfi-v3.html, output-final.html
✅ pkahfi.html or the existing repository path, versioned through git

Versioning = commits, not filenames.
```

When a full rewrite is required after two failed patches, overwrite the same canonical path, commit it, and continue. Do not create another artifact name.

## Delivery quality gate

Delivery status must match evidence:

```text
Q1 FOUNDATION-SAFE
  acceptable as an implementation candidate or bounded handoff
  never call it final, pixel-polished, or pixel-perfect

Q2 RENDER-VERIFIED
  acceptable for visual review
  remaining optical or regression gaps must be stated

Q3 PIXEL-POLISHED
  default target for final redesign delivery
  requires rendered verification, optical correction, adjacent-regression check,
  and all applicable foundation/system/genre/domain/accessibility/runtime gates passing

Q4 PIXEL-MATCHED
  only when a locked reference/spec and comparison evidence exist
```

A high average score does not advance the quality level when required evidence is missing.

## Final delivery eligibility

Final `REDESIGN COMPLETE` delivery requires:

```text
□ target quality level reached
□ foundation gates F1–F10 pass with evidence
□ applicable design-system, brand, genre, domain, and content gates pass
□ required routes/artifacts, viewports, themes, and states inspected
□ changed and adjacent regions re-inspected after the final patch
□ optical correction complete
□ runtime/export blockers resolved or explicitly outside the requested boundary
□ accessibility hard gates pass
□ touch target failures = 0 for applicable interactive surfaces
□ unresolved gaps = 0 for Q3/Q4 final approval
```

If the project has a legacy score contract, its threshold still applies, but the score cannot replace the quality-level evidence.

## Delivery procedure

```text
1. Ensure every artifact is at its canonical path.
2. Confirm the current commit matches the verified artifact.
3. Record quality target and achieved quality level.
4. Commit with a descriptive final message when repository write was requested.
5. Deliver the artifact or repository/PR reference.
6. Include gate summary, verification matrix, and key changes.
7. Include an honest gap report when the target level was not reached.
```

Recommended format:

```text
REDESIGN COMPLETE — <target>
──────────────────────────────
Quality target:   Q3 PIXEL-POLISHED
Quality achieved: Q3 PIXEL-POLISHED
Foundation gates: F1–F10 PASS
Contextual gates: PASS
Viewports/themes: <verified matrix>
Routes/states:    <verified matrix>
Iterations:       N
Skills patched:   [list]

Key changes:
  Before: [issue]   After: [fix applied]
  ...
```

When the target level is not reached:

```text
REDESIGN HANDOFF — <target>
────────────────────────────
Quality target:   Q3 PIXEL-POLISHED
Quality achieved: Q1 FOUNDATION-SAFE | Q2 RENDER-VERIFIED
Blocking evidence: [missing or failed checks]
Remaining gaps:    [specific list]
Next correction:   [specific action]
```

Do not hide a Q1 or Q2 handoff behind words such as `final`, `perfect`, `complete`, or `release-ready`.

## Pixel-perfect language

Use `pixel-perfect` only when all of the following are true:

```text
□ user explicitly requests or accepts that term
□ Q4 pixel-matched evidence exists
□ reference/spec and tolerance are declared
□ comparison covers required states and viewports
□ deviations are documented and approved
```

Otherwise prefer:

```text
foundation-safe
render-verified
pixel-polished
pixel-matched within declared tolerance
```

## Pitfalls

### CSS patch corruption

Three or more blind micro-patches to the same CSS block can corrupt selector structure.

**Rule:** after two failed patches on the same region, use rewrite safety. Re-read the whole region or file, then replace the canonical implementation coherently. Never apply a blind third patch.

### Viewport-height void

`min-height: 100vh` on sparse content can create dead space, especially on mobile.

**Rule:** choose height and section rhythm from content, task, device chrome, and composition. Do not use a fixed hero recipe as a universal replacement.

### Sticky versus fixed navigation

Do not enforce one positioning method universally. Select sticky, fixed, static, or contextual navigation from product behavior, scroll requirements, safe areas, and existing system constraints.

### Color-only status signals

Status cannot rely on color alone. Supply visible text or an accessible label and preserve sufficient contrast.

### Improvised behavior

Do not implement interaction from memory when an established pattern or existing product primitive is available. Inspect the trusted behavior source first.

### Build as visual proof

A successful lint, typecheck, test, or build is implementation evidence—not proof of hierarchy, alignment, spacing, balance, flow, responsiveness, or optical finish.

### Screenshot as runtime proof

A screenshot is visual evidence for the captured state only. It does not prove keyboard operation, dynamic states, route integrity, console health, or responsive behavior outside that capture.

## Anti-loop protection

```text
Before each produce/fix:
  iteration_count++
  if iteration_count > max_iterations:
    stop correction
    deliver the best achieved quality level
    report remaining failures and missing evidence honestly

If the same gate fails two iterations in a row:
  classify why the approach failed
  change the correction strategy for that gate
  do not repeat the same patch with slightly different numbers
```

Maximum iterations protect the workflow from endless correction. They do not convert unresolved failures into a pass or elevate the achieved quality level.
