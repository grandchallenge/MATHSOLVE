# FIGURATE-WP05–WP07: activated research tranche

**Parent:** [MATH-PROGRAMME #3093](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3093).
**Authority:** Human Steward instruction on 2026-11-03 to implement the agreed FIGURATE roadmap.
**Status:** bounded internal research. The constituent issues are not external-worker dispatches, and GitHub issue creation does not grant mathematical certification.

## Work-package register

- **WP05, source fidelity:** [MATH-PROGRAMME #3096](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3096). Read full primary papers and freeze their exact theorems, notation and admissible domains. Avoid paraphrasing abstracts into stronger results.
- **WP06, reproducible search:** [MATH-PROGRAMME #3097](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3097). Exact integer modular necessary-condition sieve, parity against the 270-row L60 archive, independent spot checks and a larger bounded panel. Record dataset identity and limits.
- **WP07, obstruction dossiers:** [MATH-PROGRAMME #3098](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3098). Identify at least three precise candidate propositions, prove their elementary implications or flag assumptions, test adversarial examples and assess prior art.

## Exact local sieve for polygonal outputs

For integer $k\geq 3$, the polygonal number at index $t$ is

$$
P_k(t)=\frac{(k-2)t^2-(k-4)t}{2}.
$$

For every integer modulus $m\geq2$, its residue image is

$$
R_{k,m}=\{P_k(t)\bmod m:1\leq t\leq2m\}.
$$

**Elementary coverage lemma (not claimed novel).** The identity

$$
P_k(t+2m)-P_k(t)=2m(k-2)t+2m^2(k-2)-m(k-4)
$$

is divisible by $m$. Therefore these first $2m$ positive indices cover the entire image of the polygonal sequence modulo $m$. If a Type B or Type C pair satisfies $ab+c=P_k(t)$, then the residue of $ab+c$ belongs to $R_{k,m}$ for every such modulus. Rejecting a pair when one modulus fails is therefore **sound**, but satisfying all chosen residue tests is **not sufficient** for membership.

For Type A, substitute the image of squares modulo $m$ into the same filtering logic.

## Implementation and acceptance

The [FIGURATE modular sieve](https://github.com/grandchallenge/MATHSOLVE/blob/main/research/figurate_residue_sieve.py) is a count-only exact compatibility-graph search. It reports rejected pair candidates, full exact membership calls, accepted edges, tuple count and first lexicographic witness. Modular precomputation is cached and uses exact integer arithmetic. No use of float approximations or unsupported extension shortcuts is permitted.

Tests must assert residue periodicity, absence of false rejection for all enumerated valid sample edges, parity with all 270 archived parameter rows, and additional larger bounds. The test fixture is referenced by its protected MATHSOLVE path rather than recopying counts.

```sh
python3 -m unittest discover -s tests -p 'test_figurate_residue_sieve.py'
python3 -m research.figurate_residue_sieve --kind B --k 3 --offset 1 --limit 120 --size 3
```

**Claims permitted now:** soundness of the elementary modular necessary condition by direct identity, and reproducible finite results where replayed.

**Claims not permitted now:** new arithmetic obstruction, superior time complexity, quantified speedup, global tuple nonexistence, source-novelty certification, or formally verified theorem.

## Structural-obstruction dossier seeds

1. **Local residue obstruction.** A pair with fixed residues $a\equiv r$, $b\equiv s$ modulo $m$ is impossible for Type B/C whenever $(rs+c)\bmod m$ is absent from $R_{k,m}$. This is a valid *conditional* obstruction and applies across all orders. It is not a new theorem until strengthened beyond the standard residue test.
2. **Extension-compatibility intersection.** For an existing Type B pair $\{a,b\}$, a candidate third entry $d$ must satisfy both $(ad+c)\bmod m\in R_{k,m}$ and $(bd+c)\bmod m\in R_{k,m}$ for each chosen modulus. The intersection of allowed candidate residue classes is a sound prefilter. Empty intersection prohibits an extension for the fixed pair, without asserting all pairs cannot extend.
3. **Congruence clique obstruction.** Construct the finite local compatibility graph on residue classes modulo $m$, including self-class edges when repeated residues are allowed among **distinct integers**. To rule out a size-$q$ tuple, demonstrate that no length-$q$ multiset of allowed residue classes satisfies all pair constraints, accounting for repeated classes and actual bounded vertex counts if finite. A simple ordinary-graph clique number that ignores repeated classes is **not** a valid general obstruction.

For every dossier, record a counterexample-search range and independently reproduce the assertion before any theorem promotion.

## Go/no-go decision and continuity

The first gate after WP05–WP07 requires: exact primary-source claim mapping; verified larger computational panel; and at least one nontrivial viable theorem proposition with a proof sketch and adversarial testing. Should these fail, narrow the project rather than scaling unproductive brute force.

No special queue labels, autonomous scheduled job, source lock or external agent assignment is created by this tranche. Operational closure still requires the affected protected GitHub checks, merge and readback; substantive mathematics still requires separate adjudication.
