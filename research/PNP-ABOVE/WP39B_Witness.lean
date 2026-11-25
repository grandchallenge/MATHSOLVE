import PNPAbove.WP39Native
import PNPAbove.WP38Bridge

namespace PNPAbove.WP39
open MIPRE MIPRE.SAT MIPRE.Cost MIPRE.Cost.PolyTimeFun WP37

/-- This single program never searches a tree or invokes SAT. It simply
enumerates the actual active variables and writes 1 exactly at identifier 0. -/
noncomputable def bitProgram : PolyTimeFun Nat Bool :=
  WP35.eqNatProgram.comp ((PolyTimeFun.id Nat).pair (PolyTimeFun.const (0 : Nat)))

theorem bitProgram_correct (i : Nat) : bitProgram i = plantedBits i := by
  change WP35.eqNatProgram (i,0) = decide (i=0)
  exact WP35.eqNat_correct _ _

noncomputable def witnessProgram : PolyTimeFun Fml BitStr :=
  (PolyTimeFun.map bitProgram).comp WP35.supportProgram

theorem witnessProgram_correct (f : Fml) :
    witnessProgram f = (WP35.support f).map plantedBits := by
  change (PolyTimeFun.map bitProgram) (WP35.supportProgram f) = _
  rw [PolyTimeFun.map_apply,WP35.supportProgram_correct]
  congr 1
  funext i
  exact bitProgram_correct i

theorem witnessProgram_verified (q : Nat) (root : Fin (2^q))
    (cs : List (Constraints q)) :
    WP35.denseWitnessVerifier
      (nativeFormula q root false cs,witnessProgram (nativeFormula q root false cs)) = true := by
  rw [witnessProgram_correct]
  exact WP38.model_bits_verified _ _ (native_plantedBits_satisfies q root cs)

theorem witnessProgram_full (q : Nat) (root : Fin (2^q)) :
    WP35.denseWitnessVerifier
      (fullNative q root false,witnessProgram (fullNative q root false)) = true :=
  witnessProgram_verified q root _

theorem witnessProgram_runs (f : Fml) :
    ∃ t ≤ witnessProgram.timeBound.eval (esize f),
      witnessProgram.code.Runs (encode f) (encode (witnessProgram f)) t :=
  witnessProgram.computes f

theorem edgeIndex_lt_square {n : Nat} (e : Fin n × Fin n) :
    edgeIndex e < n*n := by
  unfold edgeIndex
  calc
    n*e.1.val+e.2.val < n*e.1.val+n := Nat.add_lt_add_left e.2.isLt _
    _ = n*(e.1.val+1) := by ring
    _ ≤ n*n := Nat.mul_le_mul_left _ (by omega)

theorem index_surj_bounded (q i : Nat) (hi : i < 2^q * 2^q + 1) :
    ∃ e : Option (Edges q), index e = i := by
  cases i with
  | zero => exact ⟨none,rfl⟩
  | succ j =>
    have hj : j < 2^q * 2^q := by omega
    have hn : 0 < (2:Nat)^q := by positivity
    refine ⟨some (⟨j / 2^q,Nat.div_lt_of_lt_mul hj⟩,
      ⟨j % 2^q,Nat.mod_lt _ hn⟩),?_⟩
    simp only [index,edgeIndex]
    have he := Nat.mod_add_div j (2^q)
    omega

theorem parityBlock_inputsLt (d m : Nat) (f : Nat → Fml)
    (h : ∀ i, (f i).InputsLt m) (i : Nat) :
    (parityBlock d f i).InputsLt m := by
  induction d generalizing i with
  | zero => exact h i
  | succ d ih => simp [parityBlock,Fml.xor,Fml.InputsLt,ih]

theorem baseConstraint_inputsLt (q : Nat) (root v : Fin (2^q)) :
    (WP37.nativeConstraint q root v).InputsLt (2^q*2^q) := by
  have hp : (nativeParity q v).InputsLt (2^q*2^q) := by
    unfold nativeParity
    apply parityBlock_inputsLt
    intro i
    apply parityBlock_inputsLt
    intro j
    unfold edgeLeaf
    split
    · rename_i h
      exact edgeIndex_lt_square (⟨i,h.1⟩,⟨j,h.2.1⟩)
    · trivial
  unfold WP37.nativeConstraint
  split
  · exact hp
  · exact hp

theorem nativeConstraint_inputsLt (q : Nat) (root : Fin (2^q)) (pinFalse : Bool)
    (c : Constraints q) :
    (nativeConstraint q root pinFalse c).InputsLt (2^q*2^q+1) := by
  cases c with
  | none => cases pinFalse <;> simp [nativeConstraint,Fml.InputsLt]
  | some c =>
    cases c with
    | inl v =>
      change 0 < 2^q*2^q+1 ∧
        ((WP37.nativeConstraint q root v).rename Nat.succ).InputsLt (2^q*2^q+1)
      exact ⟨by omega,(baseConstraint_inputsLt q root v).rename _ (by intro i hi; omega)⟩
    | inr e =>
      change 0 < 2^q*2^q+1 ∧ edgeIndex e+1 < 2^q*2^q+1
      exact ⟨by omega,by have h := edgeIndex_lt_square e; omega⟩

theorem nativeFormula_inputsLt (q : Nat) (root : Fin (2^q)) (pinFalse : Bool)
    (cs : List (Constraints q)) :
    (nativeFormula q root pinFalse cs).InputsLt (2^q*2^q+1) := by
  induction cs with
  | nil => trivial
  | cons c cs ih => exact ⟨nativeConstraint_inputsLt q root pinFalse c,ih⟩

theorem rpn_input_lt (f : Fml) (m i : Nat) (h : f.InputsLt m)
    (hi : Fml.Node.inp i ∈ f.rpn) : i < m := by
  induction f with
  | inp j =>
    have he : i=j := by simpa [Fml.rpn] using hi
    simpa [he,Fml.InputsLt] using h
  | const b => simp [Fml.rpn] at hi
  | and f g ihf ihg =>
    simp only [Fml.rpn,List.mem_append,List.mem_singleton,reduceCtorEq,or_false] at hi
    exact hi.elim (ihf h.1) (ihg h.2)
  | or f g ihf ihg =>
    simp only [Fml.rpn,List.mem_append,List.mem_singleton,reduceCtorEq,or_false] at hi
    exact hi.elim (ihf h.1) (ihg h.2)
  | not f ih =>
    simp only [Fml.rpn,List.mem_append,List.mem_singleton,reduceCtorEq,or_false] at hi
    exact ih h hi

theorem native_active_model_unique (q : Nat) (root : Fin (2^q))
    (a : Nat → Bool) (ha : (fullNative q root false).eval a = true) :
    ∀ i ∈ WP35.support (fullNative q root false), a i = plantedBits i := by
  intro i hi
  have hb := rpn_input_lt (fullNative q root false) _ i
    (nativeFormula_inputsLt q root false _) ((WP35.mem_support _ _).1 hi)
  obtain ⟨e,he⟩ := index_surj_bounded q i hb
  have hr := congrFun ((fullNative_model_iff q root a).1 ha) e
  simpa [readNative,he] using hr

theorem witnessProgram_canonical (q : Nat) (root : Fin (2^q)) :
    WP38.CanonicalWitness (WP35.support (fullNative q root false))
      (fullNative q root false) (witnessProgram (fullNative q root false)) := by
  rw [witnessProgram_correct]
  refine ⟨⟨plantedBits,fullNative_satisfies q root,rfl⟩,?_⟩
  intro a ha
  have he : (WP35.support (fullNative q root false)).map a =
      (WP35.support (fullNative q root false)).map plantedBits :=
    List.map_congr_left (native_active_model_unique q root a ha)
  rw [he]
  exact WP38.preferred_refl _

end PNPAbove.WP39
