#!/usr/bin/env python3
"""Content-addressed local predecessor build cache. NEVER proof/admission authority.

Only fully recompiled, source-locked predecessors can seed a cache. Cache hits
check every input and output digest; restored .olean files may be used for
development elaboration, not substituted for full protected-admission replay.
"""
from __future__ import annotations

import argparse
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import stat
import subprocess
import sys
import tempfile

UPSTREAM_SHA = "5926bdff5db621f44682a101007ef2fe3ae8d970"
STAGES = {"WP18": 19, "WP19": 27, "WP20": 44, "WP21": 54, "WP22": 63, "WP23A": 65, "WP23B": 70}
STAGE_MANIFESTS = ("WP18", "WP19", "WP20", "WP21", "WP22", "WP23A", "WP23B")
TERMINAL_STATUS = {
    "WP23A": "WP23A_FIXED_GAME_INVARIANCE_AND_NO_COMPRESSION_SOUNDNESS_PREMISE_PROVED",
    "WP23B": "WP23B_EXACT_SOURCE_NATIVE_SUCCINCT_SAT_MASK__SAT_HARDNESS_TRANSFER_OPEN",
}


def predecessor_stages(stage: str) -> tuple[str, ...]:
    require(stage in TERMINAL_STATUS, f"UNSUPPORTED_ADMITTED_STAGE: {stage}")
    return STAGE_MANIFESTS[:STAGE_MANIFESTS.index(stage) + 1]


def axiom_log(stage: str) -> str:
    return "WP23_AxiomAudit.log" if stage == "WP23A" else f"{stage}_AxiomAudit.log"
FLAGS = ["LEAN_NUM_THREADS=1", "lake env lean -R WORK -o WORK/PNPAbove/MOD.olean WORK/PNPAbove/MOD.lean"]
FORMAT = "PNP-REPLAY-CACHE/1"


class Invalid(ValueError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise Invalid(message)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def digest_file(path: Path) -> str:
    return sha(path.read_bytes())


def git_blob(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def command(*args: str, cwd: Path | None = None) -> str:
    return subprocess.check_output(args, cwd=cwd, stderr=subprocess.PIPE, text=True).strip()


def strict_file(path: Path) -> bytes:
    require(path.is_file() and not path.is_symlink(), f"FILE_MISSING_OR_SYMLINK: {path}")
    return path.read_bytes()


def source_catalog(gcl: Path, stage: str = "WP23A") -> dict[str, dict[str, str]]:
    root = gcl / "research/PNP-ABOVE"
    old_replay = strict_file(root / "WP18_REPLAY.sh").decode()
    old = re.findall(r"^check_old\s+(\d{2})\s+(\S+\.lean)\s+([a-f0-9]{40})\s*$", old_replay, re.M)
    require(len(old) == 10, "LEGACY_BLOB_MAPPING_DRIFT")
    result: dict[str, dict[str, str]] = {}

    def add(module: str, path: Path, expected_blob: str, expected_sha: str | None = None) -> None:
        require(re.fullmatch(r"WP\d{2}[A-Za-z0-9]*\.lean", module) is not None,
                "BAD_MODULE_NAME")
        require(module not in result, f"DUPLICATE_MODULE: {module}")
        require(path.parent == root, "SOURCE_PATH_OUTSIDE_LOCKED_DIRECTORY")
        data = strict_file(path)
        require(git_blob(data) == expected_blob, f"ORIGINAL_SOURCE_BLOB_DRIFT: {module}")
        if expected_sha:
            require(sha(data) == expected_sha, f"ORIGINAL_SOURCE_SHA_DRIFT: {module}")
        result[module] = {"sha256": sha(data), "git_blob": expected_blob}

    for num, filename, blob in old:
        add(f"WP{num}.lean", root / filename, blob)
    for prefix in predecessor_stages(stage):
        manifest = json.loads(strict_file(root / f"{prefix}_SOURCE_LOCK.json"))
        for module, record in manifest["modules"].items():
            rel = Path(record["path"])
            require(rel.parent == Path("research/PNP-ABOVE"), "MANIFEST_PATH_ESCAPE")
            add(module, gcl / rel, record["git_blob"], record["sha256"])
    require(len(result) == STAGES[stage], f"MODULE_COUNT_DRIFT: {len(result)}")
    return dict(sorted(result.items()))


def environment(upstream: Path, stage: str = "WP23A") -> dict[str, str]:
    require(command("git", "rev-parse", "HEAD", cwd=upstream) == UPSTREAM_SHA,
            "ORIGINAL_UPSTREAM_REVISION_DRIFT")
    require(not command("git", "status", "--porcelain", "--untracked-files=no", cwd=upstream),
            "TRACKED_UPSTREAM_SOURCE_DIRTY")
    toolchain = strict_file(upstream / "lean-toolchain").decode().strip()
    prefix = Path(command("lean", "--print-prefix", cwd=upstream))
    lean = prefix / "bin/lean"
    lake = prefix / "bin/lake"
    require(lean.is_file() and lake.is_file(), "TOOLCHAIN_EXECUTABLE_MISSING")
    deps = {}
    import_deps = ("lake-manifest.json", "lean-toolchain",
                   ".lake/build/lib/lean/MIPRE/Foundations/Verifier.olean",
                   ".lake/build/lib/lean/MIPRE/Foundations/Games.olean",
                   ".lake/build/lib/lean/MIPRE/Foundations/GameTransport.olean")
    if stage == "WP23B":
        # WP23B adds these two original MIPRE import dependencies.
        import_deps += (".lake/build/lib/lean/MIPRE/Foundations/SAT/Succinct.olean",
                        ".lake/build/lib/lean/MIPRE/TM/CookLevin/Assemble.olean")
    for rel in import_deps:
        deps[rel] = digest_file(upstream / rel)
    return {"upstream_sha": UPSTREAM_SHA, "toolchain": toolchain,
            "lean_version": command("lean", "--version", cwd=upstream),
            "lean_executable_sha256": digest_file(lean),
            "lake_executable_sha256": digest_file(lake),
            "toolchain_prefix": str(prefix), "import_dependencies": deps}


def inputs(upstream: Path, gcl: Path, stage: str = "WP23A") -> tuple[str, dict]:
    catalog = source_catalog(gcl, stage)
    env = environment(upstream, stage)
    source_root = gcl / "research/PNP-ABOVE"
    manifests = {name: digest_file(source_root / f"{name}_SOURCE_LOCK.json")
                 for name in predecessor_stages(stage)}
    data = {"format": FORMAT, "stage": stage, "compiler_flags": FLAGS,
            "environment": env, "manifests": manifests, "source": catalog}
    key = sha(json.dumps(data, sort_keys=True, separators=(",", ":")).encode())
    return key, data


def check_replay(full: Path, gcl: Path, catalog: dict,
                 stage: str = "WP23A") -> dict:
    require(stage in TERMINAL_STATUS, "UNSUPPORTED_ADMITTED_STAGE")
    status = strict_file(full / "status.txt").decode().strip()
    require(status == TERMINAL_STATUS[stage], "FULL_REPLAY_FINAL_STATUS_ABSENT")
    full_log = full.with_suffix(".log")
    exit_file = full.with_suffix(".exit")
    require(strict_file(exit_file).strip() == b"0", "FULL_REPLAY_EXIT_NOT_ZERO")
    log = strict_file(full_log).decode()
    require(log.rstrip().endswith(TERMINAL_STATUS[stage]), "FULL_REPLAY_LOG_TERMINAL_MISSING")
    for prefix in predecessor_stages(stage):
        lock_marker = ("WP18_NEW_SOURCE_LOCK_PASS" if prefix == "WP18"
                       else f"{prefix}_SOURCE_LOCK_PASS")
        for marker in (f"{prefix}_STANDARD_AXIOMS_ONLY_PASS", lock_marker):
            require(marker in log, f"FULL_REPLAY_AUDIT_MISSING: {marker}")
    lock = strict_file(full / "lock.txt").decode()
    found = re.findall(rf"^{stage}_CANDIDATE=([a-f0-9]{{40}})$", lock, re.M)
    require(len(found) == 1, "FULL_REPLAY_CANDIDATE_MISSING_OR_AMBIGUOUS")
    exact = found[0]
    current = command("git", "rev-parse", "HEAD", cwd=gcl)
    require(subprocess.run(["git", "merge-base", "--is-ancestor", exact, current],
                           cwd=gcl, check=False).returncode == 0,
            "FULL_REPLAY_HEAD_NOT_IN_CURRENT_ANCESTRY")
    # The original candidate can be merged into a protected main; its
    # exact proof bytes must nevertheless match ALL current input locks.
    for name in catalog:
        require(f"CHECKING_ORIGINAL_SOURCE_{name[:-5]}" in log,
                f"FULL_REPLAY_MODULE_MISSING: {name}")
    for name in predecessor_stages(stage):
        require(len(strict_file(full / axiom_log(name))) > 30,
                f"AXIOM_LOG_MISSING: {name}")
    return {"full_replay_candidate": exact, "full_log_sha256": digest_file(full_log),
            "full_lock_sha256": digest_file(full / "lock.txt"),
            "full_status_sha256": digest_file(full / "status.txt"),
            "full_axiom_logs_sha256": {
                n: digest_file(full / axiom_log(n))
                for n in predecessor_stages(stage)}}


def cache_entry(cache_root: Path, key: str) -> Path:
    require(re.fullmatch(r"[a-f0-9]{64}", key) is not None, "INVALID_CACHE_KEY")
    return cache_root / FORMAT.replace("/", "-") / key


def safe_directory(path: Path) -> None:
    require(not path.is_symlink() and path.is_dir(), f"UNSAFE_DIRECTORY: {path}")
    require(path.stat().st_uid == os.getuid(), f"CACHE_OWNER_MISMATCH: {path}")
    require(not (path.stat().st_mode & (stat.S_IRWXG | stat.S_IRWXO)),
            f"CACHE_DIRECTORY_NOT_OWNER_ONLY: {path}")


def verify_entry(entry: Path, key: str, expected_inputs: dict) -> dict:
    safe_directory(entry)
    safe_directory(entry / "PNPAbove")
    metadata = json.loads(strict_cache_file(entry / "metadata.json"))
    require(metadata["format"] == FORMAT and metadata["key"] == key,
            "CACHE_ENTRY_IDENTITY_MISMATCH")
    require(metadata["inputs"] == expected_inputs, "CACHE_ENTRY_INPUTS_MISMATCH")
    for name, files in metadata["payload"].items():
        require(name in expected_inputs["source"], "CACHE_UNEXPECTED_MODULE")
        require(set(files) == {"lean", "olean"}, "CACHE_PAYLOAD_SCHEMA_DRIFT")
        for ext in ("lean", "olean"):
            rel = Path(f"PNPAbove/{name[:-5]}.{ext}")
            actual = sha(strict_cache_file(entry / rel))
            require(actual == files[ext], f"CACHE_PAYLOAD_CORRUPT: {rel}")
        require(files["lean"] == expected_inputs["source"][name]["sha256"],
                f"CACHE_STAGED_SOURCE_MISMATCH: {name}")
    require(set(metadata["payload"]) == set(expected_inputs["source"]),
            "CACHE_INCOMPLETE_MODULE_INVENTORY")
    return metadata


def strict_cache_file(path: Path) -> bytes:
    data = strict_file(path)
    require(path.stat().st_uid == os.getuid(), f"CACHE_FILE_OWNER_MISMATCH: {path}")
    require(not (path.stat().st_mode & (stat.S_IRWXG | stat.S_IRWXO)),
            f"CACHE_FILE_NOT_OWNER_ONLY: {path}")
    return data


def publish_seed(root: Path, entry: Path, key: str, data: dict, full: Path,
                 gcl: Path) -> dict:
    evidence = check_replay(full, gcl, data["source"], data["stage"])
    safe_directory(root)
    group = entry.parent
    group.mkdir(mode=0o700, exist_ok=True)
    safe_directory(group)
    lockfile = group / ".seed.lock"
    with lockfile.open("a+b") as lock:
        fcntl.flock(lock.fileno(), fcntl.LOCK_EX)
        if entry.exists() or entry.is_symlink():
            return verify_entry(entry, key, data)
        scratch = Path(tempfile.mkdtemp(prefix=".build-", dir=group))
        try:
            (scratch / "PNPAbove").mkdir(mode=0o700)
            payload = {}
            for name in data["source"]:
                stem = name.removesuffix(".lean")
                hashes = {}
                for ext in ("lean", "olean"):
                    src = full / "PNPAbove" / f"{stem}.{ext}"
                    content = strict_file(src)
                    dst = scratch / "PNPAbove" / f"{stem}.{ext}"
                    dst.write_bytes(content)
                    os.chmod(dst, 0o400)
                    hashes[ext] = sha(content)
                require(hashes["lean"] == data["source"][name]["sha256"],
                        f"REPLAY_SOURCE_DIFFERS_FROM_CURRENT_LOCK: {name}")
                payload[name] = hashes
            metadata = {"format": FORMAT, "key": key, "inputs": data,
                        "payload": payload, "evidence": evidence,
                        "trust": "OS_ACCOUNT_ONLY_CACHED_DEVELOPMENT_NOT_PROOF"}
            (scratch / "metadata.json").write_text(
                json.dumps(metadata, indent=2, sort_keys=True) + "\n")
            os.chmod(scratch / "metadata.json", 0o400)
            os.chmod(scratch / "PNPAbove", 0o500)
            os.chmod(scratch, 0o500)
            os.rename(scratch, entry)
        finally:
            if scratch.exists():
                shutil.rmtree(scratch)
        return verify_entry(entry, key, data)


def restore(entry: Path, key: str, data: dict, work: Path) -> dict:
    require(not work.exists() and not work.is_symlink(),
            "RESTORE_DESTINATION_ALREADY_EXISTS")
    metadata = verify_entry(entry, key, data)
    work.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=".restore-", dir=work.parent))
    try:
        target = staging / "PNPAbove"
        target.mkdir()
        for name in metadata["payload"]:
            stem = name.removesuffix(".lean")
            for ext in ("lean", "olean"):
                src = entry / "PNPAbove" / f"{stem}.{ext}"
                shutil.copyfile(src, target / src.name, follow_symlinks=False)
                os.chmod(target / src.name, 0o600)
        receipt = {"format": "PNP-REPLAY-CACHED-DEV-ONLY/1",
                   "key": key, "cache_metadata_sha256": digest_file(entry / "metadata.json"),
                   "source_gcl_head": None, "full_replay_evidence": metadata["evidence"],
                   "admission_eligible": False,
                   "not_proof": "A cache hit is NOT full source compilation or certification."}
        (staging / "cache_dev_receipt.json").write_text(
            json.dumps(receipt, indent=2, sort_keys=True) + "\n")
        os.chmod(staging / "cache_dev_receipt.json", 0o600)
        # Re-hash the bytes after copying. A stale or concurrently damaged
        # source cannot silently pass even if it was sound during lookup.
        for name, files in metadata["payload"].items():
            stem = name.removesuffix(".lean")
            for ext in ("lean", "olean"):
                path = target / f"{stem}.{ext}"
                require(digest_file(path) == files[ext],
                        f"CACHE_RESTORE_COPY_CORRUPT: {name}.{ext}")
        os.rename(staging, work)
    finally:
        if staging.exists():
            shutil.rmtree(staging)
    return metadata


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("key", "seed", "check", "restore"))
    parser.add_argument("--stage", choices=tuple(TERMINAL_STATUS), default="WP23A",
                        help="Exact admitted predecessor stage; WP23A remains the legacy default")
    parser.add_argument("--upstream", required=True, type=Path)
    parser.add_argument("--gcl", required=True, type=Path)
    parser.add_argument("--cache-root", type=Path,
                        default=Path.home() / ".cache/gcl/pnp-source-replay")
    parser.add_argument("--full-replay", type=Path)
    parser.add_argument("--work", type=Path)
    args = parser.parse_args()
    require(os.environ.get("PNP_REPLAY_ADMISSION") != "1" or args.action == "key",
            "ADMISSION_MUST_USE_UNCACHED_FULL_REPLAY")
    upstream, gcl = args.upstream.resolve(), args.gcl.resolve()
    key, data = inputs(upstream, gcl, args.stage)
    if args.action == "key":
        print(f"PNP_CONTENT_ADDRESS_KEY={key}")
        return 0
    root = args.cache_root.expanduser().absolute()
    root.mkdir(parents=True, exist_ok=True, mode=0o700)
    safe_directory(root)
    entry = cache_entry(root, key)
    if args.action == "seed":
        require(args.full_replay is not None, "SEED_REQUIRES_FULL_REPLAY")
        metadata = publish_seed(root, entry, key, data,
                                args.full_replay.absolute(), gcl)
        print(f"PNP_VERIFIED_PREDECESSOR_SEEDED key={key} "
              f"modules={len(metadata['payload'])} "
              "TRUST=OS_ACCOUNT_ONLY_NOT_ADMISSION")
        return 0
    if not entry.exists():
        print(f"PNP_CACHE_MISS key={key}", file=sys.stderr)
        return 3
    if args.action == "check":
        metadata = verify_entry(entry, key, data)
        print(f"PNP_CACHE_INTEGRITY_PASS key={key} modules={len(metadata['payload'])} "
              "ADMISSION_ELIGIBLE=false")
        return 0
    require(args.work is not None, "RESTORE_REQUIRES_WORK")
    metadata = restore(entry, key, data, args.work.absolute())
    print(f"PNP_CACHED_PREDECESSOR_RESTORED key={key} modules={len(metadata['payload'])} "
          "DEVELOPMENT_ONLY_NOT_FULL_REPLAY")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (Invalid, OSError, KeyError, json.JSONDecodeError, subprocess.CalledProcessError) as exc:
        print(f"PNP_CACHE_FAIL_CLOSED {type(exc).__name__}: {exc}", file=sys.stderr)
        sys.exit(65)
