# NS-CI-R014-A2-L4-3 — Weighted column and Carleson audit

## Status

- Campaign: `NS-CI-001`
- Parent: `MATHSOLVE#24`
- Tracker: `MATHSOLVE#58`
- Predecessor: `NS_CI_R014_A2_L4_SOURCE_SCALING_ENVELOPE.md`
- Result: `PROVED_EXACT_COLUMN_FORMULA_POSITIVE_KERNEL_ROUTE_REJECTED`
- Sufficiency for A2: no
- Numerical lane: closed

## 1. Obligation

L4-2 proved

```math
f(t)
\le
C_{LP}\|u_0\|_2
+
C_{LP}\nu^{-1/2}\Lambda(t)S_Q(t)^{1/2},
```

where

```math
S_Q(t)
=
\sum_{p=0}^{Q(t)}
2^{-2(Q(t)-p)}\lambda_pD_p(t),
\qquad
D_p(t)=\nu\|\nabla u_p(t)\|_2^2.
```

Equivalently,

```math
f(t)
\le
C_{LP}\|u_0\|_2
+
\varepsilon\nu\Lambda(t)^2
+
C_{LP}\varepsilon^{-1}\nu^{-2}S_Q(t).
```

The exact L4-3 question is whether

```math
\Lambda\in L^2(0,T),
\qquad
\sum_p\int_0^TD_p(t)dt<\infty
```

force

```math
\int_0^TS_Q(t)dt<\infty.
```

This package derives the exact column formula and proves that the implication fails for source-compatible dyadic estimate profiles. The result terminates positive weighted kernels with a nondegenerate cutoff-shell diagonal. It does not rule out a PDE-specific signed or dynamic correlation.

## 2. Exact column formula

Let

```math
E_q=\{t\in U:Q(t)=q\},
\qquad q\ge0.
```

The sets `E_q` are pairwise disjoint and partition the active set up to null sets. Since the summands are nonnegative, Tonelli gives

```math
\int_U S_Q(t)dt
=
\sum_{q\ge0}
\sum_{p=0}^{q}
2^{-2(q-p)}\lambda_p
\int_{E_q}D_p(t)dt.
```

With

```math
\mu_{p,q}=\int_{E_q}D_p(t)dt,
```

this becomes

```math
\int_U S_Qdt
=
\sum_{0\le p\le q}
2^{-2(q-p)}\lambda_p\mu_{p,q}.
```

Equivalently, after writing `q=p+j`,

```math
\int_U S_Qdt
=
\sum_{p\ge0}\lambda_p
\sum_{j\ge0}2^{-2j}
\int_{E_{p+j}}D_p(t)dt.
```

This is the complete weighted-column problem.

## 3. Available budgets

Write

```math
U_0=\|u_0\|_2,
\qquad
L_\Lambda^2=\int_0^T\Lambda(t)^2dt.
```

The selected hypothesis and Leray class provide:

### 3.1 Active-level occupancy

```math
\sum_{q\ge0}\lambda_q^2|E_q|
\le
L_\Lambda^2.
```

### 3.2 Total shell dissipation

```math
\sum_{p,q}\mu_{p,q}
=
\sum_p\int_U D_p(t)dt
\lesssim
U_0^2.
```

### 3.3 Pointwise shell-energy cap

Annular equivalence and `||u(t)||_2<=U_0` give

```math
D_p(t)
\simeq
\nu\lambda_p^2\|u_p(t)\|_2^2
\lesssim
\nu\lambda_p^2U_0^2.
```

Therefore

```math
\mu_{p,q}
\lesssim
\nu\lambda_p^2U_0^2|E_q|.
```

### 3.4 Threshold-shell lower bound

On `E_q`, minimality of `Q=q` gives

```math
\lambda_q^{-1}\|u_q(t)\|_\infty
\ge c_0\nu.
```

Bernstein then yields

```math
D_q(t)
\gtrsim
c_0^2\nu^3\lambda_q.
```

This is a lower bound. It does not prevent much larger active-shell dissipation.

## 4. Schur ledger

The dimensionless kernel

```math
K_{p,q}=2^{-2(q-p)}1_{\{p\le q\}}
```

has geometric rows and columns:

```math
\sup_q\sum_{p=0}^{q}K_{p,q}
\le\frac43,
```

```math
\sup_p\sum_{q\ge p}K_{p,q}
=\frac43.
```

The actual matrix is

```math
A_{p,q}=\lambda_pK_{p,q}.
```

Its column sum is

```math
\sum_{q\ge p}A_{p,q}
=
\frac43\lambda_p,
```

and its row sum satisfies

```math
\sum_{p=0}^{q}A_{p,q}
=
\lambda_q\sum_{j=0}^{q}2^{-3j}
\le
\frac87\lambda_q.
```

Thus ordinary positive Schur control against the unweighted measure `D_p(t)dt` fails by one frequency factor. The geometric gap suppresses shells far below the cutoff but does not suppress the diagonal `p=q`.

## 5. Best pointwise consequence of the energy cap

Using `D_p(t) lesssim nu lambda_p^2 U_0^2`,

```math
S_Q(t)
\lesssim
\nu U_0^2
\sum_{p=0}^{Q(t)}
2^{-2(Q(t)-p)}\lambda_p^3.
```

Since

```math
\lambda_p^3
=
\Lambda(t)^3 2^{-3(Q(t)-p)},
```

we obtain

```math
S_Q(t)
\lesssim
\nu U_0^2\Lambda(t)^3
\sum_{j\ge0}2^{-5j}
\lesssim
\nu U_0^2\Lambda(t)^3.
```

Substitution into the L4-2 envelope recovers

```math
f(t)
\lesssim
U_0+U_0\Lambda(t)^{5/2}.
```

This is the source upper envelope. No critical-exponent gain has occurred.

## 6. Diagonal obstruction theorem

### Theorem `NS-CI-A2-L4-Lemma-2`

Let `K_{p,q}>=0` be lower triangular and define

```math
\mathcal W_K(t)
=
\sum_{p=0}^{Q(t)}
K_{p,Q(t)}\lambda_pD_p(t).
```

Assume

```math
\inf_{q\ge q_0}K_{q,q}
\ge\kappa>0.
```

There is no bound

```math
\int_0^T\mathcal W_K(t)dt
\le
F\left(
\int_0^T\Lambda(t)^2dt,
U_0,
\nu,
T
\right)
```

valid for every dyadic profile satisfying the threshold definition, the pointwise kinetic-energy bound, the Leray-form total dissipation budget, and `Lambda in L2_t`.

The theorem concerns estimate profiles, not Navier–Stokes solutions.

### Proof

Choose a nonzero divergence-free Schwartz field `phi` supported in a fixed Fourier annulus and normalize

```math
\|\phi\|_2=1.
```

For `lambda_q=2^q`, set

```math
\phi_q(x)=\lambda_q^{3/2}\phi(\lambda_qx).
```

Then

```math
\|\phi_q\|_2=1,
```

```math
\|\phi_q\|_\infty
=\lambda_q^{3/2}\|\phi\|_\infty,
```

and

```math
\|\nabla\phi_q\|_2^2
=\lambda_q^2\|\nabla\phi\|_2^2.
```

Choose pairwise disjoint intervals `I_q` with

```math
|I_q|
=\tau_q
=
\frac{\lambda_q^{-5/2}}{q+1},
\qquad q\ge q_0.
```

On `I_q`, set

```math
u_q(t,x)=U_0\phi_q(x),
```

with every other annular shell zero. Outside the boxes set the profile to zero.

For sufficiently large `q_0`,

```math
\lambda_q^{-1}\|u_q\|_\infty
=U_0\|\phi\|_\infty\lambda_q^{1/2}
\ge c_0\nu.
```

Every shell above `q` is zero, so `Q(t)=q` on `I_q`.

The pointwise energy is `U_0^2`, and

```math
D_q(t)
=
\nu U_0^2\|\nabla\phi\|_2^2\lambda_q^2.
```

The critical-wavenumber cost converges:

```math
\int\Lambda^2dt
=
\sum_q\lambda_q^2\tau_q
=
\sum_q\frac{\lambda_q^{-1/2}}{q+1}
<\infty.
```

The total shell dissipation also converges:

```math
\sum_p\int D_pdt
=
\nu U_0^2\|\nabla\phi\|_2^2
\sum_q\frac{\lambda_q^{-1/2}}{q+1}
<\infty.
```

But the diagonal contribution gives

```math
\int\mathcal W_Kdt
\ge
\kappa\sum_q\lambda_qD_q\tau_q
```

and therefore

```math
\int\mathcal W_Kdt
\gtrsim
\kappa\nu U_0^2
\sum_q\frac{\lambda_q^{1/2}}{q+1}
=\infty.
```

This proves the theorem.

### Disposition

`PROVED_COUNTERFIXTURE`.

## 7. Saturation of the low-mode obstruction

On `I_q`,

```math
f(t)
=
\lambda_q\|u_q(t)\|_\infty
=
U_0\|\phi\|_\infty\lambda_q^{5/2}.
```

Hence

```math
\int_0^Tf(t)dt
=
U_0\|\phi\|_\infty
\sum_q\lambda_q^{5/2}\tau_q
=
U_0\|\phi\|_\infty
\sum_q\frac1{q+1}
=\infty.
```

The fixture therefore has

```math
\Lambda\in L^2_t,
\qquad
\sum_pD_p\in L^1_t,
\qquad
\sup_t\|u(t)\|_2\le U_0,
```

while `f notin L1_t`. This does not disprove A2 because the profile is not a Navier–Stokes solution. It proves that the static threshold and Leray budgets do not imply the desired positive column estimate.

## 8. Compatibility with prior estimate constraints

The box charge is

```math
\mathcal E_q(I_q)
=
\frac{\lambda_q}{\nu^2}
\int_{I_q}D_q(t)dt
\asymp
\frac{U_0^2}{\nu}
\frac{\lambda_q^{1/2}}{q+1}.
```

For large `q` this exceeds every fixed buffered-exit lower bound. Transition boxes can be appended at the previously proved physical cost

```math
O(\nu^2\lambda_q^{-1})
```

per level, whose total is summable. The shell energy `U_0^2` also exceeds the threshold floor `nu^2 lambda_q^-1` at high frequency.

No claim is made that the switching or prescribed dissipation matrix solves Navier–Stokes.

## 9. Why diagonal decay cannot rescue the current envelope

Suppose a positive kernel has `K_{q,q}->0`. On a single cutoff-shell packet, an estimate

```math
f(t)
\le
C\nu^{-1/2}\Lambda(t)
\mathcal W_K(t)^{1/2}
```

requires

```math
K_{q,q}\gtrsim1.
```

Indeed, Bernstein-saturating packets satisfy

```math
f_q^2
\asymp
\nu^{-1}\lambda_q^3D_q,
```

while the squared right side is

```math
C^2\nu^{-1}\lambda_q^2
K_{q,q}\lambda_qD_q.
```

The frequency powers already agree, leaving a uniform lower bound on `K_{q,q}`. Thus:

- pointwise cutoff-shell domination requires a nondegenerate diagonal;
- positive time-integrated column control pushes the diagonal toward decay;
- these requirements are incompatible under the available budgets.

## 10. Carleson interpretation

The desired quantity is

```math
\mathfrak C_D
=
\sum_{0\le p\le q}
2^{-2(q-p)}\lambda_p\mu_{p,q}.
```

Known information controls

```math
\sum_{p,q}\mu_{p,q}
```

and

```math
\sum_q\lambda_q^2|E_q|,
```

but not the diagonal correlation

```math
\mu_{q,q}=\int_{E_q}D_q(t)dt.
```

The fixture concentrates active occupancy and the maximum permitted shell energy on that diagonal. A valid Carleson theorem must therefore use a property of the Navier–Stokes evolution absent from the scalar budgets: signed cancellation, dynamic depletion, or a genuine decorrelation inequality.

Assuming `mathfrak C_D<infinity` is valid but merely restates the missing bridge.

## 11. Proof-obligation DAG

```text
L4-3.1 exact Tonelli column formula
    PROVED
        |
        v
L4-3.2 dimensionless Schur rows and columns
    PROVED
        |
        v
L4-3.3 weighted diagonal calculation
    PROVED: column cost grows like lambda_p
        |
        v
L4-3.4 implication from Lambda-L2 and Leray budgets
    REJECTED_COUNTERFIXTURE
        |
        +------------------------------+
        |                              |
        v                              v
positive nondegenerate kernel     PDE-specific signed or
    TERMINATED                    dynamic correlation
                                  OPEN: L4-4
```

## 12. Route disposition

| Candidate | Disposition | Exact reason |
|---|---|---|
| dimensionless geometric row bound | proved | row sum is `4/3` |
| dimensionless geometric column bound | proved | column sum is `4/3` |
| weighted Schur bound against `D_p dt` | rejected | weighted column constant is `(4/3)lambda_p` |
| pointwise energy cap | insufficient | recovers only `S_Q lesssim nu U_0^2 Lambda^3` |
| combine `Lambda L2` and total dissipation | rejected | packet fixture makes `int S_Q` diverge |
| positive kernel with `K_qq>=kappa` | terminated | diagonal obstruction theorem |
| positive kernel with decaying diagonal | incompatible with current envelope | cutoff-shell packets require `K_qq gtrsim 1` |
| weighted Carleson estimate as hypothesis | conditional/tautological | it is the missing bridge itself |
| signed or equation-dynamic correlation | open | not tested by this positive counterfixture |

## 13. Strongest surviving statement

The strongest unconditional result remains

```math
f(t)
\le
C_{LP}U_0
+
C_{LP}\nu^{-1/2}\Lambda(t)S_Q(t)^{1/2}.
```

It closes under the explicit additional hypothesis `S_Q in L1_t`, but that hypothesis is not implied by `Lambda in L2_t` and Leray energy.

## 14. Next obligation

Proceed to L4-4 only through a genuinely equation-specific mechanism:

1. a signed shell or cumulative-flux expression whose time integral telescopes without absolute values;
2. a commutator or depletion identity canceling the diagonal cutoff-shell contribution;
3. a dynamic decorrelation estimate between `D_q` and `{Q=q}`;
4. or terminate L4 and promote the independent direct critical-integral lane L5.

No further positive Schur variant is admissible unless it explicitly defeats the diagonal theorem.

## Claim boundary

This package proves failure of a class of positive weighted-column arguments under the source-level static and Leray constraints. It does not construct a Navier–Stokes counterexample, disprove A2, or rule out signed, nonlinear, or equation-specific weighted estimates.