import PNPAbove.WP20BellGap

namespace PNPAbove.WP20
open MIPRE MIPRE.CL MIPRE.Cost
set_option maxRecDepth 8192
set_option maxHeartbeats 1000000

/-- Alice's source marginal copies bits 0..min(j-1,7), never bit 8. -/
def aliceMarginalCode (j idxZ : Nat) : Prog :=
  WP18.bobMarginalCode (min j 8) idxZ

/-- Bob's source marginal outputs a literal zero at register 0, then copies
exactly j-1 original raw input bits starting at register 1. -/
def bobMarginalCode (j idxZ : Nat) : Prog :=
  if j ≤ 1 then .const WP14.sourceZero
  else .elim idxZ (.const WP14.sourceZero)
    (.cons (.const (encode false))
      (WP14.copyPrefixPad (j-1) (9-j) 1))

/-- Alice's stage-9 linear map is exactly zero; all other stages are ordinary
singleton projections of the original raw input. -/
def aliceLinearCode (j idxY : Nat) : Prog :=
  if j = 9 then .const WP14.sourceZero
  else WP18.bobLinearCode j idxY

/-- Bob's first stage is zero; all later stages are ordinary singleton
linear projections. Registers remain occupied at every stage. -/
def bobLinearCode (j idxY : Nat) : Prog :=
  if j = 1 then .const WP14.sourceZero
  else WP18.bobLinearCode j idxY

/-- Original source query compiler with two genuinely different player
question maps, built only from existing original Cost.Prog constructs. -/
def cyclicKindCode (kind offset : Nat) : Prog :=
  if kind = 0 then .const (encode (9 : Nat))
  else
    .elim (1+offset) .nil
      (.elim 1 .nil
        (.elim 1 .nil
          (WP14.numeralDispatch 5 2 0 [] (fun j off =>
            if kind = 3 then .const (WP14.sourceBitmap (j-1))
            else .elim (off+4)
              (if kind = 1 then aliceMarginalCode j off
               else if kind = 2 then aliceLinearCode j (off+1)
               else .nil)
              (if kind = 1 then bobMarginalCode j (off+2)
               else if kind = 2 then bobLinearCode j (off+3)
               else .nil)))))

def cyclicSamplerProg : Prog :=
  .elim 0 .nil
    (.elim 1 .nil (WP14.numeralDispatch 4 0 0 [] cyclicKindCode))

/- Each of the following actually evaluates the original native source DSL
at a representative input, and is not substituted by a custom interpreter. -/
#guard WP12.evalValue cyclicSamplerProg
  [encode ((3:Nat), Sampler.Query.dimension)] == encode (9:Nat)

#guard WP12.evalValue cyclicSamplerProg
  [encode ((3:Nat), Sampler.Query.marginal Player.alice 9
    ([true,false,false,false,false,false,false,false,true] : BitStr))] ==
    encode ([true,false,false,false,false,false,false,false,false] : BitStr)

#guard WP12.evalValue cyclicSamplerProg
  [encode ((3:Nat), Sampler.Query.marginal Player.bob 9
    ([true,false,false,false,false,false,false,false,true] : BitStr))] ==
    encode ([false,false,false,false,false,false,false,false,true] : BitStr)

#guard WP12.evalValue cyclicSamplerProg
  [encode ((3:Nat), Sampler.Query.linear Player.alice 9
    (WP14.allZero)
    ([false,false,false,false,false,false,false,false,true] : BitStr))] ==
    WP14.sourceZero

#guard WP12.evalValue cyclicSamplerProg
  [encode ((3:Nat), Sampler.Query.linear Player.bob 1
    (WP14.allZero)
    ([true,false,false,false,false,false,false,false,false] : BitStr))] ==
    WP14.sourceZero

#guard WP12.evalValue cyclicSamplerProg
  [encode ((3:Nat), Sampler.Query.factor Player.alice 9 WP14.allZero)] ==
    WP14.sourceBitmap 8

#guard WP14.scopedB 1 cyclicSamplerProg
#guard WP14.loopFreeB cyclicSamplerProg
#guard WP14.readBuildB cyclicSamplerProg

theorem cyclicSamplerProg_closed : cyclicSamplerProg.WellScoped 1 := by
  exact WP14.scopedB_sound 1 cyclicSamplerProg (by decide)

theorem cyclicSamplerProg_loopFree : WP11.LoopFree cyclicSamplerProg := by
  exact WP14.loopFreeB_sound cyclicSamplerProg (by decide)

theorem cyclicSamplerProg_readBuild : WP14.ReadBuild cyclicSamplerProg := by
  exact WP14.readBuildB_sound cyclicSamplerProg (by decide)

theorem cyclicSamplerProg_halts_raw (d : Data) :
    ∃ r t, Eval [d] cyclicSamplerProg r t :=
  WP11.loopfree_terminates _ cyclicSamplerProg_loopFree [d]

theorem cyclic_sourceRuns {d r : Data}
    (h : WP12.evalValue cyclicSamplerProg [d] = r) :
    ∃ t, cyclicSamplerProg.Runs d r t := by
  obtain ⟨t,ht⟩ := WP12.evalValue_sound cyclicSamplerProg [d]
    cyclicSamplerProg_loopFree
  exact ⟨t, h ▸ ht⟩

theorem cyclic_time_bound_raw (n : Nat) (d : Data) :
    ∃ r t, Eval [Data.cons (encode n) d] cyclicSamplerProg r t ∧
      t ≤ WP14.staticBuildCost cyclicSamplerProg *
        ((Data.cons (encode n) d).size + 1) := by
  obtain ⟨r,t,hr⟩ := cyclicSamplerProg_halts_raw (.cons (encode n) d)
  refine ⟨r,t,hr,?_⟩
  have hi : 1 ≤ (Data.cons (encode n) d).size := Data.size_pos _
  exact WP14.readBuild_eval_bound _ hi hr cyclicSamplerProg_readBuild
    (by
      intro x hx
      simp only [List.mem_singleton] at hx
      subst x
      rfl)

#eval WP14.staticBuildCost cyclicSamplerProg

end PNPAbove.WP20
