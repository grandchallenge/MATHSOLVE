# FIGURATE WP09-008 — Pell amplification versus split finiteness

**Programme:** FIGURATE WP09, [MATH-PROGRAMME #3145](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3145).

**Claim status:** internally proved, subject to exact-head test/CI, protected source admission, and separate literature and independent specialist certification. Standard Pell theory and factorization are classical; no priority is asserted. This tranche answers a structural exact-integer question, not a local-congruence question.

## Definitions

For integer k>=3 and positive integer index n, let

    P_k(n)=((k-2)n²-(k-4)n)/2.

An exact Type B triple at integer offset c consists of three distinct positive integers (a,b,d), with positive polygonal indices (r,s,t), such that

    ab+c=P_k(r), ad+c=P_k(s), bd+c=P_k(t).

This dossier classifies extensions of **the fixed pair (1,b)** where b=P_k(r)-c>1.

Set

    R=2(k-2), L=k-4, D=8(k-2)c+L²,
    S=R s-L, T=R t-L.

Both S and T are positive for all s,t>=1. Square completion gives

    8(k-2)P_k(n)+L²=(R n-L)².

If d=P_k(s)-c, the remaining exact equation b*d+c=P_k(t) is equivalent to

    T²-b S²=-(b-1)D,          (1)

with

    S≡T≡-L (mod R), S,T>0,

and d=P_k(s)-c positive and distinct from 1 and b. Conversely, any integral S,T satisfying (1) and these congruences, positivity and distinctness reconstructs an exact Type B triple. There is no local-to-global inference here: (1) is an identity equivalent to the **exact integer equations**.

## Theorem A: one nonsquare seed implies infinitely many exact triples

Suppose (1,b,d) is an exact Type B triple for some fixed (k,c), with b>1 a nonsquare and d>1 distinct from b. Then infinitely many exact Type B triples exist with the **same k, c and fixed pair (1,b)**.

**Proof.** Because b is positive and nonsquare, classical Pell theory supplies an integral unit u+v√b>1, with u,v positive integers and

    u²-bv²=1.

Multiplying T+S√b by this unit acts through the integer matrix

    [u  bv]
    [v   u].

The matrix has determinant 1, so it preserves the norm (1), and it is invertible modulo R. The finite multiplicative group of units in (Z/RZ)[√b] has at most R² elements. Consequently some positive power e (indeed e<=R²) of the unit is 1 modulo R. The associated e-th matrix power fixes both congruences S≡T≡-L mod R.

Apply this e-th unit to the positive seed (S,T), then repeat any number m of times. Each new (S_m,T_m) is integral, positive, preserves both the norm and required index residue conditions, and yields positive integers s_m,t_m via

    s_m=(S_m+L)/R, t_m=(T_m+L)/R.

Because u,v,S,T are positive, both S_m and T_m strictly increase with m. Hence d_m=P_k(s_m)-c eventually grows without bound, and after omitting finitely many possible collisions with 1 or b, each (1,b,d_m) is a distinct positive exact Type B triple. Every pair equation follows from the exact equivalence above. QED.

**Algorithm:** research/figurate_wp09_general_pell_amplification.py computes a fundamental Pell unit by continued fractions, finds its exact finite order modulo R, raises that congruence-preserving unit by fast squaring, and independently verifies every returned exact integer equation and norm. A valid exact seed is required; this algorithm cannot manufacture a global solution from merely local congruence compatibility.

## Theorem B: square b and nonzero D give only finitely many extensions

Suppose b=h²>1 is a square and D≠0. Then there are only **finitely many** possible positive integer d such that (1,b,d) forms an exact Type B triple for fixed k,c and first pair.

**Proof.** Equation (1) becomes

    (T-hS)(T+hS)=-(b-1)D=N≠0.

Each factor is a nonzero integer divisor of the fixed nonzero integer N. There are finitely many signed factor pairs (X,Y) with XY=N, and each determines at most one pair

    T=(X+Y)/2,  S=(Y-X)/(2h).

The index congruences and positivity conditions only restrict that finite set. Thus only finitely many exact extensions exist. QED.

The source includes a complete signed-divisor enumeration of these candidate solutions, with exact final verification. The case D=0 is expressly **excluded** from the finite theorem: the product vanishes and may have infinitely many solutions on the split lines T=±hS.

**Interpretation:** the square/nonsquare distinction predicts whether one valid fixed-pair exact seed can be amplified by Pell symmetry into infinitely many extensions (nonsquare), or whether its fixed-pair extensions are arithmetically finite (square, D nonzero). This does NOT classify the existence of an initial seed for every k,c.

## Three concrete nonsquare families beyond mere local compatibility

| order k | offset c | fixed b | seed d | indices (r,s,t) | Pell norm |
| --- | ---: | ---: | ---: | --- | ---: |
| 5 | 2 | 3 | 3430 | (2,48,83) | -98 |
| 6 | 2 | 13 | 43 | (3,5,17) | -816 |
| 20 | 2 | 18 | 13375 | (2,39,164) | -578 |

For k=5,c=2, the fundamental norm-one unit is 2+√3 and its modular order for R=6 is 6. The first amplified tuple has entries (1,3,25051687815) and indices (2,129233,223838). All three outputs are exact pentagonal numbers, not only congruent modulo finite powers.

For k=6,c=2, the unit is 649+180√13, R=8, modular order 2; the first amplified tuple has entries (1,13,125290484616373) and indices (3,7914875,28537487). All outputs are exact hexagonal numbers.

For k=20,c=2, the unit 17+4√18 has modular order 18 for R=36, recovering the earlier WP09-007 family as a special case.

**Square contrast:** at k=4,c=5,r=3 the fixed second entry b=4 is square and D=80, giving N=-240. An exact seed is (1,4,11) at indices (3,4,7). The divisor enumeration finds that this is the only exact extension for this fixed k,c,r and b with distinct positive entries. The infinite Euler construction for order 4 changes the second entry as well; it does not contradict fixed-b finiteness.

## Boundaries and next mathematical obligation

- **Exact integer theorem:** Theorem A extends a genuine seed to infinitely many genuine global solutions. Theorem B gives a true finite-extensions result for fixed square b and D≠0.
- **No blanket local-to-global principle:** The existence of an everywhere-local Type B congruence family is not shown to imply existence of an initial exact integer seed.
- **No effective universal seed-existence algorithm:** An exhaustive search can find an integer seed if one exists but does not prove absence merely by exhaustion to a finite bound.
- **Next priority:** use the Pell norm and index residue constraints to characterize which fixed (k,c,r) admit any seed. Study generalized Pell solvability, possible descent obstructions, and the arithmetic difference between all-prime local compatibility and integral positive-index solutions.
- **Novelty:** Pell units, continued fractions and factorization are classical. This programme's explicit polygonal fixed-pair conditional dichotomy is internally derived; no literature-wide original-discovery claim without source-critical review.
