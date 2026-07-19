# Content Resilience Regression Fixtures

> Cross-surface PASS/FAIL reasoning fixtures for content quantity, length, presence, localization, media, and density variation. These fixtures test relationship quality, not a preferred genre or component library.

Use these fixtures during skill evaluation and dogfooding. They are not implementation recipes or universal numeric thresholds.

---

## Fixture Protocol

For each applicable design, inspect at least:

```text
EMPTY or missing optional content
MINIMUM meaningful content
NORMAL realistic production content
MAXIMUM declared content
VARIANT localization/text scaling/media/value shape
```

Then ask:

```text
- does hierarchy remain recognizable?
- does grouping remain intact?
- does density remain scannable?
- are critical values and actions still visible?
- is the adaptation strategy discoverable and consistent?
- does the content remain usable when variation combines with constrained space?
```

---

## 1. Searchable Skill or Product Directory

### PASS candidate

```text
- zero results shows a specific empty outcome and retains a clear way to revise filters
- one result does not remain stranded in a fake multi-column composition
- long names wrap or clamp consistently without hiding the distinguishing term
- install commands scroll or wrap intentionally and remain copyable
- many rows preserve header/context and do not turn metadata into visual dust
- mobile substitutes or recomposes filters before overlap occurs
- missing optional description or category collapses cleanly
```

### FAIL candidate

```text
- zero results leaves only blank whitespace below persistent controls
- one result keeps empty grid slots that imply missing content
- long names collide with badges/actions
- all rows use fixed height and clip translated descriptions
- horizontal overflow exists but has no hint or operable path
- copy action detaches from the command it belongs to
```

---

## 2. Dense Dashboard or Data Table

### PASS candidate

```text
- large numbers, negative values, dates, percentages, and units remain distinguishable
- optional columns can disappear without breaking row identity or action ownership
- constrained width uses prioritized columns, intentional scrolling, or alternate detail view
- dense state preserves comparison alignment and status visibility
- one-row and empty states retain table/task context without looking broken
- long localized headers are tested with realistic column behavior
```

### FAIL candidate

```text
- sample data uses equal-length values that conceal alignment problems
- large values overlap icons or adjacent columns
- truncation removes the distinguishing suffix from IDs or filenames
- mobile forces every column into stacked labels that destroy comparison
- sticky headers plus controls consume most of the usable viewport
- missing values are indistinguishable from zero or unavailable data
```

---

## 3. Card Grid, Feed, or Collection

### PASS candidate

```text
- one item adopts a deliberate width/composition instead of appearing unfinished
- many items retain sibling rhythm and parent context
- title, media, metadata, and actions have consistent fallback policies
- varied image ratios use an intentional frame/crop strategy
- missing media does not erase item identity
- maximum density triggers pagination, loading boundary, or layout substitution before scanning collapses
```

### FAIL candidate

```text
- every card assumes identical title length and image ratio
- cards grow independently until row alignment and action positions become chaotic
- one missing image collapses the card and detaches its metadata
- more items only create an infinitely long wall with no orientation or prioritization
- all text is clamped to one line even when names become indistinguishable
```

---

## 4. Form, Settings, or Configuration Surface

### PASS candidate

```text
- long field labels and helper text remain associated with their control
- optional fields appear/disappear without reordering unrelated sections unpredictably
- validation messages do not push primary actions out of reach
- prefilled long values have an intentional display/edit strategy
- translated labels and 200% text scaling preserve reading and keyboard order
- repeated field groups handle one and many entries coherently
```

### FAIL candidate

```text
- labels are constrained to one line and overlap inputs
- error text is clipped or appears closer to the next field
- optional sections leave unexplained blank gaps
- long values hide the editable portion or destructive action
- repeated entries use local spacing hacks and drift from the base form structure
```

Detailed validation timing, announcement, and submission feedback remain owned by interactive gates.

---

## 5. Marketing or Editorial Landing Page

### PASS candidate

```text
- headline supports realistic long and short product language without arbitrary shrinkage
- proof sections work with one, several, or no approved proof items
- optional imagery can be removed without making copy appear detached
- CTA remains subordinate or dominant according to narrative role after copy length changes
- localized paragraphs preserve measure and section hierarchy
- sparse sections remain intentional; dense sections chunk evidence rather than flattening it
```

### FAIL candidate

```text
- hero only works with a four-word English headline
- longer copy pushes the primary action below an unexplained void or into overlap
- absent testimonial/logo content leaves fake proof containers
- every section uses the same fixed height despite content variation
- body copy is reduced to tiny low-contrast text to preserve composition
```

---

## 6. Static Commercial Creative or Reusable Poster Template

### PASS candidate

```text
- locked one-off creative is judged against its final approved content
- reusable template declares title, price, contact, disclaimer, and image bounds
- long price/contact/legal variants remain readable at delivery size
- missing optional badge or secondary copy does not leave a decorative hole
- supported aspect-ratio variants preserve mandatory content and safe areas
- unsupported content length is surfaced as an authoring constraint, not silently clipped
```

### FAIL candidate

```text
- template looks correct only with placeholder-short product names
- long contact or disclaimer text disappears after export
- missing image exposes an unfinished mask or fake shadow
- title is automatically shrunk below readable size instead of recomposed
- crop variants remove price, CTA, logo, or legal content
```

A fixed one-off creative does not need artificial empty/loading states. A reusable or generated template does need declared bounds.

---

## 7. Presentation or Report

### PASS candidate

```text
- slide/table/chart accepts realistic data labels and number formats
- one data point does not preserve a misleading multi-series legend structure
- many data points trigger aggregation, prioritization, alternate chart, or appendix detail
- long titles recompose without becoming document-page density
- missing data is explicitly represented and not confused with zero
- localized deck variants preserve narrative hierarchy and room-distance legibility
```

### FAIL candidate

```text
- chart labels overlap because only short sample categories were tested
- additional data series receive identical emphasis and destroy the takeaway
- missing values produce broken lines or unexplained blank regions
- long titles shrink every slide role and flatten the deck hierarchy
- dense tables are pasted without interpretation or readable delivery strategy
```

---

## 8. Mobile and Desktop Application Pattern Substitution

### PASS candidate

```text
- desktop tabs become scrollable navigation, segmented controls, menu, or another fitting pattern
  when count and label length exceed the available space
- desktop table keeps comparison through horizontal scroll or alternate view instead of forced card stacking
- mobile action density is prioritized rather than wrapping every control into multiple accidental rows
- state and selection survive the substituted pattern
```

### FAIL candidate

```text
- desktop component is preserved at all costs until labels overlap
- only a right overflow chevron is shown even when content exists to the left
- horizontal scroll is possible but clipped content has no discoverable affordance
- pattern substitution resets selection or changes task meaning
```

Detailed reachability, focus, gesture, and runtime behavior remain owned by interactive surface gates.

---

## 9. Localization and Text Scaling

### PASS candidate

```text
- supported locales use realistic translated strings, not machine-equal placeholders
- numbers, currency, dates, plurals, and directionality remain meaningful
- text scaling preserves hierarchy without hiding actions or detaching labels
- wrapping order follows semantic reading order
- icon-only fallbacks retain accessible names where interactive
```

### FAIL candidate

```text
- translated strings are tested only by adding random characters to English
- RTL or mixed-script content reverses visual relationships incorrectly
- 200% text scaling causes fixed-height clipping
- long localized buttons collide or become indistinguishable
- dates/prices truncate the unit or currency required for interpretation
```

---

## 10. Generated or User-Authored Content

### PASS candidate

```text
- bounds and unsupported shapes are explicit
- generated titles/descriptions use the same role and overflow rules as authored content
- broken or absent media has a stable fallback
- unusual but valid input does not destroy surrounding hierarchy
- the system exposes full critical content rather than silently discarding it
```

### FAIL candidate

```text
- generated content is assumed to have predictable length
- one extreme title expands the component over unrelated controls
- malformed media leaves invisible but space-consuming elements
- user content is hidden by fixed-height clipping with no recovery
- local exceptions produce different behavior for every item
```

Security, sanitization, validation, moderation, and runtime failure handling are outside this fixture’s foundation ownership.

---

## Anti-Bias Checks

Content resilience must not silently enforce one aesthetic:

```text
PASS: dense enterprise table with deliberate overflow and comparison structure
PASS: minimal editorial page with sparse content and no artificial filler
PASS: expressive poster template with declared text/image bounds
PASS: mobile feed with variable-height items and stable action ownership

FAIL: minimal layout that treats blank output as a valid empty state
FAIL: dense layout that hides essential values behind indiscriminate truncation
FAIL: fixed-height card system that works only with placeholder copy
FAIL: responsive design tested with short content at every viewport
```

---

## Expected Review Outcome

A content-resilience review should produce:

```text
supported bounds: declared | missing
stress states exercised: [...]
representative combinations exercised: [...]
strategies used: wrap | clamp | truncate | scroll | paginate | summarize |
                 prioritize | disclose | substitute | fixed-content only
foundation findings: canonical gate IDs only
evidence gaps: [...]
surface/domain handoffs: [...]
```

Do not award PASS because a single ideal mockup fits. PASS requires enough representative evidence for the artifact’s declared variability.
