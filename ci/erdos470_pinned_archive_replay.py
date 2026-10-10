#!/usr/bin/env python3
"""Independent, read-only verification of a pinned odd-weird archive inventory.

Checks archive custody and record interface, NOT algorithmic completeness or
absence of odd weird numbers. Never executes the archived candidate binary.
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import json
import subprocess
import tarfile
from pathlib import Path

SOURCE_SHA = "88d22faf46400f0050287c3c32c9a807ca3b1340"
EXPECTED_MANIFEST_SHA = "7d3a427a2f2f0cfea706e8ca2eceeef99f94efb9470c0d2c995dcc0f8554c4df"


def verify(root: Path) -> dict:
    def git(*args: str) -> str:
        return subprocess.check_output(["git", *args], cwd=root).decode().strip()
    head = git("rev-parse", "HEAD")
    if head != SOURCE_SHA:
        raise ValueError(f"wrong upstream source head: {head}")

    archives = sorted((root / "data-1e21").glob("*.tar.gz"))
    if len(archives) != 183:
        raise ValueError(f"archive count mismatch: {len(archives)}")

    manifest = []
    header_counts = collections.Counter()
    markers = collections.Counter()
    bound_pairs = collections.Counter()
    member_hashes = set()
    total_members = 0
    total_uncompressed = 0
    for archive in archives:
        relative = archive.relative_to(root).as_posix()
        compressed = archive.read_bytes()
        blob = hashlib.sha1(b"blob " + str(len(compressed)).encode()
                            + bytes([0]) + compressed).hexdigest()
        if blob != git("rev-parse", "HEAD:" + relative):
            raise ValueError(f"Git blob mismatch: {relative}")
        manifest.append({
            "path": relative,
            "bytes": len(compressed),
            "git_blob_sha1": blob,
            "sha256": hashlib.sha256(compressed).hexdigest(),
        })
        with tarfile.open(archive, mode="r|gz") as tf:
            for member in tf:
                if not member.isfile():
                    continue
                # Bounded read prevents a corrupt or hostile archive entry
                # from consuming unbounded memory in this diagnostic.
                if member.size > 1024 * 1024:
                    raise ValueError(f"oversized member: {relative}")
                stream = tf.extractfile(member)
                if stream is None:
                    raise ValueError(f"unreadable member: {relative}")
                raw = stream.read(1024 * 1024 + 1)
                if len(raw) != member.size:
                    raise ValueError(f"member length mismatch: {relative}")
                total_uncompressed += len(raw)
                if total_uncompressed > 2 * 1024**3:
                    raise ValueError("decompressed archive exceeds 2 GiB budget")
                rows = raw.decode("ascii").splitlines()
                if len(rows) < 4:
                    raise ValueError("incomplete historical workunit")
                k = next((i for i, line in enumerate(rows)
                          if len(line.split()) == 3), len(rows)-1)
                total_members += 1
                header_counts[k] += 1
                markers[rows[-1]] += 1
                bound_pairs[rows[0]+":"+rows[1]] += 1
                member_hashes.add(hashlib.sha256(raw).hexdigest())

    canonical = json.dumps(manifest, sort_keys=True, separators=(",", ":")).encode()
    digest = hashlib.sha256(canonical).hexdigest()
    if digest != EXPECTED_MANIFEST_SHA:
        raise ValueError(f"archive manifest digest mismatch: {digest}")
    expected = {
        "archive_count": 183,
        "record_count": 527827,
        "compressed_bytes": 36601131,
        "seven_scalar_headers": 527827,
        "t_markers": 485384,
        "c_markers": 42443,
        "distinct_member_payload_hashes": 518414,
    }
    actual = {
        "archive_count": len(archives),
        "record_count": total_members,
        "compressed_bytes": sum(item["bytes"] for item in manifest),
        "seven_scalar_headers": header_counts[7],
        "t_markers": markers["t"],
        "c_markers": markers["c"],
        "distinct_member_payload_hashes": len(member_hashes),
    }
    if actual != expected or sum(markers.values()) != total_members:
        raise ValueError(f"archive metrics differ: {actual}")

    return {
        "record_type": "GCL_ERDOS470_PINNED_ARCHIVE_REPLAY",
        "source_commit": head,
        "archive_manifest_sha256": digest,
        "archive_inventory": actual,
        "historical_executable_replayed": False,
        "historical_full_cover_verified": False,
        "six_prime_factor_theorem_verified": False,
        "odd_weird_exclusion_below_1e21_certified": False,
    }


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--checkout", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()
    report = verify(args.checkout)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    print("PASS: pinned archive count, hashes, record headers and terminal markers")
