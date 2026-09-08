# BSD-R2-A1-WP10 — p=2 Heegner primitivity barrier

## Metadata

- Campaign: `BSD-001`.
- Work package: `BSD-R2-A1-WP10-P2-HEEGNER-BARRIER`.
- Native owner: `grandchallenge/MATHSOLVE#150`.
- Parent frontier: `BSD-R2-A1-2PRIMARY-HEEGNER-INDEX`.
- Protected Solve baseline: `561ad590c45e0a4916c1b2bbb658c0ba2aed9fb8`.
- Protected Forge baseline: `c44fef1d5d235b2e496bcee9ba0f7fc54212fa0d`.
- Programme provider refresh: PR `#917`, candidate head `c717223beee0ebabb4a8a19a0cb2f6b2941fc907`.
- Selected claim: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

## Result

WP10 closes one false continuation route and sharpens the surviving arithmetic frontier.

The standard odd-prime Heegner/Kolyvagin mechanism

`rank lowering -> primitive Heegner Kolyvagin system -> sharp Sha / Heegner-index equality`

cannot be mechanically specialized to `p=2` from the admitted literature interfaces.

The reason is twofold.

1. The screened sharp primitivity/index theorem of Burungale–Castella–Kim works in a setup with `p>3` and obtains the exact Sha/index equality only after importing odd-prime primitivity.
2. Chao Li proves a genuine mod-2 obstruction to the rank-lowering step in a stronger surjective-residual subcase: the relevant level raising sends a rank-one 2-Selmer situation to rank two rather than rank zero.

This is a route obstruction, not an impossibility theorem for all p=2 Heegner or Kolyvagin methods.

## Auxiliary-field cost

WP06 already proves an exact large-`n` quadratic-descent identity. Therefore even a future exact Heegner-index theorem over the WP09 auxiliary field `K=Q(sqrt(D))` would not by itself isolate the target over `Q`.

One must also determine the exact 2-primary contribution of the rank-zero twist `E^D/Q` and the explicit WP06 descent defect groups. The all-split choice removes the dangerous local defects at `2` and every `ell|N`, but it does not make all remaining global or nonsplit-place correction groups disappear by fiat.

The same issue is visible analytically:

`L'(E/K,1) = L'(E,1) * L(E^D,1)`

because `L(E,1)=0` and `L(E^D,1) != 0`.

Thus an auxiliary-`K` complex Gross-Zagier formula introduces the exact rank-zero twist factor. At `p=2`, that factor may not be discarded as a unit without a theorem computing its valuation in the protected normalization.

## Surviving frontier

The direct arithmetic lane now requires a genuinely integral p=2 theorem of one of the following forms:

- a new p=2 Heegner/Kolyvagin primitivity theorem plus a sharp exact index/Sha-Tamagawa formula and the required twist/descent reconciliation;
- a direct exact 2-primary arithmetic-length theorem over `Q` that bypasses auxiliary-field primitivity entirely;
- another exact arithmetic mechanism yielding the WP00 valuation with every 2-primary correction explicit.

The separate Iwasawa lane remains admissible but still carries WP08's independent height-one `(2)` / relative-mu debt and the p-adic-to-complex normalization debt recorded by WP09.

## Source boundary

The route diagnosis uses only the protected Forge audit

`sources/BSD-001/HEEGNER_PRIMITIVITY_P2_BARRIER_SOURCE_AUDIT.md`

with blob `1b9f156447ff2bc87dfd08f413f7d22d31f5b66a`.

This candidate must not merge until Programme PR #917 has protected the corresponding provider-manifest identity.

## Claim boundary

WP10 does not prove:

- a general no-go theorem for p=2 Heegner/Kolyvagin methods;
- Chao Li's obstruction for every irreducible `E[2]`;
- a p=2 primitivity theorem;
- an exact 2-primary Sha/index formula;
- the rank-zero twist 2-part of BSD;
- `BSD-R2-A1`;
- novelty, priority, or MATHCERT certification.
