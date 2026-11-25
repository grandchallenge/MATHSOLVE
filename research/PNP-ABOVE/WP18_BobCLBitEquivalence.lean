import PNPAbove.WP18Query

namespace PNPAbove.WP18
open MIPRE MIPRE.CL MIPRE.Cost
set_option maxRecDepth 8192
set_option maxHeartbeats 1000000

/-! ### Source-native equivalence between Bob's CL semantics and bit strings -/

/-- A legal Bob marginal's original nine-bit encoding is the exact
input prefix followed by literal zero padding. -/
theorem bob_marginal_bits (j : Nat) (hj : 1 ≤ j) (hj9 : j ≤ 9)
    (x : Fin 9 → 𝔽₂) :
    toBits ((bobNineCL.truncate j).eval x) = bobPrefix j (toBits x) := by
  rw [bob_marginal_formula j hj hj9]
  interval_cases j <;>
    simp [toBits, bobPrefix, List.ofFn_succ]

/-- The actual original CL linear map agrees with the executable sparse
one-bit mask at every stage and all prefix vectors. -/
theorem bob_linear_bits (j : Nat) (hj : 1 ≤ j) (hj9 : j ≤ 9)
    (u y : Fin 9 → 𝔽₂) :
    toBits ((bobNineCL.mapOfPrefix (j-1) u) y) =
      bobLinearBits j (toBits y) := by
  rw [bob_linear_formula j hj hj9]
  interval_cases j <;>
    simp [toBits, bobLinearBits, WP14.bitmap, WP14.allZero,
      proj_apply, List.ofFn_succ, Finset.mem_singleton] <;>
    split_ifs <;> simp_all

theorem bob_factor_bits (j : Nat) (hj : 1 ≤ j) (hj9 : j ≤ 9)
    (u : Fin 9 → 𝔽₂) :
    indicatorBits (bobNineCL.factorOfPrefix (j-1) u) = WP14.bitmap (j-1) := by
  rw [bobNineCL_factor_singleton j hj hj9 u]
  simp [indicatorBits, WP14.bitmap, List.ofFn, Finset.mem_singleton, Fin.ext_iff]

end PNPAbove.WP18
