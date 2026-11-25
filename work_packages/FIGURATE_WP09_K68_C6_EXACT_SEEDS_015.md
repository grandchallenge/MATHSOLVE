# FIGURATE WP09-015 — exact order-68 offset-six realizations

**Status:** bounded GCL mathematical research, not independent MATHCERT certification, priority claim, or universal local-to-global theorem. Parent: [FIGURATE WP09 #3145](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3145).

## Exact global result

With $P_{68}(n)=33n^2-32n$, there exist five distinct positive Type B triples at order $68$ and offset $6$, verified by integer equalities:

| Entries $(a,b,d)$ | Positive indices $(r,s,t)$ |
| --- | --- |
| $(10,44033,128739)$ | $(116,198,13107)$ |
| $(22,13117,168855)$ | $(94,336,8193)$ |
| $(55,4085,265746)$ | $(83,666,5736)$ |
| $(61,55575,102610)$ | $(321,436,13146)$ |
| $(102145,629950,746915)$ | $(44158,48083,119408)$ |

In each row the following are **exact equalities**:

$$
ab+6=P_{68}(r),\qquad ad+6=P_{68}(s),\qquad bd+6=P_{68}(t).
$$

For the first row the three outputs are respectively $440336$, $1287396$, and $5668764393$. Thus actual positive integer existence is established for $(k,c)=(68,6)$, beyond mere finite-modulus compatibility.

## Infinitely many exact solutions

The already protected WP09-013 general fixed-first-pair Pell theorem applies to **each** row: in every case $ab$ is a positive nonsquare integer. In the first row, $Q=ab=440330$, $R=132$, $L=64$, and $\Delta=8(66)6+64^2=7264$. Set

$$
S=Rs-L=26072,\qquad X=a(Rt-L)=17300600.
$$

Then direct arithmetic yields

$$
X^2-440330S^2=10(10-44033)7264=-3197830720.
$$

The general protected theorem produces infinitely many exact positive Type B solutions retaining $(a,b)=(10,44033)$. This is a corollary of an earlier admitted theorem, not a separately certified new Pell result.

The complete all-place local sieve also accepts these parameters: $68\equiv4\pmod{16}$, $\Delta=7264=2^5\cdot227$, and $A=(68-2)/2=33$ is a square modulo $227$. The explicit exact triple, not the local test, resolves global existence.

## Complete bounded exclusion

For every unordered triple $1\le a<b<d\le100000$, exhaustive factor-graph enumeration finds **no** exact Type B triples at $(68,6)$. The enumerator factors every positive value $P_{68}(n)-6\le B^2$ into all admissible entry pairs. A triangle in the graph is equivalent to a triple. The independent small-bound direct triple oracle reproduces the result at $B=12,24,48,96$.

This is **only a bounded exclusion**. The five explicit positive solutions have entries exceeding the bound, so no global nonexistence or global uniqueness is claimed. The exploratory five seeds are not asserted to exhaust all triples up to one million.

## Reproducible source

- [Integer-exact research code](https://github.com/grandchallenge/MATHSOLVE/blob/main/research/figurate_wp09_k68_c6_exact_seeds.py)
- [Independent tests](https://github.com/grandchallenge/MATHSOLVE/blob/main/tests/test_figurate_wp09_k68_c6_exact_seeds.py)

Run `python3 -m unittest -v tests.test_figurate_wp09_k68_c6_exact_seeds`. The next unresolved locally compatible candidate pairs include $(84,2)$ and $(100,2)$. External originality review, independent certification and public editorial integration are separate obligations.
