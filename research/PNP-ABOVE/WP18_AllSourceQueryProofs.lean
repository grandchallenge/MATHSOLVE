import PNPAbove.WP18Final

namespace PNPAbove.WP18
open MIPRE MIPRE.CL MIPRE.Cost
set_option maxRecDepth 8192
set_option maxHeartbeats 1000000

/-! ### Quantified original-cost-program source query semantics -/

theorem eval_dimension_all (n : Nat) :
    WP12.evalValue asymmetricSamplerProg [encode (n, Sampler.Query.dimension)] =
      encode (9 : Nat) := by
  have hfind : (List.range 10).find? (fun j => (Nat.bits j).isEmpty) = some 0 := by decide
  simp [asymmetricSamplerProg, asymmetricKindCode, WP14.numeralDispatch,
    WP12.evalValue, Sampler.Query.toTuple, SizedEncoding.encode, Data.ofList, hfind]

theorem eval_factor_all (n : Nat) (w : Player) (j : Nat) (u : BitStr)
    (hj : 1 ≤ j) (hj9 : j ≤ 9) :
    WP12.evalValue asymmetricSamplerProg
      [encode (n, Sampler.Query.factor w j u)] = WP14.sourceBitmap (j-1) := by
  cases w <;>
    interval_cases j <;>
    simp [asymmetricSamplerProg, asymmetricKindCode, WP14.numeralDispatch,
      WP12.evalValue, Sampler.Query.toTuple, SizedEncoding.encode,
      Data.ofList, Data.ofBool]

/-- A single query theorem, valid for every length-nine marginal and both
player labels, using the actual original source program. -/
theorem eval_marginal_all (n : Nat) (w : Player) (j : Nat) (z : BitStr)
    (hj : 1 ≤ j) (hj9 : j ≤ 9) (hz : z.length = 9) :
    WP12.evalValue asymmetricSamplerProg
      [encode (n, Sampler.Query.marginal w j z)] =
        encode (match w with
          | .alice => WP14.gatedPrefix j z
          | .bob => bobPrefix j z) := by
  cases w
  · interval_cases j <;>
      simp [asymmetricSamplerProg, asymmetricKindCode, WP14.numeralDispatch,
        WP12.evalValue, Sampler.Query.toTuple, SizedEncoding.encode,
        Data.ofList, Data.ofBool]
    all_goals apply WP14.marginalCode_value _ _ _ _ (by omega) (by omega) hz (by rfl)
  · interval_cases j <;>
      simp [asymmetricSamplerProg, asymmetricKindCode, WP14.numeralDispatch,
        WP12.evalValue, Sampler.Query.toTuple, SizedEncoding.encode,
        Data.ofList, Data.ofBool]
    all_goals apply bobMarginalCode_value _ _ _ _ (by omega) (by omega) hz (by rfl)

/-- All valid original stage-linear source queries are player-specific. -/
theorem eval_linear_all (n : Nat) (w : Player) (j : Nat) (u y : BitStr)
    (hj : 1 ≤ j) (hj9 : j ≤ 9) (hu : u.length = 9) (hy : y.length = 9) :
    WP12.evalValue asymmetricSamplerProg
      [encode (n, Sampler.Query.linear w j u y)] =
        encode (match w with
          | .alice => WP14.gatedLinear j u y
          | .bob => bobLinearBits j y) := by
  cases w
  · interval_cases j <;>
      simp [asymmetricSamplerProg, asymmetricKindCode, WP14.numeralDispatch,
        WP12.evalValue, Sampler.Query.toTuple, SizedEncoding.encode,
        Data.ofList, Data.ofBool]
    all_goals apply WP14.linearCode_value _ _ _ _ _ _ (by omega) (by omega) hu hy (by rfl) (by rfl)
  · interval_cases j <;>
      simp [asymmetricSamplerProg, asymmetricKindCode, WP14.numeralDispatch,
        WP12.evalValue, Sampler.Query.toTuple, SizedEncoding.encode,
        Data.ofList, Data.ofBool]
    all_goals apply bobLinearCode_value _ _ _ _ (by omega) (by omega) hy (by rfl)

end PNPAbove.WP18
