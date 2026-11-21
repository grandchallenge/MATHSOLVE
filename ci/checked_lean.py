#!/usr/bin/env python3
"""Run Lean without a shell pipeline that can mask its failure.

Process exit status, compiler diagnostics, axiom reports, and captured output
are independently checked. A zero process exit is necessary but insufficient.
"""
from __future__ import annotations

import argparse
import contextlib
import pathlib
import re
import subprocess
import sys

ANSI = re.compile(r"\x1b\[[0-9;]*[A-Za-z]")
LEAN_ERROR = re.compile(r"(?:^|[\s:])error:", re.IGNORECASE)
LEAN_WARNING = re.compile(r"(?:^|[\s:])warning:", re.IGNORECASE)
SORRY_AXIOM = re.compile(r"\bsorryAx\b")
AXIOM_REPORT = re.compile(r"^\s*'([^']+)' depends on axioms:")


def is_lean_command(command: list[str]) -> bool:
    """Accept only direct Lean or lake env lean argv, never shell execution."""
    if not command:
        return False
    basename = pathlib.Path(command[0]).name
    if basename == "lean":
        return len(command) >= 2
    if basename == "lake":
        return len(command) >= 4 and command[1:3] == ["env", "lean"]
    return False


def check_lean(
    command: list[str],
    *,
    output: pathlib.Path | None = None,
    strict_warnings: bool = False,
    require_axioms: tuple[str, ...] = (),
) -> int:
    if not is_lean_command(command):
        print("ERROR: expected direct Lean or lake env lean argv", file=sys.stderr)
        return 2
    errors: list[str] = []
    seen_axioms: set[str] = set()
    try:
        context = output.open("w", encoding="utf-8") if output else contextlib.nullcontext(None)
        with context as archive:
            with subprocess.Popen(
                command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                text=True, errors="replace", bufsize=1, shell=False,
            ) as proc:
                assert proc.stdout is not None
                for line in proc.stdout:
                    sys.stdout.write(line)
                    sys.stdout.flush()
                    if archive is not None:
                        archive.write(line)
                    clean = ANSI.sub("", line)
                    axiom = AXIOM_REPORT.match(clean)
                    if axiom:
                        seen_axioms.add(axiom.group(1))
                    if LEAN_ERROR.search(clean):
                        errors.append("Lean error diagnostic")
                    if SORRY_AXIOM.search(clean):
                        errors.append("Lean sorryAx proof-hole dependency")
                    if strict_warnings and LEAN_WARNING.search(clean):
                        errors.append("Lean warning in strict mode")
                code = proc.wait()
    except OSError as exc:
        print(f"ERROR: Lean compiler could not execute: {exc}", file=sys.stderr)
        return 127
    if code != 0:
        errors.append(f"compiler process exit status {code}")
    missing = set(require_axioms) - seen_axioms
    if missing:
        errors.append("missing axiom reports: " + ", ".join(sorted(missing)))
    if errors:
        for error in dict.fromkeys(errors):
            print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print("PASS: Lean process exit, diagnostics and required axiom reports", file=sys.stderr)
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=pathlib.Path)
    parser.add_argument("--strict-warnings", action="store_true")
    parser.add_argument("--require-axiom", action="append", default=[])
    parser.add_argument("command", nargs=argparse.REMAINDER)
    args = parser.parse_args(argv)
    command = args.command
    if command[:1] == ["--"]:
        command = command[1:]
    return check_lean(
        command, output=args.output, strict_warnings=args.strict_warnings,
        require_axioms=tuple(args.require_axiom),
    )


if __name__ == "__main__":
    raise SystemExit(main())
