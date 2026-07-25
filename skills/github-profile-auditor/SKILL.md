---
name: github-profile-auditor
description: Audit GitHub profile for quality, consistency, and completeness—detect gaps, validate proof, and generate prioritized improvement recommendations.
license: MIT
metadata:
  ai-native-skills.version: 1.0.0
  ai-native-skills.author: puterakahfi
  ai-native-skills.type: skill
  ai-native-skills.requires: "github-profile"
  ai-native-skills.related_skills: '["github-profile", "design-review"]'
---

# GitHub Profile Auditor

```text
HARD RULES
1. Start from profile state, not desired state—observe before recommending.
2. Never invent profile data, repository state, or contribution claims.
3. Declare scope: readme-only, profile-surface, or full-profile-ecosystem.
4. Separate OBSERVED state from RECOMMENDED actions.
5. Report findings with severity, category, and actionable fix guidance.
6. Validate links, rendering, and platform constraints.
7. Check cross-surface consistency: README ↔ pins ↔ repositories ↔ CTA.
8. Repository lifecycle (active/maintained/archived) determines proof validity.
9. Stale claims ("current focus" >6 months old) are findings, not errors.
10. Private repositories are not public source proof.
11. Archive and unpin recommendations remain recommendations, never automatic.
12. Findings are findings—do not conflate missing optional enhancements with failures.
13. Verify rendered output, not source Markdown alone.
14. Unknown or unavailable evidence remains NOT_VERIFIED, never assumed.
15. Audit output feeds into redesign workflows; does not mutate the profile.
```

## Purpose and Boundary

Use this skill to validate an existing GitHub profile and detect gaps, inconsistencies, quality issues, and improvement opportunities.

It owns:

```text
profile surface observation and state reporting
quality gate validation (consistency, accessibility, functionality)
finding categorization and prioritization
gap detection (broken links, outdated metadata, weak proof)
cross-surface consistency checking
recommendation generation with actionable fix guidance
audit report composition and delivery
feedback into redesign or maintenance workflows
```

It composes github-profile-related references and design-review gates rather than redefining validation methodology.

It does not own:

```text
profile mutation or automated fixes
repository authorization or archive decisions
private data discovery
employment verification
design or strategy decisions
manual implementation of recommendations
```

## Scope Modes

```text
readme-only
  validate profile README only
  report adjacent profile-surface contradictions when observed

profile-surface
  audit identity metadata, README, pinned items, selected proof repositories,
  CTA paths, and cross-surface consistency

full-profile-ecosystem
  audit the complete public repository portfolio, repository hygiene,
  discoverability metadata, lifecycle recommendations, contribution paths,
  and optional enhancements
```

Load `references/cross-surface-validation.md` whenever scope is broader than `readme-only`.

## Inputs

```yaml
github_profile_audit_input:
  username: <required for repository-backed work>
  scope: readme-only | profile-surface | full-profile-ecosystem
  report_depth: summary | detailed | comprehensive
  focus_areas: [] <optional, e.g. ["proof-quality", "link-validation", "consistency"]>
  known_constraints: [] <optional, e.g. ["profile-redesign-in-progress"]>
```

## Procedure

```text
1. OBSERVE
   Crawl and record current profile state:
   - identity metadata (avatar, bio, links, status)
   - README content and rendering
   - pinned items and descriptions
   - selected repositories and descriptions
   - contribution context
   - external destinations and CTAs
   Mark all observations with state: OBSERVED | NOT_VERIFIED | NOT_ACCESSIBLE
   Load references/audit-checklist.md

2. VALIDATE
   Check profile against quality gates:
   - README structure and hierarchy
   - Link validity (HTTP 200, not 404/410/timeout)
   - Image rendering and theme compatibility
   - Metadata consistency (bio, links, status)
   - Repository lifecycle signals
   - Proof role definitions
   - Accessibility and narrow-width rendering
   Load references/audit-checklist.md for gate definitions

3. CROSS-CHECK
   Verify consistency across surfaces:
   - README positioning ↔ pinned repositories
   - README claims ↔ repository state and README
   - "Current focus" ↔ recent activity or explicit date
   - CTA destinations ↔ working and aligned with goal
   - Brand grammar ↔ avatar, metadata, external sites
   - Public proof ↔ accessible repositories
   Load references/cross-surface-validation.md

4. CATEGORIZE
   Classify all findings:
   - Severity: CRITICAL | HIGH | MEDIUM | LOW | INFO
   - Category: link-validation | metadata | proof-quality | consistency | rendering | enhancement
   - State: OBSERVED | RECOMMENDED | REJECTED | NOT_VERIFIED
   Load references/findings-taxonomy.md

5. PRIORITIZE
   Order findings by impact:
   - CRITICAL (blocks profile credibility or access) first
   - HIGH (impacts immediate visitor comprehension)
   - MEDIUM (gaps or opportunities)
   - LOW (polish or optional enhancements)

6. REPORT
   Compose audit report with:
   - Current state summary
   - Categorized findings by severity
   - Recommendations with fix guidance
   - Cross-surface consistency assessment
   - Readiness determination
   Load references/audit-checklist.md for acceptance gates
```

## Reference Loading

| Need | Load |
|---|---|
| Quality gates and validation rules | `references/audit-checklist.md` |
| Finding categorization and severity | `references/findings-taxonomy.md` |
| Cross-surface consistency checks | `references/cross-surface-validation.md` |

Load only the references required by scope and uncertainty.

## Observation States

Every audit claim must use one state:

```text
OBSERVED        directly visible, tool-verified, or HTTP-confirmed
RECOMMENDED     proposed from observed evidence
REJECTED        evaluated and not applicable
NOT_VERIFIED    required evidence unavailable or inaccessible
NOT_APPLICABLE  irrelevant to scope or goal
```

Never silently convert RECOMMENDED into OBSERVED, or NOT_VERIFIED into a negative finding.

## Audit Contract

```yaml
github_profile_audit_report:
  username:
  scope:
  audit_timestamp:
  profile_state:
    identity: {}
    readme: {}
    pinned_items: []
    repositories: []
    contribution_context: {}
    destinations: []
  
  findings:
    - finding_id:
      severity: CRITICAL | HIGH | MEDIUM | LOW | INFO
      category: link-validation | metadata | proof-quality | consistency | rendering | enhancement
      title:
      description:
      current_state:
      recommended_action:
      fix_guidance:
      evidence: []
      state: OBSERVED | RECOMMENDED | REJECTED | NOT_VERIFIED
  
  cross_surface_consistency:
    readme_positioning_to_pins: aligned | misaligned | NOT_VERIFIED
    claims_to_proof: aligned | misaligned | NOT_VERIFIED
    current_focus_to_activity: aligned | stale | NOT_VERIFIED
    cta_alignment: aligned | broken | NOT_VERIFIED
    brand_consistency: consistent | drift | NOT_VERIFIED
  
  summary:
    total_findings:
    critical_count:
    high_count:
    medium_count:
    low_count:
    info_count:
  
  recommendations:
    - priority: HIGH | MEDIUM | LOW
      title:
      action:
      estimated_effort: minimal | moderate | significant
      dependencies: []
  
  readiness:
    state: audit-ready | needs-fixes | hire-ready | open-source-ready | community-ready
    blockers: []
    next_step:
  
  render_evidence: []
  acceptance_checks: []
```

## Output Modes

### `summary`

Quick health check:
- Finding count by severity
- Top 3 recommendations
- Overall readiness state
- One-sentence next step

### `detailed`

Comprehensive audit:
- Full findings with evidence
- Cross-surface consistency assessment
- Categorized recommendations
- Readiness determination
- Render evidence for visual findings

### `comprehensive`

Full ecosystem audit:
- All findings with supporting evidence
- Repository hygiene review (for selected repos)
- Contribution context analysis
- Enhancement decision matrix results
- Behavioral gates validation
- Before/after comparison if profile previously audited

## Acceptance Checks

```text
□ scope is explicit
□ username verified or explicitly NOT_VERIFIED
□ all observations marked with state: OBSERVED | NOT_VERIFIED | NOT_ACCESSIBLE
□ observed state and recommendations not conflated
□ findings have evidence citations
□ links validated with HTTP response or accessibility state
□ rendering checked in light and dark themes
□ repository lifecycle (active/maintained/archived) determined
□ cross-surface consistency verified or marked NOT_VERIFIED
□ findings categorized by severity and impact
□ recommendations ordered by priority
□ remediation guidance actionable and specific
□ CTA destinations verified working
□ archive or unpin recommendations remain recommendations
□ missing optional enhancements not marked as failures
□ render evidence collected for visual findings
□ audit output ready to feed into redesign workflow
```

## Common Failure Modes

```text
❌ assuming stale proof is broken (6-month-old pin may be valid)
❌ conflating missing enhancement with quality failure
❌ marking findings without severity classification
❌ reporting RECOMMENDED as if OBSERVED
❌ ignoring private repositories when they are not public proof
❌ archive recommendations as automatic mutations
❌ not marking inaccessible evidence as NOT_VERIFIED
❌ visual findings without render evidence
❌ CTA analysis without destination verification
❌ cross-surface checks without observing all surfaces
❌ forgetting theme-dependent rendering variations
❌ treating visitor counters as expertise proof
```

## Verification & Handoff

Audit output serves three workflows:

```text
1. maintenance: User implements low-priority recommendations
2. redesign: github-profile skill uses audit findings to inform strategy
3. validation: Subsequent audits compare before/after state
```

Ensure findings are transparent, prioritized, and ready to drive action.

```text
FINAL REMINDER
Observe before judging. Separate state from strategy. Findings feed workflows.
Cross-surface consistency is the strongest quality signal. Proof quality beats badge count.
Link validity, rendering, and accessibility are non-negotiable. Missing optional enhancements
are not failures. Stale claims are findings, not disqualifications. Unknown evidence
remains NOT_VERIFIED, never assumed. Audit output informs but does not mutate.
```
