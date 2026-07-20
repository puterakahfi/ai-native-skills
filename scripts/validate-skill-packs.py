#!/usr/bin/env python3
"""Validate canonical ai-native-skills pack manifests and documentation drift."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import yaml

ROOT = Path(__file__).resolve().parents[1]
SUPPORTED_SCHEMA_VERSIONS = {"1.0"}
ALLOWED_CLASSIFICATIONS = {
    "required",
    "conditional",
    "port",
    "adapter",
    "domain-reviewer",
    "optional",
}
SEMVER_PATTERN = re.compile(r"^\d+\.\d+\.\d+$")
IDENTIFIER_PATTERN = re.compile(r"^[a-z0-9][a-z0-9-]*$")
REPOSITORY_PATTERN = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")


class PackError(ValueError):
    """Raised when a skill pack manifest or generated surface is invalid."""


@dataclass(frozen=True)
class Dependency:
    name: str
    classification: str
    concern: str
    port: str | None = None


@dataclass(frozen=True)
class ValidatedPack:
    schema_version: str
    pack_id: str
    version: str
    path: Path
    repository: str
    entrypoints: tuple[str, ...]
    dependencies: tuple[Dependency, ...]
    profiles: dict[str, tuple[str, ...]]
    workflow: str
    manifest_metadata_key: str
    version_metadata_key: str
    compatibility_requires: tuple[str, ...]
    documentation_file: Path
    documentation_heading: str
    documentation_profile: str
    pack_dependencies: tuple[str, ...]


def require_string(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise PackError(f"{label} must be a non-empty string")
    return value.strip()


def require_identifier(value: Any, label: str) -> str:
    identifier = require_string(value, label)
    if not IDENTIFIER_PATTERN.fullmatch(identifier):
        raise PackError(f"{label} must match {IDENTIFIER_PATTERN.pattern}")
    return identifier


def require_string_list(
    value: Any,
    label: str,
    *,
    allow_empty: bool = False,
    identifiers: bool = False,
) -> list[str]:
    if not isinstance(value, list):
        raise PackError(f"{label} must be a list")
    parser = require_identifier if identifiers else require_string
    result = [parser(item, f"{label}[{index}]") for index, item in enumerate(value)]
    if not allow_empty and not result:
        raise PackError(f"{label} must not be empty")
    duplicates = sorted({item for item in result if result.count(item) > 1})
    if duplicates:
        raise PackError(f"{label} contains duplicate entries: {duplicates}")
    return result


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        document = yaml.safe_load(handle)
    if not isinstance(document, dict):
        raise PackError(f"{path}: root must be a mapping")
    return document


def parse_skill_frontmatter(skill_file: Path) -> dict[str, Any]:
    if not skill_file.is_file():
        raise PackError(f"Referenced local skill does not exist: {skill_file}")
    text = skill_file.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise PackError(f"{skill_file}: missing YAML frontmatter")
    parts = text.split("---", 2)
    if len(parts) < 3:
        raise PackError(f"{skill_file}: malformed YAML frontmatter")
    frontmatter = yaml.safe_load(parts[1])
    if not isinstance(frontmatter, dict):
        raise PackError(f"{skill_file}: frontmatter must be a mapping")
    return frontmatter


def resolve_profile(
    entrypoints: Iterable[str],
    dependencies: Iterable[Dependency],
    classifications: Iterable[str],
) -> tuple[str, ...]:
    included = set(classifications)
    return tuple(entrypoints) + tuple(
        dependency.name
        for dependency in dependencies
        if dependency.classification in included
    )


def validate_local_skill(name: str, root: Path) -> None:
    skill_file = root / "skills" / name / "SKILL.md"
    frontmatter = parse_skill_frontmatter(skill_file)
    declared_name = require_identifier(frontmatter.get("name"), f"{skill_file}: name")
    if declared_name != name:
        raise PackError(
            f"{skill_file}: frontmatter name '{declared_name}' does not match dependency '{name}'"
        )


def validate_dependency(
    raw_dependency: Any,
    *,
    index: int,
    path: Path,
    root: Path,
) -> Dependency:
    label = f"{path}: skill_pack.dependencies[{index}]"
    if not isinstance(raw_dependency, dict):
        raise PackError(f"{label} must be a mapping")

    name = require_identifier(raw_dependency.get("name"), f"{label}.name")
    classification = require_string(
        raw_dependency.get("classification"), f"{label}.classification"
    )
    if classification not in ALLOWED_CLASSIFICATIONS:
        raise PackError(
            f"{label}.classification '{classification}' is invalid; "
            f"expected one of {sorted(ALLOWED_CLASSIFICATIONS)}"
        )

    raw_concern = raw_dependency.get("concern")
    if raw_concern is None and classification in {"adapter", "domain-reviewer"}:
        concern = name
    else:
        concern = require_identifier(raw_concern, f"{label}.concern")
    require_string(raw_dependency.get("reason"), f"{label}.reason")

    when = raw_dependency.get("when")
    if classification in {"conditional", "domain-reviewer"}:
        require_string(when, f"{label}.when")
    elif when is not None:
        require_string(when, f"{label}.when")

    port = raw_dependency.get("port")
    if port is not None:
        port = require_identifier(port, f"{label}.port")
    if classification == "adapter" and port is None:
        raise PackError(f"{label}: adapter dependency must declare port")
    if classification != "adapter" and port is not None:
        raise PackError(f"{label}: only adapter dependencies may declare port")

    if classification == "domain-reviewer":
        require_string_list(
            raw_dependency.get("domains"), f"{label}.domains", identifiers=True
        )

    source = require_string(raw_dependency.get("source", "local"), f"{label}.source")
    if source == "local":
        validate_local_skill(name, root)
    elif source == "external":
        repository = require_string(raw_dependency.get("repository"), f"{label}.repository")
        if not REPOSITORY_PATTERN.fullmatch(repository):
            raise PackError(f"{label}.repository must be owner/repository")
        require_string(raw_dependency.get("ref"), f"{label}.ref")
    else:
        raise PackError(f"{label}.source must be local or external")

    return Dependency(name, classification, concern, port)


def validate_pack_document(
    path: Path,
    document: dict[str, Any],
    root: Path = ROOT,
) -> ValidatedPack:
    pack = document.get("skill_pack")
    if not isinstance(pack, dict):
        raise PackError(f"{path}: missing skill_pack mapping")

    schema_version = require_string(
        pack.get("schema_version"), f"{path}: skill_pack.schema_version"
    )
    if schema_version not in SUPPORTED_SCHEMA_VERSIONS:
        raise PackError(
            f"{path}: unsupported schema_version '{schema_version}'; "
            f"supported={sorted(SUPPORTED_SCHEMA_VERSIONS)}"
        )

    pack_id = require_identifier(pack.get("id"), f"{path}: skill_pack.id")
    if pack_id != path.parent.name:
        raise PackError(
            f"{path}: pack id '{pack_id}' does not match directory '{path.parent.name}'"
        )

    version = require_string(pack.get("version"), f"{path}: skill_pack.version")
    if not SEMVER_PATTERN.fullmatch(version):
        raise PackError(f"{path}: skill_pack.version must be semantic x.y.z")

    repository = require_string(pack.get("repository"), f"{path}: skill_pack.repository")
    if not REPOSITORY_PATTERN.fullmatch(repository):
        raise PackError(f"{path}: skill_pack.repository must be owner/repository")

    entrypoints = require_string_list(
        pack.get("entrypoints"), f"{path}: skill_pack.entrypoints", identifiers=True
    )
    for entrypoint in entrypoints:
        validate_local_skill(entrypoint, root)

    raw_dependencies = pack.get("dependencies")
    if not isinstance(raw_dependencies, list) or not raw_dependencies:
        raise PackError(f"{path}: skill_pack.dependencies must be a non-empty list")

    dependencies: list[Dependency] = []
    seen_names = set(entrypoints)
    port_concerns: set[str] = set()
    pending_adapter_ports: list[tuple[str, str]] = []

    for index, raw_dependency in enumerate(raw_dependencies):
        dependency = validate_dependency(
            raw_dependency, index=index, path=path, root=root
        )
        if dependency.name in seen_names:
            raise PackError(f"{path}: duplicate skill dependency '{dependency.name}'")
        seen_names.add(dependency.name)
        if dependency.classification == "port":
            if dependency.concern in port_concerns:
                raise PackError(f"{path}: duplicate port concern '{dependency.concern}'")
            port_concerns.add(dependency.concern)
        if dependency.classification == "adapter":
            assert dependency.port is not None
            pending_adapter_ports.append((dependency.name, dependency.port))
        dependencies.append(dependency)

    for adapter_name, port in pending_adapter_ports:
        if port not in port_concerns:
            raise PackError(
                f"{path}: adapter '{adapter_name}' references unknown port concern '{port}'"
            )

    raw_profiles = pack.get("profiles")
    if not isinstance(raw_profiles, dict) or not raw_profiles:
        raise PackError(f"{path}: skill_pack.profiles must be a non-empty mapping")

    profiles: dict[str, tuple[str, ...]] = {}
    for raw_profile_name, raw_profile in raw_profiles.items():
        profile_name = require_identifier(raw_profile_name, f"{path}: profile name")
        profile_label = f"{path}: skill_pack.profiles.{profile_name}"
        if not isinstance(raw_profile, dict):
            raise PackError(f"{profile_label} must be a mapping")
        require_string(raw_profile.get("description"), f"{profile_label}.description")
        classifications = require_string_list(
            raw_profile.get("include_classifications"),
            f"{profile_label}.include_classifications",
        )
        invalid = sorted(set(classifications) - ALLOWED_CLASSIFICATIONS)
        if invalid:
            raise PackError(f"{profile_label} contains invalid classifications: {invalid}")
        profiles[profile_name] = resolve_profile(entrypoints, dependencies, classifications)

    compatibility = pack.get("compatibility")
    if not isinstance(compatibility, dict):
        raise PackError(f"{path}: skill_pack.compatibility must be a mapping")
    workflow = require_identifier(
        compatibility.get("workflow"), f"{path}: compatibility.workflow"
    )
    if workflow not in entrypoints:
        raise PackError(f"{path}: compatibility.workflow must be an entrypoint")
    manifest_metadata_key = require_string(
        compatibility.get("manifest_metadata_key"),
        f"{path}: compatibility.manifest_metadata_key",
    )
    version_metadata_key = require_string(
        compatibility.get("version_metadata_key"),
        f"{path}: compatibility.version_metadata_key",
    )
    requires_classifications = require_string_list(
        compatibility.get("requires_classifications"),
        f"{path}: compatibility.requires_classifications",
    )
    invalid_requires = sorted(set(requires_classifications) - ALLOWED_CLASSIFICATIONS)
    if invalid_requires:
        raise PackError(
            f"{path}: compatibility.requires_classifications contains invalid values: {invalid_requires}"
        )
    included = set(requires_classifications)
    compatibility_requires = tuple(
        dependency.name
        for dependency in dependencies
        if dependency.classification in included
    )

    documentation = pack.get("documentation")
    if not isinstance(documentation, dict):
        raise PackError(f"{path}: skill_pack.documentation must be a mapping")
    documentation_file = root / require_string(
        documentation.get("file"), f"{path}: documentation.file"
    )
    documentation_heading = require_string(
        documentation.get("heading"), f"{path}: documentation.heading"
    )
    documentation_profile = require_identifier(
        documentation.get("profile"), f"{path}: documentation.profile"
    )
    if documentation_profile not in profiles:
        raise PackError(
            f"{path}: documentation profile '{documentation_profile}' is not defined"
        )

    pack_dependencies = tuple(
        require_string_list(
            pack.get("pack_dependencies", []),
            f"{path}: skill_pack.pack_dependencies",
            allow_empty=True,
            identifiers=True,
        )
    )

    return ValidatedPack(
        schema_version=schema_version,
        pack_id=pack_id,
        version=version,
        path=path,
        repository=repository,
        entrypoints=tuple(entrypoints),
        dependencies=tuple(dependencies),
        profiles=profiles,
        workflow=workflow,
        manifest_metadata_key=manifest_metadata_key,
        version_metadata_key=version_metadata_key,
        compatibility_requires=compatibility_requires,
        documentation_file=documentation_file,
        documentation_heading=documentation_heading,
        documentation_profile=documentation_profile,
        pack_dependencies=pack_dependencies,
    )


def validate_workflow_binding(pack: ValidatedPack, root: Path = ROOT) -> None:
    skill_file = root / "skills" / pack.workflow / "SKILL.md"
    frontmatter = parse_skill_frontmatter(skill_file)
    metadata = frontmatter.get("metadata")
    if not isinstance(metadata, dict):
        raise PackError(f"{skill_file}: metadata must be a mapping")

    expected_manifest = pack.path.relative_to(root).as_posix()
    declared_manifest = require_string(
        metadata.get(pack.manifest_metadata_key),
        f"{skill_file}: metadata.{pack.manifest_metadata_key}",
    )
    if declared_manifest != expected_manifest:
        raise PackError(
            f"{skill_file}: {pack.manifest_metadata_key} must be "
            f"'{expected_manifest}', got '{declared_manifest}'"
        )

    declared_version = require_string(
        metadata.get(pack.version_metadata_key),
        f"{skill_file}: metadata.{pack.version_metadata_key}",
    )
    if declared_version != pack.version:
        raise PackError(
            f"{skill_file}: pack version binding must be '{pack.version}', "
            f"got '{declared_version}'"
        )

    declared_requires = tuple(
        require_string(
            metadata.get("ai-native-skills.requires"),
            f"{skill_file}: metadata.ai-native-skills.requires",
        ).split()
    )
    if declared_requires != pack.compatibility_requires:
        missing = [item for item in pack.compatibility_requires if item not in declared_requires]
        unexpected = [item for item in declared_requires if item not in pack.compatibility_requires]
        duplicates = sorted(
            {item for item in declared_requires if declared_requires.count(item) > 1}
        )
        order_mismatch = not missing and not unexpected and not duplicates
        raise PackError(
            f"{skill_file}: compatibility requires drift; missing={missing}, "
            f"unexpected={unexpected}, duplicates={duplicates}, "
            f"order_mismatch={order_mismatch}"
        )


def extract_documented_command(path: Path, heading: str) -> str:
    if not path.is_file():
        raise PackError(f"Pack documentation does not exist: {path}")
    text = path.read_text(encoding="utf-8")
    heading_index = text.find(heading)
    if heading_index < 0:
        raise PackError(f"{path}: missing heading '{heading}'")
    next_heading = text.find("\n## ", heading_index + len(heading))
    section = text[heading_index : next_heading if next_heading >= 0 else len(text)]
    block_match = re.search(r"```bash\n(?P<body>.*?)\n```", section, flags=re.DOTALL)
    if block_match is None:
        raise PackError(f"{path}: heading '{heading}' has no bash install block")
    return block_match.group("body").strip()


def render_install_command(pack: ValidatedPack, profile: str) -> str:
    if profile not in pack.profiles:
        raise PackError(f"Pack '{pack.pack_id}' has no profile '{profile}'")
    lines = [f"npx skills add {pack.repository} \\"]
    for skill in pack.profiles[profile]:
        lines.append(f"  --skill {skill} \\")
    lines.append("  -g -y")
    return "\n".join(lines)


def validate_documentation(pack: ValidatedPack) -> None:
    documented = extract_documented_command(
        pack.documentation_file, pack.documentation_heading
    )
    expected = render_install_command(pack, pack.documentation_profile)
    if documented != expected:
        raise PackError(
            f"{pack.documentation_file}: documented {pack.pack_id} command drift; "
            f"expected:\n{expected}\nactual:\n{documented}"
        )


def validate_pack_graph(packs: dict[str, ValidatedPack]) -> None:
    for pack in packs.values():
        unknown = sorted(set(pack.pack_dependencies) - set(packs))
        if unknown:
            raise PackError(f"{pack.path}: unknown pack dependencies: {unknown}")

    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(pack_id: str, trail: list[str]) -> None:
        if pack_id in visiting:
            cycle_start = trail.index(pack_id)
            cycle = trail[cycle_start:] + [pack_id]
            raise PackError(f"Skill pack dependency cycle detected: {' -> '.join(cycle)}")
        if pack_id in visited:
            return
        visiting.add(pack_id)
        trail.append(pack_id)
        for dependency in packs[pack_id].pack_dependencies:
            visit(dependency, trail)
        trail.pop()
        visiting.remove(pack_id)
        visited.add(pack_id)

    for pack_id in sorted(packs):
        visit(pack_id, [])


def load_packs(root: Path = ROOT) -> dict[str, ValidatedPack]:
    pack_paths = sorted((root / "packs").glob("*/pack.yaml"))
    if not pack_paths:
        raise PackError(f"No skill pack manifests found under {root / 'packs'}")
    packs: dict[str, ValidatedPack] = {}
    for path in pack_paths:
        validated = validate_pack_document(path, load_yaml(path), root)
        if validated.pack_id in packs:
            raise PackError(f"Duplicate skill pack id '{validated.pack_id}'")
        packs[validated.pack_id] = validated
    validate_pack_graph(packs)
    return packs


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate skill pack manifests")
    parser.add_argument("--pack", help="Validate only one pack id")
    parser.add_argument("--profile", default="complete", help="Profile for command output")
    parser.add_argument(
        "--print-install-command",
        action="store_true",
        help="Print the resolved install command after validation",
    )
    parser.add_argument(
        "--skip-docs",
        action="store_true",
        help="Skip documentation drift validation",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    packs = load_packs()
    if args.pack and args.pack not in packs:
        raise PackError(f"Unknown skill pack '{args.pack}'")
    selected = {args.pack: packs[args.pack]} if args.pack else packs

    for pack_id, pack in selected.items():
        validate_workflow_binding(pack)
        if not args.skip_docs:
            validate_documentation(pack)
        print(
            f"✓ {pack_id}: {len(pack.dependencies)} dependencies, "
            f"{len(pack.profiles)} profile(s)"
        )
        if args.print_install_command:
            print(render_install_command(pack, args.profile))

    print(f"Validated {len(selected)} skill pack(s)")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (PackError, yaml.YAMLError) as error:
        print(f"skill pack validation failed: {error}", file=sys.stderr)
        raise SystemExit(1) from error
