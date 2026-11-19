import PNPAbove.WP20SourceSemantics

namespace PNPAbove.WP20
open MIPRE MIPRE.CL MIPRE.Cost
set_option maxRecDepth 8192
set_option maxHeartbeats 1000000

/-- Every valid dimension query is answered by the real original Cost.Prog. -/
theorem all_dimension_queries (n : Nat) :
    WP12.evalValue cyclicSamplerProg [encode (n, Sampler.Query.dimension)] =
      encode (9 : Nat) := eval_dimension_all n

/-- Exact quantified factor-query interpreter, either player, any stage. -/
theorem all_factor_queries (n : Nat) (w : Player) (j : Nat) (u : BitStr)
    (hj : 1 ≤ j) (h9 : j ≤ 9) :
    WP12.evalValue cyclicSamplerProg
      [encode (n, Sampler.Query.factor w j u)] =
        WP14.sourceBitmap (j-1) :=
  eval_factor_all n w j u hj h9

/-- Real source interpreter correctness: ALL nine stages and BOTH labels,
not a finite sample of successful raw query encodings. -/
theorem all_marginal_queries (n : Nat) (w : Player) (j : Nat) (z : BitStr)
    (hj : 1 ≤ j) (h9 : j ≤ 9) (hz : z.length = 9) :
    WP12.evalValue cyclicSamplerProg
      [encode (n, Sampler.Query.marginal w j z)] =
        encode (match w with
          | .alice => alicePrefix j z
          | .bob => bobPrefix j z) := by
  cases w
  · interval_cases j <;>
      simp [cyclicSamplerProg, cyclicKindCode, WP14.numeralDispatch,
        WP12.evalValue, Sampler.Query.toTuple, SizedEncoding.encode,
        Data.ofList, Data.ofBool]
    all_goals apply aliceMarginalCode_value _ _ _ _ (by omega) (by omega) hz (by rfl)
  · interval_cases j <;>
      simp [cyclicSamplerProg, cyclicKindCode, WP14.numeralDispatch,
        WP12.evalValue, Sampler.Query.toTuple, SizedEncoding.encode,
        Data.ofList, Data.ofBool]
    all_goals apply bobMarginalCode_value _ _ _ _ (by omega) (by omega) hz (by rfl)

/-- Every valid stage linear query, for either player and arbitrary supplied
original nine-bit prefix and test vector, has exact source semantics. -/
theorem all_linear_queries (n : Nat) (w : Player) (j : Nat) (u y : BitStr)
    (hj : 1 ≤ j) (h9 : j ≤ 9) (hu : u.length = 9) (hy : y.length = 9) :
    WP12.evalValue cyclicSamplerProg
      [encode (n, Sampler.Query.linear w j u y)] =
        encode (match w with
          | .alice => aliceLinearBits j y
          | .bob => bobLinearBits j y) := by
  cases w
  · interval_cases j <;>
      simp [cyclicSamplerProg, cyclicKindCode, WP14.numeralDispatch,
        WP12.evalValue, Sampler.Query.toTuple, SizedEncoding.encode,
        Data.ofList, Data.ofBool]
    all_goals apply aliceLinearCode_value _ _ _ _ (by omega) (by omega) hy (by rfl)
  · interval_cases j <;>
      simp [cyclicSamplerProg, cyclicKindCode, WP14.numeralDispatch,
        WP12.evalValue, Sampler.Query.toTuple, SizedEncoding.encode,
        Data.ofList, Data.ofBool]
    all_goals apply bobLinearCode_value _ _ _ _ (by omega) (by omega) hy (by rfl)

end PNPAbove.WP20
