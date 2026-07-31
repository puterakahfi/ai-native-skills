#!/usr/bin/env python3
"""Generation-2 identity guard for Hermes fleet model-policy synchronization."""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import hermes_fleet_model_sync as base


SyncError = base.SyncError
EXIT_OK = base.EXIT_OK
EXIT_PREFLIGHT = base.EXIT_PREFLIGHT
EXIT_EXECUTION = base.EXIT_EXECUTION


def validate_v2_identity_state(args: Any) -> dict[str, Any]:
    preset_path = args.preset_file or base.default_preset_path(args.preset)
    preset = base.load_json_mapping(preset_path, "preset")
    if preset.get("id") != args.preset:
        raise SyncError(f"Preset id mismatch: expected {args.preset!r}")
    if preset.get("identity_generation") != 2:
        raise SyncError("Model sync requires the generation-2 agent profile preset")

    raw_profiles = preset.get("profiles")
    if not isinstance(raw_profiles, list) or not raw_profiles:
        raise SyncError("Preset profiles must be a non-empty list")
    target_ids: list[str] = []
    for item in raw_profiles:
        if not isinstance(item, dict) or not isinstance(item.get("id"), str):
            raise SyncError("Every preset profile must have an id")
        target_ids.append(base.validate_identifier(item["id"], "profile identifier"))

    legacy_ids = preset.get("legacy_profile_ids", [])
    if not isinstance(legacy_ids, list) or not all(isinstance(item, str) for item in legacy_ids):
        raise SyncError("legacy_profile_ids must be a string list")
    legacy_ids = [base.validate_identifier(item, "legacy profile identifier") for item in legacy_ids]

    hermes_home_input = args.hermes_home.expanduser()
    base.reject_symlink(hermes_home_input, "Hermes home")
    hermes_home = hermes_home_input.resolve(strict=False)
    profiles_root = hermes_home / "profiles"
    base.reject_symlink(profiles_root, "Hermes profiles root")

    legacy_present = [profile for profile in legacy_ids if (profiles_root / profile).exists()]
    if legacy_present:
        raise SyncError(
            "Legacy profile identities remain; run fleet migration before sync-models: "
            + ", ".join(legacy_present)
        )

    target_missing = [profile for profile in target_ids if not (profiles_root / profile).is_dir()]
    if target_missing:
        raise SyncError(
            "Target agent profiles are incomplete; migrate or reconcile before sync-models: "
            + ", ".join(target_missing)
        )

    return {
        "identity_generation": 2,
        "target_profile_ids": target_ids,
        "legacy_profile_ids_present": [],
        "identity_state": "TARGET_ONLY_COMPLETE",
    }


def execute(args: Any) -> tuple[int, dict[str, Any]]:
    identity = validate_v2_identity_state(args)
    code, receipt = base.execute(args)
    receipt.update(identity)
    receipt["migration_required"] = False
    receipt_path = Path(receipt["receipt_path"])
    receipt_path.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    return code, receipt


def blocked_receipt(args: Any, finding: str) -> dict[str, Any]:
    return {
        "schema_version": "1.1",
        "operation": "sync_model_policy",
        "mode": "APPLY" if args.apply else "PLAN_ONLY",
        "identity_generation": 2,
        "identity_state": "NOT_VERIFIED",
        "migration_required": "Legacy profile identities remain" in finding,
        "readiness": "BLOCKED",
        "credentials_copied": False,
        "findings": [finding],
        "completed_at": datetime.now(timezone.utc).isoformat(),
    }


def main(argv: list[str] | None = None) -> int:
    args = base.parse_args(argv or sys.argv[1:])
    try:
        code, receipt = execute(args)
    except SyncError as exc:
        receipt = blocked_receipt(args, str(exc))
        if args.json_output:
            print(json.dumps(receipt, indent=2))
        else:
            print(f"BLOCKED: {exc}", file=sys.stderr)
        return EXIT_PREFLIGHT
    except Exception as exc:
        receipt = blocked_receipt(args, f"execution_error:{exc}")
        if args.json_output:
            print(json.dumps(receipt, indent=2))
        else:
            print(f"FAILED: {exc}", file=sys.stderr)
        return EXIT_EXECUTION

    if args.json_output:
        print(json.dumps(receipt, indent=2))
    else:
        for action in receipt["actions"]:
            print(f"{action['status']:12} {action['profile']}")
        print(f"Receipt: {receipt['receipt_path']}")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
