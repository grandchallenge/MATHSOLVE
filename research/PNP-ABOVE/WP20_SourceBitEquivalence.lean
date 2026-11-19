import PNPAbove.WP20SourceQueries
import PNPAbove.WP20CLSem

namespace PNPAbove.WP20
open MIPRE MIPRE.CL MIPRE.Cost Finset
set_option maxRecDepth 8192
set_option maxHeartbeats 1000000

/-- Native CL truncate of Alice, with bit eight suppressed, agrees with
the actual executable source prefix for every legal stage and vector. -/
theorem alice_marginal_bits (j : Nat) (hj : 1 ≤ j) (h9 : j ≤ 9)
    (z : Questions) :
    toBits ((aliceCL.truncate j).eval z) = alicePrefix j (toBits z) := by
  rw [alice_marginal_formula j hj h9]
  interval_cases j <;>
    simp [toBits, alicePrefix, WP18.bobPrefix, List.ofFn_succ]

theorem bob_marginal_bits (j : Nat) (hj : 1 ≤ j) (h9 : j ≤ 9)
    (z : Questions) :
    toBits ((bobCL.truncate j).eval z) = bobPrefix j (toBits z) := by
  rw [bob_marginal_formula j hj h9]
  interval_cases j <;>
    simp [toBits, bobPrefix, WP14.allZero, List.ofFn_succ]

theorem alice_linear_bits (j : Nat) (hj : 1 ≤ j) (h9 : j ≤ 9)
    (u y : Questions) :
    toBits ((aliceCL.mapOfPrefix (j-1) u) y) =
      aliceLinearBits j (toBits y) := by
  rw [alice_linear_formula j hj h9 u y]
  interval_cases j <;>
    simp [toBits, aliceLinearBits, WP18.bobLinearBits,
      WP14.bitmap, WP14.allZero, proj_apply,
      List.ofFn_succ, Finset.mem_singleton] <;>
    split_ifs <;> simp_all

theorem bob_linear_bits (j : Nat) (hj : 1 ≤ j) (h9 : j ≤ 9)
    (u y : Questions) :
    toBits ((bobCL.mapOfPrefix (j-1) u) y) =
      bobLinearBits j (toBits y) := by
  rw [bob_linear_formula j hj h9 u y]
  interval_cases j <;>
    simp [toBits, bobLinearBits, WP18.bobLinearBits,
      WP14.bitmap, WP14.allZero, proj_apply,
      List.ofFn_succ, Finset.mem_singleton] <;>
    split_ifs <;> simp_all

theorem alice_factor_bits (j : Nat) (hj : 1 ≤ j) (h9 : j ≤ 9)
    (u : Questions) :
    indicatorBits (aliceCL.factorOfPrefix (j-1) u) =
      WP14.bitmap (j-1) := by
  rw [alice_factor j hj h9 u]
  simp [indicatorBits, WP14.bitmap, List.ofFn,
    Finset.mem_singleton, Fin.ext_iff]

theorem bob_factor_bits (j : Nat) (hj : 1 ≤ j) (h9 : j ≤ 9)
    (u : Questions) :
    indicatorBits (bobCL.factorOfPrefix (j-1) u) =
      WP14.bitmap (j-1) := by
  rw [bob_factor j hj h9 u]
  simp [indicatorBits, WP14.bitmap, List.ofFn,
    Finset.mem_singleton, Fin.ext_iff]

end PNPAbove.WP20
