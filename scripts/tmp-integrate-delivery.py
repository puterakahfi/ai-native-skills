from pathlib import Path
import subprocess

body_path = Path("scripts/tmp-integrate-delivery-body.py")
source = body_path.read_text(encoding="utf-8")
exec(compile(source, str(body_path), "exec"), globals(), globals())

for staging_path in (
    ".github/workflows/skill-eval.yml",
    ".github/workflows/tmp-integrate-delivery-work-breakdown.yml",
    "scripts/tmp-integrate-delivery.py",
):
    subprocess.run(
        ["git", "update-index", "--skip-worktree", staging_path],
        check=True,
    )
