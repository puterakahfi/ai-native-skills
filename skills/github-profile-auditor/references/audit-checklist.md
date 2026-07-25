# GitHub Profile Audit Checklist

Use this reference during the VALIDATE phase to check profile quality across all surfaces.

## Identity Metadata

### Avatar
- [ ] Avatar present and visible
- [ ] Avatar renders in both light and dark themes
- [ ] Avatar is profile-owned or explicitly licensed
- State: OBSERVED | NOT_VERIFIED

### Display Name
- [ ] Display name matches verified identity
- [ ] Display name is not misleading or spoofed
- [ ] Display name supports positioning (not generic)
- State: OBSERVED | NOT_VERIFIED

### Bio
- [ ] Bio present (if goal requires it)
- [ ] Bio is <= 160 characters (GitHub limit)
- [ ] Bio matches README positioning or clearly complements it
- [ ] Bio avoids generic descriptors ("passionate developer", etc.)
- [ ] Bio is current or explicitly historical
- State: OBSERVED | NOT_VERIFIED

### Location
- [ ] Location present (if goal requires it)
- [ ] Location is current or clearly historical
- State: OBSERVED | NOT_VERIFIED

### Website Link
- [ ] Website link present (if goal requires it)
- [ ] Website link HTTP 200 (not 404/410/timeout)
- [ ] Website destination matches profile brand
- [ ] Website displays correctly (not parked/redirect trap)
- State: OBSERVED | NOT_VERIFIED

### Social Links
- [ ] All present social links return HTTP 200
- [ ] Social profiles align with GitHub profile positioning
- [ ] No dead or redirect-chain links
- State: OBSERVED | NOT_VERIFIED

### Status
- [ ] Status present (if goal requires it)
- [ ] Status is current or has explicit date
- [ ] Status supports current positioning
- State: OBSERVED | NOT_VERIFIED

---

## README Quality

### Structure & Hierarchy
- [ ] Opening viewport (first 300px) answers: who, what value, for whom?
- [ ] Hero section establishes clear positioning
- [ ] Content order matches visitor decision path (not random)
- [ ] Headings form semantic hierarchy (no missing levels)
- [ ] Sections logically grouped
- State: OBSERVED | NOT_VERIFIED

### Content Clarity
- [ ] Identity clear in first sentence
- [ ] Positioning specific (not generic)
- [ ] Proof before decoration
- [ ] Claims are verifiable or explicitly speculative
- [ ] No placeholder text or incomplete sections
- [ ] Writing is professional and error-free
- State: OBSERVED | NOT_VERIFIED

### Links & Destinations
- [ ] All internal links (to repo sections) valid
- [ ] All external links HTTP 200
- [ ] Links are contextual (not link trees)
- [ ] CTAs are specific and actionable
- State: OBSERVED | NOT_VERIFIED

### Assets
- [ ] Images (if any) display in light and dark themes
- [ ] Images are repository-owned or licensed
- [ ] SVG/badge links are not critical content
- [ ] Critical text not baked into images
- [ ] Graceful fallback if images fail to load
- State: OBSERVED | NOT_VERIFIED

### Rendering & Accessibility
- [ ] README renders correctly on GitHub
- [ ] README readable on narrow width (mobile)
- [ ] No horizontal scrolling required
- [ ] Code blocks syntax-highlighted
- [ ] Tables render correctly
- [ ] Contrast sufficient for readability
- [ ] No essential information hidden behind external deps
- State: OBSERVED | NOT_VERIFIED

---

## Pinned Repositories

### Inventory
- [ ] Current pin count observed (0-6 on GitHub)
- [ ] Each pinned repo accessible
- [ ] Pins are not all same age/type
- State: OBSERVED | NOT_VERIFIED

### Proof Roles
- [ ] Each pin has an explicit proof role:
  - flagship (main project or identity)
  - architecture-proof (system design or technical depth)
  - shipped-product (built and deployed)
  - open-source-leadership (maintained and community-driven)
  - learning-example (educational or demonstration)
  - domain-expertise (specialized knowledge or skill)
- [ ] Proof roles are complementary (not all same)
- [ ] Proof roles support the stated goal
- State: OBSERVED | NOT_VERIFIED

### Descriptions
- [ ] Each pin has a description (not empty)
- [ ] Descriptions explain the proof role (not just what it does)
- [ ] Descriptions are concise (1-2 sentences)
- [ ] Descriptions are current or explicitly historical
- State: OBSERVED | NOT_VERIFIED

### Repository State
- [ ] Repository is public (not private)
- [ ] Repository is active or explicitly maintained
- [ ] Repository README explains the project
- [ ] Repository topics are relevant and aligned
- [ ] Repository license is present
- State: OBSERVED | NOT_VERIFIED

---

## Selected Repositories

### Discoverability
- [ ] Repository has a description (not empty)
- [ ] Description explains purpose, not just tech stack
- [ ] Repository has 3-5 relevant topics
- [ ] Topics align with repository purpose and profile positioning
- State: OBSERVED | NOT_VERIFIED

### Documentation
- [ ] README present (or project is too trivial)
- [ ] README explains what the project does
- [ ] README explains why it exists
- [ ] README includes usage examples or quick start
- [ ] README is current (not stale)
- State: OBSERVED | NOT_VERIFIED

### Lifecycle
- [ ] Repository status is clear: active | maintained | archived | experimental
- [ ] Last commit date visible and recent (for active projects)
- [ ] Issue/PR activity visible (if applicable)
- [ ] Archive rationale clear (if archived)
- State: OBSERVED | NOT_VERIFIED

### License
- [ ] License file present (LICENSE, COPYING, etc.)
- [ ] License is recognized open-source license (if public)
- State: OBSERVED | NOT_VERIFIED

---

## Contribution Context

### Recent Activity
- [ ] Recent commits visible in profile timeline
- [ ] Contribution graph shows activity pattern
- [ ] "Current focus" matches recent activity or has explicit date
- [ ] Open issues/PRs visible (if maintainer)
- State: OBSERVED | NOT_VERIFIED

### Open-Source Participation
- [ ] If open-source claim: maintained projects visible
- [ ] If maintainer claim: contribution guidance visible
- [ ] Community links present (if applicable)
- [ ] Sponsorship info visible (if applicable)
- State: OBSERVED | NOT_VERIFIED

### Collaboration
- [ ] Profile shows collaborative work (if applicable)
- [ ] Co-authored commits or contributions visible
- [ ] Team affiliations clear
- State: OBSERVED | NOT_VERIFIED

---

## Cross-Surface Consistency

### README ↔ Bio
- [ ] README positioning matches bio messaging
- [ ] Bio complements README (not contradicts)
- [ ] No conflicting identity claims
- State: aligned | misaligned | NOT_VERIFIED

### README ↔ Pins
- [ ] Pinned repos support README positioning
- [ ] Proof roles align with stated value proposition
- [ ] All pins are "complementary" (rule: not quantity-based)
- State: aligned | misaligned | NOT_VERIFIED

### README ↔ Repositories
- [ ] Selected proof repos have meaningful descriptions
- [ ] Repository READMEs support README claims
- [ ] Project ownership and contribution clear
- State: aligned | misaligned | NOT_VERIFIED

### Positioning ↔ Activity
- [ ] "Current focus" matches recent activity or is dated
- [ ] No stale claims (>6 months old without date)
- [ ] Claimed expertise supported by visible work
- State: aligned | stale | NOT_VERIFIED

### CTA ↔ Goal
- [ ] CTA destination matches profile goal
- [ ] CTA is specific (not generic "connect")
- [ ] CTA destination is working and appropriate
- State: aligned | broken | NOT_VERIFIED

### Brand ↔ Surfaces
- [ ] Visual style consistent across README, avatar, external site
- [ ] Terminology consistent (same terms used)
- [ ] Tone consistent (not wildly different)
- State: consistent | drift | NOT_VERIFIED

---

## Enhancement Evaluation

### Optional Enhancements (not required)
- [ ] Stats badges (contrib graph, language chart): Are they accurate? Do they add value?
- [ ] Dynamic content (feed, updated_at): Is it maintained? Fallback readable?
- [ ] External widgets (Vercel, Wakatime): Are they working? Are they core to profile?
- [ ] Generated SVGs: Do they add value or just visual noise?
- [ ] Animations: Do they distract or enhance?

Decision: Is this enhancement worth the maintenance cost and dependency risk?
- [ ] YES: Enhancement has clear job, fallback, and owner
- [ ] NO: Remove or mark as optional
- [ ] UNCLEAR: Recommend removal or reconsider

State: APPROVED | REJECTED | NOT_VERIFIED

---

## Severity Definitions

### CRITICAL
- Blocks profile access or credibility
- Example: website link is 404, all pins archived, README completely broken
- Action: Fix immediately

### HIGH
- Materially impacts visitor comprehension or goal achievement
- Example: bio contradicts positioning, proof is private not public, broken CTA
- Action: Fix before major job search or public promotion

### MEDIUM
- Gaps or inconsistencies that reduce effectiveness
- Example: empty pin description, outdated "current focus", weak proof role
- Action: Fix in next cycle

### LOW
- Polish or minor optimization opportunities
- Example: spacing inconsistency, missing optional enhancement, typo
- Action: Address if time permits

### INFO
- Observation or optional note
- Example: "6 pins filled; fewer stronger pins often more effective", "consider branching out to X"
- Action: Consider but not urgent
