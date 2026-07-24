# NS-CI-R014-A2-L4 — Weighted dissipation bridge

## Status

- Campaign: `NS-CI-001`
- Parent: `MATHSOLVE#24`
- Tracker: `MATHSOLVE#58`
- State: `L4_0_THROUGH_L4_2_PROVED_L4_3_ACTIVE`
- A2 status: unproved
- Numerical lane: closed

The source reconstruction, scaling audit, and active-shell envelope are complete in:

- `NS_CI_R014_A2_L4_SOURCE_SCALING_ENVELOPE.md`.

This document is the controlling roadmap for the remaining weighted-dissipation lane.

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

Therefore the dimensionally normalized positive kernel term is

```math
\nu^{-2}\sum_{p\le Q}K_{p,Q}\lambda_pD_p,
```

not the unnormalized schematic sum used during initialization.

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

The completed L4-2 lemma proves

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

The proof uses

```math
\lambda_p\|u_p\|_\infty
\lesssim
\lambda_p^{5/2}\|u_p\|_2,
```

```math
D_p\simeq\nu\lambda_p^2\|u_p\|_2^2,
```

and the exact identity

```math
\lambda_p^3
=
\Lambda^2
2^{-2(Q-p)}\lambda_p.
```

## 5. Kernel ledger

The first proved kernel is

```math
K_{p,Q}=2^{-2(Q-p)},
\qquad 0\le p\le Q.
```

It has uniform row sum

```math
\sup_Q\sum_{p=0}^QK_{p,Q}
\le
\sum_{j=0}^{\infty}4^{-j}
=
\frac43.
```

For a fixed near-cluster width `J`, the far row tail satisfies

```math
\sup_Q
\sum_{p\le Q-J-1}K_{p,Q}
\le
\frac{4^{-(J+1)}}{1-1/4}.
```

Thus replacing the shell supremum by a weighted sum incurs a uniform, geometrically decaying row kernel.

## 6. Exact remaining obstruction

Tonelli gives

```math
\int_0^TS_Q(t)dt
=
\sum_{p\ge0}\lambda_p
\int_0^T
1_{\{Q(t)\ge p\}}
2^{-2(Q(t)-p)}D_p(t)dt.
```

The Leray budget controls

```math
\sum_p\int_0^TD_p(t)dt,
```

not the extra factor `lambda_p`. The assumption

```math
\int_0^T\Lambda(t)^2dt<\infty
```

controls active-level occupancy but does not independently control its correlation with `D_p(t)`.

Uniform row summability is therefore insufficient. The remaining problem is a weighted **column** or **Carleson** estimate.

## 7. Active proof-obligation DAG

```text
L4-0 exact source definitions                    PROVED
L4-1 dimensions and dyadic scaling               PROVED
L4-2 active-shell envelope and row kernel         PROVED
    |
    v
L4-3a compute weighted column occupancy           ACTIVE
L4-3b test Lambda-L2 plus energy sufficiency       ACTIVE
L4-3c construct endpoint counterfixture            ACTIVE
    |
    +----------------------------+
    |                            |
    v                            v
L4-4 positive kernel         L4-4 signed kernel
    |                            |
    +-------------+--------------+
                  |
                  v
L4-5 uniform Schur/Carleson estimate
                  |
                  v
             f in L1 and A2
```

## 8. L4-3 acceptance test

The next stage must decide whether

```math
\int_0^T
\sum_{p=0}^{Q(t)}
2^{-2(Q(t)-p)}\lambda_pD_p(t)dt
```

is bounded by a finite function of

```math
\int_0^T\Lambda(t)^2dt,
\qquad
\|u_0\|_2,
\qquad
\nu,
\qquad
T.
```

A positive result must prove the active-set/dissipation correlation. A negative result must provide a time-frequency profile satisfying all source-normalized energy, threshold, and `Lambda in L2` constraints while making the weighted integral diverge.

## 9. Pedagogical lemma contract

Every L4-3 or later lemma must contain:

1. exact domains, active-set restrictions, and constant dependence;
2. physical dimensions and Navier–Stokes scaling;
3. numbered proof steps with named inequalities;
4. complete row and column calculations;
5. a time-integrability ledger;
6. an adversarial profile testing endpoint uniformity;
7. one disposition: `PROVED`, `CONDITIONAL`, `REJECTED_CIRCULAR`, `REJECTED_SCALING`, or `REJECTED_COUNTERFIXTURE`.

## Claim boundary

L4-0 through L4-2 are complete. The weighted pointwise envelope is proved, but its time-integrated kernel is not controlled. This document does not prove `f in L1`, regularity, the critical integral, or A2.
