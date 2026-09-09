# Next mathematical boundary after WP15

## Refined boundary

`MISSING_UNIFORM_UNSQUARED_P2_LENGTH_CONTROL`

This refines the parent boundary

`MISSING_UNIFORM_INTEGRAL_P2_ARITHMETIC_LENGTH_THEOREM`.

The distinction is material. WP15 proves that square-class information is not merely absent; it is mathematically too coarse to recover the selected integer length.

## Exact unknown

Put

`delta_2(E) := ord_2(L'(E,1)/(Omega_E Reg_E)) - sum_{ell|N} ord_2(c_ell)`.

Protected work gives:

- `delta_2(E)` is the exact analytic-minus-local integer whose value must be identified;
- `len_Z2 Sha(E/Q)[2^infinity]` is a finite even nonnegative integer;
- a modulo-square BSD theorem could at most imply `delta_2(E)` is even;
- WP13 already makes every local bad-prime Tamagawa `2`-power explicit;
- WP12 makes residual surjectivity automatic;
- WP14 removes the auxiliary level-raising-prime existence issue but exposes separate local/minimal-Selmer restrictions in the Chao Li route.

The unproved equality remains

`delta_2(E) = len_Z2 Sha(E/Q)[2^infinity]`.

## What would close the boundary

A successful successor must provide at least one of the following, uniformly for the full selected class and in compatible normalization:

1. **Exact saturation/primitivity.** A genuine integral `p=2` Kolyvagin/Euler-system saturation theorem whose complete local defect is exactly the WP13 Tamagawa length.
2. **Direct arithmetic length.** An exact theorem over `Q` identifying `delta_2(E)` with the `2`-primary Sha length without passing through an odd-prime primitivity argument.
3. **Sharp two-sided or rigidity control.** Integer-valued `p=2` bounds plus an independent rigidity theorem strong enough to force the exact value. Parity alone is insufficient.
4. **Different exact leading-term mechanism.** A source or in-package theorem that directly produces the selected complex leading-term valuation with every power of `2` retained.

Any auxiliary-`K` solution must still satisfy the WP10 composition obligations for the rank-zero twist and the WP06 descent defects unless it proves a direct `Q`-side formula that bypasses them.

## Screened routes that do not close it

The protected Forge screen at `118ae1b5c2fc2630f53000921b742c610c50db16` records:

- Barrios–Mok: square-class transport only;
- Jetchev: Tamagawa-aware Kolyvagin bound restricted to odd `p`;
- Kriz–Li: positive but restricted BSD(2) twist-family technology with odd-Tamagawa/Heegner-indivisibility and seed hypotheses;
- Yan–Zhu: good-ordinary applications for `p>2`.

These exclusions apply only to the exact screened interfaces. They are not a claim that the literature contains no closing theorem.

## Legitimate continuation boundary

Routine algebraic, local, source-applicability, and normalization deductions available from the protected stack have been exhausted through WP15. The next step that could actually prove the selected equality requires either:

- proving a materially new uniform unsquared `p=2` arithmetic theorem; or
- admitting an authoritative theorem with that exact content and applicable hypotheses.

Boundary name: `MISSING_UNIFORM_UNSQUARED_P2_LENGTH_CONTROL`.

`BSD-R2-A1` remains unproved and MATHCERT remains pending.