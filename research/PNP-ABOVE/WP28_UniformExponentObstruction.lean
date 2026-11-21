import PNPAbove.WP27RobustVerifier
import MIPRE.Foundations.SAT.FmlProg

/-!
A kernel-checkable NO-GO result for the naive fixed-λ route in PNP.
The instance-hardcoded source decider cannot have one description-length
bound independent of the formula. This does NOT rule out a fixed-code
verifier that receives an instance through its runtime input.
-/

namespace PNPAbove.WP28
open MIPRE MIPRE.Cost

/-- Arbitrarily large genuine source Boolean formulas, even without
input variables: iterated Boolean negations on a fixed constant. -/
def longFormula : Nat → MIPRE.SAT.Fml
  | 0 => .const true
  | n + 1 => .not (longFormula n)

/-- Source encoding length grows at least linearly along these formulas. -/
theorem longFormula_esize_ge (n : Nat) :
    n ≤ esize (longFormula n) := by
  induction n with
  | zero => omega
  | succ n ih =>
      rw [longFormula, MIPRE.SAT.esize_not_fml]
      omega

/-- The emitted original source programme explicitly contains the SAT
formula as a hardcoded datum; native s-m-n proves the exact cost. -/
theorem hardcoded_source_size (f : MIPRE.SAT.Fml) :
    esize (PNPAbove.WP27.robustSourceGenerator f) =
      esize PNPAbove.WP27.rawCore.code + esize f + 35 := by
  rw [PNPAbove.WP27.robustSourceGenerator_correct, Cost.hardcode_size]
  rfl

/-- The exact original machine code is at least 35 bytes/nodes larger
than its embedded original Boolean formula. -/
theorem source_size_ge_formula (f : MIPRE.SAT.Fml) :
    esize f + 35 ≤ esize (PNPAbove.WP27.robustSourceGenerator f) := by
  rw [hardcoded_source_size]
  omega

/-- For EACH proposed uniform description bound λ, there is an explicit
instance whose generated native source verifier programme exceeds λ.
This is a counterexample to the *hardcoded-input* uniform λ route. -/
theorem exists_source_size_gt (lam : Nat) :
    ∃ f : MIPRE.SAT.Fml,
      lam < esize (PNPAbove.WP27.robustSourceGenerator f) := by
  refine ⟨longFormula (lam + 1), ?_⟩
  have hsize := longFormula_esize_ge (lam + 1)
  have hsource := source_size_ge_formula (longFormula (lam + 1))
  omega

/-- No fixed source-description bound holds for ALL formulas in the
specific source-hardcoded S-M-N family of WP27. -/
theorem no_fixed_source_length :
    ¬ ∃ lam : Nat, ∀ f : MIPRE.SAT.Fml,
      esize (PNPAbove.WP27.robustSourceGenerator f) ≤ lam := by
  rintro ⟨lam, h⟩
  obtain ⟨f, hf⟩ := exists_source_size_gt lam
  exact (not_le_of_gt hf) (h f)

/-- A source-program wrapper contains its embedded original decider
description as a literal subtree; in particular it cannot be shorter. -/
theorem wrapper_payload_size (univ sampler : Cost.Prog) (dec : Cost.Data) :
    dec.size ≤ esize (Cost.Prog.wrapCore univ sampler dec) := by
  simp only [Cost.Prog.wrapCore, Cost.Prog.wrapPre, Cost.Prog.wrapHead,
    Cost.Prog.wrapCheck, Cost.Prog.wrapTail,
    Cost.Prog.esize_eq_size_toData, Cost.Prog.toData, Cost.Data.size_cons]
  omega

/-- The true original seven-level native verifier—not merely its
intermediate unwrapped decider—has an input-dependent source size. -/
theorem native_source_size_ge_formula
    (U : Cost.UniversalMachine) (S : MIPRE.CL.Sampler 7)
    (f : MIPRE.SAT.Fml) :
    esize f ≤ (PNPAbove.WP27.robustVerifier U S f).size := by
  have hw := wrapper_payload_size U.univ S.prog
    (encode (PNPAbove.WP27.robustSourceGenerator f))
  have hs := source_size_ge_formula f
  have heq : (encode (PNPAbove.WP27.robustSourceGenerator f)).size =
      esize (PNPAbove.WP27.robustSourceGenerator f) := rfl
  rw [heq] at hw
  change esize f ≤ max (esize S.prog)
    (esize (Cost.Prog.wrapCore U.univ S.prog
      (encode (PNPAbove.WP27.robustSourceGenerator f))))
  exact (by omega : esize f ≤ esize
    (Cost.Prog.wrapCore U.univ S.prog
      (encode (PNPAbove.WP27.robustSourceGenerator f)))).trans
    (Nat.le_max_right _ _)

/-- No single source λ can make ALL of the instance-hardcoded original
MIPRE Verifier 7 objects satisfy native Verifier.IsBounded λ.
This is a structural obstruction, not a proof that SAT or compression
cannot have a different globally uniform construction. -/
theorem no_fixed_native_IsBounded
    (U : Cost.UniversalMachine) (S : MIPRE.CL.Sampler 7) :
    ¬ ∃ lam : Nat, ∀ f : MIPRE.SAT.Fml,
      (PNPAbove.WP27.robustVerifier U S f).IsBounded lam := by
  rintro ⟨lam, h⟩
  have hf := native_source_size_ge_formula U S (longFormula (lam + 1))
  have hg := longFormula_esize_ge (lam + 1)
  have hb := (h (longFormula (lam + 1))).2
  omega

end PNPAbove.WP28
