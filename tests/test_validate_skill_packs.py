from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "validate-skill-packs.py"
SPEC = importlib.util.spec_from_file_location("validate_skill_packs", MODULE_PATH)
assert SPEC and SPEC.loader
validator = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = validator
SPEC.loader.exec_module(validator)


class SkillPackValidatorTest(unittest.TestCase):
    def make_repo(self, dependencies: list[dict], *, pack_dependencies: list[str] | None = None):
        temp = tempfile.TemporaryDirectory()
        root = Path(temp.name)
        (root / "packs" / "example").mkdir(parents=True)
        (root / "docs").mkdir()

        names = [
            "entrypoint",
            *(
                dependency["name"]
                for dependency in dependencies
                if dependency.get("source", "local") == "local"
            ),
        ]
        for name in names:
            skill_dir = root / "skills" / name
            skill_dir.mkdir(parents=True, exist_ok=True)
            pack_line = (
                "  ai-native-skills.pack: packs/example/pack.yaml\n"
                if name == "entrypoint"
                else ""
            )
            version_line = (
                '  ai-native-skills.pack-version: "1.0.0"\n'
                if name == "entrypoint"
                else ""
            )
            requires = " ".join(
                dependency["name"]
                for dependency in dependencies
                if dependency["classification"] in {"required", "conditional", "port"}
            )
            requires_line = (
                f'  ai-native-skills.requires: "{requires}"\n'
                if name == "entrypoint"
                else ""
            )
            (skill_dir / "SKILL.md").write_text(
                "---\n"
                f"name: {name}\n"
                "description: test\n"
                "metadata:\n"
                f"{pack_line}{version_line}{requires_line}"
                "  ai-native-skills.version: 1.0.0\n"
                "---\n",
                encoding="utf-8",
            )

        document = {
            "skill_pack": {
                "schema_version": "1.0",
                "id": "example",
                "version": "1.0.0",
                "repository": "owner/repo",
                "entrypoints": ["entrypoint"],
                "compatibility": {
                    "workflow": "entrypoint",
                    "manifest_metadata_key": "ai-native-skills.pack",
                    "version_metadata_key": "ai-native-skills.pack-version",
                    "requires_classifications": ["required", "conditional", "port"],
                },
                "dependencies": dependencies,
                "profiles": {
                    "complete": {
                        "description": "complete",
                        "include_classifications": [
                            "required",
                            "conditional",
                            "port",
                            "adapter",
                            "domain-reviewer",
                        ],
                    }
                },
                "documentation": {
                    "file": "docs/skill-packs.md",
                    "heading": "## Example Pack",
                    "profile": "complete",
                },
                "pack_dependencies": pack_dependencies or [],
            }
        }
        path = root / "packs" / "example" / "pack.yaml"
        path.write_text(yaml.safe_dump(document, sort_keys=False), encoding="utf-8")
        return temp, root, path, document

    def valid_dependencies(self):
        return [
            {"name": "alpha", "classification": "required", "concern": "a", "reason": "a"},
            {
                "name": "beta",
                "classification": "conditional",
                "concern": "b",
                "reason": "b",
                "when": "needed",
            },
        ]

    def test_duplicate_dependency_is_rejected(self):
        dependencies = [
            {"name": "alpha", "classification": "required", "concern": "a", "reason": "a"},
            {"name": "alpha", "classification": "optional", "concern": "b", "reason": "b"},
        ]
        temp, root, path, document = self.make_repo(dependencies)
        self.addCleanup(temp.cleanup)
        with self.assertRaisesRegex(validator.PackError, "duplicate skill dependency"):
            validator.validate_pack_document(path, document, root)

    def test_adapter_requires_known_port(self):
        dependencies = [
            {
                "name": "visual-port",
                "classification": "port",
                "concern": "visual",
                "reason": "port",
            },
            {
                "name": "adapter",
                "classification": "adapter",
                "port": "missing",
                "reason": "adapter",
            },
        ]
        temp, root, path, document = self.make_repo(dependencies)
        self.addCleanup(temp.cleanup)
        with self.assertRaisesRegex(validator.PackError, "unknown port concern"):
            validator.validate_pack_document(path, document, root)

    def test_invalid_classification_is_rejected(self):
        dependencies = [
            {"name": "alpha", "classification": "hard", "concern": "a", "reason": "a"},
        ]
        temp, root, path, document = self.make_repo(dependencies)
        self.addCleanup(temp.cleanup)
        with self.assertRaisesRegex(validator.PackError, "classification 'hard' is invalid"):
            validator.validate_pack_document(path, document, root)

    def test_unsupported_schema_is_rejected(self):
        temp, root, path, document = self.make_repo(self.valid_dependencies())
        self.addCleanup(temp.cleanup)
        document["skill_pack"]["schema_version"] = "2.0"
        with self.assertRaisesRegex(validator.PackError, "unsupported schema_version"):
            validator.validate_pack_document(path, document, root)

    def test_external_dependency_requires_repository_and_ref(self):
        dependencies = [
            {
                "name": "external-skill",
                "classification": "required",
                "concern": "external",
                "reason": "external",
                "source": "external",
                "repository": "owner/repo",
            }
        ]
        temp, root, path, document = self.make_repo(dependencies)
        self.addCleanup(temp.cleanup)
        with self.assertRaisesRegex(validator.PackError, r"\.ref must be a non-empty string"):
            validator.validate_pack_document(path, document, root)

    def test_domain_reviewer_requires_activation_condition(self):
        dependencies = [
            {
                "name": "reviewer",
                "classification": "domain-reviewer",
                "domains": ["brand-identity"],
                "reason": "review",
            }
        ]
        temp, root, path, document = self.make_repo(dependencies)
        self.addCleanup(temp.cleanup)
        with self.assertRaisesRegex(validator.PackError, r"\.when must be a non-empty string"):
            validator.validate_pack_document(path, document, root)

    def test_documented_full_command_must_match_profile(self):
        temp, root, path, document = self.make_repo(self.valid_dependencies())
        self.addCleanup(temp.cleanup)
        pack = validator.validate_pack_document(path, document, root)
        wrong = validator.render_install_command(pack, "complete").replace(
            "owner/repo", "other/repo"
        )
        (root / "docs" / "skill-packs.md").write_text(
            f"## Example Pack\n\n```bash\n{wrong}\n```\n", encoding="utf-8"
        )
        with self.assertRaisesRegex(validator.PackError, "command drift"):
            validator.validate_documentation(pack)

    def test_workflow_requires_order_and_duplicates_are_validated(self):
        temp, root, path, document = self.make_repo(self.valid_dependencies())
        self.addCleanup(temp.cleanup)
        pack = validator.validate_pack_document(path, document, root)
        workflow = root / "skills" / "entrypoint" / "SKILL.md"
        text = workflow.read_text(encoding="utf-8").replace(
            'ai-native-skills.requires: "alpha beta"',
            'ai-native-skills.requires: "beta alpha alpha"',
        )
        workflow.write_text(text, encoding="utf-8")
        with self.assertRaisesRegex(validator.PackError, "duplicates="):
            validator.validate_workflow_binding(pack, root)

    def test_pack_version_binding_is_validated(self):
        temp, root, path, document = self.make_repo(self.valid_dependencies())
        self.addCleanup(temp.cleanup)
        pack = validator.validate_pack_document(path, document, root)
        workflow = root / "skills" / "entrypoint" / "SKILL.md"
        text = workflow.read_text(encoding="utf-8").replace(
            'ai-native-skills.pack-version: "1.0.0"',
            'ai-native-skills.pack-version: "2.0.0"',
        )
        workflow.write_text(text, encoding="utf-8")
        with self.assertRaisesRegex(validator.PackError, "pack version binding"):
            validator.validate_workflow_binding(pack, root)

    def test_pack_dependency_cycle_is_rejected(self):
        base = dict(
            schema_version="1.0",
            version="1.0.0",
            repository="owner/repo",
            entrypoints=("entrypoint",),
            dependencies=(),
            profiles={"complete": ("entrypoint",)},
            workflow="entrypoint",
            manifest_metadata_key="ai-native-skills.pack",
            version_metadata_key="ai-native-skills.pack-version",
            compatibility_requires=(),
            documentation_file=Path("docs/skill-packs.md"),
            documentation_heading="## Example",
            documentation_profile="complete",
        )
        packs = {
            "alpha": validator.ValidatedPack(
                pack_id="alpha",
                path=Path("packs/alpha/pack.yaml"),
                pack_dependencies=("beta",),
                **base,
            ),
            "beta": validator.ValidatedPack(
                pack_id="beta",
                path=Path("packs/beta/pack.yaml"),
                pack_dependencies=("alpha",),
                **base,
            ),
        }
        with self.assertRaisesRegex(validator.PackError, "dependency cycle detected"):
            validator.validate_pack_graph(packs)

    def test_render_install_command(self):
        dependencies = [
            {"name": "alpha", "classification": "required", "concern": "a", "reason": "a"},
            {"name": "beta", "classification": "optional", "concern": "b", "reason": "b"},
        ]
        temp, root, path, document = self.make_repo(dependencies)
        self.addCleanup(temp.cleanup)
        pack = validator.validate_pack_document(path, document, root)
        command = validator.render_install_command(pack, "complete")
        self.assertIn("--skill entrypoint", command)
        self.assertIn("--skill alpha", command)
        self.assertNotIn("--skill beta", command)
        self.assertTrue(command.endswith("-g -y"))


if __name__ == "__main__":
    unittest.main()
