# Findings Taxonomy

Use this reference during the CATEGORIZE phase to classify audit findings consistently.

## Finding Structure

Every finding must include:

```yaml
finding:
  id: <unique identifier>
  severity: CRITICAL | HIGH | MEDIUM | LOW | INFO
  category: <from categories below>
  title: <concise finding title>
  description: <what was found>
  evidence: [<observable proof>]
  current_state: <what exists now>
  recommended_action: <what to do>
  fix_guidance: <how to do it>
  state: OBSERVED | RECOMMENDED | REJECTED | NOT_VERIFIED
  impact: <who cares: visitors | maintainability | credibility | goal-achievement>
```

## Categories

### link-validation

**Purpose:** Verify that external and internal links are working.

**Examples:**
- Website URL returns 404
- Social link is dead
- README heading anchor is broken
- CTA destination unreachable

**Fix Guidance:**
- Update URL to correct destination
- Remove broken link
- Verify HTTP 200 response
- Test from different network if timeout

---

### metadata

**Purpose:** Check identity metadata for accuracy, consistency, and currency.

**Examples:**
- Bio is outdated (mentions past job)
- Bio contradicts README positioning
- Location is stale (user moved)
- Avatar not loading
- Bio exceeds 160 characters

**Fix Guidance:**
- Update bio to current positioning
- Align with README narrative
- Change GitHub profile settings
- Upload new avatar
- Shorten bio to fit GitHub limit

---

### proof-quality

**Purpose:** Evaluate whether selected work credibly supports stated positioning.

**Examples:**
- Pin repo has no description (proof role unclear)
- Pinned repo is 5+ years old with no activity
- Private repo claimed as public proof
- Repository README empty or misleading
- Pin description doesn't explain proof role

**Fix Guidance:**
- Add 1-2 sentence pin description explaining proof role
- Archive inactive repo or update activity
- Ensure repository is public
- Write meaningful repository README
- Link to active proof instead

---

### consistency

**Purpose:** Verify that all surfaces tell one compatible story.

**Examples:**
- README positioning ≠ pinned repo proof
- "Current focus" is 18 months old
- Claimed expertise not visible in repositories
- CTA goal mismatched with profile narrative
- Bio contradicts README

**Fix Guidance:**
- Refresh proof to match positioning
- Date "current focus" or update it
- Add repositories that demonstrate claimed expertise
- Align CTA with goal (e.g., hiring vs. contribution)
- Update bio to match README narrative

---

### rendering

**Purpose:** Check visual appearance and accessibility.

**Examples:**
- README not readable on mobile (text too small, horizontal scroll)
- Image not loading in dark theme
- Essential text baked into image
- Code block syntax highlighting broken
- Low contrast text

**Fix Guidance:**
- Test README on narrow width (iPhone size)
- Check image theme compatibility (add `#gh-dark-mode-only` or `#gh-light-mode-only`)
- Move text out of images
- Use GFM code fencing for syntax highlighting
- Increase contrast or use semantic colors

---

### enhancement

**Purpose:** Evaluate optional badges, widgets, stats, and animations.

**Examples:**
- Stats badge broken (external service down)
- Badge claims expertise without supporting evidence
- Animation distracts from content
- Visitor counter used as trust metric
- External widget is critical content (should be text)

**Fix Guidance:**
- Verify external service reliability
- Add supporting evidence or remove badge
- Remove animation or make it subtle
- Remove visitor counter or label what it actually measures
- Move critical content out of external widgets

Decision: Is this enhancement worth the maintenance cost?

---

## Severity Mapping

| Category | Common Severity |
|---|---|
| link-validation | CRITICAL or HIGH (blocks access) |
| metadata | HIGH (impacts first impression) |
| proof-quality | MEDIUM or HIGH (affects credibility) |
| consistency | HIGH or MEDIUM (affects comprehension) |
| rendering | MEDIUM (affects accessibility) |
| enhancement | LOW or INFO (optional) |

---

## Impact Assessment

When categorizing findings, identify who is impacted:

### visitors
Finding affects how visitors understand the profile:
- Broken links prevent access
- Unclear proof roles confuse visitors
- Inconsistent messaging raises doubt

### maintainability
Finding affects how easy the profile is to keep current:
- External dependencies that break
- Stale README that needs constant updating
- Manual screenshots instead of dynamic content

### credibility
Finding affects trust:
- Claimed expertise unsupported by proof
- Private repo presented as public work
- Outdated "current focus" suggests abandonment

### goal-achievement
Finding affects whether profile achieves its purpose:
- CTA broken = hiring signal lost
- Weak proof = not hire-ready
- Generic messaging = not memorable

---

## State Definitions

### OBSERVED
- Directly visible or tool-verified (HTTP 200 confirmed, rendered, etc.)
- This is the current state
- Example: "Website link is 404 (verified 2024-07-25)"

### RECOMMENDED
- Proposed improvement based on audit rules
- Not an error; a suggestion
- Example: "Consider refreshing the pinned repos list (current pins >2 years)"

### REJECTED
- Evaluated and determined not applicable
- Example: "Visitor counter is optional; user declined to remove"

### NOT_VERIFIED
- Evidence unavailable or inaccessible
- Example: "Private repo state NOT_VERIFIED (not public)"

### NOT_APPLICABLE
- Not relevant to scope or goal
- Example: "Sponsorship link NOT_APPLICABLE (goal is not fundraising)"

---

## Recommendation Priority

Order recommendations by:

1. **Severity** (CRITICAL > HIGH > MEDIUM > LOW > INFO)
2. **Effort** (minimal effort first within severity level)
3. **Impact** (highest impact first within effort)

### Priority Matrix

| Severity | Effort | Priority |
|---|---|---|
| CRITICAL | minimal | 1 (do immediately) |
| CRITICAL | moderate | 2 (do soon) |
| CRITICAL | significant | 3 (plan now) |
| HIGH | minimal | 4 (do this week) |
| HIGH | moderate | 5 (do this month) |
| MEDIUM | minimal | 6 (quick wins) |
| MEDIUM | moderate | 7 (nice to have) |
| LOW or INFO | any | 8 (polish) |

---

## Common Finding Examples

### "Bio outdated"

```yaml
severity: HIGH
category: metadata
title: "Bio mentions past position (outdated)"
description: "GitHub bio reads 'VP of Product at OldCo (acquired 2019)' but profile README
  positions you as an independent consultant and AI engineer."
evidence: ["GitHub profile bio", "README.md positioning"]
current_state: "Bio: VP of Product at OldCo (acquired 2019)"
recommended_action: "Update bio to reflect current positioning"
fix_guidance: "Edit GitHub profile settings. Bio example: 'AI-native engineering · Systems thinking · Architect'"
impact: ["credibility", "first-impression"]
```

### "Pin description empty"

```yaml
severity: MEDIUM
category: proof-quality
title: "Pinned repo #3 has no description"
description: "Repository 'awesome-php' is pinned but has empty description.
  Visitor can't tell why this repo is pinned or what proof role it plays."
evidence: ["GitHub profile pins", "Repository settings"]
current_state: "Pin description: (empty)"
recommended_action: "Add 1-2 sentence description explaining proof role"
fix_guidance: "Go to repo settings > Description. Example: 'Community-driven PHP ecosystem resources.
  Demonstrates knowledge of frameworks, tooling, and best practices.'"
impact: ["visitors", "credibility"]
```

### "Website link broken"

```yaml
severity: CRITICAL
category: link-validation
title: "GitHub profile website link returns 404"
description: "Website URL in GitHub profile settings (https://example-old.com) is no longer
  accessible. This breaks the primary destination for profile visitors."
evidence: ["HTTP 404 response", "GitHub profile website field"]
current_state: "Website: https://example-old.com (404 Not Found)"
recommended_action: "Update website URL to current destination or remove"
fix_guidance: "Edit GitHub profile settings > Website. Enter new URL (e.g., https://pkahfi.com)
  or leave blank if no personal site. Verify HTTP 200 before saving."
impact: ["visitors", "goal-achievement"]
```
