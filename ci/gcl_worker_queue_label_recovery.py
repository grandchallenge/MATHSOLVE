"""Readback-bound operational label reconciliation for GCL worker queue."""
import argparse
import json
import subprocess
from pathlib import Path


class LabelUncertain(RuntimeError):
    pass


def gh(*args):
    return subprocess.run(["gh", *args], text=True, capture_output=True, timeout=60)


def current_labels(repo, issue):
    p = gh("api", f"repos/{repo}/issues/{issue}")
    if p.returncode:
        raise LabelUncertain("authoritative issue readback unavailable")
    data = json.loads(p.stdout)
    if not isinstance(data.get("labels"), list):
        raise LabelUncertain("malformed issue label census")
    return {r["name"] for r in data["labels"]}


def set_label(repo, issue, label, present):
    before = current_labels(repo, issue)
    if (label in before) == present:
        return "ALREADY_CORRECT"
    args = ["issue", "edit", str(issue), "--repo", repo,
            "--add-label" if present else "--remove-label", label]
    try:
        result = gh(*args)
    except subprocess.TimeoutExpired:
        result = None
    if result is not None and result.returncode and any(x in result.stderr.lower() for x in ("403", "401", "denied", "forbidden")):
        raise LabelUncertain("explicit denial; held without alternate mutation")
    if (label in current_labels(repo, issue)) != present:
        raise LabelUncertain("label mutation unverified; no replay")
    return "VERIFIED"


def reconcile(repo, issue, add, remove):
    if set(add) & set(remove):
        raise ValueError("conflicting target label sets")
    outcomes = []
    for label in add:
        # Creation is metadata setup; the queue config must register labels already.
        outcomes.append((label, set_label(repo, issue, label, True)))
    for label in remove:
        outcomes.append((label, set_label(repo, issue, label, False)))
    return outcomes


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--repo", required=True)
    p.add_argument("--issue", type=int, required=True)
    p.add_argument("--add-file", type=Path)
    p.add_argument("--remove-file", type=Path)
    p.add_argument("--add", action="append", default=[])
    p.add_argument("--remove", action="append", default=[])
    a = p.parse_args()
    def lines(path):
        return [x for x in path.read_text().splitlines() if x] if path else []
    print(json.dumps(reconcile(a.repo, a.issue, a.add + lines(a.add_file),
                               a.remove + lines(a.remove_file))))


if __name__ == "__main__":
    main()
