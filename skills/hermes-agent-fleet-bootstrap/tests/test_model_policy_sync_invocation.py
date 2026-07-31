from __future__ import annotations

import unittest
from pathlib import Path


PACKAGE = Path(__file__).resolve().parents[1]
FLEET_WRAPPER = PACKAGE / "scripts" / "hermes-fleet"
MODEL_WRAPPER = PACKAGE / "scripts" / "hermes-fleet-model-sync"
MODEL_RUNNER = PACKAGE / "scripts" / "hermes_fleet_model_sync_v2.py"
MODEL_ENGINE = PACKAGE / "scripts" / "hermes_fleet_model_sync.py"
REFERENCE = PACKAGE / "references" / "model-policy-sync.md"


class ModelPolicySyncInvocationTests(unittest.TestCase):
    def test_standard_operation_dispatches_to_model_sync_runner(self) -> None:
        wrapper = FLEET_WRAPPER.read_text(encoding="utf-8")
        self.assertIn("sync-models)", wrapper)
        self.assertIn('exec bash "$SCRIPT_DIR/hermes-fleet-model-sync" "$@"', wrapper)

    def test_reference_documents_migration_then_agent_sync(self) -> None:
        text = REFERENCE.read_text(encoding="utf-8")
        self.assertIn(
            "/hermes-agent-fleet-bootstrap migrate native-ai-engineering --apply",
            text,
        )
        self.assertIn(
            "/hermes-agent-fleet-bootstrap sync-models native-ai-engineering --apply",
            text,
        )
        self.assertIn("agent-orchestrator", text)
        self.assertIn("TARGET_ONLY_COMPLETE", text)
        self.assertIn('${HERMES_SKILL_DIR}/scripts/hermes-fleet-model-sync', text)

    def test_wrappers_are_executable_shell_scripts(self) -> None:
        for path in (FLEET_WRAPPER, MODEL_WRAPPER):
            with self.subTest(path=path):
                self.assertTrue(path.read_text(encoding="utf-8").startswith("#!/usr/bin/env bash"))

    def test_wrapper_uses_generation_two_guard(self) -> None:
        wrapper = MODEL_WRAPPER.read_text(encoding="utf-8")
        self.assertIn("hermes_fleet_model_sync_v2.py", wrapper)
        guard = MODEL_RUNNER.read_text(encoding="utf-8")
        self.assertIn("identity_generation", guard)
        self.assertIn("Legacy profile identities remain", guard)
        self.assertIn("TARGET_ONLY_COMPLETE", guard)

    def test_engine_declares_secret_exclusion(self) -> None:
        text = MODEL_ENGINE.read_text(encoding="utf-8")
        self.assertIn('"credentials_copied": False', text)
        self.assertIn("SECRET_MARKERS", text)
        self.assertNotIn("shutil.copytree", text)


if __name__ == "__main__":
    unittest.main()
