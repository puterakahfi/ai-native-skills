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
import tempfile
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

EXIT_OK = 0
EXIT_NEEDS_WORK = 2
EXIT_PREFLIGHT = 3
EXIT_EXECUTION = 4


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


SAFE_IDENTIFIER = re.compile(r"^[a-z0-9][a-z0-9._-]{0,127}$")


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
        if not isinstance(profile["skills"], list) or not all(
            isinstance(item, str) and item for item in profile["skills"]
        ):
            raise FleetError(f"Profile skills must be string list: {profile['id']}")
        validate_identifier(profile["id"], "profile id")
        if profile["gateway"] not in {"eligible", "none"}:
            raise FleetError(
                f"Unsupported gateway policy for {profile['id']}: {profile['gateway']!r}"
            )
        for skill in profile["skills"]:
            validate_identifier(skill, "skill id")
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


def directory_digest(path: Path) -> str:
    digest = hashlib.sha256()
    if path.is_symlink():
        raise FleetError(f"Symlinked managed path is not allowed: {path}")
    if not path.exists():
        return "MISSING"
    if not path.is_dir():
        raise FleetError(f"Managed path must be a directory: {path}")
    for candidate in sorted(path.rglob("*")):
        if candidate.is_symlink():
            raise FleetError(f"Symlink inside managed skill source is not allowed: {candidate}")
        if not candidate.is_file():
            continue
        rel = candidate.relative_to(path).as_posix()
        if any(part in {"__pycache__", ".git"} for part in candidate.parts):
            continue
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


def atomic_copytree(source: Path, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=f".{target.name}.", dir=str(target.parent)) as tmp:
        staged = Path(tmp) / target.name
        shutil.copytree(source, staged)
        backup = target.with_name(f".{target.name}.previous")
        if backup.exists():
            shutil.rmtree(backup)
        if target.exists():
            target.rename(backup)
        try:
            staged.rename(target)
        except Exception:
            if target.exists():
                shutil.rmtree(target)
            if backup.exists():
                backup.rename(target)
            raise
        if backup.exists():
            shutil.rmtree(backup)


def default_skills_root() -> Path:
    return Path(__file__).resolve().parents[2]


def default_preset_path(name: str) -> Path:
    return Path(__file__).resolve().parents[1] / "assets" / "presets" / f"{name}.json"


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
        default=Path(os.environ.get("HERMES_HOME", "~/.hermes")).expanduser(),
    )
    parser.add_argument("--hermes-bin", default="hermes")
    parser.add_argument("--receipt", type=Path)
    parser.add_argument("--skip-kanban", action="store_true")
    parser.add_argument("--json", action="store_true", dest="json_output")
    return parser


def plan_actions(
    preset: dict[str, Any], skills_root: Path, hermes_home: Path, operation: str
) -> tuple[list[Action], list[str]]:
    actions: list[Action] = []
    findings: list[str] = []
    profiles_root = hermes_home / "profiles"
    if profiles_root.is_symlink():
        raise FleetError(f"Symlinked Hermes profiles root is not allowed: {profiles_root}")
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
            target_hash = directory_digest(target)
            if source_hash == "MISSING":
                actions.append(Action("skill", f"{profile_id}:{skill}", "BLOCKED_SOURCE_MISSING"))
                findings.append(f"missing_skill_source:{skill}")
            elif source_hash == target_hash:
                actions.append(Action("skill", f"{profile_id}:{skill}", "SKIP_IN_SYNC"))
            elif target_hash == "MISSING":
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
    return actions, findings


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
                receipt["findings"].append(f"profile_directory_missing_after_create:{profile['id']}")
                return EXIT_EXECUTION

    for action in actions:
        if action.kind != "skill" or action.status not in {"PLAN_INSTALL", "PLAN_UPDATE"}:
            continue
        profile_id, skill = action.target.split(":", 1)
        source = args.skills_root / skill
        target = args.hermes_home / "profiles" / profile_id / "skills" / skill
        try:
            atomic_copytree(source, target)
        except Exception as exc:
            action.status = "FAILED"
            action.detail = str(exc)
            receipt["readiness"] = "BLOCKED"
            receipt["findings"].append(f"skill_copy_failed:{profile_id}:{skill}")
            return EXIT_EXECUTION
        action.status = "INSTALLED" if action.status == "PLAN_INSTALL" else "UPDATED"
        if directory_digest(source) != directory_digest(target):
            action.status = "FAILED_VERIFY"
            receipt["readiness"] = "BLOCKED"
            receipt["findings"].append(f"skill_digest_mismatch:{profile_id}:{skill}")
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
    receipt_path = args.receipt or (default_receipt_root / args.preset / "last-receipt.json")
    receipt: dict[str, Any] = {
        "schema_version": "1.0.0",
        "generated_at": utc_now(),
        "fleet_id": args.preset,
        "operation": args.operation,
        "mode": "APPLY" if args.apply else "PLAN_ONLY",
        "preset_path": str(preset_path),
        "skills_root": str(args.skills_root),
        "hermes_home": str(args.hermes_home),
        "hermes_version": "NOT_VERIFIED",
        "gateway_policy": "ORCHESTRATOR_ELIGIBLE_SPECIALISTS_NONE",
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
        actions, findings = plan_actions(
            preset, args.skills_root.resolve(), args.hermes_home.resolve(), args.operation
        )
        receipt["findings"].extend(findings)
        receipt["actions"] = [action.as_dict() for action in actions]

        blocked = [a for a in actions if a.status.startswith("BLOCKED")]
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
                    receipt["hermes_version"] = version.stdout.strip() or version.stderr.strip()
                    exit_code = execute(args, preset, actions, hermes_binary, receipt)
                    receipt["actions"] = [action.as_dict() for action in actions]
    except FleetError as exc:
        receipt["findings"].append(str(exc))
        receipt["readiness"] = "BLOCKED"
        exit_code = EXIT_PREFLIGHT
    except Exception as exc:
        receipt["findings"].append(f"unexpected_error:{type(exc).__name__}:{exc}")
        receipt["readiness"] = "BLOCKED"
        exit_code = EXIT_EXECUTION

    try:
        receipt_path.parent.mkdir(parents=True, exist_ok=True)
        receipt_path.write_text(
            json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8"
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
