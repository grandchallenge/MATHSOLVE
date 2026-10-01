"""Register fixed contest payloads through AutoLab's documented native API.

No invented reports, results or completed states. New climbs have a zero-dollar
cost cap and are left in setup; activation is a separate operational decision.
"""
import hashlib
import json
import os
from pathlib import Path
import urllib.error
import urllib.request

BASE = "https://app.autolab.ai"
ROOT = Path(__file__).resolve().parents[3]
OUT = Path("/tmp/gcl-native-submissions.json")
receipts = {"account": "jimsteeg", "entries": [], "official_scores": 0}


def api(method, path, data=None):
    req = urllib.request.Request(
        BASE + path,
        data=None if data is None else json.dumps(data).encode(),
        headers={"Authorization": "Bearer " + os.environ["AUTOLAB_TOKEN"],
                 "Content-Type": "application/json", "Accept": "application/json"},
        method=method,
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as response:
            return json.load(response)
    except urllib.error.HTTPError as error:
        # Never emit request headers or token values.
        raise RuntimeError(f"AutoLab {method} {path}: HTTP {error.code}") from None


def checkpoint():
    OUT.write_text(json.dumps(receipts, indent=2) + "\n")


def main():
    identity = api("GET", "/auth/cli/whoami")
    username = identity.get("username") or identity.get("nickname")
    if username != "jimsteeg":
        raise RuntimeError("Refused: AutoLab identity is not jimsteeg")
    projects = api("GET", "/api/v1/projects/")
    lanes = json.loads((ROOT / "work_packages/OPENMATH_2026/HILL_LANES.json").read_text())
    # H1 first; the other four payloads have exact mathematical core checks.
    h1 = Path(__file__).parent / "candidates/RH_BADER_RECONSTRUCTION_093/solution.json"
    files = {"H1": h1}
    for hill in ("H2", "H4", "H5", "H6"):
        files[hill] = ROOT / f"work_packages/OPENMATH_2026/CONTEST_CANDIDATES/{hill}/solution.json"
    # Read the official identifiers from the already-protected lane registry.
    records = lanes.get("hills", lanes.get("lanes", []))
    for hill, file in files.items():
        hill_id = next(x["exact_hill_id"] for x in records if x.get("hill_slot") == "OM26-" + hill)
        solution = file.read_text()
        digest = hashlib.sha256(file.read_bytes()).hexdigest()
        name = f"GCL 2026 {hill} fixed {digest[:12]}"
        matches = [p for p in projects if p.get("owner_username") == "jimsteeg" and p.get("name") == name]
        if len(matches) > 1:
            raise RuntimeError("Ambiguous existing climb; refused duplicate registration")
        if matches:
            slug = matches[0]["slug"]
            project = api("GET", f"/api/v1/projects/jimsteeg/{slug}")
        else:
            project = api("POST", "/api/v1/projects/", {
                "name": name, "hill": hill_id, "max_cost_usd": 0,
                "description": f"Fixed GCL contest payload {digest}. Evaluate as supplied; no search or code changes. Attribution in grandchallenge/MATHSOLVE.",
                "stop_policy": "Evaluate only the supplied payload. No generated ideas or rented compute.",
            })
            slug = project["slug"]
        endpoint = f"/api/v1/projects/jimsteeg/{slug}"
        entry = {"hill": hill, "hill_id": hill_id, "solution_sha256": digest,
                 "project_id": project["id"], "slug": slug,
                 "url": BASE + f"/projects/jimsteeg/{slug}",
                 "project_status": project.get("status"), "hill_version": project.get("hill"),
                 "stage": "CLIMB_CREATED__JOB_NOT_YET_REGISTERED"}
        receipts["entries"].append(entry)
        checkpoint()
        api("POST", endpoint + "/orchestrator/auto-generate", {"enabled": False})
        jobs = api("GET", endpoint + "/jobs/")
        title = f"Fixed {hill} payload {digest}"
        matches = [j for j in jobs["items"] if j.get("title") == title]
        if len(matches) > 1:
            raise RuntimeError("Ambiguous existing experiment; refused duplicate registration")
        if matches:
            job = matches[0]
        else:
            job = api("POST", endpoint + "/jobs/", {
                "title": title, "description": "Evaluate this exact submitted solution.json with the hill evaluator.",
                "instructions": "Do not modify solution.json. No new experiments, search or rented compute.",
                "hypothesis": "Candidate satisfies the public exact checks; official evaluation remains pending.",
                "analysis_notes": "Prior-work provenance and claim limits are retained in MATHSOLVE. No novelty or optimality claim.",
                "code": {"solution.json": solution}, "branch_from": "main",
                "locked_fields": ["title", "description", "instructions", "hypothesis", "analysis_notes", "code"],
            })
        readback = api("GET", endpoint + "/jobs/" + job["id"])
        if readback.get("code", {}).get("solution.json") != solution:
            raise RuntimeError("Server code readback differs from the submitted fixed payload")
        entry.update(job_id=readback["id"], job_status=readback["status"],
                     commit_sha=readback.get("commit_sha"),
                     stage="NATIVE_JOB_REGISTERED__OFFICIAL_EVALUATION_PENDING")
        checkpoint()
        print(json.dumps(entry))


if __name__ == "__main__":
    try:
        main()
    finally:
        checkpoint()
