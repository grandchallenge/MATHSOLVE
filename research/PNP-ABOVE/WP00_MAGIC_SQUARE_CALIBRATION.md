# PNP-ABOVE-WP00 — finite calibration: magic-square resource gap does not imply decision hardness

**Status:** bounded mathematical preflight; not a P-vs-NP lower bound or certification.  
**Related issue:** [MATHSOLVE #1136](https://github.com/grandchallenge/MATHSOLVE/issues/1136).  
**Scope:** one finite counterexample to the naive transfer from quantum/classical strategy separation to classical decision-time lower bounds. This is a calibration model, **not** yet a finite family from MIP*=RE recursive compression.

## Precise finite game

The referee picks a row r and column c independently and uniformly from {1,2,3}. Alice must return three bits for row r with even XOR. Bob returns three bits for column c whose XOR is even if c=1 or 2, odd if c=3. They win exactly when Alice's bit in position c agrees with Bob's bit in position r. Communication after receipt of questions is forbidden. The classical strategy permits shared randomness (which does not improve the maximum success over deterministic strategies).

## Classical bound: exactly 8/9

Any deterministic perfect strategy would assign an intersection bit a[r,c] from Alice's response and the same bit from Bob's response, since winning at all nine pairs enforces agreement. The XOR of all row parities is zero, whereas the XOR of all column parities is one, contradiction.

More quantitatively, any deterministic strategy must lose at least one of nine equally likely question pairs, so its success probability is at most 8/9. This bound is attained: choose a 3x3 bit table satisfying all Alice row parities and the first two column parities, but not the third; Alice outputs its rows, while Bob outputs its first two columns and corrects a single bit in the third column to make that column odd. They disagree at precisely one input pair. Shared randomness produces convex combinations and cannot improve the bound.

Thus classical game value = 8/9, not merely <=8/9.

## Quantum value: exactly 1

Let X,Y,Z be Pauli matrices and I the 2x2 identity. Use this commuting-along-each-question square of two-qubit observables:

| | c=1 | c=2 | c=3 |
|---|---|---|---|
| r=1 | X tensor I | I tensor X | X tensor X |
| r=2 | I tensor Z | Z tensor I | Z tensor Z |
| r=3 | X tensor Z | Z tensor X | Y tensor Y |

Each row's observables commute and multiply to +I; each column's observables commute, and their products are +I, +I and -I respectively. On a maximally entangled pair of four-dimensional systems, Alice measures the three observables in the selected row and Bob their transposes in the selected column. The maximally entangled-state identity makes outcomes at the intersection agree with probability 1. The product identities enforce the row/column XOR conditions. Therefore entangled game value = 1.

This is an established finite quantum-vs-classical separation, not a novel theorem.

## Distinct classical decision problem

The global 3x3 parity system (three even row sums; two even and one odd column sum) is inconsistent: XORing all six equations gives 0=1. Gaussian elimination over F_2 detects this in polynomial time. More generally, feasibility of m linear parity constraints on N bits is decidable in polynomial time, e.g. by O(min(m,N)^2 max(m,N)) elementary elimination operations with a standard dense representation.

**Finite negative interface:** the game admits a perfect quantum strategy and lacks a perfect classical strategy, but its natural global classical satisfiability question is trivially polynomial-time decidable. Thus the claim 'nonclassical perfect strategy => hard classical decision problem' is false. This does *not* refute a transfer theorem with independently specified compression-derived game families, cost measures, and uniform reductions from SAT.

## Independent mechanical finite check

Exhaustive enumeration of all 2^9 bit tables gives counts by number of satisfied (3 row + 3 column) parity constraints: {1:96, 3:320, 5:96}; no table satisfies all six. Reproduction:

```python
from itertools import product
hist = {}
for a in product((0,1), repeat=9):
    row = [sum(a[3*r:3*r+3]) % 2 == 0 for r in range(3)]
    col = [sum(a[c+3*r] for r in range(3)) % 2 == (c == 2) for c in range(3)]
    k = sum(row + col)
    hist[k] = hist.get(k, 0) + 1
assert hist == {1:96, 3:320, 5:96}
```

Enumeration verifies inconsistency of global assignments, not the full class of game strategies; the 8/9 theorem above handles question-dependent row/column responses.

## Next genuine MIP*-compression obligation

1. Pin and inspect the exact compression lemma in [MIP*=RE arXiv:2001.04383v4](https://arxiv.org/abs/2001.04383v4) (arXiv v4 is dated 16 October 2026), including all parameter transformations and promise-gap guarantees.
2. Specify *one* explicit finite family from that construction, with size, uniformity, input encoding, entangled/classical values, and all quantitative losses.
3. Define a single classical resource measure C_A(G_n) and identify whether a polynomial-time SAT solver actually constructs a corresponding low-cost strategy. Never infer this from a quantum/classical game-value gap.
4. Cross-check against PNP-WP00 machine/encoding conventions and preserve the existing Formal Conjectures definition-level concordance blocker.
5. Return either a proved restricted bound, a finite counterexample, or an exact missing transfer lemma.

**Conclusion:** source-independent finite calibration completed. MIP*-specific source extraction and classical transfer remain OPEN. No mathematical promotion or PNP claim change.
