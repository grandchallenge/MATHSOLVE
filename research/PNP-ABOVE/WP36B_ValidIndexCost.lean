import PNPAbove.WP36Copy
import PNPAbove.WP34Scope
namespace PNPAbove.WP36
open MIPRE MIPRE.Cost MIPRE.SAT
theorem bit_prefix_agreement (xs ys zs : BitStr) :
    Agree xs.length (encode (xs ++ ys)) (encode (xs ++ zs)) := by
  induction xs with
  | nil => trivial
  | cons a xs ih => exact ⟨agree_refl _ _, ih⟩

def commonFront : Nat → BitStr
  | 0 => []
  | n+1 => (encode (Fml.Node.const true)).toBitsPost ++ commonFront n

theorem commonFront_length (n : Nat) : (commonFront n).length = 7*n := by
  induction n with
  | zero => rfl
  | succ n ih =>
    rw [commonFront, List.length_append, Data.length_toBitsPost, ih]
    change 7 + 7*n = 7*(n+1)
    omega

theorem padded_rpn_prefix (n : Nat) (f : Fml) :
    ∃ tail : List Fml.Node, (WP32.padTrue n f).rpn =
      List.replicate n (.const true) ++ tail := by
  induction n with
  | zero => exact ⟨f.rpn,rfl⟩
  | succ n ih =>
    obtain ⟨tail, ht⟩ := ih
    refine ⟨tail ++ [.and], ?_⟩
    simp [WP32.padTrue, Fml.rpn, ht, List.replicate_succ, List.append_assoc]

theorem serialized_prefix (n : Nat) (tail : List Fml.Node) :
    ∃ rest : BitStr, (encode (List.replicate n (.const true : Fml.Node) ++ tail)).toBitsPost =
      commonFront n ++ rest := by
  induction n with
  | zero => exact ⟨(encode tail).toBitsPost,rfl⟩
  | succ n ih =>
    obtain ⟨rest, h⟩ := ih
    refine ⟨rest ++ [true], ?_⟩
    rw [List.replicate_succ, List.cons_append, encode_list_cons, Data.toBitsPost, h]
    simp only [commonFront, List.append_assoc]

def instanceF (n : Nat) (b : Bool) : Fml := WP32.padTrue n (.const b)
def instanceK (n : Nat) (b : Bool) : Nat := WP28B.formulaIndex (instanceF n b)

theorem instance_bits_prefix (n : Nat) (b : Bool) :
    ∃ rest : BitStr, (instanceK n b).bits = commonFront n ++ rest := by
  obtain ⟨tail, ht⟩ := padded_rpn_prefix n (.const b)
  obtain ⟨rest, hr⟩ := serialized_prefix n tail
  refine ⟨rest ++ [true], ?_⟩
  unfold instanceK WP28B.formulaIndex
  rw [WP28B.indexData_bits, Fml.encode_fml]
  change (encode (WP32.padTrue n (.const b)).rpn).toBitsPost ++ [true] = _
  rw [ht, hr, List.append_assoc]

theorem instance_agreement (n : Nat) :
    Agree (7*n) (encode (instanceK n true)) (encode (instanceK n false)) := by
  obtain ⟨a,ha⟩ := instance_bits_prefix n true
  obtain ⟨b,hb⟩ := instance_bits_prefix n false
  change Agree (7*n) (encode (instanceK n true).bits) (encode (instanceK n false).bits)
  rw [ha,hb,← commonFront_length n]
  exact bit_prefix_agreement _ _ _

theorem instance_eval (n : Nat) (b : Bool) (w : Nat → Bool) :
    (instanceF n b).eval w = b := WP32.padTrue_eval n _ w

theorem instance_esize (n : Nat) (b : Bool) :
    esize (instanceF n b) = 16*n + esize (Fml.const b) := by
  induction n with
  | zero => simp [instanceF, WP32.padTrue]
  | succ n ih =>
    change esize (Fml.and (.const true) (instanceF n b)) = _
    rw [esize_and_fml, ih]
    have hc : esize (Fml.const true) = 9 := rfl
    omega

theorem instance_index_size (n : Nat) (b : Bool) :
    esize (instanceK n b) ≤ 64*n + 41 := by
  have h := esize_nat_le (instanceK n b)
  change esize (instanceK n b) ≤ 4 * Nat.size (WP28B.formulaIndex (instanceF n b)) + 1 at h
  rw [WP28B.formulaIndex_bit_length, instance_esize] at h
  cases b with
  | false =>
    have hc : esize (Fml.const false) = 7 := rfl
    omega
  | true =>
    have hc : esize (Fml.const true) = 9 := rfl
    omega

theorem instance_index_threshold (n : Nat) (b : Bool) : n ≤ instanceK n b := by
  have h : n ≤ esize (instanceF n b) :=
    (WP32.padTrue_size_lower n _).trans (WP32.source_fml_node_count_le_encoded _)
  have hh := WP28B2.formulaIndex_numeric_exponential_lower (instanceF n b)
  exact (Nat.le_of_lt Nat.lt_two_pow_self).trans
    ((Nat.pow_le_pow_right (by decide : 0 < (2:Nat)) h).trans hh)

/-- Exact compressed-promise outputs for an unrestricted program, with no
polynomial assumption. The two inputs are both genuine valid indices. -/
theorem instance_cost_lower (p : Prog) (n t u : Nat)
    (hy : p.Runs (encode (instanceK n true)) (encode true) t)
    (hn : p.Runs (encode (instanceK n false)) (encode false) u) :
    7*n < t ∧ 7*n < u := by
  constructor
  · by_contra h
    have ht : t ≤ 7*n := by omega
    have hh := runs_agreement hy (agree_down ht (instance_agreement n))
    have he := (Eval.deterministic hh hn).1
    exact (by decide : true ≠ false) (encode_injective he)
  · by_contra h
    have hu : u ≤ 7*n := by omega
    have hh := runs_agreement hn (agree_down hu (agree_symm (instance_agreement n)))
    have he := (Eval.deterministic hh hy).1
    exact (by decide : false ≠ true) (encode_injective he)

def CorrectPromise (G : GapCompression) (U : UniversalMachine) (lam : Nat) (p : Prog) : Prop :=
  ∀ f : Fml, G.C₀ ≤ WP28B.formulaIndex f →
    ((WP30.fixedCompressed G U lam).HasPerfectPCC
        (WP28B.formulaIndex f) (G.bound.eval (WP28B.formulaIndex f + lam)) →
          ∃ t, p.Runs (encode (WP28B.formulaIndex f)) (encode true) t) ∧
    ((WP30.fixedCompressed G U lam).valStar
        (WP28B.formulaIndex f) (G.bound.eval (WP28B.formulaIndex f + lam)) ≤ (1/2 : Real) →
          ∃ t, p.Runs (encode (WP28B.formulaIndex f)) (encode false) t)

theorem unrestricted_valid_promise_linear_lower
    (G : GapCompression) (U : UniversalMachine) (lam : Nat)
    (hB : (WP28C.powerIndexedVerifier U (G.sampler 0)).IsBounded lam)
    (p : Prog) (hc : CorrectPromise G U lam p)
    (n : Nat) (hn : G.C₀ ≤ n) :
    ∃ t u, p.Runs (encode (instanceK n true)) (encode true) t ∧
      p.Runs (encode (instanceK n false)) (encode false) u ∧
      7*n < t ∧ 7*n < u ∧
      esize (instanceK n true) ≤ 64*n+41 ∧ esize (instanceK n false) ≤ 64*n+41 := by
  have hyk := hn.trans (instance_index_threshold n true)
  have hnk := hn.trans (instance_index_threshold n false)
  have hsat : ∃ w : Nat → Bool, (instanceF n true).eval w = true :=
    ⟨fun _ => false, instance_eval n true _⟩
  have hunsat : ¬ ∃ w : Nat → Bool, (instanceF n false).eval w = true := by
    rintro ⟨w,h⟩
    rw [instance_eval] at h
    contradiction
  obtain ⟨t,ht⟩ := (hc (instanceF n true) hyk).1
    (WP34.canonical_compressed_yes G U (instanceF n true) lam hB hyk hsat)
  obtain ⟨u,hu⟩ := (hc (instanceF n false) hnk).2
    (WP34.canonical_compressed_no G U (instanceF n false) lam hB hnk hunsat)
  have hcost := instance_cost_lower p n t u ht hu
  exact ⟨t,u,ht,hu,hcost.1,hcost.2,instance_index_size n true,instance_index_size n false⟩


theorem instance_cost_quadratic (p : Prog) (n t u : Nat) (hn : 1 ≤ n)
    (hy : p.Runs (encode (instanceK n true)) (encode true) t)
    (hno : p.Runs (encode (instanceK n false)) (encode false) u) :
    (3*n)*(3*n) < height p*(t+3*n) ∧ (3*n)*(3*n) < height p*(u+3*n) := by
  have hag := agree_down (show 2*(3*n) ≤ 7*n by omega) (instance_agreement n)
  have hyt : (encode true : Data).size = 3 := rfl
  have hnt : (encode false : Data).size = 1 := rfl
  have hne : (encode true : Data) ≠ encode false := by decide
  exact ⟨different_runs_copy_lower (by omega) hag (by omega) hne hy hno,
    different_runs_copy_lower (by omega) (agree_symm hag) (by omega) (Ne.symm hne) hno hy⟩

/-- Uniform unrestricted SOURCE-model quadratic lower bound on the
valid-index promise. The coefficient height p is fixed for each solver.
These constant-support formulas isolate representational overhead. -/
theorem unrestricted_valid_promise_quadratic_lower
    (G : GapCompression) (U : UniversalMachine) (lam : Nat)
    (hB : (WP28C.powerIndexedVerifier U (G.sampler 0)).IsBounded lam)
    (p : Prog) (hc : CorrectPromise G U lam p)
    (n : Nat) (hn : G.C₀ ≤ n) (hp : 1 ≤ n) :
    ∃ t u, p.Runs (encode (instanceK n true)) (encode true) t ∧
      p.Runs (encode (instanceK n false)) (encode false) u ∧
      (3*n)*(3*n) < height p*(t+3*n) ∧
      (3*n)*(3*n) < height p*(u+3*n) ∧
      esize (instanceK n true) ≤ 64*n+41 ∧ esize (instanceK n false) ≤ 64*n+41 := by
  obtain ⟨t,u,ht,hu,_,_,hs,hs'⟩ :=
    unrestricted_valid_promise_linear_lower G U lam hB p hc n hn
  have hq := instance_cost_quadratic p n t u hp ht hu
  exact ⟨t,u,ht,hu,hq.1,hq.2,hs,hs'⟩

end PNPAbove.WP36
