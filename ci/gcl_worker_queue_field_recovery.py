"""Fail-closed recovery for GitHub Issue Field mutations.

Exact field state is read before and after a mutation. Uncertain writes
are never repeated without proving the remote effect absent.
"""
from __future__ import annotations
import json
import subprocess


class UncertainFieldMutation(RuntimeError):
    pass


def command(argv, input_text=None):
    return subprocess.run(["gh", *argv], input=input_text, text=True,
                          capture_output=True, timeout=60)


def field_state(repo, issue, field_id):
    p = command(["api", f"repos/{repo}/issues/{issue}/issue-field-values"])
    if p.returncode:
        raise UncertainFieldMutation("field readback unavailable")
    rows = json.loads(p.stdout)
    if not isinstance(rows, list):
        raise UncertainFieldMutation("malformed field census")
    matches = [r for r in rows if str(r.get("issue_field_id")) == str(field_id)]
    if len(matches) > 1:
        raise UncertainFieldMutation("duplicate field identity")
    return matches[0] if matches else None


def apply_one(repo, issue, field_id, value):
    # None means clear. No impersonation or authority change.
    before = field_state(repo, issue, field_id)
    if value is None and before is None:
        return "ALREADY_CLEAR"
    if value is not None and before is not None and before.get("value") == value:
        return "ALREADY_SET"
    if value is None:
        argv = ["api", "--method", "DELETE",
                f"repos/{repo}/issues/{issue}/issue-field-values/{field_id}"]
        payload = None
    else:
        argv = ["api", "--method", "POST",
                f"repos/{repo}/issues/{issue}/issue-field-values", "--input", "-"]
        payload = json.dumps({"issue_field_values": [{"field_id": field_id, "value": value}]})
    try:
        p = command(argv, payload)
    except subprocess.TimeoutExpired:
        p = None
    if p is not None and p.returncode and any(k in p.stderr.lower() for k in ("403", "401", "denied", "forbidden")):
        raise UncertainFieldMutation("explicit denial; held without replay")
    after = field_state(repo, issue, field_id)
    if value is None and after is None:
        return "VERIFIED_CLEAR"
    if value is not None and after is not None and after.get("value") == value:
        return "VERIFIED_SET"
    raise UncertainFieldMutation("mutation remote effect unverified; no retry")


def main():
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--repo", required=True)
    p.add_argument("--issue", type=int, required=True)
    p.add_argument("--projection", required=True)
    a = p.parse_args()
    data = json.load(open(a.projection, encoding="utf-8"))
    if data.get("queue_managed") is not True:
        return
    results = []
    for row in data.get("issue_field_values", []):
        results.append(apply_one(a.repo, a.issue, row["field_id"], row["value"]))
    for field_id in data.get("clear_field_ids", []):
        results.append(apply_one(a.repo, a.issue, field_id, None))
    print(json.dumps({"outcomes": results}))


if __name__ == "__main__":
    main()
