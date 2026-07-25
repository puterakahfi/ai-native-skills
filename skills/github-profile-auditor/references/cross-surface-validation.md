# Cross-Surface Validation

Use this reference during the CROSS-CHECK phase to verify profile consistency across all public surfaces.

## Profile Ecosystem

A GitHub profile is a system of interconnected surfaces:

```text
identity metadata
  ↓ (establishes who)
profile README
  ↓ (establishes positioning & proof)
pinned repositories
  ↓ (proves ownership of work)
selected public repositories
  ↓ (demonstrates depth & scope)
contribution context
  ↓ (shows activity & participation)
external destinations
  ↓ (enables desired action)
desired action achieved
```

All surfaces must tell one compatible story. Inconsistency at any point breaks the chain.

## Consistency Checks

### 1. README Positioning ↔ Pinned Repositories

**Check:** Does pinned proof support README claim?

**Examples of alignment:**
- README: "I build AI-native engineering systems"
  Pins: ai-native-skills, ai-native-core, native-ai-fw ✓
  
- README: "Full-stack product engineer"
  Pins: 2 shipping products, 1 design system, 1 infra repo ✓
  
- README: "Open-source maintainer"
  Pins: 3-4 actively maintained projects ✓

**Examples of misalignment:**
- README: "AI systems architect"
  Pins: 6 forked awesome-lists with no ownership ✗
  
- README: "Product builder"
  Pins: All 5+ year old archived projects ✗
  
- README: "Community leader"
  Pins: All solo projects, no community contribution ✗

**Finding:** If misaligned, report which surfaces conflict and recommend:
- Update pins to match positioning, OR
- Update positioning to match actual proof, OR
- Mix pins to show complementary proof roles

### 2. README Claims ↔ Repository State & README

**Check:** Are README claims verifiable in selected repos?

**Examples of alignment:**
- README claim: "I designed the Next.js component system"
  Repository evidence: Repo exists, README explains design decisions, code shows ownership ✓
  
- README claim: "Built 3 shipped products"
  Repository evidence: 3 repos are public, have working homepage/deploy links ✓

**Examples of misalignment:**
- README claim: "Built X product"
  Repository evidence: Repo is private or archived ✗
  
- README claim: "Designed Y system"
  Repository evidence: Repo README empty, commits are all cherry-picked from others ✗
  
- README claim: "Maintained 5 open-source projects"
  Repository evidence: No open issues answered, no PRs merged in 2+ years ✗

**Finding:** If misaligned, report which claims lack evidence and recommend:
- Link to actual verifiable repositories
- Archive or unpin repos that don't support claim
- Add new evidence that does support claim
- Reframe claim to match actual proof

### 3. "Current Focus" ↔ Recent Activity

**Check:** Does stated current focus match recent activity?

**Examples of alignment:**
- README: "Currently working on: Native AI skills framework (July 2026)"
  Activity: Recent commits, open issues, active discussions ✓
  
- README: "Current focus: Product design for AI systems (June 2026 - ongoing)"
  Activity: Recent product commits, design documents updated ✓

**Examples of misalignment:**
- README: "Currently building X"
  Activity: No commits in 12 months ✗
  
- README: "Currently focused on Y"
  Activity: All recent work in different domain ✗
  
- README: "Current focus: (not stated)"
  Activity: Recent commits visible but hard to understand current direction ✗

**Finding:** If misaligned, report and recommend:
- Update "current focus" to reflect actual recent work
- Add date qualifier ("As of July 2026") to make staleness explicit
- Archive old projects or mark as "archived (2023)"
- Link to where recent work is happening if moved

### 4. CTA (Call-To-Action) ↔ Goal & Audience

**Check:** Does primary CTA match stated goal and audience?

**Examples of alignment:**
- Goal: Hiring signal
  Audience: Hiring managers, CTOs
  CTA: "View recent projects" or "Contact me for opportunities" ✓
  
- Goal: Open-source contribution
  Audience: Developers, contributors
  CTA: "See how to contribute" or "Open discussions" link ✓
  
- Goal: Consulting engagement
  Audience: Potential clients
  CTA: "Discuss a project" or "Services & rates" ✓

**Examples of misalignment:**
- Goal: Hiring signal
  CTA: "Follow my blog" (no portfolio link) ✗
  
- Goal: Open-source
  CTA: "Email me" (no link to contribution guide) ✗
  
- Goal: Consulting
  CTA: "GitHub" (breaks trust; no contact info) ✗

**Finding:** If misaligned, report and recommend:
- Make CTA specific and actionable
- Ensure destination is working (HTTP 200)
- Align CTA label with actual destination
- Ensure CTA destination matches goal

### 5. Claimed Identity ↔ GitHub Profile Metadata

**Check:** Do bio, name, and metadata support README identity claim?

**Examples of alignment:**
- README: "AI-native engineering architect"
  Bio: "Native AI systems · Systems thinking · Architect"
  Location: (relevant or not misleading)
  Status: (current or explicitly relevant) ✓
  
- README: "Product builder & designer"
  Bio: "Product engineering & design systems"
  Links: (portfolio, product pages) ✓

**Examples of misalignment:**
- README: "I specialize in infrastructure"
  Bio: "Passionate about blockchain" ✗
  
- README: "AI-native engineer"
  Status: "Hiring for Web3 positions" ✗
  
- README: "Currently consulting"
  Location: Shows past company, not current status ✗

**Finding:** If misaligned, report and recommend:
- Update bio to match README positioning
- Update status if outdated
- Correct location if misleading
- Align all metadata with primary narrative

### 6. Brand Grammar Consistency

**Check:** Is visual and verbal identity consistent across surfaces?

**Visual consistency:**
- Avatar style matches external site aesthetic
- Colors/themes align across README and personal site
- Typography consistent (if applicable)

**Verbal consistency:**
- Terminology consistent (same terms used across surfaces)
- Tone consistent (professional, casual, editorial, etc.)
- Perspective consistent (first-person, third-person)

**Examples of consistency:**
- All surfaces use "systems thinking", "architecture", "explicit" ✓
- Avatar, README, and personal site follow same visual language ✓

**Examples of drift:**
- README: "AI-native engineering"
  Personal site: "ChatGPT apps and AI products" (different terminology) ✗
  
- README: Professional, systems-focused tone
  Twitter: Casual meme-driven tone ✗ (if linked in profile)
  
- README: Third-person narrative
  Bio: First-person casual ✗

**Finding:** If drift detected, report and recommend:
- Decide on one primary brand voice
- Update surfaces to align
- Or explicitly accept the differences and mark as intentional variant

### 7. Public Proof ↔ Proof Claims

**Check:** Is all claimed proof actually public and accessible?

**Examples of alignment:**
- README: "See my work in [repo]"
  Repository: Public, accessible, README clear ✓
  
- README: "Shipped [product]"
  Product: Live, publicly accessible, author credit visible ✓

**Examples of misalignment:**
- README: "I built [system]"
  Repository: Private (author cannot share publicly) ✗
  
- README: "Shipped [product]"
  Product: Down or requiring authentication to view ✗
  
- README: "Maintained [project]"
  Repository: Archived, marked as "no longer maintained" ✗

**Finding:** If proof is private or inaccessible, report and recommend:
- Link to publicly verifiable work instead
- Describe results without linking to unavailable code
- Archive claimed work if it's no longer maintained
- Be explicit about what is private ("private implementation") vs. public proof

---

## Cross-Surface Validation Matrix

| Surface 1 | Surface 2 | Alignment Check | Misalignment Finding |
|---|---|---|---|
| README positioning | Pinned repos | Do pins prove the claim? | Update pins or positioning |
| README claims | Repo state/README | Are claims verifiable? | Add proof or update claims |
| "Current focus" | Recent activity | Is focus current? | Date it or update focus |
| CTA | Goal | Does CTA match goal? | Align or replace CTA |
| Bio | README | Do they complement? | Update bio or README |
| Brand grammar | All surfaces | Is identity consistent? | Align terminology/tone |
| Public proof claims | Repository access | Is proof accessible? | Link to public work only |

---

## Validation Procedure

1. **List all surfaces:**
   - Identity metadata (avatar, bio, location, website, status)
   - README
   - Pinned repositories (if any)
   - Selected public repositories
   - External destinations (personal site, Twitter, etc.)
   - Contribution activity

2. **Extract claims from each surface:**
   - What does this surface claim about identity?
   - What does this surface claim about capability?
   - What does this surface claim about activity?
   - What does this surface claim about availability/contact?

3. **Cross-reference each claim:**
   - Is it supported by another surface?
   - Is it contradicted?
   - Is it NOT_VERIFIED (not observable)?

4. **Classify consistency:**
   - **aligned:** Surfaces tell compatible story
   - **misaligned:** Surfaces contradict or weaken each other
   - **NOT_VERIFIED:** Evidence unavailable; cannot confirm

5. **Generate findings:**
   - Report misalignments with evidence
   - Recommend fixes with specific guidance
   - Mark NOT_VERIFIED where evidence unavailable

---

## Readiness Determination

After cross-surface validation, determine profile readiness:

### audit-ready
- Profile is observable and verifiable
- Some gaps exist but no critical misalignments
- Can proceed to redesign workflow if desired

### needs-fixes
- Misalignments or critical gaps found
- Recommend fixing before major activity (job search, public promotion)
- User can implement fixes and re-audit

### hire-ready
- All surfaces aligned
- Proof is strong and verifiable
- No critical gaps
- Suitable for active job search

### open-source-ready
- Contribution paths clear
- Maintained projects visible
- Community engagement evident
- Ready for open-source promotion

### community-ready
- Public engagement visible
- Collaboration or mentorship signaled
- Community contributions documented
- Ready for community role or sponsorship

---

## Notes

Cross-surface validation is the strongest quality signal. A beautiful README cannot compensate for weak pinned proof, broken links, or contradictory messaging.

Focus validation on coherence and evidence, not aesthetics. A plain-text profile with aligned surfaces outperforms a decorated profile with misaligned messaging.
