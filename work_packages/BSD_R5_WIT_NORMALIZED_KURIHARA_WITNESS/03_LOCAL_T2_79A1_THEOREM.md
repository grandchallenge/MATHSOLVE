# BSD R5-WIT — exact local `t_2=2` theorem for selected instance `79a1`

## 1. Protected inputs

Use:

- the protected R5-RECIP local theorem in MATHSOLVE;
- the admitted good-ordinary `Q_2` local-torsion classification at `grandchallenge/MATHFORGE@2a112e28026d33062ea314c55e69c157bf9ae863`;
- the pinned external input record for `79a1` at `grandchallenge/MATHFORGE@aeb6588785e70bb7477cdcf44b018c150674c8e4`.

The admitted model is

`[a1,a2,a3,a4,a6]=[1,1,1,-2,0]`.

For a generalized Weierstrass model write

`b2=a1^2+4a2`, `b4=2a4+a1a3`, `b6=a3^2+4a6`,
`b8=a1^2a6+4a2a6-a1a3a4+a2a3^2-a4^2`.

For `79a1` this gives

`(b2,b4,b6,b8)=(5,-3,1,-1)`.

The affine two-division polynomial is

`F2(x)=4x^3+5x^2-6x+1`.

The non-2-torsion fourth-division factor is

`F4(x)=2x^6+5x^5-15x^4+10x^3-10x^2-2x+2`.

For fixed `x`, the Weierstrass equation is quadratic in `y` with discriminant

`D(x)=(x+1)^2+4(x^3+x^2-2x)`.

## 2. Good ordinary reduction and the local range

Direct enumeration over `F_2` gives four points including infinity, so

`q_2=#E(F_2)=4`

and

`a_2=2+1-q_2=-1`.

Thus the reduction is good ordinary. Protected R5-RECIP supplies one nonzero formal rational point of order two. The admitted Ozeki–Yoshida interface bounds the full good-ordinary local 2-primary torsion order by `8`; hence only `t_2=1,2,3` remain possible.

## 3. No second order-two point

Direct enumeration gives no root of `F2` modulo `16`.

Any nonformal `Q_2`-rational torsion point under good reduction has integral affine coordinates. Therefore any second rational order-two point would give a `Z_2`-root of `F2`, hence a root modulo `16`. None exists.

So the already protected formal order-two point is the unique nonzero element of `E(Q_2)[2]`.

## 4. A rational point of order four exists

Modulo `16`, `F4` has exactly one root,

`x == 9 (mod 16)`.

Moreover

`F4'(9) == 1 (mod 2)`.

Hensel's lemma therefore gives a unique root `x_4 in Z_2` with `x_4 == 9 (mod 16)`. In fact the unique root modulo `32` is still `9`, and

`D(x_4) == D(9) == 4 (mod 32)`.

Hence `v_2(D(x_4))=2` and `D(x_4)/4 == 1 (mod 8)`. By the standard square criterion in `Q_2`, `D(x_4)` is a square. Therefore the Weierstrass quadratic in `y` has a `Q_2`-solution above `x_4`.

Since `x_4` is a root of the non-2-torsion factor of the fourth division polynomial, this point has exact order four.

## 5. No rational point of order eight

Let `P3=psi_3` and `P4=F4`. With `F2=psi_2^2`, the standard division-polynomial recurrence gives

`P5 = P4*F2^2 - P3^3`,

`P6base = P3*(P5-P4^2)`,

and

`psi_8 = psi_2 * P4 * G8`

with

`G8 = P6base*P3^2 - P5^2`.

Thus a point of exact order eight has integral affine `x`-coordinate satisfying `G8(x)=0`; the `P4` factor accounts for points already killed by four.

The exact certificate constructs `G8` over `Z[x]` from these recurrences and enumerates all classes modulo `16`. It finds no root.

Because the admitted/protected local formal subgroup has no torsion beyond order two, any order-eight point would be nonformal and therefore integral. Its `x`-coordinate would reduce to a root of `G8` modulo `16`, contradiction.

Hence `E(Q_2)` contains no point of order eight.

## 6. Exact local torsion group

There is exactly one nonzero rational point of order two, at least one point of order four, and no point of order eight. Among the admitted good-ordinary possibilities this forces

`E_79a1(Q_2)[2^infinity] ~= Z/4Z`.

Therefore

`#E_79a1(Q_2)[2^infinity]=4`

and

`t_2(79a1)=2`.

## 7. Consequence for R5-WIT

Protected R5-RECIP proves

`Delta_n^(2)=2^t_2*delta_tilde_n`

and that `t_2>=2` forces the normalized witness to vanish modulo two. Therefore on `79a1`

`Delta_n^(2)=0 mod 2`

for every admitted finite derivative level.

This does not prove that the residual Kato/Kolyvagin class vanishes. It proves only that this normalized local-regulator/Kurihara witness cannot detect it on `79a1`. An alternative residual witness is required on that sublane.

No R5-RES, R5-PRIM, D2d, BSD-R2-A1, novelty/priority, or MATHCERT certification claim is made.
