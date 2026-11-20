# PNP-ABOVE — content-addressed predecessor replay cache

## Purpose and trust boundary

PNP-CACHE-001 provides an opt-in local development accelerator for the complete,
verified original MIPRE WP08–WP23A or WP08–WP23B chains. It does not change any existing
protected-admission replay script, Lean theorem, original source, or axiom audit.
It replaces 65 or 70 redundant DEVELOPMENT compiler invocations with a hash-validated
reuse operation. The original full source compilation remains mandatory to
admit every new protected mathematical candidate.

## Content address

A cache key is SHA-256 of canonical JSON recording:
- the selected admitted predecessor stage, WP23A or WP23B;
- all 65 or 70 source SHA-256 digests and Git blobs, including the ten legacy
  source-locked WP08–WP17 modules;
- six or seven stage-specific source-lock manifest digests;
- the pinned original upstream Git revision
  5926bdff5db621f44682a101007ef2fe3ae8d970 and clean tracked tree;
- Lean toolchain, Lean version, installed Lean and Lake executable SHA-256;
- upstream lake-manifest.json and compiled MIPRE Verifier/Games/GameTransport
  dependency digests (also the original Cook–Levin and SAT imports for WP23B);
- compiler flags and cache format version.

It is intentionally independent of a *new* candidate SHA when all predecessor
sources stay exactly identical. Keys change on source, manifest, toolchain or
tracked imported interface drift.

The cache path is ~/.cache/gcl/pnp-source-replay/PNP-REPLAY-CACHE-1/HASH.
Seed is atomic under an OS file lock. Entry files are non-world-writable and
written read-only. On every lookup, the tool checks input identity, owner,
directory security, module inventory and all 130 or 140 source/object file SHA-256
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

For the protected-admitted WP23B predecessor (70 modules), explicitly
select WP23B; the legacy WP23A stage and original cache key remain stable:

    python3 "$P/PNP_REPLAY_CACHE.py" seed --stage WP23B --upstream "$U" --gcl "$G" --full-replay /tmp/gcl-pnp-wp23b-exact-77b0298-replay
    PNP_REPLAY_STAGE=WP23B bash "$P/PNP_WARM_REPLAY.sh" "$U" "$G" /tmp/new-wp23c-dev /path/to/WP23C_NewProof.lean

A stage is recognized only after its full uncached predecessor replay
and exact source-lock/AxiomAudit evidence have been admitted. Unknown stage
names fail closed. The cache is a local proof-development accelerator only.

At protected admission, use the relevant original full replay script such
as WP23A_REPLAY.sh or WP23B_REPLAY.sh; every new stage must recursively invoke its admitted predecessor,
bind the exact new source commit and independently audit all new declarations.
Cached output is not a passing protected-admission replay.

## Measured acceptance checks (CHAD, 19 November 2026)

The full WP23A precedent recompiled 65 Lean source modules and audited the
original six source-locked stages, before its protected merge.

- Warm cache restore: 0.42 seconds, 65 source and 65 compiled modules.
- Separate new Lean module import and theorem check: 10.36 seconds.
- Second full warm-wrapper execution with newly proved theorem: 11.50 seconds.
- Cached predecessor footprint: about 32 MB.
- Eighteen Python unit/hostile mutation tests: PASS (5.33 seconds total).
- Explicit admission-mode refusal: PASS.
- Fresh Lean #print axioms for new proof after restore: standard axioms only.

These are local observed timings, not controlled cross-hardware benchmarks.
The fast path avoids repeated *development* compilation while keeping
independent full-source verification and protected checks intact for admission.

## Stage-aware follow-up acceptance (19 November 2026)

With WP23B protected-admitted at MATHSOLVE
28a710900ed8217769c5bed95492e7efd2cbe779, an uncached exact-head
WP08–WP23B replay passed (70 Lean modules, 20 new theorem axioms).
The stage-aware cache preserves the old WP23A key
586f6a307c0e0df0eeae6eb38f23240b5623e75f8ba7862355f115a52f7e607a.
It seeds an independent WP23B entry with key
e5969f09416e8d88918a203339f7258a8708bf274df9a9058433999b5989aced.

- **26** unit, adversarial and stage-isolation tests: PASS (5.1 s).
- WP23B cache integrity: PASS, **70** source and compiled objects.
- New Lean module importing actual original WP23B succinct Cook–Levin theorem:
  compiled after warm restore in **6 s** (local observation).
- Wrong-stage replay / altered source, toolchain or imported Cook–Levin
  object / unknown future stage: rejected or assigned distinct keys.
- The prior WP23A object is still valid at its exact old key.
- Cached proof objects remain **development-only**: an independent complete
  source replay and axiom audit are still required at protected admission.

A future remote/shared cache would require a separate signature and
supply-chain governance protocol; it is not implemented or implied here.
