#!/usr/bin/env python3
"""Validate repository-wide executable contract coverage and exemptions."""

from __future__ import annotations

import argparse
import datetime as dt
import importlib.util
import subprocess
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker


def load_yaml(path: Path) -> dict[str, Any]:
    payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"{path}: YAML root must be a mapping")
    return payload


def load_inventory_module(root: Path):
    script = root / "scripts/inventory-contract-coverage.py"
    spec = importlib.util.spec_from_file_location("inventory_contract_coverage", script)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {script}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def schema_errors(validator: Draft202012Validator, payload: dict[str, Any]) -> list[str]:
    errors = []
    for error in sorted(validator.iter_errors(payload), key=lambda item: list(item.absolute_path)):
        location = ".".join(str(value) for value in error.absolute_path) or "<root>"
        errors.append(f"schema:{location}:{error.message}")
    return errors


def validate_exemption(
    path: Path,
    root: Path,
    validator: Draft202012Validator,
    inventory_module: Any,
    today: dt.date,
) -> list[str]:
    errors: list[str] = []
    try:
        payload = load_yaml(path)
    except Exception as exc:
        return [f"{rel(path, root)}:invalid_yaml:{exc}"]

    errors.extend(f"{rel(path, root)}:{message}" for message in schema_errors(validator, payload))
    exemption = payload.get("contract_exemption")
    if not isinstance(exemption, dict):
        return errors

    skill_path = path.parent / "SKILL.md"
    if not skill_path.exists():
        errors.append(f"{rel(path, root)}:artifact_path_missing")
        return errors
    frontmatter, frontmatter_errors = inventory_module.parse_frontmatter(skill_path)
    errors.extend(f"{rel(path, root)}:{message}" for message in frontmatter_errors)
    metadata = frontmatter.get("metadata") or {}
    if not isinstance(metadata, dict):
        metadata = {}

    artifact = exemption.get("artifact") or {}
    expected_id = str(frontmatter.get("name") or skill_path.parent.name)
    expected_type = str(inventory_module.namespaced(metadata, "type") or "")
    expected_path = rel(skill_path, root)
    if artifact.get("id") != expected_id:
        errors.append(f"{rel(path, root)}:artifact_id_mismatch:{artifact.get('id')}!={expected_id}")
    if artifact.get("path") != expected_path:
        errors.append(f"{rel(path, root)}:artifact_path_mismatch:{artifact.get('path')}!={expected_path}")
    if artifact.get("type") != expected_type:
        errors.append(f"{rel(path, root)}:artifact_type_mismatch:{artifact.get('type')}!={expected_type}")

    declaration = path.parent / "adapter.conformance.yaml"
    implements = inventory_module.namespaced(metadata, "implements")
    if declaration.exists():
        errors.append(f"{rel(path, root)}:exemption_and_declaration_cannot_coexist")
    if implements:
        errors.append(f"{rel(path, root)}:exemption_and_contract_reference_cannot_coexist")

    classification = exemption.get("classification")
    scope = set(exemption.get("scope") or [])
    blocking_issue = (exemption.get("revisit") or {}).get("blocking_issue")
    if classification == "core_gap":
        if "core_gap_tracking" not in scope:
            errors.append(f"{rel(path, root)}:core_gap_scope_missing")
        if not blocking_issue:
            errors.append(f"{rel(path, root)}:core_gap_blocking_issue_missing")
    elif classification == "provider_specific":
        if "provider_specific_execution" not in scope:
            errors.append(f"{rel(path, root)}:provider_specific_scope_missing")
        if blocking_issue:
            errors.append(f"{rel(path, root)}:provider_exemption_should_not_claim_blocking_core_issue")
    elif classification == "third_party_delegation":
        if "third_party_delegation" not in scope:
            errors.append(f"{rel(path, root)}:third_party_scope_missing")
        if blocking_issue:
            errors.append(f"{rel(path, root)}:third_party_exemption_should_not_claim_blocking_core_issue")

    review_date_raw = exemption.get("review_date")
    try:
        review_date = dt.date.fromisoformat(str(review_date_raw))
    except ValueError:
        errors.append(f"{rel(path, root)}:review_date_invalid:{review_date_raw}")
    else:
        if review_date < today:
            errors.append(f"{rel(path, root)}:review_overdue:{review_date.isoformat()}")

    return errors


def validate_retirement(root: Path) -> list[str]:
    errors: list[str] = []
    migration_path = root / "docs/compatibility-registry-migration.yaml"
    if not migration_path.exists():
        return ["docs/compatibility-registry-migration.yaml:missing"]
    payload = load_yaml(migration_path).get("compatibility_registry_migration") or {}
    for record in payload.get("retired_records", []):
        retired_path = root / str(record.get("path", ""))
        if retired_path.exists():
            errors.append(f"{rel(retired_path, root)}:retired_record_still_active")
    return errors


def tracked_generated_artifacts(root: Path) -> list[str]:
    """Return tracked bytecode/cache artifacts; ignore runner-created untracked caches."""
    result = subprocess.run(
        ["git", "-C", str(root), "ls-files", "-z"],
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.decode("utf-8", errors="replace").strip())
    tracked = [value.decode("utf-8") for value in result.stdout.split(b"\0") if value]
    return sorted(
        path
        for path in tracked
        if "/__pycache__/" in f"/{path}" or path.endswith((".pyc", ".pyo"))
    )


def validate(root: Path, core_root: Path) -> tuple[list[str], dict[str, Any]]:
    errors: list[str] = []
    inventory_module = load_inventory_module(root)
    inventory_document = inventory_module.build_inventory(root, core_root)
    inventory = inventory_document["contract_coverage_inventory"]
    summary = inventory["summary"]

    for artifact in inventory["artifacts"]:
        if artifact["classification"] in {"invalid", "unowned"}:
            errors.append(
                f"{artifact['path']}:{artifact['classification']}:"
                + ",".join(artifact.get("errors") or [])
            )
    if summary["compatibility_manifests_with_errors"]:
        errors.append(
            f"compatibility_manifests_with_errors:{summary['compatibility_manifests_with_errors']}"
        )
    if summary["duplicate_compatibility_ids"]:
        errors.append(f"duplicate_compatibility_ids:{summary['duplicate_compatibility_ids']}")

    rendered = yaml.safe_dump(inventory_document, sort_keys=False, allow_unicode=True)
    report_path = root / "docs/contract-coverage-discovery.yaml"
    if not report_path.exists() or report_path.read_text(encoding="utf-8") != rendered:
        errors.append("docs/contract-coverage-discovery.yaml:stale")

    schema = load_yaml(root / "schemas/contract-exemption.schema.yaml")
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    today = dt.datetime.now(dt.timezone.utc).date()
    exemption_paths = sorted((root / "skills").glob("*/contract.exemption.yaml"))
    for path in exemption_paths:
        errors.extend(validate_exemption(path, root, validator, inventory_module, today))

    expected_exemptions = summary["coverage"].get("reviewed_exemption", 0)
    if expected_exemptions != len(exemption_paths):
        errors.append(
            f"reviewed_exemption_count_mismatch:inventory={expected_exemptions},files={len(exemption_paths)}"
        )

    errors.extend(validate_retirement(root))

    temporary_source = [
        *root.glob(".github/workflows/tmp-*.yml"),
        *root.glob("scripts/tmp-*.py"),
    ]
    for path in temporary_source:
        errors.append(f"temporary_source_artifact:{rel(path, root)}")
    for path in tracked_generated_artifacts(root):
        errors.append(f"tracked_generated_artifact:{path}")

    return sorted(set(errors)), summary


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".")
    parser.add_argument("--core-root", required=True)
    args = parser.parse_args()
    root = Path(args.root).resolve()
    core_root = Path(args.core_root).resolve()
    errors, summary = validate(root, core_root)
    print(yaml.safe_dump(summary, sort_keys=False).strip())
    if errors:
        print("\nContract coverage validation failed:")
        for error in errors:
            print(f"- {error}")
        print(f"\nFAIL — {len(errors)} violation(s).")
        return 1
    print("\nPASS — every executable has a contract reference or valid reviewed exemption; compatibility registry is clean.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
