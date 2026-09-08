# Proofs and exact deductions

## Proof of Lemma A

If `#E(Q)_tors` were even, the finite abelian torsion group would contain an element of order `2`. Such a point is a nonzero element of `E[2]` fixed by `G_Q`, so the one-dimensional subspace that it spans would be a nonzero proper `G_Q`-stable subspace of the two-dimensional `F_2`-module `E[2]`. This contradicts irreducibility. Therefore the torsion order is odd, and its squared order has `ord_2` equal to zero.

## Proof of Corollary B

The protected rank-one interface makes `Sha(E/Q)` finite and the normalized derivative nonzero, so both valuations are defined. Apply the additive valuation to the right side of the selected formula. Lemma A removes the torsion contribution. The remaining valuation is

`ord_2(#Sha(E/Q)) + sum_{l|N} ord_2(c_l)`.

Thus the original target and the reduced target are equivalent.

## Proof of Lemma C

For an elliptic curve over `Q`, primes of bad reduction divide the conductor. Because `N` is odd, `2` is not a bad prime. The selected target additionally assumes ordinary reduction at `2`, so local-at-2 arguments must remain on the good-ordinary branch.

## Why the odd-prime route does not mechanically descend to `2`

The campaign-audited rank-one odd-prime proofs use constructions in which powers of `2` may be harmless `p`-adic units for odd `p`. An auxiliary quadratic route can also split an object into plus/minus or curve/twist pieces using operators modeled on `(1+tau)/2` and `(1-tau)/2`. Such division by `2` is integral for odd `p` but not over `Z_2`. At `p=2`, restriction/corestriction and local-condition comparisons can therefore carry finite 2-primary kernels or cokernels that contribute to the very valuation being measured.

Likewise, period, isogeny, local Euler, and interpolation conversions that are equal only up to a power of `2` are insufficient for this target. A proof must compute those powers rather than call them units.

This is a structural obstruction to transfer, not a proof that no p=2 theorem can exist.

## Computation class

No numerical computation is used to establish a mathematical claim in this package. The only new theorem-grade content is elementary exact group/valuation reasoning. Literature and source-interface claims retain their source status.