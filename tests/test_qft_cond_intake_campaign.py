#!/usr/bin/env python3
"""Positive QFT-COND-005 intake binding and hostile unknown-campaign regression."""
from __future__ import annotations

import hashlib
import json
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from ci.validate_queue_intake_bindings import validate


def write_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def exercise(campaign: str) -> list[str]:
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        did = "QFT-COND-005-EXT-015A-IA-001"
        dp = "contributions/QFT-COND-005/EXT-015/dispatches/" + did + ".json"
        tp = "handoffs/QFT-COND-005/launch/" + did + ".md"
        task = root / tp
        task.parent.mkdir(parents=True, exist_ok=True)
        task.write_text("GCL-CONTRIBUTION-DISPATCH/1\n", encoding="utf-8")
        sha = hashlib.sha256(task.read_bytes()).hexdigest()
        commit = "1" * 40
        write_json(root / ".gcl/worker_queue/JOBS.json", {
            "jobs": [{"dispatch_id": did, "dispatch_path": dp, "issue_number": 1081}]
        })
        write_json(root / dp, {
            "dispatch_id": did, "campaign": campaign,
            "github_issue_number": 1081,
            "dispatch_status": "READY_FOR_GITHUB_COMMENT", "lease_state": "ACTIVE",
            "canonical_mutation_authorized": False, "certification_authorized": False,
            "task_path": tp, "task_commit": commit
        })
        write_json(root / ".gcl/worker_queue/INTAKE_BINDINGS.json", {
            "record_type": "GCL_QUEUE_INTAKE_BINDINGS", "schema_version": "1.0.0",
            "authority_effect": {
                "queue_operation_only": True, "mathematical": False,
                "certification": False
            },
            "bindings": [{
                "dispatch_id": did, "dispatch_path": dp, "github_issue_number": 1081,
                "issue_body_sha256": "a" * 64, "task_path": tp,
                "task_commit": commit, "task_sha256": sha,
                "allowed_external_sources": ["PRIMARY_SOURCES_REQUIRED"],
                "allowed_dispositions": ["EXACT_BLOCKER"]
            }]
        })
        return validate(root)


def test_qft_dispatch_positive_and_other_campaign_rejected() -> None:
    assert exercise("QFT-COND-005") == []
    assert any("unregistered campaign" in e for e in exercise("UNREGISTERED-CAMPAIGN"))


if __name__ == "__main__":
    test_qft_dispatch_positive_and_other_campaign_rejected()
    print("QFT-COND-005 queue intake allowlist: positive and hostile PASS")
