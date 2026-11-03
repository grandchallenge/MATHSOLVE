# FIGURATE-PILOT-001 — figurate Diophantine tuples

**Parent:** [MATH-PROGRAMME #3093](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3093)
**Status:** research pilot, not a new result or mathematical certification.
**Authority:** Human Steward activation of 2026-11-03, subject to protected repository policy.

## Two distinct definitions

For integers $k\geq3$, $t\geq1$, write $P_k(t)=((k-2)t^2-(k-4)t)/2$.

- **A: figurate entries.** Distinct positive $a_i=P_k(t_i)$ and $a_i a_j+n=x_{ij}^2$ for every pair.
- **B: figurate pairwise outputs.** Distinct positive $a_i$ and $a_i a_j+c=P_k(t_{ij})$ for every pair.
- **C: both constraints.** Distinct positive figurate entries and figurate pairwise outputs.

Never interpret a Type A published result as a Type B theorem. For Type B the square discriminant is a necessary but not sufficient membership test unless one enforces the exact nonnegative index and divisibility conditions:

$$
\bigl(2(k-2)t-(k-4)\bigr)^2=8(k-2)(ab+c)+(k-4)^2.
$$

## Prior art and novelty gates

1. S. Bagchi and C. Zhou-Zheng, [Diophantine m-tuples of Triangular Numbers](https://arxiv.org/abs/2608.27697), 2026. Type A: no triangular $D(1)$ quadruple, infinite family of triangular triples and conjecture of completeness; modular $D(n)$ exclusions.
2. A. Filipin, A. Jurasić and A. Togbé, [A note on the extension of some triangular Diophantine sets](https://doi.org/10.2478/auom-2026-0018), 2026. Type B: nonextension of certain pairs. Inspect precise hypotheses before generalizing.
3. [Dujella's Diophantine tuples bibliography](https://web.math.pmf.unizg.hr/~duje/ref.html). Search all relevant figurate, polygonal and centered-polygonal variants.

A finite census is only a bounded computation; evidence of novelty requires a source-specific literature review.

## Executable baseline

Run:

`python3 -m unittest discover -s tests -p test_figurate_census.py`

`python3 -m research.figurate_census --kind B --k 3 --offset 1 --limit 100 --size 3`

The code enumerates integers bounded by their **entry value**, not their polygonal index, via an exact compatibility graph, strictly increasing clique extension, and integer witnesses. Parameters are explicit; output is deterministic JSON with independently checkable witnesses. No floating point. The checker does not itself certify the exhaustive search implementation; the test suite compares small bounds to an independently enumerated brute-force implementation.

## Research obligations

- WP01: complete source-pinned bibliography, precise family taxonomy, claims and open-status audit.
- WP02: baseline search scaling, independently checked bounded datasets for $3\leq k\leq12$, small signed offsets, size 2–4 and documented upper entry limits.
- WP03: extract modular obstructions and residue filters with algebraically justified completeness; compare against generalized Pell methods.
- WP04: prove or disprove one parameter-uniform proposition or certified algorithmic result, then route genuinely novel substantive claims through specialist mathematical review and MATHCERT.

## Acceptance and stop conditions

Pilot advances only with a new proved result, a demonstrably improved algorithm with rigorous bounds, or a credible theorem route with evidence. Absence within a finite bound is not global nonexistence. Keep benchmark specifications, input domain, actual environment, versions and exact-output hashes. This PR provides initialization, not completed research or published MkDocs coverage.
