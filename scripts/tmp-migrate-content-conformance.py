#!/usr/bin/env python3
"""One-time reviewed migration for copywriting and CRO adapters."""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Any

import yaml

MIGRATIONS: dict[str, dict[str, Any]] = {
    "copywriting": {
        "contract": "contracts/skills/content/copywriting.contract.yaml",
        "pin": "^1.0.0",
        "old_version": "1.0.0",
        "new_version": "1.0.1",
        "markers": [
            "# Copywriting",
            "## The Content Hierarchy",
            "## Headline Formulas",
            "## Tone Calibration",
            "Gate CP1: Value Proposition Clarity",
            "Gate CP4: Tone Consistency",
        ],
    },
    "cro": {
        "contract": "contracts/skills/content/cro.contract.yaml",
        "pin": "^1.0.0",
        "old_version": "1.0.0",
        "new_version": "1.0.1",
        "markers": [
            "# CRO — Conversion Rate Optimization",
            "## The Attention Economy Model",
            "## Trust Signal Architecture",
            "## Friction Audit",
            "## The 5-Second Test (self-audit)",
            "Gate CRO4: Persuasion Sequence",
        ],
    },
}


def load_yaml(path: Path) -> dict[str, Any]:
    payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"{path}: YAML root must be a mapping")
    return payload


def parse_frontmatter(text: str) -> tuple[dict[str, Any], int, int]:
    match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not match:
        raise ValueError("SKILL.md has no YAML frontmatter")
    payload = yaml.safe_load(match.group(1)) or {}
    if not isinstance(payload, dict):
        raise ValueError("SKILL.md frontmatter must be a mapping")
    return payload, match.start(1), match.end(1)


def assert_equal(label: str, actual: Any, expected: Any) -> None:
    if actual != expected:
        raise ValueError(f"{label} mismatch: actual={actual!r}, expected={expected!r}")


def render_interface(contract: dict[str, Any], contract_path: str, pin: str) -> str:
    inputs = contract.get("inputs") or {}
    outputs = contract.get("outputs") or {}
    payload = {
        "required_inputs": [str(value) for value in inputs.get("required", [])],
        "allowed_outputs": [str(value) for value in outputs.get("allowed", [])],
        "quality_gates": [str(value) for value in contract.get("quality_gates", [])],
    }
    return (
        "\n## Reviewed core contract interface\n\n"
        f"Source: `ai-native-core/{contract_path}` · compatible line: `{pin}`\n\n"
        "```yaml\n"
        + yaml.safe_dump(payload, sort_keys=False).rstrip()
        + "\n```\n\n"
        "Keep this interface synchronized with the pinned core contract. "
        "Static conformance does not replace behavioral, runtime, product, review, or approval evidence.\n"
    )


def declaration(skill_id: str, contract: dict[str, Any], contract_path: str, pin: str) -> dict[str, Any]:
    inputs = contract.get("inputs") or {}
    outputs = contract.get("outputs") or {}
    boundary = contract.get("boundary") or {}
    adapter_requirements = contract.get("adapter_requirements") or {}
    if isinstance(adapter_requirements, dict):
        requirements = [str(key) for key in adapter_requirements]
    elif isinstance(adapter_requirements, list):
        requirements = [str(value) for value in adapter_requirements]
    else:
        requirements = []
    return {
        "contract_schema": {
            "kind": "adapter_conformance",
            "version": "1.0.0",
            "path": "schemas/adapter-conformance.schema.yaml",
        },
        "adapter_conformance": {
            "adapter": {
                "id": skill_id,
                "kind": "skill",
                "patterns": ["skill-adapter"],
                "entrypoint": f"skills/{skill_id}/SKILL.md",
            },
            "implements": {
                "contract_id": skill_id,
                "contract_kind": "skill_contract",
                "contract_path": contract_path,
                "contract_version": pin,
            },
            "capability": contract.get("capability"),
            "interface": {
                "inputs": [str(value) for value in inputs.get("required", [])],
                "outputs": [str(value) for value in outputs.get("required", [])]
                + [str(value) for value in outputs.get("allowed", [])],
                "gates": [str(value) for value in contract.get("quality_gates", [])],
            },
            "boundary": {
                "covers": [str(value) for value in boundary.get("covers", [])],
                "delegates": [str(value) for value in boundary.get("does_not_cover", [])],
            },
            "dependencies": [str(value) for value in contract.get("dependencies", [])],
            "handoffs": [str(value) for value in contract.get("handoffs", [])],
            "unsupported_claims": [],
            "adapter_requirements": requirements,
            "evidence_refs": [],
        },
    }


def migrate(root: Path, core_root: Path, skill_id: str, config: dict[str, Any]) -> None:
    skill_path = root / "skills" / skill_id / "SKILL.md"
    text = skill_path.read_text(encoding="utf-8")
    frontmatter, fm_start, fm_end = parse_frontmatter(text)
    metadata = frontmatter.get("metadata") or {}
    if not isinstance(metadata, dict):
        raise ValueError(f"{skill_id}: metadata must be a mapping")
    assert_equal(f"{skill_id}.name", frontmatter.get("name"), skill_id)
    assert_equal(f"{skill_id}.type", metadata.get("ai-native-skills.type"), "skill")
    assert_equal(f"{skill_id}.version", metadata.get("ai-native-skills.version"), config["old_version"])
    if metadata.get("ai-native-skills.implements") is not None:
        raise ValueError(f"{skill_id}: implements already exists")
    if (skill_path.parent / "adapter.conformance.yaml").exists():
        raise ValueError(f"{skill_id}: declaration already exists")
    for marker in config["markers"]:
        if marker not in text:
            raise ValueError(f"{skill_id}: reviewed behavior marker missing: {marker}")
    if "## Reviewed core contract interface" in text:
        raise ValueError(f"{skill_id}: reviewed interface already exists")

    contract_document = load_yaml(core_root / config["contract"])
    contract = contract_document.get("skill_contract")
    if not isinstance(contract, dict):
        raise ValueError(f"{skill_id}: target is not a skill_contract")
    assert_equal(f"{skill_id}.contract_id", contract.get("id"), skill_id)
    assert_equal(f"{skill_id}.contract_type", contract.get("type"), "skill")

    metadata["ai-native-skills.version"] = config["new_version"]
    metadata["ai-native-skills.implements"] = f"ai-native-core/{config['contract']}"
    metadata["ai-native-skills.contract-version"] = config["pin"]
    frontmatter["metadata"] = metadata
    rendered_frontmatter = yaml.safe_dump(frontmatter, sort_keys=False).rstrip()
    text = text[:fm_start] + rendered_frontmatter + text[fm_end:]

    h1 = re.search(r"^# .+$", text, re.MULTILINE)
    if not h1:
        raise ValueError(f"{skill_id}: H1 heading missing")
    insert_at = h1.end()
    text = text[:insert_at] + render_interface(contract, config["contract"], config["pin"]) + text[insert_at:]
    skill_path.write_text(text, encoding="utf-8")
    (skill_path.parent / "adapter.conformance.yaml").write_text(
        yaml.safe_dump(declaration(skill_id, contract, config["contract"], config["pin"]), sort_keys=False),
        encoding="utf-8",
    )
    print(f"migrated {skill_id}")


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
