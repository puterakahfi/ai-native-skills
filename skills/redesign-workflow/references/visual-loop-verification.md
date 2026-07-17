# Visual Loop Verification Packets

Use this reference when a creative redesign loop is still in progress and a harness/reminder asks for "fresh verification" while full lint/build is either intentionally deferred or blocked by repository setup.

## Principle

Creative UI/UX loops are not deploy gates. Keep feedback fast until the user approves the direction or asks to commit/deploy.

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
```

## When lint is blocked

If full lint was already attempted and failed because a shared config/dependency is missing, report the concrete blocker once:

```text
npm run lint blocked by missing shared config: Cannot find package '@repo/config-eslint' imported from eslint.config.mjs
```

Do **not** keep rerunning the same failing lint command every iteration. Resume full lint only at commit/deploy boundary or after the setup issue is fixed.

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
- diff check: PASS
- routes: /en 200, /ai-designer 200
- browser DOM: overflow=false, touchFail=0, images complete
- full lint/build: intentionally deferred for creative loop; known blocker if forced: <blocker>
```
