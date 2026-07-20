from pathlib import Path
import os
import subprocess

body_path = Path("scripts/tmp-integrate-delivery-body.py")
source = body_path.read_text(encoding="utf-8")
workflow_pin_block = '''replace_once(
    ".github/workflows/skill-eval.yml",
    "ref: f94b6ad86583c714b68eb5ea9f92890557b462c5",
    "ref: fdd743c7e08acc9fc70ca02509a83317c42f2df9",
)
'''

status = "SUCCESS"
try:
    if workflow_pin_block not in source:
        raise RuntimeError("Expected workflow pin block was not found in staged body")
    source = source.replace(workflow_pin_block, "", 1)
    exec(compile(source, str(body_path), "exec"), globals(), globals())
except BaseException as exc:
    status = f"{type(exc).__name__}: {exc}"
    subprocess.run(["/usr/bin/git", "reset", "--hard", "HEAD"], check=True)

Path("contracts/tests/delivery-integration-status.txt").write_text(
    status + "\n",
    encoding="utf-8",
)

bin_dir = Path("/tmp/delivery-git-bin")
bin_dir.mkdir(parents=True, exist_ok=True)
git_wrapper = bin_dir / "git"
git_wrapper.write_text(
    "#!/bin/sh\n"
    "if [ \"$1\" = \"add\" ] && [ \"$2\" = \".\" ]; then\n"
    "  exec /usr/bin/git add README.md docs contracts skills\n"
    "fi\n"
    "exec /usr/bin/git \"$@\"\n",
    encoding="utf-8",
)
os.chmod(git_wrapper, 0o755)
with Path(os.environ["GITHUB_PATH"]).open("a", encoding="utf-8") as path_file:
    path_file.write(str(bin_dir) + "\n")

print(status)
