Search weighted clique-cluster templates whose infinite blow-up families improve the published upper bound for the four-clique Ramsey multiplicity constant.

## The open mathematical target

Color every edge of a complete graph red or blue. Let M4(G) be the number of four-vertex subsets whose six edges have the same color. The Ramsey multiplicity constant is

    c4 = lim(n -> infinity) min_{|V(G)|=n} M4(G) / binom(n,4).

The exact value of c4 is open in the literature inspected for this version. This hill targets a concrete advance on that infinite extremal problem:

    Construct a sequence of finite two-colored complete graphs, of unbounded
    order, whose limiting monochromatic K4 density is strictly below
    B* = 10486266368 / 768^4 = 0.030142273431942788...

B* is McKay's improved construction recorded in the final note of Parczyk, Pokutta, Spiegel and Szabo, arXiv:2206.04036v3 (2024; journal issue 2025). It is stronger than the paper's headline Theorem 1.1 bound 4551721/(2^24*9). Merely reproducing that headline theorem is NOT research progress against B*.

Open-status review date: 2026-09-19. This is a frozen, sourced reference, not a promise that a literature search is exhaustive. See SOURCES.md. A new bound must also pass novelty and competition review before being called a new research result.

## Why clique clusters are relevant

Alejandro Zarzuelo Urdiales's clique-cluster work studies replacing vertices with coding cliques, retaining weighted or multigraph information, and enumerating graphs by clique number. The search language here also replaces vertices by clusters, with exact control of connections and clique counts. Each cluster is a clique in one of the two colors; its size is an integer weight.

This is a related construction language, not an assertion that the CC encoding automatically preserves Ramsey density. Its coding gadgets may introduce many extra cliques. Any proposed use of that encoding must be measured on the resulting template by this evaluator. No unproved transfer principle or result from the organizer's papers is assumed for scoring. Read LIFTING.md for the elementary, self-contained theorem that connects a certificate to an infinite family.

## Certificate and the infinite family it defines

Submit a directory containing a regular, non-symlink solution.json:

```json
{
  "schema": "weighted-two-color-blowup-v1",
  "weights": [1, 1],
  "red_rows": ["01", "10"]
}
```

There are m blocks, 1 <= m <= 1024. Each weight w_i is an integer from 1 to 65535. The list red_rows encodes a symmetric m by m matrix A of bits as strings. For i != j, A_ij=1 means all inter-block edges are red, and 0 means blue. The DIAGONAL is meaningful: A_ii=1 makes block i a red clique, while A_ii=0 makes it a blue clique. These are not self-loops in the resulting simple graph.

For EVERY positive integer t, expand block i to t*w_i distinct vertices. The resulting graph G_t has t*Q vertices, where Q=sum(w_i). Thus one certificate defines arbitrarily large graphs. Common scaling of all weights does not change its density; the verifier divides out their greatest common divisor.

The exact limit is

    P(A,w) = (1/Q^4) sum_{i,j,k,l=0}^{m-1} w_i*w_j*w_k*w_l *
      [ A_ij*A_ik*A_il*A_jk*A_jl*A_kl
        + (1-A_ij)*(1-A_ik)*(1-A_il)*(1-A_jk)*(1-A_jl)*(1-A_kl) ].

Repeated indices MUST be included: two different vertices in a large cluster have the same template index. Counting only four distinct template vertices gives the wrong limit. The evaluator performs exact integer counting and rational comparisons. It returns P as a reduced fraction and separately returns the red and blue integer counts.

The example above has P=1/8. It illustrates the schema and is not a competitive seed or new mathematics. Start serious work from examples/published_cayley_768/solution.json, the attributed published construction supplied with this hill. Its density is 4551721/(2^24*9), which does NOT beat B*.

## Progress, success, and resolution

1. **Search progress:** decrease exact P compared with your previous submission. This improves your construction, but does not alone establish a previously unknown mathematical bound.
2. **The hill's bound-improvement target is achieved:** a valid certificate has exact P < B*. The evaluator sets reference_beaten=1 and target_achieved=true. This gives a checked candidate upper bound c4 <= P < B*, via the lifting theorem. Equality with B* earns no success flag. Novelty, attribution, and an approved formal/certificate trust boundary still require review.
3. **Full resolution of the parent problem:** prove the exact value of c4, including a universal lower bound matching a construction. This evaluator accepts upper-bound constructions only, and ALWAYS reports parent_problem_resolved=false. A record improvement does not resolve the exact-value problem.

No finite catalog is being completed. There is no "all cases solved" condition. Reaching a local optimum, using all 1024 blocks, or running out of time proves neither optimality nor nonexistence of a better template. Templates are one allowed construction class, not a characterization of every asymptotically optimal graph sequence.

## Scoring

| Metric | Direction | Exact meaning |
|---|---|---|
| reference_beaten | maximize | 1 iff the exact rational P is strictly less than B*, otherwise 0. |
| density_ppt | minimize | ceil(10^12 * P); an integer upper rounding of density in parts per trillion. |

Ranking is lexicographic. P itself and the exact gap B*-P are in report details. Changes smaller than 10^-12 can tie on the display metric; exact fractions must be used for any mathematical comparison. The success flag uses exact arithmetic, even for such small changes. A passing report means a valid certificate, not that the research target has been achieved or that the competition jury has accepted a solution.

## Validation and final evaluation

The mathematical objective is deterministic and uses every entry of the submitted template. Both modes compute the SAME P. This is a certificate task, so a held-out sample of graphs would provide no additional evidence about the infinite family and is not used.

private/validation.json and private/test.json instead hold disjoint tiny arithmetic fixtures, checked against an independent ordered-tuple oracle. They audit the trusted evaluator, do not provide target answers, and do not change the score. They are not presented as a generalization test. Final evaluation reruns the entire certificate with the separate audit suite.

    hills eval <submission> -H clique-cluster-ramsey-multiplicity
    hills eval <submission> -H clique-cluster-ramsey-multiplicity --final

## A realistic week of work

This is an ambitious research sprint, not a guaranteed seven-day solution. The design supports independent work on cluster weights and refinements, Cayley/symmetry-based templates, local edge changes, and exact certificate/formalization checks. The published search work and seed make reproduction feasible without rediscovering the whole field. Breaking B* is the stretch goal; a useful week can also yield a reviewed structural lemma or reusable formalization, but those contributions do not automatically receive this construction hill's success flag.

A suggested plan is to reproduce the published seed first; implement incremental counts and test new cluster constructions next; then independently certify the strongest result and document the exact new-work delta. Copying or rechecking a published construction earns no new open-problem credit. Known work may be eligible for the competition's separate formalization category if its formalization is genuinely new and approved.

## Fixed rules and trust boundary

- At most 1024 blocks, weights 1..65535, and a solution.json of at most 4 MiB. These are evaluator resource limits, not hypotheses of the parent problem.
- Verification has a 480-second internal limit and 600-second watchdog. Resource failure is not a mathematical rejection of the construction.
- The evaluator reads solution.json only and never executes submission code. Other files may contain search code, proof notes, provenance, or formal artifacts; they do not alter the numeric score.
- Duplicate keys, unknown JSON fields, nonintegral weights, asymmetric matrices, and malformed bit strings are rejected.
- The reference, certificate language, resource limits, and scoring formula are fixed for this version. Existing climbs remain on their original version after any later update.
- The Python checker and mathematical lifting argument are the computational trust boundary. Passing is not a claim of Lean/Coq verification or competition admission. Under the OpenMath handbook, score-bearing claims additionally require the approved pinned checker/certificate protocol and mathematical review. See LIFTING.md and SOURCES.md.
