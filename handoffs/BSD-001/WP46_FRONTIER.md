# BSD-001 frontier after WP46A

## Protected predecessors

- MATHSOLVE WP45A: `5f7ea71f2d86457575b2bc2f1e8c281f09ce4b87`.
- MATHFORGE WP46A local-Iwasawa descent admission: `230e449711166e0ad7cf11081cbeec28c553c0ba`.

## WP46A closure

The strict/Kummer Iwasawa comparison no longer requires a noncanonical forward lift.

For every relevant local place `w`, protected WP46A proves that the strict and classical-Kummer degree-one local conditions coincide at Iwasawa level:

`H^1(U_{w,infty}^{+,str}) ~= M_w^Kum`.

Therefore the WP45A Kummer local condition is canonically the lower truncation of the strict local condition:

`U_{w,infty}^{+,Kum}
 ~= tau_{<=1}U_{w,infty}^{+,str}`.

Hence there is a canonical reverse comparison triangle

`U_{w,infty}^{+,Kum}
 -> U_{w,infty}^{+,str}
 -> Z_w^str[-2]
 ->`,

where

`Z_w^str:=H^2(U_{w,infty}^{+,str})`.

At odd places `Z_w^str=0`; the two local conditions are canonically isomorphic.

At each `w|2`, put

`m_2:=ord_2(3-a_2)`.

Finite-layer local Tate duality and the protected literal-`p=2` Chapter-8 Iwasawa descent theorem give

`Z_w^str
 ~= Lambda_w/(2^{m_2},gamma_w-1)
 ~= Z/2^{m_2}Z`,

with trivial `Gamma_w` action.

Thus the higher strict Iwasawa correction has exact length `m_2`.

## WP45A kernel is closed

Protected WP46A further proves

`B_w^Kum=0`

at each `w|2`. The Kummer augmentation/control sequence is therefore

`0 -> (M_w^Kum)_{Gamma_w}
   -> H^1(U_{w,0}^{+,Kum})
   -> U_w
   -> 0`.

Strict descent gives

`0 -> (M_w^Kum)_{Gamma_w}
   -> H^1(U_{w,0}^{+,str})
   -> Z_w^str
   -> 0`.

Together with the protected finite strict/Kummer quotient, a 3-by-3 argument yields the canonical exact sequence

`0 -> Z_w^str
   -> U_w
   -> R_w
   -> 0`,

where

`R_w:=H^1(K_w,T_w^-)_tors`,

`len Z_w^str=m_2`,

`len U_w=2m_2`,

`len R_w=m_2`.

This is the exact derived-control filtration of the full universal-norm specialization defect.

## Remaining map-level comparison

Protected WP28 independently gives

`0 -> F_w^norm
   -> U_w
   -> E_tilde(F_2)
   -> 0`.

The two filtrations of the same group `U_w` have matching term lengths, but equality of sizes is not enough to identify their maps or subgroups.

The live D2b boundary is therefore

`MISSING_P2_MAP_LEVEL_RECONCILIATION_OF_STRICT_H2_AND_FORMAL_UNIVERSAL_NORM_FILTRATIONS`.

A successor must identify, by maps rather than cardinalities, whether the derived strict subgroup

`Z_w^str subset U_w`

is the Tan formal universal-norm subgroup

`F_w^norm subset U_w`,

and reconcile the corresponding quotient map with the literal reduction map.

Only then may the local comparison be propagated into WP40's global dual defect and the strict Bockstein normalization.

## Other live boundaries

`BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

### D1c

`MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`.

### D2a

`MISSING_P2_K_HEIGHT_NONDEGENERACY`.

### D2c

`MISSING_P2_DISEGNI_SPLIT_BAD_PRIME_NEWVECTOR_QORD_FACTORS`.

### D2d

`MISSING_P2_CLASSICAL_GROSS_ZAGIER_WP00_NORMALIZATION`.

### D2e

`MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

## Immediate successors

### WP47A — map-level formal/strict reconciliation at `2`

Compare the two exact sequences of `U_w` using the actual finite-layer maps:

1. strict Iwasawa descent and its `H^2` boundary;
2. Tan's reduction/formal universal-norm sequence;
3. Greenberg's finite strict/Kummer quotient.

The target is a commuting diagram proving or refuting

`Z_w^str = F_w^norm`

inside `U_w`, with exact quotient-map concordance. Do not infer this from equal orders.

### WP47B — split semistable bad-prime `Q^ord` factors

Continue the exact Disegni newvector/Rankin–Selberg calculation. Retain Haar measures, local L-factors, denominator pairings, Steinberg twists, and all `2`-adic scalars.

## Administrative source-index debt

The canonical MATHFORGE `provider_manifests/BSD-001.json` remains stale after WP36 and does not yet index the protected WP37–WP46 source audits. This is an administrative discoverability defect, not a theorem defect. Reconcile the full missing range in one maintenance tranche rather than patching only the most recent source.

## Claim firewall

Do not promote:

- `Z_w^str=F_w^norm` from matching lengths;
- `R_w=E_tilde(F_2)` from matching lengths;
- the canonical reverse comparison to perfectness of either global complex;
- `D_K` to a Bockstein or height defect before map-level reconciliation;
- height existence to nondegeneracy;
- canonical local `Q^ord_2=1` to global `Q^ord=1`;
- BSD, MATHCERT certification, novelty, or priority.