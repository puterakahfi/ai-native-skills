from pathlib import Path


def load(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def save(path: str, text: str) -> None:
    Path(path).write_text(text, encoding="utf-8")


def replace_once(path: str, old: str, new: str) -> None:
    text = load(path)
    count = text.count(old)
    if count != 1:
        raise SystemExit(
            f"{path}: expected exactly one match, got {count}: {old[:120]!r}"
        )
    save(path, text.replace(old, new, 1))


def insert_before(path: str, marker: str, addition: str) -> None:
    text = load(path)
    count = text.count(marker)
    if count != 1:
        raise SystemExit(
            f"{path}: expected exactly one marker, got {count}: {marker[:120]!r}"
        )
    save(path, text.replace(marker, addition + marker, 1))


def append_case(path: str, case_id: str, block: str) -> None:
    text = load(path)
    if f"id: {case_id}" in text:
        return
    save(path, text.rstrip() + "\n\n" + block.rstrip() + "\n")


# workflow-router: lifecycle remains primary; topology becomes an overlay.
p = "skills/workflow-router/SKILL.md"
replace_once(p, "ai-native-skills.version: 1.4.1", "ai-native-skills.version: 1.5.0")
replace_once(
    p,
    "product-development-workflow chatgpt-app-development",
    "product-development-workflow delivery-work-breakdown chatgpt-app-development",
)
replace_once(
    p,
    '"product-development-workflow","chatgpt-app-development"',
    '"product-development-workflow","delivery-work-breakdown","chatgpt-app-development"',
)
insert_before(
    p,
    "## Platform Specialist Overlays\n",
    """## Delivery Topology Overlay

Lifecycle selection does not choose repository topology.

```text
one independently releasable slice
  → delivery-work-breakdown may classify feature or standalone change

multiple dependent slices forming one outcome
  → delivery-work-breakdown
  → release_unit: epic
  → child PRs target the epic/integration branch
  → final epic PR targets the release branch after integrated acceptance
```

Load `delivery-work-breakdown` before Git execution for new apps, broad multi-slice capabilities, epic/feature/task decomposition, feature-flag exceptions, or unresolved base/PR targets. Repository defaults, green CI, and mergeability cannot choose the PR target.

""",
)
replace_once(
    p,
    "New capability? → new-feature-workflow\n",
    "New capability? → new-feature-workflow\n  multi-slice or target unresolved? → delivery-work-breakdown\n",
)
replace_once(
    p,
    "| ChatGPT App target creates a competing primary workflow | Preserve lifecycle and add `chatgpt-app-development` as overlay |",
    "| ChatGPT App target creates a competing primary workflow | Preserve lifecycle and add `chatgpt-app-development` as overlay |\n| Child work targets the default branch automatically | Run `delivery-work-breakdown` and preserve the governing release unit |",
)

# new-feature-workflow: topology gate before design/context/code.
p = "skills/new-feature-workflow/SKILL.md"
replace_once(p, "ai-native-skills.version: 2.2.0", "ai-native-skills.version: 2.3.0")
replace_once(
    p,
    "master-engineer master-design implementation-context-discovery",
    "master-engineer master-design delivery-work-breakdown implementation-context-discovery",
)
replace_once(
    p,
    '"phase":"plan","load":["master-engineer","decision-provenance"]},',
    '"phase":"plan","load":["master-engineer","decision-provenance"]},{"phase":"delivery-topology","load":["delivery-work-breakdown","decision-provenance"]},',
)
replace_once(
    p,
    '"required":["master-engineer","implementation-context-discovery"',
    '"required":["master-engineer","delivery-work-breakdown","implementation-context-discovery"',
)
replace_once(
    p,
    "verified scope\n→ approved architecture/design decisions",
    "verified scope\n→ approved delivery topology\n→ approved architecture/design decisions",
)
replace_once(
    p,
    "  issue_ref: <issue or task>\n\n  decision_sources:",
    """  issue_ref: <issue or task>

  delivery_topology:
    release_unit: <standalone_change | feature | epic | product_release>
    parent_ref: <epic/product ref or null>
    acceptance_criteria_refs: []
    dependency_refs: []
    independently_releasable: <true | false | unknown>
    feature_flag_policy_ref: <record | null | unknown>
    release_branch: <product-defined>
    integration_branch: <branch | not_applicable | unknown>
    base_branch: <explicit>
    pr_target: <explicit>
    topology_record_ref: <delivery-work-breakdown output>

  decision_sources:""",
)
insert_before(
    p,
    "## Phase 2 — Architecture and design decision\n",
    """## Phase 1B — Delivery topology

**Gate:** release unit, parent, acceptance traceability, dependency graph, base branch, and PR target are explicit before branch creation or PR submission.

Load `delivery-work-breakdown`. A dependent child of an epic branches from and targets the approved epic/integration branch. Direct-to-release requires independent releasability or an approved default-safe feature flag with no unflagged incomplete path.

Block orphan tasks, dependency cycles, unknown targets, and any target justified only by the repository default branch.

**Done when:** the topology verdict is PASS and recorded in workflow context.

""",
)
replace_once(
    p,
    "implementation_context_profile and convention locks\n",
    "delivery topology record, release unit, parent, base branch, and PR target\nimplementation_context_profile and convention locks\n",
)
replace_once(
    p,
    "provenance blocker, implementation-context blocker",
    "provenance blocker, delivery-topology mismatch, implementation-context blocker",
)
replace_once(
    p,
    "| Architecture/design | Decision authority |",
    "| Delivery topology | Release unit + hierarchy + PR target | Parent, dependencies, base branch, target, and exception evidence explicit |\n| Architecture/design | Decision authority |",
)
replace_once(
    p,
    "| Agent-generated issue means scope approved | Verify attributable authority |",
    "| Agent-generated issue means scope approved | Verify attributable authority |\n| Default branch becomes the PR target | Consume the approved delivery topology |\n| Green child CI means the epic is complete | Run integrated epic acceptance |",
)

# product-development-workflow: classify MVP release unit before feature branches.
p = "skills/product-development-workflow/SKILL.md"
replace_once(p, "ai-native-skills.version: 2.2.0", "ai-native-skills.version: 2.3.0")
replace_once(
    p,
    "user-research product-manager decision-provenance",
    "user-research product-manager delivery-work-breakdown decision-provenance",
)
replace_once(
    p,
    '"product-manager","decision-making","spike"',
    '"product-manager","delivery-work-breakdown","decision-making","spike"',
)
replace_once(
    p,
    '"spec-workflow","native-ai-engineer"',
    '"spec-workflow","delivery-work-breakdown","native-ai-engineer"',
)
replace_once(
    p,
    "6. Implementation runs through new-feature-workflow boundaries.",
    "6. Classify the release unit and approve hierarchy, base branches, and PR targets before implementation branches.\n7. Implementation runs through new-feature-workflow boundaries.",
)
replace_once(
    p,
    "| 3 | MVP Slice | prioritization + provenance | Smallest valuable slice explicitly approved |",
    "| 3 | MVP Slice + Delivery Topology | prioritization + `delivery-work-breakdown` + provenance | Release unit, hierarchy, integration branch, and PR targets explicitly approved |",
)
insert_before(
    p,
    "## Conditional platform specialists\n",
    """## Delivery decomposition boundary

Before implementation, load `delivery-work-breakdown`.

```text
single independently releasable slice
  → feature or standalone release unit may be valid

multiple dependent slices forming one MVP outcome
  → epic release unit
  → child PRs target the epic/integration branch
  → final epic PR targets the release branch after product acceptance
```

Equivalent trunk-based delivery is valid only with attributable default-safe activation, traceability, integrated acceptance, rollback, and release authorization. Child CI does not prove epic or product acceptance.

""",
)
replace_once(
    p,
    "Phase 5 may produce several technically approved feature submissions.",
    "Phase 5 may produce several technically approved feature submissions on an epic/integration branch.",
)

# git-workflow executes approved topology; it never invents one.
p = "skills/git-workflow/SKILL.md"
replace_once(p, "ai-native-skills.version: 1.0.1", "ai-native-skills.version: 1.1.0")
replace_once(
    p,
    "  ai-native-skills.author: puterakahfi\n  ai-native-skills.type: skill",
    "  ai-native-skills.author: puterakahfi\n  ai-native-skills.requires: \"delivery-work-breakdown decision-provenance\"\n  ai-native-skills.type: skill\n  ai-native-skills.related_skills: '[\"delivery-work-breakdown\",\"new-feature-workflow\",\"product-development-workflow\"]'",
)
replace_once(
    p,
    "Always branch from the correct base.\nEvery PR",
    "Always branch from the correct approved base.\nNever infer base or PR target from the repository default.\nConsume `delivery-work-breakdown` for product/feature work.\nEvery PR",
)
replace_once(
    p,
    "- What is the base branch? (product_defined)",
    "- What is the governing release unit and parent work item?\n- What topology record approved this operation?\n- What is the explicit base branch? (product_defined)\n- What is the explicit PR target? (product_defined)",
)
replace_once(
    p,
    "Always create from the correct base branch — never from stale local state.",
    "Always create from the correct approved base branch — never from stale local state or a guessed default. Epic children start from the approved integration branch.",
)
replace_once(
    p,
    "Checklist before submit:\n- [ ] Branch is up to date with base",
    "Checklist before submit:\n- [ ] Release unit and parent traceability are explicit\n- [ ] Base branch and PR target match the approved topology\n- [ ] Epic children do not bypass the integration branch\n- [ ] Branch is up to date with base",
)
replace_once(
    p,
    "| Create branch | From correct base, pulled fresh |",
    "| Create branch | From explicit approved base, pulled fresh |\n| Choose PR target | Matches the approved release unit and topology |",
)

# product-manager owns scope/ACs; delivery skill owns release topology.
p = "skills/product-manager/SKILL.md"
replace_once(p, "ai-native-skills.version: 1.0.1", "ai-native-skills.version: 1.1.0")
replace_once(
    p,
    "  ai-native-skills.contract-version: \"~0.1\"",
    "  ai-native-skills.contract-version: \"~0.1\"\n  ai-native-skills.related_skills: '[\"delivery-work-breakdown\",\"product-development-workflow\",\"new-feature-workflow\"]'",
)
replace_once(
    p,
    "Every task traces to acceptance criteria; implementation detail",
    "Every task traces to acceptance criteria. Multi-slice work and unresolved repository targets hand off to `delivery-work-breakdown`; task breakdown alone does not choose an epic or PR target. Implementation detail",
)
replace_once(
    p,
    "  title: \"\"\n  traces_to:",
    "  title: \"\"\n  work_item_type: task | spike | bug\n  parent_ref: \"\"\n  traces_to:",
)
insert_before(
    p,
    "## 4. Prioritization\n",
    """## Delivery topology handoff

`product-manager` owns intent, scope, acceptance criteria, priority, and task intent. When dependent slices or branch targets are unresolved, pass the verified scope and criteria to `delivery-work-breakdown`. It returns release unit, parent hierarchy, dependency graph, base branches, PR targets, integration plan, and epic acceptance plan. `git-workflow` then executes that approved topology.

""",
)
replace_once(
    p,
    "| Tasks with no AC reference | No traceability — fails gate |",
    "| Tasks with no AC reference | No traceability — fails gate |\n| Task list silently targets the default branch | Route repository topology to `delivery-work-breakdown` |",
)

# Pin CI to stacked core contract head.
replace_once(
    ".github/workflows/skill-eval.yml",
    "ref: f94b6ad86583c714b68eb5ea9f92890557b462c5",
    "ref: fdd743c7e08acc9fc70ca02509a83317c42f2df9",
)

# Strict adapter registry.
p = Path("contracts/conformance/strict-adapters.txt")
lines = p.read_text(encoding="utf-8").splitlines()
header = []
entries = []
seen_entry = False
for line in lines:
    if not seen_entry and (not line.strip() or line.lstrip().startswith("#")):
        header.append(line)
    else:
        seen_entry = True
        if line.strip() and not line.lstrip().startswith("#"):
            entries.append(line.strip())
entries.append("delivery-work-breakdown")
p.write_text("\n".join(header + sorted(set(entries))) + "\n", encoding="utf-8")

# Inventory and discovery documentation.
replace_once(
    "README.md",
    "**84 skills · 9 workflows · 6 meta-skills**",
    "**85 skills · 9 workflows · 6 meta-skills**",
)
replace_once(
    "README.md",
    "| Discover repository frameworks, components, styling, icons, tooling, and reuse constraints before code |",
    "| Classify feature vs epic and define issue/branch/PR topology | `delivery-work-breakdown` |\n| Discover repository frameworks, components, styling, icons, tooling, and reuse constraints before code |",
)
replace_once(
    "README.md",
    "npx skills add puterakahfi/ai-native-skills@workflow-router -g -y\n",
    "npx skills add puterakahfi/ai-native-skills@workflow-router -g -y\nnpx skills add puterakahfi/ai-native-skills@delivery-work-breakdown -g -y\n",
)
replace_once(
    "README.md",
    "| `skill` | One reusable capability or expert lens | `implementation-context-discovery`,",
    "| `skill` | One reusable capability or expert lens | `delivery-work-breakdown`, `implementation-context-discovery`,",
)
replace_once(
    "README.md",
    "| Map an accepted feature/design into an existing repository stack before implementation |",
    "| Decompose a release into epic/feature/task work and define branch/PR topology | `delivery-work-breakdown` |\n| Map an accepted feature/design into an existing repository stack before implementation |",
)
replace_once(
    "README.md",
    "product-development-workflow → spec-workflow → new-feature-workflow",
    "product-development-workflow → spec-workflow → delivery-work-breakdown\n  → new-feature-workflow",
)
replace_once(
    "README.md",
    "→ chatgpt-app-development + native-ai-engineer\n  → implementation-context-discovery",
    "→ delivery-work-breakdown for dependent P0 slices\n  → chatgpt-app-development + native-ai-engineer\n  → implementation-context-discovery",
)

replace_once("docs/skills.md", "- `skill`: 84", "- `skill`: 85")
replace_once(
    "docs/skills.md",
    "- Total executable skills: 99",
    "- Total executable skills: 100",
)
replace_once(
    "docs/skills.md",
    "| `skill` | Provide one reusable capability | “What capability or expert lens is needed?” | `implementation-context-discovery`,",
    "| `skill` | Provide one reusable capability | “What capability or expert lens is needed?” | `delivery-work-breakdown`, `implementation-context-discovery`,",
)
replace_once(
    "docs/skills.md",
    "### Examples\n\n- `implementation-context-discovery`",
    "### Examples\n\n- `delivery-work-breakdown` — classify release units, work hierarchy, branch bases, PR targets, and epic acceptance before Git execution.\n- `implementation-context-discovery`",
)
replace_once(
    "docs/skills.md",
    "plan → architecture/design decision → implementation-context discovery",
    "plan → delivery topology → architecture/design decision → implementation-context discovery",
)
replace_once(
    "docs/skills.md",
    "discovery → PRD → MVP → spec → implementation",
    "discovery → PRD → MVP/release-unit decomposition → spec → implementation",
)
replace_once(
    "docs/skills.md",
    "Examples:\n\n- `implementation-context-discovery`;",
    "Examples:\n\n- `delivery-work-breakdown`;\n- `implementation-context-discovery`;",
)

# Skill packs: line insertion avoids fragile trailing backslashes.
p = Path("docs/skill-packs.md")
text = p.read_text(encoding="utf-8")
text = text.replace(
    "Full product lifecycle — discovery, verified PRD/MVP decisions, implementation-context mapping",
    "Full product lifecycle — discovery, verified PRD/MVP decisions, release-unit and epic/feature/task decomposition, branch/PR topology, implementation-context mapping",
    1,
)
text = text.replace(
    "End-to-end ChatGPT App product delivery using the existing product lifecycle plus",
    "End-to-end ChatGPT App product delivery using the existing product lifecycle, release-unit/epic decomposition, plus",
    1,
)
lines = text.splitlines()
slash = chr(92)
for heading in ("## Product Development Pack", "## ChatGPT App Product Pack"):
    start = lines.index(heading)
    end = next(
        (i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")),
        len(lines),
    )
    if any("--skill delivery-work-breakdown" in line for line in lines[start:end]):
        continue
    marker = next(
        i for i in range(start, end) if "--skill decision-provenance" in lines[i]
    )
    lines.insert(marker, "  --skill delivery-work-breakdown " + slash)
dep_marker = next(
    i
    for i, line in enumerate(lines)
    if line.startswith("| `implementation-context-discovery` |")
)
lines.insert(
    dep_marker,
    "| `delivery-work-breakdown` | verified scope/criteria; repository and release context; product-defined tracker, branch, PR, flag, merge, and release policy; git-workflow for execution |",
)
p.write_text("\n".join(lines) + "\n", encoding="utf-8")

# Eval versions and focused regressions.
replace_once(
    "contracts/tests/workflow-router.test.yaml",
    "version: 1.4.1",
    "version: 1.5.0",
)
append_case(
    "contracts/tests/workflow-router.test.yaml",
    "multi-slice-product-loads-delivery-topology",
    """  - id: multi-slice-product-loads-delivery-topology
    description: A dependent broad capability keeps its lifecycle and loads delivery decomposition before Git execution.
    trigger: Add a multi-slice ChatGPT App P0 to an existing product; slices are dependent and targets are undefined.
    must_contain: [new-feature-workflow, chatgpt-app-development, delivery-work-breakdown, epic]
    must_not_contain: [every child PR targets main, default branch decides target]
    quality_gates_tested: [existing_product_feature_route_preserved, platform_specialist_overlay, release_unit_classified_before_repository_execution]
""",
)

replace_once(
    "contracts/tests/new-feature-workflow.test.yaml",
    'version: "2.2.0"',
    'version: "2.3.0"',
)
append_case(
    "contracts/tests/new-feature-workflow.test.yaml",
    "epic-child-targets-integration-branch",
    """    - id: epic-child-targets-integration-branch
      description: An epic child cannot create a branch or target main before delivery topology passes.
      trigger: Implement an MCP child slice for epic 37; default is main but no approved base or target exists.
      must_contain: [delivery-work-breakdown, release unit, parent_ref, base_branch, pr_target, BLOCKED]
      must_not_contain: [target main by default, create branch immediately]
      quality_gates_tested: [release_unit_classified_before_repository_execution, epic_child_pr_target_matches_integration_branch, no_orphan_feature_slice]
""",
)

replace_once(
    "contracts/tests/git-workflow.test.yaml",
    "version: 1.0.1",
    "version: 1.1.0",
)
append_case(
    "contracts/tests/git-workflow.test.yaml",
    "git-does-not-guess-epic-pr-target",
    """  - id: git-does-not-guess-epic-pr-target
    description: Git consumes approved epic topology rather than repository defaults.
    trigger: Create a child branch and PR for epic 37; approved base and target are epic/37-chatgpt-app-p0 while default is main.
    must_contain: [delivery-work-breakdown, epic/37-chatgpt-app-p0, base branch, PR target]
    must_not_contain: [default branch wins, target main]
    quality_gates_tested: [branch_must_be_created_from_correct_base, pr_target_must_match_approved_delivery_topology]
""",
)

replace_once(
    "contracts/tests/product-manager.test.yaml",
    "version: 1.0.1",
    "version: 1.1.0",
)
append_case(
    "contracts/tests/product-manager.test.yaml",
    "task-breakdown-hands-off-release-topology",
    """  - id: task-breakdown-hands-off-release-topology
    description: Product task breakdown delegates epic and repository topology decisions.
    trigger: Break a multi-slice ChatGPT App MVP into traceable tasks and decide PR targets.
    must_contain: [tasks_must_trace_to_acceptance_criteria, parent_ref, delivery-work-breakdown, release unit, branch topology]
    must_not_contain: [product-manager chooses main from default, floating task]
    quality_gates_tested: [acceptance_criteria_must_be_testable_not_vague, tasks_must_trace_to_acceptance_criteria]
""",
)

replace_once(
    "contracts/tests/product-development-workflow.test.yaml",
    'version: "2.2.0"',
    'version: "2.3.0"',
)
append_case(
    "contracts/tests/product-development-workflow.test.yaml",
    "multi-slice-mvp-requires-epic-acceptance",
    """    - id: multi-slice-mvp-requires-epic-acceptance
      description: Product delivery creates an epic before dependent feature branches and verifies one integrated release unit.
      trigger: Seven dependent MVP slices are approved; merge each directly to main when child CI passes.
      must_contain: [delivery-work-breakdown, "release_unit: epic", integration branch, end-to-end acceptance, release authorization]
      must_not_contain: [child CI proves product acceptance, direct child PR to main]
      quality_gates_tested: [mvp_release_unit_and_topology_defined_before_implementation, child_evidence_reconciled_at_epic_acceptance, release_ready_does_not_self_authorize_release]
""",
)
