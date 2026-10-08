#!/usr/bin/env python3
"""Reconcile GCL Worker Queue Project #2 Status from authoritative Issue Fields.

Status is a *worker-assignment* convenience only:
  AVAILABLE -> Todo; RESERVED/BLOCKED -> In Progress; RETURNED/CLOSED -> Done.
"Done" NEVER certifies mathematics, approves editorial work, closes an issue,
or admits/promotes any protected result. The GCL State Issue Field remains the
authority for operational discovery; dispatch and protected lease are separate.

Dry-run is the default. --apply requires authenticated organization Projects
write permission and does not mutate issues, labels, dispatches or evidence.
"""
from __future__ import annotations

import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import subprocess

ORG = "grandchallenge"
PROJECT_NUMBER = 2
REPOSITORIES = {
    "grandchallenge/MATHSOLVE",
    "grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS",
    "grandchallenge/COMPUTATIONAL-DIFFICULTY-ATLAS",
}
PROJECT_STATUS = {
    "AVAILABLE": "Todo",
    "RESERVED": "In Progress",
    "BLOCKED": "In Progress",
    "RETURNED": "Done",
    "CLOSED": "Done",
}


def expected_status(state: str) -> str:
    if state not in PROJECT_STATUS:
        raise ValueError(f"unknown issue-field GCL State {state!r}")
    return PROJECT_STATUS[state]


def validated_item(item: dict, fields: list[dict]) -> dict:
    content = item.get("content") or {}
    repo, issue = content.get("repository"), content.get("number")
    if repo not in REPOSITORIES or not isinstance(issue, int):
        raise ValueError(f"unrecognized queue item identity: {repo}#{issue}")
    url = content.get("url")
    if url != f"https://github.com/{repo}/issues/{issue}":
        raise ValueError(f"unbound issue URL for {repo}#{issue}: {url!r}")
    entries = [
        (entry.get("single_select_option") or {}).get("name")
        for entry in fields
        if entry.get("issue_field_name") == "GCL State"
    ]
    if len(entries) != 1 or not entries[0]:
        raise ValueError(f"missing or duplicate authoritative state {repo}#{issue}: {entries}")
    state = entries[0]
    target = expected_status(state)
    labels = set(item.get("labels") or [])
    labels_found = {x for x in labels if x.startswith("gcl-state:")}
    expected_label = f"gcl-state:{state.lower()}"
    # BLOCKED can be operationally represented through Issue Fields alone;
    # no inference from an unprocessed RESULT/1, lease, or GitHub Project value.
    if labels_found and labels_found != {expected_label}:
        raise ValueError(f"label/Issue Field conflict on {repo}#{issue}: {state}, {labels_found}")
    if state in {"AVAILABLE", "RETURNED"} and expected_label not in labels_found:
        raise ValueError(f"missing expected label on {repo}#{issue}: {state}")
    if item.get("status") not in {"Todo", "In Progress", "Done"}:
        raise ValueError(f"unknown Project Status on {repo}#{issue}")
    if not item.get("id"):
        raise ValueError(f"missing project item identity on {repo}#{issue}")
    return {
        "repo": repo,
        "issue": issue,
        "url": url,
        "item_id": item["id"],
        "state": state,
        "from_status": item["status"],
        "to_status": target,
    }


def gh(args: list[str]) -> str:
    proc = subprocess.run(["gh", *args], capture_output=True, text=True, timeout=75, check=False)
    if proc.returncode:
        raise RuntimeError(f"gh invocation failed: {args[:4]}: {proc.stderr[:350]}")
    return proc.stdout


def issue_fields(repo: str, issue: int) -> list[dict]:
    return json.loads(gh(["api", f"repos/{repo}/issues/{issue}/issue-field-values"]))


def project_items() -> list[dict]:
    data = json.loads(
        gh(["project", "item-list", str(PROJECT_NUMBER),
            "--owner", ORG, "--format", "json", "--limit", "500"])
    )
    items = data.get("items") or []
    if not items or len(items) != data.get("totalCount"):
        raise ValueError("Project listing incomplete or empty; refuse partial reconciliation")
    if len({x["id"] for x in items}) != len(items):
        raise ValueError("Duplicate Project item identity")
    return items


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true",
                        help="mutate Project Status after complete read-only validation")
    parser.add_argument("--report", type=Path, help="write a JSON audit snapshot")
    args = parser.parse_args()

    items = project_items()
    with ThreadPoolExecutor(max_workers=6) as pool:
        rows = list(pool.map(
            lambda item: validated_item(
                item, issue_fields(item["content"]["repository"], item["content"]["number"])
            ), items
        ))
    changes = [r for r in rows if r["from_status"] != r["to_status"]]
    report = {
        "project": f"https://github.com/orgs/{ORG}/projects/{PROJECT_NUMBER}",
        "items": len(rows),
        "issue_field_states": dict(Counter(r["state"] for r in rows)),
        "current_project_status": dict(Counter(r["from_status"] for r in rows)),
        "target_project_status": dict(Counter(r["to_status"] for r in rows)),
        "changes": changes,
        "applied": False,
        "boundary": "Project Status only; no result adjudication, chapter acceptance, certification or protected dispatch mutation",
    }
    print(json.dumps({k: v for k, v in report.items() if k != "changes"}, sort_keys=True), flush=True)
    print("STATUS_UPDATES", len(changes), flush=True)

    if args.apply:
        for index, item in enumerate(changes, 1):
            # Reject concurrent state changes; do not replay a stale plan.
            validated_now = validated_item(
                {"content": {"repository": item["repo"], "number": item["issue"],
                             "url": item["url"]}, "id": item["item_id"],
                 "status": item["from_status"],
                 "labels": json.loads(gh(["api", f"repos/{item['repo']}/issues/{item['issue']}"])) .get("labels", [])},
                issue_fields(item["repo"], item["issue"]),
            )
            if validated_now["state"] != item["state"]:
                raise RuntimeError(f"state changed during reconciliation: {item['url']}")
            gh(["project", "item-edit", str(PROJECT_NUMBER), "--owner", ORG,
                "--url", item["url"], "--field", "Status",
                "--value", item["to_status"]])
            if index % 10 == 0:
                print(f"APPLIED {index}/{len(changes)}", flush=True)
        current = {i["id"]: i["status"] for i in project_items()}
        mistakes = [r for r in rows if current.get(r["item_id"]) != r["to_status"]]
        if mistakes:
            raise RuntimeError(f"Project Status readback mismatch: {mistakes[:3]}")
        report["applied"] = True
        print("SUCCESS exact-item board projection and readback", flush=True)

    if args.report:
        args.report.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
