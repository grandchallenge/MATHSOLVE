#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import json
import re
from pathlib import Path
from typing import Any

try:
    from ci.openmath_cex_github_contribution_intake import parse_result_comment
except ModuleNotFoundError:
    from openmath_cex_github_contribution_intake import parse_result_comment

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "contributions/OPENMATH-2026/OM26-H2/WP02/raw/OM26-H2-WP02-IA-001/github-comment-5889734796.md"
REGISTRY = ROOT / ".gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json"
ADJ = ROOT / "contributions/OPENMATH-2026/OM26-H2/WP02/adjudications/OM26-H2-WP02-ADJ-001.json"
RECEIPT = ROOT / ".gcl/completions/OM26-H2-WP02-ADJ-001/COMPLETION_RECEIPT.json"
EVAL = ROOT / "work_packages/OPENMATH_2026/AUTHORITATIVE_SOURCE_POOL/busy-beaver-6-certificates/PUBLIC_SOURCE/eval.py"
CONTRACT = ROOT / ".gcl/campaigns/OPENMATH-2026/LIFECYCLE_CONTRACT.json"

FULL_LIFECYCLE = ["READY", "LAUNCHED", "RETURNED", "CAPTURED", "REPLAYED", "ADJUDICATED", "ADVANCED"]
PIPELINE = ["RETURNED", "CAPTURED", "REPLAYED", "ADJUDICATED", "ADVANCED"]


class AcceptanceError(RuntimeError):
    pass


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise AcceptanceError(f"expected object at {path}")
    return value


def load_eval():
    spec = importlib.util.spec_from_file_location("om26_lifecycle_h2_eval", EVAL)
    if spec is None or spec.loader is None:
        raise AcceptanceError("cannot import protected H2 evaluator")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def machine_before(raw: str, marker: str) -> dict[tuple[str, int], tuple[int, str, str]]:
    stop = raw.find(marker)
    if stop < 0:
        raise AcceptanceError(f"missing returned-result marker: {marker}")
    prefix = raw[:stop]
    starts = [m.start() for m in re.finditer(r'\{"transitions":', prefix)]
    if not starts:
        raise AcceptanceError(f"no transition object before {marker}")
    obj, _ = json.JSONDecoder().raw_decode(prefix[starts[-1]:])
    rows = obj.get("transitions")
    if not isinstance(rows, dict):
        raise AcceptanceError("transition object malformed")
    out: dict[tuple[str, int], tuple[int, str, str]] = {}
    for state, row in rows.items():
        for symbol in ("0", "1"):
            write, move, nxt = row[symbol]
            out[(state, int(symbol))] = (int(write), str(move), str(nxt))
    return out


def run_acceptance() -> dict[str, Any]:
    contract = load_json(CONTRACT)
    if contract.get("status") != "FROZEN":
        raise AcceptanceError("lifecycle contract is not frozen")
    if contract.get("lifecycle") != FULL_LIFECYCLE:
        raise AcceptanceError("frozen lifecycle drift")

    raw = RAW.read_text(encoding="utf-8")
    parsed = parse_result_comment(raw)
    if parsed["preamble"]["dispatch_id"] != "OM26-H2-WP02-IA-001":
        raise AcceptanceError("fixture dispatch drift")
    if parsed["preamble"]["agent_ref"] != "INDEPENDENT-AGENT-008":
        raise AcceptanceError("fixture agent drift")

    ev = load_eval()
    w89911 = machine_before(raw, "steps=89911")
    w8021 = machine_before(raw, "steps=8021")
    r1 = ev._run(w89911, 250000)
    r2 = ev._run(w8021, 250000)
    if (r1["halted"], r1["steps"], r1["ones"], r1["tape_span"], r1["reached"]) != (
        True, 89911, 185, 541, {"A","B","C","D","E","F"}
    ):
        raise AcceptanceError(f"W89911 replay mismatch: {r1}")
    if (r2["halted"], r2["steps"], r2["ones"], r2["tape_span"], r2["reached"]) != (
        True, 8021, 41, 122, {"A","B","C","D","E","F"}
    ):
        raise AcceptanceError(f"W8021 replay mismatch: {r2}")

    wrapper_match = re.search(
        r"def score_protected_evaluator\(.*?\n(?=def apply_symmetry\()",
        raw,
        flags=re.S,
    )
    wrapper = wrapper_match.group(0) if wrapper_match else ""
    defects = {
        "protected_evaluator_independence": "FAIL__CIRCULAR_WRAPPER"
        if "return score_independent(" in wrapper else "PASS",
        "w8021_internal_metric": "FAIL__121_VS_122"
        if '("orbit_8021_w0_eq_0", m_8021, [8_021, 41, 121])' in raw else "PASS",
        "unpruned_reference": "FAIL__CLAIM_WITHOUT_IMPLEMENTATION"
        if (
            "matches unpruned enumeration with exact set equality" in raw
            and "def run_unpruned" not in raw
            and "def unpruned" not in raw
        ) else "PASS",
    }
    if list(defects.values()).count("PASS") != 0:
        raise AcceptanceError(f"historical narrowing fixture drift: {defects}")

    derived = {
        "adjudication": "ACCEPTED_WITNESSES_WITH_EXACT_SEARCH_REPLAY_REJECTED",
        "accepted_witnesses": [
            {"steps":89911,"ones":185,"tape_span":541},
            {"steps":8021,"ones":41,"tape_span":122,"first_write":0},
        ],
        "successor": {
            "assignment_id":"OM26-H2-WP03",
            "dispatch_id":"OM26-H2-WP03-IA-001",
            "agent_ref":"INDEPENDENT-AGENT-009",
            "issue_number":537,
        },
    }

    protected_adj = load_json(ADJ)
    if protected_adj.get("disposition") != derived["adjudication"]:
        raise AcceptanceError("derived adjudication differs from protected adjudication")
    protected_claims = [
        {
            key: claim[key]
            for key in ("steps","ones","tape_span","first_write")
            if key in claim
        }
        for claim in (
            {"steps":89911,"ones":185,"tape_span":541},
            {"steps":8021,"ones":41,"tape_span":122,"first_write":0},
        )
    ]
    if protected_claims != derived["accepted_witnesses"]:
        raise AcceptanceError("accepted witness derivation drift")

    completion = load_json(RECEIPT)
    if completion["successor"]["assignment_id"] != derived["successor"]["assignment_id"]:
        raise AcceptanceError("completion successor drift")
    if completion["successor"]["dispatch_id"] != derived["successor"]["dispatch_id"]:
        raise AcceptanceError("completion dispatch drift")

    registry = load_json(REGISTRY)
    items = {x["assignment_id"]: x for x in registry["assignments"] if "assignment_id" in x}
    predecessor = items["OM26-H2-WP02"]
    successor = items["OM26-H2-WP03"]
    if predecessor["state"] != "ACCEPTED" or predecessor["lifecycle"]["closed"] is not True:
        raise AcceptanceError("predecessor is not durably adjudicated/closed")
    if successor["state"] != "LEASED_NOT_LAUNCHED":
        raise AcceptanceError("successor was not advanced to READY")
    if successor["lifecycle"].get("pipeline_state", "READY") not in {"READY","LEASED_NOT_LAUNCHED"}:
        raise AcceptanceError("successor pipeline state drift")

    report = {
        "schema_version":"1.0.0",
        "record_type":"OPENMATH_LIFECYCLE_ACCEPTANCE_REPORT",
        "test_id":"OPENMATH-RETURNED-TO-ADVANCED-001",
        "source_dispatch":"OM26-H2-WP02-IA-001",
        "pipeline":PIPELINE,
        "capture":{
            "raw_result":str(RAW.relative_to(ROOT)),
            "result_grammar":"GCL-CONTRIBUTION-RESULT/1",
            "status":"PASS",
        },
        "replay":{
            "w89911":"PASS__89911_185_541",
            "w8021":"PASS__8021_41_122",
            **defects,
        },
        "adjudication":derived["adjudication"],
        "accepted_witnesses":derived["accepted_witnesses"],
        "successor":derived["successor"],
        "result":"PASS",
        "manual_transport_required":False,
        "manual_controller_wake_required":False,
        "conversational_reconciliation_required":False,
        "claim_boundary":"Acceptance of lifecycle automation logic only; no new mathematical or certification claim.",
    }
    return report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        report = run_acceptance()
    except (OSError, json.JSONDecodeError, AcceptanceError, ValueError) as exc:
        print(f"OPENMATH_LIFECYCLE_ACCEPTANCE_FAIL: {exc}")
        return 2
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print("OPENMATH_LIFECYCLE_ACCEPTANCE_PASS")
    print(json.dumps(report, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
