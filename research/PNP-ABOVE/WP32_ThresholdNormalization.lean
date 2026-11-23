import PNPAbove.WP30Classical
import MIPRE.Foundations.SAT.FmlProg

/-!
PNP WP32: eliminate the compressor's fixed minimum-index hypothesis by an
actual source-polynomial SAT-preserving padding programme. The source answer
budget is a separate mathematical/representation obligation.
-/
namespace PNPAbove.WP32
open MIPRE MIPRE.SAT MIPRE.Cost MIPRE.Cost.PolyTimeFun

/-- Adding true conjuncts grows source encoding without changing SAT. -/
def padTrue : Nat → Fml → Fml
  | 0, f => f
  | r + 1, f => .and (.const true) (padTrue r f)

theorem padTrue_eval (r : Nat) (f : Fml) (w : Nat → Bool) :
    (padTrue r f).eval w = f.eval w := by
  induction r with
  | zero => rfl
  | succ r ih => simp [padTrue, Fml.eval, ih]

theorem padTrue_inputs (r m : Nat) (f : Fml) :
    (padTrue r f).InputsLt m ↔ f.InputsLt m := by
  induction r with
  | zero => rfl
  | succ r ih => simpa [padTrue, Fml.InputsLt] using ih

theorem padTrue_size_lower (r : Nat) (f : Fml) :
    r ≤ (padTrue r f).size := by
  induction r with
  | zero => omega
  | succ r ih =>
      change r + 1 ≤ 1 + (padTrue r f).size + 1
      omega

theorem source_fml_node_count_le_encoded (f : Fml) : f.size ≤ esize f := by
  change f.size ≤ esize f.rpn
  simpa only [Fml.length_rpn] using length_le_esize_list f.rpn

/-- This source programme has one fixed code for each fixed padding amount.
Its runtime polynomial and code do NOT depend on the SAT instance. -/
noncomputable def padTrueProgram : (r : Nat) → PolyTimeFun Fml Fml
  | 0 => PolyTimeFun.id Fml
  | r + 1 => Fml.andF.comp
      ((PolyTimeFun.const (Fml.const true)).pair (padTrueProgram r))

theorem padTrueProgram_correct (r : Nat) (f : Fml) :
    padTrueProgram r f = padTrue r f := by
  induction r with
  | zero => rfl
  | succ r ih => simp [padTrue, padTrueProgram, ih]

noncomputable def normalizedIndexProgram (r : Nat) :
    PolyTimeFun PNPAbove.WP29.Enc3CNF Nat :=
  PNPAbove.WP28B.formulaIndexProgram.comp
    ((padTrueProgram r).comp PNPAbove.WP29.formulaProgram)

theorem normalizedIndex_correct (r : Nat) (cs : PNPAbove.WP29.Enc3CNF) :
    normalizedIndexProgram r cs =
      PNPAbove.WP28B.formulaIndex (padTrue r (PNPAbove.WP29.formula cs)) := by
  simp [normalizedIndexProgram, padTrueProgram_correct,
    PNPAbove.WP29.formulaProgram_correct,
    PNPAbove.WP28B.formulaIndexProgram_correct]

/-- The native compressor's universal numeric threshold is automatically
satisfied, with no input-specific threshold premise. -/
theorem normalizedIndex_threshold (r : Nat)
    (cs : PNPAbove.WP29.Enc3CNF) :
    r ≤ normalizedIndexProgram r cs := by
  rw [normalizedIndex_correct]
  let f := padTrue r (PNPAbove.WP29.formula cs)
  have hsize : r ≤ esize f :=
    (padTrue_size_lower r _).trans (source_fml_node_count_le_encoded _)
  have hp : 2 ^ r ≤ 2 ^ esize f :=
    Nat.pow_le_pow_right (by omega : (1 : Nat) ≤ 2) hsize
  have hnum := PNPAbove.WP28B2.formulaIndex_numeric_exponential_lower f
  have hs : r ≤ 2 ^ r := Nat.le_of_lt (show r < 2 ^ r from Nat.lt_two_pow_self)
  exact hs.trans (hp.trans hnum)

/-- Exact original Cost.Prog polynomial execution certificate for
SAT-to-index compilation with the threshold padding included. -/
theorem normalizedIndex_source_polytime (r : Nat)
    (cs : PNPAbove.WP29.Enc3CNF) :
    ∃ t ≤ (normalizedIndexProgram r).timeBound.eval (esize cs),
      (normalizedIndexProgram r).code.Runs
        (encode cs) (encode (normalizedIndexProgram r cs)) t :=
  (normalizedIndexProgram r).computes cs


/-- Padding preserves finite-variable SAT, including UNSAT. -/
theorem padTrue_sat (r m : Nat) (f : Fml) :
    PNPAbove.WP24.Satisfiable m (padTrue r f) ↔
      PNPAbove.WP24.Satisfiable m f := by
  simp only [PNPAbove.WP24.Satisfiable, padTrue_eval]

/-- The same SAT-to-index algorithm, including padding, is a fixed
original-source polynomial-time Cost.Prog for each fixed r. -/
noncomputable def normalizedClassicalProgram (r : Nat)
    (oracle : PolyTimeFun Nat Bool) :
    PolyTimeFun PNPAbove.WP29.Enc3CNF Bool :=
  oracle.comp (normalizedIndexProgram r)

/-- The ORIGINAL compression completeness theorem applied to the padded
source instance, with the native C0 threshold *proved*, not assumed. -/
theorem normalized_compressed_PCC
    (G : MIPRE.GapCompression) (U : Cost.UniversalMachine)
    {m lam : Nat} (cs : List (SAT.Clause3 (Fin m)))
    (hB : (PNPAbove.WP28C.powerIndexedVerifier U (G.sampler 0)).IsBounded lam)
    (hbudget : m ≤ (2 ^ normalizedIndexProgram G.C₀
      (PNPAbove.WP29.fromOriginal3CNF cs)) ^ lam)
    (hSAT : ∃ w : Fin m → Bool, (PNPAbove.WP24.threeCNFSet cs).Sat w) :
    (PNPAbove.WP30.fixedCompressed G U lam).HasPerfectPCC
      (normalizedIndexProgram G.C₀ (PNPAbove.WP29.fromOriginal3CNF cs))
      (G.bound.eval (normalizedIndexProgram G.C₀
        (PNPAbove.WP29.fromOriginal3CNF cs) + lam)) := by
  let f := padTrue G.C₀ (PNPAbove.WP29.formula (PNPAbove.WP29.fromOriginal3CNF cs))
  have hk : G.C₀ ≤ PNPAbove.WP28B.formulaIndex f := by
    simpa only [normalizedIndex_correct] using
      (normalizedIndex_threshold G.C₀ (PNPAbove.WP29.fromOriginal3CNF cs))
  have hb : m ≤ (2 ^ PNPAbove.WP28B.formulaIndex f) ^ lam := by
    simpa only [normalizedIndex_correct] using hbudget
  have hsat : PNPAbove.WP24.Satisfiable m f := by
    apply (padTrue_sat G.C₀ m _).mpr
    obtain ⟨w, hw⟩ := hSAT
    exact ⟨w, (PNPAbove.WP29.originalFinite3CNF_sat_iff cs w).mp hw⟩
  have h := PNPAbove.WP28C.powerCompressedPCC_of_sat G U f m lam hB hk hb hsat
  simpa only [PNPAbove.WP30.fixedCompressed, normalizedIndex_correct] using h

/-- The ORIGINAL compression quantum soundness is threshold-free for
our padded encoding, even on UNSAT formulas with unused variables. -/
theorem normalized_compressed_soundness
    (G : MIPRE.GapCompression) (U : Cost.UniversalMachine)
    {m lam : Nat} (cs : List (SAT.Clause3 (Fin m)))
    (hB : (PNPAbove.WP28C.powerIndexedVerifier U (G.sampler 0)).IsBounded lam)
    (hUNSAT : ¬ ∃ w : Fin m → Bool,
      (PNPAbove.WP24.threeCNFSet cs).Sat w) :
    (PNPAbove.WP30.fixedCompressed G U lam).valStar
      (normalizedIndexProgram G.C₀ (PNPAbove.WP29.fromOriginal3CNF cs))
      (G.bound.eval (normalizedIndexProgram G.C₀
        (PNPAbove.WP29.fromOriginal3CNF cs) + lam)) ≤ (1 / 2 : Real) := by
  let f := padTrue G.C₀ (PNPAbove.WP29.formula (PNPAbove.WP29.fromOriginal3CNF cs))
  have hk : G.C₀ ≤ PNPAbove.WP28B.formulaIndex f := by
    simpa only [normalizedIndex_correct] using
      (normalizedIndex_threshold G.C₀ (PNPAbove.WP29.fromOriginal3CNF cs))
  have hscope : f.InputsLt m :=
    (padTrue_inputs G.C₀ m _).mpr (PNPAbove.WP29.original3CNF_scoped cs)
  have hunsat : ¬ PNPAbove.WP24.Satisfiable m f := by
    intro h
    obtain ⟨w, hw⟩ := (padTrue_sat G.C₀ m _).mp h
    exact hUNSAT ⟨w, (PNPAbove.WP29.originalFinite3CNF_sat_iff cs w).mpr hw⟩
  have h := PNPAbove.WP28C.powerCompressedSoundness_of_unsat
    G U f m lam hB hk hscope hunsat
  simpa only [PNPAbove.WP30.fixedCompressed, normalizedIndex_correct] using h

/-- Honest end-to-end classical reduction, now with NO unproved source
compressor threshold premise. Only the native witness budget and the
hypothetical efficient compressed-game oracle remain explicit. -/
theorem normalized_classical_SAT_transfer
    (G : MIPRE.GapCompression) (U : Cost.UniversalMachine)
    (oracle : PolyTimeFun Nat Bool) (lam : Nat)
    (hB : (PNPAbove.WP28C.powerIndexedVerifier U (G.sampler 0)).IsBounded lam)
    (hyes : ∀ k, (PNPAbove.WP30.fixedCompressed G U lam).HasPerfectPCC k
      (G.bound.eval (k + lam)) → oracle k = true)
    (hno : ∀ k, (PNPAbove.WP30.fixedCompressed G U lam).valStar k
      (G.bound.eval (k + lam)) ≤ (1 / 2 : Real) → oracle k = false)
    {m : Nat} (cs : List (SAT.Clause3 (Fin m)))
    (hbudget : m ≤ (2 ^ normalizedIndexProgram G.C₀
      (PNPAbove.WP29.fromOriginal3CNF cs)) ^ lam) :
    normalizedClassicalProgram G.C₀ oracle
      (PNPAbove.WP29.fromOriginal3CNF cs) = true ↔
      ∃ w : Fin m → Bool, (PNPAbove.WP24.threeCNFSet cs).Sat w := by
  let k := normalizedIndexProgram G.C₀ (PNPAbove.WP29.fromOriginal3CNF cs)
  constructor
  · intro htrue
    by_contra hun
    have hsound := normalized_compressed_soundness G U cs hB hun
    have hf : oracle k = false := hno k hsound
    have ht : oracle k = true := htrue
    rw [hf] at ht
    contradiction
  · intro hsat
    have hpcc := normalized_compressed_PCC G U cs hB hbudget hsat
    exact hyes k hpcc

/-- Native source polynomial-run certificate even after threshold
normalization and classical composition (assuming oracle supplied). -/
theorem normalized_classical_SAT_polytime (r : Nat)
    (oracle : PolyTimeFun Nat Bool) (cs : PNPAbove.WP29.Enc3CNF) :
    ∃ t ≤ (normalizedClassicalProgram r oracle).timeBound.eval (esize cs),
      (normalizedClassicalProgram r oracle).code.Runs
        (encode cs) (encode (normalizedClassicalProgram r oracle cs)) t :=
  (normalizedClassicalProgram r oracle).computes cs

end PNPAbove.WP32
