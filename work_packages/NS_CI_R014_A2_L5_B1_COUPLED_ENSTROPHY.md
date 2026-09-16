# NS-CI-R014-A2-L5-5 — B1 coupled-enstrophy audit

## Disposition

- Campaign: `NS-CI-001`
- Restricted target: `NS-CI-R014-A2`
- Tracker: `MATHSOLVE#59`
- Protected source head at tranche start: `6d0f94ad3227490826611473a40b92cadfbad577`
- Predecessor: `NS_CI_R014_A2_L5_ZERO_GAP_DYNAMIC_AUDIT.md`
- Result: `B1_DIRECT_DYNAMIC_ROUTE_REDUCED__SELECTOR_FREE_REPAIR_EQUALS_CLOSED_L4_COLUMN`
- A2 theorem: open
- L5: active
- MATHCERT adjudication: absent

This tranche tests the smallest safe B1 successor from L5-4. It uses the
Navier--Stokes enstrophy balance rather than another static rearrangement. The
direct moving-low-enstrophy identity recreates selector variation and a selected
non-conservative enstrophy-production term. Coupling the low and high enstrophy
balances cancels selector variation exactly, but the resulting low-amplitude
coefficient reduces algebraically to the already protected L4 weighted-column
quantity `S_Q`, including its active diagonal. Therefore this B1 dynamic family
is terminated without reopening L4.

## 1. Imported interface

For annular blocks,

```math
E_p=\|u_p\|_2^2,
\qquad
A_p=\lambda_p^2E_p,
\qquad
\Lambda=\lambda_Q.
```

The selected assumptions provide

```math
\sup_t\|u(t)\|_2\le U_0,
\qquad
\int_0^T\sum_p A_p(t)dt<\infty,
\qquad
\int_0^T\Lambda(t)^2dt<\infty.
```

The L5-4 low endpoint is

```math
W_{\le Q}(t)=\sum_{p\le Q(t)}\lambda_p^2A_p(t),
```

and B1 asks for equation-specific control of `integral W_{<=Q}`.

The protected L4 weighted-column quantity is

```math
S_Q(t)
=
\sum_{p\le Q(t)}
2^{-2(Q(t)-p)}\lambda_pD_p(t),
\qquad
D_p(t)=\nu A_p(t).
```

L4 proved that its positive-kernel route is not controlled by the selected
static budgets and that the diagonal

```math
\sum_q\lambda_q\int_{\{Q=q\}}D_q(t)dt
```

requires a genuinely new selected-transfer cancellation, active-set variation
theorem, active-diagonal depletion, commutator closure, or dynamic
decorrelation result.

## 2. Direct B1 equation: moving low enstrophy

Use mutually orthogonal dyadic projections for the exact balance and compare
with the smooth Littlewood--Paley blocks by fixed overlap constants. For a fixed
cutoff `q`, define

```math
\mathcal E_{\le q}
=\frac12\sum_{p\le q}\lambda_p^2\|P_pu\|_2^2,
```

```math
\mathcal H_{\le q}
=\sum_{p\le q}\lambda_p^4\|P_pu\|_2^2,
```

and let `\mathcal N_{\le q}` denote the corresponding projected nonlinear
enstrophy production. On smooth Galerkin approximants,

```math
\frac d{dt}\mathcal E_{\le q}
+\nu\mathcal H_{\le q}
=\mathcal N_{\le q}.
```

Up to fixed annular-equivalence constants,

```math
\mathcal H_{\le Q}\simeq W_{\le Q}.
```

Let

```math
\chi_q=1_{\{Q=q\}}.
```

If the selectors are temporarily taken to have bounded variation, multiplication
by `chi_q`, integration in time, and summation in `q` give

```math
\nu\int_0^T W_{\le Q}dt
\simeq
\sum_q\int\chi_q\mathcal N_{\le q}dt
+
\sum_q\int\mathcal E_{\le q}\,d\chi_q
-
\sum_q[\chi_q\mathcal E_{\le q}]_0^T.
```

This exposes two equation-level obligations before any estimate is made:

1. `mathcal N_{<=q}` is an H1/enstrophy production term. Unlike the shell
   L2-energy transfer in L4, its sum over all shells is not zero in 3D; the
   global remainder is vortex stretching.
2. The Stieltjes term requires weighted variation of the moving selector. The
   hypothesis `Lambda in L2_t` controls occupancy but not the number or total
   variation of active components. This is the protected B4 interface.

Thus the direct localized B1 energy identity does not by itself furnish the
required correlation estimate.

## 3. Coupled low/high repair cancels B4 exactly

The selector term is mechanical rather than intrinsic if the complementary high
enstrophy balance is retained. For every fixed `q`, write

```math
\mathcal E
=\mathcal E_{\le q}+\mathcal E_{>q}.
```

Summing the low and high identities with the same selector gives

```math
\sum_q\int
(\mathcal E_{\le q}+\mathcal E_{>q})\,d\chi_q
=
\int\mathcal E\,d\left(\sum_q\chi_q\right)
=0
```

for finite approximants, because exactly one active selector is present. Passing
through finite shell cutoffs therefore shows that a coupled argument can remove
the selector-variation ledger rather than assuming B4.

After this cancellation one is back at the full enstrophy balance

```math
\frac12\frac d{dt}\|\nabla u\|_2^2
+\nu\|\Delta u\|_2^2
=\text{vortex-stretching/nonlinear enstrophy production}.
```

The dissipation-wavenumber split can absorb strictly high interactions when the
threshold constant is chosen sufficiently small, but terms carrying a low mode
leave the standard low deformation/amplitude coefficient

```math
f(t)
:=
\sup_{p\le Q(t)}\lambda_p\|u_p(t)\|_\infty.
```

No `f in L1_t` conclusion is imported here. The next section derives directly
what the selected budgets say about this coefficient.

## 4. Exact half-integrability factorization

Define the geometrically weighted low dissipation density

```math
D_3(t)
:=
\sum_{p\le Q(t)}
\left(\frac{\lambda_p}{\Lambda(t)}\right)^3A_p(t).
```

Bernstein gives

```math
\lambda_p^2\|u_p\|_\infty^2
\lesssim
\lambda_p^3A_p.
```

Therefore

```math
f(t)^2
\lesssim
\sum_{p\le Q}\lambda_p^3A_p
=
\Lambda(t)^3D_3(t),
```

hence

```math
\boxed{
f(t)
\lesssim
\Lambda(t)^{3/2}D_3(t)^{1/2}.
}
```

Because the geometric weights are at most one,

```math
D_3(t)\le\sum_pA_p(t),
```

so Leray gives

```math
D_3^{1/2}\in L^2_t.
```

Under the selected hypothesis,

```math
\Lambda^{3/2}\in L^{4/3}_t.
```

Hölder would require `D_3^{1/2} in L4_t` to make the displayed product
integrable. The admitted budgets give only `L2_t`. This is the exact
half-integrability gap in this factorization.

The energy cap also yields the familiar pointwise endpoint

```math
D_3(t)
\lesssim U_0^2\Lambda(t)^2,
```

and therefore

```math
f(t)\lesssim U_0\Lambda(t)^{5/2}.
```

This is a consistency check, not a route for the selected `Lambda in L2_t`
hypothesis.

## 5. The missing bridge is exactly the closed L4 column

A Cauchy--Schwarz factorization of the preceding bound gives

```math
\int f(t)dt
\lesssim
\left(\int\Lambda^2dt\right)^{1/2}
\left(\int\Lambda D_3dt\right)^{1/2}.
```

But, using `Lambda=lambda_Q` and `D_p=nu A_p`,

```math
\nu\Lambda D_3
=
\nu\sum_{p\le Q}
\frac{\lambda_p^3}{\Lambda^2}A_p
```

```math
=
\sum_{p\le Q}
\left(\frac{\lambda_p}{\Lambda}\right)^2
\lambda_pD_p
```

```math
=
\sum_{p\le Q}
2^{-2(Q-p)}\lambda_pD_p
=S_Q.
```

Thus

```math
\boxed{
\nu\Lambda D_3=S_Q
}
```

pointwise, with no inequality and no loss.

The cutoff-shell term `p=Q` is

```math
\lambda_QD_Q,
```

so after integration over `E_Q={Q=q}` the exact protected L4 active diagonal
reappears:

```math
\sum_q\lambda_q\int_{E_q}D_qdt.
```

Consequently the selector-free coupled B1 repair is not a new decorrelation
mechanism. It is algebraically identical to the L4 weighted-column interface.
Reopening it would require one of the protected L4 reopening theorems, none of
which is supplied by this tranche.

## 6. Static adversarial check for the half-power gap

This fixture is used only to reject accidental functional-analytic closure after
the PDE reduction; it is not an NSE solution.

On pairwise disjoint time intervals choose dyadic `Lambda=lambda_q=lambda`,

```math
|I_q|=\lambda^{-9/4},
\qquad
A_q=\lambda^2,
\qquad
E_q=1,
```

with a threshold-compatible annular packet saturating Bernstein at the active
shell and all higher shells zero. Then

```math
\sum\Lambda^2|I_q|
=\sum\lambda^{-1/4}<\infty,
```

and

```math
\sum A_q|I_q|
=\sum\lambda^{-1/4}<\infty,
```

while the active shell can have

```math
f_q\asymp\lambda^{5/2},
```

so

```math
\sum f_q|I_q|
\asymp\sum\lambda^{1/4}=\infty.
```

The pointwise energy remains bounded. This shows that once the equation-level
calculation has reduced to `f`, the selected scalar budgets still cannot supply
the missing half power.

## 7. Literature consistency check

Cheskidov and Shvydkoy, *A unified approach to regularity problems for the 3D
Navier--Stokes and Euler equations: the use of Kolmogorov's dissipation range*,
Journal of Mathematical Fluid Mechanics 16 (2014), derive the same low-mode
coefficient and the bounds `Lambda^2 lesssim f lesssim Lambda^(5/2)` and prove
regularity under the stronger `Lambda in L^(5/2)_t` condition. This tranche does
not import that theorem as an A2 proof; the source is used only to check that the
independently derived coefficient and exponent gap are aligned with the
established dissipation-wavenumber framework.

## 8. B1 disposition and successor

The bounded B1 family tested here has two branches:

```text
MOVING_LOW_ENSTROPHY
    -> selected non-conservative enstrophy production + B4 selector variation;

COUPLED_LOW_HIGH_ENSTROPHY
    -> selector cancellation
    -> low coefficient f
    -> exact factor nu Lambda D_3 = S_Q
    -> protected L4 active diagonal.
```

Therefore

```text
B1_DIRECT_DYNAMIC_ROUTE_REDUCED__SELECTOR_FREE_REPAIR_EQUALS_CLOSED_L4_COLUMN.
```

This terminates this B1 candidate family. It does not prove that no other
Navier--Stokes correlation theorem for B1 exists.

Per the protected L5-4 handoff, the next safe move is to return to B3 only
through a mechanism genuinely different from moving-tail H1 energy,
fixed-tail bad-set splitting, threshold-residence Duhamel, or the L4 weighted
column. A direct `L6` transport-energy formulation is admissible only if its
high-pass/Leray commutators avoid the same low deformation coefficient; that is
the next bounded falsification target.

## Claim boundary

A2 remains unproved. This tranche neither proves nor refutes the Navier--Stokes
target, does not reopen L4, does not establish `f in L1_t`, and creates no
MATHCERT certification or claim promotion.