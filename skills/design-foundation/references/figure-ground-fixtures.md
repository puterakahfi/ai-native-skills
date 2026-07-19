# Figure–Ground Cross-Genre Fixtures

> Reasoning fixtures for validating that figure-ground and layering rules measure relationship quality rather than a preferred visual style.

Use each case as a PASS/FAIL discrimination exercise. Do not report the fixture name as a gate ID; findings still use canonical review gates such as `G4`, `C2`, `R8`, and applicable surface gates.

---

## Dense Dashboard

### PASS candidate

```text
- strong data regions and table containment
- sticky header remains compact and never covers row actions
- popovers remain anchored to their trigger
- selected state is distinguishable without excessive elevation
- dense visual language is accepted because scanning and comparison stay clear
```

### FAIL candidate

```text
- every nested region has its own shadow and border
- sticky toolbar plus table header consume most small-screen height
- menu opens beneath another panel
- status color blends into the containing surface
```

Expected discrimination:

```text
PASS is not rejected for density.
FAIL is rejected for containment noise, occlusion, and unclear layer ownership.
```

---

## Zen / Minimal Landing Page

### PASS candidate

```text
- near-flat canvas with little or no shadow
- grouping comes from spacing, alignment, and type hierarchy
- one dark install surface has a clear functional purpose
- no decorative layer is required to fill whitespace
```

### FAIL candidate

```text
- low-contrast sections merge into the canvas
- sticky navigation hides anchors after in-page navigation
- pale text over atmospheric imagery survives only in one crop
- a dark surface becomes more dominant than the page’s actual narrative anchor
```

Expected discrimination:

```text
PASS is not required to add cards, borders, or elevation.
FAIL is rejected even though the visual style appears restrained and clean.
```

---

## Professional SaaS Page

### PASS candidate

```text
- pricing or plan surfaces clarify comparison without making every section a card
- primary action depth remains proportionate to its importance
- navigation, cookie notice, chat launcher, and sticky CTA do not cover required content
- light and dark themes preserve surface boundaries
```

### FAIL candidate

```text
- all sections use identical elevated white cards
- chat launcher covers the mobile primary action
- translucent navigation makes body copy unreadable while scrolling
- decorative gradient becomes the strongest focal layer
```

---

## Playful / Expressive Poster

### PASS candidate

```text
- overlapping forms create energy while preserving the primary message
- product/person remains separated from the background
- mandatory price/contact/legal details stay unobstructed
- irregular depth supports the concept rather than simulating generic 3D decoration
```

### FAIL candidate

```text
- decorative shapes cross required text unpredictably
- glow and texture erase silhouette or edge clarity
- overlapping objects create an accidental second focal point
- safe-area crop removes the figure-ground cue
```

Expected discrimination:

```text
PASS is not rejected for overlap, color, or expressive depth.
FAIL is rejected for message obstruction and unstable separation.
```

---

## Mobile Application

### PASS candidate

```text
- bottom sheet clearly belongs to the current task
- background state remains understandable but appropriately de-emphasized
- primary action remains reachable above system and keyboard areas
- dismissal restores focus/context
```

### FAIL candidate

```text
- sheet, keyboard, and sticky action overlap
- scrim does not distinguish blocking from non-blocking state
- floating action button covers list content
- orientation change detaches popover or resets task context
```

---

## Desktop Application

### PASS candidate

```text
- inspector, canvas, toolbar, and modal layers have stable ownership
- floating panels remain attached to the selected object or workspace
- resize and split view preserve control access and content visibility
```

### FAIL candidate

```text
- arbitrary always-on-top panels obscure the working canvas
- multiple floating windows compete for input ownership
- tooltip or menu appears behind the host panel
```

---

## Presentation

### PASS candidate

```text
- depth or overlap reinforces one dominant idea
- annotations clearly belong to the chart or image they explain
- foreground claim remains readable at delivery distance
```

### FAIL candidate

```text
- floating labels appear detached from their data
- background imagery competes with the slide claim
- decorative layers create document-like density with no narrative role
```

---

## Static Commercial Creative

### PASS candidate

```text
- product, person, logo, offer, and contact occupy understandable depth roles
- shadows and grounding match the declared visual style
- required content survives destination crop and platform overlays
```

### FAIL candidate

```text
- product cutout appears detached from the environment
- price badge covers the product label or required feature
- generated decoration creates false text or impossible object overlap
```

Fidelity, compositing, export, crop, and generative-artifact details remain owned by static/domain gates after the universal relationship finding is recorded.

---

## Fixture Completion Rule

A valid implementation should demonstrate:

```text
□ accepts at least one flat/minimal PASS case
□ accepts at least one dense or expressive PASS case
□ rejects unintended sticky/fixed occlusion
□ rejects text/background instability
□ rejects detached floating content
□ rejects meaningless depth used as decoration
□ routes focus, crop, fidelity, runtime, and export specifics to the correct surface/domain owner
□ reports findings with canonical gate IDs rather than F-axis labels
```
