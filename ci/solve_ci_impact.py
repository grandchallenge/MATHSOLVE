"""Exact-transition routing for expensive Solve CI; not theorem authority."""
import json
import os
import re
import subprocess
from pathlib import Path
import yaml

LANES = {"pnp", "rhns", "erdos", "uc", "rsiccc", "full"}
SHARED = {"lean-toolchain", "lakefile.lean", "lake-manifest.json",
          "ci/checked_lean.py", "ci/validate_lean_ci_integrity.py",
          "ci/solve_ci_impact.py", "tests/test_solve_ci_impact.py"}
ROOT = "MathSolve.lean"
WORKFLOW = ".github/workflows/ci.yml"
MODULE = re.compile(r"MathSolve(?:\.[A-Za-z_][A-Za-z_0-9]*)+")

def module_lane(module):
    for prefixes, lane in [
        (("MathSolve.PNP.",), "pnp"),
        (("MathSolve.Erdos.", "MathSolve.FormalConjectures.E602"), "erdos"),
        (("MathSolve.RH.", "MathSolve.FormalConjectures."), "rhns"),
        (("MathSolve.UnionClosed.",), "uc"),
        (("MathSolve.RSICCC.",), "rsiccc")]:
        if module.startswith(prefixes):
            return lane
    return "full"

def imports(text):
    result = set()
    for line in text.splitlines():
        if not line.strip():
            continue
        if not line.strip().startswith("import "):
            return None
        module = line.strip()[7:]
        if not MODULE.fullmatch(module):
            return None
        result.add(module)
    return result

def workflow_impact(old, new):
    a, b = (yaml.safe_load(x)["jobs"] for x in (old, new))
    otp = a.get("otp-handoff-cross-platform") != b.get("otp-handoff-cross-platform")
    aa, bb = a.get("formal-targets"), b.get("formal-targets")
    if aa == bb:
        return set(), otp
    if not aa or not bb:
        return set(LANES), otp
    common = lambda x: {k:v for k,v in x.items() if k != "steps"}
    if common(aa) != common(bb):
        return set(LANES), otp
    def partition(job):
        steps, other = {}, []
        for s in job["steps"]:
            name = s.get("name", "")
            if name.startswith("Replay lane: ") and name[13:] in LANES:
                if name in steps:
                    raise ValueError("duplicate formal lane")
                steps[name] = s
            else:
                other.append(s)
        return steps, other
    sa, oa = partition(aa)
    sb, ob = partition(bb)
    if oa != ob:
        return set(LANES), otp
    return {n[13:] for n in sa.keys() | sb.keys() if sa.get(n) != sb.get(n)}, otp

def native_pnp_only(paths):
    # Narrow, positively identified exception: all other ledger checks retain
    # their former coverage until their own dependency closures are established.
    return bool(paths) and all(p.startswith("research/PNP-ABOVE/") for p in paths)

def classify(paths, before, after):
    selected, otp = set(), False
    for path in paths:
        low = path.lower()
        if path in SHARED or path == "requirements-ci.txt":
            selected.update(LANES)
        elif path == WORKFLOW:
            lanes, changed_otp = workflow_impact(before(path), after(path))
            selected.update(lanes)
            otp |= changed_otp
        elif path == ROOT:
            a, b = imports(before(path)), imports(after(path))
            if a is None or b is None:
                selected.update(LANES)
            else:
                selected.update(module_lane(m) for m in a ^ b)
        elif path.startswith("MathSolve/") and path.endswith(".lean"):
            selected.add(module_lane(path[:-5].replace("/", ".")))
        elif path.startswith("research/ERDOS-602/") or "erdos602" in low:
            selected.add("erdos")
        elif path.startswith("formal_sources/formal_conjectures/") or path in {
            "ci/validate_formal_conjectures_targets.py", "ci/test_formal_conjectures_targets.py",
            "schemas/formal_target_package.schema.json"}:
            selected.add("rhns")
        if (path in {"requirements-ci.txt", "ci/validate_repo_case_collisions.py"}
            or path.startswith("work_packages/OPENAI_TEN_PROOFS_WP00/")
            or path.startswith("sources/OPENAI-TEN-PROOFS-001/")
            or "openai_ten_proofs" in low or "openai-ten-proofs" in low):
            otp = True
    if "full" in selected:
        selected.update(LANES)
    return selected, otp

def git(*args):
    return subprocess.check_output(["git", *args])

def read_at(rev, path):
    if not git("ls-tree", "-z", rev, "--", path):
        return ""
    return git("show", f"{rev}:{path}").decode("utf-8")

def main():
    event = json.loads(Path(os.environ["GITHUB_EVENT_PATH"]).read_text())
    head = os.environ["GITHUB_SHA"]
    if git("rev-parse", "HEAD").decode().strip() != head:
        raise SystemExit("wrong classification checkout")
    kind = os.environ["GITHUB_EVENT_NAME"]
    subject = head
    if kind == "workflow_dispatch":
        selected, otp, paths = set(LANES), True, []
    else:
        if kind == "pull_request":
            base = git("rev-parse", "HEAD^1").decode().strip()
            subject = event["pull_request"]["head"]["sha"]
            if git("rev-parse", "HEAD^2").decode().strip() != subject:
                raise SystemExit("wrong pull request merge parent")
        elif kind == "push":
            base = event["before"]
            if base == "0" * 40:
                raise SystemExit("missing push base")
            subprocess.run(["git", "fetch", "--no-tags", "--depth=1", "origin", base], check=True)
        else:
            raise SystemExit("unsupported event")
        paths = [p.decode("utf-8") for p in git("diff", "--no-renames", "--name-only", "-z", base, head).split(b"\0") if p]
        selected, otp = classify(paths, lambda p: read_at(base,p), lambda p: read_at(head,p))
    root = imports(read_at(subject, ROOT))
    if root is None:
        selected.update(LANES)
    modules = set(root or ())
    files = [p.decode() for p in git("ls-tree", "-r", "--name-only", "-z", subject, "MathSolve").split(b"\0") if p.endswith(b".lean")]
    modules.update(p[:-5].replace("/", ".") for p in paths if p in files)
    # Close over any actual cross-family import edges in the exact subject.
    if selected and "full" not in selected:
        edges = set()
        for path in files:
            owner = module_lane(path[:-5].replace("/", "."))
            for target in re.findall(r"(?m)^\s*import\s+(MathSolve(?:\.[A-Za-z_][A-Za-z_0-9]*)*)", read_at(subject,path)):
                edges.add((owner, module_lane(target)))
        while True:
            expanded = selected | {owner for owner, dep in edges if dep in selected or dep == "full"}
            if "full" in expanded:
                expanded.update(LANES)
            if expanded == selected:
                break
            selected = expanded
    if any(not MODULE.fullmatch(m) for m in modules):
        raise SystemExit("invalid Lean module target")
    targets = (["MathSolve"] + sorted(modules)) if "full" in selected else sorted(m for m in modules if module_lane(m) in selected)
    print(json.dumps({"changed": paths, "lanes": sorted(selected), "otp": otp, "targets": targets}))
    with open(os.environ["GITHUB_OUTPUT"], "a") as out:
        for lane in sorted(LANES):
            print(f"{lane}={str(lane in selected).lower()}", file=out)
        print(f"formal={str(bool(selected)).lower()}", file=out)
        print(f"otp={str(otp).lower()}", file=out)
        print(f"native_pnp_only={str(native_pnp_only(paths)).lower()}", file=out)
        print("targets=" + " ".join(targets), file=out)

if __name__ == "__main__":
    main()
