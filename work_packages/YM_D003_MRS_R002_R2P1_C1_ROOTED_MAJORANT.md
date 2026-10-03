# YM-D003-MRS-R002-R2P1-C1 — weakest rooted-polymer majorant

Status: `CLOSED__ABSTRACT_MAJORANT_DEFINED__C2_REDUCED_TO_LINK_KERNEL_SUMS`

Parent: `YM-D003-MRS-R002-R2P1-C — MRS_RENORMALIZED_TWO_POINT_SUBGRAPH_THEOREM`

Protected base: `grandchallenge/MATHSOLVE@49b7a3642b540c3b3db752c696e49c8dd4388a36`

Protected source authorities:
- `grandchallenge/MATHFORGE@90254084f3d06dcaad1a6a950039396ea85c23f9`
- `grandchallenge/MATHFORGE@9b6413a7ca5972b7d724ea8f1594c01b8f46cf45`

## Objective

Define the weakest majorant sufficient to formulate rooted-polymer summability for the closed C0 grammar without inventing MRS exponents absent from the source.

## Source-supported ingredients

MRS Section VII supplies:
1. an adjustable small factor per occupied box;
2. resummability of polymers containing a fixed box via decay of horizontal, vertical, and Mayer links;
3. sliced propagator spatial decay in Eq. (VII.1);
4. extra smallness/scale decay for the anisotropic vertical expansion;
5. irrelevance of vertices with at least five legs;
6. paired treatment of the derivative trilinear vertex.

Sections V.E–VI separately control the background-determinant/large-field sector. That sector is region-local, not a box-to-box branching link.

## Rooted C0 object

Let G be a C0-admissible connected two-point object and choose a root box Delta_0.

Write:
- B(G) for occupied boxes;
- E_H(G), E_V(G), E_M(G) for horizontal, vertical, and Mayer links;
- BG(G) for large-field regions carrying BGDET factors;
- I_irr(G) for irrelevant >=5-leg insertions;
- I_3(G) for derivative trilinear insertions.

## Primitive weight interfaces

Use nonnegative weights:
- s_box(Delta) <= epsilon for each occupied box;
- D_H, D_V, D_M for the three link families;
- W_BG(Delta) for a BGDET factor attached locally to a large-field region;
- w_irr and w_3pair for irrelevant and paired trilinear insertions.

Section VI stability is used to absorb W_BG into the corresponding large-field box activity. BGDET therefore contributes no independent branching constant.

## Majorant

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
prod_{Delta in BG(G)} W_BG(Delta)
*
prod_{v in I_irr(G)} w_irr(v)
*
prod_{pairs in I_3(G)} w_3pair(pair).

The rooted seminorm is
||A||_C1 = sup_{Delta_0} sum_{G:Delta_0 in B(G)} |A(G)| / M(G;Delta_0),
whenever the denominator is nonzero.

## Lemma C1.1 — rooted-tree reduction

Assume finite rho-uniform constants
L_H = sup_Delta sum_{Delta'} D_H(Delta,Delta'),
L_V = sup_Delta sum_{Delta'} D_V(Delta,Delta'),
L_M = sup_Delta sum_{Delta'} D_M(Delta,Delta').

Assume the local BGDET factor is absorbed into s_box and the resulting box smallness obeys

q := epsilon * C_comb * (L_H + L_V + L_M) < 1,

where C_comb is the finite local multiplicity from the C0 grammar.

Then the tree-majorized sum of connected C0 objects containing a fixed root box converges and is bounded by a geometric factor of order 1/(1-q).

### Proof

Choose a spanning tree of the occupied-box incidence graph. Each new box contributes at most epsilon. Summing over the next link target and link type costs at most L_H+L_V+L_M, and local constructor multiplicity costs C_comb. Hence each growth step costs at most q. Summing over tree size gives sum_{n>=0}q^n. QED.

## Exact C2 residuals

C1 reduces the remaining branching estimate to:
- C2-H: rho-uniform finite L_H;
- C2-V: rho-uniform finite L_V;
- C2-M: rho-uniform finite L_M.

BGDET is discharged at C1 as a local large-field box activity using the Section VI stability bound; it is not a branching-link obligation.

## Current disposition

`C1_CLOSED__ROOTED_MAJORANT_AND_TREE_REDUCTION_PROVED__BGDET_LOCALIZED__C2_LINK_SUMS_ACTIVE`

C1 does not prove q<1. It proves exactly which link sums remain to be bounded.
