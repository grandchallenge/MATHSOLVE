import PNPAbove.WP23BNativeCost
import MIPRE.Foundations.SAT.Succinct

/-!
Original MIPRE succinct Cook--Levin for the exact source-native WP21/22
decider, with its executable program and all answer-format restrictions.
This is a verifier-acceptance-to-SAT bridge, NOT SAT-to-verifier hardness.
-/
namespace PNPAbove.WP23B
open MIPRE MIPRE.Cost PNPAbove.WP21 PNPAbove.WP22
variable (K : SAT.SuccinctCookLevin)
open scoped Classical
set_option maxRecDepth 8192
set_option maxHeartbeats 1000000

/-- The actual original polynomial-time MIPRE circuit describer, instantiated
with the original source-program binary CHSH decider, not an abstract predicate. -/
noncomputable def nativeCircuitWith (n T Q σ : Nat) (x y : BitStr) : SAT.Circuit :=
  K.describe
    ((maskedParityDecider.prog, n, T, Q, σ), x, y)

/-- An extension of two exact tape blocks to a SAT assignment of the concrete
succinct 3CNF produced by the original MIPRE Cook--Levin construction. -/
def NativeSatWith (n T Q σ : Nat) (x y : BitStr)
    (A B : Fin (2 * T) → Bool) : Prop :=
  SAT.ExtendsAnswers (K.four_mul_le T σ)
    ((nativeCircuitWith K n T Q σ x y).formula3 (K.m T σ)) A B

/-- Exact circuit input arity, from the original source theorem interface. -/
theorem nativeCircuitWith_inputs (n T Q σ : Nat) (x y : BitStr) :
    (nativeCircuitWith K n T Q σ x y).inputs = 3 * K.m T σ + 3 :=
  K.inputs_eq maskedParityDecider.prog n T Q σ x y

/-- The generated original circuit is well-formed: exact input fanout and
output discipline are inherited from the imported source construction. -/
theorem nativeCircuitWith_wellFormed (n T Q σ : Nat) (x y : BitStr) :
    (nativeCircuitWith K n T Q σ x y).WellFormed :=
  K.wellFormed ((maskedParityDecider.prog, n, T, Q, σ), x, y)

/-- An ORIGINAL SOURCE gate-size bound valid for each source-declared
question/time/program-size parameter instance. -/
theorem nativeCircuitWith_gate_bound (n T Q σ : Nat) (x y : BitStr)
    (hV : SAT.Valid maskedParityDecider.prog n T Q σ x y) :
    (nativeCircuitWith K n T Q σ x y).size ≤ K.s n T Q σ :=
  K.size_le maskedParityDecider.prog n T Q σ x y hV

/-- Source-native exact Cook--Levin semantics, with all original validity
requirements visible. No black-box SAT instance or hard-coded acceptance. -/
theorem nativeSatWith_iff_timed_answers (n T Q σ : Nat) (x y : BitStr)
    (hV : SAT.Valid maskedParityDecider.prog n T Q σ x y)
    (A B : Fin (2 * T) → Bool) :
    NativeSatWith K n T Q σ x y A B ↔
      SAT.EncodesAccepted maskedParityDecider n x y T A B :=
  K.accepts_iff maskedParityDecider n T Q σ x y hV A B

/-- Existential SAT satisfiability is exactly existence of some original
source-decider answer pair ACCEPTED WITHIN THE EXPLICIT TIME T. -/
theorem nativeSatWith_exists_iff_source_timed_acceptance (n T Q σ : Nat)
    (x y : BitStr) (hV : SAT.Valid maskedParityDecider.prog n T Q σ x y) :
    (∃ A B : Fin (2 * T) → Bool, NativeSatWith K n T Q σ x y A B) ↔
      ∃ ap bp : BitStr, ap.length ≤ T ∧ bp.length ≤ T ∧
        maskedParityDecider.AcceptsWithin n x y ap bp T := by
  constructor
  · rintro ⟨A, B, hAB⟩
    obtain ⟨ap, bp, ha, hb, _, _, hwithin⟩ :=
      (nativeSatWith_iff_timed_answers K n T Q σ x y hV A B).mp hAB
    exact ⟨ap, bp, ha, hb, hwithin⟩
  · rintro ⟨ap, bp, ha, hb, hwithin⟩
    refine ⟨fun j => SAT.tapeBits ap j, fun j => SAT.tapeBits bp j, ?_⟩
    apply (nativeSatWith_iff_timed_answers K n T Q σ x y hV _ _).mpr
    exact ⟨ap, bp, ha, hb, fun _ => rfl, fun _ => rfl, hwithin⟩

/-- Every SAT witness forces an actual original-source accepted answer and
thus the full WP22 nine-bit and singleton-bit-string guards. -/
theorem nativeSatWith_requires_original_shape (n T Q σ : Nat)
    (x y : BitStr) (hV : SAT.Valid maskedParityDecider.prog n T Q σ x y)
    (A B : Fin (2 * T) → Bool) (h : NativeSatWith K n T Q σ x y A B) :
    n ≠ 0 ∧ x.length = 9 ∧ y.length = 9 ∧
      ∃ ap bp : BitStr, ap.length = 1 ∧ bp.length = 1 ∧
        leafRule [bp[0]!, ap[0]!, y[8]!, y[0]!, x[8]!, x[0]!] = true := by
  obtain ⟨ap, bp, _, _, _, _, hwithin⟩ :=
    (nativeSatWith_iff_timed_answers K n T Q σ x y hV A B).mp h
  have hacc : maskedParityDecider.Accepts n x y ap bp :=
    hwithin.accepts
  obtain ⟨hn, hx, hy, ha, hb, hv⟩ :=
    (native_accepts_iff n x y ap bp).mp hacc
  exact ⟨hn, hx, hy, ap, bp, ha, hb, hv⟩

/-- Every original source-native accepted answer has a concrete satisfying
3SAT certificate with an explicitly computable time parameter. This is
verifier acceptance REDUCES TO SAT, not SAT REDUCES TO verifier acceptance. -/
theorem native_acceptance_produces_sat (n : Nat) (x y ap bp : BitStr)
    (hacc : maskedParityDecider.Accepts n x y ap bp) :
    ∃ A B : Fin (2 * nativeTimeParameter n x y ap bp) → Bool,
      NativeSatWith K n (nativeTimeParameter n x y ap bp)
        (max x.length y.length) (esize maskedParityDecider.prog) x y A B := by
  let T := nativeTimeParameter n x y ap bp
  let Q := max x.length y.length
  let σ := esize maskedParityDecider.prog
  have hV : SAT.Valid maskedParityDecider.prog n T Q σ x y := by
    refine ⟨?_, ?_, le_rfl, ?_, ?_⟩
    all_goals dsimp [T, Q, nativeTimeParameter] <;> omega
  obtain ⟨t, ht, hrun⟩ :=
    native_acceptance_within_explicit_cost n x y ap bp hacc
  have htime : t ≤ T := by
    dsimp [T, nativeTimeParameter]
    omega
  have hal : ap.length ≤ T := by dsimp [T, nativeTimeParameter]; omega
  have hbl : bp.length ≤ T := by dsimp [T, nativeTimeParameter]; omega
  have hwithin : maskedParityDecider.AcceptsWithin n x y ap bp T :=
    ⟨t, htime, hrun⟩
  exact (nativeSatWith_exists_iff_source_timed_acceptance K n T Q σ x y hV).mpr
    ⟨ap, bp, hal, hbl, hwithin⟩

/-- Zero source index makes every exact original succinct SAT instance
unsatisfiable, independently of its two tape-prefix assignments. -/
theorem nativeSatWith_zero_index_unsat (T Q σ : Nat) (x y : BitStr)
    (hV : SAT.Valid maskedParityDecider.prog 0 T Q σ x y) :
    ¬ ∃ A B : Fin (2 * T) → Bool, NativeSatWith K 0 T Q σ x y A B := by
  rintro ⟨A, B, hs⟩
  exact (nativeSatWith_requires_original_shape K 0 T Q σ x y hV A B hs).1 rfl

/-- The masked x8 source rejection condition becomes an exact *unsat*
certificate for the original succinct Cook--Levin 3CNF. -/
theorem nativeSatWith_x8_unsat (n T Q σ : Nat) (x y : BitStr)
    (hV : SAT.Valid maskedParityDecider.prog n T Q σ x y)
    (hx8 : x[8]! = true) :
    ¬ ∃ A B : Fin (2 * T) → Bool, NativeSatWith K n T Q σ x y A B := by
  rintro ⟨A, B, hs⟩
  obtain ⟨_, _, _, ap, bp, _, _, hleaf⟩ :=
    nativeSatWith_requires_original_shape K n T Q σ x y hV A B hs
  simp [leafRule, hx8] at hleaf

/-- The masked y0 source rejection condition likewise becomes an exact
unsat certificate of the concrete original succinct 3CNF. -/
theorem nativeSatWith_y0_unsat (n T Q σ : Nat) (x y : BitStr)
    (hV : SAT.Valid maskedParityDecider.prog n T Q σ x y)
    (hy0 : y[0]! = true) :
    ¬ ∃ A B : Fin (2 * T) → Bool, NativeSatWith K n T Q σ x y A B := by
  rintro ⟨A, B, hs⟩
  obtain ⟨_, _, _, ap, bp, _, _, hleaf⟩ :=
    nativeSatWith_requires_original_shape K n T Q σ x y hV A B hs
  simp [leafRule, hy0] at hleaf

end PNPAbove.WP23B
