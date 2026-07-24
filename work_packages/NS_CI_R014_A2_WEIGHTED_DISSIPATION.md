# NS-CI-R014-A2-L4 — Weighted dissipation bridge

## Status

- Campaign: `NS-CI-001`
- Parent: `MATHSOLVE#24`
- Tracker: `MATHSOLVE#58`
- State: `INITIALIZED_PRIMARY_LANE`
- A2 status: unproved
- Numerical lane: closed

## 1. Question

Can the assumed critical wavenumber control

```math
\Lambda\in L^2(0,T)
```

be combined with the Leray shell-dissipation budget to prove

```math
f(t)
=
\|\omega_{\le Q(t)}(t)\|_{B^0_{\infty,\infty}}
\in L^1(0,T)?
```

The lane succeeds only through a scale-critical inequality with constants uniform in the moving cutoff.

## 2. Why this lane is distinct from L3

L3 charged isolated threshold excursions. Every proved charge had physical size `nu^2 lambda_q^-1`, which is summable over dyadic levels.

L4 does not count excursions. It asks whether the **distribution of dissipation across active frequencies** supplies a weighted time-frequency estimate that is invisible to per-excursion bookkeeping.

The central object is not a dwell time but a positive or signed kernel coupling shell index `p` to active cutoff `Q(t)`.

## 3. Imported objects

The exact source definitions must be reconstructed before theorem work. The following schematic notation is fixed only for the proof ledger:

```math
\lambda_q=2^q,
\qquad
\Lambda(t)=\lambda_{Q(t)},
\qquad
u_q=\Delta_qu,
\qquad
\omega_q=\nabla\times u_q.
```

Define the shell dissipation density

```math
D_q(t)
=
\nu\|\nabla u_q(t)\|_2^2.
```

The Leray energy inequality gives

```math
\sum_q\int_0^TD_q(t)dt
\lesssim
\|u_0\|_2^2.
```

No pointwise-in-time bound on `sum_q D_q(t)` is imported.

## 4. Scaling table

Under

```math
u_\rho(x,t)=\rho u(\rho x,\rho^2t),
```

with viscosity fixed, the relevant scaling weights are:

| Quantity | Scaling factor |
|---|---:|
| `dt` | `rho^-2` |
| `lambda_q`, `Lambda` | `rho` |
| `u` | `rho` |
| `omega` | `rho^2` |
| `f` | `rho^2` |
| `||u_q||_2` | `rho^-1/2` |
| `||grad u_q||_2` | `rho^1/2` |
| `D_q=nu||grad u_q||_2^2` | `rho` |
| `lambda_q D_q` | `rho^2` |
| `Lambda^2 dt` | invariant |
| `f dt` | invariant |
| `lambda_q D_q dt` | invariant |

Therefore a pointwise positive weighted-dissipation candidate naturally has the schematic form

```math
f(t)
\lesssim
C\Lambda(t)^2
+
\sum_{p\le Q(t)}K_{p,Q(t)}\lambda_pD_p(t),
```

where `K` is dimensionless.

Scaling compatibility is necessary, not sufficient. The energy inequality controls `D_p dt`, not `lambda_p D_p dt`; the kernel must recover that extra frequency without acquiring a cutoff-dependent constant.

## 5. Baseline low-mode envelope

For a standard dyadic Besov realization,

```math
f(t)
\simeq
\sup_{p\le Q(t)}\|\omega_p(t)\|_\infty
\lesssim
\sup_{p\le Q(t)}
\lambda_p^{5/2}\|u_p(t)\|_2.
```

The exponent comes from one derivative and `L2 -> Linfinity` Bernstein in three dimensions.

Squaring gives

```math
f(t)^2
\lesssim
\sup_{p\le Q(t)}
\lambda_p^5\|u_p(t)\|_2^2.
```

Direct comparison with dissipation uses

```math
D_p(t)
\simeq
\nu\lambda_p^2\|u_p(t)\|_2^2,
```

so the naive shell ratio is

```math
\frac{\lambda_p^5\|u_p\|_2^2}{D_p}
\simeq
\nu^{-1}\lambda_p^3.
```

This calculation is pedagogically important: a pointwise estimate obtained only by squaring Bernstein is far from the critical linear form `lambda_p D_p`. Any successful argument must use the moving active cutoff, threshold information, cancellation, or time-frequency averaging—not another pointwise Bernstein step.

## 6. Proof-obligation DAG

```text
L4-0 exact source definitions
    |
    v
L4-1 scaling and dimensions
    |
    v
L4-2 explicit shell formula for f
    |
    +--------------------------+
    |                          |
    v                          v
L4-3 positive kernel       L4-4 signed/commutator kernel
    |                          |
    +-------------+------------+
                  |
                  v
          L4-5 uniform Schur or Carleson bound
                  |
                  v
          time-integrated L1 estimate for f
                  |
                  v
          WP02 regularity bridge and A2
```

Every edge is an independent proof obligation. Failure of one positive kernel does not validate a signed kernel.

## 7. Candidate kernel ledger

For each candidate write

```math
\mathcal W(t)
=
\sum_{p\le Q(t)}K_{p,Q(t)}\lambda_pD_p(t).
```

The audit must record:

| Field | Required entry |
|---|---|
| support | exact region in `(p,Q)` |
| sign | positive, signed, or commutator |
| scaling | invariant check |
| row sum | `sup_Q sum_p |K_pQ|` |
| column sum | time-integrated occupancy for fixed `p` |
| endpoint | logarithmic or power divergence |
| threshold use | strict high modes, threshold cluster, or none |
| imported norm | every non-Leray quantity |
| conclusion | proved, conditional, or rejected |

The first model family is

```math
K_{p,Q}=\kappa_{Q-p},
\qquad p\le Q,
```

with geometric, polynomial, and endpoint sequences `kappa_j`. Row summability alone does not close the estimate because of the extra factor `lambda_p` against the energy budget. The column calculation must exploit the set on which `Q(t)>=p` or a stronger active-shell relation.

## 8. Time-frequency reformulation

For a positive kernel, Tonelli gives

```math
\int_0^T\mathcal W(t)dt
=
\sum_p\lambda_p
\int_0^T
1_{\{Q(t)\ge p\}}
K_{p,Q(t)}D_p(t)dt.
```

The assumption `Lambda in L2_t` controls only

```math
\int_0^T\Lambda(t)^2dt
\simeq
\sum_k2^{2k}|\{Q=k\}|.
```

It does not by itself control the correlation between `D_p(t)` and the active set `{Q(t)>=p}`. This correlation is the exact weighted-dissipation interface.

A successful estimate must prove one of:

1. a uniform weighted column bound against `D_p dt`;
2. a Carleson measure estimate on active time-frequency boxes;
3. a signed cancellation that survives time integration;
4. a decomposition in which the extra `lambda_p` is replaced by `Lambda` and paired critically with an independently controlled factor;
5. a shell-envelope estimate stronger than the raw energy budget.

## 9. Mandatory baseline failures

Before proposing a new mechanism, the work package must reproduce and reject:

### Failure A — unrelated `L1` product

```math
\Lambda^2\in L^1_t,
\qquad
\sum_pD_p\in L^1_t
```

does not imply

```math
\Lambda^2\sum_pD_p\in L^1_t.
```

### Failure B — cutoff-dependent row constant

A kernel satisfying

```math
\sum_{p\le Q}K_{p,Q}\sim Q
```

is not uniform, even though every finite truncation is bounded.

### Failure C — threshold-shell misuse

The strict high-mode threshold applies only above `Q`. It cannot bound the shell `Q` or lower shells appearing in `f`.

### Failure D — pointwise dissipation substitution

The global integral of `sum_pD_p` cannot be used as a pointwise upper bound for an active shell.

### Failure E — hidden half-power

Any estimate equivalent to

```math
f\lesssim\Lambda^{5/2}
```

has not solved the critical `Lambda^2` problem.

## 10. Pedagogical lemma template

Every proposed lemma must use this format.

### Lemma identifier

`NS-CI-A2-L4-Lemma-N`

### Statement

State all domains, times, active-set restrictions, constants, and dependence on the Littlewood–Paley partition.

### Scaling check

List the scaling factor of every term.

### Proof

Number each inequality and name the theorem used: Bernstein, Cauchy–Schwarz, Schur, Tonelli, energy inequality, threshold definition, or cancellation identity.

### Time-integrability ledger

For each factor state its known space and whether the product closes by Hölder.

### Adversarial fixture

Give the simplest scalar or dyadic profile testing the claimed exponent and cutoff uniformity.

### Disposition

One of `PROVED`, `CONDITIONAL`, `REJECTED_CIRCULAR`, `REJECTED_SCALING`, or `REJECTED_COUNTERFIXTURE`.

## 11. Acceptance criterion

L4 closes only if it proves

```math
\int_0^Tf(t)dt
\le
C\left(
\int_0^T\Lambda(t)^2dt,
\|u_0\|_2,
\nu,
T
\right)
```

with finite dependence on the displayed data and constants uniform in all frequency truncations.

A result depending on an additional weighted shell norm must state that norm as a new restricted hypothesis and undergo a separate prior-art and scaling audit.

## 12. First executable task

Reconstruct the exact source-normalized formula for `f` and the whole-space dissipation-wavenumber definition, then produce the first weighted kernel table. No candidate inequality is promoted before this source pass.

## Claim boundary

This document initializes the primary pivot lane. It contains scaling deductions and proof obligations, not a weighted-dissipation theorem.