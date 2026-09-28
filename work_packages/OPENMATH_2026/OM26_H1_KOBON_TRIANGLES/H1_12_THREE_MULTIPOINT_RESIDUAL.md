# H1-12 residual reduction — any 95 witness requires at least three finite multiple points

**State:** `SOLVE_SOURCE_CONDITIONAL_REDUCTION__NOT_CERTIFIED`

## Inputs

1. The protected H1-12 projective reduction proves that any finite collection of counted bounded triangular faces can be carried to a projectively equivalent affine arrangement with no parallel line pairs while preserving those faces. Projective incidence multiplicities are preserved.
2. Protected MATHFORGE source reconnaissance at `eb5af08b1bb0ae7742dc46786019fe7b034b04ee` records a contemporary restricted result: for even order, a pairwise-nonparallel arrangement with at most two finite multiple points has the n=18 bound `T <= 94`. Forge explicitly does not promote this to a hill-global theorem.

## Conditional reduction

Assume an admissible n=18 hill arrangement has 95 counted bounded triangular faces.

Apply the H1-12 projective normalization to those 95 faces. The resulting affine arrangement is pairwise nonparallel and still has at least 95 counted bounded triangular faces. Because a projective automorphism preserves line concurrence and its multiplicity, the number and multiplicities of finite multiple points are unchanged except for the choice of affine chart; the chosen new line at infinity contains no pairwise arrangement intersection, so no multiple intersection is moved to infinity.

If the normalized arrangement had at most two finite multiple points, the protected Forge restricted bound would force `T <= 94`, contradicting preservation of the 95 counted faces.

Therefore, **conditional on the cited restricted upper theorem**, any 95-triangle hill witness must have at least three finite multiple points after the H1-12 no-parallel normalization.

## Operational consequence

The unresolved H1-12 search/proof surface is narrower than “all concurrence”:

- parallelism is eliminated by the Solve projective reduction;
- zero, one, or two finite multiple points are excluded from a 95 witness by the protected source-scoped restricted theorem;
- a possible 95 witness must lie in the stratum with **three or more finite multiple points**.

The next proof lane should attack the multi-core incidence budget for q >= 3 directly. The next construction lane, if resumed, should deliberately generate arrangements in that stratum rather than repeat local perturbations around the simple 93 leader.

## Claim boundary

This is a Solve-level route reduction using a protected Forge source-status input. It is not an independent proof of the restricted theorem, not a MATHCERT disposition, and not a hill-global 94 upper bound. If the cited restricted theorem is later rejected or narrowed by independent certification, this reduction must be revisited.
