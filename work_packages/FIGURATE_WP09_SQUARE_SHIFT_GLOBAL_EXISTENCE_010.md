# FIGURATE WP09-010 — exact global Type B existence for square-shifted polygonal offsets

**Programme:** [FIGURATE WP09 #3145](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3145). This is an exact-positive-integer theorem, not a local congruence test. Its tools (quadratic forms, Pell units, and square-polynomial rigidity) are classical; literature originality and independent MATHCERT certification are not asserted.

## Theorem (uniform in polygonal order and square shift)

Let k>=3, u>=1 and a>=1 be arbitrary integers and set

    P_k(n)=((k-2)n²-(k-4)n)/2,
    c=P_k(u)-a².

Then there are **infinitely many triples (a,b,d) of distinct positive integers** and positive integer indices (r,s,t) satisfying

    ab+c=P_k(r),
    ad+c=P_k(s),
    bd+c=P_k(t).

The first entry a is fixed throughout each family. Except when k=4 and a=u, there are infinitely many choices of the *fixed second entry* b as well, and each such choice admits infinitely many distinct d. In the exceptional case, c=0 and explicit square-output triples give infinitely many solutions.

The previous WP09-009 theorem is the special case a=1. The present result genuinely extends its offset family: for example k=7,u=2,a=2 yields c=3, which is not P_7(v)-1 for any positive index v.

## Step 1: infinitely many nonsquare Pell coefficients

Fix k,u,a and define

    F(r)=P_k(r)-P_k(u)+a².

For integers j>=1 take r=u+2aj. The difference P_k(r)-P_k(u) is divisible by a (the polynomial has integer values and r-u is divisible by 2a). Therefore

    b=F(r)/a

is an integer, and for sufficiently large j we have b>a. Set q=ab=F(r).

**Lemma.** Unless (k,a,u)=(4,u,u), infinitely many such j give q nonsquare.

**Proof.** Suppose instead that q_j=F(u+2aj) were a perfect square for every sufficiently large j. Let y_j=sqrt(q_j) be the nonnegative integer square root. As j tends to infinity,

    y_(j+1)-y_j  ->  2a sqrt((k-2)/2).

An integer-valued sequence with a finite real limit is eventually constant. Consequently its limit m is a positive integer, and y_j=mj+v for all sufficiently large j with integer v. Then two quadratics in j agree at infinitely many integers:

    F(u+2aj)=(mj+v)².

Thus F(r) is the square of a rational affine polynomial in r. Its leading coefficient implies (k-2)/2 is a rational square, which for integral k forces k=2h²+2 with an integer h>=1. Comparing the linear coefficient of P_k(r) gives 2h*w=1-h² for the affine square root hr+w. Since y_j=h(u+2aj)+w is an integer and hu is an integer, w is an integer. Hence h divides 1, so h=1, k=4 and w=0. Finally F(r)=r²-u²+a² must equal r² identically, forcing a=u. Contradiction outside that one exception. QED.

Therefore, unless k=4,a=u, infinitely many r=u+2aj produce integer b>a with q=ab nonsquare.

## Step 2: an exact formal repeated-entry point

For such a nonsquare q=ab, the formal entries (a,b,a) satisfy three exact output identities:

    ab+c=P_k(r),
    a*a+c=P_k(u),
    ba+c=P_k(r).

Because two entries coincide, this formal starting point is **NOT a valid Type B tuple**. Its value is that it gives an integral point on the correct generalized Pell conic.

Put

    R=2(k-2), L=k-4,
    D=8(k-2)c+L²,
    S=R*u-L, T=R*r-L, X=a*T.

The polygonal discriminant identity

    (Rn-L)²=8(k-2)P_k(n)+L²

turns the two remaining exact equations, after eliminating d, into

    X²-q*S² = a(a-b)D.                    (1)

The formal point (X,S) satisfies (1), and both X and S are positive.

## Step 3: Pell promotion with all integer conditions preserved

Because q>1 is nonsquare, choose a positive integer norm-one Pell unit U+V sqrt(q)>1, with U²-qV²=1 and U,V>0. Its multiplication matrix

    [U  qV]
    [V   U]

has determinant 1 and is invertible modulo each positive integer M. Choose

    M=2aR=4a(k-2).

The finite group of invertible pairs modulo M implies that some power e>=1 of the Pell unit is congruent to (1,0) modulo M. In fact e<=M². Thus multiplying X+S sqrt(q) by (U+V sqrt(q))^(e*m), m>=1, yields integer (X_m,S_m) satisfying:

1. The exact norm equation (1).
2. X_m≡X and S_m≡S (mod M).
3. Both coordinates are positive and strictly increase with m.

Because X_m≡aT (mod M), X_m is divisible by a, and

    T_m=X_m/a

satisfies T_m≡T (mod R). Define the positive integer polygonal indices

    t_m=(T_m+L)/R,
    s_m=(S_m+L)/R.

The stronger condition S_m≡S (mod 2aR) gives s_m≡u (mod 2a). Consequently P_k(s_m)≡P_k(u) (mod a), since the polygonal formula is integer-valued and the index difference is divisible by 2a. Hence

    d_m=(P_k(s_m)-c)/a

is a positive integer.

The exact norm equation (1) implies b*d_m+c=P_k(t_m), while the other two exact pair equations hold by definition. The entries are distinct: b>a by construction; and for a positive Pell step, S_m=V_m*aT+U_m*S > T (since aV_m>=1), so s_m>r and therefore d_m>b. In particular **the first promoted step already gives a valid Type B triple**. Repeating steps gives infinitely many strictly increasing d_m. QED.

## Step 4: the exceptional square-order case

If k=4 and a=u, then c=P_4(u)-u²=0. For every integer n>=3 the triple

    (a,b,d)=(u,4u,n²u)

has pair products (2u)²,(nu)²,(2nu)² and hence is an exact square-output Type B triple with indices (2u,nu,2nu). Every entry is positive and distinct. Varying n gives infinitely many examples.

This covers all parameter cases.

## Concrete example outside the earlier WP09-009 family

Take k=7, u=2, a=2. Then P_7(2)=7, c=3. The constructor chooses r=6, b=39 and q=ab=78, which is nonsquare. The first residue-preserving Pell step gives the **exact positive-integer tuple**

    (a,b,d) = (2, 39, 11293707732912017913758403774086454320790468713804)

at indices

    (r,s,t) = (6, 3005822048347109708020586, 13273350768868706404017954).

All three equalities ab+3=P_7(r), ad+3=P_7(s), bd+3=P_7(t) are checked by exact integer arithmetic, not approximate roots or modular tests.

The offset c=3 is **not** of the earlier form P_7(v)-1: that would require P_7(v)=4, impossible for positive v. Thus the new theorem strictly extends the preceding global-existence class.

## Reproduction and limits

- Producer: [research/figurate_wp09_square_shift_existence.py](../research/figurate_wp09_square_shift_existence.py). It checks every generated exact pair identity, both index congruences, the Pell norm and the required divisibility conditions.
- Independently written arithmetic regression: [tests/test_figurate_wp09_square_shift_existence.py](../tests/test_figurate_wp09_square_shift_existence.py). It recomputes every pair output using a different polygonal formula, checks k=3..21, u=1..4, a=1..4, distinct increasing Pell steps, different nonsquare second entries, signed offsets, and exceptions.

Run from repository root:

    python3 -m unittest -v tests.test_figurate_wp09_square_shift_existence
    python3 -m research.figurate_wp09_square_shift_existence --order 7 --index 2 --first-entry 2

**Boundaries:** This theorem proves global existence for precisely stated square-shift parameter families; it does not imply that every everywhere-locally-compatible order/offset admits an exact tuple or that an everywhere-local/global counterexample exists. The Pell construction can produce large integers even for modest input parameters; no computational efficiency or optimal seed-size assertion is made. Literature originality remains unverified; protected internal admission does not imply independent mathematical certification.
