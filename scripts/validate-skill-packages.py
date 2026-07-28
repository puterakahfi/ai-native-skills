#!/usr/bin/env python3
"""Validate skill package structure and produce a compliance inventory."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]


def load_policy(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    return data["skill_package_policy"]


def parse_skill_type(skill_md: Path) -> str:
    text = skill_md.read_text(encoding="utf-8")
    marker = "ai-native-skills.type:"
    for line in text.splitlines():
        if marker in line:
            return line.split(marker, 1)[1].strip().strip('"\'')
    return "unknown"


def validate(root: Path, policy: dict[str, Any]) -> dict[str, Any]:
    skills_root = root / "skills"
    tests_root = root / policy["behavioral_contract_root"]
    pilots = set(policy.get("pilot_skills", []))
    prohibited = set(policy.get("prohibited", []))
    discouraged = set(policy.get("discouraged", []))
    findings: list[dict[str, str]] = []
    inventory: list[dict[str, Any]] = []

    for skill_dir in sorted(path for path in skills_root.iterdir() if path.is_dir()):
        name = skill_dir.name
        skill_md = skill_dir / "SKILL.md"
        errors = 0
        warnings = 0

        def add(severity: str, rule: str, path: Path, message: str) -> None:
            nonlocal errors, warnings
            findings.append({"skill": name, "severity": severity, "rule": rule, "path": str(path.relative_to(root)), "message": message})
            errors += severity == "ERROR"
            warnings += severity == "WARNING"

        if not skill_md.is_file():
            add("ERROR", "required-skill-md", skill_dir, "Missing required SKILL.md")
            skill_type = "unknown"
        else:
            skill_type = parse_skill_type(skill_md)

        children = {p.name: p for p in skill_dir.iterdir()}
        for entry in sorted(prohibited & children.keys()):
            add("ERROR" if name in pilots else "WARNING", "prohibited-authored-path", children[entry], "Generated or dependency path must not be authored inside a skill package")
        for entry in sorted(discouraged & children.keys()):
            add("WARNING", "discouraged-path", children[entry], "Use references/, repository docs/, or centralized contracts/tests instead")

        contract = tests_root / f"{name}.test.yaml"
        substantive = skill_type in {"workflow", "meta-skill"} or contract.is_file() or (skill_dir / "scripts").is_dir()
        if substantive and not contract.is_file():
            severity = "ERROR" if name in pilots else "WARNING"
            add(severity, "missing-behavioral-contract", contract, "Substantive skill has no canonical behavioral regression contract")

        scripts_dir = skill_dir / "scripts"
        tests_dir = skill_dir / "tests"
        executable_files = []
        if scripts_dir.is_dir():
            executable_files = [p for p in scripts_dir.rglob("*") if p.is_file() and p.suffix in {".py", ".sh", ".js", ".ts", ".go"}]
        if executable_files and not tests_dir.is_dir():
            add("WARNING", "scripts-without-tests", scripts_dir, "Executable resources exist without package-local automated tests")

        status = "COMPLIANT" if errors == 0 and warnings == 0 else ("PARTIALLY_COMPLIANT" if errors == 0 else "NEEDS_MIGRATION")
        inventory.append({"skill": name, "type": skill_type, "substantive": substantive, "behavioral_contract": contract.is_file(), "errors": errors, "warnings": warnings, "status": status})

    return {
        "skill_package_validation": {
            "policy_version": policy["version"],
            "summary": {
                "skills": len(inventory),
                "errors": sum(item["errors"] for item in inventory),
                "warnings": sum(item["warnings"] for item in inventory),
            },
            "inventory": inventory,
            "findings": findings,
        }
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--policy", type=Path)
    parser.add_argument("--report-json", type=Path)
    parser.add_argument("--strict-warnings", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    policy_path = args.policy or root / "contracts/skill-package-policy.yaml"
    report = validate(root, load_policy(policy_path))
    summary = report["skill_package_validation"]["summary"]
    print(json.dumps(summary, indent=2))
    for finding in report["skill_package_validation"]["findings"]:
        print(f"{finding['severity']} {finding['rule']} {finding['path']}: {finding['message']}")
    if args.report_json:
        args.report_json.parent.mkdir(parents=True, exist_ok=True)
        args.report_json.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    if summary["errors"] or (args.strict_warnings and summary["warnings"]):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
