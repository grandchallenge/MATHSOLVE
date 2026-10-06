# E3-Q16 — additive alignment of the repeated-triplet derivative-shift sets

Disposition: **PROVED_NATIVE_COMMON_DIFFERENCE_ALIGNMENT**.

This is native GCL work. It sharpens the high-order residual left by E3-Q15 using only elementary additive energy on the two positive-density derivative-shift sets forced for the same physical fibre (B_1). No external theorem is used.

## Strongest exact statement

Assume the high-order alternatives of both repeated-triplet core families
[
F_2=(B_0,B_1,B_1,B_1),
qquad
F_3=(B_1,B_1,B_1,B_2)
]
from E3-Q15.

Let
[
E_2,E_3subseteq G=mathbb Z/Pmathbb Z
]
be the corresponding **physical derivative-shift sets** after Q15's (kin{1,2}) reparameterization, so that both sets refer to complete multiplicative derivatives of the same de-windowed physical fluctuation
[
b:=h_{B_1}.
]

Write
[
delta_eta:=rac{eta^4}{15cdot16^4},
qquad
ho_eta:=rac{delta_eta}{2}
=
rac{eta^4}{30cdot16^4}.
]

Q15 gives
[
|E_2|, |E_3|
ge
ho_eta P.
]

For a set (Esubseteq G), define
[
r_E(h):=
|{(e,e')in E^2:e'-e=h}|.
]

Then the mixed additive energy identity gives
[
oxed{
sum_{hin G}r_{E_2}(h)r_{E_3}(h)
ge
rac{|E_2|^2|E_3|^2}{P}
ge
ho_eta^4P^3.
}
]

Consequently the common-difference support
[
H:=
{hin G:r_{E_2}(h)>0, r_{E_3}(h)>0}
]
satisfies
[
oxed{
|H|
ge
rac{|E_2||E_3|}{P}
ge
ho_eta^2P.
}
]

Since (0in H), the nonzero common-difference set
[
H^ast:=Hsetminus{0}
]
obeys
[
oxed{
|H^ast|
ge
ho_eta^2P-1.
}
]

Thus for every
[
hin H^ast
]
there exist shifts
[
e_2,e_2+hin E_2,
qquad
e_3,e_3+hin E_3.
]

Equivalently, Q15's two a priori unrelated (B_1) derivative-shift systems contain a family of **matched shift-parameter parallelograms**
[
(e_2,e_2+h; e_3,e_3+h)
]
for at least
[
ho_eta^2P-1
=
rac{eta^8}{(30cdot16^4)^2}P-1
]
distinct nonzero increments (h).

Moreover, if
[
ho_eta^2Pge2,
]
then the number of matched quadruples with nonzero common difference satisfies
[
oxed{
sum_{h
e0}r_{E_2}(h)r_{E_3}(h)
ge
rac12ho_eta^4P^3.
}
]

In the asymptotic near-extremal campaign regime this auxiliary size condition holds eventually.

This does **not** yet align the Fourier frequencies selected inside the derivative-product overlaps. It replaces the raw shift-intersection problem by an additive shift-parameter compatibility problem on a positive-density family of matched differences.

## Proof

### 1. Mixed additive energy

Put
[
A:=E_2,qquad B:=E_3.
]

Let
[
r_{A-B}(x)
:=
|{(a,b)in A	imes B:a-b=x}|.
]

Then
[
sum_x r_{A-B}(x)=|A||B|.
]

By Cauchy-Schwarz over the (P) possible differences,
[
sum_x r_{A-B}(x)^2
ge
rac{|A|^2|B|^2}{P}.
]

The standard exact double-counting identity here is elementary:
[
sum_x r_{A-B}(x)^2
=
sum_h r_A(h)r_B(h).
]

Indeed both sides count quadruples
[
(a,a',b,b')in A^2	imes B^2
]
with
[
a-b=a'-b',
]
equivalently
[
a'-a=b'-b.
]

Therefore
[
sum_h r_A(h)r_B(h)
ge
rac{|A|^2|B|^2}{P}.
]

Using
[
|A|,|B|geho_eta P
]
gives
[
sum_h r_A(h)r_B(h)
ge
ho_eta^4P^3.
]

### 2. Common-difference support

For every (h),
[
r_A(h)le|A|,
qquad
r_B(h)le|B|.
]

Hence
[
r_A(h)r_B(h)le|A||B|.
]

Only (hin H) contribute to the mixed energy, so
[
rac{|A|^2|B|^2}{P}
le
sum_h r_A(h)r_B(h)
le
|H|,|A||B|.
]

Canceling (|A||B|>0),
[
|H|
ge
rac{|A||B|}{P}
ge
ho_eta^2P.
]

Since (r_A(0)=|A|) and (r_B(0)=|B|), one has (0in H). Therefore
[
|H^ast|
ge
ho_eta^2P-1.
]

For every (hin H^ast), positivity of both representation functions gives
[
e_2,e_2+hin E_2
]
and
[
e_3,e_3+hin E_3
]
for suitable (e_2,e_3).

### 3. Nonzero matched-quadruple count

The (h=0) contribution is exactly
[
r_A(0)r_B(0)=|A||B|.
]

Thus
[
sum_{h
e0}r_A(h)r_B(h)
ge
rac{|A|^2|B|^2}{P}-|A||B|.
]

Put
[
X:=|A||B|.
]

Then
[
rac{X^2}{P}-X
=
rac{X^2}{P}left(1-rac{P}{X}ight).
]

Since
[
Xgeho_eta^2P^2,
]
the condition
[
ho_eta^2Pge2
]
implies
[
X/Pge2
]
and hence
[
1-rac{P}{X}gerac12.
]

Therefore
[
sum_{h
e0}r_A(h)r_B(h)
ge
rac{X^2}{2P}
ge
rac12ho_eta^4P^3.
]

### 4. Eventual applicability

Protected E3-A03 gives
[
a_nge2^{-(C_ast+o(1))sqrt n}.
]

In the near-extremal contradiction regime used throughout tranche 04 one may take
[
etagerac12a_n.
]

The cyclic embedding has
[
P>8N,
qquad N=2^n.
]

Hence
[
Pho_eta^2
asymp
Peta^8
ge
2^{,n-O(sqrt n)}
	oinfty.
]

So
[
ho_eta^2Pge2
]
eventually.

## What this changes

Q15 explicitly warned that the two good-shift sets for (F_2) and (F_3) need not intersect because each has density only (O(eta^4)).

Q16 shows that direct intersection is the wrong additive object to demand.

Even if
[
E_2cap E_3=arnothing,
]
the two sets necessarily have many matched **difference increments**:
[
| (E_2-E_2)cap(E_3-E_3) |
ge
ho_eta^2P
]
in the representation-support sense proved above.

Thus the same physical fibre (B_1) is constrained at four derivative parameters
[
e_2, e_2+h, e_3, e_3+h
]
for many nonzero (h).

This creates a concrete additive compatibility object on which to compare the Q15 derivative spectra.

## Claim boundary

Q16 does not prove:

- that (E_2cap E_3
earnothing);
- that the Fourier frequencies selected by Q15 agree at (e_2) and (e_3);
- that frequencies are transported coherently when a shift parameter is changed by (h);
- that the matched-difference configurations integrate to a common quadratic phase;
- or any deletion bound with effective exponent below (2).

The exponent in the common-difference density is currently
[
ho_eta^2asympeta^8,
]
so cardinality alone is quantitatively insufficient.

## First defect

The high-order residual reduces from raw shift-set compatibility to:

> **E3-B-INTERIOR-DERIVATIVE-DIFFERENCE-COMPATIBILITY.**
>
> For the positive-density family of nonzero increments (h) supplied by Q16, compare the derivative spectra of the same physical fluctuation (B_1) at
> [
> e_2, e_2+h
> ]
> in the (F_2) carry geometry and at
> [
> e_3, e_3+h
> ]
> in the (F_3) carry geometry.
>
> Prove either:
> 1. coherent frequency transport across enough matched differences, yielding a joint quadratic witness; or
> 2. failure of such transport forces a deletion/density-increment cost with effective exponent (p<2).

This is strictly narrower than E3-B-INTERIOR-DERIVATIVE-COMPATIBILITY because common shift-parameter increments are now guaranteed.

## Frontier effect

- `E3-Q4-DENSITY-LOSS`: **OPEN**.
- `E3-B-FOUR-FIBRE-DEFICIT`: **OPEN_NATIVE_SUBTARGET**.
- `E3-B-REPEATED-TRIPLET-DERIVATIVE-FORCING`: remains **PROVED_NATIVE**.
- New lemma `E3-B-INTERIOR-DERIVATIVE-COMMON-DIFFERENCES`: **PROVED_NATIVE**.
- `E3-B-INTERIOR-DERIVATIVE-COMPATIBILITY`: **REDUCED**.
- New smallest high-order residual: `E3-B-INTERIOR-DERIVATIVE-DIFFERENCE-COMPATIBILITY`.
- No parent theorem or gluing-radius candidate is promoted.

## Protected basis

- E3-Q15 repeated-triplet derivative forcing.
- E3-A03 pointwise lower construction, used only for eventual applicability of the auxiliary size condition.
