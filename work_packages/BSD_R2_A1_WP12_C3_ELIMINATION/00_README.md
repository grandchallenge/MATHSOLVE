# BSD-R2-A1-WP12 — eliminate the residual `C3` branch

## Metadata

- Campaign: `BSD-001`.
- Work package: `BSD-R2-A1-WP12-C3-ELIMINATION`.
- Native owner: `grandchallenge/MATHSOLVE#156`.
- Protected Solve baseline: `5579d6c74cfa1c28b84d3448c08679e0b828a0e9`.
- Selected claim: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

## Result

WP12 proves that the `C3` residual-image branch isolated in WP10 and analysed in WP11 is empty under the full selected hypotheses.

Therefore, for every curve in `BSD-R2-A1`,

`E[2] irreducible  =>  im(rho_bar_{E,2}) = GL_2(F_2) ~= S3`.

Since WP10 already proved that an irreducible mod-2 image is either `C3` or `S3`, this implication is exact for the selected semistable, odd-conductor, good-ordinary-at-2 class.

## Proof architecture

Assume for contradiction that the image is `C3`, and set `L=Q(E[2])`.

WP11 gives:

- `Gal(L/Q)=C3`;
- every prime dividing `2N` splits completely in `L/Q`;
- `L` is totally real.

For a finite prime `ell` not dividing `2N`, the selected semistable conductor hypothesis gives good reduction and `ell != 2`. The kernel of multiplication by `2` on the good integral model is finite etale over `Z_ell`, so inertia acts trivially on `E[2]`. Hence `L/Q` is unramified at `ell`.

Thus `L/Q` is unramified at every finite prime. Its absolute discriminant is therefore `1`.

A direct degree-3 Minkowski argument rules out a totally real cubic field of discriminant `1`; see `01_C3_ELIMINATION_THEOREM.md`.

Contradiction.

## Consequence for the research frontier

The former two-branch direct-length frontier collapses to

`BSD-R2-A1-S3-DIRECT-LENGTH`.

Residual surjectivity is no longer an additional hypothesis in this campaign. However, source theorems that assume surjectivity may still impose other local, Heegner, conductor, or Selmer hypotheses; WP12 does not declare those automatic.

## Claim boundary

WP12 does not prove `BSD-R2-A1`, p=2 Kolyvagin primitivity, an exact Sha/index formula, the direct-length equality, novelty/priority, or MATHCERT certification.
