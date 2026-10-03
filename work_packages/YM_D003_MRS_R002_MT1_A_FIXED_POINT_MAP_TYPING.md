# YM-D003-MRS-R002-MT1-A — fixed-point map typing and contraction gate

Disposition: `REDUCED__MRS_SPECIFIC_MASS_RESPONSE_MAP_AND_UNIFORM_LIPSCHITZ_ESTIMATE_MISSING`

Parent: `YM-D003-MRS-R002-MT1 — EXACT_ZERO_MASS_COUNTERTERM_TUNING`

Date: 2026-10-03

## Exact primary-source replay

The primary MRS paper introduces the counterterms

`-a_rho ∫ A^4/4! - b_rho ∫ A^2/2! - c_rho ∫ A(-Delta)A - d_rho ∫(dA)^2 - e_rho ∫ F^4`

in Section III.

Immediately afterward MRS states that the relevant `b_rho ∫ A^2/2` counterterm must be tuned exactly so that the renormalized mass is zero. The paper then says this is analogous to fixing the critical bare mass in infrared scalar `phi^4_4` and **should be solved** by a fixed-point argument as in Rivasseau [R], or by a full renormalization of the two-point function / one-particle-irreducible analysis as in [FMRS1].

Section V.E does not subsequently supply that missing fixed-point theorem. It says that after horizontal/vertical decoupling the divergent two- and four-point contributions are made translation invariant by a Mayer expansion, then cancelled by counterterms of the desired form; it refers to [R] for details and proceeds to the effective-coupling flow.

Therefore the source supplies:

1. the relevant scalar counterterm parameter `b_rho`;
2. the target renormalization condition: exactly zero renormalized mass;
3. two suggested proof architectures: fixed point or full two-point/1PI renormalization.

It does **not** supply a theorem-grade quantitative mass-response map, invariant domain, derivative/Lipschitz estimate, or an MRS-specific comparison theorem transporting the scalar `phi^4_4` fixed-point theorem.

## GCL typing

For proof purposes define a candidate MRS-specific mass functional

[
m_{ho,R}(b;lambda)
  := mathcal P_{mathrm{rel},2},Gamma^{(2)}_{ho,R}(b;lambda),
]

where:

- (Gamma^{(2)}_{ho,R}) denotes the renormalized two-point/1PI object associated with the MRS finite-ultraviolet-cutoff functional integral at fixed infrared regulator (R);
- (mathcal P_{mathrm{rel},2}) denotes the relevant zero-momentum/local (A^2) projection used to define the renormalized mass;
- (b) is the coefficient of the relevant (A^2/2) counterterm.

This notation is a GCL typing device. It is **not** claimed to be a named MRS definition.

The exact tuning problem is

[
m_{ho,R}(b_ho;lambda)=0.
]

If the counterterm contribution is separated linearly, write

[
m_{ho,R}(b;lambda)=b+Sigma_{ho,R}(b;lambda)
]

after fixing the sign convention. The candidate fixed-point map is then

[
F_{ho,R}(b;lambda)=-Sigma_{ho,R}(b;lambda).
]

## Conditional fixed-point closure lemma

Let (I=[-r,r]). Suppose for all sufficiently large (ho), at fixed admissible (R) and sufficiently small (lambda):

1. (Sigma_{ho,R}(cdot;lambda)) is defined on (I);
2. there exists (q<1), independent of (ho), such that
   [
   |Sigma_{ho,R}(b;lambda)-Sigma_{ho,R}(b';lambda)|
   le q|b-b'|
   ]
   for all (b,b'in I);
3. (|Sigma_{ho,R}(0;lambda)|le (1-q)r).

Then (F_{ho,R}) maps (I) into itself and is a contraction. Hence there is a unique
(b_{ho,R}(lambda)in I) satisfying

[
b_{ho,R}=-Sigma_{ho,R}(b_{ho,R};lambda),
]

equivalently (m_{ho,R}(b_{ho,R};lambda)=0).

Moreover (|b_{ho,R}|le r), uniformly in (ho). Any allowed dependence of (r) and (q) on the fixed infrared regulator (R) must be stated explicitly.

This is an elementary Banach fixed-point argument; the theorem debt is entirely in verifying its hypotheses in the MRS gauge construction.

## Smallest confirmed missing quantitative input

The primary source does not provide the MRS-specific estimate needed to verify the contraction gate.

The sharpest useful target is:

`MT1-A1 — UNIFORM_MASS_RESPONSE_BOUND`

Construct the MRS two-point relevant self-energy/remainder (Sigma_{ho,R}(b;lambda)) and prove, on a stated interval (I_{lambda,R}),

[
|Sigma_{ho,R}(b;lambda)-Sigma_{ho,R}(b';lambda)|
le q_{lambda,R}|b-b'|,
qquad q_{lambda,R}<1,
]

uniformly for all sufficiently large ultraviolet cutoff indices (ho), together with

[
|Sigma_{ho,R}(0;lambda)|
le (1-q_{lambda,R})r_{lambda,R}.
]

Equivalently, if differentiability is available, it is enough to prove

[
sup_{hogeho_0}sup_{bin I_{lambda,R}}
|partial_bSigma_{ho,R}(b;lambda)| < 1
]

plus the base-point bound.

## Why this is the correct reduction

- MRS explicitly identifies exact mass tuning as necessary.
- MRS explicitly points to a fixed-point/1PI method rather than supplying the proof.
- Section III's perturbative counterterm calculations do not establish the all-order response of the renormalized mass to (b).
- Section V.E supplies no invariant interval or derivative estimate for the mass parameter.
- The scalar `phi^4_4` fixed-point theorem cannot supply the missing estimate without a comparison theorem because the MRS construction has different field content, gauge constraints, background dependence, regulator structure, and ultraviolet/infrared direction.

## Compatibility gate with Section VI

Any proof of `MT1-A1` must additionally verify that the admissible interval for (b) is compatible with the counterterm bounds used in the Section VI large-background stability argument. The already-proved Section VI stability result may not be silently assumed uniform under arbitrary changes of (b).

This compatibility check is downstream of constructing the response map, but it is mandatory before MT1 is closed.

## Status

`YM-D003-MRS-R002-MT1-A` is **not proved**.

It is sharply reduced to construction and control of one MRS-specific relevant two-point response:

`YM-D003-MRS-R002-MT1-A1 — UNIFORM_MASS_RESPONSE_BOUND`.

## Claim boundary

This result proves only the abstract fixed-point implication and identifies the missing MRS-specific quantitative hypothesis. It does not establish that the required (Sigma_{ho,R}) has been constructed, does not prove exact mass tuning, does not close polymer/Schwinger convergence, and does not alter the fixed-infrared-cutoff or other YM-001 boundaries.
