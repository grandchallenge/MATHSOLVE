#!/usr/bin/env python3
"""Fail-closed audit of new-generation queue intake bindings versus protected jobs.

Legacy bootstrap-pinned dispatches retain their existing intake profiles.
All protected queue dispatches lacking legacy bootstrap fields require one
explicit, immutable dispatch/issue/task binding in this manifest.
"""
from __future__ import annotations
import hashlib
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
JOBS=ROOT/".gcl/worker_queue/JOBS.json"
BINDINGS=ROOT/".gcl/worker_queue/INTAKE_BINDINGS.json"

def validate(root:Path=ROOT)->list[str]:
    errors:list[str]=[]
    jobs=json.loads((root/".gcl/worker_queue/JOBS.json").read_text(encoding="utf-8"))["jobs"]
    document=json.loads((root/".gcl/worker_queue/INTAKE_BINDINGS.json").read_text(encoding="utf-8"))
    if document.get("record_type")!="GCL_QUEUE_INTAKE_BINDINGS" or document.get("schema_version")!="1.0.0":
        errors.append("new-generation intake binding schema drift")
    auth=document.get("authority_effect") or {}
    if auth != {"queue_operation_only":True,"mathematical":False,"certification":False}:
        errors.append("intake manifest authority boundary drift")
    entries=document.get("bindings")
    if not isinstance(entries,list):
        return ["intake binding entries must be a list"]
    by_id={}
    for binding in entries:
        did=binding.get("dispatch_id")
        if not isinstance(did,str) or did in by_id:
            errors.append(f"duplicate or malformed intake binding {did!r}")
        else: by_id[did]=binding

    newer=set()
    for job in jobs:
        did=job["dispatch_id"]
        rel=Path(job["dispatch_path"])
        if rel.is_absolute() or ".." in rel.parts or not (root/rel).is_file():
            errors.append(f"{did}: protected dispatch path missing or unsafe")
            continue
        dispatch=json.loads((root/rel).read_text(encoding="utf-8"))
        if "bootstrap_sha256" in dispatch:
            if did in by_id:errors.append(f"{did}: legacy dispatch shadowed by new binding")
            continue
        newer.add(did)
        b=by_id.get(did)
        if not b:
            errors.append(f"{did}: queue job lacks intake binding")
            continue
        if b.get("dispatch_path")!=job["dispatch_path"] or b.get("github_issue_number")!=job["issue_number"]:
            errors.append(f"{did}: queue registry and intake binding disagree")
        if dispatch.get("dispatch_id")!=did or dispatch.get("github_issue_number")!=job["issue_number"]:
            errors.append(f"{did}: dispatch and queue registry disagree")
        if dispatch.get("campaign") not in {"RH-001","ERDOS-OPEN"}:
            errors.append(f"{did}: unregistered campaign")
        if dispatch.get("dispatch_status")!="READY_FOR_GITHUB_COMMENT" or dispatch.get("lease_state")!="ACTIVE":
            errors.append(f"{did}: dispatch not executable")
        if dispatch.get("canonical_mutation_authorized") is not False or dispatch.get("certification_authorized") is not False:
            errors.append(f"{did}: authority elevated")
        if b.get("task_path") != dispatch.get("task_path") or b.get("task_commit") != dispatch.get("task_commit"):
            errors.append(f"{did}: immutable task source mismatch")
        task_rel=Path(str(b.get("task_path") or ""))
        if task_rel.is_absolute() or ".." in task_rel.parts or not (root/task_rel).is_file():
            errors.append(f"{did}: immutable task path missing or unsafe")
        else:
            blob=(root/task_rel).read_bytes().replace(b"\r\n",b"\n")
            if hashlib.sha256(blob).hexdigest()!=b.get("task_sha256"):
                errors.append(f"{did}: task bytes no longer match immutable digest")
        for key in ("issue_body_sha256","task_sha256"):
            if not re.fullmatch("[0-9a-f]{64}",str(b.get(key) or "")):
                errors.append(f"{did}: invalid {key}")
        if not re.fullmatch("[0-9a-f]{40}",str(b.get("task_commit") or "")):
            errors.append(f"{did}: invalid task commit SHA")
        for key in ("allowed_external_sources","allowed_dispositions"):
            values=b.get(key)
            if not isinstance(values,list) or not values or len(values)!=len(set(values)):
                errors.append(f"{did}: malformed {key}")
        if set(b.get("allowed_external_sources") or [])-{"PROTECTED_PACKET_ONLY","PRIMARY_SOURCES_REQUIRED"}:
            errors.append(f"{did}: unsafe external-source policy")
        if set(b.get("allowed_dispositions") or [])-{
            "PROVED_REDUCTION","EXACT_REDUCTION","FINITE_CERTIFICATE","SOURCE_INTERFACE_FOUND",
            "COUNTEREXAMPLE","EXACT_BLOCKER","NO_MATERIAL_DELTA"
        }:
            errors.append(f"{did}: unknown disposition")
    for did in by_id:
        if did not in newer:errors.append(f"{did}: stale or unregistered binding")
    return errors

if __name__=="__main__":
    errors=validate()
    for e in errors:print("FAIL:",e)
    if errors:raise SystemExit(1)
    print("PASS: all new-generation queue dispatches have exact intake bindings")
