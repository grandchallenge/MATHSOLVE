# Exact local-at-2 lemmas

## Lemma 1 — good ordinary at 2 forces `a_2=+/-1`

Let `E/Q_2` have good ordinary reduction and put

`a_2 = 2+1-#E_tilde(F_2)`.

For an elliptic curve with good reduction at `p`, ordinarity is equivalent to `p not| a_p`. Hence `a_2` is odd. Hasse gives

`|a_2| <= 2 sqrt(2) < 3`.

The only odd integers satisfying this bound are `+1` and `-1`. Therefore

`a_2 in {+1,-1}`

and

`#E_tilde(F_2)=3-a_2 = 2` if `a_2=+1`, and `4` if `a_2=-1`.

**Status:** `PROVED_IN_PACKAGE`.

### Corollary

The condition

`2 not| #E_tilde(F_2)`

is impossible under the selected good-ordinary-at-2 hypothesis.

This statement is deliberately phrased as an exact divisibility fact. Terminology such as "anomalous prime" varies between sources and is not used as a theorem hypothesis here.

## Lemma 2 — exact unit-root correction

Let `alpha` be the 2-adic unit root and `beta` the non-unit root of

`X^2-a_2 X+2`.

Then

`alpha beta = 2`,

`v_2(alpha)=0`, and `v_2(beta)=1`.

Therefore `1-beta` is a 2-adic unit. Also

`(1-alpha)(1-beta) = 1-(alpha+beta)+alpha beta = 3-a_2`.

Taking valuations gives

`ord_2(1-alpha)=ord_2(3-a_2)`.

Since `alpha` is a unit,

`ord_2(1-alpha^(-1)) = ord_2((alpha-1)/alpha) = ord_2(3-a_2)`.

Thus

`ord_2(1-alpha^(-1)) = 1` when `a_2=+1`,

and

`ord_2(1-alpha^(-1)) = 2` when `a_2=-1`.

If a chosen ordinary p-adic L-function normalization contains the interpolation multiplier

`e_2(E)=(1-alpha^(-1))^2`,

then

`ord_2(e_2(E)) = 2 ord_2(3-a_2) in {2,4}`.

**Status:** `PROVED_IN_PACKAGE` for the algebraic valuation statement. The assertion that a particular p-adic L-function uses this multiplier is normalization-specific and must be source-bound before theorem use.

## Lemma 3 — standard residual 2-distinguishedness is impossible

Good ordinary reduction gives a rank-one ordinary filtration of the 2-adic Tate module over `G_Q2`. Reducing the two rank-one characters modulo `2` gives characters

`bar_psi_1, bar_psi_2 : G_Q2 -> F_2^x`.

But

`F_2^x={1}`.

Hence

`bar_psi_1 = bar_psi_2 = 1`.

Therefore the standard residual ordinary condition requiring the two diagonal residual characters to be distinct cannot hold at `p=2` for this coefficient field.

**Status:** `PROVED_IN_PACKAGE`.

### Compatibility with global irreducibility

The selected campaign assumption says the two-dimensional `F_2[G_Q]` module `E[2]` is irreducible globally. Lemma 3 concerns its restriction to the decomposition group at `2`, where the ordinary filtration is locally reducible. A globally irreducible representation may be reducible after restriction to a proper subgroup. There is no contradiction.

## Firewall

None of these lemmas identifies the complex derivative `L'(E,1)` with a p-adic derivative. Differentiating a rank-zero interpolation identity is not a valid substitute for an explicit rank-one reciprocity or p-adic Gross-Zagier theorem.