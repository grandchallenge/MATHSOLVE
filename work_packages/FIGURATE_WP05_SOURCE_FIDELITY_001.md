# FIGURATE-WP05 — primary-source fidelity checkpoint 001

**Date:** 2026-11-03. **Status:** PARTIAL SOURCE RECONSTRUCTION, not a completed full-text proof audit. **Parent:** [FIGURATE-PILOT-001](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3093); [WP05](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3096).

## Method and evidence tier

The source-linked bibliography was checked against publisher and arXiv abstract/metadata pages. The checked statements below are those *explicitly asserted in those pages*. Neither the complete source PDFs nor theorem-numbered proof bodies were accessible through the current retrieval route, so theorem numbering, intermediate lemmas, and proof dependencies remain **UNVERIFIED**. This is a narrower checkpoint than WP05's full acceptance requirement.

| ID | Exact source identifier and version | Type, offset and declared content | Confirmed scope and exclusion | Evidence tier |
| --- | --- | --- | --- | --- |
| F01 | Bagchi and Zhou-Zheng, [arXiv:2608.27697v1](https://arxiv.org/abs/2608.27697), submitted 2026-08-27 | A, triangular entries: classical square-output tuples. No all-triangular D(1) quadruple; constructs infinite D(1) triple family *conjectured* to be complete. For general n, no all-triangular D(n) pair if n congruent to 2 or 5 modulo 9. Also describes generalized-Pell pair testing with claimed asymptotic cost O(sqrt(a)) for the relevant fixed input and a local-solubility discussion. | Not a nonexistence theorem for all offsets; not a Type B theorem; triple completeness remains conjectural. | Authors' arXiv abstract; theorem-numbered proof not inspected |
| F02 | Pavao Radić, [arXiv:2609.28018v1](https://arxiv.org/abs/2609.28018), submitted 2026-09-23 | A, triangular entries and **variable** square offset u². Abstract classifies triples whose smallest entry equals T(4u−1) or T(4u), proves infinitely many u admit an all-triangular quadruple, and states that T(16k²−1) occurs in infinitely many quadruples over distinct positive integer u for each positive k. | No contradiction with F01 at fixed offset +1. Does not assert a complete classification of all offsets or all quadruples. | Authors' arXiv abstract; theorem-numbered proof not inspected |
| F03 | Filipin, Jurasić and Togbé, [DOI:10.2478/auom-2026-0018](https://reference-global.com/article/10.2478/auom-2026-0018), *An. Sci. Univ. Ovidius Constanţa*, 34(2), pp. 29–43, published 2026-07-11 | B, triangular *outputs*, arbitrary distinct positive entries: special triangular D(k) pair {k,2k}, for **k = 10 or 28**. Abstract proves this specified set cannot extend to a quadruple. | The paper's k is the **additive offset**, whereas FIGURATE code's k denotes polygonal order. No blanket Type B quadruple prohibition or exclusion for other offsets follows. | Publisher abstract and bibliographic record; complete proof not inspected |
| F04 | Filipin, Jurasić and Szalay, *Extensions of the triangular D(3)-pair {3,6}*, *Math. Slovaca* 75 (2025), 775–790 (cited in F03 publisher reference #4) | B, triangular outputs, fixed offset 3 and prescribed pair {3,6}. | **Newly elevated source dependency:** the prior bibliography mentioned general extensions but did not single out this exact 2025 constraint. Its theorem conclusions require primary full-text inspection. | Publisher bibliography citation only |
| F05 | Filipin and Szalay, *Triangular Diophantine tuples from {1,2}*, 2023 (cited as F03 reference #5) | B, triangular outputs, a prescribed initial pair {1,2}. | Existing source catalogue asserts the unit-offset nonextension; source-accurate theorem hypotheses and full text remain to be checked. | Secondary reference within a primary publisher page; proof unverified |

**Source fidelity decision:** For a source-specific theorem claim, the above evidence permits only explicit abstract-level attribution. The WP05 final gate must still recover full primary texts, capture version hashes/pages/theorem numbers, and compare exact logical hypotheses. No broad statement is upgraded from this checkpoint.

## Research target correction: universal Type B pair obstruction is impossible

**Elementary proposition (direct proof, not a claim of novelty).** Fix any polygonal order $k\geq3$ and any integer offset $c$. There are infinitely many distinct positive-integer Type B pairs satisfying

$$
ab+c=P_k(t), \qquad a\ne b.
$$

**Proof.** Take $a=1$ and $b=P_k(t)-c$. Since the polygonal sequence is unbounded and eventually strictly increasing, there are infinitely many positive indices $t$ with $b>1$. For every such $t$ we have $ab+c=P_k(t)$, the pair is positive and its entries are distinct. Distinct sufficiently large indices produce distinct $b$. This proves the claim.

**Consequence.** A proposed theorem of the form *for some k and offset c no Type B pair exists*, without further restrictions on entries, is false. A residue-class obstruction that excludes all Type B pairs for an entire offset class is therefore impossible. Local obstructions can still meaningfully exclude **prescribed entry residue classes**, **prescribed pairs**, **extensions to triples/quadruples**, or **Type C** combinations.

This observation is consistent with, and does not weaken, F01's all-triangular Type A pair exclusions: F01 restricts *both entries* to triangular values.

## Refined mathematical obligations

1. Reconstruct F01–F05 full theorem bodies, with explicit version pinned and proof-dependency matrix. In particular, inspect the 2025 prescribed triangular D(3)-pair result before classifying any analogous FIGURATE conjecture.
2. Revise WP07 targeting: search for congruence obstructions to **extension of fixed Type B pairs**, bounds on cliques under constrained entry classes, and Type C obstructions. Reject universal unrestricted Type B pair nonexistence proposals at preflight.
3. Attach reproducible finite searches or simple arithmetic proofs to each candidate, distinguish necessary local conditions from global impossibility, and carry mathematical propositions through the standard review/certification boundary.

**Documentary state:** This checkpoint closes the abstract/publisher-verified classification tranche and the Type B pair no-go preflight, but **does not close WP05**. The parent issue and WP05 remain open for proof-level source reconstruction.
