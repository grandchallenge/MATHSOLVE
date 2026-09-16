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

This tranche sharpens the direct critical-integral decomposition in two ways.
First, the pre-triangle strict-tail estimate does not require a fixed buffer
`K>=2`: every Littlewood--Paley block with index `p>Q(t)` already satisfies the
defining strict-high inequality. Hence the direct L5 norm decomposition can be
reduced from core/near/tail to the exact two-block split

```math
u=u_{\le Q}+u_{>Q}.
```

The previously separate B2 near-threshold cluster is therefore not an
independent blocker in this particular L5 representation. The uncontrolled
threshold block `p=Q` remains on the low side; every block `p>Q` is strict high.

Second, the low side has an exact weighted endpoint that can itself be
separated from the admitted scalar budgets by a threshold-compatible static
fixture. A subsequent parabolic audit shows that trying to use viscosity to
control the high `H^2` endpoint necessarily introduces either low-mode
deformation, moving-selector boundary terms, or a threshold-residence theorem.
Those are genuinely dynamic inputs, not consequences of the static L5
budgets.

The result does not close A2 and does not reopen L3 or L4.

## 1. Imported interface

Use the protected normalization

```math
E_q=\|u_q\|_2^2,
\qquad
A_q=\lambda_q^2E_q,
```

with

```math
\|u_p\|_\infty<c_0\nu\lambda_p
\qquad\text{for every }p>Q(t),
```

and no such upper estimate at `p=Q(t)` or below.

The admitted time budgets remain

```math
\sup_t\|u(t)\|_2\le U_0,
\qquad
\int_0^T\sum_{q\ge0}A_q(t)dt<\infty,
\qquad
\int_0^T\Lambda(t)^2dt<\infty.
```

The fixed inhomogeneous base block is retained as the previously admitted
finite-frequency remainder.

## 2. L5-4A — zero-gap strict-tail theorem

Define, at a time with finite `Q`,

```math
u_{>Q}=\sum_{p>Q}u_p,
\qquad
S_{>Q,N}^2=\sum_{Q<p\le N}|u_p|^2.
```

### Proposition 2.1 — quartic strict tail with `K=0`

Uniformly in the terminal index `N`,

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

### Proof

Before Minkowski,

```math
\|S_{>Q,N}\|_4^4
=
\sum_{Q<p,r\le N}\int|u_p|^2|u_r|^2dx.
```

For an ordered pair `Q<p<=r`, both blocks are strict high and therefore

```math
\int|u_p|^2|u_r|^2dx
\le
c_0^2\nu^2
\left(\frac{\lambda_p}{\lambda_r}\right)^2A_r.
```

The truncated row sum is no larger than the full geometric sum

```math
\sum_{Q<p\le r}
\left(\frac{\lambda_p}{\lambda_r}\right)^2
\le
\sum_{j\ge0}4^{-j}
=
\frac43.
```

The same Littlewood--Paley and continuum passage used in L5-3 now applies with
lower index `Q+1`; no step requires `Q+K+1`.

### Proposition 2.2 — sextic strict tail with `K=0`

Uniformly in `N`,

```math
\|u_{Q<p\le N}\|_6^6
\lesssim
c_0^4\nu^4
\sum_{Q<s\le N}\lambda_s^2A_s,
```

and hence

```math
\|u_{>Q}\|_6^4
\lesssim
c_0^{8/3}\nu^{8/3}
Z_{>Q}^{2/3},
```

where

```math
Z_{>Q}(t)
:=
\sum_{p>Q(t)}\lambda_p^2A_p(t).
```

### Proof

For `Q<p<=r<=s`, both lower factors are strict high. Thus

```math
\int|u_p|^2|u_r|^2|u_s|^2dx
\le
c_0^4\nu^4
\frac{\lambda_p^2\lambda_r^2}{\lambda_s^2}A_s.
```

For fixed `s`, deleting the absent indices `p,r<=Q` can only reduce the
nonnegative sum, so

```math
\sum_{Q<r\le s}\sum_{Q<p\le r}
\frac{\lambda_p^2\lambda_r^2}{\lambda_s^2}
\le
\frac{64}{45}\lambda_s^2.
```

The six orderings and Littlewood--Paley equivalence change only the absolute
constant. The endpoint is the same `H^2` density found in L5-3, but it begins
immediately above `Q`.

## 3. Two-block master inequality

The norm triangle and `(a+b)^4<=8(a^4+b^4)` give

```math
\|u\|_6^4
\lesssim
\|u_{\le Q}\|_6^4
+
\|u_{>Q}\|_6^4.
```

For the annular low blocks the protected L5-1 estimate is

```math
\|u_{\le Q}\|_6^4
\lesssim
U_0^2
W_{\le Q}
+
\text{fixed-base remainder},
```

with

```math
W_{\le Q}(t)
:=
\sum_{0\le r\le Q(t)}\lambda_r^2A_r(t).
```

Therefore the direct L5 route has the sharper pointwise reduction

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

There is no standalone near-cluster square in this representation.

The remaining analytic obligations are therefore:

```math
\int_0^T W_{\le Q}(t)dt<\infty
```

and

```math
\int_0^T Z_{>Q}(t)^{2/3}dt<\infty,
```

or a new identity that couples/cancels these two endpoints.

## 4. B2 disposition inside L5

The earlier core/near/tail split was useful for preventing the threshold shell
from being silently treated as strict high. The zero-gap proof preserves that
firewall more directly:

- `p=Q` belongs to `u_{<=Q}` and receives no strict-high upper bound;
- every `p>Q` belongs to `u_{>Q}` and does receive the defining upper bound.

Thus B2 is **collapsed into the low endpoint for this direct norm route**. This
is not a global theorem saying near-threshold interactions are harmless in
other PDE identities. In particular, a dynamic projected-energy calculation
can recreate finite-neighbour commutator terms. The disposition is only:

```text
B2_STANDALONE_BLOCKER_REMOVED_FROM_POINTWISE_L5_DECOMPOSITION.
```

## 5. L5-4B — exact low weighted endpoint and static separation

The low endpoint has the exact layer form

```math
\int_0^T W_{\le Q}(t)dt
=
\sum_{r\ge0}\lambda_r^2
\int_{\{t:Q(t)\ge r\}}A_r(t)dt.
```

The selected hypothesis controls only the occupancy of high active levels; it
does not supply the required correlation between the event `Q>=r` and the
shell dissipation `A_r`.

### Static threshold-compatible counterfixture

Let

```math
q_n=6n,
\qquad
\lambda_{q_n}=2^{6n},
\qquad
|I_n|=2^{-18n},
```

on pairwise disjoint time intervals, and set `Q=q_n` on `I_n`. Put a single
active low/threshold shell at `r=q_n` with

```math
A_{q_n}\asymp \nu^2\lambda_{q_n}.
```

Equivalently,

```math
E_{q_n}=A_{q_n}/\lambda_{q_n}^2
\asymp
\nu^2\lambda_{q_n}^{-1}.
```

A fixed divergence-free annular packet with this `L2` size has
`L-infinity` size comparable to `nu lambda_{q_n}` after scaling, so its
constant may be chosen to violate the threshold at `q_n`; all higher shells
are zero. Hence `Q=q_n` is compatible with the defining minimum.

The admitted static budgets are finite:

```math
\sum_n\lambda_{q_n}^2|I_n|
\asymp
\sum_n2^{-6n}
<\infty,
```

```math
\sum_nA_{q_n}|I_n|
\asymp
\nu^2\sum_n2^{-12n}
<\infty,
```

and the kinetic energy is uniformly bounded because

```math
E_{q_n}\asymp\nu^2 2^{-6n}.
```

But each interval contributes a frequency-independent amount to the weighted
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
that the exact low endpoint cannot be recovered from `Lambda in L2`, Leray
energy/dissipation, and the threshold definition by another scalar Holder or
occupancy rearrangement. A valid B1 advance must be equation-specific.

## 6. L5-4C — first dynamic audit of the B3 endpoint

The natural way to seek `Z_{>Q}` control is to use viscosity at the `H^1`
energy level. This section records the first unavoidable terms before any
claim of closure.

For a fixed cutoff `q`, write schematically

```math
V_q=P_{>q}u,
\qquad
Y_q=\|\nabla V_q\|_2^2,
\qquad
Z_q=\|\Delta V_q\|_2^2
```

(up to the fixed Littlewood--Paley equivalence constants).

The principal low--high transport has the form

```math
u_{\le q-2}\cdot\nabla V_q.
```

At the `L2` level incompressibility removes its pure transport contribution.
At the `H1` level, differentiating gives

```math
\nabla(u_{\le q-2}\cdot\nabla V_q)
=
(\nabla u_{\le q-2})\nabla V_q
+
u_{\le q-2}\cdot\nabla\nabla V_q.
```

The second term is again skew after integration. The first leaves the genuine
deformation coefficient

```math
G_q(t):=\|\nabla u_{\le q-2}(t)\|_\infty
```

through

```math
\left|
\int
(\nabla u_{\le q-2})\nabla V_q:\nabla V_q\,dx
\right|
\le
G_qY_q.
```

This term is below the cutoff and receives no strict-high smallness. Thus even
an optimistic audit in which every strictly high remainder is absorbed by
viscosity leaves a low-mode deformation input before one obtains
`nu Z_q` control.

### Moving active cutoff

If the fixed-`q` estimate is restricted to

```math
E_q=\{t:Q(t)=q\}
```

so that the strict-high hypothesis is available exactly where required, then
integration of the `Y_q'` term against `1_{E_q}` produces the selector-boundary
ledger

```math
\int Y_q\,d1_{E_q}
```

whenever that selector has bounded variation, and has no finite-measure
interpretation otherwise. `Lambda in L2` controls occupancy, not weighted
variation. This is the live B4 obstruction already characterized in L4; no new
variation theorem is proved here.

### Fixed cutoff instead of selector differentiation

If `q` is held fixed for all time, no selector derivative appears. But the
strict-high absorption is valid only on `{Q<=q}`. On `{Q>q}` the defining
smallness for all blocks `p>q` is unavailable. The selected hypothesis gives
only the measure estimate

```math
|\{t:Q(t)>q\}|
\le
\lambda_{q+1}^{-2}
\int_0^T\Lambda(t)^2dt,
```

which by itself controls neither `Y_q` nor `Z_q^(2/3)`. Supplying the missing
control is precisely a dynamic residence/depletion statement of the type whose
absence closed L3.

### Duhamel/backward-window variant

A backward parabolic representation around an active time avoids explicit
selector differentiation only if the defining strict-high condition persists
on a frequency-scale time window. Actual parabolic residence at the defining
threshold is an explicit L3 reopening condition and is not supplied by the
current hypothesis.

Hence the first dynamic B3 family has the bounded disposition

```text
MOVING_TAIL_H1_ENERGY
    -> low deformation G_q + selector variation;
FIXED_TAIL_H1_ENERGY
    -> bad-time control requiring threshold residence/depletion;
BACKWARD_DUHAMEL
    -> defining-threshold parabolic residence.
```

No member closes from the selected data alone.

This does **not** prove that no PDE-specific B3 theorem exists. It proves that
the first viscosity/maximal-regularity route is not an autonomous escape from
B1/B4/L3.

## 7. Updated residual ledger

| Blocker | L5-4 state | Exact obligation |
|---|---|---|
| B1 low core | sharpened | control `int W_{<=Q}` by an equation-specific correlation; static occupancy/dissipation rearrangements are separated by the new fixture |
| B2 near threshold | collapsed in pointwise L5 | no standalone near cluster is needed in `u=u_{<=Q}+u_{>Q}`; `p=Q` remains low |
| B3 strict tail | sharpened and dynamically audited | control `int Z_{>Q}^{2/3}` or find cancellation; first parabolic route reduces to low deformation plus B4/L3 |
| B4 selector motion | unchanged | required only when a dynamic proof differentiates/localizes the moving cutoff |

## 8. Successor state

The protected L5 target is now represented by two exact non-static endpoints:

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
\int_{\{Q\ge r\}}A_r(t)dt,
```

because the first dynamic B3 attempt immediately imports a low-mode deformation
coefficient or a previously closed selector/residence interface. If that B1
candidate fails, record its exact first PDE obstruction rather than returning
to static Holder rearrangements.

## Claim boundary

This package proves the zero-gap strict-tail estimates, the two-block master
reduction, and the stated static separation of the low weighted endpoint. It
also identifies the unavoidable low-deformation/selector/residence terms in the
first parabolic B3 route. It does not prove or refute `NS-CI-R014-A2`, global
Navier--Stokes regularity, or any MATHCERT claim; it does not reopen L3/L4; and
it creates no novelty, priority, publication, patentability, product, or
commercial claim.
