"""Placement and bounded-execution guard for direct PNP-ABOVE replays.

CHAD/WSL must use the managed SSD launcher, not raw absolute Lean paths.
This legacy direct-runner adapter is deliberately unavailable on WSL.
Historical exact source locks are not rewritten.
"""
import hashlib
import json
import os
import platform
import resource
import shutil
import subprocess
import time
from pathlib import Path

RESERVE = 2 * 1024**3
PIN = "leanprover/lean4:v4.35.0-rc3"
SLUG = "leanprover--lean4---v4.35.0-rc3"

def direct_runner_guard():
    if ("microsoft" in platform.release().lower()
            or "wsl" in platform.release().lower()
            or os.environ.get("WSL_INTEROP")
            or os.environ.get("WSL_DISTRO_NAME")):
        raise SystemExit("PNP_REPLAY_CHAD_SSD_REQUIRED: direct replay is disabled on WSL; "
                         "use the managed gcl-lean-work SSD launcher or an authorized native Linux runner. "
                         "No HDD fallback.")

def preflight(upstream, output):
    direct_runner_guard()
    upstream, output = Path(upstream).resolve(), Path(output).resolve()
    if output.exists():
        raise SystemExit("PNP_REPLAY_OUTPUT_NOT_FRESH")
    if not output.parent.is_dir():
        raise SystemExit("PNP_REPLAY_OUTPUT_PARENT_MISSING")
    free = shutil.disk_usage(output.parent).free
    if free < RESERVE:
        raise SystemExit(f"PNP_REPLAY_CAPACITY_BLOCKED: free={free}; reserve={RESERVE}")
    if (upstream/"lean-toolchain").read_text().strip() != PIN:
        raise SystemExit("PNP_REPLAY_TOOLCHAIN_PIN_MISMATCH")
    lean = (Path.home()/".elan/toolchains"/SLUG/"bin/lean").resolve(strict=True)
    version = subprocess.check_output([str(lean),"--version"],text=True,timeout=15).strip()
    if "version 4.35.0-rc3," not in version:
        raise SystemExit("PNP_REPLAY_TOOLCHAIN_VERSION_MISMATCH")
    manifest = upstream/"lake-manifest.json"
    data = json.loads(manifest.read_text())
    revisions = {}
    for pkg in data["packages"]:
        if pkg["type"] != "git":
            raise SystemExit("PNP_REPLAY_UNSUPPORTED_PACKAGE_SOURCE")
        name = pkg["name"].strip("«»")
        path = upstream/".lake/packages"/name
        rev = subprocess.check_output(["git","rev-parse","HEAD"],cwd=path,text=True,timeout=15).strip()
        if rev != pkg["rev"]:
            raise SystemExit(f"PNP_REPLAY_PACKAGE_PIN_MISMATCH: {name}")
        revisions[name] = rev
    required = [
        upstream/".lake/build/lib/lean/MIPRE/Foundations/SAT/FmlProg.olean",
        upstream/".lake/build/lib/lean/MIPRE/Foundations/Cost/BinaryCompare.olean",
    ]
    if not all(p.is_file() for p in required):
        raise SystemExit("PNP_REPLAY_DEPENDENCY_CACHE_INCOMPLETE")
    mounts = {}
    for p in (lean, upstream, output.parent):
        mounts[str(p)] = subprocess.check_output(
            ["findmnt","-T",str(p),"-n","-o","SOURCE,FSTYPE,TARGET"],
            text=True,timeout=10).strip()
    return lean, {"schema":"PNP_REPLAY_PLACEMENT/1","runner":"native-linux-direct",
                  "kernel":platform.release(),"mounts":mounts,"free_bytes":free,
                  "toolchain":version,"package_revisions":revisions,
                  "manifest_sha256":hashlib.sha256(manifest.read_bytes()).hexdigest()}

def bounded_run(cmd, *, cwd, env, log, receipt, seconds=240):
    """No unbounded dependency load; preserve exit and resource diagnostics."""
    start = time.monotonic()
    before = resource.getrusage(resource.RUSAGE_CHILDREN)
    outcome = "unknown"
    code = None
    try:
        with Path(log).open("w") as out:
            proc = subprocess.run(list(map(str,cmd)),cwd=cwd,env=env,stdout=out,
                                  stderr=subprocess.STDOUT,timeout=seconds)
        code = proc.returncode
        outcome = "passed" if code == 0 else "failed"
        proc.check_returncode()
    except subprocess.TimeoutExpired:
        outcome = "timeout"
        raise SystemExit(f"PNP_REPLAY_TIMEOUT: {Path(log).name}; {seconds}s; no automatic retry or HDD fallback")
    finally:
        after = resource.getrusage(resource.RUSAGE_CHILDREN)
        record = {"log":Path(log).name,"outcome":outcome,"exit_code":code,
                  "elapsed_seconds":round(time.monotonic()-start,3),
                  "major_faults":after.ru_majflt-before.ru_majflt,
                  "fs_input_blocks":after.ru_inblock-before.ru_inblock,
                  "timeout_seconds":seconds}
        with Path(receipt).open("a") as stream:
            stream.write(json.dumps(record,sort_keys=True)+"\n")
