# Focused Iteration Verification Packets

Use this reference during an active redesign loop when fresh evidence is required before focused review. Creative iteration is not automatically a deploy gate, but it still needs honest domain-appropriate evidence.

## Principle

```text
changed layer
→ smallest sufficient fresh evidence packet
→ focused facade review
→ adjacent regression and preservation checks
```

Full lint, build, typecheck, export preflight, or specialist production checks run when:

```text
user approves the direction for commit/PR/release
the changed implementation requires them for correctness
the declared acceptance criteria require them
specialist production readiness is being claimed
user explicitly requests full verification
```

A deferred command is recorded as deferred, never passed.

## Common packet

Every iteration captures:

```text
changed regions, files, or slides
current artifact/version identifier
primary design domain and artifact state
target gates or acceptance criteria
adjacent regression areas
preservation locks checked
evidence available and gaps
commands/checks run, failed, or deferred
```

## Digital-interface packet

For changed interactive routes/components:

```text
1. changed-file diff check when source changed
2. route/app state is actually mounted
3. rendered inspection at affected viewports/orientations/themes
4. changed controls and states exercised
5. overflow and component substitution inspected
6. relevant pointer/touch/keyboard/gesture behavior checked
7. focus/semantics checked when affected
8. runtime/console or flow-completion evidence when executable
9. brand/content/asset locks compared
```

Do not assume a 200 response means the browser is displaying the intended state. Confirm route, mounted content, and required styles/resources.

Useful runtime diagnosis:

```text
about:blank false alarm
  browser is not on the target route

unmounted surface
  route exists but required content did not mount

stylesheet/resource failure
  content exists but styling/assets are absent

runtime blank
  route, DOM/native tree, and styles exist but visible content is missing

state mismatch
  the captured state differs from the redesign acceptance state
```

A screenshot cannot prove keyboard operation, hidden states, runtime integrity, responsive substitution, or reversibility.

## Visual-communication packet

For poster, banner, social, ad, thumbnail, or other static work:

```text
1. current export at declared dimensions/ratio
2. actual-size or destination-size inspection
3. crop, safe-area, and overlay simulation
4. mandatory text survival and legibility
5. supplied logo/product/person/content comparison
6. edge/mask, resolution, compression, and color inspection when affected
7. adjacent layout and hierarchy regression check
```

Do not run runtime, keyboard, touch, or reduced-motion checks on a static image.

## Presentation packet

For slide or deck changes:

```text
1. affected slide at actual delivery scale
2. preceding and following slides
3. complete narrative sequence when structure changed
4. screen-share, room, or self-guided viewing simulation
5. chart/data/source verification when affected
6. deck consistency and repeated-layout regression
7. export/playback evidence when applicable
```

A single polished slide does not prove narrative continuity.

## Brand-identity packet

For identity changes, load `brand-identity-review/references/evidence-and-hard-gates.md`.

```text
1. primary mark and affected variants
2. construction/geometry comparison
3. small-size and declared minimum-size samples
4. monochrome and inverse samples
5. clear-space and lockup contexts when affected
6. typography/color integration
7. application contexts and production master evidence
8. similarity-risk screen when the mark concept changed
```

A large color mockup cannot prove small-size survival, variant consistency, monochrome readiness, or production masters.

## Specialized-domain packet

Use evidence declared by the loaded domain reviewer. Universal visual screenshots are supplementary, not complete specialist proof.

## When implementation checks are blocked

Report the blocker once with the exact command and reason:

```text
npm run lint: DEFERRED/BLOCKED
Reason: missing shared package @repo/config-eslint
Impact: source-level lint coverage unavailable for this iteration
Next boundary: retry before commit/PR after dependency restoration
```

Do not repeatedly run the same known-blocked command as a substitute for fresh design evidence.

## Focused re-review boundary

```text
target gate(s)
adjacent regression gates
preserved gates and locks
contextual hard gates affected by the change
new evidence gaps introduced by the change
```

Do not display or rerun the complete gate inventory for a small local change unless the change affects foundational or cross-cutting layers.

## Reporting format

```yaml
focused_verification:
  iteration: <N>
  design_domain: <domain>
  artifact_state: <state>
  changed_layers: []
  changed_regions: []
  viewing_contexts_checked: []
  target_evidence: []
  adjacent_regressions:
    passed: []
    failed: []
    not_verified: []
  preservation_locks:
    passed: []
    failed: []
    not_verified: []
  implementation_or_export_checks:
    passed: []
    failed: []
    deferred: []
  evidence_gaps: []
  ready_for_focused_review: true | false
```

`ready_for_focused_review` means the evidence packet is honest enough to review. It does not mean the artifact passed.