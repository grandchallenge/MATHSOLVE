# MATHCERT Handoff

## Lean Package

- Toolchain: Lean `v4.29.1`
- Mathlib: `v4.29.1`
- Root module: `MATHCERT/MathCert.lean`
- CI: `MATHCERT/ci/check_lean.ps1` and `MATHCERT/ci/check_lean.sh`

## Formal Files

| File | Responsibility |
|---|---|
| `Basic.lean` | Family, union-closure, support, nontriviality, frequency |
| `Frequency.lean` | Support, nontriviality, top-union, and powerset lemmas |
| `FranklStatement.lean` | Abundance and the general statement scaffold |
| `SingletonCase.lean` | Singleton half bound and abundance witness |

## Exact Replay Boundary

`MATHCERT/ci/replay_certificates.py` independently recomputes the bounded audit,
checks the source-audit hash, and verifies zero nontrivial violations for
`n <= 4`. This is finite-domain certification, not a Lean theorem.

## Remaining Interface

Keep `Family α := Finset (Finset α)` stable. Add a translation layer only if
importing predicate-based external ideal-family work.
