# Lay executive companion

The target asks whether two rational quantities contain exactly the same power of `2`. One side comes from the derivative of the complex L-function after dividing by the real period and regulator. The other comes from Sha and the local Tamagawa factors, divided by torsion.

At odd primes, strong rank-one theorems can often ignore factors that are powers of `2`, because such factors are units for an odd-prime valuation. That is precisely what cannot be done here. The campaign is measuring the power of `2` itself. A factor that was harmless in an odd-prime proof becomes part of the answer.

This package makes two substantive advances.

First, irreducibility of `E[2]` forces the rational torsion subgroup to have odd order. Therefore the torsion denominator contributes zero to the `2`-adic valuation. The selected target is exactly equivalent to comparing the normalized derivative with `#Sha` times the Tamagawa factors.

Second, the package localizes the remaining obstruction. A successful proof needs an integral theorem at `2`, not an odd-prime theorem with the letter `p` replaced by `2`. The theorem must control ordinary 2-Selmer local conditions, the relevant Iwasawa/Euler-system length, explicit reciprocity or Gross-Zagier comparison, and every local/global conversion factor. If an auxiliary quadratic field is used, the usual odd-prime plus/minus splitting must be replaced by an exact 2-primary restriction/corestriction calculation.

No such general admitted bridge is presently available for the selected class. That is the mathematical frontier, not a documentation gap.