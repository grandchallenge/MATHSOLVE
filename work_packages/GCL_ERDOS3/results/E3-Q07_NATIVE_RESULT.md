# E3-Q07 — additive energy of the Q06 good-shift set

Disposition: **PROVED_NATIVE_GOOD_SHIFT_ADDITIVE_ENERGY**.

This is native GCL work. It composes Q06 with the elementary additive-energy inequality for a dense subset of a finite abelian group.

## Strongest exact statement

Work in one adjacent Q04 fourfold branch and use the notation of Q06.

Let
\[
D\subseteq G=\mathbb Z/P\mathbb Z
\]
be the Q06 good-shift set:
\[
D=
\left\{
d:
\sigma I_d\ge \delta/2
\right\},
\]
where
\[
\delta=\frac{\alpha^2\gamma^2}{5}
>
\frac{\beta^4}{5\cdot16^4}.
\]

Q06 proves
\[
p:=\frac{|D|}{P}
\ge
\frac{\delta/2}{1-\delta/2}
\ge
\frac{\delta}{2}.
\]

Define the normalized additive energy
\[
\mathcal E(D)
:=
\frac{1}{P^3}
\#\left\{
(d_1,d_2,d_3,d_4)\in D^4:
d_1+d_2=d_3+d_4
\right\}.
\]

Then
\[
\boxed{
\mathcal E(D)\ge p^4\ge\frac{\delta^4}{16}
>
\frac{\beta^{16}}{10000\cdot16^{16}}.
}
\]

Equivalently, the Q06 joint derivative-overlap witnesses occur on at least
\[
\boxed{
\frac{\beta^{16}}{10000\cdot16^{16}}\,P^3
}
\]
additive parallelograms of shift parameters
\[
d_1+d_2=d_3+d_4.
\]

Thus the fourfold lane is no longer merely a family of unrelated good shifts. It supplies polynomially many additive relations among shifts on which the **same adjacent physical pair** has a large signed derivative spectral overlap.

This still does not prove frequency coherence or a deletion bound.

## Proof

Let
\[
r_D(s)
:=
\#\{(d_1,d_2)\in D^2:d_1+d_2=s\}.
\]

Then
\[
\sum_s r_D(s)=|D|^2,
\]
and
\[
\#\{d_1+d_2=d_3+d_4\}
=
\sum_s r_D(s)^2.
\]

By Cauchy-Schwarz,
\[
\sum_s r_D(s)^2
\ge
\frac{(\sum_s r_D(s))^2}{P}
=
\frac{|D|^4}{P}.
\]

Dividing by \(P^3\) gives
\[
\mathcal E(D)\ge\left(\frac{|D|}{P}\right)^4=p^4.
\]

Q06 gives
\[
p\ge\delta/2,
\]
hence
\[
\mathcal E(D)\ge\delta^4/16.
\]

Finally
\[
\delta>
\frac{\beta^4}{5\cdot16^4},
\]
so
\[
\frac{\delta^4}{16}
>
\frac{\beta^{16}}
{16\cdot 5^4\cdot16^{16}}
=
\frac{\beta^{16}}
{10000\cdot16^{16}}.
\]

## Correlation structure carried on every vertex of the parallelogram

For each \(d\in D\), Q06 gives
\[
\operatorname{Re}
\left[
\sigma
\sum_{\xi}
\widehat{\Delta_d a}(\xi)
\widehat{\Delta_d b}(-\xi)
e_P(-2\xi d)
\right]
\ge
\delta/2.
\]

Therefore every additive quadruple counted above consists of four shifts
\[
d_1,d_2,d_3,d_4\in D
\]
with
\[
d_1+d_2=d_3+d_4
\]
and with the same polynomial-scale joint derivative-overlap lower bound at each vertex.

No choice of a single frequency has yet been made, so no witness-identity information is discarded.

## Why this matters

The desired quadratic witness picture naturally expects derivative frequencies to vary approximately linearly with the shift:
\[
d\mapsto \xi_d.
\]

Q06 supplies many good shifts, but without relations among them one cannot test such a cocycle/Freiman law.

Q07 supplies a polynomial density of additive parallelograms in the good-shift set. The remaining theorem can therefore be posed on additive quadruples:
if one extracts derivative-frequency mass at the four shifts \(d_1,d_2,d_3,d_4\), show that the relation
\[
d_1+d_2=d_3+d_4
\]
forces either corresponding frequency compatibility or enough spectral branching/diffuseness to incur the target deletion cost.

This is strictly more structured than asking for arbitrary phase alignment among independent \(U^3\) witnesses.

## What Q07 does not prove

Large additive energy of \(D\) alone does not imply that the **spectral witnesses** chosen at its elements satisfy any additive relation.

In particular, Q07 does not prove:
- a map \(d\mapsto\xi_d\);
- a Freiman homomorphism law for that map;
- concentration of Q06 overlap on one mode;
- a common quadratic phase;
- or a point-deletion bound.

The missing theorem is joint in the shift and frequency variables.

## First defect

The fourfold branch is reduced to:

> **E3-B-DERIVATIVE-FREQUENCY-PARALLELOGRAM.**  
> On a set \(D\subseteq G\) of density at least \(c\beta^4\), each shift \(d\in D\) carries signed derivative spectral overlap at least \(c\beta^4\), and \(D\) has additive energy at least \(c'\beta^{16}\).  
> Use the additive parallelograms of \(D\) to prove either:
> 1. concentration on a graph \(d\mapsto\xi_d\) satisfying enough approximate additive relations to integrate to a joint quadratic witness; or
> 2. spectral branching/diffuseness large enough to force
> \[
> \gtrsim\beta^{1+\theta}N
> \]
> deletions for some \(\theta<1\).

## Frontier effect

- \`E3-Q4-DENSITY-LOSS\` remains **OPEN**.
- \`E3-B-FOUR-FIBRE-DEFICIT\` remains **OPEN_NATIVE_SUBTARGET**.
- Q06 derivative-overlap amplification remains **PROVED_NATIVE**.
- The positive-density good-shift set now has a theorem-grade polynomial additive-energy lower bound.
- The fourfold sub-residual is sharpened from arbitrary derivative-spectral alignment to a shift-frequency parallelogram compatibility problem.
- No parent theorem or gluing-radius candidate is promoted.
