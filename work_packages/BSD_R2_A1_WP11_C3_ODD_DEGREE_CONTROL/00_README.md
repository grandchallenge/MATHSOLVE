# BSD-R2-A1-WP11 — exact `C3` residual-branch control

## Metadata

- Campaign: `BSD-001`.
- Work package: `BSD-R2-A1-WP11-C3-ODD-DEGREE-CONTROL`.
- Native owner: `grandchallenge/MATHSOLVE#152`.
- Parent frontier: `BSD-R2-A1-2PRIMARY-DIRECT-LENGTH`.
- Protected Solve baseline: `0b55f84677ba332f58feb5569bec22b7d269862d`.
- Selected claim: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

## Scope

WP10 proved that irreducible `E[2]` has residual image either `C3` or `S3 ~= GL_2(F_2)`. WP11 treats only the `C3` branch.

Set

`L := Q(E[2])`.

Under the `C3` branch, `Gal(L/Q) ~= C3`.

## Proved results

WP11 proves in-package:

1. every prime dividing `2N` splits completely in `L/Q`;
2. `L/Q` is totally real;
3. for every `n >= 1`, restriction gives exact isomorphisms

   `Sel_{2^n}(E/Q) ~= Sel_{2^n}(E/L)^{C3}`

   and

   `Sha(E/Q)[2^n] ~= Sha(E/L)[2^n]^{C3}`;

4. passing to direct limits gives

   `Sha(E/Q)[2^infinity] ~= Sha(E/L)[2^infinity]^{C3}`;

5. because `3` is a unit in `Z_2`, the averaging idempotent

   `e = (1 + sigma + sigma^2)/3`

   is integral on every 2-primary `C3`-module. Hence Selmer and Sha over `L` split canonically into the base invariant summand and the cubic-new norm-zero summand, with no 2-primary intersection or cokernel;
6. the `C3` branch forces the minimal discriminant square class to be trivial. For each semistable bad prime `ell|N`, `n_ell := ord_ell(Delta_min)` is even, and

   - split multiplicative: `ord_2(c_ell) = ord_2(n_ell)`;
   - nonsplit multiplicative: `c_ell = 2`, so `ord_2(c_ell)=1`.

## Meaning

The `C3` branch does not suffer the quadratic `1/2` projector defect diagnosed in WP06. Its residual splitting field has odd degree, so all 2-primary restriction/corestriction defects vanish exactly.

This does not prove the direct-length identity. It instead splits the uniform frontier into two genuinely different branches:

- `C3`: exact odd-degree descent is now closed; the missing theorem is the direct arithmetic leading-term/length bridge itself (or an exact cubic-new computation if one works over `L`);
- `S3`: the p=2 primitivity/rank-lowering obstruction and quadratic-type 2-primary issues remain.

## Claim boundary

WP11 does not prove `BSD-R2-A1`, a p=2 Kolyvagin primitivity theorem, an exact Sha/index formula, a direct-length theorem, novelty/priority, or MATHCERT certification.
