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

This tranche tests the smallest safe B1 successor from L5-4. It uses finite-shell
Navier--Stokes enstrophy balances rather than another static rearrangement. The
direct moving-low-enstrophy identity recreates selector variation and a selected
non-conservative enstrophy-production term. Coupling the complementary finite
high block cancels selector variation algebraically before any infinite-shell
limit, but the resulting low-amplitude coefficient reduces exactly to the
already protected L4 weighted-column quantity `S_Q`, including its active
diagonal. This B1 candidate family is therefore terminated without reopening
L4.

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
W_{\le Q}(t)=\sum_{p\le Q(t)}\lambda_p^2A_p(t).
```

The protected L4 weighted-column quantity is

```math
S_Q(t)
=
\sum_{p\le Q(t)}
2^{-2(Q(t)-p)}\lambda_pD_p(t),
\qquad
D_p(t)=\nu A_p(t).
```

Its cutoff-shell diagonal is

```math
\sum_q\lambda_q\int_{\{Q=q\}}D_q(t)dt.
```

The protected L4 reopening conditions remain selected-transfer cancellation,
active-set variation, active-diagonal depletion, commutator closure, or genuine
dynamic decorrelation.

## 2. Direct B1 equation: moving low enstrophy

Use mutually orthogonal dyadic projections for the exact finite-shell ledger;
smooth Littlewood--Paley blocks differ only by fixed overlap constants. For a
fixed cutoff `q`, define

```math
\mathcal E_{\le q}
=\frac12\sum_{p\le q}\lambda_p^2\|P_pu\|_2^2,
```

```math
\mathcal H_{\le q}
=\sum_{p\le q}\lambda_p^4\|P_pu\|_2^2.
```

On smooth Galerkin approximants, with `mathcal N_{<=q}` the projected nonlinear
enstrophy production,

```math
\frac d{dt}\mathcal E_{\le q}
+\nu\mathcal H_{\le q}
=\mathcal N_{\le q}.
```

Up to fixed annular constants,

```math
\mathcal H_{\le Q}\simeq W_{\le Q}.
```

Let

```math
\chi_q=1_{\{Q=q\}}.
```

If the selectors are temporarily taken to have bounded variation, multiplying
the finite-shell identity by `chi_q`, integrating, and summing gives the formal
candidate ledger

```math
\nu\int_0^T W_{\le Q}dt
\simeq
\sum_q\int\chi_q\mathcal N_{\le q}dt
+
\sum_q\int\mathcal E_{\le q}\,d\chi_q
-
\sum_q[\chi_q\mathcal E_{\le q}]_0^T.
```

This exposes two equation-level obligations before any estimate:

1. `mathcal N_{<=q}` is an H1/enstrophy-production term. Unlike the shell
   L2-energy transfer, its all-shell sum is not zero in three dimensions; the
   residual is vortex stretching.
2. The Stieltjes term requires selector variation. `Lambda in L2_t` controls
   weighted occupancy but not the number or total variation of active
   components.

Thus the direct localized B1 identity does not furnish the desired correlation
estimate.

## 3. Finite-shell complementary coupling cancels selector variation

The selector term can be removed algebraically without assuming a global H1
identity for a Leray--Hopf solution. Fix a terminal shell `N`. For `q<N`, set

```math
\mathcal E_{q<p\le N}
=\frac12\sum_{q<p\le N}\lambda_p^2\|P_pu\|_2^2.
```

Then exactly

```math
\mathcal E_{\le q}+\mathcal E_{q<p\le N}
=\mathcal E_{\le N},
```

and the right side is independent of `q`. Therefore, for every finite set of
active selectors,

```math
\sum_q\int
(\mathcal E_{\le q}+\mathcal E_{q<p\le N})\,d\chi_q
=
\int\mathcal E_{\le N}\,d\left(\sum_q\chi_q\right)
=0.
```

This is a finite-dimensional algebraic identity. It does not assert global H1
regularity, bounded variation of the actual dissipation wavenumber, or passage
of a full enstrophy equality to an arbitrary Leray--Hopf solution. Its role is
only to show that the B4 term is not intrinsic to a candidate that keeps both
complementary finite blocks.

After this cancellation, the finite-shell nonlinear enstrophy production still
contains the three-dimensional stretching/low-deformation contribution. The
standard dissipation-wavenumber split absorbs strictly high interactions when
its threshold constant is sufficiently small, but terms carrying a low mode
leave the coefficient

```math
f(t)
:=
\sup_{p\le Q(t)}\lambda_p\|u_p(t)\|_\infty.
```

No `f in L1_t` conclusion is imported.

## 4. Exact half-integrability factorization

Define

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

Hence

```math
f(t)^2
\lesssim
\sum_{p\le Q}\lambda_p^3A_p
=
\Lambda(t)^3D_3(t),
```

or

```math
\boxed{
f(t)
\lesssim
\Lambda(t)^{3/2}D_3(t)^{1/2}.
}
```

Since the geometric weights are at most one,

```math
D_3(t)\le\sum_pA_p(t),
```

so Leray gives `D_3^(1/2) in L2_t`. The selected hypothesis gives
`Lambda^(3/2) in L^(4/3)_t`. Hölder would need `D_3^(1/2) in L4_t` to make this
product integrable; that input is absent.

The energy cap yields the consistency endpoint

```math
D_3(t)\lesssim U_0^2\Lambda(t)^2,
\qquad
f(t)\lesssim U_0\Lambda(t)^{5/2},
```

but this does not close under `Lambda in L2_t`.

## 5. The missing bridge is exactly the closed L4 column

Cauchy--Schwarz gives

```math
\int f(t)dt
\lesssim
\left(\int\Lambda^2dt\right)^{1/2}
\left(\int\Lambda D_3dt\right)^{1/2}.
```

Using `Lambda=lambda_Q` and `D_p=nu A_p`,

```math
\nu\Lambda D_3
=
\nu\sum_{p\le Q}\frac{\lambda_p^3}{\Lambda^2}A_p
```

```math
=
\sum_{p\le Q}
\left(\frac{\lambda_p}{\Lambda}\right)^2
\lambda_pD_p
```

```math
=
\sum_{p\le Q}2^{-2(Q-p)}\lambda_pD_p
=S_Q.
```

Thus

```math
\boxed{\nu\Lambda D_3=S_Q}
```

pointwise, with no inequality and no loss. The `p=Q` term is exactly
`lambda_Q D_Q`, so integration over the active sets reproduces the protected L4
active diagonal.

Consequently the selector-free B1 repair is not a new decorrelation theorem. It
is algebraically the closed L4 weighted-column interface. No L4 reopening
condition is established here.

## 6. Static adversarial check for the half-power gap

This fixture rejects accidental functional-analytic closure after the PDE
reduction; it is not an NSE solution.

Choose pairwise disjoint intervals, dyadic `Lambda=lambda_q=lambda`, and

```math
|I_q|=\lambda^{-9/4},
\qquad
A_q=\lambda^2,
\qquad
E_q=1,
```

with an active annular packet saturating Bernstein and all higher shells zero.
Then

```math
\sum\Lambda^2|I_q|
=\sum\lambda^{-1/4}<\infty,
```

```math
\sum A_q|I_q|
=\sum\lambda^{-1/4}<\infty,
```

while `f_q asymp lambda^(5/2)` gives

```math
\sum f_q|I_q|
\asymp\sum\lambda^{1/4}=\infty.
```

The pointwise energy remains bounded. This fixture does not make any assertion
about an actual Navier--Stokes trajectory.

## 7. Literature consistency check

Cheskidov and Shvydkoy, *A unified approach to regularity problems for the 3D
Navier--Stokes and Euler equations: the use of Kolmogorov's dissipation range*,
Journal of Mathematical Fluid Mechanics 16 (2014), use the same low-mode
coefficient and obtain the bounds `Lambda^2 lesssim f lesssim Lambda^(5/2)` and
a regularity criterion under the stronger `Lambda in L^(5/2)_t` condition.
This is a consistency check only; that stronger hypothesis is not imported into
A2.

## 8. B1 disposition and successor

The bounded family has the reduction

```text
MOVING_LOW_ENSTROPHY
    -> selected non-conservative enstrophy production + B4 selector variation;

FINITE_COMPLEMENTARY_COUPLING
    -> selector cancellation at terminal shell N
    -> low coefficient f
    -> exact factor nu Lambda D_3 = S_Q
    -> protected L4 active diagonal.
```

Therefore

```text
B1_DIRECT_DYNAMIC_ROUTE_REDUCED__SELECTOR_FREE_REPAIR_EQUALS_CLOSED_L4_COLUMN.
```

This terminates this B1 candidate family; it does not prove that no other
Navier--Stokes correlation theorem for B1 exists.

Per L5-4, the next safe move is B3 through a mechanism different from
moving-tail H1 energy, fixed-tail bad-set splitting, threshold-residence
Duhamel, or the L4 weighted column. The direct projected `L6` transport candidate
is audited separately in `NS_CI_R014_A2_L5_B3_L6_TRANSPORT_AUDIT.md`.

## Claim boundary

A2 remains unproved. This tranche neither proves nor refutes the Navier--Stokes
target, does not reopen L4, does not establish `f in L1_t`, assumes no global H1
identity for the Leray--Hopf solution, and creates no MATHCERT certification or
claim promotion.