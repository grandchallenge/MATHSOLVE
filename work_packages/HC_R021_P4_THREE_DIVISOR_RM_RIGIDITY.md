# HC-R021-P4 — Rigidity of three-divisor Chern identities in the RM plane

**Campaign:** `HC-001`  
**Restricted target:** `HC-R021-A8-CM4-C2`  
**Parent development revision:** `9ea95eedd5aceaf1b5555c856ff9f4e4bce0bc95`  
**State:** `THIRD_RM_DIVISOR_FORCED_ON_J_RAY__NO_ALTERNATE_THREE_BLOCK_DIRECTION`  
**Date:** 2026-09-16

## 1. Purpose

Determine whether the failed three-divisor construction `L025-L026` can be repaired merely by replacing

```text
J=D+qH
```

with a different ample divisor in the real-multiplication plane.

It cannot. Once the first two blocks are `B_D` and `B_H`, any third divisor whose symmetric divisor block can participate in a three-block Chern-character identity on the nonzero `beta'` ray is forced to lie on the same ray as `J`.

The result removes a continuous-looking search space and reduces the only residual three-divisor variant to divisibility of the `J` polarization itself.

## 2. Setup

Use the RM normal form

```text
D=U+V,
H=aU+bV,
ab=1,
tau=a+b,

beta'=D-(q/6)H^3,

A=1+q tau+q^2=(1+qa)(1+qb).
```

Let a third rational divisor class in the RM plane be

```text
L=mD+nH.
```

For an integral ample representative of this class define, as before,

```text
B_L=O_(2L)(L),
ch(B_L)=2L+(1/3)L^3.
```

Suppose there are rational coefficients

```text
x,y,z,C,
```

with

```text
z!=0,
C!=0,
```

such that

```text
x ch(B_D)+y ch(B_H)+z ch(B_L)
 = 2C beta'.                              (2.1)
```

The rational formulation is the correct one: denominators can be cleared afterwards whenever the three divisor classes are integral.

## 3. Linear equations

Comparing degree two in (2.1) gives

```text
xD+yH+zL=CD.
```

Since `D,H` are independent in the selected RM plane,

```text
x+zm=C,
y+zn=0.                                  (3.1)
```

Substituting these into the degree-six equation yields

```text
C D^3
 + z [L^3-mD^3-nH^3]
 = -C q H^3.                              (3.2)
```

Thus the vector

```text
W(L):=L^3-mD^3-nH^3
```

must be proportional to

```text
-(D^3+qH^3).                              (3.3)
```

## 4. Exact cubic calculation

Write

```text
L=(m+na)U+(m+nb)V.
```

Since `U^3=V^3=0`, direct expansion gives

```text
W(L)
 = 3(m+na)(Q-1) U^2V
   + 3(m+nb)(Q-1) UV^2,                  (4.1)
```

where

```text
Q:=m^2+mn tau+n^2
  =(m+na)(m+nb).                          (4.2)
```

On the other hand

```text
-(D^3+qH^3)
 = -3(1+qa) U^2V
   -3(1+qb) UV^2.                         (4.3)
```

The determinant of the two coefficient vectors in (4.1) and (4.3) is, up to the nonzero scalar `9(a-b)`,

```text
(mq-n)(Q-1).                              (4.4)
```

Therefore proportionality requires

```text
(mq-n)(m^2+mn tau+n^2-1)=0.              (4.5)
```

### The `Q=1` branch is spurious

If

```text
Q=1,
```

then (4.1) gives

```text
W(L)=0.
```

Equation (3.2) would then require

```text
D^3=-qH^3,
```

which is impossible: in the `U^2V,UV^2` basis both `D^3` and `H^3` have strictly positive coefficients and `q>0`.

Thus the second factor in (4.5) cannot produce (2.1).

We are forced onto

```text
n=mq.                                     (4.6)
```

Hence

```text
L=m(D+qH)=mJ.                             (4.7)
```

## 5. The unique one-parameter identity

Substitute `n=mq`. Then

```text
Q=m^2 A
```

and (3.2) determines

```text
z/C = -1/[m(m^2A-1)].                    (5.1)
```

The exceptional value

```text
m^2A=1
```

again makes `W(L)=0` and gives no nonzero `beta'` identity.

Using (3.1), one obtains

```text
x/C = m^2A/(m^2A-1),
y/C = q/(m^2A-1).                         (5.2)
```

Choosing the convenient scale

```text
C=m(m^2A-1)
```

gives the exact family

```text
m^3 A ch(B_D)
 + m q ch(B_H)
 - ch(B_(mJ))
 = 2m(m^2A-1) beta'.                     (5.3)
```

For `m=1`, (5.3) is exactly the identity used in `L025`:

```text
A ch(B_D)+q ch(B_H)-ch(B_J)
 = 2q(tau+q) beta',
```

because

```text
A-1=q(tau+q).
```

## 6. HC-R021-L027 — RM three-divisor rigidity

### Statement

Let `L` be a divisor class in the rational span of `D,H`. If a nontrivial rational linear combination of

```text
ch(B_D), ch(B_H), ch(B_L)
```

is a nonzero multiple of `beta'`, with a nonzero coefficient on `B_L`, then

```text
L=mJ
```

for some positive rational `m` for which `mJ` is integral and `m^2A!=1`.

After scaling, every such identity is the family (5.3).

In particular there is no third direction in the RM plane whose support geometry can replace the `J` ray while preserving the required Chern character.

### Proof

Sections 3-5.

QED.

## 7. Consequence for route design

The three-divisor search now has only two arithmetic subcases.

### 7.1 `m>=1`

If `m>=1`, then

```text
mJ-D=(m-1)D+mqH
```

and

```text
mJ-H=mD+(mq-1)H
```

are ample. Therefore the Ext-parity mechanism of `HC-R021-L026` applies verbatim: an odd `B_(mJ)` block cannot couple by a degree-one twisting morphism to the positive `B_D/B_H` blocks, and rank `20` is impossible in the corresponding three-block family.

### 7.2 `0<m<1`

This can occur only if the integral polarization `J` is divisible in `NS(X)`: the third block is a proper integral divisor of the `J` ray.

This is the **only** residual three-divisor escape left by `L027`. It is now a discrete arithmetic question rather than a search over arbitrary divisors:

```text
Does J admit a proper integral divisor L=mJ
with m^2A!=1,
and can the resulting indefinite Ext geometry
supply the mixed nullhomotopies?
```

If `J` is primitive, the entire three-divisor lane is closed by `L025-L027`.

If `J` is divisible, only its proper integral divisors need be tested.

## 8. Scope and firewall

`L027` does not decide the divisibility of `J` in the selected source datum, and it does not rule out:

- a proper integral divisor of `J` when one exists;
- four or more divisor directions;
- `K_0`-zero bridge terms;
- higher-rank/semihomogeneous or torsion bridge objects;
- a different derived-autoequivalence source class.

It proves only the rigidity of **three** symmetric divisor blocks once two of them are fixed to `D` and `H`.

## 9. Current disposition

```text
HC-R021-L027 = proved_in_solve_package_not_certified
three_divisor_third_direction_in_RM_plane = forced_to_J_ray
unique_three_divisor_identity_family = equation_5_3
m_ge_1_three_block_lane = pruned_by_L026
proper_integral_divisor_of_J = only_remaining_three_block_case
J_divisibility = open
second_factor_rank20_exists = open
HC-R021-P4 = open
restricted_target_proved = false
full_hodge_conjecture_proved = false
```

## 10. Inputs

- `HC-R021-L006`, `L025`, and `L026`;
- the RM normal form `D=U+V`, `H=aU+bV`, `ab=1`;
- the symmetric divisor-block identity `ch(B_L)=2L+L^3/3` on the fourfold.
