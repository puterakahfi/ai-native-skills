# Interactive Surface Gates

Load this reference for web, mobile, and desktop application reviews. Apply it together with `universal-gates.md` and the selected profile.

## Applicability and evidence

```text
Rendered interactive flow available → visual, interaction, accessibility, and runtime gates can be verified
Screenshot only                    → interaction/runtime gates are NOT_VERIFIED
Source only                        → implementation gates may be reviewed; rendered behavior remains NOT_VERIFIED
No motion present                  → motion-purpose gates may be NOT_APPLICABLE; reduced-motion policy still follows platform requirements
```

## Pattern and task fit

| Gate | Review question | Pass evidence |
|---|---|---|
| G6 Pattern Fit | Is the selected page and component pattern suitable for the user task, option count, content density, label length, and available space? | The design adapts or substitutes components instead of forcing a pattern beyond its useful range. |
| I1 Task Continuity | Can the user understand what happened, what is selected, and what the next valid action is? | State and next-step cues remain visible through the reviewed flow. |
| I2 State Coverage | Are loading, empty, error, success, disabled, destructive, permission, and partial states handled where the flow can produce them? | Relevant states are rendered or proven in implementation; no state is represented by silence. |
| I3 Feedback | Do actions provide timely, proportional, and reversible feedback? | Submission, save, navigation, validation, selection, and background work communicate outcome. |
| CP4 Status and Action Honesty | Do labels describe the real system state and behavior? | `Continue` or `Resume` restores meaningful task state; visit history alone uses `Recently viewed`, `Open again`, or equivalent. |

## Responsive and adaptive behavior

| Gate | Review question | Pass evidence |
|---|---|---|
| G13 Adaptive Layout | Does the layout preserve task priority and usability across required sizes and orientations? | No accidental overflow, clipping, overlap, inaccessible content, or unsupported one-column collapse. |
| G14 Target Reachability | Are controls reachable, non-overlapping, and large enough for the input method and platform? | Touch targets normally meet platform guidance; pointer targets remain discoverable and separable. |
| G15 Adaptive Type | Does typography scale or recompose without creating overflow, giant headings, or unreadable supporting text? | Tested with realistic viewport, content, localization, and text scaling where applicable. |
| I4 Overflow Strategy | Is horizontal or vertical overflow intentional, discoverable, and operable? | Previous/next affordances, scroll hints, clipping, pagination, wrapping, or component substitution match the task. |
| I5 Resize and Orientation | Does state and control access survive resize, rotation, split view, or window constraints where applicable? | No lost selection, detached controls, hidden primary action, or layout reset without reason. |

Do not require every mobile layout to become one column. Tables, timelines, canvases, editors, and comparison surfaces may need scrolling, prioritization, alternate views, or responsive component substitution.

## Accessibility and input methods

| Gate | Review question | Pass evidence |
|---|---|---|
| G16 Semantic Structure | Does the platform expose meaningful landmarks, headings, roles, names, and relationships? | Web uses appropriate HTML/ARIA; native platforms expose equivalent accessibility semantics. |
| G17 Interactive Accessibility | Can controls be identified, focused, operated, and understood with supported assistive and input methods? | Visible focus, accessible names, state announcements, error association, and non-color cues are present where applicable. |
| I6 Input Parity | Are critical actions available across the expected keyboard, pointer, touch, switch, or gesture methods? | No essential hover-only, gesture-only, drag-only, or color-only path without an alternative. |
| I7 Focus and Modal Safety | Does focus order follow the task and remain contained/restored correctly for overlays? | No focus loss, trap, unexpected jump, or background interaction through modal surfaces. |

Platform-specific thresholds belong to the selected profile and current authoritative platform guidance. A common web touch starting point is approximately 44×44 CSS pixels, but spacing, reachability, overlap, and platform convention matter more than blindly forcing every icon box to one number.

## Theme system

Score these only when multiple themes or appearance modes exist.

| Gate | Review question | Pass evidence |
|---|---|---|
| T1 Token Architecture | Are theme differences expressed through semantic roles rather than scattered mode-specific values? | Repeated colors and effects switch coherently without local overrides drifting. |
| T2 Toggle Accessibility | Is the appearance control reachable, named by the next action or current state clearly, and operable by expected inputs? | Target, label, state, focus, and feedback verified. |
| T3 Multi-Theme QA | Have all supported themes been inspected with realistic content and states? | Visual and DOM/native evidence exists for each supported mode. |
| T4 Contrast and Inversion | Do contrast, imagery, borders, shadows, charts, and status colors survive every theme? | No invisible controls, muddy hierarchy, or incorrect asset inversion. |

## Motion

| Gate | Review question | Pass evidence |
|---|---|---|
| G18 Motion Purpose | Does motion communicate state, continuity, hierarchy, causality, or spatial relationship? | Decorative motion does not distract from the task or delay interaction. |
| G19 Timing and Easing | Are durations, easing, and sequencing appropriate to distance, importance, and frequency? | Frequent micro-interactions feel immediate; larger transitions remain understandable. |
| G20 Motion Performance | Does animation avoid unnecessary layout work, dropped frames, input blocking, or battery-heavy behavior? | Runtime evidence or implementation inspection supports the claim. |
| G21 Reduced Motion | Can users who request reduced motion complete the same task without unnecessary movement or lost meaning? | Reduced-motion behavior is implemented and verified for every applicable animation. |
| G22 Motion Hierarchy | Is motion intensity proportional across the surface rather than every region competing cinematically? | Primary transitions receive emphasis; routine states stay restrained. |

`G21` is a hard gate for release review when motion exists or the platform/framework can introduce motion. It is `NOT_VERIFIED`, not zero, when only a screenshot is available.

## Runtime integrity

| Gate | Review question | Pass evidence |
|---|---|---|
| RI1 Runtime Integrity | Does the reviewed flow complete without unhandled page/app errors, broken executable assets, missing required UI, or fatal interaction regressions? | Evidence is captured from before navigation or launch until the reviewed flow completes. |

Fail RI1 when evidence shows any of the following:

- an unhandled page or application error;
- a script, module, worker, stylesheet, or equivalent executable resource receives incompatible content;
- navigation or action leaves required UI missing or unusable;
- an interaction failure prevents task completion.

Do not fail RI1 only because a framework prefetch request was cancelled or superseded. Treat cancellation as a failure only when it creates a page error, missing UI, broken interaction, or another user-visible regression.

Example browser verification:

```js
const runtimeErrors = [];

page.on('pageerror', error => runtimeErrors.push(String(error)));
page.on('response', response => {
  const type = response.request().resourceType();
  const contentType = response.headers()['content-type'] || '';
  if (['script', 'stylesheet'].includes(type) && contentType.includes('text/html')) {
    runtimeErrors.push(`HTML served as ${type}: ${response.url()}`);
  }
});

// Navigate and execute the reviewed flow.
expect(runtimeErrors).toEqual([]);
```

RI1 is a hard gate for `release` depth on rendered interactive surfaces. For a focused visual iteration, report runtime coverage honestly and do not claim release readiness without it.

## DOM probe example

Use only for rendered web surfaces and adapt selectors to the actual product:

```js
JSON.stringify({
  sheets: document.styleSheets.length,
  bg: getComputedStyle(document.body).backgroundColor,
  overflow: document.documentElement.scrollWidth > innerWidth,
  smallTargets: [...document.querySelectorAll('a,button,[role="button"]')]
    .filter(el => {
      const b = el.getBoundingClientRect();
      return b.width > 0 && b.height > 0 && (b.width < 44 || b.height < 44);
    })
    .map(el => ({ text: el.textContent?.trim(), width: el.getBoundingClientRect().width, height: el.getBoundingClientRect().height }))
});
```

A probe is evidence, not the verdict. Inspect whether small targets overlap, are touch-critical, have adequate surrounding space, or are pointer-only controls.

## Marketing interaction and conversion

Apply these only when the selected profile has a persuasion or conversion goal.

| Gate | Review question | Pass evidence |
|---|---|---|
| CRO1 Attention Flow | Does the reading path reach value, proof, and action in a coherent order? | Eye-flow and content order match the intended decision journey. |
| CRO2 Trust Integrity | Are credibility signals relevant, truthful, and placed near the claims they support? | No fake social proof or unsupported authority cues. |
| CRO3 Value Recognition | Can the intended audience understand the offer and relevance within the expected attention window? | Tested against the actual first viewport and content. |
| CRO4 Persuasion Sequence | Does the sequence reduce uncertainty and support action without manipulative interruption? | Awareness, evaluation, proof, objection handling, and action are proportionate to the offer. |

Do not apply CRO gates to internal tools, utilities, or desktop workflows unless conversion is an explicit surface goal.

## Interactive quick review

After the universal quick review, check the applicable subset:

```text
G6  pattern fit
G13 adaptive layout
G14 target reachability
G16 semantic structure
G17 interactive accessibility
I2  state coverage
I4  overflow strategy
G21 reduced motion
RI1 runtime integrity
CP4 action honesty
```

Run hard gates before calculating a release verdict.