#!/usr/bin/env python3
"""Audit/reconcile GCL Worker Queue Project #2 from authoritative Issue Fields.

This script is deliberately fail-closed. It validates both lifecycle projection
and pickup-mode routing before it will change Project Status.

Project Status is worker-assignment presentation only:
  AVAILABLE -> Todo; RESERVED/BLOCKED -> In Progress; RETURNED/CLOSED -> Done.

Pickup mode is repository-bound:
  grandchallenge/MATHSOLVE -> reservation_controlled
  Atlas repositories -> direct_editorial + gcl-pickup:direct-editorial

No Project value, label, or reservation certifies mathematics or authorizes
merge/publication/release.
"""
from __future__ import annotations

import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
BOOTSTRAP = ROOT / ".well-known/gcl-worker-queue.json"
ORG = "grandchallenge"
PROJECT_NUMBER = 2
DIRECT_LABEL = "gcl-pickup:direct-editorial"
PROJECT_STATUS = {
    "AVAILABLE": "Todo",
    "RESERVED": "In Progress",
    "BLOCKED": "In Progress",
    "RETURNED": "Done",
    "CLOSED": "Done",
}


def load_bootstrap() -> dict:
    return json.loads(BOOTSTRAP.read_text(encoding="utf-8"))


def repository_pickup_modes() -> dict[str, str]:
    modes = load_bootstrap().get("repository_pickup_modes") or {}
    if not isinstance(modes, dict) or not modes:
        raise ValueError("worker bootstrap repository pickup-mode map missing")
    return {str(k): str(v) for k, v in modes.items()}


def expected_status(state: str) -> str:
    if state not in PROJECT_STATUS:
        raise ValueError(f"unknown issue-field GCL State {state!r}")
    return PROJECT_STATUS[state]


def field_entries(fields: list[dict], name: str) -> list[dict]:
    return [entry for entry in fields if entry.get("issue_field_name") == name]


def single_select_value(fields: list[dict], name: str) -> str:
    entries = field_entries(fields, name)
    values = [(entry.get("single_select_option") or {}).get("name") for entry in entries]
    if len(values) != 1 or not values[0]:
        raise ValueError(f"missing or duplicate authoritative field {name}: {values}")
    return str(values[0])


def text_value(fields: list[dict], name: str) -> str:
    entries = field_entries(fields, name)
    values = [entry.get("value") for entry in entries]
    if len(values) != 1 or not isinstance(values[0], str) or not values[0].strip():
        raise ValueError(f"missing or duplicate authoritative field {name}: {values}")
    return values[0].strip()


def expected_pickup_mode(repo: str, labels: set[str], state: str) -> str:
    modes = repository_pickup_modes()
    if repo not in modes:
        raise ValueError(f"unconfigured queue repository: {repo}")
    mode = modes[repo]
    pickup_labels = {x for x in labels if x.startswith("gcl-pickup:")}

    if mode == "direct_editorial":
        if pickup_labels != {DIRECT_LABEL}:
            raise ValueError(
                f"direct-editorial pickup label mismatch on {repo}: {sorted(pickup_labels)}"
            )
        if state == "RESERVED":
            raise ValueError(f"direct-editorial job cannot enter reservation state: {repo}")
    elif mode == "reservation_controlled":
        if pickup_labels:
            raise ValueError(
                f"reservation-controlled job has direct/unknown pickup label on {repo}: "
                f"{sorted(pickup_labels)}"
            )
    else:
        raise ValueError(f"unknown configured pickup mode {mode!r} for {repo}")
    return mode


def validated_item(item: dict, fields: list[dict]) -> dict:
    content = item.get("content") or {}
    repo, issue = content.get("repository"), content.get("number")
    if not isinstance(repo, str) or not isinstance(issue, int):
        raise ValueError(f"unrecognized queue item identity: {repo}#{issue}")
    if repo not in repository_pickup_modes():
        raise ValueError(f"unrecognized queue repository: {repo}")

    url = content.get("url")
    if url != f"https://github.com/{repo}/issues/{issue}":
        raise ValueError(f"unbound issue URL for {repo}#{issue}: {url!r}")

    state = single_select_value(fields, "GCL State")
    campaign = text_value(fields, "GCL Campaign")
    role = single_select_value(fields, "GCL Role")
    collaboration = single_select_value(fields, "GCL Collaboration")
    phase = single_select_value(fields, "GCL Phase")
    target = expected_status(state)

    labels = set(item.get("labels") or [])
    if "gcl-job" not in labels:
        raise ValueError(f"queue item lacks gcl-job label: {repo}#{issue}")

    state_labels = {x for x in labels if x.startswith("gcl-state:")}
    expected_label = f"gcl-state:{state.lower()}"
    if state_labels and state_labels != {expected_label}:
        raise ValueError(
            f"label/Issue Field conflict on {repo}#{issue}: {state}, {state_labels}"
        )
    if state in {"AVAILABLE", "RETURNED"} and expected_label not in state_labels:
        raise ValueError(f"missing expected label on {repo}#{issue}: {state}")

    pickup_mode = expected_pickup_mode(repo, labels, state)

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
        "campaign": campaign,
        "role": role,
        "collaboration": collaboration,
        "phase": phase,
        "pickup_mode": pickup_mode,
        "from_status": item["status"],
        "to_status": target,
    }


def gh(args: list[str]) -> str:
    proc = subprocess.run(
        ["gh", *args], capture_output=True, text=True, encoding="utf-8", errors="strict", timeout=75, check=False
    )
    if proc.returncode:
        raise RuntimeError(f"gh invocation failed: {args[:4]}: {proc.stderr[:350]}")
    return proc.stdout


def issue_fields(repo: str, issue: int) -> list[dict]:
    return json.loads(gh(["api", f"repos/{repo}/issues/{issue}/issue-field-values"]))


def issue_labels(repo: str, issue: int) -> list[str]:
    issue_data = json.loads(gh(["api", f"repos/{repo}/issues/{issue}"]))
    return [str(v["name"]) for v in issue_data.get("labels", [])]


def project_items() -> list[dict]:
    data = json.loads(
        gh([
            "project", "item-list", str(PROJECT_NUMBER),
            "--owner", ORG, "--format", "json", "--limit", "500",
        ])
    )
    items = data.get("items") or []
    if not items or len(items) != data.get("totalCount"):
        raise ValueError("Project listing incomplete or empty; refuse partial reconciliation")
    if len({x["id"] for x in items}) != len(items):
        raise ValueError("duplicate Project item identity")
    return items


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--apply", action="store_true",
        help="mutate Project Status after complete pickup/lifecycle validation",
    )
    parser.add_argument("--report", type=Path, help="write a JSON audit snapshot")
    args = parser.parse_args()

    items = project_items()
    with ThreadPoolExecutor(max_workers=6) as pool:
        rows = list(pool.map(
            lambda item: validated_item(
                item,
                issue_fields(
                    item["content"]["repository"], item["content"]["number"]
                ),
            ),
            items,
        ))

    changes = [r for r in rows if r["from_status"] != r["to_status"]]
    report = {
        "project": f"https://github.com/orgs/{ORG}/projects/{PROJECT_NUMBER}",
        "items": len(rows),
        "issue_field_states": dict(Counter(r["state"] for r in rows)),
        "pickup_modes": dict(Counter(r["pickup_mode"] for r in rows)),
        "repositories": dict(Counter(r["repo"] for r in rows)),
        "current_project_status": dict(Counter(r["from_status"] for r in rows)),
        "target_project_status": dict(Counter(r["to_status"] for r in rows)),
        "changes": changes,
        "applied": False,
        "boundary": (
            "Project Status only; pickup-mode validation is fail-closed; "
            "no result adjudication, chapter acceptance, certification, merge, or release"
        ),
    }
    print(
        json.dumps({k: v for k, v in report.items() if k != "changes"}, sort_keys=True),
        flush=True,
    )
    print("STATUS_UPDATES", len(changes), flush=True)

    if args.apply:
        for index, item in enumerate(changes, 1):
            # Reject concurrent lifecycle or pickup changes; never replay a stale plan.
            current_item = {
                "content": {
                    "repository": item["repo"],
                    "number": item["issue"],
                    "url": item["url"],
                },
                "id": item["item_id"],
                "status": item["from_status"],
                "labels": issue_labels(item["repo"], item["issue"]),
            }
            validated_now = validated_item(
                current_item, issue_fields(item["repo"], item["issue"])
            )
            if (
                validated_now["state"] != item["state"]
                or validated_now["pickup_mode"] != item["pickup_mode"]
            ):
                raise RuntimeError(f"state/pickup mode changed during reconciliation: {item['url']}")

            gh([
                "project", "item-edit", str(PROJECT_NUMBER),
                "--owner", ORG,
                "--url", item["url"],
                "--field", "Status",
                "--value", item["to_status"],
            ])
            if index % 10 == 0:
                print(f"APPLIED {index}/{len(changes)}", flush=True)

        current = {i["id"]: i["status"] for i in project_items()}
        mistakes = [r for r in rows if current.get(r["item_id"]) != r["to_status"]]
        if mistakes:
            raise RuntimeError(f"Project Status readback mismatch: {mistakes[:3]}")
        report["applied"] = True
        print("SUCCESS pickup contract + exact-item board projection + readback", flush=True)

    if args.report:
        args.report.write_text(
            json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
