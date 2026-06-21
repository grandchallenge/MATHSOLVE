# MATHCERT Handoff

## Trusted Boundary

The trusted boundary is MATHCERT, not the upstream source repository and not
this exposition package.

Primary MATHCERT files:

- `MATHCERT/MathCert/Domains/UnionClosed/IdealFamilyPort/Core.lean`
- `MATHCERT/MathCert/Domains/UnionClosed/IdealFamilyPort/FranklRare.lean`
- `MATHCERT/MathCert/Domains/UnionClosed/IdealFamilyPort.lean`
- `MATHCERT/MathCert/Domains/UnionClosed/IdealFamilyBridge.lean`
- `MATHCERT/MathCert/Domains/UnionClosed/IdealFamilyNDS.lean`
- `MATHCERT/MathCert/Domains/UnionClosed/IdealFamilyTrace.lean`
- `MATHCERT/MathCert/Domains/UnionClosed/IdealFamilyContraction.lean`
- `MATHCERT/MathCert/Domains/UnionClosed/IdealFamilyNDSDiff.lean`
- `MATHCERT/MathCert/Domains/UnionClosed/IdealFamilyNDSEndgame.lean`
- `MATHCERT/MathCert/Domains/UnionClosed/IdealFamilyDuality.lean`

Primary ledger:

- `MATHCERT/claim_ledger_ideal_family_bridge.yaml`

Primary closeout docs:

- `MATHCERT/docs/ideal_family_bridge_phase_closeout.md`
- `MATHCERT/docs/ideal_family_nds_gap_assessment.md`

## Verification Commands

Run from `MATHCERT`:

```powershell
.\ci\check_lean.ps1
```

Expected gate components:

- Lean build succeeds;
- ledgers validate;
- malformed-ledger rejection tests pass;
- exact certificate replays pass;
- proof-placeholder scan finds no unregistered placeholders.

Run from `MATHSOLVE`:

```powershell
python ci/validate_solve.py
```

## Handoff Notes

The public representation remains:

```lean
Family alpha := Finset (Finset alpha)
```

Any future package consuming WP06 should depend on the checked theorem names,
not on the upstream audit files.

The upstream files remain useful for source comparison and historical
provenance. They are not a Lake dependency and they are not a certification
boundary.

