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

        names = ["entrypoint", *(dependency["name"] for dependency in dependencies)]
        for name in names:
            skill_dir = root / "skills" / name
            skill_dir.mkdir(parents=True, exist_ok=True)
            pack_line = "  ai-native-skills.pack: packs/example/pack.yaml\n" if name == "entrypoint" else ""
            requires = " ".join(
                dependency["name"]
                for dependency in dependencies
                if dependency["classification"] in {"required", "conditional", "port"}
            )
            requires_line = (
                f"  ai-native-skills.requires: \"{requires}\"\n" if name == "entrypoint" else ""
            )
            (skill_dir / "SKILL.md").write_text(
                "---\n"
                f"name: {name}\n"
                "description: test\n"
                "metadata:\n"
                f"{pack_line}{requires_line}"
                "  ai-native-skills.version: 1.0.0\n"
                "---\n",
                encoding="utf-8",
            )

        document = {
            "skill_pack": {
                "id": "example",
                "version": "1.0.0",
                "repository": "owner/repo",
                "entrypoints": ["entrypoint"],
                "compatibility": {
                    "workflow": "entrypoint",
                    "manifest_metadata_key": "ai-native-skills.pack",
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
            {"name": "visual-port", "classification": "port", "concern": "visual", "reason": "port"},
            {"name": "adapter", "classification": "adapter", "concern": "color", "port": "missing", "reason": "adapter"},
        ]
        temp, root, path, document = self.make_repo(dependencies)
        self.addCleanup(temp.cleanup)
        with self.assertRaisesRegex(validator.PackError, "unknown port concern"):
            validator.validate_pack_document(path, document, root)

    def test_documented_order_must_match_profile(self):
        dependencies = [
            {"name": "alpha", "classification": "required", "concern": "a", "reason": "a"},
            {"name": "beta", "classification": "conditional", "concern": "b", "reason": "b", "when": "needed"},
        ]
        temp, root, path, document = self.make_repo(dependencies)
        self.addCleanup(temp.cleanup)
        pack = validator.validate_pack_document(path, document, root)
        (root / "docs" / "skill-packs.md").write_text(
            "## Example Pack\n\n```bash\n"
            "npx skills add owner/repo \\\n"
            "  --skill entrypoint \\\n"
            "  --skill beta \\\n"
            "  --skill alpha \\\n"
            "  -g -y\n```\n",
            encoding="utf-8",
        )
        with self.assertRaisesRegex(validator.PackError, "order_mismatch=True"):
            validator.validate_documentation(pack)

    def test_invalid_classification_is_rejected(self):
        dependencies = [
            {"name": "alpha", "classification": "hard", "concern": "a", "reason": "a"},
        ]
        temp, root, path, document = self.make_repo(dependencies)
        self.addCleanup(temp.cleanup)
        with self.assertRaisesRegex(validator.PackError, "classification 'hard' is invalid"):
            validator.validate_pack_document(path, document, root)

    def test_pack_dependency_cycle_is_rejected(self):
        base = dict(
            repository="owner/repo",
            entrypoints=("entrypoint",),
            dependencies=(),
            profiles={"complete": ("entrypoint",)},
            workflow="entrypoint",
            metadata_key="ai-native-skills.pack",
            compatibility_requires=(),
            documentation_file=Path("docs/skill-packs.md"),
            documentation_heading="## Example",
            documentation_profile="complete",
        )
        packs = {
            "alpha": validator.ValidatedPack(
                pack_id="alpha", path=Path("packs/alpha/pack.yaml"), pack_dependencies=("beta",), **base
            ),
            "beta": validator.ValidatedPack(
                pack_id="beta", path=Path("packs/beta/pack.yaml"), pack_dependencies=("alpha",), **base
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


if __name__ == "__main__":
    unittest.main()
