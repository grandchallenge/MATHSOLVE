import PNPAbove.WP21Verifier

namespace PNPAbove.WP21
open MIPRE MIPRE.Cost

set_option maxRecDepth 8192
set_option maxHeartbeats 1000000

def ReadLet : Prog → Prop
  | .var _ | .nil | .const _ => True
  | .elim _ a b | .let_ a b => ReadLet a ∧ ReadLet b
  | .cons _ _ | .loop _ => False

def readLetB : Prog → Bool
  | .var _ | .nil | .const _ => true
  | .elim _ a b | .let_ a b => readLetB a && readLetB b
  | .cons _ _ | .loop _ => false

theorem readLetB_sound (p : Prog) (h : readLetB p = true) : ReadLet p := by
  induction p with
  | var i => trivial
  | nil => trivial
  | const d => trivial
  | cons a b ia ib => simp [readLetB] at h
  | elim i a b ia ib =>
      simp only [readLetB, Bool.and_eq_true] at h
      exact ⟨ia h.1, ib h.2⟩
  | let_ a b ia ib =>
      simp only [readLetB, Bool.and_eq_true] at h
      exact ⟨ia h.1, ib h.2⟩
  | loop b ih => simp [readLetB] at h

def literalCeiling : Prog → Nat
  | .var _ | .nil => 1
  | .const d => d.size
  | .elim _ a b | .let_ a b => max (literalCeiling a) (literalCeiling b)
  | .cons _ _ | .loop _ => 1

def inspectionSteps : Prog → Nat
  | .var _ | .nil | .const _ => 1
  | .elim _ a b => 1 + max (inspectionSteps a) (inspectionSteps b)
  | .let_ a b => 1 + inspectionSteps a + inspectionSteps b
  | .cons _ _ | .loop _ => 1

theorem inspectLet_eval_bound (B : Nat) (hB : 1 ≤ B) :
  ∀ {env : Env} {p : Prog} {r : Data} {t : Nat},
    Eval env p r t → ReadLet p →
    literalCeiling p ≤ B →
    (∀ d, d ∈ env → d.size ≤ B) →
    r.size ≤ B ∧ t ≤ inspectionSteps p * (B + 1) := by
  intro env p r t he
  induction he with
  | var env i =>
      intro hp hc henv
      have hh := WP13.env_get_size_le B hB env henv i
      constructor
      · exact hh
      · simp only [inspectionSteps, one_mul]
        omega
  | nil env =>
      intro hp hc henv
      simp [inspectionSteps, hB]
  | const env d =>
      intro hp hc henv
      simp only [literalCeiling] at hc
      constructor
      · exact hc
      · simp only [inspectionSteps, one_mul]
        omega
  | cons e1 e2 ih1 ih2 =>
      intro hp
      cases hp
  | elim_nil hget he ih =>
      rename_i e i pn pc rr tt
      intro hp hc henv
      have hchild : literalCeiling pn ≤ B := by
        simp only [literalCeiling] at hc
        omega
      obtain ⟨hs,ht⟩ := ih hp.1 hchild henv
      refine ⟨hs, ?_⟩
      simp only [inspectionSteps]
      have hmax : inspectionSteps pn ≤ max (inspectionSteps pn) (inspectionSteps pc) :=
        Nat.le_max_left _ _
      have hmul := Nat.mul_le_mul_right (B + 1) hmax
      rw [Nat.add_mul, one_mul]
      omega
  | elim_cons hget he ih =>
      rename_i e i pn pc aa bb rr tt
      intro hp hc henv
      have hchild : literalCeiling pc ≤ B := by
        simp only [literalCeiling] at hc
        omega
      have hwhole : (Data.cons aa bb).size ≤ B := by
        rw [← hget]
        exact WP13.env_get_size_le B hB e henv _
      have henv' : ∀ d, d ∈ (aa :: bb :: e) → d.size ≤ B := by
        intro d hd
        simp only [List.mem_cons] at hd
        rcases hd with rfl | rfl | he
        · simp only [Data.size_cons] at hwhole
          omega
        · simp only [Data.size_cons] at hwhole
          omega
        · exact henv d he
      obtain ⟨hs,ht⟩ := ih hp.2 hchild henv'
      refine ⟨hs, ?_⟩
      simp only [inspectionSteps]
      have hmax : inspectionSteps pc ≤ max (inspectionSteps pn) (inspectionSteps pc) :=
        Nat.le_max_right _ _
      have hmul := Nat.mul_le_mul_right (B + 1) hmax
      rw [Nat.add_mul, one_mul]
      omega
  | let_ he1 he2 ih1 ih2 =>
      rename_i e p q v rr tt uu
      intro hp hc henv
      have hc1 : literalCeiling p ≤ B := by
        simp only [literalCeiling] at hc
        omega
      have hc2 : literalCeiling q ≤ B := by
        simp only [literalCeiling] at hc
        omega
      obtain ⟨hv,ht1⟩ := ih1 hp.1 hc1 henv
      have henv' : ∀ d, d ∈ (v :: e) → d.size ≤ B := by
        intro d hd
        simp only [List.mem_cons] at hd
        rcases hd with rfl | hd
        · exact hv
        · exact henv _ hd
      obtain ⟨hr,ht2⟩ := ih2 hp.2 hc2 henv'
      refine ⟨hr, ?_⟩
      simp only [inspectionSteps, Nat.add_mul, one_mul]
      omega
  | loop_nil he ih =>
      intro hp; cases hp
  | loop_stop he ih =>
      intro hp; cases hp
  | loop_step he1 he2 ih1 ih2 =>
      intro hp; cases hp

#guard readLetB maskedParityDeciderProg

theorem maskedParity_readLet : ReadLet maskedParityDeciderProg :=
  readLetB_sound _ (by decide)

theorem decider_raw_linear (input : Data) :
    ∃ r t, Eval [input] maskedParityDeciderProg r t ∧
      t ≤ inspectionSteps maskedParityDeciderProg *
        (input.size + literalCeiling maskedParityDeciderProg + 1) := by
  obtain ⟨r,t,he⟩ := decider_raw_total input
  let B := input.size + literalCeiling maskedParityDeciderProg
  have hB : 1 ≤ B := by
    dsimp [B]
    have := Data.size_pos input
    omega
  have hceil : literalCeiling maskedParityDeciderProg ≤ B := by
    dsimp [B]
    omega
  have henv : ∀ d, d ∈ ([input] : Env) → d.size ≤ B := by
    intro d hd
    simp only [List.mem_singleton] at hd
    subst d
    dsimp [B]
    omega
  obtain ⟨_, ht⟩ :=
    inspectLet_eval_bound B hB he maskedParity_readLet hceil henv
  exact ⟨r,t,he,ht⟩

end PNPAbove.WP21
