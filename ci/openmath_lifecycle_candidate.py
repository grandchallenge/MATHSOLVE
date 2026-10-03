#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = Path(".gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json")
LANES = Path("work_packages/OPENMATH_2026/HILL_LANES.json")
BOARD = Path("handoffs/OPENMATH-2026/CEX_JOB_BOARD.md")
INDEX = Path("handoffs/OPENMATH-2026/launch/README.md")
ASSIGNMENT_RE = re.compile(r"^OM26-H([1-7])-WP([0-9]{2})$")
PIPELINE = ["RETURNED", "CAPTURED", "REPLAYED", "ADJUDICATED", "ADVANCED"]


def successor_transport_header() -> str:
    return "\n".join([
        "GITHUB_ACCESS_REQUIRED: PARTICIPANT_ENVIRONMENT_AUTHENTICATED_COMMENT_CAPABILITY",
        "RETURN_COMPLETION_RECEIPT_REQUIRED: GITHUB_ISSUE_COMMENT_URL",
    ])


class LifecycleCandidateError(RuntimeError):
    pass


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise LifecycleCandidateError(f"expected object: {path}")
    return value


def dump(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def blob_sha1(text: str) -> str:
    data = text.encode("utf-8")
    return hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


def successor_identity(assignment_id: str) -> tuple[str, str, str, str]:
    match = ASSIGNMENT_RE.fullmatch(assignment_id)
    if not match:
        raise LifecycleCandidateError(f"automatic successor unsupported: {assignment_id}")
    hill_no, wp_text = match.groups()
    wp = int(wp_text) + 1
    hill = f"OM26-H{hill_no}"
    assignment = f"{hill}-WP{wp:02d}"
    dispatch = f"{assignment}-IA-001"
    agent = f"INDEPENDENT-AGENT-{int(hill_no) * 100 + wp:03d}"
    return hill, assignment, dispatch, agent


def intake(intake_dir: Path) -> tuple[dict[str, Any], dict[str, Any], str]:
    meta = load(intake_dir / "META.json")
    receipt = load(intake_dir / "RECEIPT.json")
    raw = (intake_dir / "RAW.md").read_text(encoding="utf-8")
    return meta, receipt, raw


def plan(intake_dir: Path) -> dict[str, Any]:
    meta, receipt, raw = intake(intake_dir)
    hill, assignment, dispatch, agent = successor_identity(receipt["assignment_id"])
    residual = (
        "Independently convert the strongest predecessor claim into deterministic protected replay evidence. "
        "If it cannot be established, return the exact counterexample or blocker. "
        "Do not promote the predecessor claim merely because its RESULT/1 was structurally valid."
    )
    body = f"""GCL-CONTRIBUTION-DISPATCH/1
dispatch_id: {dispatch}
agent_ref: {agent}
campaign: OPENMATH-2026
hill: {hill}
assignment: {assignment}
concurrency_mode: independent_blind
return_protocol: GCL-CONTRIBUTION-RESULT/1

# {assignment} — automatic replay-closure successor

## Authority boundary

This bounded zero-context successor was generated after protected intake of {receipt['assignment_id']}. It does not authorize repository mutation, certification, or competition submission.

## Protected predecessor result

```text
{raw.rstrip()}
```

## Required work

{residual}

Produce replayable evidence rather than a confidence judgment. A failed replay is a valid result.

## Required result

Return exactly one narrative-only RESULT/1 with no links or attachments:

```text
GCL-CONTRIBUTION-RESULT/1
dispatch_id: {dispatch}
agent_ref: {agent}
assignment: {assignment}
disposition: <REPLAY_CLOSURE_VALIDATED|REPLAY_CLOSURE_COUNTEREXAMPLE|EXACT_BLOCKER>
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: <YES|NO>

## Strongest exact statement

...

## Derivation

...

## Assumptions beyond bootstrap

...

## Verification / falsification hooks

...

## Claim boundary

...

## Next residual

...
```

Next residual has at most three sentences.
"""
    return {
        "schema_version":"1.0.0",
        "predecessor_assignment":receipt["assignment_id"],
        "predecessor_dispatch":receipt["dispatch_id"],
        "hill":hill,
        "successor_assignment":assignment,
        "successor_dispatch":dispatch,
        "successor_agent":agent,
        "issue_title":f"[GCL-CONTRIB] OPENMATH-2026 {dispatch} — automatic replay closure",
        "issue_body":body,
        "next_residual":residual,
        "pipeline":PIPELINE,
        "comment_id":meta["comment_id"],
    }


def refresh_summary(registry: dict[str, Any]) -> dict[str, int]:
    policy = registry["mathematics_release_policy"]
    assignments = {
        x["assignment_id"]: x
        for x in registry["assignments"]
        if isinstance(x, dict) and x.get("assignment_id")
    }
    current = []
    for hill, row in policy["per_hill"].items():
        assignment_id = row.get("assignment")
        item = assignments.get(assignment_id)
        if item is None:
            raise LifecycleCandidateError(f"{hill}: current assignment missing from registry")
        current.append(item)

    current.extend(
        assignments[row["assignment_id"]]
        for row in registry.get("launch_contract", {}).get("support_scripts", {}).values()
    )

    math_assignments = [
        x for x in assignments.values()
        if x.get("class") == "MATHEMATICAL_RESEARCH"
    ]
    summary = policy["summary"]
    summary["accepted_agents"] = sum(1 for x in math_assignments if x.get("state") == "ACCEPTED")
    summary["leased_not_launched_agents"] = sum(
        1 for x in current if x.get("state") == "LEASED_NOT_LAUNCHED"
    )
    summary["launched_agents"] = sum(1 for x in current if x.get("state") == "LAUNCHED")
    summary["returned_unadjudicated_agents"] = sum(
        1 for x in current
        if x.get("state") in {"RETURNED", "CAPTURED", "ADJUDICATING"}
    )
    return summary


def board_text(registry: dict[str, Any]) -> str:
    rows=[]
    assignments=[
        x for x in registry["assignments"]
        if x.get("class")=="MATHEMATICAL_RESEARCH" and x.get("hill","").startswith("OM26-H")
    ]
    assignments.sort(key=lambda x:(x.get("hill",""),x.get("assignment_id","")))
    for x in assignments:
        lease=x.get("lease",{})
        rows.append(
            f"| `{x['assignment_id']}` | `{x.get('hill')}` | `{x.get('state')}` | "
            f"`{lease.get('dispatch_id')}` | `{lease.get('agent_ref')}` | #{lease.get('dispatch_issue_number')} |"
        )
    links=[]
    for i in range(1,8):
        row=registry["launch_contract"]["current_scripts"][f"OM26-H{i}"]
        links.append(
            f"- H{i}: {row['task_url']}" if row.get("executable")
            else f"- H{i}: guard only; no active successor lease."
        )
    for slot, row in registry["launch_contract"].get("support_scripts", {}).items():
        links.append(f"- {slot} (support): {row['task_url']}")
    return """# OPENMATH-2026 CEX job board

This page is a human projection of the protected machine registry.

## Current seven-hill independent-agent lifecycle

| Assignment | Hill | State | Dispatch | Agent | Return issue |
|---|---|---|---|---|---|
"""+"\n".join(rows)+"""

The lifecycle is `READY -> LAUNCHED -> RETURNED -> CAPTURED -> REPLAYED -> ADJUDICATED -> ADVANCED`. Intake alone creates no mathematical claim effect.

## Current task links

"""+"\n".join(links)+"""

## Launcher contract

Canonical mode is `LINK_IN_RELAY_OUT`. Voluntary participants use a registered immutable task URL. GCL may optionally launch its own workers. The worker returns one complete `GCL-RETURN-RELAY/1` payload. Authenticated GCL infrastructure owns durable GitHub intake.

## Claim boundary

Automatic fallback adjudication may preserve evidence and advance a replay-closure successor without promoting the predecessor mathematics. MATHCERT certification and competition submission remain separate authorities.
"""


def index_text(registry: dict[str, Any]) -> str:
    lines=[
        "# OPENMATH-2026 immutable launch index",
        "",
        "Canonical mode is `LINK_IN_RELAY_OUT`. No human work-package copy/paste is part of the protocol.",
        "",
        "| Hill | Immutable task | Executable |",
        "|---|---|---|",
    ]
    for i in range(1,8):
        hill=f"OM26-H{i}"
        row=registry["launch_contract"]["current_scripts"][hill]
        if row.get("executable"):
            detail=f"Yes — {row.get('assignment_id')} / {row.get('agent_ref')}"
            lines.append(f"| H{i} | {row.get('task_url')} | {detail} |")
        else:
            lines.append(f"| H{i} | {row.get('task_url','')} | No — {row.get('reason','guarded')} |")
    for slot, row in registry["launch_contract"].get("support_scripts", {}).items():
        lines.append(f"| {slot} (support) | {row.get('task_url')} | Yes — {row.get('assignment_id')} / {row.get('agent_ref')} |")
    return "\n".join(lines)+"\n"


def apply_candidate(root: Path, intake_dir: Path, issue_number: int, issue_url: str) -> dict[str, Any]:
    meta, receipt, raw = intake(intake_dir)
    p = plan(intake_dir)
    registry=load(root/REGISTRY)
    lanes=load(root/LANES)
    items={x["assignment_id"]:x for x in registry["assignments"] if x.get("assignment_id")}
    predecessor=items.get(receipt["assignment_id"])
    if predecessor is None:
        raise LifecycleCandidateError("predecessor missing from registry")
    if predecessor.get("state") not in {"LEASED_NOT_LAUNCHED","LAUNCHED","RETURNED","CAPTURED","ADJUDICATING"}:
        raise LifecycleCandidateError(f"predecessor is not open: {predecessor.get('state')}")
    lease=predecessor.get("lease",{})
    if lease.get("dispatch_id")!=receipt["dispatch_id"] or lease.get("agent_ref")!=receipt["agent_ref"]:
        raise LifecycleCandidateError("returned identity differs from protected lease")

    is_support = predecessor.get("lane_role") == "SUPPORT"
    support_slot = predecessor.get("support_slot")
    if is_support:
        registered = registry["launch_contract"].get("support_scripts", {}).get(support_slot, {})
    else:
        registered = registry["launch_contract"]["current_scripts"][p["hill"]]
    if registered.get("assignment_id") != receipt["assignment_id"]:
        raise LifecycleCandidateError("returned assignment is not the current primary/support task")

    successor_assignment=p["successor_assignment"]
    if successor_assignment in items:
        raise LifecycleCandidateError(f"successor already exists: {successor_assignment}")

    # Trusted fallback replay is deliberately conservative: structure is replayed; mathematics is not promoted.
    replay={
        "schema_version":"1.0.0",
        "record_type":"OPENMATH_LIFECYCLE_REPLAY",
        "campaign":"OPENMATH-2026",
        "hill":p["hill"],
        "assignment_id":receipt["assignment_id"],
        "dispatch_id":receipt["dispatch_id"],
        "state":"REPLAYED",
        "profile":"CONSERVATIVE_STRUCTURAL_REPLAY",
        "checks":{
            "result_schema":"PASS",
            "protected_dispatch_identity":"PASS",
            "trusted_mathematical_adapter":"NOT_REGISTERED",
        },
        "claim_effect":"NONE",
        "next_residual":p["next_residual"],
    }
    adjudication={
        "schema_version":"1.0.0",
        "record_type":"OPENMATH_AUTOMATED_BOUNDED_ADJUDICATION",
        "campaign":"OPENMATH-2026",
        "hill":p["hill"],
        "assignment_id":receipt["assignment_id"],
        "dispatch_id":receipt["dispatch_id"],
        "agent_ref":receipt["agent_ref"],
        "state":"ADJUDICATED",
        "disposition":"ACCEPTED_EVIDENCE_WITHOUT_CLAIM_PROMOTION",
        "accepted_claims":[],
        "claim_effect":"NONE",
        "certification_effect":False,
        "competition_effect":False,
        "successor":{
            "assignment_id":successor_assignment,
            "dispatch_id":p["successor_dispatch"],
            "agent_ref":p["successor_agent"],
            "issue_number":issue_number,
        },
        "claim_boundary":"The returned evidence is preserved, but no mathematical claim is promoted without a trusted replay adapter.",
    }

    raw_path=root/meta["raw_repo_path"]
    receipt_path=root/meta["receipt_repo_path"]
    raw_path.parent.mkdir(parents=True,exist_ok=True)
    receipt_path.parent.mkdir(parents=True,exist_ok=True)
    raw_path.write_text(raw,encoding="utf-8")
    receipt_path.write_text((intake_dir/"RECEIPT.json").read_text(encoding="utf-8"),encoding="utf-8")

    base=raw_path.parents[2]
    lifecycle_dir=base/"lifecycle"/receipt["dispatch_id"]
    replay_path=lifecycle_dir/"REPLAY.json"
    adjudication_path=lifecycle_dir/"ADJUDICATION.json"
    projection_path=lifecycle_dir/"PROGRAMME_PROJECTION.json"
    manifest_path=lifecycle_dir/"MANIFEST.json"
    dump(replay_path,replay)
    dump(adjudication_path,adjudication)

    predecessor["state"]="ACCEPTED"
    lease["state"]="CLOSED_AFTER_RETURN"
    lease["execution_authorized"]=False
    predecessor["lifecycle"]={
        "prepared":True,"leased":True,"launched":True,
        "launch_receipt":predecessor.get("lifecycle",{}).get("launch_receipt") or "RETURN_PROVES_EXECUTION_OCCURRED",
        "returned":True,"captured":True,"replayed":True,
        "adjudication":adjudication["disposition"],"pipeline_state":"ADVANCED",
        "certification":"NOT_ELIGIBLE","closed":True,
    }
    predecessor["successor_gate"]=f"Closed automatically; {successor_assignment} owns replay closure."

    source_lock=copy.deepcopy(predecessor.get("prerequisites",{}).get("source_lock"))
    wp=successor_assignment.rsplit("-",1)[-1]
    dispatch_path=f"contributions/OPENMATH-2026/{p['hill']}/{wp}/dispatches/{p['successor_dispatch']}.json"
    operation_path=f".gcl/operations/{p['successor_dispatch']}/OPERATION.json"
    bootstrap_path=f"handoffs/OPENMATH-2026/jobs/{p['successor_dispatch']}.md"
    launch_path=f"handoffs/OPENMATH-2026/launch/{successor_assignment}.md"

    bootstrap=p["issue_body"]
    launch=f"""GCL-ZERO-CONTEXT-LAUNCH/2
CAMPAIGN: OPENMATH-2026
HILL: {p['hill']}
ASSIGNMENT_ID: {successor_assignment}
DISPATCH_ID: {p['successor_dispatch']}
AGENT_REF: {p['successor_agent']}
PROTECTED_LEASE_IDENTITY: {successor_assignment} :: {p['successor_dispatch']} :: {p['successor_agent']}
INTENDED_RETURN: {issue_url}
EXECUTION_MODE: SELF_CONTAINED_INDEPENDENT_BLIND
{successor_transport_header()}
CANONICAL_MUTATION_AUTHORIZED: NO
COMPETITION_SUBMISSION_AUTHORIZED: NO
CERTIFICATION_AUTHORIZED: NO

{bootstrap}

## Embedded protected source snapshots

The complete protected predecessor result is embedded above.

## Return transport for independently arriving participants

The durable destination is INTENDED_RETURN above. Before doing substantive work, confirm that your environment can post a GitHub issue comment, either through your independently available authenticated GitHub capability or an explicitly authorized authenticated relay. Repository write access is not required; the worker itself need not hold GitHub credentials.

Deliver the complete GCL-RETURN-RELAY/1 envelope below as one comment on that exact issue. The protected intake validates its outer and inner identity and destination, retains the full envelope and hashes in its receipt, and processes the inner RESULT/1. Your relay must return the GitHub comment URL as the durable receipt. The assignment is not complete until that URL has been obtained and the posted comment has been read back from INTENDED_RETURN. Do not emit a successful completion response before durable posting and readback succeed.

Returning only to a private conversation is sufficient only when that conversation has the authorized relay. If neither direct posting nor a relay is available, report RETURN_TRANSPORT_UNAVAILABLE before beginning work. GCL cannot observe unrelated private chats. Do not ask the Human Steward to copy evidence. This task link does not grant a second lease or permit replacing a first valid result.

## Return envelope

```text
GCL-RETURN-RELAY/1
DISPATCH_ID: {p['successor_dispatch']}
AGENT_REF: {p['successor_agent']}
INTENDED_RETURN: {issue_url}

BEGIN_RESULT
<complete inner GCL-CONTRIBUTION-RESULT/1 verbatim>
END_RESULT
```

Authenticated GCL infrastructure owns durable GitHub intake.
"""
    (root/bootstrap_path).parent.mkdir(parents=True,exist_ok=True)
    (root/bootstrap_path).write_text(bootstrap,encoding="utf-8")
    (root/launch_path).parent.mkdir(parents=True,exist_ok=True)
    (root/launch_path).write_text(launch,encoding="utf-8")

    successor={
        "assignment_id":successor_assignment,
        "lane_role": "SUPPORT" if is_support else "PRIMARY",
        "support_slot": support_slot,
        "class":"MATHEMATICAL_RESEARCH",
        "hill":p["hill"],
        "obligation":wp,
        "external_hill_id":predecessor.get("external_hill_id"),
        "slot_binding":p["hill"],
        "state":"LEASED_NOT_LAUNCHED",
        "priority":"P0",
        "lease":{
            "state":"LEASED","dispatch_id":p["successor_dispatch"],"agent_ref":p["successor_agent"],
            "dispatch_issue_number":issue_number,"protected_lease_commit":"PENDING_CONTENT_COMMIT",
            "dispatch_url":issue_url,"return_url":issue_url,
            "readback_verified":False,"execution_authorized":True,
            "activation_condition":"PROTECTED_MERGE_OF_LIFECYCLE_CANDIDATE",
        },
        "work_package":bootstrap_path,
        "work_package_url":"PENDING_CONTENT_COMMIT",
        "operation_contract":operation_path,
        "prerequisites":{
            "predecessor_assignment":receipt["assignment_id"],
            "predecessor_adjudication":adjudication["disposition"],
            "protected_source_lock_required":bool(source_lock),
            "source_lock":source_lock,
            "solve_release":True,
        },
        "permissions":{
            "source_reconnaissance":False,"hill_specific_mathematics":True,
            "finite_exact_computation":True,"public_source_replay":True,
            "competition_submission":False,"certification":False,"canonical_claim_mutation":False,
        },
        "completion":["REPLAY_CLOSURE_VALIDATED","REPLAY_CLOSURE_COUNTEREXAMPLE","EXACT_BLOCKER"],
        "return_protocol":"GCL-CONTRIBUTION-RESULT/1",
        "successor_gate":"Executable only after the lifecycle candidate is protected.",
        "source_work_package":bootstrap_path,
        "dispatch_record":dispatch_path,
        "lifecycle":{
            "prepared":True,"leased":True,"launched":False,"launch_receipt":None,
            "returned":False,"captured":False,"replayed":False,"adjudication":"NOT_STARTED",
            "pipeline_state":"READY","certification":"NOT_ELIGIBLE","closed":False,
        },
    }
    registry["assignments"].append(successor)
    if not is_support:
        policy=registry["mathematics_release_policy"]["per_hill"][p["hill"]]
        policy.clear()
        policy.update({
            "solve_released":True,"assignment":successor_assignment,
            "agent_state":"LEASED_NOT_LAUNCHED","closed":False,
            "predecessor":{
                "assignment":receipt["assignment_id"],"agent_state":"ACCEPTED",
                "closed":True,"adjudication":adjudication["disposition"],
            },
        })
    summary=refresh_summary(registry)

    script_bucket = (registry["launch_contract"]["support_scripts"] if is_support
                     else registry["launch_contract"]["current_scripts"])
    script_key = support_slot if is_support else p["hill"]
    script_bucket[script_key]={
        "path":launch_path,"executable":True,
        "assignment_id":successor_assignment,"dispatch_id":p["successor_dispatch"],
        "agent_ref":p["successor_agent"],"intended_return":issue_url,
        "task_commit":"PENDING_CONTENT_COMMIT","task_blob_sha1":blob_sha1(launch),
        "task_url":"PENDING_CONTENT_COMMIT",
    }

    if not is_support:
        lane=next(x for x in lanes["hills"] if x["hill_slot"]==p["hill"])
        old_active=copy.deepcopy(lane.get("active_lease") or {})
        lane["status"]=f"{wp}_LEASED_NOT_LAUNCHED__AUTOMATED_SUCCESSOR"
        lane["next_action"]=f"Launch {p['successor_agent']} from the registered immutable LINK_IN_RELAY_OUT task URL."
        lane["predecessor_lease"]={
            **old_active,"assignment_id":receipt["assignment_id"],"dispatch_id":receipt["dispatch_id"],
            "agent_ref":receipt["agent_ref"],"lifecycle_state":"ACCEPTED",
            "return_evidence":meta["raw_repo_path"],"adjudication":adjudication["disposition"],
        }
        lane["active_lease"]={
            "assignment_id":successor_assignment,"dispatch_id":p["successor_dispatch"],
            "agent_ref":p["successor_agent"],"issue_url":issue_url,
            "protected_merge":"PROTECTED_LIFECYCLE_CANDIDATE","readback_verified":False,
            "lifecycle_state":"LEASED_NOT_LAUNCHED","launch_evidence":None,"return_evidence":None,
        }

    if is_support:
        lane=next(x for x in lanes["hills"] if x["hill_slot"]==p["hill"])
        lane.setdefault("supporting_leases", {})[support_slot]={
            "assignment_id":successor_assignment,"dispatch_id":p["successor_dispatch"],
            "agent_ref":p["successor_agent"],"issue_url":issue_url,
            "protected_merge":"PROTECTED_LIFECYCLE_CANDIDATE","readback_verified":False,
            "lifecycle_state":"LEASED_NOT_LAUNCHED","launch_evidence":None,"return_evidence":None,
        }

    summary=refresh_summary(registry)

    dispatch={
        "schema_version":"1.0.0","record_type":"GCL_EXTERNAL_DISPATCH",
        "dispatch_id":p["successor_dispatch"],"campaign":"OPENMATH-2026","hill":p["hill"],
        "assignment_id":successor_assignment,"agent_ref":p["successor_agent"],
        "concurrency_mode":"independent_blind","bootstrap_path":bootstrap_path,
        "bootstrap_blob_sha1":blob_sha1(bootstrap),"source_handoff_commit_sha":"PENDING_CONTENT_COMMIT",
        "return_protocol":"GCL-CONTRIBUTION-RESULT/1","github_issue_number":issue_number,
        "github_issue_url":issue_url,"github_issue_title":p["issue_title"],
        "canonical_mutation_authorized":False,"dispatch_status":"READY_FOR_GITHUB_COMMENT",
        "operation_contract":operation_path,
        "protected_lease_required": True,
    }
    operation={
        "schema_version":"1.0.0","record_type":"GCL_OPERATION_CONTRACT",
        "operation":p["successor_dispatch"],"campaign":"OPENMATH-2026","hill":p["hill"],
        "assignment_id":successor_assignment,"dispatch_id":p["successor_dispatch"],
        "agent_ref":p["successor_agent"],"objective":p["next_residual"],
        "acceptable_dispositions":["REPLAY_CLOSURE_VALIDATED","REPLAY_CLOSURE_COUNTEREXAMPLE","EXACT_BLOCKER"],
        "return_protocol":"GCL-CONTRIBUTION-RESULT/1","github_issue_number":issue_number,
        "github_issue_url":issue_url,"canonical_mutation_authorized":False,
    }
    dump(root/dispatch_path,dispatch)
    dump(root/operation_path,operation)

    projection={
        "schema_version":"1.0.0","record_type":"OPENMATH_PROGRAMME_PROJECTION",
        "campaign":"OPENMATH-2026","source_dispatch":receipt["dispatch_id"],"hill":p["hill"],
        "lane_role": "SUPPORT" if is_support else "PRIMARY", "support_slot": support_slot,
        "predecessor":{
            "assignment_id":receipt["assignment_id"],"agent_ref":receipt["agent_ref"],
            "adjudication":adjudication["disposition"],"accepted_claims":[],
        },
        "successor":{
            "assignment_id":successor_assignment,"dispatch_id":p["successor_dispatch"],
            "agent_ref":p["successor_agent"],"issue_number":issue_number,
            "lifecycle":"LEASED_NOT_LAUNCHED",
        },
        "external_agent_summary":copy.deepcopy(summary),
        "pipeline_trace":PIPELINE,"claim_effect":"NONE",
    }
    dump(projection_path,projection)
    review_path = Path("work_packages/OPENMATH_2026/COMPETITION_PACKETS/SECTION8_EVIDENCE_REVIEW_QUEUE.json")
    queue = load(root/review_path) if (root/review_path).exists() else {"record_type":"SECTION8_EVIDENCE_REVIEW_QUEUE", "items":[]}
    if not any(x["dispatch_id"] == receipt["dispatch_id"] for x in queue["items"]):
        queue["items"].append({
            "dispatch_id":receipt["dispatch_id"], "assignment_id":receipt["assignment_id"],
            "hill":p["hill"], "raw_path":meta["raw_repo_path"], "receipt_path":meta["receipt_repo_path"],
            "declared_disposition":receipt.get("disposition_declared"),
            "comment_created_at":receipt.get("comment_created_at"),
            "authenticated_actor":receipt.get("authenticated_github_actor"),
            "state":"PENDING_EXACT_MATHEMATICAL_REPLAY_AND_NOVELTY_REVIEW", "claim_effect":"NONE",
        })
    dump(root/review_path,queue)
    dump(root/REGISTRY,registry)
    dump(root/LANES,lanes)
    (root/BOARD).write_text(board_text(registry),encoding="utf-8")
    (root/INDEX).write_text(index_text(registry),encoding="utf-8")

    changed=[
        meta["raw_repo_path"],meta["receipt_repo_path"],
        str(replay_path.relative_to(root)),str(adjudication_path.relative_to(root)),
        str(projection_path.relative_to(root)),str(manifest_path.relative_to(root)),
        str(REGISTRY),str(LANES),str(BOARD),str(INDEX),
        bootstrap_path,launch_path,dispatch_path,operation_path,str(review_path),
    ]
    manifest={
        "schema_version":"1.0.0","record_type":"OPENMATH_LIFECYCLE_CANDIDATE",
        "campaign":"OPENMATH-2026","dispatch_id":receipt["dispatch_id"],
        "assignment_id":receipt["assignment_id"],"hill":p["hill"],
        "comment_id":meta["comment_id"],"pipeline":PIPELINE,
        "programme_projection_path":str(projection_path.relative_to(root)),
        "successor_assignment":successor_assignment,"successor_dispatch":p["successor_dispatch"],
        "successor_agent":p["successor_agent"],"successor_issue":issue_number,
        "changed_paths":sorted(changed),"certification_effect":False,"competition_effect":False,
    }
    dump(manifest_path,manifest)
    return manifest


def finalize_pin(root: Path, dispatch_id: str, content_commit: str) -> dict[str, Any]:
    registry=load(root/REGISTRY)
    lanes=load(root/LANES)
    predecessor=next(
        x for x in registry["assignments"]
        if x.get("lease",{}).get("dispatch_id")==dispatch_id
    )
    hill=predecessor["hill"]
    candidates=[x for x in registry["assignments"]
                if x.get("prerequisites",{}).get("predecessor_assignment")==predecessor["assignment_id"]
                and x.get("state")=="LEASED_NOT_LAUNCHED"]
    if len(candidates)!=1:
        raise LifecycleCandidateError("exact returned dispatch must have one open successor")
    successor=candidates[0]
    current_id=successor["assignment_id"]
    is_support=successor.get("lane_role")=="SUPPORT"
    launch=(registry["launch_contract"]["support_scripts"][successor["support_slot"]] if is_support
            else registry["launch_contract"]["current_scripts"][hill])
    if launch.get("assignment_id")!=current_id:
        raise LifecycleCandidateError("successor script identity drift")
    launch_path=launch["path"]
    task_url=f"https://github.com/grandchallenge/MATHSOLVE/blob/{content_commit}/{launch_path}"
    launch["task_commit"]=content_commit
    launch["task_url"]=task_url
    successor["lease"]["protected_lease_commit"]=content_commit
    successor["work_package_url"]=f"https://github.com/grandchallenge/MATHSOLVE/blob/{content_commit}/{successor['work_package']}"
    dispatch=load(root/successor["dispatch_record"])
    dispatch["source_handoff_commit_sha"]=content_commit
    dump(root/successor["dispatch_record"],dispatch)
    lane=next(x for x in lanes["hills"] if x["hill_slot"]==hill)
    if is_support:
        lane["supporting_leases"][successor["support_slot"]]["protected_merge"]=content_commit
    else:
        lane["active_lease"]["protected_merge"]=content_commit
    dump(root/REGISTRY,registry)
    dump(root/LANES,lanes)
    (root/BOARD).write_text(board_text(registry),encoding="utf-8")
    (root/INDEX).write_text(index_text(registry),encoding="utf-8")
    return {"hill":hill,"successor":current_id,"task_url":task_url,"content_commit":content_commit}


def main() -> int:
    parser=argparse.ArgumentParser()
    sub=parser.add_subparsers(dest="cmd",required=True)
    p=sub.add_parser("plan")
    p.add_argument("--intake-dir",type=Path,required=True)
    p.add_argument("--output",type=Path,required=True)
    a=sub.add_parser("apply")
    a.add_argument("--repo-root",type=Path,default=ROOT)
    a.add_argument("--intake-dir",type=Path,required=True)
    a.add_argument("--issue-number",type=int,required=True)
    a.add_argument("--issue-url",required=True)
    f=sub.add_parser("finalize-pin")
    f.add_argument("--repo-root",type=Path,default=ROOT)
    f.add_argument("--dispatch-id",required=True)
    f.add_argument("--content-commit",required=True)
    args=parser.parse_args()
    try:
        if args.cmd=="plan":
            value=plan(args.intake_dir)
            args.output.write_text(json.dumps(value,indent=2)+"\n",encoding="utf-8")
        elif args.cmd=="apply":
            value=apply_candidate(args.repo_root,args.intake_dir,args.issue_number,args.issue_url)
        else:
            value=finalize_pin(args.repo_root,args.dispatch_id,args.content_commit)
    except (OSError,json.JSONDecodeError,KeyError,ValueError,LifecycleCandidateError) as exc:
        print(f"OPENMATH_LIFECYCLE_CANDIDATE_FAIL: {exc}")
        return 2
    print(json.dumps(value,sort_keys=True))
    return 0


if __name__=="__main__":
    raise SystemExit(main())
