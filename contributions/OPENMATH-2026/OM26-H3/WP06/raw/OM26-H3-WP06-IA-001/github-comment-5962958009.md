GCL-CONTRIBUTION-RESULT/1
dispatch_id: OM26-H3-WP06-IA-001
agent_ref: INDEPENDENT-AGENT-306
assignment: OM26-H3-WP06
disposition: REPLAY_CLOSURE_VALIDATED
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: YES

## Strongest exact statement

Deterministic independent replay validates the predecessor reduction and small-block exclusion theorem without modification. For every valid weighted-two-color-blowup-v1 certificate with m blocks, positive integer weights w_1,...,w_m, total weight Q=sum_i w_i, and exact density P as defined in the pinned evaluator, one has
P >= sum_i (w_i/Q)^4 >= 1/m^3.
Consequently, every certificate with m <= 3 satisfies P >= 1/27. This lower bound is sharp over the full m<=3 class: for m=3, weights [1,1,1] and red_rows ["100","010","001"] (as well as its color complement ["011","101","110"]) yield P=1/27 exactly. The frozen McKay canonical reference is
B* = 10486266368/768^4 = 20480989/679477248,
and
1/27 - B* = 4684835/679477248 > 0.
Therefore, no certificate with at most three blocks can beat the canonical reference; any reference-beating certificate must use at least four blocks.

## Derivation

Let A in {0,1}^(m x m) be the symmetric adjacency matrix of the certificate, where diagonal entry A_ii is 1 if block i is a red clique and 0 if block i is a blue clique. In the exact ordered-tuple expansion from eval.py and README.md, the density is
P(A,w) = (1/Q^4) sum_(a,b,c,d in {0,...,m-1}) w_a w_b w_c w_d * [prod_(e) A_e + prod_(e) (1 - A_e)],
where the product runs over all six pairs formed by the four indices.
For every pure diagonal tuple (i,i,i,i), all six pairs are (i,i). If A_ii=1, the red product is 1^6=1 and the blue product is (1-1)^6=0. If A_ii=0, the red product is 0^6=0 and the blue product is (1-0)^6=1. Thus for every block i, regardless of whether A_ii is 1 or 0, the monochromatic indicator for (i,i,i,i) is identically 1.
Because edge variables and weights are nonnegative, every other ordered tuple contributes a nonnegative quantity to the numerator. Hence
P >= (sum_(i=1)^m w_i^4) / Q^4 = sum_(i=1)^m (w_i/Q)^4.

By the convexity of the function f(x)=x^4 on the non-negative reals, Jensen's inequality (or the power-mean inequality) gives
(1/m) sum_(i=1)^m (w_i/Q)^4 >= ((1/m) sum_(i=1)^m (w_i/Q))^4 = (1/m)^4 = 1/m^4.
Multiplying by m gives
sum_(i=1)^m (w_i/Q)^4 >= 1/m^3.
For m <= 3, the minimum of 1/m^3 is achieved at m=3, yielding P >= 1/27 for all m in {1,2,3}.

Sharpness for m=3 is witnessed by the certificate {"schema":"weighted-two-color-blowup-v1","weights":[1,1,1],"red_rows":["100","010","001"]}. Here, diagonal entries are red and all inter-block edges are blue. In any ordered 4-tuple with at least two distinct block labels, the tuple contains a diagonal pair (red) and an inter-block pair (blue), so it cannot be monochromatic. With only 3 available block labels, four distinct labels are impossible. Hence only the three diagonal tuples (0,0,0,0), (1,1,1,1), and (2,2,2,2) are monochromatic (all red). The exact red numerator is 3, blue numerator is 0, denominator is 3^4=81, and P = 3/81 = 1/27.

Exact comparison with the frozen reference:
B* = 10486266368/768^4 = 20480989/679477248,
1/27 = 25165824/679477248,
giving the positive gap 1/27 - B* = 4684835/679477248 > 0.
Exhaustive symbolic expansion across all 74 symmetric matrices for m in {1,2,3} confirms that the pure diagonal sum sum_i w_i^4 is the exact lower envelope of the numerator, with cross-terms vanishing identically on only two complementary matrices for m=2 and two complementary matrices for m=3.

## Assumptions beyond bootstrap

No mathematical assumptions beyond the pinned certificate definition, nonnegativity of its exact ordered-tuple summands, and standard convexity of x^4 are used. The proof holds for arbitrary positive real weights before normalization, so it applies a fortiori to integer certificate weights.

Pinned source head: 36b7c79bebd42fde17ea9f0f809406fb55e093f9.
Source SHA-256 hashes matched authenticated repository state exactly:
README.md 201d781e16ab9ef651f796c238518306c3fefcd16c3de11c213bdbec8c8a7142
eval.py 39932af840c4cd822b43be9383fb850b692635787a05562a01ae23363776697f
LIFTING.md 2e05aa6b42941954072f67a26cc9a629d7c041602d6381d6b801100280b111e7

Authorship: Independent replay worker acting in zero-context lease OM26-H3-WP06-IA-001 as INDEPENDENT-AGENT-306. GitHub transport authenticated as fyremael.

## Verification / falsification hooks

Pre-work transport check confirmed authenticated issue-comment capability on issue 645 under fyremael.

Deterministic exact replay script:
```python
from fractions import Fraction
from itertools import product
from collections import defaultdict

REFERENCE = Fraction(10486266368, 768**4)
assert REFERENCE == Fraction(20480989, 679477248)

weights = [1, 1, 1]
rows_red = ["100", "010", "001"]
rows_blue = ["011", "101", "110"]

def count_density(w, rows):
    m = len(w)
    red = blue = 0
    for a, b, c, d in product(range(m), repeat=4):
        colors = (rows[a][b], rows[a][c], rows[a][d],
                  rows[b][c], rows[b][d], rows[c][d])
        mass = w[a] * w[b] * w[c] * w[d]
        if all(x == "1" for x in colors):
            red += mass
        elif all(x == "0" for x in colors):
            blue += mass
    Q = sum(w)
    P = Fraction(red + blue, Q**4)
    return red, blue, Q**4, P

r_red, b_red, denom_red, P_red = count_density(weights, rows_red)
assert r_red == 3 and b_red == 0 and denom_red == 81
assert P_red == Fraction(1, 27)

r_blue, b_blue, denom_blue, P_blue = count_density(weights, rows_blue)
assert r_blue == 0 and b_blue == 3 and denom_blue == 81
assert P_blue == Fraction(1, 27)

GAP = P_red - REFERENCE
assert GAP == Fraction(4684835, 679477248)
assert GAP > 0

for m in (1, 2, 3):
    total_matrices = 0
    zero_cross_count = 0
    diag_combos = list(product((0, 1), repeat=m))
    offdiag_pairs = [(i, j) for i in range(m) for j in range(i + 1, m)]
    offdiag_combos = list(product((0, 1), repeat=len(offdiag_pairs)))
    for diag in diag_combos:
        for off in offdiag_combos:
            total_matrices += 1
            mat = [[0]*m for _ in range(m)]
            for i in range(m):
                mat[i][i] = diag[i]
            for (i, j), val in zip(offdiag_pairs, off):
                mat[i][j] = mat[j][i] = val
            coeffs = defaultdict(int)
            for a, b, c, d in product(range(m), repeat=4):
                colors = (mat[a][b], mat[a][c], mat[a][d],
                          mat[b][c], mat[b][d], mat[c][d])
                if all(x == 1 for x in colors) or all(x == 0 for x in colors):
                    coeffs[tuple(sorted((a, b, c, d)))] += 1
            for i in range(m):
                assert coeffs[(i, i, i, i)] == 1
            cross_terms = {k: v for k, v in coeffs.items() if len(set(k)) > 1}
            assert all(v >= 0 for v in cross_terms.values())
            if not cross_terms:
                zero_cross_count += 1
    if m == 1:
        assert total_matrices == 2 and zero_cross_count == 2
    elif m == 2:
        assert total_matrices == 8 and zero_cross_count == 2
    elif m == 3:
        assert total_matrices == 64 and zero_cross_count == 2

print("EXHAUSTIVE_REPLAY_SUCCESS")
print(f"reference={REFERENCE.numerator}/{REFERENCE.denominator}")
print(f"three_block_tight_certificate_red={r_red}")
print(f"three_block_tight_certificate_blue={b_red}")
print(f"three_block_tight_certificate_denominator={denom_red}")
print(f"three_block_tight_certificate_density={P_red.numerator}/{P_red.denominator}")
print(f"density_minus_reference={GAP.numerator}/{GAP.denominator}")
print("reference_beaten=False")
```

Execution of python h3_wp06_verify.py outputs:
```
EXHAUSTIVE_REPLAY_SUCCESS
reference=20480989/679477248
three_block_tight_certificate_red=3
three_block_tight_certificate_blue=0
three_block_tight_certificate_denominator=81
three_block_tight_certificate_density=1/27
density_minus_reference=4684835/679477248
reference_beaten=False
```
Execution of python -m py_compile h3_wp06_verify.py exits with code 0.

Falsification hook: Any valid certificate with m <= 3 blocks having exact density P < 1/27, or any mathematical flaw in the forced diagonal mass contribution or the convexity inequality, refutes this result.

## Claim boundary

This replay validates only the structural exclusion inside the pinned weighted-two-color-blowup-v1 certificate schema: certificates with 1, 2, or 3 blocks cannot beat the canonical McKay reference, and their global infimum is 1/27. It does not construct a beating certificate for m >= 4, does not establish a universal lower bound on c4 itself, and does not resolve the parent Ramsey multiplicity problem. No canonical repository mutation, official score, novelty determination, or certification is claimed.

## Next residual

Any candidate certificate beating the reference must employ at least four blocks. Future searches should analyze m >= 4 templates and exploit the general diagonal-mass inequality P >= sum_i (w_i/Q)^4 to prune weight-concentrated configurations. Novelty assessment and formal review are required for higher-order constructions.