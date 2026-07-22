#!/usr/bin/env python3
"""One-time reviewed migration for three canonical workflow adapters.

This script is intentionally allowlisted and self-deleted by its workflow. It
refuses to create a declaration unless the existing reviewed interface and
legacy boundary agree with the resolved core workflow contract.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

import yaml

MIGRATIONS = {
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


def reviewed_interface(text: str) -> dict[str, list[str]]:
    marker = "## Reviewed core contract interface"
    start = text.find(marker)
    if start < 0:
        raise ValueError("reviewed core contract interface section is missing")
    block_start = text.find("```yaml", start)
    block_end = text.find("```", block_start + len("```yaml"))
    if block_start < 0 or block_end < 0:
        raise ValueError("reviewed interface YAML block is missing")
    payload = yaml.safe_load(text[block_start + len("```yaml"):block_end]) or {}
    if not isinstance(payload, dict):
        raise ValueError("reviewed interface block must be a mapping")
    return {
        "required_inputs": [str(value) for value in payload.get("required_inputs", [])],
        "allowed_outputs": [str(value) for value in payload.get("allowed_outputs", [])],
        "quality_gates": [str(value) for value in payload.get("quality_gates", [])],
    }


def assert_equal(name: str, actual: Any, expected: Any) -> None:
    if actual != expected:
        raise ValueError(f"{name} mismatch\nactual={actual!r}\nexpected={expected!r}")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise ValueError(f"{label}: expected one occurrence of {old!r}, found {count}")
    return text.replace(old, new, 1)


def migrate(root: Path, core_root: Path, skill_id: str, config: dict[str, str]) -> None:
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

    interface = reviewed_interface(text)
    inputs = contract.get("inputs") or {}
    outputs = contract.get("outputs") or {}
    expected_required_inputs = [str(value) for value in inputs.get("required", [])]
    expected_allowed_outputs = [str(value) for value in outputs.get("allowed", [])]
    expected_gates = [str(value) for value in contract.get("quality_gates", [])]
    assert_equal(f"{skill_id}.reviewed_required_inputs", interface["required_inputs"], expected_required_inputs)
    assert_equal(f"{skill_id}.reviewed_allowed_outputs", interface["allowed_outputs"], expected_allowed_outputs)
    assert_equal(f"{skill_id}.reviewed_quality_gates", interface["quality_gates"], expected_gates)

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
                "inputs": expected_required_inputs,
                "outputs": expected_allowed_outputs,
                "gates": expected_gates,
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
