# BSD R5-WIT — exact local `t_2=1` theorem for the protected A/B controls

## 1. Inputs

Use the protected R5-RECIP local theorem, the protected WP18A control models, and the bounded local-torsion source interface admitted at

`grandchallenge/MATHFORGE@2a112e28026d33062ea314c55e69c157bf9ae863`.

For a generalized minimal Weierstrass model

`y^2 + a1*x*y + a3*y = x^3 + a2*x^2 + a4*x + a6`,

write

`b2=a1^2+4a2`, `b4=2a4+a1a3`, `b6=a3^2+4a6`,

`b8=a1^2a6+4a2a6-a1a3a4+a2a3^2-a4^2`.

The affine two-division polynomial is

`F2(x)=4x^3+b2*x^2+2b4*x+b6`.

The non-2-torsion factor of the fourth division polynomial is

`F4(x)=2x^6+b2*x^5+5b4*x^4+10b6*x^3+10b8*x^2+(b2*b8-b4*b6)x+(b4*b8-b6^2)`.

For a fixed affine `x`, the Weierstrass equation is quadratic in `y` with discriminant

`D(x)=(a1*x+a3)^2+4(x^3+a2*x^2+a4*x+a6)`.

Protected R5-RECIP proves on both controls that the formal subgroup contains exactly one nonzero rational point of order two. Thus `t_2>=1`, and the formal subgroup contains no point of order four. Protected WP18A gives `q_2=4`, while protected R5-RECIP gives `t_2<=3`.

The admitted Ozeki–Yoshida interface confirms that higher good-ordinary local torsion can occur in general, so the remaining checks must be done on the actual controls rather than inferred from good ordinarity.

Under good reduction, a torsion point outside the formal kernel has nonidentity reduction and therefore integral affine coordinates. Consequently:

1. any second independent `Q_2`-rational point of order two would give a `Z_2`-root of `F2`;
2. any `Q_2`-rational point of exact order four would be nonformal, hence would have integral `x` and give a `Z_2`-root of `F4` with square `D(x)`.

## 2. Regime-A control `53a1`

The protected minimal model is `[1,-1,1,0,0]`. Thus

`(b2,b4,b6,b8)=(-3,1,1,-1)`,

`F2(x)=4x^3-3x^2+2x+1`,

and

`F4(x)=2x^6-3x^5+5x^4+10x^3-10x^2+2x-2`.

Direct finite enumeration gives no root of `F2` modulo `16`. Therefore `F2` has no root in `Z_2`, excluding any second nonformal local point of order two.

Modulo `16`, `F4` has exactly one root class:

`x == 13 (mod 16)`.

Any `Z_2` lift of this class has residue modulo `32` equal to `13` or `29`. Direct substitution gives

`D(13) == D(29) == 20 (mod 32)`.

A `2`-adic square of valuation exactly two is congruent to `4 mod 32`: if `s=2u` with `u` odd, then `s^2=4u^2` and `u^2=1 mod 8`. Since `20/4 == 5 mod 8`, this discriminant is not a square in `Q_2`. Hence there is no local point of order four.

Combining the protected unique nonzero formal point of order two with the absence of any additional order-two point and of any order-four point gives

`E_53a1(Q_2)[2^infinity] ~= Z/2Z`

and

`t_2(53a1)=1`.

## 3. Regime-B control `203b1`

The protected minimal model is `[1,1,1,0,-2]`. Thus

`(b2,b4,b6,b8)=(5,1,-7,-9)`,

`F2(x)=4x^3+5x^2+2x-7`,

and

`F4(x)=2x^6+5x^5+5x^4-70x^3-90x^2-38x-58`.

Again `F2` has no root modulo `16`, excluding a second nonformal local point of order two.

Modulo `16`, `F4` has exactly one root class:

`x == 5 (mod 16)`.

Its two possible residue classes modulo `32` are `5` and `21`, and direct substitution gives

`D(5) == D(21) == 20 (mod 32)`.

The same square-class argument excludes a `Q_2`-rational `y`, hence excludes local order four. Therefore

`E_203b1(Q_2)[2^infinity] ~= Z/2Z`

and

`t_2(203b1)=1`.

## 4. Consequence for R5-WIT

For both protected A/B controls, the R5-RECIP normalized finite object is exactly

`Delta_n^(2)=2*delta_tilde_n`.

Therefore the automatic vanishing theorem for `t_2>=2` does not apply to either control. A nonzero mod-2 normalized Kurihara witness remains arithmetically possible on both protected diagnostic regimes.

This theorem is deliberately control-specific. It does not prove `t_2=1` uniformly on the entire selected class. The hard filter alone is not used as a substitute for an exact local torsion computation.

## 5. Claim firewall

No finite `Delta_n^(2)` is asserted nonzero here. R5-RES, R5-PRIM, D2d, BSD-R2-A1, novelty/priority, and MATHCERT certification remain unestablished.
