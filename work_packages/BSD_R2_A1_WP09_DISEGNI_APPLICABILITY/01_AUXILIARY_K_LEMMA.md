# Auxiliary imaginary-quadratic field lemma

## Proposition `BSD-A1-K001`

Assume the selected `BSD-R2-A1` hypotheses. Then there exists an imaginary quadratic field

`K = Q(sqrt(D))`

such that:

1. `D<0` is a fundamental discriminant;
2. `(D,2N)=1`;
3. `2` splits in `K`;
4. every `ell|N` splits in `K`;
5. `L(E^D,1) != 0`;
6. `ord_{s=1} L(E/K,s)=1`.

## Proof

The first five assertions are the exact bounded downstream interface admitted by MATHFORGE from the Friedberg-Hoffstein prescribed-local quadratic-twist nonvanishing theorem family.

The sign compatibility is part of that admitted interface. For the selected curve, exact analytic rank one forces the functional-equation sign of `E/Q` to be `-1`. In the classical all-`N`-split Heegner packet, the base-change sign is `-1`; hence the twist sign is `+1`. The prescribed local packet can therefore be chosen inside the central-value sign family, and the admitted source supplies `D` in that packet with `L(E^D,1) != 0`.

For quadratic base change,

`L(E/K,s) = L(E,s)L(E^D,s)`.

The first factor has a simple zero at `s=1` by the selected analytic-rank hypothesis. The second factor is nonzero there. Therefore

`ord_{s=1} L(E/K,s) = 1 + 0 = 1`.

This proves the proposition.

## Scope

The proposition is existential. It does not select a canonical discriminant and does not need one for the applicability theorem.

The proposition does not prove a p-adic Gross-Zagier identity, a Heegner-index formula, a main conjecture, or BSD. Those are separate obligations.