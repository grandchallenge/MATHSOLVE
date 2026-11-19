import PNPAbove.WP20SourceProg

namespace PNPAbove.WP20
open MIPRE MIPRE.CL MIPRE.Cost Finset
set_option maxRecDepth 8192
set_option maxHeartbeats 1000000

/-- All nine original Alice marginals, with the final register suppressed. -/
theorem alice_marginal_formula (j : Nat) (hj : 1 ≤ j) (hj9 : j ≤ 9)
    (z : Questions) :
    (aliceCL.truncate j).eval z =
      (fun i => if i.val < min j 8 then z i else 0) := by
  interval_cases j <;> funext i <;> fin_cases i <;>
    simp [aliceCL, maskedTail, WP14.tailCoordinates, RegLinear.id_apply,
      proj_apply, Finset.mem_singleton, apply_ite]

/-- All nine original Bob marginals, with the first register suppressed. -/
theorem bob_marginal_formula (j : Nat) (hj : 1 ≤ j) (hj9 : j ≤ 9)
    (z : Questions) :
    (bobCL.truncate j).eval z =
      (fun i => if i.val < j ∧ i ≠ 0 then z i else 0) := by
  interval_cases j <;> funext i <;> fin_cases i <;>
    simp [bobCL, WP14.tailChain, WP14.tailCoordinates,
      RegLinear.id_apply, proj_apply, Finset.mem_singleton, apply_ite]

/-- All nine original Alice stage maps, including the ninth zero map. -/
theorem alice_linear_formula (j : Nat) (hj : 1 ≤ j) (hj9 : j ≤ 9)
    (u y : Questions) :
    (aliceCL.mapOfPrefix (j-1) u) y =
      if j = 9 then 0
      else proj ({⟨j-1, by omega⟩} : Finset (Fin 9)) y := by
  interval_cases j <;>
    simp [aliceCL, maskedTail, WP14.tailCoordinates, RegLinear.id_apply,
      proj_apply, Finset.mem_singleton]

/-- All nine original Bob stage maps, including the first zero map. -/
theorem bob_linear_formula (j : Nat) (hj : 1 ≤ j) (hj9 : j ≤ 9)
    (u y : Questions) :
    (bobCL.mapOfPrefix (j-1) u) y =
      if j = 1 then 0
      else proj ({⟨j-1, by omega⟩} : Finset (Fin 9)) y := by
  interval_cases j <;>
    simp [bobCL, WP14.tailChain, WP14.tailCoordinates, RegLinear.id_apply,
      proj_apply, Finset.mem_singleton]

end PNPAbove.WP20
