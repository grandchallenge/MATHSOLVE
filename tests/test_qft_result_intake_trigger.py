#!/usr/bin/env python3
"""Fail-closed check that QFT worker RESULT/1 reaches issue-comment intake."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github/workflows/ns-ci-independent-contribution-intake.yml"

def test_qft_worker_title_routed() -> None:
    workflow = WORKFLOW.read_text(encoding="utf-8")
    assert "startsWith(github.event.issue.title, '[GCL-CONTRIB] QFT-COND-005 ')" in workflow
    assert "startsWith(github.event.comment.body, 'GCL-CONTRIBUTION-RESULT/1')" in workflow
    assert "github.event_name == 'workflow_dispatch'" in workflow
    assert "github.event.issue.pull_request" in workflow
    assert "--event" in workflow and "ci/ns_ci_github_contribution_intake.py" in workflow

if __name__ == "__main__":
    test_qft_worker_title_routed()
    print("QFT RESULT/1 intake title routing: PASS")
