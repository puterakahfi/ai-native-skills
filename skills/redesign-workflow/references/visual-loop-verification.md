# Visual Loop Verification Packets

Use this reference when a creative redesign loop is still in progress and a harness/reminder asks for fresh verification while full lint/build is either intentionally deferred or blocked by repository setup.

Also load `quality-levels.md`. Every verification packet must record the current quality level honestly.

## Principle

Creative UI/UX loops are not deploy gates. Keep feedback fast until the user approves the direction or asks to commit/deploy.

Fast feedback does not lower the first-pass design standard:

```text
production must already be Q1 FOUNDATION-SAFE
verification exists to prove and correct the rendered result
not to discover that typography, layout, spacing, hierarchy, grouping,
balance, flow, accessibility, or responsiveness were never considered
```

Run full lint/build/typecheck when:

```text
✓ user says the design is approved / ready
✓ preparing a commit or PR
✓ the change is non-visual and correctness depends on build/test output
✓ user explicitly asks for full verification
```

During iteration, provide a fresh lightweight packet instead.

## Lightweight packet

For changed visual routes/components, collect:

```text
1. `git diff --check -- <changed files>`
2. route status with curl/browser navigation (`/route 200`)
3. browser DOM probe:
   - image complete + rendered dimensions when image assets changed
   - overflow false
   - touch target failures 0
   - theme label/class when theme affected
4. browser visual check for the affected route and mode
5. dark/light toggle check when tokens or image blending changed
6. changed-region + adjacent-region hierarchy/alignment/spacing check
7. current quality level: Q1 | Q2 | Q3 | Q4
```

A lightweight packet may advance Q1 to Q2 when it covers the required changed routes, viewports, themes, and states. It cannot advance to Q3 without an explicit optical correction and regression pass.

## Q3 pixel-polish packet

Before claiming `pixel-polished`, collect:

```text
FOUNDATION
□ hierarchy remains unambiguous at every required viewport
□ parent → child-group spacing is stronger than sibling spacing where nested
□ grouping survives stacking and responsive collapse
□ structural and optical alignment both pass
□ visual weight and reading flow remain intentional
□ body, labels, metadata, and controls are legible at actual size

RENDERING
□ required routes/artifacts inspected
□ representative mobile, tablet, and desktop widths inspected
□ required themes inspected
□ fonts and assets loaded
□ no overflow, clipping, overlap, or stranded content
□ line breaks and content wrapping inspected

INTERACTION / RUNTIME
□ changed interactions and states exercised
□ keyboard/touch behavior checked when applicable
□ console/runtime or export errors checked

FINAL CORRECTION
□ glyph, icon, baseline, and control relationships optically corrected
□ changed regions re-inspected after the final patch
□ adjacent regions checked for rhythm and hierarchy regressions
□ foundation, system, genre/brand, domain, and accessibility gates pass
```

Q3 requires fresh evidence after the final visual patch. Evidence from an earlier commit or iteration does not prove the current artifact.

## Q4 pixel-match packet

Only when a locked visual reference or measurable design specification exists:

```text
□ reference viewport, fonts, assets, and content locked
□ comparison method declared: overlay, visual diff, measurements, or equivalent
□ tolerance declared
□ size, position, spacing, typography, color, radius, and states compared
□ intentional deviations documented and approved
```

Without a locked reference, Q4 is `NOT_APPLICABLE`. Do not invent pixel-perfect evidence from a general design direction.

## When lint is blocked

If full lint was already attempted and failed because a shared config/dependency is missing, report the concrete blocker once:

```text
npm run lint blocked by missing shared config: Cannot find package '@repo/config-eslint' imported from eslint.config.mjs
```

Do **not** keep rerunning the same failing lint command every iteration. Resume full lint only at commit/deploy boundary or after the setup issue is fixed.

## Blank page / missing hero recovery

Before diagnosing CSS or React layout, prove the browser is actually on the app page.

```text
1. Check `location.href` — if it is `about:blank`, re-navigate to the route.
2. Check `document.body.children.length` — 0 means no app DOM mounted.
3. Check `document.styleSheets.length` — 0 means CSS/resources not loaded.
4. Check dev-server process/logs — parent watcher may exit while child server still listens.
5. Check route with curl — route 200 does not guarantee browser is still on that route.
6. For Next dev, prefer `http://localhost:<port>` over `127.0.0.1` if logs show blocked cross-origin HMR/font/dev resources.
7. Re-navigate after server restart before calling the UI blank.
```

Diagnosis names:

```text
about:blank false alarm — browser is not on the app route
unmounted DOM — route loaded no body children
stylesheet drop — body exists but stylesheets = 0
resource-origin block — Next dev blocks 127.0.0.1 resources; use localhost or allowedDevOrigins
runtime blank — route + DOM + styles exist but visible content absent; inspect console/errors next
```

## Example DOM probe for image delight assets

```js
(() => ({
  route: location.pathname,
  images: [...document.images].map(img => ({
    alt: img.alt,
    complete: img.complete,
    natural: [img.naturalWidth, img.naturalHeight],
    rendered: [
      Math.round(img.getBoundingClientRect().width),
      Math.round(img.getBoundingClientRect().height),
    ],
  })),
  overflow: document.documentElement.scrollWidth > innerWidth,
  touchFail: [...document.querySelectorAll('a,button')].filter(el => {
    const b = el.getBoundingClientRect();
    return b.width > 0 && b.height > 0 && (b.width < 44 || b.height < 44);
  }).length,
}))()
```

## Reporting format

```text
Fresh visual-loop verification:
- quality target: Q3 PIXEL-POLISHED
- current quality: Q2 RENDER-VERIFIED
- diff check: PASS
- routes: /en 200, /ai-designer 200
- viewports/themes: <coverage>
- browser DOM: overflow=false, touchFail=0, images complete
- optical correction: pending | complete
- adjacent regression check: pending | complete
- full lint/build: intentionally deferred for creative loop; known blocker if forced: <blocker>
- unresolved gaps: <list>
```

Never report Q3 or use `pixel-polished` while optical correction, adjacent regression verification, or required viewport/theme evidence is pending.
