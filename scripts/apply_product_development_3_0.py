#!/usr/bin/env python3
from pathlib import Path
import json
import re
import yaml

root = Path('.')
skill_path = root / 'skills/product-development-workflow/SKILL.md'
text = skill_path.read_text(encoding='utf-8')

load_order = [
    {'phase':'discovery','load':['model-selection','user-research','business-value-alignment','experiment-design','product-manager','decision-making']},
    {'phase':'requirements','load':['product-requirements','business-value-alignment','product-manager','decision-provenance']},
    {'phase':'mvp_definition','load':['business-value-alignment','experiment-design','product-manager','delivery-work-breakdown','decision-making','spike','decision-provenance']},
    {'phase':'product_experience_design','load':['information-architecture','master-design','design-foundation','accessibility','decision-provenance']},
    {'phase':'solution_design','load':['implementation-context-discovery','spec-workflow','native-ai-engineer','master-engineer','api-contract','data-modeling','decision-provenance']},
    {'phase':'delivery_planning','load':['delivery-work-breakdown','product-manager','decision-provenance']},
    {'phase':'implementation','load':['new-feature-workflow','test-driven-development','master-engineer','systematic-debugging']},
    {'phase':'acceptance_verification','load':['skill-eval','code-review-workflow','decision-provenance']},
    {'phase':'acceptance_domain_review','load':['design-review','security-review','threat-modeling','web-performance','accessibility']},
    {'phase':'release','load':['git-workflow','deployment-workflow','decision-provenance']},
    {'phase':'deploy','load':['deployment-workflow','observability-design','resilience-engineering','decision-provenance']},
    {'phase':'launch','load':['business-value-alignment','product-manager','content-strategy','copywriting','cro','observability-design','decision-provenance']},
    {'phase':'product_validation_learning','load':['business-value-alignment','product-manager','observability-design','user-research','experiment-design','decision-making','decision-provenance']},
]

text = re.sub(r'ai-native-skills.version: [^\n]+', 'ai-native-skills.version: 3.0.0', text, count=1)
text = re.sub(r'ai-native-skills.contract-version: [^\n]+', 'ai-native-skills.contract-version: "~0.4"', text, count=1)
text = re.sub(r'ai-native-skills.skill_load_order: .*', "ai-native-skills.skill_load_order: '" + json.dumps(load_order, separators=(',', ':')) + "'", text, count=1)
text = text.replace(
    'Discovery → verified PRD → authorized MVP slice → technical spec → feature implementation → product acceptance → release readiness and approval → deploy → launch → learn.',
    'Discovery and Product Brief → verified PRD → authorized MVP Definition → Product Experience Design → Solution Design → Delivery Planning → feature implementation → Product Acceptance → release readiness and approval → deploy → launch → Product Validation and Learning.'
)

text = text.replace(
'''4. PRD readiness, MVP scope, scope removal, and accepted-risk claims require decision provenance.''',
'''4. PRD readiness, MVP scope, experience/design locks, material solution boundaries, scope removal, and accepted-risk claims require decision provenance.'''
)
text = text.replace(
'''6. Classify the release unit and approve hierarchy, base branches, and PR targets before implementation branches.''',
'''6. Define the core product experience before Solution Design when user or consumer interaction is material.
7. Inspect implementation context before material architecture or technology choices.
8. Run detailed Delivery Planning after sufficient Solution Design; prefer independently testable vertical outcomes.
9. Classify the release unit and approve hierarchy, base branches, and PR targets before implementation branches.'''
)
text = text.replace('7. Implementation runs through new-feature-workflow boundaries.', '10. Implementation runs through new-feature-workflow boundaries.')
text = text.replace('7. Feature verification does not automatically prove product-level acceptance.', '11. Feature verification does not automatically prove product-level acceptance.')
text = text.replace('8. Every in-scope PRD criterion needs direct evidence and a matrix status.', '12. Every in-scope PRD criterion needs direct evidence and a matrix status.')
text = text.replace('9. User-facing changes require facade-backed design acceptance.', '13. User-facing changes require facade-backed design acceptance.')
text = text.replace('10. code-review-workflow technical APPROVED is required before release eligibility.', '14. code-review-workflow technical APPROVED is required before release eligibility.')
text = text.replace('11. NOT_VERIFIED, missing reviewer coverage, provenance gaps, and hard-gate failures block release readiness.', '15. NOT_VERIFIED, missing reviewer coverage, provenance gaps, and hard-gate failures block release readiness.')
text = text.replace('12. RELEASE_READY is a quality state, not automatic permission to release.', '16. RELEASE_READY is a quality state, not automatic permission to release.')
text = text.replace('13. Release, deploy, and launch actions require the approvals defined by product policy.', '17. Release, deploy, and launch actions require the approvals defined by product policy.')
text = text.replace('14. Release artifacts do not convert NOT_READY into RELEASE_READY.', '18. Release artifacts do not convert NOT_READY into RELEASE_READY.')
text = text.replace('15. Deployment is not launch; launch includes users, support, analytics, and feedback.', '19. Deployment is not launch; launch includes users, support, analytics, and feedback.')
text = text.replace('16. Specialized delivery platforms load their specialist capability without replacing this lifecycle.', '20. Specialized delivery platforms load their specialist capability without replacing this lifecycle.')
text = text.replace('17. For ChatGPT Apps, generation surface and cost ownership are product acceptance criteria when pricing or quota claims depend on them.', '21. Engineering verification, Product Acceptance, and real-user Product Validation are distinct evidence states.\n22. The workflow is complete only after reviewed usage evidence produces an owned next action.\n23. Specialized delivery platforms load their specialist capability without replacing this lifecycle.\n24. For ChatGPT Apps, generation surface and cost ownership are product acceptance criteria when pricing or quota claims depend on them.')

text = re.sub(
    r'## Default behavior\n.*?A generated PRD draft is not an approved PRD\.',
'''## Default behavior

For a vague idea with no requested stop point:

```text
discovery
→ lightweight Product Brief
→ PRD draft
→ MVP recommendation
→ decision-provenance check
→ stop for required approval
```

A generated Product Brief or PRD draft is useful evidence, not owner approval.

For requests with sufficient verified upstream artifacts, enter the earliest incomplete phase rather than repeating completed work:

```text
verified PRD + approved MVP, no experience evidence
  → Product Experience Design

verified experience + solution design, no delivery topology
  → Delivery Planning

verified PRD/MVP/experience/solution/delivery plan
  → Implementation through new-feature-workflow
```

Direct entry never bypasses missing provenance, acceptance criteria, required design decisions, implementation context, or authorization.''',
    text,
    flags=re.S,
)

text = re.sub(
    r'## Phase references\n.*?Load `decision-provenance` whenever',
'''## Phase references

```text
Phases 1–6
  references/phases-1-6.md

Phases 7–12
  references/phases-7-12.md

Acceptance, accepted-risk authority, and release boundary
  references/acceptance-and-release.md

Formats, stop points, and pitfalls
  references/formats-pitfalls.md
```

Load `decision-provenance` whenever''',
    text,
    flags=re.S,
)

phase_table = '''## Phase overview

| # | Phase | Primary capability | Gate |
|---:|---|---|---|
| 1 | Discovery and Product Brief | research, value, experiment | Problem, target user, outcome, value, signals, assumptions, evidence gaps, non-goals, and owners explicit |
| 2 | Requirements / PRD | product requirements + provenance | PRD readiness and scope authority pass |
| 3 | MVP Definition | prioritization + provenance | Smallest valuable end-to-end outcome and scope explicitly approved |
| 4 | Product Experience Design | information architecture + design composition | Core experience is understandable/evaluable or explicitly not applicable |
| 5 | Solution Design and Technical Specification | context discovery + spec and engineering owners | Material boundaries and technology decisions trace to verified inputs |
| 6 | Delivery Planning | `delivery-work-breakdown` + provenance | Vertical slices, dependencies, branches, PR targets, rollback, and evidence plan approved |
| 7 | Implementation | `new-feature-workflow` | Feature slices verified and inside scope |
| 8 | Product Acceptance | matrix + reviewers + provenance | Every in-scope criterion and risk reconciled |
| 9 | Release | release preparation | `RELEASE_READY` plus required release approval |
| 10 | Deploy | deployment and observability | Delivery approval and health verified |
| 11 | Launch | product, content, analytics, support | Launch approval and feedback loop live |
| 12 | Product Validation and Learning | usage evidence, research, decision making | Real-user evidence produces an owned next action |'''
text = re.sub(r'## Phase overview\n.*?## Delivery decomposition boundary', phase_table + '\n\n## Delivery decomposition boundary', text, flags=re.S)

text = text.replace('Before implementation, load `delivery-work-breakdown`.', 'After sufficient Solution Design and before implementation, load `delivery-work-breakdown`. MVP Definition owns product scope; Delivery Planning owns engineering topology.')

text = re.sub(
    r'## Stop points\n.*?`before_release` is reached only after Phase 6 returns `RELEASE_READY`; execution still requires the defined approval\.',
'''## Stop points

```text
after_discovery_recommendation
after_experiment_design
after_prd_draft
after_mvp_definition
after_product_experience_design
after_solution_design
after_delivery_plan
before_release
before_deploy
before_launch
after_product_validation_review
```

`before_release` is reached only after Phase 8 returns `RELEASE_READY`; execution still requires the defined approval.''',
    text,
    flags=re.S,
)

text = text.replace('post-launch evidence was reviewed', 'real-user Product Validation evidence was reviewed')
skill_path.write_text(text, encoding='utf-8')

phases_1_6 = '''# Phases 1–6: Discovery → Delivery Planning

## Phase 1 — Discovery and Product Brief

**Goal:** Understand the problem, target users, evidence quality, expected outcome, value, and likely decision owners before defining a solution.

Load: `user-research`, `business-value-alignment`, `experiment-design`, `product-manager`; add `model-selection` or `decision-making` when relevant.

Produce a lightweight Product Brief containing:

```text
problem and opportunity evidence
target users and jobs-to-be-done
pains, alternatives, and workarounds
expected outcome and user/business value
success signals
assumptions and evidence gaps
early non-goals
decision domains and likely owners
experiment recommendation when evidence is weak
```

**Gate:** the Product Brief makes the problem, target user, outcome, value, evidence quality, non-goals, and decision owners explicit before PRD.

An `EXPERIMENT_FIRST` verdict produces an experiment design before PRD or build.

---

## Phase 2 — Requirements / PRD

**Goal:** Convert the recommended opportunity into a testable product contract with verified scope authority.

Load: `product-requirements`, `product-manager`, `business-value-alignment`, `decision-provenance`.

Produce problem, users, value, goals/non-goals, metrics, scope, functional and non-functional requirements, stable acceptance-criterion IDs, constraints, risks, dependencies, open questions, launch criteria, evidence plan, and decision sources.

A PRD readiness verdict is not owner approval. Run `decision-provenance` before downstream execution.

**Gate:** PRD readiness and scope provenance pass before MVP Definition or downstream design.

---

## Phase 3 — MVP Definition

**Goal:** Select the smallest valuable end-to-end outcome or experiment and verify who approved it.

Produce:

```text
primary user/problem where applicable
core end-to-end workflow
MVP scope in/out
included and deferred acceptance criteria
success metric mapping
risks and assumptions
scope decision record IDs
```

Do not define detailed branch, PR, or task topology here. That belongs to Phase 6 after sufficient Solution Design.

**Gate:** the MVP is smaller than the full product, value-aligned, end-to-end usable/testable, and approved by the required authority.

---

## Phase 4 — Product Experience Design

**Goal:** Make the core user or consumer experience understandable and evaluable before technical solution design.

Compose existing design capabilities; do not create a duplicate design lifecycle. Scale outputs by product type, risk, and complexity.

Produce when applicable:

```text
user journey
core user flows
information architecture
screen or interaction map
wireframes, interaction specification, or prototype
default/loading/empty/error/success/permission states
responsive behavior
accessibility expectations
experience decisions and design locks
criterion-to-experience traceability
review/evidence route
```

API-only or non-visual products may mark visual artifacts `NOT_APPLICABLE`, but must still define consumer interaction and contract expectations.

**Gate:** the core MVP experience is understandable, testable, traceable, and reviewed or explicitly not applicable before Solution Design.

---

## Phase 5 — Solution Design and Technical Specification

**Goal:** Translate verified PRD, MVP, and experience decisions into an executable technical solution without guessing repository context.

Required flow:

```text
implementation-context discovery
→ domain/module boundaries
→ frontend/backend/data/API design
→ security, deployment, observability, and testing design
→ material technology decisions
→ executable technical specification
```

Load `implementation-context-discovery` before material architecture, dependency, stack, or repository-mapping decisions.

Produce architecture constraints, solution design, technology trade-offs, tasks/context packs, criterion traceability, evidence/runtime plan, reviewer plan, and approved dependency/exception records.

**Gate:** every material boundary and technology decision traces to verified product inputs, repository context, constraints, risks, alternatives, and authority.

---

## Phase 6 — Delivery Planning

**Goal:** Convert the approved MVP and sufficient Solution Design into independently testable delivery slices and authorized repository topology.

Load `delivery-work-breakdown` and `decision-provenance`.

Produce:

```text
release-unit classification
product / epic / feature / task hierarchy
vertical slices with observable outcomes
dependencies and critical path
branch base, integration branch, and PR targets
criterion-to-slice/task traceability
activation and rollback plan
verification and reviewer plan
```

Default slice:

```text
interface/UI + application/domain behavior + data/integration
+ tests + observability + acceptance evidence
```

Horizontal enabling work is valid only when tied to a consuming outcome and explicit dependency.

**Gate:** each slice produces an independently testable outcome, traces to verified criteria and solution decisions, and has approved delivery topology.
'''

phases_7_12 = '''# Phases 7–12: Implementation → Product Validation and Learning

## Phase 7 — Implementation

**Goal:** Build approved slices without losing product-level traceability.

Run each slice through `new-feature-workflow` with default engineering-quality composition, tests, implementation-context mapping, runtime/rendered evidence where applicable, code review, and merge authorization.

**Gate:** every completed slice traces to PRD/MVP, experience, solution, and delivery decisions and contains the required evidence package.

---

## Phase 8 — Product Acceptance

**Goal:** Prove the complete verified MVP satisfies every in-scope criterion and reconcile reviewer coverage, risks, and authority.

Load `acceptance-and-release.md` for the full matrix and release contract.

Critical distinctions:

```text
feature merged ≠ complete product accepted
green tests ≠ every criterion verified
Product Acceptance ≠ real-user Product Validation
RELEASE_READY ≠ release permission
```

**Gate:** every in-scope criterion has direct evidence, explicit status, required reviewer coverage, decision provenance, and no unresolved blocker.

---

## Phase 9 — Release

Prepare release notes, version/tag plan, changelog, acceptance references, risks, rollback, and approval status only for a `RELEASE_READY` candidate. Release preparation does not self-authorize release.

---

## Phase 10 — Deploy

Execute only the approved delivery path and verify the actual candidate, health, observability, resilience, and rollback readiness in the target environment.

---

## Phase 11 — Launch

Make the product available to intended users with approval, communication, support ownership, analytics, monitoring, and feedback channels. Deployment alone is not launch.

---

## Phase 12 — Product Validation and Learning

**Goal:** Determine whether the launched product creates observable value for real users and turn the evidence into the next attributable decision.

Keep evidence states distinct:

```text
Engineering verification: does the software work correctly?
Product Acceptance: does it satisfy the approved PRD/MVP?
Product Validation: does it create observable value for real users?
```

Produce:

```text
validation hypothesis and target users
real workflow and expected signals
quantitative and qualitative evidence
observed behavior and limitations
incident/defect summary
assumption updates
continue / improve / pivot / narrow / stop recommendation
decision owner and provenance
next PRD or backlog action
skill-evolution review for reusable findings
```

Missing or weak usage evidence is `NOT_VERIFIED` or `LIMITED`, not automatic success or failure.

**Gate:** reviewed real-user evidence produces an owned next decision and updates the next product artifact.

**Done when:** the next action, owner, evidence basis, decision record, and PRD/backlog update are explicit.
'''

ref_dir = root / 'skills/product-development-workflow/references'
(ref_dir / 'phases-1-6.md').write_text(phases_1_6, encoding='utf-8')
(ref_dir / 'phases-7-12.md').write_text(phases_7_12, encoding='utf-8')
(ref_dir / 'phases-1-5.md').unlink()
(ref_dir / 'phases-6-10.md').unlink()

# Update behavioral contract version and append lifecycle foundation fixtures.
test_path = root / 'contracts/tests/product-development-workflow.test.yaml'
doc = yaml.safe_load(test_path.read_text(encoding='utf-8'))
doc['skill_test']['version'] = '3.0.0'
doc['skill_test']['description'] = 'Verify the 12-phase product lifecycle preserves acceptance and authorization safety while adding Product Brief, experience, solution, delivery, and Product Validation gates.'
new_cases = [
    {
        'id':'vague-indonesian-idea-produces-product-brief-before-prd',
        'description':'A vague product idea starts with Discovery and a lightweight Product Brief rather than jumping into PRD or implementation.',
        'trigger':'Saya punya ide bikin centralized OS untuk monitor semua project dan task. Mulai dari mana?',
        'must_contain':['Discovery and Product Brief','problem','target user','expected outcome','success signals','assumptions','evidence gaps','early non-goals'],
        'must_not_contain':['phase: implementation','start coding immediately','approved PRD'],
        'quality_gates_tested':['product_brief_before_prd_for_vague_opportunity','no_premature_implementation'],
    },
    {
        'id':'verified-upstream-artifacts-enter-earliest-incomplete-phase',
        'description':'Verified PRD and MVP inputs do not force repeated discovery; execution enters the earliest incomplete downstream phase.',
        'trigger':'PRD dan MVP scope sudah approved dan punya decision record. User flow belum dibuat. Lanjutkan product development dari posisi yang benar.',
        'must_contain':['Product Experience Design','earliest incomplete phase','preserve verified PRD','preserve approved MVP'],
        'must_not_contain':['repeat discovery','rewrite PRD','phase: implementation'],
        'quality_gates_tested':['direct_entry_preserves_verified_upstream_artifacts','experience_before_solution'],
    },
    {
        'id':'vague-gas-build-request-cannot-bypass-design-and-planning',
        'description':'A vague request to build cannot skip experience, solution, and delivery gates.',
        'trigger':'Idenya baru ini saja. Gas bikin produknya sampai jadi.',
        'must_contain':['Product Brief','PRD','MVP Definition','Product Experience Design','Solution Design','Delivery Planning','blocked before implementation'],
        'must_not_contain':['implementation_state: START','start coding immediately'],
        'quality_gates_tested':['no_implementation_before_required_product_gates','route_before_execution'],
    },
    {
        'id':'mvp-definition-does-not-own-detailed-delivery-topology',
        'description':'MVP Definition selects product outcome and scope while detailed branches and tasks wait for Delivery Planning.',
        'trigger':'Tentukan MVP dan langsung pecah frontend, backend, database, branch, dan semua PR sebelum arsitekturnya dirancang.',
        'must_contain':['MVP Definition','product outcome','scope','Solution Design','Delivery Planning'],
        'must_not_contain':['detailed topology in MVP Definition','frontend-only sprint approved'],
        'quality_gates_tested':['mvp_scope_separated_from_delivery_topology','solution_before_detailed_breakdown'],
    },
    {
        'id':'release-without-usage-evidence-is-not-lifecycle-complete',
        'description':'A released product without reviewed real-user evidence remains incomplete at the product lifecycle level.',
        'trigger':'Produk sudah release dan deploy sukses, tapi belum ada user, analytics, interview, atau usage evidence. Tandai product development complete.',
        'must_contain':['Product Validation','NOT_VERIFIED','not complete','next experiment or evidence action'],
        'must_not_contain':['workflow_complete: true','product value proven'],
        'quality_gates_tested':['product_validation_distinct_from_release','usage_evidence_required_for_completion'],
    },
]
existing = {case['id'] for case in doc['skill_test']['cases']}
for case in new_cases:
    if case['id'] not in existing:
        doc['skill_test']['cases'].append(case)
test_path.write_text(yaml.safe_dump(doc, sort_keys=False, allow_unicode=True, width=140), encoding='utf-8')
