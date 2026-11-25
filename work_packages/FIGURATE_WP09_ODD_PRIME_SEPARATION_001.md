# FIGURATE WP09 — an infinite odd-prime separation from all binary local tests

**Programme:** [FIGURATE-PILOT-001](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3093) · [WP09](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3145). **Research tranche 001, 5 November 2026.**

**Claim:** an explicit infinite family of offsets for which one fixed triple of distinct positive integer entries passes **every** binary-power Type B local test but fails an odd-prime local test. This proves a local-to-global **counterexample for that fixed triple**, *not* global nonexistence of Type B triples for the order/offset parameters. All formulas use exact integer arithmetic; no literary novelty or independent certification is asserted.

## The theorem

Let the polygonal order be $k=20$, so

$$
P_{20}(t)=9t^2-8t
$$

for positive integer $t$. Fix three **distinct positive entries** $a=1$, $b=242$ and $d=375$. Let

$$
c_m=2+640m,\qquad m\in\mathbb Z.
$$

**Theorem.** For **every** integer $m$:

1. The three shifted pair products $ab+c_m$, $ad+c_m$, $bd+c_m$ are **locally 20-gonal modulo $2^n$ for every positive integer exponent $n$**, with the same three entries $1,242,375$, independent of both $m$ and $n$.
2. The first shifted pair product $ab+c_m\equiv4\pmod5$ is **never** locally 20-gonal modulo 5.
3. Consequently the fixed triple $\{1,242,375\}$ is **never** an exact integer Type B triple with order 20 and offset $c_m$, despite passing **every** binary congruence condition.

Crucially, assertion 3 is **only about the specified triple**. It does not say another triple fails, or that all Type B triples with order 20 and those offsets are absent.

### Proof: all binary powers simultaneously

The classical completed-square normal form for order 20 is

$$
9P_{20}(t)+16=(9t-4)^2.
$$

As 9 is odd, it is invertible modulo every $2^n$. Thus an integer $z$ is congruent to some 20-gonal number modulo $2^n$ if and only if

$$
9z+16\text{ is a square modulo }2^n.
$$

For $m=0$, the three pairwise shifted products are

$$
ab+2=244,\quad ad+2=377,\quad bd+2=90752.
$$

Their transformed values and exact 2-adic factorization are

| Pair | Transformed value $9(xy+2)+16$ | 2-adic valuation | Odd unit modulo 8 |
| --- | --- | --- | --- |
| $ab$ | $2212=4\cdot553$ | 2 | 1 |
| $ad$ | $3409$ | 0 | 1 |
| $bd$ | $816784=16\cdot51049$ | 4 | 1 |

An integer $D\ne0$ is a square in the ring of 2-adic integers precisely when $v_2(D)$ is even and its odd unit is $1\pmod8$; this criterion also applies to negative integers using signed division. Each of the three values above is therefore a 2-adic square.

For arbitrary $m$, replacing $c=2$ with $c_m=2+640m$ changes **each** transformed value by

$$
9\cdot640m=5760m=2^7\cdot45m.
$$

Since the original valuations are $2,0,4$, adding a multiple of $2^7$ preserves each valuation and each odd unit modulo 8 (the largest original valuation is 4 and $7=4+3$). Therefore **all three transformed values remain squares in $\mathbb Z_2$ for every integer $m$**, including arbitrarily large positive and negative offsets. By the exact modular normal-form equivalence, all three pair outputs are 20-gonal residues modulo every $2^n$. The triple never changes.

### Proof: one odd prime defeats the same triple

Direct reduction gives

$$
P_{20}(t)=9t^2-8t\equiv4t^2+2t\pmod5.
$$

Evaluating $t=0,1,2,3,4\pmod5$ yields the complete residue image

$$
R_{20,5}=\{0,1,2\}.
$$

However,

$$
ab+c_m=242+(2+640m)=244+640m\equiv4\pmod5.
$$

Since 4 is absent from $R_{20,5}$, the first pair cannot equal $P_{20}(t)$ for **any positive integer index $t$**. Hence the specific three-entry set never forms an exact Type B triple.

This explicit infinite offset family establishes the required separation. It is a counterexample to the inference *“one fixed integer tuple passes all $2$-power local tests, therefore that tuple is an exact integer Type B solution.”* It is **not** a counterexample to an arbitrary-number-theoretic local-to-global principle involving all places, and it is **not** a global obstruction for the entire parameter pair $(k,c_m)$.

## Executable and independently verified evidence

- [Exact certificate program](../research/figurate_wp09_odd_prime_separation.py) calculates shifted products, transformed 2-adic square certificates, the complete polygonal image modulo 5, and the scope-limited failure conclusion.
- [Independent tests](../tests/test_figurate_wp09_odd_prime_separation.py) independently enumerate quadratic residues modulo each $2^n$, reconstruct polygonal residues directly from the quadratic polynomial, verify negative-offset signed valuation handling, test 803 offset parameters including $\pm10^{30}$, and exercise the exact positive-index polygonal membership oracle.
- The predecessor [WP08 normal form](FIGURATE_WP08_2ADIC_SQUARE_NORMAL_FORM_007.md) is used as a proven congruence equivalence, not as a claim of global integer solvability.
- CI ownership of `tests/test_figurate_` remains the repository's established GCL-CIR-001 route; do not weaken enforcement.

```sh
python3 -m research.figurate_wp09_odd_prime_separation --parameter 0
python3 -m research.figurate_wp09_odd_prime_separation --parameter -100000000000000000000
python3 -m unittest discover -s tests -p test_figurate_wp09_odd_prime_separation.py -v
```

## Interpretation and next research obligation

The theorem isolates one concrete missing ingredient between **all-power binary compatibility** and **actual positive-index integer polygonal equations**: odd-prime obstructions already matter, even when a single fixed triple passes every binary test. It is a finite-parameter polynomial computation extended to an infinite arithmetic progression by valuation stability, and is **not asserted original in the mathematical literature**.

Next: move from a counterexample for **one fixed triple** to an *all-triples* simultaneous-local certificate for a parameter family, or develop a constructive family of **exact integer Type B triples** with all three positive polygonal indices and independently audited source novelty. Those are new obligations under WP09 rather than retrospectively reopening WP08. **WP05 is excluded** from this research task.
