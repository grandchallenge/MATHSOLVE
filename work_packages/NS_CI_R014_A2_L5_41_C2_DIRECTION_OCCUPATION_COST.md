# NS-CI-R014-A2-L5-41 — stopped reciprocal-amplitude occupation bootstrap

## Disposition

- Campaign: `NS-CI-001`
- Restricted target: `NS-CI-R014-A2`
- Tracker: `MATHSOLVE#59`
- Protected mathematical predecessor:
  `340e3f14ae984251a6c5c51192a58f6dabb43675` (L5-40)
- Protected integration base:
  `1a34479235b47405a3ed185c0b1d21d6ad9be190`
- Result class: exact stopped-flow bootstrap and normal-form compression separator
- Result:
  `STOPPED_RECIPROCAL_AMPLITUDE_BOOTSTRAP_PROVED__COMPRESSION_EXPONENTIAL_LOSS_BLOCKS_FINITE_BUDGET_CLOSURE`
- A2 theorem: open
- L5: active
- L3/L4: closed
- MATHCERT adjudication: absent

L5-40 identified the full first-order occupation functional

```math
R_\beta(Z)
=
\int_0^S
\frac{|\beta(s)|^2}
{J(s,Z)|b(s,\chi(s,Z))|^2}
\,ds.
```

Its unknown factor `1/J` is geometrically natural but makes direct
equation-level control look circular: bounded distortion is what the
occupation theorem is supposed to help prove.

This tranche removes that circularity by stopping the direction flow at the
first prescribed distortion level.

The price is an exact exponential bootstrap loss.  That loss is not a proof
artifact: an explicit compression normal form realizes exponential growth of
the full L5-40 occupation relative to its reciprocal-amplitude component.

Thus the next target is not mere finiteness of reciprocal amplitude.  It is a
quantitative smallness / anti-compression / compensation theorem.

## 1. Direction flow

Let

```math
\partial_s\chi(s,Z)
=
\beta(s)B(s,\chi(s,Z)),
\qquad
\chi(0,Z)=Z,
```

with orientation-preserving Jacobian

```math
J(s,Z)=\partial_Z\chi(s,Z)>0.
```

Assume a carrier `b(s,Y)` is nonzero on the region under consideration and
that the direction chart obeys

```math
|\partial_YB|
\le
|\partial_Y(b/|b|)|.
```

Then

```math
\partial_s\log J
=
\beta(s)
\partial_YB(s,\chi).
```

Define the absolute tangent cost

```math
\Omega_{\rm abs}(s,Z)
=
\int_0^s
|\beta(\sigma)|
|\partial_YB(\sigma,\chi(\sigma,Z))|
\,d\sigma.
```

## 2. Distortion stopping time

Fix `K>0`.

Define

```math
\tau_K(Z)
=
\inf
\{
s\in[0,S]:
|\log J(s,Z)|=K
\}
\wedge S.
```

Before `\tau_K(Z)`,

```math
e^{-K}
\le
J(s,Z)
\le
e^K.
```

Let the distortion set be

```math
\mathcal E_K
=
\left\{
Z:
\sup_{0\le s\le S}
|\log J(s,Z)|
\ge K
\right\}.
```

For labels in \(\mathcal E_K\), the stopped time is the first hit of level
\(K\), including a possible first hit at the terminal time \(S\).
Every such label satisfies

```math
\Omega_{\rm abs}(\tau_K(Z),Z)
\ge
K.
```

## 3. Reciprocal-amplitude budget without J

Define the Eulerian raw-gradient budget

```math
D_b
=
\int_0^S
\int
|\partial_Yb(s,Y)|^2
\,dY\,ds
```

and the Eulerian reciprocal-amplitude budget

```math
A_\beta
=
\int_0^S
\int
\frac{|\beta(s)|^2}
{|b(s,Y)|^2}
\,dY\,ds.
```

No Jacobian appears in `A_\beta`.

This is intentionally weaker information than the full L5-40
`\mathcal R_\beta`.

## 4. Exact stopped Cauchy factorization

For each label, stop all integrals at `\tau_K(Z)` and define

```math
G_K(Z)
=
\int_0^{\tau_K(Z)}
|b(s,\chi)|^2
|\partial_YB(s,\chi)|^2
\,ds,
```

```math
A_K(Z)
=
\int_0^{\tau_K(Z)}
\frac{|\beta(s)|^2}
{|b(s,\chi)|^2}
\,ds.
```

Cauchy--Schwarz gives

```math
\boxed{
\Omega_K(Z)^2
\le
G_K(Z)A_K(Z),
}
```

where

```math
\Omega_K(Z)
=
\Omega_{\rm abs}(\tau_K(Z),Z).
```

## 5. Stopped change of variables

At time `s`, retain only labels satisfying `s<\tau_K(Z)`.

On those labels,

```math
dZ
=
J(s,Z)^{-1}
\,dY
\le
e^K dY.
```

Therefore

```math
\int G_K(Z)\,dZ
\le
e^K
\int_0^S
\int
|b|^2|\partial_YB|^2
\,dY\,ds.
```

Using the L5-38 identity,

```math
|b|^2
|\partial_Y(b/|b|)|^2
\le
|\partial_Yb|^2,
```

and the chart domination gives

```math
\boxed{
\int G_K\,dZ
\le
e^K D_b.
}
```

Similarly,

```math
\boxed{
\int A_K\,dZ
\le
e^K A_\beta.
}
```

## 6. Stopped large-measure distortion theorem

A second Cauchy--Schwarz inequality in label space yields

```math
\int
\Omega_K(Z)
\,dZ
\le
e^K
D_b^{1/2}
A_\beta^{1/2}.
```

Since `\Omega_K\ge K` on `\mathcal E_K`,

```math
\boxed{
|\mathcal E_K|
\le
\frac{e^K}{K}
D_b^{1/2}
A_\beta^{1/2}.
}
```

This is the stopped reciprocal-amplitude bootstrap.

It is a direct equation-independent consequence of:

1. the direction characteristic equation;
2. the amplitude-weighted angular identity;
3. change of variables only before the chosen distortion exit.

It does not assume the frame is already bounded.

## 7. What the estimate can prove

Let `q_h(Z)dZ` be a nonnegative critical-observable density.

If the family `q_h` is uniformly integrable and, for some fixed `K>0`,

```math
D_b^{1/2}
A_\beta^{1/2}
\ll
K e^{-K},
```

then the distortion-exit set has small Lebesgue measure and therefore small
`q_h`-mass.

On the complementary labels,

```math
e^{-K}
\le
J(s,Z)
\le
e^K
```

for the full interval.

Thus quantitative smallness of the product

```math
D_b^{1/2}A_\beta^{1/2}
```

is sufficient for first-order large-mass bounded distortion.

This is strictly weaker than global uniform frame control and still does not
bound higher jets.

## 8. Why mere finiteness is not enough

The coefficient

```math
\frac{e^K}{K}
```

does not decay as `K\to\infty`.

Indeed, `K e^{-K}` is maximized at `K=1`.

Therefore the stopped estimate cannot turn mere finiteness of

```math
D_b,
\qquad
A_\beta
```

into an arbitrarily small bad-label set.

A useful bootstrap requires quantitative smallness at some finite distortion
level.

This identifies a sharper equation-level obligation than L5-40:

> selected active-band dynamics must make reciprocal amplitude small enough
> relative to raw angular-gradient energy, or supply an anti-compression /
> signed-cancellation mechanism that avoids the exponential stopping loss.

## 9. Exact compression separator

The exponential loss is geometrically real.

On the periodic three-dimensional embedding with `Y=x_1`, define the
constant-amplitude divergence-free carrier

```math
b_A(Y)
=
A
(0,\cos Y,\sin Y),
\qquad
|b_A|=A.
```

Its normalized direction is

```math
e(Y)
=
(0,\cos Y,\sin Y).
```

Choose the direction chart

```math
B(Y)=\sin Y.
```

Then

```math
|B_Y|
=
|\cos Y|
\le
|e_Y|
=
1.
```

Let

```math
\beta
=
-\frac{\kappa}{S},
\qquad
\kappa>0.
```

The label `Z=0` is a fixed characteristic because `B(0)=0`.

Since `B_Y(0)=1`,

```math
\boxed{
J(s,0)
=
e^{-\kappa s/S}.
}
```

The reciprocal-amplitude path budget is only

```math
\boxed{
A_{\rm amp}(0)
=
\int_0^S
\frac{|\beta|^2}{|b_A|^2}
\,ds
=
\frac{\kappa^2}{S A^2}.
}
```

But the full L5-40 occupation on the same label is

```math
\begin{aligned}
R_\beta(0)
&=
\int_0^S
\frac{|\beta|^2}
{J(s,0)A^2}
\,ds
\\
&=
\boxed{
\frac{\kappa(e^\kappa-1)}
{S A^2}.
}
\end{aligned}
```

Hence

```math
\boxed{
\frac{R_\beta(0)}
{A_{\rm amp}(0)}
=
\frac{e^\kappa-1}{\kappa}.
}
```

The full occupation is exponentially larger than the reciprocal-amplitude
component under strong compression.

This is a normal-form geometric separator.  It is not asserted to be an
exact selected whole-space NSE trajectory.

## 10. Energy scale of the separator

On a normalized spatial period,

```math
\int
|\partial_Y b_A|^2
\,dY
=
A^2.
```

Therefore over time `S`,

```math
D_b
=
S A^2.
```

The Eulerian reciprocal-amplitude budget is

```math
A_\beta
=
\frac{\kappa^2}{S A^2}.
```

Thus

```math
\boxed{
D_b A_\beta
=
\kappa^2.
}
```

Large compression therefore appears together with a large dimensionless
stopped-budget product in this calibration.

The stopped theorem is consistent with the exact geometry.

## 11. Relation to the critical direction scale

In the protected L5-35/L5-37 normal form,

```math
\beta_h
=
h^{-1}\theta_h.
```

The L5-33 residual corridor

```math
\theta_h=O(h^3)
```

corresponds to

```math
\beta_h=O(h^2),
```

whereas the L5-35 absolute principal-frame scale

```math
\theta_h=O(h)
```

corresponds to

```math
\beta_h=O(1).
```

Thus principal direction motion does not supply small `\beta_h` by scaling
alone.

Any positive whole-space closure of the stopped product must therefore use
actual amplitude occupation, dynamic anti-compression, polarization
correlation, or another equation-derived structure.

## 12. What remains unresolved

This tranche does not prove that A2 controls `A_\beta`.

It does not prove that the stopped product is small on the labels carrying the
critical observable.

It does not prove a selector charge from large `D_b^{1/2}A_\beta^{1/2}`.

It does not derive a favorable correlation between `\beta`, `J`, and
`|b|`.

It does not control `U_2,U_3,U_4`.

It does not prove A2.

## 13. Hard rejection tests

Reject any successor that:

- uses finiteness of `D_b` and `A_\beta` as if it implied arbitrarily small
  distortion mass;
- drops the factor `e^K` from the stopped change of variables;
- treats the compression separator as a selected whole-space NSE counterexample;
- assumes `\beta=O(h^2)` for principal direction motion by importing the
  L5-33 residual scale;
- treats first-order bounded distortion as control of higher frame jets;
- differentiates the selector;
- reopens L3 or L4 without their protected reopening conditions.

## 14. Claim boundary

The bounded result sought is exactly

```text
STOPPED_RECIPROCAL_AMPLITUDE_BOOTSTRAP_PROVED
__COMPRESSION_EXPONENTIAL_LOSS_BLOCKS_FINITE_BUDGET_CLOSURE.
```

It proves:

- an exact stopped-flow large-measure bound using only raw-gradient energy and
  reciprocal amplitude, with no prior `J`-bound;
- a quantitative smallness condition sufficient for first-order bounded
  distortion on most labels;
- mere finiteness cannot close the route because of the exponential stopping
  loss;
- an exact normal-form compression separator makes the full occupation
  exponentially larger than its reciprocal-amplitude component;
- principal direction scaling alone does not make `\beta` small.

No MATHCERT, novelty, priority, publication, patent, product, or commercial
claim is asserted.

## 15. Next live obligation

The smallest safe successor is
`C2-MIX-DIRECTION-COMPRESSION-COST`:

> Can selected whole-space active-band dynamics force small
> `D_b^{1/2}A_\beta^{1/2}` on the critical packet mass, or supply a
> sign/correlation law that prevents large compression without requiring
> reciprocal-amplitude smallness?

Audit the tangent component first.  Higher jets remain downstream.
