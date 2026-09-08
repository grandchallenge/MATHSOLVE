# Remaining reciprocity and integral debt after WP09

WP09 materially narrows component B of `BSD-R2-A1-2MU-RECIPROCITY`, but it does not close it.

## Closed interface

There is now a suitable auxiliary imaginary quadratic field `K` for which:

- `2N` is split in the required Heegner packet;
- `L(E^D,1) != 0`;
- `L(E/K,s)` has analytic rank exactly one;
- corrected Disegni Theorem B applies at `p=2`;
- the p-adic height of the corresponding Heegner class is related exactly, in Disegni's normalization, to the cyclotomic derivative of the relevant p-adic L-function with explicit interpolation/test-vector factors.

The earlier generic label `p=2 p-adic Gross-Zagier applicability` is therefore no longer a frontier item for this auxiliary lane.

## Debt R1 — complex Gross-Zagier normalization

The target uses

`L'(E,1)/(Omega_E Reg_E)`

with the WP00 real Neron period and Neron-Tate regulator.

WP09 provides no equality between the p-adic height in Disegni's formula and this real regulator. A valid composition must instead bind an exact complex Gross-Zagier formula for the same auxiliary Heegner class and reconcile:

- `L'(E/K,1) = L'(E,1)L(E^D,1)`;
- the complex height of the Heegner point/class;
- the WP00 period convention;
- every local, modular-degree, Manin, isogeny, and test-vector normalization used to descend back to `E/Q`.

An equality of real and p-adic heights is neither assumed nor expected.

## Debt R2 — exact 2-primary Heegner index / Sha-Tamagawa relation

Even after an exact complex Gross-Zagier formula, the BSD valuation requires the index of the Heegner point relative to a Mordell-Weil generator to be converted into

`len_Z2 Sha(E/Q)[2^infinity] + sum_{ell|N} ord_2(c_ell)`.

A theorem only up to a 2-adic unit, up to a power of 2, or after inverting 2 is insufficient.

The needed input may be an integral p=2 Kolyvagin/Heegner-index theorem or an equivalent exact arithmetic-length theorem.

## Debt R3 — p-adic interpolation and local factors if the Iwasawa lane is retained

Disegni's formula contains `e_{2,infinity}` and `Q`. WP07 separately computed a forced unit-root factor in its own normalization. A future proof using the p-adic/Iwasawa lane must give an exact comparison showing how all such factors combine. They must not be identified by notation alone.

## Debt R4 — WP08 height-one `(2)` / relative-mu component

WP09 does not determine the missing global height-one `(2)` exponent of a cyclotomic characteristic relation.

Thus a main-conjecture route still needs an integral theorem such as

`mu_alg = mu_an`

or stronger integral characteristic/Fitting equality.

A direct arithmetic Heegner-index theorem may bypass this presentation, but only if it directly yields the required exact 2-primary length.

## Falsified shortcuts

The following routes remain invalid:

1. `p-adic Gross-Zagier applicable` therefore `complex BSD valuation`: false; different height and L-function objects remain.
2. `good ordinary` therefore all interpolation factors are 2-adic units: false; WP07 already exhibits a forced positive 2-adic valuation in one normalization.
3. `rank one` therefore Heegner point is a generator: false; the finite index is exactly arithmetic data that must be controlled.
4. `main conjecture away from (2)` therefore exact leading coefficient: false by WP08.
5. equality up to a power of 2: unusable for an `ord_2` target.

## Frontier

The smallest next source/theorem question is no longer whether p-adic Gross-Zagier exists at `p=2`. It is whether an admitted exact theorem supplies either:

- a fully normalized complex Gross-Zagier plus integral 2-primary Heegner-index composition sufficient to compute the target valuation; or
- an integral p=2 Iwasawa theorem closing the `(2)` exponent together with an exact p-adic-to-arithmetic leading-term comparison.

The direct arithmetic lane is preferred for the next reconnaissance because it can potentially bypass the independent WP08 mu defect rather than solving two deep inputs separately.