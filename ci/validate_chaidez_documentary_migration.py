"""Only active WP06 is migrated. Historical ledgers and generic packets stay fixed."""
import json
from pathlib import Path
try:
    from ci.chaidez_contract import ROOT, artifact_bytes, consistency_errors, schema_errors
except ModuleNotFoundError:
    from chaidez_contract import ROOT, artifact_bytes, consistency_errors, schema_errors

WP06 = "domains/union_closed/WP06_ideal_family_bridge/chaidez_v2_conformance.json"


def validate_wp06(d=None, root=ROOT):
    root = Path(root)
    d = json.loads((root / WP06).read_text()) if d is None else d
    errors = schema_errors(d, "wp06_chaidez_conformance.schema.json")
    if errors:
        return errors
    errors += consistency_errors(d, graph_only=True)
    try:
        for ref in d["required_artifacts"].values():
            artifact_bytes(root, ref)
        if d["required_artifacts"]["CLAIM_LEDGER"] != d["baseline_claim_ledger"]["artifact"]:
            errors.append("WP06 Claim Ledger must remain identical to the protected baseline")
        status = d["result_status"]
        if status["support_route_class"] != "FORMAL_PROOF" or status["foundational_profile"]["disposition"] != "PROFILE_PRESENT":
            errors.append("WP06 must retain its formal finite-computable foundation")
        else:
            profile = status["foundational_profile"]["profile"]
            if profile["carrier_type"] != "finite" or set(profile["regularity"]) != {"finite", "decidable", "computable"}:
                errors.append("WP06 foundation expanded beyond the finite-computable route")
        if status["first_executable_step"]["node_id"] != "WP06-S9":
            errors.append("WP06 next step must preserve the restricted local node")
        if set(p["debt_id"] for p in d["proof_debt"]) != {f"WP06-PD-{i:03}" for i in range(1, 8)}:
            errors.append("WP06 historical and current debt inventory changed")
        result_text = artifact_bytes(root, d["required_artifacts"]["RESULT_STATUS"]).decode()
        if status["strongest_supported_claim"] not in result_text or "FORMAL_PROOF" not in result_text:
            errors.append("WP06 status summary differs from its operative document")
        if "not a proof of Frankl's conjecture" not in result_text:
            errors.append("WP06 restricted claim boundary disappeared")
    except (ValueError, KeyError, OSError) as exc:
        errors.append(str(exc))
    return errors


def validate_legacy(root=ROOT):
    root = Path(root)
    errors = []
    try:
        legacy = json.loads((root / "governance/external_catalog_legacy_migration.json").read_text())
        expected = {"route_id": "RM-DIO-004", "classification": "LEGACY_PRE_CATALOG_ROUTE",
                    "catalog_disposition": "NOT_A_CATALOG_PROMOTION", "bounded_evidence_preserved": True,
                    "inherited_campaign_authority": False, "inherited_certification_authority": False}
        if any(legacy.get(k) != v for k, v in expected.items()) or not legacy.get("future_promotion_gate"):
            errors.append("legacy route disposition cannot inherit catalog, campaign or certification authority")
        artifact_bytes(root, legacy["preserved_artifact"])
        baseline = json.loads((root / "contracts/chaidez/generic_handoff_baseline.json").read_text())
        packets = [r for r in baseline["artifacts"] if r["path"].startswith("cert_handoffs/")]
        if baseline["handoff_count"] != 11 or len(packets) != 11 or len({r["path"] for r in packets}) != 11:
            errors.append("eleven generic baseline handoffs must be accounted exactly once")
        for ref in baseline["artifacts"]:
            data = json.loads(artifact_bytes(root, ref))
            if ref in packets:
                errors += schema_errors(data, "mathcert_handoff.schema.json")
    except (ValueError, KeyError, OSError) as exc:
        errors.append(str(exc))
    return errors


def main():
    failures = validate_wp06() + validate_legacy()
    if failures:
        raise SystemExit("\n".join(failures))
    print("WP06 v2 reference and RM-DIO legacy classification valid; eleven generic handoffs unchanged")


if __name__ == "__main__":
    main()
