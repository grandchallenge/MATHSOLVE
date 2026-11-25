import PNPAbove.WP18Sampler

namespace PNPAbove.WP18
open MIPRE MIPRE.CL MIPRE.Cost

/-- The full nine-stage Bob stream copies the first j bits without a gate. -/
def bobPrefix (j : Nat) (bs : BitStr) : BitStr :=
  bs.take j ++ List.replicate (9-j) false

/-- Bob's stage map depends on the current input bit, not on the prefix. -/
def bobLinearBits (j : Nat) (y : BitStr) : BitStr :=
  if y.getD (j-1) false then WP14.bitmap (j-1) else WP14.allZero

/-- Original source recursion computes a Bob marginal for every legal j and
every 9-bit input, not only a finite list of examples. -/
theorem bobMarginalCode_value (j idx : Nat) (env : Env) (bs : BitStr)
    (hj : 1 ≤ j) (hj9 : j ≤ 9) (hlen : bs.length = 9)
    (h : env.get idx = encode bs) :
    WP12.evalValue (bobMarginalCode j idx) env = encode (bobPrefix j bs) := by
  obtain ⟨k, rfl⟩ : ∃ k, j = k+1 := ⟨j-1, by omega⟩
  cases bs with
  | nil => simp at hlen
  | cons b bs =>
      have hk' : k ≤ bs.length := by
        simp only [List.length_cons] at hlen
        omega
      have hr := WP14.copyPrefixPad_value k (9-(k+1)) 1
        (encode b :: encode bs :: env) bs (by rfl) hk'
      simp only [bobMarginalCode, if_neg (Nat.succ_ne_zero k),
        WP12.evalValue, h,
        show (encode (b :: bs) : Data) = .cons (encode b) (encode bs) from rfl]
      change Data.cons (encode b)
        (WP12.evalValue (WP14.copyPrefixPad k (9-(k+1)) 1)
          (encode b :: encode bs :: env)) =
        Data.cons (encode b) (encode (bs.take k ++ List.replicate (9-(k+1)) false))
      exact congrArg (Data.cons (encode b)) hr

/-- Original binary-cell source inspector for the unconditional linear stage. -/
theorem bobLinearCode_value (j idx : Nat) (env : Env) (y : BitStr)
    (hj : 1 ≤ j) (hj9 : j ≤ 9) (hy : y.length = 9)
    (h : env.get idx = encode y) :
    WP12.evalValue (bobLinearCode j idx) env = encode (bobLinearBits j y) := by
  have hj0 : j ≠ 0 := by omega
  have hm := WP14.maskIfBit_value idx (j-1) (WP14.sourceBitmap (j-1))
    env y h (by omega)
  simpa only [bobLinearCode, if_neg hj0, bobLinearBits, WP14.encode_if,
      WP14.sourceBitmap, WP14.sourceZero] using hm

/-- Original CL semantics: every truncated stage retains its input coordinate
iff its index is below j. The maps truly have nine nonempty factors. -/
theorem bob_marginal_formula (j : Nat) (hj : 1 ≤ j) (hj9 : j ≤ 9)
    (z : Fin 9 → 𝔽₂) :
    (bobNineCL.truncate j).eval z =
      (fun i => if i.val < j then z i else 0) := by
  interval_cases j <;> funext i <;> fin_cases i <;>
    simp [bobNineCL, WP14.tailChain, WP14.tailCoordinates,
      RegLinear.id_apply, proj_apply, Finset.mem_singleton, apply_ite]

/-- Each Bob stage has an unconditional singleton linear projection. -/
theorem bob_linear_formula (j : Nat) (hj : 1 ≤ j) (hj9 : j ≤ 9)
    (u y : Fin 9 → 𝔽₂) :
    (bobNineCL.mapOfPrefix (j-1) u) y =
      proj ({⟨j-1, by omega⟩} : Finset (Fin 9)) y := by
  interval_cases j <;>
    simp [bobNineCL, WP14.tailChain, WP14.tailCoordinates,
      RegLinear.id_apply, proj_apply, Finset.mem_singleton]

end PNPAbove.WP18
