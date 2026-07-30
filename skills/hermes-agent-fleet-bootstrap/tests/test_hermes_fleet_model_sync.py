from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import yaml

PACKAGE = Path(__file__).resolve().parents[1]
RUNNER = PACKAGE / "scripts" / "hermes_fleet_model_sync.py"
SPEC = importlib.util.spec_from_file_location("hermes_fleet_model_sync", RUNNER)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ModelPolicySyncTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.hermes_home = self.root / ".hermes"
        self.preset = self.root / "fleet.json"
        self.receipt = self.root / "receipt.json"
        self.profile_ids = [
            "engineering-orchestrator",
            "backend-platform",
            "quality-review",
        ]
        self.preset.write_text(
            json.dumps(
                {
                    "id": "test-fleet",
                    "version": "1.0.0",
                    "orchestrator": "engineering-orchestrator",
                    "profiles": [{"id": profile} for profile in self.profile_ids],
                }
            ),
            encoding="utf-8",
        )
        for profile in self.profile_ids:
            (self.hermes_home / "profiles" / profile).mkdir(parents=True)
        self.write_config(
            "engineering-orchestrator",
            {
                "model": {
                    "provider": "openai-codex",
                    "default": "gpt-5.2-codex",
                    "openai_runtime": "codex_app_server",
                    "api_key": "SOURCE_SECRET_MUST_NOT_COPY",
                },
                "auxiliary": {
                    "compression": {
                        "provider": "openai-codex",
                        "model": "gpt-5.2-codex",
                        "api_key": "SOURCE_AUX_SECRET",
                    }
                },
                "model_aliases": {"review": "openai/gpt-5.2-codex"},
                "terminal": {"cwd": "/orchestrator"},
            },
        )
        self.write_config(
            "backend-platform",
            {
                "model": {
                    "provider": "openrouter",
                    "default": "z-ai/glm-5.2",
                    "api_key": "TARGET_SECRET",
                },
                "terminal": {"cwd": "/backend"},
                "skills": {"disabled": ["example"]},
            },
        )
        self.write_config(
            "quality-review",
            {
                "model": {"provider": "openrouter", "default": "old"},
                "terminal": {"cwd": "/review"},
            },
        )

    def tearDown(self) -> None:
        self.temp.cleanup()

    def write_config(self, profile: str, value: dict) -> None:
        path = self.hermes_home / "profiles" / profile / "config.yaml"
        path.write_text(yaml.safe_dump(value, sort_keys=False), encoding="utf-8")

    def read_config(self, profile: str) -> dict:
        path = self.hermes_home / "profiles" / profile / "config.yaml"
        return yaml.safe_load(path.read_text(encoding="utf-8"))

    def args(self, *, apply: bool = False, source_profile: str | None = None):
        return MODULE.argparse.Namespace(
            preset="test-fleet",
            apply=apply,
            preset_file=self.preset,
            hermes_home=self.hermes_home,
            source_profile=source_profile,
            receipt=self.receipt,
            json_output=True,
        )

    def test_plan_is_non_mutating_and_preset_driven(self) -> None:
        before = self.read_config("backend-platform")
        code, receipt = MODULE.execute(self.args())
        self.assertEqual(code, 0)
        self.assertEqual(self.read_config("backend-platform"), before)
        self.assertEqual(
            [action["profile"] for action in receipt["actions"]],
            ["backend-platform", "quality-review"],
        )
        self.assertTrue(all(a["status"] == "PLAN_UPDATE" for a in receipt["actions"]))

    def test_apply_syncs_policy_preserves_unmanaged_config_and_target_secrets(self) -> None:
        code, receipt = MODULE.execute(self.args(apply=True))
        self.assertEqual(code, 0)
        backend = self.read_config("backend-platform")
        self.assertEqual(backend["model"]["provider"], "openai-codex")
        self.assertEqual(backend["model"]["default"], "gpt-5.2-codex")
        self.assertEqual(backend["model"]["openai_runtime"], "codex_app_server")
        self.assertEqual(backend["model"]["api_key"], "TARGET_SECRET")
        self.assertNotIn("SOURCE_SECRET_MUST_NOT_COPY", json.dumps(backend))
        self.assertNotIn("SOURCE_AUX_SECRET", json.dumps(backend))
        self.assertEqual(backend["terminal"]["cwd"], "/backend")
        self.assertEqual(backend["skills"]["disabled"], ["example"])
        self.assertFalse(receipt["credentials_copied"])
        backups = list(
            (self.hermes_home / "profiles" / "backend-platform").glob(
                "config.yaml.bak.model-sync.*"
            )
        )
        self.assertEqual(len(backups), 1)

    def test_repeated_apply_is_idempotent(self) -> None:
        MODULE.execute(self.args(apply=True))
        backup_count = len(
            list(
                (self.hermes_home / "profiles" / "backend-platform").glob(
                    "config.yaml.bak.model-sync.*"
                )
            )
        )
        _, receipt = MODULE.execute(self.args(apply=True))
        self.assertTrue(all(a["status"] == "SKIP_IN_SYNC" for a in receipt["actions"]))
        self.assertEqual(
            len(
                list(
                    (self.hermes_home / "profiles" / "backend-platform").glob(
                        "config.yaml.bak.model-sync.*"
                    )
                )
            ),
            backup_count,
        )

    def test_target_nested_secret_is_preserved_when_source_section_is_absent(self) -> None:
        source = self.read_config("engineering-orchestrator")
        source.pop("auxiliary")
        self.write_config("engineering-orchestrator", source)
        backend = self.read_config("backend-platform")
        backend["auxiliary"] = {
            "vision": {"api_key": "TARGET_VISION_SECRET", "model": "old"}
        }
        self.write_config("backend-platform", backend)
        MODULE.execute(self.args(apply=True))
        updated = self.read_config("backend-platform")
        self.assertEqual(
            updated["auxiliary"]["vision"]["api_key"], "TARGET_VISION_SECRET"
        )
        self.assertNotIn("model", updated["auxiliary"]["vision"])

    def test_source_override_must_belong_to_preset(self) -> None:
        with self.assertRaisesRegex(MODULE.SyncError, "not present"):
            MODULE.execute(self.args(source_profile="outside-profile"))

    def test_missing_target_profile_fails_closed(self) -> None:
        missing = self.hermes_home / "profiles" / "quality-review"
        (missing / "config.yaml").unlink()
        missing.rmdir()
        with self.assertRaisesRegex(MODULE.SyncError, "Missing target profile"):
            MODULE.execute(self.args())

    def test_symlinked_target_config_fails_closed(self) -> None:
        target = self.hermes_home / "profiles" / "quality-review" / "config.yaml"
        target.unlink()
        target.symlink_to(
            self.hermes_home / "profiles" / "backend-platform" / "config.yaml"
        )
        with self.assertRaisesRegex(MODULE.SyncError, "Symlinked target profile config"):
            MODULE.execute(self.args())

    def test_unconfigured_source_model_blocks(self) -> None:
        self.write_config("engineering-orchestrator", {"model": ""})
        with self.assertRaisesRegex(MODULE.SyncError, "not configured"):
            MODULE.execute(self.args())


if __name__ == "__main__":
    unittest.main()
