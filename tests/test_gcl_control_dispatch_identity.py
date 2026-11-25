"""CONTROL-WRITE-001 correlation extension: no worker reservation semantics change."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github/workflows/gcl-worker-queue.yml"
IDENTITY = re.compile(r"CW-[A-Z0-9][A-Z0-9-]{7,63}")


def test_manual_dispatch_correlation_is_optional_not_a_new_workflow():
    source = WORKFLOW.read_text()
    assert source.startswith("name: GCL worker queue reservation controller\n")
    assert '    - cron: "17 * * * *"' in source
    assert "    types: [created]" in source
    assert "  workflow_dispatch:\n    inputs:\n      gcl_control_operation_id:" in source
    assert "        required: false" in source
    assert "format('GCL Control Plane {0}', inputs.gcl_control_operation_id)" in source
    assert "run-name:" in source


def test_receipt_provenance_is_pre_reconcile_and_bounded():
    source = WORKFLOW.read_text()
    command, reap = source.split("\n  reap:\n", 1)
    assert "gcl_control_operation_id" not in command
    assert "github.event.comment.body == '/claim'" in command
    assert "github.event.comment.body == '/release'" in command
    receipt = reap.index("GCL_CONTROL_DISPATCH_RECEIPT/1")
    check = reap.index('re.fullmatch(r"CW-[A-Z0-9][A-Z0-9-]{7,63}", operation)')
    reconcile = reap.index("Reconcile reservations and Issue Fields")
    assert check < receipt < reconcile
    assert "GCL_CONTROL_OPERATION_ID: ${{ inputs.gcl_control_operation_id }}" in reap
    assert '"run_id": os.environ["GITHUB_RUN_ID"]' in reap
    assert '"head_sha": os.environ["GITHUB_SHA"]' in reap
    assert '"event": os.environ["GITHUB_EVENT_NAME"]' in reap
    assert '"mathematical_effect": False' in reap
    assert '"certification_effect": False' in reap


def test_correlation_input_is_not_shell_interpolation_or_new_permission():
    source = WORKFLOW.read_text()
    # Inputs flow through a typed environment variable; never interpolate
    # untrusted text directly into shell commands.
    assert "GCL_CONTROL_OPERATION_ID: ${{ inputs.gcl_control_operation_id }}" in source
    assert "echo ${{ inputs.gcl_control_operation_id }}" not in source
    assert "GCL_CONTROL_OPERATION_ID" in source
    assert "  contents: read\n  issues: write\n" in source
    assert "permissions: write-all" not in source
    assert "pull-requests: write" not in source
    for good in ("CW-EXECUTION-WP02-0001", "CW-GCL-CANARY-0042"):
        assert IDENTITY.fullmatch(good)
    for bad in ("", "CW-", "CW-lowercase-abc", "CW-X;echo hacked", "/claim", "CW-AB", "CONTROL id"):
        assert IDENTITY.fullmatch(bad) is None
