#!/usr/bin/env python3
"""One-time reviewed migration for three canonical workflow adapters.

This script is intentionally allowlisted and self-deleted by its workflow. It
refuses to create a declaration unless the existing reviewed interface and
legacy boundary agree with either the canonical workflow contract or one
explicitly reviewed legacy snapshot.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

import yaml

REDESIGN_LEGACY_INTERFACE = {
    "required_inputs": [
        "current_surface",
        "confirmed_scope",
        "baseline_evidence",
        "artifact_type",
        "output_mode",
        "decision_sources",
        "acceptance_criteria",
    ],
    "required_outputs": [],
    "allowed_outputs": [
        "redesign_state",
        "route_decision",
        "confirmed_scope",
        "scope_provenance",
        "decision_log",
        "integrity_gate",
        "implementation_context_gate",
        "concurrency_gate",
        "final_diff_manifest",
        "role_composition",
        "design_owner",
        "implementation_owner",
        "repository_write_owner",
        "redesign_strategy",
        "option_comparison",
        "selected_direction",
        "layered_change_plan",
        "implementation_context_profile",
        "convention_locks",
        "reuse_extension_decisions",
        "implementation_mapping",
        "dependency_decisions",
        "value_alignment",
        "production_output",
        "verification_evidence",
        "review_report",
        "correction_handoff",
        "learning_review",
        "delivery_decision",
    ],
    "quality_gates": [
        "route_before_production",
        "exactly_one_design_owner",
        "implementation_owner_required_for_patch_or_executable_prototype",
        "exactly_one_active_repository_write_owner_for_patch_mode",
        "material_decisions_require_verified_provenance",
        "unverified_approval_or_override_claims_block_progress",
        "current_state_baseline_scope_and_locks_are_captured_before_production",
        "preservation_locks_are_recorded_and_rechecked",
        "implementation_context_is_required_before_repository_code_production",
        "package_presence_does_not_prove_canonicality",
        "implementation_mapping_precedes_code_production",
        "new_dependency_requires_proven_capability_gap_consequences_and_authority",
        "final_effective_diff_is_verified_not_only_patch_commits",
        "concurrent_writes_are_detected_and_coordinated",
        "expected_head_lease_guards_every_repository_write",
        "parent_pointer_moves_only_after_child_stability",
        "repeated_conflicting_updates_stop_without_force_overwrite",
        "every_changed_path_must_be_classified",
        "scope_contamination_blocks_review_and_delivery",
        "concurrency_block_is_not_reported_as_pass",
        "review_uses_design_review_facade_and_loaded_domain_reviewer",
        "gate_statuses_preserve_partial_not_verified_and_not_applicable",
        "contextual_hard_gates_are_reviewer_owned",
        "facade_scope_and_concurrency_control_delivery",
        "defect_classification_precedes_fix",
        "verified_reusable_fixes_run_learning_review_and_regression_eval",
        "max_iteration_delivery_is_not_labeled_as_passed",
    ],
}

MIGRATIONS: dict[str, dict[str, Any]] = {
    "design-refinement": {
        "old_contract": "contracts/skills/quality/design-refinement.contract.yaml",
        "contract": "contracts/workflows/design-refinement.contract.yaml",
        "pin": "^1.2.0",
        "old_skill_version": "2.2.0",
        "new_skill_version": "2.2.1",
    },
    "redesign-workflow": {
        "old_contract": "contracts/skills/quality/redesign-workflow.contract.yaml",
        "contract": "contracts/workflows/redesign-workflow.contract.yaml",
        "pin": "^2.2.0",
        "old_skill_version": "3.6.0",
        "new_skill_version": "3.6.1",
        "legacy_interface": REDESIGN_LEGACY_INTERFACE,
    },
    "skill-evolution": {
        "old_contract": "contracts/skills/quality/skill-evolution.contract.yaml",
        "contract": "contracts/workflows/skill-evolution.contract.yaml",
        "pin": "^1.0.0",
        "old_skill_version": "1.0.2",
        "new_skill_version": "1.0.3",
    },
}


def load_yaml(path: Path) -> dict[str, Any]:
    payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"{path}: YAML root must be a mapping")
    return payload


def frontmatter(text: str) -> dict[str, Any]:
    match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not match:
        raise ValueError("SKILL.md has no YAML frontmatter")
    payload = yaml.safe_load(match.group(1)) or {}
    if not isinstance(payload, dict):
        raise ValueError("SKILL.md frontmatter must be a mapping")
    return payload


def parse_list(raw: Any) -> list[str]:
    if raw is None:
        return []
    if isinstance(raw, list):
        return [str(item) for item in raw]
    if isinstance(raw, str):
        try:
            value = json.loads(raw)
        except json.JSONDecodeError:
            value = yaml.safe_load(raw)
        if isinstance(value, list):
            return [str(item) for item in value]
    raise ValueError(f"expected list-like metadata, got {raw!r}")


def reviewed_interface_location(text: str) -> tuple[int, int, dict[str, list[str]]]:
    marker = "## Reviewed core contract interface"
    start = text.find(marker)
    if start < 0:
        raise ValueError("reviewed core contract interface section is missing")
    block_start = text.find("```yaml", start)
    block_end = text.find("```", block_start + len("```yaml"))
    if block_start < 0 or block_end < 0:
        raise ValueError("reviewed interface YAML block is missing")
    yaml_start = block_start + len("```yaml")
    payload = yaml.safe_load(text[yaml_start:block_end]) or {}
    if not isinstance(payload, dict):
        raise ValueError("reviewed interface block must be a mapping")
    interface = {
        "required_inputs": [str(value) for value in payload.get("required_inputs", [])],
        "required_outputs": [str(value) for value in payload.get("required_outputs", [])],
        "allowed_outputs": [str(value) for value in payload.get("allowed_outputs", [])],
        "quality_gates": [str(value) for value in payload.get("quality_gates", [])],
    }
    return yaml_start, block_end, interface


def render_reviewed_interface(interface: dict[str, list[str]]) -> str:
    payload: dict[str, list[str]] = {
        "required_inputs": interface["required_inputs"],
    }
    if interface["required_outputs"]:
        payload["required_outputs"] = interface["required_outputs"]
    if interface["allowed_outputs"]:
        payload["allowed_outputs"] = interface["allowed_outputs"]
    payload["quality_gates"] = interface["quality_gates"]
    return "\n" + yaml.safe_dump(payload, sort_keys=False).rstrip() + "\n"


def assert_equal(name: str, actual: Any, expected: Any) -> None:
    if actual != expected:
        raise ValueError(f"{name} mismatch\nactual={actual!r}\nexpected={expected!r}")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise ValueError(f"{label}: expected one occurrence of {old!r}, found {count}")
    return text.replace(old, new, 1)


def migrate(root: Path, core_root: Path, skill_id: str, config: dict[str, Any]) -> None:
    skill_path = root / "skills" / skill_id / "SKILL.md"
    text = skill_path.read_text(encoding="utf-8")
    fm = frontmatter(text)
    metadata = fm.get("metadata") or {}
    if not isinstance(metadata, dict):
        raise ValueError(f"{skill_id}: metadata must be a mapping")

    assert_equal(f"{skill_id}.name", fm.get("name"), skill_id)
    assert_equal(f"{skill_id}.type", metadata.get("ai-native-skills.type"), "workflow")
    assert_equal(
        f"{skill_id}.legacy_contract",
        metadata.get("ai-native-skills.implements"),
        f"ai-native-core/{config['old_contract']}",
    )
    assert_equal(f"{skill_id}.version_pin", metadata.get("ai-native-skills.contract-version"), config["pin"])
    assert_equal(f"{skill_id}.skill_version", metadata.get("ai-native-skills.version"), config["old_skill_version"])

    contract_document = load_yaml(core_root / config["contract"])
    contract = contract_document.get("workflow_contract")
    if not isinstance(contract, dict):
        raise ValueError(f"{skill_id}: canonical contract is not workflow_contract")
    assert_equal(f"{skill_id}.contract_id", contract.get("id"), skill_id)
    assert_equal(f"{skill_id}.contract_type", contract.get("type"), "workflow")

    inputs = contract.get("inputs") or {}
    outputs = contract.get("outputs") or {}
    canonical_interface = {
        "required_inputs": [str(value) for value in inputs.get("required", [])],
        "required_outputs": [str(value) for value in outputs.get("required", [])],
        "allowed_outputs": [str(value) for value in outputs.get("allowed", [])],
        "quality_gates": [str(value) for value in contract.get("quality_gates", [])],
    }
    yaml_start, block_end, current_interface = reviewed_interface_location(text)
    if current_interface != canonical_interface:
        legacy_interface = config.get("legacy_interface")
        if legacy_interface is None:
            assert_equal(f"{skill_id}.reviewed_interface", current_interface, canonical_interface)
        assert_equal(f"{skill_id}.reviewed_legacy_interface", current_interface, legacy_interface)
        text = text[:yaml_start] + render_reviewed_interface(canonical_interface) + text[block_end:]

    boundary = contract.get("boundary") or {}
    expected_covers = [str(value) for value in boundary.get("covers", [])]
    expected_delegates = [str(value) for value in boundary.get("does_not_cover", [])]
    legacy_covers = parse_list(metadata.get("ai-native-skills.boundary.covers")) if metadata.get("ai-native-skills.boundary.covers") is not None else []
    legacy_delegates = parse_list(metadata.get("ai-native-skills.boundary.delegates")) if metadata.get("ai-native-skills.boundary.delegates") is not None else []
    assert_equal(f"{skill_id}.legacy_covers", legacy_covers, expected_covers)
    assert_equal(f"{skill_id}.legacy_delegates", legacy_delegates, expected_delegates)

    adapter_requirements = contract.get("adapter_requirements") or {}
    if isinstance(adapter_requirements, dict):
        adapter_requirement_ids = [str(key) for key in adapter_requirements]
    elif isinstance(adapter_requirements, list):
        adapter_requirement_ids = [str(value) for value in adapter_requirements]
    else:
        raise ValueError(f"{skill_id}: adapter_requirements has unsupported shape")

    declaration_outputs = canonical_interface["required_outputs"] + canonical_interface["allowed_outputs"]
    declaration = {
        "contract_schema": {
            "kind": "adapter_conformance",
            "version": "1.0.0",
            "path": "schemas/adapter-conformance.schema.yaml",
        },
        "adapter_conformance": {
            "adapter": {
                "id": skill_id,
                "kind": "workflow",
                "patterns": ["skill-adapter"],
                "entrypoint": f"skills/{skill_id}/SKILL.md",
            },
            "implements": {
                "contract_id": skill_id,
                "contract_kind": "workflow_contract",
                "contract_path": config["contract"],
                "contract_version": config["pin"],
            },
            "capability": contract.get("capability"),
            "interface": {
                "inputs": canonical_interface["required_inputs"],
                "outputs": declaration_outputs,
                "gates": canonical_interface["quality_gates"],
            },
            "boundary": {
                "covers": expected_covers,
                "delegates": expected_delegates,
            },
            "dependencies": [str(value) for value in contract.get("dependencies", [])],
            "handoffs": [str(value) for value in contract.get("handoffs", [])],
            "unsupported_claims": [],
            "adapter_requirements": adapter_requirement_ids,
            "evidence_refs": [],
        },
    }

    text = replace_once(
        text,
        f"ai-native-skills.version: {config['old_skill_version']}",
        f"ai-native-skills.version: {config['new_skill_version']}",
        f"{skill_id}.skill_version",
    )
    text = replace_once(
        text,
        f"ai-native-skills.implements: ai-native-core/{config['old_contract']}",
        f"ai-native-skills.implements: ai-native-core/{config['contract']}",
        f"{skill_id}.implements",
    )
    text = replace_once(
        text,
        f"Source: `ai-native-core/{config['old_contract']}`",
        f"Source: `ai-native-core/{config['contract']}`",
        f"{skill_id}.source",
    )

    skill_path.write_text(text, encoding="utf-8")
    declaration_path = skill_path.parent / "adapter.conformance.yaml"
    if declaration_path.exists():
        raise ValueError(f"{skill_id}: declaration already exists")
    declaration_path.write_text(yaml.safe_dump(declaration, sort_keys=False), encoding="utf-8")
    print(f"migrated {skill_id} -> {config['contract']}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".")
    parser.add_argument("--core-root", required=True)
    args = parser.parse_args()
    root = Path(args.root).resolve()
    core_root = Path(args.core_root).resolve()
    for skill_id, config in MIGRATIONS.items():
        migrate(root, core_root, skill_id, config)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
