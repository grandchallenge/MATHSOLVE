# NS-CI-R014-A2-L5-4 — Zero-gap strict tail and dynamic endpoint audit

## Disposition

- Campaign: `NS-CI-001`
- Restricted target: `NS-CI-R014-A2`
- Tracker: `MATHSOLVE#59`
- Protected source head at tranche start: `20358ac7630b4c9a6033e352a3a9a425f82bd3fb`
- Predecessor: `NS_CI_R014_A2_L5_PRETRIANGLE_STRICT_TAIL.md`
- Result: `ZERO_GAP_REDUCTION_PROVED__STATIC_B1_ENDPOINT_SEPARATED__PARABOLIC_B3_ROUTE_REDUCED`
- A2 theorem: open
- MATHCERT adjudication: absent

This tranche sharpens the direct critical-integral route in three bounded ways.
First, the pre-triangle strict-tail proof requires no fixed buffer `K`: every
shell `p>Q(t)` already satisfies the defining strict-high inequality. Second,
the low side is reduced to one exact weighted endpoint and a static
threshold-compatible fixture separates that endpoint from the admitted scalar
budgets. Third, the first parabolic attempt on the high `H^2` endpoint is
traced to its first genuinely dynamic inputs: low-mode deformation, moving
selector variation, or defining-threshold residence.

The result does not prove or refute A2 and does not reopen L3 or L4.

## 1. Imported interface

For annular blocks write

```math
E_q=\|u_q\|_2^2,
\qquad
A_q=\lambda_q^2E_q.
```

At almost every time with finite `Q=Q(t)`, the dissipation-wavenumber
definition supplies

```math
\|u_p\|_\infty<c_0\nu\lambda_p
\qquad\text{for every }p>Q,
```

and supplies no corresponding upper bound at `p=Q` or below. The admitted
budgets remain

```math
\sup_t\|u(t)\|_2\le U_0,
\qquad
\int_0^T\sum_{q\ge0}A_q(t)dt<\infty,
\qquad
\int_0^T\Lambda(t)^2dt<\infty.
```

The fixed inhomogeneous base block remains the previously admitted
finite-frequency remainder.

## 2. L5-4A — zero-gap strict-tail theorem

Define

```math
u_{>Q}=\sum_{p>Q}u_p,
\qquad
S_{>Q,N}^2=\sum_{Q<p\le N}|u_p|^2.
```

Here the first displayed symbol is the velocity tail `u_{>Q}`; no viscosity
factor is introduced.

### Proposition 2.1 — quartic tail

Uniformly in terminal index `N`,

```math
\|u_{Q<p\le N}\|_4^4
\lesssim
c_0^2\nu^2\sum_{Q<p\le N}A_p.
```

Consequently

```math
\int_0^T\|u_{>Q}(t)\|_4^4dt
\lesssim
c_0^2\nu U_0^2.
```

Before Minkowski,

```math
\|S_{>Q,N}\|_4^4
=
\sum_{Q<p,r\le N}\int|u_p|^2|u_r|^2dx.
```

For an ordered pair `Q<p<=r`, both blocks are strict high, so

```math
\int|u_p|^2|u_r|^2dx
\le
c_0^2\nu^2
\left(\frac{\lambda_p}{\lambda_r}\right)^2A_r.
```

The row sum is uniformly bounded:

```math
\sum_{Q<p\le r}
\left(\frac{\lambda_p}{\lambda_r}\right)^2
\le
\sum_{j\ge0}4^{-j}
=
\frac43.
```

The Littlewood--Paley equivalence and continuum passage from L5-3 therefore
apply with lower index `Q+1`; no step requires `Q+K+1`.

### Proposition 2.2 — sextic tail

Uniformly in `N`,

```math
\|u_{Q<p\le N}\|_6^6
\lesssim
c_0^4\nu^4
\sum_{Q<s\le N}\lambda_s^2A_s.
```

Equivalently,

```math
\|u_{>Q}\|_6^4
\lesssim
c_0^{8/3}\nu^{8/3}Z_{>Q}^{2/3},
```

where

```math
Z_{>Q}(t)
:=
\sum_{p>Q(t)}\lambda_p^2A_p(t).
```

Indeed, for `Q<p<=r<=s`,

```math
\int|u_p|^2|u_r|^2|u_s|^2dx
\le
c_0^4\nu^4
\frac{\lambda_p^2\lambda_r^2}{\lambda_s^2}A_s.
```

Deleting the absent indices `p,r<=Q` can only decrease the nonnegative ordered
triple sum, hence

```math
\sum_{Q<r\le s}\sum_{Q<p\le r}
\frac{\lambda_p^2\lambda_r^2}{\lambda_s^2}
\le
\frac{64}{45}\lambda_s^2.
```

The six orderings and Littlewood--Paley equivalence change only the absolute
constant. Thus the same `H^2` endpoint from L5-3 begins immediately above `Q`.

## 3. Two-block master inequality

Use the exact split

```math
u=u_{\le Q}+u_{>Q}.
```

The norm triangle and `(a+b)^4<=8(a^4+b^4)` give

```math
\|u\|_6^4
\lesssim
\|u_{\le Q}\|_6^4
+
\|u_{>Q}\|_6^4.
```

For the annular low blocks, L5-1 proved

```math
\|u_{\le Q}\|_6^4
\lesssim
U_0^2W_{\le Q}
+
\text{fixed-base remainder},
```

where

```math
W_{\le Q}(t)
:=
\sum_{0\le r\le Q(t)}\lambda_r^2A_r(t).
```

Therefore

```math
\boxed{
\|u(t)\|_6^4
\lesssim
U_0^2W_{\le Q}(t)
+
c_0^{8/3}\nu^{8/3}Z_{>Q}(t)^{2/3}
+
\text{fixed-base remainder}.
}
```

The direct L5 route is now reduced to

```math
\int_0^T W_{\le Q}(t)dt<\infty
```

and

```math
\int_0^T Z_{>Q}(t)^{2/3}dt<\infty,
```

or to a new identity coupling or avoiding those endpoints.

## 4. B2 disposition inside the pointwise L5 representation

The earlier core/near/tail split protected the threshold direction. The
zero-gap proof preserves the same firewall more directly:

- `p=Q` belongs to `u_{<=Q}` and receives no strict-high upper bound;
- every `p>Q` belongs to `u_{>Q}` and receives the defining upper bound.

Hence no standalone near-cluster square is needed in this pointwise norm
representation:

```text
B2_STANDALONE_BLOCKER_REMOVED_FROM_POINTWISE_L5_DECOMPOSITION.
```

This statement is deliberately local to this representation. Dynamic projected
energy or commutator identities may still create finite-neighbour terms near
`Q`; no global near-threshold depletion theorem is claimed.

## 5. L5-4B — exact low weighted endpoint and static separation

Tonelli gives the exact layer form

```math
\int_0^T W_{\le Q}(t)dt
=
\sum_{r\ge0}\lambda_r^2
\int_{\{t:Q(t)\ge r\}}A_r(t)dt.
```

Thus B1 is a correlation problem between shell dissipation and the superlevel
event `Q>=r`, not merely a summation problem.

### Static threshold-compatible fixture

Let

```math
q_n=6n,
\qquad
\lambda_{q_n}=2^{6n},
\qquad
|I_n|=2^{-18n},
```

on pairwise disjoint time intervals, and set `Q=q_n` on `I_n`. Put one active
threshold shell at `q_n` with

```math
A_{q_n}\asymp\nu^2\lambda_{q_n},
\qquad
E_{q_n}\asymp\nu^2\lambda_{q_n}^{-1}.
```

A fixed divergence-free annular packet scaled with this `L2` size has
`L-infinity` size comparable to `nu lambda_{q_n}`. Choosing its fixed amplitude
constant above the defining threshold makes `q_n` fail the strict-high test,
while all shells above `q_n` vanish; hence `Q=q_n` is compatible with the
minimum definition.

The admitted scalar budgets are finite:

```math
\sum_n\lambda_{q_n}^2|I_n|
\asymp
\sum_n2^{-6n}<\infty,
```

```math
\sum_nA_{q_n}|I_n|
\asymp
\nu^2\sum_n2^{-12n}<\infty,
```

and the kinetic energy is uniformly bounded because

```math
E_{q_n}\asymp\nu^2 2^{-6n}.
```

But every interval contributes a frequency-independent amount to the weighted
low endpoint:

```math
\lambda_{q_n}^2A_{q_n}|I_n|
\asymp
\nu^2,
```

so

```math
\int_0^T W_{\le Q}(t)dt=\infty.
```

This is a static shell/packet fixture, not a Navier--Stokes solution. It proves
only that `Lambda in L2`, Leray energy/dissipation, and the threshold definition
do not control B1 by scalar Holder, occupancy, or shell-energy rearrangement.
An actual B1 advance must use equation-specific dynamics.

## 6. L5-4C — first parabolic audit of B3

For a fixed cutoff `q`, write schematically

```math
V_q=P_{>q}u,
\qquad
Y_q=\|\nabla V_q\|_2^2,
\qquad
Z_q=\|\Delta V_q\|_2^2,
```

up to fixed Littlewood--Paley equivalence constants. The principal low--high
transport is

```math
u_{\le q-2}\cdot\nabla V_q.
```

Here again the displayed leading symbol denotes the velocity `u_{<=q-2}`.
At `L2` level incompressibility removes its pure transport contribution. At
`H1` level,

```math
\nabla(u_{\le q-2}\cdot\nabla V_q)
=
(\nabla u_{\le q-2})\nabla V_q
+
u_{\le q-2}\cdot\nabla\nabla V_q,
```

where the final leading symbol also denotes `u_{<=q-2}`. The second term is
skew after integration, but the first leaves the genuine deformation term

```math
\left|
\int(\nabla u_{\le q-2})\nabla V_q:\nabla V_q\,dx
\right|
\le
G_qY_q,
```

with

```math
G_q(t):=\|\nabla u_{\le q-2}(t)\|_\infty.
```

This coefficient lies below the cutoff and receives no strict-high smallness.
Thus, even if every strictly high remainder were optimistically absorbed by
viscosity, a low-mode deformation input remains before `nu Z_q` can be
controlled.

### Moving active cutoff

If the fixed-`q` estimate is localized to

```math
E_q=\{t:Q(t)=q\},
```

then integration of the `Y_q'` term against `1_{E_q}` produces the
selector-boundary ledger

```math
\int Y_q\,d1_{E_q}
```

when the selector has bounded variation, and has no finite-measure estimate
otherwise. `Lambda in L2` controls occupancy, not weighted variation. This is
the protected B4 interface; no variation theorem is supplied here.

### Fixed cutoff instead of selector differentiation

Holding `q` fixed removes selector differentiation, but strict-high absorption
for all blocks `p>q` is guaranteed only on `{Q<=q}`. On `{Q>q}` the selected
hypothesis yields only

```math
|\{t:Q(t)>q\}|
\le
\lambda_{q+1}^{-2}
\int_0^T\Lambda(t)^2dt,
```

which supplies no corresponding control of `Y_q` or `Z_q^{2/3}`. A theorem
turning this small occupancy into the required parabolic control would be new
dynamic information of the residence/depletion type audited in L3.

### Backward Duhamel variant

A backward parabolic representation around an active time avoids explicit
selector differentiation only if the defining strict-high condition persists
on a frequency-scale time window. Actual parabolic residence at the defining
threshold is an explicit protected L3 reopening condition and is not supplied
by the present hypothesis.

Therefore the first B3 parabolic family reduces as follows:

```text
MOVING_TAIL_H1_ENERGY
    -> low deformation G_q + selector variation;
FIXED_TAIL_H1_ENERGY
    -> bad-time control requiring residence/depletion;
BACKWARD_DUHAMEL
    -> defining-threshold parabolic residence.
```

This is a bounded route reduction, not an exhaustion theorem for all possible
PDE-specific B3 mechanisms.

## 7. Updated residual ledger

| Blocker | L5-4 state | Exact obligation |
|---|---|---|
| B1 low core | sharpened | control `int W_{<=Q}` by an equation-specific correlation/depletion theorem; the new fixture excludes further static scalar rearrangement |
| B2 near threshold | collapsed in pointwise L5 | no standalone cluster in `u=u_{<=Q}+u_{>Q}`; `p=Q` remains low; dynamic finite-neighbour terms may still occur |
| B3 strict tail | sharpened and dynamically audited | control `int Z_{>Q}^{2/3}` or avoid it; first parabolic route imports low deformation and B4/L3 interfaces |
| B4 selector motion | unchanged | arises when a dynamic proof differentiates or localizes the moving cutoff |

## 8. Successor state

The direct L5 target is now represented by two exact non-static endpoints:

```math
W_{\le Q}(t)
=
\sum_{r\le Q(t)}\lambda_r^2A_r(t)
```

and

```math
Z_{>Q}(t)^{2/3}
=
\left(
\sum_{p>Q(t)}\lambda_p^2A_p(t)
\right)^{2/3}.
```

The smallest safe successor is B1-first: seek one actual Navier--Stokes
correlation/depletion estimate for

```math
\sum_r\lambda_r^2
\int_{\{Q\ge r\}}A_r(t)dt.
```

The next B1 attempt must use the equation to decorrelate shell dissipation from
`Q>=r`; static Holder, occupancy, threshold-energy floors, and packet counting
are excluded by the fixture above. If that bounded candidate fails, record its
first exact PDE obstruction before returning to a B3 mechanism genuinely
different from moving-tail `H1` energy, fixed-tail bad-set splitting, or
threshold-residence Duhamel.

## Claim boundary

This package proves the zero-gap strict-tail estimates, the two-block pointwise
reduction, and the stated static separation of the low weighted endpoint. It
also identifies the unavoidable low-deformation/selector/residence interfaces
in the first parabolic B3 family. It does not prove or refute
`NS-CI-R014-A2`, universal critical integrability, or global Navier--Stokes
regularity; it does not reopen L3 or L4; it performs no MATHCERT adjudication;
and it creates no novelty, priority, publication, patentability, product, or
commercial claim.
