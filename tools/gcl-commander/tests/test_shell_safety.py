"""CHAD shell durability: operational scripts must never close a pasted/sourcing shell."""
from pathlib import Path
import subprocess

SCRIPTS = Path(__file__).resolve().parents[1] / "deploy"


def run_shell(src):
    return subprocess.run(["bash", "-c", src], capture_output=True, text=True, timeout=10)


def test_packaged_scripts_syntax():
    for name in ("install-wsl.sh", "upgrade-wsl.sh"):
        p = subprocess.run(["bash", "-n", str(SCRIPTS / name)], capture_output=True, text=True)
        assert p.returncode == 0, p.stderr


def test_accidental_source_is_safe_and_does_not_change_shell_flags():
    for name in ("install-wsl.sh", "upgrade-wsl.sh"):
        p = SCRIPTS / name
        script = f"source '{p}'; case $- in *e*|*u*) exit 30 ;; esac; printf SHELL_ALIVE"
        result = run_shell(script)
        assert result.returncode == 0, result.stderr
        assert result.stdout == "SHELL_ALIVE"
        assert "source is not supported" in result.stderr


def test_failed_upgrade_in_if_does_not_exit_parent_with_errexit():
    p = SCRIPTS / "upgrade-wsl.sh"
    # A missing package MUST be a child-only failure even when caller uses set -e.
    script = ("set -e; "
              f"if bash '{p}' '/definitely/absent/gcl-commander.zip' >/dev/null 2>&1; "
              "then printf UNEXPECTED; else printf CHILD_FAILED; fi; "
              "printf SHELL_ALIVE")
    result = run_shell(script)
    assert result.returncode == 0, result.stderr
    assert result.stdout == "CHILD_FAILEDSHELL_ALIVE"


def test_readme_uses_conditional_child_not_global_errexit():
    content = (SCRIPTS.parent / "README.md").read_text()
    assert "if bash -s <<'GCL_SAFE_UPGRADE'" in content
    section = content.split("## CHAD-safe copy/paste upgrade", 1)[1]
    assert section.index("if bash -s <<'GCL_SAFE_UPGRADE'") < section.index("set -euo pipefail")
    assert "else\n  printf '%s\\n' 'GCL Commander upgrade/audit returned an error" in section


def test_documented_paste_wrapper_catches_failure_even_with_errexit():
    import re
    content = (SCRIPTS.parent / "README.md").read_text()
    section = content.split("## CHAD-safe copy/paste upgrade", 1)[1]
    match = re.search(r"```bash\n(.*?)\n```", section, re.S)
    assert match
    pasted = match.group(1).replace(
        "ZIP=/mnt/d/Downloads/GCL-Commander-v0.1.4.zip",
        "ZIP=/definitely/absent/GCL-Commander-v0.1.4.zip",
    )
    result = run_shell("set -e\n" + pasted + "\nprintf PARENT_SURVIVED\n")
    assert result.returncode == 0, result.stderr
    assert result.stdout.endswith("PARENT_SURVIVED")
    assert "WSL shell remains open" in result.stderr
