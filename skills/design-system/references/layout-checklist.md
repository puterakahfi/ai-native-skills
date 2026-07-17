# Layout Tokens & Token Declaration Checklist

> Reference for design-system SKILL.md Step 6 + final gate checklist.
> Load this file when declaring layout/container tokens or verifying a screen is ready to design.

---

## Step 6: Declare Layout Tokens

```css
:root {
  --container-sm:   640px;
  --container-md:   768px;
  --container-lg:   960px;
  --container-xl:  1200px;
  --container-2xl: 1400px;

  --radius-none:  0;
  --radius-sm:    2px;
  --radius-md:    4px;
  --radius-lg:    8px;
  --radius-xl:    12px;
  --radius-full:  9999px;
}
/*
Border radius philosophy:
  Sharp (--radius-sm): code, terminal, data tables — precision feel
  Rounded (--radius-md/lg): cards, buttons — approachable
  Full (--radius-full): badges, pills, avatars

Pick ONE primary radius for a product. Mix max 2.
*/
```

---

## Token Declaration Checklist

Before designing any screen, verify this table is complete:

```
□ Color tokens declared — each has ONE semantic role
□ Spacing scale declared — 8px base, 12 steps
□ Type scale declared — one ratio chosen, 8 sizes
□ Font weights declared — 3–4 only
□ Line heights declared — 5 levels
□ Letter spacing declared — 5 levels
□ Elevation declared — 5 shadow levels
□ Motion declared — durations + easings
□ Border radius declared — 1–2 values for the product

FAIL: any hardcoded value in design that is not in token table
FAIL: same hex used in multiple semantic roles
FAIL: any font size not from the scale
FAIL: spacing value not from 8px grid
```
