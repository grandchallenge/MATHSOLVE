# NS-CI-R014-A2-L5-29 — exact same-band polarization corridor

## Disposition

- Campaign: `NS-CI-001`
- Restricted target: `NS-CI-R014-A2`
- Tracker: `MATHSOLVE#59`
- Protected mathematical predecessor:
  `24f9697ce614c82f8b4abe5da18047d3919e6b33`
- Result:
  `SAME_BAND_POLARIZATION_NULL_FACTOR_EXACT__R_TWO_THIRDS_ALIGNMENT_NOT_FORCED_POINTWISE`
- A2 theorem: open
- L5: active
- C2-MIX-DEPLETION: pointwise polarization route quantified
- MATHCERT adjudication: absent
- Evidence class: exact Fourier-symbol family plus route separation;
  not a selected whole-space trajectory

L5-28 reduces the bridge residual problem to an exact scale:

```math
\text{nonprincipal interaction}
\lesssim
R^{-2/3}
\times
\text{generic same-band interaction}.
```

The first geometric candidate is polarization cancellation.

For two orthogonal same-band source frequencies, the projected sum-frequency
interaction has an exact one-parameter null factor.

Take

```math
k_1=(N,0,0),
\qquad
k_2=(0,N,0),
\qquad
k_3=k_1+k_2.
```

For arbitrary angles `\alpha,\beta`, choose unit divergence-free
polarizations

```math
a_\alpha
=
(0,\cos\alpha,\sin\alpha),
\qquad
b_\beta
=
(\cos\beta,0,\sin\beta).
```

For

```math
u
=
A a_\alpha\cos(Nx_1)
+
A b_\beta\cos(Nx_2),
```

the exact Leray-projected coefficient at the sum phase
`\sin(Nx_1+Nx_2)` is

```math
\boxed{
\mathbb P_{k_3}(u\cdot\nabla u)_{k_3}
=
-\frac{A^2N}{2}
\sin(\alpha+\beta)e_3.
}
```

Thus the same Fourier support, the same modal amplitudes, and the same shell
energies permit every projected forcing magnitude between zero and the full
order-`A^2N` scale.

The pointwise polarization defect is

```math
\chi_{\rm pol}
=
|\sin(\alpha+\beta)|.
```

For this interaction to satisfy the L5-28 NF4-sc scale, one needs

```math
\boxed{
\chi_{\rm pol}
\lesssim
h^2
=
R^{-2/3}.
}
```

Near a null orientation, this means an angular corridor of width
`O(R^{-2/3})`.

Because support, modal energies, and amplitudes are independent of
`\alpha,\beta`, no pointwise argument using only A2, Leray scalar budgets,
support, or shell amplitudes can force this corridor.

Hence pointwise polarization alignment is not an automatic source of the
required NF4 depletion.

The next valid question is temporal:

> Does actual NSE evolution force near-null polarization for most of a
> critical interval, or does failure to enter the `R^{-2/3}` corridor itself
> create a non-summable selector/dissipation cost?

## 1. Exact divergence-free polarization family

Let

```math
a_\alpha
=
(0,c_\alpha,s_\alpha),
\qquad
b_\beta
=
(c_\beta,0,s_\beta),
```

where

```math
c_\alpha=\cos\alpha,
\quad
s_\alpha=\sin\alpha,
\quad
c_\beta=\cos\beta,
\quad
s_\beta=\sin\beta.
```

Then

```math
k_1\cdot a_\alpha=0,
\qquad
k_2\cdot b_\beta=0.
```

Also

```math
|a_\alpha|=|b_\beta|=1
```

for every pair \((\alpha,\beta)\).

Thus all fields in the family have exactly the same two source frequencies
and the same source-mode amplitudes.

## 2. Cross interaction before Leray projection

Set

```math
x=Nx_1,
\qquad
y=Nx_2.
```

Self-advection of each individual mode vanishes because of divergence freedom.

The cross terms are

```math
(a_\alpha\cos x\cdot\nabla)
(b_\beta\cos y)
=
-A^2N
c_\alpha
b_\beta
\cos x\sin y
```

and

```math
(b_\beta\cos y\cdot\nabla)
(a_\alpha\cos x)
=
-A^2N
c_\beta
a_\alpha
\cos y\sin x.
```

The coefficient of
`\sin(x+y)`
is therefore

```math
-\frac{A^2N}{2}
\left(
c_\alpha b_\beta
+
c_\beta a_\alpha
\right).
```

The vector inside parentheses is

```math
\begin{aligned}
c_\alpha b_\beta
+
c_\beta a_\alpha
&=
(
c_\alpha c_\beta,
c_\alpha c_\beta,
c_\alpha s_\beta+c_\beta s_\alpha
)
\\
&=
(
c_\alpha c_\beta,
c_\alpha c_\beta,
\sin(\alpha+\beta)
).
\end{aligned}
```

## 3. Exact Leray projection

For

```math
k_3=(N,N,0),
```

the Leray projector removes the component parallel to
\((1,1,0)\).

The first two components above are equal and therefore lie entirely in that
longitudinal direction.

The vertical component is already orthogonal to `k_3`.

Hence

```math
\boxed{
\mathbb P_{k_3}
\left(
c_\alpha b_\beta
+
c_\beta a_\alpha
\right)
=
\sin(\alpha+\beta)e_3.
}
```

Therefore

```math
\boxed{
\mathbb P_{k_3}(u\cdot\nabla u)_{k_3}
=
-\frac{A^2N}{2}
\sin(\alpha+\beta)e_3
\sin(Nx_1+Nx_2).
}
```

The exact projected forcing magnitude is

```math
\boxed{
\frac{A^2N}{2}
|\sin(\alpha+\beta)|.
}
```

## 4. Full forcing, exact cancellation, and sign reversal

The family realizes:

### Full order-one forcing

If

```math
\alpha+\beta
=
\frac\pi2
\pmod\pi,
```

then

```math
|\sin(\alpha+\beta)|=1
```

and the projected target forcing has magnitude

```math
A^2N/2.
```

### Exact cancellation

If

```math
\alpha+\beta
=
0
\pmod\pi,
```

then

```math
\sin(\alpha+\beta)=0
```

and the target projected forcing vanishes exactly.

### Sign reversal

Changing

```math
\alpha+\beta
\mapsto
-(\alpha+\beta)
```

reverses the target forcing sign without changing source frequencies or source
modal energies.

Thus polarization geometry, not scalar shell data, controls this channel.

## 5. Scalar observables are identical across the family

For every \(\alpha,\beta\):

- source support is exactly
  \(\{\pm k_1,\pm k_2\}\);
- both source frequencies have magnitude \(N\);
- both source polarizations have unit norm;
- source modal energies are identical;
- the physical amplitude scale is \(A\);
- any shell-energy functional depending only on the source modal norms is
  identical.

Therefore quantities of the form

```math
\|u_p\|_2,
\qquad
\|u_p\|_\infty
```

up to the fixed trigonometric normalization, shell support, and energy do not
determine the target interaction coefficient.

The A2 hypothesis and Leray energy/dissipation budgets are still more
coarse-grained.

## 6. Exact NF4 polarization corridor

L5-28 proves that the nonprincipal interaction assigned to the bridge residual
must be smaller than the generic same-band scale by

```math
h^2=R^{-2/3}.
```

If the present target channel is part of that residual, then

```math
\frac{A^2N}{2}
|\sin(\alpha+\beta)|
\lesssim
h^2A^2N.
```

After cancelling the common scale,

```math
\boxed{
|\sin(\alpha+\beta)|
\lesssim
h^2.
}
```

For distance

```math
d_{\rm pol}
=
\operatorname{dist}
(
\alpha+\beta,
\pi\mathbb Z
),
```

the elementary bound

```math
|\sin\theta|
\asymp
\operatorname{dist}(\theta,\pi\mathbb Z)
```

holds uniformly in a fixed small neighborhood of the null set.

Thus NF4 requires

```math
\boxed{
d_{\rm pol}
\lesssim
h^2
=
R^{-2/3}.
}
```

This is the exact pointwise alignment corridor for the fixture.

## 7. Why A2 cannot select the corridor pointwise

Consider two members of the exact family with the same \(A,N\):

```math
(\alpha,\beta)
=
(0,0)
```

and

```math
(\alpha,\beta)
=
(\pi/4,\pi/4).
```

They have the same:

- Fourier support;
- modal amplitudes;
- source modal energies;
- active frequency scale.

But their target projected forcing is respectively

```math
0
```

and

```math
A^2N/2.
```

Any pointwise inference based only on those shared scalar data therefore
cannot distinguish exact NF4 depletion from complete failure of NF4.

The A2 hypothesis is time-integrated and scalar. It does not contain the
missing polarization angle.

This does not exclude a dynamical theorem that forces the angle to evolve
toward the null set.

## 8. Pressure/Leray cancellation is already exhausted here

The displayed coefficient is computed **after** exact Leray projection.

Therefore the null factor cannot be attributed to a pressure estimate that has
not yet been used.

The pressure projection removes the equal horizontal component and leaves the
vertical polarization factor exactly.

Any further pointwise depletion must enter through additional geometry or
through cancellation among more interactions, not through reapplying Leray
projection to this same channel.

## 9. Relation to L5-16 and L5-17

L5-16 corresponds, after normalization of its source polarizations, to one
maximally non-null member of this family.

The present tranche extends that isolated fixture to a full exact continuum
from zero to maximal same-band forcing.

L5-17 showed that target variation can have either sign while strict-high
input is empty.

The current result explains one algebraic degree of freedom behind such sign
and magnitude variability: source polarization.

Neither result is a trajectory theorem.

## 10. Consequence for C2-MIX-DEPLETION

A pointwise polarization theorem strong enough for NF4 would have to prove that
the actual active packet satisfies

```math
d_{\rm pol}(t)
\lesssim
R(t)^{-2/3}
```

throughout the critical interval, or an invariant formulation of the same
small bilinear symbol.

No protected scalar estimate presently provides such information.

Therefore the next useful mechanism must be time-correlated.

The natural dichotomy is:

```text
near-null polarization for most of the critical interval
        |
        v
NF4 bridge may apply

versus

persistent non-null polarization
        |
        v
must itself be charged dynamically.
```

The second implication is not yet proved.

## 11. Next live obligation: C2-MIX-ALIGN-TIME

The smallest safe successor is:

> For an actual large active-band overshoot, can persistent failure of the
> \(R^{-2/3}\) polarization corridor over a critical interval be converted into
> selector growth, dissipation, or another non-summable cost?

A first bounded audit should retain the exact two-mode polarization parameter
and allow it to vary in time.

Test whether the time integral

```math
\int_{I_{\rm crit}}
|\sin(\alpha(t)+\beta(t))|^2\,dt
```

or its coordinate-free bilinear-symbol analogue controls:

- generated neighboring-mode energy;
- critical-frequency variance;
- or viscous dissipation.

If only instantaneous target forcing is recovered, that returns to L5-17 and
is not new.

## 12. Hard rejection tests

Reject any successor that:

- infers polarization from shell energy alone;
- treats exact pointwise cancellation as dynamically persistent;
- assumes actual NSE packets obey the two-mode ansatz;
- treats the fixture as a whole-space counterexample;
- reuses Leray projection as if it supplied another small factor;
- replaces the required \(R^{-2/3}\) corridor by an order-one angle bound;
- uses one instant of non-null forcing as a selector-charge theorem.

## 13. Claim boundary

The protected claim sought from this tranche is exactly

```text
SAME_BAND_POLARIZATION_NULL_FACTOR_EXACT
__R_TWO_THIRDS_ALIGNMENT_NOT_FORCED_POINTWISE.
```

It proves:

- an exact unit-polarization family with fixed same-band support and energies;
- projected target forcing proportional to
  \(\sin(\alpha+\beta)\);
- exact zero/full/sign-reversed forcing within that family;
- the NF4 polarization corridor
  \(d_{\rm pol}\lesssim R^{-2/3}\);
- pointwise scalar support/energy data do not determine that corridor.

It does not prove dynamic alignment or misalignment cost.

It does not prove A2.

It does not reopen L3 or L4.

No MATHCERT, novelty, priority, or publication claim is asserted.
