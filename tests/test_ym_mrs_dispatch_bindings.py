from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "contributions/YM-001/YM_D003_MRS_R002/dispatches"


def test_ym_mrs_dispatch_bindings() -> None:
    expected = {
        "A": (716, "PRIMARY_SOURCES_ALLOWED"),
        "B": (717, "PRIMARY_SOURCES_ALLOWED"),
        "C": (718, "PROTECTED_PACKET_ONLY"),
    }
    for assignment, (issue_number, external_sources) in expected.items():
        dispatch_id = f"YM-D003-MRS-R002-WP-{assignment}-IA-001"
        path = BASE / f"{dispatch_id}.json"
        obj = json.loads(path.read_text(encoding="utf-8"))

        assert obj["schema_version"] == "1.0.0"
        assert obj["dispatch_id"] == dispatch_id
        assert obj["assignment"] == assignment
        assert obj["dispatch_status"] == "READY_FOR_GITHUB_COMMENT"
        assert obj["concurrency_mode"] == "independent_blind"
        assert obj["context_class"] == "ZERO_CONTEXT"
        assert obj["external_sources"] == external_sources
        assert obj["return_protocol"] == "GCL-CONTRIBUTION-RESULT/1"
        assert obj["canonical_mutation_authorized"] is False
        assert obj["github_issue_number"] == issue_number
        assert obj["github_issue_title"].startswith(
            f"[GCL-CONTRIB] YM-D003-MRS-R002 WP-{assignment} "
        )

        bootstrap = ROOT / obj["bootstrap_path"]
        raw = bootstrap.read_bytes()
        assert hashlib.sha256(raw).hexdigest() == obj["bootstrap_sha256"]
