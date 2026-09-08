# Theorem spine

## Lemma A — irreducible `E[2]` removes the torsion valuation

Assume `E[2]` is irreducible as an `F_2[G_Q]`-module. Then `E(Q)[2]=0`, hence `#E(Q)_tors` is odd and

`ord_2(#E(Q)_tors^2)=0`.

**Status:** `PROVED_IN_PACKAGE`.

## Corollary B — exact reduced form of `BSD-R2-A1`

Under the selected hypotheses and the protected rank-one/finite-Sha interface, `BSD-R2-A1` is equivalent to

`ord_2(L'(E,1)/(Omega_E Reg_E)) = ord_2(#Sha(E/Q)) + sum_{l|N} ord_2(c_l).`

**Status:** `PROVED_IN_PACKAGE` as an algebraic reduction; it does not prove the equality.

## Lemma C — good ordinary reduction at `2` fixes the good-prime branch

Since `N` is odd, `E` has good reduction at `2`; the explicit ordinary hypothesis selects the ordinary local branch. No multiplicative exceptional-zero formula at `2` is admissible for this target.

**Status:** `PROVED_IN_PACKAGE` from the stated hypotheses.

## Imported theorem interface D — rank one and finite Sha

Analytic rank one implies algebraic rank one and finiteness of `Sha(E/Q)` through the admitted Gross-Zagier/Kolyvagin interface. The normalized derivative is a nonzero rational number under the fixed period/regulator convention.

**Status:** `LITERATURE_DERIVED`, protected-source bounded.

## Frontier proposition E — the protected odd-prime formula is not an interface at `2`

The WP02 rank-one leading-term interface has explicit odd-prime hypotheses. Therefore it is non-composable with `p=2`. Replacing `p` by `2` is not a proof step.

**Status:** `PROVED_IN_PACKAGE` as an interface/logic claim.

## Open bridge `BSD-R2-A1-BRIDGE-2INT`

It is sufficient to construct an integral 2-primary bridge that simultaneously provides:

1. exact ordinary `2^infinity` Selmer local conditions and finite-level/global control;
2. an integral 2-adic main-conjecture, Euler-system, or equivalent finite-length identity strong enough to determine the relevant 2-Selmer/Sha length;
3. an explicit reciprocity/Gross-Zagier/height comparison valid integrally at `2`;
4. every Tamagawa, period, isogeny, interpolation, and local correction with its exact `ord_2`;
5. if a quadratic base-change route is used, exact restriction/corestriction kernel and cokernel terms replacing the odd-prime plus/minus direct-sum shortcut.

After these are identified with the WP00 quantities, Corollary B gives exactly `BSD-R2-A1` and nothing stronger.

**Status:** `CONJECTURAL / OPEN`.