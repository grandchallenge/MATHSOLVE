# PNP-ABOVE — content-addressed predecessor replay cache

## Purpose and trust boundary

PNP-CACHE-001 provides an opt-in local development accelerator for the complete,
verified original MIPRE WP08–WP23A chain. It does not change any existing
protected-admission replay script, Lean theorem, original source, or axiom audit.
It replaces 65 redundant DEVELOPMENT compiler invocations with a hash-validated
reuse operation. The original full source compilation remains mandatory to
admit every new protected mathematical candidate.

## Content address

A cache key is SHA-256 of canonical JSON recording:
- all 65 source SHA-256 digests and Git blobs, including the ten legacy
  source-locked WP08–WP17 modules and the 55 later modules;
- six exact WP18–WP23A source-lock manifest digests;
- the pinned original upstream Git revision
  5926bdff5db621f44682a101007ef2fe3ae8d970 and clean tracked tree;
- Lean toolchain, Lean version, installed Lean and Lake executable SHA-256;
- upstream lake-manifest.json and compiled MIPRE Verifier/Games/GameTransport
  dependency digests;
- compiler flags and cache format version.

It is intentionally independent of a *new* candidate SHA when all predecessor
sources stay exactly identical. Keys change on source, manifest, toolchain or
tracked imported interface drift.

The cache path is ~/.cache/gcl/pnp-source-replay/PNP-REPLAY-CACHE-1/HASH.
Seed is atomic under an OS file lock. Entry files are non-world-writable and
written read-only. On every lookup, the tool checks input identity, owner,
directory security, module inventory and all 130 source/object file SHA-256
digests; missing, symlinked, stale or altered files fail closed. Restore
refuses an existing output directory and verifies every copied output digest.

This is OS-account-local evidence. A same-operator cache is NOT an
independently signed compiler attestation, immutable third-party certificate,
or substitute for source replay. No cache status can authorize certification,
source-semantic claim promotion, or a protected merge.

## Commands

Set U to the pinned original MIPRE checkout, G to the current exact
MATHSOLVE checkout, and P to G/research/PNP-ABOVE.

Seed, using a recorded full replay with exact-head, audit, terminal, status
and exit-code evidence (this prior replay is already protected admitted):

    python3 "$P/PNP_REPLAY_CACHE.py" seed --upstream "$U" --gcl "$G" \
      --full-replay /tmp/gcl-pnp-wp23a-exact-ebb9a2a-replay

Inspect and verify a key, without compiling source:

    python3 "$P/PNP_REPLAY_CACHE.py" key --upstream "$U" --gcl "$G"
    python3 "$P/PNP_REPLAY_CACHE.py" check --upstream "$U" --gcl "$G"

Compile a NEW proof file with the old verified proof objects:

    bash "$P/PNP_WARM_REPLAY.sh" "$U" "$G" \
      /tmp/new-development-work /path/to/NewLeanProof.lean

The new output directory must not exist. A cold cache returns exit code 3,
not success. An explicit PNP_REPLAY_ADMISSION=1 refuses cached reuse.

At protected admission, use the relevant original full replay script such
as WP23A_REPLAY.sh; a future WP23B_REPLAY.sh must recursively invoke it,
bind the exact new source commit and independently audit all new declarations.
Cached output is not a passing protected-admission replay.

## Measured acceptance checks (CHAD, 19 November 2026)

The full WP23A precedent recompiled 65 Lean source modules and audited the
original six source-locked stages, before its protected merge.

- Warm cache restore: 0.42 seconds, 65 source and 65 compiled modules.
- Separate new Lean module import and theorem check: 10.36 seconds.
- Second full warm-wrapper execution with newly proved theorem: 11.50 seconds.
- Cached predecessor footprint: about 32 MB.
- Sixteen Python unit/hostile mutation tests: PASS (5.33 seconds total).
- Explicit admission-mode refusal: PASS.
- Fresh Lean #print axioms for new proof after restore: standard axioms only.

These are local observed timings, not controlled cross-hardware benchmarks.
The fast path avoids repeated *development* compilation while keeping the
full 65-module verification and protected checks intact for final admission.

A future remote/shared cache would require a separate signature and
supply-chain governance protocol; it is not implemented or implied here.
