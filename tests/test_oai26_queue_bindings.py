"""Positive and hostile checks for the new source-locked OAI queue campaign."""
from __future__ import annotations
import hashlib
import json
import tempfile
from pathlib import Path
from ci.validate_queue_intake_bindings import validate
from ci.ns_ci_github_contribution_intake import profile_for_dispatch

DID = "OAI26-WP00-IA-001"
DP = f"contributions/OAI-MATH-2026/TRIAGE_001/dispatches/{DID}.json"
TP = f"handoffs/OAI-MATH-2026/launch/{DID}.md"

def save(root, name, value):
    p = root / name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(value) + "\n", encoding="utf-8")

def stage(root):
    task = root / TP
    task.parent.mkdir(parents=True, exist_ok=True)
    task.write_text("GCL-CONTRIBUTION-DISPATCH/1\n")
    digest = hashlib.sha256(task.read_bytes()).hexdigest()
    save(root, ".gcl/worker_queue/JOBS.json", {"jobs":[{"dispatch_id":DID,"issue_number":1098,
        "self_claimable":True,"dispatch_path":DP}]})
    save(root, DP, {"dispatch_id":DID,"campaign":"GCL-OAI-MATH-2026",
        "github_issue_number":1098,"dispatch_status":"READY_FOR_GITHUB_COMMENT",
        "lease_state":"ACTIVE","canonical_mutation_authorized":False,
        "certification_authorized":False,"task_path":TP,"task_commit":"a"*40})
    save(root, ".gcl/worker_queue/INTAKE_BINDINGS.json",{
        "record_type":"GCL_QUEUE_INTAKE_BINDINGS","schema_version":"1.0.0",
        "authority_effect":{"queue_operation_only":True,"mathematical":False,"certification":False},
        "bindings":[{"dispatch_id":DID,"dispatch_path":DP,"github_issue_number":1098,
            "issue_body_sha256":"b"*64,"task_path":TP,"task_commit":"a"*40,
            "task_sha256":digest,"allowed_external_sources":["PRIMARY_SOURCES_REQUIRED"],
            "allowed_dispositions":["SOURCE_INTERFACE_FOUND","EXACT_BLOCKER"]}]})

def test_positive_and_unknown_campaign():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d); stage(root)
        assert validate(root) == []
        assert profile_for_dispatch(DID, root).campaign == "GCL-OAI-MATH-2026"
        obj=json.loads((root/DP).read_text());obj["campaign"]="UNKNOWN"
        save(root, DP, obj)
        assert any("unregistered campaign" in x for x in validate(root))

def test_hostile_task_digest():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d); stage(root)
        (root/TP).write_text("tampered task\n")
        assert any("task bytes no longer match" in x for x in validate(root))

def test_hostile_dispatch_issue_mismatch():
    with tempfile.TemporaryDirectory() as d:
        root=Path(d); stage(root)
        obj=json.loads((root/DP).read_text());obj["github_issue_number"]=1100
        save(root,DP,obj)
        assert any("dispatch and queue registry disagree" in x for x in validate(root))
