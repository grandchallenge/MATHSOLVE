# Lay executive companion

The previous package found the precise danger in the usual quadratic-field strategy: at an odd prime one can split an object into plus and minus pieces by averaging with `(1+tau)/2` and `(1-tau)/2`. At the prime `2`, those operators are not integral. They can hide exactly the powers of `2` that the BSD target asks us to measure.

WP06 avoids that operation completely.

The first observation is unexpectedly strong. If `E[2]` is irreducible over `Q`, then a quadratic extension cannot create a rational point of order `2`. Therefore it cannot create any `2`-power torsion either. This makes global restriction in Galois cohomology exact enough to identify the base curve with the genuine plus eigenspace over the quadratic field, and the quadratic twist with the genuine minus eigenspace.

Local conditions can still enlarge after base change. Instead of pretending they do not, we name their discrepancy. At each nonsplit place `v`, the discrepancy is a finite cohomology group killed by `2`. At split places it is exactly zero.

There is a second defect: even when plus and minus eigenspaces are both known, they need not form a direct sum integrally. WP06 names the intersection `I_n` and the quotient `Q_n`. Both are killed by `2`. The resulting length formula is exact.

The practical consequence is that quadratic descent is no longer a vague p=2 hazard. It is a finite correction ledger. Once an integral reciprocity/Iwasawa theorem supplies the analytic-to-Selmer length, these correction terms can be carried all the way to the BSD valuation rather than guessed away.