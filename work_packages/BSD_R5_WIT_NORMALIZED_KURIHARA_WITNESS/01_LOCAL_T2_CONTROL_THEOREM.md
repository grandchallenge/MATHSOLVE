# BSD R5-WIT — exact local `t_2=1` theorem for the protected A/B controls

## 1. Inputs

Use the protected R5-RECIP local theorem and the protected WP18A control models.

For a generalized minimal Weierstrass model

`y^2 + a1*x*y + a3*y = x^3 + a2*x^2 + a4*x + a6`,

write

`b2=a1^2+4a2`, `b4=2a4+a1a3`, `b6=a3^2+4a6`,

`b8=a1^2a6+4a2a6-a1a3a4+a2a3^2-a4^2`.

The non-2-torsion factor of the fourth division polynomial is

`F4(x)=2x^6+b2*x^5+5b4*x^4+10b6*x^3+10b8*x^2+(b2*b8-b4*b6)x+(b4*b8-b6^2)`.

If a `Q_2`-rational point has exact order four, its integral `x`-coordinate is a root of `F4` in `Z_2`. For a fixed `x`, the Weierstrass equation is quadratic in `y` with discriminant

`D(x)=(a1*x+a3)^2+4(x^3+a2*x^2+a4*x+a6)`.

A necessary and sufficient condition for a corresponding `y in Q_2` is that `D(x)` be a square in `Q_2`.

Protected R5-RECIP already proves on both controls that the local 2-primary torsion contains exactly one nonzero point in the formal subgroup; hence `t_2>=1`. Protected WP18A gives `q_2=4`, so R5-RECIP gives `t_2<=3`.

## 2. Regime-A control `53a1`

The protected minimal model is `[1,-1,1,0,0]`. Thus

`(b2,b4,b6,b8)=(-3,1,1,-1)`

and

`F4(x)=2x^6-3x^5+5x^4+10x^3-10x^2+2x-2`.

Direct finite enumeration modulo `16` gives exactly one root:

`x == 13 (mod 16)`.

For this residue class,

`D(x) == 20 (mod 32)`.

Any `2`-adic square of valuation exactly two is congruent to `4 mod 32`, because an odd square is `1 mod 8`. Since `20 mod 32` has valuation two but unit part `5 mod 8`, it is not a square in `Q_2`.

Therefore `53a1(Q_2)` has no point of order four. Since its protected local 2-primary torsion is nontrivial, it follows that

`E_53a1(Q_2)[2^infinity] ~= Z/2Z`

and

`t_2(53a1)=1`.

## 3. Regime-B control `203b1`

The protected minimal model is `[1,1,1,0,-2]`. Thus

`(b2,b4,b6,b8)=(5,1,-7,-9)`

and

`F4(x)=2x^6+5x^5+5x^4-70x^3-90x^2-38x-58`.

Direct finite enumeration modulo `16` gives exactly one root:

`x == 5 (mod 16)`.

For this residue class,

`D(x) == 20 (mod 32)`.

The same square-class argument excludes a `Q_2`-rational `y`. Hence `203b1(Q_2)` also has no point of order four, and

`E_203b1(Q_2)[2^infinity] ~= Z/2Z`,

`t_2(203b1)=1`.

## 4. Consequence for R5-WIT

For both protected A/B controls, the R5-RECIP normalized finite object is exactly

`Delta_n^(2)=2*delta_tilde_n`.

Therefore the automatic vanishing theorem for `t_2>=2` does not apply to either control. A nonzero mod-2 normalized Kurihara witness remains arithmetically possible on both regimes.

This theorem is deliberately control-specific. It does not prove `t_2=1` uniformly on the entire selected class.

## 5. Claim firewall

No finite `Delta_n^(2)` is asserted nonzero here. R5-RES, R5-PRIM, D2d, BSD-R2-A1, novelty/priority, and MATHCERT certification remain unestablished.