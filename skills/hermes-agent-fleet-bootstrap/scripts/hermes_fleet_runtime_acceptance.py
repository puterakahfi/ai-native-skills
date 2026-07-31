#!/usr/bin/env python3
"""Evaluate sanitized Hermes agent-fleet runtime evidence without exposing secrets."""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

EXIT_OK = 0
EXIT_NEEDS_WORK = 2
EXIT_PREFLIGHT = 3
EXIT_EXECUTION = 4

TARGET_PROFILES = [
    "agent-orchestrator",
    "agent-product",
    "agent-architecture",
    "agent-design",
    "agent-frontend",
    "agent-backend",
    "agent-review",
]
SPECIALISTS = TARGET_PROFILES[1:]
PROHIBITED_SECRET_KEYS = {
    "token",
    "telegram_token",
    "bot_token",
    "api_key",
    "apikey",
    "password",
    "client_secret",
    "access_token",
    "refresh_token",
    "authorization",
    "cookie",
    "private_key",
}
TOKEN_VALUE = re.compile(r"^\d{5,}:[A-Za-z0-9_-]{20,}$")


class AcceptanceError(RuntimeError):
    pass


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_json(path: Path) -> dict[str, Any]:
    if path.is_symlink():
        raise AcceptanceError(f"Symlinked evidence file is not allowed: {path}")
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise AcceptanceError(f"Evidence file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise AcceptanceError(f"Invalid evidence JSON {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise AcceptanceError("Evidence root must be an object")
    return value


def scan_secret_material(value: Any, path: str = "$") -> list[str]:
    findings: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            normalized = str(key).strip().lower().replace("-", "_")
            child_path = f"{path}.{key}"
            if normalized in PROHIBITED_SECRET_KEYS:
                findings.append(f"secret_field_present:{child_path}")
            findings.extend(scan_secret_material(child, child_path))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            findings.extend(scan_secret_material(child, f"{path}[{index}]"))
    elif isinstance(value, str) and TOKEN_VALUE.fullmatch(value.strip()):
        findings.append(f"telegram_token_value_present:{path}")
    return findings


def require_bool(value: Any, label: str) -> bool:
    if not isinstance(value, bool):
        raise AcceptanceError(f"{label} must be boolean")
    return value


def require_string(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise AcceptanceError(f"{label} must be a non-empty string")
    return value.strip()


def require_string_list(value: Any, label: str) -> list[str]:
    if not isinstance(value, list) or not all(isinstance(item, str) and item for item in value):
        raise AcceptanceError(f"{label} must be a string list")
    return list(value)


def validate_profiles(evidence: dict[str, Any], checks: list[dict[str, Any]], findings: list[str]) -> None:
    identity_state = evidence.get("identity_state")
    identity_ok = identity_state == "TARGET_ONLY_COMPLETE"
    checks.append(
        {
            "id": "target_identity_state",
            "status": "PASS" if identity_ok else "FAIL",
            "detail": str(identity_state),
        }
    )
    if not identity_ok:
        findings.append("identity_state_not_target_only_complete")

    profiles = evidence.get("profiles")
    if not isinstance(profiles, list):
        raise AcceptanceError("profiles must be a list")
    ids: list[str] = []
    by_id: dict[str, dict[str, Any]] = {}
    for profile in profiles:
        if not isinstance(profile, dict):
            raise AcceptanceError("each profile must be an object")
        profile_id = require_string(profile.get("id"), "profile id")
        if profile_id in by_id:
            raise AcceptanceError(f"duplicate profile evidence: {profile_id}")
        ids.append(profile_id)
        by_id[profile_id] = profile

    exact = ids == TARGET_PROFILES
    checks.append(
        {
            "id": "exact_target_profiles",
            "status": "PASS" if exact else "FAIL",
            "detail": ids,
        }
    )
    if not exact:
        findings.append("target_profile_set_or_order_mismatch")

    orchestrator = by_id.get("agent-orchestrator", {})
    orchestrator_ok = (
        orchestrator.get("gateway") == "eligible"
        and orchestrator.get("worker_mode") == "user_facing_front_door"
    )
    checks.append(
        {
            "id": "orchestrator_gateway_contract",
            "status": "PASS" if orchestrator_ok else "FAIL",
            "detail": {
                "gateway": orchestrator.get("gateway"),
                "worker_mode": orchestrator.get("worker_mode"),
            },
        }
    )
    if not orchestrator_ok:
        findings.append("agent_orchestrator_gateway_contract_failed")

    specialist_failures = []
    for profile_id in SPECIALISTS:
        profile = by_id.get(profile_id, {})
        if profile.get("gateway") != "none" or profile.get("worker_mode") != "headless_on_demand":
            specialist_failures.append(profile_id)
    checks.append(
        {
            "id": "headless_specialist_contract",
            "status": "PASS" if not specialist_failures else "FAIL",
            "detail": specialist_failures,
        }
    )
    if specialist_failures:
        findings.append("specialists_not_headless:" + ",".join(specialist_failures))


def validate_migration_and_model_sync(
    evidence: dict[str, Any], checks: list[dict[str, Any]], findings: list[str]
) -> None:
    migration = evidence.get("migration")
    if not isinstance(migration, dict):
        raise AcceptanceError("migration evidence must be an object")
    migration_ok = (
        migration.get("readiness") in {"READY", "READY_WITH_LIMITATIONS"}
        and migration.get("identity_state") == "TARGET_ONLY_COMPLETE"
        and migration.get("credentials_copied") is False
        and migration.get("live_state_copied") is False
        and migration.get("gateway_started") is False
    )
    checks.append(
        {
            "id": "migration_acceptance",
            "status": "PASS" if migration_ok else "FAIL",
            "detail": {
                "readiness": migration.get("readiness"),
                "identity_state": migration.get("identity_state"),
            },
        }
    )
    if not migration_ok:
        findings.append("migration_evidence_failed")

    model_sync = evidence.get("model_sync")
    if not isinstance(model_sync, dict):
        raise AcceptanceError("model_sync evidence must be an object")
    targets = model_sync.get("target_profiles")
    model_sync_ok = (
        model_sync.get("readiness") == "READY"
        and model_sync.get("identity_state") == "TARGET_ONLY_COMPLETE"
        and model_sync.get("source_profile") == "agent-orchestrator"
        and targets == SPECIALISTS
        and model_sync.get("credentials_copied") is False
    )
    checks.append(
        {
            "id": "model_sync_acceptance",
            "status": "PASS" if model_sync_ok else "FAIL",
            "detail": {
                "readiness": model_sync.get("readiness"),
                "source_profile": model_sync.get("source_profile"),
                "target_profiles": targets,
            },
        }
    )
    if not model_sync_ok:
        findings.append("model_sync_evidence_failed")


def validate_scenario_common(
    scenario: dict[str, Any], index: int, task_ids: set[str]
) -> tuple[str, str, list[str], dict[str, Any]]:
    kind = require_string(scenario.get("kind"), f"scenarios[{index}].kind")
    scenario_id = require_string(scenario.get("id"), f"scenarios[{index}].id")
    task_id = require_string(scenario.get("task_id"), f"scenarios[{index}].task_id")
    if task_id in task_ids:
        raise AcceptanceError(f"duplicate task_id: {task_id}")
    task_ids.add(task_id)
    selected = require_string_list(
        scenario.get("selected_profiles"), f"scenarios[{index}].selected_profiles"
    )
    unknown = [profile for profile in selected if profile not in TARGET_PROFILES]
    if unknown:
        raise AcceptanceError(f"scenario {scenario_id} contains unknown profiles: {unknown}")
    if len(selected) != len(set(selected)):
        raise AcceptanceError(f"scenario {scenario_id} contains duplicate selected profiles")
    dependencies = scenario.get("dependencies")
    handoffs = scenario.get("handoffs")
    outputs = scenario.get("outputs")
    if not isinstance(dependencies, list):
        raise AcceptanceError(f"scenario {scenario_id} dependencies must be a list")
    if not isinstance(handoffs, list) or not handoffs:
        raise AcceptanceError(f"scenario {scenario_id} must contain observable handoffs")
    if not isinstance(outputs, list) or not outputs:
        raise AcceptanceError(f"scenario {scenario_id} must contain observable outputs")
    if scenario.get("result") != "PASS":
        raise AcceptanceError(f"scenario {scenario_id} result must be PASS")
    review = scenario.get("review")
    if not isinstance(review, dict):
        raise AcceptanceError(f"scenario {scenario_id} review must be an object")
    return kind, scenario_id, selected, review


def validate_scenarios(evidence: dict[str, Any], checks: list[dict[str, Any]], findings: list[str]) -> None:
    scenarios = evidence.get("scenarios")
    if not isinstance(scenarios, list) or not scenarios:
        raise AcceptanceError("scenarios must be a non-empty list")
    by_kind: dict[str, list[dict[str, Any]]] = {}
    task_ids: set[str] = set()
    scenario_failures: list[str] = []

    for index, scenario in enumerate(scenarios):
        if not isinstance(scenario, dict):
            raise AcceptanceError("each scenario must be an object")
        kind, scenario_id, selected, review = validate_scenario_common(
            scenario, index, task_ids
        )
        by_kind.setdefault(kind, []).append(scenario)
        selected_set = set(selected)
        ok = True

        if "agent-orchestrator" in selected_set:
            ok = False
            scenario_failures.append(f"orchestrator_counted_as_worker:{scenario_id}")
        if selected_set == set(SPECIALISTS):
            ok = False
            scenario_failures.append(f"all_specialists_invoked:{scenario_id}")

        if kind == "planning":
            required = {"agent-product", "agent-architecture"}
            forbidden = {"agent-design", "agent-frontend", "agent-backend"}
            ok = required.issubset(selected_set) and selected_set.isdisjoint(forbidden) and ok
            if review.get("required") is True and review.get("verdict") in {None, "NOT_RUN"}:
                ok = False
        elif kind == "backend":
            required = {"agent-backend", "agent-review"}
            forbidden = {"agent-design", "agent-frontend"}
            ok = required.issubset(selected_set) and selected_set.isdisjoint(forbidden) and ok
            ok = (
                review.get("required") is True
                and review.get("profile") == "agent-review"
                and review.get("verdict") in {"PASS", "PASS_WITH_LIMITATIONS"}
                and ok
            )
        elif kind == "ui":
            required = {"agent-design", "agent-frontend", "agent-review"}
            forbidden = {"agent-backend"}
            ok = required.issubset(selected_set) and selected_set.isdisjoint(forbidden) and ok
            ok = (
                review.get("required") is True
                and review.get("profile") == "agent-review"
                and review.get("verdict") in {"PASS", "PASS_WITH_LIMITATIONS"}
                and ok
            )
        else:
            raise AcceptanceError(f"unsupported scenario kind: {kind}")

        if not ok:
            scenario_failures.append(f"routing_contract_failed:{scenario_id}")

    required_kinds = {"planning", "backend", "ui"}
    missing = sorted(required_kinds - by_kind.keys())
    if missing:
        scenario_failures.append("missing_scenarios:" + ",".join(missing))

    checks.append(
        {
            "id": "bounded_specialist_routing",
            "status": "PASS" if not scenario_failures else "FAIL",
            "detail": scenario_failures,
        }
    )
    findings.extend(scenario_failures)


def validate_review_independence(
    evidence: dict[str, Any], checks: list[dict[str, Any]], findings: list[str], limitations: list[str]
) -> None:
    review = evidence.get("review_independence")
    if not isinstance(review, dict):
        raise AcceptanceError("review_independence must be an object")
    status = review.get("status")
    allowed = {
        "VERIFIED_SEPARATE_RUNTIME",
        "VERIFIED_SEPARATE_PROFILE",
        "LIMITED_SHARED_RUNTIME",
        "LIMITED_SHARED_MODEL_AND_ACCOUNT",
    }
    review_limitations = review.get("limitations")
    ok = status in allowed and isinstance(review_limitations, list)
    if str(status).startswith("LIMITED") and not review_limitations:
        ok = False
    checks.append(
        {
            "id": "review_independence_disclosure",
            "status": "PASS" if ok else "FAIL",
            "detail": {"status": status, "limitations": review_limitations},
        }
    )
    if not ok:
        findings.append("review_independence_not_honestly_disclosed")
    elif str(status).startswith("LIMITED"):
        limitations.extend(str(item) for item in review_limitations)


def validate_telegram(
    evidence: dict[str, Any], checks: list[dict[str, Any]], findings: list[str], limitations: list[str]
) -> bool:
    telegram = evidence.get("telegram")
    if not isinstance(telegram, dict):
        raise AcceptanceError("telegram evidence must be an object")
    redacted = require_bool(
        telegram.get("credential_values_redacted"),
        "telegram.credential_values_redacted",
    )
    legacy_running = require_bool(
        telegram.get("legacy_gateway_running"), "telegram.legacy_gateway_running"
    )
    configured_profile = telegram.get("configured_profile")
    live = (
        telegram.get("evidence_level") == "LIVE"
        and configured_profile == "agent-orchestrator"
        and telegram.get("gateway_started") is True
        and telegram.get("message_received") is True
        and telegram.get("response_returned") is True
        and redacted
        and not legacy_running
    )
    structurally_safe = redacted and not legacy_running and configured_profile in {
        "agent-orchestrator",
        None,
        "NOT_CONFIGURED",
    }
    checks.append(
        {
            "id": "telegram_front_door",
            "status": "PASS" if live else ("LIMITED" if structurally_safe else "FAIL"),
            "detail": {
                "evidence_level": telegram.get("evidence_level"),
                "configured_profile": configured_profile,
                "gateway_started": telegram.get("gateway_started"),
                "message_received": telegram.get("message_received"),
                "response_returned": telegram.get("response_returned"),
                "legacy_gateway_running": legacy_running,
            },
        }
    )
    if not structurally_safe:
        findings.append("telegram_gateway_safety_failed")
    elif not live:
        limitations.append("live_telegram_round_trip_not_verified")
    return live


def evaluate(evidence: dict[str, Any]) -> tuple[int, dict[str, Any]]:
    secret_findings = scan_secret_material(evidence)
    if secret_findings:
        raise AcceptanceError("Sanitized evidence contains prohibited secret material: " + ", ".join(secret_findings))
    if evidence.get("fleet_id") != "native-ai-engineering":
        raise AcceptanceError("fleet_id must be native-ai-engineering")

    checks: list[dict[str, Any]] = []
    findings: list[str] = []
    limitations: list[str] = []
    validate_profiles(evidence, checks, findings)
    validate_migration_and_model_sync(evidence, checks, findings)
    validate_scenarios(evidence, checks, findings)
    validate_review_independence(evidence, checks, findings, limitations)
    telegram_live = validate_telegram(evidence, checks, findings, limitations)

    model_workers = evidence.get("model_driven_workers")
    if not isinstance(model_workers, dict):
        raise AcceptanceError("model_driven_workers must be an object")
    model_workers_live = (
        model_workers.get("evidence_level") == "LIVE"
        and model_workers.get("specialist_execution_observed") is True
    )
    if not model_workers_live:
        limitations.append("provider_backed_specialist_execution_not_verified")
    checks.append(
        {
            "id": "model_driven_specialist_execution",
            "status": "PASS" if model_workers_live else "LIMITED",
            "detail": model_workers,
        }
    )

    failed = [check for check in checks if check["status"] == "FAIL"]
    if failed or findings:
        verdict = "NEEDS_WORK"
        exit_code = EXIT_NEEDS_WORK
    elif telegram_live and model_workers_live and not limitations:
        verdict = "PASS"
        exit_code = EXIT_OK
    else:
        verdict = "PASS_WITH_LIMITATIONS"
        exit_code = EXIT_OK

    receipt = {
        "schema_version": "1.0.0",
        "generated_at": utc_now(),
        "fleet_id": "native-ai-engineering",
        "operation": "validate_runtime_acceptance",
        "verdict": verdict,
        "checks": checks,
        "findings": sorted(set(findings)),
        "limitations": sorted(set(limitations)),
        "credentials_exposed": False,
        "telegram_live_verified": telegram_live,
        "model_driven_workers_verified": model_workers_live,
    }
    return exit_code, receipt


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="hermes-fleet-runtime-acceptance")
    parser.add_argument("preset")
    parser.add_argument("--evidence", type=Path, required=True)
    parser.add_argument("--receipt", type=Path)
    parser.add_argument("--json", action="store_true", dest="json_output")
    return parser


def render_human(receipt: dict[str, Any], receipt_path: Path) -> str:
    lines = [
        f"Hermes runtime acceptance: {receipt['fleet_id']}",
        f"Verdict: {receipt['verdict']}",
        "",
    ]
    for check in receipt["checks"]:
        lines.append(f"- {check['id']}: {check['status']}")
    if receipt["findings"]:
        lines.extend(["", "Findings:"])
        lines.extend(f"- {item}" for item in receipt["findings"])
    if receipt["limitations"]:
        lines.extend(["", "Limitations:"])
        lines.extend(f"- {item}" for item in receipt["limitations"])
    lines.extend(["", f"Receipt: {receipt_path}"])
    return "\n".join(lines)


def main(argv: Iterable[str] | None = None) -> int:
    args = build_parser().parse_args(list(argv) if argv is not None else None)
    if args.preset != "native-ai-engineering":
        print("ERROR: runtime acceptance currently supports native-ai-engineering only", file=sys.stderr)
        return EXIT_PREFLIGHT
    receipt_path = args.receipt or (
        Path.cwd()
        / ".evidence"
        / "hermes-fleet"
        / args.preset
        / "last-runtime-acceptance-receipt.json"
    )
    try:
        evidence = load_json(args.evidence)
        code, receipt = evaluate(evidence)
    except AcceptanceError as exc:
        receipt = {
            "schema_version": "1.0.0",
            "generated_at": utc_now(),
            "fleet_id": args.preset,
            "operation": "validate_runtime_acceptance",
            "verdict": "BLOCKED",
            "checks": [],
            "findings": [str(exc)],
            "limitations": [],
            "credentials_exposed": "secret material" in str(exc).lower(),
            "telegram_live_verified": False,
            "model_driven_workers_verified": False,
        }
        code = EXIT_PREFLIGHT
    except Exception as exc:
        receipt = {
            "schema_version": "1.0.0",
            "generated_at": utc_now(),
            "fleet_id": args.preset,
            "operation": "validate_runtime_acceptance",
            "verdict": "BLOCKED",
            "checks": [],
            "findings": [f"execution_error:{type(exc).__name__}:{exc}"],
            "limitations": [],
            "credentials_exposed": False,
            "telegram_live_verified": False,
            "model_driven_workers_verified": False,
        }
        code = EXIT_EXECUTION

    receipt["evidence_path"] = str(args.evidence)
    receipt["receipt_path"] = str(receipt_path)
    try:
        receipt_path.parent.mkdir(parents=True, exist_ok=True)
        receipt_path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    except OSError as exc:
        print(f"ERROR: could not write runtime acceptance receipt: {exc}", file=sys.stderr)
        return EXIT_EXECUTION

    if args.json_output:
        print(json.dumps(receipt, indent=2, sort_keys=True))
    else:
        print(render_human(receipt, receipt_path))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
