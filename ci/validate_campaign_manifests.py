#!/usr/bin/env python3
"""Compatibility entry point for reviewed campaign and MATHCERT handoff validation."""
from __future__ import annotations

from pathlib import Path
import sys

CI_DIR = Path(__file__).resolve().parent
if str(CI_DIR) not in sys.path:
    sys.path.insert(0, str(CI_DIR))

from validate_campaign_manifests_reviewed import (  # noqa: E402
    ADJUDICATED_STATES,
    HANDOFF_DIR,
    INTAKE_STATES,
    MANIFEST_DIR,
    POSITIVE_STATES,
    artifact_errors,
    campaign_manifest_errors,
    expected_campaigns,
    git_blob_sha1,
    handoff_packet_errors,
    load_json,
    main,
    manifest_errors,
    mathcert_handoff_errors,
    provider_gate_errors,
    schema_errors,
    walk_work_packages,
)

__all__ = [
    "ADJUDICATED_STATES",
    "HANDOFF_DIR",
    "INTAKE_STATES",
    "MANIFEST_DIR",
    "POSITIVE_STATES",
    "artifact_errors",
    "campaign_manifest_errors",
    "expected_campaigns",
    "git_blob_sha1",
    "handoff_packet_errors",
    "load_json",
    "main",
    "manifest_errors",
    "mathcert_handoff_errors",
    "provider_gate_errors",
    "schema_errors",
    "walk_work_packages",
]

if __name__ == "__main__":
    raise SystemExit(main())
