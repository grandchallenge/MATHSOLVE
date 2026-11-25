# E3-B02 — exact extremal-series equivalence

Disposition: **PROVED_NATIVE_SOURCE_CONFIRMED**.

Fix (kge3), and write

[
a_n:=rac{r_k(2^n)}{2^n}.
]

Then the following are equivalent:

1. every set (Asubseteqmathbb N_{>0}) with (sum_{ain A}1/a=infty) contains a non-trivial (k)-term arithmetic progression;
2. (sum_{nge1}a_n<infty).

The forward implication from (2) to (1) is E3-B01. The reverse direction is reconstructed below.

## Lemma 1 — normalized extremal density is nonincreasing

For every (N),

[
r_k(2N)le 2r_k(N).
]

Indeed, if (Asubseteq[1,2N]) is (k)-AP-free, then both
(Acap[1,N]) and (Acap[N+1,2N]), after translating the latter interval,
are (k)-AP-free subsets of an interval of length (N). Therefore each
contains at most (r_k(N)) points.

Taking (N=2^n) gives (a_{n+1}le a_n).

Hence if (sum_n a_n=infty), then the odd-index subseries
(sum_{dge1}a_{2d-1}) also diverges: the even term following each odd term is
at most the preceding odd term.

## Lemma 2 — scale-separated blocks admit no mixed 3-AP

For (dge1), define

[
M_d:=4^d=2^{2d},
qquad
L_d:=2^{2d-1}=M_d/2,
qquad
B_d:=[M_d,M_d+L_d).
]

Thus (B_d=[M_d,	frac32M_d)), while the next block starts at (4M_d).

There is no three-term arithmetic progression (x<y<z) contained in
(igcup_d B_d) whose terms do not all lie in the same block.

To see this, let (yin B_d).

- If (x) lies in an earlier block, then the largest possible earlier point is
  (<	frac32M_d/4=	frac38M_d). Hence
  (y-x>	frac58M_d), so
  (z=y+(y-x)>	frac{13}{8}M_d>	frac32M_d).
  But also (z=2y-x<2y<3M_d<4M_d), so (z) lies in the gap before the
  next block.
- If (x,yin B_d), then (y-x<	frac12M_d), hence
  (z=y+(y-x)<2M_d<4M_d); it cannot lie in a later block.

These cases exclude every mixed three-term progression.

Consequently every arithmetic progression of length (kge3) contained in
(igcup_d B_d) lies wholly inside one block: if a (k)-AP crossed a block
boundary, some consecutive triple would be a mixed 3-AP.

## Lemma 3 — divergent extremal series builds a divergent reciprocal AP-free set

Assume (sum_n a_n=infty).

For each (d), choose a (k)-AP-free set

[
C_dsubseteq[1,L_d],
qquad
|C_d|=r_k(L_d),
]

and translate it into (B_d):

[
A_d:={M_d-1+c:cin C_d}.
]

By translation invariance, each (A_d) is (k)-AP-free. By Lemma 2 their
union

[
A:=igcup_{dge1}A_d
]

is globally (k)-AP-free.

Every (min A_d) satisfies (m<	frac32M_d=3L_d). Therefore

[
sum_{min A_d}rac1m
>
rac{r_k(L_d)}{3L_d}
=
rac13 a_{2d-1}.
]

Since the odd-index subseries diverges,

[
sum_{min A}rac1m
ge
rac13sum_{dge1}a_{2d-1}
=
infty.
]

Thus divergence of the extremal series produces a (k)-AP-free set with
divergent reciprocal sum, proving the contrapositive of (1) ⇒ (2).

## Source confirmation

This equivalence is explicitly stated in:

- Ben Green and Terence Tao, *New bounds for Szemerédi's theorem, III:
  A polylogarithmic bound for r_4(N)*, Mathematika 63 (2017), Introduction.
- Terence Tao and Van Vu, *Additive Combinatorics*, Exercise 10.0.6.

The native proof above is included so the campaign does not depend on an
unexpanded citation.

## Frontier effect

- `E3-B-AP`: **PROVED** as an exact equivalence theorem.
- Minimal unresolved case: `E3-Q4-SERIES`.
- Parent Erdős Problem 3 remains **OPEN**.
- One independent verification of the reverse block construction is justified;
  equivalent replay beyond that is not.
