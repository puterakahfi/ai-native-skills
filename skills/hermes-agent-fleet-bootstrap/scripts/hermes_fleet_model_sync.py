#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import re
import shutil
import stat
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

EXIT_OK = 0
EXIT_PREFLIGHT = 3
EXIT_EXECUTION = 4
IDENTIFIER = re.compile(r"^[a-z0-9._-]+$")
MANAGED_KEYS = (
    "model",
    "auxiliary",
    "fallback_providers",
    "fallback_model",
    "model_aliases",
    "provider_routing",
    "credential_pool_strategies",
)
SECRET_MARKERS = (
    "api_key",
    "apikey",
    "token",
    "password",
    "secret",
    "authorization",
    "credential",
)


class SyncError(RuntimeError):
    pass


def package_root() -> Path:
    return Path(__file__).resolve().parents[1]


def default_preset_path(name: str) -> Path:
    return package_root() / "assets" / "presets" / f"{name}.json"


def validate_identifier(value: str, label: str) -> str:
    if not IDENTIFIER.fullmatch(value):
        raise SyncError(f"Unsafe {label}: {value!r}")
    return value


def reject_symlink(path: Path, label: str) -> None:
    if path.is_symlink():
        raise SyncError(f"Symlinked {label} is not allowed: {path}")


def load_json_mapping(path: Path, label: str) -> dict[str, Any]:
    reject_symlink(path, label)
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise SyncError(f"Missing {label}: {path}") from exc
    except json.JSONDecodeError as exc:
        raise SyncError(f"Invalid JSON in {label}: {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise SyncError(f"{label} must be a mapping: {path}")
    return value


def load_yaml_mapping(path: Path, label: str, *, missing_ok: bool = False) -> dict[str, Any]:
    reject_symlink(path, label)
    if not path.exists():
        if missing_ok:
            return {}
        raise SyncError(f"Missing {label}: {path}")
    try:
        value = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        raise SyncError(f"Invalid YAML in {label}: {path}: {exc}") from exc
    if value is None:
        return {}
    if not isinstance(value, dict):
        raise SyncError(f"{label} must be a mapping: {path}")
    return value


def is_secret_key(key: object) -> bool:
    normalized = str(key).strip().lower().replace("-", "_")
    return any(marker in normalized for marker in SECRET_MARKERS)


def sanitize_policy(source: Any, target: Any) -> Any:
    """Copy source policy while preserving target-side secret fields.

    Secret-looking keys are never copied from the source profile. If a target
    already has such a key, its existing value is retained in place.
    """
    if isinstance(source, dict):
        target_map = target if isinstance(target, dict) else {}
        result: dict[Any, Any] = {}
        for key, source_value in source.items():
            if is_secret_key(key):
                if key in target_map:
                    result[key] = copy.deepcopy(target_map[key])
                continue
            result[key] = sanitize_policy(source_value, target_map.get(key))
        for key, target_value in target_map.items():
            if key not in source and is_secret_key(key):
                result[key] = copy.deepcopy(target_value)
        return result
    if isinstance(source, list):
        target_list = target if isinstance(target, list) else []
        return [
            sanitize_policy(
                item, target_list[index] if index < len(target_list) else None
            )
            for index, item in enumerate(source)
        ]
    return copy.deepcopy(source)


def extract_secrets(value: Any) -> Any:
    if isinstance(value, dict):
        result: dict[Any, Any] = {}
        for key, child in value.items():
            if is_secret_key(key):
                result[key] = copy.deepcopy(child)
                continue
            nested = extract_secrets(child)
            if nested not in ({}, [], None):
                result[key] = nested
        return result
    if isinstance(value, list):
        result = [extract_secrets(item) for item in value]
        return [item for item in result if item not in ({}, [], None)]
    return None


def policy_from_config(source: dict[str, Any], target: dict[str, Any]) -> dict[str, Any]:
    updated = copy.deepcopy(target)
    for key in MANAGED_KEYS:
        if key in source:
            updated[key] = sanitize_policy(source[key], target.get(key))
        elif key in updated:
            secrets_only = extract_secrets(updated[key])
            if secrets_only not in ({}, [], None):
                updated[key] = secrets_only
            else:
                updated.pop(key, None)
    return updated


def canonical_policy(config: dict[str, Any]) -> dict[str, Any]:
    return {key: config[key] for key in MANAGED_KEYS if key in config}


def digest(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def validate_source_model(source: dict[str, Any]) -> None:
    model = source.get("model")
    if isinstance(model, str):
        if model.strip():
            return
        raise SyncError("Source profile model is not configured")
    if isinstance(model, dict) and model:
        return
    raise SyncError("Source profile model is not configured")


def atomic_write_yaml(path: Path, value: dict[str, Any], mode: int) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    reject_symlink(path.parent, "target profile directory")
    with tempfile.NamedTemporaryFile(
        "w",
        encoding="utf-8",
        dir=path.parent,
        prefix=".config.yaml.model-sync.",
        delete=False,
    ) as handle:
        yaml.safe_dump(value, handle, sort_keys=False, allow_unicode=True)
        temporary = Path(handle.name)
    os.chmod(temporary, stat.S_IMODE(mode))
    os.replace(temporary, path)


def default_receipt_path(hermes_home: Path, preset: str, apply: bool) -> Path:
    if apply:
        return hermes_home / "fleet-bootstrap" / preset / "last-model-sync-receipt.json"
    return Path(".evidence") / "hermes-fleet" / preset / "last-model-sync-receipt.json"


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="hermes-fleet-model-sync")
    parser.add_argument("preset")
    parser.add_argument("--apply", action="store_true", help="Apply changes; default is plan-only")
    parser.add_argument("--preset-file", type=Path)
    parser.add_argument(
        "--hermes-home",
        type=Path,
        default=Path(os.environ.get("HERMES_HOME", "~/.hermes")).expanduser(),
    )
    parser.add_argument("--source-profile")
    parser.add_argument("--receipt", type=Path)
    parser.add_argument("--json", action="store_true", dest="json_output")
    return parser.parse_args(argv)


def execute(args: argparse.Namespace) -> tuple[int, dict[str, Any]]:
    started = datetime.now(timezone.utc)
    preset_id = validate_identifier(args.preset, "preset identifier")
    preset_path = args.preset_file or default_preset_path(preset_id)
    preset = load_json_mapping(preset_path, "preset")
    if preset.get("id") != preset_id:
        raise SyncError(f"Preset id mismatch: expected {preset_id!r}")

    raw_profiles = preset.get("profiles")
    if not isinstance(raw_profiles, list) or not raw_profiles:
        raise SyncError("Preset profiles must be a non-empty list")

    profile_ids: list[str] = []
    for item in raw_profiles:
        if not isinstance(item, dict) or not isinstance(item.get("id"), str):
            raise SyncError("Every preset profile must have an id")
        profile_id = validate_identifier(item["id"], "profile identifier")
        if profile_id in profile_ids:
            raise SyncError(f"Duplicate profile id in preset: {profile_id}")
        profile_ids.append(profile_id)

    orchestrator = preset.get("orchestrator")
    if not isinstance(orchestrator, str):
        raise SyncError("Preset orchestrator must be a profile identifier")
    orchestrator = validate_identifier(orchestrator, "orchestrator identifier")
    if orchestrator not in profile_ids:
        raise SyncError("Preset orchestrator is not present in profiles")

    source_profile = validate_identifier(
        args.source_profile or orchestrator, "source profile identifier"
    )
    if source_profile not in profile_ids:
        raise SyncError("Source profile is not present in the selected preset")

    hermes_home_input = args.hermes_home.expanduser()
    reject_symlink(hermes_home_input, "Hermes home")
    hermes_home = hermes_home_input.resolve(strict=False)
    profiles_root = hermes_home / "profiles"
    reject_symlink(profiles_root, "Hermes profiles root")

    source_dir = profiles_root / source_profile
    reject_symlink(source_dir, "source profile directory")
    if not source_dir.is_dir():
        raise SyncError(f"Missing source profile directory: {source_dir}")
    source_config_path = source_dir / "config.yaml"
    source_config = load_yaml_mapping(source_config_path, "source profile config")
    validate_source_model(source_config)

    source_policy = canonical_policy(policy_from_config(source_config, {}))
    source_digest = digest(source_policy)
    timestamp = started.strftime("%Y%m%d-%H%M%S")
    actions: list[dict[str, Any]] = []

    for profile_id in profile_ids:
        if profile_id == source_profile:
            continue
        target_dir = profiles_root / profile_id
        reject_symlink(target_dir, "target profile directory")
        if not target_dir.is_dir():
            raise SyncError(f"Missing target profile directory: {target_dir}")
        target_config_path = target_dir / "config.yaml"
        target_config = load_yaml_mapping(
            target_config_path, "target profile config", missing_ok=True
        )
        updated = policy_from_config(source_config, target_config)
        before_digest = digest(
            canonical_policy(policy_from_config(target_config, {}))
        )
        after_digest = digest(canonical_policy(policy_from_config(updated, {})))
        changed = updated != target_config
        action: dict[str, Any] = {
            "profile": profile_id,
            "status": "PLAN_UPDATE" if changed else "SKIP_IN_SYNC",
            "before_digest": before_digest,
            "after_digest": after_digest,
            "backup": None,
        }
        if changed and args.apply:
            if target_config_path.exists():
                reject_symlink(target_config_path, "target profile config")
                backup = target_config_path.with_name(
                    f"config.yaml.bak.model-sync.{timestamp}"
                )
                suffix = 1
                while backup.exists():
                    backup = target_config_path.with_name(
                        f"config.yaml.bak.model-sync.{timestamp}.{suffix}"
                    )
                    suffix += 1
                shutil.copy2(target_config_path, backup)
                action["backup"] = str(backup)
                mode = target_config_path.stat().st_mode
            else:
                mode = 0o600
            atomic_write_yaml(target_config_path, updated, mode)
            action["status"] = "UPDATED" if target_config else "CREATED"
        actions.append(action)

    receipt_path = args.receipt or default_receipt_path(
        hermes_home, preset_id, args.apply
    )
    receipt = {
        "schema_version": "1.0",
        "operation": "sync_model_policy",
        "mode": "APPLY" if args.apply else "PLAN_ONLY",
        "preset": {"id": preset_id, "version": preset.get("version")},
        "source_profile": source_profile,
        "managed_keys": list(MANAGED_KEYS),
        "source_policy_digest": source_digest,
        "credentials_copied": False,
        "actions": actions,
        "readiness": "READY",
        "started_at": started.isoformat(),
        "completed_at": datetime.now(timezone.utc).isoformat(),
        "receipt_path": str(receipt_path),
    }
    receipt_path.parent.mkdir(parents=True, exist_ok=True)
    receipt_path.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    return EXIT_OK, receipt


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    try:
        code, receipt = execute(args)
    except SyncError as exc:
        receipt = {
            "schema_version": "1.0",
            "operation": "sync_model_policy",
            "mode": "APPLY" if args.apply else "PLAN_ONLY",
            "readiness": "BLOCKED",
            "credentials_copied": False,
            "findings": [str(exc)],
        }
        if args.json_output:
            print(json.dumps(receipt, indent=2))
        else:
            print(f"BLOCKED: {exc}", file=sys.stderr)
        return EXIT_PREFLIGHT
    except Exception as exc:  # fail closed with a bounded execution result
        if args.json_output:
            print(
                json.dumps(
                    {
                        "schema_version": "1.0",
                        "operation": "sync_model_policy",
                        "readiness": "BLOCKED",
                        "credentials_copied": False,
                        "findings": [f"execution_error:{exc}"],
                    },
                    indent=2,
                )
            )
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
