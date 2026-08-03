#!/usr/bin/env python3
"""Deterministic one-command bootstrap for Hermes specialist fleets."""
from __future__ import annotations

import argparse
import hashlib
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
SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")


@dataclass
class Action:
    kind: str
    target: str
    status: str
    detail: str = ""
    command: list[str] = field(default_factory=list)

    def as_dict(self) -> dict[str, Any]:
        return {
            "kind": self.kind,
            "target": self.target,
            "status": self.status,
            "detail": self.detail,
            "command": self.command,
        }


class FleetError(RuntimeError):
    pass


def validate_identifier(value: Any, label: str) -> str:
    if not isinstance(value, str) or not SAFE_IDENTIFIER.fullmatch(value):
        raise FleetError(
            f"Unsafe {label}: {value!r}; use lowercase letters, digits, dot, underscore, or hyphen"
        )
    return value


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise FleetError(f"Preset not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise FleetError(f"Invalid preset JSON {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise FleetError(f"Preset root must be an object: {path}")
    return data


def validate_preset(data: dict[str, Any]) -> None:
    required = {"id", "version", "topology", "orchestrator", "profiles"}
    missing = sorted(required - data.keys())
    if missing:
        raise FleetError(f"Preset missing required fields: {', '.join(missing)}")

    validate_identifier(data["id"], "preset id")
    validate_identifier(data["orchestrator"], "orchestrator id")
    if not isinstance(data["version"], str) or not SEMVER.fullmatch(data["version"]):
        raise FleetError(f"Preset version must be semantic version x.y.z: {data['version']!r}")

    generation = data.get("identity_generation", 1)
    if not isinstance(generation, int) or generation < 1:
        raise FleetError("identity_generation must be a positive integer")

    profiles = data.get("profiles")
    if not isinstance(profiles, list) or not profiles:
        raise FleetError("Preset profiles must be a non-empty list")

    ids: list[str] = []
    for profile in profiles:
        if not isinstance(profile, dict):
            raise FleetError("Each profile must be an object")
        for key in ("id", "description", "gateway", "skills"):
            if key not in profile:
                raise FleetError(f"Profile missing {key}: {profile}")
        if not isinstance(profile["description"], str) or not profile["description"].strip():
            raise FleetError(f"Profile description must be non-empty: {profile.get('id')}")
        if not isinstance(profile["skills"], list) or not all(
            isinstance(item, str) and item for item in profile["skills"]
        ):
            raise FleetError(f"Profile skills must be string list: {profile['id']}")
        validate_identifier(profile["id"], "profile id")
        if profile["gateway"] not in {"eligible", "none"}:
            raise FleetError(
                f"Unsupported gateway policy for {profile['id']}: {profile['gateway']!r}"
            )
        worker_mode = profile.get("worker_mode")
        if worker_mode is not None and worker_mode not in {
            "user_facing_front_door",
            "headless_on_demand",
        }:
            raise FleetError(
                f"Unsupported worker_mode for {profile['id']}: {worker_mode!r}"
            )
        for skill in profile["skills"]:
            validate_identifier(skill, "skill id")
        if len(profile["skills"]) != len(set(profile["skills"])):
            raise FleetError(f"Profile contains duplicate skill IDs: {profile['id']}")
        ids.append(profile["id"])

    if len(ids) != len(set(ids)):
        raise FleetError("Profile IDs must be unique")

    orchestrator = data["orchestrator"]
    if orchestrator not in ids:
        raise FleetError("Orchestrator must reference a declared profile")

    gateway_profiles = [p["id"] for p in profiles if p["gateway"] == "eligible"]
    if gateway_profiles != [orchestrator]:
        raise FleetError(
            "Exactly the orchestrator must be gateway-eligible; specialists must use gateway=none"
        )

    legacy_ids = data.get("legacy_profile_ids", [])
    if not isinstance(legacy_ids, list) or not all(
        isinstance(item, str) and item for item in legacy_ids
    ):
        raise FleetError("legacy_profile_ids must be a string list")
    for profile_id in legacy_ids:
        validate_identifier(profile_id, "legacy profile id")
    if len(legacy_ids) != len(set(legacy_ids)):
        raise FleetError("Legacy profile IDs must be unique")
    overlap = sorted(set(ids) & set(legacy_ids))
    if overlap:
        raise FleetError(
            f"Target and legacy profile IDs must not overlap: {', '.join(overlap)}"
        )
    if legacy_ids and data.get("mixed_identity_policy") != "block_outside_migration":
        raise FleetError(
            "Versioned identity transitions must use mixed_identity_policy=block_outside_migration"
        )


def remove_path(path: Path) -> None:
    """Remove a filesystem node without following directory symlinks."""
    if path.is_symlink() or path.is_file():
        path.unlink()
    elif path.exists():
        shutil.rmtree(path)


def directory_digest(path: Path) -> str:
    digest = hashlib.sha256()
    if path.is_symlink():
        raise FleetError(f"Symlinked managed source path is not allowed: {path}")
    if not path.exists():
        return "MISSING"
    if not path.is_dir():
        raise FleetError(f"Managed path must be a directory: {path}")
    for candidate in sorted(path.rglob("*")):
        if candidate.is_symlink():
            raise FleetError(f"Symlink inside managed skill source is not allowed: {candidate}")
        if not candidate.is_file():
            continue
        if any(part in {"__pycache__", ".git"} for part in candidate.parts):
            continue
        rel = candidate.relative_to(path).as_posix()
        digest.update(rel.encode("utf-8"))
        digest.update(b"\0")
        digest.update(candidate.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def resolve_hermes_binary(value: str) -> str | None:
    if os.path.sep in value:
        path = Path(value).expanduser()
        return str(path) if path.is_file() and os.access(path, os.X_OK) else None
    return shutil.which(value)


def run_command(command: list[str], env: dict[str, str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        text=True,
        capture_output=True,
        check=False,
        env=env,
    )


def atomic_symlink(source: Path, target: Path) -> None:
    """Atomically replace a managed skill path with a symlink to source."""
    source = source.resolve()
    if not source.is_dir() or not (source / "SKILL.md").is_file():
        raise FleetError(f"Skill source is missing SKILL.md: {source}")
    target.parent.mkdir(parents=True, exist_ok=True)
    staged = target.with_name(f".{target.name}.next-link")
    backup = target.with_name(f".{target.name}.previous")
    remove_path(staged)
    remove_path(backup)
    staged.symlink_to(source, target_is_directory=True)
    if target.is_symlink() or target.exists():
        target.rename(backup)
    try:
        staged.rename(target)
    except Exception:
        remove_path(target)
        if backup.exists() or backup.is_symlink():
            backup.rename(target)
        raise
    remove_path(backup)


def skill_target_state(source: Path, target: Path) -> str:
    """Classify a projected profile skill relative to its canonical source."""
    if not target.exists() and not target.is_symlink():
        return "MISSING"
    if target.is_symlink():
        try:
            return "IN_SYNC" if target.resolve(strict=True) == source.resolve(strict=True) else "DRIFT"
        except FileNotFoundError:
            return "DRIFT"
    if not target.is_dir():
        return "DRIFT"
    # Existing copy-style managed skills are intentionally drift: apply converts
    # them to catalog symlinks so `git pull` updates all managed profiles.
    return "DRIFT"


def default_catalog_root() -> Path:
    """Return the canonical ai-native-skills checkout used for fleet projection.

    The durable fleet update model is intentionally simple: profiles symlink their
    managed skills into a fixed catalog clone and `git pull` updates all profiles.
    `HERMES_SKILL_CATALOG_ROOT` exists for tests and non-standard installs, but
    the default must be machine-independent and not a developer checkout like
    /data/www/ai-native-skills.
    """
    configured = os.environ.get("HERMES_SKILL_CATALOG_ROOT")
    if configured:
        return Path(configured).expanduser()
    return _resolve_hermes_home() / "ai-native-skills"


def default_skills_root() -> Path:
    return default_catalog_root() / "skills"


def default_preset_path(name: str) -> Path:
    return Path(__file__).resolve().parents[1] / "assets" / "presets" / f"{name}.json"


def _resolve_hermes_home() -> Path:
    """F7 fix: detect real user's ~/.hermes when running inside an agent sandbox.

    An agent sandbox sets HOME to a profile-scoped path like
    /home/<user>/.hermes/profiles/<profile>/home, so Path("~/.hermes").expanduser()
    would resolve to the sandbox's .hermes, not the real one.

    Resolution order:
    1. HERMES_REAL_HOME env var (explicitly set by caller)
    2. HERMES_HOME env var (standard Hermes convention)
    3. Walk up from CWD to find a real ~/.hermes anchor via LOGNAME/USER
    4. Fallback: ~/.hermes (may be sandboxed — logs a warning)
    """
    # 1. Explicit override
    if real_home := os.environ.get("HERMES_REAL_HOME"):
        return Path(real_home).expanduser()

    # 2. Standard HERMES_HOME
    if hermes_home := os.environ.get("HERMES_HOME"):
        resolved = Path(hermes_home).expanduser()
        # Warn if it looks sandboxed (contains /profiles/ in path)
        if "/profiles/" in str(resolved):
            print(
                f"[hermes-fleet WARNING] HERMES_HOME={resolved} looks sandboxed "
                f"(contains /profiles/). Pass --hermes-home or set HERMES_REAL_HOME "
                f"to point to the real ~/.hermes.",
                file=__import__("sys").stderr,
            )
        return resolved

    # 3. Derive from LOGNAME/USER to get real home
    for env_var in ("LOGNAME", "USER"):
        if username := os.environ.get(env_var):
            candidate = Path(f"/home/{username}/.hermes")
            if candidate.exists():
                return candidate

    # 4. Fallback
    fallback = Path("~/.hermes").expanduser()
    if "/profiles/" in str(fallback):
        print(
            f"[hermes-fleet WARNING] Resolved hermes-home={fallback} looks sandboxed. "
            f"Pass --hermes-home explicitly.",
            file=__import__("sys").stderr,
        )
    return fallback


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="hermes-fleet")
    parser.add_argument("operation", choices=["bootstrap", "audit", "reconcile"])
    parser.add_argument("preset")
    parser.add_argument("--apply", action="store_true", help="Execute mutations; default is plan-only")
    parser.add_argument("--preset-file", type=Path)
    parser.add_argument("--skills-root", type=Path, default=default_skills_root())
    parser.add_argument(
        "--hermes-home",
        type=Path,
        default=_resolve_hermes_home(),
    )
    parser.add_argument("--hermes-bin", default="hermes")
    parser.add_argument("--receipt", type=Path)
    parser.add_argument("--skip-kanban", action="store_true")
    parser.add_argument("--json", action="store_true", dest="json_output")
    return parser


def classify_identity_state(
    preset: dict[str, Any], profiles_root: Path
) -> dict[str, Any]:
    target_ids = [profile["id"] for profile in preset["profiles"]]
    legacy_ids = list(preset.get("legacy_profile_ids", []))

    target_present = [profile_id for profile_id in target_ids if (profiles_root / profile_id).exists()]
    legacy_present = [profile_id for profile_id in legacy_ids if (profiles_root / profile_id).exists()]
    target_missing = [profile_id for profile_id in target_ids if profile_id not in target_present]
    legacy_missing = [profile_id for profile_id in legacy_ids if profile_id not in legacy_present]

    if not legacy_ids:
        state = "UNVERSIONED"
    elif not target_present and not legacy_present:
        state = "EMPTY"
    elif target_present and legacy_present:
        state = "MIXED"
    elif legacy_present:
        state = (
            "LEGACY_ONLY_COMPLETE"
            if len(legacy_present) == len(legacy_ids)
            else "LEGACY_ONLY_PARTIAL"
        )
    else:
        state = (
            "TARGET_ONLY_COMPLETE"
            if len(target_present) == len(target_ids)
            else "TARGET_ONLY_PARTIAL"
        )

    return {
        "state": state,
        "target_profile_ids": target_ids,
        "target_profiles_present": target_present,
        "target_profiles_missing": target_missing,
        "legacy_profile_ids": legacy_ids,
        "legacy_profiles_present": legacy_present,
        "legacy_profiles_missing": legacy_missing,
    }


def identity_action(
    preset: dict[str, Any], identity: dict[str, Any], operation: str
) -> tuple[Action, list[str], bool]:
    state = identity["state"]
    findings: list[str] = []
    blocked = False

    if state == "EMPTY":
        status = "READY_FRESH_BOOTSTRAP"
    elif state == "TARGET_ONLY_COMPLETE":
        status = "TARGET_ONLY"
    elif state == "TARGET_ONLY_PARTIAL":
        status = "TARGET_PARTIAL"
        if operation == "audit":
            findings.append("target_fleet_partial")
    elif state == "LEGACY_ONLY_COMPLETE":
        status = "LEGACY_ONLY"
        findings.append("legacy_fleet_requires_migration")
        blocked = operation != "audit"
    elif state == "LEGACY_ONLY_PARTIAL":
        status = "LEGACY_PARTIAL"
        findings.append("legacy_fleet_partial_requires_migration")
        blocked = operation != "audit"
    elif state == "MIXED":
        status = "MIXED_IDENTITIES"
        findings.append("mixed_identity_fleet_requires_migration")
        blocked = operation != "audit"
    else:
        status = state

    if blocked:
        status = "BLOCKED_" + status

    detail = json.dumps(
        {
            "target_present": identity["target_profiles_present"],
            "target_missing": identity["target_profiles_missing"],
            "legacy_present": identity["legacy_profiles_present"],
        },
        sort_keys=True,
    )
    return Action("identity", preset["id"], status, detail), findings, blocked


def plan_actions(
    preset: dict[str, Any], skills_root: Path, hermes_home: Path, operation: str
) -> tuple[list[Action], list[str], dict[str, Any]]:
    actions: list[Action] = []
    findings: list[str] = []
    profiles_root = hermes_home / "profiles"
    if profiles_root.is_symlink():
        raise FleetError(f"Symlinked Hermes profiles root is not allowed: {profiles_root}")

    identity = classify_identity_state(preset, profiles_root)
    state_action, state_findings, blocked_identity = identity_action(
        preset, identity, operation
    )
    actions.append(state_action)
    findings.extend(state_findings)

    if blocked_identity:
        return actions, findings, identity

    for profile in preset["profiles"]:
        profile_id = profile["id"]
        profile_dir = profiles_root / profile_id
        if profile_dir.is_symlink():
            raise FleetError(f"Symlinked Hermes profile directory is not allowed: {profile_dir}")
        profile_skills_dir = profile_dir / "skills"
        if profile_skills_dir.is_symlink():
            raise FleetError(f"Symlinked profile skills directory is not allowed: {profile_skills_dir}")

        if profile_dir.exists():
            actions.append(Action("profile", profile_id, "SKIP_EXISTS", "Existing profile preserved"))
        else:
            status = "PLAN_CREATE" if operation != "audit" else "MISSING"
            actions.append(Action("profile", profile_id, status, "Profile directory absent"))
            if operation == "audit":
                findings.append(f"missing_profile:{profile_id}")

        # Soul sync planning
        soul_rel = profile.get("soul")
        if soul_rel:
            soul_source = skills_root.parent / soul_rel
            soul_target = profile_dir / "SOUL.md"
            if not soul_source.exists():
                actions.append(Action("soul", profile_id, "BLOCKED_SOURCE_MISSING", f"Soul source missing: {soul_rel}"))
                findings.append(f"missing_soul_source:{profile_id}")
            elif soul_target.exists():
                actions.append(Action("soul", profile_id, "SKIP_EXISTS", "SOUL.md already present (use --force to overwrite)"))
            else:
                status = "PLAN_SYNC" if operation != "audit" else "MISSING"
                actions.append(Action("soul", profile_id, status, f"Source: {soul_rel}"))
                if operation == "audit":
                    findings.append(f"missing_soul:{profile_id}")

        # Config sync planning
        config_rel = profile.get("config")
        if config_rel:
            config_source = skills_root.parent / config_rel
            config_target = profile_dir / "config.yaml"
            if not config_source.exists():
                actions.append(Action("config", profile_id, "BLOCKED_SOURCE_MISSING", f"Config source missing: {config_rel}"))
                findings.append(f"missing_config_source:{profile_id}")
            elif config_target.exists():
                actions.append(Action("config", profile_id, "SKIP_EXISTS", "config.yaml already present (use --force to overwrite)"))
            else:
                status = "PLAN_SYNC" if operation != "audit" else "MISSING"
                actions.append(Action("config", profile_id, status, f"Source: {config_rel}"))
                if operation == "audit":
                    findings.append(f"missing_config:{profile_id}")

        for skill in profile["skills"]:
            source = skills_root / skill
            target = profile_skills_dir / skill
            if source.exists() and not (source / "SKILL.md").is_file():
                actions.append(
                    Action(
                        "skill",
                        f"{profile_id}:{skill}",
                        "BLOCKED_INVALID_SOURCE",
                        "Skill source is missing SKILL.md",
                    )
                )
                findings.append(f"invalid_skill_source:{skill}")
                continue
            source_hash = directory_digest(source)
            target_state = skill_target_state(source, target)
            if source_hash == "MISSING":
                actions.append(Action("skill", f"{profile_id}:{skill}", "BLOCKED_SOURCE_MISSING"))
                findings.append(f"missing_skill_source:{skill}")
            elif target_state == "IN_SYNC":
                actions.append(Action("skill", f"{profile_id}:{skill}", "SKIP_IN_SYNC"))
            elif target_state == "MISSING":
                status = "PLAN_INSTALL" if operation != "audit" else "MISSING"
                actions.append(Action("skill", f"{profile_id}:{skill}", status))
                if operation == "audit":
                    findings.append(f"missing_profile_skill:{profile_id}:{skill}")
            else:
                status = "PLAN_UPDATE" if operation != "audit" else "DRIFT"
                actions.append(Action("skill", f"{profile_id}:{skill}", status))
                if operation == "audit":
                    findings.append(f"skill_drift:{profile_id}:{skill}")

    if preset.get("kanban", {}).get("initialize", False):
        db_candidates = [hermes_home / "kanban.db", hermes_home / "kanban" / "kanban.db"]
        if any(path.exists() for path in db_candidates):
            actions.append(Action("kanban", preset["id"], "SKIP_INITIALIZED"))
        else:
            status = "PLAN_INIT" if operation != "audit" else "NOT_VERIFIED"
            actions.append(Action("kanban", preset["id"], status))
            if operation == "audit":
                findings.append("kanban_not_verified")
    return actions, findings, identity


def execute(
    args: argparse.Namespace,
    preset: dict[str, Any],
    actions: list[Action],
    hermes_binary: str,
    receipt: dict[str, Any],
) -> int:
    env = os.environ.copy()
    env["HERMES_HOME"] = str(args.hermes_home)
    profile_by_id = {p["id"]: p for p in preset["profiles"]}

    for action in actions:
        if action.status.startswith("BLOCKED"):
            receipt["findings"].append(action.status + ":" + action.target)
            receipt["readiness"] = "BLOCKED"
            return EXIT_PREFLIGHT

    for action in actions:
        if action.kind == "profile" and action.status == "PLAN_CREATE":
            profile = profile_by_id[action.target]
            command = [
                hermes_binary,
                "profile",
                "create",
                profile["id"],
                "--no-skills",
                "--no-alias",
                "--description",
                profile["description"],
            ]
            action.command = command
            result = run_command(command, env)
            if result.returncode != 0:
                action.status = "FAILED"
                action.detail = (result.stderr or result.stdout).strip()
                receipt["readiness"] = "BLOCKED"
                receipt["findings"].append(f"profile_create_failed:{profile['id']}")
                return EXIT_EXECUTION
            action.status = "CREATED"
            profile_dir = args.hermes_home / "profiles" / profile["id"]
            if not profile_dir.exists():
                action.status = "FAILED_VERIFY"
                receipt["readiness"] = "BLOCKED"
                receipt["findings"].append(
                    f"profile_directory_missing_after_create:{profile['id']}"
                )
                return EXIT_EXECUTION

    for action in actions:
        if action.kind != "skill" or action.status not in {"PLAN_INSTALL", "PLAN_UPDATE"}:
            continue
        profile_id, skill = action.target.split(":", 1)
        source = args.skills_root / skill
        target = args.hermes_home / "profiles" / profile_id / "skills" / skill
        try:
            atomic_symlink(source, target)
        except Exception as exc:
            action.status = "FAILED"
            action.detail = str(exc)
            receipt["readiness"] = "BLOCKED"
            receipt["findings"].append(f"skill_symlink_failed:{profile_id}:{skill}")
            return EXIT_EXECUTION
        action.status = "INSTALLED" if action.status == "PLAN_INSTALL" else "UPDATED"
        if skill_target_state(source, target) != "IN_SYNC":
            action.status = "FAILED_VERIFY"
            receipt["readiness"] = "BLOCKED"
            receipt["findings"].append(f"skill_symlink_mismatch:{profile_id}:{skill}")
            return EXIT_EXECUTION

    for action in actions:
        if action.kind == "soul" and action.status == "PLAN_SYNC":
            profile_id = action.target
            profile = profile_by_id[profile_id]
            soul_source = args.skills_root.parent / profile["soul"]
            soul_target = args.hermes_home / "profiles" / profile_id / "SOUL.md"
            try:
                import shutil
                shutil.copy2(soul_source, soul_target)
                action.status = "SYNCED"
            except Exception as exc:
                action.status = "FAILED"
                action.detail = str(exc)
                receipt["readiness"] = "BLOCKED"
                receipt["findings"].append(f"soul_sync_failed:{profile_id}")
                return EXIT_EXECUTION

    for action in actions:
        if action.kind == "config" and action.status == "PLAN_SYNC":
            profile_id = action.target
            profile = profile_by_id[profile_id]
            config_source = args.skills_root.parent / profile["config"]
            config_target = args.hermes_home / "profiles" / profile_id / "config.yaml"
            try:
                import shutil
                shutil.copy2(config_source, config_target)
                action.status = "SYNCED"
            except Exception as exc:
                action.status = "FAILED"
                action.detail = str(exc)
                receipt["readiness"] = "BLOCKED"
                receipt["findings"].append(f"config_sync_failed:{profile_id}")
                return EXIT_EXECUTION

    if not args.skip_kanban:
        for action in actions:
            if action.kind == "kanban" and action.status == "PLAN_INIT":
                command = [hermes_binary, "kanban", "init"]
                action.command = command
                result = run_command(command, env)
                if result.returncode != 0:
                    action.status = "FAILED"
                    action.detail = (result.stderr or result.stdout).strip()
                    receipt["readiness"] = "READY_WITH_LIMITATIONS"
                    receipt["findings"].append("kanban_init_failed")
                else:
                    action.status = "INITIALIZED"

    receipt["runtime_execution"] = "EXECUTED"
    receipt["readiness"] = "READY_WITH_LIMITATIONS" if receipt["findings"] else "READY"
    return EXIT_OK


def render_human(receipt: dict[str, Any]) -> str:
    lines = [
        f"Hermes fleet: {receipt['fleet_id']}",
        f"Preset version: {receipt['preset_version']}",
        f"Identity state: {receipt['fleet_identity_state']}",
        f"Operation: {receipt['operation']}",
        f"Mode: {receipt['mode']}",
        "",
    ]
    success_statuses = {
        "CREATED",
        "INSTALLED",
        "UPDATED",
        "INITIALIZED",
        "SKIP_EXISTS",
        "SKIP_IN_SYNC",
        "SKIP_INITIALIZED",
        "READY_FRESH_BOOTSTRAP",
        "TARGET_ONLY",
        "TARGET_PARTIAL",
    }
    for action in receipt["actions"]:
        marker = "✓" if action["status"] in success_statuses else "•"
        lines.append(f"{marker} {action['kind']} {action['target']}: {action['status']}")
    lines.extend(
        [
            "",
            f"Readiness: {receipt['readiness']}",
            f"Receipt: {receipt['receipt_path']}",
        ]
    )
    if receipt["findings"]:
        lines.append("Findings:")
        lines.extend(f"- {item}" for item in receipt["findings"])
    return "\n".join(lines)


def main(argv: Iterable[str] | None = None) -> int:
    args = build_parser().parse_args(list(argv) if argv is not None else None)
    if args.operation == "audit" and args.apply:
        print("ERROR: audit is always read-only; remove --apply", file=sys.stderr)
        return EXIT_PREFLIGHT

    preset_path = args.preset_file or default_preset_path(args.preset)
    default_receipt_root = (
        args.hermes_home / "fleet-bootstrap"
        if args.apply
        else Path.cwd() / ".evidence" / "hermes-fleet"
    )
    receipt_path = args.receipt or (
        default_receipt_root / args.preset / "last-receipt.json"
    )
    receipt: dict[str, Any] = {
        "schema_version": "2.0.0",
        "generated_at": utc_now(),
        "fleet_id": args.preset,
        "preset_version": "NOT_VERIFIED",
        "identity_generation": "NOT_VERIFIED",
        "orchestrator_profile": "NOT_VERIFIED",
        "target_profile_ids": [],
        "fleet_identity_state": "NOT_VERIFIED",
        "legacy_profiles_present": [],
        "operation": args.operation,
        "mode": "APPLY" if args.apply else "PLAN_ONLY",
        "preset_path": str(preset_path),
        "skills_root": str(args.skills_root),
        "hermes_home": str(args.hermes_home),
        "hermes_version": "NOT_VERIFIED",
        "gateway_policy": "ORCHESTRATOR_ELIGIBLE_SPECIALISTS_NONE",
        "credentials_copied": False,
        "live_state_copied": False,
        "actions": [],
        "findings": [],
        "readiness": "NOT_VERIFIED",
        "runtime_execution": "NOT_RUN",
        "receipt_path": str(receipt_path),
    }

    try:
        preset = load_json(preset_path)
        validate_preset(preset)
        if preset["id"] != args.preset:
            raise FleetError(
                f"Preset ID mismatch: requested {args.preset}, file declares {preset['id']}"
            )

        receipt["preset_version"] = preset["version"]
        receipt["identity_generation"] = preset.get("identity_generation", 1)
        receipt["orchestrator_profile"] = preset["orchestrator"]
        receipt["target_profile_ids"] = [profile["id"] for profile in preset["profiles"]]

        actions, findings, identity = plan_actions(
            preset, args.skills_root.resolve(), args.hermes_home.resolve(), args.operation
        )
        receipt["fleet_identity_state"] = identity["state"]
        receipt["legacy_profiles_present"] = identity["legacy_profiles_present"]
        receipt["findings"].extend(findings)
        receipt["actions"] = [action.as_dict() for action in actions]

        blocked = [action for action in actions if action.status.startswith("BLOCKED")]
        if blocked:
            receipt["readiness"] = "BLOCKED"
            exit_code = EXIT_PREFLIGHT
        elif args.operation == "audit":
            receipt["readiness"] = "READY" if not findings else "NEEDS_WORK"
            exit_code = EXIT_OK if not findings else EXIT_NEEDS_WORK
        elif not args.apply:
            receipt["readiness"] = "READY_TO_APPLY"
            exit_code = EXIT_OK
        else:
            hermes_binary = resolve_hermes_binary(args.hermes_bin)
            if not hermes_binary:
                receipt["findings"].append(f"hermes_not_found:{args.hermes_bin}")
                receipt["readiness"] = "BLOCKED"
                exit_code = EXIT_PREFLIGHT
            else:
                env = os.environ.copy()
                env["HERMES_HOME"] = str(args.hermes_home)
                version = run_command([hermes_binary, "--version"], env)
                if version.returncode != 0:
                    receipt["findings"].append("hermes_version_failed")
                    receipt["readiness"] = "BLOCKED"
                    exit_code = EXIT_PREFLIGHT
                else:
                    receipt["hermes_version"] = (
                        version.stdout.strip() or version.stderr.strip()
                    )
                    exit_code = execute(args, preset, actions, hermes_binary, receipt)
                    receipt["actions"] = [action.as_dict() for action in actions]
    except FleetError as exc:
        receipt["findings"].append(str(exc))
        receipt["readiness"] = "BLOCKED"
        exit_code = EXIT_PREFLIGHT
    except Exception as exc:
        receipt["findings"].append(
            f"unexpected_error:{type(exc).__name__}:{exc}"
        )
        receipt["readiness"] = "BLOCKED"
        exit_code = EXIT_EXECUTION

    try:
        receipt_path.parent.mkdir(parents=True, exist_ok=True)
        receipt_path.write_text(
            json.dumps(receipt, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    except OSError as exc:
        print(f"ERROR: could not write receipt: {exc}", file=sys.stderr)
        return EXIT_EXECUTION

    if args.json_output:
        print(json.dumps(receipt, indent=2, sort_keys=True))
    else:
        print(render_human(receipt))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
