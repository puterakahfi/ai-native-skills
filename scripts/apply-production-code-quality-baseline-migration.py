#!/usr/bin/env python3
"""Apply the reviewed issue #137 production-code quality baseline migration.

This branch-local migrator is intentionally assertion-heavy. It fails when any source
shape differs from the inspected main-branch evidence so the migration cannot silently
patch a newer or semantically different workflow.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace_once(path: str, old: str, new: str) -> None:
    target = ROOT / path
    source = target.read_text(encoding="utf-8")
    count = source.count(old)
    if count != 1:
        raise RuntimeError(f"{path}: expected exactly one match, found {count}: {old[:100]!r}")
    target.write_text(source.replace(old, new, 1), encoding="utf-8")


def patch_router() -> None:
    path = "skills/workflow-router/SKILL.md"
    replace_once(path, "  ai-native-skills.version: 1.6.0", "  ai-native-skills.version: 1.7.0")
    replace_once(
        path,
        '  ai-native-skills.requires: "redesign-workflow design-audit design-refinement design-review brand-identity-review new-feature-workflow bugfix-workflow code-review-workflow deployment-workflow product-development-workflow delivery-work-breakdown chatgpt-app-development skill-evolution skill-eval git-workflow skill-doctor spec-workflow task-continuity"',
        '  ai-native-skills.requires: "redesign-workflow design-audit design-refinement design-review brand-identity-review new-feature-workflow bugfix-workflow code-review-workflow deployment-workflow product-development-workflow delivery-work-breakdown chatgpt-app-development skill-evolution skill-eval git-workflow skill-doctor spec-workflow task-continuity production-code-quality-baseline"',
    )
    replace_once(
        path,
        '  ai-native-skills.related_skills: \'["role-switcher","product-development-workflow","delivery-work-breakdown","chatgpt-app-development","redesign-workflow","design-audit","design-refinement","design-review","brand-identity-review","skill-evolution","bugfix-workflow","new-feature-workflow","code-review-workflow","deployment-workflow","spec-workflow","task-continuity"]\'',
        '  ai-native-skills.related_skills: \'["role-switcher","product-development-workflow","delivery-work-breakdown","chatgpt-app-development","redesign-workflow","design-audit","design-refinement","design-review","brand-identity-review","skill-evolution","bugfix-workflow","new-feature-workflow","code-review-workflow","deployment-workflow","spec-workflow","task-continuity","production-code-quality-baseline"]\'',
    )
    replace_once(
        path,
        """classify requested outcome
→ select one primary lifecycle or capability
→ resolve platform/domain overlays
→ resolve design domain when design is involved
→ load only required skills/reviewers
→ execute""",
        """classify requested outcome
→ select one primary lifecycle or capability
→ classify production-code impact
→ attach production-code-quality-baseline when production behavior changes
→ resolve platform/domain overlays
→ resolve design domain when design is involved
→ load only required skills/reviewers
→ execute""",
    )
    replace_once(
        path,
        "| Fix broken implementation behavior | `bugfix-workflow` | systematic-debugging, relevant reviewers |",
        "| Fix broken implementation behavior | `bugfix-workflow` | `production-code-quality-baseline`, systematic-debugging, relevant reviewers |",
    )
    replace_once(
        path,
        "| Add a capability to an existing product | `new-feature-workflow` | spec, product/design/engineering owners |",
        "| Add a capability to an existing product | `new-feature-workflow` | `production-code-quality-baseline`, spec, product/design/engineering owners |",
    )
    section = """
## Production-Code Quality Overlay

Production-code quality is an overlay, not a second lifecycle.

```text
new feature, bugfix, behavior change, refactor, migration,
or generated code intended for repository submission
  → classify production impact
  → preserve the selected primary lifecycle
  → attach production-code-quality-baseline
```

Classification:

```text
PRODUCTION_CODE_CHANGE
NON_PRODUCTION_CHANGE
DISPOSABLE_EXPERIMENT
NOT_VERIFIED
```

Use requested outcome and repository impact, not the artifact noun or diff size alone.
`NOT_VERIFIED` blocks complete implementation or merge-readiness claims.

When attached, the overlay coordinates:

```text
TDD or attributable authorized exception
clean-code and module/failure-path assessment
conditional SOLID, DDD, pattern, Clean Architecture, security,
performance, resilience, observability, data, and design applicability
claim-appropriate evidence
independent architecture and code review
remaining approval and merge authority
```

The overlay must not manufacture abstractions. Conditional concerns may resolve to
`NOT_APPLICABLE` or `NOT_JUSTIFIED` with inspectable evidence. Silence is
`NOT_VERIFIED`, never PASS.

Until `ai-native-core#56` is accepted, this route is provisional under the reviewed
core-gap exemption owned by `production-code-quality-baseline`.

"""
    replace_once(path, "## Delivery Topology Overlay\n", section + "## Delivery Topology Overlay\n")
    replace_once(
        path,
        "Functional symptom or regression? → bugfix-workflow",
        "Functional symptom or regression? → bugfix-workflow + production-code-quality-baseline",
    )
    replace_once(
        path,
        "New capability? → new-feature-workflow",
        "New capability? → new-feature-workflow + production-code-quality-baseline",
    )


def patch_bugfix() -> None:
    path = "skills/bugfix-workflow/SKILL.md"
    replace_once(path, "  ai-native-skills.version: 1.1.0", "  ai-native-skills.version: 1.2.0")
    replace_once(
        path,
        '  ai-native-skills.requires: "systematic-debugging implementation-context-discovery master-engineer security-review test-driven-development architecture-review"',
        '  ai-native-skills.requires: "systematic-debugging implementation-context-discovery master-engineer security-review test-driven-development clean-code architecture-review code-review-workflow production-code-quality-baseline"',
    )
    replace_once(
        path,
        "  ai-native-skills.skill_load_order: '[{\"phase\":\"investigate\",\"load\":[\"systematic-debugging\"]},{\"phase\":\"pre-fix-context\",\"load\":[\"implementation-context-discovery\"],\"condition\":\"material_repository_conventions_affected\"},{\"phase\":\"fix\",\"load\":[\"systematic-debugging\"]},{\"phase\":\"review\",\"load\":[\"architecture-review\"]}]'",
        "  ai-native-skills.skill_load_order: '[{\"phase\":\"reproduce\",\"load\":[\"production-code-quality-baseline\",\"test-driven-development\"]},{\"phase\":\"investigate\",\"load\":[\"systematic-debugging\"]},{\"phase\":\"pre-fix-context\",\"load\":[\"implementation-context-discovery\"],\"condition\":\"material_repository_conventions_affected\"},{\"phase\":\"fix\",\"load\":[\"systematic-debugging\",\"master-engineer\",\"test-driven-development\",\"clean-code\"]},{\"phase\":\"verify\",\"load\":[\"clean-code\",\"production-code-quality-baseline\"]},{\"phase\":\"review\",\"load\":[\"architecture-review\",\"code-review-workflow\"]}]'",
    )
    replace_once(
        path,
        "  ai-native-skills.skills: '{\"required\":[\"systematic-debugging\",\"architecture-review\"],\"optional\":[\"implementation-context-discovery\",\"master-engineer\"]}'",
        "  ai-native-skills.skills: '{\"required\":[\"production-code-quality-baseline\",\"systematic-debugging\",\"test-driven-development\",\"clean-code\",\"architecture-review\",\"code-review-workflow\"],\"optional\":[\"implementation-context-discovery\",\"master-engineer\",\"security-review\"]}'",
    )
    replace_once(
        path,
        "  ai-native-skills.related_skills: '[\"implementation-context-discovery\",\"architecture-review\",\"test-driven-development\",\"decision-provenance\"]'",
        "  ai-native-skills.related_skills: '[\"production-code-quality-baseline\",\"implementation-context-discovery\",\"architecture-review\",\"code-review-workflow\",\"test-driven-development\",\"clean-code\",\"decision-provenance\"]'",
    )
    replace_once(
        path,
        """reproduce
→ investigate root cause
→ classify implementation-context impact
→ discover and lock repository conventions when material
→ regression test and smallest root-cause fix
→ verify
→ submit
→ independent architecture review and approval""",
        """reproduce and record RED evidence
→ attach production-code-quality-baseline
→ investigate root cause
→ classify implementation-context and conditional quality impact
→ discover and lock repository conventions when material
→ smallest root-cause fix with TDD and clean-code
→ verify claims, evidence, and baseline gates
→ submit
→ independent architecture review and code review
→ separate merge authorization""",
    )
    replace_once(
        path,
        "10. Architecture review remains independent after implementation.",
        """10. Architecture review remains independent after implementation.
11. Attach `production-code-quality-baseline` because a production bugfix changes existing behavior.
12. `test-driven-development` owns RED → minimal GREEN → refactor while green; final green tests do not prove test-first ordering.
13. Apply `clean-code` to the materially changed implementation without unrelated cleanup.
14. Classify SOLID, DDD, patterns, Clean Architecture, security, performance, resilience, observability, data, and design concerns; load specialists only when justified.
15. Run `code-review-workflow` after architecture review; technical review does not create merge authorization.""",
    )
    replace_once(
        path,
        """| Investigate | `systematic-debugging` | required |
| Pre-fix context | `implementation-context-discovery` | conditional when material repository conventions are affected |
| Fix | `systematic-debugging`; `master-engineer` when needed | required / conditional |
| Review | `architecture-review` | required |""",
        """| Reproduce/plan | `production-code-quality-baseline`, `test-driven-development` | required |
| Investigate | `systematic-debugging` | required |
| Pre-fix context | `implementation-context-discovery` | conditional when material repository conventions are affected |
| Fix | `systematic-debugging`, `master-engineer`, `test-driven-development`, `clean-code` | required / conditional owner |
| Verify | `clean-code`, `production-code-quality-baseline` | required |
| Review | `architecture-review`, `code-review-workflow` | required |""",
    )
    replace_once(
        path,
        "1. Write a regression test that reproduces the bug (`RED`).",
        "1. Load `production-code-quality-baseline`, `test-driven-development`, and `clean-code`; write a regression test that reproduces the bug (`RED`) and preserve ordering evidence.",
    )
    replace_once(
        path,
        "absence of prohibited parallel systems",
        """absence of prohibited parallel systems
clean-code assessment and behavior-change risk
production-code quality claims, evidence, gate results, and blocking gaps""",
    )
    replace_once(
        path,
        "Load `architecture-review`. Verify the actual diff against the engineering contract and discovered implementation context. Compilation or a green regression test is not architecture approval.",
        "Load `architecture-review`, then `code-review-workflow`. Verify the actual diff against the engineering contract, quality-baseline report, and discovered implementation context. Compilation or a green regression test is not architecture approval, and technical review does not create merge authorization.",
    )
    replace_once(
        path,
        "| Review | Independent approval | Approved and authorized for merge |",
        "| Review | Independent architecture and code review | Technical verdict recorded; separate merge authority still required |",
    )


def patch_spec() -> None:
    path = "skills/spec-workflow/SKILL.md"
    replace_once(path, "  ai-native-skills.version: 1.0.0", "  ai-native-skills.version: 1.1.0")
    replace_once(
        path,
        "  ai-native-skills.type: workflow\n",
        "  ai-native-skills.type: workflow\n  ai-native-skills.requires: \"product-manager plan context-manager rule-manager master-engineer native-ai-engineer test-driven-development clean-code production-code-quality-baseline\"\n",
    )
    replace_once(
        path,
        "  ai-native-skills.skill_load_order: '[{''phase'': ''constitution'', ''load'': [''native-ai-engineer'', ''master-engineer'']}, {''phase'': ''specify'', ''load'': [''product-manager'']}, {''phase'': ''plan'', ''load'': [''plan'']}, {''phase'': ''tasks'', ''load'': [''context-manager'', ''rule-manager'']}, {''phase'': ''implement'', ''load'': [''master-engineer'', ''test-driven-development'']}]'",
        "  ai-native-skills.skill_load_order: '[{''phase'': ''constitution'', ''load'': [''native-ai-engineer'', ''master-engineer'']}, {''phase'': ''specify'', ''load'': [''product-manager'']}, {''phase'': ''plan'', ''load'': [''plan'']}, {''phase'': ''tasks'', ''load'': [''context-manager'', ''rule-manager'']}, {''phase'': ''implement'', ''load'': [''production-code-quality-baseline'', ''master-engineer'', ''test-driven-development'', ''clean-code'']}]'",
    )
    replace_once(
        path,
        "  ai-native-skills.skills: '{''required'': [''product-manager'', ''plan'', ''context-manager'', ''rule-manager'', ''master-engineer'', ''native-ai-engineer''], ''optional'': [''test-driven-development'', ''spike'', ''diagram-architect'']}'",
        "  ai-native-skills.skills: '{''required'': [''product-manager'', ''plan'', ''context-manager'', ''rule-manager'', ''master-engineer'', ''native-ai-engineer'', ''production-code-quality-baseline'', ''test-driven-development'', ''clean-code''], ''optional'': [''spike'', ''diagram-architect'']}'",
    )
    replace_once(
        path,
        "No implementation starts without a spec.\nNo spec is valid without testable acceptance criteria.",
        """No implementation starts without a spec.
No spec is valid without testable acceptance criteria.
Production-code implementation attaches production-code-quality-baseline.
TDD is the default; an exception requires attributable authority and alternative verification.""",
    )
    replace_once(
        path,
        "Load `master-engineer` + `test-driven-development`.",
        "Load `production-code-quality-baseline`, `master-engineer`, `test-driven-development`, and `clean-code` for tasks classified as production-code changes.",
    )
    replace_once(
        path,
        "2. Write test first (if TDD applies)\n3. Implement to make test pass",
        """2. Record the failing behavior and RED evidence before implementation; when TDD cannot validly apply, stop for an attributable authorized exception with alternative verification
3. Implement the smallest change to make the test pass and record GREEN evidence""",
    )
    replace_once(
        path,
        "**Done when:** All tasks complete, all ACs satisfied, no scope drift.",
        "**Done when:** All tasks complete, all ACs are satisfied, no scope drift exists, and the production-code quality baseline exposes evidence, gate results, reviews, and remaining authority honestly.",
    )
    replace_once(
        path,
        "| **5. Implement** | `master-engineer`, `test-driven-development` | No scope drift |",
        "| **5. Implement** | `production-code-quality-baseline`, `master-engineer`, `test-driven-development`, `clean-code` | No scope drift; quality evidence and authority boundaries explicit |",
    )


def patch_new_feature() -> None:
    path = "skills/new-feature-workflow/SKILL.md"
    replace_once(path, "  ai-native-skills.version: 2.4.0", "  ai-native-skills.version: 2.5.0")
    replace_once(
        path,
        '  ai-native-skills.requires: "master-engineer master-design delivery-work-breakdown implementation-context-discovery decision-provenance spec-workflow clean-architecture solid-design clean-code test-driven-development architecture-review code-review-workflow design-review"',
        '  ai-native-skills.requires: "master-engineer master-design delivery-work-breakdown implementation-context-discovery decision-provenance spec-workflow production-code-quality-baseline clean-architecture solid-design clean-code test-driven-development architecture-review code-review-workflow design-review"',
    )
    replace_once(
        path,
        "  ai-native-skills.skill_load_order: '[{\"phase\":\"plan\",\"load\":[\"master-engineer\",\"decision-provenance\"]},{\"phase\":\"delivery-topology\",\"load\":[\"delivery-work-breakdown\",\"decision-provenance\"]},{\"phase\":\"design-decision\",\"load\":[\"master-engineer\",\"clean-architecture\",\"solid-design\",\"diagram-architect\",\"master-design\",\"decision-provenance\"]},{\"phase\":\"implementation-context\",\"load\":[\"implementation-context-discovery\",\"decision-provenance\"]},{\"phase\":\"implement\",\"load\":[\"master-engineer\",\"clean-code\",\"solid-design\",\"test-driven-development\"]},{\"phase\":\"verify\",\"load\":[\"clean-code\",\"solid-design\",\"architecture-review\",\"design-review\",\"decision-provenance\"]},{\"phase\":\"submit\",\"load\":[\"decision-provenance\"]},{\"phase\":\"review\",\"load\":[\"code-review-workflow\"]}]'",
        "  ai-native-skills.skill_load_order: '[{\"phase\":\"plan\",\"load\":[\"production-code-quality-baseline\",\"master-engineer\",\"decision-provenance\"]},{\"phase\":\"delivery-topology\",\"load\":[\"delivery-work-breakdown\",\"decision-provenance\"]},{\"phase\":\"design-decision\",\"load\":[\"master-engineer\",\"clean-architecture\",\"solid-design\",\"diagram-architect\",\"master-design\",\"decision-provenance\"]},{\"phase\":\"implementation-context\",\"load\":[\"implementation-context-discovery\",\"decision-provenance\"]},{\"phase\":\"implement\",\"load\":[\"production-code-quality-baseline\",\"master-engineer\",\"clean-code\",\"solid-design\",\"test-driven-development\"]},{\"phase\":\"verify\",\"load\":[\"production-code-quality-baseline\",\"clean-code\",\"solid-design\",\"architecture-review\",\"design-review\",\"decision-provenance\"]},{\"phase\":\"submit\",\"load\":[\"decision-provenance\"]},{\"phase\":\"review\",\"load\":[\"code-review-workflow\"]}]'",
    )
    replace_once(
        path,
        "  ai-native-skills.skills: '{\"required\":[\"master-engineer\",\"delivery-work-breakdown\",\"implementation-context-discovery\",\"decision-provenance\",\"clean-code\",\"test-driven-development\",\"architecture-review\",\"code-review-workflow\"],\"optional\":[\"clean-architecture\",\"solid-design\",\"diagram-architect\",\"master-design\",\"design-review\"]}'",
        "  ai-native-skills.skills: '{\"required\":[\"production-code-quality-baseline\",\"master-engineer\",\"delivery-work-breakdown\",\"implementation-context-discovery\",\"decision-provenance\",\"clean-code\",\"test-driven-development\",\"architecture-review\",\"code-review-workflow\"],\"optional\":[\"clean-architecture\",\"solid-design\",\"diagram-architect\",\"master-design\",\"design-review\"]}'",
    )
    replace_once(
        path,
        "verified scope\n→ approved delivery topology",
        "verified scope\n→ production-code-quality-baseline attachment and applicability map\n→ approved delivery topology",
    )
    replace_once(
        path,
        "24. Pre-implementation engineering design guidance never self-approves the implemented architecture or code quality.",
        """24. Pre-implementation engineering design guidance never self-approves the implemented architecture or code quality.
25. Attach `production-code-quality-baseline` for the production implementation slice; it remains an overlay and never replaces this lifecycle.
26. Record RED-before-GREEN evidence or an attributable authorized exception; final green tests alone do not prove TDD.
27. Classify conditional quality concerns before loading specialists, and preserve `NOT_APPLICABLE`, `NOT_JUSTIFIED`, and `NOT_VERIFIED` honestly.""",
    )
    replace_once(
        path,
        "Load `master-engineer`, `clean-code`, and `test-driven-development`. Load `solid-design` only when the approved implementation materially changes class/module/service ownership, extension seams, substitution contracts, client interfaces, or policy/detail dependency relationships.",
        "Load `production-code-quality-baseline`, `master-engineer`, `clean-code`, and `test-driven-development`. Load `solid-design` only when the applicability map and approved implementation materially change class/module/service ownership, extension seams, substitution contracts, client interfaces, or policy/detail dependency relationships.",
    )
    replace_once(
        path,
        "solid-design assessment when materially applicable\nclean-architecture decision trace when architecture-style or boundary design was material",
        """solid-design assessment when materially applicable
production-code baseline claims, executed-capability refs, evidence, gate results, and blocking gaps
clean-architecture decision trace when architecture-style or boundary design was material""",
    )


def patch_docs_and_catalog() -> None:
    replace_once("README.md", "**91 skills · 10 workflows · 6 meta-skills**", "**91 skills · 11 workflows · 6 meta-skills**")
    replace_once(
        "README.md",
        """Engineering quality
  implementation-context-discovery when convention evidence is material
  → architecture-review → security-review → code-review-workflow → skill-eval""",
        """Engineering quality
  workflow-router classifies production impact
  → one primary lifecycle + production-code-quality-baseline overlay
  → implementation-context-discovery when convention evidence is material
  → TDD + clean-code + justified conditional specialists
  → architecture-review → code-review-workflow → remaining merge authority""",
    )
    replace_once("docs/skills.md", "- `workflow`: 10", "- `workflow`: 11")
    replace_once("docs/skills.md", "- Total executable skills: 107", "- Total executable skills: 108")
    replace_once(
        "docs/skills.md",
        "| `product-development-workflow` | discovery → PRD → MVP/release-unit decomposition → spec → implementation → verification → release → deploy → launch → learn |",
        """| `product-development-workflow` | discovery → PRD → MVP/release-unit decomposition → spec → implementation → verification → release → deploy → launch → learn |
| `production-code-quality-baseline` | classify production impact → attach to one primary lifecycle → plan TDD/quality applicability → execute → verify claims/evidence → independent review → authority handoff |""",
    )
    replace_once(
        "docs/skills.md",
        "A platform, repository, or continuity specialist normally overlays an existing lifecycle rather than replacing it.",
        "A platform, repository, continuity, or production-code quality specialist normally overlays an existing lifecycle rather than replacing it.",
    )

    classifications_path = ROOT / "catalog/capability-discovery/classifications.json"
    classifications = json.loads(classifications_path.read_text(encoding="utf-8"))
    groups = {group["id"]: group for group in classifications["classification_groups"]}
    workflows = groups["workflows"]
    capability = "production-code-quality-baseline"
    if capability in workflows["capabilities"]:
        raise RuntimeError("classifications.json: capability already present")
    workflows["capabilities"].append(capability)
    workflows["capabilities"].sort()
    workflows.setdefault("overrides", {})[capability] = {
        "domains": ["engineering", "quality", "governance"],
        "lifecycle_stages": ["plan", "build", "verify", "release"],
        "concerns": [
            "workflow-routing",
            "implementation",
            "testing",
            "code-quality",
            "review",
            "governance",
        ],
    }
    classifications_path.write_text(
        json.dumps(classifications, separators=(",", ":")) + "\n", encoding="utf-8"
    )

    profiles_path = ROOT / "catalog/capability-discovery/job-profiles.json"
    profiles = json.loads(profiles_path.read_text(encoding="utf-8"))
    engineering = next(profile for profile in profiles["job_profiles"] if profile["id"] == "engineering-quality")
    engineering["workflow_routes"].insert(
        0,
        {
            "when": "Any substantive production-code lifecycle needs default cross-workflow quality obligations.",
            "workflow": capability,
        },
    )
    route_group = engineering["capability_groups"][0]
    if capability in route_group["required"]:
        raise RuntimeError("job-profiles.json: capability already required")
    route_group["required"].append(capability)
    route_group["required"].sort()
    engineering["expected_evidence"].insert(
        1,
        "An explicit production-code applicability verdict and evidence-backed conditional quality map.",
    )
    profiles_path.write_text(json.dumps(profiles, separators=(",", ":")) + "\n", encoding="utf-8")


def main() -> int:
    patch_router()
    patch_bugfix()
    patch_spec()
    patch_new_feature()
    patch_docs_and_catalog()
    print("PASS — issue #137 production-code quality migration applied with exact source assertions.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
