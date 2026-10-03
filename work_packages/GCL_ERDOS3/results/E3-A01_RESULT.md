# E3-A01 — adversarial attack on the dyadic bridge

Frontier node: `E3-B-SCALE-LOCAL`.

Disposition: **BOUNDARY_SHARPENED**.

## Attack target

The native B01 bridge says every **summable** dyadic density threshold is exceeded infinitely often by a reciprocally divergent set. The adversarial question is whether "summable" can be weakened using reciprocal divergence alone.

It cannot.

## Counterconstruction

Let ((	heta_j)_{jge1}) satisfy

[
0le	heta_jle1,
qquad
sum_j	heta_j=infty.
]

For each dyadic block (I_j=[2^j,2^{j+1})), choose exactly

[
m_j=leftlfloor 	heta_j2^{j-1}ightfloor
]

elements, for example the first (m_j) integers of the block, and let (A) be the union of these chosen blocks.

Then the dyadic density is

[
delta_j(A)=rac{m_j}{2^j}lerac{	heta_j}{2}le	heta_j.
]

On the other hand,

[
delta_j(A)ge rac{	heta_j}{2}-2^{-j}.
]

Since (sum_j	heta_j=infty) while (sum_j2^{-j}<infty), the series (sum_jdelta_j(A)) diverges. By the dyadic mass sandwich,

[
sum_{ain A}rac1a=infty.
]

Thus there is a reciprocally divergent set whose dyadic density **never exceeds** the prescribed nonsummable threshold.

Taking (	heta_j=1/j) gives an explicit reciprocally divergent set with (delta_j(A)	o0), so no fixed positive density conclusion is available.

## Consequence

The summability hypothesis in B01.2 is qualitatively sharp for any argument that uses only the implication

> reciprocal divergence ⇒ infinitely many dyadic blocks exceed a prescribed density threshold.

A stronger route must use more than blockwise density: cross-scale compatibility, additive structure, energy/uniformity information, or another invariant.

This construction does **not** refute Erdős Problem 3. The chosen blocks may themselves contain many arithmetic progressions. It only falsifies stronger density inferences from harmonic divergence.

## Frontier effect

- Stronger fixed-density and nonsummable-threshold variants: **REFUTED**.
- B01 summable-threshold bridge: **SURVIVES ADVERSARIAL ATTACK**.
- `E3-B-AP`: remains **OPEN**.
