from pathlib import Path
import subprocess

body_path = Path("scripts/tmp-integrate-delivery-body.py")
source = body_path.read_text(encoding="utf-8")
workflow_pin_block = '''replace_once(
    ".github/workflows/skill-eval.yml",
    "ref: f94b6ad86583c714b68eb5ea9f92890557b462c5",
    "ref: fdd743c7e08acc9fc70ca02509a83317c42f2df9",
)
'''

error = None
try:
    if workflow_pin_block not in source:
        raise RuntimeError("Expected workflow pin block was not found in staged body")
    source = source.replace(workflow_pin_block, "", 1)
    exec(compile(source, str(body_path), "exec"), globals(), globals())
except BaseException as exc:
    error = f"{type(exc).__name__}: {exc}"
    subprocess.run(["git", "reset", "--hard", "HEAD"], check=True)
    Path("contracts/tests/.delivery-integration-error").write_text(
        error + "\n",
        encoding="utf-8",
    )

for staging_path in (
    ".github/workflows/skill-eval.yml",
    ".github/workflows/tmp-integrate-delivery-work-breakdown.yml",
    "scripts/tmp-integrate-delivery.py",
):
    subprocess.run(
        ["git", "update-index", "--skip-worktree", staging_path],
        check=True,
    )

if error is not None:
    print(error)
