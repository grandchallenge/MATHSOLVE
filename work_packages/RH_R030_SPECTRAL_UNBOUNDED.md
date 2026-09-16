# RH-R030-SPECTRAL-UNBOUNDED-001 — Bounded-spectrum obstruction for Hilbert–Pólya candidates

- Campaign: `RH-001`
- Solve tracker: `grandchallenge/MATHSOLVE#257`
- Selected restricted target: `RH-R030-SPECTRAL-UNBOUNDED-001`
- Terminal target: `RH-T-000` — OPEN
- Parent theorem-graph nodes: `RH-T-030`, `RH-T-200`
- Protected prior-art audit: `grandchallenge/MATHFORGE@da746ee38823e408321b9e417649f5b837ec5627`, `reports/discovery/rh_001/rh_d009_r030_prior_art.md`
- MATHCERT state: `qualified_interface_only`; this package is not a certification disposition
- Novelty / priority claim: none

## 1. Selection decision

`RH-R030` is selected as a spectral-route necessary-condition theorem rather than as an RH-equivalent reformulation.

The selection follows the protected `RH-D-009` audit. Four route families were compared:

| Candidate family | WP02 parent | Decision | Reason |
| --- | --- | --- | --- |
| bounded spectral no-go | `RH-T-030` + `RH-T-200` | **selected** | exact theorem, no RH assumption, source-current, immediate proof path |
| Nyman–Beurling approximation | `RH-T-120` | deferred | August 2026 source frontier changed after WP02; `RH-D-003` also remains |
| Li positivity | `RH-T-110` | not selected | finite prefixes are weak; a full tail mechanism risks collapsing to the exact RH equivalence |
| zero-density / prime-error transport | `RH-T-050` + `RH-T-100` | deferred | 2025–2026 literature directly occupies the proposed bridge shape |

The selected route creates information even though it does not approach `RH-T-000` by itself: it removes the entire bounded-operator class from exact Hilbert–Pólya constructions and makes unbounded-domain analysis a mandatory future obligation.

## 2. Exact theorem statement

Define the positive ordinate set

\[
\Gamma_+ := \{\gamma>0 : \exists\,\beta\in(0,1),\;\zeta(\beta+i\gamma)=0\},
\]

with the protected classical zeta normalization and nontrivial-zero taxonomy.

### Theorem `RH-R030-SPECTRAL-UNBOUNDED-001`

Let `X` be a complex Banach space and let `A : X -> X` be a bounded linear operator. It is impossible that

\[
\Gamma_+ \subseteq \sigma(A).
\]

Consequently, no bounded self-adjoint operator on a complex Hilbert space can have spectrum containing every positive ordinate of a nontrivial zero of the Riemann zeta function. Any exact Hilbert–Pólya operator satisfying the protected ordinate-spectrum contract must be unbounded.

The theorem is deliberately stated with spectral **containment** rather than equality. This is stronger as a no-go statement: boundedness already fails before completeness, multiplicity matching, absence of extraneous spectrum, or self-adjointness are considered.

## 3. Selection-contract fields

1. **Exact theorem statement:** Section 2.
2. **Exact theorem-ledger parent:** `RH-T-030` and `RH-T-200`.
3. **Exact source/prior-art frontier:** protected Forge audit `da746ee38823e408321b9e417649f5b837ec5627`; the route also consumes the classical Riemann–von Mangoldt theorem and the standard Banach-algebra bounded-spectrum theorem.
4. **Already known:** nontrivial zero ordinates are unbounded; bounded-operator spectra are bounded. The package claims no novelty for either fact or their elementary composition.
5. **Single missing theorem:** the explicit governed composition from the zero-counting interface to the Hilbert–Pólya operator contract, with the claim boundary fixed.
6. **Why it advances the graph:** it turns `RH-T-030` into a necessary analytic property of every `RH-T-200` candidate and eliminates bounded candidates before expensive spectral matching.
7. **Why strictly narrower than RH:** it proves only that one operator class cannot realize the complete ordinate spectrum. It makes no assertion about real parts of zeros.
8. **Already equivalent to RH?:** no. The theorem is unconditional and remains true whether RH is true or false.
9. **Barrier profile:** classical zero counting + elementary spectral radius bound; no limiting exchange, positivity, or completeness assumption.
10. **False-proof fixtures:** `RH-F003`, `RH-F010`, `RH-F011` are active. Symmetry is not location; symmetry is not self-adjointness; partial or projected spectral data are not exact spectral correspondence.
11. **Smallest falsifying example/test:** a bounded operator whose spectrum contains real numbers of arbitrarily large absolute value. The bounded-spectrum theorem excludes such an example.
12. **Proof modality:** continuum analytic number theory plus functional analysis.
13. **Formal/computational support:** Lean checks the abstract spectral contradiction once unbounded ordinates are supplied; no broad numerical computation is used.
14. **Assumptions:** standard classical zeta continuation and zero-counting theorem; standard bounded-operator spectrum in a complex Banach algebra.
15. **Normalization:** spectral values are the raw real ordinates `gamma = Im(rho)`, not `1/(rho(1-rho))`, `rho(1-rho)`, a bounded transform, or a sampled finite list.
16. **Claim non-implications:** Section 7.
17. **Certification route if successful:** a later MATHCERT bounded theorem route may replay the exact Lean composition and specialist-check the imported Riemann–von Mangoldt theorem; the present package does not invoke Cert.

## 4. Proof-obligation DAG

```text
RH-P030-01  Riemann–von Mangoldt zero count implies Γ+ is unbounded above
      |
      v
RH-P030-03  choose γ in Γ+ with γ > ||A||
      ^
      |
RH-P030-02  if λ ∈ σ(A) for bounded A, then |λ| <= ||A||
      |
      v
RH-P030-04  γ ∈ σ(A) gives γ <= ||A||, contradiction
      |
      v
RH-P030-05  bounded exact ordinate-spectrum operator class eliminated
```

Status:

- `RH-P030-01`: discharged by the classical `RH-T-030` zero-counting interface.
- `RH-P030-02`: discharged by the standard Banach-algebra spectrum theorem; Mathlib theorem `spectrum.norm_le_norm_of_mem` is used in the formal composition.
- `RH-P030-03`: discharged.
- `RH-P030-04`: discharged and kernel-checkable in `MathSolve/RH/SpectralUnbounded.lean`.
- `RH-P030-05`: discharged.

## 5. Substantive proof

Let `A` be bounded. For every spectral value `lambda` of a bounded operator in a complex Banach algebra,

\[
|\lambda| \leq \|A\|.
\]

Thus `sigma(A)` is a bounded subset of the complex plane.

By the Riemann–von Mangoldt theorem,

\[
N(T)=\frac{T}{2\pi}\log\!\left(\frac{T}{2\pi e}\right)+O(\log T),
\]

under the protected multiplicity and endpoint convention. In particular `N(T) -> infinity`. Therefore the positive ordinates of nontrivial zeros cannot be bounded: for every real `R` there exists a nontrivial zero with positive ordinate `gamma > R`.

Assume for contradiction that every `gamma in Gamma_+` belongs to `sigma(A)`. Take `R=||A||` and choose `gamma in Gamma_+` with `gamma>||A||`. Spectral containment gives

\[
\gamma = |\gamma| \leq \|A\|,
\]

contradicting `gamma>||A||`.

Therefore `Gamma_+` is not contained in `sigma(A)` for any bounded operator `A`. A fortiori, no bounded self-adjoint Hilbert-space operator can satisfy the complete Hilbert–Pólya ordinate-spectrum contract. QED.

### Endpoint and multiplicity check

The proof needs only that the zero-count grows without bound. It does not require simplicity, a zero-free boundary at a particular `T`, or an enumeration with distinct ordinates. Multiplicity only strengthens the count. Any standard endpoint convention compatible with `N(T) -> infinity` yields the same unboundedness conclusion.

## 6. Formal support

`MathSolve/RH/SpectralUnbounded.lean` proves the abstract operator-theoretic core:

> no element of a complete complex normed algebra can have an unbounded real sequence contained in its spectrum.

The formal theorem consumes the unbounded sequence as a hypothesis. This is intentional. The classical Riemann–von Mangoldt theorem is the imported analytic boundary and is not re-encoded as an axiom pretending to be a new proof. The Lean file therefore verifies the exact composition step, not the external analytic theorem.

Self-adjointness is not used in the formal core. The no-go applies to all bounded operators; this is stronger than the target's Hilbert–Pólya corollary.

## 7. Exact non-implications

This package does **not** prove or imply:

- the Riemann Hypothesis;
- that any nontrivial zero lies on `Re(s)=1/2`;
- that a Hilbert–Pólya operator exists;
- that any proposed unbounded operator is self-adjoint or essentially self-adjoint;
- any domain, deficiency-index, resolvent, trace-class, compact-resolvent, determinant, or trace-formula statement;
- that an operator with several matching eigenvalues has complete spectral equality;
- that a spectrum equal to `{Im(rho)}` by definition constrains `Re(rho)`;
- simplicity of zeros;
- a new zero-free region, zero-density theorem, critical-line proportion, or finite-height verification;
- novelty, priority, or publication readiness.

The only admitted mathematical result is the bounded-operator exclusion under the raw-ordinate spectral normalization.

## 8. False-proof firewall

### `RH-F003` — symmetry is not location

The functional equation and conjugation permit off-line quartets. Nothing in this theorem uses symmetry to locate zeros.

### `RH-F010` — symmetric is not self-adjoint

The theorem does not infer self-adjointness from a formally Hermitian expression. It says only that **if** an exact candidate is a bounded operator, it cannot contain the unbounded ordinate set in its spectrum.

### `RH-F011` — partial spectral match is not exact correspondence

Finite numerical matches and spacing statistics are irrelevant to the proof. The target uses the universal containment quantifier over all positive zero ordinates.

### Claimed-proof regression fixture

A route-relevant 2026 claimed proof argues that a self-adjoint operator with spectral values `Im(rho)` has real spectrum and then uses functional-equation symmetry to infer `Re(rho)=1/2`. The first implication is vacuous: `Im(rho)` is real for every complex `rho`. The second is blocked by `RH-F003`. This package does not use that inference.

## 9. Smallest next mathematical tranche

The bounded class is now closed. The next spectral tranche, if this route is continued, should not fit or search for eigenvalues. It should select one exact **unbounded** operator class and prove one necessary domain/resolvent property before any zeta-spectrum matching is attempted.

A defensible next target shape is:

> for a specified densely defined symmetric differential or dilation operator, determine all self-adjoint extensions (or prove essential self-adjointness) and characterize whether its resolvent can support a discrete unbounded spectrum with the Riemann–von Mangoldt counting scale.

That successor requires a fresh route-specific source audit and is not opened by this package.

## 10. Terminal tranche state

`RH-R030_SELECTED__FIRST_BRIDGE_PROVED`

`RH-T-000` remains open.
