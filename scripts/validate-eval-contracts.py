#!/usr/bin/env python3
"""Validate ai-native-skills eval contracts and optionally create smoke outputs."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
TESTS_DIR = ROOT / "contracts" / "tests"
SKILLS_DIR = ROOT / "skills"
GATE_REGISTRY_PATH = (
    ROOT / "skills" / "design-review" / "references" / "gate-registry.yaml"
)


class ContractError(ValueError):
    """Raised when an eval contract is invalid."""


def require_string(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ContractError(f"{label} must be a non-empty string")
    return value.strip()


def string_list(value: Any, label: str) -> list[str]:
    if value is None:
        return []
    if not isinstance(value, list):
        raise ContractError(f"{label} must be a list")
    return [require_string(item, f"{label}[{index}]") for index, item in enumerate(value)]


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        document = yaml.safe_load(handle)
    if not isinstance(document, dict):
        raise ContractError(f"{path}: root must be a mapping")
    return document


def load_active_design_gate_ids() -> set[str]:
    if not GATE_REGISTRY_PATH.is_file():
        raise ContractError(f"Missing design gate registry: {GATE_REGISTRY_PATH}")

    document = load_yaml(GATE_REGISTRY_PATH)
    gate_groups = document.get("gate_groups")
    if not isinstance(gate_groups, dict) or not gate_groups:
        raise ContractError(f"{GATE_REGISTRY_PATH}: gate_groups must be a non-empty mapping")

    active_ids: set[str] = set()
    for group_name, raw_group in gate_groups.items():
        if not isinstance(raw_group, dict):
            raise ContractError(
                f"{GATE_REGISTRY_PATH}: gate_groups.{group_name} must be a mapping"
            )
        defaults = raw_group.get("defaults")
        gates = raw_group.get("gates")
        if not isinstance(defaults, dict):
            raise ContractError(
                f"{GATE_REGISTRY_PATH}: gate_groups.{group_name}.defaults must be a mapping"
            )
        if not isinstance(gates, dict) or not gates:
            raise ContractError(
                f"{GATE_REGISTRY_PATH}: gate_groups.{group_name}.gates must be a non-empty mapping"
            )

        default_status = defaults.get("status")
        for gate_id, raw_gate in gates.items():
            if not isinstance(gate_id, str) or not gate_id:
                raise ContractError(
                    f"{GATE_REGISTRY_PATH}: gate id must be a non-empty string"
                )
            if not isinstance(raw_gate, dict):
                raise ContractError(
                    f"{GATE_REGISTRY_PATH}: gate '{gate_id}' must be a mapping"
                )
            status = raw_gate.get("status", default_status)
            if status == "active":
                if gate_id in active_ids:
                    raise ContractError(
                        f"{GATE_REGISTRY_PATH}: duplicate active gate id '{gate_id}'"
                    )
                active_ids.add(gate_id)

    if not active_ids:
        raise ContractError(f"{GATE_REGISTRY_PATH}: no active design gates found")
    return active_ids


def load_skill_version(skill_name: str) -> str:
    skill_file = SKILLS_DIR / skill_name / "SKILL.md"
    if not skill_file.is_file():
        raise ContractError(f"Skill referenced by eval does not exist: {skill_file}")

    text = skill_file.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ContractError(f"{skill_file}: missing YAML frontmatter")

    parts = text.split("---", 2)
    if len(parts) < 3:
        raise ContractError(f"{skill_file}: malformed YAML frontmatter")

    frontmatter = yaml.safe_load(parts[1])
    if not isinstance(frontmatter, dict):
        raise ContractError(f"{skill_file}: frontmatter must be a mapping")

    declared_name = require_string(frontmatter.get("name"), f"{skill_file}: name")
    if declared_name != skill_name:
        raise ContractError(
            f"{skill_file}: frontmatter name '{declared_name}' does not match directory '{skill_name}'"
        )

    metadata = frontmatter.get("metadata")
    if not isinstance(metadata, dict):
        raise ContractError(f"{skill_file}: metadata must be a mapping")

    version = metadata.get("ai-native-skills.version")
    return require_string(
        str(version) if version is not None else None,
        f"{skill_file}: version",
    )


def find_design_gate_references(
    texts: list[str],
    active_design_gate_ids: set[str],
) -> set[str]:
    combined = "\n".join(texts)
    found: set[str] = set()
    for gate_id in sorted(active_design_gate_ids, key=len, reverse=True):
        pattern = re.compile(
            rf"(?<![A-Z0-9]){re.escape(gate_id)}(?![A-Z0-9])",
            re.IGNORECASE,
        )
        if pattern.search(combined):
            found.add(gate_id)
    return found


def validate_case(
    path: Path,
    case: Any,
    index: int,
    seen_ids: set[str],
    active_design_gate_ids: set[str],
) -> dict[str, Any]:
    label = f"{path}: cases[{index}]"
    if not isinstance(case, dict):
        raise ContractError(f"{label} must be a mapping")

    case_id = require_string(case.get("id"), f"{label}.id")
    if case_id in seen_ids:
        raise ContractError(f"{path}: duplicate case id '{case_id}'")
    seen_ids.add(case_id)

    description = require_string(case.get("description"), f"{label}.description")
    trigger = require_string(case.get("trigger"), f"{label}.trigger")

    must_contain = string_list(case.get("must_contain"), f"{label}.must_contain")
    must_not_contain = string_list(case.get("must_not_contain"), f"{label}.must_not_contain")
    one_of = string_list(case.get("must_contain_one_of"), f"{label}.must_contain_one_of")
    quality_gates = string_list(
        case.get("quality_gates_tested"),
        f"{label}.quality_gates_tested",
    )
    design_gate_ids = string_list(
        case.get("design_gate_ids"),
        f"{label}.design_gate_ids",
    )

    invalid_design_gates = sorted(
        gate_id
        for gate_id in design_gate_ids
        if gate_id not in active_design_gate_ids
    )
    if invalid_design_gates:
        raise ContractError(
            f"{label}.design_gate_ids contains unregistered or non-active ids: "
            f"{invalid_design_gates}"
        )
    if len(set(design_gate_ids)) != len(design_gate_ids):
        raise ContractError(f"{label}.design_gate_ids contains duplicates")

    sequence_required = case.get("sequence_required", [])
    if not isinstance(sequence_required, list):
        raise ContractError(f"{label}.sequence_required must be a list")

    normalized_sequences: list[dict[str, str]] = []
    for sequence_index, sequence in enumerate(sequence_required):
        sequence_label = f"{label}.sequence_required[{sequence_index}]"
        if not isinstance(sequence, dict):
            raise ContractError(f"{sequence_label} must be a mapping")
        normalized_sequences.append(
            {
                "pattern": require_string(
                    sequence.get("pattern"),
                    f"{sequence_label}.pattern",
                ),
                "must_come_before": require_string(
                    sequence.get("must_come_before"),
                    f"{sequence_label}.must_come_before",
                ),
            }
        )

    if not quality_gates:
        raise ContractError(f"{label} must declare quality_gates_tested")

    if not must_contain and not must_not_contain and not one_of and not normalized_sequences:
        raise ContractError(f"{label} must define at least one output assertion")

    positive_exact = {item.casefold() for item in must_contain}
    negative_exact = {item.casefold() for item in must_not_contain}
    overlap = sorted(positive_exact & negative_exact)
    if overlap:
        raise ContractError(f"{label} has contradictory exact patterns: {overlap}")

    referenced_design_gates = find_design_gate_references(
        [
            description,
            trigger,
            *must_contain,
            *must_not_contain,
            *one_of,
            *(
                item
                for sequence in normalized_sequences
                for item in (sequence["pattern"], sequence["must_come_before"])
            ),
        ],
        active_design_gate_ids,
    )
    undeclared_references = sorted(
        referenced_design_gates - set(design_gate_ids)
    )
    if undeclared_references:
        raise ContractError(
            f"{label} references canonical design gate ids without declaring "
            f"design_gate_ids: {undeclared_references}"
        )

    return {
        "id": case_id,
        "must_contain": must_contain,
        "must_not_contain": must_not_contain,
        "must_contain_one_of": one_of,
        "sequence_required": normalized_sequences,
        "design_gate_ids": design_gate_ids,
    }


def validate_contract(
    path: Path,
    active_design_gate_ids: set[str],
) -> tuple[str, list[dict[str, Any]]]:
    document = load_yaml(path)
    skill_test = document.get("skill_test")
    if not isinstance(skill_test, dict):
        raise ContractError(f"{path}: missing skill_test mapping")

    skill_name = require_string(skill_test.get("skill"), f"{path}: skill_test.skill")
    expected_name = path.name.removesuffix(".test.yaml")
    if skill_name != expected_name:
        raise ContractError(
            f"{path}: skill '{skill_name}' does not match filename '{expected_name}'"
        )

    test_version = require_string(
        skill_test.get("version"),
        f"{path}: skill_test.version",
    )
    skill_version = load_skill_version(skill_name)
    if test_version != skill_version:
        raise ContractError(
            f"{path}: test version {test_version} does not match skill version {skill_version}"
        )

    require_string(
        skill_test.get("description"),
        f"{path}: skill_test.description",
    )

    cases = skill_test.get("cases")
    if not isinstance(cases, list) or not cases:
        raise ContractError(
            f"{path}: skill_test.cases must be a non-empty list"
        )

    seen_ids: set[str] = set()
    normalized_cases = [
        validate_case(
            path,
            case,
            index,
            seen_ids,
            active_design_gate_ids,
        )
        for index, case in enumerate(cases)
    ]
    return skill_name, normalized_cases


def choose_safe_one_of(options: list[str], forbidden: list[str]) -> str | None:
    forbidden_folded = [item.casefold() for item in forbidden]
    for option in options:
        folded = option.casefold()
        if not any(negative in folded for negative in forbidden_folded):
            return option
    return None


def write_smoke_output(
    output_root: Path,
    skill_name: str,
    case: dict[str, Any],
) -> None:
    parts: list[str] = []
    parts.extend(sequence["pattern"] for sequence in case["sequence_required"])
    parts.extend(case["must_contain"])

    if case["must_contain_one_of"]:
        selected = choose_safe_one_of(
            case["must_contain_one_of"],
            case["must_not_contain"],
        )
        if selected is None:
            raise ContractError(
                f"{skill_name}/{case['id']}: every must_contain_one_of option "
                f"conflicts with a forbidden pattern"
            )
        parts.append(selected)

    output = "\n".join(parts) + "\n"
    output_folded = output.casefold()
    collisions = [
        forbidden
        for forbidden in case["must_not_contain"]
        if forbidden.casefold() in output_folded
    ]
    if collisions:
        raise ContractError(
            f"{skill_name}/{case['id']}: synthetic passing output hits "
            f"forbidden patterns {collisions}"
        )

    case_dir = output_root / skill_name
    case_dir.mkdir(parents=True, exist_ok=True)
    (case_dir / f"{case['id']}.txt").write_text(
        output,
        encoding="utf-8",
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate skill eval contracts"
    )
    parser.add_argument(
        "--write-smoke-outputs",
        type=Path,
        help=(
            "Write deterministic per-case passing outputs for "
            "runner compatibility smoke tests"
        ),
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if not TESTS_DIR.is_dir():
        raise ContractError(f"Missing eval contract directory: {TESTS_DIR}")

    paths = sorted(TESTS_DIR.glob("*.test.yaml"))
    if not paths:
        raise ContractError(f"No eval contracts found in {TESTS_DIR}")

    active_design_gate_ids = load_active_design_gate_ids()
    total_cases = 0
    design_gate_references = 0

    for path in paths:
        skill_name, cases = validate_contract(
            path,
            active_design_gate_ids,
        )
        total_cases += len(cases)
        design_gate_references += sum(
            len(case["design_gate_ids"]) for case in cases
        )
        if args.write_smoke_outputs:
            for case in cases:
                write_smoke_output(
                    args.write_smoke_outputs,
                    skill_name,
                    case,
                )
        print(f"✓ {skill_name}: {len(cases)} case(s)")

    print(
        f"Validated {len(paths)} eval contract(s), {total_cases} case(s), "
        f"{design_gate_references} canonical design-gate reference(s)"
    )
    if args.write_smoke_outputs:
        print(f"Smoke outputs written to {args.write_smoke_outputs}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ContractError, yaml.YAMLError) as error:
        print(
            f"eval contract validation failed: {error}",
            file=sys.stderr,
        )
        raise SystemExit(1) from error
