# TCM Semiring-Contraction Route

## Role

This lane adds Tropical Contraction Machines as a MATHSOLVE route for finite proof obligations whose search space can be represented as a semiring tensor network.

Doctrine:

> Search tropical; certify in MATHCERT.

MATHSOLVE may discover witnesses, bounds, and artifacts. It does not own the final proof boundary.

## Fixture 006

Fixture 006 is the first certificate-interchange fixture for this lane.

```bash
python -m tcm_prover.fixtures.fixture006 --out artifacts/fixture006
python -m unittest discover tests -v
```

It emits:

```text
artifacts/fixture006/
├── fixture006_report.md
├── instance.opb
├── primal_witness.json
├── pb_dual_certificate.json
├── checker_transcript.txt
├── result_card.json
├── failure_mode_ledger.md
└── proof_import_stub.lean
```

The result card status is deliberately `artifact_emitted`. Certification requires a MATHCERT checker replay.

## Boundary

The TCM search trace is evidence. The OPB instance, primal witness, and dual certificate are the handoff. MATHCERT decides whether the handoff becomes a checked claim.
