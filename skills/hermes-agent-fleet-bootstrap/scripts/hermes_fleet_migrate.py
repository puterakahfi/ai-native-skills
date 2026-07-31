#!/usr/bin/env python3
"""Backup-first, in-place Hermes profile identity migration."""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

EXIT_OK = 0
EXIT_NEEDS_WORK = 2
EXIT_PREFLIGHT = 3
EXIT_EXECUTION = 4
SAFE_IDENTIFIER = re.compile(r"^[a-z0-9][a-z0-9._-]{0,127}$")
STOPPED_GATEWAY_STATES = {
    "stopped",
    "disabled",
    "not configured",
    "not_configured",
    "none",
    "inactive",
}


class MigrationError(RuntimeError):
    pass


@dataclass
class MigrationAction:
    legacy_profile: str
    target_profile: str
    status: str
    detail: str = ""
    gateway_status: str = "NOT_VERIFIED"
    inventory: dict[str, bool] = field(default_factory=dict)
    backup_archive: str | None = None
    commands: list[list[str]] = field(default_factory=list)

    def as_dict(self) -> dict[str, Any]:
        return {
            "legacy_profile": self.legacy_profile,
            "target_profile": self.target_profile,
            "status": self.status,
            "detail": self.detail,
            "gateway_status": self.gateway_status,
            "inventory": self.inventory,
            "backup_archive": self.backup_archive,
            "commands": self.commands,
        }


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def timestamp_slug() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def validate_identifier(value: Any, label: str) -> str:
    if not isinstance(value, str) or not SAFE_IDENTIFIER.fullmatch(value):
        raise MigrationError(
            f"Unsafe {label}: {value!r}; use lowercase letters, digits, dot, underscore, or hyphen"
        )
    return value


def load_json(path: Path, label: str) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise MigrationError(f"{label} not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise MigrationError(f"Invalid {label} JSON {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise MigrationError(f"{label} root must be an object: {path}")
    return data


def default_skills_root() -> Path:
    return Path(__file__).resolve().parents[2]


def default_preset_path(name: str) -> Path:
    return Path(__file__).resolve().parents[1] / "assets" / "presets" / f"{name}.json"


def default_identity_map_path(name: str) -> Path:
    return (
        Path(__file__).resolve().parents[1]
        / "assets"
        / "profile-identity-maps"
        / f"{name}-v1-to-v2.json"
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="hermes-fleet-migrate")
    parser.add_argument("preset")
    parser.add_argument("--apply", action="store_true", help="Execute migration; default is plan-only")
    parser.add_argument(
        "--stop-gateways",
        action="store_true",
        help="Explicitly stop running legacy gateways before rename",
    )
    parser.add_argument(
        "--skip-export",
        action="store_true",
        help="Skip profile export archives; native rename still preserves the profile directory",
    )
    parser.add_argument(
        "--skip-reconcile",
        action="store_true",
        help="Skip managed-skill reconciliation and report a limitation",
    )
    parser.add_argument("--preset-file", type=Path)
    parser.add_argument("--identity-map-file", type=Path)
    parser.add_argument("--skills-root", type=Path, default=default_skills_root())
    parser.add_argument(
        "--hermes-home",
        type=Path,
        default=Path(os.environ.get("HERMES_HOME", "~/.hermes")).expanduser(),
    )
    parser.add_argument("--hermes-bin", default="hermes")
    parser.add_argument("--receipt", type=Path)
    parser.add_argument("--backup-dir", type=Path)
    parser.add_argument("--json", action="store_true", dest="json_output")
    return parser


def resolve_executable(value: str) -> str | None:
    if os.path.sep in value:
        path = Path(value).expanduser()
        return str(path) if path.is_file() and os.access(path, os.X_OK) else None
    return shutil.which(value)


def run_command(command: list[str], env: dict[str, str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, text=True, capture_output=True, check=False, env=env)


def validate_contracts(
    preset_name: str,
    preset: dict[str, Any],
    identity_map: dict[str, Any],
) -> list[dict[str, Any]]:
    if preset.get("id") != preset_name:
        raise MigrationError(
            f"Preset ID mismatch: requested {preset_name}, file declares {preset.get('id')}"
        )
    if identity_map.get("fleet") != preset_name:
        raise MigrationError(
            f"Identity map fleet mismatch: requested {preset_name}, map declares {identity_map.get('fleet')}"
        )
    if preset.get("identity_generation") != 2:
        raise MigrationError("Migration requires a generation-2 target preset")
    if identity_map.get("from_preset_major") != 1 or identity_map.get("to_preset_major") != 2:
        raise MigrationError("Identity map must declare the v1-to-v2 transition")

    profiles = preset.get("profiles")
    mappings = identity_map.get("mappings")
    legacy_ids = preset.get("legacy_profile_ids")
    if not isinstance(profiles, list) or not profiles:
        raise MigrationError("Preset profiles must be a non-empty list")
    if not isinstance(mappings, list) or not mappings:
        raise MigrationError("Identity map mappings must be a non-empty list")
    if not isinstance(legacy_ids, list) or not legacy_ids:
        raise MigrationError("Target preset must declare legacy_profile_ids")

    target_ids: list[str] = []
    descriptions: dict[str, str] = {}
    for profile in profiles:
        if not isinstance(profile, dict):
            raise MigrationError("Each target profile must be an object")
        target = validate_identifier(profile.get("id"), "target profile id")
        description = profile.get("description")
        if not isinstance(description, str) or not description.strip():
            raise MigrationError(f"Target profile description missing: {target}")
        target_ids.append(target)
        descriptions[target] = description.strip()

    normalized: list[dict[str, Any]] = []
    mapped_legacy: list[str] = []
    mapped_target: list[str] = []
    for item in mappings:
        if not isinstance(item, dict):
            raise MigrationError("Each identity mapping must be an object")
        legacy = validate_identifier(item.get("legacy_profile"), "legacy profile id")
        target = validate_identifier(item.get("target_profile"), "target profile id")
        if legacy == target:
            raise MigrationError(f"Identity mapping must change the profile ID: {legacy}")
        mapped_legacy.append(legacy)
        mapped_target.append(target)
        normalized.append(
            {
                **item,
                "legacy_profile": legacy,
                "target_profile": target,
                "description": descriptions.get(target),
            }
        )

    if len(mapped_legacy) != len(set(mapped_legacy)):
        raise MigrationError("Legacy profile mappings must be one-to-one")
    if len(mapped_target) != len(set(mapped_target)):
        raise MigrationError("Target profile mappings must be one-to-one")
    if mapped_legacy != legacy_ids:
        raise MigrationError("Identity map legacy order must exactly match preset legacy_profile_ids")
    if mapped_target != target_ids:
        raise MigrationError("Identity map target order must exactly match preset profiles")
    if any(item["description"] is None for item in normalized):
        raise MigrationError("Every target mapping must resolve to a preset description")
    return normalized


def assert_safe_profile_path(path: Path, label: str) -> None:
    if path.is_symlink():
        raise MigrationError(f"Symlinked {label} is not allowed: {path}")
    if path.exists() and not path.is_dir():
        raise MigrationError(f"{label} must be a directory: {path}")


def inventory_profile(profile_dir: Path) -> dict[str, bool]:
    probes = {
        "config": ["config.yaml"],
        "environment": [".env"],
        "auth": ["auth.json"],
        "soul": ["SOUL.md"],
        "profile_metadata": ["profile.yaml"],
        "skills": ["skills"],
        "memory": ["memory", "memories", "MEMORY.md"],
        "sessions": ["sessions"],
        "cron": ["cron", "cron_jobs.json"],
        "state_database": ["state.db", "hermes.db"],
        "gateway_state": ["gateway.pid", "gateway", "logs/gateway.log"],
        "kanban_reference": ["kanban.db", "kanban"],
    }
    return {
        key: any((profile_dir / candidate).exists() for candidate in candidates)
        for key, candidates in probes.items()
    }


def classify_actions(
    mappings: list[dict[str, Any]],
    profiles_root: Path,
) -> tuple[list[MigrationAction], str, list[str]]:
    if profiles_root.is_symlink():
        raise MigrationError(f"Symlinked Hermes profiles root is not allowed: {profiles_root}")
    if profiles_root.exists() and not profiles_root.is_dir():
        raise MigrationError(f"Hermes profiles root must be a directory: {profiles_root}")

    actions: list[MigrationAction] = []
    findings: list[str] = []
    legacy_count = target_count = conflict_count = missing_count = 0

    for mapping in mappings:
        legacy = mapping["legacy_profile"]
        target = mapping["target_profile"]
        legacy_dir = profiles_root / legacy
        target_dir = profiles_root / target
        assert_safe_profile_path(legacy_dir, "legacy profile directory")
        assert_safe_profile_path(target_dir, "target profile directory")
        legacy_exists = legacy_dir.exists()
        target_exists = target_dir.exists()

        if legacy_exists and target_exists:
            conflict_count += 1
            findings.append(f"both_profiles_present:{legacy}:{target}")
            status = "BLOCKED_BOTH_PRESENT"
            inventory = inventory_profile(legacy_dir)
        elif legacy_exists:
            legacy_count += 1
            status = "PLAN_NATIVE_RENAME"
            inventory = inventory_profile(legacy_dir)
        elif target_exists:
            target_count += 1
            status = "SKIP_ALREADY_MIGRATED"
            inventory = inventory_profile(target_dir)
        else:
            missing_count += 1
            findings.append(f"both_profiles_missing:{legacy}:{target}")
            status = "BLOCKED_BOTH_MISSING"
            inventory = {}

        actions.append(
            MigrationAction(
                legacy_profile=legacy,
                target_profile=target,
                status=status,
                detail="Native Hermes rename preserves the existing profile directory in place.",
                inventory=inventory,
            )
        )

    if conflict_count or missing_count:
        state = "BLOCKED_AMBIGUOUS"
    elif legacy_count == len(actions):
        state = "LEGACY_ONLY_COMPLETE"
    elif target_count == len(actions):
        state = "TARGET_ONLY_COMPLETE"
    elif legacy_count and target_count:
        state = "MIXED_RESUMABLE"
    else:
        state = "EMPTY"
    return actions, state, findings


def profile_gateway_status(
    hermes_binary: str,
    profile: str,
    env: dict[str, str],
) -> tuple[str, list[str]]:
    command = [hermes_binary, "profile", "show", profile]
    result = run_command(command, env)
    if result.returncode != 0:
        return "NOT_VERIFIED", command
    text = "\n".join([result.stdout, result.stderr])
    for line in text.splitlines():
        if line.strip().lower().startswith("gateway:"):
            value = line.split(":", 1)[1].strip().lower()
            return value or "NOT_VERIFIED", command
    return "NOT_VERIFIED", command


def gateway_is_stopped(status: str) -> bool:
    normalized = status.strip().lower()
    return normalized in STOPPED_GATEWAY_STATES or normalized.startswith("stopped")


def execute_simple(
    command: list[str],
    env: dict[str, str],
) -> tuple[bool, str]:
    result = run_command(command, env)
    return result.returncode == 0, (result.stderr or result.stdout).strip()


def reconcile_skills(
    args: argparse.Namespace,
    preset_path: Path,
    receipt_path: Path,
) -> tuple[bool, list[str], str]:
    runner = Path(__file__).resolve().with_name("hermes_fleet.py")
    command = [
        sys.executable,
        str(runner),
        "reconcile",
        args.preset,
        "--apply",
        "--skip-kanban",
        "--preset-file",
        str(preset_path),
        "--skills-root",
        str(args.skills_root),
        "--hermes-home",
        str(args.hermes_home),
        "--hermes-bin",
        args.hermes_bin,
        "--receipt",
        str(receipt_path),
        "--json",
    ]
    result = run_command(command, os.environ.copy())
    return result.returncode == 0, command, (result.stderr or result.stdout).strip()


def write_receipt(path: Path, receipt: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def render_human(receipt: dict[str, Any]) -> str:
    lines = [
        f"Hermes fleet migration: {receipt['fleet_id']}",
        f"Mode: {receipt['mode']}",
        f"Identity state: {receipt['identity_state']}",
        f"Readiness: {receipt['readiness']}",
        "",
    ]
    for action in receipt["actions"]:
        lines.append(
            f"- {action['legacy_profile']} -> {action['target_profile']}: {action['status']}"
        )
    if receipt["findings"]:
        lines.extend(["", "Findings:"])
        lines.extend(f"- {finding}" for finding in receipt["findings"])
    lines.extend(["", f"Receipt: {receipt['receipt_path']}"])
    return "\n".join(lines)


def main(argv: Iterable[str] | None = None) -> int:
    args = build_parser().parse_args(list(argv) if argv is not None else None)
    preset_path = args.preset_file or default_preset_path(args.preset)
    identity_map_path = args.identity_map_file or default_identity_map_path(args.preset)
    receipt_root = (
        args.hermes_home / "fleet-bootstrap"
        if args.apply
        else Path.cwd() / ".evidence" / "hermes-fleet"
    )
    receipt_path = args.receipt or (
        receipt_root / args.preset / "last-migration-receipt.json"
    )
    backup_dir = args.backup_dir or (
        args.hermes_home
        / "fleet-bootstrap"
        / args.preset
        / "migration-backups"
        / timestamp_slug()
    )

    receipt: dict[str, Any] = {
        "schema_version": "1.0.0",
        "generated_at": utc_now(),
        "fleet_id": args.preset,
        "mode": "APPLY" if args.apply else "PLAN_ONLY",
        "identity_state": "NOT_VERIFIED",
        "migration_strategy": "NATIVE_IN_PLACE_RENAME",
        "preset_path": str(preset_path),
        "identity_map_path": str(identity_map_path),
        "hermes_home": str(args.hermes_home),
        "hermes_version": "NOT_VERIFIED",
        "actions": [],
        "findings": [],
        "profiles_renamed": [],
        "profiles_preserved": [],
        "backup_archives": [],
        "credentials_copied": False,
        "live_state_copied": False,
        "live_state_preserved_in_place": True,
        "legacy_profiles_deleted": False,
        "gateway_started": False,
        "gateway_transition": "PRESERVE_STOPPED_IN_PLACE",
        "managed_skill_reconcile": "NOT_RUN",
        "reconcile_receipt": None,
        "rollback": {
            "automatic": False,
            "strategy": "hermes profile rename <target> <legacy>; use export archive for non-secret profile restore",
        },
        "readiness": "NOT_VERIFIED",
        "runtime_execution": "NOT_RUN",
        "receipt_path": str(receipt_path),
    }

    exit_code = EXIT_OK
    actions: list[MigrationAction] = []
    try:
        preset = load_json(preset_path, "preset")
        identity_map = load_json(identity_map_path, "identity map")
        mappings = validate_contracts(args.preset, preset, identity_map)
        profiles_root = args.hermes_home.resolve() / "profiles"
        actions, state, findings = classify_actions(mappings, profiles_root)
        receipt["identity_state"] = state
        receipt["findings"].extend(findings)

        if any(action.status.startswith("BLOCKED") for action in actions):
            receipt["readiness"] = "BLOCKED"
            exit_code = EXIT_PREFLIGHT
        elif not args.apply:
            receipt["readiness"] = (
                "READY_WITH_LIMITATIONS"
                if state == "TARGET_ONLY_COMPLETE"
                else "READY_TO_APPLY"
            )
            if state == "TARGET_ONLY_COMPLETE":
                receipt["findings"].append("fleet_already_migrated")
        else:
            hermes_binary = resolve_executable(args.hermes_bin)
            if not hermes_binary:
                raise MigrationError(f"Hermes binary not found: {args.hermes_bin}")
            env = os.environ.copy()
            env["HERMES_HOME"] = str(args.hermes_home)
            version = run_command([hermes_binary, "--version"], env)
            if version.returncode != 0:
                raise MigrationError("Hermes version check failed")
            receipt["hermes_version"] = version.stdout.strip() or version.stderr.strip()
            mapping_by_target = {item["target_profile"]: item for item in mappings}

            for action in actions:
                if action.status == "SKIP_ALREADY_MIGRATED":
                    receipt["profiles_preserved"].append(action.target_profile)
                    continue
                if action.status != "PLAN_NATIVE_RENAME":
                    continue

                status, show_command = profile_gateway_status(
                    hermes_binary, action.legacy_profile, env
                )
                action.gateway_status = status
                action.commands.append(show_command)
                if not gateway_is_stopped(status):
                    if not args.stop_gateways:
                        action.status = "BLOCKED_GATEWAY_NOT_STOPPED"
                        action.detail = (
                            f"Gateway status is {status!r}; rerun with --stop-gateways "
                            "or stop it manually before migration"
                        )
                        receipt["findings"].append(
                            f"gateway_not_stopped:{action.legacy_profile}:{status}"
                        )
                        receipt["readiness"] = "BLOCKED"
                        exit_code = EXIT_PREFLIGHT
                        break
                    stop_command = [
                        hermes_binary,
                        "-p",
                        action.legacy_profile,
                        "gateway",
                        "stop",
                    ]
                    stopped, detail = execute_simple(stop_command, env)
                    action.commands.append(stop_command)
                    if not stopped:
                        action.status = "FAILED_GATEWAY_STOP"
                        action.detail = detail
                        receipt["findings"].append(
                            f"gateway_stop_failed:{action.legacy_profile}"
                        )
                        receipt["readiness"] = "BLOCKED"
                        exit_code = EXIT_EXECUTION
                        break
                    status, show_command = profile_gateway_status(
                        hermes_binary, action.legacy_profile, env
                    )
                    action.gateway_status = status
                    action.commands.append(show_command)
                    if not gateway_is_stopped(status):
                        action.status = "FAILED_GATEWAY_VERIFY"
                        receipt["findings"].append(
                            f"gateway_still_not_stopped:{action.legacy_profile}:{status}"
                        )
                        receipt["readiness"] = "BLOCKED"
                        exit_code = EXIT_EXECUTION
                        break

                if not args.skip_export:
                    archive = backup_dir / f"{action.legacy_profile}.tar.gz"
                    archive.parent.mkdir(parents=True, exist_ok=True)
                    export_command = [
                        hermes_binary,
                        "profile",
                        "export",
                        action.legacy_profile,
                        "-o",
                        str(archive),
                    ]
                    exported, detail = execute_simple(export_command, env)
                    action.commands.append(export_command)
                    if not exported or not archive.is_file():
                        action.status = "FAILED_EXPORT"
                        action.detail = detail
                        receipt["findings"].append(
                            f"profile_export_failed:{action.legacy_profile}"
                        )
                        receipt["readiness"] = "BLOCKED"
                        exit_code = EXIT_EXECUTION
                        break
                    action.backup_archive = str(archive)
                    receipt["backup_archives"].append(str(archive))
                else:
                    receipt["findings"].append(
                        f"profile_export_skipped:{action.legacy_profile}"
                    )

                rename_command = [
                    hermes_binary,
                    "profile",
                    "rename",
                    action.legacy_profile,
                    action.target_profile,
                ]
                renamed, detail = execute_simple(rename_command, env)
                action.commands.append(rename_command)
                if not renamed:
                    action.status = "FAILED_RENAME"
                    action.detail = detail
                    receipt["findings"].append(
                        f"profile_rename_failed:{action.legacy_profile}:{action.target_profile}"
                    )
                    receipt["readiness"] = "BLOCKED"
                    exit_code = EXIT_EXECUTION
                    break

                legacy_dir = profiles_root / action.legacy_profile
                target_dir = profiles_root / action.target_profile
                if legacy_dir.exists() or not target_dir.is_dir():
                    action.status = "FAILED_RENAME_VERIFY"
                    receipt["findings"].append(
                        f"profile_rename_verify_failed:{action.legacy_profile}:{action.target_profile}"
                    )
                    receipt["readiness"] = "BLOCKED"
                    exit_code = EXIT_EXECUTION
                    break

                description = mapping_by_target[action.target_profile]["description"]
                describe_command = [
                    hermes_binary,
                    "profile",
                    "describe",
                    action.target_profile,
                    "--text",
                    description,
                ]
                described, detail = execute_simple(describe_command, env)
                action.commands.append(describe_command)
                if not described:
                    receipt["findings"].append(
                        f"profile_description_update_failed:{action.target_profile}"
                    )
                    action.detail = detail
                action.status = "RENAMED_IN_PLACE"
                action.inventory = inventory_profile(target_dir)
                receipt["profiles_renamed"].append(
                    {
                        "legacy_profile": action.legacy_profile,
                        "target_profile": action.target_profile,
                    }
                )

            if exit_code == EXIT_OK:
                if args.skip_reconcile:
                    receipt["managed_skill_reconcile"] = "SKIPPED"
                    receipt["findings"].append("managed_skill_reconcile_skipped")
                else:
                    reconcile_receipt = (
                        args.hermes_home
                        / "fleet-bootstrap"
                        / args.preset
                        / "migration-reconcile-receipt.json"
                    )
                    reconciled, command, detail = reconcile_skills(
                        args, preset_path, reconcile_receipt
                    )
                    receipt["reconcile_receipt"] = str(reconcile_receipt)
                    receipt["reconcile_command"] = command
                    receipt["managed_skill_reconcile"] = "PASS" if reconciled else "FAILED"
                    if not reconciled:
                        receipt["findings"].append("managed_skill_reconcile_failed")
                        receipt["reconcile_detail"] = detail
                        exit_code = EXIT_EXECUTION
                receipt["runtime_execution"] = "EXECUTED"
                receipt["readiness"] = (
                    "READY"
                    if exit_code == EXIT_OK and not receipt["findings"]
                    else "READY_WITH_LIMITATIONS"
                )
    except MigrationError as exc:
        receipt["findings"].append(str(exc))
        receipt["readiness"] = "BLOCKED"
        exit_code = EXIT_PREFLIGHT
    except Exception as exc:
        receipt["findings"].append(f"unexpected_error:{type(exc).__name__}:{exc}")
        receipt["readiness"] = "BLOCKED"
        exit_code = EXIT_EXECUTION

    receipt["actions"] = [action.as_dict() for action in actions]
    try:
        write_receipt(receipt_path, receipt)
    except OSError as exc:
        print(f"ERROR: could not write migration receipt: {exc}", file=sys.stderr)
        return EXIT_EXECUTION

    if args.json_output:
        print(json.dumps(receipt, indent=2, sort_keys=True))
    else:
        print(render_human(receipt))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
