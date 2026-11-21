import PNPAbove.WP27TotalCost
import MIPRE.Foundations.Halting.WrapperCost

/-! Original source-native SAT verifier with no all-raw-data cost axiom. -/
namespace PNPAbove.WP27
open MIPRE MIPRE.Cost

/-- Real seven-level source verifier generated polynomially from an
arbitrary SAT formula with a total-on-ALL-raw-Data decider. -/
noncomputable def robustVerifier (U : MIPRE.Cost.UniversalMachine)
    (S : MIPRE.CL.Sampler 7) (f : MIPRE.SAT.Fml) : MIPRE.Verifier 7 :=
  MIPRE.Verifier.ofSamplerDecider U S (robustSourceGenerator f)

/-- Actual original raw verifier acceptance, for all well-formed typed
tuples, is exact source formula satisfaction and common answers. -/
theorem robustVerifier_accepts_iff (U : MIPRE.Cost.UniversalMachine)
    (S : MIPRE.CL.Sampler 7) (f : MIPRE.SAT.Fml)
    (n : Nat) (x y a b : BitStr) :
    (robustVerifier U S f).decider.Accepts n x y a b ↔
      x.length = S.dim n ∧ y.length = S.dim n ∧
      f.eval (fun i => a.getD i false) = true ∧ a = b := by
  change (MIPRE.Verifier.ofSamplerDecider U S
      (robustSourceGenerator f)).decider.Accepts n x y a b ↔ _
  rw [MIPRE.Verifier.ofSamplerDecider_accepts]
  simp only [robustSourceGenerator_accepts_iff]

/-- GCL earlier conditional Verifier.IsBounded is now UNCONDITIONAL for
the ORIGINAL gap compressor's sampler, since rawHasPolyCost is proved. -/
theorem robustVerifier_isBounded (G : MIPRE.GapCompression)
    (U : MIPRE.Cost.UniversalMachine) (f : MIPRE.SAT.Fml) :
    ∃ lam, (robustVerifier U (G.sampler 0) f).IsBounded lam := by
  have hs : (G.sampler 0).prog.HasPolyCost :=
    MIPRE.CL.Sampler.hasPolyCost_of_timeBound
      (T := fun n => G.bound.eval (n + 0)) (k := G.deg)
      (MIPRE.Cost.PolyBounded.eval G.bound
        (MIPRE.Cost.PolyBounded.id.add_const 0))
      (fun n => G.sampler_time 0 n)
  have hdim : MIPRE.Cost.PolyBounded (G.sampler 0).dim :=
    (MIPRE.Cost.PolyBounded.eval G.bound
      (MIPRE.Cost.PolyBounded.id.add_const 0)).mono
        (G.sampler_dim 0)
  obtain ⟨lam,hlam⟩ :=
    MIPRE.Verifier.ofSamplerDecider_isBounded U (G.sampler 0)
      (robustSourceGenerator f) hs hdim
      (robustSourceGenerator_hasPolyCost f)
  exact ⟨lam, hlam lam le_rfl⟩

/-- This is a PCC for the actual verifier whose original source
decider Prog is produced by the original polynomial S-M-N compiler,
not just the fixed-code prototype. -/
theorem robustNativePCC_of_sat (U : Cost.UniversalMachine)
    (S : MIPRE.CL.Sampler 7) (f : MIPRE.SAT.Fml)
    (m k T : Nat) (hT : m ≤ T) (hSAT : PNPAbove.WP24.Satisfiable m f) :
    (robustVerifier U S f).HasPerfectPCC k T := by
  obtain ⟨w, hw⟩ := hSAT
  let a : BitStr := List.ofFn w
  have ha : a.length ≤ T := by
    simp only [a, List.length_ofFn]
    omega
  apply (robustVerifier U S f).hasPerfectPCC_of_accepts_diagonal ⟨a, ha⟩
  intro x y
  rw [robustVerifier_accepts_iff]
  refine ⟨MIPRE.CL.length_toBits x, MIPRE.CL.length_toBits y, ?_, rfl⟩
  have heval : (fun i => a.getD i false) = PNPAbove.WP24.bitsAt w := by
    funext i
    exact PNPAbove.WP25.ofFn_getD_eq_bitsAt w i
  simpa only [heval] using hw

/-- Native ORIGINAL source rejection for all UNSAT formula instances,
all indices and all response strings, including malformed answers. -/
theorem robustNativeRejectsAll_of_unsat (U : Cost.UniversalMachine)
    (S : MIPRE.CL.Sampler 7) (f : MIPRE.SAT.Fml) (m : Nat)
    (hscope : f.InputsLt m) (hunsat : ¬ PNPAbove.WP24.Satisfiable m f)
    (k : Nat) (x y a b : BitStr) :
    ¬ (robustVerifier U S f).decider.Accepts k x y a b := by
  intro hacc
  obtain ⟨_, _, hf, _⟩ :=
    (robustVerifier_accepts_iff U S f k x y a b).mp hacc
  apply hunsat
  let w : Fin m → Bool := fun i => a.getD i.val false
  refine ⟨w, ?_⟩
  have heq : f.eval (fun i => a.getD i false) =
      f.eval (PNPAbove.WP24.bitsAt w) := by
    apply MIPRE.SAT.Fml.eval_congr_of_inputsLt hscope
    intro i hi
    simp [PNPAbove.WP24.bitsAt, hi, w]
  exact heq ▸ hf

/-- The actual ORIGINAL source Verifier.valStar of the uniformly
source-generated Verifier 7 has the exact SAT/UNSAT zero-one promise. -/
theorem robustNativeValStar_zero_of_unsat (U : Cost.UniversalMachine)
    (S : MIPRE.CL.Sampler 7) (f : MIPRE.SAT.Fml) (m : Nat)
    (hscope : f.InputsLt m) (hunsat : ¬ PNPAbove.WP24.Satisfiable m f)
    (k T : Nat) :
    (robustVerifier U S f).valStar k T = 0 := by
  apply (robustVerifier U S f).valStar_eq_zero_of_rejects_all
  intro x y a b
  exact robustNativeRejectsAll_of_unsat U S f m hscope hunsat k x y a b

theorem robustNativeValStar_one_of_sat (U : Cost.UniversalMachine)
    (S : MIPRE.CL.Sampler 7) (f : MIPRE.SAT.Fml)
    (m k T : Nat) (hT : m ≤ T) (hSAT : PNPAbove.WP24.Satisfiable m f) :
    (robustVerifier U S f).valStar k T = 1 :=
  (robustVerifier U S f).valStar_eq_one_of_hasPerfectPCC
    (robustNativePCC_of_sat U S f m k T hT hSAT)

/-- Exact source-native SAT instance-dependence of the UNIFORMLY
compiled Verifier 7, with all possible original source finite
dimensional tensor strategies in the optimization. -/
theorem robustNativeValStar_one_iff_sat (U : Cost.UniversalMachine)
    (S : MIPRE.CL.Sampler 7) (f : MIPRE.SAT.Fml)
    (m k T : Nat) (hscope : f.InputsLt m) (hT : m ≤ T) :
    (robustVerifier U S f).valStar k T = 1 ↔
      PNPAbove.WP24.Satisfiable m f := by
  constructor
  · intro hv
    by_contra h
    have hz := robustNativeValStar_zero_of_unsat U S f m hscope h k T
    rw [hz] at hv
    norm_num at hv
  · exact robustNativeValStar_one_of_sat U S f m k T hT

/-- The original GapCompression source pipeline is now connected
to this uniform SAT-to-native-Verifier compiler, conditional only
on the source-mandated Verifier.IsBounded lambda prerequisite. -/
theorem robustConditionalCompressedPCC_of_sat (G : MIPRE.GapCompression)
    (U : Cost.UniversalMachine) (f : MIPRE.SAT.Fml)
    (m lam k : Nat)
    (hB : (robustVerifier U (G.sampler 0) f).IsBounded lam)
    (hk : G.C₀ ≤ k) (hT : m ≤ (2 ^ k) ^ lam)
    (hSAT : PNPAbove.WP24.Satisfiable m f) :
    (G.output
      ((robustVerifier U (G.sampler 0) f).sampler.prog,
       (robustVerifier U (G.sampler 0) f).decider.prog)
       lam).HasPerfectPCC k (G.bound.eval (k + lam)) := by
  apply G.completeness (robustVerifier U (G.sampler 0) f) lam k hB hk
  exact robustNativePCC_of_sat U (G.sampler 0) f m
    (2 ^ k) ((2 ^ k) ^ lam) hT hSAT

theorem robustConditionalCompressedSoundness_of_unsat (G : MIPRE.GapCompression)
    (U : Cost.UniversalMachine) (f : MIPRE.SAT.Fml)
    (m lam k : Nat)
    (hB : (robustVerifier U (G.sampler 0) f).IsBounded lam)
    (hk : G.C₀ ≤ k) (hscope : f.InputsLt m)
    (hunsat : ¬ PNPAbove.WP24.Satisfiable m f) :
    (G.output
      ((robustVerifier U (G.sampler 0) f).sampler.prog,
       (robustVerifier U (G.sampler 0) f).decider.prog)
       lam).valStar k (G.bound.eval (k + lam)) ≤ (1 / 2 : Real) := by
  apply G.soundness (robustVerifier U (G.sampler 0) f) lam k hB hk
  have hz := robustNativeValStar_zero_of_unsat U (G.sampler 0)
    f m hscope hunsat (2 ^ k) ((2 ^ k) ^ lam)
  rw [hz]
  norm_num

/-- ORIGINAL game-level classical witness exactness: on EVERY sampled
question pair, there exists a winning pair of length-bounded original
native answers iff the source SAT formula has a satisfying assignment.
The winning Alice answer yields an actual source witness; conversely a
source witness yields the same constant answer on every question pair. -/
theorem robustNativeWinningPair_iff_sat (U : MIPRE.Cost.UniversalMachine)
    (S : MIPRE.CL.Sampler 7) (f : MIPRE.SAT.Fml)
    (m k T : Nat) (hscope : f.InputsLt m) (hT : m ≤ T)
    (q r : (robustVerifier U S f).Questions k) :
    (∃ a b : MIPRE.Verifier.Answers T,
      ((robustVerifier U S f).game k T).D q r a b = true) ↔
      PNPAbove.WP24.Satisfiable m f := by
  classical
  constructor
  · rintro ⟨a, b, hgame⟩
    have hacc : (robustVerifier U S f).decider.Accepts k
        (MIPRE.CL.toBits q) (MIPRE.CL.toBits r) a.1 b.1 := by
      simpa only [MIPRE.Verifier.game, decide_eq_true_eq] using hgame
    obtain ⟨_, _, hval, _⟩ :=
      (robustVerifier_accepts_iff U S f k _ _ _ _).mp hacc
    let w : Fin m → Bool := fun i => a.1.getD i.val false
    refine ⟨w, ?_⟩
    have heq : f.eval (fun i => a.1.getD i false) =
        f.eval (PNPAbove.WP24.bitsAt w) := by
      apply MIPRE.SAT.Fml.eval_congr_of_inputsLt hscope
      intro i hi
      simp [PNPAbove.WP24.bitsAt, hi, w]
    exact heq ▸ hval
  · rintro ⟨w, hw⟩
    let aw : BitStr := List.ofFn w
    have hal : aw.length ≤ T := by simp [aw]; omega
    let a : MIPRE.Verifier.Answers T := ⟨aw, hal⟩
    refine ⟨a, a, ?_⟩
    change decide ((robustVerifier U S f).decider.Accepts k
      (MIPRE.CL.toBits q) (MIPRE.CL.toBits r) a.1 a.1) = true
    simp only [decide_eq_true_eq]
    apply (robustVerifier_accepts_iff U S f k _ _ _ _).mpr
    refine ⟨MIPRE.CL.length_toBits q, MIPRE.CL.length_toBits r, ?_, rfl⟩
    have heval : (fun i => aw.getD i false) =
        PNPAbove.WP24.bitsAt w := by
      funext i
      exact PNPAbove.WP25.ofFn_getD_eq_bitsAt w i
    simpa only [a, heval] using hw


/-- The original MIPRE GapCompression UNSAT source soundness promise is
now UNCONDITIONAL on cost: a legal exponent exists, constructed from
the actual source programme's all-raw-data runtime and the original
source sampler. There is no residual IsBounded assumption. -/
theorem robustCompressedSoundness_unconditional
    (G : MIPRE.GapCompression) (U : MIPRE.Cost.UniversalMachine)
    (f : MIPRE.SAT.Fml) (m : Nat)
    (hscope : f.InputsLt m)
    (hunsat : ¬ PNPAbove.WP24.Satisfiable m f) :
    ∃ lam, ∀ k, G.C₀ ≤ k →
      (G.output
        ((robustVerifier U (G.sampler 0) f).sampler.prog,
         (robustVerifier U (G.sampler 0) f).decider.prog)
         lam).valStar k (G.bound.eval (k + lam)) ≤ (1 / 2 : Real) := by
  obtain ⟨lam, hBounded⟩ := robustVerifier_isBounded G U f
  refine ⟨lam, fun k hk => ?_⟩
  exact robustConditionalCompressedSoundness_of_unsat
    G U f m lam k hBounded hk hscope hunsat

/-- The original compression completeness property is now also
unconditional on source execution bounds; the only parameter
requirements are the source compiler's legal k and witness budget. -/
theorem robustCompressedCompleteness_unconditional
    (G : MIPRE.GapCompression) (U : MIPRE.Cost.UniversalMachine)
    (f : MIPRE.SAT.Fml) (m : Nat)
    (hSAT : PNPAbove.WP24.Satisfiable m f) :
    ∃ lam, ∀ k, G.C₀ ≤ k → m ≤ (2 ^ k) ^ lam →
      (G.output
        ((robustVerifier U (G.sampler 0) f).sampler.prog,
         (robustVerifier U (G.sampler 0) f).decider.prog)
         lam).HasPerfectPCC k (G.bound.eval (k + lam)) := by
  obtain ⟨lam, hBounded⟩ := robustVerifier_isBounded G U f
  refine ⟨lam, fun k hk hbudget => ?_⟩
  exact robustConditionalCompressedPCC_of_sat
    G U f m lam k hBounded hk hbudget hSAT

end PNPAbove.WP27
