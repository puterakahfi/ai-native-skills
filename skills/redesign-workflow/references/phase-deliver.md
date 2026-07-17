# Phase 7 — DELIVER + PITFALLS + ANTI-LOOP

## FILE MANAGEMENT — HARD RULE

```
ONE file per project. PATCH/WRITE in-place. NEVER create versioned files.
  ❌ pkahfi-v2.html, pkahfi-v3.html, output-final.html → FORBIDDEN
  ✅ pkahfi.html → patched every iteration, versioned via git

Versioning = git commits, not filenames.
After each iteration: git commit -m "redesign: iter N — <what changed>"

If write_file full rewrite needed (2 failed patches):
  → overwrite SAME file, git commit, continue
  → never create new filename
```

---

## Phase 7: DELIVER

Only when: overall avg >= 8.0 AND G21 = 10 AND touchFail = 0.

```
1. Ensure file is at canonical output_path (single file, no version suffix)
2. git commit -m "redesign: final — <target> iter N"
3. MEDIA: output_path → deliver as file
3. Gate report summary
4. Key changes table: before → after
5. If max_iterations reached: honest gap report

Format:
  REDESIGN COMPLETE — <target>
  ──────────────────────────────
  Gates: all passing (avg X.X / 10)
  Iterations: N
  Skills patched: [list]

  Key changes:
    Before: [issue]   After: [fix applied]
    ...

  MEDIA: /path/to/output.html
```

---

## PITFALLS

### CSS patch corruption (most common failure)
3+ micro-patches to same CSS block → rules nest inside wrong selectors.  
Symptom: page goes white, `document.styleSheets.length === 0`.  
**Rule: after 2 failed patches on same region → `write_file` full rewrite. Never a 3rd patch.**

### min-height:100vh void
`min-height:100vh` + sparse content = 60% dead space on mobile.  
**Rule: NO min-height:100vh on hero. Use `padding-top:clamp(120px,16vh,180px)` + `padding-bottom:clamp(80px,14vh,140px)`.**

### Sticky vs fixed nav
`position:fixed` requires JS scroll detection for background. `position:sticky` = CSS-only, no jank.  
**Rule: always `position:sticky; top:0` for nav unless product explicitly requires fixed.**

### Color-only status signals
Status dot without `aria-label` = WCAG 1.4.1 failure (color alone).  
**Rule: `<div class="status-dot" role="img" aria-label="Status: Live"></div>`**

### Improvised behavior
Agent writes component behavior from memory = wrong a11y, wrong interaction.  
**Rule: check `ux-patterns-for-developers` catalog before writing any component behavior.**

---

## Anti-Loop Protection

```
Before each produce/fix:
  iteration_count++
  if iteration_count > max_iterations:
    deliver current best
    report remaining failures
    STOP

If same gate fails 2 iterations in a row:
  → try different approach for that specific gate
  → do not keep applying same fix that isn't working
```
