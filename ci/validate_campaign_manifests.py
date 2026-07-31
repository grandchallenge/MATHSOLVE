#!/usr/bin/env python3
"""Compatibility entry point for campaign, handoff, and current Cert-state validation."""
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
    manifest_errors,
    mathcert_handoff_errors,
    schema_errors,
    walk_work_packages,
)
from validate_campaign_manifests_reviewed import main as reviewed_main  # noqa: E402
from validate_current_cert_routes import (  # noqa: E402
    REGISTRY_PATH as CURRENT_CERT_REGISTRY_PATH,
    SCHEMA_PATH as CURRENT_CERT_SCHEMA_PATH,
    current_cert_route_errors,
    current_route_state,
    provider_gate_errors,
)
from validate_formal_conjectures_expansion import validate as formal_conjectures_errors  # noqa: E402


def main() -> int:
    status = reviewed_main()
    if status:
        return status

    errors = current_cert_route_errors()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    errors = formal_conjectures_errors()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("Expanded Formal Conjectures evidence and current Cert-route invariants passed.")
    return 0


__all__ = [
    "ADJUDICATED_STATES",
    "CURRENT_CERT_REGISTRY_PATH",
    "CURRENT_CERT_SCHEMA_PATH",
    "HANDOFF_DIR",
    "INTAKE_STATES",
    "MANIFEST_DIR",
    "POSITIVE_STATES",
    "artifact_errors",
    "campaign_manifest_errors",
    "current_cert_route_errors",
    "current_route_state",
    "expected_campaigns",
    "formal_conjectures_errors",
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
