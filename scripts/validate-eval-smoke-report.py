#!/usr/bin/env python3
"""Validate an eval smoke report against explicit expected classifications."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any

import yaml

ALLOWED_CLASSIFICATIONS = {"APPLIED", "PARTIAL", "GHOST", "INCOMPLETE"}


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return value


def load_yaml(path: Path) -> dict[str, Any]:
    value = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a YAML mapping")
    return value


def expected_map(document: dict[str, Any]) -> tuple[str, dict[tuple[str, str], str]]:
    if document.get("schema_version") != 1:
        raise ValueError("expectations schema_version must be 1")

    default = str(document.get("default_classification", "APPLIED")).strip()
    if default not in ALLOWED_CLASSIFICATIONS:
        raise ValueError(f"invalid default classification: {default}")

    raw = document.get("expected_classifications", {})
    if not isinstance(raw, dict):
        raise ValueError("expected_classifications must be a mapping")

    result: dict[tuple[str, str], str] = {}
    for skill, cases in raw.items():
        if not isinstance(skill, str) or not skill.strip():
            raise ValueError("expected skill ids must be non-empty strings")
        if not isinstance(cases, dict):
            raise ValueError(f"expected_classifications.{skill} must be a mapping")
        for case_id, classification in cases.items():
            if not isinstance(case_id, str) or not case_id.strip():
                raise ValueError(f"{skill} case ids must be non-empty strings")
            normalized = str(classification).strip()
            if normalized not in ALLOWED_CLASSIFICATIONS:
                raise ValueError(
                    f"invalid expected classification for {skill}/{case_id}: {normalized}"
                )
            key = (skill, case_id)
            if key in result:
                raise ValueError(f"duplicate expectation: {skill}/{case_id}")
            result[key] = normalized
    return default, result


def observed_map(report: dict[str, Any]) -> dict[tuple[str, str], str]:
    skills = report.get("skills")
    if not isinstance(skills, list):
        raise ValueError("report.skills must be a list")

    result: dict[tuple[str, str], str] = {}
    for skill_record in skills:
        if not isinstance(skill_record, dict):
            raise ValueError("each report skill must be an object")
        skill = str(skill_record.get("skill", "")).strip()
        if not skill:
            raise ValueError("report skill id is missing")
        cases = skill_record.get("cases")
        if not isinstance(cases, list):
            raise ValueError(f"report cases missing for {skill}")
        for case in cases:
            if not isinstance(case, dict):
                raise ValueError(f"invalid case record for {skill}")
            case_id = str(case.get("id", "")).strip()
            classification = str(case.get("classification", "")).strip()
            if not case_id:
                raise ValueError(f"case id missing for {skill}")
            if classification not in ALLOWED_CLASSIFICATIONS:
                raise ValueError(
                    f"invalid observed classification for {skill}/{case_id}: {classification}"
                )
            key = (skill, case_id)
            if key in result:
                raise ValueError(f"duplicate observed case: {skill}/{case_id}")
            result[key] = classification
    return result


def validate(
    report: dict[str, Any],
    expectations: dict[str, Any],
) -> list[str]:
    default, explicit = expected_map(expectations)
    observed = observed_map(report)
    failures: list[str] = []

    unknown_expectations = sorted(set(explicit) - set(observed))
    for skill, case_id in unknown_expectations:
        failures.append(f"expected case is absent: {skill}/{case_id}")

    for key, actual in sorted(observed.items()):
        expected = explicit.get(key, default)
        if actual != expected:
            failures.append(
                f"classification mismatch for {key[0]}/{key[1]}: "
                f"expected {expected}, got {actual}"
            )

    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", required=True, type=Path)
    parser.add_argument("--expectations", required=True, type=Path)
    args = parser.parse_args()

    try:
        report = load_json(args.report)
        expectations = load_yaml(args.expectations)
        failures = validate(report, expectations)
        observed = observed_map(report)
    except (OSError, ValueError, json.JSONDecodeError, yaml.YAMLError) as error:
        print(f"ERROR — {error}")
        return 2

    counts = Counter(observed.values())
    print(
        "Observed classifications: "
        + ", ".join(
            f"{classification}={counts.get(classification, 0)}"
            for classification in sorted(ALLOWED_CLASSIFICATIONS)
        )
    )

    if failures:
        for failure in failures:
            print(f"FAIL — {failure}")
        return 1

    print(f"PASS — {len(observed)} eval cases match explicit smoke expectations.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
