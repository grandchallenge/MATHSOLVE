# BSD-001 WP60H frontier — four-fiber odd-relation reduction

## Protected entering state

- MATHSOLVE: `1b75a922e2779178f478124948008afdd7e26a17`.
- MATHFORGE affine-fiber interface: `7da6813fcde7eb5f9badd7c86946f58691ed6f0d`.
- MATHFORGE minimal-core transition interface: `54f1eaea24b35d4ca37e778786345c3622b6fd98`.
- Tracker: `grandchallenge/MATHSOLVE#215`.
- Owner: `grandchallenge/MATHSOLVE#164`.
- Target: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

## WP60H theorem

Let `V` be an `F_2`-vector space, `G` a group,

`j:V -> Hom(G,F_2)`

injective and linear, and

`a:V -> F_2`

linear. For nonzero `c_i in V`, define the bad affine fibers

`H_i={g in G : j(c_i)(g)=a(c_i)}`.

Then

`union_i H_i = G`

if and only if the classes `c_i` admit an odd-cardinality linear dependence.

For four nonzero classes this specializes to:

`H_1 union H_2 union H_3 union H_4 = G`

if and only if some three of `c_1,c_2,c_3,c_4` sum to zero.

Under the protected WP60G residual self-dual BSS interface, this criterion applies to simultaneous localization.

## Minimal-core specialization

Protected MATHFORGE WP60H admits the exact BSS transition used by Lemma 5.15 / Corollary 5.16.

For two minimal core vertices `n_1,n_2`, choose `q_i|n_i` and set `m_i=n_i/q_i`. Then:

- `m_i` is noncore;
- `lambda(m_i)=r+1`;
- `lambda^*(m_i)=1`;
- the common-prime step needs nonzero localization of both primal spaces `H^1_{F(n_i)}` and both one-dimensional dual spaces `H^1_{F^*(m_i)}`;
- primal witnesses are not fixed by the source and may be chosen strategically if the choice genuinely proves the required nonzero map from the space.

Hence the literal-`2` `s=2` failure mode is exactly an exceptional three-term relation among the selected four witness classes.

The protected dimension/inclusion/local-condition interface does not itself assert that this relation is absent. Do not infer exclusion from the words `finite` and `transverse` or from dimensions alone.

## Refined F1 boundary

Record

`MISSING_P2_BSS_MINIMAL_CORE_THREE_TERM_RELATION_EXCLUSION_OR_REPLACEMENT_CONNECTIVITY`.

This refines

`MISSING_P2_TWO_CORE_VERTEX_SIMULTANEOUS_LOCALIZATION_OR_REPLACEMENT_CONNECTIVITY`

and the parent

`MISSING_P2_CORE_VERTEX_SIMULTANEOUS_LOCALIZATION_FOR_BSS_FITTING_CONTROL`.

## Highest-value F1 successor

Use additional global structure, not generic counting.

Admissible successor modes are:

1. derive a Poitou–Tate/global-duality incompatibility for every possible exceptional three-term relation;
2. exploit strategic primal-witness freedom and prove witnesses can always be chosen with no odd relation;
3. show that any exceptional relation itself yields an alternate core-vertex graph path;
4. prove replacement connectivity independently of the one-common-prime construction.

If none of these can be supplied, protect the exact global relation boundary and preserve other R5 routes.

## Parallel F2 successor

F2 is logically independent and may be attacked in parallel:

`MISSING_P2_ELLIPTIC_H2_H3_VERIFICATION_OVER_F2_INFINITY`.

The next F2 audit should use the exact BSS definitions of H2/H3 and test literal-`2` restricted-image/cohomology arguments directly. Do not infer H2/H3 from residual `E[2]` surjectivity by assertion.

A potentially useful H2 direction is to test whether odd multiplicative inertia for the selected semistable curve supplies a rank-one unipotent element inside the required restricted Galois group; this is only a research direction until the exact inertia and field-containment statements are proved/admitted.

## Parent route state

- R1: `MISSING_LITERAL_P2_HEEGNER_INDEX_PARITY`.
- R2: `MISSING_EXACT_WP00_TWIST_LRATIO_VALUATION_UNDER_WP09_CONSTRAINTS`.
- R3: retired on selected lane by WP60B.
- R4: `R4_EQUIVALENT_TO_FIXED_BASE_ANALYTIC_LEADING_TERM_VALUATION`.
- R5-LIFT: `MISSING_P2_KATO_ZETA_FITTING_DIVISIBILITY_AT_HEIGHT_ONE_2`.
- R5-PRIM: `MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`.
- D2a: `MISSING_P2_K_HEIGHT_NONDEGENERACY`.
- D2d: `MISSING_LITERAL_P2_COMBINED_HEEGNER_INDEX_TWIST_LRATIO_THEOREM_WITHOUT_EXTRA_MOD2_LOG_OR_RANKZERO_SEED`.
- D2e: downstream `MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

`BSD-R2-A1` remains unproved.

## Claim firewall

WP60H does not prove the actual three-term relation absent or present, the `s=2` common-prime theorem, literal-`2` core-vertex connectivity, BSS H2/H3, BSS Fitting control, R5 closure, `BSD-R2-A1`, or any MATHCERT claim.
