# HC-R021-P4 — Ext-parity obstruction for the three divisor blocks

**Campaign:** `HC-001`  
**Restricted target:** `HC-R021-A8-CM4-C2`  
**Parent development revision:** `fa5fadbc6fd4bc3d2e99f115aaa229ac81c9d310`  
**State:** `THREE_DIVISOR_BLOCK_TWISTED_COMPLEX_SPLITS_J__RANK20_IMPOSSIBLE`  
**Date:** 2026-09-16

## 1. Purpose

Strengthen `HC-R021-L025` from the natural two-term locally free realization to the divisor blocks themselves.

The three-divisor Chern identity is

```text
A ch(B_D)+q ch(B_H)-ch(B_J)
 = 2q(tau+q) beta',

B_L := i_(2L),* O_(2L)(L),
J=D+qH.
```

A tempting derived realization is a non-split twisted complex built from `A` copies of `B_D`, `q` copies of `B_H`, and one copy of `B_J` in opposite parity.

This package proves that the `J` block cannot couple to either positive block by any degree-one twisting morphism, regardless of how the copies are shifted subject to the required `K_0` signs. The obstruction is an exact Ext-parity vanishing caused by the ample differences

```text
J-D=qH,
J-H=D+(q-1)H.
```

Thus every such three-block twisted complex splits off the odd `B_J` summand, and its mixed obstruction survives. The three-divisor divisor-block lane therefore cannot contain a rank-20 second factor.

## 2. Symmetric divisor blocks and their resolutions

For an ample integral divisor class `L`, choose a nonzero divisor section of `O_X(2L)` and set

```text
B_L := O_(2L)(L).
```

It has the two-term locally free resolution

```text
0 -> O_X(-L) -> O_X(L) -> B_L -> 0.      (2.1)
```

No smoothness or transversality assumption is needed for the Ext-parity calculation below; (2.1) is the resolution of an effective Cartier divisor.

Let `L,M` be ample classes such that

```text
M-L
```

is ample.

Resolve both objects by (2.1). The sheaf-Hom complex computing

```text
RHom_X(B_M,B_L)
```

has internal degrees `-1,0,1`:

```text
p=-1 : O_X(-L-M),

p= 0 : O_X(M-L) direct_sum O_X(L-M),

p= 1 : O_X(L+M).                         (2.2)
```

## 3. Cohomological shape of the RHom complex

On the abelian fourfold, an ample line bundle has cohomology only in degree `0`, while its inverse has cohomology only in degree `4`.

Because `L+M` and `M-L` are ample, the only nonzero cohomology groups on the first page of the hypercohomology spectral sequence for (2.2) occur at

```text
(p,q)=(-1,4),
        (0,0),
        (0,4),
        (1,0).
```

In particular there is no first-page term of total degree `2`. Therefore

```text
Ext^2_X(B_M,B_L)=0.                      (3.1)
```

The total-degree-zero term comes only from

```text
H^0(X,O_X(M-L))
```

inside `p=0`. Its `d_1` map to

```text
H^0(X,O_X(L+M))
```

is multiplication by the nonzero defining section of the `2L` divisor, up to the harmless sign convention of the Hom complex. Multiplication by a nonzero section on the integral variety `X` is injective. Hence

```text
Hom_X(B_M,B_L)=Ext^0_X(B_M,B_L)=0.       (3.2)
```

Interchanging `L` and `M` gives the same conclusion for `Hom_X(B_L,B_M)`: the unique possible total-degree-zero source is multiplied injectively by the other nonzero divisor section.

Since `K_X=O_X`, Serre duality then gives

```text
Ext^4_X(B_M,B_L)=0,
Ext^4_X(B_L,B_M)=0.                      (3.3)
```

Thus every **even** Ext group between the two divisor blocks vanishes:

```text
Ext^(2r)_X(B_M,B_L)=0,
Ext^(2r)_X(B_L,B_M)=0
```

for all degrees occurring on the fourfold. Odd Ext groups may be nonzero; they are not needed below.

### HC-R021-L026a — definite-difference Ext parity

If `L,M` are ample and `M-L` or `L-M` is ample, then

```text
Ext^even_X(B_M,B_L)=0=Ext^even_X(B_L,B_M).
```

## 4. Apply to D, H, and J

Recall

```text
J=D+qH,
q>=1.
```

Then

```text
J-D=qH
```

is ample, and

```text
J-H=D+(q-1)H
```

is ample. Therefore `L026a` gives

```text
Ext^even_X(B_J,B_D)=0=Ext^even_X(B_D,B_J),
Ext^even_X(B_J,B_H)=0=Ext^even_X(B_H,B_J).   (4.1)
```

This is an intrinsic statement about the divisor blocks; it does not depend on a particular locally free totalization.

## 5. K-parity forces the J block to decouple

Consider any finite twisted complex whose graded constituents are:

- `A` copies of shifts of `B_D` with **even** shift parity;
- `q` copies of shifts of `B_H` with **even** shift parity;
- one copy of a shift of `B_J` with **odd** shift parity.

These parities are exactly what is required for the total `K_0` class

```text
A[B_D]+q[B_H]-[B_J].                    (5.1)
```

A degree-one twisting morphism from `B_J[r]` to `B_D[s]`, with `r` odd and `s` even, lies in

```text
Hom^1(B_J[r],B_D[s])
 = Ext^(1+s-r)(B_J,B_D).
```

The exponent `1+s-r` is even. By (4.1) this group is zero. The same argument applies in the reverse direction and with `B_H` in place of `B_D`.

Therefore every degree-one twisting entry between the `J` block and the `D/H` blocks is zero.

The Maurer-Cartan differential of the twisted complex is consequently block diagonal with respect to

```text
{D,H blocks}  direct_sum  {J block}.
```

Hence the total object decomposes in `D^b(X)` as

```text
E ~= C_DH direct_sum B_J[r],             (5.2)
```

where `r` is odd and `C_DH` is an arbitrary twisted complex assembled from the positive-parity `D` and `H` blocks.

No higher composition can reconnect `B_J`: a twisted-complex differential is built from degree-one entries, and every entry crossing the displayed decomposition vanishes before the Maurer-Cartan equation is imposed.

## 6. The split-off J block detects every mixed combination

The divisor block `B_J` is represented by

```text
[O_X(-J) -> O_X(J)].
```

Apply the same two-term edge argument used in `HC-R021-L025`. The reverse/off-diagonal Hom bundles are `O_X(+-2J)`, whose degree-two cohomology vanishes. Hence the diagonal degree-two characteristic action on the two line-bundle terms survives to

```text
Ext^2_X(B_J,B_J).
```

Write

```text
J=(1+qa)U+(1+qb)V.
```

For

```text
k=lambda k_7+mu k_8,
```

the action on either line-bundle term has diagonal component

```text
lambda [qa+(1+qa)^2] y_1 wedge y_2
 + mu [qb+(1+qb)^2] y_3 wedge y_4.       (6.1)
```

Both scalar coefficients are strictly positive, and the two displayed two-forms are independent. Thus

```text
ob_(B_J)(k)=0
```

implies

```text
lambda=mu=0.
```

Equivalently,

```text
ker(ob_(B_J)) intersect span(k_7,k_8)=0. (6.2)
```

A shift does not change this self-characteristic action.

By the direct-sum decomposition (5.2), the action on `E` has `ob_(B_J[r])` as a direct summand. Therefore

```text
ker(ob_E) intersect span(k_7,k_8)=0.     (6.3)
```

## 7. HC-R021-L026 — three-divisor block parity no-go

### Statement

No twisted complex assembled solely from

```text
A copies of B_D,
q copies of B_H,
one copy of B_J,
```

with shift parities realizing the virtual class

```text
A[B_D]+q[B_H]-[B_J]
```

can have second-factor obstruction rank `20`.

Indeed the `B_J` block splits off, and no nonzero linear combination of the two mixed kernel vectors `k_7,k_8` lies in the obstruction kernel.

Since the total Chern character is the nonzero scalar

```text
2q(tau+q) beta',
```

semiregularity compatibility gives

```text
ker(ob_E) subset ker(c_beta')
                    = span(k_1,...,k_8).
```

Together with (6.3),

```text
dim ker(ob_E) <= 6,
rank(ob_E) >= 22.
```

Hence rank `20` is impossible throughout this divisor-block twisted-complex family.

### Proof

Sections 2-6.

QED.

## 8. Consequence for the three-divisor idea

The three-divisor Chern identity survives as useful arithmetic, but **neither** of its two immediate derived realizations can supply the mixed nullhomotopies:

```text
natural arbitrary-differential two-term line-bundle totalization
    -> rank exactly 22                         [L025]

arbitrary twisted complex of the three divisor blocks
with the required K-parities
    -> J block splits, rank at least 22        [L026]
```

A positive construction must add an object not present in the identity itself. In particular, a `K_0`-zero bridge may be mathematically essential rather than cosmetic.

The Ext-parity calculation also suggests what such a bridge must change: it must create a degree-one twisting channel across the positive/negative `K`-parity boundary, or realize the mixed nullhomotopy through a longer higher-differential mechanism not available to the three blocks alone.

## 9. Scope and firewall

`L026` does **not** rule out:

- adding `K_0`-zero bridge objects;
- longer locally free complexes not generated solely by the three divisor blocks;
- higher-rank or semihomogeneous bundles;
- torsion/intersection-supported bridges;
- a different rank-20 class followed by an autoequivalence;
- all-orders deformation/algebraicity transport.

It closes the proposed non-split complex **when its building blocks are only `B_D`, `B_H`, and `B_J` with the shift parities forced by the Chern identity**.

## 10. Current disposition

```text
HC-R021-L026 = proved_in_solve_package_not_certified
definite_difference_even_Ext = zero
J_to_DH_degree_one_twisting_channels = zero
three_divisor_block_twisted_complex = splits_off_J
three_divisor_block_rank20 = impossible
K0_zero_or_new_geometry_bridge = required
second_factor_rank20_exists = open
all_orders_transport = open
HC-R021-P4 = open
restricted_target_proved = false
full_hodge_conjecture_proved = false
```

## 11. Inputs

- `HC-R021-L006`, `L007`, `L016`, and `L025`;
- the divisor resolution `0 -> O(-L) -> O(L) -> B_L -> 0`;
- Kodaira/IT0 vanishing for ample line bundles on an abelian variety;
- Serre duality with `K_X=O_X`;
- standard shift and twisted-complex sign/parity conventions.
