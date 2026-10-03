# YM-D003-MRS-R002-R2P1-C1 — weakest rooted-polymer majorant

Status: `CLOSED__ABSTRACT_MAJORANT_DEFINED__C2_REDUCED_TO_KERNEL_SUMS`

Parent: `YM-D003-MRS-R002-R2P1-C — MRS_RENORMALIZED_TWO_POINT_SUBGRAPH_THEOREM`

Protected base: `grandchallenge/MATHSOLVE@49b7a3642b540c3b3db752c696e49c8dd4388a36`

Protected source authorities:
- `grandchallenge/MATHFORGE@90254084f3d06dcaad1a6a950039396ea85c23f9`
- `grandchallenge/MATHFORGE@9b6413a7ca5972b7d724ea8f1594c01b8f46cf45`

## Objective

Define the weakest majorant sufficient to formulate rooted-polymer summability for the closed C0 grammar without inventing MRS exponents absent from the source.

## Source-supported ingredients

MRS Section VII supplies the qualitative convergence architecture:

1. an adjustable small factor per occupied box;
2. resummability of all polymers containing a fixed box via decay of horizontal, vertical, and Mayer links;
3. sliced propagator spatial decay in Eq. (VII.1);
4. extra smallness/scale decay for the anisotropic vertical expansion;
5. irrelevance of vertices with at least five legs;
6. paired treatment of the derivative trilinear vertex;
7. a separately controlled background-determinant/large-field sector from Sections V.E–VI.

C1 deliberately keeps these as source-derived weight classes. It does not assign an exponent not already justified.

## Rooted C0 object

Let G be a C0-admissible connected two-point object and choose one root box Delta_0 in its support.

Write:

- B(G) for occupied boxes;
- E_H(G), E_V(G), E_M(G) for horizontal, vertical, and Mayer links;
- E_BG(G) for BGDET attachments;
- I_irr(G) for explicitly irrelevant >=5-leg insertions;
- I_3(G) for derivative trilinear insertions.

## Primitive weight interfaces

Introduce nonnegative source-majorant functions:

- s_box(Delta) <= epsilon for each nonempty small-field box or large-field box, with epsilon adjustable in the MRS regime;
- D_H(Delta,Delta') for horizontal links;
- D_V(Delta,Delta') for vertical/anisotropic links;
- D_M(Delta,Delta') for Mayer links;
- W_BG(R) for a BGDET region, bounded by the Section VI stability estimate rather than by ordinary vertical expansion;
- w_irr(v) for >=5-leg irrelevant insertions;
- w_3pair(v,v') for paired derivative-trilinear insertions.

No claim is made here about explicit formulas beyond the protected MRS estimates.

## Majorant

Define

M(G;Delta_0)
=
prod_{Delta in B(G)} s_box(Delta)
*
prod_{e in E_H(G)} D_H(e)
*
prod_{e in E_V(G)} D_V(e)
*
prod_{e in E_M(G)} D_M(e)
*
prod_{r in E_BG(G)} W_BG(r)
*
prod_{v in I_irr(G)} w_irr(v)
*
prod_{pairs in I_3(G)} w_3pair(pair).

The rooted C1 seminorm is

||A||_C1
=
sup_{Delta_0}
sum_{G: Delta_0 in B(G)}
|A(G)| / M(G;Delta_0),

whenever the denominator is nonzero.

For proof use, the equivalent majorant inequality is preferred:

|A(G)| <= C * M(G;Delta_0)

with C independent of terminal ultraviolet depth rho.

## Why this is the weakest useful choice

C1 does not insert:

- a guessed power of lambda;
- a guessed scale exponent;
- a guessed exponential decay rate;
- a scalar phi^4 norm;
- a uniform BGDET factor derived from ordinary polymer links.

It records only the multiplicative structure MRS says must be summable. Quantitative values are postponed to C2 and later native lemmas.

## Lemma C1.1 — rooted-tree reduction

Assume there exist constants

L_H = sup_Delta sum_{Delta'} D_H(Delta,Delta'),
L_V = sup_Delta sum_{Delta'} D_V(Delta,Delta'),
L_M = sup_Delta sum_{Delta'} D_M(Delta,Delta'),

and a background factor bound L_BG for admissible BGDET attachments, all finite and uniform in rho.

Assume also a box smallness epsilon such that the total local branching activity

q := epsilon * C_comb * (L_H + L_V + L_M + L_BG)

is strictly less than 1, where C_comb is the finite combinatorial multiplicity produced by the C0 local constructor grammar.

Then the sum of tree-majorized connected C0 objects containing a fixed root box is finite and bounded geometrically by a constant of order 1/(1-q).

### Proof

Every finite connected C0 object has a spanning tree on its occupied-box incidence graph. Bound each object by the product of its primitive nonnegative weights and sum first over spanning-tree growth from the fixed root. At each added box, the sum over its possible link target and link type is bounded by L_H+L_V+L_M+L_BG, while the newly occupied box contributes epsilon and local constructor choices contribute at most C_comb. Therefore each generation is bounded by q times the previous one. Summing over tree size gives the geometric series sum_{n>=0} q^n. QED.

This is a standard combinatorial reduction, not the MRS-specific analytic estimate.

## Exact C2 residuals

C1 reduces the next theorem to four concrete analytic/combinatorial estimates:

### C2-H
Prove a rho-uniform finite L_H from the spatial decay of the MRS sliced/homothetic propagators and horizontal cluster links.

### C2-V
Prove a rho-uniform finite L_V including the anisotropic alpha-direction expansion and its source-stated extra small/scale-decaying factor.

### C2-M
Prove a rho-uniform finite L_M for the Mayer links generated before local two-/four-point counterterm extraction.

### C2-BG
Prove that BGDET attachments admit a root-local activity bound L_BG compatible with Section VI stability without treating them as ordinary vertical polymers.

The first three are link-summability questions. C2-BG is structurally separate.

## Current disposition

`C1_CLOSED__ROOTED_MAJORANT_AND_TREE_REDUCTION_PROVED__C2_KERNEL_SUMS_ACTIVE`

C1 does not prove that q<1. It proves exactly what must be bounded to establish q<1.

The next action is C2-H/C2-V first, because MRS gives explicit spatial-decay and anisotropic-resummation information there. C2-M and C2-BG remain separate sub-obligations.
