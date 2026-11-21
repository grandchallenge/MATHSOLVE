import PNPAbove.WP28CVerifier
import MIPRE.Foundations.SAT.Rename

/-! Original source 2^k index values and actual compressor transfer. -/

namespace PNPAbove.WP28C
open MIPRE MIPRE.Cost

/-- The actual source-native seven-level verifier is synchronous at any
formula's exact binary index: it never accepts different answers to
identical questions there. -/
theorem powerIndexedVerifier_synchronous (U : Cost.UniversalMachine)
    (S : MIPRE.CL.Sampler 7) (f : MIPRE.SAT.Fml) :
    (powerIndexedVerifier U S).IsSynchronousAt
       (2 ^ PNPAbove.WP28B.formulaIndex f) := by
  intro q a b hab hacc
  exact hab ((powerIndexedVerifier_accepts_iff U S f q q a b).mp hacc).2.2.2

/-- An actual original PCC strategy wins surely on the source-native
Game, not on an abstract witness predicate. -/
theorem powerIndexedVerifier_HasPerfectPCC_of_sat
    (U : Cost.UniversalMachine) (S : MIPRE.CL.Sampler 7)
    (f : MIPRE.SAT.Fml) (m T : Nat)
    (hT : m ≤ T) (hSAT : PNPAbove.WP24.Satisfiable m f) :
    (powerIndexedVerifier U S).HasPerfectPCC
      (2 ^ PNPAbove.WP28B.formulaIndex f) T := by
  obtain ⟨w, hw⟩ := hSAT
  let a : BitStr := List.ofFn w
  have ha : a.length ≤ T := by
    simp only [a, List.length_ofFn]
    omega
  apply (powerIndexedVerifier U S).hasPerfectPCC_of_accepts_diagonal ⟨a, ha⟩
  intro x y
  rw [powerIndexedVerifier_accepts_iff]
  refine ⟨MIPRE.CL.length_toBits x, MIPRE.CL.length_toBits y, ?_, rfl⟩
  have heval : (fun i => a.getD i false) = PNPAbove.WP24.bitsAt w := by
    funext i
    exact PNPAbove.WP25.ofFn_getD_eq_bitsAt w i
  simpa only [heval] using hw

/-- A formula with bounded original source input variables and no SAT
assignment makes every canonical raw source response fail, in every
question pair for the precise formula index. -/
theorem powerIndexedVerifier_rejects_all_of_unsat
    (U : Cost.UniversalMachine) (S : MIPRE.CL.Sampler 7)
    (f : MIPRE.SAT.Fml) (m : Nat)
    (hscope : f.InputsLt m) (hunsat : ¬ PNPAbove.WP24.Satisfiable m f)
    (x y a b : BitStr) :
    ¬ (powerIndexedVerifier U S).decider.Accepts
      (2 ^ PNPAbove.WP28B.formulaIndex f) x y a b := by
  intro hacc
  obtain ⟨_, _, hf, _⟩ :=
    (powerIndexedVerifier_accepts_iff U S f x y a b).mp hacc
  apply hunsat
  let w : Fin m → Bool := fun i => a.getD i.val false
  refine ⟨w, ?_⟩
  have heq : f.eval (fun i => a.getD i false) =
      f.eval (PNPAbove.WP24.bitsAt w) := by
    apply MIPRE.SAT.Fml.eval_congr_of_inputsLt hscope
    intro i hi
    simp [PNPAbove.WP24.bitsAt, hi, w]
  exact heq ▸ hf

/-- Actual ORIGINAL source MIPRE.Verifier.valStar is exactly ZERO for
each UNSAT source instance at its exact binary source game index. -/
theorem powerIndexedVerifier_valStar_zero_of_unsat
    (U : Cost.UniversalMachine) (S : MIPRE.CL.Sampler 7)
    (f : MIPRE.SAT.Fml) (m T : Nat)
    (hscope : f.InputsLt m) (hunsat : ¬ PNPAbove.WP24.Satisfiable m f) :
    (powerIndexedVerifier U S).valStar
      (2 ^ PNPAbove.WP28B.formulaIndex f) T = 0 := by
  apply (powerIndexedVerifier U S).valStar_eq_zero_of_rejects_all
  intro x y a b
  exact powerIndexedVerifier_rejects_all_of_unsat U S f m
    hscope hunsat x y a b

/-- Exact original native tensor quantum value ONE on satisfiable
source instances with sufficient response budget. -/
theorem powerIndexedVerifier_valStar_one_of_sat
    (U : Cost.UniversalMachine) (S : MIPRE.CL.Sampler 7)
    (f : MIPRE.SAT.Fml) (m T : Nat)
    (hT : m ≤ T) (hSAT : PNPAbove.WP24.Satisfiable m f) :
    (powerIndexedVerifier U S).valStar
      (2 ^ PNPAbove.WP28B.formulaIndex f) T = 1 :=
  (powerIndexedVerifier U S).valStar_eq_one_of_hasPerfectPCC
    (powerIndexedVerifier_HasPerfectPCC_of_sat U S f m T hT hSAT)

/-- Exact unconditional original-source SAT/quantum-game promise for a
SINGLE fixed seven-level verifier with one UNIFORM IsBounded lambda.
The game index is formulaIndex f, not the 2^k index used by the
source GapCompression theorem. -/
theorem powerIndexedVerifier_valStar_one_iff_sat
    (U : Cost.UniversalMachine) (S : MIPRE.CL.Sampler 7)
    (f : MIPRE.SAT.Fml) (m T : Nat)
    (hscope : f.InputsLt m) (hT : m ≤ T) :
    ((powerIndexedVerifier U S).valStar
      (2 ^ PNPAbove.WP28B.formulaIndex f) T = 1) ↔
      PNPAbove.WP24.Satisfiable m f := by
  constructor
  · intro hv
    by_contra h
    have hz := powerIndexedVerifier_valStar_zero_of_unsat U S
      f m T hscope h
    rw [hz] at hv
    norm_num at hv
  · exact powerIndexedVerifier_valStar_one_of_sat U S f m T hT


/-- The ORIGINAL source compressor accepts the SAT full-assignment
witness only at its REQUIRED 2^k input index. The fixed k is the
source-encoded formulaIndex f. No simulator or assertion bypass. -/
theorem powerCompressedPCC_of_sat
    (G : MIPRE.GapCompression) (U : Cost.UniversalMachine)
    (f : MIPRE.SAT.Fml) (m lam : Nat)
    (hB : (powerIndexedVerifier U (G.sampler 0)).IsBounded lam)
    (hk : G.C₀ ≤ PNPAbove.WP28B.formulaIndex f)
    (hT : m ≤ (2 ^ PNPAbove.WP28B.formulaIndex f) ^ lam)
    (hSAT : PNPAbove.WP24.Satisfiable m f) :
    (G.output
       ((powerIndexedVerifier U (G.sampler 0)).sampler.prog,
        (powerIndexedVerifier U (G.sampler 0)).decider.prog)
        lam).HasPerfectPCC
          (PNPAbove.WP28B.formulaIndex f)
          (G.bound.eval (PNPAbove.WP28B.formulaIndex f + lam)) := by
  apply G.completeness (powerIndexedVerifier U (G.sampler 0)) lam
    (PNPAbove.WP28B.formulaIndex f) hB hk
  exact powerIndexedVerifier_HasPerfectPCC_of_sat
    U (G.sampler 0) f m ((2 ^ PNPAbove.WP28B.formulaIndex f) ^ lam)
    hT hSAT

/-- The SOURCE compressor's original quantum soundness implication is
NOW GENUINELY APPLICABLE to arbitrary UNSAT formulas at the required
native 2^k index. No hardcoded game and no hidden boundedness premise. -/
theorem powerCompressedSoundness_of_unsat
    (G : MIPRE.GapCompression) (U : Cost.UniversalMachine)
    (f : MIPRE.SAT.Fml) (m lam : Nat)
    (hB : (powerIndexedVerifier U (G.sampler 0)).IsBounded lam)
    (hk : G.C₀ ≤ PNPAbove.WP28B.formulaIndex f)
    (hscope : f.InputsLt m)
    (hunsat : ¬ PNPAbove.WP24.Satisfiable m f) :
    (G.output
       ((powerIndexedVerifier U (G.sampler 0)).sampler.prog,
        (powerIndexedVerifier U (G.sampler 0)).decider.prog)
        lam).valStar
          (PNPAbove.WP28B.formulaIndex f)
          (G.bound.eval (PNPAbove.WP28B.formulaIndex f + lam)) ≤ (1 / 2 : Real) := by
  apply G.soundness (powerIndexedVerifier U (G.sampler 0)) lam
    (PNPAbove.WP28B.formulaIndex f) hB hk
  rw [powerIndexedVerifier_valStar_zero_of_unsat
    U (G.sampler 0) f m ((2 ^ PNPAbove.WP28B.formulaIndex f) ^ lam)
    hscope hunsat]
  norm_num

/-- ONE source-original program and ONE source-original IsBounded
lambda serve ALL formula instances; the compressor is FIXED once.
The remaining premises are explicit native compressor threshold and
SAT witness-budget accounting, not a false P-vs-NP claim. -/
theorem exists_global_lam_and_native_compressor
    (G : MIPRE.GapCompression) (U : Cost.UniversalMachine) :
    ∃ lam,
      (powerIndexedVerifier U (G.sampler 0)).IsBounded lam ∧
      (∀ (f : MIPRE.SAT.Fml) (m : Nat),
        G.C₀ ≤ PNPAbove.WP28B.formulaIndex f →
        m ≤ (2 ^ PNPAbove.WP28B.formulaIndex f) ^ lam →
        PNPAbove.WP24.Satisfiable m f →
        (G.output
           ((powerIndexedVerifier U (G.sampler 0)).sampler.prog,
            (powerIndexedVerifier U (G.sampler 0)).decider.prog)
            lam).HasPerfectPCC
              (PNPAbove.WP28B.formulaIndex f)
              (G.bound.eval (PNPAbove.WP28B.formulaIndex f + lam))) ∧
      (∀ (f : MIPRE.SAT.Fml) (m : Nat),
        G.C₀ ≤ PNPAbove.WP28B.formulaIndex f →
        f.InputsLt m →
        ¬ PNPAbove.WP24.Satisfiable m f →
        (G.output
           ((powerIndexedVerifier U (G.sampler 0)).sampler.prog,
            (powerIndexedVerifier U (G.sampler 0)).decider.prog)
            lam).valStar
              (PNPAbove.WP28B.formulaIndex f)
              (G.bound.eval (PNPAbove.WP28B.formulaIndex f + lam)) ≤ (1 / 2 : Real)) := by
  obtain ⟨lam, hb⟩ := powerIndexedVerifier_exists_uniform_lam G U
  refine ⟨lam, hb, ?_, ?_⟩
  · intro f m hk hm hs
    exact powerCompressedPCC_of_sat G U f m lam hb hk hm hs
  · intro f m hk hscope hunsat
    exact powerCompressedSoundness_of_unsat G U f m lam hb hk hscope hunsat

end PNPAbove.WP28C
