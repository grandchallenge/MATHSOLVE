# BSD-R2-A1 WP60H — four-fiber relation reduction

## Purpose

Continue WP60G's literal-`p=2` F1 attack from the repaired one-primal/one-dual case to the `s=2` four-constraint step used in the BSS minimal-core-vertex connectivity argument.

This package first proves an exact affine-cover criterion for any finite self-dual residual `F_2` family. It then specializes that criterion to four BSS constraints.

The package does not yet assert that the actual four classes arising from two minimal core vertices avoid the exceptional three-term relation. That is the next arithmetic/graph obligation.

## Protected inputs

- MATHSOLVE base: `1b75a922e2779178f478124948008afdd7e26a17`.
- MATHFORGE BSS affine-fiber interface: `7da6813fcde7eb5f9badd7c86946f58691ed6f0d`.
- WP60G pairwise localization theorem protected in the MATHSOLVE base.
- Tracker: `grandchallenge/MATHSOLVE#215`.
- Owner: `grandchallenge/MATHSOLVE#164`.

## Main theorem

Let `V` be an `F_2`-vector space of cohomology classes, let

`j:V -> Hom(G,F_2)`

be injective and linear, and let

`a:V -> F_2`

be linear. For nonzero `c_1,...,c_m in V`, define

`H_i={g in G : j(c_i)(g)=a(c_i)}`.

Then the complement of `union_i H_i` is nonempty if and only if every linear relation

`sum_i eps_i c_i=0`

has even Hamming weight `sum_i eps_i`.

Equivalently, the bad fibers cover `G` if and only if there is an odd-cardinality linear dependence among the `c_i`.

For four nonzero classes, coverage occurs if and only if some three of the four classes sum to zero.

## BSS consequence

After a residual self-duality `A ~= A^*(1)`, the protected BSS maps and affine constants fit exactly into this theorem. Therefore the literal-`2` `s=2` common-prime problem is no longer a generic four-hyperplane problem. It is exactly the question whether the four identified BSS cohomology classes carry a three-term relation.

Record the refined boundary:

`MISSING_P2_BSS_MINIMAL_CORE_THREE_TERM_RELATION_EXCLUSION_OR_REPLACEMENT_CONNECTIVITY`.

This refines, but does not yet close,

`MISSING_P2_TWO_CORE_VERTEX_SIMULTANEOUS_LOCALIZATION_OR_REPLACEMENT_CONNECTIVITY`.

## Highest-value successor

Read the exact BSS Lemma 5.15 / Corollary 5.16 modified-Selmer configuration and test the three possible types of three-term relation using the actual local conditions at the distinguished primes removed from the two minimal core vertices.

If every three-term relation is excluded, the common-prime step is recovered at literal `2` under the remaining BSS hypotheses. If not, determine whether the relation itself gives an alternate graph path. Do not infer either outcome without the exact modified-Selmer transition data.

## Claim firewall

WP60H does not establish:

- absence of the actual three-term relation in the BSS minimal-core configuration;
- the `s=2` common-prime step;
- minimal-core graph connectivity;
- full F1 closure;
- BSS Hypothesis 3.2/H2/H3 for the selected class;
- the BSS Fitting theorem at `p=2`;
- R5-LIFT, R5-PRIM, `BSD-R2-A1`, or MATHCERT certification.
