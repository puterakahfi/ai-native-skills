from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "hermes_fleet.py"
spec = importlib.util.spec_from_file_location("hermes_fleet", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
assert spec and spec.loader
sys.modules[spec.name] = module
spec.loader.exec_module(module)


class HermesFleetTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp())
        self.skills = self.tmp / "skills"
        self.home = self.tmp / "hermes-home"
        self.receipt = self.tmp / "receipt.json"
        self.preset = self.tmp / "preset.json"
        self.log = self.tmp / "hermes.log"
        self.hermes = self.tmp / "hermes"
        self.profile_specs = [
            {
                "id": "agent-orchestrator",
                "description": "Coordinates work.",
                "gateway": "eligible",
                "worker_mode": "user_facing_front_door",
                "skills": ["fleet-skill", "router-skill"],
                "soul": "souls/agent-orchestrator.md",
            },
            {
                "id": "agent-review",
                "description": "Reviews work.",
                "gateway": "none",
                "worker_mode": "headless_on_demand",
                "skills": ["review-skill"],
                "soul": "souls/agent-review.md",
            },
        ]
        self.write_preset()
        for skill in ["fleet-skill", "router-skill", "review-skill"]:
            path = self.skills / skill
            path.mkdir(parents=True)
            (path / "SKILL.md").write_text(
                f"---\nname: {skill}\n---\n", encoding="utf-8"
            )
        for profile_spec in self.profile_specs:
            soul = self.tmp / profile_spec["soul"]
            soul.parent.mkdir(parents=True, exist_ok=True)
            soul.write_text(f"# {profile_spec['id']} soul\n", encoding="utf-8")
        self.write_fake_hermes()

    def write_preset(self, *, include_transition: bool = False) -> None:
        data = {
            "id": "test-fleet",
            "version": "2.0.0",
            "identity_generation": 2,
            "topology": "orchestrator_with_specialists",
            "orchestrator": "agent-orchestrator",
            "kanban": {"initialize": True},
            "profiles": self.profile_specs,
        }
        if include_transition:
            data["legacy_profile_ids"] = ["engineering-orchestrator", "quality-review"]
            data["mixed_identity_policy"] = "block_outside_migration"
        self.preset.write_text(json.dumps(data), encoding="utf-8")

    def write_fake_hermes(self, fail_profile: bool = False) -> None:
        fail = "1" if fail_profile else "0"
        self.hermes.write_text(
            f'''#!/usr/bin/env python3
import os, pathlib, sys
home = pathlib.Path(os.environ["HERMES_HOME"])
log = pathlib.Path(os.environ["FAKE_HERMES_LOG"])
with log.open("a", encoding="utf-8") as handle:
    handle.write(" ".join(sys.argv[1:]) + "\\n")
args = sys.argv[1:]
if args == ["--version"]:
    print("Hermes Agent v-test")
    raise SystemExit(0)
if args[:2] == ["profile", "create"]:
    if {fail}:
        print("profile create failed", file=sys.stderr)
        raise SystemExit(9)
    (home / "profiles" / args[2]).mkdir(parents=True, exist_ok=True)
    raise SystemExit(0)
if args[:2] == ["kanban", "init"]:
    home.mkdir(parents=True, exist_ok=True)
    (home / "kanban.db").write_text("test", encoding="utf-8")
    raise SystemExit(0)
raise SystemExit(0)
''',
            encoding="utf-8",
        )
        self.hermes.chmod(0o755)

    def run_cli(self, operation: str = "bootstrap", *extra: str) -> int:
        previous = os.environ.get("FAKE_HERMES_LOG")
        os.environ["FAKE_HERMES_LOG"] = str(self.log)
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                return module.main(
                    [
                        operation,
                        "test-fleet",
                        "--preset-file",
                        str(self.preset),
                        "--skills-root",
                        str(self.skills),
                        "--hermes-home",
                        str(self.home),
                        "--hermes-bin",
                        str(self.hermes),
                        "--receipt",
                        str(self.receipt),
                        "--json",
                        *extra,
                    ]
                )
        finally:
            if previous is None:
                os.environ.pop("FAKE_HERMES_LOG", None)
            else:
                os.environ["FAKE_HERMES_LOG"] = previous

    def test_plan_is_non_mutating(self) -> None:
        self.assertEqual(self.run_cli(), module.EXIT_OK)
        self.assertFalse((self.home / "profiles").exists())
        receipt = json.loads(self.receipt.read_text(encoding="utf-8"))
        self.assertEqual(receipt["mode"], "PLAN_ONLY")
        self.assertEqual(receipt["readiness"], "READY_TO_APPLY")

    def test_apply_creates_profiles_installs_skills_and_kanban(self) -> None:
        self.assertEqual(self.run_cli("bootstrap", "--apply"), module.EXIT_OK)
        for profile_spec in self.profile_specs:
            profile = self.home / "profiles" / profile_spec["id"]
            self.assertTrue(profile.is_dir())
            for skill in profile_spec["skills"]:
                projected = profile / "skills" / skill
                self.assertTrue(projected.is_symlink())
                self.assertEqual(projected.resolve(), (self.skills / skill).resolve())
                self.assertTrue((projected / "SKILL.md").is_file())
            self.assertEqual(
                (profile / "SOUL.md").read_text(encoding="utf-8"),
                (self.tmp / profile_spec["soul"]).read_text(encoding="utf-8"),
            )
        self.assertTrue((self.home / "kanban.db").is_file())

    def test_default_skills_root_is_fixed_catalog_clone(self) -> None:
        previous = os.environ.get("HERMES_SKILL_CATALOG_ROOT")
        os.environ["HERMES_SKILL_CATALOG_ROOT"] = str(self.tmp / "catalog")
        try:
            self.assertEqual(
                module.default_skills_root(),
                self.tmp / "catalog" / "skills",
            )
        finally:
            if previous is None:
                os.environ.pop("HERMES_SKILL_CATALOG_ROOT", None)
            else:
                os.environ["HERMES_SKILL_CATALOG_ROOT"] = previous

    def test_apply_is_idempotent(self) -> None:
        self.assertEqual(self.run_cli("bootstrap", "--apply"), module.EXIT_OK)
        first_log = self.log.read_text(encoding="utf-8")
        self.log.write_text("", encoding="utf-8")
        self.assertEqual(self.run_cli("bootstrap", "--apply"), module.EXIT_OK)
        second_log = self.log.read_text(encoding="utf-8")
        self.assertIn("profile create", first_log)
        self.assertNotIn("profile create", second_log)
        statuses = {
            item["status"]
            for item in json.loads(self.receipt.read_text(encoding="utf-8"))["actions"]
        }
        self.assertIn("SKIP_EXISTS", statuses)
        self.assertIn("SKIP_IN_SYNC", statuses)

    def test_apply_converts_existing_copied_skill_to_symlink(self) -> None:
        copied = self.home / "profiles" / "agent-review" / "skills" / "review-skill"
        copied.mkdir(parents=True)
        (copied / "SKILL.md").write_text(
            "---\nname: stale-review-skill\n---\n", encoding="utf-8"
        )
        self.assertEqual(self.run_cli("reconcile", "--apply"), module.EXIT_OK)
        self.assertTrue(copied.is_symlink())
        self.assertEqual(copied.resolve(), (self.skills / "review-skill").resolve())
        statuses = {
            item["target"]: item["status"]
            for item in json.loads(self.receipt.read_text(encoding="utf-8"))["actions"]
        }
        self.assertEqual(statuses["agent-review:review-skill"], "UPDATED")

    def test_reconcile_plans_and_applies_soul_drift(self) -> None:
        profile_dir = self.home / "profiles" / "agent-orchestrator"
        profile_dir.mkdir(parents=True)
        soul = profile_dir / "SOUL.md"
        soul.write_text("# stale soul\n", encoding="utf-8")

        self.assertEqual(self.run_cli("reconcile"), module.EXIT_OK)
        receipt = json.loads(self.receipt.read_text(encoding="utf-8"))
        soul_actions = [
            item for item in receipt["actions"]
            if item["kind"] == "soul" and item["target"] == "agent-orchestrator"
        ]
        self.assertEqual(soul_actions[0]["status"], "PLAN_UPDATE")
        self.assertIn("target_sha256", soul_actions[0]["detail"])
        self.assertEqual(soul.read_text(encoding="utf-8"), "# stale soul\n")

        self.assertEqual(self.run_cli("reconcile", "--apply"), module.EXIT_OK)
        receipt = json.loads(self.receipt.read_text(encoding="utf-8"))
        soul_actions = [
            item for item in receipt["actions"]
            if item["kind"] == "soul" and item["target"] == "agent-orchestrator"
        ]
        self.assertEqual(soul_actions[0]["status"], "UPDATED")
        self.assertEqual(
            soul.read_text(encoding="utf-8"),
            (self.tmp / "souls" / "agent-orchestrator.md").read_text(encoding="utf-8"),
        )

    def test_audit_reports_soul_drift(self) -> None:
        profile_dir = self.home / "profiles" / "agent-orchestrator"
        profile_dir.mkdir(parents=True)
        (profile_dir / "SOUL.md").write_text("# stale soul\n", encoding="utf-8")

        self.assertEqual(self.run_cli("audit"), module.EXIT_NEEDS_WORK)
        receipt = json.loads(self.receipt.read_text(encoding="utf-8"))
        self.assertIn("soul_drift:agent-orchestrator", receipt["findings"])
        soul_actions = [
            item for item in receipt["actions"]
            if item["kind"] == "soul" and item["target"] == "agent-orchestrator"
        ]
        self.assertEqual(soul_actions[0]["status"], "DRIFT")

    def test_missing_skill_fails_before_mutation(self) -> None:
        (self.skills / "review-skill").rename(self.skills / "removed-skill")
        self.assertEqual(self.run_cli("bootstrap", "--apply"), module.EXIT_PREFLIGHT)
        self.assertFalse((self.home / "profiles").exists())

    def test_audit_reports_missing_target_profiles(self) -> None:
        self.assertEqual(self.run_cli("audit"), module.EXIT_NEEDS_WORK)
        receipt = json.loads(self.receipt.read_text(encoding="utf-8"))
        self.assertEqual(receipt["readiness"], "NEEDS_WORK")
        self.assertEqual(receipt["fleet_identity_state"], "UNVERSIONED")

    def test_native_preset_v2_has_one_gateway_and_headless_specialists(self) -> None:
        preset_path = (
            Path(__file__).resolve().parents[1]
            / "assets"
            / "presets"
            / "native-ai-engineering.json"
        )
        preset = json.loads(preset_path.read_text(encoding="utf-8"))
        module.validate_preset(preset)
        self.assertEqual(preset["version"], "2.1.1")
        self.assertEqual(preset["identity_generation"], 2)
        self.assertEqual(preset["orchestrator"], "agent-orchestrator")
        gateways = [p["id"] for p in preset["profiles"] if p["gateway"] == "eligible"]
        self.assertEqual(gateways, ["agent-orchestrator"])
        for profile in preset["profiles"]:
            if profile["id"] == "agent-orchestrator":
                self.assertEqual(profile["worker_mode"], "user_facing_front_door")
            else:
                self.assertEqual(profile["gateway"], "none")
                self.assertEqual(profile["worker_mode"], "headless_on_demand")

    def test_legacy_only_bootstrap_is_blocked_outside_migration(self) -> None:
        self.write_preset(include_transition=True)
        for profile_id in ["engineering-orchestrator", "quality-review"]:
            (self.home / "profiles" / profile_id).mkdir(parents=True)
        self.assertEqual(self.run_cli("bootstrap", "--apply"), module.EXIT_PREFLIGHT)
        receipt = json.loads(self.receipt.read_text(encoding="utf-8"))
        self.assertEqual(receipt["fleet_identity_state"], "LEGACY_ONLY_COMPLETE")
        self.assertTrue(
            any(action["status"] == "BLOCKED_LEGACY_ONLY" for action in receipt["actions"])
        )
        self.assertFalse((self.home / "profiles" / "agent-orchestrator").exists())

    def test_mixed_identity_bootstrap_is_blocked_outside_migration(self) -> None:
        self.write_preset(include_transition=True)
        (self.home / "profiles" / "engineering-orchestrator").mkdir(parents=True)
        (self.home / "profiles" / "agent-orchestrator").mkdir(parents=True)
        self.assertEqual(self.run_cli("reconcile", "--apply"), module.EXIT_PREFLIGHT)
        receipt = json.loads(self.receipt.read_text(encoding="utf-8"))
        self.assertEqual(receipt["fleet_identity_state"], "MIXED")
        self.assertTrue(
            any(action["status"] == "BLOCKED_MIXED_IDENTITIES" for action in receipt["actions"])
        )

    def test_audit_reports_legacy_and_mixed_states_without_mutation(self) -> None:
        self.write_preset(include_transition=True)
        (self.home / "profiles" / "engineering-orchestrator").mkdir(parents=True)
        self.assertEqual(self.run_cli("audit"), module.EXIT_NEEDS_WORK)
        receipt = json.loads(self.receipt.read_text(encoding="utf-8"))
        self.assertEqual(receipt["fleet_identity_state"], "LEGACY_ONLY_PARTIAL")
        (self.home / "profiles" / "agent-orchestrator").mkdir(parents=True)
        self.assertEqual(self.run_cli("audit"), module.EXIT_NEEDS_WORK)
        receipt = json.loads(self.receipt.read_text(encoding="utf-8"))
        self.assertEqual(receipt["fleet_identity_state"], "MIXED")

    def test_invalid_transition_contract_is_rejected(self) -> None:
        data = json.loads(self.preset.read_text(encoding="utf-8"))
        data["legacy_profile_ids"] = ["engineering-orchestrator"]
        data["mixed_identity_policy"] = "allow"
        with self.assertRaises(module.FleetError):
            module.validate_preset(data)

    def test_profile_command_failure_is_reported(self) -> None:
        self.write_fake_hermes(fail_profile=True)
        self.assertEqual(self.run_cli("bootstrap", "--apply"), module.EXIT_EXECUTION)
        receipt = json.loads(self.receipt.read_text(encoding="utf-8"))
        self.assertEqual(receipt["readiness"], "BLOCKED")
        self.assertTrue(any("profile_create_failed" in item for item in receipt["findings"]))


if __name__ == "__main__":
    unittest.main()
