"""Typed, read-only repository evidence tools plus a separately gated PR candidate.

Protected main is never mutated, and this module cannot merge PRs or bypass CI.
"""
from __future__ import annotations

import base64
import hashlib
import json
import os
from pathlib import PurePosixPath
import re
from urllib.parse import quote

from .core import Boundary, _gh, assert_identity, receipt

ALLOWED = frozenset({
    "grandchallenge/MATHSOLVE", "grandchallenge/MATH-PROGRAMME",
    "grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS",
    "grandchallenge/COMPUTATIONAL-DIFFICULTY-ATLAS",
})
SHA = re.compile(r"^[a-f0-9]{40}$")
CHANGE = re.compile(r"^[a-z0-9][a-z0-9-]{2,42}$")
DOC_PATH = re.compile(r"^(?:docs|handoffs)/[a-zA-Z0-9_.\-/]+\.md$")


def _repo(repo: str) -> str:
    if repo not in ALLOWED:
        raise Boundary("REPOSITORY_NOT_APPROVED")
    return repo


def _json_api(method: str, uri: str, data: dict | None = None) -> dict:
    if not uri.startswith("repos/grandchallenge/") or method not in ("GET", "POST", "PUT"):
        raise Boundary("REPO_API_NOT_ALLOWLISTED")
    argv = ["api", "--method", method, uri]
    if data is not None:
        argv += ["--input", "-"]
        # _gh does not permit stdin: we intentionally do not use its command
        # dispatcher for body-bearing mutations.
        raise Boundary("REPOSITORY_WRITE_NOT_ACTIVATED")
    try:
        parsed = json.loads(_gh(argv))
    except (ValueError, TypeError) as exc:
        raise Boundary("REPOSITORY_RESPONSE_MALFORMED") from exc
    if not isinstance(parsed, dict):
        raise Boundary("REPOSITORY_RESPONSE_MALFORMED")
    return parsed


def _head(repo: str) -> tuple[str, str]:
    info = _json_api("GET", f"repos/{repo}")
    branch = info.get("default_branch")
    if branch != "main":
        raise Boundary("UNEXPECTED_PROTECTED_BASE_BRANCH")
    ref = _json_api("GET", f"repos/{repo}/git/ref/heads/main")
    sha = (ref.get("object") or {}).get("sha")
    if not isinstance(sha, str) or not SHA.fullmatch(sha):
        raise Boundary("PROTECTED_HEAD_NOT_EXACT")
    return branch, sha


def repository_head(repo: str) -> dict:
    """Read an allowlisted repository's current protected default head."""
    repo = _repo(repo)
    actor = assert_identity()
    branch, sha = _head(repo)
    result = {"repository": repo, "branch": branch, "head_sha": sha,
              "operator": actor["login"], "mutation": False}
    result["receipt"] = receipt(result)
    return result


def _path(path: str) -> str:
    if not isinstance(path, str) or len(path) > 240 or path.startswith("/") or "\\" in path:
        raise Boundary("REPOSITORY_PATH_INVALID")
    parts = PurePosixPath(path).parts
    if not parts or any(p in (".", "..", "") for p in path.split("/")):
        raise Boundary("REPOSITORY_PATH_INVALID")
    if any(p.startswith(".") or p.lower() in ("secret", "secrets", "credentials", "keys") for p in parts):
        raise Boundary("REPOSITORY_SENSITIVE_PATH_DENIED")
    if parts[0] not in ("docs", "handoffs", "ci", "governance", "WORKERS.md"):
        raise Boundary("REPOSITORY_PATH_OUT_OF_SCOPE")
    return path


def repository_read_file(repo: str, path: str, expected_head: str) -> dict:
    """Read bounded file content bound to a supplied exact protected SHA."""
    repo = _repo(repo)
    path = _path(path)
    if not SHA.fullmatch(expected_head):
        raise Boundary("EXPECTED_HEAD_SHA_REQUIRED")
    assert_identity()
    _, current = _head(repo)
    if current != expected_head:
        raise Boundary("STALE_PROTECTED_HEAD")
    encoded_path = quote(path, safe="/")
    item = _json_api("GET", f"repos/{repo}/contents/{encoded_path}?ref={current}")
    if item.get("type") != "file" or item.get("encoding") != "base64":
        raise Boundary("EXPECTED_REGULAR_FILE_BASE64")
    size = item.get("size")
    if not isinstance(size, int) or size > 24_000 or size < 0:
        raise Boundary("FILE_OUTSIDE_BOUNDED_READ_SIZE")
    raw = base64.b64decode(item["content"], validate=False)
    if len(raw) != size or len(raw) > 24_000:
        raise Boundary("FILE_LENGTH_MISMATCH")
    try:
        content = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise Boundary("FILE_NOT_UTF8") from exc
    _, after = _head(repo)
    if after != current:
        raise Boundary("HEAD_MOVED_DURING_READ")
    return {"repository": repo, "path": path, "head_sha": current,
            "blob_sha": item.get("sha"), "sha256": hashlib.sha256(raw).hexdigest(),
            "content": content, "mutation": False}


def repository_pull_request(repo: str, number: int) -> dict:
    """Read PR state, author, exact head, base, and reviewer conclusions."""
    repo = _repo(repo)
    if not isinstance(number, int) or not 1 <= number <= 999999:
        raise Boundary("INVALID_PULL_NUMBER")
    assert_identity()
    p = _json_api("GET", f"repos/{repo}/pulls/{number}")
    if not isinstance(p.get("head"), dict) or not isinstance(p.get("base"), dict):
        raise Boundary("PR_IDENTITY_MISSING")
    reviews = _json_api_reviews(repo, number)
    return {"repository": repo, "number": number, "url": p.get("html_url"),
            "state": p.get("state"), "merged": p.get("merged"),
            "head": p["head"].get("sha"), "base": p["base"].get("sha"),
            "base_ref": p["base"].get("ref"),
            "author": (p.get("user") or {}).get("login"),
            "reviews": reviews, "mutation": False}


def _json_api_reviews(repo: str, number: int) -> list[dict]:
    # A bounded first page is explicitly marked non-exhaustive if full.
    reviews = json.loads(_gh(["api", "--method", "GET", f"repos/{repo}/pulls/{number}/reviews?per_page=100"]))
    if not isinstance(reviews, list):
        raise Boundary("REVIEWS_MALFORMED")
    if len(reviews) >= 100:
        raise Boundary("REVIEWS_PAGINATION_REQUIRED")
    return [{"actor": (v.get("user") or {}).get("login"),
             "state": v.get("state"), "commit_sha": v.get("commit_id")}
            for v in reviews]


def repository_document_proposal(repo: str, path: str, expected_head: str,
                                 change_id: str, markdown: str) -> dict:
    """Explicitly gated future write interface; safe until policy review/admission.

    No remote code or branch modification in the installed v0.2.0 release.
    Separate governance work is required to enable a branch-only implementation.
    """
    _repo(repo)
    _path(path)
    if not DOC_PATH.fullmatch(path) or not CHANGE.fullmatch(change_id):
        raise Boundary("PROPOSAL_SCOPE_INVALID")
    if not SHA.fullmatch(expected_head):
        raise Boundary("EXPECTED_HEAD_SHA_REQUIRED")
    if not isinstance(markdown, str) or len(markdown.encode("utf-8")) > 24_000:
        raise Boundary("PROPOSAL_CONTENT_OUT_OF_SCOPE")
    raise Boundary("REPOSITORY_WRITE_NOT_ACTIVATED_PROTECTED_REVIEW_REQUIRED")
