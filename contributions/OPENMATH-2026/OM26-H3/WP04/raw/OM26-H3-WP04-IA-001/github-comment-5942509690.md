GCL-CONTRIBUTION-RESULT/1
dispatch_id: OM26-H3-WP04-IA-001
agent_ref: INDEPENDENT-AGENT-304
assignment: OM26-H3-WP04
disposition: PROVED_REDUCTION
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: YES

## Strongest exact statement
For every valid weighted-two-color-blowup-v1 certificate with m blocks, positive integer weights w_1,...,w_m, Q=sum_i w_i, and exact density P as defined in the pinned source, one has
P >= sum_i (w_i/Q)^4 >= 1/m^3.
Consequently every certificate with m <= 3 satisfies P >= 1/27. This lower bound is sharp over the full m<=3 class: for m=3, weights [1,1,1] and red_rows ["100","010","001"] give P=1/27 exactly. The frozen reference is
B* = 10486266368/768^4 = 20480989/679477248,
and
1/27 - B* = 4684835/679477248 > 0.
Therefore no certificate with at most three blocks can beat the canonical reference; any reference-beating certificate must use at least four blocks.

Mathematical event window: 2026-10-01T23:12:46Z through 2026-10-01T23:13:19Z. Result envelope created 2026-10-01T23:14:06Z. The intended return issue was created 2026-10-01T22:17:03Z.

## Derivation
Write A_ii for the diagonal color bit of block i. In the exact ordered-tuple formula from the protected README, the tuple (i,i,i,i) contributes w_i^4/Q^4 to P for every i, regardless of A_ii: if A_ii=1 the red product is 1 and the blue product is 0, while if A_ii=0 the blue product is 1 and the red product is 0. Every other ordered-tuple contribution is nonnegative. Hence
P >= (sum_i w_i^4)/Q^4.

By convexity of x^4, equivalently the power-mean inequality,
(1/m) sum_i w_i^4 >= ((1/m) sum_i w_i)^4 = (Q/m)^4.
Thus sum_i w_i^4 >= Q^4/m^3 and therefore P >= 1/m^3. For m<=3 this gives P>=1/27.

Sharpness for the declared family is witnessed by the valid three-block certificate
{"schema":"weighted-two-color-blowup-v1","weights":[1,1,1],"red_rows":["100","010","001"]}.
Here each block is a red clique and every inter-block edge is blue. Any ordered four-tuple using both a repeated block label and a distinct label contains a red diagonal pair and a blue cross pair, so it is not monochromatic. With only three block labels, four distinct labels are impossible. Therefore the only monochromatic ordered template tuples are (0,0,0,0), (1,1,1,1), and (2,2,2,2), all red. The exact red numerator is 3, the blue numerator is 0, the denominator is 3^4=81, and P=3/81=1/27.

Exact comparison:
B* = 20480989/679477248,
1/27 = 25165824/679477248,
so the gap is 4684835/679477248 > 0.

Relative to the protected packet, this is an explicit small-block exclusion not stated in README.md, eval.py, or LIFTING.md. It does not improve B* and no broader literature novelty claim is made; no external literature search was used.

## Assumptions beyond bootstrap
No mathematical assumptions beyond the pinned certificate definition, nonnegativity of its exact ordered-tuple summands, and the standard convexity/power-mean inequality are used. The proof actually permits positive real weights before normalization, so it applies a fortiori to the positive integer certificate domain.

Pinned source head: 36b7c79bebd42fde17ea9f0f809406fb55e093f9. Launch artifact ref: 4f1b6a1500e18fc53bae135ae6713e7abb126ae4. Source SHA-256 values were recomputed from authenticated fetches and matched exactly:
README.md 201d781e16ab9ef651f796c238518306c3fefcd16c3de11c213bdbec8c8a7142
eval.py 39932af840c4cd822b43be9383fb850b692635787a05562a01ae23363776697f
LIFTING.md 2e05aa6b42941954072f67a26cc9a629d7c041602d6381d6b801100280b111e7

Authorship: OpenAI GPT-5.6 Sol, acting in this zero-context session as INDEPENDENT-AGENT-304. GitHub transport is authenticated as fyremael; that account is transport provenance, not a claim of mathematical coauthorship. Verification below is same-session verification only; no independent reviewer, independent replay, proof-assistant check, or certification is claimed.

## Verification / falsification hooks
Authenticated transport was checked before substantive work without posting a test result: login fyremael; grandchallenge/MATHSOLVE permission admin; issue 602 open; pre-return comment count 0.

Deterministic exact replay: save the following as h3_wp04_verify.py and run
python h3_wp04_verify.py
python -m py_compile h3_wp04_verify.py

```python
from fractions import Fraction
from itertools import product

REFERENCE = Fraction(10486266368, 768**4)
weights = [1,1,1]
rows = ["100", "010", "001"]

red = blue = 0
for a,b,c,d in product(range(3), repeat=4):
    colors = (rows[a][b], rows[a][c], rows[a][d],
              rows[b][c], rows[b][d], rows[c][d])
    mass = weights[a]*weights[b]*weights[c]*weights[d]
    if all(x == "1" for x in colors):
        red += mass
    elif all(x == "0" for x in colors):
        blue += mass

Q = sum(weights)
P = Fraction(red+blue, Q**4)
GAP = P - REFERENCE

assert P == Fraction(1,27)
assert GAP == Fraction(4684835, 679477248)
assert GAP > 0
assert red == 3 and blue == 0 and Q**4 == 81

print(f"reference={REFERENCE.numerator}/{REFERENCE.denominator}")
print(f"three_block_tight_certificate_red={red}")
print(f"three_block_tight_certificate_blue={blue}")
print(f"three_block_tight_certificate_denominator={Q**4}")
print(f"three_block_tight_certificate_density={P.numerator}/{P.denominator}")
print(f"density_minus_reference={GAP.numerator}/{GAP.denominator}")
print("reference_beaten=False")
print("analytic_lower_bound: for m<=3, P >= sum_i (w_i/Q)^4 >= 1/m^3 >= 1/27")
```

Observed output:
```
reference=20480989/679477248
three_block_tight_certificate_red=3
three_block_tight_certificate_blue=0
three_block_tight_certificate_denominator=81
three_block_tight_certificate_density=1/27
density_minus_reference=4684835/679477248
reference_beaten=False
analytic_lower_bound: for m<=3, P >= sum_i (w_i/Q)^4 >= 1/m^3 >= 1/27
```
The subsequent py_compile command exited successfully with no output.

Authenticated source-hash recomputation output:
README.md MATCH 201d781e16ab9ef651f796c238518306c3fefcd16c3de11c213bdbec8c8a7142
eval.py MATCH 39932af840c4cd822b43be9383fb850b692635787a05562a01ae23363776697f
LIFTING.md MATCH 2e05aa6b42941954072f67a26cc9a629d7c041602d6381d6b801100280b111e7

Falsification is immediate: any valid m<=3 certificate with exact P<1/27, or any flaw in the forced (i,i,i,i) contribution or convexity step, would refute the reduction.

## Claim boundary
This establishes only a structural exclusion inside the pinned weighted blow-up certificate language: one-, two-, and three-block certificates cannot improve the frozen McKay reference, and their exact minimum is 1/27. It does not improve the canonical upper bound, does not characterize m>=4 templates, does not prove any lower bound on c4 itself, and does not resolve the parent Ramsey multiplicity problem. No competition submission, official score, novelty determination, independent review, or certification is claimed.

## Next residual
Search or analyze m>=4; the general diagonal-mass inequality P>=sum_i(w_i/Q)^4 remains available to prune weight-concentrated regions. Promotion of this reduction requires independent replay and novelty review.