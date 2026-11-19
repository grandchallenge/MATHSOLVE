import PNPAbove.WP21Prog

namespace PNPAbove.WP21
open MIPRE MIPRE.Cost

theorem readBit_scoped (idx k n : Nat) (hi : idx < n) :
    (readBit idx k).WellScoped n := by
  induction k generalizing idx n with
  | zero =>
      simp [readBit, Prog.WellScoped, hi]
  | succ k ih =>
      simp only [readBit, Prog.WellScoped]
      exact ⟨hi, by simp [Prog.WellScoped], ih 1 (n + 2) (by omega)⟩

theorem truthTree_scoped (is : List Nat) (bits : List Bool)
    (offset n : Nat) (hi : ∀ i ∈ is, offset + i < n) :
    (truthTree is bits offset).WellScoped n := by
  induction is generalizing bits offset n with
  | nil => simp [truthTree, Prog.WellScoped]
  | cons i is ih =>
      simp only [truthTree, Prog.WellScoped]
      refine ⟨hi i (by simp), ?_, ?_⟩
      · apply ih
        intro j hj
        exact hi j (by simp [hj])
      · apply ih
        intro j hj
        have := hi j (by simp [hj])
        omega

theorem requireBits_scoped (idx k n : Nat) (s : Prog)
    (hi : idx < n) (hs : s.WellScoped (n + 3)) :
    (requireBits idx k s).WellScoped n := by
  simp [requireBits, Prog.WellScoped, reject,
    WP08.checkBits_wellScoped k idx n hi, hs]

theorem readAndDecide_scoped : readAndDecide.WellScoped 23 := by
  simp only [readAndDecide, Prog.WellScoped]
  refine ⟨readBit_scoped 16 0 23 (by omega), ?_⟩
  refine ⟨readBit_scoped 17 8 24 (by omega), ?_⟩
  refine ⟨readBit_scoped 16 0 25 (by omega), ?_⟩
  refine ⟨readBit_scoped 17 8 26 (by omega), ?_⟩
  refine ⟨readBit_scoped 16 0 27 (by omega), ?_⟩
  refine ⟨readBit_scoped 18 0 28 (by omega), ?_⟩
  apply truthTree_scoped
  intro i hi
  simp at hi
  omega

theorem deciderProg_scoped : maskedParityDeciderProg.WellScoped 1 := by
  simp only [maskedParityDeciderProg, Prog.WellScoped]
  refine ⟨by omega, by simp [reject, Prog.WellScoped], ?_⟩
  refine ⟨by omega, by simp [reject, Prog.WellScoped], ?_⟩
  refine ⟨by omega, by simp [reject, Prog.WellScoped], ?_⟩
  refine ⟨by omega, by simp [reject, Prog.WellScoped], ?_⟩
  refine ⟨by omega, by simp [reject, Prog.WellScoped], ?_⟩
  apply requireBits_scoped 4 9 11
  · omega
  apply requireBits_scoped 5 9 14
  · omega
  apply requireBits_scoped 6 1 17
  · omega
  apply requireBits_scoped 10 1 20
  · omega
  exact readAndDecide_scoped

def maskedParityDecider : MIPRE.Decider :=
  ⟨maskedParityDeciderProg, deciderProg_scoped⟩

end PNPAbove.WP21
