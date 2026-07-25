#!/usr/bin/env python3
"""Apply issue #137 review, eval-version, and pack integration with exact assertions."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace_once(path: str, old: str, new: str) -> None:
    target = ROOT / path
    source = target.read_text(encoding="utf-8")
    count = source.count(old)
    if count != 1:
        raise RuntimeError(f"{path}: expected one match, found {count}: {old[:120]!r}")
    target.write_text(source.replace(old, new, 1), encoding="utf-8")


def append_once(path: str, marker: str, content: str) -> None:
    target = ROOT / path
    source = target.read_text(encoding="utf-8")
    if marker in source:
        raise RuntimeError(f"{path}: marker already present: {marker}")
    target.write_text(source.rstrip() + "\n\n" + content.rstrip() + "\n", encoding="utf-8")


def sync_eval_versions() -> None:
    replace_once(
        "contracts/tests/workflow-router.test.yaml",
        "  version: 1.6.0",
        "  version: 1.7.0",
    )
    replace_once(
        "contracts/tests/new-feature-workflow.test.yaml",
        '  version: "2.4.0"',
        '  version: "2.5.0"',
    )
    replace_once(
        "contracts/tests/bugfix-workflow.test.yaml",
        '  version: "1.1.0"',
        '  version: "1.2.0"',
    )
    replace_once(
        "contracts/tests/code-review-workflow.test.yaml",
        '  version: "2.2.0"',
        '  version: "2.3.0"',
    )


def patch_code_review() -> None:
    path = "skills/code-review-workflow/SKILL.md"
    replace_once(path, "  ai-native-skills.version: 2.2.0", "  ai-native-skills.version: 2.3.0")
    replace_once(
        path,
        '  ai-native-skills.requires: "architecture-review clean-architecture clean-code solid-design design-review decision-provenance master-engineer systematic-debugging security-review threat-modeling"',
        '  ai-native-skills.requires: "architecture-review clean-architecture clean-code solid-design design-review decision-provenance master-engineer systematic-debugging security-review threat-modeling production-code-quality-baseline"',
    )
    replace_once(
        path,
        "  ai-native-skills.skills: '{\"required\":[\"architecture-review\",\"decision-provenance\",\"clean-code\"],\"optional\":[\"clean-architecture\",\"solid-design\",\"design-review\",\"systematic-debugging\",\"master-engineer\",\"security-review\",\"threat-modeling\"]}'",
        "  ai-native-skills.skills: '{\"required\":[\"architecture-review\",\"decision-provenance\",\"clean-code\"],\"optional\":[\"production-code-quality-baseline\",\"clean-architecture\",\"solid-design\",\"design-review\",\"systematic-debugging\",\"master-engineer\",\"security-review\",\"threat-modeling\"]}'",
    )
    replace_once(
        path,
        "20. Do not force SOLID or Clean Architecture ceremony into changes where applicability is `NOT_APPLICABLE` or `NOT_JUSTIFIED`.",
        """20. Do not force SOLID or Clean Architecture ceremony into changes where applicability is `NOT_APPLICABLE` or `NOT_JUSTIFIED`.
21. For production-code submissions, consume the `production-code-quality-baseline` report when available; do not re-run or replace the primary lifecycle.
22. Distinguish capabilities resolved, executed, evidenced, and reviewed; a capability list is not proof of execution.
23. Missing TDD ordering, clean-code, module/failure-path, conditional-applicability, or baseline gate evidence remains `NOT_VERIFIED` and may require changes.
24. Use `references/production-code-quality-baseline.md` and preserve all approval, merge, delivery, and product-acceptance boundaries.""",
    )
    replace_once(
        path,
        """    accessibility: []

  approval_policy: <product-defined>""",
        """    accessibility: []

  engineering_quality_baseline:
    report: <reference | missing | not-applicable>
    primary_lifecycle: <workflow | unknown>
    applicability_map: {}
    capabilities_resolved: []
    capabilities_executed: []
    tdd_evidence: []
    gate_results: []
    blocking_gaps: []
    remaining_authorities: []

  approval_policy: <product-defined>""",
    )
    replace_once(
        path,
        "verification evidence attached to the submission",
        """verification evidence attached to the submission
production-code quality baseline report and capability execution/evidence refs when applicable""",
    )
    replace_once(
        path,
        """  artifact_state: <rendered-interactive | rendered-static | source-only | mixed | N/A>
  required_reviewers: []""",
        """  artifact_state: <rendered-interactive | rendered-static | source-only | mixed | N/A>
  production_code_applicability: <status>
  quality_baseline_report: <present | partial | missing | not-applicable>
  tdd_ordering_evidence: <pass | authorized-exception | needs-work | not-verified | not-applicable>
  conditional_quality_map: <pass | needs-work | not-verified | not-applicable>
  required_reviewers: []""",
    )
    replace_once(
        path,
        "**Gate:** affected domains, reviewers, material claims, and required authorities are resolved.",
        """**Gate:** affected domains, reviewers, material claims, and required authorities are resolved.

For a production-code submission, load `references/production-code-quality-baseline.md`.
A missing or partial baseline is an evidence classification, not automatic proof of failure or
success. Reconstruct only what current evidence can support; never invent RED-before-GREEN
history. Mandatory unsupported claims remain `NOT_VERIFIED`, `REQUEST CHANGES`, or `BLOCKED`
according to materiality and safety.""",
    )
    replace_once(
        path,
        "Run `clean-code` when materially changed hand-written or generated implementation affects readability, maintainability, control flow, errors, duplication, local contracts, or test readability.",
        "Run `clean-code` when materially changed hand-written or generated implementation affects readability, maintainability, control flow, errors, duplication, local contracts, or test readability. Consume the submitted baseline findings as evidence inputs, then independently verify them against the actual diff and repository state.",
    )
    replace_once(
        path,
        """## Domain Results
- Architecture: [result]""",
        """## Production-Code Quality Baseline
- Production-code applicability: [status]
- Primary lifecycle and overlay consistency: [result]
- Baseline report: [present | partial | missing | N/A]
- Capabilities resolved/executed/evidenced: [result]
- TDD ordering or authorized exception: [result]
- Clean-code and module/failure-path result: [result]
- Conditional applicability map: [result]
- Mandatory gate result: [result]
- Blocking gaps: [...]
- Remaining authorities: [...]

## Domain Results
- Architecture: [result]""",
    )

    append_once(
        "contracts/tests/code-review-workflow.test.yaml",
        "resolved-baseline-capabilities-without-execution-evidence",
        """    - id: resolved-baseline-capabilities-without-execution-evidence
      description: A production-code baseline that lists selected capabilities without execution outputs or evidence cannot support technical approval.
      trigger: "Review this production PR. Its quality report lists TDD, clean-code, SOLID, and architecture-review as resolved, but contains no execution records, RED/GREEN ordering evidence, outputs, or reviewer results."
      must_contain: ["quality baseline", "capabilities resolved", "capabilities executed", "NOT_VERIFIED", "REQUEST CHANGES"]
      must_not_contain: ["Technical review: APPROVED", "Approved to merge: YES", "resolved capability proves execution"]
      quality_gates_tested: ["quality_baseline_evidence_required", "capability_resolution_is_not_execution", "technical_approval_requires_domain_evidence"]""",
    )


def patch_baseline_references_and_eval() -> None:
    replace_once(
        "skills/production-code-quality-baseline/SKILL.md",
        "The overlay coordinates existing capabilities. It does not absorb their methods or replace their ownership.",
        """The overlay coordinates existing capabilities. It does not absorb their methods or replace their ownership.

Use `references/evidence-status-authority-matrix.md` when producing applicability,
capability-state, evidence, gate, review, or transition results.""",
    )
    append_once(
        "contracts/tests/production-code-quality-baseline.test.yaml",
        "spec-production-implementation-removes-optional-tdd-ambiguity",
        """  - id: spec-production-implementation-removes-optional-tdd-ambiguity
    description: A spec-driven production implementation must attach the baseline and use TDD unless an attributable exception exists.
    trigger: The specification and acceptance criteria are complete. Implement the production task, but treat TDD as optional because the spec workflow used to say "if TDD applies".
    must_contain:
    - spec-workflow
    - production-code-quality-baseline
    - RED evidence
    - GREEN evidence
    - authorized exception
    must_not_contain:
    - if TDD applies
    - skip test-first without authority
    - test later and call it TDD
    quality_gates_tested:
    - spec_production_implementation_attaches_quality_baseline
    - tdd_red_green_refactor_required_or_authorized_exception_with_evidence""",
    )


def patch_pack_docs() -> None:
    path = "docs/skill-packs.md"
    replace_once(
        path,
        """  --skill new-feature-workflow \\
  --skill master-engineer""",
        """  --skill new-feature-workflow \\
  --skill production-code-quality-baseline \\
  --skill master-engineer""",
    )
    replace_once(
        path,
        """  --skill test-driven-development \\
  --skill architecture-review""",
        """  --skill test-driven-development \\
  --skill clean-code \\
  --skill architecture-review""",
    )
    replace_once(
        path,
        """## Identity Review Pack""",
        """## Bugfix Delivery Pack

Root-cause repair with explicit RED-before-GREEN evidence, repository-context mapping when material, clean-code and module/failure-path assessment, independent architecture and code review, and separate merge authorization.

```bash
npx skills add puterakahfi/ai-native-skills \\
  --skill bugfix-workflow \\
  --skill production-code-quality-baseline \\
  --skill systematic-debugging \\
  --skill implementation-context-discovery \\
  --skill master-engineer \\
  --skill test-driven-development \\
  --skill clean-code \\
  --skill architecture-review \\
  --skill code-review-workflow \\
  --skill security-review \\
  -g -y
```

---

## Identity Review Pack""",
    )
    replace_once(
        path,
        """  --skill new-feature-workflow \\
  --skill design-review \\
  --skill threat-modeling""",
        """  --skill new-feature-workflow \\
  --skill production-code-quality-baseline \\
  --skill test-driven-development \\
  --skill clean-code \\
  --skill design-review \\
  --skill threat-modeling""",
    )
    replace_once(
        path,
        """  --skill new-feature-workflow \\
  --skill test-driven-development \\
  --skill design-review""",
        """  --skill new-feature-workflow \\
  --skill production-code-quality-baseline \\
  --skill test-driven-development \\
  --skill clean-code \\
  --skill design-review""",
    )
    replace_once(
        path,
        """## Engineering Quality Pack

Architecture and implementation quality loop — repository-context mapping, pragmatic architecture and object-design decisions, internal code quality, testing, debugging, behavior-preserving refactoring, independent architecture/security/code review, and technical-debt governance.

```bash
npx skills add puterakahfi/ai-native-skills \\
  --skill implementation-context-discovery \\""",
        """## Engineering Quality Pack

Default cross-workflow production-code quality overlay plus repository-context mapping, pragmatic architecture and object-design decisions, internal code quality, testing, debugging, behavior-preserving refactoring, independent architecture/security/code review, and technical-debt governance.

```bash
npx skills add puterakahfi/ai-native-skills \\
  --skill production-code-quality-baseline \\
  --skill implementation-context-discovery \\""",
    )
    replace_once(
        path,
        "`clean-code` is the baseline implementation-quality lens.",
        "`production-code-quality-baseline` coordinates applicability, execution evidence, gate results, and authority handoff across the governing lifecycle. `clean-code` remains the baseline implementation-quality lens.",
    )

    hermes = "skills/hermes-profile-bootstrap/references/skill-packs.md"
    replace_once(
        hermes,
        """new-feature-workflow
bugfix-workflow
code-review-workflow""",
        """new-feature-workflow
bugfix-workflow
production-code-quality-baseline
code-review-workflow""",
    )
    replace_once(
        hermes,
        """systematic-debugging
test-driven-development
refactoring""",
        """implementation-context-discovery
master-engineer
production-code-quality-baseline
systematic-debugging
test-driven-development
clean-code
solid-design
clean-architecture
refactoring""",
    )


def main() -> int:
    sync_eval_versions()
    patch_code_review()
    patch_baseline_references_and_eval()
    patch_pack_docs()
    print("PASS — review, eval-version, reference, and pack migration applied.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
