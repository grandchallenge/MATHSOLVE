"""Constrained GitHub Projects operator. No arbitrary shell or local filesystem APIs."""
from __future__ import annotations
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import time
from collections import Counter
from datetime import datetime, timezone

ORG = "grandchallenge"
PROJECT_NO = 2
FIELD = "Queue Class"
CLASSES = ("Editorial", "Mathematics")
EDITORIAL_REPOS = {
    "grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS",
    "grandchallenge/COMPUTATIONAL-DIFFICULTY-ATLAS",
    "grandchallenge/MATH-PROGRAMME",
}
MATH_REPO = "grandchallenge/MATHSOLVE"
DIRECT = "gcl-pickup:direct-editorial"
SOURCE = "gcl-role:source-audit"
ERDOS = re.compile(r"^(?:\[GCL-ERDOS\]\s+)?ERDOS-CATALOGUE-\d{4}-S\d{2}\b")
CRITIC = re.compile(r"^ERDOS (\d{1,4}) — critical source and lemma review of ERDOS-(\d{3})-")

class Boundary(RuntimeError):
    """Named governance/integrity boundary; no mutation on failure."""


def classify(repo: str, title: str, labels: list[str]) -> tuple[str, str]:
    """Mirror the protected queue semantic classifier, conservatively."""
    ls = set(labels)
    pickup = {x for x in ls if x.startswith("gcl-pickup:")}
    if repo == MATH_REPO:
        # A mathematical source-audit role is valid on a Solve dispatch.
        # Roles describe the work; pickup labels control reservation routing.
        # Existing Erdős source-audit issues (#843, #1033, etc.) are
        # reservation-controlled and must not be rewritten or rejected.
        if pickup:
            raise Boundary("INVALID_MATHSOLVE_PICKUP_LABEL")
        return "Mathematics", "reservation_controlled"
    if repo not in EDITORIAL_REPOS:
        raise Boundary(f"UNKNOWN_JOB_REPOSITORY:{repo}")
    if pickup != {DIRECT}:
        raise Boundary(f"INVALID_DIRECT_PICKUP:{repo}")
    is_erdos = bool(ERDOS.search(title))
    is_source = SOURCE in ls
    if repo == "grandchallenge/MATH-PROGRAMME" and is_source and title.startswith(
        ("MP-MATH-TYPO-ED07 — ", "MP-MATH-TYPO-ED09 — ")
    ):
        return "Editorial", "direct_editorial"
    match = CRITIC.match(title)
    if repo == "grandchallenge/MATH-PROGRAMME" and is_source and match:
        if int(match.group(1)) != int(match.group(2)):
            raise Boundary("ERDOS_CRITIC_IDENTITY_MISMATCH")
        return "Mathematics", "direct_editorial"
    if repo == "grandchallenge/MATH-PROGRAMME" and (is_erdos or is_source):
        if not (is_erdos and is_source):
            raise Boundary("AMBIGUOUS_ERDOS_SOURCE_ROLE")
        return "Mathematics", "direct_editorial"
    if is_source:
        raise Boundary("UNCLASSIFIED_SOURCE_AUDIT")
    return "Editorial", "direct_editorial"


def _gh(args: list[str], *, retry: int = 4) -> str:
    if not args or args[0] not in ("api", "auth"):
        raise Boundary("COMMAND_NOT_ALLOWLISTED")
    for attempt in range(retry):
        try:
            p = subprocess.run(["gh", *args], capture_output=True, text=True,
                               timeout=90, check=False, env=os.environ.copy())
        except (OSError, subprocess.TimeoutExpired) as exc:
            raise Boundary(f"GH_EXECUTION_FAILED:{type(exc).__name__}") from exc
        if p.returncode == 0:
            return p.stdout
        stderr = p.stderr.strip()
        if not any(s in stderr.lower() for s in ("rate limit", "secondary rate", "timeout", "temporarily unavailable", "502", "503")) or attempt == retry - 1:
            raise Boundary("GITHUB_API_FAILED:" + stderr[:400])
        time.sleep(min(2 ** attempt * 3, 30))
    raise Boundary("GITHUB_RETRY_EXHAUSTED")


def _graphql(query: str, **variables: str | None) -> dict:
    args = ["api", "graphql", "-f", f"query={query}"]
    for k, v in variables.items():
        if v is not None:
            args += ["-f", f"{k}={v}"]
    data = json.loads(_gh(args))
    if data.get("errors"):
        raise Boundary("GRAPHQL_ERRORS:" + json.dumps(data["errors"])[:500])
    return data["data"]


def assert_identity() -> dict:
    user = json.loads(_gh(["api", "user"]))
    permitted = os.environ.get("GCL_COMMANDER_GITHUB_ACTOR", "fyremael")
    if user.get("login") != permitted:
        raise Boundary(f"WRONG_AUTHENTICATED_ACTOR:{user.get('login')}")
    return {"login": user["login"], "expected": permitted}

QUERY = '''query($cursor:String) {
 organization(login:"grandchallenge") {
  projectV2(number:2) {
   id
   items(first:100,after:$cursor) {
    totalCount
    pageInfo {hasNextPage endCursor}
    nodes {
     id
     content {
      ... on Issue {
       number title url
       repository {nameWithOwner}
       labels(first:100) {nodes {name} pageInfo {hasNextPage}}
      }
     }
     fieldValueByName(name:"Queue Class") {
      ... on ProjectV2ItemFieldSingleSelectValue {name}
     }
    }
   }
  }
 }
}'''
FIELDS = '''query {organization(login:"grandchallenge") {projectV2(number:2) {
 id fields(first:100) {nodes {... on ProjectV2SingleSelectField {
 id name options{id name}
 }}}
}}}'''
MUTATION = '''mutation($project:ID!,$item:ID!,$field:ID!,$option:String!) {
 updateProjectV2ItemFieldValue(input:{projectId:$project,itemId:$item,fieldId:$field,
 value:{singleSelectOptionId:$option}}) {projectV2Item{id}}
}'''


def fields() -> dict:
    project = _graphql(FIELDS)["organization"]["projectV2"]
    candidates = [f for f in project["fields"]["nodes"] if f and f.get("name") == FIELD]
    if len(candidates) != 1:
        raise Boundary("QUEUE_CLASS_FIELD_MISSING_OR_AMBIGUOUS")
    options = {o["name"]: o["id"] for o in candidates[0]["options"]}
    if not set(CLASSES) <= options.keys():
        raise Boundary("CLASS_OPTIONS_INCOMPLETE")
    return {"project_id": project["id"], "field_id": candidates[0]["id"], "options": options}


def inventory() -> dict:
    cursor = None
    seen: set[str] = set()
    rows = []
    total = None
    project_id = None
    while True:
        project = _graphql(QUERY, cursor=cursor)["organization"]["projectV2"]
        if not project:
            raise Boundary("PROJECT_NOT_FOUND")
        if project_id is not None and project_id != project["id"]:
            raise Boundary("PROJECT_ID_CHANGED")
        project_id = project["id"]
        page = project["items"]
        if total is None:
            total = page["totalCount"]
        elif total != page["totalCount"]:
            raise Boundary("CONCURRENT_PROJECT_MEMBERSHIP_CHANGE")
        for item in page["nodes"]:
            if item["id"] in seen:
                raise Boundary("DUPLICATE_PROJECT_ITEM")
            seen.add(item["id"])
            rows.append(item)
        if not page["pageInfo"]["hasNextPage"]:
            break
        new = page["pageInfo"]["endCursor"]
        if not new or new == cursor:
            raise Boundary("BROKEN_PAGINATION_CURSOR")
        cursor = new
    if len(rows) != total:
        raise Boundary(f"INCOMPLETE_PROJECT_SNAPSHOT:{len(rows)}/{total}")
    return {"project_id": project_id, "total_count": total, "items": rows}


def _targets(snapshot: dict) -> tuple[dict, list]:
    targets = {}
    changes = []
    issues = set()
    for item in snapshot["items"]:
        c = item.get("content")
        if not c or not c.get("repository"):
            # Draft entries and non-issues are out of GCL job classification scope.
            continue
        labels = c.get("labels")
        if labels is None or labels["pageInfo"]["hasNextPage"]:
            raise Boundary("ISSUE_LABELS_INCOMPLETE")
        names = [x["name"] for x in labels["nodes"]]
        if "gcl-job" not in names:
            continue
        identity = (c["repository"]["nameWithOwner"], c["number"])
        if identity in issues:
            raise Boundary("DUPLICATE_GCL_ISSUE")
        issues.add(identity)
        try:
            target, mode = classify(identity[0], c["title"], names)
        except Boundary as exc:
            # Identify the exact offending issue without exposing credentials
            # or performing any mutation; enables bounded operational repair.
            raise Boundary(f"{exc}: {identity[0]}#{identity[1]}") from exc
        current = (item.get("fieldValueByName") or {}).get("name")
        if current not in (None, "Editorial", "Mathematics"):
            raise Boundary("UNRECOGNIZED_EXISTING_CLASS")
        targets[item["id"]] = {"class": target, "pickup_mode": mode, "issue": f"{identity[0]}#{identity[1]}"}
        if current != target:
            changes.append({"item_id": item["id"], "issue": f"{identity[0]}#{identity[1]}",
                            "before": current, "after": target})
    return targets, changes


def plan() -> dict:
    assert_identity()
    f = fields()
    snap = inventory()
    if f["project_id"] != snap["project_id"]:
        raise Boundary("PROJECT_FIELD_IDENTITY_MISMATCH")
    targets, changes = _targets(snap)
    return {"project": f, "snapshot": snap, "targets": targets, "changes": changes,
            "counts": dict(Counter(t["class"] for t in targets.values()))}


def reconcile(*, apply: bool = False, expected_total: int | None = None) -> dict:
    """Entirely dry-run by default; apply requires explicit total-count assertion."""
    current = plan()
    snap = current["snapshot"]
    if expected_total is not None and snap["total_count"] != expected_total:
        raise Boundary("EXPECTED_PROJECT_TOTAL_MISMATCH")
    if apply and expected_total is None:
        raise Boundary("APPLY_REQUIRES_EXACT_TOTAL_COUNT")
    result = {"operation": "reconcile", "applied": False,
              "project_id": snap["project_id"], "total": snap["total_count"],
              "gcl_jobs": len(current["targets"]), "class_counts": current["counts"],
              "changes_needed": len(current["changes"]),
              "sample_changes": current["changes"][:30]}
    if not apply:
        return result
    for change in current["changes"]:
        result_id = _graphql(MUTATION, project=current["project"]["project_id"],
                             item=change["item_id"], field=current["project"]["field_id"],
                             option=current["project"]["options"][change["after"]])[
            "updateProjectV2ItemFieldValue"]["projectV2Item"]["id"]
        if result_id != change["item_id"]:
            raise Boundary("MUTATION_RETURNED_WRONG_ITEM")
    after = plan()
    if set(after["targets"]) != set(current["targets"]):
        raise Boundary("MEMBERSHIP_CHANGED_DURING_RECONCILIATION")
    if after["changes"]:
        raise Boundary("READBACK_CLASSIFICATION_INCOMPLETE")
    result.update({"applied": True, "readback_pass": True,
                   "changes_applied": len(current["changes"]),
                   "final_class_counts": after["counts"]})
    return result


def receipt(data: dict, *, base: Path | None = None) -> str:
    """Append a locally retained evidence receipt without user secrets."""
    root = base or Path.home() / ".local" / "state" / "gcl-commander" / "receipts"
    root.mkdir(parents=True, exist_ok=True, mode=0o700)
    record = {"timestamp_utc": datetime.now(timezone.utc).isoformat(), "data": data}
    serialized = json.dumps(record, sort_keys=True, indent=2) + "\n"
    sha = hashlib.sha256(serialized.encode()).hexdigest()
    path = root / f"{int(time.time())}-{sha[:12]}.json"
    path.write_text(serialized, encoding="utf-8")
    path.chmod(0o600)
    return str(path)
