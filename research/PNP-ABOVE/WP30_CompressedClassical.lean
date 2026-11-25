import PNPAbove.WP29CNF
import PNPAbove.WP28CCompression

/-!
WP30. The exact original GapCompression game is now connected to classical
source Cost.PolyTimeFun, with the unknown classical game solver as an explicit
hypothesis. This is a conditional transfer, NOT a classical lower bound.
-/
namespace PNPAbove.WP30
open MIPRE MIPRE.Cost

/-- One FIXED compressed source verifier, indexed by a finite source 3CNF
through the original binary formula index. -/
noncomputable def fixedCompressed
    (G : MIPRE.GapCompression) (U : Cost.UniversalMachine) (lam : Nat) :
    MIPRE.Verifier 7 :=
  G.output
    ((PNPAbove.WP28C.powerIndexedVerifier U (G.sampler 0)).sampler.prog,
      (PNPAbove.WP28C.powerIndexedVerifier U (G.sampler 0)).decider.prog)
    lam

/-- An original polynomial-time classical algorithm for the actual
compressed game's 1 versus at-most-half promise would yield an original
polynomial-time 3SAT decision procedure. The game oracle is a visible,
independent premise, and native threshold and budget assumptions remain. -/
theorem conditional_compressed_classical_SAT_transfer
    (G : MIPRE.GapCompression) (U : Cost.UniversalMachine)
    (oracle : Cost.PolyTimeFun Nat Bool) (lam : Nat)
    (hB : (PNPAbove.WP28C.powerIndexedVerifier U (G.sampler 0)).IsBounded lam)
    (hyes : ∀ k, (fixedCompressed G U lam).HasPerfectPCC k
      (G.bound.eval (k + lam)) → oracle k = true)
    (hno : ∀ k, (fixedCompressed G U lam).valStar k
      (G.bound.eval (k + lam)) ≤ (1 / 2 : Real) → oracle k = false)
    {m : Nat} (cs : List (MIPRE.SAT.Clause3 (Fin m)))
    (hk : G.C₀ ≤ PNPAbove.WP28B.formulaIndex
      (PNPAbove.WP29.formula (PNPAbove.WP29.fromOriginal3CNF cs)))
    (hbudget : m ≤ (2 ^ PNPAbove.WP28B.formulaIndex
      (PNPAbove.WP29.formula (PNPAbove.WP29.fromOriginal3CNF cs))) ^ lam) :
    PNPAbove.WP29.conditionalSATProgram oracle
      (PNPAbove.WP29.fromOriginal3CNF cs) = true ↔
      ∃ w : Fin m → Bool, (PNPAbove.WP24.threeCNFSet cs).Sat w := by
  let f := PNPAbove.WP29.formula (PNPAbove.WP29.fromOriginal3CNF cs)
  let k := PNPAbove.WP28B.formulaIndex f
  have hidx : PNPAbove.WP29.source3CNFIndexProgram
      (PNPAbove.WP29.fromOriginal3CNF cs) = k :=
    PNPAbove.WP29.source3CNFIndexProgram_correct _
  have hscope : f.InputsLt m := PNPAbove.WP29.original3CNF_scoped cs
  constructor
  · intro htrue
    by_contra hunsat
    have hnot : ¬ PNPAbove.WP24.Satisfiable m f := by
      intro ⟨w, hw⟩
      exact hunsat ⟨w, (PNPAbove.WP29.originalFinite3CNF_sat_iff cs w).mpr hw⟩
    have hsound := PNPAbove.WP28C.powerCompressedSoundness_of_unsat
      G U f m lam hB hk hscope hnot
    have hfalse : oracle k = false :=
      hno k (by
        simpa only [fixedCompressed] using hsound)
    have htrue' : oracle k = true := by
      change oracle (PNPAbove.WP29.source3CNFIndexProgram
        (PNPAbove.WP29.fromOriginal3CNF cs)) = true at htrue
      rwa [hidx] at htrue
    rw [hfalse] at htrue'
    contradiction
  · rintro ⟨w, hw⟩
    have hSAT : PNPAbove.WP24.Satisfiable m f :=
      ⟨w, (PNPAbove.WP29.originalFinite3CNF_sat_iff cs w).mp hw⟩
    have hcomp := PNPAbove.WP28C.powerCompressedPCC_of_sat
      G U f m lam hB hk hbudget hSAT
    have htrue : oracle k = true :=
      hyes k (by
        simpa only [fixedCompressed] using hcomp)
    change oracle (PNPAbove.WP29.source3CNFIndexProgram
      (PNPAbove.WP29.fromOriginal3CNF cs)) = true
    rwa [hidx]

/-- The conditional classical SAT decider has an ORIGINAL source
Cost.Prog run certificate polynomial in explicit source clause data size;
this bound is on the SAT-deciding oracle's binary-index input, not on
the fully expanded quantum game. -/
theorem conditional_compressed_classical_SAT_runtime
    (oracle : Cost.PolyTimeFun Nat Bool) (cs : PNPAbove.WP29.Enc3CNF) :
    ∃ t ≤ (PNPAbove.WP29.conditionalSATProgram oracle).timeBound.eval (esize cs),
      (PNPAbove.WP29.conditionalSATProgram oracle).code.Runs
        (encode cs)
        (encode (PNPAbove.WP29.conditionalSATProgram oracle cs)) t :=
  PNPAbove.WP29.conditionalClassicalSATPolytime oracle cs

end PNPAbove.WP30
