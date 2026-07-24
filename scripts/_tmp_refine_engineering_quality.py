#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one match, found {count}")
    return text.replace(old, new, 1)


# ---------------------------------------------------------------------------
# code-review-workflow
# ---------------------------------------------------------------------------
path = ROOT / "skills/code-review-workflow/SKILL.md"
text = path.read_text(encoding="utf-8")
text = replace_once(text, "ai-native-skills.version: 2.1.0", "ai-native-skills.version: 2.2.0", "code review version")
text = replace_once(
    text,
    'description: Evidence-backed code review workflow — classify changed domains, verify architecture, route user-facing changes through the design-review facade, inspect logic and security, then separate technical approval from provenance-backed merge authorization.',
    'description: Evidence-backed code review workflow — classify changed domains, verify architecture, route user-facing changes through design review, assess internal code and object/module design quality, inspect logic and security, then separate technical approval from provenance-backed merge authorization.',
    "code review description",
)
text = replace_once(
    text,
    'ai-native-skills.requires: "architecture-review design-review decision-provenance master-engineer systematic-debugging security-review threat-modeling"',
    'ai-native-skills.requires: "architecture-review clean-architecture clean-code solid-design design-review decision-provenance master-engineer systematic-debugging security-review threat-modeling"',
    "code review requires",
)
text = replace_once(
    text,
    'ai-native-skills.skill_load_order: \'[{"phase":"load-context","load":["decision-provenance"]},{"phase":"architecture-check","load":["architecture-review"]},{"phase":"design-check","load":["design-review"]},{"phase":"logic-check","load":["systematic-debugging","master-engineer"]},{"phase":"security-check","load":["security-review","threat-modeling"]},{"phase":"verdict","load":["decision-provenance"]}]\'',
    'ai-native-skills.skill_load_order: \'[{"phase":"load-context","load":["decision-provenance"]},{"phase":"architecture-check","load":["architecture-review","clean-architecture"]},{"phase":"design-check","load":["design-review"]},{"phase":"code-design-quality","load":["clean-code","solid-design"]},{"phase":"logic-check","load":["systematic-debugging","master-engineer"]},{"phase":"security-check","load":["security-review","threat-modeling"]},{"phase":"verdict","load":["decision-provenance"]}]\'',
    "code review load order",
)
text = replace_once(
    text,
    'ai-native-skills.skills: \'{"required":["architecture-review","decision-provenance"],"optional":["design-review","systematic-debugging","master-engineer","security-review","threat-modeling"]}\'',
    'ai-native-skills.skills: \'{"required":["architecture-review","decision-provenance","clean-code"],"optional":["clean-architecture","solid-design","design-review","systematic-debugging","master-engineer","security-review","threat-modeling"]}\'',
    "code review skills",
)
text = replace_once(
    text,
    "Load context → classify changes and decision claims → architecture → design acceptance → logic → security → technical verdict → merge authorization.",
    "Load context → classify changes and decision claims → architecture → design acceptance → internal code/object quality → logic → security → technical verdict → merge authorization.",
    "code review flow",
)
text = replace_once(
    text,
    "16. No merge without explicit technical approval and merge authorization.\n",
    "16. No merge without explicit technical approval and merge authorization.\n17. Run `clean-code` for materially changed implementation; lint, formatting, compilation, and green tests are not clean-code approval.\n18. Run `solid-design` only when responsibility, variation, substitution, client-interface, or dependency relationships are materially affected.\n19. Use `clean-architecture` as an architecture-style or policy/mechanism specialist only when that decision is material; `architecture-review` remains the acceptance gate.\n20. Do not force SOLID or Clean Architecture ceremony into changes where applicability is `NOT_APPLICABLE` or `NOT_JUSTIFIED`.\n",
    "code review hard rules",
)
text = replace_once(
    text,
    "  architecture: <none | affected>\n  logic: <none | affected>",
    "  architecture: <none | affected>\n  architecture_style_or_boundary_design: <none | affected>\n  internal_code_quality: <none | affected>\n  object_module_design: <none | affected>\n  logic: <none | affected>",
    "code review impact fields",
)
text = replace_once(
    text,
    "Load `architecture-review`.\n",
    "Load `architecture-review`. Load `clean-architecture` only when the submission materially changes or claims an architecture style, policy/mechanism boundary, dependency rule, use-case boundary, or broad architecture migration. `clean-architecture` supplies applicability and boundary reasoning; it does not replace the independent architecture verdict.\n",
    "architecture specialist guidance",
)
quality_phase = """## Phase 5 — Internal code and object/module design quality

Run `clean-code` when materially changed hand-written or generated implementation affects readability, maintainability, control flow, errors, duplication, local contracts, or test readability.

Run `solid-design` only when the change materially affects:

```text
class/module/service responsibility and ownership
proven variation or extension seams
inheritance, substitution, or implementation contracts
client-specific interface shape
stable-policy versus volatile-detail dependency direction
an explicit SOLID or abstraction claim
```

Inspect:

```text
repository vocabulary and conventions
readability and working-memory load
control flow, errors, comments, and duplicated knowledge
cohesive ownership and reasons to change
behavioral substitutability rather than type compatibility alone
actual client needs rather than interface-size dogma
abstraction benefit versus new indirection
behavior-change risk and required tests
```

Do not fail a submission from arbitrary line, method, parameter, or class-size limits. Do not approve internal quality merely because formatters, linters, compilation, or tests pass.

Output:

```text
Code quality: PASS | PASS WITH FLAGS | NEEDS WORK | NOT_VERIFIED | N/A
Object/module design: PASS | PASS WITH FLAGS | NEEDS WORK | NOT_VERIFIED | N/A
```

A verified blocking code-quality or object-design issue prevents technical approval. `NOT_APPLICABLE` or `NOT_JUSTIFIED` specialist conclusions must not be converted into invented work.

**Gate:** local implementation quality and materially applicable object/module design are resolved without duplicating architecture acceptance or refactoring ownership.

## Phase 6 — Logic check
"""
text = replace_once(text, "## Phase 5 — Logic check\n", quality_phase, "insert code quality phase")
text = replace_once(text, "## Phase 6 — Security check", "## Phase 7 — Security check", "renumber security")
text = replace_once(text, "## Phase 7 — Technical verdict and merge authorization", "## Phase 8 — Technical verdict and merge authorization", "renumber verdict")
text = replace_once(
    text,
    "correctable architecture, design, logic, security, test,\n",
    "correctable architecture, design, code-quality, object-design, logic, security, test,\n",
    "verdict domain list",
)
text = replace_once(
    text,
    "- Architecture: [affected/none]\n- Logic: [affected/none]",
    "- Architecture: [affected/none]\n- Architecture style/boundary design: [affected/none]\n- Internal code quality: [affected/none]\n- Object/module design: [affected/none]\n- Logic: [affected/none]",
    "report classifications",
)
text = replace_once(
    text,
    "- Architecture: [result]\n- Design: [facade verdict, evidence coverage, primary-domain coverage]\n- Logic: [result]",
    "- Architecture: [result]\n- Clean Architecture specialist: [applicability/boundary decision or N/A]\n- Design: [facade verdict, evidence coverage, primary-domain coverage]\n- Code quality: [clean-code verdict/findings/gaps]\n- Object/module design: [solid-design verdict/findings/gaps or N/A]\n- Logic: [result]",
    "report domain results",
)
text += "\n| Treat lint, formatting, or green tests as clean-code approval | Tools prove selected checks, not readability or maintainability |\n| Run SOLID on every local edit | Specialist applicability and concrete change pressure are missing |\n| Require fixed Clean Architecture layers during review | Architecture-style dogma bypasses repository context and applicability |\n"
path.write_text(text, encoding="utf-8")

# ---------------------------------------------------------------------------
# new-feature-workflow
# ---------------------------------------------------------------------------
path = ROOT / "skills/new-feature-workflow/SKILL.md"
text = path.read_text(encoding="utf-8")
text = replace_once(text, "ai-native-skills.version: 2.3.0", "ai-native-skills.version: 2.4.0", "new feature version")
text = replace_once(
    text,
    'ai-native-skills.requires: "master-engineer master-design delivery-work-breakdown implementation-context-discovery decision-provenance spec-workflow test-driven-development architecture-review code-review-workflow design-review"',
    'ai-native-skills.requires: "master-engineer master-design delivery-work-breakdown implementation-context-discovery decision-provenance spec-workflow clean-architecture solid-design clean-code test-driven-development architecture-review code-review-workflow design-review"',
    "new feature requires",
)
text = replace_once(
    text,
    'ai-native-skills.skill_load_order: \'[{"phase":"plan","load":["master-engineer","decision-provenance"]},{"phase":"delivery-topology","load":["delivery-work-breakdown","decision-provenance"]},{"phase":"design-decision","load":["master-engineer","diagram-architect","master-design","decision-provenance"]},{"phase":"implementation-context","load":["implementation-context-discovery","decision-provenance"]},{"phase":"implement","load":["master-engineer","test-driven-development"]},{"phase":"verify","load":["architecture-review","design-review","decision-provenance"]},{"phase":"submit","load":["decision-provenance"]},{"phase":"review","load":["code-review-workflow"]}]\'',
    'ai-native-skills.skill_load_order: \'[{"phase":"plan","load":["master-engineer","decision-provenance"]},{"phase":"delivery-topology","load":["delivery-work-breakdown","decision-provenance"]},{"phase":"design-decision","load":["master-engineer","clean-architecture","solid-design","diagram-architect","master-design","decision-provenance"]},{"phase":"implementation-context","load":["implementation-context-discovery","decision-provenance"]},{"phase":"implement","load":["master-engineer","clean-code","solid-design","test-driven-development"]},{"phase":"verify","load":["clean-code","solid-design","architecture-review","design-review","decision-provenance"]},{"phase":"submit","load":["decision-provenance"]},{"phase":"review","load":["code-review-workflow"]}]\'',
    "new feature load order",
)
text = replace_once(
    text,
    'ai-native-skills.skills: \'{"required":["master-engineer","delivery-work-breakdown","implementation-context-discovery","decision-provenance","test-driven-development","architecture-review","code-review-workflow"],"optional":["diagram-architect","master-design","design-review"]}\'',
    'ai-native-skills.skills: \'{"required":["master-engineer","delivery-work-breakdown","implementation-context-discovery","decision-provenance","clean-code","test-driven-development","architecture-review","code-review-workflow"],"optional":["clean-architecture","solid-design","diagram-architect","master-design","design-review"]}\'',
    "new feature skills",
)
text = replace_once(
    text,
    "20. Do not bundle unrelated, unapproved, or opportunistic migration work.\n",
    "20. Do not bundle unrelated, unapproved, or opportunistic migration work.\n21. Use `clean-architecture` only when architecture-style or policy/mechanism boundaries are materially affected and justified by forces.\n22. Use `solid-design` only when responsibility, extension, substitution, client-interface, or dependency design is material.\n23. Apply `clean-code` during implementation and verification without arbitrary size metrics or behavior-changing cleanup.\n24. Pre-implementation engineering design guidance never self-approves the implemented architecture or code quality.\n",
    "new feature hard rules",
)
text = replace_once(
    text,
    "    architecture: <true | false>\n    logic: <true | false>",
    "    architecture: <true | false>\n    architecture_style_or_boundary_design: <true | false>\n    internal_code_quality: <true | false>\n    object_module_design: <true | false>\n    logic: <true | false>",
    "new feature affected domains",
)
text = replace_once(
    text,
    "master-engineer       architecture, contracts, data, integration\nmaster-design",
    "master-engineer       architecture, contracts, data, integration\nclean-architecture    architecture-style applicability and policy/mechanism boundaries when material\nsolid-design          responsibility, extension, substitution, client-interface, dependency design when material\nmaster-design",
    "new feature relevant owners",
)
text = replace_once(
    text,
    "Load `master-engineer` and `test-driven-development`.\n",
    "Load `master-engineer`, `clean-code`, and `test-driven-development`. Load `solid-design` only when the approved implementation materially changes class/module/service ownership, extension seams, substitution contracts, client interfaces, or policy/detail dependency relationships.\n\n`clean-code` guides local implementation quality; it does not authorize unrelated cleanup or replace behavior tests. `solid-design` may conclude `NOT_APPLICABLE`; do not manufacture abstractions.\n",
    "new feature implement loading",
)
text = replace_once(
    text,
    "architecture-review\nsecurity evidence when affected",
    "clean-code review and behavior-change risk\nsolid-design assessment when materially applicable\nclean-architecture decision trace when architecture-style or boundary design was material\narchitecture-review\nsecurity evidence when affected",
    "new feature verification evidence",
)
text = replace_once(
    text,
    "architecture-review result\ndesign-review route/verdict/findings/gaps when applicable",
    "clean-code verdict/findings/gaps\nsolid-design applicability/verdict/findings when applicable\nclean-architecture applicability and boundary decision when applicable\narchitecture-review result\ndesign-review route/verdict/findings/gaps when applicable",
    "new feature submission evidence",
)
text = replace_once(
    text,
    "| CI green, therefore feature complete | Collect architecture, runtime, design, and risk evidence |",
    "| CI green, therefore feature complete | Collect code quality, object-design when applicable, architecture, runtime, design, and risk evidence |\n| Apply SOLID or Clean Architecture to every change | Classify applicability and select the smallest justified design |\n| Lint and formatting pass, therefore code quality PASS | Run clean-code evidence review without arbitrary metrics |",
    "new feature pitfalls",
)
path.write_text(text, encoding="utf-8")

# ---------------------------------------------------------------------------
# Engineering Quality Pack
# ---------------------------------------------------------------------------
path = ROOT / "docs/skill-packs.md"
text = path.read_text(encoding="utf-8")
old = """Architecture and implementation quality loop — repository-context mapping, architecture review, security review, code review, testing, debugging, refactoring, and technical-debt governance.

```bash
npx skills add puterakahfi/ai-native-skills \\
  --skill implementation-context-discovery \\
  --skill architecture-review \\
  --skill security-review \\
  --skill code-review-workflow \\
  --skill test-driven-development \\
  --skill systematic-debugging \\
  --skill refactoring \\
  --skill technical-debt-governance \\
  -g -y
```"""
new = """Architecture and implementation quality loop — repository-context mapping, pragmatic architecture and object-design decisions, internal code quality, testing, debugging, behavior-preserving refactoring, independent architecture/security/code review, and technical-debt governance.

```bash
npx skills add puterakahfi/ai-native-skills \\
  --skill implementation-context-discovery \\
  --skill master-engineer \\
  --skill clean-architecture \\
  --skill solid-design \\
  --skill clean-code \\
  --skill test-driven-development \\
  --skill systematic-debugging \\
  --skill refactoring \\
  --skill architecture-review \\
  --skill security-review \\
  --skill code-review-workflow \\
  --skill technical-debt-governance \\
  -g -y
```

`clean-code` is the baseline implementation-quality lens. Load `solid-design` only for material responsibility, extension, substitution, client-interface, or dependency-design pressure. Load `clean-architecture` only for material architecture-style or policy/mechanism boundary decisions; it may correctly return `NOT_JUSTIFIED`. Independent `architecture-review` and `code-review-workflow` remain required acceptance gates."""
text = replace_once(text, old, new, "engineering quality pack")
path.write_text(text, encoding="utf-8")

# ---------------------------------------------------------------------------
# Discovery job profile: clean-code is baseline, other two remain optional.
# ---------------------------------------------------------------------------
path = ROOT / "catalog/capability-discovery/job-profiles.json"
data = json.loads(path.read_text(encoding="utf-8"))
for profile in data["job_profiles"]:
    if profile["id"] == "engineering-quality":
        for group in profile["capability_groups"]:
            if group["purpose"] == "Design and implement the technical solution":
                if "clean-code" in group["optional"]:
                    group["optional"].remove("clean-code")
                if "clean-code" not in group["required"]:
                    group["required"].append("clean-code")
                break
        profile["expected_evidence"].insert(
            2,
            "Internal code-quality evidence with named findings, behavior-preservation risk, and materially applicable SOLID or architecture-style decisions.",
        )
        break
path.write_text(json.dumps(data, separators=(",", ":"), ensure_ascii=False) + "\n", encoding="utf-8")

# ---------------------------------------------------------------------------
# Integration eval cases
# ---------------------------------------------------------------------------
path = ROOT / "contracts/tests/code-review-workflow.test.yaml"
text = path.read_text(encoding="utf-8")
text = replace_once(text, 'version: "2.1.0"', 'version: "2.2.0"', "code review eval version")
text += """

    - id: lint-green-code-still-needs-internal-quality-review
      description: Passing formatters, lint, tests, and build does not prove readability or maintainability.
      trigger: "Review PR service ini. Lint, formatter, tests, dan build PASS, tetapi perubahan mencampur provider errors, business decisions, nested flags, dan duplicated condition knowledge. Author menyatakan code quality otomatis PASS."
      must_contain: ["clean-code", "Code quality", "readability", "behavior", "REQUEST CHANGES"]
      must_not_contain: ["Code quality: PASS because lint is green", "Approved to merge: YES"]
      quality_gates_tested: [internal_code_quality_is_explicit, tools_do_not_self_approve_clean_code, named_findings_require_evidence]

    - id: solid-and-clean-architecture-are-conditional-specialists
      description: Material interface and policy/detail changes load the specialists while trivial local edits do not force ceremony.
      trigger: "Review PR yang mengubah service ownership, inheritance contract, client interface, dan memindahkan provider SDK ke application policy. Tentukan reviewer dan bedakan specialist guidance dari architecture acceptance."
      must_contain: ["solid-design", "clean-architecture", "applicability", "architecture-review", "independent"]
      must_not_contain: ["SOLID required for every file", "Clean Architecture automatically PASS", "architecture-review not needed"]
      quality_gates_tested: [conditional_engineering_design_specialists, specialist_guidance_does_not_replace_acceptance, no_architecture_ceremony]
"""
path.write_text(text, encoding="utf-8")

path = ROOT / "contracts/tests/new-feature-workflow.test.yaml"
text = path.read_text(encoding="utf-8")
text = replace_once(text, 'version: "2.3.0"', 'version: "2.4.0"', "new feature eval version")
text += """

    - id: material-boundary-design-precedes-implementation-and-remains-independently-reviewed
      description: A material provider and policy boundary uses clean-architecture before code but still requires architecture-review after implementation.
      trigger: "Feature payment baru memindahkan provider SDK keluar dari application policy dan menambah entrypoint queue. Tentukan sequence capability dan acceptance."
      must_contain: ["clean-architecture", "implementation-context-discovery", "before implementation", "architecture-review", "independent"]
      must_not_contain: ["clean-architecture self-approves", "generic four-layer folders", "architecture PASS before implementation"]
      sequence_required:
        - pattern: "clean-architecture"
          must_come_before: "implement one approved slice|code production"
        - pattern: "implement one approved slice|code production"
          must_come_before: "architecture-review"
      quality_gates_tested: [material_boundary_design_before_implementation, repository_mapping_before_code, independent_architecture_acceptance]

    - id: local-feature-uses-clean-code-without-forcing-solid-or-clean-architecture
      description: A bounded local implementation receives clean-code guidance while specialist architecture and SOLID lenses may be not applicable.
      trigger: "Tambahkan validasi lokal kecil pada module existing tanpa interface, inheritance, provider, boundary, atau architecture change. Terapkan engineering quality tanpa over-engineering."
      must_contain: ["clean-code", "test", "smallest", "NOT_APPLICABLE"]
      must_not_contain: ["create a new architecture layer", "interface for every class", "clean-architecture required"]
      quality_gates_tested: [clean_code_baseline, solid_design_conditional, clean_architecture_conditional, smallest_justified_change]
"""
path.write_text(text, encoding="utf-8")

print("Engineering quality workflow refinement applied.")
