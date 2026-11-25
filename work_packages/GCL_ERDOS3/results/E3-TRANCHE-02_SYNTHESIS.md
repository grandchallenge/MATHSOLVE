# E3-TRANCHE-02 — synthesis against E3-Q4-SERIES

Baseline: `d9f2a46f915df19e9d2cd889e00e59c7100ae0bf`  
Protected dispatch packet: `bf9bc7f448f92d71afeae937fda133b0e1d4de80`

## Decision

All five requested returns were received and preserved. Only **E3-X01** is promoted as a mathematical tightening of `E3-Q4-SERIES`.

The parent frontier remains open:
[
sum_{nge1}rac{r_4(2^n)}{2^n}<infty.
]

Write
[
a_n:=rac{r_4(2^n)}{2^n}.
]

The promoted subtarget is:

> **E3-Q4-DENSITY-LOSS.** Prove that there exist fixed (Lge1), (c>0), (n_0), and (0<	heta<1) such that
> [
> a_{n+L}le a_nigl(1-c,a_n^	hetaigr)
> qquad(nge n_0).
> ]

If this holds, then along each residue class modulo (L),
[
a_n=O(n^{-1/	heta}),
]
and since (1/	heta>1), the required series converges.

E3-X01 does **not** prove the density-loss inequality. Its advance is to isolate this explicit sufficient missing lemma while proving that several stronger-looking naive bounded-step laws cannot hold.

## Return-by-return synthesis

### E3-Q01 — accepted, not promoted

Q01 correctly shows that the published Green–Tao 2017 quantitative machinery is fixed-ambient: its internal recurrence/energy iteration does not itself compare extremal densities at distinct ambient scales. Plain interval localization gives only
[
a_nle a_mqquad(mle n),
]
so reblocking does not improve the known pointwise exponent.

This is useful blocker evidence, but the prior frontier already required some new averaged or cross-scale estimate. Q01 therefore validates the absence of a cheap extraction; it does not by itself narrow the missing theorem as sharply as X01.

### E3-X01 — accepted and promoted

X01 establishes three exclusions using the lower-bound side of the problem:

1. no eventual fixed-step uniform fractional contraction
   [
   a_{n+L}le(1-delta)a_n;
   ]
2. no eventual fixed-window averaged uniform contraction of the same type;
3. no eventual constant-factor quasi-submultiplicativity
   [
   a_{n+m}le C a_n a_m.
   ]

Each would force decay too fast to coexist with known lower constructions.

It then identifies the density-dependent loss above. That law is strong enough to imply a summable polynomial envelope, but weak enough not to contradict the known stretched-exponential lower bound. This is the smallest useful theorem-shaped residual produced by the tranche, so it becomes the promoted frontier subtarget.

### E3-A02 — accepted as supporting boundary evidence, not promoted

A02 supplies a concrete finite counterexample to literal submultiplicativity and independently rules out eventual constant-factor quasi-submultiplicativity. It also gives useful O'Bryant-based constraints on diagonal power recurrences (a_{2n}le C a_n^p), excluding (p>sqrt2) while leaving a lower-bound-compatible region.

These are real adversarial constraints, but they do not yield a smaller selected sufficient target than the density-loss lemma from X01. They are retained as supporting evidence rather than promoted as a second frontier.

### E3-S03 — accepted, not promoted

S03's primary-source audit finds no sequence-level theorem in the scoped Green–Tao/Green line stronger than subadditivity/monotonicity. The current source interface therefore does not close or materially narrow the quantitative frontier.

### E3-V02 — verified; verification node closed

V02 independently replays the reverse block-construction implication in E3-B02. Therefore `E3-V-B02` is closed and the exact equivalence bridge is now independently verified within its declared procedural contract.

This has no effect on the open status of Erdős Problem 3 or on the truth of `E3-Q4-SERIES`.

## Resulting frontier

The campaign is no longer asking vaguely for “some recurrence stronger than monotonicity.” The promoted concrete target is `E3-Q4-DENSITY-LOSS`.

Alternative proofs of `E3-Q4-SERIES` remain logically possible. Promotion means only that this is the smallest theorem-grade sufficient residual justified by the present tranche; it does not assert necessity.

## Claim boundary

No return proves `E3-Q4-SERIES`. No return proves Erdős Problem 3. No source audit establishes that a better theorem is impossible. The only verification closure in this tranche is the pre-existing E3-B02 reverse implication.
