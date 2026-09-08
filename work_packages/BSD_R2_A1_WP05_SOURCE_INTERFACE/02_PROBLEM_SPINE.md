# Formal problem statement

## 1. Curve class

Let `E/Q` be an elliptic curve with conductor `N`. The selected class requires:

1. `E` is semistable;
2. `N` is odd;
3. `E` has good ordinary reduction at `2`;
4. the Galois module `E[2]` is irreducible over `F_2`;
5. `ord_{s=1} L(E,s)=1`.

All five conditions are hypotheses. No CM, twist-family, auxiliary-Heegner, or extra local hypothesis is silently added.

## 2. WP00 normalizations

Use the complete finite Hasse-Weil Euler product from the outset,

`L(E,s) = product_l P_l(l^{-s})^{-1}`,

and the completed function

`Lambda(E,s)=N^{s/2}(2*pi)^{-s} Gamma(s) L(E,s)`.

Fix a global minimal Neron model and minimal Neron differential `omega_E`. Define

- `Omega_E = integral_{E(R)} |omega_E|`;
- `c_l = [E(Q_l):E^0(Q_l)]`;
- `Reg_E` as the determinant of the Neron-Tate height pairing on a basis of `E(Q)/E(Q)_tors`.

The torsion term is `#E(Q)_tors^2`. Incomplete L-values, plus-period conventions, separate archimedean Tamagawa factors, optimal-isogeny conventions, and non-minimal differentials require explicit conversion and are not substitutes.

## 3. Valuation convention

For this native interface, `ord_2 : Q^x -> Z` is the additive valuation normalized by `ord_2(2)=1`; equivalently, if `q=2^n a/b` with odd nonzero integers `a,b`, then `ord_2(q)=n`.

WP00 used `ord_2` notation in the selected target but did not separately spell out this normalization. This line closes that documentary ambiguity; it does not attribute new text to WP00.

## 4. Imported rank-one interface

Under analytic rank one, the protected Gross-Zagier/Kolyvagin interface supplies algebraic rank one and finiteness of `Sha(E/Q)`. Gross-Zagier also supplies rationality and nonvanishing of the normalized derivative needed to apply `ord_2`.

## 5. Selected target

Prove or disprove

`ord_2(L'(E,1)/(Omega_E Reg_E)) = ord_2((#Sha(E/Q) product_{l|N} c_l)/(#E(Q)_tors^2)).`

No stronger conclusion is licensed.