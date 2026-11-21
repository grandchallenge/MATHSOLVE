#!/usr/bin/env python3
"""Required guard against shell pipelines masking Lean compiler failures.

Scan all repository GitHub workflow run steps; any local Lean/lake compilation
must use ci/checked_lean.py instead of a raw shell command. A pinned external
container replay is separately constrained to a non-pipelined, fail-fast shell.
"""
from __future__ import annotations

import pathlib
import re
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / ".github" / "workflows"
COMPILER = re.compile(
    r"(?<![\w/.])(?:lake[ \t]+env[ \t]+lean[ \t]+|"
    r"lake[ \t]+build(?:[ \t]+|$)|"
    r"lean[ \t]+(?!-{1,2}(?:version|help|numeric-version)\b))",
    re.IGNORECASE,
)
RUNNER = re.compile(r"^python(?:3(?:\.\d+)?)?\s+.*checked_lean\.py\b")
SHELL_OPERATORS = re.compile(r"\|\||(?<!\|)\|(?!\|)|&&|[;&]")
ALLOWED_EXTERNAL = (".github/workflows/openmath-kobon-bader93.yml", "h7-pinned-lean")


def shell_has_unquoted_pipe(script: str) -> bool:
    """Identify shell pipeline/OR operators, ignoring quoted grep regexes."""
    quote = ""
    escaped = False
    comment = False
    for idx, char in enumerate(script):
        if char == "\n":
            comment = False
        if comment:
            continue
        if escaped:
            escaped = False
            continue
        if char == "\\" and quote != "'":
            escaped = True
            continue
        if quote:
            if char == quote:
                quote = ""
            continue
        if char in ("'", '"'):
            quote = char
            continue
        if char == "#" and (idx == 0 or script[idx - 1].isspace()):
            comment = True
            continue
        if char == "|":
            return True
    return False


def errors_for_run(
    script: str, *,
    relative_path: str, job: str, step_name: str,
) -> list[str]:
    found: list[str] = []
    if COMPILER.search(script) and shell_has_unquoted_pipe(script):
        found.append(
            f"{relative_path}:{job}:{step_name}: "
            "unquoted shell pipe/OR in a Lean compilation step is forbidden"
        )
    for lineno, raw in enumerate(script.splitlines(), start=1):
        if raw.lstrip().startswith("#"):
            continue
        match = COMPILER.search(raw)
        if not match:
            continue
        prefix = raw[:match.start()].strip()
        suffix = raw[match.end():]
        location = f"{relative_path}:{job}:{step_name}:line {lineno}"
        if (relative_path, job) == ALLOWED_EXTERNAL:
            # This exact digest-pinned Docker step uses Lean inside its own
            # fail-fast bash -lc and deliberately has no host-side wrapper.
            if (
                "docker run " in script
                and "ghcr.io/ottogin/lean-mathlib@sha256:" in script
                and "bash -lc 'set -euo pipefail;" in script
                and "| tee" not in script
                and "|| true" not in script
            ):
                continue
            found.append(f"{location}: external Lean has lost its pinned fail-fast container")
            continue
        if not RUNNER.search(prefix):
            found.append(f"{location}: local Lean/lake compiler must use checked_lean.py")
            continue
        # The Python runner itself is the last safety boundary. Piping its
        # exit to tee (or ignoring it with || true) would undo that boundary.
        if SHELL_OPERATORS.search(suffix):
            found.append(f"{location}: shell operator after checked_lean.py masks exit")
    return found


def scan(root: pathlib.Path = ROOT) -> list[str]:
    found: list[str] = []
    runner_path = root / "ci" / "checked_lean.py"
    if not runner_path.is_file():
        found.append("missing mandatory ci/checked_lean.py")
    workflows = root / ".github" / "workflows"
    files = sorted([*workflows.glob("*.yml"), *workflows.glob("*.yaml")])
    if not files:
        return found + ["no GitHub workflows to audit"]
    for path in files:
        relative = path.relative_to(root).as_posix()
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
        except (OSError, yaml.YAMLError) as exc:
            found.append(f"{relative}: YAML unreadable: {exc}")
            continue
        if not isinstance(data, dict) or not isinstance(data.get("jobs"), dict):
            found.append(f"{relative}: jobs map absent")
            continue
        for jobname, jobvalue in data["jobs"].items():
            if not isinstance(jobvalue, dict):
                continue
            steps = jobvalue.get("steps") or []
            if not isinstance(steps, list):
                found.append(f"{relative}:{jobname}: steps not a list")
                continue
            for idx, step in enumerate(steps):
                if not isinstance(step, dict):
                    continue
                run = step.get("run")
                if not isinstance(run, str):
                    continue
                found.extend(errors_for_run(
                    run, relative_path=relative, job=str(jobname),
                    step_name=str(step.get("name") or idx),
                ))
    # The validator is not optional: it runs in the existing ledgers check
    # which is already REQUIRED by the protected main ruleset.
    ci = root / ".github/workflows/ci.yml"
    try:
        data = yaml.safe_load(ci.read_text(encoding="utf-8"))
        steps = data["jobs"]["ledgers"]["steps"]
        guarded = [
            step for step in steps if isinstance(step, dict)
            and "python ci/validate_lean_ci_integrity.py" in str(step.get("run") or "")
            and "python -m unittest tests/test_lean_ci_integrity.py" in str(step.get("run") or "")
            and not step.get("if")
        ]
        if len(guarded) != 1:
            found.append("required ledgers check missing unconditional Lean guard and regression suite")
    except (KeyError, TypeError, OSError, yaml.YAMLError):
        found.append("cannot verify Lean guard binding to required ledgers job")
    return found


def main() -> int:
    found = scan()
    if found:
        for problem in found:
            print("FAIL: " + problem, file=sys.stderr)
        print(f"Lean workflow safety: {len(found)} violation(s)", file=sys.stderr)
        return 1
    print("PASS: Lean workflow invocations use checked runner or pinned fail-fast container")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
