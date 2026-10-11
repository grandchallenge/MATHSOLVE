#!/usr/bin/env python3
"""Fail-closed post-merge ED01–ED07 queue reconciliation and ED08 activation.

Run only from protected MATHSOLVE main with an authorized gh Projects-write
identity. --apply is explicit. No queue/project label is claim authority.
"""
from __future__ import annotations
import argparse
import json
import os
import subprocess
from pathlib import Path

from gcl_queue_class_contract import classify

ORG = "grandchallenge"
REPO = "grandchallenge/MATH-PROGRAMME"
PROJECT_NUMBER = "2"
PARENT = 1255
PRS = {1256: 2543, 1257: 2544, 1258: 2545, 1259: 2547,
       1260: 2548, 1261: 2549, 1262: 2551}
SUCCESSOR = 1263
ARCHIVE = 1264
BINDING = json.loads(
    (Path(__file__).resolve().parents[1] / ".gcl/worker_queue/PROJECT.json").read_text()
)
PROJECT_ID = BINDING["project"]["id"]
STATE_FIELD = BINDING["issue_fields"]["state"]["rest_id"]
STATUS_FIELD = BINDING["project_status_field"]
EXPECTED = {**{n: "RETURNED" for n in PRS}, SUCCESSOR: "AVAILABLE"}


def gh(*args: str, payload: object | None = None) -> str:
    p = subprocess.run(["gh", *args], input=json.dumps(payload) if payload is not None else None,
                       text=True, encoding="utf-8", capture_output=True, timeout=120)
    if p.returncode:
        raise RuntimeError(f"gh {' '.join(args[:4])}: {p.stderr[:400]}")
    return p.stdout


def api(path: str, *, method: str | None = None, payload: object | None = None):
    args = ["api"]
    if method:
        args += ["--method", method]
    args += [path]
    if payload is not None:
        args += ["--input", "-"]
    result = gh(*args, payload=payload)
    return json.loads(result) if result.strip() else {}


def issue(n: int):
    return api(f"repos/{REPO}/issues/{n}")


def label_names(data: dict) -> set[str]:
    return {x["name"] for x in data.get("labels", [])}


def field_values(n: int) -> dict[str, str]:
    result = api(f"repos/{REPO}/issues/{n}/issue-field-values")
    if not isinstance(result, list):
        raise RuntimeError(f"{n}: unreadable Issue Fields")
    out = {}
    for item in result:
        name = item.get("issue_field_name")
        if not name or name in out:
            raise RuntimeError(f"{n}: ambiguous Issue Field {name}")
        out[name] = (item.get("single_select_option") or {}).get("name") or item.get("value")
    return out


def project_items() -> dict[str, dict]:
    raw = json.loads(gh("project", "item-list", PROJECT_NUMBER, "--owner", ORG,
                        "--limit", "3000", "--format", "json"))
    rows = raw.get("items") or []
    if len(rows) != raw.get("totalCount") or len(rows) < 9:
        raise RuntimeError(f"incomplete Project #2 snapshot: {len(rows)}/{raw.get('totalCount')}")
    indexed = {}
    for row in rows:
        link = str((row.get("content") or {}).get("url") or "")
        if link in indexed:
            raise RuntimeError(f"duplicate Project URL {link!r}")
        indexed[link] = row
    return indexed


def project_fields():
    raw = json.loads(gh("project", "field-list", PROJECT_NUMBER, "--owner", ORG,
                        "--limit", "100", "--format", "json"))
    fields = {row.get("name"): row for row in raw.get("fields", [])}
    if fields.get("Status", {}).get("id") != STATUS_FIELD["field_id"]:
        raise RuntimeError("Project Status binding drift")
    cls = fields.get("Queue Class") or {}
    opts = {v.get("name"): v.get("id") for v in cls.get("options", [])}
    if cls.get("id") != "PVTSSF_lADOB9Ao_c4BlwurzhlJkjI" or not opts.get("Editorial"):
        raise RuntimeError("Queue Class field/Editorial option not live or unverified")
    return cls["id"], opts["Editorial"]


def current_class(item: dict):
    return item.get("queueClass", item.get("Queue Class"))


def project_edit(item: dict, field_id: str, option_id: str):
    gh("project", "item-edit", "--id", item["id"], "--project-id", PROJECT_ID,
       "--field-id", field_id, "--single-select-option-id", option_id)


def update_state(n: int, wanted: str):
    api(f"repos/{REPO}/issues/{n}/issue-field-values", method="POST",
        payload={"issue_field_values": [{"field_id": STATE_FIELD, "value": wanted}]})


def set_label(n: int, old: str, new: str):
    # The RETURNED label does not yet exist in the Programme repository.
    # Materialize only this bounded discovery label before removing AVAILABLE.
    if (old, new) not in {
        ("gcl-state:available", "gcl-state:returned"),
        ("gcl-state:blocked", "gcl-state:available"),
    }:
        raise RuntimeError("unapproved typography state-label transition")
    rec = issue(n)
    labels = label_names(rec)
    if new not in labels:
        catalog = json.loads(gh("label", "list", "--repo", REPO,
                                "--json", "name", "--limit", "1000"))
        if not isinstance(catalog, list):
            raise RuntimeError("unreadable repository label catalog")
        if new not in {row["name"] for row in catalog}:
            if new != "gcl-state:returned":
                raise RuntimeError("preexisting AVAILABLE label was unexpectedly deleted")
            gh("label", "create", new, "--repo", REPO,
               "--color", "cfd8dc",
               "--description", "Returned editorial evidence awaiting independent verification")
        gh("issue", "edit", str(n), "--repo", REPO, "--add-label", new)
    if old in labels:
        gh("issue", "edit", str(n), "--repo", REPO, "--remove-label", old)


def preflight():
    workflow = "grandchallenge/MATH-PROGRAMME/.github/workflows/erdos-catalogue-queue-projection.yml@refs/heads/main"
    clerk = (os.environ.get("GITHUB_ACTIONS") == "true" and
             os.environ.get("GITHUB_REPOSITORY") == REPO and
             os.environ.get("GITHUB_REF") == "refs/heads/main" and
             os.environ.get("GITHUB_WORKFLOW_REF") == workflow)
    if clerk:
        # Protected release-trust workflow minted a repository-limited Council Clerk
        # installation token with organization Projects write and issues write.
        # Verify the token is scoped to precisely this Programme repository.
        installation = api("installation/repositories?per_page=100")
        allowed = {r.get("full_name") for r in installation.get("repositories", [])}
        if allowed != {REPO} or installation.get("total_count") != 1:
            raise RuntimeError("Council Clerk installation token repository scope drift")
    else:
        actor = api("user").get("login")
        if actor not in {"fyremael", "jimsteeg"}:
            raise RuntimeError("unauthorized Projects queue operator")
    actual_main = api("repos/grandchallenge/MATHSOLVE/git/ref/heads/main")["object"]["sha"]
    local_head = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True,
                                text=True, check=True).stdout.strip()
    if actual_main != local_head:
        raise RuntimeError("run protected current MATHSOLVE main, not an unmerged candidate")
    modes = json.loads((Path(__file__).resolve().parents[1] /
                        ".well-known/gcl-worker-queue.json").read_text())["repository_pickup_modes"]
    if modes.get(REPO) != "direct_editorial":
        raise RuntimeError("protected pickup registration missing")
    for n, pr in PRS.items():
        rec = issue(n)
        labs = label_names(rec)
        if rec.get("state") != "open" or "gcl-pickup:direct-editorial" not in labs:
            raise RuntimeError(f"{n}: pickup/issue drift")
        expected_role = "source-audit" if n == 1262 else "constructive"
        if f"gcl-role:{expected_role}" not in labs:
            raise RuntimeError(f"{n}: protected role drift")
        if classify(REPO, rec["title"], labs, modes=modes)[0] != "Editorial":
            raise RuntimeError(f"{n}: must be Editorial")
        comments = api(f"repos/{REPO}/issues/{n}/comments?per_page=100")
        valid = [r for r in comments if r.get("body", "").startswith("RESULT/1\n")
                 and f"ASSIGNMENT_ID: MP-MATH-TYPO-ED{n-1255:02d}" in r["body"]
                 and f"/pull/{pr}" in r["body"]
                 and "DISPOSITION: PARTIAL" in r["body"] and r.get("user", {}).get("login")]
        if len(valid) != 1:
            raise RuntimeError(f"{n}: not exactly one authenticated matching RESULT/1")
        merged = api(f"repos/{REPO}/pulls/{pr}")
        if not merged.get("merged_at") or not merged.get("merge_commit_sha"):
            raise RuntimeError(f"{n}: PR #{pr} not protected merged")
    ed08 = issue(SUCCESSOR)
    labs = label_names(ed08)
    if ed08.get("state") != "open" or not {"gcl-job","gcl-role:verify",
                 "gcl-pickup:direct-editorial"}.issubset(labs):
        raise RuntimeError("ED08 role/route drift")
    if classify(REPO, ed08["title"], labs, modes=modes)[0] != "Editorial":
        raise RuntimeError("ED08 semantic queue must be Editorial")
    if any(r.get("body", "").startswith("RESULT/1") for r in
           api(f"repos/{REPO}/issues/{SUCCESSOR}/comments?per_page=100")):
        raise RuntimeError("ED08 already has a worker result; no reactivation")
    for n in [*PRS, SUCCESSOR, ARCHIVE]:
        fields = field_values(n)
        if fields.get("GCL Campaign") != "MATH-TYPOGRAPHY-REMEDIATION-001":
            raise RuntimeError(f"{n}: campaign field missing/drifted")
        state = fields.get("GCL State")
        allowed = {EXPECTED[n], "AVAILABLE"} if n in PRS else (
            {"BLOCKED", "AVAILABLE"} if n == SUCCESSOR else {"BLOCKED"})
        if state not in allowed:
            raise RuntimeError(f"{n}: unexpected GCL State {state}")
    return actual_main


def verify(n: int, item: dict, expected: str):
    fields = field_values(n)
    labels = label_names(issue(n))
    if fields.get("GCL State") != expected:
        raise RuntimeError(f"{n}: Issue Field readback failed")
    if f"gcl-state:{expected.lower()}" not in labels:
        raise RuntimeError(f"{n}: state label readback failed")
    if "gcl-state:available" in labels and expected != "AVAILABLE":
        raise RuntimeError(f"{n}: stale AVAILABLE label")
    if current_class(item) != "Editorial":
        raise RuntimeError(f"{n}: Queue Class not Editorial")
    status = "Todo" if expected == "AVAILABLE" else "Done"
    if item.get("status") != status:
        raise RuntimeError(f"{n}: Project Status {item.get('status')}, expected {status}")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--apply", action="store_true")
    args = p.parse_args()
    main_sha = preflight()
    initial = project_items()
    cls_id, cls_option = project_fields()
    for n in [*PRS, SUCCESSOR, ARCHIVE]:
        if f"https://github.com/{REPO}/issues/{n}" not in initial:
            raise RuntimeError(f"{n}: missing from canonical Project #2")
    print(json.dumps({"mode": "apply" if args.apply else "dry-run",
                      "operator_project": PROJECT_ID, "protected_solve_head": main_sha,
                      "transition": EXPECTED, "archive_remains_blocked": ARCHIVE},
                     sort_keys=True))
    if not args.apply:
        return
    # First remove seven stale pickup slots. ED08 remains blocked throughout.
    for n in PRS:
        item = initial[f"https://github.com/{REPO}/issues/{n}"]
        project_edit(item, cls_id, cls_option)
        set_label(n, "gcl-state:available", "gcl-state:returned")
        update_state(n, "RETURNED")
        project_edit(item, STATUS_FIELD["field_id"], STATUS_FIELD["options"]["Done"])
    interim = project_items()
    for n in PRS:
        verify(n, interim[f"https://github.com/{REPO}/issues/{n}"], "RETURNED")
    # ED08 is the ONLY newly discoverable task; all predecessor receipts remain PARTIAL.
    item = interim[f"https://github.com/{REPO}/issues/{SUCCESSOR}"]
    project_edit(item, cls_id, cls_option)
    project_edit(item, STATUS_FIELD["field_id"], STATUS_FIELD["options"]["Todo"])
    update_state(SUCCESSOR, "AVAILABLE")
    # Do not label it AVAILABLE until the field and Project presentation read back.
    candidate = project_items()[f"https://github.com/{REPO}/issues/{SUCCESSOR}"]
    if field_values(SUCCESSOR).get("GCL State") != "AVAILABLE" or (
        candidate.get("status") != "Todo" or current_class(candidate) != "Editorial"):
        update_state(SUCCESSOR, "BLOCKED")
        raise RuntimeError("ED08 pre-exposure readback failed; reverted to BLOCKED field")
    set_label(SUCCESSOR, "gcl-state:blocked", "gcl-state:available")
    final = project_items()
    for n, state in EXPECTED.items():
        verify(n, final[f"https://github.com/{REPO}/issues/{n}"], state)
    if field_values(ARCHIVE).get("GCL State") != "BLOCKED":
        raise RuntimeError("ED09 no longer blocked")
    if api("repos/grandchallenge/MATHSOLVE/git/ref/heads/main")["object"]["sha"] != main_sha:
        raise RuntimeError("protected controller moved during execution; repeat readback")
    print(json.dumps({"receipt": "TYPO-ED08-ACTIVATION-READBACK/1",
                      "project": PROJECT_ID, "protected_controller": main_sha,
                      "returned": list(PRS), "available": SUCCESSOR,
                      "still_blocked": ARCHIVE, "complete": True}, sort_keys=True))


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, KeyError, RuntimeError, subprocess.TimeoutExpired,
            subprocess.CalledProcessError, json.JSONDecodeError) as exc:
        raise SystemExit(f"QUEUE_RECONCILIATION_BLOCKED: {exc}")
