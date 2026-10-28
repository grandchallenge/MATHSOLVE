# E3-Q11 — coarse-step/carry gauge equivalence in the cyclic embedding

Disposition: **PROVED_NATIVE_CARRY_GAUGE_EQUIVALENCE**.

This is native GCL work. It identifies an exact redundancy in the Q02/Q09 cyclic representation and prevents the campaign from treating two gauge-equivalent D01 families as independent witness constraints.

## Strongest exact statement

Let a D01 labelled family be described by integers
[
i, q, c_0,c_1,c_2,c_3
]
with physical block labels
[
j_t=i+tq+c_t.
]

For physical fibre functions (f_{j_t}) on (mathbb Z/Pmathbb Z), define the Q02 translated labelled functions
[
F_t(x):=f_{j_t}(x-c_tN).
]

Equivalently, when (f_j=1_{B_j}),
[
F_t=1_{c_tN+B_{j_t}}.
]

Fix any integer (s), and define
[
q':=q+s,
qquad
c_t':=c_t-ts.
]

Then the physical block labels are unchanged:
[
i+tq'+c_t'
=
i+tq+c_t
=
j_t.
]

Let
[
F_t'(x):=f_{j_t}(x-c_t'N).
]

For the four-term progression functional
[
Lambda(F_0,F_1,F_2,F_3)
=
mathbb E_{x,d}
prod_{t=0}^{3}F_t(x+td),
]
one has the exact identity
[
oxed{
Lambda(F_0',F_1',F_2',F_3')
=
Lambda(F_0,F_1,F_2,F_3).
}
]

More strongly, the identity holds term-by-term after any decomposition of each physical fibre function. In particular it preserves:

- the pure Q09 window baseline;
- every Q10 term (T_{F,S});
- every singleton geometry-bias correlation;
- every multi-fluctuation correlation;
- and every **scalar multilinear average** obtained by expanding the same unrestricted cyclic four-linear functional.

**Scope correction (step-resolved witnesses).** The equality above is an equality of full averages, not of their unaveraged step profiles or their Fourier coefficients at fixed frequencies. Define `K_F(d) = E_x product_t F_t(x+t*d)`. The same substitution proves the more precise covariance `K_F'(d) = K_F(d+s*N)`. With the discrete Fourier convention `Khat(k) = E_d K(d) exp(-2*pi*i*k*d/P)`, this gives `Khat_F'(k) = exp(2*pi*i*k*s*N/P) Khat_F(k)`. Thus the Fourier magnitudes are invariant, but nonzero-frequency phases need not be. Similarly, finite differences of the step profile translate; they are not generally identical pointwise at the same `d`. A Fourier/derivative witness is preserved only when its construction is invariant under this translation or when the witness is transformed covariantly.

**Finite adversarial example.** Set `N=16`, `P=67`, `s=1`, `i=q=0`, `c_t=t`, and let each physical fibre function `f_j` be the delta function at residue zero. This is the L01 `F15` gauge, mapped to `F16` with `q'=1`, `c'_t=0`. Then `K_F(d)=1/67` exactly when `d=16 (mod 67)` and zero otherwise; after the gauge change, `K_F'(d)=1/67` exactly when `d=0 (mod 67)` and zero otherwise. Both full averages equal `1/67^2`, while their Fourier mode `k=1` differs by the nontrivial phase `exp(2*pi*i*16/67)`. This example does not challenge the exact gauge equivalence of full averages; it disproves the stronger reading that fixed-frequency phases or pointwise step profiles are unchanged.

## Proof

Because
[
c_t'=c_t-ts,
]
we have
[
F_t'(z)
=
f_{j_t}(z-c_t'N)
=
f_{j_t}(z-c_tN+tsN).
]

Therefore
[
F_t'(x+td)
=
f_{j_t}igl(x+td-c_tN+tsNigr)
=
F_tigl(x+t(d+sN)igr).
]

Hence
[
prod_{t=0}^{3}F_t'(x+td)
=
prod_{t=0}^{3}F_tigl(x+t(d+sN)igr).
]

The map
[
dlongmapsto d+sN
]
is a bijection of (mathbb Z/Pmathbb Z). Averaging over (d) gives
[
Lambda(F_0',F_1',F_2',F_3')
=
Lambda(F_0,F_1,F_2,F_3).
]

If each
[
f_j=a_j+b_j
]
is decomposed and the multilinear average is expanded, the same change of variables applies to every selected term separately. Thus the equivalence is termwise.

## Application to the L01 core

Protected E3-L01 gives
[
F_{15}=(i,q,c)=(0,0,0123),
]
and
[
F_{16}=(0,1,0000).
]

Taking
[
s=1
]
in the theorem sends
[
q=0mapsto q'=1
]
and
[
c_t=tmapsto c_t'=0.
]

Therefore
[
oxed{
F_{15}sim F_{16}
}
]
under the Q02 cyclic embedding.

Both have physical block word
[
(0,1,2,3),
]
and their unrestricted cyclic mixed averages are exactly the same after the step-variable change
[
dmapsto d+N
]
(or equivalently (dmapsto d-N), depending on direction).

For Q09/Q10 this implies:

- their pure-window baselines are identical;
- the Q10 singleton weight for physical fibre (j) in (F_{15}), translated back by (jN), is exactly the (F_{16}) singleton weight for the same physical fibre;
- their corresponding multi-(h) terms are identical after the same translation;
- they cannot provide two independent signed geometry constraints merely because L01 counts them as two distinct D01 families.

## Why this does not collapse the finite L01 certificate

L01 classifies **integer carry families** before the unrestricted cyclic averaging step. (F_{15}) and (F_{16}) correspond to different coarse-step/carry descriptions and are distinct families in the exact finite (N=7) obstruction.

Q11 says only that the full-group Q02 embedding forgets this distinction.

The lost information is the localization of the integer step/residue pair ((u,v)) to its specific D01 carry cell.

Thus a proof that needs the independent force of both (F_{15}) and (F_{16}) cannot rely solely on unrestricted cyclic averages. It must retain carry-cell localization or an equivalent piece of integer geometry.

## First defect

Q10's de-windowed residual reduces further:

> **E3-B-CARRY-LOCALIZED-JOINT-WITNESS.**  
> Recover family-specific information lost under Q11's coarse-step/carry gauge equivalence by localizing the four-linear averages to the exact D01 carry cells (or an equivalent integer-domain formulation), and then show that the resulting geometry-bias / multi-fluctuation witnesses across the L01 core are incompatible with four near-extremal internally 4-AP-free fibres unless
> [
> gtrsimeta^{1+	heta}N
> ]
> points are deleted for some (0<	heta<1).

In particular, comparing the unrestricted Q10 constraints from (F_{15}) and (F_{16}) cannot by itself create a contradiction: they are the same constraint in different gauges.

## Frontier effect

- `E3-Q4-DENSITY-LOSS`: **OPEN**.
- `E3-B-FOUR-FIBRE-DEFICIT`: **OPEN_NATIVE_SUBTARGET**.
- `E3-B-DEWINDOWED-CANCELLATION-DICHOTOMY`: **PROVED_NATIVE**.
- New lemma `E3-B-CARRY-GAUGE-EQUIVALENCE`: **PROVED_NATIVE**.
- `E3-B-DEWINDOWED-GEOMETRY-OR-JOINT-INCOMPATIBILITY`: **REDUCED**.
- New smallest de-windowed residual: `E3-B-CARRY-LOCALIZED-JOINT-WITNESS`.
- No parent theorem or gluing-radius candidate is promoted.

## Protected basis

- E3-L01 family table, especially (F_{15}=(0,0,0123)) and (F_{16}=(0,1,0000)).
- E3-Q02 unrestricted cyclic four-linear embedding.
- E3-Q09 local de-windowing.
- E3-Q10 de-windowed cancellation dichotomy.
