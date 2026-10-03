# E3-TRANCHE-03 — representation shift for the four-term extremal series

Protected baseline: `8444c84b37be48f0a43f0e61e9841c039d60c8d0`.

## Governing frontier

Let
[
a_n:=rac{r_4(2^n)}{2^n}.
]

The protected frontier remains

[
sum_{nge1}a_n<infty.
]

The promoted sufficient route from E3-X01 is to prove an eventual bounded-step
density loss

[
a_{n+L}le a_nigl(1-c,a_n^	hetaigr),
qquad
Lge1, c>0, 0<	heta<1.
]

This tranche does not assume that route is true. One lane is explicitly tasked
with falsifying it.

## Why change representation

The raw sequence (a_n) suppresses the mechanism behind the elementary
monotonicity (a_{n+L}le a_n). That inequality comes from partitioning a
large interval into smaller blocks and ignoring all arithmetic progressions
that cross block boundaries. Any strict improvement must therefore measure the
cost of making the blocks mutually compatible.

The tranche uses five linked representations.

### 1. Gluing defect

For fixed (L), define

[
D_{L,n}:=a_n-a_{n+L}ge0.
]

The promoted density-loss target is exactly a lower bound of the form

[
D_{L,n}ge c,a_n^{1+	heta}.
]

Interpretation: (D_{L,n}) is the density mass that must be sacrificed when
(2^L) individually strong (4)-AP-free blocks are glued into one globally
(4)-AP-free set.

### 2. Reciprocal-potential coordinate

For (	heta>0), define

[
U_	heta(n):=a_n^{-	heta}.
]

The nonlinear loss law above becomes a candidate positive-drift law for
(U_	heta). A proof that (U_	heta) gains a fixed positive amount every
(L) scales would turn the problem into an additive growth statement.

### 3. Persistence profile

Define

[
P(alpha):=#{nge1:a_ngealpha}.
]

For a nonnegative sequence, the layer-cake identity suggests

[
sum_n a_n=int_0^1 P(alpha),dalpha
]

in the extended nonnegative sense. Thus the convergence problem may be read as:
how many dyadic scales can sustain extremal density at least (alpha)?
A bound (P(alpha)llalpha^{-	heta}) with (	heta<1) would be sufficient.

### 4. Extremizer tree

Take a (4)-AP-free extremizer at a large dyadic scale and recursively
partition it into (2^L) equal subblocks. If (D_{L,n}) is very small over
many scales, average block deficits are small at many levels. This produces a
tree containing many near-extremal fibers. Cross-sibling arithmetic
constraints are then the missing object, rather than a pointwise estimate on
one set.

### 5. Digit-and-carry fibers

Write an integer in a large interval as

[
x=iN+u,qquad 0le i<2^L,quad 0le u<N.
]

For a progression with difference (d=qN+v), the four block indices are
controlled by the finite carry pattern

[
leftlfloorrac{u+t v}{N}ightfloor,qquad t=0,1,2,3.
]

This converts cross-block (4)-AP avoidance into a finite family of
constraints among residue fibers. The purpose is to expose a combinatorial
object that can admit stability bounds, LP dual certificates, or an explicit
counterconstruction.

## Research discipline

The representations above are a research programme, not theorem authority.
E3-R01 must establish the exact implication dictionary and identify any false
converses. E3-D01 must compile the digit/carry constraints exactly. E3-G01 is
the primary theorem attack. E3-C01 is computational evidence only. E3-A03 is
authorized to kill the promoted route. E3-S04 may import only exact
source-supported interfaces.

Recent source context motivates the shift but does not prove it. Green's 2026
survey still lists Green–Tao 2017 as the endpoint for the (k=4) upper bound
and says substantially new ideas appear necessary. Gowers' 2020 example warns
that ordinary Fourier-uniformity alone does not force the random-model count
of four-term progressions. The tranche therefore asks for structure-sensitive
cross-fiber information rather than a generic pseudorandomness slogan.

## Promotion rule

A return may be promoted only if it does at least one of the following:

1. proves a new theorem that strictly narrows E3-Q4-DENSITY-LOSS;
2. refutes the promoted route or a named subfamily with a valid construction;
3. reduces the frontier to a smaller exact finite/local statement with a
   proved implication back to the series;
4. identifies a primary-source theorem whose hypotheses can be instantiated
   without silently strengthening them.

No computational trend, heuristic exponent, or source analogy is promotable by
itself.
