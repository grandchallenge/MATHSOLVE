import PNPAbove.WP37Complete
import MIPRE.Foundations.SAT.FmlProg

namespace PNPAbove.WP37
open MIPRE MIPRE.Cost MIPRE.SAT
open scoped BigOperators

/-- Balanced parity formula: uses the actual pinned SAT.Fml XOR builder,
not auxiliary variables or a truth table. -/
def parityBlock : Nat → (Nat → Fml) → Nat → Fml
  | 0, f, i => f i
  | d+1, f, i => Fml.xor (parityBlock d f i) (parityBlock d f (i+2^d))

theorem xor_bit_eval (f g : Fml) (a : Nat → Bool) :
    bit ((Fml.xor f g).eval a) = bit (f.eval a) + bit (g.eval a) := by
  simp only [Fml.xor, Fml.eval]
  cases f.eval a <;> cases g.eval a <;> decide

theorem parityBlock_eval (d : Nat) (f : Nat → Fml) (i : Nat) (a : Nat → Bool) :
    bit ((parityBlock d f i).eval a) =
      ∑ j ∈ Finset.range (2^d), bit ((f (i+j)).eval a) := by
  induction d generalizing i with
  | zero => simp [parityBlock]
  | succ d ih =>
    rw [parityBlock,xor_bit_eval,ih,ih,pow_succ, Nat.mul_two,Finset.sum_range_add]
    simp only [Nat.add_assoc]

theorem parityBlock_esize (d : Nat) (f : Nat → Fml) (B : Nat)
    (hB : ∀ i, esize (f i) + 16 ≤ B) (i : Nat) :
    esize (parityBlock d f i) + 16 ≤ 4^d * B := by
  induction d generalizing i with
  | zero => simpa [parityBlock] using hB i
  | succ d ih =>
    rw [parityBlock,esize_xor_fml,pow_succ]
    have he : 4^d * 4 * B = 4*(4^d*B) := by ring
    rw [he]
    have h1 := ih i
    have h2 := ih (i+2^d)
    omega

def edgeIndex {n : Nat} (e : Fin n × Fin n) : Nat := n*e.1.val + e.2.val
def induced (n : Nat) (a : Nat → Bool) : Assignment (Fin n × Fin n) :=
  fun e => a (edgeIndex e)

theorem edgeIndex_injective (n : Nat) : Function.Injective (@edgeIndex n) := by
  intro e f h
  have hn : 0 < n := Nat.zero_lt_of_lt e.1.isLt
  have h1 := congrArg (fun x : Nat => x / n) h
  have h2 := congrArg (fun x : Nat => x % n) h
  simp only [edgeIndex,Nat.mul_add_div hn,Nat.mul_add_mod,
    Nat.div_eq_of_lt e.2.isLt,Nat.div_eq_of_lt f.2.isLt,
    Nat.mod_eq_of_lt e.2.isLt,Nat.mod_eq_of_lt f.2.isLt, Nat.add_zero] at h1 h2
  exact Prod.ext (Fin.ext h1) (Fin.ext h2)

theorem induced_surjective (n : Nat) : Function.Surjective (induced n) := by
  classical
  intro a
  let w : Nat → Bool := fun i =>
    if h : ∃ e : Fin n × Fin n, edgeIndex e = i then a (Classical.choose h) else false
  refine ⟨w,?_⟩
  funext e
  have h : ∃ f : Fin n × Fin n, edgeIndex f = edgeIndex e := ⟨e,rfl⟩
  have he : Classical.choose h = e :=
    edgeIndex_injective n (Classical.choose_spec h)
  simp [induced,w,he]

def edgeLeaf (n : Nat) (v : Fin n) (i j : Nat) : Fml :=
  if i < n ∧ j < n ∧ i ≠ j ∧ (v.val = i ∨ v.val = j)
  then .inp (n*i+j) else .const false

theorem edgeLeaf_eval (n : Nat) (v : Fin n) (i j : Fin n) (a : Nat → Bool) :
    bit ((edgeLeaf n v i j).eval a) =
      if completeInc v (i,j) then bit (induced n a (i,j)) else 0 := by
  simp only [edgeLeaf,i.isLt,j.isLt,true_and,completeInc]
  by_cases h : i ≠ j ∧ (v = i ∨ v = j)
  · have hv : i.val ≠ j.val ∧ (v.val = i.val ∨ v.val = j.val) := by
      simpa only [ne_eq,Fin.val_inj] using h
    simp [h,hv,Fml.eval,induced,edgeIndex]
  · have hv : ¬ (i.val ≠ j.val ∧ (v.val = i.val ∨ v.val = j.val)) := by
      simpa only [ne_eq,Fin.val_inj] using h
    simp [h,hv,Fml.eval,bit]

def nativeParity (q : Nat) (v : Fin (2^q)) : Fml :=
  parityBlock q (fun i => parityBlock q (edgeLeaf (2^q) v i) 0) 0

theorem nativeParity_eval (q : Nat) (v : Fin (2^q)) (a : Nat → Bool) :
    bit ((nativeParity q v).eval a) = parity completeInc (induced (2^q) a) v := by
  unfold nativeParity parity
  rw [parityBlock_eval,Fintype.sum_prod_type]
  simp only [Nat.zero_add]
  simp_rw [parityBlock_eval,Nat.zero_add]
  rw [← Fin.sum_univ_eq_sum_range]
  apply Finset.sum_congr rfl
  intro i _
  rw [← Fin.sum_univ_eq_sum_range]
  apply Finset.sum_congr rfl
  intro j _
  exact edgeLeaf_eval _ _ _ _ _

def nativeConstraint (q : Nat) (root v : Fin (2^q)) : Fml :=
  if v = root then nativeParity q v else .not (nativeParity q v)

theorem bit_eq_one (b : Bool) : bit b = 1 ↔ b = true := by cases b <;> decide
theorem bit_eq_zero (b : Bool) : bit b = 0 ↔ b = false := by cases b <;> decide

theorem nativeConstraint_eval (q : Nat) (root v : Fin (2^q)) (a : Nat → Bool) :
    (nativeConstraint q root v).eval a = true ↔
      ParityConstraint completeInc (charge root) v (induced (2^q) a) := by
  unfold nativeConstraint ParityConstraint charge
  rw [← nativeParity_eval]
  by_cases h : v = root
  · simp [h,bit_eq_one]
  · simp [h,Fml.eval,bit_eq_zero]

def nativeConjunction (q : Nat) (root : Fin (2^q)) (vs : List (Fin (2^q))) : Fml :=
  vs.foldr (fun v f => .and (nativeConstraint q root v) f) (.const true)

theorem nativeConjunction_eval (q : Nat) (root : Fin (2^q)) (vs : List (Fin (2^q)))
    (a : Nat → Bool) :
    (nativeConjunction q root vs).eval a = true ↔
      ∀ v ∈ vs, ParityConstraint completeInc (charge root) v (induced (2^q) a) := by
  induction vs with
  | nil => simp [nativeConjunction,Fml.eval]
  | cons v vs ih =>
    change ((nativeConstraint q root v).eval a &&
      (nativeConjunction q root vs).eval a) = true ↔ _
    simp [Bool.and_eq_true,nativeConstraint_eval,ih]

/-- Exact original source SAT encoding of every subsystem, with no extra
variables. Surjectivity ensures both directions of the SAT equivalence. -/
theorem nativeSubsys_sat_iff (q : Nat) (root : Fin (2^q)) (S : Finset (Fin (2^q))) :
    (∃ a : Nat → Bool, (nativeConjunction q root S.toList).eval a = true) ↔
      ∃ a : Assignment (Fin (2^q) × Fin (2^q)), ∀ v ∈ S,
        ParityConstraint completeInc (charge root) v a := by
  constructor
  · rintro ⟨a,ha⟩
    exact ⟨induced _ a,fun v hv => (nativeConjunction_eval _ _ _ _).1 ha v (by simpa using hv)⟩
  · rintro ⟨a,ha⟩
    obtain ⟨w,hw⟩ := induced_surjective (2^q) a
    refine ⟨w,(nativeConjunction_eval _ _ _ _).2 ?_⟩
    intro v hv
    rw [hw]
    exact ha v (by simpa using hv)

theorem native_full_unsat (q : Nat) (root : Fin (2^q)) :
    ¬ ∃ a : Nat → Bool,
      (nativeConjunction q root (Finset.univ : Finset (Fin (2^q))).toList).eval a = true := by
  rw [nativeSubsys_sat_iff]
  simpa using complete_unsat root

theorem native_proper_sat (q : Nat) (root : Fin (2^q)) (S : Finset (Fin (2^q)))
    (h : S.card < 2^q) :
    ∃ a : Nat → Bool, (nativeConjunction q root S.toList).eval a = true := by
  rw [nativeSubsys_sat_iff]
  exact complete_proper_sat root S (by simpa using h)


theorem edgeLeaf_esize (q : Nat) (v : Fin (2^q)) (i j : Nat) :
    esize (edgeLeaf (2^q) v i j) + 16 ≤ 8*q+25 := by
  unfold edgeLeaf
  split
  · rename_i h
    obtain ⟨hi,hj,_,_⟩ := h
    have hn : 0 < (2:Nat)^q := by positivity
    have hm : 2^q*i+j < 2^(q+q) := by
      rw [pow_add]
      have hh := Nat.mul_le_mul_left (2^q) (show i+1 ≤ 2^q by omega)
      rw [Nat.mul_add,Nat.mul_one] at hh
      omega
    have hb := (Nat.size_le).2 hm
    have hc := esize_nat_le (2^q*i+j)
    have he : esize (Fml.inp (2^q*i+j)) = esize (2^q*i+j)+4 := by
      change (1+esize (2^q*i+j)+1)+1+1 = _
      omega
    rw [he]
    omega
  · have hc := esize_constFml_le false
    omega

theorem nativeParity_esize (q : Nat) (v : Fin (2^q)) :
    esize (nativeParity q v) + 16 ≤ 4^q * (4^q*(8*q+25)) := by
  unfold nativeParity
  apply parityBlock_esize
  intro i
  apply parityBlock_esize
  intro j
  exact edgeLeaf_esize q v i j

theorem nativeConstraint_esize (q : Nat) (root v : Fin (2^q)) :
    esize (nativeConstraint q root v) ≤ 4^q * (4^q*(8*q+25)) := by
  have h := nativeParity_esize q v
  unfold nativeConstraint
  split
  · omega
  · rw [esize_not_fml]
    omega

theorem nativeConjunction_esize (q : Nat) (root : Fin (2^q)) (vs : List (Fin (2^q))) :
    esize (nativeConjunction q root vs) ≤
      vs.length * (4^q*(4^q*(8*q+25))+7)+9 := by
  induction vs with
  | nil => simpa [nativeConjunction] using esize_constFml_le true
  | cons v vs ih =>
    change esize (Fml.and (nativeConstraint q root v) (nativeConjunction q root vs)) ≤ _
    rw [esize_and_fml,List.length_cons,Nat.add_mul,one_mul]
    have h := nativeConstraint_esize q root v
    omega

theorem native_full_esize (q : Nat) (root : Fin (2^q)) :
    esize (nativeConjunction q root (Finset.univ : Finset (Fin (2^q))).toList) ≤
      2^q * (4^q*(4^q*(8*q+25))+7)+9 := by
  have h := nativeConjunction_esize q root (Finset.univ : Finset (Fin (2^q))).toList
  simpa using h

/-- For N=2^q vertices, the actual native encoded formula is polynomial
in N, with the sharper O(N^5 log N) bound given above. -/
theorem native_full_polynomial_esize (q : Nat) (root : Fin (2^q)) :
    esize (nativeConjunction q root (Finset.univ : Finset (Fin (2^q))).toList) ≤
      (2^q)^6 * 33 + 7*2^q+9 := by
  have h := native_full_esize q root
  have h4 : (4:Nat)^q = (2:Nat)^q * 2^q := by
    rw [show (4:Nat)=2*2 by decide,Nat.mul_pow]
  have hq : q ≤ (2:Nat)^q := Nat.le_of_lt Nat.lt_two_pow_self
  have hpos : 0 < (2:Nat)^q := by positivity
  have hN : 1 ≤ (2:Nat)^q := by omega
  have hb : 8*q+25 ≤ 33*2^q := by omega
  rw [h4] at h
  calc
    _ ≤ 2^q * ((2^q*2^q)*( (2^q*2^q)*(8*q+25))+7)+9 := h
    _ ≤ 2^q * ((2^q*2^q)*( (2^q*2^q)*(33*2^q))+7)+9 :=
      Nat.add_le_add_right (Nat.mul_le_mul_left _ (Nat.add_le_add_right
        (Nat.mul_le_mul_left _ (Nat.mul_le_mul_left _ hb)) _)) _
    _ = _ := by ring

end PNPAbove.WP37
