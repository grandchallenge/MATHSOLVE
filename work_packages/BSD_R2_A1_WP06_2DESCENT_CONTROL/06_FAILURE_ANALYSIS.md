# Failure analysis

## FR-01 — integral averaging by `(1 +/- tau)/2`

**Disposition:** terminated. Division by `2` is not integral over `Z_2` and can erase the target valuation. Replaced by the exact `I_n`/`Q_n` sequence.

## FR-02 — assume `M_n = M_n^+ direct_sum M_n^-`

**Disposition:** terminated. The intersection and quotient can both be nonzero. WP06 retains both as exponent-2 correction groups.

## FR-03 — extrapolate the mod-2 augmentation sequence to `2^n`

**Disposition:** terminated. The characteristic-2 exact sequence used in mod-2 quadratic descent does not lift naively to `Z/2^n`: the augmentation of the norm element is `2`, not `0`. WP06 instead uses inflation-restriction and genuine eigenspaces.

## FR-04 — declare nonsplit local defects zero

**Disposition:** terminated. The defect is the explicit group `H^1(Gal(K_w/Q_v),E(K_w))` or its twisted analogue. It vanishes at split places; otherwise it must be retained or proved zero.

## FR-05 — identify the global defect with the entire sum of local norm indices

**Disposition:** terminated. `D_n^+` and `D_n^-` inject into the local defect sums but need not fill them. Global reciprocity can impose relations. The exact global quotient is retained.

## FR-06 — use Kummer and Greenberg ordinary conditions interchangeably at 2

**Disposition:** terminated. The finite classical Selmer theorem uses Kummer conditions. The future Iwasawa route uses the separately defined ordinary condition from the connected-etale 2-divisible group. Split-at-2 auxiliary fields transport both without discrepancy.

## FR-07 — infer BSD from the Sha-length identity

**Disposition:** terminated. The identity compares arithmetic groups across the quadratic extension. It supplies no equality to the complex leading term. An integral reciprocity/height theorem is still required.

## Reopening rule

Any discarded shortcut may reopen only if an exact theorem computes the missing exponent-2 group or proves it zero under the unchanged selected hypotheses.