import PNPAbove.WP18

namespace PNPAbove.WP18
open MIPRE MIPRE.CL MIPRE.Cost

/-- Original source program for Bob's unconditional prefix copy. -/
def bobMarginalCode (j idxZ : Nat) : Prog :=
  if j = 0 then .const WP14.sourceZero
  else .elim idxZ (.const WP14.sourceZero)
    (.cons (.var 0) (WP14.copyPrefixPad (j-1) (9-j) 1))

/-- Original source program for Bob's ninth-stage singleton linear map. -/
def bobLinearCode (j idxY : Nat) : Prog :=
  if j = 0 then .const WP14.sourceZero
  else WP14.maskIfBit idxY (j-1) (WP14.sourceBitmap (j-1))

/-- Read the actual encoded Player at source environment position off+4.
The true (Bob) branch introduces two source variables; they are accounted
for by explicit +2 shifts of the original vector indices. -/
def asymmetricKindCode (kind offset : Nat) : Prog :=
  if kind = 0 then .const (encode (9 : Nat))
  else
    .elim (1+offset) .nil
      (.elim 1 .nil
        (.elim 1 .nil
          (WP14.numeralDispatch 5 2 0 [] (fun j off =>
            if kind = 3 then .const (WP14.sourceBitmap (j-1))
            else .elim (off+4)
              (if kind = 1 then WP14.marginalCode j off
               else if kind = 2 then WP14.linearCode j off (off+1)
               else .nil)
              (if kind = 1 then bobMarginalCode j (off+2)
               else if kind = 2 then bobLinearCode j (off+3)
               else .nil)))))

/-- The original source query compiler with distinct Alice/Bob branches. -/
def asymmetricSamplerProg : Prog :=
  .elim 0 .nil
    (.elim 1 .nil (WP14.numeralDispatch 4 0 0 [] asymmetricKindCode))

#guard WP12.evalValue asymmetricSamplerProg
  [encode ((3:Nat), Sampler.Query.dimension)] == encode (9:Nat)

#guard WP12.evalValue asymmetricSamplerProg
  [encode ((3:Nat), Sampler.Query.marginal Player.alice 9
    ([false,true,false,false,false,false,false,false,false] : BitStr))] ==
    encode WP14.allZero

#guard WP12.evalValue asymmetricSamplerProg
  [encode ((3:Nat), Sampler.Query.marginal Player.bob 9
    ([false,true,false,false,false,false,false,false,false] : BitStr))] ==
    encode ([false,true,false,false,false,false,false,false,false] : BitStr)

#guard WP12.evalValue asymmetricSamplerProg
  [encode ((3:Nat), Sampler.Query.linear Player.bob 2
    ([false,false,false,false,false,false,false,false,false] : BitStr)
    ([false,true,false,false,false,false,false,false,false] : BitStr))] ==
    WP14.sourceBitmap 1

#guard WP12.evalValue asymmetricSamplerProg
  [encode ((3:Nat), Sampler.Query.factor Player.bob 8
    ([false,false,false,false,false,false,false,false,false] : BitStr))] ==
    WP14.sourceBitmap 7


/-! ### Original-source scoping, halting and per-query runtime -/

#guard WP14.scopedB 1 asymmetricSamplerProg
#guard WP14.loopFreeB asymmetricSamplerProg
#guard WP14.readBuildB asymmetricSamplerProg

set_option maxRecDepth 8192 in
theorem asymmetricSamplerProg_closed : asymmetricSamplerProg.WellScoped 1 := by
  exact WP14.scopedB_sound 1 asymmetricSamplerProg (by decide)

set_option maxRecDepth 8192 in
theorem asymmetricSamplerProg_loopFree : WP11.LoopFree asymmetricSamplerProg := by
  exact WP14.loopFreeB_sound asymmetricSamplerProg (by decide)

set_option maxRecDepth 8192 in
theorem asymmetricSamplerProg_readBuild : WP14.ReadBuild asymmetricSamplerProg := by
  exact WP14.readBuildB_sound asymmetricSamplerProg (by decide)

/-- Termination on every original source query, including malformed raw data. -/
theorem asymmetricSamplerProg_halts_raw (d : Data) :
    ∃ r t, Eval [d] asymmetricSamplerProg r t :=
  WP11.loopfree_terminates _ asymmetricSamplerProg_loopFree [d]

/-- Native evaluation and operational semantics, with no oracle substitution. -/
theorem sourceRuns {d r : Data}
    (h : WP12.evalValue asymmetricSamplerProg [d] = r) :
    ∃ t, asymmetricSamplerProg.Runs d r t := by
  obtain ⟨t, ht⟩ := WP12.evalValue_sound asymmetricSamplerProg [d]
    asymmetricSamplerProg_loopFree
  exact ⟨t, h ▸ ht⟩

/-- Uniform polynomial degree one runtime on all raw source data values. -/
theorem asymmetric_time_bound_raw (n : Nat) (d : Data) :
    ∃ r t, Eval [Data.cons (encode n) d] asymmetricSamplerProg r t ∧
      t ≤ WP14.staticBuildCost asymmetricSamplerProg *
        ((Data.cons (encode n) d).size + 1) := by
  obtain ⟨r, t, hr⟩ := asymmetricSamplerProg_halts_raw (.cons (encode n) d)
  refine ⟨r,t,hr,?_⟩
  have hinput : 1 ≤ (Data.cons (encode n) d).size := Data.size_pos _
  exact WP14.readBuild_eval_bound _ hinput hr asymmetricSamplerProg_readBuild
    (by
      intro x hx
      simp only [List.mem_singleton] at hx
      subst x
      rfl)

#eval WP14.staticBuildCost asymmetricSamplerProg

end PNPAbove.WP18
