# YM-D003-MRS-R002-R2P1-C4 — marked-polymer response

Status: `PROVED__C4_CLOSED`

Fix the admissible infrared regulator R and small coupling. Let `P_mass` be the mass component of the complete quadratic local projector proved in C3.

Define `F_{rho,R}(b)` by applying `P_mass` to the renormalized local 1PI two-point polymer sum after removing the isolated explicit `b A^2/2` contribution. The exact equation is

`b = F_{rho,R}(b)`.

## Unmarked bound

C2 rooted summability plus C3 localization give a constant `A_R`, independent of terminal ultraviolet depth, with

`|F_{rho,R}(0)| <= A_R epsilon`.

The complementary marginal quadratic local corrections obey analogous bounded-output estimates.

## Marked response lemma

There is a constant `B_R`, independent of terminal ultraviolet depth, such that on a small interval around zero,

`|dF_{rho,R}/db| <= B_R epsilon`.

At finite cutoff, differentiate the polymer expansion before taking any limit. Since the isolated explicit quadratic contribution was removed from F, each surviving derivative term is a nontrivial two-point polymer with one marked quadratic insertion, or the equivalent marked propagator response if the quadratic term is placed in the Gaussian part.

A polymer with n local insertion sites has at most `C_mark n` possible marks. C2 controls an exponentially support-weighted rooted activity. For fixed `a>0`, `n <= C(a) exp(a n)`, so the mark is absorbed by the same exponential activity reserve. The fixed infrared regulator controls the equivalent low-momentum resolvent factor. Thus the marked sum is `O(epsilon)` uniformly in rho.

## Contraction

Choose the small-coupling allocation so that

`B_R epsilon <= 1/2`

and let

`I_R=[-2A_R epsilon,2A_R epsilon]`.

For `b in I_R`,

`|F_{rho,R}(b)| <= |F_{rho,R}(0)| + (1/2)|b| <= 2A_R epsilon`.

Hence `F_{rho,R}` maps `I_R` into itself and is a contraction uniformly in rho. Banach's theorem gives a unique finite-cutoff coefficient `b_{rho,R}` satisfying the exact zero-mass equation.

## Simultaneous scale induction

At each scale carry the complete local quadratic coefficient vector, the exact mass coordinate, and the C3 irrelevant remainder. The C2/C3 estimates are uniform on `I_R`; the marked bound makes the mass update contractive; the marginal quadratic coordinates remain bounded local outputs of the same summable family; and the C3 remainder has positive lower-scale gain.

Therefore the local two-point bound and running exact mass bound close simultaneously with constants independent of terminal ultraviolet depth.

## Boundary

C4 is local to the fixed-IR MRS construction. C5 must still verify compatibility with the background/gauge-restoring counterterm organization and the Section VI stability interface.

Disposition:

`R2P1_C4_CLOSED__UNIFORM_MARKED_RESPONSE_CONTRACTION_AND_SIMULTANEOUS_INDUCTION_PROVED__C5_AUTHORIZED`
