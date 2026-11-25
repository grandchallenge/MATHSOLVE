#!/usr/bin/env python3
"""Exactly-bound reservation-response posting with remote-effect reconciliation.

A failed post is not retried. Readback establishes whether it already landed.
Explicit permission/policy denial is never bypassed or retried.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import subprocess

MARKER = "GCL-QUEUE-RESPONSE-ORIGIN/1"
TRUSTED_ACTOR = "github-actions[bot]"


class ResponseUncertain(RuntimeError):
    pass


def call(args: list[str], *, input_text: str | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(["gh", *args], input=input_text, text=True,
                          capture_output=True, timeout=60)


def history(repo: str, issue: int) -> list[dict]:
    p = call(["api", "--paginate", f"repos/{repo}/issues/{issue}/comments?per_page=100",
              "--jq", ".[] | {id,body,author:.user.login,author_type:.user.type} | @json"])
    if p.returncode:
        raise ResponseUncertain("authoritative issue comment readback unavailable")
    try:
        rows = [json.loads(line) for line in p.stdout.splitlines() if line.strip()]
    except (ValueError, TypeError) as e:
        raise ResponseUncertain("malformed remote response census") from e
    if any(not isinstance(x.get("id"), int) or not isinstance(x.get("body"), str) for x in rows):
        raise ResponseUncertain("malformed remote comment")
    if len({x["id"] for x in rows}) != len(rows):
        raise ResponseUncertain("duplicate remote comment identities")
    return rows


def response_body(original: str, command_comment_id: int) -> str:
    if command_comment_id < 1 or MARKER in original:
        raise ValueError("invalid source command or nested custody marker")
    return original.rstrip("\n") + "\n\n" + MARKER + "\nsource_comment_id: " + str(command_comment_id) + "\n"


def reconcile(rows: list[dict], expected: str, command_comment_id: int) -> int | None:
    suffix = MARKER + "\nsource_comment_id: " + str(command_comment_id) + "\n"
    # A public commenter can copy a response and custody marker. Only the
    # authenticated controller bot may satisfy authoritative readback.
    same = [x for x in rows if x.get("author") == TRUSTED_ACTOR
            and x.get("author_type") == "Bot" and suffix in x["body"]]
    if len(same) > 1:
        raise ResponseUncertain("duplicate responses for one source command")
    if same:
        if same[0]["body"] != expected:
            raise ResponseUncertain("conflicting response for source command")
        return same[0]["id"]
    return None


def post_once(repo: str, issue: int, command_comment_id: int, response: str) -> dict:
    expected = response_body(response, command_comment_id)
    existing = reconcile(history(repo, issue), expected, command_comment_id)
    if existing is not None:
        return {"outcome": "ALREADY_POSTED", "comment_id": existing}
    try:
        p = call(["api", "--method", "POST", f"repos/{repo}/issues/{issue}/comments",
                  "--input", "-"], input_text=json.dumps({"body": expected}))
    except subprocess.TimeoutExpired:
        p = None
    if p is not None and p.returncode and ("403" in p.stderr or "401" in p.stderr or "denied" in p.stderr.lower()):
        raise ResponseUncertain("explicit GitHub denial: operation held without retry")
    # Even on a successful local exit, remote effect requires readback.
    actual = reconcile(history(repo, issue), expected, command_comment_id)
    if actual is None:
        raise ResponseUncertain("post effect unverified; no automatic replay")
    return {"outcome": "VERIFIED_POSTED", "comment_id": actual}


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--repo", required=True)
    p.add_argument("--issue", required=True, type=int)
    p.add_argument("--source-comment-id", required=True, type=int)
    p.add_argument("--body-file", required=True, type=Path)
    a = p.parse_args()
    print(json.dumps(post_once(a.repo, a.issue, a.source_comment_id,
                               a.body_file.read_text(encoding="utf-8")), sort_keys=True))


if __name__ == "__main__":
    main()
