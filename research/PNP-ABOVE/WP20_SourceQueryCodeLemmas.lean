import PNPAbove.WP20SourceProg

namespace PNPAbove.WP20
open MIPRE MIPRE.CL MIPRE.Cost Finset
set_option maxRecDepth 8192
set_option maxHeartbeats 1000000

/-- The exact original-data Alice prefix: copy at most eight coordinates
and supply literal zero padding for the ignored ninth coordinate. -/
def alicePrefix (j : Nat) (z : BitStr) : BitStr :=
  WP18.bobPrefix (min j 8) z

/-- The exact original-data Bob prefix: literal false first coordinate,
then the first j-1 input suffix coordinates, then zero padding. -/
def bobPrefix (j : Nat) (z : BitStr) : BitStr :=
  if j ≤ 1 then WP14.allZero
  else false :: ((z.drop 1).take (j-1) ++ List.replicate (9-j) false)

def aliceLinearBits (j : Nat) (y : BitStr) : BitStr :=
  if j = 9 then WP14.allZero else WP18.bobLinearBits j y

def bobLinearBits (j : Nat) (y : BitStr) : BitStr :=
  if j = 1 then WP14.allZero else WP18.bobLinearBits j y

/-- Unconditional Alice source copying, stopping before bit eight. -/
theorem aliceMarginalCode_value (j idx : Nat) (env : Env) (z : BitStr)
    (hj : 1 ≤ j) (hj9 : j ≤ 9) (hz : z.length = 9)
    (h : env.get idx = encode z) :
    WP12.evalValue (aliceMarginalCode j idx) env = encode (alicePrefix j z) := by
  unfold aliceMarginalCode alicePrefix
  exact WP18.bobMarginalCode_value (min j 8) idx env z
    (by omega) (by omega) hz h

/-- Original source recursion for Bob's zero-first-bit marginal, proved
for every valid j and every length-nine raw input. -/
theorem bobMarginalCode_value (j idx : Nat) (env : Env) (z : BitStr)
    (hj : 1 ≤ j) (hj9 : j ≤ 9) (hz : z.length = 9)
    (h : env.get idx = encode z) :
    WP12.evalValue (bobMarginalCode j idx) env = encode (bobPrefix j z) := by
  by_cases hj1 : j = 1
  · subst j
    simp [bobMarginalCode, bobPrefix, WP14.sourceZero, WP12.evalValue]
  · have hjgt : 1 < j := by omega
    obtain ⟨k,rfl⟩ : ∃ k, j = k+1 := ⟨j-1, by omega⟩
    cases z with
    | nil => simp at hz
    | cons b bs =>
        have hk' : k ≤ bs.length := by
          simp only [List.length_cons] at hz
          omega
        have hr := WP14.copyPrefixPad_value k (9-(k+1)) 1
          (encode b :: encode bs :: env) bs (by rfl) hk'
        simp only [bobMarginalCode, if_neg (show ¬(k+1 ≤ 1) by omega),
          WP12.evalValue, h,
          show (encode (b :: bs) : Data) = .cons (encode b) (encode bs) from rfl]
        change Data.cons (encode false)
          (WP12.evalValue (WP14.copyPrefixPad k (9-(k+1)) 1)
            (encode b :: encode bs :: env)) =
          encode (bobPrefix (k+1) (b::bs))
        rw [hr]
        simp [bobPrefix, show ¬(k+1 ≤ 1) by omega]
        rfl

theorem aliceLinearCode_value (j idx : Nat) (env : Env) (y : BitStr)
    (hj : 1 ≤ j) (hj9 : j ≤ 9) (hy : y.length = 9)
    (h : env.get idx = encode y) :
    WP12.evalValue (aliceLinearCode j idx) env = encode (aliceLinearBits j y) := by
  by_cases hj9' : j = 9
  · simp [aliceLinearCode, aliceLinearBits, hj9', WP14.sourceZero, WP12.evalValue]
  · simpa only [aliceLinearCode, aliceLinearBits, if_neg hj9'] using
      WP18.bobLinearCode_value j idx env y hj hj9 hy h

theorem bobLinearCode_value (j idx : Nat) (env : Env) (y : BitStr)
    (hj : 1 ≤ j) (hj9 : j ≤ 9) (hy : y.length = 9)
    (h : env.get idx = encode y) :
    WP12.evalValue (bobLinearCode j idx) env = encode (bobLinearBits j y) := by
  by_cases hj1 : j = 1
  · simp [bobLinearCode, bobLinearBits, hj1, WP14.sourceZero, WP12.evalValue]
  · simpa only [bobLinearCode, bobLinearBits, if_neg hj1] using
      WP18.bobLinearCode_value j idx env y hj hj9 hy h

/-- The actual source programme handles dimensions and factors for every
index, stage, and player, rather than only the #guard examples. -/
theorem eval_dimension_all (n : Nat) :
    WP12.evalValue cyclicSamplerProg [encode (n, Sampler.Query.dimension)] =
      encode (9 : Nat) := by
  have hfind : (List.range 10).find? (fun j => (Nat.bits j).isEmpty) = some 0 := by decide
  simp [cyclicSamplerProg, cyclicKindCode, WP14.numeralDispatch,
    WP12.evalValue, Sampler.Query.toTuple, SizedEncoding.encode, Data.ofList, hfind]

theorem eval_factor_all (n : Nat) (w : Player) (j : Nat) (u : BitStr)
    (hj : 1 ≤ j) (hj9 : j ≤ 9) :
    WP12.evalValue cyclicSamplerProg
      [encode (n, Sampler.Query.factor w j u)] = WP14.sourceBitmap (j-1) := by
  cases w <;>
    interval_cases j <;>
    simp [cyclicSamplerProg, cyclicKindCode, WP14.numeralDispatch,
      WP12.evalValue, Sampler.Query.toTuple, SizedEncoding.encode,
      Data.ofList, Data.ofBool]

end PNPAbove.WP20
