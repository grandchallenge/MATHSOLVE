# Iwasawa interface and exact debt

## Characteristic elements

For a finitely generated torsion `Lambda=Z_2[[T]]` module `M`, let `f_M` be a generator of its characteristic ideal. Define

`mu(M)=v_(2)(f_M)`.

Changing `f_M` by a unit does not change this integer.

For an analytic element `L_2(T) in Lambda`, define analogously

`mu_an(L_2)=v_(2)(L_2)`.

These definitions concern the global cyclotomic Iwasawa algebra. They are not the WP07 local Euler/interpolation multiplier.

## Conditional main-conjecture firewall

Suppose a future theorem establishes

`(f_M) Lambda[1/2] = (L_2) Lambda[1/2]`.

WP08 Theorem 1 then gives

`f_M = 2^delta u L_2`

in the total quotient field, with

`delta = mu(M)-mu_an(L_2)`.

Therefore the integral main conjecture

`(f_M)=(L_2)`

holds exactly when `delta=0`.

Equivalently, an away-from-`(2)` main conjecture plus equality of the analytic and algebraic mu exponents yields the full principal-ideal equality. Without the mu equality, the localization does not determine the integral statement.

## Leading-term consequence

If the two sides also have the same augmentation order `r`, then after removing `T^r`, the first nonzero coefficients differ in `ord_2` by exactly `delta`.

For a rank-one BSD route this is decisive: an unknown `delta` cannot be absorbed into a unit because `2` is not a unit in `Z_2` and the target asks for the exact `ord_2` of the leading term.

## What Kato does and does not imply here

Current external reconnaissance of Kato's primary 2004 paper records two distinct statements relevant to this interface:

- his p=2 formulation of the height-one main-conjecture comparison excludes a height-one prime containing `2`;
- the ordinary Euler-system theorem gives a one-sided characteristic-length statement at height-one primes not containing `p`.

Therefore WP08 must not be read as saying that Kato already proves the conditional away-from-`(2)` equality displayed above. Kato supplies important one-sided and cotorsion information, but the equality hypothesis in the firewall is intentionally stronger.

The logical point is instead:

> even if the remaining non-`(2)` reverse divisibility were supplied, the exact 2-primary BSD route would still need the `(2)` exponent.

## Two independent remaining debts

The campaign now distinguishes:

`MU-DEBT` — determine the integral height-one `(2)` component, equivalently the relative analytic/algebraic mu exponent for a main-conjecture route, or bypass it by a direct exact arithmetic theorem;

`RECIPROCITY-DEBT` — identify the relevant rank-one p-adic/Heegner object with the WP00-normalized complex derivative and regulator, retaining the WP07 unit-root multiplier and all Tamagawa, period, isogeny, Manin, Euler, and height corrections.

Neither debt implies the other.