# NS-CI-R014-A2-L4-3 — Weighted column and Carleson audit

## Status

- Campaign: `NS-CI-001`
- Parent: `MATHSOLVE#24`
- Tracker: `MATHSOLVE#58`
- Predecessor: `NS_CI_R014_A2_L4_SOURCE_ENVELOPE.md`
- Result: `PROVED_EXACT_COLUMN_FORMULA_POSITIVE_KERNEL_ROUTE_REJECTED`
- Sufficiency for A2: no
- Numerical lane: closed

## 1. Obligation

The preceding work package proved, on the active set and up to the fixed base-shell remainder,

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

This package derives the complete column formula, proves that ordinary positive Schur control fails at the diagonal, and constructs a dyadic packet fixture satisfying the source-level threshold, energy, dissipation, and `Lambda in L2` constraints while both `int S_Q` and `int f` diverge.

The conclusion is limited but decisive: **the positive weighted-column estimate does not follow from the selected hypothesis, the Leray budgets, and the static dissipation-wavenumber definition alone.** A PDE-specific signed or dynamic correlation remains logically possible and belongs to L4-4.

## 2. Time partition and exact column formula

Let

```math
E_q
=
\{t\in U:Q(t)=q\},
\qquad q\ge0.
```

The sets `E_q` are pairwise disjoint and partition the active set up to null sets. Since every term in `S_Q` is nonnegative, Tonelli gives the exact identity

```math
\int_U S_Q(t)dt
=
\sum_{q\ge0}
\sum_{p=0}^{q}
2^{-2(q-p)}\lambda_p
\int_{E_q}D_p(t)dt.
```

Reindexing by `j=q-p`,

```math
\int_U S_Q(t)dt
=
\sum_{p\ge0}\lambda_p
\sum_{j\ge0}2^{-2j}
\int_{E_{p+j}}D_p(t)dt.
```

Define the dissipation matrix

```math
\mu_{p,q}
=
\int_{E_q}D_p(t)dt,
\qquad 0\le p\le q.
```

Then

```math
\int_U S_Qdt
=
\sum_{0\le p\le q}
2^{-2(q-p)}\lambda_p\mu_{p,q}.
```

This is the line-addressable L4-3 column problem.

## 3. Available budgets

Write

```math
U_0=\|u_0\|_2,
\qquad
L_\Lambda^2=\int_0^T\Lambda(t)^2dt.
```

The imported information is:

### 3.1 Wavenumber occupancy

```math
\sum_{q\ge0}\lambda_q^2|E_q|
\le
L_\Lambda^2.
```

### 3.2 Total shell dissipation

```math
\sum_{p\ge0}\sum_{q\ge0}\mu_{p,q}
=
\sum_{p\ge0}\int_U D_p(t)dt
\lesssim
U_0^2.
```

### 3.3 Pointwise shell-energy cap

For annular shells,

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

By Bernstein,

```math
D_q(t)
\gtrsim
c_0^2\nu^3\lambda_q.
```

This is a lower bound. It does not prevent much larger dissipation on the active shell.

## 4. Row and column calculations

The dimensionless kernel is

```math
K_{p,q}=2^{-2(q-p)}1_{\{p\le q\}}.
```

Its rows and columns are geometrically summable:

```math
\sup_q\sum_{p=0}^{q}K_{p,q}
\le
\sum_{j\ge0}2^{-2j}
=
\frac43,
```

and

```math
\sup_p\sum_{q\ge p}K_{p,q}
=
\frac43.
```

These bounds do not act on the actual weighted matrix, which contains `lambda_p`:

```math
A_{p,q}
=
\lambda_pK_{p,q}.
```

For fixed `p`,

```math
\sum_{q\ge p}A_{p,q}
=
\frac43\lambda_p.
```

The column constant grows with frequency. Ordinary positive Schur control against the unweighted measure `D_p(t)dt` therefore fails before any PDE estimate is used.

For fixed `q`,

```math
\sum_{p=0}^{q}A_{p,q}
=
\lambda_q
\sum_{j=0}^{q}2^{-3j}
\le
\frac87\lambda_q.
```

The row cost is likewise proportional to the active frequency. The geometric gap controls distance below the cutoff, but it does not suppress the diagonal `p=q`.

## 5. Best estimate from the pointwise energy cap

Using the pointwise shell-energy cap,

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

Substitution into the square-root envelope gives

```math
f(t)
\lesssim
U_0
+
U_0\Lambda(t)^{5/2},
```

which is the already-audited source upper envelope. The weighted dissipation rewrite has not improved the source exponent under pointwise energy control alone.

This estimate closes under `Lambda in L3_t`, or directly under the known `Lambda in L5/2_t` source criterion after reverting to the sharper source envelope, but not under `Lambda in L2_t`.

## 6. Diagonal obstruction theorem

### Theorem `NS-CI-A2-L4-Lemma-2`

Let `K_{p,q}>=0` be a positive lower-triangular kernel and define

```math
\mathcal W_K(t)
=
\sum_{p=0}^{Q(t)}K_{p,Q(t)}\lambda_pD_p(t).
```

Assume the diagonal is nondegenerate:

```math
\inf_{q\ge q_0}K_{q,q}
\ge\kappa>0.
```

There is no bound of the form

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

valid for all dyadic profiles satisfying:

1. the dissipation-wavenumber threshold definition;
2. the pointwise energy bound `||u(t)||_2<=U_0`;
3. the Leray-form total shell-dissipation budget;
4. `Lambda in L2_t`.

The statement concerns estimate profiles, not Navier–Stokes solutions.

### Proof

Choose a nonzero divergence-free Schwartz field `phi` with Fourier support in a fixed annulus and normalize

```math
\|\phi\|_2=1.
```

For `lambda_q=2^q`, define the rescaled packet

```math
\phi_q(x)
=
\lambda_q^{3/2}\phi(\lambda_qx).
```

Then

```math
\|\phi_q\|_2=1,
\qquad
\|\phi_q\|_\infty
=\lambda_q^{3/2}\|\phi\|_\infty,
\qquad
\|\nabla\phi_q\|_2^2
=\lambda_q^2\|\nabla\phi\|_2^2.
```

Choose pairwise disjoint intervals `I_q` of lengths

```math
\tau_q
=
\frac{\lambda_q^{-5/2}}{q+1},
\qquad q\ge q_0.
```

On `I_q`, set

```math
u_q(t,x)=U_0\phi_q(x),
```

with all other annular shells zero. Outside the union of the intervals set the profile to zero.

For sufficiently large `q_0`,

```math
\lambda_q^{-1}\|u_q\|_\infty
=U_0\|\phi\|_\infty\lambda_q^{1/2}
\ge c_0\nu.
```

Since every shell above `q` is zero, the dissipation wavenumber is exactly `Q(t)=q` on `I_q`.

The pointwise kinetic energy is

```math
\|u(t)\|_2^2=U_0^2.
```

The active-shell dissipation is

```math
D_q(t)
=
\nu U_0^2\|\nabla\phi\|_2^2\lambda_q^2.
```

The critical-wavenumber cost is finite:

```math
\int\Lambda^2dt
=
\sum_{q\ge q_0}\lambda_q^2\tau_q
=
\sum_{q\ge q_0}
\frac{\lambda_q^{-1/2}}{q+1}
<\infty.
```

The total shell dissipation is also finite:

```math
\sum_p\int D_pdt
=
\nu U_0^2\|\nabla\phi\|_2^2
\sum_{q\ge q_0}
\frac{\lambda_q^{-1/2}}{q+1}
<\infty.
```

But the diagonal contribution to the weighted kernel satisfies

```math
\int\mathcal W_Kdt
\ge
\kappa\sum_{q\ge q_0}
\lambda_qD_q\tau_q
```

and hence

```math
\int\mathcal W_Kdt
\gtrsim
\kappa\nu U_0^2
\sum_{q\ge q_0}
\frac{\lambda_q^{1/2}}{q+1}
=\infty.
```

This proves the theorem.

### Scaling check

Each packet box has:

```math
\Lambda^2\tau_q
\asymp
\lambda_q^{-1/2}(q+1)^{-1},
```

```math
D_q\tau_q
\asymp
\nu U_0^2\lambda_q^{-1/2}(q+1)^{-1},
```

and

```math
\lambda_qD_q\tau_q
\asymp
\nu U_0^2\lambda_q^{1/2}(q+1)^{-1}.
```

The first two series converge; the third diverges.

### Disposition

`PROVED_COUNTERFIXTURE`.

## 7. The fixture also saturates the low-mode obstruction

On `I_q`,

```math
f(t)
=
\lambda_q\|u_q(t)\|_\infty
=
U_0\|\phi\|_\infty\lambda_q^{5/2}.
```

Therefore

```math
\int_0^Tf(t)dt
=
U_0\|\phi\|_\infty
\sum_{q\ge q_0}
\lambda_q^{5/2}\tau_q
```

and

```math
\int_0^Tf(t)dt
=
U_0\|\phi\|_\infty
\sum_{q\ge q_0}\frac1{q+1}
=\infty.
```

Thus the same profile has:

```math
\Lambda\in L^2_t,
\qquad
\sum_pD_p\in L^1_t,
\qquad
\sup_t\|u(t)\|_2\le U_0,
```

but

```math
f\notin L^1_t.
```

This does not disprove A2, because the profile is not a Navier–Stokes solution. It proves that no theorem based only on the static threshold definition, energy size, total dissipation, and positive shell bookkeeping can establish the bridge.

## 8. Compatibility with previous estimate constraints

The fixture is static inside each box and has arbitrarily high dissipation charge relative to the previously proved rapid-exit minimum. Indeed,

```math
\mathcal E_q(I_q)
=
\frac{\lambda_q}{\nu^2}
\int_{I_q}D_q(t)dt
\asymp
\frac{U_0^2}{\nu}
\frac{\lambda_q^{1/2}}{q+1}.
```

For large `q`, this exceeds every fixed buffered-exit lower bound. Transition boxes may therefore be appended with the required local charge at total additional physical cost

```math
\sum_qO(\nu^2\lambda_q^{-1})<\infty.
```

The fixture also respects the threshold shell-energy floor because its shell energy is `U_0^2`, much larger than `nu^2 lambda_q^-1` at high frequency.

No claim is made that the packet switching, transition mechanism, or prescribed dissipation matrix solves the Navier–Stokes equation.

## 9. Why diagonal decay does not rescue the proved envelope

Suppose one tries to replace the geometric kernel by a positive kernel with `K_{q,q}->0`. On a single cutoff-shell packet, a square-root estimate of the form

```math
f(t)
\le
C\nu^{-1/2}\Lambda(t)
\mathcal W_K(t)^{1/2}
```

would reduce to

```math
\lambda_q\|u_q\|_\infty
\le
C\nu^{-1/2}\lambda_q
\left(K_{q,q}\lambda_qD_q\right)^{1/2}.
```

For Bernstein-saturating packets,

```math
\left(\lambda_q\|u_q\|_\infty\right)^2
\asymp
\nu^{-1}\lambda_q^3D_q.
```

Consequently the pointwise domination requires

```math
K_{q,q}\gtrsim1.
```

The two requirements are incompatible:

- time-integrated positive column control pushes the diagonal weight toward decay;
- pointwise control of the cutoff-shell contribution requires a nondegenerate diagonal.

This is the exact positive-kernel obstruction.

## 10. Carleson interpretation

The desired positive estimate can be written as the finiteness of

```math
\mathfrak C_D
=
\sum_{0\le p\le q}
2^{-2(q-p)}\lambda_p\mu_{p,q}.
```

The known scalar budgets control only

```math
\sum_{p,q}\mu_{p,q}
```

and

```math
\sum_q\lambda_q^2|E_q|.
```

They impose no upper bound on the diagonal correlation

```math
\mu_{q,q}
=
\int_{E_q}D_q(t)dt.
```

The packet fixture concentrates both the active-set indicator and the maximum admissible shell dissipation on the diagonal. A valid Carleson theorem must therefore use a property of the Navier–Stokes evolution not present in the scalar budgets, such as a signed flux identity, a dynamic depletion mechanism, or a nontrivial correlation inequality.

Calling `mathfrak C_D<infinity` a hypothesis is mathematically valid but merely restates the missing bridge. It is not an A2 proof.

## 11. Proof-obligation DAG disposition

```text
L4-3.1 exact Tonelli column formula
    PROVED
        |
        v
L4-3.2 dimensionless Schur rows/columns
    PROVED
        |
        v
L4-3.3 weighted diagonal audit
    PROVED: coefficient grows like lambda_p
        |
        v
L4-3.4 static budget implication
    REJECTED_COUNTERFIXTURE
        |
        +------------------------------+
        |                              |
        v                              v
positive kernel with            PDE-specific signed or
nondegenerate diagonal          dynamic correlation
    TERMINATED                      OPEN: L4-4
```

## 12. Route disposition

| Candidate | Disposition | Exact reason |
|---|---|---|
| dimensionless geometric row bound | proved | row sum is `4/3` |
| dimensionless geometric column bound | proved | column sum is `4/3` |
| weighted Schur bound against `D_p dt` | rejected | weighted column constant is `(4/3)lambda_p` |
| pointwise energy cap | insufficient | recovers only `S_Q lesssim nu U_0^2 Lambda^3` |
| combine `Lambda L2` and total dissipation | rejected | diagonal packet fixture makes `int S_Q` diverge |
| positive kernel with `K_qq>=kappa` | terminated | general diagonal obstruction theorem |
| positive kernel with decaying diagonal | incompatible with current pointwise envelope | cutoff-shell packets require `K_qq gtrsim 1` |
| weighted Carleson estimate as a new hypothesis | conditional/tautological | it is the missing bridge itself |
| signed or equation-dynamic correlation | open | not tested by this positive-kernel counterfixture |

## 13. Strongest surviving statement

The strongest unconditional statement remains the pointwise envelope

```math
f(t)
\le
C_{LP}U_0
+
C_{LP}\nu^{-1/2}\Lambda(t)S_Q(t)^{1/2}.
```

It becomes useful under the explicit additional hypothesis

```math
S_Q\in L^1(0,T).
```

But `S_Q in L1` is not implied by `Lambda in L2` and Leray energy. The positive weighted-dissipation lane is therefore exhausted at L4-3.

## 14. Next obligation

Proceed to L4-4 only through a genuinely equation-specific mechanism:

1. derive a signed shell or cumulative-flux expression whose time integral telescopes without taking absolute values;
2. identify a commutator or depletion term that cancels the diagonal cutoff-shell contribution;
3. prove a dynamic decorrelation estimate between `D_q` and `{Q=q}`;
4. or terminate L4 and promote the independent direct critical-integral lane L5.

No further positive Schur variant is admissible unless it defeats the diagonal theorem explicitly.

## Claim boundary

This package proves the failure of a class of positive weighted-column arguments under the source-level static and energy constraints. It does not construct a Navier–Stokes counterexample, disprove A2, or rule out signed, nonlinear, or equation-specific weighted dissipation estimates.