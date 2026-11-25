#!/usr/bin/env python3
"""Fail-closed GCL queue classification and *admission-budget* checks.

Queue CLASS is semantic; pickup MODE is operational. In particular, Erdős
source-audit issues in MATH-PROGRAMME remain direct-editorial pickup but are
mathematics research preparation, never editorial manuscript jobs.

This module does NOT query or modify Project #2. The audit consumes a complete
authenticated Project snapshot and refuses incomplete/ambiguous data. Budget
checks are for available-job admission only; they do not assert worker-runtime
concurrency where no protected direct-editorial reservation exists.
"""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import re
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
BOOTSTRAP = ROOT / ".well-known/gcl-worker-queue.json"
PROJECT_NUMBER = 2
QUEUE_CLASSES = ("Editorial", "Mathematics")
DIRECT = "gcl-pickup:direct-editorial"
SOURCE_ROLE = "gcl-role:source-audit"
ERDOS_TITLE = re.compile(r"^(?:\[GCL-ERDOS\]\s+)?ERDOS-CATALOGUE-\d{4}-S\d{2}\b")
ERDOS_CRITIC_TITLE = re.compile(
    r"^ERDOS (\d{1,4}) — critical source and lemma review of ERDOS-(\d{3})-"
)



R41_TRACKS = {
    "ERDOS-041-R41-A — fourth-order overlap propagation or counterexample": ("gcl-role:constructive", 2790),
    "ERDOS-041-R41-B — prove or refute a scale-owned capacity invariant": ("gcl-role:constructive", 2791),
    "ERDOS-041-R41-C — independent Pauli-level proof audit and falsification": ("gcl-role:verify", 2792),
    "ERDOS-041-R41-D — spectral moment-flow renormalization experiment": ("gcl-role:constructive", 2793),
}


class QueueIntegrityError(ValueError):
    pass


def pickup_modes() -> dict[str, str]:
    data = json.loads(BOOTSTRAP.read_text(encoding="utf-8"))
    return data["repository_pickup_modes"]


def classify(repository: str, title: str, labels: Iterable[str],
             *, modes: dict[str, str] | None = None) -> tuple[str, str]:
    """Return (semantic queue class, pickup mode); fail closed on conflicts."""
    modes = pickup_modes() if modes is None else modes
    if repository not in modes:
        raise QueueIntegrityError(f"unknown repository: {repository}")
    mode = modes[repository]
    ls = set(labels)
    pickup_labels = {s for s in ls if s.startswith("gcl-pickup:")}
    if mode == "reservation_controlled":
        # SOURCE_ROLE names mathematical research/source work, not a pickup route.
        # Legitimate Solve dispatches such as #843 and #1033 carry this role.
        # Preserve their protected reservation and RESULT/1 semantics.
        if pickup_labels:
            raise QueueIntegrityError("reservation issue contains direct pickup label")
        return "Mathematics", mode
    if mode != "direct_editorial" or pickup_labels != {DIRECT}:
        raise QueueIntegrityError("invalid direct-editorial pickup routing")

    if repository == "grandchallenge/MATH-PROGRAMME" and title.startswith("ERDOS-041-R41-"):
        bound = R41_TRACKS.get(title)
        if not bound or bound[0] not in ls or "gcl-collab:cooperative" not in ls:
            raise QueueIntegrityError("invalid Erdős #41 research specialist route")
        return "Mathematics", mode
    erdos = bool(ERDOS_TITLE.search(title))
    role = SOURCE_ROLE in ls
    # Editorial source-defect inventories have a SOURCE_AUDIT process role;
    # do not mistake either for Erdős mathematical research.
    if repository == "grandchallenge/MATH-PROGRAMME" and role and title.startswith(
        ("MP-MATH-TYPO-ED07 — ", "MP-MATH-TYPO-ED09 — ")
    ):
        return "Editorial", mode
    # A bounded Erdős mathematics critical-source docket can also use direct
    # issue pickup, unlike reservation-controlled Solve. Here we match a
    # tightly concordant subject-title grammar; the live Programme Project
    # reconciler additionally requires protected 24-cohort issue ID binding.
    critic = ERDOS_CRITIC_TITLE.match(title)
    if repository == "grandchallenge/MATH-PROGRAMME" and role and critic:
        if int(critic.group(1)) != int(critic.group(2)):
            raise QueueIntegrityError("Erdős critic problem/title identity mismatch")
        return "Mathematics", mode
    if repository == "grandchallenge/MATH-PROGRAMME" and (erdos or role):
        if not (erdos and role):
            raise QueueIntegrityError("ambiguous Erdős source-audit identity")
        return "Mathematics", mode
    if role:
        raise QueueIntegrityError("unclassified source-audit outside Erdős catalogue")
    return "Editorial", mode


def validate_snapshot(snapshot: dict, *, require_views: bool = False) -> dict:
    """Check exact row identity and every classification; no partial samples.

    Input: {project_number, complete, rows:[{repository, issue_number, title,
    labels, queue_class, issue_state, gcl_state, project_item_id}], views: ...}.
    The caller must generate complete=True only after paginating every item
    through the authenticated Project API and comparing total_count.
    """
    if snapshot.get("project_number") != PROJECT_NUMBER or snapshot.get("complete") is not True:
        raise QueueIntegrityError("Project identity or full-pagination proof missing")
    rows = snapshot.get("rows")
    expected_total = snapshot.get("total_count")
    if not isinstance(rows, list) or not isinstance(expected_total, int):
        raise QueueIntegrityError("missing rows or Project total_count")
    if len(rows) != expected_total:
        raise QueueIntegrityError(f"partial Project snapshot: {len(rows)}/{expected_total}")
    identities: set[tuple[str, int]] = set()
    project_ids: set[str] = set()
    counts: Counter[str] = Counter()
    for row in rows:
        if not isinstance(row, dict):
            raise QueueIntegrityError("invalid project item")
        repo = row.get("repository")
        n = row.get("issue_number")
        item_id = row.get("project_item_id")
        if not isinstance(repo, str) or not isinstance(n, int) or n < 1:
            raise QueueIntegrityError("missing repository or issue identity")
        if not isinstance(item_id, str) or not item_id:
            raise QueueIntegrityError(f"{repo}#{n}: missing Project item identity")
        key = (repo, n)
        if key in identities or item_id in project_ids:
            raise QueueIntegrityError(f"duplicate Project item {repo}#{n}")
        identities.add(key)
        project_ids.add(item_id)
        labels = row.get("labels")
        title = row.get("title")
        if not isinstance(labels, list) or not all(isinstance(s, str) for s in labels) or not isinstance(title, str):
            raise QueueIntegrityError(f"{repo}#{n}: missing title or labels")
        if repo == "grandchallenge/MATH-PROGRAMME" and title.startswith("ERDOS-041-R41-"):
            bound = R41_TRACKS.get(title)
            if not bound or bound[1] != n:
                raise QueueIntegrityError(f"{repo}#{n}: ERDOS-041 identity drift")
        cls, mode = classify(repo, title, labels)
        if row.get("queue_class") != cls:
            raise QueueIntegrityError(f"{repo}#{n}: Queue Class {row.get('queue_class')!r}, expected {cls!r}")
        if row.get("pickup_mode") not in (None, mode):
            raise QueueIntegrityError(f"{repo}#{n}: pickup-mode mismatch")
        if row.get("gcl_state") not in {"AVAILABLE", "RESERVED", "RETURNED", "BLOCKED", "CLOSED"}:
            raise QueueIntegrityError(f"{repo}#{n}: unrecognized/missing GCL State")
        counts[cls] += 1
    if require_views:
        views = snapshot.get("views") or {}
        for cls, name in (("Editorial", "EDITORIAL"), ("Mathematics", "MATHEMATICS")):
            row = views.get(name)
            if not isinstance(row, dict) or not row.get("id") or row.get("queue_class") != cls:
                raise QueueIntegrityError(f"saved {name} Project view readback missing")
        if "AVAILABLE" not in views or not views["AVAILABLE"].get("id"):
            raise QueueIntegrityError("global AVAILABLE Project view missing")
    return {"total_count":len(rows), "classes":dict(counts), "views_verified":require_views}


def check_admission(queue_class: str, available_counts: dict[str, int],
                    limits: dict[str, int]) -> dict:
    """Budget check for adding ONE AVAILABLE item; no shared pool.

    Requires an explicit protected limit for EACH class and actual current
    AVAILABLE counts from a complete consistent Project snapshot. This is
    admission control, not concurrency accounting for independently launched
    direct-editorial workers.
    """
    if set(limits) != set(QUEUE_CLASSES) or set(available_counts) != set(QUEUE_CLASSES):
        raise QueueIntegrityError("class budgets/counts incomplete; no admission authorized")
    if queue_class not in QUEUE_CLASSES:
        raise QueueIntegrityError("unknown queue class")
    if any(not isinstance(v, int) or isinstance(v, bool) or v < 0
           for v in list(limits.values()) + list(available_counts.values())):
        raise QueueIntegrityError("invalid class budget/count")
    remaining = limits[queue_class] - available_counts[queue_class]
    return {"queue_class":queue_class, "admit":remaining > 0, "remaining_before":remaining,
            "other_class_unchanged":True}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--snapshot", type=Path, required=True)
    parser.add_argument("--require-views", action="store_true")
    args = parser.parse_args()
    try:
        report = validate_snapshot(json.loads(args.snapshot.read_text(encoding="utf-8")),
                                   require_views=args.require_views)
    except (QueueIntegrityError, KeyError, TypeError, json.JSONDecodeError) as exc:
        print("BLOCKED: " + str(exc))
        return 1
    print("PASS " + json.dumps(report, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
