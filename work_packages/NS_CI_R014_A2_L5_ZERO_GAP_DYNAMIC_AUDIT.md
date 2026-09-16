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
The pre-triangle strict-tail proof needs no fixed buffer `K`; the low endpoint
is separated from the admitted scalar budgets by a threshold-compatible
fixture; and the first parabolic attack on the high `H^2` endpoint is reduced
to explicit dynamic inputs. The result does not prove or refute A2 and does not
reopen L3 or L4.

## 1. Imported interface

For annular blocks write

```math
E_q=\|u_q\|_2^2,
\qquad
A_q=\lambda_q^2E_q.
```

At almost every time with finite `Q=Q(t)`,

```math
\|u_p\|_\infty<c_0\nu\lambda_p
\qquad\text{for every }p>Q,
```

with no corresponding upper bound at `p=Q` or below. The admitted budgets are

```math
\sup_t\|u(t)\|_2\le U_0,
\qquad
\int_0^T\sum_{q\ge0}A_q(t)dt<\infty,
\qquad
\int_0^T\Lambda(t)^2dt<\infty.
```

The inhomogeneous base block remains a fixed-frequency remainder.

## 2. L5-4A — zero-gap strict-tail theorem

Define

```math
u_{>Q}:=\sum_{p>Q}u_p,
\qquad
S_{>Q,N}^2:=\sum_{Q<p\le N}|u_p|^2.
```

In the first display, the intended symbol is the velocity tail `u_{>Q}`.

For every finite terminal index `N`,

```math
\|u_{Q<p\le N}\|_4^4
\lesssim
c_0^2\nu^2\sum_{Q<p\le N}A_p,
```

and

```math
\|u_{Q<p\le N}\|_6^6
\lesssim
c_0^4\nu^4\sum_{Q<s\le N}\lambda_s^2A_s.
```

The proof is exactly the L5-3 pre-triangle proof with lower index `Q+1`.
For `Q<p<=r`,

```math
\int|u_p|^2|u_r|^2dx
\le
c_0^2\nu^2
\left(\frac{\lambda_p}{\lambda_r}\right)^2A_r,
```

and

```math
\sum_{Q<p\le r}
\left(\frac{\lambda_p}{\lambda_r}\right)^2
\le\frac43.
```

For `Q<p<=r<=s`,

```math
\int|u_p|^2|u_r|^2|u_s|^2dx
\le
c_0^4\nu^4
\frac{\lambda_p^2\lambda_r^2}{\lambda_s^2}A_s,
```

while deleting indices at or below `Q` can only reduce the nonnegative ordered
triple sum, so

```math
\sum_{Q<r\le s}\sum_{Q<p\le r}
\frac{\lambda_p^2\lambda_r^2}{\lambda_s^2}
\le\frac{64}{45}\lambda_s^2.
```

Thus, uniformly in terminal frequency,

```math
\int_0^T\|u_{>Q}(t)\|_4^4dt
\lesssim c_0^2\nu U_0^2,
```

and

```math
\|u_{>Q}\|_6^4
\lesssim
c_0^{8/3}\nu^{8/3}Z_{>Q}^{2/3},
\qquad
Z_{>Q}(t):=\sum_{p>Q(t)}\lambda_p^2A_p(t).
```

No step requires `p>Q+K`.

## 3. Two-block master inequality

Use the exact split

```math
u=u_{\le Q}+u_{>Q}.
```

The protected low estimate is

```math
\|u_{\le Q}\|_6^4
\lesssim
U_0^2W_{\le Q}
+
\text{fixed-base remainder},
```

with

```math
W_{\le Q}(t):=\sum_{0\le r\le Q(t)}\lambda_r^2A_r(t).
```

Hence

```math
\boxed{
\|u(t)\|_6^4
\lesssim
U_0^2W_{\le Q}(t)
+c_0^{8/3}\nu^{8/3}Z_{>Q}(t)^{2/3}
+\text{fixed-base remainder}.
}
```

The remaining direct L5 obligations are

```math
\int_0^T W_{\le Q}(t)dt<\infty
```

and

```math
\int_0^T Z_{>Q}(t)^{2/3}dt<\infty,
```

or a new identity coupling or avoiding these endpoints.

## 4. B2 is not standalone in this representation

The zero-gap split preserves the threshold firewall exactly: `p=Q` stays in
`u_{<=Q}` and receives no strict-high upper bound, while every `p>Q` lies in
`u_{>Q}` and does receive that bound. Therefore

```text
B2_STANDALONE_BLOCKER_REMOVED_FROM_POINTWISE_L5_DECOMPOSITION.
```

This is scoped only to the pointwise norm representation. Dynamic projected
energy and commutator identities can still create finite-neighbour terms near
`Q`; no global near-threshold depletion theorem is asserted.

## 5. L5-4B — exact low endpoint and static separation

Tonelli gives

```math
\int_0^T W_{\le Q}(t)dt
=
\sum_{r\ge0}\lambda_r^2
\int_{\{t:Q(t)\ge r\}}A_r(t)dt.
```

Thus B1 is a correlation problem between shell dissipation and the event
`Q>=r`.

Take pairwise disjoint intervals `I_n` and set

```math
q_n=6n,
\qquad
\lambda_{q_n}=2^{6n},
\qquad
|I_n|=2^{-18n},
\qquad
Q=q_n\text{ on }I_n.
```

Place one threshold shell at `q_n` with

```math
A_{q_n}\asymp\nu^2\lambda_{q_n},
\qquad
E_{q_n}\asymp\nu^2\lambda_{q_n}^{-1}.
```

A fixed divergence-free annular packet with this `L2` scaling has supremum
comparable to `\nu\lambda_{q_n}`; its fixed amplitude constant can be chosen so
that shell `q_n` violates the defining strict-high inequality while every
higher shell is zero. Thus `Q=q_n` is compatible with the minimum definition.

The admitted scalar budgets are finite:

```math
\sum_n\lambda_{q_n}^2|I_n|
\asymp\sum_n2^{-6n}<\infty,
```

```math
\sum_nA_{q_n}|I_n|
\asymp\nu^2\sum_n2^{-12n}<\infty,
```

and `E_{q_n}\asymp\nu^2 2^{-6n}` is uniformly bounded. But

```math
\lambda_{q_n}^2A_{q_n}|I_n|
\asymp\nu^2
```

on every interval, so

```math
\int_0^T W_{\le Q}(t)dt=\infty.
```

This is a static shell/packet fixture, not a Navier--Stokes solution. It shows
that the exact low endpoint cannot follow from the selected scalar budgets and
the threshold definition by another Holder, occupancy, or shell-energy
rearrangement. A B1 advance must use equation-specific dynamics.

## 6. L5-4C — first parabolic audit of B3

For a fixed cutoff `q`, let

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

The intended leading symbol in that display is the velocity `u_{<=q-2}`. At
`L2` level incompressibility removes the pure transport contribution. At `H1`
level,

```math
\nabla(u_{\le q-2}\cdot\nabla V_q)
=
(\nabla u_{\le q-2})\nabla V_q
+u_{\le q-2}\cdot\nabla\nabla V_q.
```

The final transport term is skew after integration, but the first term leaves

```math
\left|\int
(\nabla u_{\le q-2})\nabla V_q:\nabla V_q\,dx\right|
\le G_qY_q,
```

where

```math
G_q(t):=\|\nabla u_{\le q-2}(t)\|_\infty.
```

`G_q` lies below the cutoff and receives no strict-high smallness. Thus even an
optimistic audit that absorbs every strictly high remainder leaves a low-mode
deformation input before `\nu Z_q` can be controlled.

If this fixed-`q` estimate is localized to `E_q={t:Q(t)=q}`, integrating the
`Y_q'` term against `1_{E_q}` creates the selector-boundary ledger

```math
\int Y_q\,d1_{E_q},
```

which requires weighted variation control absent from `Lambda in L2`; this is
the protected B4 interface.

If instead `q` is held fixed globally, strict-high absorption for every `p>q`
is guaranteed only on `{Q<=q}`. On the complementary set,

```math
|\{t:Q(t)>q\}|
\le\lambda_{q+1}^{-2}
\int_0^T\Lambda(t)^2dt,
```

but this occupancy estimate alone gives no control of `Y_q` or `Z_q^{2/3}`.
Turning it into the required parabolic estimate would be a new
residence/depletion theorem of the type whose absence closed L3.

Finally, a backward Duhamel representation around an active time avoids
explicit selector differentiation only if the defining strict-high condition
persists on a frequency-scale time window. Defining-threshold parabolic
residence is itself a protected L3 reopening condition.

Therefore the first B3 parabolic family reduces to

```text
MOVING_TAIL_H1_ENERGY
    -> low deformation G_q + selector variation;
FIXED_TAIL_H1_ENERGY
    -> bad-time control requiring residence/depletion;
BACKWARD_DUHAMEL
    -> defining-threshold parabolic residence.
```

This is a bounded route reduction, not an exhaustion theorem for every
possible PDE-specific B3 mechanism.

## 7. Updated residual ledger

| Blocker | L5-4 state | Exact obligation |
|---|---|---|
| B1 low core | sharpened | control `int W_{<=Q}` by an equation-specific correlation/depletion theorem; the fixture excludes further static scalar rearrangement |
| B2 near threshold | collapsed in pointwise L5 | no standalone cluster in `u=u_{<=Q}+u_{>Q}`; dynamic finite-neighbour terms may still occur |
| B3 strict tail | sharpened and dynamically audited | control `int Z_{>Q}^{2/3}` or avoid it; the first parabolic route imports low deformation and B4/L3 interfaces |
| B4 selector motion | unchanged | arises when a dynamic proof differentiates or localizes the moving cutoff |

## 8. Successor state

The smallest safe successor is B1-first: seek an actual Navier--Stokes
correlation/depletion estimate for

```math
\sum_r\lambda_r^2
\int_{\{Q\ge r\}}A_r(t)dt.
```

Static Holder, occupancy, threshold-energy floors, and packet counting are now
excluded as sufficient mechanisms. If the bounded B1 candidate fails, record
its first exact PDE obstruction before returning to a B3 mechanism genuinely
different from moving-tail `H1` energy, fixed-tail bad-set splitting, or
threshold-residence Duhamel.

## Claim boundary

This package proves the zero-gap strict-tail estimates, the two-block pointwise
reduction, and the stated static separation of the low weighted endpoint. It
also identifies the low-deformation/selector/residence interfaces in the first
parabolic B3 family. It does not prove or refute `NS-CI-R014-A2`, universal
critical integrability, or global Navier--Stokes regularity; it does not reopen
L3 or L4; it performs no MATHCERT adjudication; and it creates no novelty,
priority, publication, patentability, product, or commercial claim.
