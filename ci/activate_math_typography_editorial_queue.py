#!/usr/bin/env python3
"""One-shot, idempotent GCL Project #2 activation for MATH-TYPOGRAPHY-REMEDIATION-001.

Requires `gh` authenticated as an existing operator with organization
Projects write permission and MATH-PROGRAMME issue write permission.
Dry-run by default; --apply mutates only the nine explicitly bound issues.
The Project and Issue Fields are a discovery projection, not execution authority.
"""
from __future__ import annotations

import argparse
import base64
import json
import subprocess
import sys

OWNER = "grandchallenge"
REPO = "grandchallenge/MATH-PROGRAMME"
PROJECT = 2
ISSUE_FIRST = 1256
ISSUE_LAST = 1264
PARENT = 1255
CAMPAIGN = "MATH-TYPOGRAPHY-REMEDIATION-001"
PR = 1034
ROLE_BY_ISSUE = {
    1256: ("CONSTRUCTIVE", "constructive", "AVAILABLE", "SHARED"),
    1257: ("CONSTRUCTIVE", "constructive", "AVAILABLE", "SHARED"),
    1258: ("CONSTRUCTIVE", "constructive", "AVAILABLE", "SHARED"),
    1259: ("CONSTRUCTIVE", "constructive", "AVAILABLE", "SHARED"),
    1260: ("CONSTRUCTIVE", "constructive", "AVAILABLE", "SHARED"),
    1261: ("CONSTRUCTIVE", "constructive", "AVAILABLE", "SHARED"),
    1262: ("SOURCE", "source-audit", "AVAILABLE", "SHARED"),
    1263: ("VERIFY", "verify", "BLOCKED", "VERIFICATION"),
    1264: ("SOURCE", "source-audit", "BLOCKED", "SHARED"),
}
FIELDS = {
    "GCL State": 47953501,
    "GCL Campaign": 47953502,
    "GCL Role": 47953503,
    "GCL Collaboration": 47953504,
    "GCL Phase": 47953505,
}
PROJECT_ITEM_STATUS = {"AVAILABLE": "Todo", "BLOCKED": "In Progress"}
REQUIRED_MODE = "direct_editorial"

def gh(*args: str, data: object | None = None) -> str:
    cmd = ["gh", *args]
    proc = subprocess.run(
        cmd, input=None if data is None else json.dumps(data),
        text=True, encoding="utf-8", capture_output=True, check=False, timeout=90,
    )
    if proc.returncode:
        raise RuntimeError(
            f"GitHub command failed: {cmd[:5]}: {proc.stderr[:500]}"
        )
    return proc.stdout

def api(url: str, *, method: str | None = None, payload: object | None = None):
    args = ["api"]
    if method:
        args += ["--method", method]
    args.append(url)
    if payload is not None:
        args += ["--input", "-"]
    return json.loads(gh(*args, data=payload))

def url(n: int) -> str:
    return f"https://github.com/{REPO}/issues/{n}"

def project_items() -> dict[str, dict]:
    data = json.loads(gh("project", "item-list", str(PROJECT), "--owner", OWNER,
                         "--format", "json", "--limit", "500"))
    rows = data.get("items") or []
    if len(rows) != data.get("totalCount"):
        raise RuntimeError("Incomplete Project listing; do not mutate based on partial data")
    links = [str((row.get("content") or {}).get("url") or "") for row in rows]
    if len(links) != len(set(links)):
        raise RuntimeError("Duplicate Project content URLs, refusing ambiguous operation")
    return {link: row for link, row in zip(links, rows)}

def issue(n: int) -> dict:
    return api(f"repos/{REPO}/issues/{n}")

def verify_authority() -> None:
    login = api("user").get("login")
    if login not in {"fyremael", "jimsteeg"}:
        raise RuntimeError(f"Unrecognized queue operator {login!r}")
    merged = api(f"repos/{OWNER}/MATHSOLVE/pulls/{PR}")
    if merged.get("merged") is not True:
        raise RuntimeError("Protected pickup-mode PR #1034 has not merged")
    content = api(
        "repos/grandchallenge/MATHSOLVE/contents/"
        ".well-known/gcl-worker-queue.json?ref=main"
    )
    source = base64.b64decode(content["content"]).decode("utf-8")
    mapping = json.loads(source).get("repository_pickup_modes") or {}
    if mapping.get(REPO) != REQUIRED_MODE:
        raise RuntimeError("Current protected worker bootstrap does not admit this repository")
    print(f"Authenticated operator {login}: protected pickup mode confirmed")

def preflight() -> dict[str, dict]:
    verify_authority()
    existing = project_items()  # also tests actual Projects read capability
    for n, (role, role_label, state, phase) in ROLE_BY_ISSUE.items():
        record = issue(n)
        if record.get("state") != "open":
            raise RuntimeError(f"{n}: issue no longer open")
        labels = {x["name"] for x in record.get("labels", [])}
        required = {"gcl-job", "gcl-pickup:direct-editorial",
                    "gcl-collab:cooperative", f"gcl-role:{role_label}"}
        if not required.issubset(labels):
            raise RuntimeError(f"{n}: required pickup labels missing: {sorted(required-labels)}")
        if "gcl-state:returned" in labels or "gcl-state:reserved" in labels:
            raise RuntimeError(f"{n}: already returned or reserved")
        if state != "AVAILABLE" and "gcl-state:available" in labels:
            raise RuntimeError(f"{n}: dependency-blocked assignment incorrectly available")
        if state == "AVAILABLE" and any(
            x.startswith("gcl-state:") and x != "gcl-state:available"
            for x in labels
        ):
            raise RuntimeError(f"{n}: conflicting queue-state label {labels}")
        # The zero-context work item binds the immutable parent issue URL.
        if f"issues/{PARENT}" not in str(record.get("body") or ""):
            raise RuntimeError(f"{n}: missing campaign parent identity")
    return existing

def field_payload(n: int) -> dict:
    role, _, state, phase = ROLE_BY_ISSUE[n]
    values = {
        "GCL State": state, "GCL Campaign": CAMPAIGN,
        "GCL Role": role, "GCL Collaboration": "COOPERATIVE",
        "GCL Phase": phase,
    }
    return {"issue_field_values": [
        {"field_id": FIELDS[name], "value": value}
        for name, value in values.items()
    ]}

def check_fields(n: int) -> None:
    rows = api(f"repos/{REPO}/issues/{n}/issue-field-values")
    by_name = {}
    for row in rows:
        name = row.get("issue_field_name")
        if not name or name in by_name:
            raise RuntimeError(f"{n}: duplicate/unnamed authoritative Issue Field {name!r}")
        option = row.get("single_select_option") or {}
        by_name[name] = option.get("name") or row.get("value")
    expected = {("GCL State", ROLE_BY_ISSUE[n][2]),
                ("GCL Campaign", CAMPAIGN),
                ("GCL Role", ROLE_BY_ISSUE[n][0]),
                ("GCL Collaboration", "COOPERATIVE"),
                ("GCL Phase", ROLE_BY_ISSUE[n][3])}
    for field, wanted in expected:
        if by_name.get(field) != wanted:
            raise RuntimeError(
                f"{n}: authoritative Issue Field drift: {field}: "
                f"{by_name.get(field)!r} != {wanted!r}"
            )

def verify_one(n: int, items: dict[str, dict]) -> None:
    link = url(n)
    entry = items.get(link)
    if not entry:
        raise RuntimeError(f"{n}: missing from GCL Project #2")
    state = ROLE_BY_ISSUE[n][2]
    if entry.get("status") != PROJECT_ITEM_STATUS[state]:
        raise RuntimeError(f"{n}: presentation Status does not match {state}")
    labels = {x["name"] for x in issue(n).get("labels", [])}
    state_label = "gcl-state:" + state.lower()
    if state == "AVAILABLE" and state_label not in labels:
        raise RuntimeError(f"{n}: no available label despite AVAILABLE field")
    if state == "BLOCKED" and "gcl-state:available" in labels:
        raise RuntimeError(f"{n}: blocked job exposed by available label")
    check_fields(n)

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true",
                    help="perform queue item, Issue Field, label and board writes")
    args = ap.parse_args()
    existing = preflight()
    print(json.dumps({
        "project": f"https://github.com/orgs/{OWNER}/projects/{PROJECT}",
        "planned_jobs": [{"issue": n, "state": meta[2], "role": meta[0],
                          "already_in_project": url(n) in existing}
                         for n, meta in ROLE_BY_ISSUE.items()],
        "mode": "apply" if args.apply else "dry-run",
    }, indent=2))
    if not args.apply:
        return 0
    for n in sorted(ROLE_BY_ISSUE):
        link = url(n)
        if link not in existing:
            gh("project", "item-add", str(PROJECT), "--owner", OWNER,
               "--url", link, "--format", "json")
        # Fail closed in BLOCKED while setting all metadata, then expose the
        # issue only after the pickup labels and Issue Fields agree.
        state = ROLE_BY_ISSUE[n][2]
        payload = field_payload(n)
        if state == "AVAILABLE":
            for row in payload["issue_field_values"]:
                if row["field_id"] == FIELDS["GCL State"]:
                    row["value"] = "BLOCKED"
        api(f"repos/{REPO}/issues/{n}/issue-field-values",
            method="POST", payload=payload)
        if state == "AVAILABLE":
            gh("issue", "edit", str(n), "--repo", REPO,
               "--add-label", "gcl-state:available")
            # This is the final transition into the discoverable AVAILABLE view.
            api(f"repos/{REPO}/issues/{n}/issue-field-values",
                method="POST", payload=field_payload(n))
        gh("project", "item-edit", str(PROJECT), "--owner", OWNER,
           "--url", link, "--field", "Status", "--value",
           PROJECT_ITEM_STATUS[state])
        print(f"Initialized {REPO}#{n}: {state}", flush=True)
    current = project_items()
    for n in sorted(ROLE_BY_ISSUE):
        verify_one(n, current)
    print("PASS: nine Project items, authoritative Issue Fields, labels "
          "and presentation statuses read back; 7 AVAILABLE, 2 BLOCKED")
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except (ValueError, OSError, RuntimeError, subprocess.TimeoutExpired) as exc:
        print(f"QUEUE POPULATION BLOCKED: {exc}", file=sys.stderr)
        sys.exit(2)
