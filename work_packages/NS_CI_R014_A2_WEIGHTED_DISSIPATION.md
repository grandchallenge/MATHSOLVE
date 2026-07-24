# NS-CI-R014-A2-L4 — Weighted dissipation bridge

## Status

- Campaign: `NS-CI-001`
- Parent: `MATHSOLVE#24`
- Tracker: `MATHSOLVE#58`
- State: `L4_0_THROUGH_L4_3_COMPLETE_POSITIVE_KERNEL_TERMINATED`
- A2 status: unproved
- Numerical lane: closed

Completed artifacts:

- `NS_CI_R014_A2_L4_SOURCE_SCALING_ENVELOPE.md` — source normalization, scaling, and active-shell envelope;
- `NS_CI_R014_A2_L4_WEIGHTED_COLUMN.md` — exact column formula, Schur audit, and positive-kernel counterfixture.

This document is the controlling roadmap for the surviving weighted-dissipation lane.

## 1. Question

Can

```math
\Lambda\in L^2(0,T)
```

be combined with the Leray shell-dissipation budget to prove

```math
f(t)
=
\sup_{-1\le p\le Q(t)}
\lambda_p\|u_p(t)\|_\infty
\in L^1(0,T)?
```

The lane succeeds only through a scale-critical estimate with constants uniform in the moving cutoff.

## 2. Source-normalized definitions

For `lambda_q=2^q`,

```math
Q(t)
=
\min\left\{
q\ge0:
\lambda_p^{-1}\|u_p(t)\|_\infty<c_0\nu
\text{ for every }p>q
\right\},
```

and

```math
\Lambda(t)=\lambda_{Q(t)}.
```

On the active set

```math
U=\{t:\Lambda(t)>1\},
```

minimality gives

```math
\|u_{Q(t)}(t)\|_\infty
\ge
c_0\nu\Lambda(t).
```

The strict-high-mode threshold controls only `p>Q`. It gives no upper bound for `p=Q` or lower shells.

The restored source envelope is

```math
c_0\nu\Lambda(t)^2
\le
f(t)
\le
C\|u_0\|_2\Lambda(t)^{5/2},
\qquad t\in U.
```

On `U^c`, `Q=0` and

```math
f(t)\lesssim\|u_0\|_2.
```

## 3. Scaling and dimensional normalization

Under

```math
u_\rho(x,t)=\rho u(\rho x,\rho^2t),
```

with viscosity fixed,

| Quantity | Scaling factor |
|---|---:|
| `dt` | `rho^-2` |
| `Lambda`, `lambda_p` | `rho` |
| `f` | `rho^2` |
| `nu Lambda^2` | `rho^2` |
| `D_p=nu||grad u_p||_2^2` | `rho` |
| `lambda_p D_p` | `rho^2` |
| `nu^-2 lambda_p D_p` | `rho^2` |

Physical dimensions distinguish homogeneity from a valid pointwise comparison:

```math
[f]=[\nu\Lambda^2]
=[\nu^{-2}\lambda_pD_p]
=T^{-1}.
```

## 4. Proved weighted pointwise envelope

For annular shells `p>=0`, define

```math
D_p(t)=\nu\|\nabla u_p(t)\|_2^2.
```

Set

```math
S_Q(t)
=
\sum_{p=0}^{Q(t)}
2^{-2(Q(t)-p)}\lambda_pD_p(t).
```

L4-2 proves

```math
f(t)
\le
C\|u_0\|_2
+
C\nu^{-1/2}\Lambda(t)S_Q(t)^{1/2}.
```

Equivalently, for every `epsilon>0`,

```math
f(t)
\le
C\|u_0\|_2
+
\epsilon\nu\Lambda(t)^2
+
C\epsilon^{-1}\nu^{-2}S_Q(t).
```

The dimensionless geometric kernel

```math
K_{p,Q}=2^{-2(Q-p)}1_{\{p\le Q\}}
```

has uniformly bounded row and column sums. The actual weighted matrix contains `lambda_p`, and that factor is the critical obstruction.

## 5. L4-3 exact column formula

Let

```math
E_q=\{t\in U:Q(t)=q\}
```

and

```math
\mu_{p,q}=\int_{E_q}D_p(t)dt.
```

Tonelli gives

```math
\int_US_Q(t)dt
=
\sum_{0\le p\le q}
2^{-2(q-p)}\lambda_p\mu_{p,q}.
```

Equivalently,

```math
\int_US_Qdt
=
\sum_{p\ge0}\lambda_p
\sum_{j\ge0}2^{-2j}
\int_{E_{p+j}}D_p(t)dt.
```

The known budgets are

```math
\sum_q\lambda_q^2|E_q|
\le
\int_0^T\Lambda(t)^2dt,
```

```math
\sum_{p,q}\mu_{p,q}
\lesssim
\|u_0\|_2^2,
```

and

```math
D_p(t)
\lesssim
\nu\lambda_p^2\|u_0\|_2^2.
```

None controls the diagonal correlation `mu_{q,q}` with the additional factor `lambda_q`.

## 6. Schur audit

For the dimensionless kernel,

```math
\sup_q\sum_{p\le q}K_{p,q}
=
\sup_p\sum_{q\ge p}K_{p,q}
=
\frac43.
```

For the weighted matrix

```math
A_{p,q}=\lambda_pK_{p,q},
```

one has

```math
\sum_{q\ge p}A_{p,q}
=
\frac43\lambda_p,
```

and

```math
\sum_{p\le q}A_{p,q}
\le
\frac87\lambda_q.
```

Thus ordinary positive Schur control against `D_p(t)dt` is not uniform in frequency.

Using only the pointwise energy cap yields

```math
S_Q(t)
\lesssim
\nu\|u_0\|_2^2\Lambda(t)^3,
```

and hence recovers only

```math
f(t)
\lesssim
\|u_0\|_2
+
\|u_0\|_2\Lambda(t)^{5/2}.
```

No exponent gain has occurred.

## 7. L4-3 counterfixture and theorem

The completed L4-3 artifact proves:

> For every positive lower-triangular kernel with a nondegenerate diagonal `inf_q K_qq>0`, no bound of `int W_K` by `||Lambda||_L2`, the pointwise kinetic-energy bound, the total shell-dissipation budget, viscosity, and time can hold for all source-compatible dyadic profiles.

The fixture uses disjoint intervals

```math
|I_q|
=
\frac{\lambda_q^{-5/2}}{q+1}
```

and one `L2`-normalized Bernstein-saturating annular packet at shell `q` on `I_q`. It satisfies

```math
\int\Lambda^2dt
\asymp
\sum_q\frac{\lambda_q^{-1/2}}{q+1}
<\infty,
```

and

```math
\sum_p\int D_pdt
\asymp
\sum_q\frac{\lambda_q^{-1/2}}{q+1}
<\infty,
```

but

```math
\int S_Qdt
\gtrsim
\sum_q\frac{\lambda_q^{1/2}}{q+1}
=\infty.
```

The same fixture saturates the source upper envelope and has

```math
\int f(t)dt
\asymp
\sum_q\frac1{q+1}
=\infty.
```

It is an estimate counterfixture, not a Navier–Stokes solution.

## 8. Diagonal incompatibility

A positive kernel with decaying diagonal could evade the preceding divergence, but it cannot dominate the cutoff-shell contribution in the proved square-root envelope.

For a cutoff-shell Bernstein-saturating packet,

```math
f_q^2
\asymp
\nu^{-1}\lambda_q^3D_q.
```

A bound

```math
f
\le
C\nu^{-1/2}\Lambda
\left(
\sum_{p\le Q}K_{p,Q}\lambda_pD_p
\right)^{1/2}
```

requires

```math
K_{q,q}\gtrsim1.
```

Therefore:

- pointwise cutoff-shell domination requires a nondegenerate diagonal;
- positive time-integrated column control requires suppressing that diagonal;
- the two requirements are incompatible under the static budgets.

## 9. Proof-obligation DAG

```text
L4-0 exact source definitions                    PROVED
L4-1 dimensions and dyadic scaling               PROVED
L4-2 active-shell envelope and row kernel         PROVED
L4-3a exact weighted column formula               PROVED
L4-3b Schur and diagonal calculation              PROVED
L4-3c Lambda-L2 plus energy sufficiency            REJECTED_COUNTERFIXTURE
L4-3d positive kernel with nondegenerate diagonal TERMINATED
    |
    +-------------------------------+
    |                               |
    v                               v
L4-4 signed/commutator kernel    L5 direct critical integral
OPEN                            INDEPENDENT
```

## 10. Route disposition

| Route | Disposition |
|---|---|
| dimensionless geometric row/column sums | `PROVED` |
| weighted Schur estimate against Leray dissipation | `REJECTED_COUNTERFIXTURE` |
| pointwise energy cap | `INSUFFICIENT_SOURCE_EXPONENT_RECOVERED` |
| any positive kernel with `K_qq>=kappa` | `TERMINATED_DIAGONAL_OBSTRUCTION` |
| positive kernel with decaying diagonal | `INCOMPATIBLE_WITH_CUTOFF_SHELL_DOMINATION` |
| signed or commutator correlation | `OPEN_L4_4` |
| direct critical-integral route | `OPEN_L5` |

## 11. Next obligation

L4 may proceed only through an equation-specific signed or dynamic mechanism that explicitly defeats the diagonal theorem. Admissible targets are:

1. a signed shell or cumulative-flux expression whose time integral genuinely telescopes;
2. a commutator or depletion identity canceling the active diagonal contribution;
3. a PDE-derived decorrelation estimate between `D_q` and `{Q=q}`.

No further positive Schur variant is admissible without an explicit proof that its cutoff-shell diagonal is both pointwise sufficient and time-integrable.

## Claim boundary

L4-0 through L4-3 are complete. The positive weighted-dissipation route is terminated under the source-level static and Leray budgets. This document does not prove `f in L1`, regularity, the critical integral, or A2, and it does not rule out signed, nonlinear, or equation-specific weighted estimates.