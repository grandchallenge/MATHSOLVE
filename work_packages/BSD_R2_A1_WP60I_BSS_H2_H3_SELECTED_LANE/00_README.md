# BSD-R2-A1 WP60I — selected-lane BSS H2/H3 determination

## Purpose

Continue the independent F2 obligation isolated by WP60F:

`MISSING_P2_ELLIPTIC_H2_H3_VERIFICATION_OVER_F2_INFINITY`.

WP60I determines the exact selected-lane outcome rather than assuming that the odd-prime BSS verification extends to `p=2`.

## Protected inputs

- INTELLECT: `fc9ee5537bf07586dffcc621e753204ecd835365`.
- MATHSOLVE base: `a73525fefc362aa4e1e03f006a46fd1dc3b961e8`.
- MATHFORGE: `54f1eaea24b35d4ca37e778786345c3622b6fd98`.
- Tracker: `grandchallenge/MATHSOLVE#215`.
- WP60I operation: `grandchallenge/MATHSOLVE#225`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.

Material protected predecessors:

1. WP12: every selected irreducible residual representation has image `GL_2(F_2) ~= S3`;
2. WP13: at every odd semistable bad prime `ell`, with `n_ell=ord_ell(Delta_min)`, inertia on `E[2^m]` is given in a Tate basis by `[[1,n_ell t_m],[0,1]]`, with `t_m` surjective;
3. MATHFORGE WP60F: exact BSS standard hypotheses `(H2)` and `(H3)` and the fact that the published elliptic verification uses `p>3`.

## Result

For every curve in the selected semistable, odd-conductor, good-ordinary-at-`2`, irreducible-`E[2]` lane:

1. there is an odd bad prime `ell` for which `n_ell` is odd;
2. the restricted `2`-adic image over `Q(mu_{2^infinity})` contains a primitive unipotent, so the formal literal-`2` BSS hypothesis `(H2)` holds;
3. the restricted mod-`4` image is `SL_2(Z/4)` and the full mod-`4` image is `GL_2(Z/4)`;
4. `H^1(GL_2(Z/4),F_2^2)` is nonzero; an exact 96-element finite verifier is included;
5. inflation therefore gives a nonzero class in the first BSS `(H3)` cohomology group for `K=F=Q`, and self-duality gives the same conclusion for the dual group.

Hence the selected lane satisfies `(H2)` but fails `(H3)` at literal `p=2`.

Record:

`BSS_LITERAL_P2_SELECTED_H2_HOLDS_H3_FAILS`.

The former F2 uncertainty is therefore replaced by the negative route disposition

`R5_BSS_STANDARD_HYPOTHESIS_ROUTE_BLOCKED_BY_H3_AT_LITERAL_P2`.

This blocks the currently screened BSS standard-hypothesis application architecture for the selected lane. It does not prove that every possible BSS-derived or Kolyvagin-system argument at `p=2` is impossible; a theorem that removes or bypasses `(H3)` remains a legitimate reopening form.

## Verification

Run:

```bash
python work_packages/BSD_R2_A1_WP60I_BSS_H2_H3_SELECTED_LANE/02_GL2Z4_H1_CERTIFICATE.py
```

The verifier enumerates all `96` elements of `GL_2(Z/4)`, proves the displayed generators generate the whole group, constructs a crossed homomorphism on all group elements, checks the cocycle identity on all `96^2=9216` ordered pairs, and proves it is not a coboundary by evaluating it on an element acting trivially on `F_2^2`.

## Route effect

- F1 remains open at `MISSING_P2_BSS_MINIMAL_CORE_THREE_TERM_RELATION_EXCLUSION_OR_REPLACEMENT_CONNECTIVITY`.
- F2 is no longer a missing verification; it is determined negatively because `(H3)` fails.
- The standard BSS route cannot close R5 for the selected lane without a new theorem that bypasses `(H3)`.
- R5-LIFT, R5-PRIM, R1, R2, R4, D2a, D2d and D2e remain unchanged.
- `BSD-R2-A1` remains unproved.

## Claim firewall

WP60I does not establish:

- F1 closure or literal-`2` core-vertex connectivity;
- a literal-`2` BSS Fitting theorem;
- impossibility of every alternative Kolyvagin/Fitting argument;
- R5-LIFT or R5-PRIM;
- `BSD-R2-A1`;
- MATHCERT certification, novelty, or priority.
