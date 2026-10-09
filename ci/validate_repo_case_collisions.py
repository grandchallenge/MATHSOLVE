#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import sys
import unicodedata
from collections import defaultdict


def tracked_paths() -> list[str]:
    proc = subprocess.run(
        ["git", "ls-files", "-z"],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return [p.decode("utf-8") for p in proc.stdout.split(b"\0") if p]


def collision_key(path: str) -> str:
    # Windows/macOS portability: normalize Unicode and case-fold every path.
    return unicodedata.normalize("NFC", path).casefold()


def main() -> int:
    groups: dict[str, list[str]] = defaultdict(list)
    for path in tracked_paths():
        groups[collision_key(path)].append(path)

    collisions = [
        sorted(paths)
        for paths in groups.values()
        if len(set(paths)) > 1
    ]
    if collisions:
        print("FAIL: repository contains case/Unicode-fold path collisions")
        for paths in sorted(collisions):
            print("  COLLISION:")
            for path in paths:
                print(f"    {path}")
        return 1

    print("PASS: tracked repository paths are case/Unicode-fold collision-free")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
