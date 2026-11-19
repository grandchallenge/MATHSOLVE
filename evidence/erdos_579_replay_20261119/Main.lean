/-
Upstream source notice

Selected upstream portions are modified from TCSlib
https://github.com/Shilun-Allan-Li/tcslib
commit a8c77c605cb9843b3eaebe11253c4eef15ded3f7, and FABL
https://github.com/Polarnova/FABL
commit 164f830312946ccac6e7fdc7bb9493f0149e820d.
Their original source notices are retained below. Changes include
the Lean 4.33.1/Mathlib port, selection of needed declarations,
expanded notation and explicit replacement of source automation.
The following Apache 2.0 license applies to those upstream portions.

Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
-/

end Bounty

section

/- The reverse-mixing closure is copied as source; no TCSlib/FABL import is used. -/
open scoped BigOperators Topology Classical

namespace BooleanAnalysis

variable {n : ℕ}

-- TCSlib.BooleanAnalysis.Basic:62
/-- Defines the Boolean hypercube `{0,1}ⁿ`.

**Source:** [OD14, §1.1]. -/
abbrev BoolCube (n : ℕ) := Fin n → Bool

-- TCSlib.BooleanAnalysis.Basic:67
/-- Defines a real-valued Boolean function `f : {0,1}ⁿ → ℝ`.

**Source:** [OD14, §1.1]. -/
abbrev BooleanFunc (n : ℕ) := BoolCube n → ℝ

-- TCSlib.BooleanAnalysis.Basic:76
/-- Defines the uniform probability weight `2⁻ⁿ` on each point of `{0,1}ⁿ`.

**Source:** [OD14, §1.1]. -/
noncomputable def uniformWeight (n : ℕ) : ℝ := (2 : ℝ)⁻¹ ^ n

-- TCSlib.BooleanAnalysis.Basic:81
/-- Expectation of `f` under the uniform measure on `{0,1}ⁿ`.
  `𝔼[f] = 2⁻ⁿ · ∑_{x ∈ {0,1}ⁿ} f(x)`.

**Source:** [OD14, §1.1]. -/
noncomputable def expect (f : BooleanFunc n) : ℝ :=
  uniformWeight n * ∑ x : BoolCube n, f x

-- TCSlib.BooleanAnalysis.Basic:88
/-- The Boolean-cube expectation is Mathlib's uniform expectation on the finite cube.

**Source:** [OD14, §1.1]; Mathlib, `Fintype.expect_eq_sum_div_card`. -/
lemma expect_eq_fintypeExpect (f : BooleanFunc n) : expect f = 𝔼 x, f x := by
  rw [Fintype.expect_eq_sum_div_card]
  unfold expect uniformWeight
  simp [Fintype.card_pi, Fintype.card_bool, div_eq_inv_mul]

-- TCSlib.BooleanAnalysis.Basic:96
/-- The `L²` inner product on Boolean functions with respect to the uniform measure:
  `⟪f, g⟫ = 𝔼[f · g] = 2⁻ⁿ · ∑_x f(x) g(x)`.

**Source:** [OD14, §1.2]. -/
noncomputable def innerProduct (f g : BooleanFunc n) : ℝ :=
  expect (fun x ↦ f x * g x)

-- TCSlib.BooleanAnalysis.Basic:138
/-- Converts a `Bool` to `{-1, 1} ⊆ ℝ`: `false ↦ 1`, `true ↦ -1`.

**Source:** [OD14, §1.1]. -/
def boolToSign (b : Bool) : ℝ := if b then -1 else 1

lemma boolToSign_false : boolToSign false = 1 := rfl
lemma boolToSign_true : boolToSign true = -1 := rfl

-- TCSlib.BooleanAnalysis.Basic:149
lemma boolToSign_sq (b : Bool) : boolToSign b ^ 2 = 1 := by
  cases b <;> simp [boolToSign]

-- TCSlib.BooleanAnalysis.Basic:153
lemma boolToSign_mul_self (b : Bool) : boolToSign b * boolToSign b = 1 := by
  cases b <;> simp [boolToSign]

-- TCSlib.BooleanAnalysis.Basic:157
/-- The Walsh–Fourier character `χ_S : {0,1}ⁿ → ℝ` associated to a set `S ⊆ [n]`.
  `χ_S(x) = ∏_{i ∈ S} (-1)^{x_i}`.

  This forms an orthonormal basis for `L²({0,1}ⁿ, uniform)`.

**Source:** [OD14, §1.2]. -/
noncomputable def chiS (S : Finset (Fin n)) : BooleanFunc n :=
  fun x ↦ ∏ i ∈ S, boolToSign (x i)

-- TCSlib.BooleanAnalysis.Basic:168
/-- The character `χ_∅` is the constant function `1`. -/
lemma chiS_empty : chiS ((∅ : Finset (Fin n))) = fun _ ↦ 1 := by
  ext x; simp [chiS]

-- TCSlib.BooleanAnalysis.Basic:173
/-- The character `χ_{i}` for a singleton `{i}` equals `(-1)^{x_i}`. -/
lemma chiS_singleton (i : Fin n) (x : BoolCube n) :
    chiS ({i}) x = boolToSign (x i) := by
  simp [chiS]

-- TCSlib.BooleanAnalysis.Basic:179
/-- Walsh characters take values in `{-1, 1}`. -/
lemma chiS_sq_eq_one (S : Finset (Fin n)) (x : BoolCube n) :
    chiS (S) x ^ 2 = 1 := by
  simp only [chiS]
  induction S using Finset.induction with
  | empty => simp
  | insert a s ha ih =>
    rw [Finset.prod_insert ha, mul_pow, boolToSign_sq, one_mul]
    exact ih

-- TCSlib.BooleanAnalysis.Basic:195
/-- The pointwise product of two Walsh characters is another Walsh character (up to sign),
  specifically `χ_S · χ_T = χ_{S Δ T}` where `Δ` denotes symmetric difference. -/
lemma chiS_mul_chiS (S T : Finset (Fin n)) (x : BoolCube n) :
    chiS (S) x * chiS (T) x = chiS (symmDiff S T) x := by
  simp only [chiS]
  -- Decompose: S = (S \ T) ∪ (S ∩ T), T = (T \ S) ∪ (T ∩ S)
  have hS : ∏ i ∈ S, boolToSign (x i) =
      (∏ i ∈ S \ T, boolToSign (x i)) * ∏ i ∈ S ∩ T, boolToSign (x i) := by
    conv_lhs => rw [← Finset.sdiff_union_inter S T]
    apply Finset.prod_union
    simp only [Finset.disjoint_left, Finset.mem_sdiff, Finset.mem_inter, not_and]
    tauto
  have hT : ∏ i ∈ T, boolToSign (x i) =
      (∏ i ∈ T \ S, boolToSign (x i)) * ∏ i ∈ S ∩ T, boolToSign (x i) := by
    conv_lhs => rw [← Finset.sdiff_union_inter T S]
    rw [Finset.inter_comm T S]
    apply Finset.prod_union
    simp only [Finset.disjoint_left, Finset.mem_sdiff, Finset.mem_inter, not_and]
    tauto
  -- The intersection product squares to 1
  have hcancel : (∏ i ∈ S ∩ T, boolToSign (x i)) * ∏ i ∈ S ∩ T, boolToSign (x i) = 1 := by
    rw [← Finset.prod_mul_distrib]; simp [boolToSign_mul_self]
  rw [hS, hT, symmDiff_def, Finset.sup_eq_union, Finset.prod_union disjoint_sdiff_sdiff]
  -- Goal: (A * P) * (B * P) = A * B  where P² = 1
  set P := ∏ i ∈ S ∩ T, boolToSign (x i)
  set A := ∏ i ∈ S \ T, boolToSign (x i)
  set B := ∏ i ∈ T \ S, boolToSign (x i)
  calc A * P * (B * P) = A * B * (P * P) := by ring
    _ = A * B * 1 := by rw [hcancel]
    _ = A * B := by ring

-- TCSlib.BooleanAnalysis.Basic:228
/-- The Fourier–Walsh coefficient of `f` at frequency `S`:
  `f̂(S) = ⟪f, χ_S⟫ = 2⁻ⁿ · ∑_x f(x) · χ_S(x)`.

**Source:** [OD14, §1.2]. -/
noncomputable def fourierCoeff (f : BooleanFunc n) (S : Finset (Fin n)) : ℝ :=
  innerProduct f (chiS S)

-- TCSlib.BooleanAnalysis.Basic:244
/-- Key identity: `∑_{S ⊆ [n]} ∏_{i∈S} c_i = ∏_i (1 + c_i)`.
  Used via `Finset.prod_one_add`. -/
private lemma sum_prod_subset_eq_prod_one_add (c : Fin n → ℝ) :
    ∑ S : Finset (Fin n), ∏ i ∈ S, c i =
    ∏ i : Fin n, (1 + c i) := by
  -- Use Finset.prod_one_add: ∏_{i∈s} (1 + f i) = ∑_{t∈s.powerset} ∏_{i∈t} f i
  rw [Finset.prod_one_add Finset.univ]
  -- Now RHS = ∑ t ∈ Finset.univ.powerset, ∏ i ∈ t, c i
  -- Reindex: Finset.univ.powerset ≅ all Finset (Fin n) via id
  apply Finset.sum_nbij id
  · intro t _; exact Finset.mem_powerset.mpr (Finset.subset_univ t)
  · intro t₁ _ t₂ _ h; exact h
  · intro t ht; exact ⟨t, Finset.mem_univ t, rfl⟩
  · intro t _; rfl

-- TCSlib.BooleanAnalysis.Basic:259
/-- The sum of `χ_S(x) * χ_S(y)` over all `S ⊆ [n]` equals `2ⁿ` if `x = y`, else `0`.
  This is the completeness kernel for the Walsh basis. -/
private lemma sum_chiS_mul_eq (x y : BoolCube n) :
    ∑ S : Finset (Fin n), chiS S x * chiS S y = if x = y then (2 : ℝ) ^ n else 0 := by
  simp only [chiS, ← Finset.prod_mul_distrib]
  rw [sum_prod_subset_eq_prod_one_add]
  split_ifs with hxy
  · subst hxy; simp only [boolToSign_mul_self]
    simp only [Finset.prod_const, Finset.card_univ, Fintype.card_fin]
    norm_num
  · obtain ⟨i, hi⟩ := Function.ne_iff.mp hxy
    apply Finset.prod_eq_zero (Finset.mem_univ i)
    have : boolToSign (x i) * boolToSign (y i) = -1 := by
      cases hxi : x i <;> cases hyi : y i <;> simp_all [boolToSign]
    simp [this]

-- TCSlib.BooleanAnalysis.Basic:275
/-- **Walsh Expansion**: every Boolean function `f : {0,1}ⁿ → ℝ` can be written as
  `f(x) = ∑_{S ⊆ [n]} f̂(S) · χ_S(x)`.

  This is the Fourier inversion formula for the uniform measure on `{0,1}ⁿ`.

**Source:** [OD14, §1.3]. -/
theorem walsh_expansion (f : BooleanFunc n) (x : BoolCube n) :
    f x = ∑ S : Finset (Fin n), fourierCoeff f S * chiS S x := by
  simp only [fourierCoeff, innerProduct, expect, uniformWeight]
  -- Goal: f x = ∑_S (2⁻ⁿ * ∑_y f(y) * χ_S(y)) * χ_S(x)
  -- Proof: show both sides equal 2⁻ⁿ * ∑_y f(y) * ∑_S χ_S(y) * χ_S(x)
  --        then use the completeness kernel
  symm
  calc ∑ S : Finset (Fin n), ((2:ℝ)⁻¹^n * ∑ y, f y * chiS S y) * chiS S x
      = (2:ℝ)⁻¹^n * ∑ y : BoolCube n, ∑ S : Finset (Fin n), f y * (chiS S y * chiS S x) := by
        -- Move 2⁻¹^n outside by rearranging: ∑_S (a * b_S) * c_S = a * ∑_S b_S * c_S,
        -- then swap sum order and distribute f y
        have step1 : ∑ S : Finset (Fin n), ((2:ℝ)⁻¹^n * ∑ y, f y * chiS S y) * chiS S x =
            (2:ℝ)⁻¹^n * ∑ S : Finset (Fin n), (∑ y, f y * chiS S y) * chiS S x := by
          rw [Finset.mul_sum]
          apply Finset.sum_congr rfl; intro S _; ring
        have step2 : ∑ S : Finset (Fin n), (∑ y, f y * chiS S y) * chiS S x =
            ∑ y : BoolCube n, ∑ S : Finset (Fin n), f y * (chiS S y * chiS S x) := by
          simp_rw [Finset.sum_mul]
          rw [Finset.sum_comm]
          apply Finset.sum_congr rfl; intro y _
          apply Finset.sum_congr rfl; intro S _; ring
        rw [step1, step2]
    _ = (2:ℝ)⁻¹^n * ∑ y : BoolCube n, f y * (∑ S, chiS S y * chiS S x) := by
        congr 1
        apply Finset.sum_congr rfl; intro y _
        rw [← Finset.mul_sum]
    _ = (2:ℝ)⁻¹^n * ∑ y : BoolCube n, f y * (if y = x then (2:ℝ)^n else 0) := by
        simp_rw [sum_chiS_mul_eq]
    _ = (2:ℝ)⁻¹^n * (f x * (2:ℝ)^n) := by
        congr 1
        simp [Finset.sum_ite_eq', Finset.mem_univ]
    _ = f x := by
        rw [← mul_assoc, mul_comm ((2:ℝ)⁻¹^n) (f x), mul_assoc, ← mul_pow,
            inv_mul_cancel₀ (by norm_num : (2:ℝ) ≠ 0), one_pow, mul_one]

-- TCSlib.BooleanAnalysis.Basic:333
/-- Summing `χ_S` over the entire hypercube gives `2ⁿ` if `S = ∅`, else `0`. -/
private lemma sum_chiS (S : Finset (Fin n)) :
    ∑ x : BoolCube n, chiS S x = if S = ∅ then 2 ^ n else 0 := by
  simp only [chiS]
  by_cases hS : S = ∅
  · subst hS; simp [Fintype.card_pi, Fintype.card_bool]
  · simp only [hS, if_false]
    have factored : ∑ x : BoolCube n, ∏ i ∈ S, boolToSign (x i) =
        ∑ x : BoolCube n, ∏ i : Fin n, (if i ∈ S then boolToSign (x i) else 1) := by
      congr 1; ext x; rw [← Finset.prod_filter]; simp
    rw [factored]
    -- Goal: ∑ x : BoolCube n, ∏ i : Fin n, g i (x i) = 0
    -- where g i b = if i ∈ S then boolToSign b else 1
    -- Factor: = ∏ i : Fin n, ∑ b : Bool, g i b  (by Fintype.prod_sum reversed)
    rw [show ∑ x : BoolCube n, ∏ i : Fin n, (if i ∈ S then boolToSign (x i) else 1) =
        ∏ i : Fin n, ∑ b : Bool, (if i ∈ S then boolToSign b else 1) from
      (Fintype.prod_sum (fun i b => if i ∈ S then boolToSign b else 1)).symm]
    obtain ⟨i, hi⟩ := Finset.nonempty_iff_ne_empty.mpr hS
    apply Finset.prod_eq_zero (Finset.mem_univ i)
    simp [hi, boolToSign]

-- TCSlib.BooleanAnalysis.Basic:354
/-- **Orthonormality**: `⟪χ_S, χ_T⟫ = [S = T]`.

  The Walsh characters form an orthonormal system in `L²({0,1}ⁿ, uniform)`.

**Source:** [OD14, §1.2]. -/
theorem fourier_coeff_chi (S T : Finset (Fin n)) :
    innerProduct (chiS S) (chiS T) = if S = T then 1 else 0 := by
  simp only [innerProduct, expect, uniformWeight]
  have step : ∑ x : BoolCube n, chiS S x * chiS T x =
      ∑ x : BoolCube n, chiS (symmDiff S T) x := by
    congr 1; ext x; exact chiS_mul_chiS S T x
  rw [step, sum_chiS]
  by_cases hst : S = T
  · -- S = T: symmDiff S T = ∅
    subst hst
    simp only [symmDiff_self, Finset.bot_eq_empty, ↓reduceIte]
    rw [← mul_pow]; norm_num
  · -- S ≠ T: symmDiff S T ≠ ∅
    have hd : symmDiff S T ≠ ∅ := by
      intro h
      apply hst
      have : symmDiff S T = ⊥ := by rwa [Finset.bot_eq_empty]
      exact symmDiff_eq_bot.mp this
    simp [hd, hst]

-- TCSlib.BooleanAnalysis.Basic:385
/-- **Parseval's Identity**: `‖f‖² = ∑_{S ⊆ [n]} f̂(S)²`.

  The sum of squared Fourier coefficients equals the squared `L²` norm.

**Source:** [OD14, §1.4]. -/
theorem parseval (f : BooleanFunc n) :
    innerProduct f f = ∑ S : Finset (Fin n), fourierCoeff f S ^ 2 := by
  -- Expand f = ∑_S f̂(S) χ_S and use bilinearity + orthonormality
  have expand : innerProduct f f =
      ∑ S : Finset (Fin n), ∑ T : Finset (Fin n),
        fourierCoeff f S * fourierCoeff f T * innerProduct (chiS S) (chiS T) := by
    -- Expand innerProduct and uniformWeight first so f x * f x becomes visible
    simp_rw [innerProduct, expect, uniformWeight]
    -- Now rewrite f(x)*f(x) using walsh_expansion
    simp_rw [show ∀ x : BoolCube n, f x * f x =
        (∑ S : Finset (Fin n), fourierCoeff f S * chiS S x) *
        (∑ T : Finset (Fin n), fourierCoeff f T * chiS T x) from fun x => by
      rw [← walsh_expansion f x]]
    -- Goal: 2⁻¹^n * ∑_x (∑_S ...) * (∑_T ...) = ∑_S ∑_T f̂S * f̂T * (2⁻¹^n * ∑_x χSx * χTx)
    -- Use the rearrangement:
    rw [show (2:ℝ)⁻¹^n * ∑ x : BoolCube n,
        (∑ S : Finset (Fin n), fourierCoeff f S * chiS S x) *
        (∑ T : Finset (Fin n), fourierCoeff f T * chiS T x) =
        ∑ S : Finset (Fin n), ∑ T : Finset (Fin n),
          fourierCoeff f S * fourierCoeff f T * ((2:ℝ)⁻¹^n * ∑ x : BoolCube n, chiS S x * chiS T x) from by
      -- Step 1: move 2⁻¹^n inside x-sum
      rw [Finset.mul_sum]
      -- Goal: ∑_x 2⁻¹^n * ((∑_S ...) * (∑_T ...)) = ∑_S ∑_T f̂S * f̂T * (...)
      -- Step 2: per x, expand products of sums and collect:
      -- ∑_x 2⁻¹^n * (∑_S ∑_T f̂S * χSx * (f̂T * χTx)) = ∑_S ∑_T f̂S * f̂T * (2⁻¹^n * ∑_x χSx*χTx)
      -- Step 2a: expand per-x product to ∑_x ∑_S ∑_T
      rw [show ∑ x : BoolCube n, (2:ℝ)⁻¹^n *
          ((∑ S : Finset (Fin n), fourierCoeff f S * chiS S x) *
          (∑ T : Finset (Fin n), fourierCoeff f T * chiS T x)) =
          ∑ x : BoolCube n, ∑ S : Finset (Fin n), ∑ T : Finset (Fin n),
            (2:ℝ)⁻¹^n * (fourierCoeff f S * chiS S x * (fourierCoeff f T * chiS T x)) from by
        apply Finset.sum_congr rfl; intro x _
        rw [Finset.sum_mul, Finset.mul_sum]
        apply Finset.sum_congr rfl; intro S _
        rw [show (2:ℝ)⁻¹^n * (fourierCoeff f S * chiS S x * ∑ T, fourierCoeff f T * chiS T x) =
            ∑ T, (2:ℝ)⁻¹^n * (fourierCoeff f S * chiS S x * (fourierCoeff f T * chiS T x)) from by
          rw [show fourierCoeff f S * chiS S x * ∑ T, fourierCoeff f T * chiS T x =
              ∑ T, fourierCoeff f S * chiS S x * (fourierCoeff f T * chiS T x) from Finset.mul_sum _ _ _]
          rw [Finset.mul_sum]]]
      rw [Finset.sum_comm]
      apply Finset.sum_congr rfl; intro S _
      -- Step 2c: swap x and T
      rw [Finset.sum_comm]
      apply Finset.sum_congr rfl; intro T _
      -- Step 2d: factor out f̂S * f̂T
      rw [show ∑ x : BoolCube n, (2:ℝ)⁻¹^n * (fourierCoeff f S * chiS S x * (fourierCoeff f T * chiS T x)) =
          fourierCoeff f S * fourierCoeff f T * ((2:ℝ)⁻¹^n * ∑ x : BoolCube n, chiS S x * chiS T x) from by
        rw [show ∑ x : BoolCube n, (2:ℝ)⁻¹^n * (fourierCoeff f S * chiS S x * (fourierCoeff f T * chiS T x)) =
            ∑ x : BoolCube n, (fourierCoeff f S * fourierCoeff f T) * ((2:ℝ)⁻¹^n * (chiS S x * chiS T x)) from by
          apply Finset.sum_congr rfl; intro x _; ring]
        rw [← Finset.mul_sum, ← Finset.mul_sum]]]
  rw [expand]
  simp_rw [fourier_coeff_chi, mul_ite, mul_one, mul_zero]
  simp_rw [Finset.sum_ite_eq, Finset.mem_univ, if_true]
  apply Finset.sum_congr rfl; intro S _; ring

-- TCSlib.BooleanAnalysis.Basic:446
/-- **Plancherel's Identity**: `⟪f, g⟫ = ∑_{S ⊆ [n]} f̂(S)ĝ(S)`
  The sum of the products of Fourier coefficients equals the inner product -/
theorem plancherel (f g : BooleanFunc n) :
  innerProduct f g = ∑ S : Finset (Fin n), fourierCoeff f S * fourierCoeff g S := by
  -- Expand f and g, and use bilinearity + orthonormality
  have expand : innerProduct f g =
      ∑ S : Finset (Fin n), ∑ T : Finset (Fin n),
        fourierCoeff f S * fourierCoeff g T * innerProduct (chiS S) (chiS T) := by
    -- The exact same expansion logic you used in Parseval, just with `f(x) * g(x)`
    simp_rw [innerProduct, expect, uniformWeight]
    simp_rw [show ∀ x : BoolCube n, f x * g x =
        (∑ S : Finset (Fin n), fourierCoeff f S * chiS S x) *
        (∑ T : Finset (Fin n), fourierCoeff g T * chiS T x) from fun x => by
      rw [← walsh_expansion f x, ← walsh_expansion g x]]
    -- ... (Proceed with the exact same Finset sum rearrangement steps from parseval) ...
    rw [show (2:ℝ)⁻¹^n * ∑ x : BoolCube n,
        (∑ S : Finset (Fin n), fourierCoeff f S * chiS S x) *
        (∑ T : Finset (Fin n), fourierCoeff g T * chiS T x) =
        ∑ S : Finset (Fin n), ∑ T : Finset (Fin n),
          fourierCoeff f S * fourierCoeff g T * ((2:ℝ)⁻¹^n * ∑ x : BoolCube n, chiS S x * chiS T x) from by
      -- Step 1: move 2⁻¹^n inside x-sum
      rw [Finset.mul_sum]
      rw [show ∑ x : BoolCube n, (2:ℝ)⁻¹^n *
          ((∑ S : Finset (Fin n), fourierCoeff f S * chiS S x) *
          (∑ T : Finset (Fin n), fourierCoeff g T * chiS T x)) =
          ∑ x : BoolCube n, ∑ S : Finset (Fin n), ∑ T : Finset (Fin n),
            (2:ℝ)⁻¹^n * (fourierCoeff f S * chiS S x * (fourierCoeff g T * chiS T x)) from by
        apply Finset.sum_congr rfl; intro x _
        rw [Finset.sum_mul, Finset.mul_sum]
        apply Finset.sum_congr rfl; intro S _
        rw [show (2:ℝ)⁻¹^n * (fourierCoeff f S * chiS S x * ∑ T, fourierCoeff g T * chiS T x) =
            ∑ T, (2:ℝ)⁻¹^n * (fourierCoeff f S * chiS S x * (fourierCoeff g T * chiS T x)) from by
          rw [show fourierCoeff f S * chiS S x * ∑ T, fourierCoeff g T * chiS T x =
              ∑ T, fourierCoeff f S * chiS S x * (fourierCoeff g T * chiS T x) from Finset.mul_sum _ _ _]
          rw [Finset.mul_sum]]]
      rw [Finset.sum_comm]
      apply Finset.sum_congr rfl; intro S _
      -- Step 2c: swap x and T
      rw [Finset.sum_comm]
      apply Finset.sum_congr rfl; intro T _
      rw [show ∑ x : BoolCube n, (2:ℝ)⁻¹^n * (fourierCoeff f S * chiS S x * (fourierCoeff g T * chiS T x)) =
          fourierCoeff f S * fourierCoeff g T * ((2:ℝ)⁻¹^n * ∑ x : BoolCube n, chiS S x * chiS T x) from by
        rw [show ∑ x : BoolCube n, (2:ℝ)⁻¹^n * (fourierCoeff f S * chiS S x * (fourierCoeff g T * chiS T x)) =
            ∑ x : BoolCube n, (fourierCoeff f S * fourierCoeff g T) * ((2:ℝ)⁻¹^n * (chiS S x * chiS T x)) from by
          apply Finset.sum_congr rfl; intro x _; ring]
        rw [← Finset.mul_sum, ← Finset.mul_sum]]]
  rw [expand]
  simp_rw [fourier_coeff_chi, mul_ite, mul_one, mul_zero]
  simp_rw [Finset.sum_ite_eq, Finset.mem_univ, if_true]

-- TCSlib.BooleanAnalysis.Basic:750
/-- The **noise operator** `T_ρ` with noise rate `ρ ∈ [-1, 1]`:
  `T_ρ f(x) = 𝔼_y[f(y)]` where each coordinate of `y` independently equals
  `x_i` with probability `(1+ρ)/2` and `¬x_i` with probability `(1-ρ)/2`.

  In the Fourier domain: `(T_ρ f)̂(S) = ρ^{|S|} · f̂(S)`.

**Source:** [OD14, §2.4]. -/
noncomputable def noiseOp (ρ : ℝ) (f : BooleanFunc n) : BooleanFunc n :=
  fun x ↦ ∑ S : Finset (Fin n), ρ ^ S.card * fourierCoeff f S * chiS S x

-- TCSlib.BooleanAnalysis.Basic:760
/-- **Noise operator in Fourier domain**: `(T_ρ f)̂(S) = ρ^{|S|} · f̂(S)`.

**Source:** [OD14, §2.4]. -/
theorem noiseOp_fourier (ρ : ℝ) (f : BooleanFunc n) (S : Finset (Fin n)) :
    fourierCoeff (noiseOp ρ f) S = ρ ^ S.card * fourierCoeff f S := by
  -- ⟨T_ρ f, χ_S⟩ = 2⁻ⁿ ∑_x (∑_T ρ^|T| f̂(T) χ_T(x)) * χ_S(x)
  --              = ∑_T ρ^|T| f̂(T) * ⟨χ_T, χ_S⟩ = ρ^|S| f̂(S)
  simp only [fourierCoeff, innerProduct, expect, uniformWeight, noiseOp]
  -- After unfolding: goal has (2⁻ⁿ * ∑ y f(y) χ_T(y)) for fourierCoeff f T
  -- Manipulate directly
  -- Goal: 2⁻¹^n * ∑_x (∑_T ρ^T.card * (2⁻¹^n * ∑_y f_y * χ_T_y) * χ_T_x) * χ_S_x
  --     = ρ^S.card * (2⁻¹^n * ∑_y f_y * χ_S_y)
  rw [show (2:ℝ)⁻¹^n * ∑ x : BoolCube n,
      (∑ T : Finset (Fin n), ρ ^ T.card * (2⁻¹^n * ∑ y : BoolCube n, f y * chiS T y) * chiS T x) * chiS S x =
      ∑ T : Finset (Fin n), ρ ^ T.card * (2⁻¹^n * ∑ y : BoolCube n, f y * chiS T y) *
        ((2:ℝ)⁻¹^n * ∑ x : BoolCube n, chiS T x * chiS S x) from by
    -- Step 1: distribute 2⁻¹^n over x-sum
    rw [show (2:ℝ)⁻¹^n * ∑ x : BoolCube n,
        (∑ T : Finset (Fin n), ρ ^ T.card * (2⁻¹^n * ∑ y : BoolCube n, f y * chiS T y) * chiS T x) * chiS S x =
        ∑ x : BoolCube n, (2:ℝ)⁻¹^n *
        ((∑ T : Finset (Fin n), ρ ^ T.card * (2⁻¹^n * ∑ y : BoolCube n, f y * chiS T y) * chiS T x) * chiS S x) from by
      rw [Finset.mul_sum]]
    -- Step 2: distribute over T-sum and rearrange
    rw [show ∑ x : BoolCube n, (2:ℝ)⁻¹^n *
        ((∑ T : Finset (Fin n), ρ ^ T.card * (2⁻¹^n * ∑ y : BoolCube n, f y * chiS T y) * chiS T x) * chiS S x) =
        ∑ x : BoolCube n, ∑ T : Finset (Fin n),
          ρ ^ T.card * (2⁻¹^n * ∑ y : BoolCube n, f y * chiS T y) *
          ((2:ℝ)⁻¹^n * (chiS T x * chiS S x)) from by
      apply Finset.sum_congr rfl; intro x _
      rw [show (2:ℝ)⁻¹^n *
          ((∑ T : Finset (Fin n), ρ ^ T.card * (2⁻¹^n * ∑ y : BoolCube n, f y * chiS T y) * chiS T x) * chiS S x) =
          ∑ T : Finset (Fin n), ρ ^ T.card * (2⁻¹^n * ∑ y : BoolCube n, f y * chiS T y) *
          ((2:ℝ)⁻¹^n * (chiS T x * chiS S x)) from by
        rw [Finset.sum_mul]
        simp_rw [Finset.mul_sum]
        apply Finset.sum_congr rfl; intro T _; ring]]
    -- Step 3: swap x and T sums
    rw [Finset.sum_comm]
    apply Finset.sum_congr rfl; intro T _
    -- Step 4: factor out ρ^T.card * f̂(T)
    rw [show ∑ x : BoolCube n, ρ ^ T.card * (2⁻¹^n * ∑ y : BoolCube n, f y * chiS T y) *
        ((2:ℝ)⁻¹^n * (chiS T x * chiS S x)) =
        ρ ^ T.card * (2⁻¹^n * ∑ y : BoolCube n, f y * chiS T y) *
        ((2:ℝ)⁻¹^n * ∑ x, chiS T x * chiS S x) from by
      rw [show ∑ x : BoolCube n, ρ ^ T.card * (2⁻¹^n * ∑ y : BoolCube n, f y * chiS T y) *
          ((2:ℝ)⁻¹^n * (chiS T x * chiS S x)) =
          ∑ x : BoolCube n, (ρ ^ T.card * (2⁻¹^n * ∑ y : BoolCube n, f y * chiS T y) * (2:ℝ)⁻¹^n) *
          (chiS T x * chiS S x) from by
        apply Finset.sum_congr rfl; intro x _; ring]
      rw [← Finset.mul_sum]; ring]]
  simp_rw [show ∀ T : Finset (Fin n),
      (2:ℝ)⁻¹^n * ∑ x, chiS T x * chiS S x = if T = S then 1 else 0 from fun T => by
    rw [show (2:ℝ)⁻¹^n * ∑ x, chiS T x * chiS S x =
        innerProduct (chiS T) (chiS S) from by simp [innerProduct, expect, uniformWeight]]
    exact fourier_coeff_chi T S]
  simp only [mul_ite, mul_one, mul_zero, Finset.sum_ite_eq', Finset.mem_univ, if_true]

-- TCSlib.BooleanAnalysis.Basic:817
/-- The noise operator is self-adjoint. -/
lemma noiseOp_self_adjoint (ρ : ℝ) (f g : BooleanFunc n) :
    innerProduct (noiseOp ρ f) g = innerProduct f (noiseOp ρ g) := by
  calc
    innerProduct (noiseOp ρ f) g
      = ∑ S : Finset (Fin n), fourierCoeff (noiseOp ρ f) S * fourierCoeff g S := by
        rw [plancherel]

    _ = ∑ S : Finset (Fin n), (ρ ^ S.card * fourierCoeff f S) * fourierCoeff g S := by
        -- Apply the multiplier property to every term in the sum
        apply Finset.sum_congr rfl
        intro S _
        rw [noiseOp_fourier]

    _ = ∑ S : Finset (Fin n), fourierCoeff f S * (ρ ^ S.card * fourierCoeff g S) := by
        -- Rearrange the multiplication (associativity and commutativity)
        apply Finset.sum_congr rfl
        intro S _
        ring

    _ = ∑ S : Finset (Fin n), fourierCoeff f S * fourierCoeff (noiseOp ρ g) S := by
        -- Fold the multiplier property back up for g
        apply Finset.sum_congr rfl
        intro S _
        rw [noiseOp_fourier]

    _ = innerProduct f (noiseOp ρ g) := by
        -- Apply Plancherel in reverse
        rw [← plancherel]

-- TCSlib.BooleanAnalysis.Basic:919
/-- The inner product is symmetric. -/
lemma innerProduct_comm (f g : BooleanFunc n) :
    innerProduct f g = innerProduct g f := by
  simp [innerProduct, expect, mul_comm]

-- TCSlib.BooleanAnalysis.Basic:1016
/-- `boolToSign` negates under `Bool.not`. -/
lemma boolToSign_not (b : Bool) : boolToSign (!b) = -boolToSign b := by
  cases b <;> simp [boolToSign]

end BooleanAnalysis

namespace BooleanAnalysis.ThresholdFunctions

variable {n : ℕ}

-- TCSlib.BooleanAnalysis.ThresholdFunctions.Basic:232
/-- The uniform expectation of a constant function is that constant. -/
lemma expect_const (c : ℝ) : expect (fun _ : BoolCube n ↦ c) = c := by
  rw [expect_eq_fintypeExpect]
  exact Fintype.expect_const c

-- TCSlib.BooleanAnalysis.ThresholdFunctions.Basic:238
/-- The uniform expectation is additive. -/
lemma expect_add (f g : BooleanFunc n) :
    expect (fun x ↦ f x + g x) = expect f + expect g := by
  simp only [expect, Finset.sum_add_distrib, mul_add]

-- TCSlib.BooleanAnalysis.ThresholdFunctions.Basic:243
/-- The uniform expectation commutes with scalar multiplication. -/
lemma expect_const_mul (c : ℝ) (f : BooleanFunc n) :
    expect (fun x ↦ c * f x) = c * expect f := by
  simp only [expect, ← Finset.mul_sum]
  ring

end BooleanAnalysis.ThresholdFunctions

namespace Bonami

open BooleanAnalysis

-- TCSlib.BooleanAnalysis.Hypercontractivity.Decomposition:22
/-- Restricts a Boolean function by fixing its final coordinate.

**Source:** [OD14, Cor. 9.6 (proof)]. -/
noncomputable def restrictLast {n : ℕ} (f : BooleanFunc (n + 1)) (b : Bool) : BooleanFunc n :=
  fun x => f (Fin.snoc x b)

-- TCSlib.BooleanAnalysis.Hypercontractivity.Decomposition:28
/-- Defines the average of a Boolean function over its final coordinate.

**Source:** [OD14, Cor. 9.6 (proof)]. -/
noncomputable def avgLast {n : ℕ} (f : BooleanFunc (n + 1)) : BooleanFunc n :=
  fun x => (restrictLast f false x + restrictLast f true x) / 2

-- TCSlib.BooleanAnalysis.Hypercontractivity.Decomposition:34
/-- Defines the half-difference of a Boolean function over its final coordinate.

**Source:** [OD14, Cor. 9.6 (proof)]. -/
noncomputable def diffLast {n : ℕ} (f : BooleanFunc (n + 1)) : BooleanFunc n :=
  fun x => (restrictLast f false x - restrictLast f true x) / 2

-- TCSlib.BooleanAnalysis.Hypercontractivity.Decomposition:56
/-- Splits a sum over an `(n + 1)`-dimensional Boolean cube by its final coordinate.

**Source:** [OD14, Cor. 9.6 (proof)]. -/
lemma sum_boolCube_succ {n : ℕ} (φ : BoolCube (n + 1) → ℝ) :
    ∑ x : BoolCube (n + 1), φ x =
    ∑ x : BoolCube n, φ (Fin.snoc x false) + ∑ x : BoolCube n, φ (Fin.snoc x true) := by
  have h_split :
      ∑ x : BoolCube (n + 1), φ x = ∑ x : BoolCube n × Bool, φ (Fin.snoc x.1 x.2) := by
    apply Finset.sum_bij (fun x _ => (Fin.init x, x (Fin.last n)))
    · simp +zetaDelta at *
    · simp +contextual [funext_iff]
      exact fun a₁ a₂ h₁ h₂ x => by
        cases x using Fin.lastCases <;> simp_all +decide [Fin.init]
    · intro b hb
      use Fin.snoc b.1 b.2
      aesop
    · aesop
  simp_all +decide [← Finset.sum_add_distrib]
  erw [Finset.sum_product]
  exact Finset.sum_congr rfl fun _ _ => by rw [Finset.sum_eq_add] <;> aesop

-- TCSlib.BooleanAnalysis.Hypercontractivity.Decomposition:77
/-- Computes the uniform weight of an `(n + 1)`-dimensional Boolean cube.

**Source:** [OD14, Cor. 9.6 (proof)]. -/
lemma uniformWeight_succ (n : ℕ) :
    uniformWeight (n + 1) = uniformWeight n / 2 := by
  simp [uniformWeight, pow_succ]
  ring

-- TCSlib.BooleanAnalysis.Hypercontractivity.Decomposition:85
/-- Identifies Fourier coefficients of the final-coordinate average with lifted coefficients.

**Source:** [OD14, Cor. 9.6 (proof)]. -/
lemma fourierCoeff_avgLast {n : ℕ} (f : BooleanFunc (n + 1)) (S : Finset (Fin n)) :
    BooleanAnalysis.fourierCoeff (avgLast f) S =
      BooleanAnalysis.fourierCoeff f (S.image Fin.castSucc) := by
  unfold avgLast
  simp +decide only [BooleanAnalysis.fourierCoeff]
  ring_nf
  unfold innerProduct
  simp +decide only [one_div, mul_comm]
  ring_nf
  unfold expect
  simp +decide only [chiS, restrictLast, one_div, mul_comm, Finset.sum_add_distrib,
    Finset.mul_sum _ _ _, mul_left_comm]
  ring_nf
  rw [add_comm 1 n, uniformWeight_succ, ← mul_add, sum_boolCube_succ]
  ring_nf
  simp +decide [mul_comm, mul_left_comm, Finset.mul_sum _ _ _]

-- TCSlib.BooleanAnalysis.Hypercontractivity.Decomposition:105
/-- The Fourier coefficient of `diffLast f` at `S` is the lifted coefficient containing
the final coordinate.

**Source:** [OD14, Cor. 9.6 (proof)]. -/
lemma fourierCoeff_diffLast {n : ℕ} (f : BooleanFunc (n + 1)) (S : Finset (Fin n)) :
    BooleanAnalysis.fourierCoeff (diffLast f) S =
      BooleanAnalysis.fourierCoeff f (S.image Fin.castSucc ∪ {Fin.last n}) := by
  unfold diffLast BooleanAnalysis.fourierCoeff innerProduct expect chiS restrictLast
  rw [uniformWeight_succ]
  rw [show (Finset.univ : Finset (Fin (n + 1) → Bool)) =
    Finset.image (fun x : Fin n → Bool => Fin.snoc x Bool.false) Finset.univ ∪
      Finset.image (fun x : Fin n → Bool => Fin.snoc x Bool.true) Finset.univ from ?_,
    Finset.sum_union]
  · rw [Finset.sum_image, Finset.sum_image] <;>
      norm_num [Finset.prod_union, Finset.prod_image, boolToSign]
    ring_nf
    · simp +decide only [mul_assoc, Finset.sum_add_distrib, Finset.sum_mul _ _ _]
      rw [mul_add]
    · exact fun x y h => by simpa using congrArg Fin.init h
    · exact fun x y h => by simpa using congrArg Fin.init h
  · norm_num [Finset.disjoint_left]
  · ext x
    by_cases hx : x (Fin.last n) <;>
      simp +decide only [Finset.mem_univ, Finset.mem_union, Finset.mem_image, true_and, true_iff]
    · exact Or.inr ⟨fun i => x i.castSucc, by
        ext i
        cases i using Fin.lastCases <;> aesop⟩
    · exact Or.inl ⟨fun i => x i.castSucc, by
        ext i
        cases i using Fin.lastCases <;> aesop⟩

-- TCSlib.BooleanAnalysis.Hypercontractivity.Decomposition:136
/-- Expresses expectation on an `(n + 1)`-cube as the average over the two restrictions.

**Source:** [OD14, Cor. 9.6 (proof)]. -/
lemma expect_succ_eq {n : ℕ} (φ : BooleanFunc (n + 1)) :
    expect φ = (expect (restrictLast φ false) + expect (restrictLast φ true)) / 2 := by
  unfold expect restrictLast
  rw [sum_boolCube_succ, uniformWeight_succ]
  ring

end Bonami

namespace OneBit

open BooleanAnalysis Real Bonami

-- TCSlib.BooleanAnalysis.Hypercontractivity.OneBit:15
private lemma boolCube1_univ :
    (Finset.univ : Finset (BoolCube 1)) =
    {fun _ => false, fun _ => true} := by decide

-- TCSlib.BooleanAnalysis.Hypercontractivity.OneBit:19
private lemma finsetFin1_univ :
    (Finset.univ : Finset (Finset (Fin 1))) = {∅, {0}} := by decide

-- TCSlib.BooleanAnalysis.Hypercontractivity.OneBit:22
private lemma boolCube1_ne :
    (fun _ : Fin 1 => false) ≠ (fun _ : Fin 1 => true) := by decide

-- TCSlib.BooleanAnalysis.Hypercontractivity.OneBit:25
private lemma finsetFin1_ne : (∅ : Finset (Fin 1)) ≠ {0} := by decide

-- TCSlib.BooleanAnalysis.Hypercontractivity.OneBit:27
lemma one_bit_val_false (f : BooleanFunc 1) :
    f (fun _ => false) = BooleanAnalysis.fourierCoeff f ∅ + BooleanAnalysis.fourierCoeff f {⟨0, by omega⟩} := by
  conv_lhs => rw [walsh_expansion f]
  conv_lhs => rw [show (Finset.univ : Finset (Finset (Fin 1))) = {∅, {0}} from finsetFin1_univ]
  rw [Finset.sum_pair finsetFin1_ne]
  simp [chiS, boolToSign]

-- TCSlib.BooleanAnalysis.Hypercontractivity.OneBit:34
lemma one_bit_val_true (f : BooleanFunc 1) :
    f (fun _ => true) = BooleanAnalysis.fourierCoeff f ∅ - BooleanAnalysis.fourierCoeff f {⟨0, by omega⟩} := by
  conv_lhs => rw [walsh_expansion f]
  conv_lhs => rw [show (Finset.univ : Finset (Finset (Fin 1))) = {∅, {0}} from finsetFin1_univ]
  rw [Finset.sum_pair finsetFin1_ne]
  simp [chiS, boolToSign]; ring

-- TCSlib.BooleanAnalysis.Hypercontractivity.OneBit:41
lemma expect_abs_rpow_one_bit (p : ℝ) (f : BooleanFunc 1) :
    BooleanAnalysis.expect (fun x => |f x| ^ p) =
    (|BooleanAnalysis.fourierCoeff f ∅ + BooleanAnalysis.fourierCoeff f {⟨0, by omega⟩}| ^ p +
     |BooleanAnalysis.fourierCoeff f ∅ - BooleanAnalysis.fourierCoeff f {⟨0, by omega⟩}| ^ p) / 2 := by
  unfold BooleanAnalysis.expect uniformWeight
  conv_lhs => rw [show (Finset.univ : Finset (BoolCube 1)) = {fun _ => false, fun _ => true}
    from boolCube1_univ]
  rw [Finset.sum_pair boolCube1_ne]
  simp only [one_bit_val_false, one_bit_val_true]
  norm_num; ring

end OneBit

namespace SimpleHypercontractivity

open BooleanAnalysis MeasureTheory Set Filter Real Bonami
variable {n : ℕ}

-- TCSlib.BooleanAnalysis.Hypercontractivity.EvenMoments:15
lemma chiS_snoc_castSucc {n : ℕ} (S : Finset (Fin n)) (x : BoolCube n) (b : Bool) :
    chiS (S.image Fin.castSucc) (Fin.snoc x b) = chiS S x := by
  unfold chiS; simp_all only [Fin.castSucc_inj, implies_true, injOn_of_eq_iff_eq, Finset.prod_image, Fin.snoc_castSucc];

-- TCSlib.BooleanAnalysis.Hypercontractivity.EvenMoments:19
lemma chiS_snoc_with_last {n : ℕ} (S : Finset (Fin n)) (x : BoolCube n) (b : Bool) :
    chiS (S.image Fin.castSucc ∪ {Fin.last n}) (Fin.snoc x b) = boolToSign b * chiS S x := by
  unfold chiS; simp +decide only [Finset.union_singleton, Finset.mem_image, Fin.castSucc_ne_last,
    and_false, exists_false, not_false_eq_true, Finset.prod_insert, Fin.snoc_last, Fin.castSucc_inj,
    implies_true, injOn_of_eq_iff_eq, Finset.prod_image, Fin.snoc_castSucc] ;

-- TCSlib.BooleanAnalysis.Hypercontractivity.EvenMoments:25
lemma finset_fin_succ_sum_partition {n : ℕ} (φ : Finset (Fin (n + 1)) → ℝ) :
    ∑ S : Finset (Fin (n + 1)), φ S =
    ∑ T : Finset (Fin n), φ (T.image Fin.castSucc) +
    ∑ T : Finset (Fin n), φ (T.image Fin.castSucc ∪ {Fin.last n}) := by
  
  have h_partition : Finset.univ = Finset.image (fun T : Finset (Fin n) => T.image Fin.castSucc) (Finset.univ : Finset (Finset (Fin n))) ∪ Finset.image (fun T : Finset (Fin n) => T.image Fin.castSucc ∪ {Fin.last n}) (Finset.univ : Finset (Finset (Fin n))) := by
    ext S;
    by_cases h : Fin.last n ∈ S <;> simp +decide only [Finset.mem_univ, Finset.union_singleton,
      Finset.mem_union, Finset.mem_image, true_and, true_iff];
    · refine Or.inr ⟨ Finset.univ.filter fun i => Fin.castSucc i ∈ S, ?_ ⟩;
      ext i; simp [Finset.mem_insert, Finset.mem_image];
      exact ⟨ fun hi => hi.elim ( fun hi => hi.symm ▸ h ) fun ⟨ a, ha₁, ha₂ ⟩ => ha₂ ▸ ha₁, fun hi => if hi' : i = Fin.last n then Or.inl hi' else Or.inr ⟨ ⟨ i.val, lt_of_le_of_ne ( Fin.le_last _ ) ( by simpa [ Fin.ext_iff ] using hi' ) ⟩, by simpa [ Fin.ext_iff ] using hi, rfl ⟩ ⟩;
    · refine' Or.inl ⟨ Finset.univ.filter fun i => Fin.castSucc i ∈ S, _ ⟩;
      ext i; simp [Finset.mem_image];
      exact ⟨ fun ⟨ a, ha₁, ha₂ ⟩ => ha₂ ▸ ha₁, fun hi => by cases i using Fin.lastCases <;> aesop ⟩;
  rw [ h_partition, Finset.sum_union ] <;> norm_num [ Finset.disjoint_right ];
  · rw [ Finset.sum_image, Finset.sum_image ];
    · intro T hT T' hT' h_eq; simp_all +decide [ Finset.ext_iff ] ;
      intro a; specialize h_eq ( Fin.castSucc a ) ; aesop;
    · intro T hT T' hT' h_eq; simp_all +decide [ Finset.ext_iff ] ;
      intro a; specialize h_eq ( Fin.castSucc a ) ; aesop;
  · intro a x H; replace H := Finset.ext_iff.mp H ( Fin.last n ) ; simp +decide at H;

-- TCSlib.BooleanAnalysis.Hypercontractivity.EvenMoments:48
lemma card_image_castSucc {n : ℕ} (S : Finset (Fin n)) :
    (S.image Fin.castSucc).card = S.card := by
  exact Finset.card_image_of_injective S (Fin.castSucc_injective n)

-- TCSlib.BooleanAnalysis.Hypercontractivity.EvenMoments:52
lemma card_image_castSucc_union_last {n : ℕ} (S : Finset (Fin n)) :
    (S.image Fin.castSucc ∪ {Fin.last n}).card = S.card + 1 := by
  rw [ Finset.card_union, Finset.card_image_of_injective ] <;> norm_num [ Function.Injective ]

-- TCSlib.BooleanAnalysis.Hypercontractivity.EvenMoments:56
lemma noiseOp_snoc {n : ℕ} (ρ : ℝ) (f : BooleanFunc (n + 1)) (x : BoolCube n) (b : Bool) :
    noiseOp ρ f (Fin.snoc x b) =
    noiseOp ρ (avgLast f) x + boolToSign b * ρ * noiseOp ρ (diffLast f) x := by
  unfold noiseOp
  rw [finset_fin_succ_sum_partition]
  apply congrArg₂ (fun u v : ℝ ↦ u + v)
  · apply Finset.sum_congr rfl
    intro T _
    rw [← fourierCoeff_avgLast, card_image_castSucc, chiS_snoc_castSucc]
  · rw [Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro T _
    rw [← fourierCoeff_diffLast, card_image_castSucc_union_last,
      chiS_snoc_with_last, pow_succ]
    ring

-- TCSlib.BooleanAnalysis.Hypercontractivity.EvenMoments:72
lemma expect_rpow_abs_nonneg (p : ℝ) (f : BooleanFunc n) :
    0 ≤ BooleanAnalysis.expect (fun x => |f x| ^ p) := by
  unfold BooleanAnalysis.expect uniformWeight
  apply mul_nonneg (pow_nonneg (by positivity) _)
  apply Finset.sum_nonneg
  intro x _; positivity

-- TCSlib.BooleanAnalysis.Hypercontractivity.EvenMoments:79
lemma noiseOp_compose (ρ σ : ℝ) (f : BooleanFunc n) :
    noiseOp ρ (noiseOp σ f) = noiseOp (ρ * σ) f := by
  ext x
  simp only [noiseOp]
  congr 1; ext S
  rw [noiseOp_fourier]; ring

end SimpleHypercontractivity

namespace GeneralHypercontractivity

open BooleanAnalysis OneBit Bonami SimpleHypercontractivity Real
variable {n : ℕ}

-- TCSlib.BooleanAnalysis.Hypercontractivity.General:15
noncomputable def noiseKernel (ρ : ℝ) {n : ℕ} (x y : BoolCube n) : ℝ :=
  ∏ i : Fin n, (1 + ρ * boolToSign (x i) * boolToSign (y i)) / 2

-- TCSlib.BooleanAnalysis.Hypercontractivity.General:18
lemma noiseKernel_nonneg {ρ : ℝ} (hρ0 : 0 ≤ ρ) (hρ1 : ρ ≤ 1)
    (x y : BoolCube n) : 0 ≤ noiseKernel ρ x y := by
  refine Finset.prod_nonneg fun i _ ↦ ?_
  cases x i <;> cases y i <;> norm_num [boolToSign] <;> nlinarith

-- TCSlib.BooleanAnalysis.Hypercontractivity.General:23
lemma sum_fourier_kernel (ρ : ℝ) (x y : BoolCube n) :
    ∑ S : Finset (Fin n), ρ ^ S.card * chiS S x * chiS S y =
    ∏ i : Fin n, (1 + ρ * boolToSign (x i) * boolToSign (y i)) := by
  have h_prod_sum : ∏ i : Fin n, (1 + ρ * boolToSign (x i) * boolToSign (y i)) =
      ∑ S : Finset (Fin n), ∏ i ∈ S, (ρ * boolToSign (x i) * boolToSign (y i)) := by
    simp +decide [add_comm, Finset.prod_add]
  rw [h_prod_sum, Finset.sum_congr rfl]
  intros; simp_all +decide [Finset.prod_mul_distrib, chiS]

-- TCSlib.BooleanAnalysis.Hypercontractivity.General:32
lemma noiseOp_eq_kernel_sum (ρ : ℝ) (g : BooleanFunc n) (x : BoolCube n) :
    noiseOp ρ g x = ∑ y : BoolCube n, noiseKernel ρ x y * g y := by
  unfold noiseOp noiseKernel BooleanAnalysis.fourierCoeff BooleanAnalysis.innerProduct
  simp +decide [BooleanAnalysis.expect]
  unfold uniformWeight
  simp +decide [div_eq_inv_mul, Finset.mul_sum, mul_assoc, mul_comm, mul_left_comm]
  rw [Finset.sum_comm, Finset.sum_congr rfl]; intros; ring_nf
  rw [← sum_fourier_kernel]
  simp +decide [mul_assoc, mul_comm, mul_left_comm, Finset.mul_sum]

-- TCSlib.BooleanAnalysis.Hypercontractivity.General:42
lemma expect_succ_eq_iterated (h : BooleanFunc (n + 1)) :
    expect h = expect (fun x' =>
      (1/2 : ℝ) * (h (Fin.snoc x' false) + h (Fin.snoc x' true))) := by
  unfold expect
  rw [sum_boolCube_succ]
  norm_num [Finset.mul_sum, mul_add, mul_assoc, mul_left_comm,
            Finset.sum_add_distrib, uniformWeight_succ]
  ring_nf

-- TCSlib.BooleanAnalysis.Hypercontractivity.General:51
lemma norm_collapse_rpow (p : ℝ) (_hp : 0 < p) (f : BooleanFunc (n + 1)) :
    expect (fun x => |f x| ^ p) =
    expect (fun x' => (1/2 : ℝ) *
      (|f (Fin.snoc x' false)| ^ p + |f (Fin.snoc x' true)| ^ p)) := by
  convert expect_succ_eq_iterated _ using 1

-- TCSlib.BooleanAnalysis.Hypercontractivity.General:57
lemma noiseKernel_sum_right {ρ : ℝ} (_hρ0 : 0 ≤ ρ) (_hρ1 : ρ ≤ 1)
    (x : BoolCube n) : ∑ y : BoolCube n, noiseKernel ρ x y = 1 := by
  unfold noiseKernel;
  
  have h_factor : ∑ y : BoolCube n, (∏ i : Fin n, (1 + ρ * boolToSign (x i) * boolToSign (y i)) / 2) = ∏ i : Fin n, ∑ y : Bool, (1 + ρ * boolToSign (x i) * boolToSign y) / 2 := by
    exact Eq.symm (Fintype.prod_sum fun i j => (1 + ρ * boolToSign (x i) * boolToSign j) / 2);
  rw [ h_factor, Finset.prod_eq_one ] ; intros ; norm_num [ Finset.sum_div _ _ _, boolToSign ] ; ring

-- TCSlib.BooleanAnalysis.Hypercontractivity.General:65
lemma noiseKernel_sum_left {ρ : ℝ} (hρ0 : 0 ≤ ρ) (hρ1 : ρ ≤ 1)
    (y : BoolCube n) : ∑ x : BoolCube n, noiseKernel ρ x y = 1 := by
  convert noiseKernel_sum_right hρ0 hρ1 y using 1;
  unfold noiseKernel; congr; ext; ring_nf;
  ac_rfl

end GeneralHypercontractivity

namespace BooleanAnalysis.Hypercontractivity


-- TCSlib.BooleanAnalysis.Hypercontractivity.CubeBasic:125
/-- The indicator of a cube event is one on the event and zero elsewhere.
[OD14, §9.1] This reuses Mathlib's set indicator. -/
noncomputable def cubeIndicator {n : ℕ} (A : BoolCube n → Prop) : BooleanFunc n :=
  Set.indicator {x | A x} (fun _ => 1)

-- TCSlib.BooleanAnalysis.Hypercontractivity.CubeBasic:130
/-- Uniform event probability is the expectation of its indicator. [OD14, §9.1] -/
noncomputable def cubeProbability {n : ℕ} (A : BoolCube n → Prop) : ℝ :=
  expect (cubeIndicator A)

-- TCSlib.BooleanAnalysis.Hypercontractivity.CubeBasic:138
/-- The real-exponent `Lᵖ` expression on the uniform cube; applications use `p ≥ 1`.
[OD14, §9.5, Thms. 9.21–9.22] The raw formula is retained at every real exponent so the
reverse-hypercontractivity mean can reuse it without changing its boundary conventions. -/
noncomputable abbrev cubeLpNorm {n : ℕ} (p : ℝ) (f : BooleanFunc n) : ℝ :=
  (expect (fun x => |f x| ^ p)) ^ (1 / p)

end BooleanAnalysis.Hypercontractivity

namespace ReverseBonamiBeckner

open BooleanAnalysis Bonami OneBit SimpleHypercontractivity
variable {n : ℕ}

-- TCSlib.BooleanAnalysis.Hypercontractivity.ReverseBonamiBeckner:58
/-- Pointwise nonnegativity, the natural domain of reverse hypercontractivity.
[OD14, Exs. 10.6--10.9] -/
def IsNonnegative (f : BooleanFunc n) : Prop :=
  ∀ x, 0 ≤ f x

-- TCSlib.BooleanAnalysis.Hypercontractivity.ReverseBonamiBeckner:64
/-- The uniform `L^p` mean for finite real exponents. At `p = 0` this is the geometric mean; for
`p ≤ 0`, a function with a zero has mean zero. [OD14, Exs. 10.6--10.9]
The ordinary expression is shared with `Hypercontractivity.cubeLpNorm`. The source also
defines the `p = -∞` mean as the minimum; that endpoint is not represented here. -/
noncomputable def lpMean (p : ℝ) (f : BooleanFunc n) : ℝ :=
  if (∃ x, f x = 0) ∧ p ≤ 0 then 0
  else if p = 0 then Real.exp (expect (fun x ↦ Real.log |f x|))
  else BooleanAnalysis.Hypercontractivity.cubeLpNorm p f

-- TCSlib.BooleanAnalysis.Hypercontractivity.ReverseBonamiBeckner:73
/-- For positive exponents, `lpMean` is the usual power mean. -/
lemma lpMean_of_pos (p : ℝ) (hp : 0 < p) (f : BooleanFunc n) :
    lpMean p f = (expect (fun x ↦ |f x| ^ p)) ^ (1 / p) := by
  simp [lpMean, BooleanAnalysis.Hypercontractivity.cubeLpNorm, hp.ne', not_le.mpr hp]

-- TCSlib.BooleanAnalysis.Hypercontractivity.ReverseBonamiBeckner:78
/-- Power means with a positive exponent are nonnegative. -/
lemma lpMean_nonneg (p : ℝ) (hp : 0 < p) (f : BooleanFunc n) : 0 ≤ lpMean p f := by
  rw [lpMean_of_pos p hp]
  exact Real.rpow_nonneg (expect_rpow_abs_nonneg p f) _

-- TCSlib.BooleanAnalysis.Hypercontractivity.ReverseBonamiBeckner:83
/-- Power means with a positive exponent are monotone on nonnegative functions. -/
lemma lpMean_mono (p : ℝ) (hp : 0 < p) {f g : BooleanFunc n} (hf : IsNonnegative f)
    (hfg : ∀ x, f x ≤ g x) : lpMean p f ≤ lpMean p g := by
  have hg : ∀ x, 0 ≤ g x := fun x ↦ (hf x).trans (hfg x)
  rw [lpMean_of_pos p hp, lpMean_of_pos p hp]
  simp_rw [abs_of_nonneg (hf _), abs_of_nonneg (hg _)]
  refine Real.rpow_le_rpow
    (by
      rw [expect_eq_fintypeExpect]
      exact Finset.expect_nonneg fun x _ ↦ Real.rpow_nonneg (hf x) p) ?_ (by positivity)
  exact mul_le_mul_of_nonneg_left
    (Finset.sum_le_sum fun x _ ↦ Real.rpow_le_rpow (hf x) (hfg x) hp.le)
    (pow_nonneg (by norm_num) _)

-- TCSlib.BooleanAnalysis.Hypercontractivity.ReverseBonamiBeckner:97
/-- Power means with a positive exponent are homogeneous. -/
lemma lpMean_const_mul (p c : ℝ) (hp : 0 < p) (hc : 0 < c) (f : BooleanFunc n) :
    lpMean p (fun x ↦ c * f x) = c * lpMean p f := by
  have hE : expect (fun x ↦ |c * f x| ^ p) = c ^ p * expect (fun x ↦ |f x| ^ p) := by
    unfold expect
    simp_rw [abs_mul, abs_of_pos hc, Real.mul_rpow hc.le (abs_nonneg _), ← Finset.mul_sum]
    ring
  rw [lpMean_of_pos p hp, lpMean_of_pos p hp, hE,
    Real.mul_rpow (Real.rpow_nonneg hc.le p) (expect_rpow_abs_nonneg p f),
    ← Real.rpow_mul hc.le, mul_one_div, div_self hp.ne', Real.rpow_one]

-- TCSlib.BooleanAnalysis.Hypercontractivity.ReverseBonamiBeckner:108
/-- On the empty cube every mean is the single value of the function. -/
lemma lpMean_dim_zero (p : ℝ) (hp : 0 < p) (f : BooleanFunc 0) (hf : IsNonnegative f) :
    lpMean p f = f (fun i ↦ Fin.elim0 i) := by
  rw [lpMean_of_pos p hp]
  unfold expect uniformWeight
  norm_num
  change (|f (fun i ↦ Fin.elim0 i)| ^ p) ^ p⁻¹ = f (fun i ↦ Fin.elim0 i)
  rw [abs_of_nonneg (hf _), ← Real.rpow_mul (hf _), show p * p⁻¹ = 1 by field_simp,
    Real.rpow_one]

-- TCSlib.BooleanAnalysis.Hypercontractivity.ReverseBonamiBeckner:118
/-- Splitting off the last coordinate: an `L^p` mean on `n + 1` bits is the `L^p`
mean over the first `n` bits of the one-bit `L^p` means. -/
lemma lpMean_collapse_last (p : ℝ) (hp : 0 < p) (f : BooleanFunc (n + 1)) :
    lpMean p f =
      lpMean p (fun x : BoolCube n ↦
        lpMean p (fun y : BoolCube 1 ↦ f (Fin.snoc x (y 0)))) := by
  have hinner (x : BoolCube n) :
      0 ≤ expect (fun y : BoolCube 1 ↦ |f (Fin.snoc x (y 0))| ^ p) :=
    by
      rw [expect_eq_fintypeExpect]
      exact Finset.expect_nonneg fun y _ ↦ Real.rpow_nonneg (abs_nonneg _) p
  rw [lpMean_of_pos p hp, lpMean_of_pos p hp]
  simp_rw [lpMean_of_pos p hp, abs_of_nonneg (Real.rpow_nonneg (hinner _) _),
    ← Real.rpow_mul (hinner _), show 1 / p * p = 1 by field_simp, Real.rpow_one]
  rw [GeneralHypercontractivity.norm_collapse_rpow p hp f]
  congr 2 with x
  unfold expect uniformWeight
  rw [show (Finset.univ : Finset (BoolCube 1)) = {fun _ ↦ false, fun _ ↦ true} by decide,
    Finset.sum_pair (by decide)]
  norm_num

-- TCSlib.BooleanAnalysis.Hypercontractivity.ReverseBonamiBeckner:139
/-- Iterated means over two blocks of coordinates commute. -/
lemma lpMean_comm (p : ℝ) (hp : 0 < p) (F : BoolCube n → BoolCube 1 → ℝ) :
    lpMean p (fun x ↦ lpMean p (fun y ↦ F x y)) =
      lpMean p (fun y ↦ lpMean p (fun x ↦ F x y)) := by
  have hx (x : BoolCube n) : 0 ≤ expect (fun y : BoolCube 1 ↦ |F x y| ^ p) :=
    by
      rw [expect_eq_fintypeExpect]
      exact Finset.expect_nonneg fun y _ ↦ Real.rpow_nonneg (abs_nonneg _) p
  have hy (y : BoolCube 1) : 0 ≤ expect (fun x : BoolCube n ↦ |F x y| ^ p) :=
    by
      rw [expect_eq_fintypeExpect]
      exact Finset.expect_nonneg fun x _ ↦ Real.rpow_nonneg (abs_nonneg _) p
  simp_rw [lpMean_of_pos p hp, abs_of_nonneg (Real.rpow_nonneg (hx _) _),
    abs_of_nonneg (Real.rpow_nonneg (hy _) _), ← Real.rpow_mul (hx _), ← Real.rpow_mul (hy _),
    show 1 / p * p = 1 by field_simp, Real.rpow_one]
  congr 1
  unfold expect
  simp_rw [Finset.mul_sum]
  rw [Finset.sum_comm]
  simp_rw [← mul_assoc, mul_comm (uniformWeight n)]

-- TCSlib.BooleanAnalysis.Hypercontractivity.ReverseBonamiBeckner:162
/-- Fourier coefficients are homogeneous. -/
lemma fourierCoeff_const_mul (c : ℝ) (f : BooleanFunc n) (S : Finset (Fin n)) :
    BooleanAnalysis.fourierCoeff (fun x ↦ c * f x) S = c * BooleanAnalysis.fourierCoeff f S := by
  unfold BooleanAnalysis.fourierCoeff innerProduct expect
  simp_rw [mul_assoc, ← Finset.mul_sum]
  ring

-- TCSlib.BooleanAnalysis.Hypercontractivity.ReverseBonamiBeckner:169
/-- The noise operator is homogeneous. -/
lemma noiseOp_const_mul (ρ c : ℝ) (f : BooleanFunc n) :
    noiseOp ρ (fun x ↦ c * f x) = fun x ↦ c * noiseOp ρ f x := by
  funext x
  unfold noiseOp
  simp_rw [fourierCoeff_const_mul, Finset.mul_sum]
  exact Finset.sum_congr rfl fun S _ ↦ by ring

-- TCSlib.BooleanAnalysis.Hypercontractivity.ReverseBonamiBeckner:177
/-- On the empty cube the noise operator is the identity. -/
lemma noiseOp_dim_zero (ρ : ℝ) (f : BooleanFunc 0) : noiseOp ρ f = f := by
  funext x
  conv_rhs => rw [walsh_expansion f]
  refine Finset.sum_congr rfl fun S _ ↦ ?_
  obtain rfl : S = ∅ := Finset.eq_empty_of_forall_notMem fun i _ ↦ i.elim0
  simp

-- TCSlib.BooleanAnalysis.Hypercontractivity.ReverseBonamiBeckner:185
/-- The noise operator preserves nonnegativity, since its kernel is nonnegative. -/
lemma noiseOp_nonneg {ρ : ℝ} (hρ0 : 0 ≤ ρ) (hρ1 : ρ ≤ 1) {f : BooleanFunc n}
    (hf : IsNonnegative f) : IsNonnegative (noiseOp ρ f) := fun x ↦ by
  rw [GeneralHypercontractivity.noiseOp_eq_kernel_sum]
  exact Finset.sum_nonneg fun y _ ↦
    mul_nonneg (GeneralHypercontractivity.noiseKernel_nonneg hρ0 hρ1 x y) (hf y)

-- TCSlib.BooleanAnalysis.Hypercontractivity.ReverseBonamiBeckner:192
/-- The noise operator shrinks the coefficient of a one-bit affine function. -/
lemma noiseOp_affine_one_bit (ρ a : ℝ) :
    noiseOp ρ (fun x : BoolCube 1 ↦ 1 + a * boolToSign (x 0)) =
      fun x ↦ 1 + (ρ * a) * boolToSign (x 0) := by
  funext x
  unfold noiseOp
  rw [show (Finset.univ : Finset (Finset (Fin 1))) = {∅, {0}} by decide,
    Finset.sum_pair (by decide)]
  norm_num [BooleanAnalysis.fourierCoeff, innerProduct, expect, uniformWeight, chiS, boolToSign]
  repeat' first
    | rw [show (Finset.univ : Finset (BoolCube 1)) =
        {fun _ ↦ false, fun _ ↦ true} by decide]
    | rw [Finset.sum_pair (by decide)]
  cases hx : x 0 <;> norm_num [boolToSign] <;> ring

-- TCSlib.BooleanAnalysis.Hypercontractivity.ReverseBonamiBeckner:207
/-- The Fourier coefficients of the average of the two restrictions of the last bit. -/
lemma fourierCoeff_avgLast (f : BooleanFunc (n + 1)) (S : Finset (Fin n)) :
    BooleanAnalysis.fourierCoeff (avgLast f) S =
      (BooleanAnalysis.fourierCoeff (restrictLast f false) S + BooleanAnalysis.fourierCoeff (restrictLast f true) S) / 2 := by
  unfold BooleanAnalysis.fourierCoeff innerProduct expect avgLast
  ring_nf
  rw [Finset.sum_add_distrib, ← Finset.sum_mul, ← Finset.sum_mul]
  ring

-- TCSlib.BooleanAnalysis.Hypercontractivity.ReverseBonamiBeckner:216
/-- The Fourier coefficients of the difference of the two restrictions of the last bit. -/
lemma fourierCoeff_diffLast (f : BooleanFunc (n + 1)) (S : Finset (Fin n)) :
    BooleanAnalysis.fourierCoeff (diffLast f) S =
      (BooleanAnalysis.fourierCoeff (restrictLast f false) S - BooleanAnalysis.fourierCoeff (restrictLast f true) S) / 2 := by
  unfold BooleanAnalysis.fourierCoeff innerProduct expect diffLast
  ring_nf
  rw [Finset.sum_add_distrib, ← Finset.sum_mul, ← Finset.sum_mul]
  ring

-- TCSlib.BooleanAnalysis.Hypercontractivity.ReverseBonamiBeckner:225
/-- Noise on `n + 1` bits factors as noise on the last bit applied to the noised
restrictions of the first `n` bits. -/
lemma noiseOp_snoc_slice (ρ : ℝ) (f : BooleanFunc (n + 1)) (x : BoolCube n) (y : BoolCube 1) :
    noiseOp ρ f (Fin.snoc x (y 0)) =
      noiseOp ρ (fun t : BoolCube 1 ↦ noiseOp ρ (restrictLast f (t 0)) x) y := by
  have hy : y = Fin.snoc (fun i ↦ Fin.elim0 i) (y 0) := by
    funext i
    fin_cases i
    rfl
  conv_lhs => rw [noiseOp_snoc]
  conv_rhs => rw [hy, noiseOp_snoc, noiseOp_dim_zero, noiseOp_dim_zero]
  dsimp [avgLast, diffLast, restrictLast]
  unfold noiseOp
  simp_rw [fourierCoeff_avgLast, fourierCoeff_diffLast]
  simp only [show (Fin.snoc (fun i ↦ Fin.elim0 i) false : BoolCube 1) 0 = false from rfl,
    show (Fin.snoc (fun i ↦ Fin.elim0 i) true : BoolCube 1) 0 = true from rfl]
  ring_nf
  rw [Finset.sum_add_distrib, Finset.sum_add_distrib]
  repeat rw [← Finset.sum_mul]
  ring

-- TCSlib.BooleanAnalysis.Hypercontractivity.ReverseBonamiBeckner:248
/-- Newton's binomial series: for `|x| < 1` the function `(1 + x) ^ s` is the sum
of the generalized binomial series. -/
private lemma hasSum_choose_rpow {s x : ℝ} (hx : |x| < 1) :
    HasSum (fun k : ℕ ↦ Ring.choose s k * x ^ k) ((1 + x) ^ s) := by
  have hsum := (Real.one_add_rpow_hasFPowerSeriesOnBall_zero (a := s)).hasSum_sub
    (show x ∈ Metric.eball (0 : ℝ) 1 by
      simpa only [Metric.mem_eball, edist_dist, Real.dist_eq, sub_zero,
        ENNReal.ofReal_lt_one] using hx)
  convert! hsum using 1
  ext k
  simp [binomialSeries, mul_comm]

-- TCSlib.BooleanAnalysis.Hypercontractivity.ReverseBonamiBeckner:260
/-- The even part of the binomial series is summable. -/
private lemma summable_choose_even {s x : ℝ} (hx : |x| < 1) :
    Summable (fun k : ℕ ↦ Ring.choose s (2 * k) * x ^ (2 * k)) :=
  (hasSum_choose_rpow hx).summable.comp_injective
    (mul_right_injective₀ (by norm_num : (2 : ℕ) ≠ 0))

-- TCSlib.BooleanAnalysis.Hypercontractivity.ReverseBonamiBeckner:266
/-- Symmetrizing the binomial series kills the odd terms. -/
private lemma even_part_rpow_eq_tsum {s x : ℝ} (hx : |x| < 1) :
    ((1 + x) ^ s + (1 - x) ^ s) / 2 =
      ∑' k : ℕ, Ring.choose s (2 * k) * x ^ (2 * k) := by
  have hxneg : |-x| < 1 := by simpa using hx
  have hboth : HasSum
      (fun k : ℕ ↦ (Ring.choose s k * x ^ k + Ring.choose s k * (-x) ^ k) / 2)
      (((1 + x) ^ s + (1 + -x) ^ s) / 2) :=
    ((hasSum_choose_rpow hx).add (hasSum_choose_rpow hxneg)).div_const 2
  have heven := (summable_choose_even (s := s) hx).hasSum
  have hall : HasSum
      (fun k : ℕ ↦ (Ring.choose s k * x ^ k + Ring.choose s k * (-x) ^ k) / 2)
      ((∑' k : ℕ, Ring.choose s (2 * k) * x ^ (2 * k)) + 0) := by
    apply HasSum.even_add_odd
    · convert heven using 1
      funext k
      rw [Even.neg_pow (even_two.mul_right k)]
      ring
    · convert (hasSum_zero : HasSum (fun _ : ℕ ↦ (0 : ℝ)) 0) using 1
      funext k
      rw [show (-x) ^ (2 * k + 1) = -(x ^ (2 * k + 1)) by
        rw [pow_add, Even.neg_pow (even_two.mul_right k), pow_one]
        ring]
      ring
  rw [show 1 - x = 1 + -x by ring]
  simpa using hboth.unique hall

-- TCSlib.BooleanAnalysis.Hypercontractivity.ReverseBonamiBeckner:293
/-- The `L^s` moment of the one-bit function `1 + b χ`, for `|b| < 1`. -/
private lemma expect_abs_rpow_affine (s b : ℝ) (hb : |b| < 1) :
    expect (fun x : BoolCube 1 ↦ |1 + b * boolToSign (x 0)| ^ s) =
      ((1 + b) ^ s + (1 - b) ^ s) / 2 := by
  obtain ⟨hb1, hb2⟩ := abs_lt.mp hb
  set f : BooleanFunc 1 := fun x ↦ 1 + b * boolToSign (x 0) with hf_def
  have hfalse : (1 : ℝ) + b = BooleanAnalysis.fourierCoeff f ∅ + BooleanAnalysis.fourierCoeff f {⟨0, by omega⟩} := by
    rw [← OneBit.one_bit_val_false f, hf_def]
    norm_num [boolToSign]
  have htrue : (1 : ℝ) - b = BooleanAnalysis.fourierCoeff f ∅ - BooleanAnalysis.fourierCoeff f {⟨0, by omega⟩} := by
    rw [← OneBit.one_bit_val_true f, hf_def]
    norm_num [boolToSign]
    ring
  rw [OneBit.expect_abs_rpow_one_bit, show BooleanAnalysis.fourierCoeff f ∅ = 1 by linarith,
    show BooleanAnalysis.fourierCoeff f {⟨0, by omega⟩} = b by linarith,
    abs_of_pos (by linarith : (0:ℝ) < 1 + b), abs_of_pos (by linarith : (0:ℝ) < 1 - b)]

-- TCSlib.BooleanAnalysis.Hypercontractivity.ReverseBonamiBeckner:310
/-- The second generalized binomial coefficient. -/
private lemma ring_choose_two (s : ℝ) : Ring.choose s 2 = s * (s - 1) / 2 := by
  have h := Ring.choose_smul_choose (R := ℝ) s (show 1 ≤ 2 by omega)
  norm_num [nsmul_eq_mul, Ring.choose_one_right] at h ⊢
  linarith

-- TCSlib.BooleanAnalysis.Hypercontractivity.ReverseBonamiBeckner:316
/-- Two steps of Pascal's recurrence for generalized binomial coefficients. -/
private lemma ring_choose_even_succ (s : ℝ) (k : ℕ) :
    Ring.choose s (2 * (k + 1)) =
      Ring.choose s (2 * k) * (s - (2 * k : ℕ)) * (s - (2 * k + 1 : ℕ)) /
        (((2 * k + 1 : ℕ) : ℝ) * ((2 * k + 2 : ℕ) : ℝ)) := by
  have h1 := Ring.choose_smul_choose (R := ℝ) s (Nat.le_succ (2 * k))
  have h2 := Ring.choose_smul_choose (R := ℝ) s (Nat.le_succ (2 * k + 1))
  simp only [nsmul_eq_mul] at h1 h2
  norm_num at h1 h2 ⊢
  have h1' : Ring.choose s (2 * k + 1) =
      Ring.choose s (2 * k) * (s - 2 * (k : ℝ)) / (2 * (k : ℝ) + 1) :=
    (eq_div_iff (by positivity)).2 (by nlinarith [h1])
  have h2' : Ring.choose s (2 * k + 1 + 1) =
      Ring.choose s (2 * k + 1) * (s - (2 * (k : ℝ) + 1)) / (2 * (k : ℝ) + 2) :=
    (eq_div_iff (by positivity)).2 (by nlinarith [h2])
  rw [show 2 * (k + 1) = 2 * k + 1 + 1 by omega, h2', h1']
  field_simp

-- TCSlib.BooleanAnalysis.Hypercontractivity.ReverseBonamiBeckner:334
/-- For an exponent in `(0, 1)` all even generalized binomial coefficients past
the constant term are nonpositive. -/
private lemma ring_choose_even_nonpos (s : ℝ) (hs0 : 0 < s) (hs1 : s < 1) :
    ∀ k : ℕ, 1 ≤ k → Ring.choose s (2 * k) ≤ 0 := by
  intro k
  induction k using Nat.strong_induction_on with
  | h k ih =>
      intro hk
      match k, hk with
      | 1, _ =>
          rw [ring_choose_two]
          nlinarith
      | (k + 2), _ =>
          rw [ring_choose_even_succ]
          have hprev := ih (k + 1) (by omega) (by omega)
          have hfac : 0 ≤ (s - (2 * (k + 1) : ℕ)) * (s - (2 * (k + 1) + 1 : ℕ)) := by
            apply mul_nonneg_of_nonpos_of_nonpos <;> norm_num <;> linarith
          refine div_nonpos_of_nonpos_of_nonneg ?_ (by positivity)
          rw [mul_assoc]
          exact mul_nonpos_of_nonpos_of_nonneg hprev hfac

-- TCSlib.BooleanAnalysis.Hypercontractivity.ReverseBonamiBeckner:355
/-- The scalar factor estimate used to compare corresponding even Taylor
coefficients in Borell's proof. -/
lemma borell_factor_bound (p q ρ : ℝ) (hq : 0 < q) (hqp : q < p) (hp : p < 1)
    (hρ0 : 0 ≤ ρ) (hρsq : ρ ^ 2 = (1 - p) / (1 - q))
    (m : ℕ) (hm : 2 ≤ m) :
    ρ * ((m : ℝ) - q) ≤ (m : ℝ) - p := by
  have hq1 : q < 1 := hqp.trans hp
  have hm' : (2 : ℝ) ≤ m := by exact_mod_cast hm
  have hρrel : ρ ^ 2 * (1 - q) = 1 - p := by
    rw [hρsq, div_mul_cancel₀ _ (sub_pos.mpr hq1).ne']
  have hquad : 0 ≤ (m : ℝ) ^ 2 - 2 * m + p + q - p * q := by
    nlinarith [mul_nonneg (show 0 ≤ (m : ℝ) by linarith) (show 0 ≤ (m : ℝ) - 2 by linarith),
      mul_nonneg hq.le (sub_pos.mpr hp).le]
  refine (sq_le_sq₀ (mul_nonneg hρ0 (by linarith)) (by linarith)).mp ?_
  have key : 0 ≤ ((m : ℝ) - p) ^ 2 * (1 - q) - ρ ^ 2 * (1 - q) * ((m : ℝ) - q) ^ 2 := by
    rw [hρrel]
    nlinarith [mul_nonneg (sub_nonneg.mpr hqp.le) hquad]
  nlinarith [key, sub_pos.mpr hq1]

-- TCSlib.BooleanAnalysis.Hypercontractivity.ReverseBonamiBeckner:374
/-- The inductive step of the coefficient comparison: Pascal's recurrence turns
the bound for `2K` into the bound for `2K + 2`, at the cost of the two factors
controlled by `borell_factor_bound`. -/
private lemma choose_even_ratio_step (p q ρ : ℝ) (hq : 0 < q) (hqp : q < p) (hp : p < 1)
    (hρ0 : 0 ≤ ρ) (hρsq : ρ ^ 2 = (1 - p) / (1 - q)) (K : ℕ) (hK : 1 ≤ K)
    (hih : Ring.choose p (2 * K) ≤ (p / q) * Ring.choose q (2 * K) * ρ ^ (2 * K)) :
    Ring.choose p (2 * (K + 1)) ≤
      (p / q) * Ring.choose q (2 * (K + 1)) * ρ ^ (2 * (K + 1)) := by
  have hp0 : 0 < p := hq.trans hqp
  have hq1 : q < 1 := hqp.trans hp
  have hK1 : (1 : ℝ) ≤ (K : ℝ) := by exact_mod_cast hK
  have hm1 : 0 ≤ ((2 * K + 1 : ℕ) : ℝ) - q := by push_cast; linarith
  have hmp0 : 0 ≤ ((2 * K : ℕ) : ℝ) - p := by push_cast; linarith
  have hmp1 : 0 ≤ ((2 * K + 1 : ℕ) : ℝ) - p := by push_cast; linarith
  -- the two factors introduced by Pascal's recurrence shrink by at least `ρ ^ 2`
  have hfac : ρ ^ 2 * ((((2 * K : ℕ) : ℝ) - q) * (((2 * K + 1 : ℕ) : ℝ) - q)) ≤
      (((2 * K : ℕ) : ℝ) - p) * (((2 * K + 1 : ℕ) : ℝ) - p) := by
    calc
      ρ ^ 2 * ((((2 * K : ℕ) : ℝ) - q) * (((2 * K + 1 : ℕ) : ℝ) - q)) =
          (ρ * (((2 * K : ℕ) : ℝ) - q)) * (ρ * (((2 * K + 1 : ℕ) : ℝ) - q)) := by ring
      _ ≤ (((2 * K : ℕ) : ℝ) - p) * (((2 * K + 1 : ℕ) : ℝ) - p) :=
        mul_le_mul (borell_factor_bound p q ρ hq hqp hp hρ0 hρsq (2 * K) (by omega))
          (borell_factor_bound p q ρ hq hqp hp hρ0 hρsq (2 * K + 1) (by omega))
          (mul_nonneg hρ0 hm1) hmp0
  -- the comparison term is nonpositive, so multiplying by it reverses `hfac`
  have hrq_nonpos : (p / q) * Ring.choose q (2 * K) * ρ ^ (2 * K) ≤ 0 :=
    mul_nonpos_of_nonpos_of_nonneg
      (mul_nonpos_of_nonneg_of_nonpos (div_nonneg hp0.le hq.le)
        (ring_choose_even_nonpos q hq hq1 K hK))
      (pow_nonneg hρ0 _)
  have hnumle :
      Ring.choose p (2 * K) * (p - (2 * K : ℕ)) * (p - (2 * K + 1 : ℕ)) ≤
        (p / q) * (Ring.choose q (2 * K) * (q - (2 * K : ℕ)) *
          (q - (2 * K + 1 : ℕ))) * ρ ^ (2 * (K + 1)) := by
    calc
      Ring.choose p (2 * K) * (p - (2 * K : ℕ)) * (p - (2 * K + 1 : ℕ)) =
          Ring.choose p (2 * K) *
            ((((2 * K : ℕ) : ℝ) - p) * (((2 * K + 1 : ℕ) : ℝ) - p)) := by ring
      _ ≤ ((p / q) * Ring.choose q (2 * K) * ρ ^ (2 * K)) *
          ((((2 * K : ℕ) : ℝ) - p) * (((2 * K + 1 : ℕ) : ℝ) - p)) :=
        mul_le_mul_of_nonneg_right hih (mul_nonneg hmp0 hmp1)
      _ ≤ ((p / q) * Ring.choose q (2 * K) * ρ ^ (2 * K)) *
          (ρ ^ 2 * ((((2 * K : ℕ) : ℝ) - q) * (((2 * K + 1 : ℕ) : ℝ) - q))) :=
        mul_le_mul_of_nonpos_left hfac hrq_nonpos
      _ = (p / q) * (Ring.choose q (2 * K) * (q - (2 * K : ℕ)) *
          (q - (2 * K + 1 : ℕ))) * ρ ^ (2 * (K + 1)) := by
        rw [show 2 * (K + 1) = 2 * K + 2 by omega, pow_add]
        ring
  rw [ring_choose_even_succ p K, ring_choose_even_succ q K]
  convert! div_le_div_of_nonneg_right hnumle
    (by positivity : (0:ℝ) ≤ (((2 * K + 1 : ℕ) : ℝ) * ((2 * K + 2 : ℕ) : ℝ))) using 1 <;> ring

-- TCSlib.BooleanAnalysis.Hypercontractivity.ReverseBonamiBeckner:426
/-- Coefficientwise comparison of the two even Taylor series in Borell's proof. -/
private lemma choose_even_ratio_le (p q ρ : ℝ) (hq : 0 < q) (hqp : q < p) (hp : p < 1)
    (hρ0 : 0 ≤ ρ) (hρsq : ρ ^ 2 = (1 - p) / (1 - q)) :
    ∀ k : ℕ, 1 ≤ k →
      Ring.choose p (2 * k) ≤ (p / q) * Ring.choose q (2 * k) * ρ ^ (2 * k) := by
  have hq1 : q < 1 := hqp.trans hp
  intro k hk
  induction k with
  | zero => omega
  | succ k ih =>
      match k with
      | 0 =>
          rw [ring_choose_two, ring_choose_two]
          field_simp [hq.ne', (sub_pos.mpr hq1).ne'] at hρsq ⊢
          norm_num [pow_two] at hρsq ⊢
          nlinarith
      | (k + 1) =>
          exact choose_even_ratio_step p q ρ hq hqp hp hρ0 hρsq (k + 1) (by omega)
            (ih (by omega))

-- TCSlib.BooleanAnalysis.Hypercontractivity.ReverseBonamiBeckner:446
/-- Lemma A.1 away from the endpoints `a = ±1`.  Expand both sides in even
powers of `a` and compare coefficients with `choose_even_ratio_le`. -/
lemma reverse_two_point_normalized (p q ρ a : ℝ)
    (hq : 0 < q) (hqp : q < p) (hp : p < 1)
    (hρ0 : 0 ≤ ρ) (hρsq : ρ ^ 2 = (1 - p) / (1 - q))
    (ha : |a| < 1) :
    lpMean q (noiseOp ρ (fun x : BoolCube 1 ↦ 1 + a * boolToSign (x 0))) ≥
      lpMean p (fun x : BoolCube 1 ↦ 1 + a * boolToSign (x 0)) := by
  have hp0 : 0 < p := hq.trans hqp
  have hq1 : q < 1 := hqp.trans hp
  have hρ1 : ρ < 1 := by
    have : ρ ^ 2 < 1 := by rw [hρsq, div_lt_one (sub_pos.mpr hq1)]; linarith
    nlinarith [sq_nonneg ρ]
  have hρa : |ρ * a| < 1 := by
    rw [abs_mul, abs_of_nonneg hρ0]
    nlinarith [abs_nonneg a]
  -- the two Taylor series, with their constant terms split off
  have hsump := summable_choose_even (s := p) (x := a) ha
  have hsumq := summable_choose_even (s := q) (x := ρ * a) hρa
  have hPseries : ((1 + a) ^ p + (1 - a) ^ p) / 2 =
      1 + ∑' k : ℕ, Ring.choose p (2 * (k + 1)) * a ^ (2 * (k + 1)) := by
    rw [even_part_rpow_eq_tsum ha, hsump.tsum_eq_zero_add]
    simp
  have hQseries : ((1 + ρ * a) ^ q + (1 - ρ * a) ^ q) / 2 =
      1 + ∑' k : ℕ, Ring.choose q (2 * (k + 1)) * (ρ * a) ^ (2 * (k + 1)) := by
    rw [even_part_rpow_eq_tsum hρa, hsumq.tsum_eq_zero_add]
    simp
  -- comparison of the two tails
  have hterm (k : ℕ) :
      Ring.choose p (2 * (k + 1)) * a ^ (2 * (k + 1)) ≤
        (p / q) * (Ring.choose q (2 * (k + 1)) * (ρ * a) ^ (2 * (k + 1))) := by
    calc
      Ring.choose p (2 * (k + 1)) * a ^ (2 * (k + 1)) ≤
          ((p / q) * Ring.choose q (2 * (k + 1)) * ρ ^ (2 * (k + 1))) * a ^ (2 * (k + 1)) :=
        mul_le_mul_of_nonneg_right
          (choose_even_ratio_le p q ρ hq hqp hp hρ0 hρsq (k + 1) (by omega))
          (by rw [show 2 * (k + 1) = (k + 1) + (k + 1) by omega, pow_add]; exact mul_self_nonneg _)
      _ = (p / q) * (Ring.choose q (2 * (k + 1)) * (ρ * a) ^ (2 * (k + 1))) := by
        rw [mul_pow]; ring
  have htail :
      (∑' k : ℕ, Ring.choose p (2 * (k + 1)) * a ^ (2 * (k + 1))) ≤
        (p / q) * ∑' k : ℕ, Ring.choose q (2 * (k + 1)) * (ρ * a) ^ (2 * (k + 1)) := by
    rw [← tsum_mul_left]
    exact (hsump.comp_injective (add_left_injective 1)).tsum_le_tsum hterm
      ((hsumq.comp_injective (add_left_injective 1)).mul_left (p / q))
  -- the symmetrized moments are positive, and the tail comparison plus the
  -- tangent line inequality at `1` compares them
  obtain ⟨ha1, ha2⟩ := abs_lt.mp ha
  obtain ⟨hρa1, hρa2⟩ := abs_lt.mp hρa
  have hPpos : 0 < ((1 + a) ^ p + (1 - a) ^ p) / 2 := by
    have := Real.rpow_pos_of_pos (show (0:ℝ) < 1 + a by linarith) p
    have := Real.rpow_pos_of_pos (show (0:ℝ) < 1 - a by linarith) p
    linarith
  have hQpos : 0 < ((1 + ρ * a) ^ q + (1 - ρ * a) ^ q) / 2 := by
    have := Real.rpow_pos_of_pos (show (0:ℝ) < 1 + ρ * a by linarith) q
    have := Real.rpow_pos_of_pos (show (0:ℝ) < 1 - ρ * a by linarith) q
    linarith
  have hPQ : ((1 + a) ^ p + (1 - a) ^ p) / 2 ≤
      (((1 + ρ * a) ^ q + (1 - ρ * a) ^ q) / 2) ^ (p / q) := by
    calc
      ((1 + a) ^ p + (1 - a) ^ p) / 2 ≤
          1 + (p / q) * ((((1 + ρ * a) ^ q + (1 - ρ * a) ^ q) / 2) - 1) := by
        rw [hPseries, hQseries]; linarith
      _ ≤ (((1 + ρ * a) ^ q + (1 - ρ * a) ^ q) / 2) ^ (p / q) := by
        simpa using one_add_mul_self_le_rpow_one_add
          (s := (((1 + ρ * a) ^ q + (1 - ρ * a) ^ q) / 2) - 1) (by linarith)
          ((le_div_iff₀ hq).2 (by simpa using hqp.le))
  rw [ge_iff_le, lpMean_of_pos q hq, lpMean_of_pos p hp0, noiseOp_affine_one_bit,
    expect_abs_rpow_affine q (ρ * a) hρa, expect_abs_rpow_affine p a ha]
  refine (Real.rpow_le_rpow hPpos.le hPQ (by positivity)).trans_eq ?_
  rw [← Real.rpow_mul hQpos.le, show p / q * (1 / p) = 1 / q by field_simp]

-- TCSlib.BooleanAnalysis.Hypercontractivity.ReverseBonamiBeckner:518
/-- Every point of the one-bit cube is one of the two constant strings. -/
private lemma boolCube_one_cases (x : BoolCube 1) :
    x = (fun _ ↦ false) ∨ x = (fun _ ↦ true) := by
  cases hx : x 0
  · exact Or.inl (by funext i; fin_cases i; exact hx)
  · exact Or.inr (by funext i; fin_cases i; exact hx)

-- TCSlib.BooleanAnalysis.Hypercontractivity.ReverseBonamiBeckner:525
/-- A nonzero nonnegative one-bit function has the form `c (1 + a χ)` with
`c > 0` and `|a| ≤ 1`. -/
lemma normalize_one_bit (f : BooleanFunc 1) (hf : IsNonnegative f) (hf0 : f ≠ 0) :
    ∃ c a : ℝ, 0 < c ∧ -1 ≤ a ∧ a ≤ 1 ∧
      f = fun x ↦ c * (1 + a * boolToSign (x 0)) := by
  set u := f (fun _ ↦ false)
  set v := f (fun _ ↦ true)
  have hu : 0 ≤ u := hf _
  have hv : 0 ≤ v := hf _
  have huv : 0 < u + v := by
    rcases (by linarith : (0:ℝ) ≤ u + v).lt_or_eq with h | h
    · exact h
    · refine absurd (funext fun x ↦ ?_) hf0
      rcases boolCube_one_cases x with rfl | rfl
      · show u = 0; linarith
      · show v = 0; linarith
  refine ⟨(u + v) / 2, (u - v) / (u + v), by linarith, ?_, ?_, funext fun x ↦ ?_⟩
  · rw [le_div_iff₀ huv]; linarith
  · rw [div_le_iff₀ huv]; linarith
  · rcases boolCube_one_cases x with rfl | rfl <;>
      simp only [boolToSign_false, boolToSign_true] <;>
      field_simp <;> ring

-- TCSlib.BooleanAnalysis.Hypercontractivity.ReverseBonamiBeckner:548
/-- The one-bit power means depend continuously on the Fourier coefficient. -/
private lemma continuous_lpMean_affine (s : ℝ) (hs : 0 < s) :
    Continuous fun a : ℝ ↦ lpMean s (fun x : BoolCube 1 ↦ 1 + a * boolToSign (x 0)) := by
  simp_rw [lpMean_of_pos s hs]
  unfold expect
  refine (Real.continuous_rpow_const (by positivity)).comp
    (continuous_const.mul (continuous_finset_sum _ fun x _ ↦ ?_))
  exact (Real.continuous_rpow_const hs.le).comp
    (Continuous.abs (continuous_const.add (continuous_id.mul continuous_const)))

-- TCSlib.BooleanAnalysis.Hypercontractivity.ReverseBonamiBeckner:558
/-- The complete two-point reverse Bonami-Beckner inequality.  Homogeneity and
continuity discharge the zero function and the endpoints `a = ±1`.

**Source:** [OD14, Exs. 10.6--10.9]. -/
theorem reverse_bonami_beckner_one_bit (p q ρ : ℝ)
    (hq : 0 < q) (hqp : q < p) (hp : p < 1)
    (hρ0 : 0 ≤ ρ) (hρsq : ρ ^ 2 = (1 - p) / (1 - q))
    (f : BooleanFunc 1) (hf : IsNonnegative f) :
    lpMean q (noiseOp ρ f) ≥ lpMean p f := by
  have hp0 : 0 < p := hq.trans hqp
  rcases eq_or_ne f 0 with rfl | hf0
  · rw [lpMean_of_pos p hp0, lpMean_of_pos q hq,
      show noiseOp ρ (0 : BooleanFunc 1) = 0 by
        funext x; simp [noiseOp, BooleanAnalysis.fourierCoeff, innerProduct, expect]]
    unfold expect
    simp only [Pi.zero_apply, abs_zero, Real.zero_rpow hp0.ne', Real.zero_rpow hq.ne',
      Finset.sum_const_zero, mul_zero, one_div]
    rw [Real.zero_rpow (inv_ne_zero hp0.ne'), Real.zero_rpow (inv_ne_zero hq.ne')]
  obtain ⟨c, a, hc, ha0, ha1, hfa⟩ := normalize_one_bit f hf hf0
  -- the inequality for `|a| < 1` extends to `a = ±1` by continuity
  have hclosed : IsClosed {b : ℝ |
      lpMean p (fun x : BoolCube 1 ↦ 1 + b * boolToSign (x 0)) ≤
        lpMean q (noiseOp ρ (fun x : BoolCube 1 ↦ 1 + b * boolToSign (x 0)))} :=
    isClosed_le (continuous_lpMean_affine p hp0)
      (by simpa only [noiseOp_affine_one_bit, Function.comp_def, Pi.mul_apply, id_eq] using
        (continuous_lpMean_affine q hq).comp (continuous_const.mul continuous_id))
  have hIoo : Set.Ioo (-1 : ℝ) 1 ⊆ {b : ℝ |
      lpMean p (fun x : BoolCube 1 ↦ 1 + b * boolToSign (x 0)) ≤
        lpMean q (noiseOp ρ (fun x : BoolCube 1 ↦ 1 + b * boolToSign (x 0)))} := fun b hb ↦
    reverse_two_point_normalized p q ρ b hq hqp hp hρ0 hρsq (by rw [abs_lt]; exact hb)
  have hIcc := hclosed.closure_subset_iff.mpr hIoo
  rw [closure_Ioo (by norm_num : (-1 : ℝ) ≠ 1)] at hIcc
  rw [hfa, noiseOp_const_mul, lpMean_const_mul q c hq hc, lpMean_const_mul p c hp0 hc]
  exact mul_le_mul_of_nonneg_left (hIcc ⟨ha0, ha1⟩) hc.le

-- TCSlib.BooleanAnalysis.Hypercontractivity.ReverseBonamiBeckner:595
/-- Minkowski's inequality for finite sums with exponent `r ≥ 1`. -/
private lemma finset_Lr_sum_le {ι κ : Type*} [DecidableEq ι] (r : ℝ) (hr : 1 ≤ r)
    (s : Finset ι) (t : Finset κ) (a : ι → κ → ℝ) (ha : ∀ i ∈ s, ∀ j ∈ t, 0 ≤ a i j) :
    (∑ j ∈ t, (∑ i ∈ s, a i j) ^ r) ^ (1 / r) ≤
      ∑ i ∈ s, (∑ j ∈ t, a i j ^ r) ^ (1 / r) := by
  have hr0 : 0 < r := lt_of_lt_of_le zero_lt_one hr
  induction s using Finset.induction_on with
  | empty => simp [Real.zero_rpow hr0.ne', Real.zero_rpow (inv_ne_zero hr0.ne')]
  | @insert i s his ih =>
      simp only [Finset.sum_insert his]
      calc
        (∑ j ∈ t, (a i j + ∑ k ∈ s, a k j) ^ r) ^ (1 / r) ≤
            (∑ j ∈ t, a i j ^ r) ^ (1 / r) + (∑ j ∈ t, (∑ k ∈ s, a k j) ^ r) ^ (1 / r) :=
          Real.Lp_add_le_of_nonneg t hr (fun j hj ↦ ha i (Finset.mem_insert_self i s) j hj)
            (fun j hj ↦ Finset.sum_nonneg fun k hk ↦ ha k (Finset.mem_insert_of_mem hk) j hj)
        _ ≤ (∑ j ∈ t, a i j ^ r) ^ (1 / r) + ∑ k ∈ s, (∑ j ∈ t, a k j ^ r) ^ (1 / r) :=
          add_le_add le_rfl (ih fun k hk j hj ↦ ha k (Finset.mem_insert_of_mem hk) j hj)

-- TCSlib.BooleanAnalysis.Hypercontractivity.ReverseBonamiBeckner:613
/-- Reverse Minkowski in the mixed-norm form needed to exchange the last bit
with the first `n` bits during tensorization.

**Source:** [OD14, Exs. 10.6--10.9 (tensorization argument)]. -/
lemma reverse_minkowski_mixed (p q : ℝ) (hq : 0 < q) (hqp : q ≤ p)
    (F : BoolCube n → BoolCube 1 → ℝ) (hF : ∀ x y, 0 ≤ F x y) :
    lpMean q (fun x ↦ lpMean p (fun y ↦ F x y)) ≥
      lpMean p (fun y ↦ lpMean q (fun x ↦ F x y)) := by
  classical
  have hp0 : 0 < p := lt_of_lt_of_le hq hqp
  set r := p / q with hr_def
  have hr : 1 ≤ r := (le_div_iff₀ hq).2 (by simpa using hqp)
  have hEp (x : BoolCube n) : 0 ≤ expect fun y : BoolCube 1 ↦ F x y ^ p :=
    by
      rw [expect_eq_fintypeExpect]
      exact Finset.expect_nonneg fun y _ ↦ Real.rpow_nonneg (hF x y) p
  have hEq (y : BoolCube 1) : 0 ≤ expect fun x : BoolCube n ↦ F x y ^ q :=
    by
      rw [expect_eq_fintypeExpect]
      exact Finset.expect_nonneg fun x _ ↦ Real.rpow_nonneg (hF x y) q
  rw [lpMean_of_pos q hq, lpMean_of_pos p hp0]
  simp_rw [lpMean_of_pos p hp0, lpMean_of_pos q hq, abs_of_nonneg (hF _ _),
    abs_of_nonneg (Real.rpow_nonneg (hEp _) _), abs_of_nonneg (Real.rpow_nonneg (hEq _) _),
    ← Real.rpow_mul (hEp _), ← Real.rpow_mul (hEq _)]
  ring_nf
  have hA0 : 0 ≤ expect fun x : BoolCube n ↦
      (expect fun y : BoolCube 1 ↦ F x y ^ p) ^ (p⁻¹ * q) :=
    by
      rw [expect_eq_fintypeExpect]
      exact Finset.expect_nonneg fun x _ ↦ Real.rpow_nonneg (hEp x) _
  have hB0 : 0 ≤ expect fun y : BoolCube 1 ↦
      (expect fun x : BoolCube n ↦ F x y ^ q) ^ (p * q⁻¹) :=
    by
      rw [expect_eq_fintypeExpect]
      exact Finset.expect_nonneg fun y _ ↦ Real.rpow_nonneg (hEq y) _
  apply (Real.rpow_le_rpow_iff (Real.rpow_nonneg hB0 _) (Real.rpow_nonneg hA0 _) hq).1
  rw [← Real.rpow_mul hB0, ← Real.rpow_mul hA0]
  ring_nf
  rw [show q * p⁻¹ = 1 / r by rw [hr_def]; field_simp, show q * q⁻¹ = 1 by field_simp,
    Real.rpow_one]
  -- both sides are now unweighted finite sums, where Minkowski applies
  have hraw := finset_Lr_sum_le r hr Finset.univ Finset.univ (fun x y ↦ F x y ^ q)
    (fun x _ y _ ↦ Real.rpow_nonneg (hF x y) q)
  have hwn : (0:ℝ) ≤ uniformWeight n := pow_nonneg (by norm_num) _
  have hw1 : (0:ℝ) ≤ uniformWeight 1 := pow_nonneg (by norm_num) _
  unfold expect
  calc
    (uniformWeight 1 * ∑ y : BoolCube 1,
        (uniformWeight n * ∑ x : BoolCube n, F x y ^ q) ^ r) ^ (1 / r) =
        uniformWeight n * uniformWeight 1 ^ (1 / r) *
          (∑ y : BoolCube 1, (∑ x : BoolCube n, F x y ^ q) ^ r) ^ (1 / r) := by
      have hsum : 0 ≤ ∑ y : BoolCube 1, (∑ x : BoolCube n, F x y ^ q) ^ r :=
        Finset.sum_nonneg fun y _ ↦ Real.rpow_nonneg
          (Finset.sum_nonneg fun x _ ↦ Real.rpow_nonneg (hF x y) q) r
      rw [show (∑ y : BoolCube 1, (uniformWeight n * ∑ x : BoolCube n, F x y ^ q) ^ r) =
          uniformWeight n ^ r * ∑ y : BoolCube 1, (∑ x : BoolCube n, F x y ^ q) ^ r by
        rw [Finset.mul_sum]
        exact Finset.sum_congr rfl fun y _ ↦ Real.mul_rpow hwn
          (Finset.sum_nonneg fun x _ ↦ Real.rpow_nonneg (hF x y) q)]
      rw [Real.mul_rpow hw1 (mul_nonneg (Real.rpow_nonneg hwn r) hsum),
        Real.mul_rpow (Real.rpow_nonneg hwn r) hsum, ← Real.rpow_mul hwn,
        show r * (1 / r) = 1 by field_simp, Real.rpow_one]
      ring
    _ ≤ uniformWeight n * uniformWeight 1 ^ (1 / r) *
          ∑ x : BoolCube n, (∑ y : BoolCube 1, (F x y ^ q) ^ r) ^ (1 / r) :=
      mul_le_mul_of_nonneg_left hraw (by positivity)
    _ = uniformWeight n * ∑ x : BoolCube n,
          (uniformWeight 1 * ∑ y : BoolCube 1, F x y ^ p) ^ (1 / r) := by
      rw [mul_assoc, Finset.mul_sum]
      refine congrArg _ (Finset.sum_congr rfl fun x _ ↦ ?_)
      rw [Real.mul_rpow hw1 (Finset.sum_nonneg fun y _ ↦ Real.rpow_nonneg (hF x y) p)]
      refine congrArg _ (congrArg (fun z : ℝ ↦ z ^ (1 / r)) (Finset.sum_congr rfl fun y _ ↦ ?_))
      rw [← Real.rpow_mul (hF x y), hr_def]
      congr 1
      field_simp

-- TCSlib.BooleanAnalysis.Hypercontractivity.ReverseBonamiBeckner:689
/-- A one-bit reverse bound tensorizes to every Boolean cube.  The inductive
step splits off the last bit with `noiseOp_snoc_slice` and `lpMean_collapse_last`,
then exchanges the two blocks with `reverse_minkowski_mixed`.

**Source:** [OD14, Exs. 10.6--10.9]. -/
theorem tensorize_reverse_bonami_beckner (p q ρ : ℝ)
    (hq : 0 < q) (hqp : q < p)
    (hρ0 : 0 ≤ ρ) (hρ1 : ρ ≤ 1)
    (hone : ∀ f : BooleanFunc 1, IsNonnegative f →
      lpMean q (noiseOp ρ f) ≥ lpMean p f)
    (f : BooleanFunc n) (hf : IsNonnegative f) :
    lpMean q (noiseOp ρ f) ≥ lpMean p f := by
  have hp0 : 0 < p := hq.trans hqp
  induction n with
  | zero => rw [noiseOp_dim_zero, lpMean_dim_zero q hq f hf, lpMean_dim_zero p hp0 f hf]
  | succ k ih =>
      set F : BoolCube k → BoolCube 1 → ℝ :=
        fun x y ↦ noiseOp ρ (restrictLast f (y 0)) x
      have hF (x : BoolCube k) (y : BoolCube 1) : 0 ≤ F x y :=
        noiseOp_nonneg hρ0 hρ1 (fun z ↦ hf (Fin.snoc z (y 0))) x
      calc
        lpMean q (noiseOp ρ f) =
            lpMean q (fun x : BoolCube k ↦ lpMean q (noiseOp ρ (fun y : BoolCube 1 ↦ F x y))) := by
          rw [lpMean_collapse_last q hq (noiseOp ρ f)]
          exact congrArg _ (funext fun x ↦ congrArg _ (funext fun y ↦ noiseOp_snoc_slice ρ f x y))
        _ ≥ lpMean q (fun x : BoolCube k ↦ lpMean p (fun y : BoolCube 1 ↦ F x y)) :=
          lpMean_mono q hq (fun x ↦ lpMean_nonneg p hp0 _) fun x ↦ hone (fun y ↦ F x y) (hF x)
        _ ≥ lpMean p (fun y : BoolCube 1 ↦ lpMean q (fun x : BoolCube k ↦ F x y)) :=
          reverse_minkowski_mixed p q hq hqp.le F hF
        _ ≥ lpMean p (fun y : BoolCube 1 ↦
              lpMean p (fun x : BoolCube k ↦ restrictLast f (y 0) x)) :=
          lpMean_mono p hp0 (fun y ↦ lpMean_nonneg p hp0 _) fun y ↦
            ih (restrictLast f (y 0)) fun x ↦ hf (Fin.snoc x (y 0))
        _ = lpMean p (fun x : BoolCube k ↦
              lpMean p (fun y : BoolCube 1 ↦ f (Fin.snoc x (y 0)))) :=
          (lpMean_comm p hp0 fun x y ↦ f (Fin.snoc x (y 0))).symm
        _ = lpMean p f := (lpMean_collapse_last p hp0 f).symm

-- TCSlib.BooleanAnalysis.Hypercontractivity.ReverseBonamiBeckner:727
/-- States reverse hypercontractivity at sharp correlation for `0 < q < p < 1`.

**Source:** [OD14, Exs. 10.6--10.9]. -/
theorem reverse_bonami_beckner_positive_sharp (p q ρ : ℝ)
    (hq : 0 < q) (hqp : q < p) (hp : p < 1)
    (hρ0 : 0 ≤ ρ) (hρ1 : ρ ≤ 1) (hρsq : ρ ^ 2 = (1 - p) / (1 - q))
    (f : BooleanFunc n) (hf : IsNonnegative f) :
    lpMean q (noiseOp ρ f) ≥ lpMean p f :=
  tensorize_reverse_bonami_beckner p q ρ hq hqp hρ0 hρ1
    (fun g hg ↦ reverse_bonami_beckner_one_bit p q ρ hq hqp hp hρ0 hρsq g hg) f hf

-- TCSlib.BooleanAnalysis.Hypercontractivity.ReverseBonamiBeckner:740
/-- More noise can only increase an `L^q` mean when `q < 1`.  Together with
`noiseOp_compose`, this relaxes equality in the correlation constraint. -/
lemma lpMean_noise_antitone (q ρ σ : ℝ) (hq : q < 1)
    (hρ0 : 0 ≤ ρ) (hρσ : ρ ≤ σ) (hσ1 : σ ≤ 1)
    (f : BooleanFunc n) (hf : IsNonnegative f) :
    lpMean q (noiseOp ρ f) ≥ lpMean q (noiseOp σ f) := by
  classical
  have mean_nonneg : ∀ (r : ℝ) (u : BooleanFunc n), 0 ≤ lpMean r u := by
    intro r u
    unfold lpMean
    split_ifs
    · exact le_rfl
    · positivity
    · exact Real.rpow_nonneg (by
        rw [expect_eq_fintypeExpect]
        exact Finset.expect_nonneg fun x _ ↦ Real.rpow_nonneg (abs_nonneg (u x)) r) _
  have expect_pos : ∀ (u : BooleanFunc n), (∀ x, 0 < u x) → 0 < expect u := by
    intro u hu
    unfold expect uniformWeight
    exact mul_pos (pow_pos (by norm_num) _)
      (Finset.sum_pos (fun x _ ↦ hu x) Finset.univ_nonempty)
  have noise_positive : ∀ (τ : ℝ), 0 ≤ τ → τ ≤ 1 → ∀ (u : BooleanFunc n),
      (∀ x, 0 < u x) → ∀ x, 0 < noiseOp τ u x := by
    intro τ hτ0 hτ1 u hu x
    rw [GeneralHypercontractivity.noiseOp_eq_kernel_sum]
    have hkdiag : 0 < GeneralHypercontractivity.noiseKernel τ x x := by
      unfold GeneralHypercontractivity.noiseKernel
      apply Finset.prod_pos
      intro i hi
      cases x i <;> norm_num [boolToSign] <;> linarith
    calc
      0 < GeneralHypercontractivity.noiseKernel τ x x * u x := mul_pos hkdiag (hu x)
      _ ≤ ∑ y : BoolCube n, GeneralHypercontractivity.noiseKernel τ x y * u y := by
        have h := Finset.single_le_sum
          (s := Finset.univ)
          (fun y _ ↦ mul_nonneg
            (GeneralHypercontractivity.noiseKernel_nonneg hτ0 hτ1 x y) (hu y).le)
          (Finset.mem_univ x)
        simpa using h
  have kernel_double_sum : ∀ (τ : ℝ), 0 ≤ τ → τ ≤ 1 → ∀ (u : BooleanFunc n),
      ∑ x : BoolCube n, ∑ y : BoolCube n,
          GeneralHypercontractivity.noiseKernel τ x y * u y = ∑ y : BoolCube n, u y := by
    intro τ hτ0 hτ1 u
    rw [Finset.sum_comm]
    apply Finset.sum_congr rfl
    intro y hy
    rw [← Finset.sum_mul,
      GeneralHypercontractivity.noiseKernel_sum_left hτ0 hτ1 y, one_mul]
  have convex_rpow_of_neg : ∀ {r : ℝ}, r < 0 →
      ConvexOn ℝ (Set.Ioi 0) (fun x : ℝ ↦ x ^ r) := by
    intro r hr
    have hneglog : ConvexOn ℝ (Set.Ioi 0) (fun x : ℝ ↦ -Real.log x) := by
      refine ⟨convex_Ioi 0, ?_⟩
      intro x hx y hy a b ha hb hab
      have hlog := strictConcaveOn_log_Ioi.concaveOn.2 hx hy ha hb hab
      simp only [smul_eq_mul] at hlog ⊢
      linarith
    have hinner : ConvexOn ℝ (Set.Ioi 0) (fun x : ℝ ↦ r * Real.log x) := by
      have h := hneglog.smul (show 0 ≤ -r by linarith)
      convert! h using 1
      ext x
      simp only [smul_eq_mul]
      ring
    refine ⟨convex_Ioi 0, ?_⟩
    intro x hx y hy a b ha hb hab
    have hinner_le := hinner.2 hx hy ha hb hab
    have hcombo : 0 < a • x + b • y := by
      simp only [smul_eq_mul]
      rcases eq_or_lt_of_le ha with ha0 | ha'
      · subst a
        norm_num at hab ⊢
        simpa [hab] using hy
      · exact add_pos_of_pos_of_nonneg (mul_pos ha' hx) (mul_nonneg hb hy.le)
    calc
      (a • x + b • y) ^ r = Real.exp (r * Real.log (a • x + b • y)) := by
        rw [Real.rpow_def_of_pos hcombo]
        congr 1
        ring
      _ ≤ Real.exp (a • (r * Real.log x) + b • (r * Real.log y)) :=
        Real.exp_le_exp.mpr hinner_le
      _ ≤ a • Real.exp (r * Real.log x) + b • Real.exp (r * Real.log y) :=
        convexOn_exp.2 (Set.mem_univ _) (Set.mem_univ _) ha hb hab
      _ = a • x ^ r + b • y ^ r := by
        rw [Real.rpow_def_of_pos hx, Real.rpow_def_of_pos hy]
        congr 2 <;> congr 1 <;> ring
  have expect_rpow_le_noise : ∀ (r τ : ℝ), 0 < r → r < 1 → 0 ≤ τ → τ ≤ 1 →
      ∀ (u : BooleanFunc n), IsNonnegative u →
        expect (fun x ↦ u x ^ r) ≤ expect (fun x ↦ noiseOp τ u x ^ r) := by
    intro r τ hr0 hr1 hτ0 hτ1 u hu
    unfold expect
    refine mul_le_mul_of_nonneg_left ?_ (pow_nonneg (by norm_num) _)
    rw [← kernel_double_sum τ hτ0 hτ1 (fun x ↦ u x ^ r)]
    refine Finset.sum_le_sum fun x _ ↦ ?_
    rw [GeneralHypercontractivity.noiseOp_eq_kernel_sum]
    exact (Real.concaveOn_rpow hr0.le hr1.le).le_map_sum
      (fun y _ ↦ GeneralHypercontractivity.noiseKernel_nonneg hτ0 hτ1 x y)
      (GeneralHypercontractivity.noiseKernel_sum_right hτ0 hτ1 x)
      (fun y _ ↦ hu y)
  have expect_noise_le_rpow : ∀ (r τ : ℝ), r < 0 → 0 ≤ τ → τ ≤ 1 →
      ∀ (u : BooleanFunc n), (∀ x, 0 < u x) →
        expect (fun x ↦ noiseOp τ u x ^ r) ≤ expect (fun x ↦ u x ^ r) := by
    intro r τ hr hτ0 hτ1 u hu
    unfold expect
    refine mul_le_mul_of_nonneg_left ?_ (pow_nonneg (by norm_num) _)
    rw [← kernel_double_sum τ hτ0 hτ1 (fun x ↦ u x ^ r)]
    refine Finset.sum_le_sum fun x _ ↦ ?_
    rw [GeneralHypercontractivity.noiseOp_eq_kernel_sum]
    exact (convex_rpow_of_neg hr).map_sum_le
      (fun y _ ↦ GeneralHypercontractivity.noiseKernel_nonneg hτ0 hτ1 x y)
      (GeneralHypercontractivity.noiseKernel_sum_right hτ0 hτ1 x)
      (fun y _ ↦ hu y)
  have expect_log_le_noise : ∀ (τ : ℝ), 0 ≤ τ → τ ≤ 1 →
      ∀ (u : BooleanFunc n), (∀ x, 0 < u x) →
        expect (fun x ↦ Real.log (u x)) ≤
          expect (fun x ↦ Real.log (noiseOp τ u x)) := by
    intro τ hτ0 hτ1 u hu
    unfold expect
    refine mul_le_mul_of_nonneg_left ?_ (pow_nonneg (by norm_num) _)
    rw [← kernel_double_sum τ hτ0 hτ1 (fun x ↦ Real.log (u x))]
    refine Finset.sum_le_sum fun x _ ↦ ?_
    rw [GeneralHypercontractivity.noiseOp_eq_kernel_sum]
    exact strictConcaveOn_log_Ioi.concaveOn.le_map_sum
      (fun y _ ↦ GeneralHypercontractivity.noiseKernel_nonneg hτ0 hτ1 x y)
      (GeneralHypercontractivity.noiseKernel_sum_right hτ0 hτ1 x)
      (fun y _ ↦ hu y)
  have one_step : ∀ (r τ : ℝ), r < 1 → 0 ≤ τ → τ ≤ 1 →
      ∀ (u : BooleanFunc n), IsNonnegative u →
        lpMean r (noiseOp τ u) ≥ lpMean r u := by
    intro r τ hr hτ0 hτ1 u hu
    have hnoise := noiseOp_nonneg hτ0 hτ1 hu
    by_cases hrpos : 0 < r
    · rw [lpMean_of_pos r hrpos, lpMean_of_pos r hrpos]
      simp_rw [abs_of_nonneg (hnoise _), abs_of_nonneg (hu _)]
      exact Real.rpow_le_rpow
        (by
          rw [expect_eq_fintypeExpect]
          exact Finset.expect_nonneg fun x _ ↦ Real.rpow_nonneg (hu x) r)
        (expect_rpow_le_noise r τ hrpos hr hτ0 hτ1 u hu)
        (by positivity)
    · have hrnonpos : r ≤ 0 := le_of_not_gt hrpos
      by_cases hz : ∃ x, u x = 0
      · rw [show lpMean r u = 0 by simp [lpMean, BooleanAnalysis.Hypercontractivity.cubeLpNorm, hz, hrnonpos]]
        exact mean_nonneg r _
      · have hupos : ∀ x, 0 < u x := fun x ↦
          lt_of_le_of_ne (hu x) (Ne.symm (not_exists.mp hz x))
        have hnpos := noise_positive τ hτ0 hτ1 u hupos
        have hnz : ¬∃ x, noiseOp τ u x = 0 := not_exists.mpr fun x hx ↦ (hnpos x).ne' hx
        rcases eq_or_lt_of_le hrnonpos with rfl | hrneg
        · rw [show lpMean 0 (noiseOp τ u) =
              Real.exp (expect (fun x ↦ Real.log |noiseOp τ u x|)) by simp [lpMean, BooleanAnalysis.Hypercontractivity.cubeLpNorm, hnz],
            show lpMean 0 u = Real.exp (expect (fun x ↦ Real.log |u x|)) by
              simp [lpMean, BooleanAnalysis.Hypercontractivity.cubeLpNorm, hz]]
          simp_rw [abs_of_pos (hnpos _), abs_of_pos (hupos _)]
          exact Real.exp_le_exp.mpr (expect_log_le_noise τ hτ0 hτ1 u hupos)
        · rw [show lpMean r (noiseOp τ u) =
              (expect (fun x ↦ |noiseOp τ u x| ^ r)) ^ (1 / r) by
                simp [lpMean, BooleanAnalysis.Hypercontractivity.cubeLpNorm, hnz, hrneg.ne],
            show lpMean r u = (expect (fun x ↦ |u x| ^ r)) ^ (1 / r) by
                simp [lpMean, BooleanAnalysis.Hypercontractivity.cubeLpNorm, hz, hrneg.ne]]
          simp_rw [abs_of_pos (hnpos _), abs_of_pos (hupos _)]
          exact (Real.rpow_le_rpow_iff_of_neg
            (expect_pos _ fun x ↦ Real.rpow_pos_of_pos (hupos x) r)
            (expect_pos _ fun x ↦ Real.rpow_pos_of_pos (hnpos x) r)
            (one_div_neg.mpr hrneg)).2
              (expect_noise_le_rpow r τ hrneg hτ0 hτ1 u hupos)
  have hσ0 : 0 ≤ σ := le_trans hρ0 hρσ
  by_cases hσzero : σ = 0
  · have hρzero : ρ = 0 := le_antisymm (by simpa [hσzero] using hρσ) hρ0
    subst σ
    subst ρ
    rfl
  · let τ : ℝ := ρ / σ
    have hτ0 : 0 ≤ τ := div_nonneg hρ0 hσ0
    have hσpos : 0 < σ := lt_of_le_of_ne hσ0 (Ne.symm hσzero)
    have hτ1 : τ ≤ 1 := (div_le_one hσpos).2 hρσ
    have hfac : noiseOp τ (noiseOp σ f) = noiseOp ρ f := by
      rw [noiseOp_compose]
      congr 2
      dsimp [τ]
      field_simp
    rw [← hfac]
    exact one_step q τ hq hτ0 hτ1 (noiseOp σ f)
      (noiseOp_nonneg hσ0 hσ1 hf)

-- TCSlib.BooleanAnalysis.Hypercontractivity.ReverseBonamiBeckner:924
/-- The reverse Young inequality: for `0 < r < 1` and conjugate exponent
`r / (r - 1) < 0` the arithmetic-geometric comparison reverses. -/
private lemma reverse_young {r a b : ℝ} (hr0 : 0 < r) (hr1 : r < 1) (ha : 0 ≤ a) (hb : 0 < b) :
    a * b ≥ a ^ r / r + b ^ (r / (r - 1)) / (r / (r - 1)) := by
  have hrm1 : r - 1 ≠ 0 := (sub_neg.mpr hr1).ne
  have hbase : 0 < b ^ (1 / (r - 1)) := Real.rpow_pos_of_pos hb _
  set t : ℝ := a / b ^ (1 / (r - 1)) with ht_def
  have ht : 0 ≤ t := div_nonneg ha hbase.le
  have haeq : a = t * b ^ (1 / (r - 1)) := by rw [ht_def]; field_simp
  -- the tangent line inequality at `t = 1` for the concave power `t ^ r`
  have htan : t ^ r ≤ 1 + r * (t - 1) := by
    simpa using rpow_one_add_le_one_add_mul_self (s := t - 1) (by linarith) hr0.le hr1.le
  have haq : a ^ r = t ^ r * b ^ (r / (r - 1)) := by
    rw [haeq, Real.mul_rpow ht hbase.le, ← Real.rpow_mul hb.le]
    congr 2
    ring
  have habeq : a * b = t * b ^ (r / (r - 1)) := by
    calc
      a * b = t * (b ^ (1 / (r - 1)) * b ^ (1 : ℝ)) := by rw [haeq, Real.rpow_one]; ring
      _ = t * b ^ (1 / (r - 1) + 1) := by rw [Real.rpow_add hb]
      _ = t * b ^ (r / (r - 1)) := by
        congr 2
        field_simp
        ring
  rw [haq, habeq]
  field_simp [hr0.ne', hrm1]
  nlinarith [mul_le_mul_of_nonneg_right htan (Real.rpow_nonneg hb.le (r / (r - 1)))]

-- TCSlib.BooleanAnalysis.Hypercontractivity.ReverseBonamiBeckner:952
/-- A nonnegative function with a positive value has positive `r`-th moment. -/
private lemma expect_rpow_pos {r : ℝ} {u : BooleanFunc n} (hu : ∀ x, 0 ≤ u x)
    (hex : ∃ x, 0 < u x) : 0 < expect (fun x ↦ u x ^ r) := by
  obtain ⟨x, hx⟩ := hex
  unfold expect uniformWeight
  exact mul_pos (pow_pos (by norm_num) _)
    (Finset.sum_pos' (fun z _ ↦ Real.rpow_nonneg (hu z) _)
      ⟨x, Finset.mem_univ x, Real.rpow_pos_of_pos hx _⟩)

-- TCSlib.BooleanAnalysis.Hypercontractivity.ReverseBonamiBeckner:961
/-- Dividing by its own `L^r` mean normalizes the `r`-th moment to `1`. -/
private lemma expect_normalized_rpow_eq_one {r : ℝ} (hr0 : r ≠ 0) (u : BooleanFunc n)
    (hu : ∀ x, 0 ≤ u x) (hE : 0 < expect (fun x ↦ u x ^ r)) :
    expect (fun x ↦ (u x / (expect (fun z ↦ u z ^ r)) ^ (1 / r)) ^ r) = 1 := by
  set E := expect (fun z ↦ u z ^ r)
  have hpow : (E ^ (1 / r)) ^ r = E := by
    rw [← Real.rpow_mul hE.le, one_div_mul_cancel hr0, Real.rpow_one]
  simp_rw [Real.div_rpow (hu _) (Real.rpow_pos_of_pos hE _).le, hpow]
  unfold expect
  rw [← Finset.sum_div, ← mul_div_assoc]
  exact div_self hE.ne'

-- TCSlib.BooleanAnalysis.Hypercontractivity.ReverseBonamiBeckner:973
/-- Rescaling both arguments of the inner product. -/
private lemma innerProduct_eq_mul_expect_div (u v : BooleanFunc n) {A B : ℝ}
    (hA : A ≠ 0) (hB : B ≠ 0) :
    innerProduct u v = A * B * expect (fun x ↦ (u x / A) * (v x / B)) := by
  have hx (x : BoolCube n) : u x * v x = A * B * ((u x / A) * (v x / B)) := by field_simp
  unfold innerProduct expect
  simp_rw [hx, ← Finset.mul_sum]
  ring

-- TCSlib.BooleanAnalysis.Hypercontractivity.ReverseBonamiBeckner:982
/-- Reverse Hölder for a positive exponent `r < 1` and its negative conjugate. -/
private lemma reverse_holder_of_pos (r : ℝ) (hr0 : 0 < r) (hr1 : r < 1)
    (u v : BooleanFunc n) (hu : IsNonnegative u) (hv : IsNonnegative v) :
    innerProduct u v ≥ lpMean r u * lpMean (r / (r - 1)) v := by
  classical
  set s := r / (r - 1) with hs_def
  have hsneg : s < 0 := div_neg_of_pos_of_neg hr0 (sub_neg.mpr hr1)
  by_cases hupos : ∃ x, 0 < u x
  · by_cases hvzero : ∃ x, v x = 0
    · -- a zero of `v` makes the right-hand side vanish
      rw [show lpMean s v = 0 by simp [lpMean, BooleanAnalysis.Hypercontractivity.cubeLpNorm, hvzero, hsneg.le], mul_zero]
      unfold innerProduct
      rw [expect_eq_fintypeExpect]
      exact Finset.expect_nonneg fun x _ ↦ mul_nonneg (hu x) (hv x)
    · have hvpos (x : BoolCube n) : 0 < v x :=
        (hv x).lt_of_ne (Ne.symm (not_exists.mp hvzero x))
      have hEu : 0 < expect (fun x ↦ u x ^ r) := expect_rpow_pos hu hupos
      have hEv : 0 < expect (fun x ↦ v x ^ s) :=
        expect_rpow_pos hv ⟨Classical.arbitrary _, hvpos _⟩
      set A := (expect (fun x ↦ u x ^ r)) ^ (1 / r) with hA_def
      set B := (expect (fun x ↦ v x ^ s)) ^ (1 / s) with hB_def
      have hApos : 0 < A := Real.rpow_pos_of_pos hEu _
      have hBpos : 0 < B := Real.rpow_pos_of_pos hEv _
      -- the pointwise reverse Young inequality, averaged over the cube
      have hone : 1 ≤ expect (fun x ↦ (u x / A) * (v x / B)) := by
        have hright : expect (fun x ↦ (u x / A) ^ r / r + (v x / B) ^ s / s) = 1 := by
          have hnormu := expect_normalized_rpow_eq_one hr0.ne' u hu hEu
          have hnormv := expect_normalized_rpow_eq_one hsneg.ne v hv hEv
          rw [← hA_def] at hnormu
          rw [← hB_def] at hnormv
          unfold expect at hnormu hnormv ⊢
          rw [Finset.sum_add_distrib, ← Finset.sum_div, ← Finset.sum_div, mul_add,
            ← mul_div_assoc, ← mul_div_assoc, hnormu, hnormv, hs_def]
          field_simp
          ring
        rw [← hright]
        unfold expect
        exact mul_le_mul_of_nonneg_left
          (Finset.sum_le_sum fun x _ ↦ reverse_young hr0 hr1
            (div_nonneg (hu x) hApos.le) (div_pos (hvpos x) hBpos))
          (pow_nonneg (by norm_num) _)
      have hpu : lpMean r u = A := by
        rw [lpMean_of_pos r hr0, hA_def]
        simp_rw [abs_of_nonneg (hu _)]
      have hsv : lpMean s v = B := by
        rw [hB_def]
        simp [lpMean, BooleanAnalysis.Hypercontractivity.cubeLpNorm, hvzero, hsneg.ne, abs_of_pos (hvpos _)]
      rw [hpu, hsv, innerProduct_eq_mul_expect_div u v hApos.ne' hBpos.ne']
      nlinarith [mul_le_mul_of_nonneg_left hone (mul_nonneg hApos.le hBpos.le)]
  · -- `u` vanishes identically
    obtain rfl : u = 0 := funext fun x ↦ le_antisymm (not_lt.mp (not_exists.mp hupos x)) (hu x)
    simp [innerProduct, lpMean, BooleanAnalysis.Hypercontractivity.cubeLpNorm, expect, uniformWeight, hr0.ne', not_le.mpr hr0]

-- TCSlib.BooleanAnalysis.Hypercontractivity.ReverseBonamiBeckner:1035
/-- Reverse Hölder bounds the inner product below by the product of conjugate means
for finite `p < 1`, `p ≠ 0`. This is the inequality consequence of the source's sharp
infimum-duality identity, used in the two-function corollary; the full identity and
its infinite-exponent endpoint are not asserted here.

**Source:** [OD14, Exs. 10.6--10.9]. -/
lemma reverse_holder (p : ℝ) (hp : p < 1) (hp0 : p ≠ 0)
    (f g : BooleanFunc n) (hf : IsNonnegative f) (hg : IsNonnegative g) :
    innerProduct f g ≥ lpMean p f * lpMean (p / (p - 1)) g := by
  rcases lt_or_gt_of_ne hp0 with hpneg | hppos
  · -- for `p < 0` apply the positive case to the conjugate exponent
    have hpm1 : p - 1 ≠ 0 := (sub_neg.mpr hp).ne
    have hq0 : 0 < p / (p - 1) := div_pos_of_neg_of_neg hpneg (sub_neg.mpr hp)
    have hq1 : p / (p - 1) < 1 := by
      rw [div_lt_iff_of_neg (sub_neg.mpr hp)]
      linarith
    have hconj : (p / (p - 1)) / (p / (p - 1) - 1) = p := by field_simp; ring
    have h := reverse_holder_of_pos (p / (p - 1)) hq0 hq1 g f hg hf
    rw [hconj] at h
    simpa only [BooleanAnalysis.innerProduct_comm, mul_comm] using h
  · exact reverse_holder_of_pos p hppos hp f g hf hg

-- TCSlib.BooleanAnalysis.Hypercontractivity.ReverseBonamiBeckner:1057
/-- Reverse hypercontractivity extends to nonnegative functions for real exponents
`q ≤ p ≤ 1` with `q < 1` and correlations `0 ≤ ρ ≤ 1` up to the sharp bound
`ρ² ≤ (1-p)/(1-q)`.

**Source:** [OD14, Exs. 10.6--10.9].

**Proof sketch.** Continuity at exponents zero and one reaches the boundary cases.
Reverse Hölder handles negative exponents, and the noise semigroup factors the case
where the exponents lie on opposite sides of zero. These steps reduce the inequality
to the positive-exponent sharp theorem. -/
lemma extend_reverse_bonami_beckner (p q ρ : ℝ)
    (hq : q < 1) (hqp : q ≤ p) (hp : p ≤ 1)
    (hρ0 : 0 ≤ ρ) (hρ1 : ρ ≤ 1) (hρsq : ρ ^ 2 ≤ (1 - p) / (1 - q))
    (f : BooleanFunc n) (hf : IsNonnegative f) :
    lpMean q (noiseOp ρ f) ≥ lpMean p f := by
  classical
  have mean_nonneg (r : ℝ) (u : BooleanFunc n) : 0 ≤ lpMean r u := by
    unfold lpMean
    split_ifs
    · exact le_rfl
    · positivity
    · exact Real.rpow_nonneg (by
        rw [expect_eq_fintypeExpect]
        exact Finset.expect_nonneg fun x _ ↦ Real.rpow_nonneg (abs_nonneg _) r) _
  have noise_strict_pos : ∀ (R : ℝ), 0 ≤ R → R < 1 →
      ∀ (u : BooleanFunc n), IsNonnegative u → (∃ y, 0 < u y) →
        ∀ x, 0 < noiseOp R u x := by
    intro R hR0 hR1 u hu hex x
    rw [GeneralHypercontractivity.noiseOp_eq_kernel_sum]
    have hkernel (y : BoolCube n) :
        0 < GeneralHypercontractivity.noiseKernel R x y := by
      unfold GeneralHypercontractivity.noiseKernel
      apply Finset.prod_pos
      intro i hi
      cases x i <;> cases y i <;> norm_num [boolToSign] <;> nlinarith
    exact Finset.sum_pos'
      (fun y _ ↦ mul_nonneg (hkernel y).le (hu y))
      ⟨hex.choose, Finset.mem_univ _, mul_pos (hkernel hex.choose) hex.choose_spec⟩
  have positive_subsharp : ∀ (P Q R : ℝ), 0 < Q → Q < P → P < 1 →
      0 ≤ R → R ≤ 1 → R ^ 2 ≤ (1 - P) / (1 - Q) →
      ∀ (u : BooleanFunc n), IsNonnegative u →
        lpMean Q (noiseOp R u) ≥ lpMean P u := by
    intro P Q R hQ hQP hP hR0 hR1 hRsq u hu
    let S : ℝ := Real.sqrt ((1 - P) / (1 - Q))
    have hden : 0 < 1 - Q := sub_pos.mpr (lt_trans hQP hP)
    have hratio0 : 0 ≤ (1 - P) / (1 - Q) :=
      div_nonneg (sub_nonneg.mpr hP.le) hden.le
    have hS0 : 0 ≤ S := Real.sqrt_nonneg _
    have hSsq : S ^ 2 = (1 - P) / (1 - Q) := Real.sq_sqrt hratio0
    have hS1 : S ≤ 1 := by
      rw [← sq_le_sq₀ hS0 (by norm_num : (0 : ℝ) ≤ 1), hSsq]
      norm_num
      exact (div_le_one hden).2 (by linarith)
    have hRS : R ≤ S := by
      rw [← sq_le_sq₀ hR0 hS0, hSsq]
      exact hRsq
    exact le_trans
      (reverse_bonami_beckner_positive_sharp P Q S hQ hQP hP hS0 hS1 hSsq u hu)
      (lpMean_noise_antitone Q R S (lt_trans hQP hP) hR0 hRS hS1 u hu)
  have lpMean_continuous_zero (u : BooleanFunc n) (hu : ∀ x, 0 < u x) :
      ContinuousAt (fun r : ℝ ↦ lpMean r u) 0 := by
    let M : ℝ → ℝ := fun r ↦ expect (fun x ↦ u x ^ r)
    let A : ℝ := expect (fun x ↦ Real.log (u x))
    have hnz : ¬∃ x, u x = 0 := not_exists.mpr fun x hx ↦ (hu x).ne' hx
    have hM0 : M 0 = 1 := by simp [M, expect, uniformWeight]
    have hMpos (r : ℝ) : 0 < M r := by
      dsimp [M, expect, uniformWeight]
      apply mul_pos (pow_pos (by norm_num) _)
      exact Finset.sum_pos' (fun x _ ↦ (Real.rpow_pos_of_pos (hu x) r).le)
        ⟨Classical.arbitrary _, Finset.mem_univ _, Real.rpow_pos_of_pos (hu _) r⟩
    have hM : HasDerivAt M A 0 := by
      dsimp [M, A, expect]
      apply HasDerivAt.const_mul
      apply HasDerivAt.fun_sum
      intro x hx
      change HasDerivAt (fun r : ℝ ↦ u x ^ r) (Real.log (u x)) 0
      simpa only [Real.rpow_def_of_pos (hu x), id_eq, mul_zero, Real.exp_zero,
        one_mul, mul_one] using
        ((hasDerivAt_id (x := (0 : ℝ))).const_mul (Real.log (u x))).exp
    have hlog : HasDerivAt (fun r ↦ Real.log (M r)) A 0 := by
      convert hM.log (hMpos 0).ne' using 1
      all_goals simp [hM0]
    let G : ℝ → ℝ :=
      Function.update (fun r ↦ (Real.log (M r) - Real.log (M 0)) / (r - 0)) 0 A
    have hG : ContinuousAt G 0 := hlog.continuousAt_div
    have hfun : (fun r : ℝ ↦ lpMean r u) = fun r ↦ Real.exp (G r) := by
      funext r
      by_cases hr : r = 0
      · subst r
        simp [lpMean, BooleanAnalysis.Hypercontractivity.cubeLpNorm, hnz, G, A, abs_of_pos (hu _)]
      · rw [lpMean, BooleanAnalysis.Hypercontractivity.cubeLpNorm]
        simp only [hnz, false_and, if_neg hr,
          BooleanAnalysis.Hypercontractivity.cubeLpNorm]
        have habs : expect (fun x ↦ |u x| ^ r) = M r := by
          have heq : (fun x ↦ |u x| ^ r) = fun x ↦ u x ^ r := by
            funext x
            rw [abs_of_pos (hu x)]
          rw [heq]
        rw [habs, Real.rpow_def_of_pos (hMpos r)]
        simp [G, hr, hM0, div_eq_mul_inv]
    rw [hfun]
    simpa only [Function.comp_def] using Real.continuous_exp.continuousAt.comp hG
  have zero_subsharp : ∀ (P R : ℝ), 0 < P → P < 1 →
      0 ≤ R → R ≤ 1 → R ^ 2 ≤ 1 - P →
      ∀ (u : BooleanFunc n), IsNonnegative u →
        lpMean 0 (noiseOp R u) ≥ lpMean P u := by
    intro P R hP0 hP1 hR0 hR1 hRsq u hu
    by_cases hu0 : u = 0
    · subst u
      rw [show noiseOp R (0 : BooleanFunc n) = 0 by
        funext x
        simp [noiseOp, BooleanAnalysis.fourierCoeff, innerProduct, expect]]
      simp [lpMean, BooleanAnalysis.Hypercontractivity.cubeLpNorm, hP0.ne', not_le.mpr hP0, expect, uniformWeight]
    · have hex : ∃ y, 0 < u y := by
        by_contra h
        push_neg at h
        exact hu0 (funext fun y ↦ le_antisymm (h y) (hu y))
      have hRlt : R < 1 := by nlinarith [sq_nonneg R]
      have houtpos := noise_strict_pos R hR0 hRlt u hu hex
      have ht : Filter.Tendsto (fun r : ℝ ↦ lpMean r (noiseOp R u))
          (nhdsWithin 0 (Set.Ioi 0)) (nhds (lpMean 0 (noiseOp R u))) :=
        (lpMean_continuous_zero (noiseOp R u) houtpos).mono_left inf_le_left
      apply ge_of_tendsto ht
      filter_upwards [self_mem_nhdsWithin,
        (eventually_lt_nhds hP0).filter_mono inf_le_left] with r hr0 hrP
      change 0 < r at hr0
      have hr1 : r < 1 := lt_trans hrP hP1
      have hbound : R ^ 2 ≤ (1 - P) / (1 - r) := by
        rw [le_div_iff₀ (sub_pos.mpr hr1)]
        calc
          R ^ 2 * (1 - r) ≤ R ^ 2 * 1 :=
            mul_le_mul_of_nonneg_left (by linarith) (sq_nonneg R)
          _ = R ^ 2 := by ring
          _ ≤ 1 - P := hRsq
      exact positive_subsharp P r R hr0 hrP hP1 hR0 hR1 hbound u hu
  have negative_subsharp : ∀ (P Q R : ℝ), Q < P → P < 0 →
      0 ≤ R → R ≤ 1 → R ^ 2 ≤ (1 - P) / (1 - Q) →
      ∀ (u : BooleanFunc n), IsNonnegative u →
        lpMean Q (noiseOp R u) ≥ lpMean P u := by
    intro P Q R hQP hP hR0 hR1 hRsq u hu
    by_cases hz : ∃ x, u x = 0
    · have hright : lpMean P u = 0 := by simp [lpMean, BooleanAnalysis.Hypercontractivity.cubeLpNorm, hz, hP.le]
      rw [hright]
      exact mean_nonneg Q _
    · have hupos : ∀ x, 0 < u x :=
        fun x ↦ (hu x).lt_of_ne (Ne.symm (not_exists.mp hz x))
      have hratio_lt : (1 - P) / (1 - Q) < 1 := by
        rw [div_lt_one (by linarith : 0 < 1 - Q)]
        linarith
      have hRlt : R < 1 := by nlinarith [sq_nonneg R]
      let H : BooleanFunc n := noiseOp R u
      have hHpos : ∀ x, 0 < H x :=
        noise_strict_pos R hR0 hRlt u hu ⟨Classical.arbitrary _, hupos _⟩
      have hE : 0 < expect (fun x ↦ H x ^ Q) :=
        expect_rpow_pos (fun x ↦ (hHpos x).le) ⟨Classical.arbitrary _, hHpos _⟩
      let A : ℝ := (expect (fun x ↦ H x ^ Q)) ^ (1 / Q)
      have hApos : 0 < A := Real.rpow_pos_of_pos hE _
      let Q' : ℝ := Q / (Q - 1)
      let P' : ℝ := P / (P - 1)
      have hQ'0 : 0 < Q' := by
        dsimp [Q']
        exact div_pos_of_neg_of_neg (lt_trans hQP hP) (by linarith)
      have hP'0 : 0 < P' := by
        dsimp [P']
        exact div_pos_of_neg_of_neg hP (by linarith)
      have hPm : P - 1 ≠ 0 := by linarith
      have hQm : Q - 1 ≠ 0 := by linarith
      have hOneP : 1 - P ≠ 0 := by linarith
      have hOneQ : 1 - Q ≠ 0 := by linarith
      have heqP : P / (P - 1) = (-P) / (1 - P) := by
        field_simp [hPm, hOneP]
        all_goals ring
      have heqQ : Q / (Q - 1) = (-Q) / (1 - Q) := by
        field_simp [hQm, hOneQ]
        all_goals ring
      have hP'Q' : P' < Q' := by
        dsimp [P', Q']
        rw [heqP, heqQ,
          div_lt_div_iff₀ (by linarith : 0 < 1 - P) (by linarith : 0 < 1 - Q)]
        nlinarith
      have hQ'1 : Q' < 1 := by
        dsimp [Q']
        rw [div_lt_iff_of_neg (by linarith : Q - 1 < 0)]
        linarith
      have h1Q : 1 - Q' = 1 / (1 - Q) := by
        dsimp [Q']
        field_simp [hQm, hOneQ]
        all_goals ring
      have h1P : 1 - P' = 1 / (1 - P) := by
        dsimp [P']
        field_simp [hPm, hOneP]
        all_goals ring
      have hratio : (1 - Q') / (1 - P') = (1 - P) / (1 - Q) := by
        rw [h1Q, h1P]
        field_simp [hOneP, hOneQ]
      let g : BooleanFunc n := fun x ↦ (H x / A) ^ (Q - 1)
      have hgpos (x : BoolCube n) : 0 < g x :=
        Real.rpow_pos_of_pos (div_pos (hHpos x) hApos) _
      have hQne : Q ≠ 0 := by linarith
      have hnormQ : expect (fun x ↦ (H x / A) ^ Q) = 1 := by
        simpa [A] using expect_normalized_rpow_eq_one
          hQne H (fun x ↦ (hHpos x).le) hE
      have hnormg : lpMean Q' g = 1 := by
        rw [lpMean_of_pos Q' hQ'0]
        simp_rw [abs_of_pos (hgpos _)]
        have hmom : expect (fun x ↦ g x ^ Q') = 1 := by
          rw [← hnormQ]
          apply congrArg expect
          funext x
          dsimp [g, Q']
          rw [← Real.rpow_mul (div_pos (hHpos x) hApos).le]
          congr 1
          field_simp [hQm]
        rw [hmom, one_div, Real.one_rpow]
      have hinner : innerProduct H g = A := by
        have hpoint (x : BoolCube n) : H x * g x = A * (H x / A) ^ Q := by
          dsimp [g]
          have hrpow :
              (H x / A) ^ Q = (H x / A) * (H x / A) ^ (Q - 1) := by
            calc
              (H x / A) ^ Q = (H x / A) ^ (Q - 1 + 1) := by
                congr 1
                all_goals ring
              _ = (H x / A) ^ (Q - 1) * (H x / A) ^ (1 : ℝ) :=
                Real.rpow_add (div_pos (hHpos x) hApos) (Q - 1) 1
              _ = (H x / A) * (H x / A) ^ (Q - 1) := by
                rw [Real.rpow_one]
                ring
          rw [hrpow]
          field_simp
        unfold innerProduct expect
        simp_rw [hpoint, ← Finset.mul_sum]
        rw [show uniformWeight n * (A * ∑ x, (H x / A) ^ Q) =
          A * (uniformWeight n * ∑ x, (H x / A) ^ Q) by ring]
        change A * expect (fun x ↦ (H x / A) ^ Q) = A
        rw [hnormQ]
        ring
      have hBB : lpMean P' (noiseOp R g) ≥ lpMean Q' g := by
        have hRsq' : R ^ 2 ≤ (1 - Q') / (1 - P') := by
          rw [hratio]
          exact hRsq
        exact positive_subsharp Q' P' R hP'0 hP'Q' hQ'1 hR0 hR1 hRsq' g
          (fun x ↦ (hgpos x).le)
      have hhold := reverse_holder P (by linarith : P < 1) (by linarith : P ≠ 0)
        u (noiseOp R g) hu (noiseOp_nonneg hR0 hR1 fun x ↦ (hgpos x).le)
      rw [show P / (P - 1) = P' by rfl] at hhold
      have hself : innerProduct u (noiseOp R g) = innerProduct H g := by
        dsimp [H]
        exact (BooleanAnalysis.noiseOp_self_adjoint R u g).symm
      rw [hself, hinner] at hhold
      rw [hnormg] at hBB
      have hmul : lpMean P u ≤ lpMean P u * lpMean P' (noiseOp R g) := by
        simpa only [mul_one] using
          mul_le_mul_of_nonneg_left hBB (mean_nonneg P u)
      have hA : A = lpMean Q H := by
        dsimp [A]
        rw [lpMean, BooleanAnalysis.Hypercontractivity.cubeLpNorm]
        simp only [not_exists.mpr (fun x hx ↦ (hHpos x).ne' hx), false_and, if_false,
          if_neg hQne, BooleanAnalysis.Hypercontractivity.cubeLpNorm]
        simp_rw [abs_of_pos (hHpos _)]
      dsimp [H] at hA
      rw [← hA]
      exact hmul.trans hhold
  have zero_target : ∀ (Q R : ℝ), Q < 0 →
      0 ≤ R → R ≤ 1 → R ^ 2 ≤ 1 / (1 - Q) →
      ∀ (u : BooleanFunc n), IsNonnegative u →
        lpMean Q (noiseOp R u) ≥ lpMean 0 u := by
    intro Q R hQ hR0 hR1 hRsq u hu
    by_cases hz : ∃ x, u x = 0
    · have hright : lpMean 0 u = 0 := by simp [lpMean, BooleanAnalysis.Hypercontractivity.cubeLpNorm, hz]
      rw [hright]
      exact mean_nonneg Q _
    · have hupos : ∀ x, 0 < u x :=
        fun x ↦ (hu x).lt_of_ne (Ne.symm (not_exists.mp hz x))
      have ht : Filter.Tendsto (fun r : ℝ ↦ lpMean r u)
          (nhdsWithin 0 (Set.Iio 0)) (nhds (lpMean 0 u)) :=
        (lpMean_continuous_zero u hupos).mono_left inf_le_left
      apply le_of_tendsto ht
      filter_upwards [self_mem_nhdsWithin,
        (eventually_gt_nhds hQ).filter_mono inf_le_left] with r hr0 hQr
      change r < 0 at hr0
      have hden : 0 < 1 - Q := by linarith
      have hscaled : R ^ 2 * (1 - Q) ≤ 1 := (le_div_iff₀ hden).mp hRsq
      have hbound : R ^ 2 ≤ (1 - r) / (1 - Q) := by
        rw [le_div_iff₀ hden]
        linarith
      exact negative_subsharp r Q R hQr hr0 hR0 hR1 hbound u hu
  have cross_zero : ∀ (P Q R : ℝ), Q < 0 → 0 < P → P < 1 →
      0 ≤ R → R ≤ 1 → R ^ 2 ≤ (1 - P) / (1 - Q) →
      ∀ (u : BooleanFunc n), IsNonnegative u →
        lpMean Q (noiseOp R u) ≥ lpMean P u := by
    intro P Q R hQ hP0 hP1 hR0 hR1 hRsq u hu
    let A : ℝ := Real.sqrt (1 / (1 - Q))
    have hden : 0 < 1 - Q := by linarith
    have hfrac : 0 < 1 / (1 - Q) := one_div_pos.mpr hden
    have hA0 : 0 < A := Real.sqrt_pos.2 hfrac
    have hAsq : A ^ 2 = 1 / (1 - Q) := Real.sq_sqrt hfrac.le
    have hfrac1 : 1 / (1 - Q) ≤ 1 := (div_le_one hden).2 (by linarith)
    have hA1 : A ≤ 1 := by nlinarith [hAsq, hA0, hfrac1]
    have hRA : R ≤ A := by
      rw [← sq_le_sq₀ hR0 hA0.le, hAsq]
      exact hRsq.trans (by
        rw [div_le_div_iff_of_pos_right hden]
        nlinarith)
    let T : ℝ := R / A
    have hT0 : 0 ≤ T := div_nonneg hR0 hA0.le
    have hT1 : T ≤ 1 := (div_le_one hA0).2 hRA
    have hscaled : R ^ 2 * (1 - Q) ≤ 1 - P := (le_div_iff₀ hden).mp hRsq
    have hTsq : T ^ 2 ≤ 1 - P := by
      dsimp [T]
      rw [div_pow, hAsq]
      field_simp [hden.ne', hA0.ne']
      nlinarith
    have hcomp : noiseOp A (noiseOp T u) = noiseOp R u := by
      rw [noiseOp_compose]
      congr 2
      dsimp [T]
      field_simp
    rw [← hcomp]
    exact le_trans
      (zero_subsharp P T hP0 hP1 hT0 hT1 hTsq u hu)
      (zero_target Q A hQ hA0.le hA1 hAsq.le (noiseOp T u)
        (noiseOp_nonneg hT0 hT1 hu))
  have lpMean_const (r c : ℝ) (hc : 0 ≤ c) :
      lpMean r (fun _ : BoolCube n ↦ c) = c := by
    by_cases hc0 : c = 0
    · subst c
      by_cases hr : r ≤ 0
      · simp [lpMean, BooleanAnalysis.Hypercontractivity.cubeLpNorm, hr]
      · have hr0 : 0 < r := lt_of_not_ge hr
        rw [lpMean_of_pos r hr0]
        simp [expect, uniformWeight, Real.zero_rpow hr0.ne']
        rw [Real.zero_rpow (inv_pos.mpr hr0).ne']
    · have hcpos : 0 < c := lt_of_le_of_ne hc (Ne.symm hc0)
      by_cases hr0 : r = 0
      · subst r
        simp [lpMean, BooleanAnalysis.Hypercontractivity.cubeLpNorm, hc0, abs_of_pos hcpos, expect, uniformWeight, Real.exp_log hcpos]
      · rw [lpMean, BooleanAnalysis.Hypercontractivity.cubeLpNorm]
        simp only [not_exists.mpr (fun _ h ↦ hc0 h), false_and, if_false, if_neg hr0,
          BooleanAnalysis.Hypercontractivity.cubeLpNorm, abs_of_pos hcpos]
        have he : expect (fun _ : BoolCube n ↦ c ^ r) = c ^ r := by
          simp [expect, uniformWeight]
        rw [he, ← Real.rpow_mul hcpos.le]
        field_simp
        exact Real.rpow_one c
  have noiseOp_zero (u : BooleanFunc n) :
      noiseOp 0 u = fun _ ↦ expect u := by
    funext x
    rw [GeneralHypercontractivity.noiseOp_eq_kernel_sum]
    unfold GeneralHypercontractivity.noiseKernel expect uniformWeight
    simp [Finset.prod_const, Finset.card_univ, ← Finset.mul_sum]
  have endpoint_one : ∀ (Q R : ℝ), Q < 1 → 0 ≤ R → R ≤ 1 →
      R ^ 2 ≤ (1 - 1) / (1 - Q) →
      ∀ (u : BooleanFunc n), IsNonnegative u →
        lpMean Q (noiseOp R u) ≥ lpMean 1 u := by
    intro Q R hQ hR0 hR1 hRsq u hu
    have hR : R = 0 := by
      have hden : 0 < 1 - Q := sub_pos.mpr hQ
      rw [show (1 - 1) / (1 - Q) = 0 by
        field_simp
        all_goals ring] at hRsq
      nlinarith [sq_nonneg R]
    subst R
    rw [noiseOp_zero]
    have hexpect : 0 ≤ expect u := by
      rw [expect_eq_fintypeExpect]
      exact Finset.expect_nonneg fun x _ ↦ hu x
    rw [lpMean_const Q (expect u) hexpect, lpMean_of_pos 1 (by norm_num)]
    simp_rw [abs_of_nonneg (hu _), Real.rpow_one]
    norm_num
  have noiseOp_one (u : BooleanFunc n) : noiseOp 1 u = u := by
    funext x
    unfold noiseOp
    simp only [one_pow, one_mul]
    exact (walsh_expansion u x).symm
  by_cases hp1 : p = 1
  · subst p
    exact endpoint_one q ρ hq hρ0 hρ1 hρsq f hf
  have hp' : p < 1 := lt_of_le_of_ne hp hp1
  by_cases hqp' : q = p
  · subst q
    simpa only [noiseOp_one] using
      lpMean_noise_antitone p ρ 1 hp' hρ0 hρ1 (by norm_num) f hf
  have hqp'' : q < p := lt_of_le_of_ne hqp hqp'
  rcases lt_trichotomy p 0 with hpneg | hpzero | hppos
  · exact negative_subsharp p q ρ hqp'' hpneg hρ0 hρ1 hρsq f hf
  · subst p
    exact zero_target q ρ (by linarith) hρ0 hρ1 (by simpa using hρsq) f hf
  · rcases lt_trichotomy q 0 with hqneg | hqzero | hqpos
    · exact cross_zero p q ρ hqneg hppos hp' hρ0 hρ1 hρsq f hf
    · subst q
      exact zero_subsharp p ρ hppos hp' hρ0 hρ1 (by simpa using hρsq) f hf
    · exact positive_subsharp p q ρ hqpos hqp'' hp' hρ0 hρ1 hρsq f hf

-- TCSlib.BooleanAnalysis.Hypercontractivity.ReverseBonamiBeckner:1451
/-- Reverse hypercontractivity holds for nonnegative cube functions and finite
`q ≤ p ≤ 1`, `q < 1`, at the stated sharp correlation bound.
The source's strict `q < p` theorem is extended here to equal finite exponents.
Its `q = -∞` minimum-mean endpoint is not represented.

**Source:** [OD14, Exs. 10.6--10.9]. -/
theorem reverse_bonami_beckner (p q ρ : ℝ)
    (hq : q < 1) (hqp : q ≤ p) (hp : p ≤ 1)
    (hρ0 : 0 ≤ ρ) (hρ1 : ρ ≤ 1) (hρsq : ρ ^ 2 ≤ (1 - p) / (1 - q))
    (f : BooleanFunc n) (hf : IsNonnegative f) :
    lpMean q (noiseOp ρ f) ≥ lpMean p f :=
  extend_reverse_bonami_beckner p q ρ hq hqp hp hρ0 hρ1 hρsq f hf

-- TCSlib.BooleanAnalysis.Hypercontractivity.ReverseBonamiBeckner:1464
/-- Extended power means of a nonnegative function are nondecreasing in their exponent
up to one. [OD14, Exs. 10.6--10.9, extended-mean calculus]

**Proof sketch.** Jensen's inequality for powers compares exponents of the same sign.
Concavity of the logarithm compares either side with the geometric mean at zero.
If a function has a zero, use the stipulated zero value of its nonpositive means. -/
private lemma lpMean_exponent_mono (a b : ℝ) (hab : a ≤ b) (hb : b ≤ 1)
    (f : BooleanFunc n) (hf : IsNonnegative f) :
    lpMean a f ≤ lpMean b f := by
  have lpMean_nonneg_all (p : ℝ) (f : BooleanFunc n) : 0 ≤ lpMean p f := by
    unfold lpMean
    split_ifs
    · exact le_rfl
    · positivity
    · exact Real.rpow_nonneg (by
        rw [expect_eq_fintypeExpect]
        exact Finset.expect_nonneg fun x _ ↦ Real.rpow_nonneg (abs_nonneg (f x)) p) _
  have expect_pos_of_pos (f : BooleanFunc n) (hf : ∀ x, 0 < f x) : 0 < expect f := by
    unfold expect uniformWeight
    exact mul_pos (pow_pos (by norm_num) _)
      (Finset.sum_pos (fun x _ ↦ hf x) Finset.univ_nonempty)
  have expect_rpow_jensen (t : ℝ) (ht : 1 ≤ t)
      (f : BooleanFunc n) (hf : ∀ x, 0 ≤ f x) :
      (expect f) ^ t ≤ expect (fun x ↦ f x ^ t) := by
    unfold expect
    have hw : ∑ _x : BoolCube n, uniformWeight n = 1 := by
      unfold uniformWeight
      simp [Finset.card_univ]
    have h := Real.rpow_arith_mean_le_arith_mean_rpow
      (Finset.univ : Finset (BoolCube n)) (fun _ ↦ uniformWeight n) f
      (fun _ _ ↦ pow_nonneg (by norm_num) _) hw (fun x _ ↦ hf x) ht
    simpa only [← Finset.mul_sum] using h
  have expect_log_le_log_expect (f : BooleanFunc n) (hf : ∀ x, 0 < f x) :
      expect (fun x ↦ Real.log (f x)) ≤ Real.log (expect f) := by
    unfold expect
    have hw : ∑ _x : BoolCube n, uniformWeight n = 1 := by
      unfold uniformWeight
      simp [Finset.card_univ]
    have h := strictConcaveOn_log_Ioi.concaveOn.le_map_sum
      (t := (Finset.univ : Finset (BoolCube n))) (w := fun _ ↦ uniformWeight n) (p := f)
      (fun _ _ ↦ pow_nonneg (by norm_num) _) hw (fun x _ ↦ hf x)
    simpa only [smul_eq_mul, ← Finset.mul_sum] using h
  have lpMean_mono_pos_exp {a b : ℝ} (ha : 0 < a) (hab : a ≤ b)
      (f : BooleanFunc n) (hf : IsNonnegative f) : lpMean a f ≤ lpMean b f := by
    have hb : 0 < b := lt_of_lt_of_le ha hab
    rw [lpMean_of_pos a ha, lpMean_of_pos b hb]
    simp_rw [abs_of_nonneg (hf _)]
    have hA : 0 ≤ expect (fun x ↦ f x ^ a) :=
      by
        rw [expect_eq_fintypeExpect]
        exact Finset.expect_nonneg fun x _ ↦ Real.rpow_nonneg (hf x) a
    have hB : 0 ≤ expect (fun x ↦ f x ^ b) :=
      by
        rw [expect_eq_fintypeExpect]
        exact Finset.expect_nonneg fun x _ ↦ Real.rpow_nonneg (hf x) b
    have hratio : 1 ≤ b / a := by
      apply (le_div_iff₀ ha).2
      simpa using hab
    have hJ := expect_rpow_jensen (b / a) hratio (fun x ↦ f x ^ a)
      (fun x ↦ Real.rpow_nonneg (hf x) a)
    simp_rw [← Real.rpow_mul (hf _)] at hJ
    have hab' : a * (b / a) = b := by field_simp
    rw [hab'] at hJ
    rw [← Real.rpow_le_rpow_iff (Real.rpow_nonneg hA _) (Real.rpow_nonneg hB _) hb]
    rw [← Real.rpow_mul hA, ← Real.rpow_mul hB]
    have hleft : 1 / a * b = b / a := by field_simp
    have hright : 1 / b * b = 1 := by field_simp
    rw [hleft, hright, Real.rpow_one]
    exact hJ
  have lpMean_mono_neg_exp {a b : ℝ} (ha : a < 0) (hab : a ≤ b) (hb : b < 0)
      (f : BooleanFunc n) (hf : IsNonnegative f) : lpMean a f ≤ lpMean b f := by
    by_cases hz : ∃ x, f x = 0
    · simp only [lpMean, BooleanAnalysis.Hypercontractivity.cubeLpNorm, hz, true_and, if_pos ha.le, if_pos hb.le]
      exact le_rfl
    · have hfpos : ∀ x, 0 < f x :=
        fun x ↦ lt_of_le_of_ne (hf x) (Ne.symm (not_exists.mp hz x))
      simp only [lpMean, BooleanAnalysis.Hypercontractivity.cubeLpNorm, hz, false_and, if_false, if_neg ha.ne, if_neg hb.ne,
        BooleanAnalysis.Hypercontractivity.cubeLpNorm]
      simp_rw [abs_of_pos (hfpos _)]
      have hA : 0 < expect (fun x ↦ f x ^ a) :=
        expect_pos_of_pos _ fun x ↦ Real.rpow_pos_of_pos (hfpos x) a
      have hB : 0 < expect (fun x ↦ f x ^ b) :=
        expect_pos_of_pos _ fun x ↦ Real.rpow_pos_of_pos (hfpos x) b
      have hratio : 1 ≤ a / b := by
        rw [le_div_iff_of_neg hb]
        nlinarith
      have hJ := expect_rpow_jensen (a / b) hratio (fun x ↦ f x ^ b)
        (fun x ↦ Real.rpow_nonneg (hf x) b)
      simp_rw [← Real.rpow_mul (hf _)] at hJ
      have hab' : b * (a / b) = a := by field_simp [hb.ne]
      rw [hab'] at hJ
      rw [← Real.rpow_le_rpow_iff_of_neg
        (Real.rpow_pos_of_pos hB _) (Real.rpow_pos_of_pos hA _) ha]
      rw [← Real.rpow_mul hB.le, ← Real.rpow_mul hA.le]
      have hleft : 1 / b * a = a / b := by field_simp
      have hright : 1 / a * a = 1 := by field_simp [ha.ne]
      rw [hleft, hright, Real.rpow_one]
      exact hJ
  have lpMean_neg_le_zero {a : ℝ} (ha : a < 0)
      (f : BooleanFunc n) (hf : IsNonnegative f) :
      lpMean a f ≤ lpMean 0 f := by
    by_cases hz : ∃ x, f x = 0
    · simp [lpMean, BooleanAnalysis.Hypercontractivity.cubeLpNorm, hz, ha.le]
    · have hfpos : ∀ x, 0 < f x :=
        fun x ↦ lt_of_le_of_ne (hf x) (Ne.symm (not_exists.mp hz x))
      rw [show lpMean a f = (expect (fun x ↦ f x ^ a)) ^ (1 / a) by
        simp [lpMean, BooleanAnalysis.Hypercontractivity.cubeLpNorm, hz, ha.ne, abs_of_pos (hfpos _)],
        show lpMean 0 f = Real.exp (expect (fun x ↦ Real.log (f x))) by
          simp [lpMean, BooleanAnalysis.Hypercontractivity.cubeLpNorm, hz, abs_of_pos (hfpos _)]]
      have hA : 0 < expect (fun x ↦ f x ^ a) :=
        expect_pos_of_pos _ fun x ↦ Real.rpow_pos_of_pos (hfpos x) a
      rw [Real.rpow_def_of_pos hA]
      apply Real.exp_le_exp.mpr
      have hJ := expect_log_le_log_expect (fun x ↦ f x ^ a)
        (fun x ↦ Real.rpow_pos_of_pos (hfpos x) a)
      simp_rw [Real.log_rpow (hfpos _)] at hJ
      have hJ' : a * expect (fun x ↦ Real.log (f x)) ≤
          Real.log (expect (fun x ↦ f x ^ a)) := by
        convert hJ using 1
        unfold expect
        rw [← Finset.mul_sum]
        ring
      calc
        Real.log (expect (fun x ↦ f x ^ a)) * (1 / a) =
            Real.log (expect (fun x ↦ f x ^ a)) / a := by ring_nf
        _ ≤ expect (fun x ↦ Real.log (f x)) :=
          (div_le_iff_of_neg ha).2 (by simpa [mul_comm] using hJ')
  have lpMean_zero_le_pos {b : ℝ} (hb : 0 < b)
      (f : BooleanFunc n) (hf : IsNonnegative f) :
      lpMean 0 f ≤ lpMean b f := by
    by_cases hz : ∃ x, f x = 0
    · have hzero : lpMean 0 f = 0 := by simp [lpMean, BooleanAnalysis.Hypercontractivity.cubeLpNorm, hz]
      rw [hzero]
      exact lpMean_nonneg_all b f
    · have hfpos : ∀ x, 0 < f x :=
        fun x ↦ lt_of_le_of_ne (hf x) (Ne.symm (not_exists.mp hz x))
      rw [show lpMean 0 f = Real.exp (expect (fun x ↦ Real.log (f x))) by
        simp [lpMean, BooleanAnalysis.Hypercontractivity.cubeLpNorm, hz, abs_of_pos (hfpos _)],
        lpMean_of_pos b hb]
      simp_rw [abs_of_pos (hfpos _)]
      have hB : 0 < expect (fun x ↦ f x ^ b) :=
        expect_pos_of_pos _ fun x ↦ Real.rpow_pos_of_pos (hfpos x) b
      rw [Real.rpow_def_of_pos hB]
      apply Real.exp_le_exp.mpr
      have hJ := expect_log_le_log_expect (fun x ↦ f x ^ b)
        (fun x ↦ Real.rpow_pos_of_pos (hfpos x) b)
      simp_rw [Real.log_rpow (hfpos _)] at hJ
      have hJ' : b * expect (fun x ↦ Real.log (f x)) ≤
          Real.log (expect (fun x ↦ f x ^ b)) := by
        convert hJ using 1
        unfold expect
        rw [← Finset.mul_sum]
        ring
      calc
        expect (fun x ↦ Real.log (f x)) ≤
            Real.log (expect (fun x ↦ f x ^ b)) / b :=
          (le_div_iff₀ hb).2 (by simpa [mul_comm] using hJ')
        _ = Real.log (expect (fun x ↦ f x ^ b)) * (1 / b) := by ring_nf
  rcases lt_trichotomy b 0 with hbneg | hbzero | hbpos
  · exact lpMean_mono_neg_exp (lt_of_le_of_lt hab hbneg) hab hbneg f hf
  · subst b
    rcases lt_or_eq_of_le hab with haneg | ha0
    · exact lpMean_neg_le_zero haneg f hf
    · subst a
      exact le_rfl
  · rcases lt_trichotomy a 0 with haneg | hazero | hapos
    · exact (lpMean_neg_le_zero haneg f hf).trans (lpMean_zero_le_pos hbpos f hf)
    · subst a
      exact lpMean_zero_le_pos hbpos f hf
    · exact lpMean_mono_pos_exp hapos hab f hf

-- TCSlib.BooleanAnalysis.Hypercontractivity.ReverseBonamiBeckner:1635
/-- The two-function form gives `E[f(x)g(y)] ≥ ‖f‖_p ‖g‖_q` for nonnegative
functions on correlated Boolean strings and finite `p,q < 1`.
The source also permits an exponent of one at correlation zero; those endpoint cases
and infinite exponents are not represented by this declaration.

**Source:** [OD14, Exs. 10.6--10.9]. -/
theorem reverse_bonami_beckner_two_function (p q ρ : ℝ)
    (hp : p < 1) (hq : q < 1)
    (hρ0 : 0 ≤ ρ) (hρ1 : ρ ≤ 1) (hρsq : ρ ^ 2 ≤ (1 - p) * (1 - q))
    (f g : BooleanFunc n) (hf : IsNonnegative f) (hg : IsNonnegative g) :
    innerProduct f (noiseOp ρ g) ≥ lpMean p f * lpMean q g := by
  have lpMean_nonneg_all (r : ℝ) (u : BooleanFunc n) : 0 ≤ lpMean r u := by
    unfold lpMean
    split_ifs
    · exact le_rfl
    · exact (Real.exp_pos _).le
    · exact Real.rpow_nonneg (by
        rw [expect_eq_fintypeExpect]
        exact Finset.expect_nonneg fun x _ ↦ Real.rpow_nonneg (abs_nonneg _) _) _
  have lpMean_zero_le_expect (u : BooleanFunc n) (hu : IsNonnegative u) :
      lpMean 0 u ≤ expect u := by
    convert lpMean_exponent_mono 0 1 (by norm_num) le_rfl u hu using 1
    rw [lpMean_of_pos 1 zero_lt_one]
    simp [abs_of_nonneg (hu _)]
  have reverse_holder_zero (u v : BooleanFunc n) (hu : IsNonnegative u)
      (hv : IsNonnegative v) :
      innerProduct u v ≥ lpMean 0 u * lpMean 0 v := by
    classical
    by_cases huzero : ∃ x, u x = 0
    · rw [show lpMean 0 u = 0 by simp [lpMean, BooleanAnalysis.Hypercontractivity.cubeLpNorm, huzero], zero_mul]
      unfold innerProduct
      rw [expect_eq_fintypeExpect]
      exact Finset.expect_nonneg fun x _ ↦ mul_nonneg (hu x) (hv x)
    · by_cases hvzero : ∃ x, v x = 0
      · rw [show lpMean 0 v = 0 by simp [lpMean, BooleanAnalysis.Hypercontractivity.cubeLpNorm, hvzero], mul_zero]
        unfold innerProduct
        rw [expect_eq_fintypeExpect]
        exact Finset.expect_nonneg fun x _ ↦ mul_nonneg (hu x) (hv x)
      · have hupos : ∀ x, 0 < u x := fun x ↦
            (hu x).lt_of_ne (Ne.symm (not_exists.mp huzero x))
        have hvpos : ∀ x, 0 < v x := fun x ↦
            (hv x).lt_of_ne (Ne.symm (not_exists.mp hvzero x))
        have hprodpos : IsNonnegative (fun x ↦ u x * v x) :=
          fun x ↦ mul_nonneg (hu x) (hv x)
        have hprodzero : ¬∃ x, u x * v x = 0 := by
          push_neg
          exact fun x ↦ mul_ne_zero (hupos x).ne' (hvpos x).ne'
        have hmul : lpMean 0 (fun x ↦ u x * v x) = lpMean 0 u * lpMean 0 v := by
          rw [show lpMean 0 (fun x ↦ u x * v x) =
              Real.exp (expect (fun x ↦ Real.log (u x * v x))) by
            unfold lpMean
            rw [if_neg (by simpa using hprodzero), if_pos rfl]
            simp_rw [abs_of_pos (mul_pos (hupos _) (hvpos _))]]
          rw [show lpMean 0 u = Real.exp (expect (fun x ↦ Real.log (u x))) by
            simp [lpMean, BooleanAnalysis.Hypercontractivity.cubeLpNorm, huzero, abs_of_pos (hupos _)]]
          rw [show lpMean 0 v = Real.exp (expect (fun x ↦ Real.log (v x))) by
            simp [lpMean, BooleanAnalysis.Hypercontractivity.cubeLpNorm, hvzero, abs_of_pos (hvpos _)]]
          simp_rw [Real.log_mul (hupos _).ne' (hvpos _).ne']
          unfold expect
          rw [Finset.sum_add_distrib, mul_add, Real.exp_add]
        rw [← hmul]
        exact lpMean_zero_le_expect (fun x ↦ u x * v x) hprodpos
  have two_function_core : ∀ (a b R : ℝ), a < 1 → a ≠ 0 →
      0 ≤ R → R ≤ 1 → R ^ 2 ≤ (1 - a) * (1 - b) →
      ∀ (u v : BooleanFunc n), IsNonnegative u → IsNonnegative v →
        innerProduct u (noiseOp R v) ≥ lpMean a u * lpMean b v := by
    intro a b R ha ha0 hR0 hR1 hRsq u v hu hv
    let c := a / (a - 1)
    let d := 1 - R ^ 2 / (1 - a)
    have h1a : 0 < 1 - a := sub_pos.mpr ha
    have ham1 : a - 1 ≠ 0 := (sub_neg.mpr ha).ne
    have hc1 : c < 1 := by
      dsimp [c]
      rw [div_lt_iff_of_neg (sub_neg.mpr ha)]
      linarith
    have hconj : 1 - c = 1 / (1 - a) := by
      dsimp [c]
      field_simp [h1a.ne', ham1]
      ring
    have hRsq1 : R ^ 2 ≤ 1 := by nlinarith
    have hbd : b ≤ d := by
      have hdiv : R ^ 2 / (1 - a) ≤ 1 - b := by
        rw [div_le_iff₀ h1a]
        simpa [mul_comm] using hRsq
      dsimp [d]
      linarith
    have hd1 : d ≤ 1 := by
      dsimp [d]
      exact sub_le_self 1 (div_nonneg (sq_nonneg R) h1a.le)
    have hcd : c ≤ d := by
      rw [show c = 1 - 1 / (1 - a) by linarith [hconj]]
      dsimp [d]
      have := div_le_div_of_nonneg_right hRsq1 h1a.le
      linarith
    have hratio : (1 - d) / (1 - c) = R ^ 2 := by
      rw [hconj]
      dsimp [d]
      field_simp [h1a.ne']
      ring
    have hholder := reverse_holder a ha ha0 u (noiseOp R v) hu
      (noiseOp_nonneg hR0 hR1 hv)
    have hbb := reverse_bonami_beckner d c R hc1 hcd hd1 hR0 hR1
      (by rw [hratio]) v hv
    have hmean : lpMean c (noiseOp R v) ≥ lpMean b v :=
      (lpMean_exponent_mono b d hbd hd1 v hv).trans hbb
    exact (mul_le_mul_of_nonneg_left hmean (lpMean_nonneg_all a u)).trans hholder
  by_cases hp0 : p = 0
  · by_cases hq0 : q = 0
    · subst p
      subst q
      have hhold :=
        reverse_holder_zero f (noiseOp ρ g) hf (noiseOp_nonneg hρ0 hρ1 hg)
      have hcorr : ρ ^ 2 ≤ (1 - (0 : ℝ)) / (1 - (0 : ℝ)) := by
        norm_num
        simpa using hρsq
      have hbb := reverse_bonami_beckner 0 0 ρ (by norm_num) le_rfl (by norm_num)
        hρ0 hρ1 hcorr g hg
      exact (mul_le_mul_of_nonneg_left hbb (lpMean_nonneg_all 0 f)).trans hhold
    · subst p
      calc
        lpMean 0 f * lpMean q g = lpMean q g * lpMean 0 f := mul_comm _ _
        _ ≤ innerProduct g (noiseOp ρ f) := two_function_core q 0 ρ hq hq0 hρ0 hρ1
          (by simpa [mul_comm] using hρsq) g f hg hf
        _ = innerProduct f (noiseOp ρ g) := by
          rw [innerProduct_comm, noiseOp_self_adjoint]
  · exact two_function_core p q ρ hp hp0 hρ0 hρ1 hρsq f g hf hg

end ReverseBonamiBeckner

namespace Er579

open BooleanAnalysis BooleanAnalysis.Hypercontractivity ReverseBonamiBeckner

-- Er579.ReverseInput:18
theorem cube_indicator_nonnegative {n : ℕ} (A : BoolCube n → Prop) :
    IsNonnegative (cubeIndicator A) := by
  classical
  intro x
  by_cases hx : A x <;> simp [cubeIndicator, hx]

-- Er579.ReverseInput:24
theorem cube_probability_nonnegative {n : ℕ} (A : BoolCube n → Prop) :
    0 ≤ cubeProbability A := by
  unfold cubeProbability
  rw [expect_eq_fintypeExpect]
  exact Finset.expect_nonneg fun x _ ↦ cube_indicator_nonnegative A x

-- Er579.ReverseInput:30
theorem cube_indicator_power_mean {n : ℕ} (A : BoolCube n → Prop)
    (p : ℝ) (hp : 0 < p) :
    lpMean p (cubeIndicator A) = (cubeProbability A) ^ (1 / p) := by
  classical
  rw [lpMean_of_pos p hp]
  have hpow : (fun x ↦ |cubeIndicator A x| ^ p) = cubeIndicator A := by
    funext x
    by_cases hx : A x <;> simp [cubeIndicator, hx, Real.zero_rpow hp.ne']
  rw [hpow]
  rfl

-- Er579.ReverseInput:41
/-- Two uniform Boolean events have a dimension-independent positive-noise
joint-probability lower bound. The correlation parameter is `ρ`; its bit-flip
probability is `(1-ρ)/2`. -/
theorem cube_set_mixing {n : ℕ} (ρ : ℝ) (hρ0 : 0 < ρ) (hρ1 : ρ < 1)
    (A B : BoolCube n → Prop) :
    (cubeProbability A) ^ (1 / (1 - ρ)) *
        (cubeProbability B) ^ (1 / (1 - ρ)) ≤
      innerProduct (cubeIndicator A) (noiseOp ρ (cubeIndicator B)) := by
  have hp : 0 < 1 - ρ := sub_pos.mpr hρ1
  have hp1 : 1 - ρ < 1 := sub_lt_self 1 hρ0
  have hsq : ρ ^ 2 ≤ (1 - (1 - ρ)) * (1 - (1 - ρ)) := by
    nlinarith
  have h := reverse_bonami_beckner_two_function (1 - ρ) (1 - ρ) ρ
    hp1 hp1 hρ0.le hρ1.le hsq (cubeIndicator A) (cubeIndicator B)
    (cube_indicator_nonnegative A) (cube_indicator_nonnegative B)
  rw [cube_indicator_power_mean A (1 - ρ) hp,
    cube_indicator_power_mean B (1 - ρ) hp] at h
  exact h

-- Er579.ReverseInput:60
/-- Equal-mass events, including a set and its antipodal translate, have
joint probability at least `a^(2/(1-ρ))`. -/
theorem cube_set_mixing_same_mass {n : ℕ} (ρ : ℝ)
    (hρ0 : 0 < ρ) (hρ1 : ρ < 1) (A B : BoolCube n → Prop)
    (hAB : cubeProbability B = cubeProbability A) :
    (cubeProbability A) ^ (2 / (1 - ρ)) ≤
      innerProduct (cubeIndicator A) (noiseOp ρ (cubeIndicator B)) := by
  have h := cube_set_mixing ρ hρ0 hρ1 A B
  rw [hAB] at h
  have hexp : 1 / (1 - ρ) + 1 / (1 - ρ) = 2 / (1 - ρ) := by ring
  have hsum : 1 / (1 - ρ) + 1 / (1 - ρ) ≠ 0 :=
    ne_of_gt (add_pos (one_div_pos.mpr (sub_pos.mpr hρ1))
      (one_div_pos.mpr (sub_pos.mpr hρ1)))
  rw [← Real.rpow_add' (cube_probability_nonnegative A) hsum] at h
  simpa only [hexp] using h

end Er579

end

section

/-! Selected, proved classical Friedgut and Russo inputs, with the
 dimension-independent Er579 adapter. This file imports Mathlib alone.
 Upstream Apache 2.0 notices are retained in each source fragment. -/

/- Source fragment: FABL.Chapter01.FunctionsAsMultilinearPolynomials. Original licenses and source proofs retained. -/

section

/-
Copyright (c) 2026 Asher Yan. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Asher Yan with Codex
-/

/-!
# Functions as multilinear polynomials

Book items: Definition 1.2, Theorem 1.1, Exercise 1.10, Exercise 1.11(b).

Formalization of Sections 1.1 and 1.2 of O'Donnell's *Analysis of Boolean Functions*.

Each section uses the cube representation appropriate to its mathematical statements.
-/

open scoped BigOperators

namespace FABL

variable {n : ℕ}

-- Source: FABL.Chapter01.FunctionsAsMultilinearPolynomials:34
/-- The sign alphabet `{-1, 1}`, represented by the two units of `ℤ`. -/
abbrev Sign := ℤˣ

-- Source: FABL.Chapter01.FunctionsAsMultilinearPolynomials:37
/-- The sign cube `{-1, 1}ⁿ`. -/
abbrev SignCube (n : ℕ) := Fin n → Sign

-- Source: FABL.Chapter01.FunctionsAsMultilinearPolynomials:45
/-- The real value of a sign. -/
def signValue (s : Sign) : ℝ := ((s : ℤ) : ℝ)

-- Source: FABL.Chapter01.FunctionsAsMultilinearPolynomials:48
 theorem signValue_one : signValue 1 = 1 := by
  simp [signValue]

-- Source: FABL.Chapter01.FunctionsAsMultilinearPolynomials:51
 theorem signValue_neg_one : signValue (-1) = -1 := by
  simp [signValue]

-- Source: FABL.Chapter01.FunctionsAsMultilinearPolynomials:58
/-- The indicator polynomial `𝟙_{a}(x) = ∏ᵢ (1 + aᵢxᵢ)/2` from Section 1.2. -/
noncomputable def indicatorPolynomial (a x : (FABL.SignCube (n))) : ℝ :=
  ∏ i, (1 + signValue (a i) * signValue (x i)) / 2

-- Source: FABL.Chapter01.FunctionsAsMultilinearPolynomials:62
/-- The indicator polynomial is one exactly at its indexed point. -/
theorem indicatorPolynomial_eq_ite (a x : (FABL.SignCube (n))) :
    indicatorPolynomial a x = if x = a then 1 else 0 := by
  classical
  have hfactor (i : Fin n) :
      (1 + signValue (a i) * signValue (x i)) / 2 =
        if x i = a i then (1 : ℝ) else 0 := by
    rcases Int.units_eq_one_or (a i) with ha | ha <;>
      rcases Int.units_eq_one_or (x i) with hx | hx <;>
      simp [signValue, ha, hx]
  rw [indicatorPolynomial]
  simp_rw [hfactor]
  rw [Fintype.prod_boole]
  congr 1
  apply propext
  constructor
  · intro h
    funext i
    exact h i
  · intro h i
    exact congrFun h i

-- Source: FABL.Chapter01.FunctionsAsMultilinearPolynomials:84
/-- The interpolation formula used for existence in O'Donnell, Theorem 1.1. -/
theorem sum_indicatorPolynomial (f : (FABL.SignCube (n)) → ℝ) (x : (FABL.SignCube (n))) :
    f x = ∑ a, f a * indicatorPolynomial a x := by
  classical
  simp [indicatorPolynomial_eq_ite]

-- Source: FABL.Chapter01.FunctionsAsMultilinearPolynomials:90
/-- The monomial `xˢ = ∏ i ∈ S, xᵢ` on the sign cube. -/
def monomial (S : Finset (Fin n)) (x : (FABL.SignCube (n))) : ℝ :=
  ∏ i ∈ S, signValue (x i)

-- Source: FABL.Chapter01.FunctionsAsMultilinearPolynomials:94
/-- A sign-cube monomial bundled as a character of the additivized multiplicative cube. -/
noncomputable def signMonomialChar (S : Finset (Fin n)) :
    AddChar (Additive ((FABL.SignCube (n)))) ℝ where
  toFun x := monomial S x.toMul
  map_zero_eq_one' := by simp [monomial, signValue]
  map_add_eq_mul' x y := by
    simp [monomial, signValue, Finset.prod_mul_distrib]

-- Source: FABL.Chapter01.FunctionsAsMultilinearPolynomials:102
/-- The subset parameterization of sign-cube monomial characters is injective. -/
theorem signMonomialChar_injective : Function.Injective
    (signMonomialChar : Finset (Fin n) → AddChar (Additive ((FABL.SignCube (n)))) ℝ) := by
  classical
  intro S T h
  ext i
  have hi := congrArg
    (fun ψ : AddChar (Additive ((FABL.SignCube (n)))) ℝ ↦
      ψ (.ofMul (fun j ↦ if j = i then -1 else 1))) h
  have hv (j : Fin n) : signValue (if j = i then -1 else 1) =
      if j = i then (-1 : ℝ) else 1 := by
    split_ifs <;> simp [signValue_one, signValue_neg_one]
  have hi' : (if i ∈ S then (-1 : ℝ) else 1) = if i ∈ T then -1 else 1 := by
    simpa [signMonomialChar, monomial, hv, Finset.prod_ite_eq'] using hi
  by_cases hS : i ∈ S <;> by_cases hT : i ∈ T <;>
    simp [hS, hT] at hi' ⊢ <;> norm_num at hi'

-- Source: FABL.Chapter01.FunctionsAsMultilinearPolynomials:119
/-- Orthogonality of sign-cube monomials, delegated to Mathlib's finite-character theorem. -/
theorem expect_monomial_mul (S T : Finset (Fin n)) :
    (𝔼 x : (FABL.SignCube (n)), monomial S x * monomial T x) = if S = T then 1 else 0 := by
  have hreindex : (𝔼 x : (FABL.SignCube (n)), monomial S x * monomial T x) =
      RCLike.wInner RCLike.cWeight (signMonomialChar S) (signMonomialChar T) := by
    rw [RCLike.wInner_cWeight_eq_expect]
    symm
    apply Fintype.expect_equiv Additive.toMul
    intro x
    simp [RCLike.inner_apply, signMonomialChar, mul_comm] <;> rfl
  rw [hreindex]
  simpa [signMonomialChar_injective.eq_iff] using
    (AddChar.wInner_cWeight_eq_boole (signMonomialChar S) (signMonomialChar T))

-- Source: FABL.Chapter01.FunctionsAsMultilinearPolynomials:152
/-- The uniform coefficient `f̂(S)` of a real-valued function on the sign cube. -/
noncomputable def fourierCoeff (f : (FABL.SignCube (n)) → ℝ) (S : Finset (Fin n)) : ℝ :=
  𝔼 x, f x * monomial S x

/-! The private finite-index API below is used only for the proof of Exercise 1.11(b). -/

-- Source: FABL.Chapter01.FunctionsAsMultilinearPolynomials:327
/-- The indicator interpolation polynomial expanded in the squarefree monomial family. -/
theorem indicatorPolynomial_fourier_sum (a x : (FABL.SignCube (n))) :
    indicatorPolynomial a x =
      (Fintype.card ((FABL.SignCube (n))) : ℝ)⁻¹ * ∑ S, monomial S a * monomial S x := by
  classical
  rw [indicatorPolynomial]
  calc
    (∏ i, (1 + signValue (a i) * signValue (x i)) / 2) =
        ∏ i, (2 : ℝ)⁻¹ * (signValue (a i) * signValue (x i) + 1) := by
      apply Finset.prod_congr rfl
      intro i _
      ring
    _ = (∏ _i : Fin n, (2 : ℝ)⁻¹) *
        ∏ i, (signValue (a i) * signValue (x i) + 1) := by
      rw [Finset.prod_mul_distrib]
    _ = (Fintype.card ((FABL.SignCube (n))) : ℝ)⁻¹ *
        ∏ i, (signValue (a i) * signValue (x i) + 1) := by
      congr 1
      simp [Fintype.card_units_int]
    _ = (Fintype.card ((FABL.SignCube (n))) : ℝ)⁻¹ *
        ∑ S, monomial S a * monomial S x := by
      rw [Fintype.prod_add (fun i ↦ signValue (a i) * signValue (x i)) (fun _ ↦ 1)]
      congr 1
      apply Finset.sum_congr rfl
      intro S _
      simp [monomial, Finset.prod_mul_distrib]

-- Source: FABL.Chapter01.FunctionsAsMultilinearPolynomials:354
/-- The Fourier expansion obtained by inserting the monomial expansion of every point indicator. -/
theorem fourier_expansion_from_interpolation (f : (FABL.SignCube (n)) → ℝ)
    (x : (FABL.SignCube (n))) :
    f x = ∑ S, fourierCoeff f S * monomial S x := by
  classical
  let c : ℝ := (Fintype.card ((FABL.SignCube (n))) : ℝ)⁻¹
  calc
    f x = ∑ a, f a * indicatorPolynomial a x := sum_indicatorPolynomial f x
    _ = ∑ a, f a * (c * ∑ S, monomial S a * monomial S x) := by
      apply Finset.sum_congr rfl
      intro a _
      rw [indicatorPolynomial_fourier_sum]
    _ = ∑ a, ∑ S, (c * (f a * monomial S a)) * monomial S x := by
      apply Finset.sum_congr rfl
      intro a _
      rw [Finset.mul_sum]
      rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro S _
      ring
    _ = ∑ S, ∑ a, (c * (f a * monomial S a)) * monomial S x := by
      rw [Finset.sum_comm]
    _ = ∑ S, (c * ∑ a, f a * monomial S a) * monomial S x := by
      apply Finset.sum_congr rfl
      intro S _
      rw [← Finset.sum_mul, ← Finset.mul_sum]
    _ = ∑ S, fourierCoeff f S * monomial S x := by
      apply Finset.sum_congr rfl
      intro S _
      rw [fourierCoeff, Fintype.expect_eq_sum_div_card, div_eq_inv_mul]

-- Source: FABL.Chapter01.FunctionsAsMultilinearPolynomials:630
/-- The multilinear polynomial with coefficient function `a`, evaluated at `x`. -/
def multilinearPolynomial (a : Finset (Fin n) → ℝ) (x : (FABL.SignCube (n))) : ℝ :=
  ∑ S, a S * monomial S x

-- Source: FABL.Chapter01.FunctionsAsMultilinearPolynomials:634
/-- O'Donnell, Theorem 1.1: every real-valued function on `{-1,1}ⁿ` has a unique multilinear
expansion. -/
theorem fourier_expansion_unique (f : (FABL.SignCube (n)) → ℝ) :
    (∀ x, f x = multilinearPolynomial (fourierCoeff f) x) ∧
      ∀ a : Finset (Fin n) → ℝ,
        (∀ x, f x = multilinearPolynomial a x) → a = fourierCoeff f := by
  classical
  constructor
  · intro x
    simpa [multilinearPolynomial] using fourier_expansion_from_interpolation f x
  · intro a ha
    funext T
    have hcoeff : fourierCoeff f T = a T := by
      rw [fourierCoeff]
      calc
        (𝔼 x, f x * monomial T x) =
            𝔼 x, (∑ S, a S * monomial S x) * monomial T x := by
          apply Finset.expect_congr rfl
          intro x _
          rw [ha x, multilinearPolynomial]
        _ = 𝔼 x, ∑ S, (a S * monomial S x) * monomial T x := by
          congr 1
          funext x
          rw [Finset.sum_mul]
        _ = ∑ S, 𝔼 x, (a S * monomial S x) * monomial T x := by
          rw [Finset.expect_sum_comm]
        _ = ∑ S, a S * (if S = T then 1 else 0) := by
          apply Finset.sum_congr rfl
          intro S _
          rw [← expect_monomial_mul S T, Finset.mul_expect]
          apply Finset.expect_congr rfl
          intro x _
          ring
        _ = a T := by simp
    exact hcoeff.symm

-- Source: FABL.Chapter01.FunctionsAsMultilinearPolynomials:670
/-- The expansion identity from O'Donnell, Theorem 1.1. -/
theorem fourier_expansion (f : (FABL.SignCube (n)) → ℝ) (x : (FABL.SignCube (n))) :
    f x = ∑ S, fourierCoeff f S * monomial S x := by
  simpa [multilinearPolynomial] using (fourier_expansion_unique f).1 x

end FABL

end

/- Source fragment: FABL.Chapter01.ParityBasis. Original licenses and source proofs retained. -/

section

/-
Copyright (c) 2026 Asher Yan. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Asher Yan with Codex
-/

/-!
# The orthonormal basis of parity functions

Book items: Definition 1.3, Notation 1.4, Fact 1.6, Fact 1.7, Theorem 1.5.

Formalization of Section 1.3 of O'Donnell's *Analysis of Boolean Functions*.
-/

open Finset
open scoped BigOperators symmDiff

namespace FABL

variable {n : ℕ}

-- Source: FABL.Chapter01.ParityBasis:27
/-- The normalized inner product `⟨f,g⟩ = 𝔼[f g]` from O'Donnell, Definition 1.3. -/
noncomputable def uniformInner {Ω : Type*} [Fintype Ω] (f g : Ω → ℝ) : ℝ :=
  RCLike.wInner RCLike.cWeight f g

-- Source: FABL.Chapter01.ParityBasis:37
/-- The uniform distribution denoted by `x ∼ Ω`; see O'Donnell, Notation 1.4. -/
noncomputable def uniformPMF (Ω : Type*) [Fintype Ω] [Nonempty Ω] : PMF Ω :=
  PMF.uniformOfFintype Ω

-- Source: FABL.Chapter01.ParityBasis:41
/-- Integration against the uniform PMF is Mathlib's normalized finite expectation. -/
theorem integral_uniformPMF_eq_expect {Ω : Type*} [Fintype Ω] [Nonempty Ω]
    [MeasurableSpace Ω] [MeasurableSingletonClass Ω]
    (f : Ω → ℝ) :
    ∫ x, f x ∂(uniformPMF Ω).toMeasure = 𝔼 x, f x := by
  rw [PMF.integral_eq_sum, uniformPMF]
  simp_rw [PMF.uniformOfFintype_apply, ENNReal.toReal_inv, smul_eq_mul]
  rw [Fintype.expect_eq_sum_div_card]
  simp_rw [ENNReal.toReal_natCast]
  rw [← Finset.mul_sum, div_eq_inv_mul]

-- Source: FABL.Chapter01.ParityBasis:76
/-- The subset-indexed real Walsh basis on the sign cube. Its construction regards the
multiplicative sign cube as an additive group and reuses Mathlib's `AddChar` linear independence. -/
noncomputable def walshBasis (n : ℕ) :
    Module.Basis (Finset (Fin n)) ℝ ((FABL.SignCube (n)) → ℝ) := by
  classical
  exact basisOfLinearIndependentOfCardEqFinrank (b := fun S ↦ monomial S)
    (by
      let e : (Additive ((FABL.SignCube (n))) → ℝ) ≃ₗ[ℝ] ((FABL.SignCube (n)) → ℝ) :=
        { toFun := fun f x ↦ f (Additive.ofMul x)
          invFun := fun f x ↦ f (Additive.toMul x)
          left_inv := by intro f; ext x; rfl
          right_inv := by intro f; ext x; rfl
          map_add' := by intros; rfl
          map_smul' := by intros; rfl }
      exact
        (((AddChar.linearIndependent (Additive ((FABL.SignCube (n)))) ℝ).comp signMonomialChar
          signMonomialChar_injective).map' e.toLinearMap e.ker))
    (by
      simp [Module.finrank_fintype_fun_eq_card, Fintype.card_finset,
        Fintype.card_units_int])

-- Source: FABL.Chapter01.ParityBasis:97
/-- O'Donnell, Theorem 1.5: the parity functions form an orthonormal basis. -/
theorem parity_orthonormal_basis :
    (∀ S : Finset (Fin n), walshBasis n S = monomial S) ∧
      ∀ S T : Finset (Fin n),
        (FABL.uniformInner (monomial S) (monomial T)) = if S = T then 1 else 0 := by
  constructor
  · intro S
    unfold walshBasis
    exact congrFun (coe_basisOfLinearIndependentOfCardEqFinrank _ _) S
  · intro S T
    have hreindex : (FABL.uniformInner (monomial S) (monomial T)) =
        RCLike.wInner RCLike.cWeight (signMonomialChar S) (signMonomialChar T) := by
      rw [uniformInner, RCLike.wInner_cWeight_eq_expect,
        RCLike.wInner_cWeight_eq_expect]
      symm
      apply Fintype.expect_equiv Additive.toMul
      intro x
      rfl
    rw [hreindex]
    simpa [signMonomialChar_injective.eq_iff] using
      (AddChar.wInner_cWeight_eq_boole (signMonomialChar S) (signMonomialChar T))

end FABL

end

/- Source fragment: FABL.Chapter01.BasicFourierFormulas. Original licenses and source proofs retained. -/

section

/-
Copyright (c) 2026 Asher Yan. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Asher Yan with Codex
-/

/-!
# Basic Fourier formulas

Book items: Definition 1.3, Definition 1.10, Definition 1.11, Definition 1.17, Definition 1.18,
Definition 1.19, Fact 1.12, Fact 1.14, Proposition 1.8, Proposition 1.9, Proposition 1.13,
Proposition 1.15, Proposition 1.16, Parseval's Theorem, Plancherel's Theorem, Exercise 1.16.

Formalization of Section 1.4 of O'Donnell's *Analysis of Boolean Functions*.
-/

open Finset
open scoped BigOperators

namespace FABL

variable {n : ℕ}

-- Source: FABL.Chapter01.BasicFourierFormulas:29
/-- A sign-valued Boolean function on the sign cube. -/
abbrev BooleanFunction (n : ℕ) := (FABL.SignCube (n)) → Sign

-- Source: FABL.Chapter01.BasicFourierFormulas:32
/-- Regard a sign-valued function as real-valued. -/
def BooleanFunction.toReal (f : BooleanFunction n) : (FABL.SignCube (n)) → ℝ :=
  fun x ↦ signValue (f x)

-- Source: FABL.Chapter01.BasicFourierFormulas:36
/-- Uniform probability of a decidable event on a finite nonempty type. -/
noncomputable def uniformProbability {Ω : Type*} [Fintype Ω] [Nonempty Ω]
    (P : Ω → Prop) [DecidablePred P] : ℝ :=
  𝔼 x, if P x then (1 : ℝ) else 0

-- Source: FABL.Chapter01.BasicFourierFormulas:41
/-- O'Donnell, Definition 1.10: relative Hamming distance, obtained by normalizing Mathlib's
`hammingDist`. -/
noncomputable def relativeHammingDist {Ω β : Type*} [Fintype Ω] [Nonempty Ω] [DecidableEq β]
    (f g : Ω → β) : ℝ :=
  (hammingDist f g : ℝ) / Fintype.card Ω

-- Source: FABL.Chapter01.BasicFourierFormulas:47
/-- Relative Hamming distance is the uniform probability that two functions disagree. -/
theorem uniformProbability_ne_eq_relativeHammingDist {Ω β : Type*} [Fintype Ω] [Nonempty Ω]
    [DecidableEq β] (f g : Ω → β) :
    uniformProbability (fun x ↦ f x ≠ g x) = relativeHammingDist f g := by
  classical
  rw [uniformProbability, Fintype.expect_eq_sum_div_card, relativeHammingDist, hammingDist]
  congr 1
  simp only [Finset.sum_boole]

-- Source: FABL.Chapter01.BasicFourierFormulas:78
/-- Parseval's identity on `{-1,1}ⁿ`. -/
theorem parseval (f : (FABL.SignCube (n)) → ℝ) :
    (FABL.uniformInner (f) (f)) = ∑ S, fourierCoeff f S ^ 2 := by
  classical
  rw [uniformInner, RCLike.wInner_cWeight_eq_expect]
  simp only [RCLike.inner_apply, starRingEnd_apply, star_trivial]
  calc
    (𝔼 x, f x * f x) =
        𝔼 x, ((∑ S, fourierCoeff f S * monomial S x) * f x) := by
      apply Finset.expect_congr rfl
      intro x _
      rw [← fourier_expansion f x]
    _ = 𝔼 x, ∑ S, (fourierCoeff f S * monomial S x) * f x := by
      congr 1
      funext x
      rw [Finset.sum_mul]
    _ = ∑ S, 𝔼 x, (fourierCoeff f S * monomial S x) * f x := by
      rw [Finset.expect_sum_comm]
    _ = ∑ S, fourierCoeff f S ^ 2 := by
      apply Finset.sum_congr rfl
      intro S _
      simp_rw [mul_assoc]
      rw [← Finset.mul_expect]
      simp [fourierCoeff, pow_two, mul_comm]

-- Source: FABL.Chapter01.BasicFourierFormulas:103
/-- The Boolean-valued specialization following Parseval's identity. -/
theorem sum_sq_fourierCoeff_eq_one (f : BooleanFunction n) :
    ∑ S, fourierCoeff f.toReal S ^ 2 = 1 := by
  rw [← parseval, uniformInner, RCLike.wInner_cWeight_eq_expect]
  simp only [RCLike.inner_apply, BooleanFunction.toReal, starRingEnd_apply, star_trivial]
  calc
    (𝔼 x, signValue (f x) * signValue (f x)) = 𝔼 _x : (FABL.SignCube (n)), (1 : ℝ) := by
      apply Finset.expect_congr rfl
      intro x _
      rcases Int.units_eq_one_or (f x) with h | h <;> simp [signValue_one, signValue_neg_one, h]
    _ = 1 := Fintype.expect_const 1

-- Source: FABL.Chapter01.BasicFourierFormulas:163
/-- Plancherel's identity on `{-1,1}ⁿ`. -/
theorem plancherel (f g : (FABL.SignCube (n)) → ℝ) :
    (FABL.uniformInner (f) (g)) = ∑ S, fourierCoeff f S * fourierCoeff g S := by
  classical
  rw [uniformInner, RCLike.wInner_cWeight_eq_expect]
  simp only [RCLike.inner_apply, starRingEnd_apply, star_trivial]
  calc
    (𝔼 x, g x * f x) =
        𝔼 x, ((∑ S, fourierCoeff g S * monomial S x) * f x) := by
      apply Finset.expect_congr rfl
      intro x _
      rw [← fourier_expansion g x]
    _ = 𝔼 x, ∑ S, (fourierCoeff g S * monomial S x) * f x := by
      congr 1
      funext x
      rw [Finset.sum_mul]
    _ = ∑ S, 𝔼 x, (fourierCoeff g S * monomial S x) * f x := by
      rw [Finset.expect_sum_comm]
    _ = ∑ S, fourierCoeff f S * fourierCoeff g S := by
      apply Finset.sum_congr rfl
      intro S _
      simp_rw [mul_assoc]
      rw [← Finset.mul_expect]
      simp [fourierCoeff, mul_comm]

-- Source: FABL.Chapter01.BasicFourierFormulas:188
/-- O'Donnell, Proposition 1.9: correlation of sign-valued functions is one minus twice their
relative Hamming distance. -/
theorem uniformInner_eq_one_sub_two_mul_relativeHammingDist (f g : BooleanFunction n) :
    (FABL.uniformInner (f.toReal) (g.toReal)) = 1 - 2 * relativeHammingDist f g := by
  classical
  rw [uniformInner, RCLike.wInner_cWeight_eq_expect,
    ← uniformProbability_ne_eq_relativeHammingDist f g, uniformProbability]
  simp only [RCLike.inner_apply, BooleanFunction.toReal, starRingEnd_apply, star_trivial]
  calc
    (𝔼 x, signValue (g x) * signValue (f x)) =
        (𝔼 x, (1 - 2 * (if f x ≠ g x then (1 : ℝ) else 0))) := by
      apply Finset.expect_congr rfl
      intro x _
      rcases Int.units_eq_one_or (f x) with hf | hf <;>
        rcases Int.units_eq_one_or (g x) with hg | hg <;>
        simp [signValue_one, signValue_neg_one, hf, hg] <;> norm_num
    _ = 1 - 2 * (𝔼 x, if f x ≠ g x then (1 : ℝ) else 0) := by
      rw [Finset.expect_sub_distrib, ← Finset.mul_expect]
      simp

-- Source: FABL.Chapter01.BasicFourierFormulas:462
/-- O'Donnell, Definition 1.17: Fourier weight on `S`. -/
noncomputable def fourierWeight (f : (FABL.SignCube (n)) → ℝ) (S : Finset (Fin n)) : ℝ :=
  fourierCoeff f S ^ 2

-- Source: FABL.Chapter01.BasicFourierFormulas:533
/-- The Fourier weight above degree `k`. -/
noncomputable def fourierWeightAbove (k : ℕ) (f : (FABL.SignCube (n)) → ℝ) : ℝ :=
  ∑ S ∈ (Finset.univ.filter fun S : Finset (Fin n) ↦ k < S.card), fourierWeight f S

end FABL

end

/- Source fragment: FABL.Chapter02.SocialChoiceFunctions.Definitions. Original licenses and source proofs retained. -/

section

/-
Copyright (c) 2026 Asher Yan. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Asher Yan with Codex
-/

/-!
# Social choice function definitions

Book items: Exercise 1.30(a), Definition 2.1, Definition 2.2, Definition 2.3, Definition 2.4,
Definition 2.5, Definition 2.6, Definition 2.7, Exercise 2.3.

Basic definitions and examples from Section 2.1 of O'Donnell's *Analysis of Boolean Functions*.
-/

open Finset
open scoped BigOperators

namespace FABL

variable {n : ℕ}

-- Source: FABL.Chapter02.SocialChoiceFunctions.Definitions:28
/-- The book's sign convention: `sgn(t) = 1` for `t ≥ 0` and `-1` otherwise. -/
noncomputable def thresholdSign (t : ℝ) : Sign :=
  if 0 ≤ t then 1 else -1

-- Source: FABL.Chapter02.SocialChoiceFunctions.Definitions:38
/-- The real value of `thresholdSign t` is the usual two-valued sign convention. -/
theorem signValue_thresholdSign (t : ℝ) :
    signValue (thresholdSign t) = if 0 ≤ t then 1 else -1 := by
  by_cases ht : 0 ≤ t <;> simp [signValue_one, signValue_neg_one, thresholdSign, ht]

-- Source: FABL.Chapter02.SocialChoiceFunctions.Definitions:48
/-- The real encoding distinguishes the two signs. -/
theorem signValue_injective : Function.Injective signValue := by
  intro a b hab
  apply Units.ext
  change (((a : ℤ) : ℝ) = ((b : ℤ) : ℝ)) at hab
  exact_mod_cast hab

-- Source: FABL.Chapter02.SocialChoiceFunctions.Definitions:66
/-- `-1` is the least sign. -/
theorem neg_one_le_sign (s : Sign) : (-1 : Sign) ≤ s := by
  rcases Int.units_eq_one_or s with rfl | rfl
  · change (-1 : ℤ) ≤ 1
    omega
  · exact le_rfl

-- Source: FABL.Chapter02.SocialChoiceFunctions.Definitions:210
/-- O'Donnell, Definition 2.4: a function is a `k`-junta when it depends on a set of at most
`k` coordinates. The dependence predicate is Mathlib's `DependsOn`. -/
def IsKJunta {β : Type*} (f : (FABL.SignCube (n)) → β) (k : ℕ) : Prop :=
  ∃ S : Finset (Fin n), S.card ≤ k ∧ DependsOn f (S : Set (Fin n))

end FABL

end

/- Source fragment: FABL.Chapter02.InfluencesAndDerivatives.BooleanInfluence. Original licenses and source proofs retained. -/

section

/-
Copyright (c) 2026 Asher Yan. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Asher Yan with Codex
-/

/-!
# Boolean influence

Book items: Definition 2.12, Definition 2.13, Fact 2.14, Example 2.15.

Pivotal coordinates, cube edges, and Boolean influences from Section 2.2 of O'Donnell's
*Analysis of Boolean Functions*.
-/

open Finset
open scoped BigOperators

namespace FABL

variable {n : ℕ}

-- Source: FABL.Chapter02.InfluencesAndDerivatives.BooleanInfluence:28
/-- Set coordinate `i` of a sign-cube input to `b`, using Mathlib's `Function.update`. -/
def setCoordinate (x : (FABL.SignCube (n))) (i : Fin n) (b : Sign) : (FABL.SignCube (n)) :=
  Function.update x i b

-- Source: FABL.Chapter02.InfluencesAndDerivatives.BooleanInfluence:32
/-- Reading the coordinate just set returns its new value. -/
 theorem setCoordinate_apply_self (x : (FABL.SignCube (n))) (i : Fin n) (b : Sign) :
    setCoordinate x i b i = b := by
  simp [setCoordinate, Function.update_self]

-- Source: FABL.Chapter02.InfluencesAndDerivatives.BooleanInfluence:37
/-- Setting one coordinate leaves every other coordinate unchanged. -/
 theorem setCoordinate_apply_of_ne (x : (FABL.SignCube (n))) {i j : Fin n} (h : j ≠ i)
    (b : Sign) : setCoordinate x i b j = x j := by
  simp [setCoordinate, Function.update_of_ne h]

-- Source: FABL.Chapter02.InfluencesAndDerivatives.BooleanInfluence:42
/-- Setting a coordinate to its present value leaves the input unchanged. -/
 theorem setCoordinate_eq_self (x : (FABL.SignCube (n))) (i : Fin n) :
    setCoordinate x i (x i) = x := by
  exact Function.update_eq_self i x

-- Source: FABL.Chapter02.InfluencesAndDerivatives.BooleanInfluence:52
/-- O'Donnell, Definition 2.12: flip coordinate `i` of a sign-cube input. -/
def flipCoordinate (x : (FABL.SignCube (n))) (i : Fin n) : (FABL.SignCube (n)) :=
  setCoordinate x i (-x i)

-- Source: FABL.Chapter02.InfluencesAndDerivatives.BooleanInfluence:62
/-- O'Donnell, Definition 2.12: coordinate `i` is pivotal for `f` at `x`. -/
def IsPivotal {β : Type*} (f : (FABL.SignCube (n)) → β) (i : Fin n) (x : (FABL.SignCube (n))) : Prop :=
  f x ≠ f (flipCoordinate x i)

-- Source: FABL.Chapter02.InfluencesAndDerivatives.BooleanInfluence:66
/-- Pivotality is equivalently disagreement between the two restrictions of one coordinate. -/
theorem isPivotal_iff_setCoordinate_ne {β : Type*} (f : (FABL.SignCube (n)) → β)
    (i : Fin n) (x : (FABL.SignCube (n))) :
    IsPivotal f i x ↔
      f (setCoordinate x i 1) ≠ f (setCoordinate x i (-1)) := by
  rcases Int.units_eq_one_or (x i) with hi | hi
  · have hplus : setCoordinate x i 1 = x := by
      simpa [hi] using setCoordinate_eq_self x i
    have hflip : flipCoordinate x i = setCoordinate x i (-1) := by
      simp [flipCoordinate, hi]
    rw [IsPivotal, hplus, hflip]
  · have hminus : setCoordinate x i (-1) = x := by
      simpa [hi] using setCoordinate_eq_self x i
    have hflip : flipCoordinate x i = setCoordinate x i 1 := by
      simp [flipCoordinate, hi]
    rw [IsPivotal, hminus, hflip, ne_comm]

-- Source: FABL.Chapter02.InfluencesAndDerivatives.BooleanInfluence:83
/-- O'Donnell, Definition 2.13: pivotal probability for a Boolean-valued function. -/
noncomputable def booleanInfluence (f : BooleanFunction n) (i : Fin n) : ℝ :=
  by
    classical
    exact uniformProbability (IsPivotal f i)

end FABL

end

/- Source fragment: FABL.Chapter02.InfluencesAndDerivatives.DiscreteDerivatives. Original licenses and source proofs retained. -/

section

/-
Copyright (c) 2026 Asher Yan. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Asher Yan with Codex
-/

/-!
# Discrete derivatives

Book items: Definition 2.16, Definition 2.17, Definition 2.18, Definition 2.23, Definition 2.25,
Equation (2.1), Proposition 2.19, Proposition 2.21, Proposition 2.22, Proposition 2.24, Proposition
2.26, Theorem 2.20.

Discrete derivatives, coordinate expectations, Laplacians, and their Fourier formulas from
Section 2.2 of O'Donnell's *Analysis of Boolean Functions*.
-/

open Finset
open scoped BigOperators

namespace FABL

variable {n : ℕ}

-- Source: FABL.Chapter02.InfluencesAndDerivatives.DiscreteDerivatives:30
/-- O'Donnell, Definition 2.16: the `i`th discrete derivative, as an `ℝ`-linear map. -/
noncomputable def discreteDerivative (i : Fin n) :
    ((FABL.SignCube (n)) → ℝ) →ₗ[ℝ] ((FABL.SignCube (n)) → ℝ) where
  toFun f x :=
    (f (setCoordinate x i 1) - f (setCoordinate x i (-1))) / 2
  map_add' f g := by
    funext x
    simp only [Pi.add_apply]
    ring
  map_smul' c f := by
    funext x
    simp only [Pi.smul_apply, smul_eq_mul, RingHom.id_apply]
    ring

-- Source: FABL.Chapter02.InfluencesAndDerivatives.DiscreteDerivatives:44
/-- The pointwise formula defining O'Donnell's discrete derivative. -/
 theorem discreteDerivative_apply (i : Fin n) (f : (FABL.SignCube (n)) → ℝ)
    (x : (FABL.SignCube (n))) :
    discreteDerivative i f x =
      (f (setCoordinate x i 1) - f (setCoordinate x i (-1))) / 2 :=
  rfl

-- Source: FABL.Chapter02.InfluencesAndDerivatives.DiscreteDerivatives:88
/-- The discrete derivative of a parity monomial removes coordinate `i` when it occurs and is
zero otherwise. -/
theorem discreteDerivative_monomial (i : Fin n) (S : Finset (Fin n))
    (x : (FABL.SignCube (n))) :
    discreteDerivative i (monomial S) x =
      if i ∈ S then monomial (S.erase i) x else 0 := by
  classical
  by_cases hi : i ∈ S
  · rw [if_pos hi]
    have hprod (b : Sign) :
        ∏ j ∈ S.erase i, signValue (setCoordinate x i b j) =
          ∏ j ∈ S.erase i, signValue (x j) := by
      apply Finset.prod_congr rfl
      intro j hj
      rw [setCoordinate_apply_of_ne x (Finset.ne_of_mem_erase hj)]
    simp only [discreteDerivative_apply]
    rw [monomial, monomial]
    rw [← Finset.mul_prod_erase _ _ hi]
    rw [← Finset.mul_prod_erase _ _ hi]
    rw [hprod, hprod]
    simp [monomial, setCoordinate_apply_self, signValue_one, signValue_neg_one]
  · rw [if_neg hi]
    have hprod (b : Sign) :
        ∏ j ∈ S, signValue (setCoordinate x i b j) = ∏ j ∈ S, signValue (x j) := by
      apply Finset.prod_congr rfl
      intro j hj
      have hne : j ≠ i := by
        intro h
        subst j
        exact hi hj
      rw [setCoordinate_apply_of_ne x hne]
    simp [discreteDerivative_apply, monomial, hprod]

-- Source: FABL.Chapter02.InfluencesAndDerivatives.DiscreteDerivatives:121
/-- O'Donnell, Proposition 2.19, Equation (2.2): the Fourier expansion of a discrete
derivative. -/
theorem discreteDerivative_eq_fourier_sum (f : (FABL.SignCube (n)) → ℝ) (i : Fin n)
    (x : (FABL.SignCube (n))) :
    discreteDerivative i f x =
      ∑ S with i ∈ S, fourierCoeff f S * monomial (S.erase i) x := by
  classical
  rw [discreteDerivative_apply, fourier_expansion f, fourier_expansion f]
  calc
    ((∑ S, fourierCoeff f S * monomial S (setCoordinate x i 1)) -
          ∑ S, fourierCoeff f S * monomial S (setCoordinate x i (-1))) / 2 =
        ∑ S, fourierCoeff f S * discreteDerivative i (monomial S) x := by
      rw [← Finset.sum_sub_distrib, Finset.sum_div]
      apply Finset.sum_congr rfl
      intro S _
      rw [discreteDerivative_apply]
      ring
    _ = ∑ S with i ∈ S, fourierCoeff f S * monomial (S.erase i) x := by
      rw [Finset.sum_filter]
      apply Finset.sum_congr rfl
      intro S _
      rw [discreteDerivative_monomial]
      split_ifs <;> ring

-- Source: FABL.Chapter02.InfluencesAndDerivatives.DiscreteDerivatives:145
/-- The real-valued indicator that coordinate `i` is pivotal for `f` at `x`. -/
noncomputable def pivotalIndicator (f : BooleanFunction n) (i : Fin n)
    (x : (FABL.SignCube (n))) : ℝ := by
  classical
  exact if IsPivotal f i x then 1 else 0

-- Source: FABL.Chapter02.InfluencesAndDerivatives.DiscreteDerivatives:151
/-- O'Donnell, Equation (2.1): the squared derivative of a Boolean function is the pivotality
indicator. -/
theorem sq_discreteDerivative_toReal_eq_pivotalIndicator (f : BooleanFunction n)
    (i : Fin n) (x : (FABL.SignCube (n))) :
    discreteDerivative i f.toReal x ^ 2 = pivotalIndicator f i x := by
  classical
  rw [pivotalIndicator]
  rw [isPivotal_iff_setCoordinate_ne]
  rcases Int.units_eq_one_or (f (setCoordinate x i 1)) with hp | hp <;>
    rcases Int.units_eq_one_or (f (setCoordinate x i (-1))) with hm | hm <;>
    norm_num [discreteDerivative_apply, BooleanFunction.toReal, signValue_one, signValue_neg_one, hp, hm]

-- Source: FABL.Chapter02.InfluencesAndDerivatives.DiscreteDerivatives:163
/-- O'Donnell, Definition 2.17: the real-valued influence `Inf_i[f] = 𝔼[(D_i f)²]`. -/
noncomputable def influence (f : (FABL.SignCube (n)) → ℝ) (i : Fin n) : ℝ :=
  𝔼 x, discreteDerivative i f x ^ 2

-- Source: FABL.Chapter02.InfluencesAndDerivatives.DiscreteDerivatives:167
/-- Every real-valued influence is nonnegative. -/
theorem influence_nonneg (f : (FABL.SignCube (n)) → ℝ) (i : Fin n) :
    0 ≤ influence f i := by
  rw [influence, Fintype.expect_eq_sum_div_card]
  positivity

-- Source: FABL.Chapter02.InfluencesAndDerivatives.DiscreteDerivatives:187
/-- O'Donnell, Definitions 2.13 and 2.17 agree on Boolean-valued functions. -/
theorem booleanInfluence_eq_influence_toReal (f : BooleanFunction n) (i : Fin n) :
    booleanInfluence f i = influence f.toReal i := by
  classical
  rw [booleanInfluence, uniformProbability, influence]
  apply Finset.expect_congr rfl
  intro x _
  simpa [pivotalIndicator] using
    (sq_discreteDerivative_toReal_eq_pivotalIndicator f i x).symm

-- Source: FABL.Chapter02.InfluencesAndDerivatives.DiscreteDerivatives:209
/-- O'Donnell, Definition 2.23: average over coordinate `i`, as an `ℝ`-linear map. -/
noncomputable def coordinateExpectation (i : Fin n) :
    ((FABL.SignCube (n)) → ℝ) →ₗ[ℝ] ((FABL.SignCube (n)) → ℝ) where
  toFun f x :=
    (f (setCoordinate x i 1) + f (setCoordinate x i (-1))) / 2
  map_add' f g := by
    funext x
    simp only [Pi.add_apply]
    ring
  map_smul' c f := by
    funext x
    simp only [Pi.smul_apply, smul_eq_mul, RingHom.id_apply]
    ring

-- Source: FABL.Chapter02.InfluencesAndDerivatives.DiscreteDerivatives:223
/-- O'Donnell, Proposition 2.24: the coordinate expectation is the average of the two
coordinate restrictions. -/
 theorem coordinateExpectation_apply (i : Fin n) (f : (FABL.SignCube (n)) → ℝ)
    (x : (FABL.SignCube (n))) :
    coordinateExpectation i f x =
      (f (setCoordinate x i 1) + f (setCoordinate x i (-1))) / 2 :=
  rfl

-- Source: FABL.Chapter02.InfluencesAndDerivatives.DiscreteDerivatives:231
/-- Coordinate expectation kills a parity monomial containing `i` and fixes every other parity
monomial. -/
theorem coordinateExpectation_monomial (i : Fin n) (S : Finset (Fin n))
    (x : (FABL.SignCube (n))) :
    coordinateExpectation i (monomial S) x =
      if i ∈ S then 0 else monomial S x := by
  classical
  by_cases hi : i ∈ S
  · rw [if_pos hi]
    have hprod (b : Sign) :
        ∏ j ∈ S.erase i, signValue (setCoordinate x i b j) =
          ∏ j ∈ S.erase i, signValue (x j) := by
      apply Finset.prod_congr rfl
      intro j hj
      rw [setCoordinate_apply_of_ne x (Finset.ne_of_mem_erase hj)]
    simp only [coordinateExpectation_apply]
    rw [monomial, ← Finset.mul_prod_erase _ _ hi]
    rw [monomial, ← Finset.mul_prod_erase _ _ hi]
    rw [hprod, hprod]
    simp [setCoordinate_apply_self, signValue_one, signValue_neg_one]
  · rw [if_neg hi]
    have hprod (b : Sign) :
        ∏ j ∈ S, signValue (setCoordinate x i b j) = ∏ j ∈ S, signValue (x j) := by
      apply Finset.prod_congr rfl
      intro j hj
      have hne : j ≠ i := by
        intro h
        subst j
        exact hi hj
      rw [setCoordinate_apply_of_ne x hne]
    simp [coordinateExpectation_apply, monomial, hprod]

-- Source: FABL.Chapter02.InfluencesAndDerivatives.DiscreteDerivatives:263
/-- O'Donnell, Proposition 2.24: the Fourier expansion of the coordinate expectation. -/
theorem coordinateExpectation_eq_fourier_sum (f : (FABL.SignCube (n)) → ℝ) (i : Fin n)
    (x : (FABL.SignCube (n))) :
    coordinateExpectation i f x =
      ∑ S with i ∉ S, fourierCoeff f S * monomial S x := by
  classical
  rw [coordinateExpectation_apply, fourier_expansion f, fourier_expansion f]
  calc
    ((∑ S, fourierCoeff f S * monomial S (setCoordinate x i 1)) +
          ∑ S, fourierCoeff f S * monomial S (setCoordinate x i (-1))) / 2 =
        ∑ S, fourierCoeff f S * coordinateExpectation i (monomial S) x := by
      rw [← Finset.sum_add_distrib, Finset.sum_div]
      apply Finset.sum_congr rfl
      intro S _
      rw [coordinateExpectation_apply]
      ring
    _ = ∑ S with i ∉ S, fourierCoeff f S * monomial S x := by
      rw [Finset.sum_filter]
      apply Finset.sum_congr rfl
      intro S _
      rw [coordinateExpectation_monomial]
      split_ifs <;> ring

-- Source: FABL.Chapter02.InfluencesAndDerivatives.DiscreteDerivatives:306
/-- O'Donnell, Proposition 2.24: `f = x_i D_i f + E_i f` pointwise. -/
theorem eq_signValue_mul_discreteDerivative_add_coordinateExpectation
    (f : (FABL.SignCube (n)) → ℝ) (i : Fin n) (x : (FABL.SignCube (n))) :
    f x = signValue (x i) * discreteDerivative i f x + coordinateExpectation i f x := by
  rcases Int.units_eq_one_or (x i) with hi | hi
  · have hx : setCoordinate x i 1 = x := by
      simpa [hi] using setCoordinate_eq_self x i
    rw [hi, signValue_one, discreteDerivative_apply, coordinateExpectation_apply, hx]
    ring
  · have hx : setCoordinate x i (-1) = x := by
      simpa [hi] using setCoordinate_eq_self x i
    rw [hi, signValue_neg_one, discreteDerivative_apply, coordinateExpectation_apply, hx]
    ring

-- Source: FABL.Chapter02.InfluencesAndDerivatives.DiscreteDerivatives:320
/-- O'Donnell, Definition 2.25: the coordinate Laplacian `L_i = I - E_i`. -/
noncomputable def coordinateLaplacian (i : Fin n) :
    ((FABL.SignCube (n)) → ℝ) →ₗ[ℝ] ((FABL.SignCube (n)) → ℝ) :=
  LinearMap.id - coordinateExpectation i

-- Source: FABL.Chapter02.InfluencesAndDerivatives.DiscreteDerivatives:325
/-- The pointwise formula defining the coordinate Laplacian. -/
 theorem coordinateLaplacian_apply (i : Fin n) (f : (FABL.SignCube (n)) → ℝ)
    (x : (FABL.SignCube (n))) :
    coordinateLaplacian i f x = f x - coordinateExpectation i f x := by
  rfl

-- Source: FABL.Chapter02.InfluencesAndDerivatives.DiscreteDerivatives:331
/-- O'Donnell, Proposition 2.26: the coordinate Laplacian is `x_i D_i f`. -/
theorem coordinateLaplacian_eq_signValue_mul_discreteDerivative
    (f : (FABL.SignCube (n)) → ℝ) (i : Fin n) (x : (FABL.SignCube (n))) :
    coordinateLaplacian i f x = signValue (x i) * discreteDerivative i f x := by
  rw [coordinateLaplacian_apply]
  linarith [eq_signValue_mul_discreteDerivative_add_coordinateExpectation f i x]

-- Source: FABL.Chapter02.InfluencesAndDerivatives.DiscreteDerivatives:357
/-- O'Donnell, Proposition 2.26: the coordinate Laplacian retains exactly the Fourier terms
containing coordinate `i`. -/
theorem coordinateLaplacian_eq_fourier_sum (f : (FABL.SignCube (n)) → ℝ) (i : Fin n)
    (x : (FABL.SignCube (n))) :
    coordinateLaplacian i f x =
      ∑ S with i ∈ S, fourierCoeff f S * monomial S x := by
  classical
  rw [coordinateLaplacian_apply, fourier_expansion f,
    coordinateExpectation_eq_fourier_sum]
  rw [Finset.sum_filter, Finset.sum_filter, ← Finset.sum_sub_distrib]
  apply Finset.sum_congr rfl
  intro S _
  by_cases hi : i ∈ S <;> simp [hi]

-- Source: FABL.Chapter02.InfluencesAndDerivatives.DiscreteDerivatives:371
/-- The coordinate Laplacian retains a Fourier coefficient exactly when its index contains the
chosen coordinate. -/
theorem fourierCoeff_coordinateLaplacian (f : (FABL.SignCube (n)) → ℝ) (i : Fin n)
    (S : Finset (Fin n)) :
    fourierCoeff (coordinateLaplacian i f) S =
      if i ∈ S then fourierCoeff f S else 0 := by
  classical
  have hcoeff := (fourier_expansion_unique (coordinateLaplacian i f)).2
    (fun T ↦ if i ∈ T then fourierCoeff f T else 0) (by
      intro x
      rw [multilinearPolynomial, coordinateLaplacian_eq_fourier_sum,
        Finset.sum_filter]
      apply Finset.sum_congr rfl
      intro T _
      split_ifs <;> ring)
  exact (congrFun hcoeff S).symm

-- Source: FABL.Chapter02.InfluencesAndDerivatives.DiscreteDerivatives:388
/-- O'Donnell, Proposition 2.26: the Laplacian's normalized squared norm is the coordinate
influence. -/
theorem uniformInner_coordinateLaplacian_self_eq_influence
    (f : (FABL.SignCube (n)) → ℝ) (i : Fin n) :
    (FABL.uniformInner (coordinateLaplacian i f) (coordinateLaplacian i f)) = influence f i := by
  rw [uniformInner, RCLike.wInner_cWeight_eq_expect, influence]
  apply Finset.expect_congr rfl
  intro x _
  simp only [RCLike.inner_apply, starRingEnd_apply, star_trivial]
  rw [coordinateLaplacian_eq_signValue_mul_discreteDerivative]
  rcases Int.units_eq_one_or (x i) with hi | hi
  · simp [hi, signValue_one, signValue_neg_one, pow_two]
  · simp [hi, signValue_one, signValue_neg_one, pow_two]

-- Source: FABL.Chapter02.InfluencesAndDerivatives.DiscreteDerivatives:402
/-- O'Donnell, Theorem 2.20: influence is the Fourier weight on subsets containing coordinate
`i`. -/
theorem influence_eq_sum_sq_fourierCoeff (f : (FABL.SignCube (n)) → ℝ) (i : Fin n) :
    influence f i = ∑ S with i ∈ S, fourierCoeff f S ^ 2 := by
  classical
  calc
    influence f i = (FABL.uniformInner (coordinateLaplacian i f) (coordinateLaplacian i f)) :=
      (uniformInner_coordinateLaplacian_self_eq_influence f i).symm
    _ = ∑ S, fourierCoeff (coordinateLaplacian i f) S ^ 2 := parseval _
    _ = ∑ S with i ∈ S, fourierCoeff f S ^ 2 := by
      rw [Finset.sum_filter]
      apply Finset.sum_congr rfl
      intro S _
      rw [fourierCoeff_coordinateLaplacian]
      split_ifs <;> ring

-- Source: FABL.Chapter02.InfluencesAndDerivatives.DiscreteDerivatives:442
/-- For a monotone Boolean function, a discrete derivative is its own square: it is the
`0`-`1` pivotality indicator. -/
theorem sq_discreteDerivative_toReal_eq_self_of_monotone
    (f : BooleanFunction n) (hf : Monotone f) (i : Fin n) (x : (FABL.SignCube (n))) :
    discreteDerivative i f.toReal x ^ 2 = discreteDerivative i f.toReal x := by
  have hle : f (setCoordinate x i (-1)) ≤ f (setCoordinate x i 1) := by
    apply hf
    intro j
    by_cases hj : j = i
    · subst j
      simp only [setCoordinate_apply_self]
      exact neg_one_le_sign 1
    · simp [setCoordinate_apply_of_ne x hj]
  rcases Int.units_eq_one_or (f (setCoordinate x i 1)) with hp | hp <;>
    rcases Int.units_eq_one_or (f (setCoordinate x i (-1))) with hm | hm
  · norm_num [discreteDerivative_apply, BooleanFunction.toReal, signValue_one, signValue_neg_one, hp, hm]
  · norm_num [discreteDerivative_apply, BooleanFunction.toReal, signValue_one, signValue_neg_one, hp, hm]
  · rw [hp, hm] at hle
    exact False.elim ((by decide : ¬ ((1 : Sign) ≤ -1)) hle)
  · norm_num [discreteDerivative_apply, BooleanFunction.toReal, signValue_one, signValue_neg_one, hp, hm]

end FABL

end

/- Source fragment: FABL.Chapter02.TotalInfluence.Basic. Original licenses and source proofs retained. -/

section

/-
Copyright (c) 2026 Asher Yan. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Asher Yan with Codex
-/

/-!
# Total influence

Book items: Definition 2.27, Fact 2.29, Example 2.30, Equation (2.4), Proposition 2.28.

Basic total-influence definitions and examples from Section 2.3 of O'Donnell's
*Analysis of Boolean Functions*.
-/

open Finset
open Filter
open scoped Asymptotics BigOperators Real

namespace FABL

variable {n : ℕ}

-- Source: FABL.Chapter02.TotalInfluence.Basic:29
/-- O'Donnell, Definition 2.27: the total influence is the sum of the coordinate influences. -/
noncomputable def totalInfluence (f : (FABL.SignCube (n)) → ℝ) : ℝ :=
  ∑ i, influence f i

-- Source: FABL.Chapter02.TotalInfluence.Basic:33
/-- Total influence is nonnegative. -/
theorem totalInfluence_nonneg (f : (FABL.SignCube (n)) → ℝ) :
    0 ≤ totalInfluence f := by
  exact Finset.sum_nonneg fun i _ ↦ influence_nonneg f i

end FABL

end

/- Source fragment: FABL.Chapter02.TotalInfluence.MajorityOptimality. Original licenses and source proofs retained. -/

section

/-
Copyright (c) 2026 Asher Yan. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Asher Yan with Codex
-/

/-!
# Majority maximizes total influence

Book items: Equation (2.3), Proposition 2.31, Proposition 2.32, Theorem 2.33.

Restriction identities and the majority extremal argument from Section 2.3 of O'Donnell's
*Analysis of Boolean Functions*.
-/

open Finset
open Filter
open scoped Asymptotics BigOperators Real

namespace FABL

variable {n : ℕ}

-- Source: FABL.Chapter02.TotalInfluence.MajorityOptimality:33
/-- Uniform expectation over the two signs is their arithmetic mean. -/
theorem expect_sign (g : Sign → ℝ) :
    (𝔼 b : Sign, g b) = (g 1 + g (-1)) / 2 := by
  rw [Fintype.expect_eq_sum_div_card]
  have huniv : (Finset.univ : Finset Sign) = {1, -1} := by
    ext b
    rcases Int.units_eq_one_or b with hb | hb <;> simp [hb]
  rw [huniv]
  norm_num

-- Source: FABL.Chapter02.TotalInfluence.MajorityOptimality:43
/-- Mathlib's `Fin.consEquiv` gives the uniform-expectation slicing identity for the cube. -/
theorem expect_fin_cons (h : (FABL.SignCube (n + 1)) → ℝ) :
    (𝔼 x, h x) =
      ((𝔼 x : (FABL.SignCube (n)), h (Fin.cons 1 x)) +
        (𝔼 x : (FABL.SignCube (n)), h (Fin.cons (-1) x))) / 2 := by
  calc
    (𝔼 x, h x) = 𝔼 p : Sign × (FABL.SignCube (n)), h (Fin.cons p.1 p.2) := by
      apply Fintype.expect_equiv (Fin.consEquiv (fun _ : Fin (n + 1) ↦ Sign)).symm
      intro x
      simp
    _ = 𝔼 b : Sign, 𝔼 x : (FABL.SignCube (n)), h (Fin.cons b x) := by
      exact Finset.expect_product Finset.univ Finset.univ _
    _ = ((𝔼 x : (FABL.SignCube (n)), h (Fin.cons 1 x)) +
        (𝔼 x : (FABL.SignCube (n)), h (Fin.cons (-1) x))) / 2 := expect_sign _

end FABL

end

/- Source fragment: FABL.Chapter02.TotalInfluence.LaplacianAndPoincare. Original licenses and source proofs retained. -/

section

/-
Copyright (c) 2026 Asher Yan. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Asher Yan with Codex
-/

/-!
# Laplacian and Poincare inequality

Book items: Definition 2.34, Definition 2.36, Example 2.30, Proposition 2.35, Proposition 2.37,
Poincare inequality, Theorem 2.38, Exercise 2.17.

The discrete gradient, Laplacian, spectral total-influence formulas, and Poincare equality cases
from Section 2.3 of O'Donnell's *Analysis of Boolean Functions*.
-/

open Finset
open Filter
open scoped Asymptotics BigOperators Real

namespace FABL

variable {n : ℕ}

-- Source: FABL.Chapter02.TotalInfluence.LaplacianAndPoincare:165
/-- O'Donnell, Theorem 2.38, first Fourier formula: total influence is Fourier weight weighted
by subset cardinality. -/
theorem totalInfluence_eq_sum_card_mul_sq_fourierCoeff
    (f : (FABL.SignCube (n)) → ℝ) :
    totalInfluence f = ∑ S, (S.card : ℝ) * fourierCoeff f S ^ 2 := by
  classical
  rw [totalInfluence]
  simp_rw [influence_eq_sum_sq_fourierCoeff]
  calc
    (∑ i, ∑ S with i ∈ S, fourierCoeff f S ^ 2) =
        ∑ S, ∑ i with i ∈ S, fourierCoeff f S ^ 2 := by
      simp_rw [Finset.sum_filter]
      rw [Finset.sum_comm]
    _ = ∑ S, (S.card : ℝ) * fourierCoeff f S ^ 2 := by
      apply Finset.sum_congr rfl
      intro S _
      simp

end FABL

end

/- Source fragment: FABL.Chapter02.FKN. Original licenses and source proofs retained. -/

section

/-
Copyright (c) 2026 Asher Yan. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Asher Yan with Codex
-/

/-!
# The Friedgut--Kalai--Naor theorem

Book items: FKN Theorem.

The degree-two moment argument from Section 9.1 of O'Donnell's
*Analysis of Boolean Functions*, used in Section 2.5.
-/

open Finset
open scoped Asymptotics BigOperators

namespace FABL

variable {n : ℕ}

-- Source: FABL.Chapter02.FKN:84
/-- Slicing a function into its odd and even parts gives its second-moment identity. -/
theorem expect_sq_eq_expect_odd_even
    (d e : (FABL.SignCube (n)) → ℝ)
    (f : (FABL.SignCube (n + 1)) → ℝ)
    (hf : ∀ b x, f (Fin.cons b x) = signValue b * d x + e x) :
    (𝔼 x, f x ^ 2) = (𝔼 x, d x ^ 2) + 𝔼 x, e x ^ 2 := by
  rw [expect_fin_cons]
  have hp (x : (FABL.SignCube (n))) : f (Fin.cons 1 x) = d x + e x := by
    simpa [signValue_one, signValue_neg_one] using hf 1 x
  have hm (x : (FABL.SignCube (n))) : f (Fin.cons (-1) x) = -d x + e x := by
    simpa [signValue_one, signValue_neg_one] using hf (-1) x
  simp_rw [hp, hm]
  rw [show (fun x : (FABL.SignCube (n)) ↦ (d x + e x) ^ 2) =
      fun x ↦ d x ^ 2 + 2 * (d x * e x) + e x ^ 2 by
    funext x; ring]
  rw [show (fun x : (FABL.SignCube (n)) ↦ (-d x + e x) ^ 2) =
      fun x ↦ d x ^ 2 - 2 * (d x * e x) + e x ^ 2 by
    funext x; ring]
  simp_rw [Finset.expect_add_distrib, Finset.expect_sub_distrib, ← Finset.mul_expect]
  ring

-- Source: FABL.Chapter02.FKN:105
/-- Slicing a function into its odd and even parts gives its fourth-moment identity. -/
theorem expect_fourth_eq_expect_odd_even
    (d e : (FABL.SignCube (n)) → ℝ)
    (f : (FABL.SignCube (n + 1)) → ℝ)
    (hf : ∀ b x, f (Fin.cons b x) = signValue b * d x + e x) :
    (𝔼 x, f x ^ 4) =
      (𝔼 x, d x ^ 4) + 6 * (𝔼 x, d x ^ 2 * e x ^ 2) + 𝔼 x, e x ^ 4 := by
  rw [expect_fin_cons]
  have hp (x : (FABL.SignCube (n))) : f (Fin.cons 1 x) = d x + e x := by
    simpa [signValue_one, signValue_neg_one] using hf 1 x
  have hm (x : (FABL.SignCube (n))) : f (Fin.cons (-1) x) = -d x + e x := by
    simpa [signValue_one, signValue_neg_one] using hf (-1) x
  simp_rw [hp, hm]
  calc
    ((𝔼 x, (d x + e x) ^ 4) + 𝔼 x, (-d x + e x) ^ 4) / 2 =
        𝔼 x, ((d x + e x) ^ 4 + (-d x + e x) ^ 4) / 2 := by
      rw [← Finset.expect_add_distrib, Finset.expect_div]
    _ = (𝔼 x, (d x ^ 4 + 6 * (d x ^ 2 * e x ^ 2) + e x ^ 4)) := by
      apply Finset.expect_congr rfl
      intro x _
      ring
    _ = (𝔼 x, d x ^ 4) + 6 * (𝔼 x, d x ^ 2 * e x ^ 2) + 𝔼 x, e x ^ 4 := by
      simp_rw [Finset.expect_add_distrib, ← Finset.mul_expect]

-- Source: FABL.Chapter02.FKN:129
/-- Cauchy--Schwarz for the mixed fourth moment. -/
theorem expect_sq_mul_sq_sq_le (d e : (FABL.SignCube (n)) → ℝ) :
    (𝔼 x, d x ^ 2 * e x ^ 2) ^ 2 ≤
      (𝔼 x, d x ^ 4) * 𝔼 x, e x ^ 4 := by
  have h := Finset.expect_mul_sq_le_sq_mul_sq
    (Finset.univ : Finset ((FABL.SignCube (n)))) (fun x ↦ d x ^ 2) (fun x ↦ e x ^ 2)
  convert h using 1
  all_goals first | rfl | ring_nf

end FABL

end

/- Source fragment: FABL.Chapter02.NoiseStability.NoiseKernels. Original licenses and source proofs retained. -/

section

/-
Copyright (c) 2026 Asher Yan. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Asher Yan with Codex
-/

/-!
# Noise kernels

Book items: Definition 2.40, Definition 2.41.

Finite product noise kernels, correlated pairs, and finite-PMF expectation formulas from
Section 2.4 of O'Donnell's *Analysis of Boolean Functions*.
-/

open Complex Filter Finset MeasureTheory ProbabilityTheory Set WithLp
open scoped Asymptotics BigOperators ENNReal RealInnerProductSpace Topology

namespace FABL

variable {n : ℕ}

-- Source: FABL.Chapter02.NoiseStability.NoiseKernels:28
/-- O'Donnell, Definition 2.40: the independent product of a finite family of probability mass
functions. -/
noncomputable def independentProductPMF {ι : Type*} [Fintype ι]
    {α : ι → Type*} [∀ i, Fintype (α i)] (p : ∀ i, PMF (α i)) :
    PMF (∀ i, α i) := by
  classical
  refine PMF.ofFintype (fun x ↦ ∏ i, p i (x i)) ?_
  rw [← Fintype.prod_sum]
  apply Finset.prod_eq_one
  intro i _
  simpa only [tsum_fintype] using (p i).tsum_coe

-- Source: FABL.Chapter02.NoiseStability.NoiseKernels:40
/-- Evaluation of the independent product PMF is the product of its coordinate masses. -/
 theorem independentProductPMF_apply {ι : Type*} [Fintype ι]
    {α : ι → Type*} [∀ i, Fintype (α i)] (p : ∀ i, PMF (α i))
    (x : ∀ i, α i) :
    independentProductPMF p x = ∏ i, p i (x i) := by
  rfl

-- Source: FABL.Chapter02.NoiseStability.NoiseKernels:47
/-- O'Donnell, Definition 2.40: the probability of retaining a coordinate in the equivalent
second formulation. -/
noncomputable def correlationKeepProbability
    (ρ : ℝ) (hρ : ρ ∈ Set.Icc (-1 : ℝ) 1) : NNReal :=
  ⟨(1 + ρ) / 2, by linarith [hρ.1]⟩

-- Source: FABL.Chapter02.NoiseStability.NoiseKernels:53
/-- O'Donnell, Definition 2.40: the retention probability associated to a correlation parameter
is at most one. -/
theorem correlationKeepProbability_le_one
    (ρ : ℝ) (hρ : ρ ∈ Set.Icc (-1 : ℝ) 1) :
    correlationKeepProbability ρ hρ ≤ 1 := by
  exact_mod_cast (show (1 + ρ) / 2 ≤ (1 : ℝ) by linarith [hρ.2])

-- Source: FABL.Chapter02.NoiseStability.NoiseKernels:60
/-- O'Donnell, Definition 2.40: the one-coordinate noise distribution which retains `x`
with probability `(1 + ρ) / 2` and reverses it with probability `(1 - ρ) / 2`. -/
noncomputable def coordinateNoisePMF (ρ : ℝ) (hρ : ρ ∈ Set.Icc (-1 : ℝ) 1)
    (x : Sign) : PMF Sign :=
  let p := correlationKeepProbability ρ hρ
  let hp : p ≤ 1 := correlationKeepProbability_le_one ρ hρ
  (PMF.ofFintype (fun b : Bool ↦ cond b p (1 - p)) (by simp [hp])).map fun keep ↦
    if keep then x else -x

-- Source: FABL.Chapter02.NoiseStability.NoiseKernels:133
/-- O'Donnell, Definition 2.40: `Nρ(x)`, the independent coordinate noise kernel on the
sign cube. -/
noncomputable def noiseKernel (ρ : ℝ) (hρ : ρ ∈ Set.Icc (-1 : ℝ) 1)
    (x : (FABL.SignCube (n))) : PMF (FABL.SignCube (n)) :=
  independentProductPMF fun i ↦ coordinateNoisePMF ρ hρ (x i)

-- Source: FABL.Chapter02.NoiseStability.NoiseKernels:156
/-- O'Donnell, Definition 2.41: the joint law of a uniform string and a conditionally
`ρ`-correlated string. -/
noncomputable def correlatedPairPMF (ρ : ℝ) (hρ : ρ ∈ Set.Icc (-1 : ℝ) 1) :
    PMF ((FABL.SignCube (n)) × (FABL.SignCube (n))) :=
  (uniformPMF (FABL.SignCube (n))).bind fun x ↦
    (noiseKernel ρ hρ x).map fun y ↦ (x, y)

-- Source: FABL.Chapter02.NoiseStability.NoiseKernels:275
/-- O'Donnell, Definitions 2.40--2.43: finite expectation with respect to a probability mass
function. -/
noncomputable def pmfExpectation {Ω : Type*} [Fintype Ω] (p : PMF Ω)
    (f : Ω → ℝ) : ℝ :=
  ∑ x, (p x).toReal * f x

-- Source: FABL.Chapter02.NoiseStability.NoiseKernels:281
/-- PMF expectation agrees with integration against the associated measure. -/
theorem pmfExpectation_eq_integral {Ω : Type*} [Fintype Ω]
    [MeasurableSpace Ω] [MeasurableSingletonClass Ω] (p : PMF Ω) (f : Ω → ℝ) :
    pmfExpectation p f = ∫ x, f x ∂p.toMeasure := by
  rw [PMF.integral_eq_sum]
  simp only [pmfExpectation, smul_eq_mul]

-- Source: FABL.Chapter02.NoiseStability.NoiseKernels:288
/-- Expectation under a mapped finite PMF is expectation after composition. -/
theorem pmfExpectation_map {Ω Λ : Type*} [Fintype Ω] [Fintype Λ]
    (p : PMF Ω) (g : Ω → Λ) (f : Λ → ℝ) :
    pmfExpectation (p.map g) f = pmfExpectation p (f ∘ g) := by
  letI : MeasurableSpace Ω := ⊤
  letI : MeasurableSpace Λ := ⊤
  rw [pmfExpectation_eq_integral, pmfExpectation_eq_integral]
  rw [← PMF.toMeasure_map g p (measurable_of_finite g)]
  exact MeasureTheory.integral_map (measurable_of_finite g).aemeasurable
    (measurable_of_finite f).aestronglyMeasurable

-- Source: FABL.Chapter02.NoiseStability.NoiseKernels:299
/-- The expectation of the constant-one random variable is one. -/
theorem pmfExpectation_const_one {Ω : Type*} [Fintype Ω] (p : PMF Ω) :
    pmfExpectation p (fun _ ↦ 1) = 1 := by
  letI : MeasurableSpace Ω := ⊤
  rw [pmfExpectation_eq_integral]
  simp

-- Source: FABL.Chapter02.NoiseStability.NoiseKernels:318
/-- The law of total expectation for finite PMFs. -/
theorem pmfExpectation_bind {Ω Λ : Type*} [Fintype Ω] [Fintype Λ]
    (p : PMF Ω) (q : Ω → PMF Λ) (f : Λ → ℝ) :
    pmfExpectation (p.bind q) f =
      pmfExpectation p (fun x ↦ pmfExpectation (q x) f) := by
  classical
  unfold pmfExpectation
  simp_rw [PMF.bind_apply, tsum_fintype]
  have htoReal (y : Λ) :
      (∑ x, p x * q x y).toReal = ∑ x, (p x).toReal * (q x y).toReal := by
    rw [ENNReal.toReal_sum]
    · simp only [ENNReal.toReal_mul]
    · intro x _
      exact ENNReal.mul_ne_top (p.apply_ne_top x) ((q x).apply_ne_top y)
  simp_rw [htoReal, Finset.sum_mul]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro x _
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro y _
  ring

-- Source: FABL.Chapter02.NoiseStability.NoiseKernels:341
/-- A constant factor can be pulled out of a finite PMF expectation. -/
theorem pmfExpectation_const_mul {Ω : Type*} [Fintype Ω]
    (p : PMF Ω) (c : ℝ) (f : Ω → ℝ) :
    pmfExpectation p (fun x ↦ c * f x) = c * pmfExpectation p f := by
  unfold pmfExpectation
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro x _
  ring

-- Source: FABL.Chapter02.NoiseStability.NoiseKernels:361
/-- Finite PMF expectation preserves addition. -/
theorem pmfExpectation_add {Ω : Type*} [Fintype Ω]
    (p : PMF Ω) (f g : Ω → ℝ) :
    pmfExpectation p (fun x ↦ f x + g x) = pmfExpectation p f + pmfExpectation p g := by
  unfold pmfExpectation
  rw [← Finset.sum_add_distrib]
  apply Finset.sum_congr rfl
  intro x _
  ring

-- Source: FABL.Chapter02.NoiseStability.NoiseKernels:371
/-- Finite PMF expectation commutes with a finite sum. -/
theorem pmfExpectation_sum {Ω ι : Type*} [Fintype Ω] [Fintype ι]
    (p : PMF Ω) (f : ι → Ω → ℝ) :
    pmfExpectation p (fun x ↦ ∑ i, f i x) =
      ∑ i, pmfExpectation p (f i) := by
  classical
  unfold pmfExpectation
  simp_rw [Finset.mul_sum]
  exact Finset.sum_comm

-- Source: FABL.Chapter02.NoiseStability.NoiseKernels:395
/-- The expectation of a constant under a finite PMF is that constant. -/
theorem pmfExpectation_const {Ω : Type*} [Fintype Ω]
    (p : PMF Ω) (c : ℝ) :
    pmfExpectation p (fun _ ↦ c) = c := by
  rw [show (fun _ : Ω ↦ c) = fun x ↦ c * (fun _ : Ω ↦ (1 : ℝ)) x by
    funext x
    simp]
  rw [pmfExpectation_const_mul, pmfExpectation_const_one, mul_one]

-- Source: FABL.Chapter02.NoiseStability.NoiseKernels:404
/-- Finite PMF expectation is monotone. -/
theorem pmfExpectation_mono {Ω : Type*} [Fintype Ω]
    (p : PMF Ω) {f g : Ω → ℝ} (hfg : ∀ x, f x ≤ g x) :
    pmfExpectation p f ≤ pmfExpectation p g := by
  unfold pmfExpectation
  exact Finset.sum_le_sum fun x _ ↦
    mul_le_mul_of_nonneg_left (hfg x) ENNReal.toReal_nonneg

-- Source: FABL.Chapter02.NoiseStability.NoiseKernels:412
/-- A pointwise nonnegative random variable has nonnegative finite PMF expectation. -/
theorem pmfExpectation_nonneg {Ω : Type*} [Fintype Ω]
    (p : PMF Ω) {f : Ω → ℝ} (hf : ∀ x, 0 ≤ f x) :
    0 ≤ pmfExpectation p f := by
  rw [← pmfExpectation_const p 0]
  exact pmfExpectation_mono p hf

-- Source: FABL.Chapter02.NoiseStability.NoiseKernels:419
/-- Expectation under Mathlib's uniform finite PMF is normalized finite expectation. -/
theorem pmfExpectation_uniformPMF_eq_expect
    {Ω : Type*} [Fintype Ω] [Nonempty Ω]
    (f : Ω → ℝ) :
    pmfExpectation (uniformPMF Ω) f = 𝔼 x, f x := by
  letI : MeasurableSpace Ω := ⊤
  rw [pmfExpectation_eq_integral, integral_uniformPMF_eq_expect]

-- Source: FABL.Chapter02.NoiseStability.NoiseKernels:427
/-- O'Donnell, Definition 2.41: the expected real sign after one-coordinate noise is `ρ` times
the original sign. -/
theorem pmfExpectation_coordinateNoisePMF_signValue
    (ρ : ℝ) (hρ : ρ ∈ Set.Icc (-1 : ℝ) 1) (x : Sign) :
    pmfExpectation (coordinateNoisePMF ρ hρ x) signValue = ρ * signValue x := by
  let p := correlationKeepProbability ρ hρ
  have hp : p ≤ 1 := correlationKeepProbability_le_one ρ hρ
  have hpENN : (p : ENNReal) ≤ 1 := by exact_mod_cast hp
  have hpcoe : (p : ℝ) = (1 + ρ) / 2 := rfl
  rw [coordinateNoisePMF, pmfExpectation_map]
  change pmfExpectation (PMF.ofFintype (fun b : Bool ↦ cond b p (1 - p)) (by simp [hp]))
    (fun keep ↦ signValue (if keep then x else -x)) = _
  simp only [pmfExpectation, PMF.ofFintype_apply, Fintype.sum_bool,
    Bool.cond_false, Bool.cond_true, Bool.apply_cond, ENNReal.coe_toReal, ↓reduceIte]
  rw [ENNReal.toReal_sub_of_le hpENN (by simp), ENNReal.toReal_one,
    ENNReal.coe_toReal, hpcoe]
  rcases Int.units_eq_one_or x with rfl | rfl <;> norm_num [signValue_one, signValue_neg_one] <;> ring

-- Source: FABL.Chapter02.NoiseStability.NoiseKernels:445
/-- Expectations of coordinatewise products factor under an independent product PMF. -/
theorem pmfExpectation_independentProductPMF_prod {ι : Type*} [Fintype ι]
    [DecidableEq ι] {α : ι → Type*} [∀ i, Fintype (α i)]
    (p : ∀ i, PMF (α i))
    (q : ∀ i, α i → ℝ) :
    pmfExpectation (independentProductPMF p) (fun x ↦ ∏ i, q i (x i)) =
      ∏ i, pmfExpectation (p i) (q i) := by
  classical
  unfold pmfExpectation
  simp_rw [independentProductPMF_apply, ENNReal.toReal_prod, ← Finset.prod_mul_distrib]
  exact (Fintype.prod_sum fun i y ↦ (p i y).toReal * q i y).symm

-- Source: FABL.Chapter02.NoiseStability.NoiseKernels:457
/-- O'Donnell, Example 2.44 and Proposition 2.47: the noise kernel sends a Walsh monomial's
expectation to its correlation eigenvalue. -/
theorem pmfExpectation_noiseKernel_monomial
    (ρ : ℝ) (hρ : ρ ∈ Set.Icc (-1 : ℝ) 1) (x : (FABL.SignCube (n)))
    (S : Finset (Fin n)) :
    pmfExpectation (noiseKernel ρ hρ x) (monomial S) =
      ρ ^ S.card * monomial S x := by
  classical
  let q : (i : Fin n) → Sign → ℝ := fun i y ↦ if i ∈ S then signValue y else 1
  have hmonomial (y : (FABL.SignCube (n))) : monomial S y = ∏ i, q i (y i) := by
    rw [monomial]
    simp [q]
  rw [show pmfExpectation (noiseKernel ρ hρ x) (monomial S) =
      pmfExpectation (noiseKernel ρ hρ x) (fun y ↦ ∏ i, q i (y i)) by
    apply Finset.sum_congr rfl
    intro y _
    rw [hmonomial]]
  rw [noiseKernel, pmfExpectation_independentProductPMF_prod]
  simp only [q]
  have hcoordinate (i : Fin n) :
      pmfExpectation (coordinateNoisePMF ρ hρ (x i))
          (fun y ↦ if i ∈ S then signValue y else 1) =
        if i ∈ S then ρ * signValue (x i) else 1 := by
    by_cases hi : i ∈ S
    · simp only [hi, if_true]
      exact pmfExpectation_coordinateNoisePMF_signValue ρ hρ (x i)
    · simp only [hi, if_false]
      exact pmfExpectation_const_one (coordinateNoisePMF ρ hρ (x i))
  simp_rw [hcoordinate]
  rw [Finset.prod_ite]
  simp only [Finset.prod_const_one, mul_one]
  rw [Finset.prod_mul_distrib, Finset.prod_const]
  simp [monomial]

end FABL

end

/- Source fragment: FABL.Chapter02.NoiseStability.NoiseOperator. Original licenses and source proofs retained. -/

section

/-
Copyright (c) 2026 Asher Yan. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Asher Yan with Codex
-/

/-!
# Noise operator and stability

Book items: Definition 2.42, Definition 2.43, Definition 2.46, Fact 2.48, Proposition 2.47, Theorem
2.45.

The noise operator, noise stability, noise sensitivity, and the majority limit from Section 2.4
of O'Donnell's *Analysis of Boolean Functions*.
-/

open Complex Filter Finset MeasureTheory ProbabilityTheory Set WithLp
open scoped Asymptotics BigOperators ENNReal RealInnerProductSpace Topology

namespace FABL

variable {n : ℕ}

-- Source: FABL.Chapter02.NoiseStability.NoiseOperator:34
/-- O'Donnell, Definition 2.46: the Fourier multiplier form of the noise operator.  The
construction uses the Walsh basis to obtain linearity by construction. -/
noncomputable def noiseOperator (ρ : ℝ) :
    ((FABL.SignCube (n)) → ℝ) →ₗ[ℝ] ((FABL.SignCube (n)) → ℝ) :=
  (walshBasis n).constr ℝ fun S ↦ ρ ^ S.card • monomial S

-- Source: FABL.Chapter02.NoiseStability.NoiseOperator:40
/-- O'Donnell, Proposition 2.47: each Walsh character is an eigenfunction of the noise
operator, with eigenvalue `ρ ^ |S|`. -/
 theorem noiseOperator_monomial (ρ : ℝ) (S : Finset (Fin n)) :
    noiseOperator ρ (monomial S) = ρ ^ S.card • monomial S := by
  rw [noiseOperator]
  have hbasis : walshBasis n S = monomial S := parity_orthonormal_basis.1 S
  simpa only [hbasis] using
    (Module.Basis.constr_basis (walshBasis n) ℝ
      (fun T : Finset (Fin n) ↦ ρ ^ T.card • monomial T) S)

-- Source: FABL.Chapter02.NoiseStability.NoiseOperator:50
/-- O'Donnell, Proposition 2.47: pointwise form of the Walsh-character eigenvalue identity. -/
theorem noiseOperator_monomial_apply (ρ : ℝ) (S : Finset (Fin n))
    (x : (FABL.SignCube (n))) :
    noiseOperator ρ (monomial S) x = ρ ^ S.card * monomial S x := by
  rw [noiseOperator_monomial]
  rfl

-- Source: FABL.Chapter02.NoiseStability.NoiseOperator:57
/-- The conditional-expectation realization of the noise operator. -/
private noncomputable def kernelNoiseOperator
    (ρ : ℝ) (hρ : ρ ∈ Set.Icc (-1 : ℝ) 1) :
    ((FABL.SignCube (n)) → ℝ) →ₗ[ℝ] ((FABL.SignCube (n)) → ℝ) where
  toFun f x := pmfExpectation (noiseKernel ρ hρ x) f
  map_add' f g := by
    funext x
    unfold pmfExpectation
    simp only [Pi.add_apply]
    rw [← Finset.sum_add_distrib]
    apply Finset.sum_congr rfl
    intro y _
    ring
  map_smul' c f := by
    funext x
    unfold pmfExpectation
    simp only [Pi.smul_apply, smul_eq_mul, RingHom.id_apply]
    rw [Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro y _
    ring

-- Source: FABL.Chapter02.NoiseStability.NoiseOperator:79
/-- The Fourier multiplier and conditional-expectation constructions of `Tρ` agree. -/
private theorem kernelNoiseOperator_eq_noiseOperator
    (ρ : ℝ) (hρ : ρ ∈ Set.Icc (-1 : ℝ) 1) :
    kernelNoiseOperator ρ hρ = (noiseOperator ρ :
      ((FABL.SignCube (n)) → ℝ) →ₗ[ℝ] ((FABL.SignCube (n)) → ℝ)) := by
  apply (walshBasis n).ext
  intro S
  funext x
  have hbasis : walshBasis n S = monomial S := parity_orthonormal_basis.1 S
  rw [hbasis, kernelNoiseOperator, noiseOperator_monomial_apply]
  exact pmfExpectation_noiseKernel_monomial ρ hρ x S

-- Source: FABL.Chapter02.NoiseStability.NoiseOperator:91
/-- O'Donnell, Definition 2.46: conditional expectation under `Nρ(x)` equals evaluation of
the Fourier-multiplier noise operator. -/
theorem noiseOperator_apply_eq_pmfExpectation
    (ρ : ℝ) (hρ : ρ ∈ Set.Icc (-1 : ℝ) 1)
    (f : (FABL.SignCube (n)) → ℝ) (x : (FABL.SignCube (n))) :
    noiseOperator ρ f x = pmfExpectation (noiseKernel ρ hρ x) f := by
  rw [← kernelNoiseOperator_eq_noiseOperator ρ hρ]
  rfl

-- Source: FABL.Chapter02.NoiseStability.NoiseOperator:100
/-- O'Donnell, Definition 2.42: noise stability is the expected product over the honest
`ρ`-correlated pair distribution. -/
noncomputable def noiseStability (ρ : ℝ) (hρ : ρ ∈ Set.Icc (-1 : ℝ) 1)
    (f : (FABL.SignCube (n)) → ℝ) : ℝ :=
  pmfExpectation (correlatedPairPMF ρ hρ) fun xy ↦ f xy.1 * f xy.2

-- Source: FABL.Chapter02.NoiseStability.NoiseOperator:211
/-- O'Donnell, Fact 2.48: stability is the normalized inner product with the noise operator. -/
theorem noiseStability_eq_uniformInner_noiseOperator
    (ρ : ℝ) (hρ : ρ ∈ Set.Icc (-1 : ℝ) 1)
    (f : (FABL.SignCube (n)) → ℝ) :
    noiseStability ρ hρ f = (FABL.uniformInner (f) (noiseOperator ρ f)) := by
  unfold noiseStability correlatedPairPMF
  rw [pmfExpectation_bind]
  simp_rw [pmfExpectation_map]
  rw [pmfExpectation_uniformPMF_eq_expect]
  rw [uniformInner, RCLike.wInner_cWeight_eq_expect]
  apply Finset.expect_congr rfl
  intro x _
  simp only [RCLike.inner_apply, starRingEnd_apply, star_trivial]
  change pmfExpectation (noiseKernel ρ hρ x) (fun y ↦ f x * f y) =
    noiseOperator ρ f x * f x
  rw [pmfExpectation_const_mul, noiseOperator_apply_eq_pmfExpectation ρ hρ]
  ring

end FABL

end

/- Source fragment: FABL.Chapter02.NoiseStability.FourierFormulas. Original licenses and source proofs retained. -/

section

/-
Copyright (c) 2026 Asher Yan. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Asher Yan with Codex
-/

/-!
# Fourier formulas for noise stability

Book items: Example 2.44, Proposition 2.47, Theorem 2.49, Exercise 2.42.

The Fourier and spectral-moment formulas for noise stability and noise sensitivity from Section 2.4
of O'Donnell's *Analysis of Boolean Functions*.
-/

open Complex Filter Finset MeasureTheory ProbabilityTheory Set WithLp
open scoped Asymptotics BigOperators ENNReal RealInnerProductSpace Topology

namespace FABL

variable {n : ℕ}

-- Source: FABL.Chapter02.NoiseStability.FourierFormulas:28
/-- O'Donnell, Proposition 2.47: pointwise Fourier expansion of the noise operator. -/
theorem noiseOperator_fourier_expansion (ρ : ℝ) (f : (FABL.SignCube (n)) → ℝ)
    (x : (FABL.SignCube (n))) :
    noiseOperator ρ f x =
      ∑ S, ρ ^ S.card * fourierCoeff f S * monomial S x := by
  classical
  have hf : f = ∑ S, fourierCoeff f S • monomial S := by
    funext y
    simp only [Finset.sum_apply, Pi.smul_apply, smul_eq_mul]
    exact fourier_expansion f y
  conv_lhs => rw [hf]
  rw [map_sum]
  simp_rw [map_smul, noiseOperator_monomial]
  simp only [Finset.sum_apply, Pi.smul_apply, smul_eq_mul]
  apply Finset.sum_congr rfl
  intro S _
  ring

-- Source: FABL.Chapter02.NoiseStability.FourierFormulas:76
/-- O'Donnell, Theorem 2.49: the subset-indexed Fourier formula for noise stability. -/
theorem noiseStability_eq_sum_rho_pow_mul_sq_fourierCoeff
    (ρ : ℝ) (hρ : ρ ∈ Set.Icc (-1 : ℝ) 1) (f : (FABL.SignCube (n)) → ℝ) :
    noiseStability ρ hρ f =
      ∑ S, ρ ^ S.card * fourierCoeff f S ^ 2 := by
  rw [noiseStability_eq_uniformInner_noiseOperator]
  rw [uniformInner, RCLike.wInner_cWeight_eq_expect]
  simp only [RCLike.inner_apply, starRingEnd_apply, star_trivial]
  calc
    (𝔼 x, noiseOperator ρ f x * f x) =
        𝔼 x, (∑ S, ρ ^ S.card * fourierCoeff f S * monomial S x) * f x := by
      apply Finset.expect_congr rfl
      intro x _
      rw [noiseOperator_fourier_expansion]
    _ = 𝔼 x, ∑ S, (ρ ^ S.card * fourierCoeff f S * monomial S x) * f x := by
      apply Finset.expect_congr rfl
      intro x _
      rw [Finset.sum_mul]
    _ = ∑ S, 𝔼 x, (ρ ^ S.card * fourierCoeff f S * monomial S x) * f x := by
      rw [Finset.expect_sum_comm]
    _ = ∑ S, ρ ^ S.card * fourierCoeff f S ^ 2 := by
      apply Finset.sum_congr rfl
      intro S _
      rw [show (𝔼 x, (ρ ^ S.card * fourierCoeff f S * monomial S x) * f x) =
          ρ ^ S.card * fourierCoeff f S * (𝔼 x, f x * monomial S x) by
        symm
        calc
          ρ ^ S.card * fourierCoeff f S * (𝔼 x, f x * monomial S x) =
              𝔼 x, (ρ ^ S.card * fourierCoeff f S) * (f x * monomial S x) :=
            Finset.mul_expect Finset.univ (fun x ↦ f x * monomial S x)
              (ρ ^ S.card * fourierCoeff f S)
          _ = 𝔼 x, (ρ ^ S.card * fourierCoeff f S * monomial S x) * f x := by
            apply Finset.expect_congr rfl
            intro x _
            ring]
      rw [← fourierCoeff]
      ring

end FABL

end

/- Source fragment: FABL.Chapter02.NoiseStability.StableInfluence. Original licenses and source proofs retained. -/

section

/-
Copyright (c) 2026 Asher Yan. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Asher Yan with Codex
-/

/-!
# Stable influence

Book items: Definition 2.52, Fact 2.53, Proposition 2.50, Proposition 2.51, Proposition 2.54,
Exercise 2.40, Exercise 2.45.

Stability curves, extremal stability, stable influences, and derivative formulas from Section 2.4
of O'Donnell's *Analysis of Boolean Functions*.
-/

open Complex Filter Finset MeasureTheory ProbabilityTheory Set WithLp
open scoped Asymptotics BigOperators ENNReal RealInnerProductSpace Topology

namespace FABL

variable {n : ℕ}

-- Source: FABL.Chapter02.NoiseStability.StableInfluence:200
/-- O'Donnell, Proposition 2.19 and Definition 2.52: Fourier coefficients of a discrete
derivative, in insert/erase coordinates. -/
theorem fourierCoeff_discreteDerivative (f : (FABL.SignCube (n)) → ℝ)
    (i : Fin n) (T : Finset (Fin n)) :
    fourierCoeff (discreteDerivative i f) T =
      if i ∈ T then 0 else fourierCoeff f (insert i T) := by
  classical
  unfold fourierCoeff
  calc
    (𝔼 x, discreteDerivative i f x * monomial T x) =
        𝔼 x, (∑ S with i ∈ S, fourierCoeff f S * monomial (S.erase i) x) *
          monomial T x := by
      apply Finset.expect_congr rfl
      intro x _
      rw [discreteDerivative_eq_fourier_sum]
    _ = 𝔼 x, ∑ S with i ∈ S,
          (fourierCoeff f S * monomial (S.erase i) x) * monomial T x := by
      apply Finset.expect_congr rfl
      intro x _
      rw [Finset.sum_mul]
    _ = ∑ S with i ∈ S,
          𝔼 x, (fourierCoeff f S * monomial (S.erase i) x) * monomial T x := by
      rw [Finset.expect_sum_comm]
    _ = ∑ S with i ∈ S,
          fourierCoeff f S * (if S.erase i = T then 1 else 0) := by
      apply Finset.sum_congr rfl
      intro S _
      rw [← expect_monomial_mul (S.erase i) T, Finset.mul_expect]
      apply Finset.expect_congr rfl
      intro x _
      ring
    _ = if i ∈ T then 0 else fourierCoeff f (insert i T) := by
      by_cases hiT : i ∈ T
      · rw [if_pos hiT]
        apply Finset.sum_eq_zero
        intro S hS
        have hiS : i ∈ S := (Finset.mem_filter.mp hS).2
        have hne : S.erase i ≠ T := by
          intro hEq
          have : i ∉ S.erase i := by simp
          rw [hEq] at this
          exact this hiT
        simp [hne]
      · rw [if_neg hiT, Finset.sum_eq_single (insert i T)]
        · simp [hiT]
        · intro S hS hne
          have hiS : i ∈ S := (Finset.mem_filter.mp hS).2
          have herase : S.erase i ≠ T := by
            exact (Finset.erase_eq_iff_eq_insert hiS hiT).not.mpr hne
          simp [herase]
        · simp

-- Source: FABL.Chapter02.NoiseStability.StableInfluence:252
/-- O'Donnell, Definition 2.52: the `ρ`-stable influence of coordinate `i`, in its exact
Fourier form. -/
noncomputable def stableInfluence (ρ : ℝ) (f : (FABL.SignCube (n)) → ℝ) (i : Fin n) : ℝ :=
  ∑ S with i ∈ S, ρ ^ (S.card - 1) * fourierCoeff f S ^ 2

-- Source: FABL.Chapter02.NoiseStability.StableInfluence:257
/-- Erasing a distinguished member bijects subsets containing it with subsets not containing it. -/
private def eraseContainingEquiv (i : Fin n) :
    {S : Finset (Fin n) // i ∈ S} ≃ {T : Finset (Fin n) // i ∉ T} where
  toFun S := ⟨S.1.erase i, by simp⟩
  invFun T := ⟨insert i T.1, by simp⟩
  left_inv S := by
    apply Subtype.ext
    simp [Finset.insert_erase S.2]
  right_inv T := by
    apply Subtype.ext
    simp [T.2]

-- Source: FABL.Chapter02.NoiseStability.StableInfluence:269
/-- O'Donnell, Definition 2.52: the Fourier definition of stable influence agrees with
the noise stability of the discrete derivative. -/
theorem stableInfluence_eq_noiseStability_discreteDerivative
    (ρ : ℝ) (hρ : ρ ∈ Set.Icc (0 : ℝ) 1)
    (f : (FABL.SignCube (n)) → ℝ) (i : Fin n) :
    stableInfluence ρ f i =
      noiseStability ρ ⟨by linarith [hρ.1], hρ.2⟩ (discreteDerivative i f) := by
  rw [stableInfluence, noiseStability_eq_sum_rho_pow_mul_sq_fourierCoeff ρ
    ⟨by linarith [hρ.1], hρ.2⟩ (discreteDerivative i f)]
  simp_rw [fourierCoeff_discreteDerivative]
  simp only [ite_pow, zero_pow (by norm_num : (2 : ℕ) ≠ 0), mul_ite, mul_zero]
  rw [show (∑ T, if i ∈ T then 0 else
      ρ ^ T.card * fourierCoeff f (insert i T) ^ 2) =
      ∑ T with i ∉ T, ρ ^ T.card * fourierCoeff f (insert i T) ^ 2 by
    rw [Finset.sum_filter]
    apply Finset.sum_congr rfl
    intro T _
    by_cases hiT : i ∈ T <;> simp [hiT]]
  have hleft :
      (∑ S with i ∈ S, ρ ^ (S.card - 1) * fourierCoeff f S ^ 2) =
        ∑ S : {S : Finset (Fin n) // i ∈ S},
          ρ ^ (S.1.card - 1) * fourierCoeff f S.1 ^ 2 := by
    symm
    simpa using (Finset.sum_subtype_eq_sum_filter
      (s := (Finset.univ : Finset (Finset (Fin n))))
      (p := fun S : Finset (Fin n) ↦ i ∈ S)
      (fun S ↦ ρ ^ (S.card - 1) * fourierCoeff f S ^ 2))
  have hright :
      (∑ T with i ∉ T, ρ ^ T.card * fourierCoeff f (insert i T) ^ 2) =
        ∑ T : {T : Finset (Fin n) // i ∉ T.1},
          ρ ^ T.1.card * fourierCoeff f (insert i T.1) ^ 2 := by
    exact Finset.sum_subtype
      ((Finset.univ : Finset (Finset (Fin n))).filter fun T ↦ i ∉ T)
      (by simp)
      (fun T ↦ ρ ^ T.card * fourierCoeff f (insert i T) ^ 2)
  rw [hleft, hright]
  apply Fintype.sum_equiv (eraseContainingEquiv i)
  intro S
  change ρ ^ (S.1.card - 1) * fourierCoeff f S.1 ^ 2 =
    ρ ^ (S.1.erase i).card * fourierCoeff f (insert i (S.1.erase i)) ^ 2
  rw [Finset.card_erase_of_mem S.2, Finset.insert_erase S.2]

-- Source: FABL.Chapter02.NoiseStability.StableInfluence:315
/-- O'Donnell, Definition 2.52: stable influence is nonnegative for correlation parameters in
`[0,1]`. -/
theorem stableInfluence_nonneg (ρ : ℝ) (hρ : ρ ∈ Set.Icc (0 : ℝ) 1)
    (f : (FABL.SignCube (n)) → ℝ) (i : Fin n) :
    0 ≤ stableInfluence ρ f i := by
  unfold stableInfluence
  exact Finset.sum_nonneg fun S _ ↦
    mul_nonneg (pow_nonneg hρ.1 _) (sq_nonneg _)

end FABL

end

/- Source fragment: FABL.Chapter03.LowDegreeSpectralConcentration. Original licenses and source proofs retained. -/

section

/-
Copyright (c) 2026 Asher Yan. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Asher Yan with Codex
-/

/-!
# Low-degree spectral concentration

Book items: Definition 3.1, Fact 3.7, Lemma 3.5, Proposition 3.2, Proposition 3.3, Proposition 3.6,
Theorem 3.4, Exercise 3.4.

Formalization of Section 3.1 of O'Donnell's *Analysis of Boolean Functions*.
-/

open Finset
open scoped BigOperators

namespace FABL

variable {n : ℕ}

-- Source: FABL.Chapter03.LowDegreeSpectralConcentration:28
/-- O'Donnell, Definition 3.1: Fourier weight strictly above a real degree cutoff. The cutoff is
real because the book subsequently uses `𝐈[f] / ε` and `1 / δ`. -/
noncomputable def fourierWeightAboveReal (k : ℝ) (f : (FABL.SignCube (n)) → ℝ) : ℝ :=
  ∑ S ∈ (Finset.univ.filter fun S : Finset (Fin n) ↦ k < (S.card : ℝ)), fourierWeight f S

-- Source: FABL.Chapter03.LowDegreeSpectralConcentration:33
/-- O'Donnell, Definition 3.1: the Fourier spectrum is `ε`-concentrated through degree `k`. -/
def IsFourierSpectrumConcentratedUpTo
    (f : (FABL.SignCube (n)) → ℝ) (ε k : ℝ) : Prop :=
  fourierWeightAboveReal k f ≤ ε

-- Source: FABL.Chapter03.LowDegreeSpectralConcentration:38
/-- The real-cutoff definition specializes to the natural-cutoff tail from Chapter 1. -/
theorem fourierWeightAboveReal_natCast (k : ℕ) (f : (FABL.SignCube (n)) → ℝ) :
    fourierWeightAboveReal k f = fourierWeightAbove k f := by
  classical
  unfold fourierWeightAboveReal fourierWeightAbove
  congr 1
  ext S
  simp

-- Source: FABL.Chapter03.LowDegreeSpectralConcentration:61
/-- O'Donnell, Proposition 3.2: total influence controls the Fourier mass above the real cutoff
`𝐈[f] / ε`. -/
theorem isFourierSpectrumConcentratedUpTo_totalInfluence_div
    (f : (FABL.SignCube (n)) → ℝ) {ε : ℝ} (hε : 0 < ε) :
    IsFourierSpectrumConcentratedUpTo f ε (totalInfluence f / ε) := by
  classical
  unfold IsFourierSpectrumConcentratedUpTo
  let I : ℝ := totalInfluence f
  have hI : 0 ≤ I := totalInfluence_nonneg f
  by_cases hIzero : I = 0
  · have hweighted :
        (∑ S : Finset (Fin n), (S.card : ℝ) * fourierCoeff f S ^ 2) = 0 := by
      rw [← totalInfluence_eq_sum_card_mul_sq_fourierCoeff]
      exact hIzero
    have hterm (S : Finset (Fin n)) :
        (S.card : ℝ) * fourierCoeff f S ^ 2 = 0 :=
      (Finset.sum_eq_zero_iff_of_nonneg fun T _ ↦
        mul_nonneg (Nat.cast_nonneg T.card) (sq_nonneg (fourierCoeff f T))).mp
          hweighted S (Finset.mem_univ S)
    have htail : fourierWeightAboveReal (totalInfluence f / ε) f = 0 := by
      rw [show totalInfluence f / ε = 0 by change I / ε = 0; simp [hIzero]]
      unfold fourierWeightAboveReal
      apply Finset.sum_eq_zero
      intro S hS
      have hcardNat : 0 < S.card := by
        simpa using (Finset.mem_filter.mp hS).2
      have hcard : 0 < (S.card : ℝ) := by exact_mod_cast hcardNat
      unfold fourierWeight
      nlinarith [hterm S, sq_nonneg (fourierCoeff f S)]
    rw [htail]
    exact hε.le
  · have hIpos : 0 < I := lt_of_le_of_ne hI (Ne.symm hIzero)
    let t : ℝ := I / ε
    have ht : 0 < t := div_pos hIpos hε
    have hmul : t * fourierWeightAboveReal t f ≤ I := by
      calc
        t * fourierWeightAboveReal t f =
            ∑ S ∈ (Finset.univ.filter fun S : Finset (Fin n) ↦ t < (S.card : ℝ)),
              t * fourierWeight f S := by
          rw [fourierWeightAboveReal, Finset.mul_sum]
        _ ≤ ∑ S ∈ (Finset.univ.filter fun S : Finset (Fin n) ↦ t < (S.card : ℝ)),
              (S.card : ℝ) * fourierWeight f S := by
          apply Finset.sum_le_sum
          intro S hS
          exact mul_le_mul_of_nonneg_right (Finset.mem_filter.mp hS |>.2).le
            (sq_nonneg (fourierCoeff f S))
        _ ≤ ∑ S : Finset (Fin n), (S.card : ℝ) * fourierWeight f S := by
          exact Finset.sum_le_sum_of_subset_of_nonneg (Finset.filter_subset _ _)
            (fun S _ _ ↦ mul_nonneg (Nat.cast_nonneg S.card)
              (sq_nonneg (fourierCoeff f S)))
        _ = I := by
          simpa [fourierWeight, I] using
            (totalInfluence_eq_sum_card_mul_sq_fourierCoeff f).symm
    have htail : fourierWeightAboveReal t f ≤ I / t :=
      (le_div_iff₀ ht).2 (by simpa [mul_comm] using hmul)
    have hquotient : I / t = ε := by
      dsimp [t]
      field_simp
    change fourierWeightAboveReal t f ≤ ε
    exact htail.trans_eq hquotient

/-! ## The support bound for low-degree functions -/

-- Source: FABL.Chapter03.LowDegreeSpectralConcentration:271
/-- Restrict a real-valued function on an `(n+1)`-cube by fixing its first coordinate. -/
def firstCoordinateSlice (f : (FABL.SignCube (n + 1)) → ℝ) (b : Sign) : (FABL.SignCube (n)) → ℝ :=
  fun x ↦ f (Fin.cons b x)

-- Source: FABL.Chapter03.LowDegreeSpectralConcentration:279
/-- Lift a frequency past the first coordinate. -/
def tailFrequency (S : Finset (Fin n)) : Finset (Fin (n + 1)) :=
  S.map (Fin.succEmb n)

-- Source: FABL.Chapter03.LowDegreeSpectralConcentration:283
 theorem card_tailFrequency (S : Finset (Fin n)) :
    (tailFrequency S).card = S.card := by
  simp [tailFrequency]

-- Source: FABL.Chapter03.LowDegreeSpectralConcentration:287
 theorem zero_notMem_tailFrequency (S : Finset (Fin n)) :
    (0 : Fin (n + 1)) ∉ tailFrequency S := by
  simp [tailFrequency]

-- Source: FABL.Chapter03.LowDegreeSpectralConcentration:291
/-- A tail frequency evaluates on a cons input as the original frequency. -/
theorem monomial_tailFrequency_fin_cons (S : Finset (Fin n))
    (b : Sign) (x : (FABL.SignCube (n))) :
    monomial (tailFrequency S) (Fin.cons b x) = monomial S x := by
  classical
  simp [monomial, tailFrequency, Finset.prod_map]

-- Source: FABL.Chapter03.LowDegreeSpectralConcentration:298
/-- Adding the first coordinate to a tail frequency contributes the fixed first sign. -/
theorem monomial_insert_zero_tailFrequency_fin_cons (S : Finset (Fin n))
    (b : Sign) (x : (FABL.SignCube (n))) :
    monomial (insert 0 (tailFrequency S)) (Fin.cons b x) =
      signValue b * monomial S x := by
  classical
  rw [monomial, Finset.prod_insert (zero_notMem_tailFrequency S)]
  change signValue b * monomial (tailFrequency S) (Fin.cons b x) = _
  rw [monomial_tailFrequency_fin_cons]

-- Source: FABL.Chapter03.LowDegreeSpectralConcentration:308
/-- The coefficient on a tail frequency is the mean of the two slice coefficients. -/
theorem fourierCoeff_tailFrequency (f : (FABL.SignCube (n + 1)) → ℝ)
    (S : Finset (Fin n)) :
    fourierCoeff f (tailFrequency S) =
      (fourierCoeff (firstCoordinateSlice f 1) S +
        fourierCoeff (firstCoordinateSlice f (-1)) S) / 2 := by
  rw [fourierCoeff, expect_fin_cons]
  simp_rw [monomial_tailFrequency_fin_cons]
  rfl

-- Source: FABL.Chapter03.LowDegreeSpectralConcentration:318
/-- The coefficient on a frequency containing the first coordinate is half the difference of the
two slice coefficients. -/
theorem fourierCoeff_insert_zero_tailFrequency (f : (FABL.SignCube (n + 1)) → ℝ)
    (S : Finset (Fin n)) :
    fourierCoeff f (insert 0 (tailFrequency S)) =
      (fourierCoeff (firstCoordinateSlice f 1) S -
        fourierCoeff (firstCoordinateSlice f (-1)) S) / 2 := by
  rw [fourierCoeff, expect_fin_cons]
  simp_rw [monomial_insert_zero_tailFrequency_fin_cons,
    signValue_one, signValue_neg_one]
  rw [show (𝔼 x : (FABL.SignCube (n)),
      f (Fin.cons (-1) x) * (-1 * monomial S x)) =
        -(𝔼 x : (FABL.SignCube (n)), f (Fin.cons (-1) x) * monomial S x) by
      rw [← Finset.expect_neg_distrib]
      apply Finset.expect_congr rfl
      intro x _
      ring]
  simp [fourierCoeff, firstCoordinateSlice]
  ring

end FABL

end

/- Source fragment: FABL.Chapter04.KKL. Original licenses and source proofs retained. -/

section

/-
Copyright (c) 2026 Asher Yan. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Asher Yan with Codex
-/

/-!
# The Kahn--Kalai--Linial theorem

This module proves the KKL theorem stated after Proposition 4.13. The proof follows the
Edge-KKL argument deferred by the book to Section 9.6: the spectral Jensen lower bound for total
stable influence is combined with the `(2,4)` hypercontractive estimate.
-/

open Finset
open scoped BigOperators Real

namespace FABL

/-! ## Hypercontractive estimate for Edge-KKL -/

variable {n : ℕ}

-- Source: FABL.Chapter04.KKL:33
private theorem fourier_ext {f g : (FABL.SignCube (n)) → ℝ}
    (h : ∀ S, fourierCoeff f S = fourierCoeff g S) : f = g := by
  funext x
  rw [fourier_expansion f x, fourier_expansion g x]
  apply Finset.sum_congr rfl
  intro S _
  rw [h S]

-- Source: FABL.Chapter04.KKL:41
/-- The noise operator multiplies the Fourier coefficient at `S` by `ρ^|S|`. -/
theorem fourierCoeff_noiseOperator (rho : ℝ) (f : (FABL.SignCube (n)) → ℝ)
    (S : Finset (Fin n)) :
    fourierCoeff (noiseOperator rho f) S =
      rho ^ S.card * fourierCoeff f S := by
  rw [fourierCoeff]
  calc
    (𝔼 x, noiseOperator rho f x * monomial S x) =
        𝔼 x, (∑ T, rho ^ T.card * fourierCoeff f T * monomial T x) * monomial S x := by
      apply Finset.expect_congr rfl
      intro x _
      rw [noiseOperator_fourier_expansion]
    _ = 𝔼 x, ∑ T,
        (rho ^ T.card * fourierCoeff f T) * (monomial T x * monomial S x) := by
      apply Finset.expect_congr rfl
      intro x _
      rw [Finset.sum_mul]
      apply Finset.sum_congr rfl
      intro T _
      ring
    _ = ∑ T, (rho ^ T.card * fourierCoeff f T) *
        (𝔼 x, monomial T x * monomial S x) := by
      rw [Finset.expect_sum_comm]
      apply Finset.sum_congr rfl
      intro T _
      rw [← Finset.mul_expect]
    _ = rho ^ S.card * fourierCoeff f S := by
      simp_rw [expect_monomial_mul]
      simp

-- Source: FABL.Chapter04.KKL:71
/-- Noise operators form a multiplicative semigroup. -/
theorem noiseOperator_comp (rho sigma : ℝ) (f : (FABL.SignCube (n)) → ℝ) :
    noiseOperator rho (noiseOperator sigma f) = noiseOperator (rho * sigma) f := by
  apply fourier_ext
  intro S
  simp only [fourierCoeff_noiseOperator]
  rw [mul_pow]
  ring

-- Source: FABL.Chapter04.KKL:80
/-- The noise operator is self-adjoint for the uniform inner product. -/
theorem uniformInner_noiseOperator_left (rho : ℝ)
    (f g : (FABL.SignCube (n)) → ℝ) :
    (FABL.uniformInner (noiseOperator rho f) (g)) = (FABL.uniformInner (f) (noiseOperator rho g)) := by
  rw [plancherel, plancherel]
  simp_rw [fourierCoeff_noiseOperator]
  apply Finset.sum_congr rfl
  intro S _
  ring

-- Source: FABL.Chapter04.KKL:90
private noncomputable def firstCoordinateOddPart
    (f : (FABL.SignCube (n + 1)) → ℝ) : (FABL.SignCube (n)) → ℝ :=
  fun x ↦ (firstCoordinateSlice f 1 x - firstCoordinateSlice f (-1) x) / 2

-- Source: FABL.Chapter04.KKL:94
private noncomputable def firstCoordinateEvenPart
    (f : (FABL.SignCube (n + 1)) → ℝ) : (FABL.SignCube (n)) → ℝ :=
  fun x ↦ (firstCoordinateSlice f 1 x + firstCoordinateSlice f (-1) x) / 2

-- Source: FABL.Chapter04.KKL:98
private theorem fourierCoeff_firstCoordinateOddPart
    (f : (FABL.SignCube (n + 1)) → ℝ) (S : Finset (Fin n)) :
    fourierCoeff (firstCoordinateOddPart f) S =
      fourierCoeff f (insert 0 (tailFrequency S)) := by
  rw [fourierCoeff_insert_zero_tailFrequency]
  unfold firstCoordinateOddPart fourierCoeff
  rw [show (fun x ↦
      ((firstCoordinateSlice f 1 x - firstCoordinateSlice f (-1) x) / 2) * monomial S x) =
      fun x ↦
        (firstCoordinateSlice f 1 x * monomial S x -
          firstCoordinateSlice f (-1) x * monomial S x) / 2 by
    funext x
    ring]
  rw [← Finset.expect_div, Finset.expect_sub_distrib]

-- Source: FABL.Chapter04.KKL:113
private theorem fourierCoeff_firstCoordinateEvenPart
    (f : (FABL.SignCube (n + 1)) → ℝ) (S : Finset (Fin n)) :
    fourierCoeff (firstCoordinateEvenPart f) S =
      fourierCoeff f (tailFrequency S) := by
  rw [fourierCoeff_tailFrequency]
  unfold firstCoordinateEvenPart fourierCoeff
  rw [show (fun x ↦
      ((firstCoordinateSlice f 1 x + firstCoordinateSlice f (-1) x) / 2) * monomial S x) =
      fun x ↦
        (firstCoordinateSlice f 1 x * monomial S x +
          firstCoordinateSlice f (-1) x * monomial S x) / 2 by
    funext x
    ring]
  rw [← Finset.expect_div, Finset.expect_add_distrib]

-- Source: FABL.Chapter04.KKL:128
private theorem fourierCoeff_slice_eq_tail_add_sign_mul_insert
    (f : (FABL.SignCube (n + 1)) → ℝ) (b : Sign) (S : Finset (Fin n)) :
    fourierCoeff (firstCoordinateSlice f b) S =
      fourierCoeff f (tailFrequency S) +
        signValue b * fourierCoeff f (insert 0 (tailFrequency S)) := by
  have hmean := fourierCoeff_tailFrequency f S
  have hdiff := fourierCoeff_insert_zero_tailFrequency f S
  rcases Int.units_eq_one_or b with rfl | rfl
  · simp only [signValue_one, one_mul]
    linarith
  · simp only [signValue_neg_one, neg_one_mul]
    linarith

-- Source: FABL.Chapter04.KKL:141
private theorem noiseOperator_firstCoordinateSlice
    (rho : ℝ) (f : (FABL.SignCube (n + 1)) → ℝ) (b : Sign) :
    firstCoordinateSlice (noiseOperator rho f) b =
      fun x ↦
        signValue b * rho * noiseOperator rho (firstCoordinateOddPart f) x +
          noiseOperator rho (firstCoordinateEvenPart f) x := by
  apply fourier_ext
  intro S
  rw [fourierCoeff_slice_eq_tail_add_sign_mul_insert,
    fourierCoeff_noiseOperator, fourierCoeff_noiseOperator,
    card_tailFrequency, Finset.card_insert_of_notMem (zero_notMem_tailFrequency S),
    card_tailFrequency]
  unfold fourierCoeff
  rw [show (fun x ↦
      (signValue b * rho * noiseOperator rho (firstCoordinateOddPart f) x +
        noiseOperator rho (firstCoordinateEvenPart f) x) * monomial S x) =
      fun x ↦
        signValue b * rho *
            (noiseOperator rho (firstCoordinateOddPart f) x * monomial S x) +
          noiseOperator rho (firstCoordinateEvenPart f) x * monomial S x by
    funext x
    ring]
  rw [Finset.expect_add_distrib, ← Finset.mul_expect,
    ]
  change rho ^ S.card * fourierCoeff f (tailFrequency S) +
      signValue b * (rho ^ (S.card + 1) *
        fourierCoeff f (insert 0 (tailFrequency S))) =
    signValue b * rho *
        fourierCoeff (noiseOperator rho (firstCoordinateOddPart f)) S +
      fourierCoeff (noiseOperator rho (firstCoordinateEvenPart f)) S
  rw [fourierCoeff_noiseOperator, fourierCoeff_noiseOperator,
    fourierCoeff_firstCoordinateOddPart, fourierCoeff_firstCoordinateEvenPart,
    pow_succ]
  ring

-- Source: FABL.Chapter04.KKL:176
private noncomputable def kklNoiseRoot : ℝ := Real.sqrt (1 / 3 : ℝ)

-- Source: FABL.Chapter04.KKL:178
private theorem kklNoiseRoot_sq : kklNoiseRoot ^ 2 = (1 / 3 : ℝ) := by
  exact Real.sq_sqrt (by norm_num)

-- Source: FABL.Chapter04.KKL:181
private theorem expect_sq_nonneg (f : (FABL.SignCube (n)) → ℝ) :
    0 ≤ 𝔼 x, f x ^ 2 := by
  rw [Fintype.expect_eq_sum_div_card]
  positivity

-- Source: FABL.Chapter04.KKL:186
private theorem expect_fourth_nonneg (f : (FABL.SignCube (n)) → ℝ) :
    0 ≤ 𝔼 x, f x ^ 4 := by
  rw [Fintype.expect_eq_sum_div_card]
  positivity

-- Source: FABL.Chapter04.KKL:191
private theorem expect_sq_mul_sq_nonneg (d e : (FABL.SignCube (n)) → ℝ) :
    0 ≤ 𝔼 x, d x ^ 2 * e x ^ 2 := by
  rw [Fintype.expect_eq_sum_div_card]
  positivity

-- Source: FABL.Chapter04.KKL:196
private theorem fourthMoment_le_sq_of_slice
    (d e : (FABL.SignCube (n)) → ℝ) (f : (FABL.SignCube (n + 1)) → ℝ)
    (hf : ∀ b x, f (Fin.cons b x) = signValue b * d x + e x)
    (A B : ℝ) (hA : 0 ≤ A) (hB : 0 ≤ B)
    (hd : (𝔼 x, d x ^ 4) ≤ A ^ 2 / 9)
    (he : (𝔼 x, e x ^ 4) ≤ B ^ 2) :
    (𝔼 x, f x ^ 4) ≤ (A + B) ^ 2 := by
  let D₄ := 𝔼 x, d x ^ 4
  let E₄ := 𝔼 x, e x ^ 4
  let C := 𝔼 x, d x ^ 2 * e x ^ 2
  have hD₄ : 0 ≤ D₄ := expect_fourth_nonneg d
  have hE₄ : 0 ≤ E₄ := expect_fourth_nonneg e
  have hC : 0 ≤ C := expect_sq_mul_sq_nonneg d e
  have hCSq : C ^ 2 ≤ D₄ * E₄ := expect_sq_mul_sq_sq_le d e
  have hProduct : D₄ * E₄ ≤ (A * B / 3) ^ 2 := by
    calc
      D₄ * E₄ ≤ (A ^ 2 / 9) * B ^ 2 :=
        mul_le_mul hd he hE₄ (div_nonneg (sq_nonneg A) (by norm_num))
      _ = (A * B / 3) ^ 2 := by ring
  have hCross : C ≤ A * B / 3 :=
    (sq_le_sq₀ hC (div_nonneg (mul_nonneg hA hB) (by norm_num))).mp
      (hCSq.trans hProduct)
  rw [expect_fourth_eq_expect_odd_even d e f hf]
  change D₄ + 6 * C + E₄ ≤ (A + B) ^ 2
  change D₄ ≤ A ^ 2 / 9 at hd
  change E₄ ≤ B ^ 2 at he
  nlinarith [sq_nonneg A]

-- Source: FABL.Chapter04.KKL:224
private theorem expect_noiseOperator_kklNoiseRoot_fourth_le_sq_expect_sq
    (f : (FABL.SignCube (n)) → ℝ) :
    (𝔼 x, noiseOperator kklNoiseRoot f x ^ 4) ≤ (𝔼 x, f x ^ 2) ^ 2 := by
  induction n with
  | zero =>
      have hnoise : noiseOperator kklNoiseRoot f = f := by
        apply fourier_ext
        intro S
        rw [fourierCoeff_noiseOperator]
        have hS : S = ∅ := by
          apply Finset.eq_empty_iff_forall_notMem.mpr
          intro i
          exact Fin.elim0 i
        subst S
        simp
      rw [hnoise]
      let x₀ : (FABL.SignCube (0)) := fun i ↦ Fin.elim0 i
      have hf : f = fun _ ↦ f x₀ := by
        funext x
        rw [Subsingleton.elim x x₀]
      rw [hf]
      simp
      ring_nf
      exact le_rfl
  | succ n ih =>
      let d := firstCoordinateOddPart f
      let e := firstCoordinateEvenPart f
      let Td := noiseOperator kklNoiseRoot d
      let Te := noiseOperator kklNoiseRoot e
      have hslice (b : Sign) (x : (FABL.SignCube (n))) :
          noiseOperator kklNoiseRoot f (Fin.cons b x) =
            signValue b * (kklNoiseRoot * Td x) + Te x := by
        have h := congrFun (noiseOperator_firstCoordinateSlice kklNoiseRoot f b) x
        simpa [firstCoordinateSlice, d, e, Td, Te, mul_assoc] using h
      have hA : 0 ≤ 𝔼 x, d x ^ 2 := expect_sq_nonneg d
      have hB : 0 ≤ 𝔼 x, e x ^ 2 := expect_sq_nonneg e
      have hd : (𝔼 x, (kklNoiseRoot * Td x) ^ 4) ≤
          (𝔼 x, d x ^ 2) ^ 2 / 9 := by
        calc
          (𝔼 x, (kklNoiseRoot * Td x) ^ 4) =
              𝔼 x, kklNoiseRoot ^ 4 * Td x ^ 4 := by
            apply Finset.expect_congr rfl
            intro x _
            ring
          _ = kklNoiseRoot ^ 4 * (𝔼 x, Td x ^ 4) :=
            (Finset.mul_expect Finset.univ (fun x ↦ Td x ^ 4) (kklNoiseRoot ^ 4)).symm
          _ ≤ kklNoiseRoot ^ 4 * (𝔼 x, d x ^ 2) ^ 2 := by
            gcongr
            exact ih d
          _ = (𝔼 x, d x ^ 2) ^ 2 / 9 := by
            rw [show kklNoiseRoot ^ 4 = (kklNoiseRoot ^ 2) ^ 2 by ring,
              kklNoiseRoot_sq]
            ring
      have he : (𝔼 x, Te x ^ 4) ≤ (𝔼 x, e x ^ 2) ^ 2 := ih e
      apply (fourthMoment_le_sq_of_slice
        (fun x ↦ kklNoiseRoot * Td x) Te (noiseOperator kklNoiseRoot f)
        hslice (𝔼 x, d x ^ 2) (𝔼 x, e x ^ 2) hA hB hd he).trans_eq
      rw [expect_sq_eq_expect_odd_even d e f]
      intro b x
      dsimp [d, e, firstCoordinateOddPart, firstCoordinateEvenPart, firstCoordinateSlice]
      rcases Int.units_eq_one_or b with rfl | rfl <;> simp [signValue_one, signValue_neg_one] <;> ring

-- Source: FABL.Chapter04.KKL:286
private theorem expect_mul_fourth_le_expect_sq_cubed_mul_expect_fourth
    (g h : (FABL.SignCube (n)) → ℝ)
    (hg3 : ∀ x, g x ^ 3 = g x) (hg4 : ∀ x, g x ^ 4 = g x ^ 2) :
    (𝔼 x, g x * h x) ^ 4 ≤
      (𝔼 x, g x ^ 2) ^ 3 * (𝔼 x, h x ^ 4) := by
  let alpha := 𝔼 x, g x ^ 2
  let B := 𝔼 x, g x ^ 2 * h x ^ 2
  let H₄ := 𝔼 x, h x ^ 4
  have halpha : 0 ≤ alpha := expect_sq_nonneg g
  have hB : 0 ≤ B := by
    dsimp [B]
    rw [Fintype.expect_eq_sum_div_card]
    positivity
  have hH₄ : 0 ≤ H₄ := expect_fourth_nonneg h
  have hfirst := Finset.expect_mul_sq_le_sq_mul_sq
    (Finset.univ : Finset ((FABL.SignCube (n)))) (fun x ↦ g x ^ 2) (fun x ↦ g x * h x)
  have hfirstB : (𝔼 x, g x * h x) ^ 2 ≤ alpha * B := by
    calc
      (𝔼 x, g x * h x) ^ 2 =
          (𝔼 x, g x ^ 2 * (g x * h x)) ^ 2 := by
        congr 1
        apply Finset.expect_congr rfl
        intro x _
        rw [show g x ^ 2 * (g x * h x) = g x ^ 3 * h x by ring, hg3]
      _ ≤ (𝔼 x, (g x ^ 2) ^ 2) * 𝔼 x, (g x * h x) ^ 2 := hfirst
      _ = alpha * B := by
        congr 1
        · apply Finset.expect_congr rfl
          intro x _
          calc
            (g x ^ 2) ^ 2 = g x ^ 4 := by ring
            _ = g x ^ 2 := hg4 x
        · apply Finset.expect_congr rfl
          intro x _
          ring
  have hsecond := Finset.expect_mul_sq_le_sq_mul_sq
    (Finset.univ : Finset ((FABL.SignCube (n)))) g (fun x ↦ g x * h x ^ 2)
  have hrestricted : (𝔼 x, g x ^ 2 * h x ^ 4) ≤ H₄ := by
    apply Finset.expect_le_expect
    intro x _
    have heq : (g x ^ 2) ^ 2 = g x ^ 2 := by
      calc
        (g x ^ 2) ^ 2 = g x ^ 4 := by ring
        _ = g x ^ 2 := hg4 x
    have hg2 : g x ^ 2 ≤ 1 := by
      nlinarith [sq_nonneg (g x ^ 2 - 1)]
    exact mul_le_of_le_one_left (by positivity) hg2
  have hsecond' : B ^ 2 ≤ alpha * H₄ := by
    calc
      B ^ 2 = (𝔼 x, g x * (g x * h x ^ 2)) ^ 2 := by
        congr 1
        apply Finset.expect_congr rfl
        intro x _
        ring
      _ ≤ (𝔼 x, g x ^ 2) * 𝔼 x, (g x * h x ^ 2) ^ 2 := hsecond
      _ = alpha * (𝔼 x, g x ^ 2 * h x ^ 4) := by
        have hpoint :
            (fun x ↦ (g x * h x ^ 2) ^ 2) =
              (fun x ↦ g x ^ 2 * h x ^ 4) := by
          funext x
          ring
        change (𝔼 x, g x ^ 2) * (𝔼 x, (g x * h x ^ 2) ^ 2) =
          (𝔼 x, g x ^ 2) * (𝔼 x, g x ^ 2 * h x ^ 4)
        rw [hpoint]
      _ ≤ alpha * H₄ := mul_le_mul_of_nonneg_left hrestricted halpha
  calc
    (𝔼 x, g x * h x) ^ 4 = ((𝔼 x, g x * h x) ^ 2) ^ 2 := by ring
    _ ≤ (alpha * B) ^ 2 := by gcongr
    _ = alpha ^ 2 * B ^ 2 := by ring
    _ ≤ alpha ^ 2 * (alpha * H₄) := by gcongr
    _ = alpha ^ 3 * H₄ := by ring

-- Source: FABL.Chapter04.KKL:358
private theorem discreteDerivative_toReal_cube (f : BooleanFunction n) (i : Fin n)
    (x : (FABL.SignCube (n))) :
    discreteDerivative i f.toReal x ^ 3 = discreteDerivative i f.toReal x := by
  rcases Int.units_eq_one_or (f (setCoordinate x i 1)) with hp | hp <;>
    rcases Int.units_eq_one_or (f (setCoordinate x i (-1))) with hm | hm <;>
    norm_num [discreteDerivative_apply, BooleanFunction.toReal, signValue_one, signValue_neg_one, hp, hm]

-- Source: FABL.Chapter04.KKL:365
private theorem discreteDerivative_toReal_fourth (f : BooleanFunction n) (i : Fin n)
    (x : (FABL.SignCube (n))) :
    discreteDerivative i f.toReal x ^ 4 = discreteDerivative i f.toReal x ^ 2 := by
  rcases Int.units_eq_one_or (f (setCoordinate x i 1)) with hp | hp <;>
    rcases Int.units_eq_one_or (f (setCoordinate x i (-1))) with hm | hm <;>
    norm_num [discreteDerivative_apply, BooleanFunction.toReal, signValue_one, signValue_neg_one, hp, hm]

-- Source: FABL.Chapter04.KKL:372
/-- Corollary 9.12 at `ρ = 1 / 3`, specialized to a Boolean discrete derivative. -/
theorem stableInfluence_one_third_sq_le_booleanInfluence_cube
    (f : BooleanFunction n) (i : Fin n) :
    stableInfluence (1 / 3 : ℝ) f.toReal i ^ 2 ≤ booleanInfluence f i ^ 3 := by
  let g := discreteDerivative i f.toReal
  let u := noiseOperator kklNoiseRoot g
  let h := noiseOperator kklNoiseRoot u
  let A := stableInfluence (1 / 3 : ℝ) f.toReal i
  let alpha := influence f.toReal i
  have hthird : (1 / 3 : ℝ) ∈ Set.Icc (0 : ℝ) 1 := by norm_num
  have hthird' : (1 / 3 : ℝ) ∈ Set.Icc (-1 : ℝ) 1 := by norm_num
  have hrootProduct : kklNoiseRoot * kklNoiseRoot = (1 / 3 : ℝ) := by
    nlinarith [kklNoiseRoot_sq]
  have hsemigroup : h = noiseOperator (1 / 3 : ℝ) g := by
    dsimp [h, u]
    rw [noiseOperator_comp, hrootProduct]
  have hAinner : A = (FABL.uniformInner (g) (noiseOperator (1 / 3 : ℝ) g)) := by
    dsimp [A, g]
    rw [stableInfluence_eq_noiseStability_discreteDerivative (1 / 3 : ℝ) hthird,
      noiseStability_eq_uniformInner_noiseOperator (1 / 3 : ℝ) hthird']
  have hAexpect : A = 𝔼 x, g x * h x := by
    rw [hAinner, ← hsemigroup]
    simp only [uniformInner, RCLike.wInner_cWeight_eq_expect, RCLike.inner_apply,
      starRingEnd_apply, star_trivial]
    apply Finset.expect_congr rfl
    intro x _
    ring
  have huSq : (𝔼 x, u x ^ 2) = A := by
    calc
      (𝔼 x, u x ^ 2) = (FABL.uniformInner (u) (u)) := by
        simp only [uniformInner, RCLike.wInner_cWeight_eq_expect, RCLike.inner_apply,
          starRingEnd_apply, star_trivial]
        apply Finset.expect_congr rfl
        intro x _
        ring
      _ = (FABL.uniformInner (g) (h)) := by
        dsimp [u, h]
        exact uniformInner_noiseOperator_left kklNoiseRoot g
          (noiseOperator kklNoiseRoot g)
      _ = (FABL.uniformInner (g) (noiseOperator (1 / 3 : ℝ) g)) := by rw [← hsemigroup]
      _ = A := hAinner.symm
  have hhFourth : (𝔼 x, h x ^ 4) ≤ A ^ 2 := by
    calc
      (𝔼 x, h x ^ 4) ≤ (𝔼 x, u x ^ 2) ^ 2 := by
        exact expect_noiseOperator_kklNoiseRoot_fourth_le_sq_expect_sq u
      _ = A ^ 2 := by rw [huSq]
  have hA : 0 ≤ A := stableInfluence_nonneg (1 / 3 : ℝ) hthird f.toReal i
  have halpha : 0 ≤ alpha := influence_nonneg f.toReal i
  have hfourth : A ^ 4 ≤ alpha ^ 3 * A ^ 2 := by
    calc
      A ^ 4 = (𝔼 x, g x * h x) ^ 4 := by rw [hAexpect]
      _ ≤ (𝔼 x, g x ^ 2) ^ 3 * (𝔼 x, h x ^ 4) := by
        exact expect_mul_fourth_le_expect_sq_cubed_mul_expect_fourth g h
          (discreteDerivative_toReal_cube f i)
          (discreteDerivative_toReal_fourth f i)
      _ = alpha ^ 3 * (𝔼 x, h x ^ 4) := by rfl
      _ ≤ alpha ^ 3 * A ^ 2 := by gcongr
  have hresult : A ^ 2 ≤ alpha ^ 3 := by
    by_cases hAzero : A = 0
    · simpa [hAzero] using pow_nonneg halpha 3
    · have hApos : 0 < A := lt_of_le_of_ne hA (Ne.symm hAzero)
      have hA2pos : 0 < A ^ 2 := sq_pos_of_pos hApos
      by_contra hnot
      have hlt : alpha ^ 3 < A ^ 2 := lt_of_not_ge hnot
      have hmul : alpha ^ 3 * A ^ 2 < A ^ 2 * A ^ 2 :=
        mul_lt_mul_of_pos_right hlt hA2pos
      nlinarith [hfourth, hmul]
  simpa [A, alpha, booleanInfluence_eq_influence_toReal] using hresult

variable {n : ℕ}

end FABL

end

/- Source fragment: FABL.Chapter09.SmallSetExpansion. Original licenses and source proofs retained. -/

section

/-
Copyright (c) 2026 Asher Yan. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Asher Yan with Codex
-/

/-!
# Hypercontractivity and small subsets of the cube

Book items: equation (9.4), the `(2,4)`- and `(4/3,2)`-Hypercontractivity Theorems,
Corollaries 9.8 and 9.12, Example 9.9, Definition 9.10, Remark 9.11, equation (9.7),
and Exercises 9.6--9.7.
-/

open Finset
open scoped BigOperators Real

namespace FABL

variable {n : ℕ}

/-! ## The `(2,4)` theorem -/

/-! ## Duality across `2` -/

/-! ## Homogeneous functions -/

/-! ## Small sets and stable influences -/

-- Source: FABL.Chapter09.SmallSetExpansion:581
/-- O'Donnell, Corollary 9.12, written as `a * √a = a^{3/2}` to avoid introducing a
separate real-exponent convention for influence. -/
theorem stableInfluence_oneThird_le_booleanInfluence_mul_sqrt
    (f : BooleanFunction n) (i : Fin n) :
    stableInfluence (1 / 3 : ℝ) f.toReal i ≤
      booleanInfluence f i * Real.sqrt (booleanInfluence f i) := by
  let A := stableInfluence (1 / 3 : ℝ) f.toReal i
  let a := booleanInfluence f i
  have hA : 0 ≤ A := stableInfluence_nonneg (1 / 3 : ℝ) (by norm_num) f.toReal i
  have ha : 0 ≤ a := by
    dsimp only [a]
    rw [booleanInfluence_eq_influence_toReal]
    exact influence_nonneg f.toReal i
  have hsquare := stableInfluence_one_third_sq_le_booleanInfluence_cube f i
  have hrhs : 0 ≤ a * Real.sqrt a := mul_nonneg ha (Real.sqrt_nonneg _)
  apply (sq_le_sq₀ hA hrhs).1
  calc
    A ^ 2 ≤ a ^ 3 := hsquare
    _ = (a * Real.sqrt a) ^ 2 := by
      rw [mul_pow, Real.sq_sqrt ha]
      ring

/-! ## The stable hypercube graph -/

/-! ## The codimension-`k` subcube example -/

/-! ## Exercises 9.6--9.7 -/

end FABL

end

/- Source fragment: FABL.Chapter08.ProductFourierBases. Original licenses and source proofs retained. -/

section

/-
Copyright (c) 2026 Asher Yan. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Asher Yan with Codex
-/

/-!
# Fourier bases for finite product spaces

Book items: Definition 8.1, Example 8.2, Notation 8.3, Notation 8.4, Definition 8.5,
Fact 8.6, Definition 8.7, Example 8.8, Remark 8.9, Example 8.10, Definition 8.11,
Definition 8.12, Proposition 8.13, Definition 8.14, Example 8.15, and Exercises 8.2--8.5.

This module develops the weighted finite-product `L²` model used throughout Chapter 8. A
single-site Fourier basis has an arbitrary finite index type with a distinguished constant-one
index. Its product basis is constructed with Mathlib's finite-dimensional basis API, while all
probability calculations use the existing finite `PMF` expectation and independent-product law.
-/

open Finset
open scoped BigOperators RealInnerProductSpace

namespace FABL

/-! ## Finite full-support probability spaces -/

-- Source: FABL.Chapter08.ProductFourierBases:44
/-- O'Donnell, Definition 8.1: the product law `π⊗n` on `Ωⁿ`. -/
noncomputable def productProbabilityPMF
    {Ω : Type*} [Fintype Ω] (π : PMF Ω) (n : ℕ) :
    PMF (Fin n → Ω) :=
  independentProductPMF fun _ ↦ π

-- Source: FABL.Chapter08.ProductFourierBases:50
/-- The product law evaluates as the product of its coordinate masses. -/
 theorem productProbabilityPMF_apply
    {Ω : Type*} [Fintype Ω] (π : PMF Ω) (n : ℕ) (x : Fin n → Ω) :
    productProbabilityPMF π n x = ∏ i, π (x i) := by
  rfl

-- Source: FABL.Chapter08.ProductFourierBases:64
/-- The real function space denoted `L²(Ωⁿ, π⊗n)` in Definition 8.1. The probability law is
kept explicit because the same finite function type may be studied under several laws. -/
abbrev ProductL2 (Ω : Type*) (n : ℕ) := (Fin n → Ω) → ℝ

-- Source: FABL.Chapter08.ProductFourierBases:68
/-- The PMF-weighted real inner product `⟨f,g⟩ = 𝔼[f g]`. -/
noncomputable def pmfInner {Ω : Type*} [Fintype Ω]
    (π : PMF Ω) (f g : Ω → ℝ) : ℝ :=
  pmfExpectation π fun x ↦ f x * g x

-- Source: FABL.Chapter08.ProductFourierBases:73
/-- The weighted inner product is exactly the existing finite PMF expectation. -/
theorem pmfInner_eq_expect {Ω : Type*} [Fintype Ω]
    (π : PMF Ω) (f g : Ω → ℝ) :
    pmfInner π f g = pmfExpectation π (fun x ↦ f x * g x) := by
  rfl

-- Source: FABL.Chapter08.ProductFourierBases:112
/-- A weighted self-inner product is nonnegative. -/
theorem pmfInner_self_nonneg {Ω : Type*} [Fintype Ω]
    (π : PMF Ω) (f : Ω → ℝ) :
    0 ≤ pmfInner π f f := by
  rw [pmfInner_eq_expect]
  exact pmfExpectation_nonneg π fun x ↦ mul_self_nonneg (f x)

-- Source: FABL.Chapter08.ProductFourierBases:139
/-- The inner product on `L²(Ωⁿ,π⊗n)`. -/
noncomputable def productInner
    {Ω : Type*} [Fintype Ω] (π : PMF Ω) (n : ℕ)
    (f g : ProductL2 Ω n) : ℝ :=
  pmfInner (productProbabilityPMF π n) f g

/-! ## Indicator and Fourier bases -/

-- Source: FABL.Chapter08.ProductFourierBases:170
/-- O'Donnell, Definition 8.7: a single-site Fourier basis is an orthonormal basis whose
distinguished zero-indexed vector is the constant-one function. -/
structure FiniteFourierBasis
    (Ω : Type*) [Fintype Ω] [Nonempty Ω] (π : PMF Ω)
    (ι : Type*) [Fintype ι] [Nonempty ι] [DecidableEq ι] where
  /-- Index of the constant-one basis vector. -/
  zeroIndex : ι
  /-- The underlying algebraic basis. -/
  basis : Module.Basis ι ℝ (Ω → ℝ)
  /-- The zero-indexed basis vector is constant one. -/
  basis_zero : basis zeroIndex = fun _ ↦ 1
  /-- Orthonormality for the PMF-weighted inner product. -/
  orthonormal : ∀ a b,
    pmfExpectation π (fun x ↦ basis a x * basis b x) =
      if a = b then 1 else 0

-- Source: FABL.Chapter08.ProductFourierBases:186
/-- A finite family orthonormal for a PMF-weighted inner product is linearly independent. -/
theorem linearIndependent_of_pmf_orthonormal
    {Ω : Type*} [Fintype Ω] {π : PMF Ω}
    {ι : Type*} [Finite ι] [DecidableEq ι]
    (v : ι → Ω → ℝ)
    (horth : ∀ a b,
      pmfExpectation π (fun x ↦ v a x * v b x) = if a = b then 1 else 0) :
    LinearIndependent ℝ v := by
  classical
  letI := Fintype.ofFinite ι
  rw [Fintype.linearIndependent_iff]
  intro c hc a
  have hinner := congrArg
    (fun h : Ω → ℝ ↦ pmfExpectation π (fun x ↦ h x * v a x)) hc
  simp only [Finset.sum_apply, Pi.smul_apply, smul_eq_mul, Pi.zero_apply,
    zero_mul, pmfExpectation_const] at hinner
  rw [show (fun x ↦ (∑ i, c i * v i x) * v a x) =
      (fun x ↦ ∑ i, c i * (v i x * v a x)) by
    funext x
    rw [Finset.sum_mul]
    apply Finset.sum_congr rfl
    intro i _
    ring] at hinner
  rw [pmfExpectation_sum] at hinner
  simp_rw [pmfExpectation_const_mul, horth] at hinner
  simpa using hinner

/-! ## Existence of Fourier bases -/

/-! ## Multi-indices and product bases -/

-- Source: FABL.Chapter08.ProductFourierBases:310
/-- O'Donnell, Definition 8.11: an `n`-dimensional multi-index with entries in `ι`. -/
abbrev MultiIndex (n : ℕ) (ι : Type*) := Fin n → ι

-- Source: FABL.Chapter08.ProductFourierBases:313
/-- The support of a multi-index relative to a distinguished zero index. -/
def multiIndexSupport {n : ℕ} {ι : Type*} [DecidableEq ι]
    (zeroIndex : ι) (a : MultiIndex n ι) : Finset (Fin n) :=
  Finset.univ.filter fun i ↦ a i ≠ zeroIndex

-- Source: FABL.Chapter08.ProductFourierBases:330
/-- O'Donnell, Definition 8.12: product of the single-site Fourier functions indexed by a
multi-index. -/
noncomputable def FiniteFourierBasis.productFunction
    {Ω : Type*} [Fintype Ω] [Nonempty Ω] {π : PMF Ω}
    {ι : Type*} [Fintype ι] [Nonempty ι] [DecidableEq ι]
    (B : FiniteFourierBasis Ω π ι)
    {n : ℕ} (a : MultiIndex n ι) (x : Fin n → Ω) : ℝ :=
  ∏ i, B.basis (a i) (x i)

-- Source: FABL.Chapter08.ProductFourierBases:339
/-- The zero multi-index denotes the constant-one function. -/
 theorem FiniteFourierBasis.productFunction_zero
    {Ω : Type*} [Fintype Ω] [Nonempty Ω] {π : PMF Ω}
    {ι : Type*} [Fintype ι] [Nonempty ι] [DecidableEq ι]
    (B : FiniteFourierBasis Ω π ι) {n : ℕ} (x : Fin n → Ω) :
    B.productFunction (fun _ ↦ B.zeroIndex) x = 1 := by
  simp [FiniteFourierBasis.productFunction, B.basis_zero]

-- Source: FABL.Chapter08.ProductFourierBases:347
/-- Proposition 8.13, orthonormality part: products of single-site Fourier functions are
orthonormal under the product law. -/
theorem FiniteFourierBasis.productFunction_orthonormal
    {Ω : Type*} [Fintype Ω] [Nonempty Ω] {π : PMF Ω}
    {ι : Type*} [Fintype ι] [Nonempty ι] [DecidableEq ι]
    (B : FiniteFourierBasis Ω π ι)
    {n : ℕ} (a b : MultiIndex n ι) :
    pmfExpectation (productProbabilityPMF π n)
      (fun x ↦ B.productFunction a x * B.productFunction b x) =
        if a = b then 1 else 0 := by
  classical
  rw [show (fun x ↦ B.productFunction a x * B.productFunction b x) =
      (fun x ↦ ∏ i, B.basis (a i) (x i) * B.basis (b i) (x i)) by
    funext x
    simp only [FiniteFourierBasis.productFunction]
    exact (Finset.prod_mul_distrib ..).symm]
  rw [productProbabilityPMF,
    pmfExpectation_independentProductPMF_prod
      (fun _ : Fin n ↦ π)
      (fun i x ↦ B.basis (a i) x * B.basis (b i) x)]
  simp_rw [B.orthonormal]
  by_cases h : a = b
  · subst b
    simp
  · simp only [if_false, h]
    obtain ⟨i, hi⟩ : ∃ i, a i ≠ b i := by
      simpa [Function.ne_iff] using h
    exact Finset.prod_eq_zero (Finset.mem_univ i) (by simp [hi])

-- Source: FABL.Chapter08.ProductFourierBases:376
/-- An orthonormal finite family is linearly independent; this is the linear-independence step
in Proposition 8.13. -/
theorem FiniteFourierBasis.productFunction_linearIndependent
    {Ω : Type*} [Fintype Ω] [Nonempty Ω] {π : PMF Ω}
    {ι : Type*} [Fintype ι] [Nonempty ι] [DecidableEq ι]
    (B : FiniteFourierBasis Ω π ι) (n : ℕ) :
    LinearIndependent ℝ (B.productFunction (n := n)) := by
  classical
  rw [Fintype.linearIndependent_iff]
  intro c hc a
  have hinner := congrArg
    (fun h : (Fin n → Ω) → ℝ ↦
      pmfExpectation (productProbabilityPMF π n)
        (fun x ↦ h x * B.productFunction a x)) hc
  simp only [Finset.sum_apply, Pi.smul_apply, smul_eq_mul, Pi.zero_apply,
    zero_mul, pmfExpectation_const] at hinner
  rw [show (fun x ↦ (∑ i, c i * B.productFunction i x) * B.productFunction a x) =
      (fun x ↦ ∑ i, c i *
        (B.productFunction i x * B.productFunction a x)) by
    funext x
    rw [Finset.sum_mul]
    apply Finset.sum_congr rfl
    intro i _
    ring] at hinner
  rw [pmfExpectation_sum] at hinner
  simp_rw [pmfExpectation_const_mul, B.productFunction_orthonormal] at hinner
  simpa using hinner

-- Source: FABL.Chapter08.ProductFourierBases:404
/-- O'Donnell, Proposition 8.13: the product functions form a basis of the full product
function space. -/
noncomputable def FiniteFourierBasis.productBasis
    {Ω : Type*} [Fintype Ω] [Nonempty Ω] {π : PMF Ω}
    {ι : Type*} [Fintype ι] [Nonempty ι] [DecidableEq ι]
    (B : FiniteFourierBasis Ω π ι) (n : ℕ) :
    Module.Basis (MultiIndex n ι) ℝ (ProductL2 Ω n) := by
  classical
  apply basisOfLinearIndependentOfCardEqFinrank (B.productFunction_linearIndependent n)
  have hcard : Fintype.card ι = Fintype.card Ω := by
    simpa [Module.finrank_fintype_fun_eq_card] using
      (Module.finrank_eq_card_basis B.basis).symm
  simp [Module.finrank_fintype_fun_eq_card, hcard]

-- Source: FABL.Chapter08.ProductFourierBases:418
/-- The product basis evaluates to the defining product function. -/
 theorem FiniteFourierBasis.productBasis_apply
    {Ω : Type*} [Fintype Ω] [Nonempty Ω] {π : PMF Ω}
    {ι : Type*} [Fintype ι] [Nonempty ι] [DecidableEq ι]
    (B : FiniteFourierBasis Ω π ι) (n : ℕ) (a : MultiIndex n ι) :
    B.productBasis n a = B.productFunction a := by
  classical
  simp [FiniteFourierBasis.productBasis]

/-! ## Fourier coefficients and expansion -/

-- Source: FABL.Chapter08.ProductFourierBases:429
/-- O'Donnell, Definition 8.14: Fourier coefficient on a product-basis multi-index. -/
noncomputable def FiniteFourierBasis.fourierCoeff
    {Ω : Type*} [Fintype Ω] [Nonempty Ω] {π : PMF Ω}
    {ι : Type*} [Fintype ι] [Nonempty ι] [DecidableEq ι]
    (B : FiniteFourierBasis Ω π ι) {n : ℕ}
    (f : ProductL2 Ω n) (a : MultiIndex n ι) : ℝ :=
  pmfExpectation (productProbabilityPMF π n)
    (fun x ↦ f x * B.productFunction a x)

-- Source: FABL.Chapter08.ProductFourierBases:449
/-- Exercise 8.3 and Definition 8.14: weighted-inner-product coefficients coincide with the
algebraic coordinates of the product basis. -/
theorem FiniteFourierBasis.fourierCoeff_eq_productBasis_repr
    {Ω : Type*} [Fintype Ω] [Nonempty Ω] {π : PMF Ω}
    {ι : Type*} [Fintype ι] [Nonempty ι] [DecidableEq ι]
    (B : FiniteFourierBasis Ω π ι) {n : ℕ}
    (f : ProductL2 Ω n) (a : MultiIndex n ι) :
    B.fourierCoeff f a = (B.productBasis n).repr f a := by
  classical
  let c : MultiIndex n ι → ℝ := fun b ↦ (B.productBasis n).repr f b
  have hrepr : (∑ b, c b • B.productFunction b) = f := by
    simpa only [c, B.productBasis_apply] using (B.productBasis n).sum_repr f
  have hinner := congrArg
    (fun h : ProductL2 Ω n ↦
      pmfExpectation (productProbabilityPMF π n)
        (fun x ↦ h x * B.productFunction a x)) hrepr
  simp only [Finset.sum_apply, Pi.smul_apply, smul_eq_mul] at hinner
  rw [show (fun x ↦ (∑ b, c b * B.productFunction b x) * B.productFunction a x) =
      (fun x ↦ ∑ b, c b *
        (B.productFunction b x * B.productFunction a x)) by
    funext x
    rw [Finset.sum_mul]
    apply Finset.sum_congr rfl
    intro b _
    ring] at hinner
  rw [pmfExpectation_sum] at hinner
  simp_rw [pmfExpectation_const_mul, B.productFunction_orthonormal] at hinner
  simpa [FiniteFourierBasis.fourierCoeff, c] using hinner.symm

-- Source: FABL.Chapter08.ProductFourierBases:478
/-- O'Donnell, Definition 8.14: every function has its product Fourier expansion. -/
theorem FiniteFourierBasis.fourier_expansion
    {Ω : Type*} [Fintype Ω] [Nonempty Ω] {π : PMF Ω}
    {ι : Type*} [Fintype ι] [Nonempty ι] [DecidableEq ι]
    (B : FiniteFourierBasis Ω π ι) {n : ℕ}
    (f : ProductL2 Ω n) (x : Fin n → Ω) :
    f x = ∑ a, B.fourierCoeff f a * B.productFunction a x := by
  classical
  have h := congrFun ((B.productBasis n).sum_repr f) x
  simp only [Finset.sum_apply, Pi.smul_apply, smul_eq_mul,
    B.productBasis_apply] at h
  rw [← h]
  apply Finset.sum_congr rfl
  intro a _
  rw [B.fourierCoeff_eq_productBasis_repr]

-- Source: FABL.Chapter08.ProductFourierBases:494
/-- The coefficients in the product Fourier expansion are unique. -/
theorem FiniteFourierBasis.fourier_expansion_unique
    {Ω : Type*} [Fintype Ω] [Nonempty Ω] {π : PMF Ω}
    {ι : Type*} [Fintype ι] [Nonempty ι] [DecidableEq ι]
    (B : FiniteFourierBasis Ω π ι) {n : ℕ}
    (f : ProductL2 Ω n) (c : MultiIndex n ι → ℝ)
    (hc : ∀ x, f x = ∑ a, c a * B.productFunction a x) :
    c = B.fourierCoeff f := by
  classical
  funext a
  have hfun : (∑ b, c b • B.productFunction b) = f := by
    funext x
    simp [hc x]
  have hfunBasis : (∑ b, c b • B.productBasis n b) = f := by
    simpa only [B.productBasis_apply] using hfun
  have hrepr := (B.productBasis n).repr_sum_self c
  rw [hfunBasis] at hrepr
  have hcoord := congrFun hrepr a
  rw [B.fourierCoeff_eq_productBasis_repr]
  exact hcoord.symm

/-! ## The uniform sign cube -/

-- Source: FABL.Chapter08.ProductFourierBases:517
/-- An explicit enumeration of the two signs, used only to discharge finite example
computations. -/
def finTwoSignEquiv : Fin 2 ≃ Sign where
  toFun i := if i = 0 then -1 else 1
  invFun x := if x = -1 then 0 else 1
  left_inv i := by
    fin_cases i <;> simp
  right_inv x := by
    rcases Int.units_eq_one_or x with rfl | rfl <;> simp

-- Source: FABL.Chapter08.ProductFourierBases:527
/-- The two single-site Fourier functions on a uniformly random sign. -/
def signSiteFourierFunction (j : Fin 2) (x : Sign) : ℝ :=
  if j = 0 then 1 else signValue x

-- Source: FABL.Chapter08.ProductFourierBases:531
/-- The constant function and the sign function are orthonormal under the uniform sign law. -/
theorem signSiteFourierFunction_orthonormal (a b : Fin 2) :
    pmfExpectation (uniformPMF Sign)
      (fun x ↦ signSiteFourierFunction a x * signSiteFourierFunction b x) =
        if a = b then 1 else 0 := by
  rw [pmfExpectation_uniformPMF_eq_expect]
  calc
    (𝔼 x : Sign, signSiteFourierFunction a x * signSiteFourierFunction b x) =
        𝔼 i : Fin 2,
          signSiteFourierFunction a (finTwoSignEquiv i) *
            signSiteFourierFunction b (finTwoSignEquiv i) := by
      symm
      apply Fintype.expect_equiv finTwoSignEquiv
      intro i
      rfl
    _ = if a = b then 1 else 0 := by
      fin_cases a <;> fin_cases b <;>
        norm_num [Fintype.expect_eq_sum_div_card, signSiteFourierFunction,
          finTwoSignEquiv, signValue]

-- Source: FABL.Chapter08.ProductFourierBases:551
/-- The single-site Fourier basis for a uniformly random sign. -/
noncomputable def signSiteBasis : Module.Basis (Fin 2) ℝ (Sign → ℝ) := by
  classical
  apply basisOfLinearIndependentOfCardEqFinrank
    (linearIndependent_of_pmf_orthonormal signSiteFourierFunction
      signSiteFourierFunction_orthonormal)
  simp [Module.finrank_fintype_fun_eq_card, Sign]

-- Source: FABL.Chapter08.ProductFourierBases:559
/-- The sign-site basis evaluates as the explicit constant/sign family. -/
 theorem signSiteBasis_apply (j : Fin 2) :
    signSiteBasis j = signSiteFourierFunction j := by
  classical
  simp [signSiteBasis]

-- Source: FABL.Chapter08.ProductFourierBases:565
/-- O'Donnell, Example 8.8: the single-site Fourier basis for the uniform sign law. -/
noncomputable def signSiteFourierBasis :
    FiniteFourierBasis Sign (uniformPMF Sign) (Fin 2) where
  zeroIndex := 0
  basis := signSiteBasis
  basis_zero := by
    funext x
    simp [signSiteBasis_apply, signSiteFourierFunction]
  orthonormal := by
    intro a b
    simpa only [signSiteBasis_apply] using signSiteFourierFunction_orthonormal a b

-- Source: FABL.Chapter08.ProductFourierBases:577
/-- The subset of coordinates where a binary multi-index is nonzero. -/
def signMultiIndexSupport {n : ℕ} (a : MultiIndex n (Fin 2)) : Finset (Fin n) :=
  multiIndexSupport (0 : Fin 2) a

-- Source: FABL.Chapter08.ProductFourierBases:581
/-- A binary-indexed product Fourier function is the usual sign-cube parity monomial. -/
theorem signSiteFourierBasis_productFunction_eq_monomial
    {n : ℕ} (a : MultiIndex n (Fin 2)) (x : (FABL.SignCube (n))) :
    signSiteFourierBasis.productFunction a x = monomial (signMultiIndexSupport a) x := by
  classical
  rw [FiniteFourierBasis.productFunction, monomial]
  calc
    (∏ i, signSiteFourierBasis.basis (a i) (x i)) =
        ∏ i, if i ∈ signMultiIndexSupport a then signValue (x i) else 1 := by
      apply Finset.prod_congr rfl
      intro i _
      by_cases hi : a i = 0
      · simp [signSiteFourierBasis, signSiteBasis, signSiteFourierFunction,
          signMultiIndexSupport, multiIndexSupport, hi]
      · have hai : a i = 1 := Fin.eq_one_of_ne_zero (a i) hi
        simp [signSiteFourierBasis, signSiteBasis, signSiteFourierFunction,
          signMultiIndexSupport, multiIndexSupport, hai]
    _ = ∏ i ∈ signMultiIndexSupport a, signValue (x i) := by
      exact Fintype.prod_ite_mem _ _

end FABL

end

/- Source fragment: FABL.Chapter08.GeneralizedFourierFormulas. Original licenses and source proofs retained. -/

section

/-
Copyright (c) 2026 Asher Yan. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Asher Yan with Codex
-/

/-!
# Generalized Fourier formulas

Book items: Proposition 8.16, Definition 8.17, Remark 8.18, Proposition 8.19,
Corollaries 8.20--8.21, Definition 8.22, Propositions 8.23--8.24, Example 8.25,
Definitions 8.26--8.27, Propositions 8.28 and 8.31, Remark 8.29, Definition 8.30,
Definition 8.32, Proposition 8.33, and Exercises 8.6--8.13.

The constructions in this module are basis-free whenever the book's mathematics is basis-free:
coordinate projection, coordinate Laplacian, influence, product noise, stability, and degree are
defined from the finite PMF model. A `FiniteFourierBasis` is then used to prove their spectral
formulas and independence from the chosen basis. The final section records explicit compatibility
with FABL's canonical uniform sign-cube APIs from Chapters 1 and 2.
-/

open Finset
open scoped BigOperators

namespace FABL

variable {n : ℕ}

/-! ## Moments and Proposition 8.16 -/

-- Source: FABL.Chapter08.GeneralizedFourierFormulas:37
/-- The zero multi-index of a single-site Fourier basis. -/
def FiniteFourierBasis.zeroMultiIndex
    {Ω : Type*} [Fintype Ω] [Nonempty Ω] {π : PMF Ω}
    {ι : Type*} [Fintype ι] [Nonempty ι] [DecidableEq ι]
    (B : FiniteFourierBasis Ω π ι) (n : ℕ) : MultiIndex n ι :=
  fun _ ↦ B.zeroIndex

-- Source: FABL.Chapter08.GeneralizedFourierFormulas:44
/-- Mean under a finite product law. -/
noncomputable def productMean
    {Ω : Type*} [Fintype Ω] (π : PMF Ω) {n : ℕ}
    (f : ProductL2 Ω n) : ℝ :=
  pmfExpectation (productProbabilityPMF π n) f

-- Source: FABL.Chapter08.GeneralizedFourierFormulas:87
/-- PMF expectation preserves addition in the pointwise function module. -/
theorem pmfExpectation_add_fun
    {Ω : Type*} [Fintype Ω] (π : PMF Ω) (f g : Ω → ℝ) :
    pmfExpectation π (f + g) = pmfExpectation π f + pmfExpectation π g := by
  change pmfExpectation π (fun x ↦ f x + g x) = _
  exact pmfExpectation_add _ _ _

-- Source: FABL.Chapter08.GeneralizedFourierFormulas:94
/-- PMF expectation preserves scalar multiplication in the pointwise function module. -/
theorem pmfExpectation_smul_fun
    {Ω : Type*} [Fintype Ω] (π : PMF Ω) (c : ℝ) (f : Ω → ℝ) :
    pmfExpectation π (c • f) = c * pmfExpectation π f := by
  change pmfExpectation π (fun x ↦ c * f x) = _
  exact pmfExpectation_const_mul _ _ _

-- Source: FABL.Chapter08.GeneralizedFourierFormulas:174
/-- The product Fourier coefficient at the zero multi-index is the mean. -/
theorem FiniteFourierBasis.fourierCoeff_zeroMultiIndex
    {Ω : Type*} [Fintype Ω] [Nonempty Ω] {π : PMF Ω}
    {ι : Type*} [Fintype ι] [Nonempty ι] [DecidableEq ι]
    (B : FiniteFourierBasis Ω π ι) {n : ℕ}
    (f : ProductL2 Ω n) :
    B.fourierCoeff f (B.zeroMultiIndex n) = productMean π f := by
  unfold FiniteFourierBasis.fourierCoeff productMean
  apply congrArg (pmfExpectation (productProbabilityPMF π n))
  funext x
  change f x * B.productFunction (fun _ ↦ B.zeroIndex) x = f x
  rw [B.productFunction_zero, mul_one]

-- Source: FABL.Chapter08.GeneralizedFourierFormulas:224
/-- Proposition 8.16, Plancherel: the weighted product inner product is the dot product of
Fourier coefficients. -/
theorem FiniteFourierBasis.plancherel
    {Ω : Type*} [Fintype Ω] [Nonempty Ω] {π : PMF Ω}
    {ι : Type*} [Fintype ι] [Nonempty ι] [DecidableEq ι]
    (B : FiniteFourierBasis Ω π ι) {n : ℕ}
    (f g : ProductL2 Ω n) :
    productInner π n f g = ∑ a, B.fourierCoeff f a * B.fourierCoeff g a := by
  classical
  unfold productInner
  rw [pmfInner_eq_expect]
  calc
    pmfExpectation (productProbabilityPMF π n) (fun x ↦ f x * g x) =
        pmfExpectation (productProbabilityPMF π n)
          (fun x ↦ (∑ a, B.fourierCoeff f a * B.productFunction a x) * g x) := by
      apply congrArg (pmfExpectation (productProbabilityPMF π n))
      funext x
      rw [← B.fourier_expansion f x]
    _ = pmfExpectation (productProbabilityPMF π n)
        (fun x ↦ ∑ a, B.fourierCoeff f a *
          (g x * B.productFunction a x)) := by
      apply congrArg (pmfExpectation (productProbabilityPMF π n))
      funext x
      rw [Finset.sum_mul]
      apply Finset.sum_congr rfl
      intro a _
      ring
    _ = ∑ a, B.fourierCoeff f a * B.fourierCoeff g a := by
      rw [pmfExpectation_sum]
      apply Finset.sum_congr rfl
      intro a _
      rw [pmfExpectation_const_mul]
      rfl

/-! ## Coordinate projections -/

-- Source: FABL.Chapter08.GeneralizedFourierFormulas:345
/-- Combine the retained coordinates of `x` on `J` with fresh coordinates from `y` outside
`J`. -/
def mergeOnCoordinates
    {Ω : Type*} {n : ℕ} (J : Finset (Fin n))
    (x y : Fin n → Ω) : Fin n → Ω :=
  fun i ↦ if i ∈ J then x i else y i

-- Source: FABL.Chapter08.GeneralizedFourierFormulas:352
/-- A function depends only on coordinates in `J` when agreeing on `J` forces equal outputs. -/
def DependsOnlyOnCoordinates
    {Ω : Type*} {n : ℕ} (f : ProductL2 Ω n) (J : Finset (Fin n)) : Prop :=
  ∀ ⦃x y⦄, (∀ i ∈ J, x i = y i) → f x = f y

-- Source: FABL.Chapter08.GeneralizedFourierFormulas:357
/-- O'Donnell, Definition 8.17: projection onto the coordinates `J`, obtained by rerandomizing
all coordinates outside `J`. -/
noncomputable def projectOnCoordinates
    {Ω : Type*} [Fintype Ω] (π : PMF Ω) {n : ℕ}
    (J : Finset (Fin n)) (f : ProductL2 Ω n) : ProductL2 Ω n :=
  fun x ↦ pmfExpectation (productProbabilityPMF π n)
    (fun y ↦ f (mergeOnCoordinates J x y))

-- Source: FABL.Chapter08.GeneralizedFourierFormulas:376
/-- Projection respects scalar multiplication. -/
theorem projectOnCoordinates_smul
    {Ω : Type*} [Fintype Ω] (π : PMF Ω) {n : ℕ}
    (J : Finset (Fin n)) (c : ℝ) (f : ProductL2 Ω n) :
    projectOnCoordinates π J (c • f) =
      c • projectOnCoordinates π J f := by
  funext x
  unfold projectOnCoordinates
  simp only [Pi.smul_apply, smul_eq_mul]
  exact pmfExpectation_const_mul _ _ _

-- Source: FABL.Chapter08.GeneralizedFourierFormulas:387
/-- Projection commutes with a finite sum. -/
theorem projectOnCoordinates_sum
    {Ω κ : Type*} [Fintype Ω] [Fintype κ] (π : PMF Ω) {n : ℕ}
    (J : Finset (Fin n)) (f : κ → ProductL2 Ω n) :
    projectOnCoordinates π J (∑ k, f k) =
      ∑ k, projectOnCoordinates π J (f k) := by
  funext x
  unfold projectOnCoordinates
  rw [show (fun y ↦ (∑ k, f k) (mergeOnCoordinates J x y)) =
      (fun y ↦ ∑ k, f k (mergeOnCoordinates J x y)) by
    funext y
    simp]
  rw [pmfExpectation_sum]
  simp only [Finset.sum_apply]

-- Source: FABL.Chapter08.GeneralizedFourierFormulas:402
/-- The output of coordinate projection depends only on retained coordinates. -/
theorem projectOnCoordinates_dependsOnly
    {Ω : Type*} [Fintype Ω] (π : PMF Ω) {n : ℕ}
    (J : Finset (Fin n)) (f : ProductL2 Ω n) :
    DependsOnlyOnCoordinates (projectOnCoordinates π J f) J := by
  intro x z hxz
  unfold projectOnCoordinates
  congr 1
  funext y
  congr 1
  funext i
  by_cases hi : i ∈ J
  · simp [mergeOnCoordinates, hi, hxz i hi]
  · simp [mergeOnCoordinates, hi]

-- Source: FABL.Chapter08.GeneralizedFourierFormulas:417
/-- Projection fixes every function already depending only on the retained coordinates. -/
theorem projectOnCoordinates_eq_self_of_dependsOnly
    {Ω : Type*} [Fintype Ω] (π : PMF Ω) {n : ℕ}
    {J : Finset (Fin n)} {f : ProductL2 Ω n}
    (hf : DependsOnlyOnCoordinates f J) :
    projectOnCoordinates π J f = f := by
  funext x
  unfold projectOnCoordinates
  have hpoint : (fun y ↦ f (mergeOnCoordinates J x y)) = fun _ ↦ f x := by
    funext y
    apply hf
    intro i hi
    simp [mergeOnCoordinates, hi]
  rw [hpoint, pmfExpectation_const]

-- Source: FABL.Chapter08.GeneralizedFourierFormulas:432
/-- The mean of a single-site Fourier basis function. -/
theorem FiniteFourierBasis.expect_basis
    {Ω : Type*} [Fintype Ω] [Nonempty Ω] {π : PMF Ω}
    {ι : Type*} [Fintype ι] [Nonempty ι] [DecidableEq ι]
    (B : FiniteFourierBasis Ω π ι) (a : ι) :
    pmfExpectation π (B.basis a) = if a = B.zeroIndex then 1 else 0 := by
  have horth := B.orthonormal a B.zeroIndex
  rw [B.basis_zero] at horth
  simpa using horth

-- Source: FABL.Chapter08.GeneralizedFourierFormulas:442
/-- A multi-index support is contained in `J` exactly when every coordinate outside `J` has
the distinguished zero index. -/
theorem multiIndexSupport_subset_iff
    {n : ℕ} {ι : Type*} [DecidableEq ι]
    (zeroIndex : ι) (a : MultiIndex n ι) (J : Finset (Fin n)) :
    multiIndexSupport zeroIndex a ⊆ J ↔
      ∀ i, i ∉ J → a i = zeroIndex := by
  constructor
  · intro h i hi
    by_contra hai
    have hisupport : i ∈ multiIndexSupport zeroIndex a := by
      simp [multiIndexSupport, hai]
    exact hi (h hisupport)
  · intro h i hi
    have hai : a i ≠ zeroIndex := by
      simpa [multiIndexSupport] using hi
    by_contra hiJ
    exact hai (h i hiJ)

-- Source: FABL.Chapter08.GeneralizedFourierFormulas:461
/-- Proposition 8.19 on one basis vector: projection keeps precisely the product functions whose
support lies in the retained coordinate set. -/
theorem FiniteFourierBasis.projectOnCoordinates_productFunction
    {Ω : Type*} [Fintype Ω] [Nonempty Ω] {π : PMF Ω}
    {ι : Type*} [Fintype ι] [Nonempty ι] [DecidableEq ι]
    (B : FiniteFourierBasis Ω π ι) {n : ℕ}
    (J : Finset (Fin n)) (a : MultiIndex n ι) :
    projectOnCoordinates π J (B.productFunction a) =
      if multiIndexSupport B.zeroIndex a ⊆ J then B.productFunction a else 0 := by
  classical
  funext x
  unfold projectOnCoordinates
  rw [show (fun y ↦ B.productFunction a (mergeOnCoordinates J x y)) =
      (fun y ↦ ∏ i,
        if i ∈ J then B.basis (a i) (x i) else B.basis (a i) (y i)) by
    funext y
    simp only [FiniteFourierBasis.productFunction]
    apply Finset.prod_congr rfl
    intro i _
    by_cases hi : i ∈ J <;> simp [mergeOnCoordinates, hi]]
  rw [productProbabilityPMF,
    pmfExpectation_independentProductPMF_prod
      (fun _ : Fin n ↦ π)
      (fun i y ↦ if i ∈ J then B.basis (a i) (x i) else B.basis (a i) y)]
  simp_rw [show ∀ i, pmfExpectation π
      (fun y ↦ if i ∈ J then B.basis (a i) (x i) else B.basis (a i) y) =
      if i ∈ J then B.basis (a i) (x i)
      else if a i = B.zeroIndex then 1 else 0 by
    intro i
    by_cases hi : i ∈ J
    · simp [hi, pmfExpectation_const]
    · simp [hi, B.expect_basis]]
  by_cases hsupport : multiIndexSupport B.zeroIndex a ⊆ J
  · rw [if_pos hsupport]
    have houtside := (multiIndexSupport_subset_iff B.zeroIndex a J).mp hsupport
    simp only [FiniteFourierBasis.productFunction]
    apply Finset.prod_congr rfl
    intro i _
    by_cases hi : i ∈ J
    · simp [hi]
    · simp [hi, houtside i hi, B.basis_zero]
  · rw [if_neg hsupport]
    obtain ⟨i, hiSupport, hiJ⟩ := Finset.not_subset.mp hsupport
    have hai : a i ≠ B.zeroIndex := (Finset.mem_filter.mp hiSupport).2
    exact Finset.prod_eq_zero (Finset.mem_univ i) (by simp [hiJ, hai])

-- Source: FABL.Chapter08.GeneralizedFourierFormulas:507
/-- Proposition 8.19: projection filters the Fourier expansion by support. -/
theorem FiniteFourierBasis.projectOnCoordinates_fourier_expansion
    {Ω : Type*} [Fintype Ω] [Nonempty Ω] {π : PMF Ω}
    {ι : Type*} [Fintype ι] [Nonempty ι] [DecidableEq ι]
    (B : FiniteFourierBasis Ω π ι) {n : ℕ}
    (J : Finset (Fin n)) (f : ProductL2 Ω n) (x : Fin n → Ω) :
    projectOnCoordinates π J f x =
      ∑ a with multiIndexSupport B.zeroIndex a ⊆ J,
        B.fourierCoeff f a * B.productFunction a x := by
  classical
  have hf : f = ∑ a, B.fourierCoeff f a • B.productFunction a := by
    funext y
    simpa only [Finset.sum_apply, Pi.smul_apply, smul_eq_mul] using
      B.fourier_expansion f y
  calc
    projectOnCoordinates π J f x =
        projectOnCoordinates π J
          (∑ a, B.fourierCoeff f a • B.productFunction a) x := by
      exact congrArg (fun h : ProductL2 Ω n ↦ projectOnCoordinates π J h x) hf
    _ = (∑ a, projectOnCoordinates π J
        (B.fourierCoeff f a • B.productFunction a)) x := by
      rw [projectOnCoordinates_sum]
    _ = (∑ a, B.fourierCoeff f a •
        projectOnCoordinates π J (B.productFunction a)) x := by
      have hsum :
          (∑ a, projectOnCoordinates π J
              (B.fourierCoeff f a • B.productFunction a)) =
            ∑ a, B.fourierCoeff f a •
              projectOnCoordinates π J (B.productFunction a) := by
        apply Finset.sum_congr rfl
        intro a _
        rw [projectOnCoordinates_smul]
      exact congrFun hsum x
    _ = ∑ a with multiIndexSupport B.zeroIndex a ⊆ J,
        B.fourierCoeff f a * B.productFunction a x := by
      simp_rw [B.projectOnCoordinates_productFunction]
      simp only [Finset.sum_apply, Pi.smul_apply, smul_eq_mul, ite_apply,
        Pi.zero_apply]
      rw [Finset.sum_filter]
      apply Finset.sum_congr rfl
      intro a _
      by_cases ha : multiIndexSupport B.zeroIndex a ⊆ J <;> simp [ha]

-- Source: FABL.Chapter08.GeneralizedFourierFormulas:550
/-- The coefficient of a projection is retained exactly on supported multi-indices. -/
theorem FiniteFourierBasis.fourierCoeff_projectOnCoordinates
    {Ω : Type*} [Fintype Ω] [Nonempty Ω] {π : PMF Ω}
    {ι : Type*} [Fintype ι] [Nonempty ι] [DecidableEq ι]
    (B : FiniteFourierBasis Ω π ι) {n : ℕ}
    (J : Finset (Fin n)) (f : ProductL2 Ω n) (a : MultiIndex n ι) :
    B.fourierCoeff (projectOnCoordinates π J f) a =
      if multiIndexSupport B.zeroIndex a ⊆ J then B.fourierCoeff f a else 0 := by
  classical
  let c : MultiIndex n ι → ℝ := fun b ↦
    if multiIndexSupport B.zeroIndex b ⊆ J then B.fourierCoeff f b else 0
  have hc : ∀ x, projectOnCoordinates π J f x =
      ∑ b, c b * B.productFunction b x := by
    intro x
    rw [B.projectOnCoordinates_fourier_expansion]
    simp [c, Finset.sum_filter]
  have hunique := B.fourier_expansion_unique (projectOnCoordinates π J f) c hc
  exact (congrFun hunique a).symm

-- Source: FABL.Chapter08.GeneralizedFourierFormulas:583
/-- Exercise 8.7: coordinate projection is self-adjoint. -/
theorem projectOnCoordinates_selfAdjoint
    {Ω : Type*} [Fintype Ω] [Nonempty Ω] {π : PMF Ω}
    {ι : Type*} [Fintype ι] [Nonempty ι] [DecidableEq ι]
    (B : FiniteFourierBasis Ω π ι) {n : ℕ}
    (J : Finset (Fin n)) (f g : ProductL2 Ω n) :
    productInner π n f (projectOnCoordinates π J g) =
      productInner π n (projectOnCoordinates π J f) g := by
  rw [B.plancherel, B.plancherel]
  apply Finset.sum_congr rfl
  intro a _
  rw [B.fourierCoeff_projectOnCoordinates,
    B.fourierCoeff_projectOnCoordinates]
  split_ifs <;> ring

-- Source: FABL.Chapter08.GeneralizedFourierFormulas:612
/-- O'Donnell's `Eᵢ`: rerandomize coordinate `i` and retain every other coordinate. -/
noncomputable def coordinateProjection
    {Ω : Type*} [Fintype Ω] (π : PMF Ω) {n : ℕ}
    (i : Fin n) (f : ProductL2 Ω n) : ProductL2 Ω n :=
  projectOnCoordinates π (Finset.univ.erase i) f

/-! ## Laplacians and influences -/

-- Source: FABL.Chapter08.GeneralizedFourierFormulas:650
/-- O'Donnell, Definition 8.22: the coordinate Laplacian `Lᵢ = I - Eᵢ`. -/
noncomputable def productCoordinateLaplacian
    {Ω : Type*} [Fintype Ω] (π : PMF Ω) {n : ℕ}
    (i : Fin n) (f : ProductL2 Ω n) : ProductL2 Ω n :=
  f - coordinateProjection π i f

-- Source: FABL.Chapter08.GeneralizedFourierFormulas:677
/-- O'Donnell, Definition 8.22: influence is the squared weighted norm of the coordinate
Laplacian. -/
noncomputable def productInfluence
    {Ω : Type*} [Fintype Ω] (π : PMF Ω) {n : ℕ}
    (f : ProductL2 Ω n) (i : Fin n) : ℝ :=
  productInner π n (productCoordinateLaplacian π i f)
    (productCoordinateLaplacian π i f)

-- Source: FABL.Chapter08.GeneralizedFourierFormulas:685
/-- O'Donnell, Definition 8.22: total influence. -/
noncomputable def productTotalInfluence
    {Ω : Type*} [Fintype Ω] (π : PMF Ω) {n : ℕ}
    (f : ProductL2 Ω n) : ℝ :=
  ∑ i, productInfluence π f i

-- Source: FABL.Chapter08.GeneralizedFourierFormulas:796
/-- Influence is nonnegative. -/
theorem productInfluence_nonneg
    {Ω : Type*} [Fintype Ω] (π : PMF Ω) {n : ℕ}
    (f : ProductL2 Ω n) (i : Fin n) :
    0 ≤ productInfluence π f i :=
  pmfInner_self_nonneg _ _

/-! ## Conditional-variance formula -/

-- Source: FABL.Chapter08.GeneralizedFourierFormulas:831
/-- Replace coordinate `i` of `x` by `ω`. -/
def replaceCoordinate
    {Ω : Type*} {n : ℕ} (x : Fin n → Ω) (i : Fin n) (ω : Ω) : Fin n → Ω :=
  Function.update x i ω

-- Source: FABL.Chapter08.GeneralizedFourierFormulas:836
/-- Projection onto all coordinates except `i` is the one-site expectation over a fresh value of
coordinate `i`. -/
theorem coordinateProjection_apply
    {Ω : Type*} [Fintype Ω] (π : PMF Ω) {n : ℕ}
    (i : Fin n) (f : ProductL2 Ω n) (x : Fin n → Ω) :
    coordinateProjection π i f x =
      pmfExpectation π (fun ω ↦ f (replaceCoordinate x i ω)) := by
  classical
  unfold coordinateProjection projectOnCoordinates
  let q : (j : Fin n) → Ω → ℝ := fun j ω ↦
    if j = i then f (replaceCoordinate x i ω) else 1
  have hmerge (y : Fin n → Ω) :
      mergeOnCoordinates (Finset.univ.erase i) x y = replaceCoordinate x i (y i) := by
    funext j
    by_cases hji : j = i
    · subst j
      simp [mergeOnCoordinates, replaceCoordinate]
    · simp [mergeOnCoordinates, replaceCoordinate, hji]
  have hprod (y : Fin n → Ω) :
      f (replaceCoordinate x i (y i)) = ∏ j, q j (y j) := by
    rw [Finset.prod_eq_single i]
    · simp [q]
    · intro j _ hji
      simp [q, hji]
    · simp
  simp_rw [hmerge, hprod]
  rw [productProbabilityPMF,
    pmfExpectation_independentProductPMF_prod (fun _ : Fin n ↦ π) q]
  rw [Finset.prod_eq_single i]
  · simp [q]
  · intro j _ hji
    simp [q, hji, pmfExpectation_const_one]
  · simp

-- Source: FABL.Chapter08.GeneralizedFourierFormulas:870
/-- Conditional variance in coordinate `i`, with the other coordinates fixed by `x`. -/
noncomputable def coordinateConditionalVariance
    {Ω : Type*} [Fintype Ω] (π : PMF Ω) {n : ℕ}
    (f : ProductL2 Ω n) (i : Fin n) (x : Fin n → Ω) : ℝ :=
  let m := pmfExpectation π (fun ω ↦ f (replaceCoordinate x i ω))
  pmfExpectation π fun ω ↦ (f (replaceCoordinate x i ω) - m) ^ 2

-- Source: FABL.Chapter08.GeneralizedFourierFormulas:1009
/-- Coordinate projection is unchanged when its queried coordinate is replaced. -/
theorem coordinateProjection_replaceCoordinate
    {Ω : Type*} [Fintype Ω] (π : PMF Ω) {n : ℕ}
    (i : Fin n) (f : ProductL2 Ω n) (x : Fin n → Ω) (ω : Ω) :
    coordinateProjection π i f (replaceCoordinate x i ω) =
      coordinateProjection π i f x := by
  unfold coordinateProjection
  apply projectOnCoordinates_dependsOnly π (Finset.univ.erase i) f
  intro j hj
  have hji : j ≠ i := by simpa using hj
  simp [replaceCoordinate, Function.update_of_ne hji]

-- Source: FABL.Chapter08.GeneralizedFourierFormulas:1021
/-- Pointwise conditional variance is the coordinate projection of the squared Laplacian. -/
theorem coordinateConditionalVariance_eq_coordinateProjection_sq_laplacian
    {Ω : Type*} [Fintype Ω] (π : PMF Ω) {n : ℕ}
    (f : ProductL2 Ω n) (i : Fin n) (x : Fin n → Ω) :
    coordinateConditionalVariance π f i x =
      coordinateProjection π i
        (fun z ↦ productCoordinateLaplacian π i f z ^ 2) x := by
  rw [coordinateConditionalVariance, coordinateProjection_apply]
  simp only [productCoordinateLaplacian, Pi.sub_apply]
  have hm : pmfExpectation π (fun ω ↦ f (replaceCoordinate x i ω)) =
      coordinateProjection π i f x := by
    rw [← coordinateProjection_apply]
  rw [hm]
  apply congrArg (pmfExpectation π)
  funext ω
  rw [coordinateProjection_replaceCoordinate]

-- Source: FABL.Chapter08.GeneralizedFourierFormulas:1038
/-- Projection preserves the global mean. -/
theorem FiniteFourierBasis.productMean_projectOnCoordinates
    {Ω : Type*} [Fintype Ω] [Nonempty Ω] {π : PMF Ω}
    {ι : Type*} [Fintype ι] [Nonempty ι] [DecidableEq ι]
    (B : FiniteFourierBasis Ω π ι) {n : ℕ}
    (J : Finset (Fin n)) (f : ProductL2 Ω n) :
    productMean π (projectOnCoordinates π J f) = productMean π f := by
  rw [← B.fourierCoeff_zeroMultiIndex,
    B.fourierCoeff_projectOnCoordinates]
  have hzero : multiIndexSupport B.zeroIndex (B.zeroMultiIndex n) = ∅ := by
    ext i
    simp [multiIndexSupport, FiniteFourierBasis.zeroMultiIndex]
  rw [hzero, if_pos (Finset.empty_subset J), B.fourierCoeff_zeroMultiIndex]

-- Source: FABL.Chapter08.GeneralizedFourierFormulas:1052
/-- Proposition 8.24: influence is the expectation of the conditional coordinate variance. -/
theorem FiniteFourierBasis.productInfluence_eq_expect_coordinateConditionalVariance
    {Ω : Type*} [Fintype Ω] [Nonempty Ω] {π : PMF Ω}
    {ι : Type*} [Fintype ι] [Nonempty ι] [DecidableEq ι]
    (B : FiniteFourierBasis Ω π ι) {n : ℕ}
    (f : ProductL2 Ω n) (i : Fin n) :
    productInfluence π f i =
      productMean π (coordinateConditionalVariance π f i) := by
  rw [show coordinateConditionalVariance π f i =
      coordinateProjection π i
        (fun z ↦ productCoordinateLaplacian π i f z ^ 2) by
    funext x
    exact coordinateConditionalVariance_eq_coordinateProjection_sq_laplacian π f i x]
  unfold coordinateProjection
  rw [B.productMean_projectOnCoordinates]
  unfold productInfluence productMean productInner
  rw [pmfInner_eq_expect]
  congr 1
  funext x
  ring

-- Source: FABL.Chapter08.GeneralizedFourierFormulas:1156
/-- Product mean respects scalar multiplication. -/
theorem productMean_smul
    {Ω : Type*} [Fintype Ω] (π : PMF Ω) {n : ℕ}
    (c : ℝ) (f : ProductL2 Ω n) :
    productMean π (c • f) = c * productMean π f := by
  unfold productMean
  exact pmfExpectation_const_mul _ _ _

/-! ## Coordinatewise noise operators (Exercise 8.11) -/

/-! ## Product noise and stability -/

/-! ## Stable influences -/

/-! ## Basis-free degree -/

/-! ## Compatibility with the canonical uniform sign-cube API -/

-- Source: FABL.Chapter08.GeneralizedFourierFormulas:2154
/-- The independent product of uniform finite laws is the uniform law on the function space. -/
theorem productProbabilityPMF_uniform
    {V D : Type*} [Fintype V] [DecidableEq V] [Fintype D] [Nonempty D] :
    independentProductPMF (fun _ : V ↦ uniformPMF D) = uniformPMF (V → D) := by
  classical
  ext assignment
  simp [independentProductPMF_apply, uniformPMF, PMF.uniformOfFintype_apply, Fintype.card_pi,
    ENNReal.inv_pow]

-- Source: FABL.Chapter08.GeneralizedFourierFormulas:2163
/-- In particular, the Chapter 8 product law agrees with the canonical uniform sign-cube law. -/
theorem productProbabilityPMF_uniformSign (n : ℕ) :
    productProbabilityPMF (uniformPMF Sign) n = uniformPMF (FABL.SignCube (n)) := by
  exact productProbabilityPMF_uniform

-- Source: FABL.Chapter08.GeneralizedFourierFormulas:2168
/-- Binary multi-indices are equivalent to subsets through their nonzero supports. -/
def signMultiIndexEquivFinset (n : ℕ) :
    MultiIndex n (Fin 2) ≃ Finset (Fin n) where
  toFun := signMultiIndexSupport
  invFun S i := if i ∈ S then 1 else 0
  left_inv a := by
    funext i
    by_cases hai : a i = 0
    · simp [signMultiIndexSupport, multiIndexSupport, hai]
    · have hone : a i = 1 := Fin.eq_one_of_ne_zero (a i) hai
      simp [signMultiIndexSupport, multiIndexSupport, hone]
  right_inv S := by
    ext i
    simp [signMultiIndexSupport, multiIndexSupport]

-- Source: FABL.Chapter08.GeneralizedFourierFormulas:2183
/-- Product Fourier coefficients for the sign-site basis are exactly the existing subset-indexed
Walsh coefficients. -/
theorem signSiteFourierBasis_fourierCoeff_eq_fourierCoeff
    {n : ℕ} (f : (FABL.SignCube (n)) → ℝ) (a : MultiIndex n (Fin 2)) :
    signSiteFourierBasis.fourierCoeff f a =
      fourierCoeff f (signMultiIndexSupport a) := by
  unfold FiniteFourierBasis.fourierCoeff fourierCoeff
  rw [productProbabilityPMF_uniformSign, pmfExpectation_uniformPMF_eq_expect]
  apply Finset.expect_congr rfl
  intro x _
  rw [signSiteFourierBasis_productFunction_eq_monomial]

-- Source: FABL.Chapter08.GeneralizedFourierFormulas:2226
/-- The product weighted inner product under uniform signs is FABL's canonical normalized inner
product. -/
theorem productInner_uniformSign (f g : (FABL.SignCube (n)) → ℝ) :
    productInner (uniformPMF Sign) n f g = (FABL.uniformInner (f) (g)) := by
  unfold productInner
  rw [pmfInner_eq_expect, productProbabilityPMF_uniformSign,
    pmfExpectation_uniformPMF_eq_expect, uniformInner,
    RCLike.wInner_cWeight_eq_expect]
  apply Finset.expect_congr rfl
  intro x _
  simp [RCLike.inner_apply, mul_comm]

-- Source: FABL.Chapter08.GeneralizedFourierFormulas:2238
/-- The one-site form of coordinate projection on the sign cube is the average of the two sign
restrictions. -/
theorem coordinateProjection_uniformSign_apply
    (i : Fin n) (f : (FABL.SignCube (n)) → ℝ) (x : (FABL.SignCube (n))) :
    coordinateProjection (uniformPMF Sign) i f x =
      (f (setCoordinate x i 1) + f (setCoordinate x i (-1))) / 2 := by
  rw [coordinateProjection_apply, pmfExpectation_uniformPMF_eq_expect]
  calc
    (𝔼 ω : Sign, f (replaceCoordinate x i ω)) =
        𝔼 j : Fin 2, f (replaceCoordinate x i (finTwoSignEquiv j)) := by
      symm
      apply Fintype.expect_equiv finTwoSignEquiv
      intro j
      rfl
    _ = (f (setCoordinate x i 1) + f (setCoordinate x i (-1))) / 2 := by
      norm_num [Fintype.expect_eq_sum_div_card, Fin.sum_univ_two,
        finTwoSignEquiv, replaceCoordinate, setCoordinate]
      ring

-- Source: FABL.Chapter08.GeneralizedFourierFormulas:2257
/-- Remark 8.18: Chapter 8 coordinate projection is exactly Chapter 2's
`coordinateExpectation`. -/
theorem coordinateProjection_uniformSign_eq_coordinateExpectation
    (i : Fin n) (f : (FABL.SignCube (n)) → ℝ) :
    coordinateProjection (uniformPMF Sign) i f = coordinateExpectation i f := by
  funext x
  rw [coordinateProjection_uniformSign_apply, coordinateExpectation_apply]

-- Source: FABL.Chapter08.GeneralizedFourierFormulas:2265
/-- Chapter 8 coordinate Laplacian specializes to the existing Chapter 2 Laplacian. -/
theorem productCoordinateLaplacian_uniformSign_eq_coordinateLaplacian
    (i : Fin n) (f : (FABL.SignCube (n)) → ℝ) :
    productCoordinateLaplacian (uniformPMF Sign) i f = coordinateLaplacian i f := by
  rw [productCoordinateLaplacian, coordinateLaplacian]
  change f - coordinateProjection (uniformPMF Sign) i f =
    f - coordinateExpectation i f
  rw [coordinateProjection_uniformSign_eq_coordinateExpectation]

-- Source: FABL.Chapter08.GeneralizedFourierFormulas:2274
/-- Chapter 8 influence specializes to the canonical Chapter 2 influence without changing the
old API. -/
theorem productInfluence_uniformSign_eq_influence
    (f : (FABL.SignCube (n)) → ℝ) (i : Fin n) :
    productInfluence (uniformPMF Sign) f i = influence f i := by
  rw [productInfluence, productCoordinateLaplacian_uniformSign_eq_coordinateLaplacian,
    productInner_uniformSign]
  exact uniformInner_coordinateLaplacian_self_eq_influence f i

-- Source: FABL.Chapter08.GeneralizedFourierFormulas:2283
/-- Total influence also specializes definitionally through the coordinate bridge. -/
theorem productTotalInfluence_uniformSign_eq_totalInfluence
    (f : (FABL.SignCube (n)) → ℝ) :
    productTotalInfluence (uniformPMF Sign) f = totalInfluence f := by
  unfold productTotalInfluence totalInfluence
  apply Finset.sum_congr rfl
  intro i _
  exact productInfluence_uniformSign_eq_influence f i

end FABL

end

/- Source fragment: FABL.Chapter08.OrthogonalDecomposition. Original licenses and source proofs retained. -/

section

/-
Copyright (c) 2026 Asher Yan. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Asher Yan with Codex
-/

/-!
# Orthogonal decomposition on finite product spaces

Book items: Lemma 8.34, Theorem 8.35, Proposition 8.36, Example 8.37,
Definition 8.38, and Exercises 8.14--8.22.

The book's basis-free orthogonal component is implemented through the exact-support component
already constructed for an arbitrary finite Fourier basis.  The Möbius formula below proves that
this representation is independent of the chosen basis: it is the alternating sum of the
probabilistic coordinate projections.
-/

open Finset
open scoped BigOperators

namespace FABL

/-! ## Exact-support orthogonal components -/

/-! ## Intersections of coordinate projections -/

/-! ## The six properties and uniqueness -/

/-! ## Boolean-lattice Möbius inversion -/

/-! ## Projection, martingale, and degree consequences -/

/-! ## Definition 8.38 and the direct formulas of Exercise 8.18 -/

/-! ## The `L∞` estimate of Exercise 8.19 -/

-- Source: FABL.Chapter08.OrthogonalDecomposition:965
/-- The finite-product `L∞` norm used in Exercise 8.19. -/
noncomputable def productSupNorm
    {Ω : Type*} [Fintype Ω] [Nonempty Ω] {n : ℕ}
    (f : ProductL2 Ω n) : ℝ :=
  (Finset.univ : Finset (Fin n → Ω)).sup' Finset.univ_nonempty fun x ↦ |f x|

-- Source: FABL.Chapter08.OrthogonalDecomposition:971
/-- Every point evaluation is bounded by the finite-product supremum norm. -/
theorem abs_le_productSupNorm
    {Ω : Type*} [Fintype Ω] [Nonempty Ω] {n : ℕ}
    (f : ProductL2 Ω n) (x : Fin n → Ω) :
    |f x| ≤ productSupNorm f := by
  exact Finset.le_sup' (fun y ↦ |f y|) (Finset.mem_univ x)

-- Source: FABL.Chapter08.OrthogonalDecomposition:978
/-- Coordinate projection is a contraction for the finite-product supremum norm, pointwise. -/
theorem abs_projectOnCoordinates_le_productSupNorm
    {Ω : Type*} [Fintype Ω] [Nonempty Ω] (π : PMF Ω) {n : ℕ}
    (J : Finset (Fin n)) (f : ProductL2 Ω n) (x : Fin n → Ω) :
    |projectOnCoordinates π J f x| ≤ productSupNorm f := by
  unfold projectOnCoordinates
  apply abs_le.mpr
  constructor
  · calc
      -productSupNorm f =
          pmfExpectation (productProbabilityPMF π n)
            (fun _ ↦ -productSupNorm f) :=
        (pmfExpectation_const _ _).symm
      _ ≤ pmfExpectation (productProbabilityPMF π n)
          (fun y ↦ f (mergeOnCoordinates J x y)) := by
        apply pmfExpectation_mono
        intro y
        exact neg_le_of_abs_le
          (abs_le_productSupNorm f (mergeOnCoordinates J x y))
  · calc
      pmfExpectation (productProbabilityPMF π n)
          (fun y ↦ f (mergeOnCoordinates J x y)) ≤
          pmfExpectation (productProbabilityPMF π n)
            (fun _ ↦ productSupNorm f) := by
        apply pmfExpectation_mono
        intro y
        exact le_of_abs_le
          (abs_le_productSupNorm f (mergeOnCoordinates J x y))
      _ = productSupNorm f := pmfExpectation_const _ _

/-! ## Restricting an exact-support component (Exercise 8.21) -/

/-! ## Coordinate symmetry -/

end FABL

end

/- Source fragment: FABL.Chapter03.LearningTheory.LearningModel. Original licenses and source proofs retained. -/

section

/-
Copyright (c) 2026 Asher Yan. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Asher Yan with Codex
-/

/-!
# Learning algorithms and sparse hypotheses

Book items: Definition 3.27, Definition 3.28, Proposition 3.31, Theorem 3.29.

Finite hypothesis representations, spectral concentration, and sparse Fourier hypotheses.
-/

open Finset MeasureTheory ProbabilityTheory Set
open scoped BigOperators ENNReal

namespace FABL

universe u v

variable {n : ℕ}

-- Source: FABL.Chapter03.LearningTheory.LearningModel:87
/-- Fourier weight outside an arbitrary collection of characters. -/
noncomputable def fourierWeightOutside
    (f : (FABL.SignCube (n)) → ℝ) (𝓕 : Set (Finset (Fin n))) : ℝ :=
  by
    classical
    exact ∑ S ∈ (Finset.univ.filter fun S : Finset (Fin n) ↦ S ∉ 𝓕), fourierWeight f S

-- Source: FABL.Chapter03.LearningTheory.LearningModel:94
/-- O'Donnell, Definition 3.28: the Fourier spectrum is ε-concentrated on an arbitrary
collection. -/
def IsFourierSpectrumConcentratedOn
    (f : (FABL.SignCube (n)) → ℝ) (ε : ℝ) (𝓕 : Set (Finset (Fin n))) : Prop :=
  fourierWeightOutside f 𝓕 ≤ ε

namespace SparseFourierHypothesis

end SparseFourierHypothesis

namespace SparseFourierHypothesis

end SparseFourierHypothesis

end FABL

end

/- Source fragment: FABL.Chapter03.LearningTheory.LowDegree. Original licenses and source proofs retained. -/

section

/-
Copyright (c) 2026 Asher Yan. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Asher Yan with Codex
-/

/-!
# Low-degree learning

Book items: Low-Degree Algorithm, Theorem 3.36, Corollary 3.32, Corollary 3.33, Corollary 3.34,
Corollary 3.35, Exercise 3.36.

The Low-Degree Algorithm and the structural learning corollaries of Section 3.4.
-/

open Finset MeasureTheory ProbabilityTheory Set
open scoped BigOperators ENNReal

namespace FABL

universe u v

variable {n : ℕ}

/-! ## The Low-Degree Algorithm and its structural corollaries -/

-- Source: FABL.Chapter03.LearningTheory.LowDegree:112
/-- Raising the degree cutoff can only decrease the Fourier tail. -/
theorem fourierWeightAboveReal_antitone (f : (FABL.SignCube (n)) → ℝ)
    {a b : ℝ} (hab : a ≤ b) :
    fourierWeightAboveReal b f ≤ fourierWeightAboveReal a f := by
  classical
  unfold fourierWeightAboveReal
  apply Finset.sum_le_sum_of_subset_of_nonneg
  · intro S hS
    rw [Finset.mem_filter] at hS ⊢
    exact ⟨Finset.mem_univ S, hab.trans_lt hS.2⟩
  · intro S _ _
    exact sq_nonneg (fourierCoeff f S)

-- Source: FABL.Chapter03.LearningTheory.LowDegree:125
/-- Fourier concentration persists when the degree cutoff is increased. -/
theorem IsFourierSpectrumConcentratedUpTo.mono_cutoff
    {f : (FABL.SignCube (n)) → ℝ} {ε a b : ℝ}
    (h : IsFourierSpectrumConcentratedUpTo f ε a) (hab : a ≤ b) :
    IsFourierSpectrumConcentratedUpTo f ε b := by
  exact (fourierWeightAboveReal_antitone f hab).trans h

end FABL

end

/- Source fragment: FABL.Chapter09.Friedgut. Original licenses and source proofs retained. -/

section

/-
Copyright (c) 2026 Asher Yan. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Asher Yan with Codex
-/

/-!
# Influential coordinates and junta concentration

Book support: the influential-coordinate cardinal estimate and the
low-degree mass bound used in Theorem 9.28.
-/

open Finset Set
open scoped BigOperators

namespace FABL

variable {n : ℕ}

-- Source: FABL.Chapter09.Friedgut:28
/-- Coordinates whose ordinary Boolean influence is at least `τ`. -/
noncomputable def influentialCoordinates
    (f : BooleanFunction n) (τ : ℝ) : Finset (Fin n) :=
  Finset.univ.filter fun i ↦ τ ≤ booleanInfluence f i

-- Source: FABL.Chapter09.Friedgut:33
 theorem mem_influentialCoordinates
    (f : BooleanFunction n) (τ : ℝ) (i : Fin n) :
    i ∈ influentialCoordinates f τ ↔ τ ≤ booleanInfluence f i := by
  simp [influentialCoordinates]

-- Source: FABL.Chapter09.Friedgut:38
theorem not_mem_influentialCoordinates
    (f : BooleanFunction n) (τ : ℝ) (i : Fin n) :
    i ∉ influentialCoordinates f τ ↔ booleanInfluence f i < τ := by
  simp [influentialCoordinates]

-- Source: FABL.Chapter09.Friedgut:43
/-- The threshold times the number of influential coordinates is at most total influence. -/
theorem card_influentialCoordinates_mul_le_totalInfluence
    (f : BooleanFunction n) (τ : ℝ) :
    ((influentialCoordinates f τ).card : ℝ) * τ ≤ totalInfluence f.toReal := by
  rw [totalInfluence]
  calc
    ((influentialCoordinates f τ).card : ℝ) * τ =
        ∑ i ∈ influentialCoordinates f τ, τ := by simp [mul_comm]
    _ ≤ ∑ i ∈ influentialCoordinates f τ, influence f.toReal i := by
      apply Finset.sum_le_sum
      intro i hi
      rw [← booleanInfluence_eq_influence_toReal]
      exact (mem_influentialCoordinates f τ i).mp hi
    _ ≤ ∑ i, influence f.toReal i := by
      exact Finset.sum_le_sum_of_subset_of_nonneg (by simp)
        (fun i _ _ ↦ influence_nonneg f.toReal i)

-- Source: FABL.Chapter09.Friedgut:60
/-- Theorem 9.28's cardinal bound in the algebraic threshold form used by its proof. -/
theorem card_influentialCoordinates_le_div
    (f : BooleanFunction n) {τ : ℝ} (hτ : 0 < τ) :
    ((influentialCoordinates f τ).card : ℝ) ≤ totalInfluence f.toReal / τ := by
  exact (le_div_iff₀ hτ).2 (card_influentialCoordinates_mul_le_totalInfluence f τ)

-- Source: FABL.Chapter09.Friedgut:66
/-- Low-degree Fourier mass containing a fixed coordinate. -/
noncomputable def lowDegreeCoordinateMass
    (f : BooleanFunction n) (i : Fin n) (k : ℕ) : ℝ :=
  ∑ S ∈ (Finset.univ.filter fun S : Finset (Fin n) ↦ i ∈ S ∧ S.card ≤ k),
    fourierCoeff f.toReal S ^ 2

-- Source: FABL.Chapter09.Friedgut:72
/-- A low-degree coordinate mass is controlled by one-third stable influence. -/
theorem lowDegreeCoordinateMass_le_three_pow_mul_stableInfluence
    (f : BooleanFunction n) (i : Fin n) (k : ℕ) :
    lowDegreeCoordinateMass f i k ≤
      (3 : ℝ) ^ k * stableInfluence (1 / 3 : ℝ) f.toReal i := by
  classical
  unfold lowDegreeCoordinateMass stableInfluence
  simp only [Finset.sum_filter]
  calc
    (∑ S, if i ∈ S ∧ S.card ≤ k then fourierCoeff f.toReal S ^ 2 else 0) ≤
        ∑ S, (3 : ℝ) ^ k *
          (if i ∈ S then (1 / 3 : ℝ) ^ (S.card - 1) *
            fourierCoeff f.toReal S ^ 2 else 0) := by
      apply Finset.sum_le_sum
      intro S _
      by_cases hS : i ∈ S ∧ S.card ≤ k
      · rw [if_pos hS, if_pos hS.1]
        have hcardPos : 0 < S.card := Finset.card_pos.mpr ⟨i, hS.1⟩
        have hpow :
            1 ≤ (3 : ℝ) ^ k * (1 / 3 : ℝ) ^ (S.card - 1) := by
          have hexp : S.card - 1 ≤ k := by omega
          rw [show (1 / 3 : ℝ) ^ (S.card - 1) =
              ((3 : ℝ) ^ (S.card - 1))⁻¹ by
            rw [one_div, inv_pow]]
          rw [← div_eq_mul_inv]
          exact (le_div_iff₀ (pow_pos (by norm_num) _)).2 <| by
            simpa using pow_le_pow_right₀ (by norm_num : (1 : ℝ) ≤ 3)
              hexp
        calc
          fourierCoeff f.toReal S ^ 2 =
              1 * fourierCoeff f.toReal S ^ 2 := by ring
          _ ≤ ((3 : ℝ) ^ k * (1 / 3 : ℝ) ^ (S.card - 1)) *
              fourierCoeff f.toReal S ^ 2 :=
            mul_le_mul_of_nonneg_right hpow (sq_nonneg _)
          _ = (3 : ℝ) ^ k * ((1 / 3 : ℝ) ^ (S.card - 1) *
              fourierCoeff f.toReal S ^ 2) := by ring
      · rw [if_neg hS]
        positivity
    _ = (3 : ℝ) ^ k *
        ∑ S, if i ∈ S then (1 / 3 : ℝ) ^ (S.card - 1) *
          fourierCoeff f.toReal S ^ 2 else 0 := by rw [Finset.mul_sum]

-- Source: FABL.Chapter09.Friedgut:114
/-- The low-degree Fourier weight on sets not contained in the influential coordinates. -/
noncomputable def lowDegreeOutsideInfluentialMass
    (f : BooleanFunction n) (τ : ℝ) (k : ℕ) : ℝ :=
  ∑ S ∈ (Finset.univ.filter fun S : Finset (Fin n) ↦
      S.card ≤ k ∧ ¬S ⊆ influentialCoordinates f τ),
    fourierCoeff f.toReal S ^ 2

-- Source: FABL.Chapter09.Friedgut:121
/-- Every bad Fourier set can be charged to at least one noninfluential coordinate it contains. -/
theorem lowDegreeOutsideInfluentialMass_le_sum_coordinateMass
    (f : BooleanFunction n) (τ : ℝ) (k : ℕ) :
    lowDegreeOutsideInfluentialMass f τ k ≤
      ∑ i ∈ (Finset.univ.filter fun i : Fin n ↦ i ∉ influentialCoordinates f τ),
        lowDegreeCoordinateMass f i k := by
  classical
  unfold lowDegreeOutsideInfluentialMass lowDegreeCoordinateMass
  let bad := Finset.univ.filter fun S : Finset (Fin n) ↦
    S.card ≤ k ∧ ¬S ⊆ influentialCoordinates f τ
  calc
    (∑ S ∈ bad, fourierCoeff f.toReal S ^ 2) ≤
        ∑ S ∈ bad, ∑ i : Fin n,
          if i ∉ influentialCoordinates f τ ∧ i ∈ S
          then fourierCoeff f.toReal S ^ 2 else 0 := by
      apply Finset.sum_le_sum
      intro S hS
      have hbad := (Finset.mem_filter.mp hS).2.2
      obtain ⟨i, hiS, hiJ⟩ := Set.not_subset.mp hbad
      have hi : i ∉ influentialCoordinates f τ ∧ i ∈ S := ⟨hiJ, hiS⟩
      have hilt : booleanInfluence f i < τ :=
        (not_mem_influentialCoordinates f τ i).mp hiJ
      calc
        fourierCoeff f.toReal S ^ 2 ≤
            ∑ j ∈ ({i} : Finset (Fin n)),
              if j ∉ influentialCoordinates f τ ∧ j ∈ S
              then fourierCoeff f.toReal S ^ 2 else 0 := by
          rw [Finset.sum_singleton, if_pos hi]
        _ ≤ ∑ j : Fin n,
              if j ∉ influentialCoordinates f τ ∧ j ∈ S
              then fourierCoeff f.toReal S ^ 2 else 0 := by
          apply Finset.sum_le_sum_of_subset_of_nonneg (by simp)
          intro j _ _
          split_ifs <;> positivity
    _ ≤ ∑ S : Finset (Fin n), ∑ i : Fin n,
          if i ∉ influentialCoordinates f τ ∧ i ∈ S ∧ S.card ≤ k
          then fourierCoeff f.toReal S ^ 2 else 0 := by
      dsimp [bad]
      rw [Finset.sum_filter]
      apply Finset.sum_le_sum
      intro S _
      by_cases hS : S.card ≤ k ∧ ¬S ⊆ influentialCoordinates f τ
      · rw [if_pos hS]
        apply Finset.sum_le_sum
        intro i _
        by_cases hcond : booleanInfluence f i < τ ∧ i ∈ S
        · simp [hcond, hS.1]
        · have hcondOrig :
              ¬(i ∉ influentialCoordinates f τ ∧ i ∈ S) := by
            intro h
            exact hcond ⟨(not_mem_influentialCoordinates f τ i).mp h.1, h.2⟩
          have hrfalseOrig :
              ¬(i ∉ influentialCoordinates f τ ∧ i ∈ S ∧ S.card ≤ k) := by
            intro h
            exact hcondOrig ⟨h.1, h.2.1⟩
          rw [if_neg hcondOrig, if_neg hrfalseOrig]
      · rw [if_neg hS]
        positivity
    _ = ∑ i ∈ (Finset.univ.filter fun i : Fin n ↦
          i ∉ influentialCoordinates f τ),
        ∑ S ∈ (Finset.univ.filter fun S : Finset (Fin n) ↦ i ∈ S ∧ S.card ≤ k),
          fourierCoeff f.toReal S ^ 2 := by
      rw [Finset.sum_comm]
      simp only [Finset.sum_filter]
      apply Finset.sum_congr rfl
      intro i _
      by_cases hi : i ∉ influentialCoordinates f τ
      · rw [if_pos hi]
        apply Finset.sum_congr rfl
        intro S _
        by_cases hS : i ∈ S ∧ S.card ≤ k <;> simp [hi, hS]
      · rw [if_neg hi]
        have hnotlt : ¬booleanInfluence f i < τ := by
          intro hlt
          exact hi ((not_mem_influentialCoordinates f τ i).2 hlt)
        simp [mem_influentialCoordinates, hnotlt]

-- Source: FABL.Chapter09.Friedgut:198
/-- A noninfluential coordinate has little low-degree Fourier mass. -/
theorem lowDegreeCoordinateMass_le_three_pow_mul_sqrt_threshold_mul_influence
    (f : BooleanFunction n) {τ : ℝ} (k : ℕ)
    {i : Fin n} (hi : i ∉ influentialCoordinates f τ) :
    lowDegreeCoordinateMass f i k ≤
      (3 : ℝ) ^ k * Real.sqrt τ * booleanInfluence f i := by
  have hinf : booleanInfluence f i < τ :=
    (not_mem_influentialCoordinates f τ i).mp hi
  have hinf0 : 0 ≤ booleanInfluence f i := by
    rw [booleanInfluence_eq_influence_toReal]
    exact influence_nonneg f.toReal i
  calc
    lowDegreeCoordinateMass f i k ≤
        (3 : ℝ) ^ k * stableInfluence (1 / 3 : ℝ) f.toReal i :=
      lowDegreeCoordinateMass_le_three_pow_mul_stableInfluence f i k
    _ ≤ (3 : ℝ) ^ k *
        (booleanInfluence f i * Real.sqrt (booleanInfluence f i)) := by
      gcongr
      exact stableInfluence_oneThird_le_booleanInfluence_mul_sqrt f i
    _ ≤ (3 : ℝ) ^ k * (booleanInfluence f i * Real.sqrt τ) := by
      apply mul_le_mul_of_nonneg_left _ (pow_nonneg (by norm_num) _)
      exact mul_le_mul_of_nonneg_left (Real.sqrt_le_sqrt (le_of_lt hinf)) hinf0
    _ = (3 : ℝ) ^ k * Real.sqrt τ * booleanInfluence f i := by ring

-- Source: FABL.Chapter09.Friedgut:222
/-- The core estimate in Theorem 9.28. -/
theorem lowDegreeOutsideInfluentialMass_le
    (f : BooleanFunction n) (τ : ℝ) (k : ℕ) :
    lowDegreeOutsideInfluentialMass f τ k ≤
      (3 : ℝ) ^ k * Real.sqrt τ * totalInfluence f.toReal := by
  calc
    lowDegreeOutsideInfluentialMass f τ k ≤
        ∑ i ∈ (Finset.univ.filter fun i : Fin n ↦ i ∉ influentialCoordinates f τ),
          lowDegreeCoordinateMass f i k :=
      lowDegreeOutsideInfluentialMass_le_sum_coordinateMass f τ k
    _ ≤ ∑ i ∈ (Finset.univ.filter fun i : Fin n ↦ i ∉ influentialCoordinates f τ),
          (3 : ℝ) ^ k * Real.sqrt τ * booleanInfluence f i := by
      apply Finset.sum_le_sum
      intro i hi
      exact lowDegreeCoordinateMass_le_three_pow_mul_sqrt_threshold_mul_influence
        f k (Finset.mem_filter.mp hi).2
    _ ≤ ∑ i : Fin n, (3 : ℝ) ^ k * Real.sqrt τ * booleanInfluence f i := by
      apply Finset.sum_le_sum_of_subset_of_nonneg (by simp)
      intro i _ _
      exact mul_nonneg
        (mul_nonneg (pow_nonneg (by norm_num) _) (Real.sqrt_nonneg _)) <| by
          rw [booleanInfluence_eq_influence_toReal]
          exact influence_nonneg f.toReal i
    _ = (3 : ℝ) ^ k * Real.sqrt τ * totalInfluence f.toReal := by
      rw [totalInfluence]
      simp_rw [← booleanInfluence_eq_influence_toReal]
      rw [← Finset.mul_sum]

-- Source: FABL.Chapter09.Friedgut:250
/-- The threshold chosen in Theorem 9.28. -/
noncomputable def theorem9_28Threshold
    (f : BooleanFunction n) (ε : ℝ) (k : ℕ) : ℝ :=
  ε ^ 2 / totalInfluence f.toReal ^ 2 * ((9 : ℝ)⁻¹) ^ k

-- Source: FABL.Chapter09.Friedgut:255
/-- The Fourier family in the first conclusion of Theorem 9.28. -/
def theorem9_28Family
    (f : BooleanFunction n) (ε : ℝ) (k : ℕ) : Set (Finset (Fin n)) :=
  {S | S ⊆ influentialCoordinates f (theorem9_28Threshold f ε k)} ∪
    {S | k < S.card}

-- Source: FABL.Chapter09.Friedgut:261
theorem theorem9_28Threshold_pos
    (f : BooleanFunction n) {ε : ℝ} (hε : 0 < ε) (k : ℕ)
    (hI : 0 < totalInfluence f.toReal) :
    0 < theorem9_28Threshold f ε k := by
  unfold theorem9_28Threshold
  positivity

-- Source: FABL.Chapter09.Friedgut:268
theorem sqrt_theorem9_28Threshold
    (f : BooleanFunction n) {ε : ℝ} (hε : 0 < ε) (k : ℕ)
    (hI : 0 < totalInfluence f.toReal) :
    Real.sqrt (theorem9_28Threshold f ε k) =
      ε / totalInfluence f.toReal * (1 / 3 : ℝ) ^ k := by
  let r := ε / totalInfluence f.toReal * (1 / 3 : ℝ) ^ k
  have hr : 0 ≤ r := by dsimp [r]; positivity
  have hthreshold : theorem9_28Threshold f ε k = r ^ 2 := by
    dsimp [theorem9_28Threshold, r]
    have hthird : ((9 : ℝ)⁻¹) ^ k = ((1 / 3 : ℝ) ^ k) ^ 2 := by
      rw [sq, ← mul_pow]
      norm_num
    rw [hthird, mul_pow, div_pow]
    ring
  rw [hthreshold, Real.sqrt_sq_eq_abs, abs_of_nonneg hr]

-- Source: FABL.Chapter09.Friedgut:284
theorem card_theorem9_28_influentialCoordinates_le
    (f : BooleanFunction n) {ε : ℝ} (hε : 0 < ε) (k : ℕ)
    (hI : 0 < totalInfluence f.toReal) :
    ((influentialCoordinates f (theorem9_28Threshold f ε k)).card : ℝ) ≤
      totalInfluence f.toReal ^ 3 / ε ^ 2 * (9 : ℝ) ^ k := by
  have hτ := theorem9_28Threshold_pos f hε k hI
  calc
    ((influentialCoordinates f (theorem9_28Threshold f ε k)).card : ℝ) ≤
        totalInfluence f.toReal / theorem9_28Threshold f ε k :=
      card_influentialCoordinates_le_div f hτ
    _ = totalInfluence f.toReal ^ 3 / ε ^ 2 * (9 : ℝ) ^ k := by
      unfold theorem9_28Threshold
      have hε0 : ε ≠ 0 := ne_of_gt hε
      have hI0 : totalInfluence f.toReal ≠ 0 := ne_of_gt hI
      field_simp [hε0, hI0]
      rw [← mul_pow]
      norm_num

-- Source: FABL.Chapter09.Friedgut:302
theorem fourierWeightOutside_theorem9_28Family
    (f : BooleanFunction n) (ε : ℝ) (k : ℕ) :
    fourierWeightOutside f.toReal (theorem9_28Family f ε k) =
      lowDegreeOutsideInfluentialMass f (theorem9_28Threshold f ε k) k := by
  classical
  unfold fourierWeightOutside lowDegreeOutsideInfluentialMass theorem9_28Family fourierWeight
  congr 1
  ext S
  simp [not_lt, and_comm]

-- Source: FABL.Chapter09.Friedgut:312
/-- The first spectral-concentration conclusion of Theorem 9.28. -/
theorem theorem9_28_spectrum_concentrated
    (f : BooleanFunction n) {ε : ℝ} (hε : 0 < ε) (k : ℕ)
    (hI : 0 < totalInfluence f.toReal) :
    IsFourierSpectrumConcentratedOn f.toReal ε (theorem9_28Family f ε k) := by
  unfold IsFourierSpectrumConcentratedOn
  rw [fourierWeightOutside_theorem9_28Family]
  calc
    lowDegreeOutsideInfluentialMass f (theorem9_28Threshold f ε k) k ≤
        (3 : ℝ) ^ k * Real.sqrt (theorem9_28Threshold f ε k) *
          totalInfluence f.toReal :=
      lowDegreeOutsideInfluentialMass_le f (theorem9_28Threshold f ε k) k
    _ = ε := by
      rw [sqrt_theorem9_28Threshold f hε k hI]
      have hI0 : totalInfluence f.toReal ≠ 0 := ne_of_gt hI
      field_simp [hI0]
      rw [← mul_pow]
      norm_num

-- Source: FABL.Chapter09.Friedgut:331
/-- The low-degree Fourier family supported on Theorem 9.28's influential coordinates. -/
def theorem9_28SmallFamily
    (f : BooleanFunction n) (ε : ℝ) (k : ℕ) : Set (Finset (Fin n)) :=
  {S | S ⊆ influentialCoordinates f (theorem9_28Threshold f ε k) ∧ S.card ≤ k}

-- Source: FABL.Chapter09.Friedgut:336
/-- The complement of Theorem 9.28's small family is covered by the complement of its first
family and the high-degree tail. -/
theorem fourierWeightOutside_theorem9_28SmallFamily_le_add
    (f : BooleanFunction n) (ε : ℝ) (k : ℕ) :
    fourierWeightOutside f.toReal (theorem9_28SmallFamily f ε k) ≤
      fourierWeightOutside f.toReal (theorem9_28Family f ε k) +
        fourierWeightAbove k f.toReal := by
  classical
  unfold fourierWeightOutside theorem9_28SmallFamily theorem9_28Family fourierWeightAbove
  simp only [Finset.sum_filter]
  rw [← Finset.sum_add_distrib]
  apply Finset.sum_le_sum
  intro S _
  by_cases hJ : S ⊆ influentialCoordinates f (theorem9_28Threshold f ε k)
  · by_cases hk : S.card ≤ k
    · have hngt : ¬k < S.card := Nat.not_lt_of_ge hk
      simp [hJ, hk, hngt]
    · have hgt : k < S.card := Nat.lt_of_not_ge hk
      simp [hJ, hk, hgt]
  · by_cases hk : S.card ≤ k
    · have hngt : ¬k < S.card := Nat.not_lt_of_ge hk
      simp [hJ, hk, hngt]
    · have hgt : k < S.card := Nat.lt_of_not_ge hk
      simp [hJ, hk, hgt]

-- Source: FABL.Chapter09.Friedgut:361
/-- The second spectral-concentration conclusion of Theorem 9.28. -/
theorem theorem9_28_small_spectrum_concentrated
    (f : BooleanFunction n) {ε : ℝ} (hε : 0 < ε) (k : ℕ)
    (hI : 0 < totalInfluence f.toReal)
    (hdegree : IsFourierSpectrumConcentratedUpTo f.toReal ε k) :
    IsFourierSpectrumConcentratedOn f.toReal (2 * ε)
      (theorem9_28SmallFamily f ε k) := by
  have hfirst := theorem9_28_spectrum_concentrated f hε k hI
  unfold IsFourierSpectrumConcentratedOn at hfirst ⊢
  have htail : fourierWeightAbove k f.toReal ≤ ε := by
    simpa [IsFourierSpectrumConcentratedUpTo, fourierWeightAboveReal_natCast] using hdegree
  exact (fourierWeightOutside_theorem9_28SmallFamily_le_add f ε k).trans <| by
    linarith

/-! ## Boolean rounding of a coordinate projection -/

-- Source: FABL.Chapter09.Friedgut:377
/-- The conditional expectation of a Boolean function after retaining the coordinates in `J`. -/
noncomputable def booleanCoordinateProjection
    (f : BooleanFunction n) (J : Finset (Fin n)) : (FABL.SignCube (n)) → ℝ :=
  projectOnCoordinates (uniformPMF Sign) J f.toReal

-- Source: FABL.Chapter09.Friedgut:382
/-- Round the conditional expectation on `J` back to a Boolean `J`-junta. -/
noncomputable def coordinateJuntaApproximation
    (f : BooleanFunction n) (J : Finset (Fin n)) : BooleanFunction n :=
  fun x ↦ thresholdSign (booleanCoordinateProjection f J x)

-- Source: FABL.Chapter09.Friedgut:387
/-- The coordinate projection has the expected Walsh coefficient filter. -/
theorem fourierCoeff_booleanCoordinateProjection
    (f : BooleanFunction n) (J : Finset (Fin n)) (T : Finset (Fin n)) :
    fourierCoeff (booleanCoordinateProjection f J) T =
      if T ⊆ J then fourierCoeff f.toReal T else 0 := by
  let a : MultiIndex n (Fin 2) := (signMultiIndexEquivFinset n).symm T
  have ha : signMultiIndexSupport a = T := (signMultiIndexEquivFinset n).apply_symm_apply T
  have h := signSiteFourierBasis.fourierCoeff_projectOnCoordinates J f.toReal a
  rw [signSiteFourierBasis_fourierCoeff_eq_fourierCoeff,
    signSiteFourierBasis_fourierCoeff_eq_fourierCoeff] at h
  change fourierCoeff (projectOnCoordinates (uniformPMF Sign) J f.toReal)
      (signMultiIndexSupport a) =
    if signMultiIndexSupport a ⊆ J then
      fourierCoeff f.toReal (signMultiIndexSupport a) else 0 at h
  simpa [booleanCoordinateProjection, ha] using h

-- Source: FABL.Chapter09.Friedgut:403
/-- A Boolean function has uniform supremum norm one. -/
theorem productSupNorm_toReal_eq_one (f : BooleanFunction n) :
    productSupNorm f.toReal = 1 := by
  apply le_antisymm
  · unfold productSupNorm
    apply Finset.sup'_le
    intro x _
    rcases Int.units_eq_one_or (f x) with hx | hx <;>
      simp [BooleanFunction.toReal, signValue_one, signValue_neg_one, hx]
  · let x : (FABL.SignCube (n)) := fun _ ↦ 1
    calc
      (1 : ℝ) = |f.toReal x| := by
        rcases Int.units_eq_one_or (f x) with hx | hx <;>
          simp [BooleanFunction.toReal, signValue_one, signValue_neg_one, hx]
      _ ≤ productSupNorm f.toReal := abs_le_productSupNorm f.toReal x

-- Source: FABL.Chapter09.Friedgut:419
/-- Conditional expectations of Boolean functions stay in the interval `[-1,1]`. -/
theorem abs_booleanCoordinateProjection_le_one
    (f : BooleanFunction n) (J : Finset (Fin n)) (x : (FABL.SignCube (n))) :
    |booleanCoordinateProjection f J x| ≤ 1 := by
  rw [← productSupNorm_toReal_eq_one f]
  exact abs_projectOnCoordinates_le_productSupNorm
    (uniformPMF Sign) J f.toReal x

-- Source: FABL.Chapter09.Friedgut:427
/-- The rounded conditional expectation depends only on the retained coordinates. -/
theorem coordinateJuntaApproximation_dependsOnly
    (f : BooleanFunction n) (J : Finset (Fin n)) :
    DependsOnlyOnCoordinates (coordinateJuntaApproximation f J).toReal J := by
  intro x y hxy
  simp only [coordinateJuntaApproximation, BooleanFunction.toReal]
  apply congrArg signValue
  apply congrArg thresholdSign
  simpa [booleanCoordinateProjection] using
    (projectOnCoordinates_dependsOnly (uniformPMF Sign) J f.toReal hxy)

-- Source: FABL.Chapter09.Friedgut:438
/-- The rounded conditional expectation is a junta on at most `|J|` coordinates. -/
theorem coordinateJuntaApproximation_isKJunta
    (f : BooleanFunction n) (J : Finset (Fin n)) :
    IsKJunta (coordinateJuntaApproximation f J) J.card := by
  refine ⟨J, le_rfl, ?_⟩
  intro x y hxy
  unfold coordinateJuntaApproximation
  congr 1
  exact projectOnCoordinates_dependsOnly (uniformPMF Sign) J f.toReal hxy

-- Source: FABL.Chapter09.Friedgut:448
/-- Projection energy is one minus the Boolean Fourier mass outside subsets of `J`. -/
theorem uniformInner_booleanCoordinateProjection_self
    (f : BooleanFunction n) (J : Finset (Fin n)) :
    (FABL.uniformInner (booleanCoordinateProjection f J) (booleanCoordinateProjection f J)) =
      1 - fourierWeightOutside f.toReal {S | S ⊆ J} := by
  classical
  let inside := Finset.univ.filter fun S : Finset (Fin n) ↦ S ⊆ J
  let outside := Finset.univ.filter fun S : Finset (Fin n) ↦ ¬S ⊆ J
  have hinner :
      (FABL.uniformInner (booleanCoordinateProjection f J) (booleanCoordinateProjection f J)) =
        ∑ S ∈ inside, fourierCoeff f.toReal S ^ 2 := by
    rw [plancherel]
    simp_rw [fourierCoeff_booleanCoordinateProjection]
    dsimp [inside]
    rw [Finset.sum_filter]
    apply Finset.sum_congr rfl
    intro S _
    by_cases hS : S ⊆ J <;> simp [hS, pow_two]
  have hsplit :
      (∑ S ∈ inside, fourierCoeff f.toReal S ^ 2) +
          ∑ S ∈ outside, fourierCoeff f.toReal S ^ 2 = 1 := by
    have hpartition := Finset.sum_filter_add_sum_filter_not
      (Finset.univ : Finset (Finset (Fin n)))
      (fun S : Finset (Fin n) ↦ S ⊆ J)
      (fun S ↦ fourierCoeff f.toReal S ^ 2)
    rw [sum_sq_fourierCoeff_eq_one] at hpartition
    simpa [inside, outside] using hpartition
  rw [hinner]
  have houtside :
      fourierWeightOutside f.toReal {S | S ⊆ J} =
        ∑ S ∈ outside, fourierCoeff f.toReal S ^ 2 := by
    simp [fourierWeightOutside, fourierWeight, outside]
  rw [houtside]
  linarith

-- Source: FABL.Chapter09.Friedgut:483
/-- Self-adjointness of conditional expectation moves a `J`-junta from one side of the inner
product to the other. -/
theorem uniformInner_coordinateJuntaApproximation
    (f : BooleanFunction n) (J : Finset (Fin n)) :
    (FABL.uniformInner (f.toReal) ((coordinateJuntaApproximation f J).toReal)) =
      (FABL.uniformInner (booleanCoordinateProjection f J) ((coordinateJuntaApproximation f J).toReal)) := by
  have hdepends := coordinateJuntaApproximation_dependsOnly f J
  have hfixed := projectOnCoordinates_eq_self_of_dependsOnly
    (uniformPMF Sign) hdepends
  have hadjoint := projectOnCoordinates_selfAdjoint signSiteFourierBasis J
    f.toReal (coordinateJuntaApproximation f J).toReal
  rw [hfixed, productInner_uniformSign, productInner_uniformSign] at hadjoint
  simpa [booleanCoordinateProjection] using hadjoint

-- Source: FABL.Chapter09.Friedgut:498
/-- The rounded projection correlates with the projection by its expected absolute value. -/
theorem uniformInner_projection_rounding_eq_expect_abs
    (f : BooleanFunction n) (J : Finset (Fin n)) :
    (FABL.uniformInner (booleanCoordinateProjection f J) ((coordinateJuntaApproximation f J).toReal)) =
      𝔼 x, |booleanCoordinateProjection f J x| := by
  rw [uniformInner, RCLike.wInner_cWeight_eq_expect]
  apply Finset.expect_congr rfl
  intro x _
  simp only [RCLike.inner_apply, starRingEnd_apply, star_trivial,
    coordinateJuntaApproximation, BooleanFunction.toReal,
    signValue_thresholdSign]
  by_cases hx : 0 ≤ booleanCoordinateProjection f J x
  · simp [hx, abs_of_nonneg hx]
  · have hx' : booleanCoordinateProjection f J x < 0 := lt_of_not_ge hx
    simp [hx, abs_of_neg hx']

-- Source: FABL.Chapter09.Friedgut:515
/-- Expected absolute projection dominates its squared `L²` energy for Boolean inputs. -/
theorem uniformInner_projection_self_le_expect_abs
    (f : BooleanFunction n) (J : Finset (Fin n)) :
    (FABL.uniformInner (booleanCoordinateProjection f J) (booleanCoordinateProjection f J)) ≤
      𝔼 x, |booleanCoordinateProjection f J x| := by
  rw [uniformInner, RCLike.wInner_cWeight_eq_expect]
  apply Finset.expect_le_expect
  intro x _
  simp only [RCLike.inner_apply, starRingEnd_apply, star_trivial]
  have habs := abs_booleanCoordinateProjection_le_one f J x
  have habs0 := abs_nonneg (booleanCoordinateProjection f J x)
  nlinarith [sq_abs (booleanCoordinateProjection f J x)]

-- Source: FABL.Chapter09.Friedgut:528
/-- Exercise 3.34's rounding principle in the exact form used by Theorem 9.28: the nearest
Boolean `J`-junta has error at most half the Fourier weight outside subsets of `J`. -/
theorem two_mul_relativeHammingDist_coordinateJuntaApproximation_le
    (f : BooleanFunction n) (J : Finset (Fin n)) :
    2 * relativeHammingDist f (coordinateJuntaApproximation f J) ≤
      fourierWeightOutside f.toReal {S | S ⊆ J} := by
  have hcorrelation :=
    uniformInner_eq_one_sub_two_mul_relativeHammingDist f
      (coordinateJuntaApproximation f J)
  have hmove := uniformInner_coordinateJuntaApproximation f J
  have habs := uniformInner_projection_rounding_eq_expect_abs f J
  have henergy := uniformInner_projection_self_le_expect_abs f J
  have houtside := uniformInner_booleanCoordinateProjection_self f J
  linarith

-- Source: FABL.Chapter09.Friedgut:543
/-- Fourier weight outside a family is antitone in the family. -/
theorem fourierWeightOutside_antitone
    (f : (FABL.SignCube (n)) → ℝ) {A B : Set (Finset (Fin n))}
    (hAB : A ⊆ B) :
    fourierWeightOutside f B ≤ fourierWeightOutside f A := by
  classical
  unfold fourierWeightOutside
  apply Finset.sum_le_sum_of_subset_of_nonneg
  · intro S hS
    simp only [Finset.mem_filter, Finset.mem_univ, true_and] at hS ⊢
    intro hSA
    exact hS (hAB hSA)
  · intro S _ _
    exact sq_nonneg (fourierCoeff f S)

-- Source: FABL.Chapter09.Friedgut:593
/-- Vanishing total influence kills every nonconstant Walsh coefficient. -/
theorem fourierCoeff_eq_zero_of_totalInfluence_eq_zero
    (f : (FABL.SignCube (n)) → ℝ) (hI : totalInfluence f = 0)
    {S : Finset (Fin n)} (hS : S ≠ ∅) :
    fourierCoeff f S = 0 := by
  have hsum :
      (∑ T : Finset (Fin n), (T.card : ℝ) * fourierCoeff f T ^ 2) = 0 := by
    rw [← totalInfluence_eq_sum_card_mul_sq_fourierCoeff]
    exact hI
  have hterm : (S.card : ℝ) * fourierCoeff f S ^ 2 = 0 :=
    (Finset.sum_eq_zero_iff_of_nonneg fun T _ ↦
      mul_nonneg (Nat.cast_nonneg T.card) (sq_nonneg (fourierCoeff f T))).mp
        hsum S (Finset.mem_univ S)
  have hcard : 0 < (S.card : ℝ) := by
    exact_mod_cast Finset.card_pos.mpr (Finset.nonempty_iff_ne_empty.mpr hS)
  have hcardne : (S.card : ℝ) ≠ 0 := ne_of_gt hcard
  have hsquare : fourierCoeff f S ^ 2 = 0 :=
    (mul_eq_zero.mp hterm).resolve_left hcardne
  exact sq_eq_zero_iff.mp hsquare

-- Source: FABL.Chapter09.Friedgut:613
/-- A Boolean function of total influence zero is constant. -/
theorem eq_of_totalInfluence_toReal_eq_zero
    (f : BooleanFunction n) (hI : totalInfluence f.toReal = 0)
    (x y : (FABL.SignCube (n))) :
    f x = f y := by
  apply signValue_injective
  change f.toReal x = f.toReal y
  rw [fourier_expansion f.toReal x, fourier_expansion f.toReal y]
  apply Finset.sum_congr rfl
  intro S _
  by_cases hS : S = ∅
  · subst S
    simp [monomial]
  · rw [fourierCoeff_eq_zero_of_totalInfluence_eq_zero f.toReal hI hS]
    simp

-- Source: FABL.Chapter09.Friedgut:629
/-- A zero-influence Boolean function is a `0`-junta. -/
theorem isKJunta_zero_of_totalInfluence_eq_zero
    (f : BooleanFunction n) (hI : totalInfluence f.toReal = 0) :
    IsKJunta f 0 := by
  refine ⟨∅, by simp, ?_⟩
  intro x y _
  exact eq_of_totalInfluence_toReal_eq_zero f hI x y

-- Source: FABL.Chapter09.Friedgut:637
/-- A zero-influence Boolean function has all its spectrum on the empty character. -/
theorem spectrum_concentrated_on_empty_of_totalInfluence_eq_zero
    (f : BooleanFunction n) (hI : totalInfluence f.toReal = 0)
    {ε : ℝ} (hε : 0 ≤ ε) :
    IsFourierSpectrumConcentratedOn f.toReal ε {S | S ⊆ (∅ : Finset (Fin n))} := by
  unfold IsFourierSpectrumConcentratedOn
  have hzero :
      fourierWeightOutside f.toReal {S | S ⊆ (∅ : Finset (Fin n))} = 0 := by
    classical
    unfold fourierWeightOutside
    rw [Finset.sum_filter]
    apply Finset.sum_eq_zero
    intro S _
    by_cases hS : S = ∅
    · simp [hS]
    · simp [hS, fourierWeight,
        fourierCoeff_eq_zero_of_totalInfluence_eq_zero f.toReal hI hS]
  rw [hzero]
  exact hε

-- Source: FABL.Chapter09.Friedgut:657
/-- The integral degree cutoff used in Friedgut's Junta Theorem. -/
noncomputable def friedgutDegree (f : BooleanFunction n) (ε : ℝ) : ℕ :=
  ⌈totalInfluence f.toReal / ε⌉₊

-- Source: FABL.Chapter09.Friedgut:661
/-- Proposition 3.2 supplies Friedgut's low-degree concentration premise at the integral cutoff. -/
theorem spectrum_concentrated_up_to_friedgutDegree
    (f : BooleanFunction n) {ε : ℝ} (hε : 0 < ε) :
    IsFourierSpectrumConcentratedUpTo f.toReal ε (friedgutDegree f ε) := by
  apply (isFourierSpectrumConcentratedUpTo_totalInfluence_div f.toReal hε).mono_cutoff
  exact Nat.le_ceil _

-- Source: FABL.Chapter09.Friedgut:668
/-- Friedgut's influential coordinate set at the Markov degree cutoff. -/
noncomputable def friedgutCoordinates
    (f : BooleanFunction n) (ε : ℝ) : Finset (Fin n) :=
  influentialCoordinates f
    (theorem9_28Threshold f ε (friedgutDegree f ε))

-- Source: FABL.Chapter09.Friedgut:674
/-- The explicit finite bound underlying the book's `exp(O(I[f] / ε))` notation. The leading
one totalizes the bound for constant functions. -/
noncomputable def friedgutJuntaSizeBound
    (f : BooleanFunction n) (ε : ℝ) : ℝ :=
  1 + totalInfluence f.toReal ^ 3 / ε ^ 2 *
    (9 : ℝ) ^ friedgutDegree f ε

-- Source: FABL.Chapter09.Friedgut:681
/-- The explicit cardinality bound for Friedgut's coordinates in the nonconstant case. -/
theorem card_friedgutCoordinates_le
    (f : BooleanFunction n) {ε : ℝ} (hε : 0 < ε)
    (hI : 0 < totalInfluence f.toReal) :
    ((friedgutCoordinates f ε).card : ℝ) ≤
      totalInfluence f.toReal ^ 3 / ε ^ 2 *
        (9 : ℝ) ^ friedgutDegree f ε := by
  simpa [friedgutCoordinates] using
    card_theorem9_28_influentialCoordinates_le
      f hε (friedgutDegree f ε) hI

-- Source: FABL.Chapter09.Friedgut:692
/-- Friedgut's spectrum is concentrated on low-degree characters from its influential set. -/
theorem friedgut_spectrum_concentrated
    (f : BooleanFunction n) {ε : ℝ} (hε : 0 < ε)
    (hI : 0 < totalInfluence f.toReal) :
    IsFourierSpectrumConcentratedOn f.toReal (2 * ε)
      {S | S ⊆ friedgutCoordinates f ε ∧ S.card ≤ friedgutDegree f ε} := by
  simpa [friedgutCoordinates, theorem9_28SmallFamily] using
    theorem9_28_small_spectrum_concentrated f hε (friedgutDegree f ε) hI
      (spectrum_concentrated_up_to_friedgutDegree f hε)

-- Source: FABL.Chapter09.Friedgut:702
/-- The explicit rounded function in Friedgut's theorem is `ε`-close and depends only on the
influential coordinate set. -/
theorem friedgut_coordinateJunta_close
    (f : BooleanFunction n) {ε : ℝ} (hε : 0 < ε)
    (hI : 0 < totalInfluence f.toReal) :
    relativeHammingDist f
      (coordinateJuntaApproximation f (friedgutCoordinates f ε)) ≤ ε := by
  let k := friedgutDegree f ε
  let J := influentialCoordinates f (theorem9_28Threshold f ε k)
  have hsmall := theorem9_28_small_spectrum_concentrated f hε k hI
    (spectrum_concentrated_up_to_friedgutDegree f hε)
  have hfamilies : theorem9_28SmallFamily f ε k ⊆ {S | S ⊆ J} := by
    intro S hS
    exact hS.1
  have hsubsetMass :
      fourierWeightOutside f.toReal {S | S ⊆ J} ≤ 2 * ε :=
    (fourierWeightOutside_antitone f.toReal hfamilies).trans hsmall
  have hround := two_mul_relativeHammingDist_coordinateJuntaApproximation_le f J
  dsimp [friedgutCoordinates, k, J] at hround ⊢
  nlinarith

-- Source: FABL.Chapter09.Friedgut:723
/-- Friedgut's Junta Theorem, with the asymptotic junta size represented by the stronger explicit
bound obtained in Theorem 9.28. -/
theorem friedgut_junta
    (f : BooleanFunction n) {ε : ℝ} (hε : 0 < ε) :
    ∃ (J : Finset (Fin n)) (g : BooleanFunction n),
      (J.card : ℝ) ≤ friedgutJuntaSizeBound f ε ∧
      IsFourierSpectrumConcentratedOn f.toReal (2 * ε)
        {S | S ⊆ J ∧ S.card ≤ friedgutDegree f ε} ∧
      IsKJunta g J.card ∧ relativeHammingDist f g ≤ ε := by
  by_cases hIz : totalInfluence f.toReal = 0
  · refine ⟨∅, f, ?_, ?_, isKJunta_zero_of_totalInfluence_eq_zero f hIz, ?_⟩
    · simp [friedgutJuntaSizeBound, hIz]
    · have hfamily :
          {S : Finset (Fin n) | S ⊆ (∅ : Finset (Fin n))} =
            {S | S ⊆ (∅ : Finset (Fin n)) ∧ S.card ≤ friedgutDegree f ε} := by
          ext S
          simp only [Set.mem_setOf_eq, Finset.subset_empty]
          constructor
          · intro hS
            subst S
            simp
          · exact fun hS ↦ hS.1
      rw [← hfamily]
      exact spectrum_concentrated_on_empty_of_totalInfluence_eq_zero
        f hIz (show 0 ≤ 2 * ε by positivity)
    · simp [relativeHammingDist, hammingDist, hε.le]
  · have hI : 0 < totalInfluence f.toReal :=
      lt_of_le_of_ne (totalInfluence_nonneg f.toReal) (Ne.symm hIz)
    let J := friedgutCoordinates f ε
    let g := coordinateJuntaApproximation f J
    refine ⟨J, g, ?_, ?_, ?_, ?_⟩
    · have hcard := card_friedgutCoordinates_le f hε hI
      dsimp [J, friedgutJuntaSizeBound]
      linarith
    · simpa [J] using friedgut_spectrum_concentrated f hε hI
    · exact coordinateJuntaApproximation_isKJunta f J
    · simpa [J, g] using friedgut_coordinateJunta_close f hε hI

end FABL

end

/- Source fragment: Er579.FriedgutRegev.UniformFriedgut. Original licenses and source proofs retained. -/

section

/-! A dimension-independent Boolean junta bound obtained from the proved finite
Friedgut theorem. The parameter `M` bounds total uniform influence. -/

namespace Er579.FriedgutRegev

-- Source: Er579.FriedgutRegev.UniformFriedgut:10
noncomputable def uniformJuntaBound (M ε : ℝ) : ℕ :=
  ⌈1 + M ^ 3 / ε ^ 2 * (9 : ℝ) ^ ⌈M / ε⌉₊⌉₊

-- Source: Er579.FriedgutRegev.UniformFriedgut:13
theorem friedgut_size_bound_of_influence_bound {n : ℕ}
    (M ε : ℝ) (hM : 0 ≤ M) (hε : 0 < ε)
    (f : FABL.BooleanFunction n) (hf : FABL.totalInfluence f.toReal ≤ M) :
    FABL.friedgutJuntaSizeBound f ε ≤
      1 + M ^ 3 / ε ^ 2 * (9 : ℝ) ^ ⌈M / ε⌉₊ := by
  have hI : 0 ≤ FABL.totalInfluence f.toReal := FABL.totalInfluence_nonneg _
  have hdegree : FABL.friedgutDegree f ε ≤ ⌈M / ε⌉₊ := by
    unfold FABL.friedgutDegree
    exact Nat.ceil_mono (div_le_div_of_nonneg_right hf hε.le)
  have hcube : FABL.totalInfluence f.toReal ^ 3 ≤ M ^ 3 :=
    pow_le_pow_left₀ hI hf 3
  have hcoeff : FABL.totalInfluence f.toReal ^ 3 / ε ^ 2 ≤ M ^ 3 / ε ^ 2 :=
    div_le_div_of_nonneg_right hcube (sq_nonneg ε)
  have hpower : (9 : ℝ) ^ FABL.friedgutDegree f ε ≤ (9 : ℝ) ^ ⌈M / ε⌉₊ :=
    pow_le_pow_right₀ (by norm_num : (1 : ℝ) ≤ 9) hdegree
  unfold FABL.friedgutJuntaSizeBound
  exact add_le_add le_rfl (mul_le_mul hcoeff hpower
    (pow_nonneg (by norm_num) _)
    (div_nonneg (pow_nonneg hM _) (sq_nonneg ε)))

-- Source: Er579.FriedgutRegev.UniformFriedgut:33
/-- Uniform finite Boolean functions of bounded total influence admit a junta
approximation with a coordinate bound independent of the cube dimension. -/
theorem uniform_friedgut {n : ℕ} (M ε : ℝ) (hM : 0 ≤ M) (hε : 0 < ε)
    (f : FABL.BooleanFunction n) (hf : FABL.totalInfluence f.toReal ≤ M) :
    ∃ (J : Finset (Fin n)) (g : FABL.BooleanFunction n),
      J.card ≤ uniformJuntaBound M ε ∧
      DependsOn g (J : Set (Fin n)) ∧ FABL.relativeHammingDist f g ≤ ε := by
  obtain ⟨S, g, hS, _, hgjunta, herror⟩ := FABL.friedgut_junta f hε
  obtain ⟨J, hJ, hdepends⟩ := hgjunta
  refine ⟨J, g, ?_, hdepends, herror⟩
  have hbound : (J.card : ℝ) ≤ (uniformJuntaBound M ε : ℝ) := by
    calc
      (J.card : ℝ) ≤ S.card := by exact_mod_cast hJ
      _ ≤ FABL.friedgutJuntaSizeBound f ε := hS
      _ ≤ 1 + M ^ 3 / ε ^ 2 * (9 : ℝ) ^ ⌈M / ε⌉₊ :=
        friedgut_size_bound_of_influence_bound M ε hM hε f hf
      _ ≤ (uniformJuntaBound M ε : ℝ) := Nat.le_ceil _
  exact_mod_cast hbound

end Er579.FriedgutRegev

end

/- Source fragment: FABL.Chapter08.BiasedAnalysis. Original licenses and source proofs retained. -/

section

/-
Copyright (c) 2026 Asher Yan. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Asher Yan with Codex
-/

/-!
# Biased Fourier analysis

Book items: Definitions 8.39--8.40, Examples 8.41--8.42, Notation 8.43,
Definition 8.44, Proposition 8.45, Definition 8.46, Example 8.47,
the Margulis--Russo Formula, Remark 8.48, the internally proved majority part of
Example 8.49 (balance and critical probability), Definition 8.50, and Exercise 8.27.

The externally sourced clique/connectivity threshold asymptotics in Example 8.49 are deliberately
absent from the production dependency closure. The graph-property implementation below closes the
finite encoding and the edge-majority/parity structural examples; the remaining named graph
predicates stay book-facing Blueprint statements until their independent graph-theory development
is supplied. Exercises 8.23--8.26 and 8.28--8.31 are not claimed by this module.

The biased sign law is the existing one-coordinate resampling law at mean
`1 - 2p`.  The Fourier basis is obtained as a two-vector specialization of
the general finite-product basis from Section 8.1.
-/

open Finset Set
open scoped BigOperators

namespace FABL

variable {n : ℕ}

-- Source: FABL.Chapter08.BiasedAnalysis:41
/-- O'Donnell, Definition 8.39: the mean `μ = q - p = 1 - 2p`. -/
def biasMean (p : ℝ) : ℝ := 1 - 2 * p

-- Source: FABL.Chapter08.BiasedAnalysis:44
/-- O'Donnell, Definition 8.39: the variance scale `σ² = 4p(1-p)`. -/
def biasVarianceScale (p : ℝ) : ℝ := 4 * p * (1 - p)

-- Source: FABL.Chapter08.BiasedAnalysis:47
/-- O'Donnell, Definition 8.39: `σ = √(4p(1-p))`. -/
noncomputable def biasSigma (p : ℝ) : ℝ := Real.sqrt (biasVarianceScale p)

-- Source: FABL.Chapter08.BiasedAnalysis:50
theorem biasMean_mem_Icc (p : ℝ) (hp : p ∈ Set.Icc (0 : ℝ) 1) :
    biasMean p ∈ Set.Icc (-1 : ℝ) 1 := by
  constructor <;> simp only [biasMean] <;> linarith [hp.1, hp.2]

-- Source: FABL.Chapter08.BiasedAnalysis:54
theorem biasVarianceScale_nonneg (p : ℝ) (hp : p ∈ Set.Icc (0 : ℝ) 1) :
    0 ≤ biasVarianceScale p := by
  unfold biasVarianceScale
  exact mul_nonneg (mul_nonneg (by norm_num) hp.1) (sub_nonneg.mpr hp.2)

-- Source: FABL.Chapter08.BiasedAnalysis:59
theorem biasSigma_sq (p : ℝ) (hp : p ∈ Set.Icc (0 : ℝ) 1) :
    biasSigma p ^ 2 = biasVarianceScale p := by
  exact Real.sq_sqrt (biasVarianceScale_nonneg p hp)

-- Source: FABL.Chapter08.BiasedAnalysis:63
theorem biasSigma_pos (p : ℝ) (hp : p ∈ Set.Ioo (0 : ℝ) 1) :
    0 < biasSigma p := by
  rw [biasSigma]
  exact Real.sqrt_pos.2 <| by
    unfold biasVarianceScale
    exact mul_pos (mul_pos (by norm_num) hp.1) (sub_pos.mpr hp.2)

-- Source: FABL.Chapter08.BiasedAnalysis:70
/-- The book's `πₚ`: a sign is `-1` with probability `p` and `+1` with probability `1-p`. -/
noncomputable def biasedSignPMF (p : ℝ) (hp : p ∈ Set.Icc (0 : ℝ) 1) : PMF Sign :=
  coordinateNoisePMF (biasMean p) (biasMean_mem_Icc p hp) 1

-- Source: FABL.Chapter08.BiasedAnalysis:74
theorem biasedSignPMF_apply_one (p : ℝ) (hp : p ∈ Set.Icc (0 : ℝ) 1) :
    biasedSignPMF p hp 1 =
      (correlationKeepProbability (biasMean p) (biasMean_mem_Icc p hp) : ENNReal) := by
  classical
  simp [biasedSignPMF, coordinateNoisePMF, Finset.sum_filter]

-- Source: FABL.Chapter08.BiasedAnalysis:80
theorem biasedSignPMF_apply_neg_one (p : ℝ) (hp : p ∈ Set.Icc (0 : ℝ) 1) :
    biasedSignPMF p hp (-1) =
      1 - (correlationKeepProbability (biasMean p) (biasMean_mem_Icc p hp) : ENNReal) := by
  classical
  simp [biasedSignPMF, coordinateNoisePMF, Finset.sum_filter]

-- Source: FABL.Chapter08.BiasedAnalysis:86
/-- Point masses of the biased sign law, expressed as real probabilities. -/
theorem biasedSignPMF_apply_toReal (p : ℝ) (hp : p ∈ Set.Icc (0 : ℝ) 1)
    (x : Sign) :
    ((biasedSignPMF p hp x).toReal : ℝ) =
      if x = 1 then 1 - p else p := by
  rcases Int.units_eq_one_or x with rfl | rfl
  · rw [biasedSignPMF_apply_one]
    change (1 + biasMean p) / 2 = 1 - p
    rw [biasMean]
    ring
  · rw [biasedSignPMF_apply_neg_one]
    have hr : correlationKeepProbability (biasMean p) (biasMean_mem_Icc p hp) ≤ 1 :=
      correlationKeepProbability_le_one _ _
    have hrENN :
        (correlationKeepProbability (biasMean p) (biasMean_mem_Icc p hp) : ENNReal) ≤ 1 := by
      exact_mod_cast hr
    rw [ENNReal.toReal_sub_of_le hrENN (by simp), ENNReal.toReal_one, ENNReal.coe_toReal]
    change 1 - (1 + biasMean p) / 2 = p
    simp [biasMean]
    ring

-- Source: FABL.Chapter08.BiasedAnalysis:119
/-- The biased sign has mean `μ = 1 - 2p`. -/
theorem pmfExpectation_biasedSignPMF_signValue
    (p : ℝ) (hp : p ∈ Set.Icc (0 : ℝ) 1) :
    pmfExpectation (biasedSignPMF p hp) signValue = biasMean p := by
  exact pmfExpectation_coordinateNoisePMF_signValue (biasMean p)
    (biasMean_mem_Icc p hp) 1 |>.trans (by simp [signValue_one])

-- Source: FABL.Chapter08.BiasedAnalysis:126
/-- Definition 8.39's normalized centered one-bit function. -/
noncomputable def biasedStandardizedSign
    (p : ℝ) (x : Sign) : ℝ :=
  (signValue x - biasMean p) / biasSigma p

-- Source: FABL.Chapter08.BiasedAnalysis:131
theorem biasedStandardizedSign_one_eq
    (p : ℝ) :
    biasedStandardizedSign p 1 = 2 * p / biasSigma p := by
  unfold biasedStandardizedSign biasMean
  simp [signValue_one]

-- Source: FABL.Chapter08.BiasedAnalysis:137
theorem biasedStandardizedSign_neg_one_eq
    (p : ℝ) :
    biasedStandardizedSign p (-1) = -2 * (1 - p) / biasSigma p := by
  unfold biasedStandardizedSign biasMean
  simp [signValue_neg_one]
  ring

-- Source: FABL.Chapter08.BiasedAnalysis:180
/-- The standardized sign has mean zero. -/
theorem pmfExpectation_biasedStandardizedSign
    (p : ℝ) (hp : p ∈ Set.Ioo (0 : ℝ) 1) :
    pmfExpectation (biasedSignPMF p ⟨hp.1.le, hp.2.le⟩)
      (biasedStandardizedSign p) = 0 := by
  unfold biasedStandardizedSign
  rw [show (fun x : Sign ↦ (signValue x - biasMean p) / biasSigma p) =
      fun x ↦ (biasSigma p)⁻¹ * signValue x +
        (-(biasSigma p)⁻¹ * biasMean p) by
    funext x
    simp [div_eq_mul_inv]
    ring]
  rw [pmfExpectation_add, pmfExpectation_const_mul, pmfExpectation_const]
  rw [pmfExpectation_biasedSignPMF_signValue p ⟨hp.1.le, hp.2.le⟩]
  ring

-- Source: FABL.Chapter08.BiasedAnalysis:196
/-- The standardized sign has second moment one. -/
theorem pmfExpectation_biasedStandardizedSign_sq
    (p : ℝ) (hp : p ∈ Set.Ioo (0 : ℝ) 1) :
    pmfExpectation (biasedSignPMF p ⟨hp.1.le, hp.2.le⟩)
      (fun x ↦ biasedStandardizedSign p x ^ 2) = 1 := by
  classical
  unfold pmfExpectation
  rw [show (Finset.univ : Finset Sign) = {1, -1} by ext x; simp [Int.units_eq_one_or]]
  rw [Finset.sum_insert (by norm_num : (1 : Sign) ∉ {(-1 : Sign)}), Finset.sum_singleton]
  rw [biasedSignPMF_apply_toReal p ⟨hp.1.le, hp.2.le⟩ 1,
    biasedSignPMF_apply_toReal p ⟨hp.1.le, hp.2.le⟩ (-1)]
  simp only [if_pos, if_neg (by norm_num : (-1 : Sign) ≠ 1),
    biasedStandardizedSign, signValue_one, signValue_neg_one]
  have hs : biasSigma p ≠ 0 := ne_of_gt (biasSigma_pos p hp)
  simp only [div_pow]
  rw [biasSigma_sq p ⟨hp.1.le, hp.2.le⟩]
  unfold biasMean biasVarianceScale
  have hscale : 4 * p * (1 - p) ≠ 0 := by
    have hpos : 0 < 4 * p * (1 - p) :=
      mul_pos (mul_pos (by norm_num) hp.1) (sub_pos.mpr hp.2)
    exact ne_of_gt hpos
  have hden : p - p ^ 2 ≠ 0 := by
    have hpos : 0 < p * (1 - p) := mul_pos hp.1 (sub_pos.mpr hp.2)
    nlinarith
  have hprod : p * (1 - p) ≠ 0 :=
    ne_of_gt (mul_pos hp.1 (sub_pos.mpr hp.2))
  field_simp [hscale]
  rw [div_eq_iff hprod]
  ring

-- Source: FABL.Chapter08.BiasedAnalysis:226
/-- The two one-site functions `1, φ` from Definition 8.39. -/
noncomputable def biasedSiteFourierFunction
    (p : ℝ) (j : Fin 2) (x : Sign) : ℝ :=
  if j = 0 then 1 else biasedStandardizedSign p x

-- Source: FABL.Chapter08.BiasedAnalysis:231
/-- The biased one-site family is orthonormal. -/
theorem biasedSiteFourierFunction_orthonormal
    (p : ℝ) (hp : p ∈ Set.Ioo (0 : ℝ) 1) (a b : Fin 2) :
    pmfExpectation (biasedSignPMF p ⟨hp.1.le, hp.2.le⟩)
      (fun x ↦ biasedSiteFourierFunction p a x * biasedSiteFourierFunction p b x) =
      if a = b then 1 else 0 := by
  fin_cases a <;> fin_cases b
  · simp [biasedSiteFourierFunction, pmfExpectation_const]
  · simp [biasedSiteFourierFunction, pmfExpectation_biasedStandardizedSign p hp]
  · simp [biasedSiteFourierFunction, pmfExpectation_biasedStandardizedSign p hp]
  · simpa [biasedSiteFourierFunction, pow_two] using
      pmfExpectation_biasedStandardizedSign_sq p hp

-- Source: FABL.Chapter08.BiasedAnalysis:244
/-- The algebraic basis underlying the biased one-site Fourier basis. -/
noncomputable def biasedSiteBasis (p : ℝ) (hp : p ∈ Set.Ioo (0 : ℝ) 1) :
    Module.Basis (Fin 2) ℝ (Sign → ℝ) := by
  classical
  apply basisOfLinearIndependentOfCardEqFinrank
    (linearIndependent_of_pmf_orthonormal (biasedSiteFourierFunction p)
      (biasedSiteFourierFunction_orthonormal p hp))
  simp [Module.finrank_fintype_fun_eq_card, Sign]

-- Source: FABL.Chapter08.BiasedAnalysis:253
 theorem biasedSiteBasis_apply
    (p : ℝ) (hp : p ∈ Set.Ioo (0 : ℝ) 1) (j : Fin 2) :
    biasedSiteBasis p hp j = biasedSiteFourierFunction p j := by
  classical
  simp [biasedSiteBasis]

-- Source: FABL.Chapter08.BiasedAnalysis:259
/-- O'Donnell, Definitions 8.39--8.40: the biased single-site Fourier basis. -/
noncomputable def biasedSiteFourierBasis
    (p : ℝ) (hp : p ∈ Set.Ioo (0 : ℝ) 1) :
    FiniteFourierBasis Sign (biasedSignPMF p ⟨hp.1.le, hp.2.le⟩) (Fin 2) where
  zeroIndex := 0
  basis := biasedSiteBasis p hp
  basis_zero := by funext x; simp [biasedSiteBasis_apply, biasedSiteFourierFunction]
  orthonormal := by
    intro a b
    simpa only [biasedSiteBasis_apply] using
      biasedSiteFourierFunction_orthonormal p hp a b

-- Source: FABL.Chapter08.BiasedAnalysis:271
/-- The binary multi-index associated with a subset. -/
def subsetMultiIndex {n : ℕ} (S : Finset (Fin n)) : MultiIndex n (Fin 2) :=
  fun i ↦ if i ∈ S then 1 else 0

-- Source: FABL.Chapter08.BiasedAnalysis:311
/-- O'Donnell, Definition 8.40: the biased monomial `φ_S`. -/
noncomputable def biasedMonomial
    (p : ℝ) (hp : p ∈ Set.Ioo (0 : ℝ) 1)
    (S : Finset (Fin n)) (x : (FABL.SignCube (n))) : ℝ :=
  (biasedSiteFourierBasis p hp).productFunction (subsetMultiIndex S) x

-- Source: FABL.Chapter08.BiasedAnalysis:317
/-- O'Donnell, Definition 8.40: the `p`-biased Fourier coefficient. -/
noncomputable def biasedFourierCoeff
    (p : ℝ) (hp : p ∈ Set.Ioo (0 : ℝ) 1)
    (f : (FABL.SignCube (n)) → ℝ) (S : Finset (Fin n)) : ℝ :=
  (biasedSiteFourierBasis p hp).fourierCoeff f (subsetMultiIndex S)

-- Source: FABL.Chapter08.BiasedAnalysis:323
/-- The biased monomial is the product of standardized signs on `S`. -/
theorem biasedMonomial_apply
    (p : ℝ) (hp : p ∈ Set.Ioo (0 : ℝ) 1)
    (S : Finset (Fin n)) (x : (FABL.SignCube (n))) :
    biasedMonomial p hp S x = ∏ i ∈ S, biasedStandardizedSign p (x i) := by
  classical
  rw [biasedMonomial, FiniteFourierBasis.productFunction]
  simp only [biasedSiteFourierBasis, biasedSiteBasis_apply,
    biasedSiteFourierFunction, subsetMultiIndex]
  calc
    (∏ i, if (if i ∈ S then (1 : Fin 2) else 0) = 0 then
        1 else biasedStandardizedSign p (x i)) =
        ∏ i, if i ∈ S then biasedStandardizedSign p (x i) else 1 := by
      apply Finset.prod_congr rfl
      intro i _
      by_cases hi : i ∈ S <;> simp [hi]
    _ = ∏ i ∈ S, biasedStandardizedSign p (x i) := by simp

/-! ## Influences under the biased law -/

-- Source: FABL.Chapter08.BiasedAnalysis:567
/-- Expectation under the one-site biased sign law is the explicit two-point weighted average. -/
theorem pmfExpectation_biasedSignPMF
    (p : ℝ) (hp : p ∈ Set.Ioo (0 : ℝ) 1) (g : Sign → ℝ) :
    pmfExpectation (biasedSignPMF p ⟨hp.1.le, hp.2.le⟩) g =
      (1 - p) * g 1 + p * g (-1) := by
  classical
  unfold pmfExpectation
  rw [show (Finset.univ : Finset Sign) = {1, -1} by
    ext x
    simp [Int.units_eq_one_or]]
  rw [Finset.sum_insert (by norm_num : (1 : Sign) ∉ {(-1 : Sign)}),
    Finset.sum_singleton, biasedSignPMF_apply_toReal p ⟨hp.1.le, hp.2.le⟩ 1,
    biasedSignPMF_apply_toReal p ⟨hp.1.le, hp.2.le⟩ (-1)]
  simp

-- Source: FABL.Chapter08.BiasedAnalysis:582
/-- Pointwise form of Proposition 8.45: the conditional coordinate variance of a Boolean
function is `σ²` exactly when the coordinate is pivotal. -/
theorem coordinateConditionalVariance_biasedSignPMF_toReal
    (p : ℝ) (hp : p ∈ Set.Ioo (0 : ℝ) 1)
    (f : BooleanFunction n) (i : Fin n) (x : (FABL.SignCube (n))) :
    coordinateConditionalVariance (biasedSignPMF p ⟨hp.1.le, hp.2.le⟩)
        f.toReal i x =
      biasSigma p ^ 2 *
        (if f x ≠ f (flipCoordinate x i) then (1 : ℝ) else 0) := by
  let xplus := setCoordinate x i 1
  let xminus := setCoordinate x i (-1)
  have hplusSet : replaceCoordinate x i 1 = xplus := rfl
  have hminusSet : replaceCoordinate x i (-1) = xminus := rfl
  rcases Int.units_eq_one_or (f xplus) with hfp | hfp <;>
    rcases Int.units_eq_one_or (f xminus) with hfm | hfm <;>
      rcases Int.units_eq_one_or (x i) with hxi | hxi
  all_goals
    have hxself : setCoordinate x i (x i) = x := setCoordinate_eq_self x i
    have hxcurrent : (if x i = 1 then xplus else xminus) = x := by
      rcases Int.units_eq_one_or (x i) with hx | hx
      · simpa [hx, xplus] using hxself
      · simpa [hx, xminus] using hxself
    have hfx : f x = if x i = 1 then f xplus else f xminus := by
      by_cases hxone : x i = 1
      · have hxpeq : xplus = x := by
          simpa [xplus, hxone] using hxself
        simp [hxone, hxpeq]
      · have hxneg : x i = -1 := (Int.units_eq_one_or (x i)).resolve_left hxone
        have hxmeq : xminus = x := by
          simpa [xminus, hxneg] using hxself
        simp [hxone, hxmeq]
    have hflip :
        flipCoordinate x i = if x i = 1 then xminus else xplus := by
      funext j
      by_cases hji : j = i
      · subst j
        rcases Int.units_eq_one_or (x i) with hx | hx <;>
          simp [flipCoordinate, xplus, xminus, setCoordinate, hx]
      · simp [flipCoordinate, xplus, xminus, setCoordinate,
          Function.update_of_ne hji, hxi]
    unfold coordinateConditionalVariance
    rw [pmfExpectation_biasedSignPMF p hp]
    simp only [hplusSet, hminusSet]
    rw [pmfExpectation_biasedSignPMF p hp]
    simp only [hplusSet, hminusSet]
    simp [BooleanFunction.toReal, signValue_one, signValue_neg_one, hfp, hfm, hxi, hfx, xplus, xminus, hflip,
      biasSigma_sq p ⟨hp.1.le, hp.2.le⟩, biasVarianceScale] <;>
      ring

-- Source: FABL.Chapter08.BiasedAnalysis:631
/-- Probability that flipping coordinate `i` changes a Boolean function under the biased product
law. -/
noncomputable def biasedFlipProbability
    (p : ℝ) (hp : p ∈ Set.Ioo (0 : ℝ) 1)
    (f : BooleanFunction n) (i : Fin n) : ℝ :=
  productMean (biasedSignPMF p ⟨hp.1.le, hp.2.le⟩) fun x ↦
    if f x ≠ f (flipCoordinate x i) then 1 else 0

-- Source: FABL.Chapter08.BiasedAnalysis:639
/-- Proposition 8.45: generalized influence equals `σ²` times deterministic-flip
probability. -/
theorem productInfluence_biased_eq_sigma_sq_mul_flipProbability
    (p : ℝ) (hp : p ∈ Set.Ioo (0 : ℝ) 1)
    (f : BooleanFunction n) (i : Fin n) :
    productInfluence (biasedSignPMF p ⟨hp.1.le, hp.2.le⟩) f.toReal i =
      biasSigma p ^ 2 * biasedFlipProbability p hp f i := by
  let B := biasedSiteFourierBasis p hp
  rw [B.productInfluence_eq_expect_coordinateConditionalVariance]
  unfold biasedFlipProbability productMean
  rw [show coordinateConditionalVariance
      (biasedSignPMF p ⟨hp.1.le, hp.2.le⟩) f.toReal i =
      fun x ↦ biasSigma p ^ 2 *
        (if f x ≠ f (flipCoordinate x i) then (1 : ℝ) else 0) by
    funext x
    exact coordinateConditionalVariance_biasedSignPMF_toReal p hp f i x]
  exact pmfExpectation_const_mul _ _ _

-- Source: FABL.Chapter08.BiasedAnalysis:695
/-- Flip probability is the biased expectation of the squared canonical discrete derivative. -/
theorem biasedFlipProbability_eq_expect_sq_discreteDerivative
    (p : ℝ) (hp : p ∈ Set.Ioo (0 : ℝ) 1)
    (f : BooleanFunction n) (i : Fin n) :
    biasedFlipProbability p hp f i =
      productMean (biasedSignPMF p ⟨hp.1.le, hp.2.le⟩)
        (fun x ↦ discreteDerivative i f.toReal x ^ 2) := by
  unfold biasedFlipProbability productMean
  apply congrArg (pmfExpectation _)
  funext x
  rw [sq_discreteDerivative_toReal_eq_pivotalIndicator]
  by_cases h : f x = f (flipCoordinate x i) <;>
    simp [pivotalIndicator, IsPivotal, h]

-- Source: FABL.Chapter08.BiasedAnalysis:709
/-- The singleton biased Fourier coefficient is `σ` times the biased mean of the canonical
discrete derivative. -/
theorem biasedFourierCoeff_singleton_eq_sigma_mul_expect_discreteDerivative
    (p : ℝ) (hp : p ∈ Set.Ioo (0 : ℝ) 1)
    (f : (FABL.SignCube (n)) → ℝ) (i : Fin n) :
    biasedFourierCoeff p hp f {i} =
      biasSigma p *
        productMean (biasedSignPMF p ⟨hp.1.le, hp.2.le⟩)
          (discreteDerivative i f) := by
  let law := biasedSignPMF p ⟨hp.1.le, hp.2.le⟩
  let B := biasedSiteFourierBasis p hp
  let h : ProductL2 Sign n := fun x ↦ f x * biasedMonomial p hp {i} x
  have hprojection : coordinateProjection law i h =
      biasSigma p • discreteDerivative i f := by
    funext x
    rw [coordinateProjection_apply, pmfExpectation_biasedSignPMF p hp]
    simp only [h, replaceCoordinate, biasedMonomial_apply, Finset.prod_singleton]
    simp only [Function.update_self]
    rw [biasedStandardizedSign_one_eq, biasedStandardizedSign_neg_one_eq]
    have hs : biasSigma p ≠ 0 := ne_of_gt (biasSigma_pos p hp)
    have hs2 := biasSigma_sq p ⟨hp.1.le, hp.2.le⟩
    simp only [Pi.smul_apply, smul_eq_mul, discreteDerivative_apply]
    field_simp [hs]
    rw [hs2]
    unfold biasVarianceScale
    simp only [setCoordinate]
    ring
  unfold biasedFourierCoeff FiniteFourierBasis.fourierCoeff productMean
  change pmfExpectation (productProbabilityPMF law n) h =
    biasSigma p * pmfExpectation (productProbabilityPMF law n) (discreteDerivative i f)
  calc
    pmfExpectation (productProbabilityPMF law n) h =
        productMean law (coordinateProjection law i h) := by
      simpa [law, B, productMean, coordinateProjection] using
        ((biasedSiteFourierBasis p hp).productMean_projectOnCoordinates
          (Finset.univ.erase i) h).symm
    _ = productMean law (biasSigma p • discreteDerivative i f) := by rw [hprojection]
    _ = biasSigma p * productMean law (discreteDerivative i f) :=
      productMean_smul law (biasSigma p) _

-- Source: FABL.Chapter08.BiasedAnalysis:749
/-- Proposition 8.45, monotone case: influence is `σ` times the singleton coefficient. -/
theorem productInfluence_biased_eq_sigma_mul_singletonCoeff_of_monotone
    (p : ℝ) (hp : p ∈ Set.Ioo (0 : ℝ) 1)
    (f : BooleanFunction n) (hf : Monotone f) (i : Fin n) :
    productInfluence (biasedSignPMF p ⟨hp.1.le, hp.2.le⟩) f.toReal i =
      biasSigma p * biasedFourierCoeff p hp f.toReal {i} := by
  rw [productInfluence_biased_eq_sigma_sq_mul_flipProbability p hp f i,
    biasedFlipProbability_eq_expect_sq_discreteDerivative p hp f i]
  have hsq : (fun x ↦ discreteDerivative i f.toReal x ^ 2) =
      discreteDerivative i f.toReal := by
    funext x
    exact sq_discreteDerivative_toReal_eq_self_of_monotone f hf i x
  rw [hsq,
    biasedFourierCoeff_singleton_eq_sigma_mul_expect_discreteDerivative p hp f.toReal i]
  ring

/-! ## Encoded finite graph properties -/

/-! ## Margulis--Russo calculus -/

-- Source: FABL.Chapter08.BiasedAnalysis:865
/-- Uniform Walsh monomials have moment `μ^|S|` under the `p`-biased product law. -/
theorem productMean_biasedSignPMF_monomial
    (p : ℝ) (hp : p ∈ Set.Icc (0 : ℝ) 1)
    (S : Finset (Fin n)) :
    productMean (biasedSignPMF p hp) (monomial S) =
      biasMean p ^ S.card := by
  classical
  let law := biasedSignPMF p hp
  let q : (i : Fin n) → Sign → ℝ := fun i x ↦ if i ∈ S then signValue x else 1
  have hmonomial : (monomial S : (FABL.SignCube (n)) → ℝ) = fun x ↦ ∏ i, q i (x i) := by
    funext x
    rw [monomial]
    simp [q]
  unfold productMean
  rw [hmonomial, productProbabilityPMF,
    pmfExpectation_independentProductPMF_prod (fun _ : Fin n ↦ law) q]
  have hfactor (i : Fin n) : pmfExpectation law (q i) =
      if i ∈ S then biasMean p else 1 := by
    by_cases hi : i ∈ S
    · simp [q, hi, law, pmfExpectation_biasedSignPMF_signValue]
    · simp [q, hi, pmfExpectation_const]
  simp_rw [hfactor]
  rw [Fintype.prod_ite_mem]
  simp

-- Source: FABL.Chapter08.BiasedAnalysis:890
/-- The finite polynomial giving `𝔼[f]` as a function of the common coordinate mean `μ`. -/
noncomputable def biasedExpectationPolynomial
    (f : (FABL.SignCube (n)) → ℝ) (μ : ℝ) : ℝ :=
  ∑ S, μ ^ S.card * fourierCoeff f S

-- Source: FABL.Chapter08.BiasedAnalysis:895
/-- Evaluation of the expectation polynomial at `μ = 1-2p` is the actual biased
expectation. -/
theorem biasedExpectationPolynomial_biasMean
    (p : ℝ) (hp : p ∈ Set.Icc (0 : ℝ) 1)
    (f : (FABL.SignCube (n)) → ℝ) :
    biasedExpectationPolynomial f (biasMean p) =
      productMean (biasedSignPMF p hp) f := by
  classical
  let law := biasedSignPMF p hp
  unfold biasedExpectationPolynomial productMean
  calc
    (∑ S, biasMean p ^ S.card * fourierCoeff f S) =
        ∑ S, fourierCoeff f S *
          pmfExpectation (productProbabilityPMF law n) (monomial S) := by
      apply Finset.sum_congr rfl
      intro S _
      rw [← productMean_biasedSignPMF_monomial p hp S]
      change productMean (biasedSignPMF p hp) (monomial S) *
        fourierCoeff f S = fourierCoeff f S *
          productMean law (monomial S)
      simp [law, mul_comm]
    _ = pmfExpectation (productProbabilityPMF law n)
        (fun x ↦ ∑ S, fourierCoeff f S * monomial S x) := by
      rw [pmfExpectation_sum]
      apply Finset.sum_congr rfl
      intro S _
      rw [pmfExpectation_const_mul]
    _ = pmfExpectation (productProbabilityPMF law n) f := by
      apply congrArg (pmfExpectation (productProbabilityPMF law n))
      funext x
      exact (fourier_expansion f x).symm

-- Source: FABL.Chapter08.BiasedAnalysis:927
/-- The derivative of the finite expectation polynomial. -/
theorem hasDerivAt_biasedExpectationPolynomial
    (f : (FABL.SignCube (n)) → ℝ) (μ : ℝ) :
    HasDerivAt (biasedExpectationPolynomial f)
      (∑ S, (S.card : ℝ) * μ ^ (S.card - 1) * fourierCoeff f S) μ := by
  unfold biasedExpectationPolynomial
  apply HasDerivAt.fun_sum
  intro S _
  simpa [mul_assoc] using
    (hasDerivAt_pow S.card μ).mul_const (fourierCoeff f S)

-- Source: FABL.Chapter08.BiasedAnalysis:938
/-- Biased expectation of a canonical discrete derivative in uniform Fourier coordinates. -/
theorem productMean_biasedSignPMF_discreteDerivative
    (p : ℝ) (hp : p ∈ Set.Ioo (0 : ℝ) 1)
    (f : (FABL.SignCube (n)) → ℝ) (i : Fin n) :
    productMean (biasedSignPMF p ⟨hp.1.le, hp.2.le⟩)
        (discreteDerivative i f) =
      ∑ S with i ∈ S,
        fourierCoeff f S * biasMean p ^ (S.card - 1) := by
  classical
  let law := biasedSignPMF p ⟨hp.1.le, hp.2.le⟩
  unfold productMean
  have hfun : discreteDerivative i f = fun x ↦
      ∑ S, if i ∈ S then fourierCoeff f S * monomial (S.erase i) x else 0 := by
    funext x
    rw [discreteDerivative_eq_fourier_sum, Finset.sum_filter]
  rw [hfun, pmfExpectation_sum, Finset.sum_filter]
  apply Finset.sum_congr rfl
  intro S _
  by_cases hi : i ∈ S
  · simp only [hi, if_true]
    rw [pmfExpectation_const_mul]
    rw [show pmfExpectation (productProbabilityPMF law n) (monomial (S.erase i)) =
        productMean law (monomial (S.erase i)) by rfl,
      productMean_biasedSignPMF_monomial p ⟨hp.1.le, hp.2.le⟩,
      Finset.card_erase_of_mem hi]
  · simp [hi, pmfExpectation_const]

-- Source: FABL.Chapter08.BiasedAnalysis:965
/-- Summing biased derivative means gives the formal derivative of the expectation
polynomial. -/
theorem sum_productMean_biasedSignPMF_discreteDerivative
    (p : ℝ) (hp : p ∈ Set.Ioo (0 : ℝ) 1)
    (f : (FABL.SignCube (n)) → ℝ) :
    ∑ i, productMean (biasedSignPMF p ⟨hp.1.le, hp.2.le⟩)
        (discreteDerivative i f) =
      ∑ S, (S.card : ℝ) * biasMean p ^ (S.card - 1) * fourierCoeff f S := by
  classical
  simp_rw [productMean_biasedSignPMF_discreteDerivative p hp f,
    Finset.sum_filter]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro S _
  rw [show (∑ i, if i ∈ S then
      fourierCoeff f S * biasMean p ^ (S.card - 1) else 0) =
      (S.card : ℝ) *
        (fourierCoeff f S * biasMean p ^ (S.card - 1)) by
    calc
      (∑ i, if i ∈ S then fourierCoeff f S * biasMean p ^ (S.card - 1) else 0) =
          ∑ i ∈ S, fourierCoeff f S * biasMean p ^ (S.card - 1) := by
        simp [Finset.sum_ite_mem]
      _ = (S.card : ℝ) *
          (fourierCoeff f S * biasMean p ^ (S.card - 1)) := by simp]
  ring

-- Source: FABL.Chapter08.BiasedAnalysis:991
/-- Margulis--Russo Formula (8.8): exact derivative with respect to `μ`. -/
theorem hasDerivAt_biasedExpectationPolynomial_eq_singletons
    (p : ℝ) (hp : p ∈ Set.Ioo (0 : ℝ) 1)
    (f : (FABL.SignCube (n)) → ℝ) :
    HasDerivAt (biasedExpectationPolynomial f)
      ((biasSigma p)⁻¹ * ∑ i, biasedFourierCoeff p hp f {i})
      (biasMean p) := by
  have hbase := hasDerivAt_biasedExpectationPolynomial f (biasMean p)
  convert hbase using 1
  rw [← sum_productMean_biasedSignPMF_discreteDerivative p hp f]
  simp_rw [biasedFourierCoeff_singleton_eq_sigma_mul_expect_discreteDerivative p hp f]
  rw [← Finset.mul_sum]
  have hs : biasSigma p ≠ 0 := ne_of_gt (biasSigma_pos p hp)
  field_simp [hs]

-- Source: FABL.Chapter08.BiasedAnalysis:1006
/-- The probability that a Boolean function has sign `-1`, under the actual biased law. -/
noncomputable def biasedMinusProbability
    (p : ℝ) (hp : p ∈ Set.Icc (0 : ℝ) 1)
    (f : BooleanFunction n) : ℝ :=
  productMean (biasedSignPMF p hp) fun x ↦ if f x = -1 then 1 else 0

-- Source: FABL.Chapter08.BiasedAnalysis:1012
/-- A globally defined finite polynomial for the biased `-1` probability. -/
noncomputable def biasedMinusProbabilityPolynomial
    (f : BooleanFunction n) (p : ℝ) : ℝ :=
  (1 - biasedExpectationPolynomial f.toReal (biasMean p)) / 2

-- Source: FABL.Chapter08.BiasedAnalysis:1017
/-- Expected sign equals one minus twice the probability of sign `-1`. -/
theorem productMean_toReal_eq_one_sub_two_mul_minusProbability
    {Ω : Type*} [Fintype Ω] (law : PMF Ω) (f : Ω → Sign) :
    pmfExpectation law (fun x ↦ signValue (f x)) =
      1 - 2 * pmfExpectation law (fun x ↦ if f x = -1 then 1 else 0) := by
  have hpoint : (fun x ↦ signValue (f x)) =
    (fun _ ↦ (1 : ℝ)) + (-2 : ℝ) •
        (fun x ↦ if f x = -1 then (1 : ℝ) else 0) := by
    funext x
    rcases Int.units_eq_one_or (f x) with hx | hx
    · simp [signValue_one, signValue_neg_one, hx]
    · simp [signValue_one, signValue_neg_one, hx]
      norm_num
  rw [hpoint, pmfExpectation_add_fun, pmfExpectation_const,
    pmfExpectation_smul_fun]
  ring

-- Source: FABL.Chapter08.BiasedAnalysis:1034
/-- The probability polynomial agrees with the actual biased probability throughout `[0,1]`. -/
theorem biasedMinusProbabilityPolynomial_eq
    (p : ℝ) (hp : p ∈ Set.Icc (0 : ℝ) 1)
    (f : BooleanFunction n) :
    biasedMinusProbabilityPolynomial f p = biasedMinusProbability p hp f := by
  unfold biasedMinusProbabilityPolynomial biasedMinusProbability
  rw [biasedExpectationPolynomial_biasMean p hp]
  have hsign := productMean_toReal_eq_one_sub_two_mul_minusProbability
    (productProbabilityPMF (biasedSignPMF p hp) n) f
  change (1 - productMean (biasedSignPMF p hp) f.toReal) / 2 = _
  unfold productMean at hsign ⊢
  have hsign' :
      pmfExpectation (productProbabilityPMF (biasedSignPMF p hp) n) f.toReal =
        1 - 2 * pmfExpectation (productProbabilityPMF (biasedSignPMF p hp) n)
          (fun x ↦ if f x = -1 then 1 else 0) := by
    change pmfExpectation (productProbabilityPMF (biasedSignPMF p hp) n)
      (fun x ↦ signValue (f x)) = _
    exact hsign
  rw [hsign']
  ring

-- Source: FABL.Chapter08.BiasedAnalysis:1055
/-- The `p`-derivative of the `-1` probability polynomial is the Margulis--Russo singleton
sum. -/
theorem hasDerivAt_biasedMinusProbabilityPolynomial
    (p : ℝ) (hp : p ∈ Set.Ioo (0 : ℝ) 1)
    (f : BooleanFunction n) :
    HasDerivAt (biasedMinusProbabilityPolynomial f)
      ((biasSigma p)⁻¹ * ∑ i, biasedFourierCoeff p hp f.toReal {i}) p := by
  have harg : HasDerivAt biasMean (-2) p := by
    change HasDerivAt (fun t : ℝ ↦ 1 - 2 * t) (-2) p
    simpa using ((hasDerivAt_id p).const_mul 2).const_sub 1
  have hcomp :=
    (hasDerivAt_biasedExpectationPolynomial_eq_singletons p hp f.toReal).comp p harg
  have hresult := ((hasDerivAt_const p 1).sub hcomp).div_const 2
  change HasDerivAt
    (fun t ↦ (1 - biasedExpectationPolynomial f.toReal (biasMean t)) / 2) _ p
  convert hresult using 1 <;> try rfl
  ring

-- Source: FABL.Chapter08.BiasedAnalysis:1073
/-- Margulis--Russo Formula (8.9): for monotone Boolean functions the `p`-derivative is
`I[f]/σ²`. -/
theorem hasDerivAt_biasedMinusProbabilityPolynomial_eq_totalInfluence
    (p : ℝ) (hp : p ∈ Set.Ioo (0 : ℝ) 1)
    (f : BooleanFunction n) (hf : Monotone f) :
    HasDerivAt (biasedMinusProbabilityPolynomial f)
      (productTotalInfluence (biasedSignPMF p ⟨hp.1.le, hp.2.le⟩) f.toReal /
        biasSigma p ^ 2) p := by
  have hbase := hasDerivAt_biasedMinusProbabilityPolynomial p hp f
  convert hbase using 1
  have hinf :
      productTotalInfluence (biasedSignPMF p ⟨hp.1.le, hp.2.le⟩) f.toReal =
        biasSigma p * ∑ i, biasedFourierCoeff p hp f.toReal {i} := by
    unfold productTotalInfluence
    simp_rw [productInfluence_biased_eq_sigma_mul_singletonCoeff_of_monotone p hp f hf]
    rw [Finset.mul_sum]
  rw [hinf]
  have hs : biasSigma p ≠ 0 := ne_of_gt (biasSigma_pos p hp)
  field_simp [hs]

-- Source: FABL.Chapter08.BiasedAnalysis:1168
/-- The biased `-1` probability polynomial is continuous. -/
theorem continuous_biasedMinusProbabilityPolynomial
    (f : BooleanFunction n) :
    Continuous (biasedMinusProbabilityPolynomial f) := by
  unfold biasedMinusProbabilityPolynomial biasedExpectationPolynomial biasMean
  fun_prop

/-! ## The internally proved majority part of Example 8.49 -/

-- Source: FABL.Chapter08.BiasedAnalysis:1399
/-- At `p=1/2`, the biased sign law is the uniform sign law. -/
theorem biasedSignPMF_one_half_eq_uniform :
    biasedSignPMF (1 / 2 : ℝ) (by constructor <;> norm_num) = uniformPMF Sign := by
  ext x
  rw [← ENNReal.toReal_eq_toReal_iff'
    ((biasedSignPMF (1 / 2 : ℝ) (by constructor <;> norm_num)).apply_ne_top x)
    ((uniformPMF Sign).apply_ne_top x)]
  rw [biasedSignPMF_apply_toReal (1 / 2) (by constructor <;> norm_num) x]
  rcases Int.units_eq_one_or x with hx | hx <;> subst x <;>
    norm_num [uniformPMF, PMF.uniformOfFintype_apply, Fintype.card_units_int]

end FABL

end

end

/- Source fragment: Er579.RandomRealization.FiniteProbability. Original licenses and source proofs retained. -/

section

/-!
Finite probability calculations used by the two random realizations.
All probabilities are finite weighted sums. No probabilistic existence
principle is assumed: a normalized total weight and a strict bad-event
bound directly produce an actual finite outcome.
-/

namespace Er579.RandomRealization

open scoped BigOperators Classical

section FiniteProbability

variable {Ω : Type*} [Fintype Ω]

-- Source: Er579.RandomRealization.FiniteProbability:20
noncomputable def eventWeight (w : Ω → ℝ) (E : Ω → Prop) : ℝ := by
  classical
  exact ∑ ω, if E ω then w ω else 0

-- Source: Er579.RandomRealization.FiniteProbability:24
def finiteExpectation (w : Ω → ℝ) (f : Ω → ℝ) : ℝ :=
  ∑ ω, w ω * f ω

-- Source: Er579.RandomRealization.FiniteProbability:27
theorem finiteExpectation_add (w : Ω → ℝ) (f g : Ω → ℝ) :
    finiteExpectation w (fun ω => f ω + g ω) = finiteExpectation w f + finiteExpectation w g := by
  unfold finiteExpectation
  simp only [mul_add, Finset.sum_add_distrib]

-- Source: Er579.RandomRealization.FiniteProbability:32
theorem finiteExpectation_const_mul (w : Ω → ℝ) (f : Ω → ℝ) (a : ℝ) :
    finiteExpectation w (fun ω => a * f ω) = a * finiteExpectation w f := by
  unfold finiteExpectation
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro ω _
  ring

-- Source: Er579.RandomRealization.FiniteProbability:40
theorem finiteExpectation_sum {ι : Type*} (w : Ω → ℝ) (s : Finset ι)
    (f : ι → Ω → ℝ) :
    finiteExpectation w (fun ω => ∑ i ∈ s, f i ω) = ∑ i ∈ s, finiteExpectation w (f i) := by
  unfold finiteExpectation
  simp_rw [Finset.mul_sum]
  exact Finset.sum_comm

-- Source: Er579.RandomRealization.FiniteProbability:47
theorem eventWeight_eq_expect_indicator (w : Ω → ℝ) (E : Ω → Prop) :
    eventWeight w E = finiteExpectation w (fun ω => if E ω then 1 else 0) := by
  classical
  unfold eventWeight finiteExpectation
  apply Finset.sum_congr rfl
  intro ω _
  by_cases h : E ω <;> simp [h]

-- Source: Er579.RandomRealization.FiniteProbability:55
theorem eventWeight_nonneg (w : Ω → ℝ) (hw : ∀ ω, 0 ≤ w ω) (E : Ω → Prop) :
    0 ≤ eventWeight w E := by
  classical
  unfold eventWeight
  apply Finset.sum_nonneg
  intro ω _
  split_ifs
  · exact hw ω
  · exact le_rfl

-- Source: Er579.RandomRealization.FiniteProbability:65
theorem eventWeight_mono (w : Ω → ℝ) (hw : ∀ ω, 0 ≤ w ω)
    {E F : Ω → Prop} (hEF : ∀ ω, E ω → F ω) :
    eventWeight w E ≤ eventWeight w F := by
  classical
  unfold eventWeight
  apply Finset.sum_le_sum
  intro ω _
  by_cases hE : E ω
  · simp only [if_pos hE, if_pos (hEF ω hE)]
    exact le_rfl
  · simp only [if_neg hE]
    split_ifs
    · exact hw ω
    · exact le_rfl

-- Source: Er579.RandomRealization.FiniteProbability:80
theorem eventWeight_or_le (w : Ω → ℝ) (hw : ∀ ω, 0 ≤ w ω)
    (E F : Ω → Prop) :
    eventWeight w (fun ω => E ω ∨ F ω) ≤ eventWeight w E + eventWeight w F := by
  classical
  unfold eventWeight
  rw [← Finset.sum_add_distrib]
  apply Finset.sum_le_sum
  intro ω _
  by_cases hE : E ω
  · by_cases hF : F ω
    · rw [if_pos (Or.inl hE), if_pos hE, if_pos hF]
      linarith [hw ω]
    · rw [if_pos (Or.inl hE), if_pos hE, if_neg hF, add_zero]
  · by_cases hF : F ω
    · rw [if_pos (Or.inr hF), if_neg hE, if_pos hF, zero_add]
    · rw [if_neg (not_or.mpr ⟨hE, hF⟩), if_neg hE, if_neg hF, add_zero]

-- Source: Er579.RandomRealization.FiniteProbability:97
theorem exists_outside_event (w : Ω → ℝ) (hnorm : ∑ ω, w ω = 1)
    (E : Ω → Prop) (hE : eventWeight w E < 1) : ∃ ω, ¬ E ω := by
  classical
  by_contra! h
  have : eventWeight w E = 1 := by
    simpa only [eventWeight, if_pos (h _)] using hnorm
  linarith

-- Source: Er579.RandomRealization.FiniteProbability:105
theorem exists_avoiding_two (w : Ω → ℝ) (hw : ∀ ω, 0 ≤ w ω)
    (hnorm : ∑ ω, w ω = 1) (E F : Ω → Prop)
    (hEF : eventWeight w E + eventWeight w F < 1) :
    ∃ ω, ¬ E ω ∧ ¬ F ω := by
  have hbad : eventWeight w (fun ω => E ω ∨ F ω) < 1 :=
    lt_of_le_of_lt (eventWeight_or_le w hw E F) hEF
  obtain ⟨ω, hω⟩ := exists_outside_event w hnorm (fun ω => E ω ∨ F ω) hbad
  exact ⟨ω, not_or.mp hω⟩

-- Source: Er579.RandomRealization.FiniteProbability:114
theorem finite_markov_mul (w : Ω → ℝ) (hw : ∀ ω, 0 ≤ w ω)
    (f : Ω → ℝ) (hf : ∀ ω, 0 ≤ f ω) (a : ℝ) (_ha : 0 ≤ a) :
    a * eventWeight w (fun ω => a ≤ f ω) ≤ finiteExpectation w f := by
  classical
  unfold eventWeight finiteExpectation
  rw [Finset.mul_sum]
  apply Finset.sum_le_sum
  intro ω _
  by_cases h : a ≤ f ω
  · simpa only [if_pos h, mul_comm a (w ω)] using mul_le_mul_of_nonneg_left h (hw ω)
  · simp only [if_neg h, mul_zero]
    exact mul_nonneg (hw ω) (hf ω)

-- Source: Er579.RandomRealization.FiniteProbability:127
theorem finite_markov (w : Ω → ℝ) (hw : ∀ ω, 0 ≤ w ω)
    (f : Ω → ℝ) (hf : ∀ ω, 0 ≤ f ω) (a : ℝ) (ha : 0 < a) :
    eventWeight w (fun ω => a ≤ f ω) ≤ finiteExpectation w f / a := by
  apply (le_div_iff₀ ha).2
  simpa only [mul_comm] using finite_markov_mul w hw f hf a ha.le

-- Source: Er579.RandomRealization.FiniteProbability:133
theorem eventWeight_exists_le_sum {ι : Type*} [Fintype ι]
    (w : Ω → ℝ) (hw : ∀ ω, 0 ≤ w ω) (E : ι → Ω → Prop) :
    eventWeight w (fun ω => ∃ i, E i ω) ≤ ∑ i, eventWeight w (E i) := by
  classical
  unfold eventWeight
  rw [Finset.sum_comm]
  apply Finset.sum_le_sum
  intro ω _
  by_cases h : ∃ i, E i ω
  · obtain ⟨i, hi⟩ := h
    have hex : ∃ j, E j ω := ⟨i, hi⟩
    rw [if_pos hex]
    have hsingle : (if E i ω then w ω else 0) ≤ ∑ j, if E j ω then w ω else 0 :=
      Finset.single_le_sum (f := fun j : ι => if E j ω then w ω else 0)
        (fun j _ => by
          split_ifs
          · exact hw ω
          · exact le_rfl)
        (Finset.mem_univ i)
    simpa only [if_pos hi] using hsingle
  · simp only [if_neg h]
    apply Finset.sum_nonneg
    intro i _
    split_ifs
    · exact hw ω
    · exact le_rfl

-- Source: Er579.RandomRealization.FiniteProbability:160
theorem finiteExpectation_square_ge (w : Ω → ℝ) (hw : ∀ ω, 0 ≤ w ω)
    (hnorm : ∑ ω, w ω = 1) (f : Ω → ℝ) :
    (finiteExpectation w f) ^ 2 ≤ finiteExpectation w (fun ω => (f ω) ^ 2) := by
  let m := finiteExpectation w f
  have hnonneg : 0 ≤ ∑ ω, w ω * (f ω - m) ^ 2 :=
    Finset.sum_nonneg (fun ω _ => mul_nonneg (hw ω) (sq_nonneg _))
  have hexpand : (∑ ω, w ω * (f ω - m) ^ 2) =
      finiteExpectation w (fun ω => (f ω) ^ 2) - m ^ 2 := by
    calc
      (∑ ω, w ω * (f ω - m) ^ 2) =
          ∑ ω, (w ω * (f ω) ^ 2 - 2 * m * (w ω * f ω) + m ^ 2 * w ω) := by
        apply Finset.sum_congr rfl
        intro ω _
        ring
      _ = finiteExpectation w (fun ω => (f ω) ^ 2) - m ^ 2 := by
        rw [Finset.sum_add_distrib, Finset.sum_sub_distrib, ← Finset.mul_sum,
          ← Finset.mul_sum, hnorm]
        change finiteExpectation w (fun ω => (f ω) ^ 2) - 2 * m * m + m ^ 2 * 1 = _
        ring
  rw [hexpand] at hnonneg
  exact sub_nonneg.mp hnonneg

end FiniteProbability

end Er579.RandomRealization

end

/- Source fragment: Er579.CapMoments. Original licenses and source proofs retained. -/

section

/-!
Elementary finite-moment bounds for the caps.  A threshold of half a
standard deviation avoids any central-limit dependency.
-/

namespace Er579.CapMoments

open scoped BigOperators
open RandomRealization
open Classical

variable {Ω : Type*} [Fintype Ω]

-- Source: Er579.CapMoments:17
/-- Weighted Cauchy--Schwarz restricted to an event, without square roots. -/
theorem restricted_cauchy (w : Ω → ℝ) (hw : ∀ x, 0 ≤ w x)
    (Y : Ω → ℝ) (E : Ω → Prop) :
    (finiteExpectation w (fun x => if E x then Y x else 0)) ^ 2 ≤
      finiteExpectation w (fun x => Y x ^ 2) * eventWeight w E := by
  classical
  have h := Finset.sum_sq_le_sum_mul_sum_of_sq_le_mul
    (Finset.univ : Finset Ω)
    (r := fun x => w x * (if E x then Y x else 0))
    (f := fun x => w x * Y x ^ 2)
    (g := fun x => if E x then w x else 0)
    (fun x _ => mul_nonneg (hw x) (sq_nonneg _))
    (fun x _ => by
      split_ifs
      · exact hw x
      · exact le_rfl)
    (fun x _ => by split_ifs <;> nlinarith [hw x])
  exact h

-- Source: Er579.CapMoments:36
/-- The part of a nonnegative variable below a threshold contributes at
most that threshold under a normalized law. -/
theorem mean_le_threshold_add_restricted (w : Ω → ℝ)
    (hw : ∀ x, 0 ≤ w x) (hprob : ∑ x, w x = 1)
    (Y : Ω → ℝ) (a : ℝ) (ha : 0 ≤ a) :
    finiteExpectation w Y ≤ a +
      finiteExpectation w (fun x => if a ≤ Y x then Y x else 0) := by
  classical
  have h : finiteExpectation w Y ≤
      finiteExpectation w (fun x => a + if a ≤ Y x then Y x else 0) := by
    apply Finset.sum_le_sum
    intro x _
    apply mul_le_mul_of_nonneg_left _ (hw x)
    by_cases hx : a ≤ Y x
    · simp only [if_pos hx]
      linarith
    · simp only [if_neg hx, add_zero]
      exact (not_le.mp hx).le
  simpa only [finiteExpectation, mul_add, Finset.sum_add_distrib,
    ← Finset.sum_mul, hprob, one_mul] using h

-- Source: Er579.CapMoments:57
/-- The exact Paley--Zygmund constant needed for the caps. -/
theorem paley_zygmund_quarter (w : Ω → ℝ)
    (hw : ∀ x, 0 ≤ w x) (hprob : ∑ x, w x = 1)
    (Y : Ω → ℝ) (hY : ∀ x, 0 ≤ Y x) (μ : ℝ) (hμ : 0 < μ)
    (hmean : finiteExpectation w Y = μ)
    (hsecond : finiteExpectation w (fun x => Y x ^ 2) ≤ 3 * μ ^ 2) :
    3 / 16 ≤ eventWeight w (fun x => μ / 4 ≤ Y x) := by
  let E : Ω → Prop := fun x => μ / 4 ≤ Y x
  let b := finiteExpectation w (fun x => if E x then Y x else 0)
  let p := eventWeight w E
  have hp : 0 ≤ p := eventWeight_nonneg w hw E
  have hb : 0 ≤ b := by
    apply Finset.sum_nonneg
    intro x _
    apply mul_nonneg (hw x)
    dsimp only
    split_ifs
    · exact hY x
    · exact le_rfl
  have hm : μ ≤ μ / 4 + b := by
    simpa only [hmean] using mean_le_threshold_add_restricted w hw hprob Y
      (μ / 4) (by positivity)
  have hcs : b ^ 2 ≤ finiteExpectation w (fun x => Y x ^ 2) * p :=
    restricted_cauchy w hw Y E
  have hcs' : b ^ 2 ≤ (3 * μ ^ 2) * p :=
    hcs.trans (mul_le_mul_of_nonneg_right hsecond hp)
  have hbound : μ ^ 2 * (3 / 16) ≤ μ ^ 2 * p := by
    nlinarith
  exact (mul_le_mul_iff_right₀ (sq_pos_of_pos hμ)).mp (by
    simpa only [mul_comm] using hbound)

-- Source: Er579.CapMoments:88
/-- Finite event weights are preserved by a weight-preserving permutation. -/
theorem event_equiv (w : Ω → ℝ) (e : Ω ≃ Ω)
    (hw : ∀ x, w (e x) = w x) (E : Ω → Prop) :
    eventWeight w (fun x => E (e x)) = eventWeight w E := by
  classical
  unfold eventWeight
  exact Fintype.sum_equiv e _ _ (fun x => by rw [hw x])

-- Source: Er579.CapMoments:96
/-- A symmetric real random variable puts half of an absolute tail on
each side of every strictly positive threshold. -/
theorem positive_tail_half (w : Ω → ℝ) (S : Ω → ℝ) (e : Ω ≃ Ω)
    (hw : ∀ x, w (e x) = w x) (hS : ∀ x, S (e x) = -S x)
    (a : ℝ) (ha : 0 < a) :
    eventWeight w (fun x => a ^ 2 ≤ S x ^ 2) =
      2 * eventWeight w (fun x => a ≤ S x) := by
  classical
  have hswap : eventWeight w (fun x => a ≤ -S x) =
      eventWeight w (fun x => a ≤ S x) := by
    simpa only [hS] using event_equiv w e hw (fun x => a ≤ S x)
  have hsplit : eventWeight w (fun x => a ^ 2 ≤ S x ^ 2) =
      eventWeight w (fun x => a ≤ S x) +
        eventWeight w (fun x => a ≤ -S x) := by
    unfold eventWeight
    rw [← Finset.sum_add_distrib]
    apply Finset.sum_congr rfl
    intro x _
    by_cases hpos : a ≤ S x
    · have habs : a ^ 2 ≤ S x ^ 2 := by nlinarith
      have hneg : ¬ a ≤ -S x := by linarith
      simp only [if_pos hpos, if_pos habs, if_neg hneg, add_zero]
    · by_cases hneg : a ≤ -S x
      · have habs : a ^ 2 ≤ S x ^ 2 := by nlinarith
        simp only [if_neg hpos, if_pos habs, if_pos hneg, zero_add]
      · have habs : ¬ a ^ 2 ≤ S x ^ 2 := by nlinarith
        simp only [if_neg hpos, if_neg hneg, if_neg habs, add_zero]
  rw [hsplit, hswap]
  ring

-- Source: Er579.CapMoments:126
theorem cap_mass_of_moments (w : Ω → ℝ)
    (hw : ∀ x, 0 ≤ w x) (hprob : ∑ x, w x = 1)
    (S : Ω → ℝ) (μ : ℝ) (hμ : 0 < μ)
    (hsecond : finiteExpectation w (fun x => S x ^ 2) = μ)
    (hfourth : finiteExpectation w (fun x => S x ^ 4) ≤ 3 * μ ^ 2)
    (e : Ω ≃ Ω) (he : ∀ x, w (e x) = w x)
    (hS : ∀ x, S (e x) = -S x) :
    3 / 32 ≤ eventWeight w (fun x => Real.sqrt μ / 2 ≤ S x) := by
  have hm := paley_zygmund_quarter w hw hprob (fun x => S x ^ 2)
    (fun x => sq_nonneg _) μ hμ hsecond (by simpa only [← pow_mul] using hfourth)
  have ha : 0 < Real.sqrt μ / 2 := by positivity
  have heq : (Real.sqrt μ / 2) ^ 2 = μ / 4 := by
    nlinarith [Real.sq_sqrt hμ.le]
  rw [← heq, positive_tail_half w S e he hS _ ha] at hm
  linarith

end Er579.CapMoments

end

section

/-!
Finite real probability weights and the biased-mask product laws.
Every definition is a finite sum or product.  `BoundedMaskCorrelation` is
an explicitly named proposition, not an axiom or an asserted theorem.
-/

namespace Er579

open scoped BigOperators Classical

noncomputable section

/-- A probability law on a finite type, represented by real point weights. -/
structure FiniteProbability (Ω : Type*) [Fintype Ω] where
  weight : Ω → ℝ
  nonneg : ∀ ω, 0 ≤ weight ω
  sum_one : ∑ ω, weight ω = 1

namespace FiniteProbability

variable {Ω Ψ : Type*} [Fintype Ω] [Fintype Ψ]

def expect (p : FiniteProbability Ω) (f : Ω → ℝ) : ℝ :=
  RandomRealization.finiteExpectation p.weight f

noncomputable def event (p : FiniteProbability Ω) (E : Ω → Prop) : ℝ :=
  RandomRealization.eventWeight p.weight E

theorem expect_const (p : FiniteProbability Ω) (r : ℝ) :
    p.expect (fun _ => r) = r := by
  simp only [expect, RandomRealization.finiteExpectation, ← Finset.sum_mul, p.sum_one,
    one_mul]

theorem expect_nonneg (p : FiniteProbability Ω) {f : Ω → ℝ}
    (hf : ∀ ω, 0 ≤ f ω) : 0 ≤ p.expect f := by
  apply Finset.sum_nonneg
  intro ω _
  exact mul_nonneg (p.nonneg ω) (hf ω)

theorem expect_mono (p : FiniteProbability Ω) {f g : Ω → ℝ}
    (h : ∀ ω, f ω ≤ g ω) : p.expect f ≤ p.expect g := by
  apply Finset.sum_le_sum
  intro ω _
  exact mul_le_mul_of_nonneg_left (h ω) (p.nonneg ω)

theorem event_nonneg (p : FiniteProbability Ω) (E : Ω → Prop) : 0 ≤ p.event E :=
  RandomRealization.eventWeight_nonneg _ p.nonneg _

theorem event_true (p : FiniteProbability Ω) : p.event (fun _ => True) = 1 := by
  simp [event, RandomRealization.eventWeight, p.sum_one]

theorem event_false (p : FiniteProbability Ω) : p.event (fun _ => False) = 0 := by
  simp [event, RandomRealization.eventWeight]

theorem event_le_one (p : FiniteProbability Ω) (E : Ω → Prop) : p.event E ≤ 1 := by
  simpa [event, RandomRealization.eventWeight, p.sum_one] using
    RandomRealization.eventWeight_mono p.weight p.nonneg
    (E := E) (F := fun _ => True) (fun _ _ => trivial)

theorem event_mono (p : FiniteProbability Ω) {E F : Ω → Prop}
    (h : ∀ ω, E ω → F ω) : p.event E ≤ p.event F :=
  RandomRealization.eventWeight_mono _ p.nonneg h

theorem event_mono_on_support (p : FiniteProbability Ω) {E F : Ω → Prop}
    (h : ∀ ω, p.weight ω ≠ 0 → E ω → F ω) : p.event E ≤ p.event F := by
  classical
  unfold event RandomRealization.eventWeight
  apply Finset.sum_le_sum
  intro ω _
  by_cases hw : p.weight ω = 0
  · simp [hw]
  · by_cases he : E ω
    · simp only [if_pos he, if_pos (h ω hw he)]
      exact le_rfl
    · simp only [if_neg he]
      split_ifs
      · exact p.nonneg ω
      · exact le_rfl

theorem event_or_le (p : FiniteProbability Ω) (E F : Ω → Prop) :
    p.event (fun ω => E ω ∨ F ω) ≤ p.event E + p.event F :=
  RandomRealization.eventWeight_or_le _ p.nonneg _ _

theorem event_exists_le_sum {ι : Type*} [Fintype ι]
    (p : FiniteProbability Ω) (E : ι → Ω → Prop) :
    p.event (fun ω => ∃ i, E i ω) ≤ ∑ i, p.event (E i) :=
  RandomRealization.eventWeight_exists_le_sum _ p.nonneg _

theorem ext (p q : FiniteProbability Ω) (h : ∀ ω, p.weight ω = q.weight ω) : p = q := by
  cases p with
  | mk w hw hs =>
    cases q with
    | mk w' hw' hs' =>
      have heq : w = w' := funext h
      subst w'
      rfl

def dirac (ω₀ : Ω) : FiniteProbability Ω where
  weight ω := if ω = ω₀ then 1 else 0
  nonneg ω := by split_ifs <;> norm_num
  sum_one := by simp

def pi {I A : Type*} [Fintype I] [Fintype A] (p : I → FiniteProbability A) :
    FiniteProbability (I → A) where
  weight x := ∏ i, (p i).weight (x i)
  nonneg x := Finset.prod_nonneg (fun i _ => (p i).nonneg _)
  sum_one := by
    rw [← Fintype.prod_sum]
    simp only [sum_one, Finset.prod_const_one]

theorem event_eq_expect_indicator (p : FiniteProbability Ω) (E : Ω → Prop) :
    p.event E = p.expect (fun ω => if E ω then 1 else 0) := by
  classical
  unfold event expect RandomRealization.eventWeight RandomRealization.finiteExpectation
  apply Finset.sum_congr rfl
  intro ω _
  by_cases h : E ω <;> simp [h]

theorem expect_add (p : FiniteProbability Ω) (f g : Ω → ℝ) :
    p.expect (fun ω => f ω + g ω) = p.expect f + p.expect g := by
  simp only [expect, RandomRealization.finiteExpectation, mul_add, Finset.sum_add_distrib]

theorem expect_sum {ι : Type*} [Fintype ι] (p : FiniteProbability Ω)
    (f : ι → Ω → ℝ) : p.expect (fun ω => ∑ i, f i ω) = ∑ i, p.expect (f i) := by
  simp only [expect, RandomRealization.finiteExpectation, Finset.mul_sum]
  exact Finset.sum_comm

theorem expect_const_mul (p : FiniteProbability Ω) (r : ℝ) (f : Ω → ℝ) :
    p.expect (fun ω => r * f ω) = r * p.expect f := by
  unfold expect RandomRealization.finiteExpectation
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro ω _
  ring

theorem expect_mul_const (p : FiniteProbability Ω) (f : Ω → ℝ) (r : ℝ) :
    p.expect (fun ω => f ω * r) = p.expect f * r := by
  unfold expect RandomRealization.finiteExpectation
  rw [Finset.sum_mul]
  apply Finset.sum_congr rfl
  intro ω _
  ring

/-- Independent product of two finite laws. -/
def prod (p : FiniteProbability Ω) (q : FiniteProbability Ψ) :
    FiniteProbability (Ω × Ψ) where
  weight x := p.weight x.1 * q.weight x.2
  nonneg x := mul_nonneg (p.nonneg _) (q.nonneg _)
  sum_one := by
    rw [Fintype.sum_prod_type]
    simp only [← Finset.mul_sum, q.sum_one, mul_one, p.sum_one]

theorem prod_weight (p : FiniteProbability Ω) (q : FiniteProbability Ψ)
    (x : Ω) (y : Ψ) : (p.prod q).weight (x, y) = p.weight x * q.weight y := rfl

theorem prod_expect (p : FiniteProbability Ω) (q : FiniteProbability Ψ)
    (f : Ω × Ψ → ℝ) :
    (p.prod q).expect f = p.expect (fun x => q.expect (fun y => f (x, y))) := by
  simp only [expect, RandomRealization.finiteExpectation, prod, Fintype.sum_prod_type,
    Finset.mul_sum, mul_assoc]

theorem prod_expect_right (p : FiniteProbability Ω) (q : FiniteProbability Ψ)
    (f : Ω × Ψ → ℝ) :
    (p.prod q).expect f = q.expect (fun y => p.expect (fun x => f (x, y))) := by
  rw [prod_expect]
  simp only [expect, RandomRealization.finiteExpectation, Finset.mul_sum]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro y _
  apply Finset.sum_congr rfl
  intro x _
  ring

theorem prod_expect_mul (p : FiniteProbability Ω) (q : FiniteProbability Ψ)
    (f : Ω → ℝ) (g : Ψ → ℝ) :
    (p.prod q).expect (fun x => f x.1 * g x.2) = p.expect f * q.expect g := by
  rw [prod_expect]
  simp_rw [expect_const_mul]
  exact expect_mul_const p f (q.expect g)

theorem prod_event_and (p : FiniteProbability Ω) (q : FiniteProbability Ψ)
    (E : Ω → Prop) (F : Ψ → Prop) :
    (p.prod q).event (fun x => E x.1 ∧ F x.2) = p.event E * q.event F := by
  classical
  unfold event RandomRealization.eventWeight prod
  rw [Fintype.sum_prod_type, Finset.sum_mul]
  apply Finset.sum_congr rfl
  intro x _
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro y _
  by_cases he : E x <;> by_cases hf : F y <;> simp [he, hf]

theorem prod_event_fst (p : FiniteProbability Ω) (q : FiniteProbability Ψ)
    (E : Ω → Prop) : (p.prod q).event (fun x => E x.1) = p.event E := by
  classical
  simp only [event, RandomRealization.eventWeight, prod, Fintype.sum_prod_type]
  apply Finset.sum_congr rfl
  intro x _
  by_cases h : E x
  · simp only [if_pos h, ← Finset.mul_sum, q.sum_one, mul_one]
  · simp only [if_neg h, Finset.sum_const_zero]

theorem prod_event_snd (p : FiniteProbability Ω) (q : FiniteProbability Ψ)
    (E : Ψ → Prop) : (p.prod q).event (fun x => E x.2) = q.event E := by
  classical
  simp only [event, RandomRealization.eventWeight, prod, Fintype.sum_prod_type]
  have hterm (x : Ω) :
      (∑ y, if E y then p.weight x * q.weight y else 0) =
        p.weight x * ∑ y, if E y then q.weight y else 0 := by
    rw [Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro y _
    split_ifs <;> simp
  simp_rw [hterm]
  rw [← Finset.sum_mul, p.sum_one, one_mul]

def pairCoordinateEquiv {I A D : Type*} :
    (I → A × D) ≃ (I → A) × (I → D) where
  toFun σ := (fun i => (σ i).1, fun i => (σ i).2)
  invFun x := fun i => (x.1 i, x.2 i)
  left_inv _ := rfl
  right_inv _ := rfl

theorem pi_pair_fst_expect {I A D : Type*} [Fintype I] [Fintype A] [Fintype D]
    (p : I → FiniteProbability (A × D)) (q : I → FiniteProbability A)
    (h : ∀ i a, (∑ d, (p i).weight (a, d)) = (q i).weight a) (f : (I → A) → ℝ) :
    (pi p).expect (fun σ => f (fun i => (σ i).1)) = (pi q).expect f := by
  change (∑ σ : I → A × D, (∏ i : I, (p i).weight (σ i)) * f (fun i => (σ i).1)) =
    ∑ γ : I → A, (∏ i : I, (q i).weight (γ i)) * f γ
  calc
    _ = ∑ x : (I → A) × (I → D),
        (∏ i, (p i).weight (x.1 i, x.2 i)) * f x.1 :=
      Fintype.sum_equiv pairCoordinateEquiv _ _ (fun _ => rfl)
    _ = _ := by
      rw [Fintype.sum_prod_type]
      apply Finset.sum_congr rfl
      intro γ _
      dsimp only
      rw [← Finset.sum_mul]
      rw [← Fintype.prod_sum (fun i d => (p i).weight (γ i, d))]
      simp_rw [h]

theorem pi_pair_snd_expect {I A D : Type*} [Fintype I] [Fintype A] [Fintype D]
    (p : I → FiniteProbability (A × D)) (q : I → FiniteProbability D)
    (h : ∀ i d, (∑ a, (p i).weight (a, d)) = (q i).weight d) (f : (I → D) → ℝ) :
    (pi p).expect (fun σ => f (fun i => (σ i).2)) = (pi q).expect f := by
  change (∑ σ : I → A × D, (∏ i : I, (p i).weight (σ i)) * f (fun i => (σ i).2)) =
    ∑ γ : I → D, (∏ i : I, (q i).weight (γ i)) * f γ
  calc
    _ = ∑ x : (I → A) × (I → D),
        (∏ i, (p i).weight (x.1 i, x.2 i)) * f x.2 :=
      Fintype.sum_equiv pairCoordinateEquiv _ _ (fun _ => rfl)
    _ = _ := by
      rw [Fintype.sum_prod_type_right]
      apply Finset.sum_congr rfl
      intro γ _
      dsimp only
      rw [← Finset.sum_mul]
      rw [← Fintype.prod_sum (fun i a => (p i).weight (a, γ i))]
      simp_rw [h]

end FiniteProbability

/-- A mask bit has bias one quarter. -/
def maskBitWeight (x : Bool) : ℝ := if x then 1 / 4 else 3 / 4

theorem maskBitWeight_nonneg (x : Bool) : 0 ≤ maskBitWeight x := by
  cases x <;> norm_num [maskBitWeight]

theorem maskBitWeight_sum : (∑ x : Bool, maskBitWeight x) = 1 := by
  norm_num [maskBitWeight, Fintype.sum_bool]

/-- Stationary paired bits are disjoint and have the correct biased marginals. -/
def maskPairBitWeight (x : Bool × Bool) : ℝ :=
  if x.1 then (if x.2 then 0 else 1 / 4)
  else (if x.2 then 1 / 4 else 1 / 2)

theorem maskPairBitWeight_nonneg (x : Bool × Bool) : 0 ≤ maskPairBitWeight x := by
  rcases x with ⟨x, y⟩
  cases x <;> cases y <;> norm_num [maskPairBitWeight]

theorem maskPairBitWeight_sum : (∑ x : Bool × Bool, maskPairBitWeight x) = 1 := by
  norm_num [Fintype.sum_prod_type, Fintype.sum_bool, maskPairBitWeight]

section Masks

variable {B : Type*} [Fintype B]

def maskWeight (γ : B → Bool) : ℝ := ∏ b, maskBitWeight (γ b)

theorem maskWeight_nonneg (γ : B → Bool) : 0 ≤ maskWeight γ := by
  exact Finset.prod_nonneg (fun _ _ => maskBitWeight_nonneg _)

theorem maskWeight_sum : (∑ γ : B → Bool, maskWeight γ) = 1 := by
  unfold maskWeight
  rw [← Fintype.prod_sum]
  simp only [maskBitWeight_sum, Finset.prod_const_one]

def maskLaw : FiniteProbability (B → Bool) where
  weight := maskWeight
  nonneg := maskWeight_nonneg
  sum_one := maskWeight_sum

def maskMean (f : (B → Bool) → ℝ) : ℝ := maskLaw.expect f

noncomputable def conditionalMaskCoordWeight (J : Finset B) (z : B → Bool)
    (b : B) (x : Bool) : ℝ := by
  classical
  exact if b ∈ J then (if x = z b then 1 else 0) else maskBitWeight x

noncomputable def conditionalMaskWeight (J : Finset B) (z γ : B → Bool) : ℝ :=
  ∏ b, conditionalMaskCoordWeight J z b (γ b)

noncomputable def residualPairCoordWeight (J : Finset B) (z : B → Bool)
    (b : B) (x : Bool × Bool) : ℝ := by
  classical
  exact if b ∈ J then (if x = (z b, z b) then 1 else 0) else maskPairBitWeight x

noncomputable def residualPairWeight (J : Finset B) (z : B → Bool)
    (σ : B → Bool × Bool) : ℝ := ∏ b, residualPairCoordWeight J z b (σ b)

omit [Fintype B] in
theorem residualPairCoordWeight_nonneg (J : Finset B) (z : B → Bool)
    (b : B) (x : Bool × Bool) : 0 ≤ residualPairCoordWeight J z b x := by
  classical
  unfold residualPairCoordWeight
  split_ifs <;> try norm_num
  exact maskPairBitWeight_nonneg x

omit [Fintype B] in
theorem residualPairCoordWeight_sum (J : Finset B) (z : B → Bool) (b : B) :
    (∑ x : Bool × Bool, residualPairCoordWeight J z b x) = 1 := by
  classical
  by_cases h : b ∈ J
  · simp [residualPairCoordWeight, h]
  · simp [residualPairCoordWeight, h, maskPairBitWeight_sum]

theorem residualPairWeight_nonneg (J : Finset B) (z : B → Bool)
    (σ : B → Bool × Bool) : 0 ≤ residualPairWeight J z σ := by
  exact Finset.prod_nonneg (fun _ _ => residualPairCoordWeight_nonneg _ _ _ _)

theorem residualPairWeight_sum (J : Finset B) (z : B → Bool) :
    (∑ σ : B → Bool × Bool, residualPairWeight J z σ) = 1 := by
  unfold residualPairWeight
  rw [← Fintype.prod_sum]
  simp only [residualPairCoordWeight_sum, Finset.prod_const_one]

noncomputable def residualPairLaw (J : Finset B) (z : B → Bool) :
    FiniteProbability (B → Bool × Bool) where
  weight := residualPairWeight J z
  nonneg := residualPairWeight_nonneg J z
  sum_one := residualPairWeight_sum J z

noncomputable def residualCorrelation (J : Finset B) (z : B → Bool)
    (f : (B → Bool) → ℝ) : ℝ :=
  (residualPairLaw J z).expect (fun σ =>
    f (fun b => (σ b).1) * f (fun b => (σ b).2))

theorem residualPairWeight_zero_of_shared_outside (J : Finset B) (z : B → Bool)
    (σ : B → Bool × Bool) (b : B) (hb : b ∉ J)
    (h₁ : (σ b).1 = true) (h₂ : (σ b).2 = true) :
    residualPairWeight J z σ = 0 := by
  classical
  apply Finset.prod_eq_zero (Finset.mem_univ b)
  simp [residualPairCoordWeight, hb, maskPairBitWeight, h₁, h₂]

theorem residualPair_shared_mem (J : Finset B) (z : B → Bool)
    (σ : B → Bool × Bool) (hσ : residualPairWeight J z σ ≠ 0)
    (b : B) (h₁ : (σ b).1 = true) (h₂ : (σ b).2 = true) : b ∈ J := by
  classical
  by_contra hb
  exact hσ (residualPairWeight_zero_of_shared_outside J z σ b hb h₁ h₂)

theorem residualCorrelation_nonneg (J : Finset B) (z : B → Bool)
    {f : (B → Bool) → ℝ} (hf : ∀ γ, 0 ≤ f γ) :
    0 ≤ residualCorrelation J z f := by
  apply FiniteProbability.expect_nonneg
  intro σ
  exact mul_nonneg (hf _) (hf _)

theorem residualCorrelation_le_one (J : Finset B) (z : B → Bool)
    {f : (B → Bool) → ℝ} (hf : ∀ γ, 0 ≤ f γ ∧ f γ ≤ 1) :
    residualCorrelation J z f ≤ 1 := by
  simpa [residualCorrelation, FiniteProbability.expect_const] using (residualPairLaw J z).expect_mono
    (f := fun σ => f (fun b => (σ b).1) * f (fun b => (σ b).2))
    (g := fun _ => 1) (fun σ => by
      exact mul_le_one₀ (hf _).2 (hf _).1 (hf _).2)

end Masks

/-! General bias is needed only for the monotone mask reduction.  The
ordinary construction continues to use the bias one-quarter law above. -/

def biasMaskBitWeight (ρ : ℝ) (x : Bool) : ℝ := if x then ρ else 1 - ρ

def biasMaskPairBitWeight (ρ : ℝ) (x : Bool × Bool) : ℝ :=
  if x.1 then (if x.2 then 0 else ρ)
  else (if x.2 then ρ else 1 - 2 * ρ)

def biasMaskBitLaw (ρ : ℝ) (hρ0 : 0 ≤ ρ) (hρ1 : ρ ≤ 1) :
    FiniteProbability Bool where
  weight := biasMaskBitWeight ρ
  nonneg x := by cases x <;> simp [biasMaskBitWeight] <;> linarith
  sum_one := by simp [biasMaskBitWeight]

def biasMaskPairBitLaw (ρ : ℝ) (hρ0 : 0 ≤ ρ) (hρhalf : ρ ≤ 1 / 2) :
    FiniteProbability (Bool × Bool) where
  weight := biasMaskPairBitWeight ρ
  nonneg x := by rcases x with ⟨x, y⟩; cases x <;> cases y <;>
    simp [biasMaskPairBitWeight] <;> linarith
  sum_one := by simp [Fintype.sum_prod_type, biasMaskPairBitWeight]; ring

section BiasedMasks

variable {B : Type*} [Fintype B]

def biasMaskLaw (ρ : ℝ) (hρ0 : 0 ≤ ρ) (hρ1 : ρ ≤ 1) :
    FiniteProbability (B → Bool) := FiniteProbability.pi (fun _ => biasMaskBitLaw ρ hρ0 hρ1)

def biasMaskMean (ρ : ℝ) (hρ0 : 0 ≤ ρ) (hρ1 : ρ ≤ 1)
    (f : (B → Bool) → ℝ) : ℝ := (biasMaskLaw ρ hρ0 hρ1).expect f

def biasConditionalMaskLaw (ρ : ℝ) (hρ0 : 0 ≤ ρ) (hρ1 : ρ ≤ 1)
    (J : Finset B) (z : B → Bool) : FiniteProbability (B → Bool) :=
  FiniteProbability.pi (fun b => if b ∈ J then FiniteProbability.dirac (z b)
    else biasMaskBitLaw ρ hρ0 hρ1)

def biasConditionalMaskMean (ρ : ℝ) (hρ0 : 0 ≤ ρ) (hρ1 : ρ ≤ 1)
    (J : Finset B) (z : B → Bool) (f : (B → Bool) → ℝ) : ℝ :=
  (biasConditionalMaskLaw ρ hρ0 hρ1 J z).expect f

def biasResidualPairLaw (ρ : ℝ) (hρ0 : 0 ≤ ρ) (hρhalf : ρ ≤ 1 / 2)
    (J : Finset B) (z : B → Bool) : FiniteProbability (B → Bool × Bool) :=
  FiniteProbability.pi (fun b => if b ∈ J then FiniteProbability.dirac (z b, z b)
    else biasMaskPairBitLaw ρ hρ0 hρhalf)

def biasResidualCorrelation (ρ : ℝ) (hρ0 : 0 ≤ ρ) (hρhalf : ρ ≤ 1 / 2)
    (J : Finset B) (z : B → Bool) (f : (B → Bool) → ℝ) : ℝ :=
  (biasResidualPairLaw ρ hρ0 hρhalf J z).expect
    (fun σ => f (fun b => (σ b).1) * f (fun b => (σ b).2))

theorem biasResidualPair_shared_mem (ρ : ℝ) (hρ0 : 0 ≤ ρ) (hρhalf : ρ ≤ 1 / 2)
    (J : Finset B) (z : B → Bool) (σ : B → Bool × Bool)
    (hσ : (biasResidualPairLaw ρ hρ0 hρhalf J z).weight σ ≠ 0)
    (b : B) (h₁ : (σ b).1 = true) (h₂ : (σ b).2 = true) : b ∈ J := by
  by_contra hb
  apply hσ
  apply Finset.prod_eq_zero (Finset.mem_univ b)
  simp [hb, biasMaskPairBitLaw, biasMaskPairBitWeight, h₁, h₂]

theorem maskLaw_eq_biasMaskLaw : (maskLaw : FiniteProbability (B → Bool)) =
    biasMaskLaw (1 / 4) (by norm_num) (by norm_num) := by
  apply FiniteProbability.ext
  intro γ
  unfold maskLaw maskWeight biasMaskLaw FiniteProbability.pi
  apply Finset.prod_congr rfl
  intro b _
  cases γ b <;> norm_num [biasMaskBitLaw, biasMaskBitWeight, maskBitWeight]

theorem residualPairLaw_eq_biasResidualPairLaw (J : Finset B) (z : B → Bool) :
    residualPairLaw J z = biasResidualPairLaw (1 / 4) (by norm_num) (by norm_num) J z := by
  apply FiniteProbability.ext
  intro σ
  unfold residualPairLaw residualPairWeight biasResidualPairLaw FiniteProbability.pi
  apply Finset.prod_congr rfl
  intro b _
  by_cases hb : b ∈ J
  · simp [hb, residualPairCoordWeight, FiniteProbability.dirac]
  · rcases hσb : σ b with ⟨x, y⟩
    cases x <;> cases y <;> norm_num [hb, residualPairCoordWeight,
      biasMaskPairBitLaw, biasMaskPairBitWeight, maskPairBitWeight, hσb]

end BiasedMasks

/-- The precise analytic input used by the finite masked counting proof.
It must be proved from the weak Friedgut--Regev capture theorem before the
full development can be complete. -/
def BoundedMaskCorrelation : Prop :=
  ∀ ε : ℝ, 0 < ε → ε ≤ 1 →
    ∃ R : ℕ, ∃ d : ℝ, 0 < d ∧
      ∀ (B : Type) (_ : Fintype B) (f : (B → Bool) → ℝ),
        (∀ γ, 0 ≤ f γ ∧ f γ ≤ 1) → ε ≤ maskMean f →
        ∃ (J : Finset B) (z : B → Bool),
          J.card ≤ R ∧ d ≤ residualCorrelation J z f

end

end Er579

end

/- Source fragment: Er579.RandomRealization.HeavyCells. Original licenses and source proofs retained. -/

section

/-! The deterministic heavy-cell argument supplying quadratically many
potential edges inside every overly large candidate independent set. -/

namespace Er579.RandomRealization

open scoped BigOperators Classical

variable {Q : Type*} [Fintype Q]

-- Source: Er579.RandomRealization.HeavyCells:13
theorem exists_adjacent_heavy_cells (H : SimpleGraph Q)
    (cell selected : Q → ℝ) (t a ε : ℝ)
    (hcell : ∀ q, 0 ≤ cell q) (hselected : ∀ q, selected q ≤ cell q)
    (hsum : ∑ q, cell q = t) (hε : 0 ≤ ε)
    (hα : ∀ W : Finset Q, H.IsIndepSet (W : Set Q) → ∑ q ∈ W, cell q ≤ a * t)
    (hlarge : (a + ε) * t < ∑ q, selected q) :
    ∃ q q', H.Adj q q' ∧ ε * cell q ≤ selected q ∧ ε * cell q' ≤ selected q' := by
  let W : Finset Q := Finset.univ.filter (fun q => ε * cell q ≤ selected q)
  have hnot : ¬ H.IsIndepSet (W : Set Q) := by
    intro hW
    have hpoint (q : Q) : selected q ≤ (if q ∈ W then cell q else 0) + ε * cell q := by
      by_cases hq : q ∈ W
      · rw [if_pos hq]
        exact (hselected q).trans (le_add_of_nonneg_right (mul_nonneg hε (hcell q)))
      · rw [if_neg hq, zero_add]
        have hn : ¬ ε * cell q ≤ selected q := by simpa only [W, Finset.mem_filter,
          Finset.mem_univ, true_and] using hq
        exact (lt_of_not_ge hn).le
    have hbound : (∑ q, selected q) ≤ (∑ q ∈ W, cell q) + ε * t := by
      calc
        (∑ q, selected q) ≤ ∑ q, ((if q ∈ W then cell q else 0) + ε * cell q) :=
          Finset.sum_le_sum (fun q _ => hpoint q)
        _ = (∑ q ∈ W, cell q) + ε * t := by
          rw [Finset.sum_add_distrib, ← Finset.mul_sum, hsum]
          simp only [Finset.sum_ite_mem, Finset.univ_inter]
    have hsmall := hα W hW
    nlinarith
  simp only [SimpleGraph.IsIndepSet, Set.Pairwise] at hnot
  push Not at hnot
  obtain ⟨q, hq, q', hq', _, hadj⟩ := hnot
  have hqheavy : ε * cell q ≤ selected q := by
    simpa only [W, Finset.mem_coe, Finset.mem_filter, Finset.mem_univ, true_and] using hq
  have hqheavy' : ε * cell q' ≤ selected q' := by
    simpa only [W, Finset.mem_coe, Finset.mem_filter, Finset.mem_univ, true_and] using hq'
  exact ⟨q, q', hadj, hqheavy, hqheavy'⟩

end Er579.RandomRealization

end

/- Source fragment: Er579.RandomRealization.NaturalBlowup. Original licenses and source proofs retained. -/

section

/-! Exact natural multiplicities for the rational weighted A profiles. -/

namespace Er579.RandomRealization

open scoped BigOperators Classical

variable {Q : Type*} [Fintype Q]

-- Source: Er579.RandomRealization.NaturalBlowup:13
def totalMultiplicity (m : Q → ℕ) : ℕ := ∑ q, m q

-- Source: Er579.RandomRealization.NaturalBlowup:15
abbrev BlowupVertex (m : Q → ℕ) (L : ℕ) := Σ q : Q, Fin (m q * L ^ 5)

-- Source: Er579.RandomRealization.NaturalBlowup:17
def profileBlowup (H : SimpleGraph Q) (m : Q → ℕ) (L : ℕ) :
    SimpleGraph (BlowupVertex m L) := H.comap Sigma.fst

-- Source: Er579.RandomRealization.NaturalBlowup:20
theorem blowupVertex_card (m : Q → ℕ) (L : ℕ) :
    Fintype.card (BlowupVertex m L) = totalMultiplicity m * L ^ 5 := by
  simp only [BlowupVertex, Fintype.card_sigma, Fintype.card_fin, totalMultiplicity,
    Finset.sum_mul]

-- Source: Er579.RandomRealization.NaturalBlowup:25
noncomputable def profileCell (m : Q → ℕ) (L : ℕ) (q : Q) : Finset (BlowupVertex m L) :=
  Finset.univ.filter (fun v => v.1 = q)

-- Source: Er579.RandomRealization.NaturalBlowup:28
def profileFiberEquiv (m : Q → ℕ) (L : ℕ) (q : Q) :
    {v : BlowupVertex m L // v.1 = q} ≃ Fin (m q * L ^ 5) where
  toFun v := by
    rcases v with ⟨⟨q', i⟩, h⟩
    change q' = q at h
    subst q'
    exact i
  invFun i := ⟨⟨q, i⟩, rfl⟩
  left_inv v := by
    rcases v with ⟨⟨q', i⟩, h⟩
    change q' = q at h
    subst q'
    rfl
  right_inv i := rfl

-- Source: Er579.RandomRealization.NaturalBlowup:43
theorem profileCell_card (m : Q → ℕ) (L : ℕ) (q : Q) :
    (profileCell m L q).card = m q * L ^ 5 := by
  have h : Fintype.card {v : BlowupVertex m L // v.1 = q} = m q * L ^ 5 := by
    simpa only [Fintype.card_fin] using Fintype.card_congr (profileFiberEquiv m L q)
  simpa only [Fintype.card_subtype, profileCell] using h

-- Source: Er579.RandomRealization.NaturalBlowup:49
noncomputable def selectedCell (m : Q → ℕ) (L : ℕ)
    (I : Finset (BlowupVertex m L)) (q : Q) : Finset (BlowupVertex m L) :=
  I.filter (fun v => v.1 = q)

omit [Fintype Q] in

-- Source: Er579.RandomRealization.NaturalBlowup:54
theorem mem_selectedCell (m : Q → ℕ) (L : ℕ)
    (I : Finset (BlowupVertex m L)) (q : Q) (v : BlowupVertex m L) :
    v ∈ selectedCell m L I q ↔ v ∈ I ∧ v.1 = q := by
  simp only [selectedCell, Finset.mem_filter]

omit [Fintype Q] in

-- Source: Er579.RandomRealization.NaturalBlowup:60
theorem selectedCell_subset (m : Q → ℕ) (L : ℕ)
    (I : Finset (BlowupVertex m L)) (q : Q) : selectedCell m L I q ⊆ I :=
  Finset.filter_subset _ _

-- Source: Er579.RandomRealization.NaturalBlowup:64
theorem selectedCell_card_le (m : Q → ℕ) (L : ℕ)
    (I : Finset (BlowupVertex m L)) (q : Q) :
    (selectedCell m L I q).card ≤ m q * L ^ 5 := by
  rw [← profileCell_card m L q]
  apply Finset.card_le_card
  intro v hv
  simp only [selectedCell, Finset.mem_filter] at hv
  simp only [profileCell, Finset.mem_filter, Finset.mem_univ, true_and]
  exact hv.2

-- Source: Er579.RandomRealization.NaturalBlowup:74
theorem selectedCell_card_sum (m : Q → ℕ) (L : ℕ)
    (I : Finset (BlowupVertex m L)) : ∑ q, (selectedCell m L I q).card = I.card := by
  symm
  exact Finset.card_eq_sum_card_fiberwise (f := Sigma.fst) (t := Finset.univ)
    (fun _ _ => Finset.mem_univ _)

-- Source: Er579.RandomRealization.NaturalBlowup:80
def ProfileIndependenceBound (H : SimpleGraph Q) (m : Q → ℕ) (a : ℝ) : Prop :=
  ∀ W : Finset Q, H.IsIndepSet (W : Set Q) → ∑ q ∈ W, (m q : ℝ) ≤ a * totalMultiplicity m

-- Source: Er579.RandomRealization.NaturalBlowup:83
theorem large_set_adjacent_heavy_profiles (H : SimpleGraph Q) (m : Q → ℕ) (L : ℕ)
    (I : Finset (BlowupVertex m L)) (a ε : ℝ) (hε : 0 ≤ ε)
    (hα : ProfileIndependenceBound H m a)
    (hlarge : (a + ε) * Fintype.card (BlowupVertex m L) < I.card) :
    ∃ q q', H.Adj q q' ∧
      ε * (m q * L ^ 5 : ℕ) ≤ (selectedCell m L I q).card ∧
      ε * (m q' * L ^ 5 : ℕ) ≤ (selectedCell m L I q').card := by
  apply exists_adjacent_heavy_cells H
    (fun q => (m q * L ^ 5 : ℕ))
    (fun q => ((selectedCell m L I q).card : ℝ))
    (Fintype.card (BlowupVertex m L)) a ε
  · intro q
    positivity
  · intro q
    exact_mod_cast selectedCell_card_le m L I q
  · rw [blowupVertex_card]
    simp only [Nat.cast_mul, Nat.cast_pow, Nat.cast_sum, totalMultiplicity,
      Finset.sum_mul]
  · exact hε
  · intro W hW
    have hb := hα W hW
    calc
      (∑ q ∈ W, ((m q * L ^ 5 : ℕ) : ℝ)) = (∑ q ∈ W, (m q : ℝ)) * (L : ℝ) ^ 5 := by
        simp only [Nat.cast_mul, Nat.cast_pow, Finset.sum_mul]
      _ ≤ (a * totalMultiplicity m) * (L : ℝ) ^ 5 :=
        mul_le_mul_of_nonneg_right hb (by positivity)
      _ = a * Fintype.card (BlowupVertex m L) := by
        rw [blowupVertex_card]
        push_cast
        ring
  · have hs : (∑ q, ((selectedCell m L I q).card : ℝ)) = I.card := by
      exact_mod_cast selectedCell_card_sum m L I
    simpa only [hs] using hlarge

end Er579.RandomRealization

end

/- Source fragment: Er579.OctahedronExclusion. Original licenses and source proofs retained. -/

section

/-!
The noninduced octahedron exclusion used by the biased-mask construction.
Every containment below is an injective edge-preserving map; no reflection
of nonadjacency is assumed.
-/

namespace Er579

-- Source: Er579.OctahedronExclusion:15
abbrev OctVertex := Σ _ : Fin 3, Fin 2

-- Source: Er579.OctahedronExclusion:17
abbrev octahedron : SimpleGraph OctVertex :=
  SimpleGraph.completeMultipartiteGraph (fun _ : Fin 3 => Fin 2)

-- Source: Er579.OctahedronExclusion:20
theorem octahedron_adj (x y : OctVertex) :
    octahedron.Adj x y ↔ x.1 ≠ y.1 := by
  simp [octahedron, SimpleGraph.completeMultipartiteGraph]

-- Source: Er579.OctahedronExclusion:24
/-- Excludes triangles as required subgraphs, with arbitrary additional edges. -/
def TriangleFree {V : Type*} (G : SimpleGraph V) : Prop :=
  ∀ a b c, G.Adj a b → G.Adj b c → G.Adj c a → False

-- Source: Er579.OctahedronExclusion:28
/-- Opposite vertices must be distinct; adjacent distinctness follows from looplessness. -/
def C4Free {V : Type*} (G : SimpleGraph V) : Prop :=
  ∀ a b c d, a ≠ c → b ≠ d →
    G.Adj a b → G.Adj b c → G.Adj c d → G.Adj d a → False

-- Source: Er579.OctahedronExclusion:33
/-- The prescribed two-part graph, including all and only the specified cross edges. -/
def twoPartGraph {A B PA PB : Type*} (GA : SimpleGraph A) (GB : SimpleGraph B)
    (M : PA → PB → Prop) (labelA : A → PA) (labelB : B → PB) :
    SimpleGraph (A ⊕ B) where
  Adj x y := match x, y with
    | .inl a, .inl a' => GA.Adj a a'
    | .inr b, .inr b' => GB.Adj b b'
    | .inl a, .inr b => M (labelA a) (labelB b)
    | .inr b, .inl a => M (labelA a) (labelB b)
  symm := by
    constructor
    intro x y h
    cases x <;> cases y
    · exact GA.adj_symm h
    · exact h
    · exact h
    · exact GB.adj_symm h
  loopless := by
    constructor
    intro x
    cases x
    · exact GA.irrefl
    · exact GB.irrefl

-- Source: Er579.OctahedronExclusion:57
theorem twoPartGraph_adj_inl_inl {A B PA PB : Type*}
    (GA : SimpleGraph A) (GB : SimpleGraph B) (M : PA → PB → Prop)
    (labelA : A → PA) (labelB : B → PB) (a a' : A) :
    (twoPartGraph GA GB M labelA labelB).Adj (.inl a) (.inl a') ↔ GA.Adj a a' :=
  Iff.rfl

-- Source: Er579.OctahedronExclusion:63
theorem twoPartGraph_adj_inr_inr {A B PA PB : Type*}
    (GA : SimpleGraph A) (GB : SimpleGraph B) (M : PA → PB → Prop)
    (labelA : A → PA) (labelB : B → PB) (b b' : B) :
    (twoPartGraph GA GB M labelA labelB).Adj (.inr b) (.inr b') ↔ GB.Adj b b' :=
  Iff.rfl

-- Source: Er579.OctahedronExclusion:69
theorem twoPartGraph_adj_inl_inr {A B PA PB : Type*}
    (GA : SimpleGraph A) (GB : SimpleGraph B) (M : PA → PB → Prop)
    (labelA : A → PA) (labelB : B → PB) (a : A) (b : B) :
    (twoPartGraph GA GB M labelA labelB).Adj (.inl a) (.inr b) ↔
      M (labelA a) (labelB b) := Iff.rfl

-- Source: Er579.OctahedronExclusion:75
private def side {A B : Type*} : A ⊕ B → Bool
  | .inl _ => false
  | .inr _ => true

-- Source: Er579.OctahedronExclusion:79
private theorem side_false {A B : Type*} {x : A ⊕ B} (h : side x = false) :
    ∃ a, x = .inl a := by
  cases x with
  | inl a => exact ⟨a, rfl⟩
  | inr b => simp [side] at h

-- Source: Er579.OctahedronExclusion:85
private theorem side_true {A B : Type*} {x : A ⊕ B} (h : side x = true) :
    ∃ b, x = .inr b := by
  cases x with
  | inl a => simp [side] at h
  | inr b => exact ⟨b, rfl⟩

-- Source: Er579.OctahedronExclusion:91
private def MonoTriangle (color : OctVertex → Bool) : Prop :=
  ∃ x y z : OctVertex, x.1 ≠ y.1 ∧ y.1 ≠ z.1 ∧ z.1 ≠ x.1 ∧
    color x = color y ∧ color y = color z

-- Source: Er579.OctahedronExclusion:95
private def MonoC4 (color : OctVertex → Bool) : Prop :=
  ∃ x y z w : OctVertex, x ≠ z ∧ y ≠ w ∧
    x.1 ≠ y.1 ∧ y.1 ≠ z.1 ∧ z.1 ≠ w.1 ∧ w.1 ≠ x.1 ∧
    color x = color y ∧ color y = color z ∧ color z = color w

-- Source: Er579.OctahedronExclusion:100
private def StarPartition (color : OctVertex → Bool) : Prop :=
  ∃ i j k : Fin 3, ∃ s t : Fin 2,
    i ≠ j ∧ i ≠ k ∧ j ≠ k ∧ s ≠ t ∧
    color ⟨i, 0⟩ = false ∧ color ⟨i, 1⟩ = false ∧
    color ⟨j, 0⟩ = true ∧ color ⟨j, 1⟩ = true ∧
    color ⟨k, s⟩ = false ∧ color ⟨k, t⟩ = true

-- Source: Er579.OctahedronExclusion:107
/-- Exhaustive finite classification of all 64 ways to place six vertices in two parts. -/
private theorem color_partition : ∀ color : OctVertex → Bool,
    MonoTriangle color ∨ MonoC4 color ∨ StarPartition color := by
  let _ : DecidablePred MonoTriangle := fun color => by
    unfold MonoTriangle
    infer_instance
  let _ : DecidablePred MonoC4 := fun color => by
    unfold MonoC4
    infer_instance
  let _ : DecidablePred StarPartition := fun color => by
    unfold StarPartition
    infer_instance
  decide

-- Source: Er579.OctahedronExclusion:121
private theorem no_mono_triangle {A B PA PB : Type*}
    (GA : SimpleGraph A) (GB : SimpleGraph B) (M : PA → PB → Prop)
    (labelA : A → PA) (labelB : B → PB)
    (hTA : TriangleFree GA) (hTB : TriangleFree GB)
    (f : SimpleGraph.Copy octahedron (twoPartGraph GA GB M labelA labelB)) :
    ¬ MonoTriangle (fun x => side (f x)) := by
  rintro ⟨x, y, z, hxy, hyz, hzx, hcxy, hcyz⟩
  have exy := f.toHom.map_adj ((octahedron_adj x y).2 hxy)
  have eyz := f.toHom.map_adj ((octahedron_adj y z).2 hyz)
  have ezx := f.toHom.map_adj ((octahedron_adj z x).2 hzx)
  cases hx : f x with
  | inl a =>
    have hyc : side (f y) = false := by simpa [side, hx] using hcxy.symm
    have hzc : side (f z) = false := hcyz.symm.trans hyc
    obtain ⟨b, hy⟩ := side_false hyc
    obtain ⟨c, hz⟩ := side_false hzc
    exact hTA a b c (by simpa [SimpleGraph.Copy.toHom_apply, twoPartGraph_adj_inl_inl, twoPartGraph_adj_inr_inr, twoPartGraph_adj_inl_inr, hx, hy] using exy)
      (by simpa [SimpleGraph.Copy.toHom_apply, twoPartGraph_adj_inl_inl, twoPartGraph_adj_inr_inr, twoPartGraph_adj_inl_inr, hy, hz] using eyz) (by simpa [SimpleGraph.Copy.toHom_apply, twoPartGraph_adj_inl_inl, twoPartGraph_adj_inr_inr, twoPartGraph_adj_inl_inr, hz, hx] using ezx)
  | inr a =>
    have hyc : side (f y) = true := by simpa [side, hx] using hcxy.symm
    have hzc : side (f z) = true := hcyz.symm.trans hyc
    obtain ⟨b, hy⟩ := side_true hyc
    obtain ⟨c, hz⟩ := side_true hzc
    exact hTB a b c (by simpa [SimpleGraph.Copy.toHom_apply, twoPartGraph_adj_inl_inl, twoPartGraph_adj_inr_inr, twoPartGraph_adj_inl_inr, hx, hy] using exy)
      (by simpa [SimpleGraph.Copy.toHom_apply, twoPartGraph_adj_inl_inl, twoPartGraph_adj_inr_inr, twoPartGraph_adj_inl_inr, hy, hz] using eyz) (by simpa [SimpleGraph.Copy.toHom_apply, twoPartGraph_adj_inl_inl, twoPartGraph_adj_inr_inr, twoPartGraph_adj_inl_inr, hz, hx] using ezx)

-- Source: Er579.OctahedronExclusion:147
private theorem no_mono_c4 {A B PA PB : Type*}
    (GA : SimpleGraph A) (GB : SimpleGraph B) (M : PA → PB → Prop)
    (labelA : A → PA) (labelB : B → PB)
    (hCA : C4Free GA) (hCB : C4Free GB)
    (f : SimpleGraph.Copy octahedron (twoPartGraph GA GB M labelA labelB)) :
    ¬ MonoC4 (fun x => side (f x)) := by
  rintro ⟨x, y, z, w, hxz, hyw, hxy, hyz, hzw, hwx, hcxy, hcyz, hczw⟩
  have exy := f.toHom.map_adj ((octahedron_adj x y).2 hxy)
  have eyz := f.toHom.map_adj ((octahedron_adj y z).2 hyz)
  have ezw := f.toHom.map_adj ((octahedron_adj z w).2 hzw)
  have ewx := f.toHom.map_adj ((octahedron_adj w x).2 hwx)
  have efxz : f x ≠ f z := f.injective.ne hxz
  have efyw : f y ≠ f w := f.injective.ne hyw
  cases hx : f x with
  | inl a =>
    have hyc : side (f y) = false := by simpa [side, hx] using hcxy.symm
    have hzc : side (f z) = false := hcyz.symm.trans hyc
    have hwc : side (f w) = false := hczw.symm.trans hzc
    obtain ⟨b, hy⟩ := side_false hyc
    obtain ⟨c, hz⟩ := side_false hzc
    obtain ⟨d, hw⟩ := side_false hwc
    exact hCA a b c d (by simpa [hx, hz] using efxz)
      (by simpa [hy, hw] using efyw)
      (by simpa [SimpleGraph.Copy.toHom_apply, twoPartGraph_adj_inl_inl, twoPartGraph_adj_inr_inr, twoPartGraph_adj_inl_inr, hx, hy] using exy) (by simpa [SimpleGraph.Copy.toHom_apply, twoPartGraph_adj_inl_inl, twoPartGraph_adj_inr_inr, twoPartGraph_adj_inl_inr, hy, hz] using eyz)
      (by simpa [SimpleGraph.Copy.toHom_apply, twoPartGraph_adj_inl_inl, twoPartGraph_adj_inr_inr, twoPartGraph_adj_inl_inr, hz, hw] using ezw) (by simpa [SimpleGraph.Copy.toHom_apply, twoPartGraph_adj_inl_inl, twoPartGraph_adj_inr_inr, twoPartGraph_adj_inl_inr, hw, hx] using ewx)
  | inr a =>
    have hyc : side (f y) = true := by simpa [side, hx] using hcxy.symm
    have hzc : side (f z) = true := hcyz.symm.trans hyc
    have hwc : side (f w) = true := hczw.symm.trans hzc
    obtain ⟨b, hy⟩ := side_true hyc
    obtain ⟨c, hz⟩ := side_true hzc
    obtain ⟨d, hw⟩ := side_true hwc
    exact hCB a b c d (by simpa [hx, hz] using efxz)
      (by simpa [hy, hw] using efyw)
      (by simpa [SimpleGraph.Copy.toHom_apply, twoPartGraph_adj_inl_inl, twoPartGraph_adj_inr_inr, twoPartGraph_adj_inl_inr, hx, hy] using exy) (by simpa [SimpleGraph.Copy.toHom_apply, twoPartGraph_adj_inl_inl, twoPartGraph_adj_inr_inr, twoPartGraph_adj_inl_inr, hy, hz] using eyz)
      (by simpa [SimpleGraph.Copy.toHom_apply, twoPartGraph_adj_inl_inl, twoPartGraph_adj_inr_inr, twoPartGraph_adj_inl_inr, hz, hw] using ezw) (by simpa [SimpleGraph.Copy.toHom_apply, twoPartGraph_adj_inl_inl, twoPartGraph_adj_inr_inr, twoPartGraph_adj_inl_inr, hw, hx] using ewx)

-- Source: Er579.OctahedronExclusion:184
/-- A labelled two-part graph with the exact five-edge exclusions contains no noninduced K222. -/
theorem twoPartGraph_octahedron_free {A B PA PB : Type*}
    (GA : SimpleGraph A) (GB : SimpleGraph B)
    (H : SimpleGraph PA) (HB : SimpleGraph PB)
    (M : PA → PB → Prop) (labelA : A → PA) (labelB : B → PB)
    (hTA : TriangleFree GA) (hTB : TriangleFree GB)
    (hCA : C4Free GA) (hCB : C4Free GB)
    (hA : ∀ a a', GA.Adj a a' → H.Adj (labelA a) (labelA a'))
    (hB : ∀ b b', GB.Adj b b' → HB.Adj (labelB b) (labelB b'))
    (hLeaves : ∀ b w z, GB.Adj b w → GB.Adj b z → w ≠ z → labelB w ≠ labelB z)
    (hCompat : ∀ q q', H.Adj q q' → ∀ b w z,
      HB.Adj b w → HB.Adj b z → w ≠ z →
        ¬ (M q w ∧ M q z ∧ M q' b ∧ M q' w ∧ M q' z)) :
    octahedron.Free (twoPartGraph GA GB M labelA labelB) := by
  rintro ⟨f⟩
  rcases color_partition (fun x => side (f x)) with hT | hC | hP
  · exact no_mono_triangle GA GB M labelA labelB hTA hTB f hT
  · exact no_mono_c4 GA GB M labelA labelB hCA hCB f hC
  obtain ⟨i, j, k, s, t, hij, hik, hjk, _hst, ci0, _ci1, cj0, cj1, cks, ckt⟩ := hP
  obtain ⟨u, hu⟩ := side_false ci0
  obtain ⟨w, hw⟩ := side_true cj0
  obtain ⟨z, hz⟩ := side_true cj1
  obtain ⟨a, ha⟩ := side_false cks
  obtain ⟨b, hb⟩ := side_true ckt
  have eau : GA.Adj a u := by
    simpa [SimpleGraph.Copy.toHom_apply, twoPartGraph_adj_inl_inl, twoPartGraph_adj_inr_inr, twoPartGraph_adj_inl_inr, ha, hu] using f.toHom.map_adj ((octahedron_adj ⟨k, s⟩ ⟨i, 0⟩).2 hik.symm)
  have ebw : GB.Adj b w := by
    simpa [SimpleGraph.Copy.toHom_apply, twoPartGraph_adj_inl_inl, twoPartGraph_adj_inr_inr, twoPartGraph_adj_inl_inr, hb, hw] using f.toHom.map_adj ((octahedron_adj ⟨k, t⟩ ⟨j, 0⟩).2 hjk.symm)
  have ebz : GB.Adj b z := by
    simpa [SimpleGraph.Copy.toHom_apply, twoPartGraph_adj_inl_inl, twoPartGraph_adj_inr_inr, twoPartGraph_adj_inl_inr, hb, hz] using f.toHom.map_adj ((octahedron_adj ⟨k, t⟩ ⟨j, 1⟩).2 hjk.symm)
  have hwz : w ≠ z := by
    have hpos : (⟨j, 0⟩ : OctVertex) ≠ ⟨j, 1⟩ := by simp
    simpa [hw, hz] using f.injective.ne hpos
  have maw : M (labelA a) (labelB w) := by
    simpa [SimpleGraph.Copy.toHom_apply, twoPartGraph_adj_inl_inl, twoPartGraph_adj_inr_inr, twoPartGraph_adj_inl_inr, ha, hw] using f.toHom.map_adj ((octahedron_adj ⟨k, s⟩ ⟨j, 0⟩).2 hjk.symm)
  have maz : M (labelA a) (labelB z) := by
    simpa [SimpleGraph.Copy.toHom_apply, twoPartGraph_adj_inl_inl, twoPartGraph_adj_inr_inr, twoPartGraph_adj_inl_inr, ha, hz] using f.toHom.map_adj ((octahedron_adj ⟨k, s⟩ ⟨j, 1⟩).2 hjk.symm)
  have mub : M (labelA u) (labelB b) := by
    simpa [SimpleGraph.Copy.toHom_apply, twoPartGraph_adj_inl_inl, twoPartGraph_adj_inr_inr, twoPartGraph_adj_inl_inr, hu, hb] using f.toHom.map_adj ((octahedron_adj ⟨i, 0⟩ ⟨k, t⟩).2 hik)
  have muw : M (labelA u) (labelB w) := by
    simpa [SimpleGraph.Copy.toHom_apply, twoPartGraph_adj_inl_inl, twoPartGraph_adj_inr_inr, twoPartGraph_adj_inl_inr, hu, hw] using f.toHom.map_adj ((octahedron_adj ⟨i, 0⟩ ⟨j, 0⟩).2 hij)
  have muz : M (labelA u) (labelB z) := by
    simpa [SimpleGraph.Copy.toHom_apply, twoPartGraph_adj_inl_inl, twoPartGraph_adj_inr_inr, twoPartGraph_adj_inl_inr, hu, hz] using f.toHom.map_adj ((octahedron_adj ⟨i, 0⟩ ⟨j, 1⟩).2 hij)
  exact hCompat _ _ (hA _ _ eau) _ _ _ (hB _ _ ebw) (hB _ _ ebz)
    (hLeaves _ _ _ ebw ebz hwz) ⟨maw, maz, mub, muw, muz⟩

end Er579

end

/- Source fragment: Er579.RandomRealization.Cleanup. Original licenses and source proofs retained. -/

section

/-! Delete one specified vertex from each ordered triangle/four-cycle.
Ordered occurrences avoid quotienting cycles by their dihedral symmetries;
their overcount is harmless in the expectation bounds. -/

namespace Er579.RandomRealization

open scoped BigOperators Classical

variable {V : Type*} [Fintype V]

-- Source: Er579.RandomRealization.Cleanup:16
noncomputable def triangleOccurrences (G : SimpleGraph V) : Finset (V × V × V) := by
  classical
  exact Finset.univ.filter fun abc =>
    G.Adj abc.1 abc.2.1 ∧ G.Adj abc.2.1 abc.2.2 ∧ G.Adj abc.2.2 abc.1

-- Source: Er579.RandomRealization.Cleanup:21
noncomputable def squareOccurrences (G : SimpleGraph V) : Finset (V × V × V × V) := by
  classical
  exact Finset.univ.filter fun abcd =>
    abcd.1 ≠ abcd.2.2.1 ∧ abcd.2.1 ≠ abcd.2.2.2 ∧
      G.Adj abcd.1 abcd.2.1 ∧ G.Adj abcd.2.1 abcd.2.2.1 ∧
      G.Adj abcd.2.2.1 abcd.2.2.2 ∧ G.Adj abcd.2.2.2 abcd.1

-- Source: Er579.RandomRealization.Cleanup:28
noncomputable def cleanupVertices (G : SimpleGraph V) : Finset V := by
  classical
  exact (triangleOccurrences G).image Prod.fst ∪ (squareOccurrences G).image Prod.fst

-- Source: Er579.RandomRealization.Cleanup:32
abbrev CleanVertex (G : SimpleGraph V) := {v : V // v ∉ cleanupVertices G}

-- Source: Er579.RandomRealization.Cleanup:34
def cleanedGraph (G : SimpleGraph V) : SimpleGraph (CleanVertex G) :=
  G.comap Subtype.val

-- Source: Er579.RandomRealization.Cleanup:37
theorem cleanupVertices_card_le (G : SimpleGraph V) :
    (cleanupVertices G).card ≤ (triangleOccurrences G).card + (squareOccurrences G).card := by
  classical
  unfold cleanupVertices
  exact (Finset.card_union_le _ _).trans
    (Nat.add_le_add (Finset.card_image_le) (Finset.card_image_le))

-- Source: Er579.RandomRealization.Cleanup:44
theorem cleanedGraph_triangleFree (G : SimpleGraph V) : TriangleFree (cleanedGraph G) := by
  classical
  intro a b c hab hbc hca
  have hocc : (a.val, b.val, c.val) ∈ triangleOccurrences G := by
    simp only [triangleOccurrences, Finset.mem_filter, Finset.mem_univ, true_and]
    exact ⟨hab, hbc, hca⟩
  have hbad : a.val ∈ cleanupVertices G := by
    unfold cleanupVertices
    apply Finset.mem_union_left
    exact Finset.mem_image.mpr ⟨(a.val, b.val, c.val), hocc, rfl⟩
  exact a.property hbad

-- Source: Er579.RandomRealization.Cleanup:56
theorem cleanedGraph_c4Free (G : SimpleGraph V) : C4Free (cleanedGraph G) := by
  classical
  intro a b c d hac hbd hab hbc hcd hda
  have hac' : a.val ≠ c.val := by
    intro h
    exact hac (Subtype.ext h)
  have hbd' : b.val ≠ d.val := by
    intro h
    exact hbd (Subtype.ext h)
  have hocc : (a.val, b.val, c.val, d.val) ∈ squareOccurrences G := by
    simp only [squareOccurrences, Finset.mem_filter, Finset.mem_univ, true_and]
    exact ⟨hac', hbd', hab, hbc, hcd, hda⟩
  have hbad : a.val ∈ cleanupVertices G := by
    unfold cleanupVertices
    apply Finset.mem_union_right
    exact Finset.mem_image.mpr ⟨(a.val, b.val, c.val, d.val), hocc, rfl⟩
  exact a.property hbad

-- Source: Er579.RandomRealization.Cleanup:74
theorem cleanVertex_card_eq (G : SimpleGraph V) :
    Fintype.card (CleanVertex G) = Fintype.card V - (cleanupVertices G).card := by
  classical
  unfold CleanVertex
  rw [Fintype.card_subtype_compl]
  simp

-- Source: Er579.RandomRealization.Cleanup:87
theorem cleanVertex_card_eq_real (G : SimpleGraph V) :
    (Fintype.card (CleanVertex G) : ℝ) =
      (Fintype.card V : ℝ) - (cleanupVertices G).card := by
  rw [cleanVertex_card_eq]
  exact Nat.cast_sub (Finset.card_le_card (Finset.subset_univ (cleanupVertices G)))

-- Source: Er579.RandomRealization.Cleanup:93
theorem cleanedGraph_indepNum_le (G : SimpleGraph V) :
    (cleanedGraph G).indepNum ≤ G.indepNum := by
  classical
  obtain ⟨s, hs⟩ := (cleanedGraph G).exists_isNIndepSet_indepNum
  have hI : G.IsIndepSet ((s.image Subtype.val : Finset V) : Set V) := by
    intro x hx y hy hxy
    obtain ⟨a, ha, rfl⟩ := Finset.mem_image.mp hx
    obtain ⟨b, hb, rfl⟩ := Finset.mem_image.mp hy
    exact hs.isIndepSet ha hb (fun hab => hxy (congrArg Subtype.val hab))
  have hcard : (s.image Subtype.val).card = (cleanedGraph G).indepNum := by
    rw [Finset.card_image_of_injective _ Subtype.val_injective, hs.card_eq]
  simpa only [hcard] using hI.card_le_indepNum

end Er579.RandomRealization

end

/- Source fragment: Er579.CrossDensity. Original licenses and source proofs retained. -/

section

namespace Er579.CrossDensity

open scoped BigOperators Classical
open RandomRealization

variable {A B Q F : Type*} [Fintype A] [Fintype B] [Fintype Q] [Fintype F]

-- Source: Er579.CrossDensity:13
noncomputable def crossPairs (C : A → B → Prop) : Finset (A × B) :=
  Finset.univ.filter (fun ab => C ab.1 ab.2)

-- Source: Er579.CrossDensity:16
noncomputable def neighborProfiles (M : Q → B → Prop) (q : Q) : Finset B :=
  Finset.univ.filter (M q)

-- Source: Er579.CrossDensity:19
theorem filter_card_indicator {X : Type*} [Fintype X] (P : X → Prop) :
    (Finset.univ.filter P).card = ∑ x : X, if P x then 1 else 0 := by
  classical
  rw [Finset.card_eq_sum_ones, Finset.sum_filter]

-- Source: Er579.CrossDensity:24
theorem filter_card_indicator_real {X : Type*} [Fintype X] (P : X → Prop) :
    ((Finset.univ.filter P).card : ℝ) = ∑ x : X, if P x then 1 else 0 := by
  exact_mod_cast filter_card_indicator P

-- Source: Er579.CrossDensity:28
theorem crossPairs_card_eq_sum (C : A → B → Prop) :
    (crossPairs C).card = ∑ a : A, (Finset.univ.filter (C a)).card := by
  rw [crossPairs, filter_card_indicator, Fintype.sum_prod_type]
  apply Finset.sum_congr rfl
  intro a _
  exact (filter_card_indicator (C a)).symm

-- Source: Er579.CrossDensity:35
theorem product_fiber_predicate_card (P : B → Prop) :
    (Finset.univ.filter (fun bf : B × F => P bf.1)).card =
      (Finset.univ.filter P).card * Fintype.card F := by
  rw [filter_card_indicator, Fintype.sum_prod_type, filter_card_indicator]
  rw [Finset.sum_mul]
  apply Finset.sum_congr rfl
  intro b _
  by_cases hb : P b <;> simp [hb]

-- Source: Er579.CrossDensity:44
/-- The exact number of prescribed cross pairs before either cleanup. -/
theorem blowup_crossPairs_card (m : Q → ℕ) (L : ℕ) (M : Q → B → Prop) :
    (crossPairs (fun (a : BlowupVertex m L) (b : B × F) => M a.1 b.1)).card =
      Fintype.card F * L ^ 5 * ∑ q : Q, m q * (neighborProfiles M q).card := by
  rw [crossPairs_card_eq_sum, Fintype.sum_sigma]
  simp_rw [product_fiber_predicate_card]
  simp only [Finset.sum_const, Finset.card_univ, Fintype.card_fin, smul_eq_mul]
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro q _
  unfold neighborProfiles
  ring

-- Source: Er579.CrossDensity:57
/-- This orientation matches the cap-density theorem: average B after
sampling an A profile. -/
noncomputable def weightedCrossDensity (νA : FiniteProbability Q)
    (νB : FiniteProbability B) (M : Q → B → Prop) : ℝ :=
  νB.expect (fun b => νA.event (fun q => M q b))

-- Source: Er579.CrossDensity:63
theorem weightedCrossDensity_eq_Amean (νA : FiniteProbability Q)
    (νB : FiniteProbability B) (M : Q → B → Prop) :
    weightedCrossDensity νA νB M = νA.expect (fun q => νB.event (M q)) := by
  classical
  have hB : (νA.prod νB).event (fun qb => M qb.1 qb.2) =
      νB.expect (fun b => νA.event (fun q => M q b)) := by
    rw [FiniteProbability.event_eq_expect_indicator, FiniteProbability.prod_expect_right]
    apply congrArg νB.expect
    funext b
    exact (FiniteProbability.event_eq_expect_indicator νA (fun q => M q b)).symm
  have hA : (νA.prod νB).event (fun qb => M qb.1 qb.2) =
      νA.expect (fun q => νB.event (M q)) := by
    rw [FiniteProbability.event_eq_expect_indicator, FiniteProbability.prod_expect]
    apply congrArg νA.expect
    funext q
    exact (FiniteProbability.event_eq_expect_indicator νB (M q)).symm
  exact hB.symm.trans hA

-- Source: Er579.CrossDensity:81
theorem uniform_event_card {X : Type*} [Fintype X] (ν : FiniteProbability X)
    (huniform : ∀ x, ν.weight x = 1 / (Fintype.card X : ℝ)) (P : X → Prop) :
    ν.event P = (Finset.univ.filter P).card / (Fintype.card X : ℝ) := by
  classical
  calc
    ν.event P = ∑ x : X, (if P x then (1 : ℝ) else 0) / Fintype.card X := by
      unfold FiniteProbability.event eventWeight
      apply Finset.sum_congr rfl
      intro x _
      by_cases hx : P x <;> simp [hx, huniform x]
    _ = (∑ x : X, if P x then (1 : ℝ) else 0) / Fintype.card X := by
      rw [Finset.sum_div]
    _ = (Finset.univ.filter P).card / (Fintype.card X : ℝ) := by
      rw [← filter_card_indicator_real]

-- Source: Er579.CrossDensity:96
theorem weightedCrossDensity_formula (νA : FiniteProbability Q)
    (νB : FiniteProbability B) (m : Q → ℕ) (M : Q → B → Prop)
    (hA : ∀ q, νA.weight q = (m q : ℝ) / totalMultiplicity m)
    (hB : ∀ b, νB.weight b = 1 / (Fintype.card B : ℝ)) :
    weightedCrossDensity νA νB M =
      (∑ q : Q, m q * (neighborProfiles M q).card : ℕ) /
        ((totalMultiplicity m : ℝ) * Fintype.card B) := by
  classical
  rw [weightedCrossDensity_eq_Amean]
  simp_rw [uniform_event_card νB hB]
  unfold FiniteProbability.expect finiteExpectation
  simp_rw [hA]
  simp only [Nat.cast_sum, Nat.cast_mul, neighborProfiles]
  rw [Finset.sum_div]
  apply Finset.sum_congr rfl
  intro q _
  ring

-- Source: Er579.CrossDensity:114
theorem blowup_crossPairs_weighted_identity (νA : FiniteProbability Q)
    (νB : FiniteProbability B) (m : Q → ℕ) (L : ℕ) (M : Q → B → Prop)
    (hA : ∀ q, νA.weight q = (m q : ℝ) / totalMultiplicity m)
    (hB : ∀ b, νB.weight b = 1 / (Fintype.card B : ℝ))
    (hm : 0 < totalMultiplicity m) (hcardB : 0 < Fintype.card B) :
    ((crossPairs (fun (a : BlowupVertex m L) (b : B × F) => M a.1 b.1)).card : ℝ) =
      weightedCrossDensity νA νB M * Fintype.card (BlowupVertex m L) *
        Fintype.card (B × F) := by
  rw [blowup_crossPairs_card, weightedCrossDensity_formula νA νB m M hA hB,
    blowupVertex_card, Fintype.card_prod]
  have hmR : (totalMultiplicity m : ℝ) ≠ 0 := by exact_mod_cast (Nat.ne_of_gt hm)
  have hBR : (Fintype.card B : ℝ) ≠ 0 := by exact_mod_cast (Nat.ne_of_gt hcardB)
  push_cast
  field_simp [hmR, hBR]

-- Source: Er579.CrossDensity:129
theorem blowup_crossPairs_dense (νA : FiniteProbability Q)
    (νB : FiniteProbability B) (m : Q → ℕ) (L : ℕ) (M : Q → B → Prop)
    (hA : ∀ q, νA.weight q = (m q : ℝ) / totalMultiplicity m)
    (hB : ∀ b, νB.weight b = 1 / (Fintype.card B : ℝ))
    (hm : 0 < totalMultiplicity m) (hcardB : 0 < Fintype.card B)
    (t : ℕ) (hAt : Fintype.card (BlowupVertex m L) = t)
    (hBt : Fintype.card (B × F) = t) (p : ℝ)
    (hp : p ≤ weightedCrossDensity νA νB M) :
    p * (t : ℝ) ^ 2 ≤
      (crossPairs (fun (a : BlowupVertex m L) (b : B × F) => M a.1 b.1)).card := by
  rw [blowup_crossPairs_weighted_identity νA νB m L M hA hB hm hcardB, hAt, hBt]
  have h := mul_le_mul_of_nonneg_right hp (sq_nonneg (t : ℝ))
  simpa only [pow_two, mul_assoc] using h

-- Source: Er579.CrossDensity:143
abbrev Survivor {X : Type*} (S : Finset X) := {x : X // x ∉ S}

-- Source: Er579.CrossDensity:145
noncomputable def retainedPairs (C : A → B → Prop) (SA : Finset A) (SB : Finset B) :
    Finset (A × B) :=
  (crossPairs C).filter (fun ab => ab.1 ∉ SA ∧ ab.2 ∉ SB)

-- Source: Er579.CrossDensity:149
theorem survivor_crossPairs_card (C : A → B → Prop) (SA : Finset A) (SB : Finset B) :
    (crossPairs (fun (a : Survivor SA) (b : Survivor SB) => C a.val b.val)).card =
      (retainedPairs C SA SB).card := by
  classical
  let forget : Survivor SA × Survivor SB → A × B := fun ab => (ab.1.val, ab.2.val)
  have hinj : Function.Injective forget := by
    intro ab cd h
    apply Prod.ext
    · exact Subtype.ext (congrArg Prod.fst h)
    · exact Subtype.ext (congrArg Prod.snd h)
  have himage : (crossPairs (fun (a : Survivor SA) (b : Survivor SB) =>
      C a.val b.val)).image forget = retainedPairs C SA SB := by
    ext ab
    constructor
    · intro h
      obtain ⟨cd, hcd, rfl⟩ := Finset.mem_image.mp h
      have hc : C cd.1.val cd.2.val := (Finset.mem_filter.mp hcd).2
      simp only [retainedPairs, crossPairs, Finset.mem_filter, Finset.mem_univ, true_and]
      exact ⟨hc, cd.1.property, cd.2.property⟩
    · intro h
      rcases (Finset.mem_filter.mp h) with ⟨hab, ha, hb⟩
      have hc : C ab.1 ab.2 := (Finset.mem_filter.mp hab).2
      apply Finset.mem_image.mpr
      exact ⟨(⟨ab.1, ha⟩, ⟨ab.2, hb⟩), by simp [crossPairs, hc], rfl⟩
  rw [← himage, Finset.card_image_of_injective _ hinj]

-- Source: Er579.CrossDensity:175
/-- Every lost pair has a deleted A endpoint or a deleted B endpoint. -/
theorem crossPairs_cleanup_loss (C : A → B → Prop) (SA : Finset A) (SB : Finset B) :
    (crossPairs C).card ≤
      (crossPairs (fun (a : Survivor SA) (b : Survivor SB) => C a.val b.val)).card +
        SA.card * Fintype.card B + SB.card * Fintype.card A := by
  classical
  have hsubset : crossPairs C ⊆
      (retainedPairs C SA SB ∪ SA.product Finset.univ) ∪ Finset.univ.product SB := by
    intro ab hab
    by_cases ha : ab.1 ∈ SA
    · exact Finset.mem_union_left _ (Finset.mem_union_right _
        (Finset.mem_product.mpr ⟨ha, Finset.mem_univ _⟩))
    · by_cases hb : ab.2 ∈ SB
      · exact Finset.mem_union_right _ (Finset.mem_product.mpr ⟨Finset.mem_univ _, hb⟩)
      · exact Finset.mem_union_left _ (Finset.mem_union_left _
          (Finset.mem_filter.mpr ⟨hab, ha, hb⟩))
  have h1 := Finset.card_union_le (retainedPairs C SA SB) (SA.product Finset.univ)
  have h2 := Finset.card_union_le
    (retainedPairs C SA SB ∪ SA.product Finset.univ) (Finset.univ.product SB)
  have hc := Finset.card_le_card hsubset
  have hsurv := survivor_crossPairs_card C SA SB
  have hPA : (SA.product (Finset.univ : Finset B)).card = SA.card * Fintype.card B := by
    simp
  have hPB : ((Finset.univ : Finset A).product SB).card = SB.card * Fintype.card A := by
    simp [Nat.mul_comm]
  omega

-- Source: Er579.CrossDensity:202
def crossEdge (ab : A × B) : Sym2 (A ⊕ B) :=
  Sym2.mk (Sum.inl ab.1) (Sum.inr ab.2)

omit [Fintype A] [Fintype B] in

-- Source: Er579.CrossDensity:206
theorem crossEdge_injective : Function.Injective (crossEdge (A := A) (B := B)) := by
  intro ab cd h
  rcases Sym2.eq_iff.mp h with ⟨h₁, h₂⟩ | ⟨h₁, _⟩
  · apply Prod.ext
    · exact Sum.inl.inj h₁
    · exact Sum.inr.inj h₂
  · cases h₁

-- Source: Er579.CrossDensity:214
theorem crossPairs_le_twoPartGraph_edges {PA PB : Type*}
    (GA : SimpleGraph A) (GB : SimpleGraph B) (M : PA → PB → Prop)
    (labelA : A → PA) (labelB : B → PB) :
    (crossPairs (fun a b => M (labelA a) (labelB b))).card ≤
      (twoPartGraph GA GB M labelA labelB).edgeFinset.card := by
  classical
  let C : A → B → Prop := fun a b => M (labelA a) (labelB b)
  have hsubset : (crossPairs C).image crossEdge ⊆
      (twoPartGraph GA GB M labelA labelB).edgeFinset := by
    intro e he
    obtain ⟨ab, hab, rfl⟩ := Finset.mem_image.mp he
    apply SimpleGraph.mem_edgeFinset.mpr
    exact (Finset.mem_filter.mp hab).2
  calc
    (crossPairs C).card = ((crossPairs C).image crossEdge).card :=
      (Finset.card_image_of_injective _ crossEdge_injective).symm
    _ ≤ (twoPartGraph GA GB M labelA labelB).edgeFinset.card :=
      Finset.card_le_card hsubset

-- Source: Er579.CrossDensity:233
/-- Cleanup preserves the desired ordinary-graph density, counting
unordered edges exactly once across the two parts. -/
theorem cleaned_twoPartGraph_dense {PA PB : Type*}
    (GA : SimpleGraph A) (GB : SimpleGraph B) (M : PA → PB → Prop)
    (labelA : A → PA) (labelB : B → PB) (t : ℕ)
    (hA : Fintype.card A = t) (hB : Fintype.card B = t) (p ε : ℝ)
    (hp : p * (t : ℝ) ^ 2 ≤ (crossPairs (fun a b => M (labelA a) (labelB b))).card)
    (hdelA : ((cleanupVertices GA).card : ℝ) ≤ ε * t)
    (hdelB : ((cleanupVertices GB).card : ℝ) ≤ ε * t) :
    (p - 2 * ε) * (t : ℝ) ^ 2 ≤
      (twoPartGraph (cleanedGraph GA) (cleanedGraph GB) M
        (fun a => labelA a.val) (fun b => labelB b.val)).edgeFinset.card := by
  classical
  let C : A → B → Prop := fun a b => M (labelA a) (labelB b)
  have hloss : ((crossPairs C).card : ℝ) ≤
      ((crossPairs (fun (a : CleanVertex GA) (b : CleanVertex GB) =>
        C a.val b.val)).card : ℝ) +
      (cleanupVertices GA).card * (t : ℝ) + (cleanupVertices GB).card * (t : ℝ) := by
    have h := crossPairs_cleanup_loss C (cleanupVertices GA) (cleanupVertices GB)
    rw [hA, hB] at h
    exact_mod_cast h
  have hedge : ((crossPairs (fun (a : CleanVertex GA) (b : CleanVertex GB) =>
      C a.val b.val)).card : ℝ) ≤
      (twoPartGraph (cleanedGraph GA) (cleanedGraph GB) M
        (fun a => labelA a.val) (fun b => labelB b.val)).edgeFinset.card := by
    exact_mod_cast crossPairs_le_twoPartGraph_edges (cleanedGraph GA) (cleanedGraph GB)
      M (fun a => labelA a.val) (fun b => labelB b.val)
  have hdelA' := mul_le_mul_of_nonneg_right hdelA (Nat.cast_nonneg (α := ℝ) t)
  have hdelB' := mul_le_mul_of_nonneg_right hdelB (Nat.cast_nonneg (α := ℝ) t)
  nlinarith

end Er579.CrossDensity

end

/- Source fragment: Er579.CubeCaps. Original licenses and source proofs retained. -/

section

namespace Er579.CubeCaps

open scoped BigOperators
open BooleanAnalysis
open CapMoments RandomRealization

-- Source: Er579.CubeCaps:11
def signSum {n : ℕ} (x : BoolCube n) : ℝ := ∑ i, boolToSign (x i)

-- Source: Er579.CubeCaps:13
theorem signSum_snoc {n : ℕ} (x : BoolCube n) (b : Bool) :
    signSum (Fin.snoc x b) = signSum x + boolToSign b := by
  simp only [signSum, Fin.sum_univ_castSucc, Fin.snoc_castSucc, Fin.snoc_last]

-- Source: Er579.CubeCaps:17
theorem second_moment_succ (n : ℕ) :
    expect (fun x : BoolCube (n + 1) => signSum x ^ 2) =
      expect (fun x : BoolCube n => signSum x ^ 2) + 1 := by
  rw [Bonami.expect_succ_eq]
  change (expect (fun x : BoolCube n => (signSum (Fin.snoc x false)) ^ 2) +
    expect (fun x : BoolCube n => (signSum (Fin.snoc x true)) ^ 2)) / 2 = _
  simp only [signSum_snoc, boolToSign_false, boolToSign_true]
  rw [← ThresholdFunctions.expect_add]
  have h : (fun x : BoolCube n => (signSum x + 1) ^ 2 + (signSum x + -1) ^ 2) =
      (fun x => 2 * signSum x ^ 2 + 2) := by funext x; ring
  rw [h, ThresholdFunctions.expect_add, ThresholdFunctions.expect_const_mul,
    ThresholdFunctions.expect_const]
  ring

-- Source: Er579.CubeCaps:31
theorem second_moment (n : ℕ) :
    expect (fun x : BoolCube n => signSum x ^ 2) = n := by
  induction n with
  | zero => simp [signSum, expect]
  | succ n ih => rw [second_moment_succ, ih]; simp

-- Source: Er579.CubeCaps:37
theorem fourth_moment_succ (n : ℕ) :
    expect (fun x : BoolCube (n + 1) => signSum x ^ 4) =
      expect (fun x : BoolCube n => signSum x ^ 4) +
      6 * expect (fun x : BoolCube n => signSum x ^ 2) + 1 := by
  rw [Bonami.expect_succ_eq]
  change (expect (fun x : BoolCube n => (signSum (Fin.snoc x false)) ^ 4) +
    expect (fun x : BoolCube n => (signSum (Fin.snoc x true)) ^ 4)) / 2 = _
  simp only [signSum_snoc, boolToSign_false, boolToSign_true]
  rw [← ThresholdFunctions.expect_add]
  have h : (fun x : BoolCube n => (signSum x + 1) ^ 4 + (signSum x + -1) ^ 4) =
      (fun x => 2 * signSum x ^ 4 + 12 * signSum x ^ 2 + 2) := by funext x; ring
  rw [h, ThresholdFunctions.expect_add, ThresholdFunctions.expect_add,
    ThresholdFunctions.expect_const_mul, ThresholdFunctions.expect_const_mul,
    ThresholdFunctions.expect_const]
  ring

-- Source: Er579.CubeCaps:53
theorem fourth_moment (n : ℕ) :
    expect (fun x : BoolCube n => signSum x ^ 4) = 3 * (n : ℝ) ^ 2 - 2 * n := by
  induction n with
  | zero => simp [signSum, expect]
  | succ n ih => rw [fourth_moment_succ, ih, second_moment]; push_cast; ring

-- Source: Er579.CubeCaps:59
theorem fourth_moment_le (n : ℕ) :
    expect (fun x : BoolCube n => signSum x ^ 4) ≤ 3 * (n : ℝ) ^ 2 := by
  rw [fourth_moment]
  have : 0 ≤ (n : ℝ) := Nat.cast_nonneg n
  linarith

-- Source: Er579.CubeCaps:65
def antipode (n : ℕ) : BoolCube n ≃ BoolCube n where
  toFun x := fun i => !(x i)
  invFun x := fun i => !(x i)
  left_inv x := by funext i; simp
  right_inv x := by funext i; simp

-- Source: Er579.CubeCaps:71
theorem signSum_antipode (n : ℕ) (x : BoolCube n) :
    signSum (antipode n x) = -signSum x := by
  simp only [signSum, antipode, Equiv.coe_fn_mk, boolToSign_not, Finset.sum_neg_distrib]

-- Source: Er579.CubeCaps:75
theorem finiteExpectation_uniform {n : ℕ} (f : BooleanFunc n) :
    finiteExpectation (fun _ : BoolCube n => uniformWeight n) f = expect f := by
  simp only [finiteExpectation, expect, Finset.mul_sum]

-- Source: Er579.CubeCaps:79
theorem uniform_weight_sum (n : ℕ) :
    (∑ _x : BoolCube n, uniformWeight n) = 1 := by
  have h := ThresholdFunctions.expect_const (n := n) (1 : ℝ)
  simpa only [expect, Finset.mul_sum, mul_one] using h

-- Source: Er579.CubeCaps:84
theorem positive_cap_mass (n : ℕ) (hn : 0 < n) :
    3 / 32 ≤ eventWeight (fun _ : BoolCube n => uniformWeight n)
      (fun x => Real.sqrt (n : ℝ) / 2 ≤ signSum x) := by
  apply cap_mass_of_moments (fun _ : BoolCube n => uniformWeight n)
    (fun _ => pow_nonneg (by norm_num [uniformWeight]) _)
    (uniform_weight_sum n) signSum (n : ℝ) (by exact_mod_cast hn)
    (e := antipode n)
  · rw [finiteExpectation_uniform, second_moment]
  · rw [finiteExpectation_uniform]
    exact fourth_moment_le n
  · intro x; rfl
  · exact signSum_antipode n

end Er579.CubeCaps

end

/- Source fragment: Er579.CubeGeneratorLimits. Original licenses and source proofs retained. -/

section

namespace Er579.CubeGenerators

open Filter
open scoped Topology

-- Source: Er579.CubeGeneratorLimits:10
def dimension (k : ℕ) : ℕ := k ^ 6

-- Source: Er579.CubeGeneratorLimits:12
def degree (k : ℕ) : ℕ := 2 ^ (4 * k ^ 3)

-- Source: Er579.CubeGeneratorLimits:14
noncomputable def theta (k : ℕ) : ℝ := 1 / (k : ℝ) ^ 2

-- Source: Er579.CubeGeneratorLimits:16
noncomputable def accuracy (k : ℕ) : ℝ := 1 / (2 : ℝ) ^ (k ^ 3)

-- Source: Er579.CubeGeneratorLimits:18
noncomputable def sizeBound (k : ℕ) : ℝ :=
  2 * Real.exp (4 * (k : ℝ) ^ 3 - (k : ℝ) ^ 4 / 4)

-- Source: Er579.CubeGeneratorLimits:21
noncomputable def intersectionBound (k : ℕ) : ℝ :=
  Real.exp (-8 * (k : ℝ) ^ 3 + (Real.exp 16 - 1) * (k : ℝ) ^ 2)

-- Source: Er579.CubeGeneratorLimits:24
noncomputable def fourBound (k : ℕ) : ℝ :=
  Real.exp (16 * (k : ℝ) ^ 3 - 2 * (k : ℝ) ^ 4)

-- Source: Er579.CubeGeneratorLimits:27
noncomputable def spectralBound (k : ℕ) : ℝ :=
  2 * Real.exp ((k : ℝ) ^ 6 - (2 : ℝ) ^ (2 * k ^ 3) / 16)

-- Source: Er579.CubeGeneratorLimits:30
noncomputable def failureBound (k : ℕ) : ℝ :=
  sizeBound k + intersectionBound k + fourBound k + spectralBound k

-- Source: Er579.CubeGeneratorLimits:33
theorem degree_pos (k : ℕ) : 0 < degree k := by
  exact pow_pos (by norm_num) _

-- Source: Er579.CubeGeneratorLimits:36
theorem accuracy_pos (k : ℕ) : 0 < accuracy k := by
  exact one_div_pos.mpr (pow_pos (by norm_num) _)

-- Source: Er579.CubeGeneratorLimits:39
theorem accuracy_le_one (k : ℕ) : accuracy k ≤ 1 := by
  unfold accuracy
  apply (div_le_one (pow_pos (by norm_num) _)).2
  exact one_le_pow₀ (by norm_num)

-- Source: Er579.CubeGeneratorLimits:44
theorem degree_le_exp (k : ℕ) : (degree k : ℝ) ≤ Real.exp (4 * (k : ℝ) ^ 3) := by
  unfold degree
  push_cast
  calc
    (2 : ℝ) ^ (4 * k ^ 3) ≤ (Real.exp 1) ^ (4 * k ^ 3) := by
      apply pow_le_pow_left₀ (by norm_num)
      linarith [Real.add_one_le_exp (1 : ℝ)]
    _ = Real.exp (4 * (k : ℝ) ^ 3) := by
      rw [← Real.exp_nat_mul]
      congr 1
      push_cast
      ring

-- Source: Er579.CubeGeneratorLimits:57
theorem accuracy_degree_identity (k : ℕ) :
    (degree k : ℝ) * accuracy k ^ 2 = (2 : ℝ) ^ (2 * k ^ 3) := by
  unfold degree accuracy
  push_cast
  have hp : (2 : ℝ) ^ (k ^ 3) ≠ 0 := pow_ne_zero _ (by norm_num)
  rw [div_pow]
  norm_num only [one_pow]
  rw [← pow_mul]
  have he : 4 * k ^ 3 = 2 * k ^ 3 + k ^ 3 * 2 := by omega
  rw [he, pow_add]
  field_simp

-- Source: Er579.CubeGeneratorLimits:69
private theorem exp_neg_nat_tendsto :
    Tendsto (fun k : ℕ => Real.exp (-(k : ℝ))) atTop (𝓝 0) := by
  exact Real.tendsto_exp_neg_atTop_nhds_zero.comp tendsto_natCast_atTop_atTop

-- Source: Er579.CubeGeneratorLimits:73
private theorem exp_limit_from_bound (f : ℕ → ℝ)
    (h : ∀ᶠ k in atTop, f k ≤ -(k : ℝ)) :
    Tendsto (fun k => Real.exp (f k)) atTop (𝓝 0) := by
  apply squeeze_zero' (Eventually.of_forall (fun k => (Real.exp_pos _).le))
    (h.mono (fun k hk => Real.exp_le_exp.mpr hk)) exp_neg_nat_tendsto

-- Source: Er579.CubeGeneratorLimits:79
private theorem size_exponent_bound :
    ∀ᶠ k : ℕ in atTop, 4 * (k : ℝ) ^ 3 - (k : ℝ) ^ 4 / 4 ≤ -(k : ℝ) := by
  filter_upwards [eventually_ge_atTop 32] with k hk
  have hx : (32 : ℝ) ≤ k := by exact_mod_cast hk
  have hx1 : (1 : ℝ) ≤ k := by linarith
  have hcube : (k : ℝ) ≤ (k : ℝ) ^ 3 := by
    nlinarith [sq_nonneg ((k : ℝ) - 1)]
  have hmul := mul_nonneg (show 0 ≤ (k : ℝ) ^ 3 by positivity)
    (show 0 ≤ (k : ℝ) / 4 - 5 by linarith)
  nlinarith [show (k : ℝ) ^ 4 = (k : ℝ) ^ 3 * (k : ℝ) by ring]

-- Source: Er579.CubeGeneratorLimits:90
private theorem intersection_exponent_bound :
    ∀ᶠ k : ℕ in atTop,
      -8 * (k : ℝ) ^ 3 + (Real.exp 16 - 1) * (k : ℝ) ^ 2 ≤ -(k : ℝ) := by
  filter_upwards [(tendsto_natCast_atTop_atTop (R := ℝ)).eventually_ge_atTop
    (Real.exp 16 + 2)] with k hk
  have hx : (1 : ℝ) ≤ k := by linarith [Real.exp_pos (16 : ℝ)]
  have hsq : (k : ℝ) ≤ (k : ℝ) ^ 2 := by nlinarith
  have hmul := mul_nonneg (sq_nonneg (k : ℝ))
    (show 0 ≤ 8 * (k : ℝ) - (Real.exp 16 - 1) - 1 by linarith)
  nlinarith [show (k : ℝ) ^ 3 = (k : ℝ) ^ 2 * (k : ℝ) by ring]

-- Source: Er579.CubeGeneratorLimits:101
private theorem four_exponent_bound :
    ∀ᶠ k : ℕ in atTop, 16 * (k : ℝ) ^ 3 - 2 * (k : ℝ) ^ 4 ≤ -(k : ℝ) := by
  filter_upwards [eventually_ge_atTop 16] with k hk
  have hx : (16 : ℝ) ≤ k := by exact_mod_cast hk
  have hx1 : (1 : ℝ) ≤ k := by linarith
  have hcube : (k : ℝ) ≤ (k : ℝ) ^ 3 := by
    nlinarith [sq_nonneg ((k : ℝ) - 1)]
  have hmul := mul_nonneg (show 0 ≤ (k : ℝ) ^ 3 by positivity)
    (show 0 ≤ 2 * (k : ℝ) - 17 by linarith)
  nlinarith [show (k : ℝ) ^ 4 = (k : ℝ) ^ 3 * (k : ℝ) by ring]

-- Source: Er579.CubeGeneratorLimits:112
private theorem spectral_exponent_bound :
    ∀ᶠ k : ℕ in atTop, (k : ℝ) ^ 6 - (2 : ℝ) ^ (2 * k ^ 3) / 16 ≤ -(k : ℝ) := by
  have hlim : Tendsto (fun k : ℕ => (k : ℝ) ^ 6 / (2 : ℝ) ^ k) atTop (𝓝 0) :=
    tendsto_pow_const_div_const_pow_of_one_lt 6 (by norm_num)
  filter_upwards [hlim.eventually (gt_mem_nhds (show (0 : ℝ) < 1 / 32 by norm_num)),
    eventually_ge_atTop 2] with k hr hk
  have hx : (2 : ℝ) ≤ k := by exact_mod_cast hk
  have hpow : 32 * (k : ℝ) ^ 6 ≤ (2 : ℝ) ^ k := by
    have ht := (div_lt_iff₀ (pow_pos (show (0 : ℝ) < 2 by norm_num) k)).mp hr
    linarith
  have hexp : k ≤ 2 * k ^ 3 := by
    have hksq : 1 ≤ k ^ 2 := one_le_pow₀ (by omega)
    have hkcube : k ≤ k ^ 3 := by
      calc
        k = k * 1 := by omega
        _ ≤ k * k ^ 2 := Nat.mul_le_mul_left k hksq
        _ = k ^ 3 := by ring
    omega
  have hpower : (2 : ℝ) ^ k ≤ (2 : ℝ) ^ (2 * k ^ 3) :=
    pow_le_pow_right₀ (by norm_num) hexp
  have hxpow : (k : ℝ) ≤ (k : ℝ) ^ 6 := by
    calc
      (k : ℝ) = (k : ℝ) ^ 1 := by ring
      _ ≤ (k : ℝ) ^ 6 := pow_le_pow_right₀ (by linarith) (by norm_num)
  linarith

-- Source: Er579.CubeGeneratorLimits:138
theorem sizeBound_tendsto : Tendsto sizeBound atTop (𝓝 0) := by
  change Tendsto (fun k : ℕ => 2 * Real.exp (4 * (k : ℝ) ^ 3 - (k : ℝ) ^ 4 / 4)) _ _
  simpa only [sizeBound, mul_zero] using
    (exp_limit_from_bound _ size_exponent_bound).const_mul (2 : ℝ)

-- Source: Er579.CubeGeneratorLimits:143
theorem intersectionBound_tendsto : Tendsto intersectionBound atTop (𝓝 0) :=
  exp_limit_from_bound _ intersection_exponent_bound

-- Source: Er579.CubeGeneratorLimits:146
theorem fourBound_tendsto : Tendsto fourBound atTop (𝓝 0) :=
  exp_limit_from_bound _ four_exponent_bound

-- Source: Er579.CubeGeneratorLimits:149
theorem spectralBound_tendsto : Tendsto spectralBound atTop (𝓝 0) := by
  change Tendsto (fun k : ℕ => 2 * Real.exp ((k : ℝ) ^ 6 - (2 : ℝ) ^ (2 * k ^ 3) / 16)) _ _
  simpa only [spectralBound, mul_zero] using
    (exp_limit_from_bound _ spectral_exponent_bound).const_mul (2 : ℝ)

-- Source: Er579.CubeGeneratorLimits:154
theorem failureBound_tendsto : Tendsto failureBound atTop (𝓝 0) := by
  change Tendsto (fun k => sizeBound k + intersectionBound k + fourBound k + spectralBound k) _ _
  simpa only [failureBound, add_zero] using
    ((sizeBound_tendsto.add intersectionBound_tendsto).add fourBound_tendsto).add
      spectralBound_tendsto

-- Source: Er579.CubeGeneratorLimits:160
theorem failureBound_eventually_lt_one : ∀ᶠ k in atTop, failureBound k < 1 :=
  failureBound_tendsto.eventually (gt_mem_nhds (by norm_num))

end Er579.CubeGenerators

end

/- Source fragment: Er579.CubeProfiles. Original licenses and source proofs retained. -/

section

namespace Er579.CubeProfiles

open scoped BigOperators
open BooleanAnalysis BooleanAnalysis.Hypercontractivity

-- Source: Er579.CubeProfiles:10
def xor {n : ℕ} (x y : BoolCube n) : BoolCube n := fun i => Bool.xor (x i) (y i)

-- Source: Er579.CubeProfiles:12
def zero (n : ℕ) : BoolCube n := fun _ => false

-- Source: Er579.CubeProfiles:14
def one (n : ℕ) : BoolCube n := fun _ => true

-- Source: Er579.CubeProfiles:16
theorem xor_comm {n : ℕ} (x y : BoolCube n) : xor x y = xor y x := by
  funext i
  simp only [xor]
  cases x i <;> cases y i <;> rfl

-- Source: Er579.CubeProfiles:21
theorem xor_assoc {n : ℕ} (x y z : BoolCube n) : xor (xor x y) z = xor x (xor y z) := by
  funext i
  simp only [xor]
  cases x i <;> cases y i <;> cases z i <;> rfl

-- Source: Er579.CubeProfiles:26
theorem xor_self {n : ℕ} (x : BoolCube n) : xor x x = zero n := by
  funext i
  simp only [xor, zero]
  cases x i <;> rfl

-- Source: Er579.CubeProfiles:31
theorem xor_zero {n : ℕ} (x : BoolCube n) : xor x (zero n) = x := by
  funext i
  simp only [xor, zero]
  cases x i <;> rfl

-- Source: Er579.CubeProfiles:36
theorem xor_cancel {n : ℕ} (x t : BoolCube n) : xor (xor x t) t = x := by
  rw [xor_assoc, xor_self, xor_zero]

-- Source: Er579.CubeProfiles:39
def shift {n : ℕ} (t : BoolCube n) : BoolCube n ≃ BoolCube n where
  toFun x := xor x t
  invFun x := xor x t
  left_inv x := xor_cancel x t
  right_inv x := xor_cancel x t

-- Source: Er579.CubeProfiles:45
def translate {n : ℕ} (t : BoolCube n) (f : BooleanFunc n) : BooleanFunc n :=
  fun x => f (xor x t)

-- Source: Er579.CubeProfiles:48
theorem sign_xor (a b : Bool) : boolToSign (Bool.xor a b) =
    boolToSign a * boolToSign b := by
  cases a <;> cases b <;> norm_num [boolToSign]

-- Source: Er579.CubeProfiles:52
theorem chi_xor {n : ℕ} (S : Finset (Fin n)) (x t : BoolCube n) :
    chiS S (xor x t) = chiS S x * chiS S t := by
  simp only [chiS, xor, sign_xor, Finset.prod_mul_distrib]

-- Source: Er579.CubeProfiles:56
theorem expect_translate {n : ℕ} (t : BoolCube n) (f : BooleanFunc n) :
    expect (translate t f) = expect f := by
  unfold expect translate
  congr 1
  exact (shift t).sum_comp f

-- Source: Er579.CubeProfiles:62
theorem fourier_translate {n : ℕ} (t : BoolCube n) (f : BooleanFunc n)
    (S : Finset (Fin n)) :
    BooleanAnalysis.fourierCoeff (translate t f) S = chiS S t * BooleanAnalysis.fourierCoeff f S := by
  unfold BooleanAnalysis.fourierCoeff innerProduct expect translate
  have h : (∑ x : BoolCube n, f (xor x t) * chiS S x) =
      ∑ y : BoolCube n, f y * chiS S (xor y t) := by
    exact Fintype.sum_equiv (shift t) _ _ (fun x => by
      simp only [shift, Equiv.coe_fn_mk, xor_cancel])
  rw [h]
  simp_rw [chi_xor, ← mul_assoc]
  rw [← Finset.sum_mul]
  ring

-- Source: Er579.CubeProfiles:75
theorem innerProduct_translate {n : ℕ} (t : BoolCube n) (f : BooleanFunc n) :
    innerProduct f (translate t f) =
      ∑ S : Finset (Fin n), chiS S t * BooleanAnalysis.fourierCoeff f S ^ 2 := by
  rw [plancherel]
  apply Finset.sum_congr rfl
  intro S _
  rw [fourier_translate]
  ring

-- Source: Er579.CubeProfiles:84
theorem innerProduct_sum_right {n : ℕ} {ι : Type*} [Fintype ι]
    (f : BooleanFunc n) (g : ι → BooleanFunc n) :
    innerProduct f (fun x => ∑ i, g i x) = ∑ i, innerProduct f (g i) := by
  unfold innerProduct expect
  simp only [Finset.mul_sum]
  exact Finset.sum_comm

-- Source: Er579.CubeProfiles:91
theorem innerProduct_div_right {n : ℕ} (f g : BooleanFunc n) (c : ℝ) :
    innerProduct f (fun x => g x / c) = innerProduct f g / c := by
  simp only [innerProduct, expect, mul_div_assoc, Finset.sum_div]

-- Source: Er579.CubeProfiles:95
noncomputable def averageTranslate {n : ℕ} {ι : Type*} [Fintype ι]
    (s : ι → BoolCube n) (f : BooleanFunc n) : BooleanFunc n :=
  fun x => (∑ i, f (xor x (s i))) / Fintype.card ι

-- Source: Er579.CubeProfiles:99
noncomputable def eigenvalue {n : ℕ} {ι : Type*} [Fintype ι]
    (s : ι → BoolCube n) (S : Finset (Fin n)) : ℝ :=
  (∑ i, chiS S (s i)) / Fintype.card ι

-- Source: Er579.CubeProfiles:103
theorem averageTranslate_energy {n : ℕ} {ι : Type*} [Fintype ι]
    (s : ι → BoolCube n) (f : BooleanFunc n) :
    innerProduct f (averageTranslate s f) =
      ∑ S : Finset (Fin n), eigenvalue s S * BooleanAnalysis.fourierCoeff f S ^ 2 := by
  change innerProduct f (fun x => (∑ i, translate (s i) f x) / Fintype.card ι) = _
  rw [innerProduct_div_right, innerProduct_sum_right]
  simp_rw [innerProduct_translate]
  rw [Finset.sum_comm, Finset.sum_div]
  apply Finset.sum_congr rfl
  intro S _
  rw [← Finset.sum_mul]
  simp only [eigenvalue, div_mul_eq_mul_div]

-- Source: Er579.CubeProfiles:116
theorem antipodalNoise_energy {n : ℕ} (ρ : ℝ) (f : BooleanFunc n) :
    innerProduct f (noiseOp ρ (translate (one n) f)) =
      ∑ S : Finset (Fin n), (chiS S (one n) * ρ ^ S.card) * BooleanAnalysis.fourierCoeff f S ^ 2 := by
  rw [plancherel]
  apply Finset.sum_congr rfl
  intro S _
  rw [noiseOp_fourier, fourier_translate]
  ring

-- Source: Er579.CubeProfiles:125
/-- Uniform character approximation bounds the energy error directly,
without an operator-norm formalization. -/
theorem energy_comparison {n : ℕ} {ι : Type*} [Fintype ι]
    (s : ι → BoolCube n) (ρ ξ : ℝ) (f : BooleanFunc n)
    (hclose : ∀ S : Finset (Fin n),
      |eigenvalue s S - chiS S (one n) * ρ ^ S.card| ≤ ξ) :
    innerProduct f (noiseOp ρ (translate (one n) f)) ≤
      innerProduct f (averageTranslate s f) + ξ * innerProduct f f := by
  rw [antipodalNoise_energy, averageTranslate_energy, parseval]
  rw [Finset.mul_sum, ← Finset.sum_add_distrib]
  apply Finset.sum_le_sum
  intro S _
  have h := (abs_le.mp (hclose S)).1
  have hterm : chiS S (one n) * ρ ^ S.card ≤ eigenvalue s S + ξ := by linarith
  have hm := mul_le_mul_of_nonneg_right hterm (sq_nonneg (BooleanAnalysis.fourierCoeff f S))
  simpa only [add_mul] using hm

-- Source: Er579.CubeProfiles:142
def cayley {n : ℕ} {ι : Type*} (s : ι → BoolCube n) : SimpleGraph (BoolCube n) where
  Adj x y := x ≠ y ∧ ∃ i, xor x (s i) = y
  symm := by
    constructor
    rintro x y ⟨hne, i, hi⟩
    refine ⟨hne.symm, i, ?_⟩
    rw [← hi, xor_cancel]
  loopless := by
    constructor
    intro x
    exact fun h => h.1 rfl

-- Source: Er579.CubeProfiles:154
theorem translate_ne_self {n : ℕ} (x t : BoolCube n) (ht : t ≠ zero n) :
    xor x t ≠ x := by
  intro h
  have heq := congrArg (fun y => xor x y) h
  rw [← xor_assoc, xor_self, xor_comm (zero n) t, xor_zero] at heq
  exact ht heq

-- Source: Er579.CubeProfiles:161
theorem independent_energy_zero {n : ℕ} {ι : Type*} [Fintype ι]
    (s : ι → BoolCube n) (hs : ∀ i, s i ≠ zero n)
    (I : Finset (BoolCube n)) (hI : (cayley s).IsIndepSet I) :
    innerProduct (cubeIndicator (fun x => x ∈ I))
      (averageTranslate s (cubeIndicator (fun x => x ∈ I))) = 0 := by
  classical
  change innerProduct (cubeIndicator (fun x => x ∈ I))
    (fun x => (∑ i, translate (s i) (cubeIndicator (fun x => x ∈ I)) x) /
      Fintype.card ι) = 0
  rw [innerProduct_div_right, innerProduct_sum_right]
  have hzero : ∀ i, innerProduct (cubeIndicator (fun x => x ∈ I))
      (translate (s i) (cubeIndicator (fun x => x ∈ I))) = 0 := by
    intro i
    unfold innerProduct expect
    have heach : ∀ x : BoolCube n,
        cubeIndicator (fun x => x ∈ I) x *
          translate (s i) (cubeIndicator (fun x => x ∈ I)) x = 0 := by
      intro x
      by_cases hx : x ∈ I
      · have hy : xor x (s i) ∉ I := by
          intro hy
          exact ((cayley s).isIndepSet_iff.1 hI hx hy
            (translate_ne_self x (s i) (hs i)).symm)
            ⟨(translate_ne_self x (s i) (hs i)).symm, i, rfl⟩
        simp [cubeIndicator, translate, hx, hy]
      · simp [cubeIndicator, hx]
    simp only [heach, Finset.sum_const_zero, mul_zero]
  simp only [hzero, Finset.sum_const_zero, zero_div]

end Er579.CubeProfiles

end

/- Source fragment: Er579.CubeGeometry. Original licenses and source proofs retained. -/

section

namespace Er579.CubeGeometry

open scoped Classical
open BooleanAnalysis
open CubeProfiles

-- Source: Er579.CubeGeometry:10
/-- A direction is antipodal outside its exceptional coordinate set. -/
def nearAntipode {n : ℕ} (T : Finset (Fin n)) : BoolCube n :=
  fun j => !(decide (j ∈ T))

-- Source: Er579.CubeGeometry:14
theorem nearAntipode_injective {n : ℕ} :
    Function.Injective (nearAntipode (n := n)) := by
  intro T U h
  ext j
  have hj := congrFun h j
  by_cases hT : j ∈ T <;> by_cases hU : j ∈ U <;>
    simp_all [nearAntipode]

-- Source: Er579.CubeGeometry:22
theorem nearAntipode_ne_zero {n : ℕ} (T : Finset (Fin n))
    (hT : T.card < n) : nearAntipode T ≠ zero n := by
  have hcard : T.card < (Finset.univ : Finset (Fin n)).card := by
    simpa using hT
  obtain ⟨j, _, hj⟩ := Finset.exists_mem_notMem_of_card_lt_card hcard
  intro heq
  have hh := congrFun heq j
  simpa [nearAntipode, zero, hj] using hh

-- Source: Er579.CubeGeometry:31
theorem directions_injective {n : ℕ} {ι : Type*}
    (T : ι → Finset (Fin n)) (L : ℝ)
    (hsize : ∀ i, L ≤ (T i).card)
    (hinter : ∀ i j, i ≠ j → ((T i ∩ T j).card : ℝ) < L) :
    Function.Injective (fun i => nearAntipode (T i)) := by
  intro i j hij
  by_contra hne
  have hT : T i = T j := nearAntipode_injective hij
  have hlt := hinter i j hne
  rw [← hT, Finset.inter_self] at hlt
  exact (not_lt_of_ge (hsize i)) hlt

-- Source: Er579.CubeGeometry:43
theorem xor_left_injective {n : ℕ} (x : BoolCube n) :
    Function.Injective (fun y => xor x y) := by
  intro a b hab
  apply (shift x).injective
  simpa only [shift, Equiv.coe_fn_mk, CubeProfiles.xor_comm] using hab

-- Source: Er579.CubeGeometry:49
theorem xor_translated_pair {n : ℕ} (x a b : BoolCube n) :
    xor (xor x a) (xor x b) = xor a b := by
  funext j
  simp only [CubeProfiles.xor]
  cases x j <;> cases a j <;> cases b j <;> rfl

-- Source: Er579.CubeGeometry:55
theorem nearAntipode_triple_ne_zero {n : ℕ}
    (T U V : Finset (Fin n))
    (hsmall : T.card + U.card + V.card < n) :
    xor (nearAntipode T) (xor (nearAntipode U) (nearAntipode V)) ≠ zero n := by
  have hcard : (T ∪ U ∪ V).card < (Finset.univ : Finset (Fin n)).card := by
    have h1 := Finset.card_union_le T U
    have h2 := Finset.card_union_le (T ∪ U) V
    simp only [Finset.card_univ, Fintype.card_fin]
    omega
  obtain ⟨j, _, hj⟩ := Finset.exists_mem_notMem_of_card_lt_card hcard
  have hT : j ∉ T := fun h => hj (Finset.mem_union.mpr
    (Or.inl (Finset.mem_union.mpr (Or.inl h))))
  have hU : j ∉ U := fun h => hj (Finset.mem_union.mpr
    (Or.inl (Finset.mem_union.mpr (Or.inr h))))
  have hV : j ∉ V := fun h => hj (Finset.mem_union.mpr (Or.inr h))
  intro heq
  have hh := congrFun heq j
  simpa [CubeProfiles.xor, nearAntipode, zero, hT, hU, hV] using hh

-- Source: Er579.CubeGeometry:74
theorem cayley_triangleFree {n : ℕ} {ι : Type*} (s : ι → BoolCube n)
    (hthree : ∀ i j l, xor (s i) (xor (s j) (s l)) ≠ zero n) :
    TriangleFree (cayley s) := by
  intro x y z hxy hyz hzx
  obtain ⟨_, i, hi⟩ := hxy
  obtain ⟨_, j, hj⟩ := hyz
  obtain ⟨_, l, hl⟩ := hzx
  have hclosed : xor (xor (xor x (s i)) (s j)) (s l) = x := by
    rw [hi, hj, hl]
  rw [xor_assoc, xor_assoc] at hclosed
  apply hthree i j l
  apply xor_left_injective x
  simpa only [xor_zero] using hclosed

-- Source: Er579.CubeGeometry:88
theorem nearAntipode_cayley_triangleFree {n : ℕ} {ι : Type*}
    (T : ι → Finset (Fin n)) (L : ℕ)
    (hsize : ∀ i, (T i).card ≤ L) (hsmall : 3 * L < n) :
    TriangleFree (cayley (fun i => nearAntipode (T i))) := by
  apply cayley_triangleFree
  intro i j l
  apply nearAntipode_triple_ne_zero
  have hi := hsize i
  have hj := hsize j
  have hl := hsize l
  omega

-- Source: Er579.CubeGeometry:100
/-- Four distinct indices never sum to zero. -/
def FourIndependent {n : ℕ} {ι : Type*} (s : ι → BoolCube n) : Prop :=
  ∀ i j l r, i ≠ j → i ≠ l → i ≠ r → j ≠ l → j ≠ r → l ≠ r →
    xor (xor (s i) (s j)) (xor (s l) (s r)) ≠ zero n

-- Source: Er579.CubeGeometry:105
theorem pair_representation_unique {n : ℕ} {ι : Type*}
    (s : ι → BoolCube n) (hs : Function.Injective s) (hfour : FourIndependent s)
    {i j l r : ι} (hij : i ≠ j) (hlr : l ≠ r)
    (heq : xor (s i) (s j) = xor (s l) (s r)) :
    (i = l ∧ j = r) ∨ (i = r ∧ j = l) := by
  by_cases hil : i = l
  · left
    refine ⟨hil, hs ?_⟩
    subst l
    exact xor_left_injective (s i) heq
  by_cases hir : i = r
  · right
    refine ⟨hir, hs ?_⟩
    subst r
    rw [xor_comm (s l) (s i)] at heq
    exact xor_left_injective (s i) heq
  have hjl : j ≠ l := by
    intro hjl
    subst l
    have hieq : s i = s r := by
      rw [xor_comm (s i) (s j)] at heq
      exact xor_left_injective (s j) heq
    exact hir (hs hieq)
  have hjr : j ≠ r := by
    intro hjr
    subst r
    have hieq : s i = s l := by
      rw [xor_comm (s i) (s j), xor_comm (s l) (s j)] at heq
      exact xor_left_injective (s j) heq
    exact hil (hs hieq)
  have hz : xor (xor (s i) (s j)) (xor (s l) (s r)) = zero n := by
    rw [heq, CubeProfiles.xor_self]
  exact False.elim (hfour i j l r hij hil hir hjl hjr hlr hz)

-- Source: Er579.CubeGeometry:139
/-- A distinct profile pair has at most two common neighbours. -/
theorem common_neighbors_card_le_two {n : ℕ} {ι : Type*}
    (s : ι → BoolCube n) (hs : Function.Injective s) (hfour : FourIndependent s)
    (x y : BoolCube n) (hxy : x ≠ y) :
    (Finset.univ.filter (fun b => (cayley s).Adj b x ∧ (cayley s).Adj b y)).card ≤ 2 := by
  classical
  by_cases hcenter : ∃ b, (cayley s).Adj b x ∧ (cayley s).Adj b y
  · obtain ⟨b₀, ⟨_, i₀, hi₀⟩, ⟨_, j₀, hj₀⟩⟩ := hcenter
    have hij₀ : i₀ ≠ j₀ := by
      intro heq
      apply hxy
      rw [← hi₀, ← hj₀, heq]
    have hsubset : Finset.univ.filter (fun b =>
        (cayley s).Adj b x ∧ (cayley s).Adj b y) ⊆ {b₀, xor x (s j₀)} := by
      intro b hb
      obtain ⟨⟨_, i, hi⟩, ⟨_, j, hj⟩⟩ := (Finset.mem_filter.mp hb).2
      have hij : i ≠ j := by
        intro heq
        apply hxy
        rw [← hi, ← hj, heq]
      have hpair : xor (s i) (s j) = xor (s i₀) (s j₀) := by
        calc
          xor (s i) (s j) = xor x y := by
            rw [← hi, ← hj, xor_translated_pair]
          _ = xor (s i₀) (s j₀) := by
            rw [← hi₀, ← hj₀, xor_translated_pair]
      rcases pair_representation_unique s hs hfour hij hij₀ hpair with
        ⟨hii, _⟩ | ⟨hij₀, _⟩
      · have hbb : b = b₀ := by
          apply (shift (s i₀)).injective
          change xor b (s i₀) = xor b₀ (s i₀)
          rw [hii] at hi
          rw [hi, hi₀]
        simp [hbb]
      · have hbb : b = xor x (s j₀) := by
          rw [← hij₀, ← hi, xor_cancel]
        simp [hbb]
    exact (Finset.card_le_card hsubset).trans Finset.card_le_two
  · have hempty : Finset.univ.filter (fun b =>
        (cayley s).Adj b x ∧ (cayley s).Adj b y) = ∅ := by
      apply Finset.eq_empty_iff_forall_notMem.mpr
      intro b hb
      exact hcenter ⟨b, (Finset.mem_filter.mp hb).2⟩
    rw [hempty]
    simp

-- Source: Er579.CubeGeometry:185
theorem audited_dimension_bounds {k : ℕ} (hk : 5 ≤ k) :
    (k : ℝ) ^ 3 < (k : ℝ) ^ 4 / 4 ∧
      12 * (k : ℝ) ^ 4 < (k : ℝ) ^ 6 := by
  have hkR : (5 : ℝ) ≤ k := by exact_mod_cast hk
  have hkpos : (0 : ℝ) < k := by linarith
  have hlow : 4 * (k : ℝ) ^ 3 < (k : ℝ) ^ 4 := by
    calc
      4 * (k : ℝ) ^ 3 < (k : ℝ) * (k : ℝ) ^ 3 :=
        mul_lt_mul_of_pos_right (by linarith) (pow_pos hkpos 3)
      _ = (k : ℝ) ^ 4 := by ring
  have hhigh : 12 * (k : ℝ) ^ 4 < (k : ℝ) ^ 6 := by
    have hsq : (12 : ℝ) < (k : ℝ) ^ 2 := by nlinarith
    calc
      12 * (k : ℝ) ^ 4 < (k : ℝ) ^ 2 * (k : ℝ) ^ 4 :=
        mul_lt_mul_of_pos_right hsq (pow_pos hkpos 4)
      _ = (k : ℝ) ^ 6 := by ring
  exact ⟨by linarith, hhigh⟩

-- Source: Er579.CubeGeometry:203
theorem audited_direction_nonzero {k : ℕ} (hk : 5 ≤ k)
    (T : Finset (Fin (k ^ 6))) (hsize : (T.card : ℝ) ≤ 4 * (k : ℝ) ^ 4) :
    nearAntipode T ≠ zero (k ^ 6) := by
  apply nearAntipode_ne_zero
  have hd := (audited_dimension_bounds hk).2
  have hp : (0 : ℝ) ≤ (k : ℝ) ^ 4 := pow_nonneg (Nat.cast_nonneg _) _
  have hlt : (T.card : ℝ) < (k : ℝ) ^ 6 := by linarith
  exact_mod_cast hlt

-- Source: Er579.CubeGeometry:212
theorem audited_directions_injective {k : ℕ} (hk : 5 ≤ k) {ι : Type*}
    (T : ι → Finset (Fin (k ^ 6)))
    (hsize : ∀ i, (k : ℝ) ^ 4 / 4 ≤ (T i).card)
    (hinter : ∀ i j, i ≠ j → ((T i ∩ T j).card : ℝ) < (k : ℝ) ^ 3) :
    Function.Injective (fun i => nearAntipode (T i)) := by
  apply directions_injective T ((k : ℝ) ^ 4 / 4) hsize
  intro i j hij
  exact (hinter i j hij).trans (audited_dimension_bounds hk).1

-- Source: Er579.CubeGeometry:221
theorem audited_cayley_triangleFree {k : ℕ} (hk : 5 ≤ k) {ι : Type*}
    (T : ι → Finset (Fin (k ^ 6)))
    (hsize : ∀ i, ((T i).card : ℝ) ≤ 4 * (k : ℝ) ^ 4) :
    TriangleFree (cayley (fun i => nearAntipode (T i))) := by
  apply nearAntipode_cayley_triangleFree T (4 * k ^ 4)
  · intro i
    exact_mod_cast hsize i
  · have h := (audited_dimension_bounds hk).2
    have heq : (3 : ℝ) * (4 * (k : ℝ) ^ 4) = 12 * (k : ℝ) ^ 4 := by ring
    rw [← heq] at h
    exact_mod_cast h

-- Source: Er579.CubeGeometry:233
/-- All deterministic structural consequences of the audited tuple conditions. -/
theorem audited_geometry {k : ℕ} (hk : 5 ≤ k) {ι : Type*}
    (T : ι → Finset (Fin (k ^ 6)))
    (hlower : ∀ i, (k : ℝ) ^ 4 / 4 ≤ (T i).card)
    (hupper : ∀ i, ((T i).card : ℝ) ≤ 4 * (k : ℝ) ^ 4)
    (hinter : ∀ i j, i ≠ j → ((T i ∩ T j).card : ℝ) < (k : ℝ) ^ 3)
    (hfour : FourIndependent (fun i => nearAntipode (T i))) :
    (∀ i, nearAntipode (T i) ≠ zero (k ^ 6)) ∧
      Function.Injective (fun i => nearAntipode (T i)) ∧
      TriangleFree (cayley (fun i => nearAntipode (T i))) ∧
      ∀ x y, x ≠ y →
        (Finset.univ.filter (fun b =>
          (cayley (fun i => nearAntipode (T i))).Adj b x ∧
          (cayley (fun i => nearAntipode (T i))).Adj b y)).card ≤ 2 := by
  have hinj := audited_directions_injective hk T hlower hinter
  exact ⟨fun i => audited_direction_nonzero hk (T i) (hupper i), hinj,
    audited_cayley_triangleFree hk T hupper,
    fun x y hxy => common_neighbors_card_le_two _ hinj hfour x y hxy⟩

end Er579.CubeGeometry

end

/- Source fragment: Er579.RandomRealization.Bernoulli. Original licenses and source proofs retained. -/

section

/-! Exact finite Bernoulli product probabilities.  The same forced-bit
identity supplies the absent-edge estimate and each short-cycle expectation. -/

namespace Er579.RandomRealization

open scoped BigOperators Classical

variable {E : Type*} [Fintype E] [DecidableEq E]

-- Source: Er579.RandomRealization.Bernoulli:15
def bernoulliBitWeight (r : ℝ) (b : Bool) : ℝ := if b then r else 1 - r

-- Source: Er579.RandomRealization.Bernoulli:17
def bernoulliWeight (r : ℝ) (ω : E → Bool) : ℝ :=
  ∏ e, bernoulliBitWeight r (ω e)

-- Source: Er579.RandomRealization.Bernoulli:20
theorem bernoulliBitWeight_sum (r : ℝ) : ∑ b : Bool, bernoulliBitWeight r b = 1 := by
  simp [bernoulliBitWeight]

-- Source: Er579.RandomRealization.Bernoulli:23
theorem bernoulliWeight_sum (r : ℝ) : ∑ ω : E → Bool, bernoulliWeight r ω = 1 := by
  unfold bernoulliWeight
  rw [← Fintype.prod_sum]
  simp only [bernoulliBitWeight_sum, Finset.prod_const_one]

omit [DecidableEq E] in

-- Source: Er579.RandomRealization.Bernoulli:29
theorem bernoulliWeight_nonneg {r : ℝ} (hr0 : 0 ≤ r) (hr1 : r ≤ 1)
    (ω : E → Bool) : 0 ≤ bernoulliWeight r ω := by
  apply Finset.prod_nonneg
  intro e _
  cases ω e <;> simp only [bernoulliBitWeight, Bool.false_eq_true,
    if_false, if_true]
  · exact sub_nonneg.mpr hr1
  · exact hr0

-- Source: Er579.RandomRealization.Bernoulli:38
theorem bernoulliWeight_forced (r : ℝ) (K : Finset E) (b : Bool) :
    eventWeight (bernoulliWeight r) (fun ω => ∀ e ∈ K, ω e = b) =
      (bernoulliBitWeight r b) ^ K.card := by
  classical
  let f : E → Bool → ℝ := fun e x =>
    if e ∈ K then if x = b then bernoulliBitWeight r x else 0 else bernoulliBitWeight r x
  have hterm (ω : E → Bool) :
      (if ∀ e ∈ K, ω e = b then bernoulliWeight r ω else 0) = ∏ e, f e (ω e) := by
    by_cases h : ∀ e ∈ K, ω e = b
    · rw [if_pos h]
      unfold bernoulliWeight
      apply Finset.prod_congr rfl
      intro e _
      by_cases he : e ∈ K
      · simp only [f, if_pos he, if_pos (h e he)]
      · simp only [f, if_neg he]
    · rw [if_neg h]
      push Not at h
      obtain ⟨e, he, hne⟩ := h
      symm
      apply Finset.prod_eq_zero (Finset.mem_univ e)
      simp only [f, if_pos he, if_neg hne]
  unfold eventWeight
  trans ∑ ω : E → Bool, ∏ e, f e (ω e)
  · apply Finset.sum_congr rfl
    intro ω _
    by_cases h : ∀ e ∈ K, ω e = b
    · simpa only [if_pos h] using hterm ω
    · simpa only [if_neg h] using hterm ω
  rw [← Fintype.prod_sum]
  have hsum (e : E) : (∑ x : Bool, f e x) =
      if e ∈ K then bernoulliBitWeight r b else 1 := by
    by_cases he : e ∈ K
    · cases b <;> simp [f, he, bernoulliBitWeight]
    · simpa only [f, if_neg he] using bernoulliBitWeight_sum r
  simp_rw [hsum]
  simp [Finset.prod_ite_mem]

-- Source: Er579.RandomRealization.Bernoulli:76
theorem bernoulli_absent_weight (r : ℝ) (K : Finset E) :
    eventWeight (bernoulliWeight r) (fun ω => ∀ e ∈ K, ω e = false) =
      (1 - r) ^ K.card := by
  simpa only [bernoulliBitWeight, Bool.false_eq_true, if_false] using
    bernoulliWeight_forced r K false

-- Source: Er579.RandomRealization.Bernoulli:82
theorem bernoulli_present_weight (r : ℝ) (K : Finset E) :
    eventWeight (bernoulliWeight r) (fun ω => ∀ e ∈ K, ω e = true) = r ^ K.card := by
  simpa only [bernoulliBitWeight, if_true] using bernoulliWeight_forced r K true

-- Source: Er579.RandomRealization.Bernoulli:86
theorem bernoulli_absent_weight_le_exp {r : ℝ} (hr1 : r ≤ 1) (K : Finset E) :
    eventWeight (bernoulliWeight r) (fun ω => ∀ e ∈ K, ω e = false) ≤
      Real.exp (-r * K.card) := by
  rw [bernoulli_absent_weight]
  calc
    (1 - r) ^ K.card ≤ (Real.exp (-r)) ^ K.card := by
      exact pow_le_pow_left₀ (sub_nonneg.mpr hr1)
        (by linarith [Real.add_one_le_exp (-r)]) _
    _ = Real.exp (-r * K.card) := by
      rw [← Real.exp_nat_mul]
      congr 1
      ring

end Er579.RandomRealization

end

/- Source fragment: Er579.RandomRealization.ProductProbability. Original licenses and source proofs retained. -/

section

/-! Independent finite coordinates, used both for graph-edge bits and
for independent perfect-matching permutations. -/

namespace Er579.RandomRealization

open scoped BigOperators Classical

variable {E X : Type*} [Fintype E] [DecidableEq E]

-- Source: Er579.RandomRealization.ProductProbability:14
def productWeight (w : E → X → ℝ) (ω : E → X) : ℝ := ∏ e, w e (ω e)

-- Source: Er579.RandomRealization.ProductProbability:16
theorem productWeight_sum [Fintype X] (w : E → X → ℝ) (h : ∀ e, ∑ x, w e x = 1) :
    ∑ ω, productWeight w ω = 1 := by
  unfold productWeight
  rw [← Fintype.prod_sum]
  simp only [h, Finset.prod_const_one]

-- Source: Er579.RandomRealization.ProductProbability:22
theorem productWeight_nonneg (w : E → X → ℝ) (h : ∀ e x, 0 ≤ w e x)
    (ω : E → X) : 0 ≤ productWeight w ω := by
  exact Finset.prod_nonneg (fun e _ => h e (ω e))

-- Source: Er579.RandomRealization.ProductProbability:26
theorem productWeight_event [Fintype X] (w : E → X → ℝ) (P : E → X → Prop) :
    eventWeight (productWeight w) (fun ω => ∀ e, P e (ω e)) =
      ∏ e, eventWeight (w e) (P e) := by
  have hterm (ω : E → X) :
      (if ∀ e, P e (ω e) then productWeight w ω else 0) =
        ∏ e, if P e (ω e) then w e (ω e) else 0 := by
    by_cases h : ∀ e, P e (ω e)
    · rw [if_pos h]
      unfold productWeight
      apply Finset.prod_congr rfl
      intro e _
      rw [if_pos (h e)]
    · rw [if_neg h]
      push Not at h
      obtain ⟨e, he⟩ := h
      symm
      exact Finset.prod_eq_zero (Finset.mem_univ e) (if_neg he)
  unfold eventWeight
  trans ∑ ω : E → X, ∏ e, if P e (ω e) then w e (ω e) else 0
  · apply Finset.sum_congr rfl
    intro ω _
    by_cases h : ∀ e, P e (ω e)
    · simpa only [if_pos h] using hterm ω
    · simpa only [if_neg h] using hterm ω
  exact (Fintype.prod_sum (fun e x => if P e x then w e x else 0)).symm

end Er579.RandomRealization

end

/- Source fragment: Er579.CubeGenerators. Original licenses and source proofs retained. -/

section

namespace Er579.CubeGenerators

open Er579.RandomRealization
open BooleanAnalysis Er579.CubeProfiles
open scoped BigOperators Classical

section FiniteTools

variable {X E : Type*} [Fintype X] [Fintype E] [DecidableEq E]

-- Source: Er579.CubeGenerators:19
theorem expectation_mono (w : X → ℝ) (hw : ∀ x, 0 ≤ w x)
    {f g : X → ℝ} (h : ∀ x, f x ≤ g x) :
    finiteExpectation w f ≤ finiteExpectation w g := by
  exact Finset.sum_le_sum (fun x _ => mul_le_mul_of_nonneg_left (h x) (hw x))

-- Source: Er579.CubeGenerators:24
theorem expectation_const (w : X → ℝ) (hnorm : ∑ x, w x = 1) (c : ℝ) :
    finiteExpectation w (fun _ => c) = c := by
  simp only [finiteExpectation, ← Finset.sum_mul, hnorm, one_mul]

-- Source: Er579.CubeGenerators:28
theorem expectation_neg (w : X → ℝ) (f : X → ℝ) :
    finiteExpectation w (fun x => -f x) = -finiteExpectation w f := by
  simp only [finiteExpectation, mul_neg, Finset.sum_neg_distrib]

-- Source: Er579.CubeGenerators:32
theorem expectation_sub (w : X → ℝ) (f g : X → ℝ) :
    finiteExpectation w (fun x => f x - g x) =
      finiteExpectation w f - finiteExpectation w g := by
  simp only [finiteExpectation, mul_sub, Finset.sum_sub_distrib]

-- Source: Er579.CubeGenerators:37
theorem product_expectation (w : E → X → ℝ) (f : E → X → ℝ) :
    finiteExpectation (productWeight w) (fun ω => ∏ e, f e (ω e)) =
      ∏ e, finiteExpectation (w e) (f e) := by
  unfold finiteExpectation productWeight
  simp_rw [← Finset.prod_mul_distrib]
  exact (Fintype.prod_sum (fun e x => w e x * f e x)).symm

-- Source: Er579.CubeGenerators:44
theorem product_exp_sum (w : E → X → ℝ) (f : E → X → ℝ) (t : ℝ) :
    finiteExpectation (productWeight w) (fun ω => Real.exp (t * ∑ e, f e (ω e))) =
      ∏ e, finiteExpectation (w e) (fun x => Real.exp (t * f e x)) := by
  simp_rw [Finset.mul_sum, Real.exp_sum]
  exact product_expectation w (fun e x => Real.exp (t * f e x))

-- Source: Er579.CubeGenerators:50
theorem product_mgf_bound (w : E → X → ℝ) (hw : ∀ e x, 0 ≤ w e x)
    (f : E → X → ℝ) (t : ℝ) (b : E → ℝ)
    (hmgf : ∀ e, finiteExpectation (w e) (fun x => Real.exp (t * f e x)) ≤ Real.exp (b e)) :
    finiteExpectation (productWeight w) (fun ω => Real.exp (t * ∑ e, f e (ω e))) ≤
      Real.exp (∑ e, b e) := by
  rw [product_exp_sum, Real.exp_sum]
  apply Finset.prod_le_prod
  · intro e _
    exact Finset.sum_nonneg (fun x _ => mul_nonneg (hw e x) (Real.exp_pos _).le)
  · intro e _
    exact hmgf e

-- Source: Er579.CubeGenerators:62
theorem finite_chernoff (w : X → ℝ) (hw : ∀ x, 0 ≤ w x)
    (g : X → ℝ) (a t b : ℝ) (ht : 0 ≤ t)
    (hmgf : finiteExpectation w (fun x => Real.exp (t * g x)) ≤ Real.exp b) :
    eventWeight w (fun x => a ≤ g x) ≤ Real.exp (b - t * a) := by
  have hevent : eventWeight w (fun x => a ≤ g x) ≤
      eventWeight w (fun x => Real.exp (t * a) ≤ Real.exp (t * g x)) := by
    apply eventWeight_mono w hw
    intro x hx
    exact Real.exp_le_exp.mpr (mul_le_mul_of_nonneg_left hx ht)
  calc
    eventWeight w (fun x => a ≤ g x) ≤
        finiteExpectation w (fun x => Real.exp (t * g x)) / Real.exp (t * a) :=
      hevent.trans (finite_markov w hw _ (fun x => (Real.exp_pos _).le) _ (Real.exp_pos _))
    _ ≤ Real.exp b / Real.exp (t * a) :=
      div_le_div_of_nonneg_right hmgf (Real.exp_pos _).le
    _ = Real.exp (b - t * a) := (Real.exp_sub _ _).symm

-- Source: Er579.CubeGenerators:79
/-- A lossy bounded-observation MGF suffices for the spectral union bound.
The proof uses the second-order exponential remainder for arguments of size at most one. -/
theorem centered_mgf_bound (w : X → ℝ) (hw : ∀ x, 0 ≤ w x)
    (hnorm : ∑ x, w x = 1) (f : X → ℝ) (hf : ∀ x, |f x| ≤ 1)
    (t : ℝ) (ht : |t| ≤ 1 / 2) :
    finiteExpectation w (fun x => Real.exp (t * (f x - finiteExpectation w f))) ≤
      Real.exp (4 * t ^ 2) := by
  let μ := finiteExpectation w f
  have hμlo : -1 ≤ μ := by
    have h := expectation_mono w hw (fun x => (abs_le.mp (hf x)).1)
    simpa only [expectation_const w hnorm, μ] using h
  have hμhi : μ ≤ 1 := by
    have h := expectation_mono w hw (fun x => (abs_le.mp (hf x)).2)
    simpa only [expectation_const w hnorm, μ] using h
  have hpoint (x : X) :
      Real.exp (t * (f x - μ)) ≤ 1 + t * (f x - μ) + 4 * t ^ 2 := by
    have hcenter : |f x - μ| ≤ 2 := by
      rw [abs_le]
      have hx := abs_le.mp (hf x)
      constructor <;> linarith
    have harg : |t * (f x - μ)| ≤ 1 := by
      rw [abs_mul]
      calc
        |t| * |f x - μ| ≤ (1 / 2 : ℝ) * 2 :=
          mul_le_mul ht hcenter (abs_nonneg _) (by norm_num)
        _ = 1 := by norm_num
    have hrem := Real.norm_exp_sub_one_sub_id_le (by simpa only [Real.norm_eq_abs] using harg)
    rw [Real.norm_eq_abs, Real.norm_eq_abs, sq_abs] at hrem
    have hu := (abs_le.mp hrem).2
    have hs : (f x - μ) ^ 2 ≤ 4 := by
      calc
        (f x - μ) ^ 2 = |f x - μ| ^ 2 := (sq_abs _).symm
        _ ≤ (2 : ℝ) ^ 2 := pow_le_pow_left₀ (abs_nonneg _) hcenter 2
        _ = 4 := by norm_num
    have hsq := mul_le_mul_of_nonneg_left hs (sq_nonneg t)
    nlinarith [show (t * (f x - μ)) ^ 2 = t ^ 2 * (f x - μ) ^ 2 by ring]
  calc
    finiteExpectation w (fun x => Real.exp (t * (f x - μ))) ≤
        finiteExpectation w (fun x => 1 + t * (f x - μ) + 4 * t ^ 2) :=
      expectation_mono w hw hpoint
    _ = 1 + 4 * t ^ 2 := by
      rw [finiteExpectation_add, finiteExpectation_add, expectation_const w hnorm,
        finiteExpectation_const_mul, expectation_sub, expectation_const w hnorm]
      rw [expectation_const w hnorm]
      change 1 + t * (μ - μ) + 4 * t ^ 2 = _
      ring
    _ ≤ Real.exp (4 * t ^ 2) := by linarith [Real.add_one_le_exp (4 * t ^ 2)]

end FiniteTools

section SamplingIdentities

variable {E X : Type*} [Fintype E] [Fintype X] [DecidableEq E]

-- Source: Er579.CubeGenerators:133
theorem product_normalization (w : E → X → ℝ) (hnorm : ∀ e, ∑ x, w e x = 1) :
    ∑ ω : E → X, productWeight w ω = 1 := by
  unfold productWeight
  rw [← Fintype.prod_sum]
  simp only [hnorm, Finset.prod_const_one]

-- Source: Er579.CubeGenerators:139
theorem bernoulli_normalization (r : ℝ) : ∑ ω : E → Bool, bernoulliWeight r ω = 1 := by
  unfold bernoulliWeight
  rw [← Fintype.prod_sum]
  simp only [bernoulliBitWeight_sum, Finset.prod_const_one]

-- Source: Er579.CubeGenerators:144
theorem product_event_identity (w : E → X → ℝ) (P : E → X → Prop) :
    eventWeight (productWeight w) (fun ω => ∀ e, P e (ω e)) =
      ∏ e, eventWeight (w e) (P e) := by
  unfold eventWeight productWeight
  have hpoint (ω : E → X) :
      (if ∀ e, P e (ω e) then ∏ e, w e (ω e) else 0) =
        ∏ e, if P e (ω e) then w e (ω e) else 0 := by
    by_cases h : ∀ e, P e (ω e)
    · simp only [if_pos h, if_pos (h _)]
    · rw [if_neg h]
      push Not at h
      obtain ⟨e, he⟩ := h
      symm
      exact Finset.prod_eq_zero (Finset.mem_univ e) (if_neg he)
  trans ∑ ω : E → X, ∏ e, if P e (ω e) then w e (ω e) else 0
  · apply Finset.sum_congr rfl
    intro ω _
    by_cases h : ∀ e, P e (ω e)
    · simpa only [if_pos h] using hpoint ω
    · simpa only [if_neg h] using hpoint ω
  · exact (Fintype.prod_sum (fun e x => if P e x then w e x else 0)).symm

-- Source: Er579.CubeGenerators:166
theorem bernoulli_forced_true (r : ℝ) (K : Finset E) :
    eventWeight (bernoulliWeight r) (fun ω : E → Bool => ∀ e ∈ K, ω e = true) = r ^ K.card := by
  let f : E → Bool → ℝ := fun e b =>
    if e ∈ K then if b = true then bernoulliBitWeight r b else 0 else bernoulliBitWeight r b
  have hpoint (ω : E → Bool) :
      (if ∀ e ∈ K, ω e = true then bernoulliWeight r ω else 0) =
        ∏ e, f e (ω e) := by
    by_cases h : ∀ e ∈ K, ω e = true
    · rw [if_pos h]
      unfold bernoulliWeight
      apply Finset.prod_congr rfl
      intro e _
      by_cases he : e ∈ K
      · simp only [f, if_pos he, if_pos (h e he)]
      · simp only [f, if_neg he]
    · rw [if_neg h]
      push Not at h
      obtain ⟨e, he, hne⟩ := h
      symm
      exact Finset.prod_eq_zero (Finset.mem_univ e) (by simp only [f, if_pos he, if_neg hne])
  unfold eventWeight
  trans ∑ ω : E → Bool, ∏ e, f e (ω e)
  · apply Finset.sum_congr rfl
    intro ω _
    by_cases h : ∀ e ∈ K, ω e = true
    · simpa only [if_pos h] using hpoint ω
    · simpa only [if_neg h] using hpoint ω
  rw [← Fintype.prod_sum]
  have hs (e : E) : (∑ b : Bool, f e b) = if e ∈ K then r else 1 := by
    by_cases he : e ∈ K <;> simp [he, f, bernoulliBitWeight]
  simp_rw [hs]
  simp only [Fintype.prod_ite_mem, Finset.prod_const]

-- Source: Er579.CubeGenerators:199
theorem product_expectation_coordinate (w : E → X → ℝ)
    (hnorm : ∀ e, ∑ x, w e x = 1) (i : E) (f : X → ℝ) :
    finiteExpectation (productWeight w) (fun ω => f (ω i)) =
      finiteExpectation (w i) f := by
  have hprod (ω : E → X) : f (ω i) =
      ∏ e, if e = i then f (ω e) else 1 := by
    simp only [Fintype.prod_ite_eq']
  simp_rw [hprod]
  rw [product_expectation w (fun e x => if e = i then f x else 1)]
  have hfactor (e : E) :
      finiteExpectation (w e) (fun x => if e = i then f x else 1) =
        if e = i then finiteExpectation (w e) f else 1 := by
    by_cases he : e = i
    · simp only [he, if_true]
    · simp only [if_neg he]
      exact expectation_const _ (hnorm e) 1
  simp_rw [hfactor]
  simp only [Fintype.prod_ite_eq']

-- Source: Er579.CubeGenerators:218
theorem product_event_coordinate (w : E → X → ℝ)
    (hnorm : ∀ e, ∑ x, w e x = 1) (i : E) (P : X → Prop) :
    eventWeight (productWeight w) (fun ω => P (ω i)) = eventWeight (w i) P := by
  rw [eventWeight_eq_expect_indicator, eventWeight_eq_expect_indicator]
  exact product_expectation_coordinate w hnorm i (fun x => if P x then 1 else 0)

-- Source: Er579.CubeGenerators:224
theorem bernoulli_sign_product (r : ℝ) (S : Finset E) :
    finiteExpectation (bernoulliWeight r) (fun x => ∏ i ∈ S, boolToSign (x i)) =
      (1 - 2 * r) ^ S.card := by
  have hp (x : E → Bool) : (∏ i ∈ S, boolToSign (x i)) =
      ∏ i, if i ∈ S then boolToSign (x i) else 1 := by
    simp only [Fintype.prod_ite_mem]
  simp_rw [hp]
  change finiteExpectation (productWeight (fun _ : E => bernoulliBitWeight r))
    (fun x => ∏ i, if i ∈ S then boolToSign (x i) else 1) = _
  rw [product_expectation (fun _ : E => bernoulliBitWeight r)
    (fun i b => if i ∈ S then boolToSign b else 1)]
  have hs (i : E) :
      finiteExpectation (bernoulliBitWeight r)
        (fun b => if i ∈ S then boolToSign b else 1) =
          if i ∈ S then 1 - 2 * r else 1 := by
    by_cases hi : i ∈ S
    · simp [finiteExpectation, bernoulliBitWeight, boolToSign, hi]
      ring
    · simp [finiteExpectation, bernoulliBitWeight, hi]
  simp_rw [hs]
  simp only [Fintype.prod_ite_mem, Finset.prod_const]

-- Source: Er579.CubeGenerators:246
theorem bernoulli_character_mean {n : ℕ} (r : ℝ) (S : Finset (Fin n)) :
    finiteExpectation (bernoulliWeight r) (fun x : BoolCube n => chiS S (xor (one n) x)) =
      chiS S (one n) * (1 - 2 * r) ^ S.card := by
  simp_rw [chi_xor]
  rw [finiteExpectation_const_mul]
  exact congrArg (fun z => chiS S (one n) * z) (bernoulli_sign_product r S)

-- Source: Er579.CubeGenerators:253
theorem expectation_exp_indicator (w : X → ℝ) (hnorm : ∑ x, w x = 1)
    (P : X → Prop) [DecidablePred P] (t : ℝ) :
    finiteExpectation w (fun x => Real.exp (t * (if P x then 1 else 0))) =
      1 + (Real.exp t - 1) * eventWeight w P := by
  calc
    _ = (∑ x, w x) + (Real.exp t - 1) * eventWeight w P := by
      unfold finiteExpectation eventWeight
      rw [Finset.mul_sum, ← Finset.sum_add_distrib]
      apply Finset.sum_congr rfl
      intro x _
      by_cases hx : P x <;> simp only [if_pos, if_neg, hx, mul_one, mul_zero, Real.exp_zero]
      · ring
      · simp
    _ = _ := by rw [hnorm]

-- Source: Er579.CubeGenerators:268
noncomputable def bitSupport (x : E → Bool) : Finset E :=
  Finset.univ.filter (fun i => x i = true)

-- Source: Er579.CubeGenerators:271
theorem mem_bitSupport (x : E → Bool) (i : E) : i ∈ bitSupport x ↔ x i = true := by
  simp only [bitSupport, Finset.mem_filter, Finset.mem_univ, true_and]

-- Source: Er579.CubeGenerators:274
theorem support_card_eq_sum (x : E → Bool) :
    ((bitSupport x).card : ℝ) = ∑ i, if x i = true then (1 : ℝ) else 0 := by
  exact Finset.natCast_card_filter _ _

-- Source: Er579.CubeGenerators:278
theorem bernoulli_card_mgf (r t : ℝ) :
    finiteExpectation (bernoulliWeight r)
      (fun x : E → Bool => Real.exp (t * (bitSupport x).card)) =
        (1 + r * (Real.exp t - 1)) ^ Fintype.card E := by
  simp_rw [support_card_eq_sum]
  change finiteExpectation (productWeight (fun _ : E => bernoulliBitWeight r))
    (fun x => Real.exp (t * ∑ i, if x i = true then (1 : ℝ) else 0)) = _
  rw [product_exp_sum (fun _ : E => bernoulliBitWeight r)
    (fun _ b => if b = true then (1 : ℝ) else 0) t]
  have hs : finiteExpectation (bernoulliBitWeight r)
      (fun b => Real.exp (t * (if b = true then 1 else 0))) = 1 + r * (Real.exp t - 1) := by
    simp [finiteExpectation, bernoulliBitWeight]
    ring
  simp only [hs, Finset.prod_const, Finset.card_univ]

-- Source: Er579.CubeGenerators:293
theorem bernoulli_card_mgf_le {r : ℝ} (hr0 : 0 ≤ r) (hr1 : r ≤ 1) (t : ℝ) :
    finiteExpectation (bernoulliWeight r)
      (fun x : E → Bool => Real.exp (t * (bitSupport x).card)) ≤
        Real.exp ((Fintype.card E : ℝ) * r * (Real.exp t - 1)) := by
  rw [bernoulli_card_mgf]
  have hbase : 0 ≤ 1 + r * (Real.exp t - 1) := by
    nlinarith [mul_nonneg hr0 (Real.exp_pos t).le]
  calc
    (1 + r * (Real.exp t - 1)) ^ Fintype.card E ≤
        (Real.exp (r * (Real.exp t - 1))) ^ Fintype.card E := by
      apply pow_le_pow_left₀ hbase
      linarith [Real.add_one_le_exp (r * (Real.exp t - 1))]
    _ = Real.exp ((Fintype.card E : ℝ) * r * (Real.exp t - 1)) := by
      rw [← Real.exp_nat_mul]
      congr 1
      ring

end SamplingIdentities

section Concentration

variable {X : Type*} [Fintype X]

-- Source: Er579.CubeGenerators:316
theorem iid_centered_sum_tail (w : X → ℝ) (hw : ∀ x, 0 ≤ w x)
    (hnorm : ∑ x, w x = 1) (f : X → ℝ) (hf : ∀ x, |f x| ≤ 1)
    (d : ℕ) (ε : ℝ) (hε0 : 0 ≤ ε) (hε1 : ε ≤ 1) :
    eventWeight (productWeight (fun _ : Fin d => w))
      (fun ω => (d : ℝ) * ε ≤ ∑ i, (f (ω i) - finiteExpectation w f)) ≤
        Real.exp (-(d : ℝ) * ε ^ 2 / 16) := by
  have ht : |ε / 8| ≤ 1 / 2 := by
    rw [abs_of_nonneg (by positivity)]
    linarith
  have hmgf := product_mgf_bound (fun _ : Fin d => w) (fun _ x => hw x)
    (fun _ x => f x - finiteExpectation w f) (ε / 8)
    (fun _ => 4 * (ε / 8) ^ 2)
    (fun _ => centered_mgf_bound w hw hnorm f hf (ε / 8) ht)
  have hb : (∑ _ : Fin d, (4 * (ε / 8) ^ 2 : ℝ)) = (d : ℝ) * 4 * (ε / 8) ^ 2 := by
    simp only [Finset.sum_const, Finset.card_univ, Fintype.card_fin, nsmul_eq_mul]
    ring
  rw [hb] at hmgf
  have h := finite_chernoff (productWeight (fun _ : Fin d => w))
    (productWeight_nonneg _ (fun _ x => hw x))
    (fun ω => ∑ i, (f (ω i) - finiteExpectation w f)) ((d : ℝ) * ε)
    (ε / 8) ((d : ℝ) * 4 * (ε / 8) ^ 2) (by positivity) hmgf
  convert h using 1
  congr 1
  ring

-- Source: Er579.CubeGenerators:341
theorem iid_average_concentration (w : X → ℝ) (hw : ∀ x, 0 ≤ w x)
    (hnorm : ∑ x, w x = 1) (f : X → ℝ) (hf : ∀ x, |f x| ≤ 1)
    {d : ℕ} (hd : 0 < d) (ε : ℝ) (hε0 : 0 ≤ ε) (hε1 : ε ≤ 1) :
    eventWeight (productWeight (fun _ : Fin d => w))
      (fun ω => ε ≤ |(∑ i, f (ω i)) / d - finiteExpectation w f|) ≤
        2 * Real.exp (-(d : ℝ) * ε ^ 2 / 16) := by
  have hdR : (0 : ℝ) < d := by exact_mod_cast hd
  let upper : (Fin d → X) → Prop :=
    fun ω => (d : ℝ) * ε ≤ ∑ i, (f (ω i) - finiteExpectation w f)
  let lower : (Fin d → X) → Prop :=
    fun ω => (d : ℝ) * ε ≤ ∑ i, (-f (ω i) - finiteExpectation w (fun x => -f x))
  have hcontained : ∀ ω : Fin d → X,
      ε ≤ |(∑ i, f (ω i)) / d - finiteExpectation w f| → upper ω ∨ lower ω := by
    intro ω hω
    have hu : (∑ i, (f (ω i) - finiteExpectation w f)) =
        (d : ℝ) * ((∑ i, f (ω i)) / d - finiteExpectation w f) := by
      rw [Finset.sum_sub_distrib]
      simp only [Finset.sum_const, Finset.card_univ, Fintype.card_fin, nsmul_eq_mul]
      field_simp
    have hl : (∑ i, (-f (ω i) - finiteExpectation w (fun x => -f x))) =
        -(∑ i, (f (ω i) - finiteExpectation w f)) := by
      rw [expectation_neg]
      simp_rw [show ∀ z : ℝ, -z - -finiteExpectation w f =
        -(z - finiteExpectation w f) by intro z; ring]
      simp only [Finset.sum_neg_distrib]
    by_cases hz : 0 ≤ (∑ i, f (ω i)) / d - finiteExpectation w f
    · left
      change (d : ℝ) * ε ≤ _
      rw [hu]
      rw [abs_of_nonneg hz] at hω
      exact mul_le_mul_of_nonneg_left hω hdR.le
    · right
      change (d : ℝ) * ε ≤ _
      rw [hl, hu]
      rw [abs_of_neg (lt_of_not_ge hz)] at hω
      nlinarith
  have hupper := iid_centered_sum_tail w hw hnorm f hf d ε hε0 hε1
  have hlower := iid_centered_sum_tail w hw hnorm (fun x => -f x)
    (fun x => by simpa only [abs_neg] using hf x) d ε hε0 hε1
  calc
    eventWeight (productWeight (fun _ : Fin d => w))
        (fun ω => ε ≤ |(∑ i, f (ω i)) / d - finiteExpectation w f|) ≤
      eventWeight (productWeight (fun _ : Fin d => w)) (fun ω => upper ω ∨ lower ω) :=
        eventWeight_mono _ (productWeight_nonneg _ (fun _ x => hw x)) hcontained
    _ ≤ eventWeight (productWeight (fun _ : Fin d => w)) upper +
        eventWeight (productWeight (fun _ : Fin d => w)) lower :=
      eventWeight_or_le _ (productWeight_nonneg _ (fun _ x => hw x)) upper lower
    _ ≤ 2 * Real.exp (-(d : ℝ) * ε ^ 2 / 16) := by linarith

-- Source: Er579.CubeGenerators:390
theorem theta_range {k : ℕ} (hk : 3 ≤ k) : 0 ≤ theta k ∧ theta k ≤ 1 / 9 := by
  have hx : (3 : ℝ) ≤ k := by exact_mod_cast hk
  unfold theta
  constructor
  · positivity
  · apply (div_le_iff₀ (show (0 : ℝ) < (k : ℝ) ^ 2 by positivity)).2
    nlinarith

-- Source: Er579.CubeGenerators:398
theorem dimension_theta {k : ℕ} (hk : 0 < k) :
    (dimension k : ℝ) * theta k = (k : ℝ) ^ 4 := by
  have hne : (k : ℝ) ≠ 0 := by exact_mod_cast hk.ne'
  unfold dimension theta
  push_cast
  field_simp

-- Source: Er579.CubeGenerators:405
private theorem exp_one_le_three : Real.exp (1 : ℝ) ≤ 3 := by
  have h := Real.abs_exp_sub_one_sub_id_le (show |(1 : ℝ)| ≤ 1 by norm_num)
  have hu := (abs_le.mp h).2
  norm_num at hu
  linarith

-- Source: Er579.CubeGenerators:411
private theorem exp_neg_one_le_half : Real.exp (-1 : ℝ) ≤ 1 / 2 := by
  rw [Real.exp_neg, inv_eq_one_div]
  apply (div_le_iff₀ (Real.exp_pos (1 : ℝ))).2
  linarith [Real.add_one_le_exp (1 : ℝ)]

-- Source: Er579.CubeGenerators:416
theorem sampled_support_size_bound {k : ℕ} (hk : 3 ≤ k) :
    eventWeight (bernoulliWeight (theta k))
      (fun x : BoolCube (dimension k) =>
        ((bitSupport x).card : ℝ) < (k : ℝ) ^ 4 / 4 ∨
          4 * (k : ℝ) ^ 4 < (bitSupport x).card) ≤
      2 * Real.exp (-(k : ℝ) ^ 4 / 4) := by
  have hr := theta_range hk
  have hr1 : theta k ≤ 1 := by linarith [hr.2]
  have hw := bernoulliWeight_nonneg hr.1 hr1 (E := Fin (dimension k))
  let μ : ℝ := (k : ℝ) ^ 4
  have hμ : 0 ≤ μ := by positivity
  have hmean := dimension_theta (show 0 < k by omega)
  have hmgfU := bernoulli_card_mgf_le (E := Fin (dimension k)) hr.1 hr1 (1 : ℝ)
  have hmgfL := bernoulli_card_mgf_le (E := Fin (dimension k)) hr.1 hr1 (-1 : ℝ)
  simp only [Fintype.card_fin, hmean, one_mul, neg_one_mul] at hmgfU hmgfL
  have hupper := finite_chernoff (bernoulliWeight (theta k)) hw
    (fun x : BoolCube (dimension k) => ((bitSupport x).card : ℝ)) (4 * μ) 1
    (μ * (Real.exp 1 - 1)) (by norm_num) (by simpa only [one_mul, μ] using hmgfU)
  have hlower := finite_chernoff (bernoulliWeight (theta k)) hw
    (fun x : BoolCube (dimension k) => -((bitSupport x).card : ℝ)) (-μ / 4) 1
    (μ * (Real.exp (-1) - 1)) (by norm_num) (by simpa only [one_mul, μ] using hmgfL)
  have hUB : eventWeight (bernoulliWeight (theta k))
      (fun x : BoolCube (dimension k) => 4 * μ ≤ (bitSupport x).card) ≤ Real.exp (-μ / 4) := by
    refine hupper.trans (Real.exp_le_exp.mpr ?_)
    nlinarith [exp_one_le_three]
  have hLB : eventWeight (bernoulliWeight (theta k))
      (fun x : BoolCube (dimension k) => ((bitSupport x).card : ℝ) ≤ μ / 4) ≤ Real.exp (-μ / 4) := by
    have hevent : (fun x : BoolCube (dimension k) => ((bitSupport x).card : ℝ) ≤ μ / 4) =
        (fun x => -μ / 4 ≤ -((bitSupport x).card : ℝ)) := by
      funext x
      apply propext
      constructor <;> intro h <;> linarith
    rw [hevent]
    refine hlower.trans (Real.exp_le_exp.mpr ?_)
    nlinarith [exp_neg_one_le_half]
  have hmono : eventWeight (bernoulliWeight (theta k))
      (fun x : BoolCube (dimension k) =>
        ((bitSupport x).card : ℝ) < μ / 4 ∨ 4 * μ < (bitSupport x).card) ≤
      eventWeight (bernoulliWeight (theta k))
        (fun x : BoolCube (dimension k) =>
          ((bitSupport x).card : ℝ) ≤ μ / 4 ∨ 4 * μ ≤ (bitSupport x).card) := by
    apply eventWeight_mono _ hw
    intro x hx
    exact hx.elim (fun h => Or.inl h.le) (fun h => Or.inr h.le)
  have hor := eventWeight_or_le (bernoulliWeight (theta k)) hw
    (fun x : BoolCube (dimension k) => ((bitSupport x).card : ℝ) ≤ μ / 4)
    (fun x : BoolCube (dimension k) => 4 * μ ≤ (bitSupport x).card)
  change _ ≤ 2 * Real.exp (-μ / 4)
  linarith

end Concentration

section ArraySampling

variable {E F : Type*} [Fintype E] [Fintype F] [DecidableEq E] [DecidableEq F]

-- Source: Er579.CubeGenerators:472
def transposeEquiv : (E → F → Bool) ≃ (F → E → Bool) where
  toFun ω j i := ω i j
  invFun ω i j := ω j i
  left_inv _ := rfl
  right_inv _ := rfl

-- Source: Er579.CubeGenerators:478
theorem array_weight_transpose (r : ℝ) (ω : E → F → Bool) :
    productWeight (fun _ : E => bernoulliWeight r) ω =
      productWeight (fun _ : F => bernoulliWeight r) (transposeEquiv ω) := by
  unfold productWeight bernoulliWeight
  exact Finset.prod_comm

-- Source: Er579.CubeGenerators:484
theorem array_event_transpose (r : ℝ) (P : (E → F → Bool) → Prop) :
    eventWeight (productWeight (fun _ : E => bernoulliWeight r)) P =
      eventWeight (productWeight (fun _ : F => bernoulliWeight r))
        (fun ω => P (transposeEquiv.symm ω)) := by
  unfold eventWeight
  apply Fintype.sum_equiv transposeEquiv
  intro ω
  simp only [Equiv.symm_apply_apply]
  by_cases h : P ω
  · simp only [if_pos h]
    exact array_weight_transpose r ω
  · simp only [if_neg h]

-- Source: Er579.CubeGenerators:497
theorem array_expectation_transpose (r : ℝ) (f : (E → F → Bool) → ℝ) :
    finiteExpectation (productWeight (fun _ : E => bernoulliWeight r)) f =
      finiteExpectation (productWeight (fun _ : F => bernoulliWeight r))
        (fun ω => f (transposeEquiv.symm ω)) := by
  unfold finiteExpectation
  apply Fintype.sum_equiv transposeEquiv
  intro ω
  simp only [Equiv.symm_apply_apply]
  rw [array_weight_transpose]

-- Source: Er579.CubeGenerators:507
theorem bernoulli_two_bits (r : ℝ) (i j : E) (hij : i ≠ j) :
    eventWeight (bernoulliWeight r) (fun x : E → Bool => x i = true ∧ x j = true) = r ^ 2 := by
  have hevent : (fun x : E → Bool => x i = true ∧ x j = true) =
      (fun x => ∀ e ∈ ({i, j} : Finset E), x e = true) := by
    funext x
    simp only [Finset.mem_insert, Finset.mem_singleton, forall_eq_or_imp, forall_eq]
  rw [hevent]
  rw [bernoulli_forced_true]
  simp [hij]

-- Source: Er579.CubeGenerators:517
theorem bernoulli_two_bits_mgf_le {r : ℝ} (hr0 : 0 ≤ r) (hr1 : r ≤ 1)
    (i j : E) (hij : i ≠ j) (t : ℝ) :
    finiteExpectation (bernoulliWeight r)
      (fun x : E → Bool => Real.exp (t * (if x i = true ∧ x j = true then 1 else 0))) ≤
        Real.exp ((Real.exp t - 1) * r ^ 2) := by
  rw [expectation_exp_indicator (bernoulliWeight r) (bernoulli_normalization r)
    (fun x : E → Bool => x i = true ∧ x j = true) t,
    bernoulli_two_bits r i j hij]
  linarith [Real.add_one_le_exp ((Real.exp t - 1) * r ^ 2)]

-- Source: Er579.CubeGenerators:527
theorem array_intersection_mgf_le {r : ℝ} (hr0 : 0 ≤ r) (hr1 : r ≤ 1)
    (i j : E) (hij : i ≠ j) (t : ℝ) :
    finiteExpectation (productWeight (fun _ : E => bernoulliWeight r))
      (fun ω : E → F → Bool => Real.exp (t * ((bitSupport (ω i) ∩ bitSupport (ω j)).card : ℝ))) ≤
        Real.exp ((Fintype.card F : ℝ) * (Real.exp t - 1) * r ^ 2) := by
  have hcount (ω : F → E → Bool) :
      ((bitSupport (transposeEquiv.symm ω i) ∩ bitSupport (transposeEquiv.symm ω j)).card : ℝ) =
        ∑ a : F, if ω a i = true ∧ ω a j = true then (1 : ℝ) else 0 := by
    have hset : bitSupport (transposeEquiv.symm ω i) ∩ bitSupport (transposeEquiv.symm ω j) =
        Finset.univ.filter (fun a => ω a i = true ∧ ω a j = true) := by
      ext a
      rw [Finset.mem_inter]
      simp only [mem_bitSupport, Finset.mem_filter, Finset.mem_univ, true_and]
      rfl
    rw [hset]
    exact Finset.natCast_card_filter _ _
  rw [array_expectation_transpose]
  simp_rw [hcount]
  have h := product_mgf_bound (fun _ : F => bernoulliWeight r)
    (fun _ x => bernoulliWeight_nonneg hr0 hr1 x)
    (fun (_ : F) (x : E → Bool) => if x i = true ∧ x j = true then (1 : ℝ) else 0) t
    (fun _ => (Real.exp t - 1) * r ^ 2)
    (fun _ => bernoulli_two_bits_mgf_le hr0 hr1 i j hij t)
  convert h using 1
  simp only [Finset.sum_const, Finset.card_univ, nsmul_eq_mul]
  ring

-- Source: Er579.CubeGenerators:554
theorem sign_product_square (S : Finset E) (x : E → Bool) :
    (∏ i ∈ S, boolToSign (x i)) ^ 2 = 1 := by
  rw [← Finset.prod_pow]
  simp only [boolToSign_sq, Finset.prod_const_one]

-- Source: Er579.CubeGenerators:559
theorem sign_product_positive_weight (r : ℝ) (S : Finset E) :
    eventWeight (bernoulliWeight r)
      (fun x : E → Bool => (∏ i ∈ S, boolToSign (x i)) = 1) =
        (1 + (1 - 2 * r) ^ S.card) / 2 := by
  have hp (x : E → Bool) :
      (if (∏ i ∈ S, boolToSign (x i)) = 1 then (1 : ℝ) else 0) =
        (1 + (∏ i ∈ S, boolToSign (x i))) / 2 := by
    rcases (sq_eq_one_iff).mp (sign_product_square S x) with h | h
    · simp only [h, if_true]
      norm_num
    · simp only [h]
      norm_num
  rw [eventWeight_eq_expect_indicator]
  simp_rw [hp]
  have hexp : finiteExpectation (bernoulliWeight r)
      (fun x : E → Bool => (1 + (∏ i ∈ S, boolToSign (x i))) / 2) =
        (1 + finiteExpectation (bernoulliWeight r) (fun x : E → Bool =>
          ∏ i ∈ S, boolToSign (x i))) / 2 := by
    unfold finiteExpectation
    have hpoint (x : E → Bool) : bernoulliWeight r x *
        ((1 + (∏ i ∈ S, boolToSign (x i))) / 2) =
          (bernoulliWeight r x + bernoulliWeight r x * (∏ i ∈ S, boolToSign (x i))) / 2 := by ring
    simp_rw [hpoint]
    rw [← Finset.sum_div, Finset.sum_add_distrib, bernoulli_normalization]
  rw [hexp, bernoulli_sign_product]

-- Source: Er579.CubeGenerators:585
theorem four_parity_weight (r : ℝ) (i j l q : E)
    (hij : i ≠ j) (hil : i ≠ l) (hiq : i ≠ q)
    (hjl : j ≠ l) (hjq : j ≠ q) (hlq : l ≠ q) :
    eventWeight (bernoulliWeight r) (fun x : E → Bool =>
      Bool.xor (Bool.xor (x i) (x j)) (Bool.xor (x l) (x q)) = false) =
        (1 + (1 - 2 * r) ^ 4) / 2 := by
  let S : Finset E := {i, j, l, q}
  have hS : S.card = 4 := by simp [S, hij, hil, hiq, hjl, hjq, hlq]
  have hprod (x : E → Bool) : (∏ a ∈ S, boolToSign (x a)) =
      boolToSign (x i) * (boolToSign (x j) * (boolToSign (x l) * boolToSign (x q))) := by
    simp [S, hij, hil, hiq, hjl, hjq, hlq]
  have hevent : (fun x : E → Bool =>
      Bool.xor (Bool.xor (x i) (x j)) (Bool.xor (x l) (x q)) = false) =
        (fun x => (∏ a ∈ S, boolToSign (x a)) = 1) := by
    funext x
    rw [hprod]
    cases x i <;> cases x j <;> cases x l <;> cases x q <;>
      norm_num [boolToSign, Bool.xor]
  rw [hevent, sign_product_positive_weight, hS]

-- Source: Er579.CubeGenerators:605
theorem four_parity_weight_le {r : ℝ} (hr0 : 0 ≤ r) (hr1 : r ≤ 1 / 9)
    (i j l q : E) (hij : i ≠ j) (hil : i ≠ l) (hiq : i ≠ q)
    (hjl : j ≠ l) (hjq : j ≠ q) (hlq : l ≠ q) :
    eventWeight (bernoulliWeight r) (fun x : E → Bool =>
      Bool.xor (Bool.xor (x i) (x j)) (Bool.xor (x l) (x q)) = false) ≤
        Real.exp (-2 * r) := by
  rw [four_parity_weight r i j l q hij hil hiq hjl hjq hlq]
  have hr2 : r ^ 2 ≤ r / 9 := by nlinarith [mul_nonneg hr0 (sub_nonneg.mpr hr1)]
  have hr3 : 0 ≤ r ^ 3 := by positivity
  have hr4 : r ^ 4 ≤ r ^ 3 := by
    have h := mul_nonneg hr3 (show 0 ≤ 1 - r by linarith)
    nlinarith [show r ^ 4 = r ^ 3 * r by ring]
  calc
    (1 + (1 - 2 * r) ^ 4) / 2 ≤ 1 - 2 * r := by nlinarith
    _ ≤ Real.exp (-2 * r) := by linarith [Real.add_one_le_exp (-2 * r)]

-- Source: Er579.CubeGenerators:621
theorem array_four_zero_bound {r : ℝ} (hr0 : 0 ≤ r) (hr1 : r ≤ 1 / 9)
    (i j l q : E) (hij : i ≠ j) (hil : i ≠ l) (hiq : i ≠ q)
    (hjl : j ≠ l) (hjq : j ≠ q) (hlq : l ≠ q) :
    eventWeight (productWeight (fun _ : E => bernoulliWeight r))
      (fun ω : E → F → Bool => ∀ a : F,
        Bool.xor (Bool.xor (ω i a) (ω j a)) (Bool.xor (ω l a) (ω q a)) = false) ≤
          Real.exp (-2 * r * Fintype.card F) := by
  rw [array_event_transpose]
  change eventWeight (productWeight (fun _ : F => bernoulliWeight r))
    (fun ω => ∀ a : F,
      Bool.xor (Bool.xor (ω a i) (ω a j)) (Bool.xor (ω a l) (ω a q)) = false) ≤ _
  rw [product_event_identity (fun _ : F => bernoulliWeight r)
    (fun (_ : F) (x : E → Bool) =>
      Bool.xor (Bool.xor (x i) (x j)) (Bool.xor (x l) (x q)) = false)]
  simp only [Finset.prod_const, Finset.card_univ]
  have hbase := four_parity_weight_le hr0 hr1 i j l q hij hil hiq hjl hjq hlq
  calc
    eventWeight (bernoulliWeight r) (fun x : E → Bool =>
        Bool.xor (Bool.xor (x i) (x j)) (Bool.xor (x l) (x q)) = false) ^ Fintype.card F ≤
      (Real.exp (-2 * r)) ^ Fintype.card F := by
        apply pow_le_pow_left₀ _ hbase
        exact eventWeight_nonneg _ (bernoulliWeight_nonneg hr0 (by linarith)) _
    _ = Real.exp (-2 * r * Fintype.card F) := by
      rw [← Real.exp_nat_mul]
      congr 1
      ring

end ArraySampling

-- Source: Er579.CubeGenerators:650
abbrev Sample (k : ℕ) := Fin (degree k) → BoolCube (dimension k)

-- Source: Er579.CubeGenerators:652
noncomputable def sampleWeight (k : ℕ) : Sample k → ℝ :=
  productWeight (fun _ => bernoulliWeight (theta k))

-- Source: Er579.CubeGenerators:655
def sampleDirections {k : ℕ} (ω : Sample k) : Fin (degree k) → BoolCube (dimension k) :=
  fun i => xor (one (dimension k)) (ω i)

-- Source: Er579.CubeGenerators:658
def BadSize (k : ℕ) (ω : Sample k) : Prop :=
  ∃ i, ((bitSupport (ω i)).card : ℝ) < (k : ℝ) ^ 4 / 4 ∨
    4 * (k : ℝ) ^ 4 < (bitSupport (ω i)).card

-- Source: Er579.CubeGenerators:662
def BadIntersection (k : ℕ) (ω : Sample k) : Prop :=
  ∃ p : Fin (degree k) × Fin (degree k), p.1 ≠ p.2 ∧
    (k : ℝ) ^ 3 ≤ (bitSupport (ω p.1) ∩ bitSupport (ω p.2)).card

-- Source: Er579.CubeGenerators:666
def FourDistinct {E : Type*} (i j l q : E) : Prop :=
  i ≠ j ∧ i ≠ l ∧ i ≠ q ∧ j ≠ l ∧ j ≠ q ∧ l ≠ q

-- Source: Er579.CubeGenerators:669
def BadFour (k : ℕ) (ω : Sample k) : Prop :=
  ∃ t : (Fin (degree k) × Fin (degree k)) × (Fin (degree k) × Fin (degree k)),
    FourDistinct t.1.1 t.1.2 t.2.1 t.2.2 ∧
      ∀ a, Bool.xor (Bool.xor (ω t.1.1 a) (ω t.1.2 a))
        (Bool.xor (ω t.2.1 a) (ω t.2.2 a)) = false

-- Source: Er579.CubeGenerators:675
def BadSpectral (k : ℕ) (ω : Sample k) : Prop :=
  ∃ S : Finset (Fin (dimension k)), accuracy k <
    |eigenvalue (sampleDirections ω) S - chiS S (one (dimension k)) * (1 - 2 * theta k) ^ S.card|

-- Source: Er579.CubeGenerators:679
def BadTuple (k : ℕ) (ω : Sample k) : Prop :=
  BadSize k ω ∨ BadIntersection k ω ∨ BadFour k ω ∨ BadSpectral k ω

-- Source: Er579.CubeGenerators:682
def GoodTuple (k : ℕ) (T : Fin (degree k) → Finset (Fin (dimension k))) : Prop :=
  (∀ i, (k : ℝ) ^ 4 / 4 ≤ (T i).card) ∧
  (∀ i, ((T i).card : ℝ) ≤ 4 * (k : ℝ) ^ 4) ∧
  (∀ i j, i ≠ j → ((T i ∩ T j).card : ℝ) < (k : ℝ) ^ 3) ∧
  Er579.CubeGeometry.FourIndependent (fun i => Er579.CubeGeometry.nearAntipode (T i)) ∧
  ∀ S : Finset (Fin (dimension k)),
    |eigenvalue (fun i => Er579.CubeGeometry.nearAntipode (T i)) S -
      chiS S (one (dimension k)) * (1 - 2 * theta k) ^ S.card| ≤ accuracy k

-- Source: Er579.CubeGenerators:691
theorem sampleWeight_normalized (k : ℕ) : ∑ ω, sampleWeight k ω = 1 := by
  exact product_normalization _ (fun _ => bernoulli_normalization (theta k))

-- Source: Er579.CubeGenerators:694
theorem sampleWeight_nonnegative {k : ℕ} (hk : 3 ≤ k) (ω : Sample k) : 0 ≤ sampleWeight k ω := by
  have hr := theta_range hk
  exact productWeight_nonneg _ (fun _ x => bernoulliWeight_nonneg hr.1 (by linarith [hr.2]) x) ω

-- Source: Er579.CubeGenerators:698
theorem sample_badSize_le {k : ℕ} (hk : 3 ≤ k) :
    eventWeight (sampleWeight k) (BadSize k) ≤ sizeBound k := by
  have hw := sampleWeight_nonnegative hk
  have hsingle (i : Fin (degree k)) :
      eventWeight (sampleWeight k) (fun ω =>
        ((bitSupport (ω i)).card : ℝ) < (k : ℝ) ^ 4 / 4 ∨
          4 * (k : ℝ) ^ 4 < (bitSupport (ω i)).card) ≤
        2 * Real.exp (-(k : ℝ) ^ 4 / 4) := by
    change eventWeight (productWeight (fun _ : Fin (degree k) => bernoulliWeight (theta k))) _ ≤ _
    rw [product_event_coordinate (fun _ : Fin (degree k) => bernoulliWeight (theta k))
      (fun _ => bernoulli_normalization (theta k)) i
      (fun x : BoolCube (dimension k) => ((bitSupport x).card : ℝ) < (k : ℝ) ^ 4 / 4 ∨
        4 * (k : ℝ) ^ 4 < (bitSupport x).card)]
    exact sampled_support_size_bound hk
  have hu := eventWeight_exists_le_sum (sampleWeight k) hw
    (fun i ω => ((bitSupport (ω i)).card : ℝ) < (k : ℝ) ^ 4 / 4 ∨
      4 * (k : ℝ) ^ 4 < (bitSupport (ω i)).card)
  have hs := Finset.sum_le_sum (fun i (_ : i ∈ Finset.univ) => hsingle i)
  have hc : (∑ _ : Fin (degree k), (2 * Real.exp (-(k : ℝ) ^ 4 / 4))) =
      (degree k : ℝ) * (2 * Real.exp (-(k : ℝ) ^ 4 / 4)) := by
    simp only [Finset.sum_const, Finset.card_univ, Fintype.card_fin, nsmul_eq_mul]
  have hsum : eventWeight (sampleWeight k) (BadSize k) ≤
      (degree k : ℝ) * (2 * Real.exp (-(k : ℝ) ^ 4 / 4)) := by
    exact hu.trans (hc ▸ hs)
  calc
    eventWeight (sampleWeight k) (BadSize k) ≤
        (degree k : ℝ) * (2 * Real.exp (-(k : ℝ) ^ 4 / 4)) := hsum
    _ ≤ Real.exp (4 * (k : ℝ) ^ 3) * (2 * Real.exp (-(k : ℝ) ^ 4 / 4)) :=
      mul_le_mul_of_nonneg_right (degree_le_exp k) (by positivity)
    _ = sizeBound k := by
      unfold sizeBound
      rw [mul_left_comm, ← Real.exp_add]
      congr 2
      ring

-- Source: Er579.CubeGenerators:733
theorem dimension_theta_sq {k : ℕ} (hk : 0 < k) :
    (dimension k : ℝ) * theta k ^ 2 = (k : ℝ) ^ 2 := by
  have hne : (k : ℝ) ≠ 0 := by exact_mod_cast hk.ne'
  unfold dimension theta
  push_cast
  field_simp

-- Source: Er579.CubeGenerators:740
theorem sampled_intersection_bound {k : ℕ} (hk : 3 ≤ k)
    (i j : Fin (degree k)) (hij : i ≠ j) :
    eventWeight (sampleWeight k)
      (fun ω => (k : ℝ) ^ 3 ≤ (bitSupport (ω i) ∩ bitSupport (ω j)).card) ≤
      Real.exp ((Real.exp 16 - 1) * (k : ℝ) ^ 2 - 16 * (k : ℝ) ^ 3) := by
  have hr := theta_range hk
  have hmgf := array_intersection_mgf_le (F := Fin (dimension k)) hr.1
    (show theta k ≤ 1 by linarith [hr.2]) i j hij (16 : ℝ)
  have hmean := dimension_theta_sq (show 0 < k by omega)
  have hexp : (dimension k : ℝ) * (Real.exp 16 - 1) * theta k ^ 2 =
      (Real.exp 16 - 1) * (k : ℝ) ^ 2 := by
    calc
      _ = (Real.exp 16 - 1) * ((dimension k : ℝ) * theta k ^ 2) := by ring
      _ = _ := by rw [hmean]
  simp only [Fintype.card_fin, hexp] at hmgf
  exact finite_chernoff (sampleWeight k) (sampleWeight_nonnegative hk)
    (fun ω => ((bitSupport (ω i) ∩ bitSupport (ω j)).card : ℝ)) ((k : ℝ) ^ 3) 16
    ((Real.exp 16 - 1) * (k : ℝ) ^ 2) (by norm_num) hmgf

-- Source: Er579.CubeGenerators:759
theorem sample_badIntersection_le {k : ℕ} (hk : 3 ≤ k) :
    eventWeight (sampleWeight k) (BadIntersection k) ≤ intersectionBound k := by
  let B : ℝ := Real.exp ((Real.exp 16 - 1) * (k : ℝ) ^ 2 - 16 * (k : ℝ) ^ 3)
  have hsingle (p : Fin (degree k) × Fin (degree k)) :
      eventWeight (sampleWeight k) (fun ω => p.1 ≠ p.2 ∧
        (k : ℝ) ^ 3 ≤ (bitSupport (ω p.1) ∩ bitSupport (ω p.2)).card) ≤ B := by
    by_cases hp : p.1 = p.2
    · simp only [hp, ne_eq, not_true_eq_false, false_and, eventWeight, if_false,
        Finset.sum_const_zero]
      exact (Real.exp_pos _).le
    · exact (eventWeight_mono _ (sampleWeight_nonnegative hk) (fun _ h => h.2)).trans
        (sampled_intersection_bound hk p.1 p.2 hp)
  have hu := eventWeight_exists_le_sum (sampleWeight k) (sampleWeight_nonnegative hk)
    (fun (p : Fin (degree k) × Fin (degree k)) ω => p.1 ≠ p.2 ∧
      (k : ℝ) ^ 3 ≤ (bitSupport (ω p.1) ∩ bitSupport (ω p.2)).card)
  have hs := Finset.sum_le_sum (fun p (_ : p ∈ Finset.univ) => hsingle p)
  have hc : (∑ _ : Fin (degree k) × Fin (degree k), B) = (degree k : ℝ) ^ 2 * B := by
    simp only [Finset.sum_const, Finset.card_univ, Fintype.card_prod, Fintype.card_fin,
      nsmul_eq_mul, Nat.cast_mul]
    ring
  have hsum : eventWeight (sampleWeight k) (BadIntersection k) ≤ (degree k : ℝ) ^ 2 * B :=
    hu.trans (hc ▸ hs)
  calc
    eventWeight (sampleWeight k) (BadIntersection k) ≤ (degree k : ℝ) ^ 2 * B := hsum
    _ ≤ (Real.exp (4 * (k : ℝ) ^ 3)) ^ 2 * B :=
      mul_le_mul_of_nonneg_right
        (pow_le_pow_left₀ (Nat.cast_nonneg _) (degree_le_exp k) 2) (Real.exp_pos _).le
    _ = intersectionBound k := by
      unfold B intersectionBound
      rw [← Real.exp_nat_mul, ← Real.exp_add]
      congr 1
      ring

-- Source: Er579.CubeGenerators:792
theorem sample_badFour_le {k : ℕ} (hk : 3 ≤ k) :
    eventWeight (sampleWeight k) (BadFour k) ≤ fourBound k := by
  let Q := (Fin (degree k) × Fin (degree k)) × (Fin (degree k) × Fin (degree k))
  let B : ℝ := Real.exp (-2 * (k : ℝ) ^ 4)
  let E : Q → Sample k → Prop := fun t ω =>
    FourDistinct t.1.1 t.1.2 t.2.1 t.2.2 ∧
      ∀ a, Bool.xor (Bool.xor (ω t.1.1 a) (ω t.1.2 a))
        (Bool.xor (ω t.2.1 a) (ω t.2.2 a)) = false
  have hsingle (t : Q) : eventWeight (sampleWeight k) (E t) ≤ B := by
    by_cases h : FourDistinct t.1.1 t.1.2 t.2.1 t.2.2
    · rcases h with ⟨hij, hil, hiq, hjl, hjq, hlq⟩
      have hr := theta_range hk
      have hb := array_four_zero_bound (F := Fin (dimension k)) hr.1 hr.2
        t.1.1 t.1.2 t.2.1 t.2.2 hij hil hiq hjl hjq hlq
      have he : -2 * theta k * (dimension k : ℝ) = -2 * (k : ℝ) ^ 4 := by
        calc
          _ = -2 * ((dimension k : ℝ) * theta k) := by ring
          _ = _ := by rw [dimension_theta (show 0 < k by omega)]
      simp only [Fintype.card_fin, he] at hb
      exact (eventWeight_mono _ (sampleWeight_nonnegative hk) (fun _ h => h.2)).trans hb
    · simp only [E, h, false_and, eventWeight, if_false, Finset.sum_const_zero]
      exact (Real.exp_pos _).le
  have hu := eventWeight_exists_le_sum (sampleWeight k) (sampleWeight_nonnegative hk) E
  have hs := Finset.sum_le_sum (fun t (_ : t ∈ Finset.univ) => hsingle t)
  have hc : (∑ _ : Q, B) = (degree k : ℝ) ^ 4 * B := by
    simp only [Q, Finset.sum_const, Finset.card_univ, Fintype.card_prod,
      Fintype.card_fin, nsmul_eq_mul, Nat.cast_mul]
    ring
  have hsum : eventWeight (sampleWeight k) (BadFour k) ≤ (degree k : ℝ) ^ 4 * B :=
    hu.trans (hc ▸ hs)
  calc
    eventWeight (sampleWeight k) (BadFour k) ≤ (degree k : ℝ) ^ 4 * B := hsum
    _ ≤ Real.exp (4 * (k : ℝ) ^ 3) ^ 4 * B :=
      mul_le_mul_of_nonneg_right
        (pow_le_pow_left₀ (Nat.cast_nonneg _) (degree_le_exp k) 4) (Real.exp_pos _).le
    _ = fourBound k := by
      unfold B fourBound
      rw [← Real.exp_nat_mul, ← Real.exp_add]
      congr 1
      ring

-- Source: Er579.CubeGenerators:833
theorem chi_abs_le_one {n : ℕ} (S : Finset (Fin n)) (x : BoolCube n) : |chiS S x| ≤ 1 := by
  rw [abs_le]
  have h := chiS_sq_eq_one S x
  constructor <;> nlinarith

-- Source: Er579.CubeGenerators:838
theorem sampled_character_bound {k : ℕ} (hk : 3 ≤ k) (S : Finset (Fin (dimension k))) :
    eventWeight (sampleWeight k) (fun ω => accuracy k <
      |eigenvalue (sampleDirections ω) S - chiS S (one (dimension k)) *
        (1 - 2 * theta k) ^ S.card|) ≤
          2 * Real.exp (-(degree k : ℝ) * accuracy k ^ 2 / 16) := by
  have hr := theta_range hk
  have hconc := iid_average_concentration (bernoulliWeight (theta k))
    (bernoulliWeight_nonneg hr.1 (show theta k ≤ 1 by linarith [hr.2]))
    (bernoulli_normalization (theta k))
    (fun x : BoolCube (dimension k) => chiS S (xor (one (dimension k)) x))
    (fun x => chi_abs_le_one S _) (degree_pos k) (accuracy k)
    (accuracy_pos k).le (accuracy_le_one k)
  have hclosed : eventWeight (sampleWeight k) (fun ω => accuracy k ≤
      |eigenvalue (sampleDirections ω) S - chiS S (one (dimension k)) *
        (1 - 2 * theta k) ^ S.card|) ≤
          2 * Real.exp (-(degree k : ℝ) * accuracy k ^ 2 / 16) := by
    simpa only [sampleWeight, sampleDirections, eigenvalue, Fintype.card_fin,
      bernoulli_character_mean] using hconc
  exact (eventWeight_mono _ (sampleWeight_nonnegative hk) (fun _ h => h.le)).trans hclosed

-- Source: Er579.CubeGenerators:858
theorem two_pow_le_exp (n : ℕ) : (2 : ℝ) ^ n ≤ Real.exp n := by
  calc
    (2 : ℝ) ^ n ≤ Real.exp 1 ^ n := by
      apply pow_le_pow_left₀ (by norm_num)
      linarith [Real.add_one_le_exp (1 : ℝ)]
    _ = Real.exp n := by rw [← Real.exp_nat_mul, mul_one]

-- Source: Er579.CubeGenerators:865
theorem sample_badSpectral_le {k : ℕ} (hk : 3 ≤ k) :
    eventWeight (sampleWeight k) (BadSpectral k) ≤ spectralBound k := by
  let B : ℝ := 2 * Real.exp (-(degree k : ℝ) * accuracy k ^ 2 / 16)
  have hu := eventWeight_exists_le_sum (sampleWeight k) (sampleWeight_nonnegative hk)
    (fun S ω => accuracy k < |eigenvalue (sampleDirections ω) S -
      chiS S (one (dimension k)) * (1 - 2 * theta k) ^ S.card|)
  have hs := Finset.sum_le_sum (fun S (_ : S ∈ Finset.univ) => sampled_character_bound hk S)
  have hc : (∑ _ : Finset (Fin (dimension k)), B) = (2 : ℝ) ^ dimension k * B := by
    simp only [Finset.sum_const, Finset.card_univ, Fintype.card_finset, Fintype.card_fin,
      nsmul_eq_mul, Nat.cast_pow, Nat.cast_ofNat]
  have hsum : eventWeight (sampleWeight k) (BadSpectral k) ≤ (2 : ℝ) ^ dimension k * B :=
    hu.trans (hc ▸ hs)
  calc
    eventWeight (sampleWeight k) (BadSpectral k) ≤ (2 : ℝ) ^ dimension k * B := hsum
    _ ≤ Real.exp (dimension k) * B :=
      mul_le_mul_of_nonneg_right (two_pow_le_exp _) (by positivity)
    _ = spectralBound k := by
      unfold B spectralBound
      rw [mul_left_comm, ← Real.exp_add]
      congr 2
      rw [show -(degree k : ℝ) * accuracy k ^ 2 = -((degree k : ℝ) * accuracy k ^ 2) by ring,
        accuracy_degree_identity]
      simp only [dimension, Nat.cast_pow]
      ring

-- Source: Er579.CubeGenerators:890
theorem sample_badTuple_le {k : ℕ} (hk : 3 ≤ k) :
    eventWeight (sampleWeight k) (BadTuple k) ≤ failureBound k := by
  have hw := sampleWeight_nonnegative hk
  have h1 := eventWeight_or_le (sampleWeight k) hw (BadSize k)
    (fun ω => BadIntersection k ω ∨ BadFour k ω ∨ BadSpectral k ω)
  have h2 := eventWeight_or_le (sampleWeight k) hw (BadIntersection k)
    (fun ω => BadFour k ω ∨ BadSpectral k ω)
  have h3 := eventWeight_or_le (sampleWeight k) hw (BadFour k) (BadSpectral k)
  have hs := sample_badSize_le hk
  have hi := sample_badIntersection_le hk
  have hf := sample_badFour_le hk
  have hp := sample_badSpectral_le hk
  unfold BadTuple failureBound
  linarith

-- Source: Er579.CubeGenerators:905
theorem nearAntipode_support {n : ℕ} (x : BoolCube n) :
    Er579.CubeGeometry.nearAntipode (bitSupport x) = xor (one n) x := by
  funext a
  unfold Er579.CubeGeometry.nearAntipode CubeProfiles.xor one
  simp only [mem_bitSupport]
  cases x a <;> rfl

-- Source: Er579.CubeGenerators:912
theorem four_directions_zero_iff {k : ℕ} (ω : Sample k)
    (i j l q : Fin (degree k)) :
    xor (xor (sampleDirections ω i) (sampleDirections ω j))
        (xor (sampleDirections ω l) (sampleDirections ω q)) = zero (dimension k) ↔
      ∀ a, Bool.xor (Bool.xor (ω i a) (ω j a)) (Bool.xor (ω l a) (ω q a)) = false := by
  constructor
  · intro h a
    have ha := congrFun h a
    cases h₁ : ω i a <;> cases h₂ : ω j a <;> cases h₃ : ω l a <;> cases h₄ : ω q a <;>
      simpa [sampleDirections, CubeProfiles.xor, one, zero, h₁, h₂, h₃, h₄] using ha
  · intro h
    funext a
    have ha := h a
    cases h₁ : ω i a <;> cases h₂ : ω j a <;> cases h₃ : ω l a <;> cases h₄ : ω q a <;>
      simpa [sampleDirections, CubeProfiles.xor, one, zero, h₁, h₂, h₃, h₄] using ha

-- Source: Er579.CubeGenerators:928
theorem goodTuple_of_not_bad {k : ℕ} (ω : Sample k) (h : ¬ BadTuple k ω) :
    GoodTuple k (fun i => bitSupport (ω i)) := by
  obtain ⟨hs, hi, hf, hp⟩ : ¬ BadSize k ω ∧ ¬ BadIntersection k ω ∧
      ¬ BadFour k ω ∧ ¬ BadSpectral k ω := by
    simpa only [BadTuple, not_or] using h
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · intro i
    exact le_of_not_gt (fun hlt => hs ⟨i, Or.inl hlt⟩)
  · intro i
    exact le_of_not_gt (fun hlt => hs ⟨i, Or.inr hlt⟩)
  · intro i j hij
    exact lt_of_not_ge (fun hle => hi ⟨(i, j), hij, hle⟩)
  · intro i j l q hij hil hiq hjl hjq hlq hzero
    have hraw : xor (xor (sampleDirections ω i) (sampleDirections ω j))
        (xor (sampleDirections ω l) (sampleDirections ω q)) = zero (dimension k) := by
      simpa only [nearAntipode_support, sampleDirections] using hzero
    exact hf ⟨((i, j), (l, q)), ⟨hij, hil, hiq, hjl, hjq, hlq⟩,
      (four_directions_zero_iff ω i j l q).mp hraw⟩
  · intro S
    have hle : |eigenvalue (sampleDirections ω) S - chiS S (one (dimension k)) *
        (1 - 2 * theta k) ^ S.card| ≤ accuracy k :=
      le_of_not_gt (fun hlt => hp ⟨S, hlt⟩)
    have heq : (fun i => Er579.CubeGeometry.nearAntipode (bitSupport (ω i))) = sampleDirections ω := by
      funext i
      exact nearAntipode_support (ω i)
    rw [heq]
    exact hle

-- Source: Er579.CubeGenerators:956
/-- The actual finite generator tuple exists for every sufficiently large integer.
All probabilistic inputs are proved finite weighted-sum calculations above. -/
theorem eventually_exists_good_tuple :
    ∀ᶠ k in Filter.atTop, ∃ T : Fin (degree k) → Finset (Fin (dimension k)), GoodTuple k T := by
  filter_upwards [failureBound_eventually_lt_one, Filter.eventually_ge_atTop 3] with k hk hk3
  have hbad : eventWeight (sampleWeight k) (BadTuple k) < 1 :=
    lt_of_le_of_lt (sample_badTuple_le hk3) hk
  obtain ⟨ω, hω⟩ := exists_outside_event (sampleWeight k) (sampleWeight_normalized k) (BadTuple k) hbad
  exact ⟨fun i => bitSupport (ω i), goodTuple_of_not_bad ω hω⟩

end Er579.CubeGenerators

end

/- Source fragment: Er579.CubeIndependence. Original licenses and source proofs retained. -/

section

namespace Er579.CubeProfiles

open scoped BigOperators
open BooleanAnalysis BooleanAnalysis.Hypercontractivity

-- Source: Er579.CubeIndependence:9
theorem cube_probability_le_one {n : ℕ} (A : BoolCube n → Prop) :
    cubeProbability A ≤ 1 := by
  classical
  unfold cubeProbability
  rw [expect_eq_fintypeExpect]
  calc
    (𝔼 x, cubeIndicator A x) ≤ 𝔼 _x : BoolCube n, (1 : ℝ) := by
      apply Finset.expect_le_expect
      intro x _
      by_cases hx : A x <;> simp [cubeIndicator, hx]
    _ = 1 := Fintype.expect_const 1

-- Source: Er579.CubeIndependence:21
theorem cubeIndicator_translate {n : ℕ} (t : BoolCube n) (A : BoolCube n → Prop) :
    cubeIndicator (fun x => A (xor x t)) = translate t (cubeIndicator A) := rfl

-- Source: Er579.CubeIndependence:24
theorem cubeProbability_translate {n : ℕ} (t : BoolCube n) (A : BoolCube n → Prop) :
    cubeProbability (fun x => A (xor x t)) = cubeProbability A := by
  unfold cubeProbability
  rw [cubeIndicator_translate, expect_translate]

-- Source: Er579.CubeIndependence:29
theorem innerProduct_indicator_self {n : ℕ} (A : BoolCube n → Prop) :
    innerProduct (cubeIndicator A) (cubeIndicator A) = cubeProbability A := by
  classical
  unfold innerProduct cubeProbability
  congr 1
  funext x
  by_cases hx : A x <;> simp [cubeIndicator, hx]

-- Source: Er579.CubeIndependence:37
theorem cubeProbability_finset {n : ℕ} (I : Finset (BoolCube n)) :
    cubeProbability (fun x => x ∈ I) =
      (I.card : ℝ) / Fintype.card (BoolCube n) := by
  classical
  unfold cubeProbability
  rw [expect_eq_fintypeExpect]
  change (𝔼 x : BoolCube n, (Set.indicator (I : Set (BoolCube n)) 1 x : ℝ)) = _
  rw [Finset.expect_indicator_one, Finset.nnratCast_dens]

-- Source: Er579.CubeIndependence:46
/-- Integer-exponent reverse mixing turns character approximation into a
dyadic independence bound.  Its hypotheses are all finite properties of
the sampled generator tuple. -/
theorem independent_probability_le_dyadic {n : ℕ} {ι : Type*} [Fintype ι]
    (k : ℕ) (hk : 2 ≤ k) (s : ι → BoolCube n)
    (hs : ∀ i, s i ≠ zero n)
    (hclose : ∀ S : Finset (Fin n),
      |eigenvalue s S - chiS S (one n) * (1 - 2 / (k : ℝ) ^ 2) ^ S.card| ≤
        ((2 : ℝ)⁻¹) ^ (k ^ 3))
    (I : Finset (BoolCube n)) (hI : (cayley s).IsIndepSet I) :
    cubeProbability (fun x => x ∈ I) ≤ ((2 : ℝ)⁻¹) ^ k := by
  let A : BoolCube n → Prop := fun x => x ∈ I
  let a := cubeProbability A
  let ρ := 1 - 2 / (k : ℝ) ^ 2
  let ξ := ((2 : ℝ)⁻¹) ^ (k ^ 3)
  have hkreal : (2 : ℝ) ≤ k := by exact_mod_cast hk
  have hkpos : 0 < (k : ℝ) := by linarith
  have hksq : 0 < (k : ℝ) ^ 2 := sq_pos_of_pos hkpos
  have hρ0 : 0 < ρ := by
    dsimp only [ρ]
    have hfrac : 2 / (k : ℝ) ^ 2 < 1 := by
      apply (div_lt_one hksq).2
      nlinarith
    linarith
  have hρ1 : ρ < 1 := by
    dsimp only [ρ]
    have hfrac : 0 < 2 / (k : ℝ) ^ 2 := div_pos (by norm_num) hksq
    linarith
  have hexp : 2 / (1 - ρ) = (k ^ 2 : ℕ) := by
    dsimp only [ρ]
    push_cast
    field_simp
    ring
  have hmix := Er579.cube_set_mixing_same_mass ρ hρ0 hρ1 A
    (fun x => A (xor x (one n))) (cubeProbability_translate (one n) A)
  rw [hexp, Real.rpow_natCast, cubeIndicator_translate] at hmix
  have hcomp := energy_comparison s ρ ξ (cubeIndicator A) hclose
  rw [independent_energy_zero s hs I hI, innerProduct_indicator_self, zero_add] at hcomp
  have ha0 : 0 ≤ a := Er579.cube_probability_nonnegative A
  have ha1 : a ≤ 1 := cube_probability_le_one A
  have hξ : 0 ≤ ξ := by positivity
  have hpower : a ^ (k ^ 2) ≤ ξ := by
    have hbound : ξ * a ≤ ξ := by
      simpa only [mul_one] using (mul_le_mul_of_nonneg_left ha1 hξ)
    exact hmix.trans (hcomp.trans hbound)
  have hpow : (((2 : ℝ)⁻¹) ^ k) ^ (k ^ 2) = ξ := by
    dsimp only [ξ]
    rw [← pow_mul]
    congr 1
    ring
  rw [← hpow] at hpower
  have hkexp : k ^ 2 ≠ 0 := pow_ne_zero 2 (by omega)
  exact (pow_le_pow_iff_left₀ ha0 (by positivity) hkexp).mp hpower

-- Source: Er579.CubeIndependence:100
theorem indepNum_le_dyadic {n : ℕ} {ι : Type*} [Fintype ι]
    (k : ℕ) (hk : 2 ≤ k) (s : ι → BoolCube n)
    (hs : ∀ i, s i ≠ zero n)
    (hclose : ∀ S : Finset (Fin n),
      |eigenvalue s S - chiS S (one n) * (1 - 2 / (k : ℝ) ^ 2) ^ S.card| ≤
        ((2 : ℝ)⁻¹) ^ (k ^ 3)) :
    ((cayley s).indepNum : ℝ) ≤ ((2 : ℝ)⁻¹) ^ k * Fintype.card (BoolCube n) := by
  obtain ⟨I, hI⟩ := (cayley s).exists_isNIndepSet_indepNum
  have h := independent_probability_le_dyadic k hk s hs hclose I hI.isIndepSet
  rw [cubeProbability_finset, hI.card_eq] at h
  exact (div_le_iff₀ (by exact_mod_cast Fintype.card_pos)).mp h

end Er579.CubeProfiles

end

/- Source fragment: Er579.FriedgutRegev.Lexicographic. Original licenses and source proofs retained. -/

section

/-!
Lexicographic Boolean thresholds realizing arbitrary dyadic biases.  The
acceptance polynomial has uniform derivative at most two, independent of
the denominator.  The product-law and influence transfers are separate
proof obligations; this file does not assert a junta theorem.
-/

namespace Er579.FriedgutRegev

-- Source: Er579.FriedgutRegev.Lexicographic:16
theorem bool_min_false (b : Bool) : min false b = false := by cases b <;> rfl

-- Source: Er579.FriedgutRegev.Lexicographic:17
theorem bool_min_true (b : Bool) : min true b = b := by cases b <;> rfl

-- Source: Er579.FriedgutRegev.Lexicographic:18
theorem bool_max_false (b : Bool) : max false b = b := by cases b <;> rfl

-- Source: Er579.FriedgutRegev.Lexicographic:19
theorem bool_max_true (b : Bool) : max true b = true := by cases b <;> rfl

-- Source: Er579.FriedgutRegev.Lexicographic:21
/-- A monotone threshold accepting exactly the top `k` binary words. -/
def lexThreshold : (n : ℕ) → ℕ → (Fin n → Bool) → Bool
  | 0, k, _ => decide (0 < k)
  | n + 1, k, x =>
      if k ≤ 2 ^ n then min (x 0) (lexThreshold n k (Fin.tail x))
      else max (x 0) (lexThreshold n (k - 2 ^ n) (Fin.tail x))

-- Source: Er579.FriedgutRegev.Lexicographic:28
theorem lexThreshold_monotone (n k : ℕ) : Monotone (lexThreshold n k) := by
  induction n generalizing k with
  | zero =>
      intro x y hxy
      exact le_rfl
  | succ n ih =>
      intro x y hxy
      have htail : Fin.tail x ≤ Fin.tail y := fun i => hxy i.succ
      unfold lexThreshold
      split_ifs
      · exact min_le_min (hxy 0) (ih k htail)
      · exact max_le_max (hxy 0) (ih (k - 2 ^ n) htail)

-- Source: Er579.FriedgutRegev.Lexicographic:41
/-- The acceptance polynomial of the recursive threshold. -/
def lexProbability : ℕ → ℕ → ℝ → ℝ
  | 0, k, _ => if 0 < k then 1 else 0
  | n + 1, k, p =>
      if k ≤ 2 ^ n then p * lexProbability n k p
      else p + (1 - p) * lexProbability n (k - 2 ^ n) p

-- Source: Er579.FriedgutRegev.Lexicographic:48
theorem lexProbability_mem_Icc (n k : ℕ) {p : ℝ}
    (hp : p ∈ Set.Icc (0 : ℝ) 1) :
    lexProbability n k p ∈ Set.Icc (0 : ℝ) 1 := by
  induction n generalizing k with
  | zero =>
      unfold lexProbability
      split_ifs <;> constructor <;> norm_num
  | succ n ih =>
      unfold lexProbability
      split_ifs
      · have h := ih k
        constructor
        · exact mul_nonneg hp.1 h.1
        · exact mul_le_one₀ hp.2 h.1 h.2
      · have h := ih (k - 2 ^ n)
        constructor
        · exact add_nonneg hp.1 (mul_nonneg (by linarith [hp.2]) h.1)
        · have ht : (1 - p) * lexProbability n (k - 2 ^ n) p ≤ (1 - p) * 1 :=
            mul_le_mul_of_nonneg_left h.2 (by linarith [hp.2])
          linarith

-- Source: Er579.FriedgutRegev.Lexicographic:69
/-- Uniform bits realize the exact dyadic probability. -/
theorem lexProbability_half (n k : ℕ) (hk : k ≤ 2 ^ n) :
    lexProbability n k (1 / 2) = (k : ℝ) / (2 : ℝ) ^ n := by
  induction n generalizing k with
  | zero =>
      have hk' : k = 0 ∨ k = 1 := by simp only [pow_zero] at hk; omega
      rcases hk' with rfl | rfl <;> norm_num [lexProbability]
  | succ n ih =>
      unfold lexProbability
      split_ifs with h
      · rw [ih k h, pow_succ]
        ring
      · have hle : 2 ^ n ≤ k := le_of_lt (lt_of_not_ge h)
        have hsub : k - 2 ^ n ≤ 2 ^ n := by
          rw [pow_succ] at hk
          omega
        rw [ih (k - 2 ^ n) hsub, Nat.cast_sub hle, Nat.cast_pow, Nat.cast_ofNat,
          pow_succ]
        have hP : (2 : ℝ) ^ n ≠ 0 := ne_of_gt (pow_pos (by norm_num) n)
        field_simp
        ring

-- Source: Er579.FriedgutRegev.Lexicographic:91
/-- The uniform derivative, hence the pivotal sum, is at most two. -/
theorem lexProbability_hasDerivAt_half (n k : ℕ) :
    ∃ d : ℝ, 0 ≤ d ∧ d ≤ 2 ∧ HasDerivAt (lexProbability n k) d (1 / 2) := by
  induction n generalizing k with
  | zero =>
      refine ⟨0, le_rfl, by norm_num, ?_⟩
      change HasDerivAt (fun _ : ℝ => if 0 < k then 1 else 0) 0 (1 / 2)
      exact hasDerivAt_const _ _
  | succ n ih =>
      have hhalf : (1 / 2 : ℝ) ∈ Set.Icc (0 : ℝ) 1 := by norm_num
      by_cases h : k ≤ 2 ^ n
      · obtain ⟨d, hd0, hd2, hd⟩ := ih k
        have hv := lexProbability_mem_Icc n k hhalf
        refine ⟨lexProbability n k (1 / 2) + (1 / 2) * d, ?_, ?_, ?_⟩
        · linarith [hv.1]
        · linarith [hv.2]
        · have hfun : lexProbability (n + 1) k = fun p => p * lexProbability n k p := by
            funext p
            simp [lexProbability, h]
          rw [hfun]
          change HasDerivAt (fun p => p * lexProbability n k p)
            (lexProbability n k (1 / 2) + (1 / 2) * d) (1 / 2)
          convert (hasDerivAt_id (1 / 2 : ℝ)).mul hd using 1 <;>
            first | rfl | simp [id_eq]
      · obtain ⟨d, hd0, hd2, hd⟩ := ih (k - 2 ^ n)
        have hv := lexProbability_mem_Icc n (k - 2 ^ n) hhalf
        refine ⟨1 - lexProbability n (k - 2 ^ n) (1 / 2) + (1 / 2) * d,
          ?_, ?_, ?_⟩
        · linarith [hv.2]
        · linarith [hv.1]
        · have hfun : lexProbability (n + 1) k =
              fun p => p + (1 - p) * lexProbability n (k - 2 ^ n) p := by
            funext p
            simp [lexProbability, h]
          rw [hfun]
          change HasDerivAt (fun p => p + (1 - p) * lexProbability n (k - 2 ^ n) p)
            (1 - lexProbability n (k - 2 ^ n) (1 / 2) + (1 / 2) * d) (1 / 2)
          convert (hasDerivAt_id (1 / 2 : ℝ)).add
            (((hasDerivAt_const (1 / 2 : ℝ) 1).sub (hasDerivAt_id (1 / 2 : ℝ))).mul hd)
            using 1 <;> first | rfl | (simp only [Pi.sub_apply, id_eq]; ring)

end Er579.FriedgutRegev

end

/- Source fragment: Er579.FriedgutRegev.LexicographicLaw. Original licenses and source proofs retained. -/

section

/-!
Finite product-law verification for the lexicographic embedding.  The raw
weight formula is polynomial in the bias, including outside `[0,1]`; inside
that interval it is the ordinary Bernoulli product probability.
-/

namespace Er579.FriedgutRegev

open scoped BigOperators

-- Source: Er579.FriedgutRegev.LexicographicLaw:15
def bernoulliBitWeight (p : ℝ) (b : Bool) : ℝ := if b then p else 1 - p

-- Source: Er579.FriedgutRegev.LexicographicLaw:17
def bitProductWeight {n : ℕ} (p : ℝ) (x : Fin n → Bool) : ℝ :=
  ∏ i, bernoulliBitWeight p (x i)

-- Source: Er579.FriedgutRegev.LexicographicLaw:20
def bitProductMean {n : ℕ} (p : ℝ) (f : (Fin n → Bool) → ℝ) : ℝ :=
  ∑ x, bitProductWeight p x * f x

-- Source: Er579.FriedgutRegev.LexicographicLaw:23
theorem bitProductWeight_sum (n : ℕ) (p : ℝ) :
    (∑ x : Fin n → Bool, bitProductWeight p x) = 1 := by
  unfold bitProductWeight
  rw [← Fintype.prod_sum]
  simp [bernoulliBitWeight]

-- Source: Er579.FriedgutRegev.LexicographicLaw:29
theorem bitProductMean_const (n : ℕ) (p c : ℝ) :
    bitProductMean p (fun _ : Fin n → Bool => c) = c := by
  unfold bitProductMean
  rw [← Finset.sum_mul, bitProductWeight_sum, one_mul]

-- Source: Er579.FriedgutRegev.LexicographicLaw:34
theorem bitProductWeight_cons (n : ℕ) (p : ℝ) (b : Bool) (x : Fin n → Bool) :
    bitProductWeight p (Fin.cons b x) =
      (if b then p else 1 - p) * bitProductWeight p x := by
  simp [bitProductWeight, bernoulliBitWeight, Fin.prod_univ_succ]

-- Source: Er579.FriedgutRegev.LexicographicLaw:39
theorem bitProductMean_succ (n : ℕ) (p : ℝ)
    (f : (Fin (n + 1) → Bool) → ℝ) :
    bitProductMean p f =
      (1 - p) * bitProductMean p (fun x => f (Fin.cons false x)) +
      p * bitProductMean p (fun x => f (Fin.cons true x)) := by
  have hsum := Fintype.sum_equiv (Fin.consEquiv (fun _ : Fin (n + 1) => Bool))
    (fun y : Bool × (Fin n → Bool) =>
      bitProductWeight p (Fin.cons y.1 y.2) * f (Fin.cons y.1 y.2))
    (fun x => bitProductWeight p x * f x) (fun _ => rfl)
  unfold bitProductMean
  rw [← hsum, Fintype.sum_prod_type, Fintype.sum_bool]
  simp only [bitProductWeight_cons, Bool.false_eq_true, if_false, if_true]
  simp_rw [mul_assoc]
  rw [← Finset.mul_sum, ← Finset.mul_sum]
  ring

-- Source: Er579.FriedgutRegev.LexicographicLaw:55
/-- The recursive polynomial is the actual finite Bernoulli acceptance probability. -/
theorem bitProductMean_lexThreshold (n k : ℕ) (p : ℝ) :
    bitProductMean p (fun x : Fin n → Bool => if lexThreshold n k x then 1 else 0) =
      lexProbability n k p := by
  induction n generalizing k with
  | zero =>
      simp only [lexThreshold, Bool.decide_iff, lexProbability]
      split_ifs <;> exact bitProductMean_const 0 p _
  | succ n ih =>
      rw [bitProductMean_succ]
      by_cases h : k ≤ 2 ^ n
      · simp only [lexThreshold, if_pos h, Fin.cons_zero, Fin.tail_cons,
          bool_min_false, bool_min_true, Bool.false_eq_true, if_false]
        rw [bitProductMean_const, ih, lexProbability, if_pos h]
        ring
      · simp only [lexThreshold, if_neg h, Fin.cons_zero, Fin.tail_cons,
          bool_max_false, bool_max_true, if_true]
        rw [bitProductMean_const, ih, lexProbability, if_neg h]
        ring

end Er579.FriedgutRegev

end

/- Source fragment: Er579.FriedgutRegev.CaptureArithmetic. Original licenses and source proofs retained. -/

section

/-!
Finite arithmetic needed by the weak-capture route.  No capture or inverse-influence
theorem is assumed or asserted in this file.  In particular, these lemmas do not close
the analytic Friedgut--Regev dependency.
-/

open scoped BigOperators

namespace Er579.FriedgutRegev

variable {Ω : Type*} [Fintype Ω]

-- Source: Er579.FriedgutRegev.CaptureArithmetic:69
/-- The varying-bias kernel uses the stricter uniform `1/12` barrier. -/
theorem mass_lt_half_of_biased_energy_lt (a q E : ℝ)
    (hq : q ≤ 2 / 5) (hqone : q < 1)
    (hspectral : (a ^ 2 - q * a) / (1 - q) ≤ E)
    (henergy : E < 1 / 12) : a < 1 / 2 := by
  by_contra h
  have hhalf : 1 / 2 ≤ a := le_of_not_gt h
  have hden : 0 < 1 - q := sub_pos.mpr hqone
  have hspec' : a ^ 2 - q * a ≤ E * (1 - q) :=
    (div_le_iff₀ hden).mp hspectral
  have he' : E * (1 - q) < (1 / 12) * (1 - q) :=
    mul_lt_mul_of_pos_right henergy hden
  have hprod : 0 ≤ (a - 1 / 2) * (a + 1 / 2 - q) :=
    mul_nonneg (sub_nonneg.mpr hhalf) (by linarith)
  nlinarith

end Er579.FriedgutRegev

end

/- Source fragment: Er579.FriedgutRegev.BooleanAdapter. Original licenses and source proofs retained. -/

section

/-! Exact conversion between Bernoulli Boolean cubes and FABL sign cubes. -/

namespace Er579.FriedgutRegev

open scoped BigOperators 

noncomputable section

-- Source: Er579.FriedgutRegev.BooleanAdapter:12
/-- `true` is the sign `-1`, following FABL's biased truth convention. -/
def boolSign : Bool ≃ FABL.Sign where
  toFun b := if b then -1 else 1
  invFun s := decide (s = -1)
  left_inv b := by cases b <;> norm_num
  right_inv s := by
    rcases Int.units_eq_one_or s with rfl | rfl <;> norm_num

-- Source: Er579.FriedgutRegev.BooleanAdapter:20
def boolCubeSign (n : ℕ) : (Fin n → Bool) ≃ FABL.SignCube n :=
  Equiv.piCongrRight fun _ => boolSign

-- Source: Er579.FriedgutRegev.BooleanAdapter:23
def encodeBoolean {n : ℕ} (h : (Fin n → Bool) → Bool) : FABL.BooleanFunction n :=
  fun x => boolSign (h ((boolCubeSign n).symm x))

-- Source: Er579.FriedgutRegev.BooleanAdapter:26
def decodeBoolean {n : ℕ} (g : FABL.BooleanFunction n) : (Fin n → Bool) → Bool :=
  fun x => boolSign.symm (g (boolCubeSign n x))

-- Source: Er579.FriedgutRegev.BooleanAdapter:29
theorem boolSign_antitone : Antitone boolSign := by
  intro x y hxy
  cases x <;> cases y <;>
    norm_num [boolSign, ← Units.val_le_val] at *
  exact (by decide : ¬ true ≤ false) hxy

-- Source: Er579.FriedgutRegev.BooleanAdapter:35
theorem boolSign_symm_antitone : Antitone boolSign.symm := by
  intro x y hxy
  rcases Int.units_eq_one_or x with rfl | rfl <;>
    rcases Int.units_eq_one_or y with rfl | rfl <;>
    norm_num [boolSign, ← Units.val_le_val] at *

-- Source: Er579.FriedgutRegev.BooleanAdapter:41
theorem encodeBoolean_monotone {n : ℕ} (h : (Fin n → Bool) → Bool)
    (hh : Monotone h) : Monotone (encodeBoolean h) := by
  intro x y hxy
  apply boolSign_antitone
  apply hh
  intro i
  exact boolSign_symm_antitone (hxy i)

-- Source: Er579.FriedgutRegev.BooleanAdapter:49
theorem signProductWeight_boolCubeSign {n : ℕ} (p : ℝ)
    (hp : p ∈ Set.Icc (0 : ℝ) 1) (x : Fin n → Bool) :
    (FABL.productProbabilityPMF (FABL.biasedSignPMF p hp) n (boolCubeSign n x)).toReal =
      bitProductWeight p x := by
  rw [FABL.productProbabilityPMF_apply, ENNReal.toReal_prod]
  unfold bitProductWeight
  apply Finset.prod_congr rfl
  intro i _
  rw [FABL.biasedSignPMF_apply_toReal]
  cases hx : x i <;> norm_num [bernoulliBitWeight, boolCubeSign, boolSign, hx]

-- Source: Er579.FriedgutRegev.BooleanAdapter:60
theorem biasedProductMean_eq_bitProductMean {n : ℕ} (p : ℝ)
    (hp : p ∈ Set.Icc (0 : ℝ) 1) (f : FABL.SignCube n → ℝ) :
    FABL.productMean (FABL.biasedSignPMF p hp) f =
      bitProductMean p (fun x => f (boolCubeSign n x)) := by
  unfold FABL.productMean FABL.pmfExpectation bitProductMean
  exact (Fintype.sum_equiv (boolCubeSign n)
    (fun x => bitProductWeight p x * f (boolCubeSign n x))
    (fun x => (FABL.productProbabilityPMF (FABL.biasedSignPMF p hp) n x).toReal * f x)
    (fun x => by rw [signProductWeight_boolCubeSign])).symm

-- Source: Er579.FriedgutRegev.BooleanAdapter:70
theorem encoded_minusProbability_eq_bitProductMean {n : ℕ}
    (h : (Fin n → Bool) → Bool) (p : ℝ) (hp : p ∈ Set.Icc (0 : ℝ) 1) :
    FABL.biasedMinusProbabilityPolynomial (encodeBoolean h) p =
      bitProductMean p (fun x => if h x then 1 else 0) := by
  rw [FABL.biasedMinusProbabilityPolynomial_eq p hp]
  unfold FABL.biasedMinusProbability
  rw [biasedProductMean_eq_bitProductMean]
  apply congrArg (bitProductMean p)
  funext x
  simp only [encodeBoolean, Equiv.symm_apply_apply]
  cases h x <;> norm_num [boolSign]

-- Source: Er579.FriedgutRegev.BooleanAdapter:82
theorem relativeHamming_encode_decode {n : ℕ}
    (h : (Fin n → Bool) → Bool) (g : FABL.BooleanFunction n) :
    FABL.relativeHammingDist (encodeBoolean h) g =
      bitProductMean (1 / 2)
        (fun x => if h x ≠ decodeBoolean g x then (1 : ℝ) else 0) := by
  rw [← FABL.uniformProbability_ne_eq_relativeHammingDist]
  unfold FABL.uniformProbability
  rw [← FABL.pmfExpectation_uniformPMF_eq_expect,
    ← FABL.productProbabilityPMF_uniformSign]
  have hp : (1 / 2 : ℝ) ∈ Set.Icc (0 : ℝ) 1 := by norm_num
  rw [← FABL.biasedSignPMF_one_half_eq_uniform]
  change FABL.productMean (FABL.biasedSignPMF (1 / 2) hp)
    (fun x => if encodeBoolean h x ≠ g x then (1 : ℝ) else 0) = _
  rw [biasedProductMean_eq_bitProductMean]
  apply congrArg (bitProductMean (1 / 2))
  funext x
  simp only [encodeBoolean, decodeBoolean, Equiv.symm_apply_apply]
  congr 1
  exact propext (not_congr boolSign.eq_symm_apply.symm)

end

end Er579.FriedgutRegev

end

/- Source fragment: Er579.FriedgutRegev.BlockLaw. Original licenses and source proofs retained. -/

section

/-! Exact finite push-forward and independent-block identities. -/

namespace Er579.FriedgutRegev

open scoped BigOperators Classical

noncomputable section

variable {I A C : Type*} [Fintype I] [Fintype A] [Fintype C]

-- Source: Er579.FriedgutRegev.BlockLaw:14
def piExpect (p : I → FiniteProbability A) (f : (I → A) → ℝ) : ℝ :=
  (FiniteProbability.pi p).expect f

-- Source: Er579.FriedgutRegev.BlockLaw:17
def pushForward (p : FiniteProbability A) (χ : A → C) : FiniteProbability C where
  weight c := ∑ a, if χ a = c then p.weight a else 0
  nonneg c := Finset.sum_nonneg (fun a _ => by split_ifs; exact p.nonneg a; exact le_rfl)
  sum_one := by
    rw [Finset.sum_comm]
    simpa using p.sum_one

-- Source: Er579.FriedgutRegev.BlockLaw:24
theorem pushForward_expect (p : FiniteProbability A) (χ : A → C) (f : C → ℝ) :
    (pushForward p χ).expect f = p.expect (fun a => f (χ a)) := by
  unfold FiniteProbability.expect RandomRealization.finiteExpectation pushForward
  simp_rw [Finset.sum_mul]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro a _
  simp

omit [Fintype A] [Fintype C] in

-- Source: Er579.FriedgutRegev.BlockLaw:34
theorem product_graph_indicator (w : I → A → ℝ) (χ : A → C)
    (x : I → A) (y : I → C) :
    (∏ i, if χ (x i) = y i then w i (x i) else 0) =
      if (fun i => χ (x i)) = y then ∏ i, w i (x i) else 0 := by
  by_cases h : (fun i => χ (x i)) = y
  · have hi (i : I) : χ (x i) = y i := congrFun h i
    simp [hi]
  · rw [if_neg h]
    have hex : ∃ i, χ (x i) ≠ y i := by
      by_contra hn
      push Not at hn
      exact h (funext hn)
    obtain ⟨i, hi⟩ := hex
    exact Finset.prod_eq_zero (Finset.mem_univ i) (by simp [hi])

-- Source: Er579.FriedgutRegev.BlockLaw:49
/-- Encoding independent blocks gives independent encoded coordinates. -/
theorem pushForward_pi (p : I → FiniteProbability A) (χ : A → C) :
    pushForward (FiniteProbability.pi p) (fun x i => χ (x i)) =
      FiniteProbability.pi (fun i => pushForward (p i) χ) := by
  apply FiniteProbability.ext
  intro y
  dsimp only [pushForward, FiniteProbability.pi]
  let F : I → A → ℝ := fun i a => if χ a = y i then (p i).weight a else 0
  change _ = ∏ i, ∑ a, F i a
  rw [Fintype.prod_sum]
  apply Finset.sum_congr rfl
  intro x _
  by_cases hxy : (fun i => χ (x i)) = y
  · simpa only [F, if_pos hxy] using
      (product_graph_indicator (fun i => (p i).weight) χ x y).symm
  · simpa only [F, if_neg hxy] using
      (product_graph_indicator (fun i => (p i).weight) χ x y).symm

-- Source: Er579.FriedgutRegev.BlockLaw:67
theorem pi_pushForward_expect (p : I → FiniteProbability A) (χ : A → C)
    (f : (I → C) → ℝ) :
    piExpect p (fun x => f (fun i => χ (x i))) =
      piExpect (fun i => pushForward (p i) χ) f := by
  unfold piExpect
  rw [← pushForward_expect (FiniteProbability.pi p) (fun x i => χ (x i)) f,
    pushForward_pi]

-- Source: Er579.FriedgutRegev.BlockLaw:75
def lexBitLaw (n : ℕ) (p : ℝ) (hp : p ∈ Set.Icc (0 : ℝ) 1) :
    FiniteProbability (Fin n → Bool) where
  weight := bitProductWeight p
  nonneg x := Finset.prod_nonneg (fun i _ => by
    unfold bernoulliBitWeight
    split_ifs
    · exact hp.1
    · exact sub_nonneg.mpr hp.2)
  sum_one := bitProductWeight_sum n p

-- Source: Er579.FriedgutRegev.BlockLaw:88
theorem pushForward_lexThreshold_true (n k : ℕ) (p : ℝ)
    (hp : p ∈ Set.Icc (0 : ℝ) 1) :
    (pushForward (lexBitLaw n p hp) (lexThreshold n k)).weight true =
      lexProbability n k p := by
  dsimp only [pushForward, lexBitLaw]
  rw [← bitProductMean_lexThreshold n k p]
  unfold bitProductMean
  apply Finset.sum_congr rfl
  intro x _
  cases hx : lexThreshold n k x <;> simp [hx]

-- Source: Er579.FriedgutRegev.BlockLaw:99
theorem pushForward_lexThreshold_false (n k : ℕ) (p : ℝ)
    (hp : p ∈ Set.Icc (0 : ℝ) 1) :
    (pushForward (lexBitLaw n p hp) (lexThreshold n k)).weight false =
      1 - lexProbability n k p := by
  have hs := (pushForward (lexBitLaw n p hp) (lexThreshold n k)).sum_one
  rw [Fintype.sum_bool, pushForward_lexThreshold_true] at hs
  linarith

end

end Er579.FriedgutRegev

end

/- Source fragment: Er579.FriedgutRegev.DyadicBias. Original licenses and source proofs retained. -/

section

/-!
Finite exact biases for the monotone higher-bias replacement.  The denominator
is a power of two, so the bias has an exact finite uniform-bit realization.
-/

namespace Er579.FriedgutRegev

open Set

-- Source: Er579.FriedgutRegev.DyadicBias:15
/-- Every nonempty subinterval of `[0,1]` contains a nontrivial dyadic bias. -/
theorem exists_dyadic_between (a b : ℝ) (ha : 0 ≤ a) (hab : a < b)
    (hb : b ≤ 1) :
    ∃ (ℓ k : ℕ), 0 < k ∧ k < 2 ^ ℓ ∧
      a < (k : ℝ) / (2 : ℝ) ^ ℓ ∧ (k : ℝ) / (2 : ℝ) ^ ℓ < b := by
  obtain ⟨ℓ, hℓ⟩ := pow_unbounded_of_one_lt (1 / (b - a))
    (show (1 : ℝ) < 2 by norm_num)
  have hP : 0 < (2 : ℝ) ^ ℓ := pow_pos (by norm_num) ℓ
  have hw : 0 < b - a := sub_pos.mpr hab
  have hgap : 1 < (b - a) * (2 : ℝ) ^ ℓ := by
    have h := (div_lt_iff₀ hw).mp hℓ
    simpa [mul_comm] using h
  let k : ℕ := ⌊a * (2 : ℝ) ^ ℓ⌋₊ + 1
  have hkpos : 0 < k := by dsimp [k]; omega
  have hlow : a * (2 : ℝ) ^ ℓ < (k : ℝ) := by
    simpa [k] using Nat.lt_floor_add_one (a * (2 : ℝ) ^ ℓ)
  have hhigh : (k : ℝ) < b * (2 : ℝ) ^ ℓ := by
    have hf := Nat.floor_le (mul_nonneg ha hP.le)
    have hk : (k : ℝ) = (⌊a * (2 : ℝ) ^ ℓ⌋₊ : ℝ) + 1 := by
      simp [k]
    rw [hk]
    nlinarith
  have hkbound : (k : ℝ) < (2 : ℝ) ^ ℓ := by
    calc
      (k : ℝ) < b * (2 : ℝ) ^ ℓ := hhigh
      _ ≤ 1 * (2 : ℝ) ^ ℓ := mul_le_mul_of_nonneg_right hb hP.le
      _ = (2 : ℝ) ^ ℓ := one_mul _
  refine ⟨ℓ, k, hkpos, ?_, ?_, ?_⟩
  · exact_mod_cast hkbound
  · exact (lt_div_iff₀ hP).mpr hlow
  · exact (div_lt_iff₀ hP).mpr hhigh

-- Source: Er579.FriedgutRegev.DyadicBias:47
/-- A continuous derivative of a probability-valued function is small at an
actual dyadic point.  The factor two pays for selecting a finite exact bias
after the mean value theorem. -/
theorem exists_dyadic_derivative_lt (F F' : ℝ → ℝ) (a b : ℝ)
    (ha : 0 ≤ a) (hab : a < b) (hb : b ≤ 1)
    (hF : ContinuousOn F (Icc a b)) (hF' : Continuous F')
    (hderiv : ∀ x ∈ Ioo a b, HasDerivAt F (F' x) x)
    (hFa : 0 ≤ F a) (hFb : F b ≤ 1) :
    ∃ (ℓ k : ℕ), 0 < k ∧ k < 2 ^ ℓ ∧
      a < (k : ℝ) / (2 : ℝ) ^ ℓ ∧ (k : ℝ) / (2 : ℝ) ^ ℓ < b ∧
      F' ((k : ℝ) / (2 : ℝ) ^ ℓ) < 2 / (b - a) := by
  obtain ⟨c, hc, hcderiv⟩ := exists_hasDerivAt_eq_slope F F' hab hF hderiv
  have hw : 0 < b - a := sub_pos.mpr hab
  have hnum : F b - F a ≤ 1 := by linarith
  have hslope : (F b - F a) / (b - a) ≤ 1 / (b - a) :=
    div_le_div_of_nonneg_right hnum hw.le
  have hcsmall : F' c < 2 / (b - a) := by
    rw [hcderiv]
    have hpos : 0 < 1 / (b - a) := one_div_pos.mpr hw
    calc
      (F b - F a) / (b - a) ≤ 1 / (b - a) := hslope
      _ < 2 / (b - a) := by
        have htwo : 2 / (b - a) = 2 * (1 / (b - a)) := by ring
        rw [htwo]
        linarith
  let U : Set ℝ := Ioo a b ∩ {x | F' x < 2 / (b - a)}
  have hUopen : IsOpen U :=
    isOpen_Ioo.inter (isOpen_lt hF' continuous_const)
  have hcU : c ∈ U := ⟨hc, hcsmall⟩
  obtain ⟨u, v, ⟨huc, hcv⟩, huvU⟩ :=
    mem_nhds_iff_exists_Ioo_subset.mp (hUopen.mem_nhds hcU)
  let a' : ℝ := max a u
  let b' : ℝ := min b v
  have ha' : 0 ≤ a' := ha.trans (le_max_left _ _)
  have hac : a' < c := max_lt hc.1 huc
  have hcb : c < b' := lt_min hc.2 hcv
  have hb' : b' ≤ 1 := (min_le_left _ _).trans hb
  obtain ⟨ℓ, k, hk0, hkP, hkleft, hkright⟩ :=
    exists_dyadic_between a' b' ha' (hac.trans hcb) hb'
  have hquv : (k : ℝ) / (2 : ℝ) ^ ℓ ∈ Ioo u v :=
    ⟨(le_max_right _ _).trans_lt hkleft, hkright.trans_le (min_le_right _ _)⟩
  have hqU := huvU hquv
  exact ⟨ℓ, k, hk0, hkP, hqU.1.1, hqU.1.2, hqU.2⟩

end Er579.FriedgutRegev

end

/- Source fragment: Er579.FriedgutRegev.RussoSelection. Original licenses and source proofs retained. -/

section

/-! Dyadic bias selection for the actual Margulis--Russo derivative. -/

namespace Er579.FriedgutRegev

open scoped BigOperators 

noncomputable section

-- Source: Er579.FriedgutRegev.RussoSelection:12
def minusProbabilityDerivative {n : ℕ} (f : FABL.BooleanFunction n) (p : ℝ) : ℝ :=
  ∑ S : Finset (Fin n), (S.card : ℝ) * (FABL.biasMean p) ^ (S.card - 1) *
    FABL.fourierCoeff f.toReal S

-- Source: Er579.FriedgutRegev.RussoSelection:16
theorem continuous_minusProbabilityDerivative {n : ℕ} (f : FABL.BooleanFunction n) :
    Continuous (minusProbabilityDerivative f) := by
  unfold minusProbabilityDerivative FABL.biasMean
  fun_prop

-- Source: Er579.FriedgutRegev.RussoSelection:21
theorem hasDerivAt_minusProbabilityPolynomial {n : ℕ} (f : FABL.BooleanFunction n)
    (p : ℝ) :
    HasDerivAt (FABL.biasedMinusProbabilityPolynomial f)
      (minusProbabilityDerivative f p) p := by
  have harg : HasDerivAt FABL.biasMean (-2) p := by
    change HasDerivAt (fun t : ℝ => 1 - 2 * t) (-2) p
    simpa using ((hasDerivAt_id p).const_mul 2).const_sub 1
  have hbase := (FABL.hasDerivAt_biasedExpectationPolynomial f.toReal
    (FABL.biasMean p)).comp p harg
  have hresult := ((hasDerivAt_const p 1).sub hbase).div_const 2
  unfold FABL.biasedMinusProbabilityPolynomial minusProbabilityDerivative
  convert hresult using 1 <;> first | rfl | ring

-- Source: Er579.FriedgutRegev.RussoSelection:34
theorem minusProbabilityPolynomial_mem_Icc {n : ℕ} (f : FABL.BooleanFunction n)
    (p : ℝ) (hp : p ∈ Set.Icc (0 : ℝ) 1) :
    FABL.biasedMinusProbabilityPolynomial f p ∈ Set.Icc (0 : ℝ) 1 := by
  rw [FABL.biasedMinusProbabilityPolynomial_eq p hp f]
  unfold FABL.biasedMinusProbability FABL.productMean
  constructor
  · apply FABL.pmfExpectation_nonneg
    intro x
    split_ifs <;> norm_num
  · calc
      _ ≤ FABL.pmfExpectation _ (fun _ => (1 : ℝ)) := by
        apply FABL.pmfExpectation_mono
        intro x
        split_ifs <;> norm_num
      _ = 1 := FABL.pmfExpectation_const _ _

-- Source: Er579.FriedgutRegev.RussoSelection:50
/-- Within every nonempty bias interval, a genuinely dyadic bias has pivotal
sum bounded by twice the reciprocal interval width. -/
theorem exists_dyadic_bounded_russo {n : ℕ} (f : FABL.BooleanFunction n)
    (hf : Monotone f) (a b : ℝ) (ha : 0 ≤ a) (hab : a < b) (hb : b ≤ 1) :
    ∃ ℓ k : ℕ, 0 < k ∧ k < 2 ^ ℓ ∧
      a < (k : ℝ) / (2 : ℝ) ^ ℓ ∧ (k : ℝ) / (2 : ℝ) ^ ℓ < b ∧
      ∃ hq : (k : ℝ) / (2 : ℝ) ^ ℓ ∈ Set.Ioo (0 : ℝ) 1,
        FABL.productTotalInfluence
          (FABL.biasedSignPMF ((k : ℝ) / (2 : ℝ) ^ ℓ) ⟨hq.1.le, hq.2.le⟩)
          f.toReal / FABL.biasSigma ((k : ℝ) / (2 : ℝ) ^ ℓ) ^ 2 < 2 / (b - a) := by
  obtain ⟨ℓ, k, hk0, hkl, haq, hqb, hd⟩ := exists_dyadic_derivative_lt
    (FABL.biasedMinusProbabilityPolynomial f) (minusProbabilityDerivative f)
    a b ha hab hb (FABL.continuous_biasedMinusProbabilityPolynomial f).continuousOn
    (continuous_minusProbabilityDerivative f)
    (fun p _ => hasDerivAt_minusProbabilityPolynomial f p)
    (minusProbabilityPolynomial_mem_Icc f a ⟨ha, le_trans hab.le hb⟩).1
    (minusProbabilityPolynomial_mem_Icc f b ⟨le_trans ha hab.le, hb⟩).2
  have hq : (k : ℝ) / (2 : ℝ) ^ ℓ ∈ Set.Ioo (0 : ℝ) 1 :=
    ⟨lt_of_le_of_lt ha haq, lt_of_lt_of_le hqb hb⟩
  refine ⟨ℓ, k, hk0, hkl, haq, hqb, hq, ?_⟩
  have heq := (hasDerivAt_minusProbabilityPolynomial f _).unique
    (FABL.hasDerivAt_biasedMinusProbabilityPolynomial_eq_totalInfluence _ hq f hf)
  simpa only [← heq] using hd

end

end Er579.FriedgutRegev

end

/- Source fragment: Er579.FriedgutRegev.LexicographicEmbedding. Original licenses and source proofs retained. -/

section

/-! Exact independent lexicographic blocks and their influence cost. -/

namespace Er579.FriedgutRegev

open scoped BigOperators Classical

noncomputable section

-- Source: Er579.FriedgutRegev.LexicographicEmbedding:13
def blockCubeEquiv (n ℓ : ℕ) : (Fin (n * ℓ) → Bool) ≃ (Fin n → Fin ℓ → Bool) where
  toFun x i j := x (finProdFinEquiv (i, j))
  invFun x i := x (finProdFinEquiv.symm i).1 (finProdFinEquiv.symm i).2
  left_inv x := by
    funext i
    change x (finProdFinEquiv (finProdFinEquiv.symm i)) = x i
    rw [Equiv.apply_symm_apply]
  right_inv x := by
    funext i j
    simp

-- Source: Er579.FriedgutRegev.LexicographicEmbedding:24
def lexEncode {n ℓ : ℕ} (k : ℕ) (x : Fin n → Fin ℓ → Bool) : Fin n → Bool :=
  fun i => lexThreshold ℓ k (x i)

-- Source: Er579.FriedgutRegev.LexicographicEmbedding:27
def lexLift {n : ℕ} (ℓ k : ℕ) (h : (Fin n → Bool) → Bool) :
    (Fin (n * ℓ) → Bool) → Bool := fun x => h (lexEncode k (blockCubeEquiv n ℓ x))

-- Source: Er579.FriedgutRegev.LexicographicEmbedding:30
theorem lexLift_monotone {n : ℕ} (ℓ k : ℕ) (h : (Fin n → Bool) → Bool)
    (hh : Monotone h) : Monotone (lexLift ℓ k h) := by
  intro x y hxy
  apply hh
  intro i
  apply lexThreshold_monotone
  intro j
  exact hxy (finProdFinEquiv (i, j))

-- Source: Er579.FriedgutRegev.LexicographicEmbedding:39
theorem blockCube_productWeight (n ℓ : ℕ) (p : ℝ) (x : Fin (n * ℓ) → Bool) :
    bitProductWeight p x = ∏ i : Fin n, bitProductWeight p (blockCubeEquiv n ℓ x i) := by
  unfold bitProductWeight
  have heq := Fintype.prod_equiv (finProdFinEquiv : Fin n × Fin ℓ ≃ Fin (n * ℓ))
    (fun z => bernoulliBitWeight p (x (finProdFinEquiv z)))
    (fun i => bernoulliBitWeight p (x i)) (fun _ => rfl)
  rw [← heq, Fintype.prod_prod_type]
  rfl

-- Source: Er579.FriedgutRegev.LexicographicEmbedding:48
theorem bitProductMean_blocks (n ℓ : ℕ) (p : ℝ)
    (hp : p ∈ Set.Icc (0 : ℝ) 1) (f : (Fin n → Fin ℓ → Bool) → ℝ) :
    bitProductMean p (fun x => f (blockCubeEquiv n ℓ x)) =
      piExpect (fun _ : Fin n => lexBitLaw ℓ p hp) f := by
  unfold bitProductMean piExpect FiniteProbability.expect RandomRealization.finiteExpectation
  have heq := Fintype.sum_equiv (blockCubeEquiv n ℓ)
    (fun x => bitProductWeight p x * f (blockCubeEquiv n ℓ x))
    (fun x => (∏ i : Fin n, bitProductWeight p (x i)) * f x)
    (fun x => by rw [blockCube_productWeight])
  rw [heq]
  apply Finset.sum_congr (by ext; simp)
  intro x _
  rfl

-- Source: Er579.FriedgutRegev.LexicographicEmbedding:62
theorem pushForward_lexThreshold_eq_biasLaw (ℓ k : ℕ) (p : ℝ)
    (hp : p ∈ Set.Icc (0 : ℝ) 1) :
    pushForward (lexBitLaw ℓ p hp) (lexThreshold ℓ k) =
      biasMaskBitLaw (lexProbability ℓ k p)
        (lexProbability_mem_Icc ℓ k hp).1 (lexProbability_mem_Icc ℓ k hp).2 := by
  apply FiniteProbability.ext
  intro b
  cases b
  · exact pushForward_lexThreshold_false ℓ k p hp
  · exact pushForward_lexThreshold_true ℓ k p hp

-- Source: Er579.FriedgutRegev.LexicographicEmbedding:73
/-- The lifted Boolean probability is the original probability evaluated at
the exact block acceptance polynomial. -/
theorem minusProbability_lexLift {n : ℕ} (ℓ k : ℕ)
    (h : (Fin n → Bool) → Bool) (p : ℝ) (hp : p ∈ Set.Icc (0 : ℝ) 1) :
    FABL.biasedMinusProbabilityPolynomial (encodeBoolean (lexLift ℓ k h)) p =
      FABL.biasedMinusProbabilityPolynomial (encodeBoolean h) (lexProbability ℓ k p) := by
  rw [encoded_minusProbability_eq_bitProductMean _ p hp,
    encoded_minusProbability_eq_bitProductMean _ _ (lexProbability_mem_Icc ℓ k hp)]
  unfold lexLift
  rw [bitProductMean_blocks n ℓ p hp
    (fun x => if h (lexEncode k x) then 1 else 0)]
  change piExpect (fun _ : Fin n => lexBitLaw ℓ p hp)
    (fun x => if h (fun i => lexThreshold ℓ k (x i)) then 1 else 0) = _
  rw [pi_pushForward_expect _ (lexThreshold ℓ k) (fun x => if h x then 1 else 0)]
  simp_rw [pushForward_lexThreshold_eq_biasLaw]
  unfold piExpect FiniteProbability.expect RandomRealization.finiteExpectation bitProductMean
  apply Finset.sum_congr (by ext; simp)
  intro x _
  rfl

-- Source: Er579.FriedgutRegev.LexicographicEmbedding:93
theorem hasDerivAt_minusProbability_half {n : ℕ} (h : (Fin n → Bool) → Bool)
    (hh : Monotone h) :
    HasDerivAt (FABL.biasedMinusProbabilityPolynomial (encodeBoolean h))
      (FABL.totalInfluence (encodeBoolean h).toReal) (1 / 2) := by
  have hp : (1 / 2 : ℝ) ∈ Set.Ioo (0 : ℝ) 1 := by norm_num
  have hd := FABL.hasDerivAt_biasedMinusProbabilityPolynomial_eq_totalInfluence
    (1 / 2) hp (encodeBoolean h) (encodeBoolean_monotone h hh)
  rw [FABL.biasSigma_sq _ ⟨hp.1.le, hp.2.le⟩,
    FABL.biasedSignPMF_one_half_eq_uniform,
    FABL.productTotalInfluence_uniformSign_eq_totalInfluence] at hd
  norm_num [FABL.biasVarianceScale] at hd
  exact hd

-- Source: Er579.FriedgutRegev.LexicographicEmbedding:106
/-- Lexicographic blocks cost at most a factor two in the pivotal sum,
independently of the block length. -/
theorem lexLift_totalInfluence_le {n : ℕ} (ℓ k : ℕ) (hk : k ≤ 2 ^ ℓ)
    (h : (Fin n → Bool) → Bool) (hh : Monotone h)
    (hq : (k : ℝ) / (2 : ℝ) ^ ℓ ∈ Set.Ioo (0 : ℝ) 1) :
    FABL.totalInfluence (encodeBoolean (lexLift ℓ k h)).toReal ≤
      2 * minusProbabilityDerivative (encodeBoolean h) ((k : ℝ) / (2 : ℝ) ^ ℓ) := by
  obtain ⟨d, _, hd2, hd⟩ := lexProbability_hasDerivAt_half ℓ k
  have hcomp := (hasDerivAt_minusProbabilityPolynomial (encodeBoolean h)
    (lexProbability ℓ k (1 / 2))).comp (1 / 2) hd
  have hnear : FABL.biasedMinusProbabilityPolynomial (encodeBoolean (lexLift ℓ k h))
      =ᶠ[nhds (1 / 2 : ℝ)]
        (fun p => FABL.biasedMinusProbabilityPolynomial (encodeBoolean h)
          (lexProbability ℓ k p)) := by
    filter_upwards [isOpen_Ioo.mem_nhds (by norm_num : (1 / 2 : ℝ) ∈ Set.Ioo (0 : ℝ) 1)]
      with p hp
    exact minusProbability_lexLift ℓ k h p ⟨hp.1.le, hp.2.le⟩
  have heq := (hasDerivAt_minusProbability_half (lexLift ℓ k h)
    (lexLift_monotone ℓ k h hh)).unique (hcomp.congr_of_eventuallyEq hnear)
  rw [lexProbability_half ℓ k hk] at heq
  have hident := (hasDerivAt_minusProbabilityPolynomial (encodeBoolean h) _).unique
    (FABL.hasDerivAt_biasedMinusProbabilityPolynomial_eq_totalInfluence _ hq
      (encodeBoolean h) (encodeBoolean_monotone h hh))
  have hnonneg : 0 ≤ minusProbabilityDerivative (encodeBoolean h)
      ((k : ℝ) / (2 : ℝ) ^ ℓ) := by
    rw [hident]
    apply div_nonneg _ (sq_nonneg _)
    unfold FABL.productTotalInfluence
    exact Finset.sum_nonneg (fun i _ => FABL.productInfluence_nonneg _ _ i)
  rw [heq]
  simpa only [mul_comm] using mul_le_mul_of_nonneg_left hd2 hnonneg

end

end Er579.FriedgutRegev

end

/- Source fragment: Er579.FriedgutRegev.JuntaTransfer. Original licenses and source proofs retained. -/

section

/-! Product conditioning and deterministic junta transfer through independent
finite blocks. All point weights and conditional laws are explicit. -/

namespace Er579.FriedgutRegev

open scoped BigOperators Classical

noncomputable section

variable {I A C : Type*} [Fintype I] [Fintype A] [Fintype C]

-- Source: Er579.FriedgutRegev.JuntaTransfer:14
def blockSplit (J : Finset I) : (I → A) ≃
    ((i : {i : I // i ∈ J}) → A) × ((i : {i : I // i ∉ J}) → A) :=
  Equiv.piEquivPiSubtypeProd (fun i => i ∈ J) (fun _ => A)

-- Source: Er579.FriedgutRegev.JuntaTransfer:18
theorem split_product_weight (p : I → FiniteProbability A) (J : Finset I)
    (x : (i : {i : I // i ∈ J}) → A) (y : (i : {i : I // i ∉ J}) → A) :
    (∏ i, (p i).weight ((blockSplit J).symm (x, y) i)) =
      (∏ i : {i : I // i ∈ J}, (p i).weight (x i)) *
        ∏ i : {i : I // i ∉ J}, (p i).weight (y i) := by
  rw [← Fintype.prod_subtype_mul_prod_subtype (fun i => i ∈ J)]
  congr 1 <;> apply Finset.prod_congr (by ext; simp) <;> intro i _ <;>
    simp [blockSplit, Equiv.piEquivPiSubtypeProd_symm_apply, i.property]

-- Source: Er579.FriedgutRegev.JuntaTransfer:27
theorem pi_split_expect (p : I → FiniteProbability A) (J : Finset I)
    (f : (I → A) → ℝ) :
    piExpect p f =
      piExpect (fun i : {i : I // i ∈ J} => p i) (fun x =>
        piExpect (fun i : {i : I // i ∉ J} => p i)
          (fun y => f ((blockSplit J).symm (x, y)))) := by
  unfold piExpect FiniteProbability.expect RandomRealization.finiteExpectation
  have heq := Fintype.sum_equiv (blockSplit (A := A) J)
    (fun x => (FiniteProbability.pi p).weight x * f x)
    (fun z => (FiniteProbability.pi p).weight ((blockSplit J).symm z) *
      f ((blockSplit J).symm z))
    (fun x => by simp)
  rw [heq, Fintype.sum_prod_type]
  simp only [FiniteProbability.pi, split_product_weight, Finset.mul_sum, mul_assoc]
  apply Finset.sum_congr (by ext; simp)
  intro x _
  apply Finset.sum_congr (by ext; simp)
  intro y _
  congr 2

-- Source: Er579.FriedgutRegev.JuntaTransfer:47
/-- An expectation of a function depending on `J` only uses the coordinate
laws on `J`. -/
theorem pi_expect_dependsOn_congr [Nonempty A]
    (p q : I → FiniteProbability A) (J : Finset I) (f : (I → A) → ℝ)
    (hf : DependsOn f (J : Set I)) (hpq : ∀ i ∈ J, p i = q i) :
    piExpect p f = piExpect q f := by
  let a₀ : A := Classical.choice inferInstance
  let F : ((i : {i : I // i ∈ J}) → A) → ℝ := fun x =>
    f ((blockSplit J).symm (x, fun _ => a₀))
  have hF (x : (i : {i : I // i ∈ J}) → A) (y : (i : {i : I // i ∉ J}) → A) :
      f ((blockSplit J).symm (x, y)) = F x := by
    apply hf
    intro i hi
    change i ∈ J at hi
    simp [blockSplit, Equiv.piEquivPiSubtypeProd_symm_apply, hi]
  rw [pi_split_expect p J f, pi_split_expect q J f]
  simp_rw [hF]
  simp only [piExpect, FiniteProbability.expect_const]
  have hinside : (fun i : {i : I // i ∈ J} => p i) = fun i : {i : I // i ∈ J} => q i :=
    funext (fun i => hpq i i.property)
  rw [hinside]

-- Source: Er579.FriedgutRegev.JuntaTransfer:69
/-- Conditional block law given its encoded value, with positive fiber mass. -/
def fiberLaw (p : FiniteProbability A) (χ : A → C) (c : C)
    (hc : 0 < (pushForward p χ).weight c) : FiniteProbability A where
  weight a := if χ a = c then p.weight a / (pushForward p χ).weight c else 0
  nonneg a := by
    split_ifs
    · exact div_nonneg (p.nonneg a) hc.le
    · exact le_rfl
  sum_one := by
    have hsum :
        (∑ a, if χ a = c then p.weight a / (pushForward p χ).weight c else 0) =
          (∑ a, if χ a = c then p.weight a else 0) / (pushForward p χ).weight c := by
      rw [Finset.sum_div]
      apply Finset.sum_congr rfl
      intro a _
      split_ifs <;> simp
    rw [hsum]
    change (pushForward p χ).weight c / (pushForward p χ).weight c = 1
    exact div_self (ne_of_gt hc)

-- Source: Er579.FriedgutRegev.JuntaTransfer:89
theorem fiberLaw_bayes (p : FiniteProbability A) (χ : A → C) (c : C)
    (hc : 0 < (pushForward p χ).weight c) (a : A) :
    (pushForward p χ).weight c * (fiberLaw p χ c hc).weight a =
      if χ a = c then p.weight a else 0 := by
  change _ * (if χ a = c then _ / _ else 0) = _
  split_ifs
  · field_simp
  · simp

-- Source: Er579.FriedgutRegev.JuntaTransfer:98
/-- Finite Bayes identity for a product of independently encoded blocks. -/
theorem fiberProduct_bayes_expect (p : FiniteProbability A) (χ : A → C)
    (hpos : ∀ c, 0 < (pushForward p χ).weight c)
    (f : (I → C) → (I → A) → ℝ) :
    (FiniteProbability.pi (fun _ : I => pushForward p χ)).expect (fun γ =>
      (FiniteProbability.pi (fun i => fiberLaw p χ (γ i) (hpos _))).expect (f γ)) =
    (FiniteProbability.pi (fun _ : I => p)).expect
      (fun x => f (fun i => χ (x i)) x) := by
  unfold FiniteProbability.expect RandomRealization.finiteExpectation
  simp only [FiniteProbability.pi, Finset.mul_sum]
  have hpoint (γ : I → C) (x : I → A) :
      (∏ i, (pushForward p χ).weight (γ i)) *
          ((∏ i, (fiberLaw p χ (γ i) (hpos _)).weight (x i)) * f γ x) =
        (if (fun i => χ (x i)) = γ then ∏ i, p.weight (x i) else 0) * f γ x := by
    rw [← mul_assoc, ← Finset.prod_mul_distrib]
    simp_rw [fiberLaw_bayes]
    rw [product_graph_indicator]
  simp_rw [hpoint]
  rw [Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro x _
  simp

-- Source: Er579.FriedgutRegev.JuntaTransfer:121
def blockAverage (p : FiniteProbability A) (χ : A → C)
    (hpos : ∀ c, 0 < (pushForward p χ).weight c) (G : (I → A) → Bool)
    (γ : I → C) : ℝ :=
  (FiniteProbability.pi (fun i => fiberLaw p χ (γ i) (hpos _))).expect
    (fun x => if G x then 1 else 0)

-- Source: Er579.FriedgutRegev.JuntaTransfer:127
def blockRound (p : FiniteProbability A) (χ : A → C)
    (hpos : ∀ c, 0 < (pushForward p χ).weight c) (G : (I → A) → Bool)
    (γ : I → C) : Bool := decide ((1 / 2 : ℝ) ≤ blockAverage p χ hpos G γ)

-- Source: Er579.FriedgutRegev.JuntaTransfer:131
theorem blockAverage_dependsOn [Nonempty A]
    (p : FiniteProbability A) (χ : A → C)
    (hpos : ∀ c, 0 < (pushForward p χ).weight c) (G : (I → A) → Bool)
    (J : Finset I) (hG : DependsOn G (J : Set I)) :
    DependsOn (blockAverage p χ hpos G) (J : Set I) := by
  intro γ γ' hγ
  apply pi_expect_dependsOn_congr _ _ J
  · intro x y hxy
    change (if G x then (1 : ℝ) else 0) = (if G y then (1 : ℝ) else 0)
    rw [hG hxy]
  · intro i hi
    simp only [hγ i hi]

-- Source: Er579.FriedgutRegev.JuntaTransfer:144
theorem blockRound_dependsOn [Nonempty A]
    (p : FiniteProbability A) (χ : A → C)
    (hpos : ∀ c, 0 < (pushForward p χ).weight c) (G : (I → A) → Bool)
    (J : Finset I) (hG : DependsOn G (J : Set I)) :
    DependsOn (blockRound p χ hpos G) (J : Set I) := by
  intro γ γ' hγ
  unfold blockRound
  rw [blockAverage_dependsOn p χ hpos G J hG hγ]

-- Source: Er579.FriedgutRegev.JuntaTransfer:153
def booleanLoss (h : Bool) (a : ℝ) : ℝ := if h then 1 - a else a

-- Source: Er579.FriedgutRegev.JuntaTransfer:155
theorem boolean_round_disagreement_le (h : Bool) (a : ℝ)
    (ha0 : 0 ≤ a) (ha1 : a ≤ 1) :
    (if h ≠ decide ((1 / 2 : ℝ) ≤ a) then (1 : ℝ) else 0) ≤
      2 * booleanLoss h a := by
  cases h <;> by_cases ha : (1 / 2 : ℝ) ≤ a
  · rw [decide_eq_true ha]
    norm_num [booleanLoss]
    linarith
  · rw [decide_eq_false ha]
    norm_num [booleanLoss]
    linarith
  · rw [decide_eq_true ha]
    norm_num [booleanLoss]
    linarith
  · rw [decide_eq_false ha]
    norm_num [booleanLoss]
    linarith

-- Source: Er579.FriedgutRegev.JuntaTransfer:173
theorem blockAverage_mem_Icc (p : FiniteProbability A) (χ : A → C)
    (hpos : ∀ c, 0 < (pushForward p χ).weight c) (G : (I → A) → Bool)
    (γ : I → C) : blockAverage p χ hpos G γ ∈ Set.Icc (0 : ℝ) 1 := by
  constructor
  · apply FiniteProbability.expect_nonneg
    intro x
    cases G x <;> norm_num
  · calc
      _ ≤ (FiniteProbability.pi (fun i => fiberLaw p χ (γ i) (hpos _))).expect
          (fun _ => (1 : ℝ)) := by
        apply FiniteProbability.expect_mono
        intro x
        cases G x <;> norm_num
      _ = 1 := FiniteProbability.expect_const _ _

-- Source: Er579.FriedgutRegev.JuntaTransfer:188
theorem fiber_expect_booleanLoss (p : FiniteProbability A) (χ : A → C)
    (hpos : ∀ c, 0 < (pushForward p χ).weight c) (G : (I → A) → Bool)
    (γ : I → C) (h : Bool) :
    (FiniteProbability.pi (fun i => fiberLaw p χ (γ i) (hpos _))).expect
      (fun x => if h ≠ G x then 1 else 0) =
        booleanLoss h (blockAverage p χ hpos G γ) := by
  let law := FiniteProbability.pi (fun i => fiberLaw p χ (γ i) (hpos _))
  cases h
  · unfold booleanLoss blockAverage
    apply congrArg (FiniteProbability.expect law)
    funext x
    cases G x <;> norm_num
  · have hfun : (fun x => if true ≠ G x then (1 : ℝ) else 0) =
        fun x => 1 + (-1) * (if G x then (1 : ℝ) else 0) := by
      funext x
      cases G x <;> norm_num
    rw [hfun]
    change law.expect (fun x => 1 + (-1) * (if G x then (1 : ℝ) else 0)) =
      1 - law.expect (fun x => if G x then (1 : ℝ) else 0)
    rw [FiniteProbability.expect_add, FiniteProbability.expect_const,
      FiniteProbability.expect_const_mul]
    ring

-- Source: Er579.FriedgutRegev.JuntaTransfer:211
/-- Averaging a block junta over the internal states, then rounding, gives a
mask junta. Its disagreement is at most twice the original disagreement. -/
theorem blockRound_disagreement_le_twice (p : FiniteProbability A) (χ : A → C)
    (hpos : ∀ c, 0 < (pushForward p χ).weight c)
    (G : (I → A) → Bool) (h : (I → C) → Bool) :
    (FiniteProbability.pi (fun _ : I => pushForward p χ)).expect
      (fun γ => if h γ ≠ blockRound p χ hpos G γ then (1 : ℝ) else 0) ≤
    2 * (FiniteProbability.pi (fun _ : I => p)).expect
      (fun x => if h (fun i => χ (x i)) ≠ G x then (1 : ℝ) else 0) := by
  let law := FiniteProbability.pi (fun _ : I => pushForward p χ)
  calc
    _ ≤ law.expect (fun γ => 2 * booleanLoss (h γ) (blockAverage p χ hpos G γ)) := by
      apply law.expect_mono
      intro γ
      exact boolean_round_disagreement_le _ _
        (blockAverage_mem_Icc p χ hpos G γ).1
        (blockAverage_mem_Icc p χ hpos G γ).2
    _ = 2 * law.expect (fun γ => booleanLoss (h γ) (blockAverage p χ hpos G γ)) :=
      FiniteProbability.expect_const_mul _ _ _
    _ = _ := by
      congr 1
      simp_rw [← fiber_expect_booleanLoss]
      exact fiberProduct_bayes_expect p χ hpos
        (fun γ x => if h γ ≠ G x then (1 : ℝ) else 0)

end

end Er579.FriedgutRegev

end

/- Source fragment: Er579.FriedgutRegev.HigherBiasJunta. Original licenses and source proofs retained. -/

section

/-! Dimension-independent junta approximation at an increasing dyadic bias.
This is the classical Friedgut replacement for the stronger FR input. -/

namespace Er579.FriedgutRegev

open scoped BigOperators Classical

noncomputable section

-- Source: Er579.FriedgutRegev.HigherBiasJunta:14
/-- A monotone Boolean function has a bounded-coordinate approximation at
some bias in each nonempty interval. The coordinate bound depends only on
the interval width and approximation error. -/
theorem higher_bias_junta {n : ℕ} (h : (Fin n → Bool) → Bool) (hh : Monotone h)
    (a b ε : ℝ) (ha : 0 ≤ a) (hab : a < b) (hb : b ≤ 1) (hε : 0 < ε) :
    ∃ (q : ℝ) (hq0 : 0 ≤ q) (hq1 : q ≤ 1), a < q ∧ q < b ∧
      ∃ (J : Finset (Fin n)) (g : (Fin n → Bool) → Bool),
        J.card ≤ uniformJuntaBound (4 / (b - a)) (ε / 2) ∧
        DependsOn g (J : Set (Fin n)) ∧
        biasMaskMean q hq0 hq1
          (fun x => if h x ≠ g x then (1 : ℝ) else 0) ≤ ε := by
  obtain ⟨ℓ, k, _, hkℓ, haq, hqb, hq, hsmall⟩ := exists_dyadic_bounded_russo
    (encodeBoolean h) (encodeBoolean_monotone h hh) a b ha hab hb
  let q : ℝ := (k : ℝ) / (2 : ℝ) ^ ℓ
  have hq0 : 0 ≤ q := hq.1.le
  have hq1 : q ≤ 1 := hq.2.le
  let M : ℝ := 4 / (b - a)
  have hM : 0 ≤ M := div_nonneg (by norm_num) (sub_nonneg.mpr hab.le)
  have hident := (hasDerivAt_minusProbabilityPolynomial (encodeBoolean h) q).unique
    (FABL.hasDerivAt_biasedMinusProbabilityPolynomial_eq_totalInfluence q hq
      (encodeBoolean h) (encodeBoolean_monotone h hh))
  have hsmall' : minusProbabilityDerivative (encodeBoolean h) q < 2 / (b - a) := by
    rw [hident]
    exact hsmall
  have hI : FABL.totalInfluence (encodeBoolean (lexLift ℓ k h)).toReal ≤ M := by
    have hbound := lexLift_totalInfluence_le ℓ k hkℓ.le h hh hq
    change FABL.totalInfluence (encodeBoolean (lexLift ℓ k h)).toReal ≤ 4 / (b - a)
    calc
      _ ≤ 2 * minusProbabilityDerivative (encodeBoolean h) q := hbound
      _ ≤ 4 / (b - a) := by
        rw [show (4 : ℝ) / (b - a) = 2 * (2 / (b - a)) by ring]
        linarith
  obtain ⟨S, gbit, hS, hgbit, herr⟩ := uniform_friedgut M (ε / 2) hM
    (by positivity) (encodeBoolean (lexLift ℓ k h)) hI
  let blockIndex : Fin (n * ℓ) → Fin n := fun t => (finProdFinEquiv.symm t).1
  let J : Finset (Fin n) := S.image blockIndex
  let G : (Fin n → Fin ℓ → Bool) → Bool := fun x =>
    decodeBoolean gbit ((blockCubeEquiv n ℓ).symm x)
  have hG : DependsOn G (J : Set (Fin n)) := by
    intro x y hxy
    apply congrArg boolSign.symm
    apply hgbit
    intro t ht
    have htJ : blockIndex t ∈ J := Finset.mem_image_of_mem blockIndex ht
    change boolSign (x (blockIndex t) (finProdFinEquiv.symm t).2) =
      boolSign (y (blockIndex t) (finProdFinEquiv.symm t).2)
    rw [hxy (blockIndex t) htJ]
  have hp : (1 / 2 : ℝ) ∈ Set.Icc (0 : ℝ) 1 := by norm_num
  let p := lexBitLaw ℓ (1 / 2) hp
  let χ := lexThreshold ℓ k
  have hmap : pushForward p χ = biasMaskBitLaw q hq0 hq1 := by
    apply FiniteProbability.ext
    intro c
    cases c
    · change (pushForward p χ).weight false = 1 - q
      rw [pushForward_lexThreshold_false, lexProbability_half ℓ k hkℓ.le]
    · change (pushForward p χ).weight true = q
      rw [pushForward_lexThreshold_true, lexProbability_half ℓ k hkℓ.le]
  have hpos : ∀ c, 0 < (pushForward p χ).weight c := by
    intro c
    rw [hmap]
    cases c <;> simp [biasMaskBitLaw, biasMaskBitWeight]
    · exact hq.2
    · exact hq.1
  let g := blockRound p χ hpos G
  refine ⟨q, hq0, hq1, haq, hqb, J, g, le_trans (Finset.card_image_le) hS,
    blockRound_dependsOn p χ hpos G J hG, ?_⟩
  have hrawerror :
      piExpect (fun _ : Fin n => p)
        (fun x => if h (fun i => χ (x i)) ≠ G x then (1 : ℝ) else 0) =
          FABL.relativeHammingDist (encodeBoolean (lexLift ℓ k h)) gbit := by
    rw [relativeHamming_encode_decode]
    rw [← bitProductMean_blocks n ℓ (1 / 2) hp
      (fun x => if h (fun i => χ (x i)) ≠ G x then (1 : ℝ) else 0)]
    apply congrArg (bitProductMean (1 / 2))
    funext x
    simp only [G, Equiv.symm_apply_apply]
    rfl
  have htransfer := blockRound_disagreement_le_twice p χ hpos G h
  change piExpect (fun _ : Fin n => pushForward p χ)
    (fun x => if h x ≠ g x then (1 : ℝ) else 0) ≤
      2 * piExpect (fun _ : Fin n => p)
        (fun x => if h (fun i => χ (x i)) ≠ G x then (1 : ℝ) else 0) at htransfer
  rw [hrawerror] at htransfer
  have htarget : biasMaskMean q hq0 hq1
      (fun x => if h x ≠ g x then (1 : ℝ) else 0) ≤
        2 * FABL.relativeHammingDist (encodeBoolean (lexLift ℓ k h)) gbit := by
    simpa only [hmap, biasMaskMean, biasMaskLaw, g, piExpect] using htransfer
  exact le_trans htarget (by linarith)

end

end Er579.FriedgutRegev

end

/- Source fragment: Er579.FriedgutRegev.IncrementHelpers. Original licenses and source proofs retained. -/

section

/-! Exact finite-coordinate reindexing for the mask increment. This module
does not import the increment or disintegration modules. -/

namespace Er579.FriedgutRegev

open scoped BigOperators Classical

noncomputable section

variable {B D A : Type*} [Fintype B] [Fintype D] [Fintype A]

-- Source: Er579.FriedgutRegev.IncrementHelpers:14
def coordinateCubeEquiv (e : B ≃ D) : (B → A) ≃ (D → A) where
  toFun x d := x (e.symm d)
  invFun x b := x (e b)
  left_inv x := by funext b; simp
  right_inv x := by funext d; simp

-- Source: Er579.FriedgutRegev.IncrementHelpers:20
/-- Reindexing any finite alphabet transports the independent product law
exactly; the alphabet need not be Boolean. -/
theorem pi_reindex_expect (e : B ≃ D) (p : B → FiniteProbability A)
    (f : (B → A) → ℝ) :
    (FiniteProbability.pi p).expect f =
      (FiniteProbability.pi (fun d => p (e.symm d))).expect
        (fun x => f (fun b => x (e b))) := by
  unfold FiniteProbability.expect RandomRealization.finiteExpectation
  have hweight (x : B → A) :
      (∏ b, (p b).weight (x b)) =
        ∏ d, (p (e.symm d)).weight (x (e.symm d)) := by
    apply Fintype.prod_equiv e
    intro b
    simp
  have heq := Fintype.sum_equiv (coordinateCubeEquiv (A := A) e)
    (fun x => (∏ b, (p b).weight (x b)) * f x)
    (fun x => (∏ d, (p (e.symm d)).weight (x d)) * f (fun b => x (e b)))
    (fun x => by
      rw [hweight]
      congr 1
      apply congrArg f
      funext b
      simp [coordinateCubeEquiv])
  exact heq

-- Source: Er579.FriedgutRegev.IncrementHelpers:50
theorem biasMaskMean_reindex (e : B ≃ D) (q : ℝ) (hq0 : 0 ≤ q) (hq1 : q ≤ 1)
    (f : (B → Bool) → ℝ) :
    biasMaskMean q hq0 hq1 f =
      biasMaskMean q hq0 hq1 (fun x : D → Bool => f (fun b => x (e b))) := by
  unfold biasMaskMean biasMaskLaw
  exact pi_reindex_expect e (fun _ : B => biasMaskBitLaw q hq0 hq1) f

-- Source: Er579.FriedgutRegev.IncrementHelpers:57
/-- The proved junta approximation applies to every finite coordinate type
with exactly the same bound as on `Fin n`. -/
theorem higher_bias_junta_finite (h : (B → Bool) → Bool) (hh : Monotone h)
    (a b ε : ℝ) (ha : 0 ≤ a) (hab : a < b) (hb : b ≤ 1) (hε : 0 < ε) :
    ∃ (q : ℝ) (hq0 : 0 ≤ q) (hq1 : q ≤ 1), a < q ∧ q < b ∧
      ∃ (J : Finset B) (g : (B → Bool) → Bool),
        J.card ≤ uniformJuntaBound (4 / (b - a)) (ε / 2) ∧
        DependsOn g (J : Set B) ∧
        biasMaskMean q hq0 hq1
          (fun x => if h x ≠ g x then (1 : ℝ) else 0) ≤ ε := by
  let e : B ≃ Fin (Fintype.card B) := Fintype.equivFin B
  let h' : (Fin (Fintype.card B) → Bool) → Bool := fun x => h (fun b => x (e b))
  have hh' : Monotone h' := by
    intro x y hxy
    apply hh
    intro b
    exact hxy (e b)
  obtain ⟨q, hq0, hq1, haq, hqb, J', g', hJ', hg', herr⟩ :=
    higher_bias_junta h' hh' a b ε ha hab hb hε
  let J : Finset B := J'.image e.symm
  let g : (B → Bool) → Bool := fun x => g' (fun d => x (e.symm d))
  have hg : DependsOn g (J : Set B) := by
    intro x y hxy
    apply hg'
    intro d hd
    exact hxy (e.symm d) (Finset.mem_image_of_mem e.symm hd)
  refine ⟨q, hq0, hq1, haq, hqb, J, g,
    le_trans Finset.card_image_le hJ', hg, ?_⟩
  rw [biasMaskMean_reindex e]
  have hfun : (fun x : Fin (Fintype.card B) → Bool =>
      if h (fun b => x (e b)) ≠ g (fun b => x (e b)) then (1 : ℝ) else 0) =
      fun x => if h' x ≠ g' x then (1 : ℝ) else 0 := by
    funext x
    simp [g, h']
  rw [hfun]
  exact herr

end

end Er579.FriedgutRegev

end

/- Source fragment: Er579.MaskDisintegration. Original licenses and source proofs retained. -/

section

/-! Exact finite mask conditioning. Old fixed coordinates take priority when
a new atom overlaps them. All identities hold at the endpoints of the bias
interval as well as in its interior. -/

namespace Er579

open scoped BigOperators Classical

noncomputable section

-- Source: Er579.MaskDisintegration:15
def overwriteMask {B : Type*} (J : Finset B) (z γ : B → Bool) : B → Bool :=
  fun b => if b ∈ J then z b else γ b

-- Source: Er579.MaskDisintegration:18
def oldPriorityPattern {B : Type*} (J : Finset B) (z w : B → Bool) : B → Bool :=
  fun b => if b ∈ J then z b else w b

-- Source: Er579.MaskDisintegration:21
theorem overwriteMask_empty {B : Type*} (z γ : B → Bool) :
    overwriteMask ∅ z γ = γ := by
  funext b
  simp [overwriteMask]

-- Source: Er579.MaskDisintegration:26
theorem overwriteMask_comp {B : Type*} (J K : Finset B) (z w γ : B → Bool) :
    overwriteMask J z (overwriteMask K w γ) =
      overwriteMask (J ∪ K) (oldPriorityPattern J z w) γ := by
  funext b
  by_cases hJ : b ∈ J <;> by_cases hK : b ∈ K <;>
    simp [overwriteMask, oldPriorityPattern, hJ, hK]

-- Source: Er579.MaskDisintegration:33
theorem overwriteMask_monotone {B : Type*} (J : Finset B) (z : B → Bool) :
    Monotone (overwriteMask J z) := by
  intro γ η h b
  by_cases hb : b ∈ J
  · simp [overwriteMask, hb]
  · simpa only [overwriteMask, if_neg hb] using h b

-- Source: Er579.MaskDisintegration:40
private theorem product_graph_indicator_dependent
    {I A C : Type*} [Fintype I] (w : I → A → ℝ) (χ : I → A → C)
    (x : I → A) (y : I → C) :
    (∏ i, if χ i (x i) = y i then w i (x i) else 0) =
      if (fun i => χ i (x i)) = y then ∏ i, w i (x i) else 0 := by
  by_cases h : (fun i => χ i (x i)) = y
  · have hi (i : I) : χ i (x i) = y i := congrFun h i
    simp [hi]
  · rw [if_neg h]
    have hex : ∃ i, χ i (x i) ≠ y i := by
      by_contra hn
      push Not at hn
      exact h (funext hn)
    obtain ⟨i, hi⟩ := hex
    exact Finset.prod_eq_zero (Finset.mem_univ i) (by simp [hi])

-- Source: Er579.MaskDisintegration:56
theorem coordinatePushForward_pi
    {I A C : Type*} [Fintype I] [Fintype A] [Fintype C]
    (p : I → FiniteProbability A) (χ : I → A → C) :
    FriedgutRegev.pushForward (FiniteProbability.pi p) (fun x i => χ i (x i)) =
      FiniteProbability.pi (fun i => FriedgutRegev.pushForward (p i) (χ i)) := by
  apply FiniteProbability.ext
  intro y
  dsimp only [FriedgutRegev.pushForward, FiniteProbability.pi]
  let F : I → A → ℝ := fun i a => if χ i a = y i then (p i).weight a else 0
  change _ = ∏ i, ∑ a, F i a
  rw [Fintype.prod_sum]
  apply Finset.sum_congr rfl
  intro x _
  by_cases hxy : (fun i => χ i (x i)) = y
  · simpa only [F, if_pos hxy] using
      (product_graph_indicator_dependent (fun i => (p i).weight) χ x y).symm
  · simpa only [F, if_neg hxy] using
      (product_graph_indicator_dependent (fun i => (p i).weight) χ x y).symm

-- Source: Er579.MaskDisintegration:75
theorem finitePushForward_const {A C : Type*} [Fintype A] [Fintype C]
    (p : FiniteProbability A) (c : C) :
    FriedgutRegev.pushForward p (fun _ => c) = FiniteProbability.dirac c := by
  apply FiniteProbability.ext
  intro y
  by_cases h : c = y
  · subst y
    simp [FriedgutRegev.pushForward, FiniteProbability.dirac, p.sum_one]
  · have h' : y ≠ c := Ne.symm h
    simp [FriedgutRegev.pushForward, FiniteProbability.dirac, h, h']

-- Source: Er579.MaskDisintegration:86
theorem finitePushForward_id {A : Type*} [Fintype A] (p : FiniteProbability A) :
    FriedgutRegev.pushForward p (fun a => a) = p := by
  apply FiniteProbability.ext
  intro a
  simp [FriedgutRegev.pushForward]

-- Source: Er579.MaskDisintegration:92
theorem biasConditionalMaskLaw_eq_pushForward {B : Type*} [Fintype B]
    (q : ℝ) (hq0 : 0 ≤ q) (hq1 : q ≤ 1) (J : Finset B) (z : B → Bool) :
    biasConditionalMaskLaw q hq0 hq1 J z =
      FriedgutRegev.pushForward (biasMaskLaw q hq0 hq1) (overwriteMask J z) := by
  unfold biasConditionalMaskLaw biasMaskLaw overwriteMask
  rw [coordinatePushForward_pi]
  congr 1
  funext b
  change (if b ∈ J then FiniteProbability.dirac (z b) else biasMaskBitLaw q hq0 hq1) =
    FriedgutRegev.pushForward (biasMaskBitLaw q hq0 hq1)
      (fun x : Bool => if b ∈ J then z b else x)
  by_cases hb : b ∈ J
  · rw [if_pos hb]
    have hmap : (fun x : Bool => if b ∈ J then z b else x) = (fun _ => z b) := by
      funext x
      simp [hb]
    rw [hmap]
    exact (finitePushForward_const (biasMaskBitLaw q hq0 hq1) (z b)).symm
  · rw [if_neg hb]
    have hmap : (fun x : Bool => if b ∈ J then z b else x) = (fun x => x) := by
      funext x
      simp [hb]
    rw [hmap]
    exact (finitePushForward_id (biasMaskBitLaw q hq0 hq1)).symm

-- Source: Er579.MaskDisintegration:117
theorem biasConditionalMaskMean_eq_overwrite {B : Type*} [Fintype B]
    (q : ℝ) (hq0 : 0 ≤ q) (hq1 : q ≤ 1)
    (J : Finset B) (z : B → Bool) (f : (B → Bool) → ℝ) :
    biasConditionalMaskMean q hq0 hq1 J z f =
      biasMaskMean q hq0 hq1 (fun γ => f (overwriteMask J z γ)) := by
  unfold biasConditionalMaskMean biasMaskMean
  rw [biasConditionalMaskLaw_eq_pushForward, FriedgutRegev.pushForward_expect]

-- Source: Er579.MaskDisintegration:125
theorem biasConditionalMaskMean_overwrite {B : Type*} [Fintype B]
    (q : ℝ) (hq0 : 0 ≤ q) (hq1 : q ≤ 1)
    (J K : Finset B) (z w : B → Bool) (f : (B → Bool) → ℝ) :
    biasConditionalMaskMean q hq0 hq1 K w (fun γ => f (overwriteMask J z γ)) =
      biasConditionalMaskMean q hq0 hq1 (J ∪ K) (oldPriorityPattern J z w) f := by
  rw [biasConditionalMaskMean_eq_overwrite q hq0 hq1 K w,
    biasConditionalMaskMean_eq_overwrite q hq0 hq1 (J ∪ K) (oldPriorityPattern J z w)]
  apply congrArg (biasMaskMean q hq0 hq1)
  funext γ
  rw [overwriteMask_comp]

-- Source: Er579.MaskDisintegration:136
def overwritePair {B : Type*} (J : Finset B) (z : B → Bool)
    (σ : B → Bool × Bool) : B → Bool × Bool :=
  fun b => if b ∈ J then (z b, z b) else σ b

-- Source: Er579.MaskDisintegration:140
theorem overwritePair_fst {B : Type*} (J : Finset B) (z : B → Bool)
    (σ : B → Bool × Bool) :
    (fun b => (overwritePair J z σ b).1) = overwriteMask J z (fun b => (σ b).1) := by
  funext b
  by_cases hb : b ∈ J <;> simp [overwritePair, overwriteMask, hb]

-- Source: Er579.MaskDisintegration:146
theorem overwritePair_snd {B : Type*} (J : Finset B) (z : B → Bool)
    (σ : B → Bool × Bool) :
    (fun b => (overwritePair J z σ b).2) = overwriteMask J z (fun b => (σ b).2) := by
  funext b
  by_cases hb : b ∈ J <;> simp [overwritePair, overwriteMask, hb]

-- Source: Er579.MaskDisintegration:152
theorem biasResidualPairLaw_eq_pushForward {B : Type*} [Fintype B]
    (q : ℝ) (hq0 : 0 ≤ q) (hqhalf : q ≤ 1 / 2) (J : Finset B) (z : B → Bool) :
    biasResidualPairLaw q hq0 hqhalf J z =
      FriedgutRegev.pushForward
        (FiniteProbability.pi (fun _ : B => biasMaskPairBitLaw q hq0 hqhalf))
        (overwritePair J z) := by
  unfold biasResidualPairLaw overwritePair
  rw [coordinatePushForward_pi]
  congr 1
  funext b
  change (if b ∈ J then FiniteProbability.dirac (z b, z b)
      else biasMaskPairBitLaw q hq0 hqhalf) =
    FriedgutRegev.pushForward (biasMaskPairBitLaw q hq0 hqhalf)
      (fun x : Bool × Bool => if b ∈ J then (z b, z b) else x)
  by_cases hb : b ∈ J
  · rw [if_pos hb]
    have hmap : (fun x : Bool × Bool => if b ∈ J then (z b, z b) else x) =
        (fun _ => (z b, z b)) := by
      funext x
      simp [hb]
    rw [hmap]
    exact (finitePushForward_const (biasMaskPairBitLaw q hq0 hqhalf) (z b, z b)).symm
  · rw [if_neg hb]
    have hmap : (fun x : Bool × Bool => if b ∈ J then (z b, z b) else x) =
        (fun x => x) := by
      funext x
      simp [hb]
    rw [hmap]
    exact (finitePushForward_id (biasMaskPairBitLaw q hq0 hqhalf)).symm

-- Source: Er579.MaskDisintegration:182
theorem biasResidualCorrelation_eq_overwrite {B : Type*} [Fintype B]
    (q : ℝ) (hq0 : 0 ≤ q) (hqhalf : q ≤ 1 / 2)
    (J : Finset B) (z : B → Bool) (f : (B → Bool) → ℝ) :
    biasResidualCorrelation q hq0 hqhalf J z f =
      (FiniteProbability.pi (fun _ : B => biasMaskPairBitLaw q hq0 hqhalf)).expect
        (fun σ => f (overwriteMask J z (fun b => (σ b).1)) *
          f (overwriteMask J z (fun b => (σ b).2))) := by
  unfold biasResidualCorrelation
  rw [biasResidualPairLaw_eq_pushForward, FriedgutRegev.pushForward_expect]
  apply congrArg (FiniteProbability.expect _)
  funext σ
  rw [overwritePair_fst, overwritePair_snd]

-- Source: Er579.MaskDisintegration:206
theorem biasResidualCorrelation_empty_overwrite {B : Type*} [Fintype B]
    (q : ℝ) (hq0 : 0 ≤ q) (hqhalf : q ≤ 1 / 2)
    (J : Finset B) (z : B → Bool) (f : (B → Bool) → ℝ) :
    biasResidualCorrelation q hq0 hqhalf ∅ (fun _ => false)
      (fun γ => f (overwriteMask J z γ)) =
        biasResidualCorrelation q hq0 hqhalf J z f := by
  rw [biasResidualCorrelation_eq_overwrite q hq0 hqhalf ∅ (fun _ => false),
    biasResidualCorrelation_eq_overwrite q hq0 hqhalf J z f]
  apply congrArg (FiniteProbability.expect _)
  funext σ
  rw [overwriteMask_empty, overwriteMask_empty]

-- Source: Er579.MaskDisintegration:218
/-- Product expectation separated into the coordinates in `K` and its complement. -/
theorem finitePi_expect_split {B A : Type*} [Fintype B] [Fintype A]
    (p : B → FiniteProbability A) (K : Finset B) (f : (B → A) → ℝ) :
    (FiniteProbability.pi p).expect f =
      ∑ u : K → A, (∏ b : K, (p b).weight (u b)) *
        ∑ v : {b : B // b ∉ K} → A,
          (∏ b : {b : B // b ∉ K}, (p b).weight (v b)) *
            f ((Equiv.piEquivPiSubtypeProd (fun b : B => b ∈ K) (fun _ => A)).symm
              (u, v)) := by
  let e := Equiv.piEquivPiSubtypeProd (fun b : B => b ∈ K) (fun _ => A)
  have hweight (u : K → A) (v : {b : B // b ∉ K} → A) :
      (∏ b : B, (p b).weight (e.symm (u, v) b)) =
        (∏ b : K, (p b).weight (u b)) *
          ∏ b : {b : B // b ∉ K}, (p b).weight (v b) := by
    rw [← Fintype.prod_subtype_mul_prod_subtype (fun b : B => b ∈ K)]
    congr 1
    · apply Finset.prod_congr (by ext b; simp)
      intro b _
      simp [e, Equiv.piEquivPiSubtypeProd, b.property]
    · apply Finset.prod_congr (by ext b; simp)
      intro b _
      simp [e, Equiv.piEquivPiSubtypeProd, b.property]
  unfold FiniteProbability.expect RandomRealization.finiteExpectation FiniteProbability.pi
  calc
    (∑ x : B → A, (∏ b, (p b).weight (x b)) * f x) =
        ∑ y : (K → A) × ({b : B // b ∉ K} → A),
          (∏ b, (p b).weight (e.symm y b)) * f (e.symm y) :=
      Fintype.sum_equiv e _ _ (fun x => by simp)
    _ = _ := by
      rw [Fintype.sum_prod_type]
      apply Finset.sum_congr rfl
      intro u _
      rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro v _
      rw [hweight]
      ring

-- Source: Er579.MaskDisintegration:256
def maskAtomWeight {B : Type*} (q : ℝ) (K : Finset B) (u : K → Bool) : ℝ :=
  ∏ b : K, biasMaskBitWeight q (u b)

-- Source: Er579.MaskDisintegration:259
theorem maskAtomWeight_nonneg {B : Type*}
    (q : ℝ) (hq0 : 0 ≤ q) (hq1 : q ≤ 1) (K : Finset B) (u : K → Bool) :
    0 ≤ maskAtomWeight q K u := by
  unfold maskAtomWeight
  apply Finset.prod_nonneg
  intro b _
  cases u b <;> simp [biasMaskBitWeight, hq0, hq1]

-- Source: Er579.MaskDisintegration:275
def extendMaskAtom {B : Type*} (K : Finset B) (u : K → Bool) : B → Bool :=
  fun b => if hb : b ∈ K then u ⟨b, hb⟩ else false

-- Source: Er579.MaskDisintegration:278
def combineMaskAtom {B : Type*} (K : Finset B)
    (u : K → Bool) (v : {b : B // b ∉ K} → Bool) : B → Bool :=
  (Equiv.piEquivPiSubtypeProd (fun b : B => b ∈ K) (fun _ => Bool)).symm (u, v)

-- Source: Er579.MaskDisintegration:282
def maskCapturingAtoms {B : Type*} (K : Finset B) (T : (B → Bool) → Bool) :
    Finset (K → Bool) := Finset.univ.filter (fun u => T (extendMaskAtom K u))

-- Source: Er579.MaskDisintegration:285
theorem biasConditionalMaskMean_atom_eq_complement {B : Type*} [Fintype B]
    (q : ℝ) (hq0 : 0 ≤ q) (hq1 : q ≤ 1)
    (K : Finset B) (u : K → Bool) (f : (B → Bool) → ℝ) :
    biasConditionalMaskMean q hq0 hq1 K (extendMaskAtom K u) f =
      ∑ v : {b : B // b ∉ K} → Bool,
        (∏ b : {b : B // b ∉ K}, biasMaskBitWeight q (v b)) *
          f (combineMaskAtom K u v) := by
  let p : B → FiniteProbability Bool := fun b => if b ∈ K then
    FiniteProbability.dirac (extendMaskAtom K u b) else biasMaskBitLaw q hq0 hq1
  unfold biasConditionalMaskMean biasConditionalMaskLaw
  change (FiniteProbability.pi p).expect f = _
  rw [finitePi_expect_split p K f]
  have hK (a : K → Bool) :
      (∏ b : K, (p b).weight (a b)) = if a = u then 1 else 0 := by
    by_cases ha : a = u
    · subst a
      simp [p, FiniteProbability.dirac, extendMaskAtom]
    · rw [if_neg ha]
      have hex : ∃ b, a b ≠ u b := by
        by_contra hn
        push Not at hn
        exact ha (funext hn)
      obtain ⟨b, hb⟩ := hex
      apply Finset.prod_eq_zero (Finset.mem_univ b)
      simp [p, FiniteProbability.dirac, extendMaskAtom, b.property, hb]
  have hC (v : {b : B // b ∉ K} → Bool) :
      (∏ b : {b : B // b ∉ K}, (p b).weight (v b)) =
        ∏ b : {b : B // b ∉ K}, biasMaskBitWeight q (v b) := by
    apply Finset.prod_congr rfl
    intro b _
    simp [p, b.property, biasMaskBitLaw]
  simp_rw [hK, hC]
  simp [combineMaskAtom]

-- Source: Er579.MaskDisintegration:319
theorem biasMaskMean_eq_sum_atoms {B : Type*} [Fintype B]
    (q : ℝ) (hq0 : 0 ≤ q) (hq1 : q ≤ 1)
    (K : Finset B) (f : (B → Bool) → ℝ) :
    biasMaskMean q hq0 hq1 f =
      ∑ u : K → Bool, maskAtomWeight q K u *
        biasConditionalMaskMean q hq0 hq1 K (extendMaskAtom K u) f := by
  unfold biasMaskMean biasMaskLaw
  rw [finitePi_expect_split _ K f]
  change (∑ u : K → Bool, maskAtomWeight q K u *
    ∑ v : {b : B // b ∉ K} → Bool,
      (∏ b : {b : B // b ∉ K}, biasMaskBitWeight q (v b)) *
        f (combineMaskAtom K u v)) = _
  apply Finset.sum_congr rfl
  intro u _
  rw [biasConditionalMaskMean_atom_eq_complement]

-- Source: Er579.MaskDisintegration:335
theorem maskJunta_combine_eq_extend {B : Type*}
    (K : Finset B) (T : (B → Bool) → Bool) (hT : DependsOn T (K : Set B))
    (u : K → Bool) (v : {b : B // b ∉ K} → Bool) :
    T (combineMaskAtom K u v) = T (extendMaskAtom K u) := by
  apply hT
  intro b hb
  have hb' : b ∈ K := hb
  simp [combineMaskAtom, extendMaskAtom, Equiv.piEquivPiSubtypeProd, hb']

-- Source: Er579.MaskDisintegration:344
theorem biasConditionalMaskMean_atom_junta_inside {B : Type*} [Fintype B]
    (q : ℝ) (hq0 : 0 ≤ q) (hq1 : q ≤ 1)
    (K : Finset B) (T : (B → Bool) → Bool) (hT : DependsOn T (K : Set B))
    (u : K → Bool) (f : (B → Bool) → ℝ) :
    biasConditionalMaskMean q hq0 hq1 K (extendMaskAtom K u)
      (fun γ => if T γ then f γ else 0) =
        if T (extendMaskAtom K u) then
          biasConditionalMaskMean q hq0 hq1 K (extendMaskAtom K u) f else 0 := by
  rw [biasConditionalMaskMean_atom_eq_complement]
  by_cases hu : T (extendMaskAtom K u) = true
  · rw [if_pos hu, biasConditionalMaskMean_atom_eq_complement]
    apply Finset.sum_congr rfl
    intro v _
    rw [maskJunta_combine_eq_extend K T hT]
    simp [hu]
  · rw [if_neg hu]
    apply Finset.sum_eq_zero
    intro v _
    rw [maskJunta_combine_eq_extend K T hT]
    simp [hu]

-- Source: Er579.MaskDisintegration:365
theorem biasMaskMean_junta_inside_eq_sum_atoms {B : Type*} [Fintype B]
    (q : ℝ) (hq0 : 0 ≤ q) (hq1 : q ≤ 1)
    (K : Finset B) (T : (B → Bool) → Bool) (hT : DependsOn T (K : Set B))
    (f : (B → Bool) → ℝ) :
    biasMaskMean q hq0 hq1 (fun γ => if T γ then f γ else 0) =
      ∑ u ∈ maskCapturingAtoms K T, maskAtomWeight q K u *
        biasConditionalMaskMean q hq0 hq1 K (extendMaskAtom K u) f := by
  rw [biasMaskMean_eq_sum_atoms q hq0 hq1 K]
  simp_rw [biasConditionalMaskMean_atom_junta_inside q hq0 hq1 K T hT]
  unfold maskCapturingAtoms
  rw [Finset.sum_filter]
  apply Finset.sum_congr rfl
  intro u _
  by_cases hu : T (extendMaskAtom K u) = true <;> simp [hu]

-- Source: Er579.MaskDisintegration:380
theorem biasMaskMean_junta_mass_eq_sum_atoms {B : Type*} [Fintype B]
    (q : ℝ) (hq0 : 0 ≤ q) (hq1 : q ≤ 1)
    (K : Finset B) (T : (B → Bool) → Bool) (hT : DependsOn T (K : Set B)) :
    biasMaskMean q hq0 hq1 (fun γ => if T γ then 1 else 0) =
      ∑ u ∈ maskCapturingAtoms K T, maskAtomWeight q K u := by
  have h := biasMaskMean_junta_inside_eq_sum_atoms q hq0 hq1 K T hT (fun _ => 1)
  simpa [biasConditionalMaskMean, FiniteProbability.expect_const] using h

end

end Er579

end

/- Source fragment: Er579.MaskDensityIncrement. Original licenses and source proofs retained. -/

section

/-!
The finite density increment and bounded-iteration bookkeeping. The
analytic input is the proved classical Friedgut junta theorem, applied
at an increasing bias. No weak-capture assertion is assumed.
-/

namespace Er579

open scoped BigOperators Classical

noncomputable section

-- Source: Er579.MaskDensityIncrement:19
def disjointBitWeight {n : ℕ} (q : ℝ) (σ : Fin n → Bool × Bool) : ℝ :=
  ∏ i, biasMaskPairBitWeight q (σ i)

-- Source: Er579.MaskDensityIncrement:22
def disjointBitInner {n : ℕ} (q : ℝ) (f g : (Fin n → Bool) → ℝ) : ℝ :=
  ∑ σ : Fin n → Bool × Bool, disjointBitWeight q σ *
    f (fun i => (σ i).1) * g (fun i => (σ i).2)

-- Source: Er579.MaskDensityIncrement:26
theorem biasMaskMean_eq_bitProductMean {n : ℕ} (q : ℝ) (hq0 : 0 ≤ q) (hq1 : q ≤ 1)
    (f : (Fin n → Bool) → ℝ) :
    biasMaskMean q hq0 hq1 f = FriedgutRegev.bitProductMean q f := by
  unfold biasMaskMean biasMaskLaw FiniteProbability.expect
    RandomRealization.finiteExpectation FiniteProbability.pi
    FriedgutRegev.bitProductMean FriedgutRegev.bitProductWeight
  apply Finset.sum_congr (by ext x; simp)
  intro x _
  rfl

-- Source: Er579.MaskDensityIncrement:36
theorem biasResidualCorrelation_empty_eq_disjointBitInner {n : ℕ}
    (q : ℝ) (hq0 : 0 ≤ q) (hqhalf : q ≤ 1 / 2) (f : (Fin n → Bool) → ℝ) :
    biasResidualCorrelation q hq0 hqhalf ∅ (fun _ => false) f =
      disjointBitInner q f f := by
  unfold biasResidualCorrelation biasResidualPairLaw FiniteProbability.expect
    RandomRealization.finiteExpectation FiniteProbability.pi
    disjointBitInner disjointBitWeight
  apply Finset.sum_congr (by ext σ; simp)
  intro σ _
  simp [biasMaskPairBitLaw, mul_assoc]

-- Source: Er579.MaskDensityIncrement:47
theorem biasConditionalMaskMean_empty {B : Type*} [Fintype B]
    (q : ℝ) (hq0 : 0 ≤ q) (hq1 : q ≤ 1) (f : (B → Bool) → ℝ) :
    biasConditionalMaskMean q hq0 hq1 ∅ (fun _ => false) f = biasMaskMean q hq0 hq1 f := by
  simp [biasConditionalMaskMean, biasConditionalMaskLaw, biasMaskMean, biasMaskLaw]

-- Source: Er579.MaskDensityIncrement:52
theorem paired_cons_fst {n : ℕ} (b : Bool × Bool) (σ : Fin n → Bool × Bool) :
    (fun i => ((Fin.cons b σ : Fin (n + 1) → Bool × Bool) i).1) =
      Fin.cons b.1 (fun i => (σ i).1) := by
  funext i
  refine Fin.cases ?_ (fun j => ?_) i <;> simp

-- Source: Er579.MaskDensityIncrement:58
theorem paired_cons_snd {n : ℕ} (b : Bool × Bool) (σ : Fin n → Bool × Bool) :
    (fun i => ((Fin.cons b σ : Fin (n + 1) → Bool × Bool) i).2) =
      Fin.cons b.2 (fun i => (σ i).2) := by
  funext i
  refine Fin.cases ?_ (fun j => ?_) i <;> simp

-- Source: Er579.MaskDensityIncrement:64
theorem disjointBitWeight_cons {n : ℕ} (q : ℝ) (b : Bool × Bool)
    (σ : Fin n → Bool × Bool) :
    disjointBitWeight q (Fin.cons b σ) = biasMaskPairBitWeight q b * disjointBitWeight q σ := by
  simp [disjointBitWeight, Fin.prod_univ_succ]

-- Source: Er579.MaskDensityIncrement:69
theorem disjointBitInner_succ (n : ℕ) (q : ℝ)
    (f g : (Fin (n + 1) → Bool) → ℝ) :
    disjointBitInner q f g =
      (1 - 2 * q) * disjointBitInner q (fun x => f (Fin.cons false x)) (fun x => g (Fin.cons false x)) +
      q * disjointBitInner q (fun x => f (Fin.cons false x)) (fun x => g (Fin.cons true x)) +
      q * disjointBitInner q (fun x => f (Fin.cons true x)) (fun x => g (Fin.cons false x)) := by
  have hsum := Fintype.sum_equiv (Fin.consEquiv (fun _ : Fin (n + 1) => Bool × Bool))
    (fun y : (Bool × Bool) × (Fin n → Bool × Bool) =>
      disjointBitWeight q (Fin.cons y.1 y.2) *
        f (fun i => ((Fin.cons y.1 y.2 : Fin (n + 1) → Bool × Bool) i).1) *
          g (fun i => ((Fin.cons y.1 y.2 : Fin (n + 1) → Bool × Bool) i).2))
    (fun σ => disjointBitWeight q σ * f (fun i => (σ i).1) * g (fun i => (σ i).2))
    (fun _ => rfl)
  unfold disjointBitInner
  rw [← hsum, Fintype.sum_prod_type, Fintype.sum_prod_type]
  simp only [Fintype.sum_bool, disjointBitWeight_cons, paired_cons_fst, paired_cons_snd,
    biasMaskPairBitWeight, Bool.false_eq_true, if_true, if_false, zero_mul, Finset.sum_const_zero]
  simp_rw [mul_assoc]
  rw [← Finset.mul_sum, ← Finset.mul_sum, ← Finset.mul_sum]
  ring

-- Source: Er579.MaskDensityIncrement:90
theorem biasResidualPair_fst_expect {B : Type*} [Fintype B]
    (q : ℝ) (hq0 : 0 ≤ q) (hqhalf : q ≤ 1 / 2) (hq1 : q ≤ 1)
    (J : Finset B) (z : B → Bool) (f : (B → Bool) → ℝ) :
    (biasResidualPairLaw q hq0 hqhalf J z).expect (fun σ => f (fun b => (σ b).1)) =
      (biasConditionalMaskLaw q hq0 hq1 J z).expect f := by
  unfold biasResidualPairLaw biasConditionalMaskLaw
  apply FiniteProbability.pi_pair_fst_expect
  intro b x
  by_cases hb : b ∈ J
  · cases x <;> cases z b <;> simp [hb, FiniteProbability.dirac]
  · cases x
    · simp [hb, biasMaskPairBitLaw, biasMaskPairBitWeight, biasMaskBitLaw, biasMaskBitWeight]
      ring
    · simp [hb, biasMaskPairBitLaw, biasMaskPairBitWeight, biasMaskBitLaw, biasMaskBitWeight]

-- Source: Er579.MaskDensityIncrement:105
theorem biasResidualPair_snd_expect {B : Type*} [Fintype B]
    (q : ℝ) (hq0 : 0 ≤ q) (hqhalf : q ≤ 1 / 2) (hq1 : q ≤ 1)
    (J : Finset B) (z : B → Bool) (f : (B → Bool) → ℝ) :
    (biasResidualPairLaw q hq0 hqhalf J z).expect (fun σ => f (fun b => (σ b).2)) =
      (biasConditionalMaskLaw q hq0 hq1 J z).expect f := by
  unfold biasResidualPairLaw biasConditionalMaskLaw
  apply FiniteProbability.pi_pair_snd_expect
  intro b x
  by_cases hb : b ∈ J
  · cases x <;> cases z b <;> simp [hb, FiniteProbability.dirac]
  · cases x
    · simp [hb, biasMaskPairBitLaw, biasMaskPairBitWeight, biasMaskBitLaw, biasMaskBitWeight]
      ring
    · simp [hb, biasMaskPairBitLaw, biasMaskPairBitWeight, biasMaskBitLaw, biasMaskBitWeight]

-- Source: Er579.MaskDensityIncrement:120
/-- The elementary Markov contraction used in the spectral induction. -/
theorem biasResidualCorrelation_le_secondMoment {B : Type*} [Fintype B]
    (q : ℝ) (hq0 : 0 ≤ q) (hqhalf : q ≤ 1 / 2) (hq1 : q ≤ 1)
    (J : Finset B) (z : B → Bool) (f : (B → Bool) → ℝ) :
    biasResidualCorrelation q hq0 hqhalf J z f ≤
      biasConditionalMaskMean q hq0 hq1 J z (fun γ => f γ ^ 2) := by
  let p := biasResidualPairLaw q hq0 hqhalf J z
  have hpoint (σ : B → Bool × Bool) :
      f (fun b => (σ b).1) * f (fun b => (σ b).2) ≤
        (f (fun b => (σ b).1) ^ 2 + f (fun b => (σ b).2) ^ 2) / 2 := by
    nlinarith [sq_nonneg (f (fun b => (σ b).1) - f (fun b => (σ b).2))]
  calc
    biasResidualCorrelation q hq0 hqhalf J z f ≤
        p.expect (fun σ =>
          (f (fun b => (σ b).1) ^ 2 + f (fun b => (σ b).2) ^ 2) / 2) :=
      p.expect_mono hpoint
    _ = (p.expect (fun σ => f (fun b => (σ b).1) ^ 2) +
        p.expect (fun σ => f (fun b => (σ b).2) ^ 2)) / 2 := by
      simp only [div_eq_mul_inv, FiniteProbability.expect_mul_const, FiniteProbability.expect_add]
    _ = biasConditionalMaskMean q hq0 hq1 J z (fun γ => f γ ^ 2) := by
      unfold p
      rw [biasResidualPair_fst_expect q hq0 hqhalf hq1 J z (fun γ => f γ ^ 2),
        biasResidualPair_snd_expect q hq0 hqhalf hq1 J z (fun γ => f γ ^ 2)]
      unfold biasConditionalMaskMean
      ring

-- Source: Er579.MaskDensityIncrement:146
theorem disjointBitInner_self_le_secondMoment {n : ℕ}
    (q : ℝ) (hq0 : 0 ≤ q) (hqhalf : q ≤ 1 / 2) (hq1 : q ≤ 1)
    (f : (Fin n → Bool) → ℝ) :
    disjointBitInner q f f ≤ FriedgutRegev.bitProductMean q (fun x => f x ^ 2) := by
  have h := biasResidualCorrelation_le_secondMoment q hq0 hqhalf hq1
    (∅ : Finset (Fin n)) (fun _ => false) f
  rw [biasResidualCorrelation_empty_eq_disjointBitInner,
    biasConditionalMaskMean_empty, biasMaskMean_eq_bitProductMean] at h
  exact h

-- Source: Er579.MaskDensityIncrement:156
theorem bitProductMean_mix {n : ℕ} (q r s : ℝ)
    (f g : (Fin n → Bool) → ℝ) :
    FriedgutRegev.bitProductMean q (fun x => r * f x + s * g x) =
      r * FriedgutRegev.bitProductMean q f + s * FriedgutRegev.bitProductMean q g := by
  unfold FriedgutRegev.bitProductMean
  rw [Finset.mul_sum, Finset.mul_sum, ← Finset.sum_add_distrib]
  apply Finset.sum_congr rfl
  intro x _
  ring

-- Source: Er579.MaskDensityIncrement:166
theorem bitProductMean_mix_secondMoment {n : ℕ} (q : ℝ)
    (f₀ f₁ : (Fin n → Bool) → ℝ) :
    FriedgutRegev.bitProductMean q (fun x => ((1 - q) * f₀ x + q * f₁ x) ^ 2) +
        q * (1 - q) * FriedgutRegev.bitProductMean q (fun x => (f₁ x - f₀ x) ^ 2) =
      (1 - q) * FriedgutRegev.bitProductMean q (fun x => f₀ x ^ 2) +
        q * FriedgutRegev.bitProductMean q (fun x => f₁ x ^ 2) := by
  unfold FriedgutRegev.bitProductMean
  rw [Finset.mul_sum, ← Finset.sum_add_distrib,
    Finset.mul_sum, Finset.mul_sum, ← Finset.sum_add_distrib]
  apply Finset.sum_congr rfl
  intro x _
  ring

-- Source: Er579.MaskDensityIncrement:179
theorem disjointBitInner_mix_sub {n : ℕ} (q : ℝ)
    (f₀ f₁ : (Fin n → Bool) → ℝ) :
    disjointBitInner q (fun x => (1 - q) * f₀ x + q * f₁ x)
        (fun x => (1 - q) * f₀ x + q * f₁ x) -
      q ^ 2 * disjointBitInner q (fun x => f₁ x - f₀ x) (fun x => f₁ x - f₀ x) =
      (1 - 2 * q) * disjointBitInner q f₀ f₀ +
        q * disjointBitInner q f₀ f₁ + q * disjointBitInner q f₁ f₀ := by
  unfold disjointBitInner
  rw [Finset.mul_sum, ← Finset.sum_sub_distrib,
    Finset.mul_sum, Finset.mul_sum, Finset.mul_sum,
    ← Finset.sum_add_distrib, ← Finset.sum_add_distrib]
  apply Finset.sum_congr rfl
  intro σ _
  ring

-- Source: Er579.MaskDensityIncrement:194
/-- The negative eigenvalue bound for every finite biased disjoint cube,
proved by one-coordinate induction and the elementary Markov contraction.
The multiplied form avoids division by `1-q`. -/
theorem disjointBitInner_spectral_lower {n : ℕ}
    (q : ℝ) (hq0 : 0 ≤ q) (hqhalf : q ≤ 1 / 2) (hq1 : q ≤ 1)
    (f : (Fin n → Bool) → ℝ) :
    (FriedgutRegev.bitProductMean q f) ^ 2 -
        q * FriedgutRegev.bitProductMean q (fun x => f x ^ 2) ≤
      (1 - q) * disjointBitInner q f f := by
  induction n with
  | zero =>
      have hf : f = fun _ => f (fun i => Fin.elim0 i) := by
        funext x
        exact congrArg f (Subsingleton.elim _ _)
      rw [hf]
      simp only [FriedgutRegev.bitProductMean_const]
      simp [disjointBitInner, disjointBitWeight]
      nlinarith
  | succ n ih =>
      let f₀ : (Fin n → Bool) → ℝ := fun x => f (Fin.cons false x)
      let f₁ : (Fin n → Bool) → ℝ := fun x => f (Fin.cons true x)
      let g : (Fin n → Bool) → ℝ := fun x => (1 - q) * f₀ x + q * f₁ x
      let h : (Fin n → Bool) → ℝ := fun x => f₁ x - f₀ x
      have hm : FriedgutRegev.bitProductMean q f = FriedgutRegev.bitProductMean q g := by
        rw [FriedgutRegev.bitProductMean_succ]
        exact (bitProductMean_mix q (1 - q) q f₀ f₁).symm
      have hv : FriedgutRegev.bitProductMean q (fun x => f x ^ 2) =
          FriedgutRegev.bitProductMean q (fun x => g x ^ 2) +
            q * (1 - q) * FriedgutRegev.bitProductMean q (fun x => h x ^ 2) := by
        rw [FriedgutRegev.bitProductMean_succ]
        exact (bitProductMean_mix_secondMoment q f₀ f₁).symm
      have he : disjointBitInner q f f = disjointBitInner q g g - q ^ 2 * disjointBitInner q h h := by
        rw [disjointBitInner_succ]
        exact (disjointBitInner_mix_sub q f₀ f₁).symm
      have hg := ih g
      have hh := disjointBitInner_self_le_secondMoment q hq0 hqhalf hq1 h
      have hc : 0 ≤ (1 - q) * q ^ 2 := mul_nonneg (sub_nonneg.mpr hq1) (sq_nonneg q)
      have hh' := mul_le_mul_of_nonneg_left hh hc
      calc
        (FriedgutRegev.bitProductMean q f) ^ 2 -
            q * FriedgutRegev.bitProductMean q (fun x => f x ^ 2) =
            (FriedgutRegev.bitProductMean q g) ^ 2 -
              q * FriedgutRegev.bitProductMean q (fun x => g x ^ 2) -
              ((1 - q) * q ^ 2) * FriedgutRegev.bitProductMean q (fun x => h x ^ 2) := by
          rw [hm, hv]
          ring
        _ ≤ (1 - q) * disjointBitInner q g g -
            ((1 - q) * q ^ 2) * FriedgutRegev.bitProductMean q (fun x => h x ^ 2) :=
          sub_le_sub_right hg _
        _ ≤ (1 - q) * disjointBitInner q g g - ((1 - q) * q ^ 2) * disjointBitInner q h h :=
          sub_le_sub_left hh' _
        _ = (1 - q) * disjointBitInner q f f := by rw [he]; ring

-- Source: Er579.MaskDensityIncrement:247
/-- The uniform half-mass barrier needed by the varying-bias junta step. -/
theorem biasBoolean_mass_lt_half_of_energy_lt {n : ℕ}
    (q : ℝ) (hq0 : 0 ≤ q) (hqhalf : q ≤ 1 / 2) (hq1 : q ≤ 1)
    (hqtwofifths : q ≤ 2 / 5) (g : (Fin n → Bool) → Bool)
    (henergy : biasResidualCorrelation q hq0 hqhalf ∅ (fun _ => false)
      (fun x => if g x then 1 else 0) < 1 / 12) :
    biasMaskMean q hq0 hq1 (fun x => if g x then 1 else 0) < 1 / 2 := by
  let f : (Fin n → Bool) → ℝ := fun x => if g x then 1 else 0
  have hs := disjointBitInner_spectral_lower q hq0 hqhalf hq1 f
  have hv : FriedgutRegev.bitProductMean q (fun x => f x ^ 2) =
      FriedgutRegev.bitProductMean q f := by
    unfold FriedgutRegev.bitProductMean
    apply Finset.sum_congr rfl
    intro x _
    cases hg : g x <;> simp [f, hg]
  rw [hv, ← biasMaskMean_eq_bitProductMean q hq0 hq1 f,
    ← biasResidualCorrelation_empty_eq_disjointBitInner q hq0 hqhalf f] at hs
  apply FriedgutRegev.mass_lt_half_of_biased_energy_lt _ q _ hqtwofifths (by linarith)
    _ henergy
  exact (div_le_iff₀ (show 0 < 1 - q by linarith)).mpr (by simpa only [mul_comm] using hs)

-- Source: Er579.MaskDensityIncrement:268
theorem bitProductWeight_nonneg {n : ℕ} (q : ℝ) (hq0 : 0 ≤ q) (hq1 : q ≤ 1)
    (x : Fin n → Bool) : 0 ≤ FriedgutRegev.bitProductWeight q x := by
  unfold FriedgutRegev.bitProductWeight
  apply Finset.prod_nonneg
  intro i _
  cases x i <;> simp [FriedgutRegev.bernoulliBitWeight] <;> linarith

-- Source: Er579.MaskDensityIncrement:275
theorem bitProductMean_mono_function {n : ℕ} (q : ℝ) (hq0 : 0 ≤ q) (hq1 : q ≤ 1)
    (f g : (Fin n → Bool) → ℝ) (hfg : ∀ x, f x ≤ g x) :
    FriedgutRegev.bitProductMean q f ≤ FriedgutRegev.bitProductMean q g := by
  unfold FriedgutRegev.bitProductMean
  apply Finset.sum_le_sum
  intro x _
  exact mul_le_mul_of_nonneg_left (hfg x) (bitProductWeight_nonneg q hq0 hq1 x)

-- Source: Er579.MaskDensityIncrement:283
theorem monotone_bool_cons_slice {n : ℕ}
    (f : (Fin (n + 1) → Bool) → ℝ) (hf : Monotone f) (b : Bool) :
    Monotone (fun x => f (Fin.cons b x)) := by
  intro x y hxy
  apply hf
  intro i
  refine Fin.cases ?_ (fun j => ?_) i
  · simp
  · simpa only [Fin.cons_succ] using hxy j

-- Source: Er579.MaskDensityIncrement:293
theorem false_cons_le_true_cons {n : ℕ} (x : Fin n → Bool) :
    (Fin.cons false x : Fin (n + 1) → Bool) ≤ Fin.cons true x := by
  intro i
  refine Fin.cases ?_ (fun j => ?_) i
  · simp only [Fin.cons_zero]
    exact Bool.false_le true
  · simp

-- Source: Er579.MaskDensityIncrement:301
/-- Raising the Bernoulli bias cannot lower the mean of any monotone real
function. No Boolean-value or differentiability assumption is needed. -/
theorem bitProductMean_mono_bias {n : ℕ}
    (p q : ℝ) (hp0 : 0 ≤ p) (hq1 : q ≤ 1) (hpq : p ≤ q)
    (f : (Fin n → Bool) → ℝ) (hf : Monotone f) :
    FriedgutRegev.bitProductMean p f ≤ FriedgutRegev.bitProductMean q f := by
  induction n with
  | zero =>
      have heq : f = fun _ => f (fun i => Fin.elim0 i) := by
        funext x
        exact congrArg f (Subsingleton.elim _ _)
      rw [heq]
      simpa only [FriedgutRegev.bitProductMean_const] using le_refl (f (fun i => Fin.elim0 i))
  | succ n ih =>
      let f₀ : (Fin n → Bool) → ℝ := fun x => f (Fin.cons false x)
      let f₁ : (Fin n → Bool) → ℝ := fun x => f (Fin.cons true x)
      have h₀ := ih f₀ (monotone_bool_cons_slice f hf false)
      have h₁ := ih f₁ (monotone_bool_cons_slice f hf true)
      have hq0 : 0 ≤ q := hp0.trans hpq
      have hp1 : p ≤ 1 := hpq.trans hq1
      have hcross : FriedgutRegev.bitProductMean q f₀ ≤ FriedgutRegev.bitProductMean q f₁ :=
        bitProductMean_mono_function q hq0 hq1 f₀ f₁
          (fun x => hf (false_cons_le_true_cons x))
      rw [FriedgutRegev.bitProductMean_succ, FriedgutRegev.bitProductMean_succ]
      calc
        (1 - p) * FriedgutRegev.bitProductMean p f₀ + p * FriedgutRegev.bitProductMean p f₁ ≤
            (1 - p) * FriedgutRegev.bitProductMean q f₀ + p * FriedgutRegev.bitProductMean q f₁ :=
          add_le_add (mul_le_mul_of_nonneg_left h₀ (sub_nonneg.mpr hp1))
            (mul_le_mul_of_nonneg_left h₁ hp0)
        _ ≤ (1 - q) * FriedgutRegev.bitProductMean q f₀ + q * FriedgutRegev.bitProductMean q f₁ := by
          nlinarith [mul_nonneg (sub_nonneg.mpr hpq) (sub_nonneg.mpr hcross)]

-- Source: Er579.MaskDensityIncrement:333
theorem biasMaskMean_mono_bias {n : ℕ}
    (p q : ℝ) (hp0 : 0 ≤ p) (hp1 : p ≤ 1) (hq0 : 0 ≤ q) (hq1 : q ≤ 1)
    (hpq : p ≤ q) (f : (Fin n → Bool) → ℝ) (hf : Monotone f) :
    biasMaskMean p hp0 hp1 f ≤ biasMaskMean q hq0 hq1 f := by
  rw [biasMaskMean_eq_bitProductMean, biasMaskMean_eq_bitProductMean]
  exact bitProductMean_mono_bias p q hp0 hq1 hpq f hf

-- Source: Er579.MaskDensityIncrement:340
theorem biasMaskMean_mono_bias_finite {B : Type*} [Fintype B]
    (p q : ℝ) (hp0 : 0 ≤ p) (hp1 : p ≤ 1) (hq0 : 0 ≤ q) (hq1 : q ≤ 1)
    (hpq : p ≤ q) (f : (B → Bool) → ℝ) (hf : Monotone f) :
    biasMaskMean p hp0 hp1 f ≤ biasMaskMean q hq0 hq1 f := by
  let e : B ≃ Fin (Fintype.card B) := Fintype.equivFin B
  rw [FriedgutRegev.biasMaskMean_reindex e, FriedgutRegev.biasMaskMean_reindex e]
  apply biasMaskMean_mono_bias p q hp0 hp1 hq0 hq1 hpq
  intro x y hxy
  apply hf
  intro b
  exact hxy (e b)

-- Source: Er579.MaskDensityIncrement:352
theorem biasResidualCorrelation_empty_reindex
    {B D : Type*} [Fintype B] [Fintype D] (e : B ≃ D)
    (q : ℝ) (hq0 : 0 ≤ q) (hqhalf : q ≤ 1 / 2) (f : (B → Bool) → ℝ) :
    biasResidualCorrelation q hq0 hqhalf ∅ (fun _ => false) f =
      biasResidualCorrelation q hq0 hqhalf ∅ (fun _ : D => false)
        (fun x => f (fun b => x (e b))) := by
  unfold biasResidualCorrelation biasResidualPairLaw
  simp only [Finset.notMem_empty, if_false]
  exact FriedgutRegev.pi_reindex_expect e
    (fun _ : B => biasMaskPairBitLaw q hq0 hqhalf)
    (fun σ => f (fun b => (σ b).1) * f (fun b => (σ b).2))

-- Source: Er579.MaskDensityIncrement:364
theorem biasBoolean_mass_lt_half_of_energy_lt_finite {B : Type*} [Fintype B]
    (q : ℝ) (hq0 : 0 ≤ q) (hqhalf : q ≤ 1 / 2) (hq1 : q ≤ 1)
    (hqtwofifths : q ≤ 2 / 5) (g : (B → Bool) → Bool)
    (henergy : biasResidualCorrelation q hq0 hqhalf ∅ (fun _ => false)
      (fun x => if g x then 1 else 0) < 1 / 12) :
    biasMaskMean q hq0 hq1 (fun x => if g x then 1 else 0) < 1 / 2 := by
  let e : B ≃ Fin (Fintype.card B) := Fintype.equivFin B
  rw [FriedgutRegev.biasMaskMean_reindex e]
  apply biasBoolean_mass_lt_half_of_energy_lt q hq0 hqhalf hq1 hqtwofifths
    (fun x => g (fun b => x (e b)))
  rw [biasResidualCorrelation_empty_reindex e] at henergy
  exact henergy

-- Source: Er579.MaskDensityIncrement:377
def maskBoolIndicator {B : Type*} (h : (B → Bool) → Bool) : (B → Bool) → ℝ :=
  fun x => if h x then 1 else 0

-- Source: Er579.MaskDensityIncrement:380
def maskThreshold {B : Type*} (τ : ℝ) (f : (B → Bool) → ℝ) : (B → Bool) → Bool :=
  fun x => if τ ≤ f x then true else false

-- Source: Er579.MaskDensityIncrement:383
theorem maskThreshold_monotone {B : Type*} (τ : ℝ)
    (f : (B → Bool) → ℝ) (hf : Monotone f) : Monotone (maskThreshold τ f) := by
  intro x y hxy
  by_cases hx : τ ≤ f x
  · have hy : τ ≤ f y := hx.trans (hf hxy)
    simp [maskThreshold, hx, hy]
  · simp [maskThreshold, hx]

-- Source: Er579.MaskDensityIncrement:391
theorem maskThreshold_scaled_indicator_le {B : Type*} (τ : ℝ) (_hτ0 : 0 ≤ τ)
    (f : (B → Bool) → ℝ) (hf : ∀ x, 0 ≤ f x) (x : B → Bool) :
    τ * maskBoolIndicator (maskThreshold τ f) x ≤ f x := by
  by_cases hx : τ ≤ f x
  · simp [maskBoolIndicator, maskThreshold, hx]
  · simp [maskBoolIndicator, maskThreshold, hx, hf x]

-- Source: Er579.MaskDensityIncrement:398
theorem biasThreshold_energy_le {B : Type*} [Fintype B]
    (q : ℝ) (hq0 : 0 ≤ q) (hqhalf : q ≤ 1 / 2)
    (τ : ℝ) (hτ0 : 0 ≤ τ) (f : (B → Bool) → ℝ) (hf : ∀ x, 0 ≤ f x) :
    τ ^ 2 * biasResidualCorrelation q hq0 hqhalf ∅ (fun _ => false)
      (maskBoolIndicator (maskThreshold τ f)) ≤
        biasResidualCorrelation q hq0 hqhalf ∅ (fun _ => false) f := by
  let p := biasResidualPairLaw q hq0 hqhalf (∅ : Finset B) (fun _ => false)
  have hpoint (σ : B → Bool × Bool) :
      τ ^ 2 * (maskBoolIndicator (maskThreshold τ f) (fun b => (σ b).1) *
        maskBoolIndicator (maskThreshold τ f) (fun b => (σ b).2)) ≤
        f (fun b => (σ b).1) * f (fun b => (σ b).2) := by
    have hx := maskThreshold_scaled_indicator_le τ hτ0 f hf (fun b => (σ b).1)
    have hy := maskThreshold_scaled_indicator_le τ hτ0 f hf (fun b => (σ b).2)
    have hz : 0 ≤ τ * maskBoolIndicator (maskThreshold τ f) (fun b => (σ b).2) := by
      apply mul_nonneg hτ0
      unfold maskBoolIndicator
      split_ifs <;> norm_num
    have hh := mul_le_mul hx hy hz (hf (fun b => (σ b).1))
    calc
      _ = (τ * maskBoolIndicator (maskThreshold τ f) (fun b => (σ b).1)) *
          (τ * maskBoolIndicator (maskThreshold τ f) (fun b => (σ b).2)) := by ring
      _ ≤ _ := hh
  have h := p.expect_mono hpoint
  rw [FiniteProbability.expect_const_mul] at h
  exact h

-- Source: Er579.MaskDensityIncrement:424
theorem biasIndicator_energy_approx_le {B : Type*} [Fintype B]
    (q : ℝ) (hq0 : 0 ≤ q) (hqhalf : q ≤ 1 / 2) (hq1 : q ≤ 1)
    (h g : (B → Bool) → Bool) :
    biasResidualCorrelation q hq0 hqhalf ∅ (fun _ => false) (maskBoolIndicator g) ≤
      biasResidualCorrelation q hq0 hqhalf ∅ (fun _ => false) (maskBoolIndicator h) +
        2 * biasMaskMean q hq0 hq1 (fun x => if h x ≠ g x then 1 else 0) := by
  let p := biasResidualPairLaw q hq0 hqhalf (∅ : Finset B) (fun _ => false)
  let D : (B → Bool) → ℝ := fun x => if h x ≠ g x then 1 else 0
  have hpoint (x y : B → Bool) :
      maskBoolIndicator g x * maskBoolIndicator g y ≤
        maskBoolIndicator h x * maskBoolIndicator h y + D x + D y := by
    cases hx : h x <;> cases hy : h y <;> cases gx : g x <;> cases gy : g y <;>
      norm_num [maskBoolIndicator, D, hx, hy, gx, gy]
  calc
    biasResidualCorrelation q hq0 hqhalf ∅ (fun _ => false) (maskBoolIndicator g) ≤
        p.expect (fun σ => maskBoolIndicator h (fun b => (σ b).1) *
          maskBoolIndicator h (fun b => (σ b).2) + D (fun b => (σ b).1) +
            D (fun b => (σ b).2)) := p.expect_mono (fun σ => hpoint _ _)
    _ = _ := by
      rw [FiniteProbability.expect_add, FiniteProbability.expect_add]
      change biasResidualCorrelation q hq0 hqhalf ∅ (fun _ => false) (maskBoolIndicator h) +
        (biasResidualPairLaw q hq0 hqhalf ∅ (fun _ => false)).expect
          (fun σ => D (fun b => (σ b).1)) +
        (biasResidualPairLaw q hq0 hqhalf ∅ (fun _ => false)).expect
          (fun σ => D (fun b => (σ b).2)) = _
      rw [biasResidualPair_fst_expect q hq0 hqhalf hq1,
        biasResidualPair_snd_expect q hq0 hqhalf hq1]
      change biasResidualCorrelation q hq0 hqhalf ∅ (fun _ => false) (maskBoolIndicator h) +
        biasConditionalMaskMean q hq0 hq1 ∅ (fun _ => false) D +
        biasConditionalMaskMean q hq0 hq1 ∅ (fun _ => false) D = _
      simp only [biasConditionalMaskMean_empty]
      ring

-- Source: Er579.MaskDensityIncrement:457
theorem biasThreshold_outside_le {B : Type*} [Fintype B]
    (q : ℝ) (hq0 : 0 ≤ q) (hq1 : q ≤ 1)
    (τ : ℝ) (hτ0 : 0 ≤ τ) (f : (B → Bool) → ℝ)
    (hf1 : ∀ x, f x ≤ 1) (g : (B → Bool) → Bool) :
    biasMaskMean q hq0 hq1 (fun x => if g x then 0 else f x) ≤
      τ + biasMaskMean q hq0 hq1
        (fun x => if maskThreshold τ f x ≠ g x then 1 else 0) := by
  let p : FiniteProbability (B → Bool) := biasMaskLaw q hq0 hq1
  have hpoint (x : B → Bool) :
      (if g x then (0 : ℝ) else f x) ≤
        τ + (if maskThreshold τ f x ≠ g x then 1 else 0) := by
    cases hg : g x
    · by_cases hx : τ ≤ f x
      · simp [maskThreshold, hx]
        linarith [hf1 x]
      · simp [maskThreshold, hx]
        exact (not_le.mp hx).le
    · simp
      split_ifs <;> linarith
  have hh := p.expect_mono hpoint
  rw [FiniteProbability.expect_add, FiniteProbability.expect_const] at hh
  exact hh

-- Source: Er579.MaskDensityIncrement:480
/-- A bounded-mass capturing set contains a positive-probability atom
whose conditional mean grows by at least four thirds.  We buy strict
slack below the available factor three halves. -/
theorem exists_density_increment_atom {A : Type*} [Fintype A]
    (w : A → ℝ) (hw : ∀ a, 0 ≤ w a) (T : Finset A) (g : A → ℝ)
    (s : ℝ) (hs : 0 < s)
    (hsmall : ∑ a ∈ T, w a ≤ 1 / 2)
    (hinside : 3 * s / 4 ≤ ∑ a ∈ T, w a * g a) :
    ∃ a ∈ T, 0 < w a ∧ (4 / 3 : ℝ) * s ≤ g a := by
  classical
  by_contra h
  push Not at h
  have hsum : (∑ a ∈ T, w a * g a) ≤
      ((4 / 3 : ℝ) * s) * ∑ a ∈ T, w a := by
    rw [Finset.mul_sum]
    apply Finset.sum_le_sum
    intro a ha
    by_cases hwa : w a = 0
    · simp [hwa]
    · have hpos : 0 < w a := lt_of_le_of_ne (hw a) (Ne.symm hwa)
      have hg : g a < (4 / 3 : ℝ) * s := h a ha hpos
      simpa only [mul_comm] using mul_le_mul_of_nonneg_left hg.le (hw a)
  have hbound : ((4 / 3 : ℝ) * s) * ∑ a ∈ T, w a ≤
      ((4 / 3 : ℝ) * s) * (1 / 2) :=
    mul_le_mul_of_nonneg_left hsmall (by positivity)
  linarith

-- Source: Er579.MaskDensityIncrement:550
theorem biasMaskMean_inside_add_outside {B : Type*} [Fintype B]
    (q : ℝ) (hq0 : 0 ≤ q) (hq1 : q ≤ 1)
    (g : (B → Bool) → Bool) (f : (B → Bool) → ℝ) :
    biasMaskMean q hq0 hq1 (fun x => if g x then f x else 0) +
      biasMaskMean q hq0 hq1 (fun x => if g x then 0 else f x) =
        biasMaskMean q hq0 hq1 f := by
  unfold biasMaskMean
  rw [← FiniteProbability.expect_add]
  apply congrArg (FiniteProbability.expect _)
  funext x
  cases g x <;> simp

-- Source: Er579.MaskDensityIncrement:562
/-- One genuine density-increment step, using only the proved higher-bias
junta approximation and the finite spectral half-mass barrier. -/
theorem exists_mask_density_increment {B : Type*} [Fintype B]
    (p a b ε : ℝ) (hp0 : 0 ≤ p) (hp1 : p ≤ 1)
    (ha0 : 0 ≤ a) (hab : a < b) (hb : b ≤ 2 / 5) (hpa : p ≤ a)
    (hε : 0 < ε) (f : (B → Bool) → ℝ)
    (hf : ∀ γ, 0 ≤ f γ ∧ f γ ≤ 1) (hmono : Monotone f)
    (hmean : ε ≤ biasMaskMean p hp0 hp1 f)
    (hsmall : ∀ (q : ℝ) (hq0 : 0 ≤ q) (hqhalf : q ≤ 1 / 2), a < q → q < b →
      biasResidualCorrelation q hq0 hqhalf ∅ (fun _ => false) f <
        (ε / 8) ^ 2 / 96) :
    ∃ (q : ℝ) (hq0 : 0 ≤ q) (hq1 : q ≤ 1), a < q ∧ q < b ∧
      ∃ (K : Finset B) (w : B → Bool),
        K.card ≤ FriedgutRegev.uniformJuntaBound (4 / (b - a))
          (min (ε / 8) (1 / 192) / 2) ∧
        (4 / 3 : ℝ) * biasMaskMean p hp0 hp1 f ≤
          biasConditionalMaskMean q hq0 hq1 K w f := by
  let τ : ℝ := ε / 8
  let e : ℝ := min (ε / 8) (1 / 192)
  let h := maskThreshold τ f
  have hτ : 0 < τ := by dsimp [τ]; positivity
  have he : 0 < e := by dsimp [e]; exact lt_min (by positivity) (by norm_num)
  have heε : e ≤ ε / 8 := min_le_left _ _
  have hec : e ≤ 1 / 192 := min_le_right _ _
  obtain ⟨q, hq0, hq1, haq, hqb, K, g, hK, hg, herr⟩ :=
    FriedgutRegev.higher_bias_junta_finite h (maskThreshold_monotone τ f hmono)
      a b e ha0 hab (by linarith) he
  have hqhalf : q ≤ 1 / 2 := by linarith
  have hqcap : q ≤ 2 / 5 := hqb.le.trans hb
  have hqenergy := hsmall q hq0 hqhalf haq hqb
  have hscaled := biasThreshold_energy_le q hq0 hqhalf τ hτ.le f (fun γ => (hf γ).1)
  have hhenergy : biasResidualCorrelation q hq0 hqhalf ∅ (fun _ => false)
      (maskBoolIndicator h) < 1 / 96 := by
    have hτsq : 0 < τ ^ 2 := sq_pos_of_pos hτ
    change τ ^ 2 * biasResidualCorrelation q hq0 hqhalf ∅ (fun _ => false)
      (maskBoolIndicator h) ≤ _ at hscaled
    change biasResidualCorrelation q hq0 hqhalf ∅ (fun _ => false) f < τ ^ 2 / 96 at hqenergy
    by_contra hh
    have hh' : (1 / 96 : ℝ) ≤ biasResidualCorrelation q hq0 hqhalf ∅ (fun _ => false)
        (maskBoolIndicator h) := le_of_not_gt hh
    have hm := mul_le_mul_of_nonneg_left hh' hτsq.le
    nlinarith
  have hgenergy : biasResidualCorrelation q hq0 hqhalf ∅ (fun _ => false)
      (maskBoolIndicator g) < 1 / 12 := by
    have happrox := biasIndicator_energy_approx_le q hq0 hqhalf hq1 h g
    linarith
  have hmass : biasMaskMean q hq0 hq1 (maskBoolIndicator g) < 1 / 2 :=
    biasBoolean_mass_lt_half_of_energy_lt_finite q hq0 hqhalf hq1 hqcap g hgenergy
  have hout : biasMaskMean q hq0 hq1 (fun x => if g x then 0 else f x) ≤ ε / 4 := by
    have hh := biasThreshold_outside_le q hq0 hq1 τ hτ.le f (fun γ => (hf γ).2) g
    change biasMaskMean q hq0 hq1 (fun x => if g x then 0 else f x) ≤
      τ + biasMaskMean q hq0 hq1 (fun x => if h x ≠ g x then 1 else 0) at hh
    dsimp [τ] at hh
    linarith
  have hraise : biasMaskMean p hp0 hp1 f ≤ biasMaskMean q hq0 hq1 f :=
    biasMaskMean_mono_bias_finite p q hp0 hp1 hq0 hq1 (hpa.trans haq.le) f hmono
  have hinside : 3 * biasMaskMean p hp0 hp1 f / 4 ≤
      biasMaskMean q hq0 hq1 (fun x => if g x then f x else 0) := by
    have hsplit := biasMaskMean_inside_add_outside q hq0 hq1 g f
    linarith
  unfold maskBoolIndicator at hmass
  rw [biasMaskMean_junta_mass_eq_sum_atoms q hq0 hq1 K g hg] at hmass
  rw [biasMaskMean_junta_inside_eq_sum_atoms q hq0 hq1 K g hg f] at hinside
  obtain ⟨u, _, _, hu⟩ := exists_density_increment_atom
    (maskAtomWeight q K) (maskAtomWeight_nonneg q hq0 hq1 K)
    (maskCapturingAtoms K g)
    (fun u => biasConditionalMaskMean q hq0 hq1 K (extendMaskAtom K u) f)
    (biasMaskMean p hp0 hp1 f) (hε.trans_le hmean) hmass.le hinside
  exact ⟨q, hq0, hq1, haq, hqb, K, extendMaskAtom K u, hK, hu⟩

-- Source: Er579.MaskDensityIncrement:632
/-- Every positive-density monotone mask function has positive residual
correlation after fixing a bounded number of coordinates. The bias and
coordinate bounds are uniform in the dimension. -/
theorem monotone_bounded_mask_correlation
    (ε : ℝ) (hε : 0 < ε) (hε1 : ε ≤ 1) :
    ∃ (R : ℕ) (d : ℝ), 0 < d ∧
      ∀ (B : Type*) (_ : Fintype B) (f : (B → Bool) → ℝ),
        (∀ γ, 0 ≤ f γ ∧ f γ ≤ 1) → Monotone f → ε ≤ maskMean f →
        ∃ (q : ℝ) (hq0 : 0 ≤ q) (hqhalf : q ≤ 1 / 2),
          1 / 4 ≤ q ∧ q ≤ 2 / 5 ∧
          ∃ (J : Finset B) (z : B → Bool),
            J.card ≤ R ∧ d ≤ biasResidualCorrelation q hq0 hqhalf J z f := by
  obtain ⟨L, hLpow⟩ := pow_unbounded_of_one_lt (1 / ε) (show (1 : ℝ) < 4 / 3 by norm_num)
  have hL : 1 < (4 / 3 : ℝ) ^ L * ε := (div_lt_iff₀ hε).mp hLpow
  have hLpos : 0 < L := by
    by_contra hn
    have hzero : L = 0 := Nat.eq_zero_of_not_pos hn
    rw [hzero] at hL
    norm_num at hL
    linarith
  have hLreal : 0 < (L : ℝ) := by exact_mod_cast hLpos
  let v : ℝ := (3 / 20) / (L : ℝ)
  have hv : 0 < v := by dsimp [v]; positivity
  have hLv : (L : ℝ) * v = 3 / 20 := by
    dsimp [v]
    field_simp [ne_of_gt hLreal]
  let endpoint : ℕ → ℝ := fun i => 1 / 4 + (i : ℝ) * v
  have hezero : endpoint 0 = 1 / 4 := by simp [endpoint]
  have heL : endpoint L = 2 / 5 := by dsimp [endpoint]; rw [hLv]; norm_num
  have henext (i : ℕ) : endpoint (i + 1) = endpoint i + v := by
    simp only [endpoint, Nat.cast_add, Nat.cast_one]
    ring
  have hequarter (i : ℕ) : 1 / 4 ≤ endpoint i := by
    dsimp [endpoint]
    linarith [mul_nonneg (Nat.cast_nonneg (α := ℝ) i) hv.le]
  have heupper (i : ℕ) (hi : i ≤ L) : endpoint i ≤ 2 / 5 := by
    have hi' : (i : ℝ) ≤ (L : ℝ) := by exact_mod_cast hi
    have hh := mul_le_mul_of_nonneg_right hi' hv.le
    dsimp [endpoint]
    rw [hLv] at hh
    linarith
  let K : ℕ := FriedgutRegev.uniformJuntaBound (4 / v) (min (ε / 8) (1 / 192) / 2)
  let d : ℝ := (ε / 8) ^ 2 / 96
  have hd : 0 < d := by dsimp [d]; positivity
  refine ⟨L * K, d, hd, ?_⟩
  intro B _ f hf hmono hmean
  by_contra hcert
  have hnone (q : ℝ) (hq0 : 0 ≤ q) (hqhalf : q ≤ 1 / 2)
      (hqlo : 1 / 4 ≤ q) (hqhi : q ≤ 2 / 5)
      (J : Finset B) (z : B → Bool) (hJ : J.card ≤ L * K) :
      biasResidualCorrelation q hq0 hqhalf J z f < d := by
    by_contra h
    exact hcert ⟨q, hq0, hqhalf, hqlo, hqhi, J, z, hJ, le_of_not_gt h⟩
  have hreach : ∀ i : ℕ, i ≤ L →
      ∃ (J : Finset B) (z : B → Bool) (q : ℝ) (hq0 : 0 ≤ q) (hq1 : q ≤ 1),
        J.card ≤ i * K ∧ 1 / 4 ≤ q ∧ q ≤ endpoint i ∧
        (4 / 3 : ℝ) ^ i * ε ≤ biasConditionalMaskMean q hq0 hq1 J z f := by
    intro i
    induction i with
    | zero =>
        intro _
        refine ⟨∅, (fun _ => false), 1 / 4, by norm_num, by norm_num,
          by simp, le_rfl, ?_, ?_⟩
        · rw [hezero]
        · rw [biasConditionalMaskMean_empty]
          simpa only [pow_zero, one_mul, maskMean, maskLaw_eq_biasMaskLaw, biasMaskMean] using hmean
    | succ i ih =>
        intro hi
        have hiL : i ≤ L := Nat.le_trans (Nat.le_succ i) hi
        obtain ⟨J, z, p, hp0, hp1, hJ, hplo, hpupper, hvalue⟩ := ih hiL
        let F : (B → Bool) → ℝ := fun γ => f (overwriteMask J z γ)
        have hF : ∀ γ, 0 ≤ F γ ∧ F γ ≤ 1 := fun γ => hf (overwriteMask J z γ)
        have hFmono : Monotone F := hmono.comp (overwriteMask_monotone J z)
        have hepspow : ε ≤ (4 / 3 : ℝ) ^ i * ε := by
          simpa only [one_mul] using mul_le_mul_of_nonneg_right
            (one_le_pow₀ (show (1 : ℝ) ≤ 4 / 3 by norm_num)) hε.le
        have hFmean : ε ≤ biasMaskMean p hp0 hp1 F := by
          rw [← biasConditionalMaskMean_eq_overwrite p hp0 hp1 J z f]
          exact hepspow.trans hvalue
        have hinc : endpoint i < endpoint (i + 1) := by rw [henext]; linarith
        have hsmall (q : ℝ) (hq0 : 0 ≤ q) (hqhalf : q ≤ 1 / 2)
            (hqleft : endpoint i < q) (hqright : q < endpoint (i + 1)) :
            biasResidualCorrelation q hq0 hqhalf ∅ (fun _ => false) F <
              (ε / 8) ^ 2 / 96 := by
          rw [biasResidualCorrelation_empty_overwrite q hq0 hqhalf J z f]
          exact hnone q hq0 hqhalf ((hequarter i).trans hqleft.le)
            (hqright.le.trans (heupper (i + 1) hi)) J z
            (hJ.trans (Nat.mul_le_mul_right K hiL))
        obtain ⟨q, hq0, hq1, hqleft, hqright, S, w, hS, hgain⟩ :=
          exists_mask_density_increment p (endpoint i) (endpoint (i + 1)) ε hp0 hp1
            (by linarith [hequarter i]) hinc (heupper (i + 1) hi) hpupper hε F
            hF hFmono hFmean hsmall
        have hwidth : endpoint (i + 1) - endpoint i = v := by rw [henext]; ring
        rw [hwidth] at hS
        change S.card ≤ K at hS
        refine ⟨J ∪ S, oldPriorityPattern J z w, q, hq0, hq1, ?_,
          (hequarter i).trans hqleft.le, hqright.le, ?_⟩
        · calc
            (J ∪ S).card ≤ J.card + S.card := Finset.card_union_le J S
            _ ≤ i * K + K := Nat.add_le_add hJ hS
            _ = (i + 1) * K := by rw [Nat.add_mul, Nat.one_mul]
        · rw [← biasConditionalMaskMean_overwrite q hq0 hq1 J S z w f]
          change (4 / 3 : ℝ) ^ (i + 1) * ε ≤ biasConditionalMaskMean q hq0 hq1 S w F
          have hv' : (4 / 3 : ℝ) ^ i * ε ≤ biasMaskMean p hp0 hp1 F := by
            rw [← biasConditionalMaskMean_eq_overwrite p hp0 hp1 J z f]
            exact hvalue
          calc
            (4 / 3 : ℝ) ^ (i + 1) * ε = (4 / 3) * ((4 / 3) ^ i * ε) := by rw [pow_succ]; ring
            _ ≤ (4 / 3) * biasMaskMean p hp0 hp1 F :=
              mul_le_mul_of_nonneg_left hv' (by norm_num)
            _ ≤ biasConditionalMaskMean q hq0 hq1 S w F := hgain
  obtain ⟨J, z, q, hq0, hq1, _, _, _, hvalue⟩ := hreach L le_rfl
  have hupper : biasConditionalMaskMean q hq0 hq1 J z f ≤ 1 := by
    unfold biasConditionalMaskMean
    simpa only [FiniteProbability.expect_const] using
      (biasConditionalMaskLaw q hq0 hq1 J z).expect_mono (fun γ => (hf γ).2)
  exact (not_lt_of_ge (hvalue.trans hupper)) hL

end

end Er579

end

/- Source fragment: Er579.MaskedCompatibility. Original licenses and source proofs retained. -/

section

/-!
The finite masked compatibility graph and its counting obstruction.
The coefficient-separated counting bound is combined with the proved
monotone residual-correlation theorem at the end of this module.
-/

namespace Er579

open scoped BigOperators Classical

variable {P B : Type*}

noncomputable section

-- Source: Er579.MaskedCompatibility:18
/-- A coefficient profile thinned by a Boolean row mask. -/
def maskedCross (C : P → B → Prop) (q : P × (B → Bool)) (b : B) : Prop :=
  C q.1 b ∧ q.2 b = true

-- Source: Er579.MaskedCompatibility:22
/-- The ordered five-cross-edge obstruction over a distinct-leaf B star. -/
def fiveCellPattern (HB : SimpleGraph B) (M : (P × (B → Bool)) → B → Prop)
    (q q' : P × (B → Bool)) : Prop :=
  ∃ b w z, HB.Adj b w ∧ HB.Adj b z ∧ w ≠ z ∧
    M q w ∧ M q z ∧ M q' b ∧ M q' w ∧ M q' z

-- Source: Er579.MaskedCompatibility:28
/-- Distinct profiles are adjacent exactly when both five-cell orientations
are excluded.  This graph is simple; its diagonal is not suppressed in
subsequent probability estimates. -/
def maskedCompatibilityGraph (HB : SimpleGraph B) (C : P → B → Prop) :
    SimpleGraph (P × (B → Bool)) where
  Adj q q' := q ≠ q' ∧
    ¬ fiveCellPattern HB (maskedCross C) q q' ∧
    ¬ fiveCellPattern HB (maskedCross C) q' q
  symm := ⟨by
    intro q q' h
    exact ⟨h.1.symm, h.2.2, h.2.1⟩⟩
  loopless := ⟨by
    intro q h
    exact h.1 rfl⟩

-- Source: Er579.MaskedCompatibility:43
/-- Interface used by the ordinary-graph octahedron exclusion. -/
theorem maskedCompatibility_excludes (HB : SimpleGraph B) (C : P → B → Prop)
    {q q' : P × (B → Bool)} (h : (maskedCompatibilityGraph HB C).Adj q q')
    {b w z : B} (hbw : HB.Adj b w) (hbz : HB.Adj b z) (hwz : w ≠ z) :
    ¬ (maskedCross C q w ∧ maskedCross C q z ∧ maskedCross C q' b ∧
      maskedCross C q' w ∧ maskedCross C q' z) := by
  intro hp
  exact h.2.1 ⟨b, w, z, hbw, hbz, hwz, hp⟩

-- Source: Er579.MaskedCompatibility:52
/-- This weaker property ignores pairs having the same coefficient.
It is enough because their entire probability is charged to the diagonal. -/
def CoefficientSeparatedIncompatible (HB : SimpleGraph B) (C : P → B → Prop)
    (F : Set (P × (B → Bool))) : Prop :=
  ∀ q ∈ F, ∀ q' ∈ F, q.1 ≠ q'.1 →
    fiveCellPattern HB (maskedCross C) q q' ∨ fiveCellPattern HB (maskedCross C) q' q

-- Source: Er579.MaskedCompatibility:59
theorem independent_coefficientSeparatedIncompatible
    (HB : SimpleGraph B) (C : P → B → Prop) (F : Set (P × (B → Bool)))
    (hF : (maskedCompatibilityGraph HB C).IsIndepSet F) :
    CoefficientSeparatedIncompatible HB C F := by
  intro q hq q' hq' haa
  have hqq : q ≠ q' := by
    intro h
    exact haa (congrArg Prod.fst h)
  have hn := hF hq hq' hqq
  by_contra h
  exact hn ⟨hqq, (not_or.mp h).1, (not_or.mp h).2⟩

-- Source: Er579.MaskedCompatibility:71
def MaskExtends (γ γ' : B → Bool) : Prop := ∀ b, γ b = true → γ' b = true

-- Source: Er579.MaskedCompatibility:73
/-- Coefficientwise upward closure does not claim ordinary graph
independence for pairs derived from one original coefficient. -/
def maskUpwardClosure (F : Set (P × (B → Bool))) : Set (P × (B → Bool)) :=
  {q | ∃ γ, (q.1, γ) ∈ F ∧ MaskExtends γ q.2}

-- Source: Er579.MaskedCompatibility:78
theorem subset_maskUpwardClosure (F : Set (P × (B → Bool))) :
    F ⊆ maskUpwardClosure F := by
  intro q hq
  exact ⟨q.2, hq, fun _ h => h⟩

-- Source: Er579.MaskedCompatibility:83
theorem maskUpwardClosure_monotone (F : Set (P × (B → Bool))) (a : P)
    {γ γ' : B → Bool} (h : MaskExtends γ γ')
    (hγ : (a, γ) ∈ maskUpwardClosure F) : (a, γ') ∈ maskUpwardClosure F := by
  obtain ⟨γ₀, hγ₀, h₀⟩ := hγ
  exact ⟨γ₀, hγ₀, fun b hb => h b (h₀ b hb)⟩

-- Source: Er579.MaskedCompatibility:89
theorem fiveCellPattern_mono (HB : SimpleGraph B) (C : P → B → Prop)
    (a a' : P) {γ₀ γ γ'₀ γ' : B → Bool}
    (hγ : MaskExtends γ₀ γ) (hγ' : MaskExtends γ'₀ γ')
    (hp : fiveCellPattern HB (maskedCross C) (a, γ₀) (a', γ'₀)) :
    fiveCellPattern HB (maskedCross C) (a, γ) (a', γ') := by
  obtain ⟨b, w, z, hbw, hbz, hwz, hqw, hqz, hq'b, hq'w, hq'z⟩ := hp
  exact ⟨b, w, z, hbw, hbz, hwz, ⟨hqw.1, hγ w hqw.2⟩,
    ⟨hqz.1, hγ z hqz.2⟩, ⟨hq'b.1, hγ' b hq'b.2⟩,
    ⟨hq'w.1, hγ' w hq'w.2⟩, ⟨hq'z.1, hγ' z hq'z.2⟩⟩

-- Source: Er579.MaskedCompatibility:99
theorem coefficientSeparatedIncompatible_upward
    (HB : SimpleGraph B) (C : P → B → Prop) (F : Set (P × (B → Bool)))
    (hF : CoefficientSeparatedIncompatible HB C F) :
    CoefficientSeparatedIncompatible HB C (maskUpwardClosure F) := by
  intro q hq q' hq' haa
  obtain ⟨γ, hγ, hext⟩ := hq
  obtain ⟨γ', hγ', hext'⟩ := hq'
  rcases hF (q.1, γ) hγ (q'.1, γ') hγ' haa with h | h
  · exact Or.inl (fiveCellPattern_mono HB C _ _ hext hext' h)
  · exact Or.inr (fiveCellPattern_mono HB C _ _ hext' hext h)

-- Source: Er579.MaskedCompatibility:110
/-- A coefficient sees every vertex of a B star. -/
def coefficientStar (C : P → B → Prop) (a : P) (b w z : B) : Prop :=
  C a b ∧ C a w ∧ C a z

-- Source: Er579.MaskedCompatibility:114
/-- A surviving incompatibility witness has both leaves among the fixed
coordinates, while its center may lie anywhere in B. -/
def fixedLeafStarWitness (HB : SimpleGraph B) (C : P → B → Prop)
    [Fintype B] (J : Finset B) (a a' : P) : Prop :=
  ∃ b w z, HB.Adj b w ∧ HB.Adj b z ∧ w ≠ z ∧ w ∈ J ∧ z ∈ J ∧
    (coefficientStar C a b w z ∨ coefficientStar C a' b w z)

-- Source: Er579.MaskedCompatibility:121
theorem separated_masked_pair_diagonal_or_witness [Fintype B]
    (HB : SimpleGraph B) (C : P → B → Prop) (F : Set (P × (B → Bool)))
    (hF : CoefficientSeparatedIncompatible HB C F)
    (J : Finset B) (a a' : P) (γ γ' : B → Bool)
    (hγ : ∀ b, γ b = true → γ' b = true → b ∈ J)
    (hq : (a, γ) ∈ F) (hq' : (a', γ') ∈ F) :
    a = a' ∨ fixedLeafStarWitness HB C J a a' := by
  classical
  by_cases haa : a = a'
  · exact Or.inl haa
  right
  have hp : fiveCellPattern HB (maskedCross C) (a, γ) (a', γ') ∨
      fiveCellPattern HB (maskedCross C) (a', γ') (a, γ) :=
    hF (a, γ) hq (a', γ') hq' haa
  rcases hp with hp | hp
  · rcases hp with ⟨b, w, z, hbw, hbz, hwz, hqw, hqz, hq'b, hq'w, hq'z⟩
    exact ⟨b, w, z, hbw, hbz, hwz, hγ w hqw.2 hq'w.2,
      hγ z hqz.2 hq'z.2, Or.inr ⟨hq'b.1, hq'w.1, hq'z.1⟩⟩
  · rcases hp with ⟨b, w, z, hbw, hbz, hwz, hq'w, hq'z, hqb, hqw, hqz⟩
    exact ⟨b, w, z, hbw, hbz, hwz, hγ w hqw.2 hq'w.2,
      hγ z hqz.2 hq'z.2, Or.inl ⟨hqb.1, hqw.1, hqz.1⟩⟩

section FiniteCoefficients

variable [Fintype P] [Fintype B]

-- Source: Er579.MaskedCompatibility:169
/-- The coefficient-average membership function is fractional. -/
noncomputable def profileFraction (ν : FiniteProbability P)
    (F : Set (P × (B → Bool))) (γ : B → Bool) : ℝ :=
  ν.event (fun a => (a, γ) ∈ F)

omit [Fintype B] in

-- Source: Er579.MaskedCompatibility:175
theorem profileFraction_mem_Icc (ν : FiniteProbability P)
    (F : Set (P × (B → Bool))) (γ : B → Bool) :
    0 ≤ profileFraction ν F γ ∧ profileFraction ν F γ ≤ 1 :=
  ⟨ν.event_nonneg _, ν.event_le_one _⟩

omit [Fintype B] in

-- Source: Er579.MaskedCompatibility:181
theorem profileFraction_upward_monotone (ν : FiniteProbability P)
    (F : Set (P × (B → Bool))) {γ γ' : B → Bool} (h : MaskExtends γ γ') :
    profileFraction ν (maskUpwardClosure F) γ ≤
      profileFraction ν (maskUpwardClosure F) γ' := by
  apply FiniteProbability.event_mono
  intro a ha
  exact maskUpwardClosure_monotone F a h ha

omit [Fintype B] in

-- Source: Er579.MaskedCompatibility:190
theorem profileFraction_upward_monotone_order (ν : FiniteProbability P)
    (F : Set (P × (B → Bool))) : Monotone (profileFraction ν (maskUpwardClosure F)) := by
  intro γ γ' hγ
  apply profileFraction_upward_monotone ν F
  intro b hb
  have hbb : true ≤ γ' b := by simpa only [hb] using hγ b
  cases h' : γ' b with
  | false =>
      have hbad : ¬ ((true : Bool) ≤ false) := by decide
      exact False.elim (hbad (by simpa only [h'] using hbb))
  | true => rfl

-- Source: Er579.MaskedCompatibility:202
/-- Weighted mass of a family of masked profiles. -/
noncomputable def maskedProfileMass (ν : FiniteProbability P)
    (F : Set (P × (B → Bool))) : ℝ :=
  maskMean (profileFraction ν F)

-- Source: Er579.MaskedCompatibility:207
theorem maskedProfileMass_le_upward_mean (ν : FiniteProbability P)
    (F : Set (P × (B → Bool))) :
    maskedProfileMass ν F ≤ maskMean (profileFraction ν (maskUpwardClosure F)) := by
  apply FiniteProbability.expect_mono
  intro γ
  apply FiniteProbability.event_mono
  intro a ha
  exact subset_maskUpwardClosure F ha

-- Source: Er579.MaskedCompatibility:216
/-- The actual independent product profile law. -/
def maskedProfileLaw (ν : FiniteProbability P) : FiniteProbability (P × (B → Bool)) :=
  ν.prod maskLaw

-- Source: Er579.MaskedCompatibility:234
def pairLeftProfile (x : (P × P) × (B → Bool × Bool)) : P × (B → Bool) :=
  (x.1.1, fun b => (x.2 b).1)

-- Source: Er579.MaskedCompatibility:237
def pairRightProfile (x : (P × P) × (B → Bool × Bool)) : P × (B → Bool) :=
  (x.1.2, fun b => (x.2 b).2)

-- Source: Er579.MaskedCompatibility:240
/-- Independent coefficient sampling commutes with an arbitrary paired-mask
law. In particular no coefficient is conditioned on family membership. -/
theorem pairedFraction_eq_pair_membership (ν : FiniteProbability P)
    (F : Set (P × (B → Bool))) (joint : FiniteProbability (B → Bool × Bool)) :
    joint.expect (fun σ => profileFraction ν F (fun b => (σ b).1) *
      profileFraction ν F (fun b => (σ b).2)) =
      ((ν.prod ν).prod joint).event (fun x =>
        pairLeftProfile x ∈ F ∧ pairRightProfile x ∈ F) := by
  classical
  rw [FiniteProbability.event_eq_expect_indicator, FiniteProbability.prod_expect_right]
  congr 1
  funext σ
  unfold profileFraction pairLeftProfile pairRightProfile
  rw [← FiniteProbability.prod_event_and]
  exact FiniteProbability.event_eq_expect_indicator (ν.prod ν)
    (fun a => (a.1, fun b => (σ b).1) ∈ F ∧
      (a.2, fun b => (σ b).2) ∈ F)

-- Source: Er579.MaskedCompatibility:265
theorem coefficient_diagonal_le (ν : FiniteProbability P) (ω : ℝ)
    (hω : ∀ a, ν.weight a ≤ ω) :
    (ν.prod ν).event (fun a => a.1 = a.2) ≤ ω := by
  classical
  have heq : (ν.prod ν).event (fun a => a.1 = a.2) =
      ∑ a, ν.weight a * ν.weight a := by
    simp [FiniteProbability.event, RandomRealization.eventWeight,
      FiniteProbability.prod, Fintype.sum_prod_type]
  rw [heq]
  calc
    (∑ a, ν.weight a * ν.weight a) ≤ ∑ a, ω * ν.weight a := by
      apply Finset.sum_le_sum
      intro a _
      exact mul_le_mul_of_nonneg_right (hω a) (ν.nonneg a)
    _ = ω := by rw [← Finset.mul_sum, ν.sum_one, mul_one]

omit [Fintype B] in

-- Source: Er579.MaskedCompatibility:282
theorem coefficient_star_pair_le (ν : FiniteProbability P) (C : P → B → Prop)
    (b w z : B) (η : ℝ)
    (hη : ν.event (fun a => coefficientStar C a b w z) ≤ η) :
    (ν.prod ν).event (fun a =>
      coefficientStar C a.1 b w z ∨ coefficientStar C a.2 b w z) ≤ 2 * η := by
  have h := (ν.prod ν).event_or_le
    (fun a => coefficientStar C a.1 b w z)
    (fun a => coefficientStar C a.2 b w z)
  rw [FiniteProbability.prod_event_fst ν ν (fun a => coefficientStar C a b w z),
    FiniteProbability.prod_event_snd ν ν (fun a => coefficientStar C a b w z)] at h
  linarith

end FiniteCoefficients

section StarCount

variable [Fintype B]

-- Source: Er579.MaskedCompatibility:300
def commonStarCenters (HB : SimpleGraph B) (w z : B) : Finset B := by
  classical
  exact Finset.univ.filter (fun b => HB.Adj b w ∧ HB.Adj b z)

-- Source: Er579.MaskedCompatibility:304
def fixedLeafStars (HB : SimpleGraph B) (J : Finset B) : Finset (B × B × B) := by
  classical
  exact (J.product J).biUnion (fun wz =>
    if wz.1 ≠ wz.2 then
      (commonStarCenters HB wz.1 wz.2).image (fun b => (b, wz.1, wz.2))
    else ∅)

-- Source: Er579.MaskedCompatibility:311
theorem mem_fixedLeafStars_iff (HB : SimpleGraph B) (J : Finset B) (t : B × B × B) :
    t ∈ fixedLeafStars HB J ↔ HB.Adj t.1 t.2.1 ∧ HB.Adj t.1 t.2.2 ∧
      t.2.1 ≠ t.2.2 ∧ t.2.1 ∈ J ∧ t.2.2 ∈ J := by
  classical
  constructor
  · intro ht
    obtain ⟨wz, hwzJ, ht⟩ := Finset.mem_biUnion.mp ht
    by_cases hwz : wz.1 ≠ wz.2
    · rw [if_pos hwz] at ht
      obtain ⟨b, hb, rfl⟩ := Finset.mem_image.mp ht
      have hb' : HB.Adj b wz.1 ∧ HB.Adj b wz.2 := by
        simpa [commonStarCenters] using hb
      exact ⟨hb'.1, hb'.2, hwz, (Finset.mem_product.mp hwzJ).1,
        (Finset.mem_product.mp hwzJ).2⟩
    · rw [if_neg hwz] at ht
      simp at ht
  · rintro ⟨hbw, hbz, hwz, hw, hz⟩
    apply Finset.mem_biUnion.mpr
    refine ⟨(t.2.1, t.2.2), Finset.mem_product.mpr ⟨hw, hz⟩, ?_⟩
    rw [if_pos hwz]
    exact Finset.mem_image.mpr ⟨t.1, by simp [commonStarCenters, hbw, hbz], rfl⟩

-- Source: Er579.MaskedCompatibility:333
/-- Ordered leaf pairs give the harmless bound kappa times |J| squared.+Centers outside J are included. -/
theorem fixedLeafStars_card_le (HB : SimpleGraph B) (J : Finset B) (κ : ℕ)
    (hκ : ∀ w z, w ≠ z → (commonStarCenters HB w z).card ≤ κ) :
    (fixedLeafStars HB J).card ≤ J.card ^ 2 * κ := by
  classical
  unfold fixedLeafStars
  calc
    ((J.product J).biUnion (fun wz => if wz.1 ≠ wz.2 then
        (commonStarCenters HB wz.1 wz.2).image (fun b => (b, wz.1, wz.2))
        else ∅)).card ≤
      ∑ wz ∈ J.product J, (if wz.1 ≠ wz.2 then
        (commonStarCenters HB wz.1 wz.2).image (fun b => (b, wz.1, wz.2))
        else ∅).card := Finset.card_biUnion_le
    _ ≤ ∑ _wz ∈ J.product J, κ := by
      apply Finset.sum_le_sum
      intro wz _
      by_cases hwz : wz.1 ≠ wz.2
      · rw [if_pos hwz]
        exact Finset.card_image_le.trans (hκ _ _ hwz)
      · simp [hwz]
    _ = J.card ^ 2 * κ := by simp [Finset.card_product, pow_two]

-- Source: Er579.MaskedCompatibility:355
theorem fixedLeafStarWitness_iff (HB : SimpleGraph B) (C : P → B → Prop)
    (J : Finset B) (a a' : P) :
    fixedLeafStarWitness HB C J a a' ↔
      ∃ t ∈ fixedLeafStars HB J,
        coefficientStar C a t.1 t.2.1 t.2.2 ∨ coefficientStar C a' t.1 t.2.1 t.2.2 := by
  constructor
  · rintro ⟨b, w, z, hbw, hbz, hwz, hw, hz, hc⟩
    exact ⟨(b, w, z), (mem_fixedLeafStars_iff HB J _).mpr ⟨hbw, hbz, hwz, hw, hz⟩, hc⟩
  · rintro ⟨t, ht, hc⟩
    rcases (mem_fixedLeafStars_iff HB J t).mp ht with ⟨hbw, hbz, hwz, hw, hz⟩
    exact ⟨t.1, t.2.1, t.2.2, hbw, hbz, hwz, hw, hz, hc⟩

end StarCount

section QuantitativeBound

variable [Fintype P] [Fintype B]

-- Source: Er579.MaskedCompatibility:373
/-- Finite mask/count estimate, including the coefficient diagonal.  The
weaker ordered-pair bound replaces binomial(|J|,2) by |J| squared. -/
theorem separated_masked_pairedFraction_le
    (ν : FiniteProbability P) (HB : SimpleGraph B) (C : P → B → Prop)
    (F : Set (P × (B → Bool)))
    (hF : CoefficientSeparatedIncompatible HB C F)
    (J : Finset B) (joint : FiniteProbability (B → Bool × Bool))
    (hjoint : ∀ σ, joint.weight σ ≠ 0 → ∀ b,
      (σ b).1 = true → (σ b).2 = true → b ∈ J)
    (κ : ℕ) (ω η : ℝ)
    (hω : ∀ a, ν.weight a ≤ ω) (hη0 : 0 ≤ η)
    (hκ : ∀ w z, w ≠ z → (commonStarCenters HB w z).card ≤ κ)
    (hstar : ∀ b w z, HB.Adj b w → HB.Adj b z → w ≠ z →
      ν.event (fun a => coefficientStar C a b w z) ≤ η) :
    joint.expect (fun σ => profileFraction ν F (fun b => (σ b).1) *
      profileFraction ν F (fun b => (σ b).2)) ≤
      ω + 2 * (κ : ℝ) * (J.card : ℝ) ^ 2 * η := by
  classical
  let T := {t : B × B × B // t ∈ fixedLeafStars HB J}
  let law := (ν.prod ν).prod joint
  let E : ((P × P) × (B → Bool × Bool)) → Prop :=
    fun x => pairLeftProfile x ∈ F ∧ pairRightProfile x ∈ F
  let D : ((P × P) × (B → Bool × Bool)) → Prop := fun x => x.1.1 = x.1.2
  let W : T → ((P × P) × (B → Bool × Bool)) → Prop := fun t x =>
    coefficientStar C x.1.1 t.val.1 t.val.2.1 t.val.2.2 ∨
      coefficientStar C x.1.2 t.val.1 t.val.2.1 t.val.2.2
  have hmono : law.event E ≤ law.event (fun x => D x ∨ ∃ t, W t x) := by
    apply FiniteProbability.event_mono_on_support
    intro x hx hE
    have hσ : joint.weight x.2 ≠ 0 := by
      intro hzero
      apply hx
      simp [law, FiniteProbability.prod, hzero]
    have hh := separated_masked_pair_diagonal_or_witness HB C F hF J
      x.1.1 x.1.2 (fun b => (x.2 b).1) (fun b => (x.2 b).2)
      (hjoint x.2 hσ) hE.1 hE.2
    rcases hh with hd | hw
    · exact Or.inl hd
    · obtain ⟨t, ht, hc⟩ := (fixedLeafStarWitness_iff HB C J _ _).mp hw
      exact Or.inr ⟨⟨t, ht⟩, hc⟩
  have hd : law.event D ≤ ω := by
    change ((ν.prod ν).prod joint).event
      (fun x => x.1.1 = x.1.2) ≤ ω
    rw [FiniteProbability.prod_event_fst (ν.prod ν) joint (fun a => a.1 = a.2)]
    exact coefficient_diagonal_le ν ω hω
  have hw (t : T) : law.event (W t) ≤ 2 * η := by
    change ((ν.prod ν).prod joint).event
      (fun x => coefficientStar C x.1.1 t.val.1 t.val.2.1 t.val.2.2 ∨
        coefficientStar C x.1.2 t.val.1 t.val.2.1 t.val.2.2) ≤ 2 * η
    rw [FiniteProbability.prod_event_fst (ν.prod ν) joint (fun a =>
      coefficientStar C a.1 t.val.1 t.val.2.1 t.val.2.2 ∨
        coefficientStar C a.2 t.val.1 t.val.2.1 t.val.2.2)]
    rcases (mem_fixedLeafStars_iff HB J t.val).mp t.property with
      ⟨hbw, hbz, hwz, _, _⟩
    exact coefficient_star_pair_le ν C _ _ _ η (hstar _ _ _ hbw hbz hwz)
  have hsum : law.event (fun x => ∃ t, W t x) ≤
      ((fixedLeafStars HB J).card : ℝ) * (2 * η) := by
    calc
      law.event (fun x => ∃ t, W t x) ≤ ∑ t : T, law.event (W t) :=
        law.event_exists_le_sum W
      _ ≤ ∑ _t : T, 2 * η := by
        apply Finset.sum_le_sum
        intro t _
        exact hw t
      _ = ((fixedLeafStars HB J).card : ℝ) * (2 * η) := by
        simp [T]
  have hcount : ((fixedLeafStars HB J).card : ℝ) ≤
      (J.card : ℝ) ^ 2 * (κ : ℝ) := by
    exact_mod_cast fixedLeafStars_card_le HB J κ hκ
  calc
    joint.expect (fun σ => profileFraction ν F (fun b => (σ b).1) *
      profileFraction ν F (fun b => (σ b).2)) = law.event E :=
      pairedFraction_eq_pair_membership ν F joint
    _ ≤ law.event D + law.event (fun x => ∃ t, W t x) :=
      hmono.trans (law.event_or_le D (fun x => ∃ t, W t x))
    _ ≤ ω + ((fixedLeafStars HB J).card : ℝ) * (2 * η) := add_le_add hd hsum
    _ ≤ ω + ((J.card : ℝ) ^ 2 * (κ : ℝ)) * (2 * η) := by
      simpa only [add_comm] using add_le_add_left
        (mul_le_mul_of_nonneg_right hcount (show 0 ≤ 2 * η by positivity)) ω
    _ = ω + 2 * (κ : ℝ) * (J.card : ℝ) ^ 2 * η := by ring

-- Source: Er579.MaskedCompatibility:470
/-- Uniform all-bias bound for the coefficientwise upward closure of an
independent family. The upward closure is not assumed graph-independent. -/
theorem upward_independent_biasResidualCorrelation_le
    (ν : FiniteProbability P) (HB : SimpleGraph B) (C : P → B → Prop)
    (F : Set (P × (B → Bool)))
    (hF : (maskedCompatibilityGraph HB C).IsIndepSet F)
    (ρ : ℝ) (hρ0 : 0 ≤ ρ) (hρhalf : ρ ≤ 1 / 2)
    (J : Finset B) (z : B → Bool) (κ : ℕ) (ω η : ℝ)
    (hω : ∀ a, ν.weight a ≤ ω) (hη0 : 0 ≤ η)
    (hκ : ∀ w z, w ≠ z → (commonStarCenters HB w z).card ≤ κ)
    (hstar : ∀ b w z, HB.Adj b w → HB.Adj b z → w ≠ z →
      ν.event (fun a => coefficientStar C a b w z) ≤ η) :
    biasResidualCorrelation ρ hρ0 hρhalf J z
      (profileFraction ν (maskUpwardClosure F)) ≤
      ω + 2 * (κ : ℝ) * (J.card : ℝ) ^ 2 * η := by
  apply separated_masked_pairedFraction_le ν HB C (maskUpwardClosure F)
    (coefficientSeparatedIncompatible_upward HB C F
      (independent_coefficientSeparatedIncompatible HB C F hF))
    J (biasResidualPairLaw ρ hρ0 hρhalf J z)
    (fun σ hσ b hb₁ hb₂ => biasResidualPair_shared_mem ρ hρ0 hρhalf J z σ hσ b hb₁ hb₂)
    κ ω η hω hη0 hκ hstar

-- Source: Er579.MaskedCompatibility:525
/-- The finite compatibility consequence of a proved monotone varying-bias
certificate. The actual family is enlarged coefficientwise before the
certificate is applied. -/
theorem independent_maskedProfileMass_lt_of_monotoneCertificate
    (ν : FiniteProbability P) (HB : SimpleGraph B) (C : P → B → Prop)
    (κ R : ℕ) (ω η ε d : ℝ)
    (hη0 : 0 ≤ η)
    (hω : ∀ a, ν.weight a ≤ ω)
    (hκ : ∀ w z, w ≠ z → (commonStarCenters HB w z).card ≤ κ)
    (hstar : ∀ b w z, HB.Adj b w → HB.Adj b z → w ≠ z →
      ν.event (fun a => coefficientStar C a b w z) ≤ η)
    (hres : ∀ f : (B → Bool) → ℝ, (∀ γ, 0 ≤ f γ ∧ f γ ≤ 1) → Monotone f →
      ε ≤ maskMean f →
      ∃ q : ℝ, ∃ hq0 : 0 ≤ q, ∃ hqhalf : q ≤ 1 / 2,
        ∃ (J : Finset B) (z : B → Bool),
          J.card ≤ R ∧ d ≤ biasResidualCorrelation q hq0 hqhalf J z f)
    (hgap : ω + 2 * (κ : ℝ) * (R : ℝ) ^ 2 * η < d)
    (F : Set (P × (B → Bool)))
    (hF : (maskedCompatibilityGraph HB C).IsIndepSet F) :
    maskedProfileMass ν F < ε := by
  by_contra h
  have hmass : ε ≤ maskMean (profileFraction ν (maskUpwardClosure F)) :=
    (le_of_not_gt h).trans (maskedProfileMass_le_upward_mean ν F)
  obtain ⟨q, hq0, hqhalf, J, z, hJ, hd⟩ := hres
    (profileFraction ν (maskUpwardClosure F))
    (profileFraction_mem_Icc ν (maskUpwardClosure F))
    (profileFraction_upward_monotone_order ν F) hmass
  have hb := upward_independent_biasResidualCorrelation_le ν HB C F hF
    q hq0 hqhalf J z κ ω η hω hη0 hκ hstar
  have hJR : (J.card : ℝ) ^ 2 ≤ (R : ℝ) ^ 2 := by
    have hcast : (J.card : ℝ) ≤ (R : ℝ) := by exact_mod_cast hJ
    nlinarith [Nat.cast_nonneg (α := ℝ) J.card, Nat.cast_nonneg (α := ℝ) R]
  have hbound : ω + 2 * (κ : ℝ) * (J.card : ℝ) ^ 2 * η ≤
      ω + 2 * (κ : ℝ) * (R : ℝ) ^ 2 * η := by
    have hc : 0 ≤ 2 * (κ : ℝ) * η := by positivity
    have hh := mul_le_mul_of_nonneg_left hJR hc
    nlinarith
  exact (not_lt_of_ge (hd.trans (hb.trans hbound))) hgap

end QuantitativeBound

-- Source: Er579.MaskedCompatibility:566
/-- Uniform weighted independence bound, with the entire analytic input
proved. The parameters depend only on the requested independent mass. -/
theorem maskedCompatibility_uniform_independent_mass_bound
    (ε : ℝ) (hε : 0 < ε) (hε1 : ε ≤ 1) :
    ∃ (R : ℕ) (d : ℝ), 0 < d ∧
      ∀ (P B : Type*) (_ : Fintype P) (_ : Fintype B)
        (ν : FiniteProbability P) (HB : SimpleGraph B) (C : P → B → Prop)
        (κ : ℕ) (ω η : ℝ),
        0 ≤ η → (∀ a, ν.weight a ≤ ω) →
        (∀ w z, w ≠ z → (commonStarCenters HB w z).card ≤ κ) →
        (∀ b w z, HB.Adj b w → HB.Adj b z → w ≠ z →
          ν.event (fun a => coefficientStar C a b w z) ≤ η) →
        ω + 2 * (κ : ℝ) * (R : ℝ) ^ 2 * η < d →
        ∀ F : Set (P × (B → Bool)),
          (maskedCompatibilityGraph HB C).IsIndepSet F → maskedProfileMass ν F < ε := by
  obtain ⟨R, d, hd, hcert⟩ := monotone_bounded_mask_correlation ε hε hε1
  refine ⟨R, d, hd, ?_⟩
  intro P B _ _ ν HB C κ ω η hη hω hκ hstar hgap F hF
  apply independent_maskedProfileMass_lt_of_monotoneCertificate ν HB C κ R ω η ε d
    hη hω hκ hstar ?_ hgap F hF
  intro f hf hmono hmass
  obtain ⟨q, hq0, hqhalf, _, _, J, z, hJ, hc⟩ := hcert B inferInstance f hf hmono hmass
  exact ⟨q, hq0, hqhalf, J, z, hJ, hc⟩

end

end Er579

end

/- Source fragment: Er579.CubeStarCaps. Original licenses and source proofs retained. -/

section

namespace Er579.CubeStarCaps

open scoped BigOperators Classical
open BooleanAnalysis CubeProfiles CubeGeometry CubeCaps RandomRealization

-- Source: Er579.CubeStarCaps:11
/-- Keep the finite-cube enumeration fixed when introducing classical decisions. -/
abbrev cubeFintype (n : ℕ) : Fintype (BoolCube n) := inferInstance

-- Source: Er579.CubeStarCaps:14
/-- Uniform coefficients, independently sampled from all masks. -/
noncomputable def coefficientLaw (n : ℕ) : FiniteProbability (BoolCube n) where
  weight _ := uniformWeight n
  nonneg _ := by unfold uniformWeight; positivity
  sum_one := uniform_weight_sum n

-- Source: Er579.CubeStarCaps:20
theorem coefficientLaw_weight (n : ℕ) (a : BoolCube n) :
    (coefficientLaw n).weight a = 1 / (2 : ℝ) ^ n := by
  simp only [coefficientLaw, uniformWeight, inv_pow, one_div]

-- Source: Er579.CubeStarCaps:24
theorem coefficientLaw_weight_card (n : ℕ) (a : BoolCube n) :
    (coefficientLaw n).weight a = 1 / (Fintype.card (BoolCube n) : ℝ) := by
  rw [coefficientLaw_weight]
  simp only [BoolCube, Fintype.card_fun, Fintype.card_bool, Fintype.card_fin,
    Nat.cast_pow, Nat.cast_ofNat]

-- Source: Er579.CubeStarCaps:30
theorem coefficientLaw_weight_pos (n : ℕ) (a : BoolCube n) :
    0 < (coefficientLaw n).weight a := by
  rw [coefficientLaw_weight]
  positivity

-- Source: Er579.CubeStarCaps:35
theorem coefficientLaw_expect {n : ℕ} (f : BooleanFunc n) :
    (coefficientLaw n).expect f = BooleanAnalysis.expect f :=
  finiteExpectation_uniform f

-- Source: Er579.CubeStarCaps:39
/-- The half-standard-deviation cap. -/
def cap {n : ℕ} (a b : BoolCube n) : Prop :=
  Real.sqrt (n : ℝ) / 2 ≤ signSum (CubeProfiles.xor a b)

-- Source: Er579.CubeStarCaps:43
theorem cap_mass_shift (n : ℕ) (b : BoolCube n) :
    (coefficientLaw n).event (fun a => cap a b) =
      eventWeight (fun _ : BoolCube n => uniformWeight n)
        (fun a => Real.sqrt (n : ℝ) / 2 ≤ signSum a) := by
  exact CapMoments.event_equiv (fun _ : BoolCube n => uniformWeight n)
    (shift b) (fun _ => rfl)
    (fun a => Real.sqrt (n : ℝ) / 2 ≤ signSum a)

-- Source: Er579.CubeStarCaps:51
theorem cap_mass_lower (n : ℕ) (hn : 0 < n) (b : BoolCube n) :
    3 / 32 ≤ (coefficientLaw n).event (fun a => cap a b) := by
  rw [cap_mass_shift]
  exact positive_cap_mass n hn

-- Source: Er579.CubeStarCaps:56
theorem mask_coordinate_mass {B : Type*} [Fintype B] (b : B) :
    (maskLaw : FiniteProbability (B → Bool)).event (fun γ => γ b = true) = 1 / 4 := by
  classical
  let g : B → Bool → ℝ := fun j t =>
    if j = b then (if t = true then maskBitWeight t else 0) else maskBitWeight t
  have hpoint (γ : B → Bool) :
      (if γ b = true then ∏ j, maskBitWeight (γ j) else 0) = ∏ j, g j (γ j) := by
    by_cases hγ : γ b = true
    · rw [if_pos hγ]
      apply Finset.prod_congr rfl
      intro j _
      by_cases hj : j = b
      · subst j
        simp [g, hγ]
      · simp [g, hj]
    · rw [if_neg hγ]
      symm
      apply Finset.prod_eq_zero (Finset.mem_univ b)
      simp [g, hγ]
  have hcoord (j : B) : (∑ t : Bool, g j t) = if j = b then 1 / 4 else 1 := by
    by_cases hj : j = b <;> norm_num [g, hj, maskBitWeight, Fintype.sum_bool]
  simp only [FiniteProbability.event, eventWeight, maskLaw, maskWeight]
  trans ∑ γ : B → Bool, ∏ j : B, g j (γ j)
  · apply Finset.sum_congr rfl
    intro γ _
    by_cases hγ : γ b = true
    · simpa only [if_pos hγ] using hpoint γ
    · simpa only [if_neg hγ] using hpoint γ
  rw [← Fintype.prod_sum]
  simp_rw [hcoord]
  simp

-- Source: Er579.CubeStarCaps:88
theorem masked_cross_mass_generic {P B : Type*} [Fintype P] [Fintype B]
    (ν : FiniteProbability P) (C : P → B → Prop) (b : B) :
    (maskedProfileLaw ν).event (fun q => maskedCross C q b) =
      ν.event (fun a => C a b) / 4 := by
  classical
  unfold maskedProfileLaw maskedCross
  calc
    (ν.prod (maskLaw : FiniteProbability (B → Bool))).event
        (fun q => C q.1 b ∧ q.2 b = true) =
      ν.event (fun a => C a b) *
        (maskLaw : FiniteProbability (B → Bool)).event
          (fun γ => γ b = true) :=
      FiniteProbability.prod_event_and ν maskLaw
        (fun a => C a b) (fun γ => γ b = true)
    _ = ν.event (fun a => C a b) / 4 := by
      rw [mask_coordinate_mass]
      ring

-- Source: Er579.CubeStarCaps:106
theorem masked_cross_mass (n : ℕ) (b : BoolCube n) :
    letI : Fintype (BoolCube n) := cubeFintype n
    letI : DecidableEq (BoolCube n) := Classical.decEq _
    (maskedProfileLaw (B := BoolCube n) (coefficientLaw n)).event
      (fun q => maskedCross cap q b) =
      (coefficientLaw n).event (fun a => cap a b) / 4 := by
  classical
  letI : Fintype (BoolCube n) := cubeFintype n
  letI : DecidableEq (BoolCube n) := Classical.decEq _
  exact masked_cross_mass_generic (coefficientLaw n) cap b

-- Source: Er579.CubeStarCaps:117
theorem masked_cross_mass_lower (n : ℕ) (hn : 0 < n) (b : BoolCube n) :
    letI : Fintype (BoolCube n) := cubeFintype n
    letI : DecidableEq (BoolCube n) := Classical.decEq _
    3 / 128 ≤
      (maskedProfileLaw (B := BoolCube n) (coefficientLaw n)).event
        (fun q => maskedCross cap q b) := by
  classical
  letI : Fintype (BoolCube n) := cubeFintype n
  letI : DecidableEq (BoolCube n) := Classical.decEq _
  rw [masked_cross_mass]
  have h := cap_mass_lower n hn b
  linarith

-- Source: Er579.CubeStarCaps:130
theorem masked_cross_density_lower (n : ℕ) (hn : 0 < n) :
    letI : Fintype (BoolCube n) := cubeFintype n
    letI : DecidableEq (BoolCube n) := Classical.decEq _
    3 / 128 ≤ (coefficientLaw n).expect (fun b =>
      (maskedProfileLaw (B := BoolCube n) (coefficientLaw n)).event
        (fun q => maskedCross cap q b)) := by
  classical
  letI : Fintype (BoolCube n) := cubeFintype n
  letI : DecidableEq (BoolCube n) := Classical.decEq _
  have h := (coefficientLaw n).expect_mono (fun b => masked_cross_mass_lower n hn b)
  simpa only [FiniteProbability.expect_const] using h

-- Source: Er579.CubeStarCaps:142
def partialSignSum {n : ℕ} (T : Finset (Fin n)) (x : BoolCube n) : ℝ :=
  ∑ i ∈ T, boolToSign (x i)

-- Source: Er579.CubeStarCaps:145
theorem expect_finset_sum {n : ℕ} {ι : Type*} (T : Finset ι)
    (f : ι → BooleanFunc n) :
    BooleanAnalysis.expect (fun x => ∑ i ∈ T, f i x) =
      ∑ i ∈ T, BooleanAnalysis.expect (f i) := by
  simp only [BooleanAnalysis.expect, Finset.mul_sum]
  exact Finset.sum_comm

-- Source: Er579.CubeStarCaps:152
theorem expect_sign_product {n : ℕ} (i j : Fin n) :
    BooleanAnalysis.expect (fun x : BoolCube n =>
      boolToSign (x i) * boolToSign (x j)) = if i = j then 1 else 0 := by
  simpa only [innerProduct, chiS_singleton, Finset.singleton_inj] using
    fourier_coeff_chi ({i} : Finset (Fin n)) {j}

-- Source: Er579.CubeStarCaps:158
/-- Exact variance of any partial sum of independent uniform signs. -/
theorem partial_second_moment {n : ℕ} (T : Finset (Fin n)) :
    BooleanAnalysis.expect (fun x : BoolCube n => partialSignSum T x ^ 2) = T.card := by
  have hex : (fun x : BoolCube n => partialSignSum T x ^ 2) =
      (fun x => ∑ i ∈ T, ∑ j ∈ T, boolToSign (x i) * boolToSign (x j)) := by
    funext x
    simp only [partialSignSum, pow_two, Finset.sum_mul, Finset.mul_sum]
    exact Finset.sum_comm
  rw [hex, expect_finset_sum]
  simp_rw [expect_finset_sum, expect_sign_product]
  simp

-- Source: Er579.CubeStarCaps:170
theorem partial_second_moment_shift {n : ℕ} (T : Finset (Fin n)) (b : BoolCube n) :
    (coefficientLaw n).expect (fun a => partialSignSum T (CubeProfiles.xor a b) ^ 2) =
      T.card := by
  rw [coefficientLaw_expect]
  change BooleanAnalysis.expect
    (CubeProfiles.translate b (fun a => partialSignSum T a ^ 2)) = T.card
  rw [CubeProfiles.expect_translate, partial_second_moment]

-- Source: Er579.CubeStarCaps:178
theorem partialSignSum_eq_sum_ite {n : ℕ} (T : Finset (Fin n)) (x : BoolCube n) :
    partialSignSum T x = ∑ j : Fin n, if j ∈ T then boolToSign (x j) else 0 := by
  simp [partialSignSum]

-- Source: Er579.CubeStarCaps:182
/-- On adjacent profiles, the full cap sums cancel outside T. -/
theorem adjacent_signSum_add {n : ℕ} (T : Finset (Fin n)) (a b : BoolCube n) :
    signSum (CubeProfiles.xor a b) +
        signSum (CubeProfiles.xor a (CubeProfiles.xor b (nearAntipode T))) =
      2 * partialSignSum T (CubeProfiles.xor a b) := by
  rw [← xor_assoc, partialSignSum_eq_sum_ite]
  simp only [signSum, ← Finset.sum_add_distrib, Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro j _
  by_cases hj : j ∈ T
  · simp only [nearAntipode, hj, decide_true, Bool.not_true,
      CubeProfiles.xor]
    cases a j <;> cases b j <;> norm_num [boolToSign]
  · simp only [nearAntipode, hj, decide_false, Bool.not_false,
      CubeProfiles.xor]
    cases a j <;> cases b j <;> norm_num [boolToSign]

-- Source: Er579.CubeStarCaps:199
theorem adjacent_caps_force_partial {n : ℕ} (T : Finset (Fin n)) (a b : BoolCube n)
    (hb : cap a b) (hb' : cap a (CubeProfiles.xor b (nearAntipode T))) :
    Real.sqrt (n : ℝ) / 2 ≤ partialSignSum T (CubeProfiles.xor a b) := by
  have hadd := adjacent_signSum_add T a b
  dsimp only [cap] at hb hb'
  linarith

-- Source: Er579.CubeStarCaps:206
/-- A second moment suffices: no exponential concentration theorem is needed. -/
theorem adjacent_cap_probability_le {n : ℕ} (hn : 0 < n)
    (T : Finset (Fin n)) (b : BoolCube n) :
    (coefficientLaw n).event (fun a =>
      cap a b ∧ cap a (CubeProfiles.xor b (nearAntipode T))) ≤
      4 * (T.card : ℝ) / n := by
  have hnR : (0 : ℝ) < n := by exact_mod_cast hn
  have hmono : (coefficientLaw n).event (fun a =>
        cap a b ∧ cap a (CubeProfiles.xor b (nearAntipode T))) ≤
      (coefficientLaw n).event (fun a =>
        (n : ℝ) / 4 ≤ partialSignSum T (CubeProfiles.xor a b) ^ 2) := by
    apply FiniteProbability.event_mono
    intro a ha
    have hp := adjacent_caps_force_partial T a b ha.1 ha.2
    have hs := Real.sq_sqrt hnR.le
    have hs0 := Real.sqrt_nonneg (n : ℝ)
    have hsq := pow_le_pow_left₀ (show 0 ≤ Real.sqrt (n : ℝ) / 2 by positivity) hp 2
    nlinarith
  have hmark := finite_markov (coefficientLaw n).weight (coefficientLaw n).nonneg
    (fun a => partialSignSum T (CubeProfiles.xor a b) ^ 2)
    (fun _ => sq_nonneg _) ((n : ℝ) / 4) (by positivity)
  change (coefficientLaw n).event (fun a =>
      (n : ℝ) / 4 ≤ partialSignSum T (CubeProfiles.xor a b) ^ 2) ≤
    (coefficientLaw n).expect (fun a => partialSignSum T (CubeProfiles.xor a b) ^ 2) /
      ((n : ℝ) / 4) at hmark
  rw [partial_second_moment_shift] at hmark
  calc
    (coefficientLaw n).event (fun a =>
        cap a b ∧ cap a (CubeProfiles.xor b (nearAntipode T))) ≤
      (coefficientLaw n).event (fun a =>
        (n : ℝ) / 4 ≤ partialSignSum T (CubeProfiles.xor a b) ^ 2) := hmono
    _ ≤ (T.card : ℝ) / ((n : ℝ) / 4) := hmark
    _ = 4 * (T.card : ℝ) / n := by ring

-- Source: Er579.CubeStarCaps:240
theorem coefficient_star_le {n : ℕ} {ι : Type*} (hn : 0 < n)
    (T : ι → Finset (Fin n)) (L : ℝ) (hsize : ∀ i, ((T i).card : ℝ) ≤ L)
    (b w z : BoolCube n) (hbw : (cayley (fun i => nearAntipode (T i))).Adj b w) :
    (coefficientLaw n).event (fun a => coefficientStar cap a b w z) ≤ 4 * L / n := by
  obtain ⟨_, i, hi⟩ := hbw
  have hmono : (coefficientLaw n).event (fun a => coefficientStar cap a b w z) ≤
      (coefficientLaw n).event (fun a => cap a b ∧ cap a w) := by
    apply FiniteProbability.event_mono
    intro a ha
    exact ⟨ha.1, ha.2.1⟩
  have hnR : (0 : ℝ) < n := by exact_mod_cast hn
  calc
    (coefficientLaw n).event (fun a => coefficientStar cap a b w z) ≤
      (coefficientLaw n).event (fun a => cap a b ∧ cap a w) := hmono
    _ ≤ 4 * ((T i).card : ℝ) / n := by
      rw [← hi]
      exact adjacent_cap_probability_le hn (T i) b
    _ ≤ 4 * L / n := div_le_div_of_nonneg_right
      (mul_le_mul_of_nonneg_left (hsize i) (by norm_num)) hnR.le

-- Source: Er579.CubeStarCaps:260
theorem coefficient_star_k_le {k : ℕ} (hk : 0 < k) {ι : Type*}
    (T : ι → Finset (Fin (k ^ 6)))
    (hsize : ∀ i, ((T i).card : ℝ) ≤ 4 * (k : ℝ) ^ 4)
    (b w z : BoolCube (k ^ 6))
    (hbw : (cayley (fun i => nearAntipode (T i))).Adj b w) :
    (coefficientLaw (k ^ 6)).event (fun a => coefficientStar cap a b w z) ≤
      16 / (k : ℝ) ^ 2 := by
  have h := coefficient_star_le (pow_pos hk 6) T (4 * (k : ℝ) ^ 4) hsize b w z hbw
  have hkR : (k : ℝ) ≠ 0 := by exact_mod_cast (Nat.ne_of_gt hk)
  calc
    (coefficientLaw (k ^ 6)).event (fun a => coefficientStar cap a b w z) ≤
      4 * (4 * (k : ℝ) ^ 4) / (k ^ 6 : ℕ) := h
    _ = 16 / (k : ℝ) ^ 2 := by
      push_cast
      field_simp [hkR]
      ring

-- Source: Er579.CubeStarCaps:277
theorem commonStarCenters_card_le_two {n : ℕ} {ι : Type*}
    (s : ι → BoolCube n) (hs : Function.Injective s) (hfour : FourIndependent s)
    (w z : BoolCube n) (hwz : w ≠ z) :
    (commonStarCenters (cayley s) w z).card ≤ 2 := by
  exact common_neighbors_card_le_two s hs hfour w z hwz

-- Source: Er579.CubeStarCaps:283
noncomputable def starRate (k : ℕ) : ℝ := 16 / (k : ℝ) ^ 2

-- Source: Er579.CubeStarCaps:285
noncomputable def atomRate (k : ℕ) : ℝ := 1 / (2 : ℝ) ^ (k ^ 6)

-- Source: Er579.CubeStarCaps:287
theorem coefficientLaw_weight_atomRate (k : ℕ) (a : BoolCube (k ^ 6)) :
    (coefficientLaw (k ^ 6)).weight a = atomRate k :=
  coefficientLaw_weight (k ^ 6) a

-- Source: Er579.CubeStarCaps:291
theorem starRate_nonneg (k : ℕ) : 0 ≤ starRate k := by
  unfold starRate
  positivity

open Filter
open scoped Topology

-- Source: Er579.CubeStarCaps:298
theorem starRate_tendsto_zero : Tendsto starRate atTop (𝓝 0) := by
  change Tendsto (fun k : ℕ => 16 / (k : ℝ) ^ 2) atTop (𝓝 0)
  have hi : Tendsto (fun k : ℕ => (k : ℝ)⁻¹) atTop (𝓝 0) :=
    tendsto_inv_atTop_nhds_zero_nat
  simpa only [div_eq_mul_inv, inv_pow, zero_pow (by norm_num : 2 ≠ 0),
    mul_zero] using (hi.pow 2).const_mul (16 : ℝ)

-- Source: Er579.CubeStarCaps:305
theorem atomRate_tendsto_zero : Tendsto atomRate atTop (𝓝 0) := by
  change Tendsto (fun k : ℕ => 1 / (2 : ℝ) ^ (k ^ 6)) atTop (𝓝 0)
  have hp : Tendsto (fun n : ℕ => (1 / 2 : ℝ) ^ n) atTop (𝓝 0) :=
    tendsto_pow_atTop_nhds_zero_of_lt_one (by norm_num) (by norm_num)
  have hi : Tendsto (fun k : ℕ => k ^ 6) atTop atTop :=
    tendsto_pow_atTop (by norm_num)
  simpa only [Function.comp_def, one_div, inv_pow] using hp.comp hi

-- Source: Er579.CubeStarCaps:313
theorem fixed_mask_error_tendsto_zero (R : ℕ) :
    Tendsto (fun k => atomRate k + 4 * (R : ℝ) ^ 2 * starRate k) atTop (𝓝 0) := by
  simpa only [mul_zero, add_zero] using
    atomRate_tendsto_zero.add (starRate_tendsto_zero.const_mul (4 * (R : ℝ) ^ 2))

-- Source: Er579.CubeStarCaps:318
theorem fixed_mask_error_eventually_lt (R : ℕ) {d : ℝ} (hd : 0 < d) :
    ∀ᶠ k : ℕ in atTop, atomRate k + 4 * (R : ℝ) ^ 2 * starRate k < d :=
  (fixed_mask_error_tendsto_zero R).eventually (gt_mem_nhds hd)

end Er579.CubeStarCaps

end

/- Source fragment: Er579.CubeStage. Original licenses and source proofs retained. -/

section

namespace Er579.CubeStage

open BooleanAnalysis CubeProfiles CubeGeometry CubeGenerators
open BooleanAnalysis.Hypercontractivity
open scoped BigOperators Topology

-- Source: Er579.CubeStage:11
abbrev Profile (k : ℕ) := BoolCube (dimension k)

-- Source: Er579.CubeStage:13
abbrev Supports (k : ℕ) := Fin (degree k) → Finset (Fin (dimension k))

-- Source: Er579.CubeStage:15
def directions {k : ℕ} (T : Supports k) : Fin (degree k) → Profile k :=
  fun i => nearAntipode (T i)

-- Source: Er579.CubeStage:18
def baseGraph {k : ℕ} (T : Supports k) : SimpleGraph (Profile k) :=
  cayley (directions T)

-- Source: Er579.CubeStage:21
noncomputable def law (k : ℕ) : FiniteProbability (Profile k) :=
  CubeStarCaps.coefficientLaw (dimension k)

-- Source: Er579.CubeStage:24
noncomputable def dyadicRate (k : ℕ) : ℝ := ((2 : ℝ)⁻¹) ^ k

-- Source: Er579.CubeStage:26
/-- The fully proved cube input for the masked graph construction. -/
structure Stage (k : ℕ) where
  supports : Supports k
  nonzero : ∀ i, directions supports i ≠ zero (dimension k)
  injective : Function.Injective (directions supports)
  triangleFree : Er579.TriangleFree (baseGraph supports)
  commonCenters : ∀ w z, w ≠ z → (commonStarCenters (baseGraph supports) w z).card ≤ 2
  independence : ((baseGraph supports).indepNum : ℝ) ≤
    dyadicRate k * Fintype.card (Profile k)
  coefficientUniform : ∀ a, (law k).weight a = 1 / (Fintype.card (Profile k) : ℝ)
  coefficientAtoms : ∀ a, (law k).weight a = CubeStarCaps.atomRate k
  coefficientPositive : ∀ a, 0 < (law k).weight a
  capMass : ∀ b, 3 / 32 ≤ (law k).event (fun a => CubeStarCaps.cap a b)
  starMass : ∀ b w z, (baseGraph supports).Adj b w →
    (law k).event (fun a => coefficientStar CubeStarCaps.cap a b w z) ≤ CubeStarCaps.starRate k

-- Source: Er579.CubeStage:42
theorem stage_of_good_tuple {k : ℕ} (hk : 5 ≤ k) (T : Supports k)
    (hT : GoodTuple k T) : Nonempty (Stage k) := by
  obtain ⟨hlower, hupper, hinter, hfour, hspectral⟩ := hT
  obtain ⟨hnonzero, hinj, htri, _⟩ :=
    audited_geometry hk T hlower hupper hinter hfour
  have hclose : ∀ S : Finset (Fin (dimension k)),
      |eigenvalue (directions T) S - chiS S (one (dimension k)) *
        (1 - 2 / (k : ℝ) ^ 2) ^ S.card| ≤ ((2 : ℝ)⁻¹) ^ (k ^ 3) := by
    intro S
    change |eigenvalue (fun i => nearAntipode (T i)) S - chiS S (one (dimension k)) *
      (1 - 2 / (k : ℝ) ^ 2) ^ S.card| ≤ ((2 : ℝ)⁻¹) ^ (k ^ 3)
    simpa only [theta, accuracy, div_eq_mul_inv, one_mul, inv_pow] using hspectral S
  have hind := indepNum_le_dyadic k (show 2 ≤ k by omega)
    (directions T) hnonzero hclose
  refine ⟨{
    supports := T
    nonzero := hnonzero
    injective := hinj
    triangleFree := htri
    commonCenters := ?_
    independence := hind
    coefficientUniform := ?_
    coefficientAtoms := ?_
    coefficientPositive := ?_
    capMass := ?_
    starMass := ?_
  }⟩
  · intro w z hwz
    exact CubeStarCaps.commonStarCenters_card_le_two (directions T) hinj hfour w z hwz
  · intro a
    exact CubeStarCaps.coefficientLaw_weight_card (dimension k) a
  · intro a
    exact CubeStarCaps.coefficientLaw_weight_atomRate k a
  · intro a
    exact CubeStarCaps.coefficientLaw_weight_pos (dimension k) a
  · intro b
    exact CubeStarCaps.cap_mass_lower (dimension k) (pow_pos (show 0 < k by omega) 6) b
  · intro b w z hbw
    exact CubeStarCaps.coefficient_star_k_le (show 0 < k by omega) T hupper b w z hbw

-- Source: Er579.CubeStage:82
/-- Every sufficiently large parameter has an actual cube stage, with no
analytic, sampling or geometric existence hypotheses. -/
theorem eventually_exists_stage : ∀ᶠ k in Filter.atTop, Nonempty (Stage k) := by
  filter_upwards [eventually_exists_good_tuple, Filter.eventually_ge_atTop 5] with k hT hk
  obtain ⟨T, hT⟩ := hT
  exact stage_of_good_tuple hk T hT

-- Source: Er579.CubeStage:89
theorem dyadicRate_tendsto_zero : Filter.Tendsto dyadicRate Filter.atTop (𝓝 0) := by
  change Filter.Tendsto (fun k : ℕ => ((2 : ℝ)⁻¹) ^ k) Filter.atTop (𝓝 0)
  exact tendsto_pow_atTop_nhds_zero_of_lt_one (by norm_num) (by norm_num)

-- Source: Er579.CubeStage:97
theorem dyadicRate_pos (k : ℕ) : 0 < dyadicRate k := by
  unfold dyadicRate
  positivity

end Er579.CubeStage

end

/- Source fragment: Er579.ProfileWeights. Original licenses and source proofs retained. -/

section

namespace Er579.ProfileWeights

open scoped BigOperators Classical
open RandomRealization

variable {P B : Type*} [Fintype P] [Fintype B]

-- Source: Er579.ProfileWeights:10
def maskMultiplicity (γ : B → Bool) : ℕ := ∏ b, if γ b then 1 else 3

-- Source: Er579.ProfileWeights:12
def profileMultiplicity (q : P × (B → Bool)) : ℕ := maskMultiplicity q.2

-- Source: Er579.ProfileWeights:14
def denominator (P B : Type*) [Fintype P] [Fintype B] : ℕ :=
  Fintype.card P * 4 ^ Fintype.card B

-- Source: Er579.ProfileWeights:17
theorem maskMultiplicity_pos (γ : B → Bool) : 0 < maskMultiplicity γ := by
  apply Finset.prod_pos
  intro b _
  cases γ b <;> norm_num

-- Source: Er579.ProfileWeights:22
theorem profileMultiplicity_pos (q : P × (B → Bool)) : 0 < profileMultiplicity q :=
  maskMultiplicity_pos q.2

-- Source: Er579.ProfileWeights:25
theorem maskMultiplicity_sum : (∑ γ : B → Bool, maskMultiplicity γ) =
    4 ^ Fintype.card B := by
  unfold maskMultiplicity
  rw [← Fintype.prod_sum (fun (_ : B) (x : Bool) => (if x then 1 else 3 : ℕ))]
  have h : (∑ x : Bool, if x then (1 : ℕ) else 3) = 4 := by
    norm_num [Fintype.sum_bool]
  simp only [h, Finset.prod_const, Finset.card_univ]

-- Source: Er579.ProfileWeights:33
theorem profileMultiplicity_sum :
    (∑ q : P × (B → Bool), profileMultiplicity q) = denominator P B := by
  rw [Fintype.sum_prod_type]
  simp only [profileMultiplicity, maskMultiplicity_sum, Finset.sum_const,
    Finset.card_univ, smul_eq_mul, denominator]

-- Source: Er579.ProfileWeights:39
theorem denominator_pos (hP : 0 < Fintype.card P) : 0 < denominator P B :=
  Nat.mul_pos hP (pow_pos (by norm_num) _)

-- Source: Er579.ProfileWeights:42
theorem maskWeight_eq_div (γ : B → Bool) :
    maskWeight γ = (maskMultiplicity γ : ℝ) / (4 : ℝ) ^ Fintype.card B := by
  have h : ∀ b : B, maskBitWeight (γ b) = ((if γ b then 1 else 3 : ℕ) : ℝ) / 4 := by
    intro b
    cases γ b <;> norm_num [maskBitWeight]
  unfold maskWeight maskMultiplicity
  simp only [h, Nat.cast_prod, Finset.prod_div_distrib, Finset.prod_const,
    Finset.card_univ]

-- Source: Er579.ProfileWeights:51
theorem profileWeight_eq (ν : FiniteProbability P)
    (huniform : ∀ a, ν.weight a = 1 / (Fintype.card P : ℝ))
    (q : P × (B → Bool)) :
    ν.weight q.1 * maskWeight q.2 =
      (profileMultiplicity q : ℝ) / (denominator P B : ℝ) := by
  rw [huniform, maskWeight_eq_div]
  simp only [profileMultiplicity, denominator, Nat.cast_mul, Nat.cast_pow, Nat.cast_ofNat]
  ring

-- Source: Er579.ProfileWeights:60
/-- Natural cell multiplicities recover exactly the weighted mask family
mass; no approximation of real profile weights is used. -/
theorem profileMass_finset (ν : FiniteProbability P)
    (huniform : ∀ a, ν.weight a = 1 / (Fintype.card P : ℝ))
    (W : Finset (P × (B → Bool))) :
    maskedProfileMass ν (W : Set (P × (B → Bool))) =
      (∑ q ∈ W, (profileMultiplicity q : ℝ)) / (denominator P B : ℝ) := by
  classical
  unfold maskedProfileMass maskMean profileFraction FiniteProbability.expect
    FiniteProbability.event finiteExpectation eventWeight maskLaw
  simp only [Finset.mul_sum]
  rw [Finset.sum_comm]
  simp only [Finset.mem_coe]
  change (∑ a : P, ∑ γ : B → Bool,
    maskWeight γ * (if (a, γ) ∈ W then ν.weight a else 0)) = _
  have hp : (∑ a : P, ∑ γ : B → Bool,
      maskWeight γ * (if (a, γ) ∈ W then ν.weight a else 0)) =
      ∑ q : P × (B → Bool), if q ∈ W then
        (profileMultiplicity q : ℝ) / (denominator P B : ℝ) else 0 := by
    rw [Fintype.sum_prod_type]
    apply Finset.sum_congr rfl
    intro a _
    apply Finset.sum_congr rfl
    intro γ _
    by_cases h : (a, γ) ∈ W
    · simp only [if_pos h]
      rw [mul_comm, profileWeight_eq ν huniform (a, γ)]
    · simp only [if_neg h, mul_zero]
  rw [hp]
  simp only [Finset.sum_ite_mem, Finset.univ_inter, Finset.sum_div]

-- Source: Er579.ProfileWeights:91
theorem independent_multiplicity_bound (ν : FiniteProbability P)
    (huniform : ∀ a, ν.weight a = 1 / (Fintype.card P : ℝ))
    (H : SimpleGraph (P × (B → Bool))) (a : ℝ)
    (hα : ∀ W : Finset (P × (B → Bool)), H.IsIndepSet (W : Set _) →
      maskedProfileMass ν (W : Set (P × (B → Bool))) ≤ a)
    (hP : 0 < Fintype.card P)
    (W : Finset (P × (B → Bool))) (hW : H.IsIndepSet (W : Set _)) :
    (∑ q ∈ W, (profileMultiplicity q : ℝ)) ≤ a * (denominator P B : ℝ) := by
  have h := hα W hW
  rw [profileMass_finset ν huniform W] at h
  exact (div_le_iff₀ (by exact_mod_cast denominator_pos (B := B) hP)).mp h

end Er579.ProfileWeights

end

/- Source fragment: Er579.RandomRealization.BernoulliGraph. Original licenses and source proofs retained. -/

section

namespace Er579.RandomRealization

open scoped BigOperators Classical

variable {V : Type*}

-- Source: Er579.RandomRealization.BernoulliGraph:11
def bernoulliGraph (G : SimpleGraph V) (ω : Sym2 V → Bool) : SimpleGraph V where
  Adj u v := G.Adj u v ∧ ω (Sym2.mk u v) = true
  symm := by
    constructor
    intro u v h
    refine ⟨G.adj_symm h.1, ?_⟩
    rw [Sym2.eq_swap]
    exact h.2
  loopless := by
    constructor
    intro v h
    exact G.irrefl h.1

-- Source: Er579.RandomRealization.BernoulliGraph:24
noncomputable def cellCrossEdges (U W : Finset V) : Finset (Sym2 V) :=
  (U ×ˢ W).image (fun p => Sym2.mk p.1 p.2)

-- Source: Er579.RandomRealization.BernoulliGraph:27
theorem cellCrossEdges_card (U W : Finset V) (hdisjoint : Disjoint U W) :
    (cellCrossEdges U W).card = U.card * W.card := by
  have hinj : Set.InjOn (fun p : V × V => Sym2.mk p.1 p.2) (U ×ˢ W : Finset (V × V)) := by
    intro p hp q hq heq
    have hp' := Finset.mem_product.mp hp
    have hq' := Finset.mem_product.mp hq
    rcases Sym2.eq_iff.mp heq with ⟨h1, h2⟩ | ⟨h1, _⟩
    · exact Prod.ext h1 h2
    · exact ((Finset.disjoint_left.mp hdisjoint) hp'.1 (h1.symm ▸ hq'.2)).elim
  unfold cellCrossEdges
  rw [Finset.card_image_of_injOn hinj, Finset.card_product]

-- Source: Er579.RandomRealization.BernoulliGraph:39
theorem independent_forces_cross_absent (G : SimpleGraph V) (I U W : Finset V)
    (hUI : U ⊆ I) (hWI : W ⊆ I) (hallowed : ∀ u ∈ U, ∀ v ∈ W, G.Adj u v)
    (ω : Sym2 V → Bool) (hI : (bernoulliGraph G ω).IsIndepSet (I : Set V)) :
    ∀ e ∈ cellCrossEdges U W, ω e = false := by
  intro e he
  obtain ⟨p, hp, rfl⟩ := Finset.mem_image.mp he
  obtain ⟨hu, hv⟩ := Finset.mem_product.mp hp
  have hadj := hallowed p.1 hu p.2 hv
  cases hbit : ω (Sym2.mk p.1 p.2)
  · rfl
  · exact (hI (hUI hu) (hWI hv) hadj.ne ⟨hadj, hbit⟩).elim

-- Source: Er579.RandomRealization.BernoulliGraph:51
theorem bernoulli_independent_weight_le [Fintype (Sym2 V)] [DecidableEq (Sym2 V)]
    (G : SimpleGraph V) (I U W : Finset V)
    (hUI : U ⊆ I) (hWI : W ⊆ I) (hdisjoint : Disjoint U W)
    (hallowed : ∀ u ∈ U, ∀ v ∈ W, G.Adj u v)
    (r : ℝ) (hr0 : 0 ≤ r) (hr1 : r ≤ 1) :
    eventWeight (bernoulliWeight (E := Sym2 V) r)
      (fun ω : Sym2 V → Bool => (bernoulliGraph G ω).IsIndepSet (I : Set V)) ≤
      Real.exp (-r * (U.card : ℝ) * (W.card : ℝ)) := by
  calc
    eventWeight (bernoulliWeight (E := Sym2 V) r)
        (fun ω : Sym2 V → Bool => (bernoulliGraph G ω).IsIndepSet (I : Set V)) ≤
        eventWeight (bernoulliWeight (E := Sym2 V) r)
          (fun ω : Sym2 V → Bool => ∀ e ∈ cellCrossEdges U W, ω e = false) :=
      eventWeight_mono (bernoulliWeight (E := Sym2 V) r)
        (bernoulliWeight_nonneg (E := Sym2 V) hr0 hr1)
        (fun ω hI => independent_forces_cross_absent G I U W hUI hWI hallowed ω hI)
    _ ≤ Real.exp (-r * ((cellCrossEdges U W).card : ℝ)) :=
      bernoulli_absent_weight_le_exp hr1 (cellCrossEdges U W)
    _ = Real.exp (-r * (U.card : ℝ) * (W.card : ℝ)) := by
      rw [cellCrossEdges_card U W hdisjoint, Nat.cast_mul, mul_assoc]

end Er579.RandomRealization

end

/- Source fragment: Er579.RandomRealization.BernoulliA. Original licenses and source proofs retained. -/

section

namespace Er579.RandomRealization

open scoped BigOperators Classical

variable {Q : Type*} [Fintype Q] [DecidableEq Q]

-- Source: Er579.RandomRealization.BernoulliA:12
noncomputable def aEdgeProbability (L : ℕ) : ℝ := 1 / (L : ℝ) ^ 4

-- Source: Er579.RandomRealization.BernoulliA:14
theorem aEdgeProbability_bounds {L : ℕ} (hL : 0 < L) :
    0 ≤ aEdgeProbability L ∧ aEdgeProbability L ≤ 1 := by
  have hreal : (1 : ℝ) ≤ L := by exact_mod_cast hL
  have hpow : (1 : ℝ) ≤ (L : ℝ) ^ 4 := one_le_pow₀ hreal
  have hpos : 0 < (L : ℝ) ^ 4 := lt_of_lt_of_le (by norm_num) hpow
  constructor
  · exact le_of_lt (one_div_pos.mpr hpos)
  · exact (div_le_iff₀ hpos).2 (by simpa using hpow)

-- Source: Er579.RandomRealization.BernoulliA:23
theorem bernoulliA_fixed_large_set (H : SimpleGraph Q) (m : Q → ℕ) (L : ℕ)
    (hm : ∀ q, 1 ≤ m q) (hL : 0 < L) (a ε : ℝ) (hε : 0 ≤ ε)
    (hα : ProfileIndependenceBound H m a) (I : Finset (BlowupVertex m L))
    (hlarge : (a + ε) * Fintype.card (BlowupVertex m L) < I.card) :
    eventWeight (bernoulliWeight (E := Sym2 (BlowupVertex m L)) (aEdgeProbability L))
      (fun ω => (bernoulliGraph (profileBlowup H m L) ω).IsIndepSet (I : Set (BlowupVertex m L))) ≤
      Real.exp (-(ε ^ 2 * (L : ℝ) ^ 6)) := by
  obtain ⟨q, q', hadj, hqheavy, hqheavy'⟩ :=
    large_set_adjacent_heavy_profiles H m L I a ε hε hα hlarge
  let U := selectedCell m L I q
  let W := selectedCell m L I q'
  have hUI : U ⊆ I := selectedCell_subset m L I q
  have hWI : W ⊆ I := selectedCell_subset m L I q'
  have hdisjoint : Disjoint U W := by
    apply Finset.disjoint_left.mpr
    intro v hvU hvW
    have hvq : v.1 = q := (mem_selectedCell m L I q v).mp hvU |>.2
    have hvq' : v.1 = q' := (mem_selectedCell m L I q' v).mp hvW |>.2
    exact hadj.ne (hvq.symm.trans hvq')
  have hallowed : ∀ u ∈ U, ∀ v ∈ W, (profileBlowup H m L).Adj u v := by
    intro u hu v hv
    have huq : u.1 = q := (mem_selectedCell m L I q u).mp hu |>.2
    have hvq : v.1 = q' := (mem_selectedCell m L I q' v).mp hv |>.2
    change H.Adj u.1 v.1
    rw [huq, hvq]
    exact hadj
  have hminimum (p : Q) : (L : ℝ) ^ 5 ≤ ((m p * L ^ 5 : ℕ) : ℝ) := by
    have hnat : L ^ 5 ≤ m p * L ^ 5 := by
      simpa only [one_mul] using Nat.mul_le_mul_right (L ^ 5) (hm p)
    exact_mod_cast hnat
  have hU : ε * (L : ℝ) ^ 5 ≤ (U.card : ℝ) :=
    (mul_le_mul_of_nonneg_left (hminimum q) hε).trans hqheavy
  have hW : ε * (L : ℝ) ^ 5 ≤ (W.card : ℝ) :=
    (mul_le_mul_of_nonneg_left (hminimum q') hε).trans hqheavy'
  obtain ⟨hp0, hp1⟩ := aEdgeProbability_bounds hL
  have hprod : (ε * (L : ℝ) ^ 5) * (ε * (L : ℝ) ^ 5) ≤ (U.card : ℝ) * W.card :=
    mul_le_mul hU hW (by positivity) (by positivity)
  have hscale := mul_le_mul_of_nonneg_left hprod hp0
  have hLne : (L : ℝ) ≠ 0 := ne_of_gt (by exact_mod_cast hL)
  have hidentity : aEdgeProbability L * (ε * (L : ℝ) ^ 5) * (ε * (L : ℝ) ^ 5) =
      ε ^ 2 * (L : ℝ) ^ 6 := by
    unfold aEdgeProbability
    field_simp [hLne]
  have hexp : -aEdgeProbability L * (U.card : ℝ) * W.card ≤ -(ε ^ 2 * (L : ℝ) ^ 6) := by
    nlinarith [hscale, hidentity]
  exact (bernoulli_independent_weight_le (profileBlowup H m L) I U W
    hUI hWI hdisjoint hallowed (aEdgeProbability L) hp0 hp1).trans
      (Real.exp_le_exp.mpr hexp)

-- Source: Er579.RandomRealization.BernoulliA:72
theorem bernoulliA_independence_bad_weight (H : SimpleGraph Q) (m : Q → ℕ) (L : ℕ)
    (hm : ∀ q, 1 ≤ m q) (hL : 0 < L) (a ε : ℝ) (hε : 0 ≤ ε)
    (hα : ProfileIndependenceBound H m a) :
    eventWeight (bernoulliWeight (E := Sym2 (BlowupVertex m L)) (aEdgeProbability L))
      (fun ω => (a + ε) * Fintype.card (BlowupVertex m L) <
        ((bernoulliGraph (profileBlowup H m L) ω).indepNum : ℝ)) ≤
      (2 : ℝ) ^ (totalMultiplicity m * L ^ 5) * Real.exp (-(ε ^ 2 * (L : ℝ) ^ 6)) := by
  let w := bernoulliWeight (E := Sym2 (BlowupVertex m L)) (aEdgeProbability L)
  let P : Finset (BlowupVertex m L) → (Sym2 (BlowupVertex m L) → Bool) → Prop :=
    fun I ω => (a + ε) * Fintype.card (BlowupVertex m L) < I.card ∧
      (bernoulliGraph (profileBlowup H m L) ω).IsIndepSet (I : Set (BlowupVertex m L))
  have hw : ∀ ω, 0 ≤ w ω := bernoulliWeight_nonneg
    (aEdgeProbability_bounds hL).1 (aEdgeProbability_bounds hL).2
  have hmono : eventWeight w
      (fun ω => (a + ε) * Fintype.card (BlowupVertex m L) <
        ((bernoulliGraph (profileBlowup H m L) ω).indepNum : ℝ)) ≤
      eventWeight w (fun ω => ∃ I, P I ω) := by
    apply eventWeight_mono w hw
    intro ω hbad
    obtain ⟨I, hI⟩ := (bernoulliGraph (profileBlowup H m L) ω).exists_isNIndepSet_indepNum
    refine ⟨I, ?_, hI.isIndepSet⟩
    simpa only [hI.card_eq] using hbad
  have heach (I : Finset (BlowupVertex m L)) : eventWeight w (P I) ≤
      Real.exp (-(ε ^ 2 * (L : ℝ) ^ 6)) := by
    by_cases hlarge : (a + ε) * Fintype.card (BlowupVertex m L) < I.card
    · have hm' : eventWeight w (P I) ≤ eventWeight w
          (fun ω => (bernoulliGraph (profileBlowup H m L) ω).IsIndepSet (I : Set (BlowupVertex m L))) :=
        eventWeight_mono w hw (fun _ h => h.2)
      exact hm'.trans (bernoulliA_fixed_large_set H m L hm hL a ε hε hα I hlarge)
    · have hz : eventWeight w (P I) = 0 := by
        unfold eventWeight
        apply Finset.sum_eq_zero
        intro ω _
        exact if_neg (fun h => hlarge h.1)
      rw [hz]
      exact (Real.exp_pos _).le
  calc
    eventWeight w _ ≤ ∑ I, eventWeight w (P I) :=
      hmono.trans (eventWeight_exists_le_sum w hw P)
    _ ≤ ∑ _I : Finset (BlowupVertex m L), Real.exp (-(ε ^ 2 * (L : ℝ) ^ 6)) :=
      Finset.sum_le_sum (fun I _ => heach I)
    _ = (2 : ℝ) ^ (totalMultiplicity m * L ^ 5) * Real.exp (-(ε ^ 2 * (L : ℝ) ^ 6)) := by
      simp only [Finset.sum_const, Finset.card_univ, nsmul_eq_mul, Fintype.card_finset,
        Nat.cast_pow, Nat.cast_ofNat, blowupVertex_card]

end Er579.RandomRealization

end

/- Source fragment: Er579.RandomRealization.FiniteCounting. Original licenses and source proofs retained. -/

section

namespace Er579.RandomRealization

open scoped BigOperators Classical

variable {Ω ι : Type*} [Fintype Ω]

-- Source: Er579.RandomRealization.FiniteCounting:10
theorem finiteExpectation_card_filter (w : Ω → ℝ) (s : Finset ι)
    (P : Ω → ι → Prop) :
    finiteExpectation w (fun ω => ((s.filter (P ω)).card : ℝ)) =
      ∑ i ∈ s, eventWeight w (fun ω => P ω i) := by
  have hcard (ω : Ω) : ((s.filter (P ω)).card : ℝ) =
      ∑ i ∈ s, if P ω i then (1 : ℝ) else 0 := Finset.natCast_card_filter _ _
  have hfirst : finiteExpectation w (fun ω => ((s.filter (P ω)).card : ℝ)) =
      finiteExpectation w (fun ω => ∑ i ∈ s, if P ω i then (1 : ℝ) else 0) := by
    unfold finiteExpectation
    apply Finset.sum_congr rfl
    intro ω _
    exact congrArg (fun r : ℝ => w ω * r) (hcard ω)
  rw [hfirst, finiteExpectation_sum]
  apply Finset.sum_congr rfl
  intro i _
  unfold finiteExpectation eventWeight
  apply Finset.sum_congr rfl
  intro ω _
  by_cases h : P ω i <;> simp [h]

end Er579.RandomRealization

end

/- Source fragment: Er579.RandomRealization.RealizationFromBounds. Original licenses and source proofs retained. -/

section

/-! A proved finite bridge from the two estimates of a random realization
to an actual cleaned finite graph.  The estimates are theorem hypotheses;
no probability estimate or existence statement is postulated as an axiom. -/

namespace Er579.RandomRealization

open scoped BigOperators Classical

variable {Ω V : Type*} [Fintype Ω] [Fintype V]

-- Source: Er579.RandomRealization.RealizationFromBounds:15
noncomputable def shortCycleCount (G : SimpleGraph V) : ℕ :=
  (triangleOccurrences G).card + (squareOccurrences G).card

-- Source: Er579.RandomRealization.RealizationFromBounds:18
theorem exists_clean_realization_from_bounds
    (w : Ω → ℝ) (hw : ∀ ω, 0 ≤ w ω) (hnorm : ∑ ω, w ω = 1)
    (sample : Ω → SimpleGraph V) (alphaBound deleteBound : ℝ)
    (hdelete : 0 < deleteBound)
    (hestimates :
      eventWeight w (fun ω => alphaBound < (sample ω).indepNum) +
        finiteExpectation w (fun ω => (shortCycleCount (sample ω) : ℝ)) / deleteBound < 1) :
    ∃ ω,
      TriangleFree (cleanedGraph (sample ω)) ∧
      C4Free (cleanedGraph (sample ω)) ∧
      ((cleanedGraph (sample ω)).indepNum : ℝ) ≤ alphaBound ∧
      (cleanupVertices (sample ω)).card < deleteBound ∧
      (Fintype.card V : ℝ) - deleteBound < Fintype.card (CleanVertex (sample ω)) := by
  have hcycle : eventWeight w (fun ω => deleteBound ≤ (shortCycleCount (sample ω) : ℝ)) ≤
      finiteExpectation w (fun ω => (shortCycleCount (sample ω) : ℝ)) / deleteBound :=
    finite_markov w hw _ (fun _ => Nat.cast_nonneg _) deleteBound hdelete
  have hboth : eventWeight w (fun ω => alphaBound < (sample ω).indepNum) +
      eventWeight w (fun ω => deleteBound ≤ (shortCycleCount (sample ω) : ℝ)) < 1 := by
    linarith
  obtain ⟨ω, hα, hC⟩ := exists_avoiding_two w hw hnorm
    (fun ω => alphaBound < (sample ω).indepNum)
    (fun ω => deleteBound ≤ (shortCycleCount (sample ω) : ℝ)) hboth
  have hα' : ((cleanedGraph (sample ω)).indepNum : ℝ) ≤ alphaBound := by
    have hmono : ((cleanedGraph (sample ω)).indepNum : ℝ) ≤ (sample ω).indepNum := by
      exact_mod_cast cleanedGraph_indepNum_le (sample ω)
    exact hmono.trans (le_of_not_gt hα)
  have hC' : (shortCycleCount (sample ω) : ℝ) < deleteBound := lt_of_not_ge hC
  have hD : ((cleanupVertices (sample ω)).card : ℝ) < deleteBound := by
    have hbound : ((cleanupVertices (sample ω)).card : ℝ) ≤ shortCycleCount (sample ω) := by
      exact_mod_cast cleanupVertices_card_le (sample ω)
    exact hbound.trans_lt hC'
  refine ⟨ω, cleanedGraph_triangleFree _, cleanedGraph_c4Free _, hα', hD, ?_⟩
  rw [cleanVertex_card_eq_real]
  linarith

end Er579.RandomRealization

end

/- Source fragment: Er579.RandomRealization.BernoulliCycles. Original licenses and source proofs retained. -/

section

namespace Er579.RandomRealization

open scoped BigOperators Classical

variable {V : Type*}

-- Source: Er579.RandomRealization.BernoulliCycles:12
def trianglePattern (G : SimpleGraph V) (t : V × V × V) : Prop :=
  G.Adj t.1 t.2.1 ∧ G.Adj t.2.1 t.2.2 ∧ G.Adj t.2.2 t.1

-- Source: Er579.RandomRealization.BernoulliCycles:15
def squarePattern (G : SimpleGraph V) (t : V × V × V × V) : Prop :=
  t.1 ≠ t.2.2.1 ∧ t.2.1 ≠ t.2.2.2 ∧
    G.Adj t.1 t.2.1 ∧ G.Adj t.2.1 t.2.2.1 ∧
    G.Adj t.2.2.1 t.2.2.2 ∧ G.Adj t.2.2.2 t.1

-- Source: Er579.RandomRealization.BernoulliCycles:20
theorem bernoulli_triangle_weight_le [Fintype (Sym2 V)] [DecidableEq (Sym2 V)]
    (G : SimpleGraph V) (r : ℝ) (hr0 : 0 ≤ r) (hr1 : r ≤ 1) (t : V × V × V) :
    eventWeight (bernoulliWeight (E := Sym2 V) r)
      (fun ω => trianglePattern (bernoulliGraph G ω) t) ≤ r ^ 3 := by
  rcases t with ⟨a, b, c⟩
  let K : Finset (Sym2 V) := {Sym2.mk a b, Sym2.mk b c, Sym2.mk c a}
  by_cases hbase : G.Adj a b ∧ G.Adj b c ∧ G.Adj c a
  · obtain ⟨hab, hbc, hca⟩ := hbase
    have hnab := hab.ne
    have hnbc := hbc.ne
    have hnca := hca.ne
    have hK : K.card = 3 := by
      simp [K, hnab, hnbc, hnca, Ne.symm hnab, Ne.symm hnca]
    calc
      eventWeight (bernoulliWeight (E := Sym2 V) r)
          (fun ω => trianglePattern (bernoulliGraph G ω) (a, b, c)) ≤
          eventWeight (bernoulliWeight (E := Sym2 V) r) (fun ω => ∀ e ∈ K, ω e = true) := by
        apply eventWeight_mono _ (bernoulliWeight_nonneg hr0 hr1)
        intro ω hω e he
        rcases hω with ⟨hab', hbc', hca'⟩
        simp only [K, Finset.mem_insert, Finset.mem_singleton] at he
        rcases he with rfl | rfl | rfl
        · exact hab'.2
        · exact hbc'.2
        · exact hca'.2
      _ = r ^ 3 := by rw [bernoulli_present_weight, hK]
  · have himpossible (ω : Sym2 V → Bool) :
        ¬ trianglePattern (bernoulliGraph G ω) (a, b, c) := by
      rintro ⟨hab, hbc, hca⟩
      exact hbase ⟨hab.1, hbc.1, hca.1⟩
    have hz : eventWeight (bernoulliWeight (E := Sym2 V) r)
        (fun ω => trianglePattern (bernoulliGraph G ω) (a, b, c)) = 0 := by
      unfold eventWeight
      apply Finset.sum_eq_zero
      intro ω _
      exact if_neg (himpossible ω)
    rw [hz]
    exact pow_nonneg hr0 _

-- Source: Er579.RandomRealization.BernoulliCycles:59
theorem bernoulli_square_weight_le [Fintype (Sym2 V)] [DecidableEq (Sym2 V)]
    (G : SimpleGraph V) (r : ℝ) (hr0 : 0 ≤ r) (hr1 : r ≤ 1) (t : V × V × V × V) :
    eventWeight (bernoulliWeight (E := Sym2 V) r)
      (fun ω => squarePattern (bernoulliGraph G ω) t) ≤ r ^ 4 := by
  rcases t with ⟨a, b, c, d⟩
  let K : Finset (Sym2 V) := {Sym2.mk a b, Sym2.mk b c, Sym2.mk c d, Sym2.mk d a}
  by_cases hbase : squarePattern G (a, b, c, d)
  · rcases hbase with ⟨hac, hbd, hab, hbc, hcd, hda⟩
    have hnab := hab.ne
    have hnbc := hbc.ne
    have hncd := hcd.ne
    have hnda := hda.ne
    have hK : K.card = 4 := by
      simp [K, hac, hbd, hnab, hnbc, hncd, hnda,
        Ne.symm hac, Ne.symm hnab, Ne.symm hnda]
    calc
      eventWeight (bernoulliWeight (E := Sym2 V) r)
          (fun ω => squarePattern (bernoulliGraph G ω) (a, b, c, d)) ≤
          eventWeight (bernoulliWeight (E := Sym2 V) r) (fun ω => ∀ e ∈ K, ω e = true) := by
        apply eventWeight_mono _ (bernoulliWeight_nonneg hr0 hr1)
        intro ω hω e he
        rcases hω with ⟨_, _, hab', hbc', hcd', hda'⟩
        simp only [K, Finset.mem_insert, Finset.mem_singleton] at he
        rcases he with rfl | rfl | rfl | rfl
        · exact hab'.2
        · exact hbc'.2
        · exact hcd'.2
        · exact hda'.2
      _ = r ^ 4 := by rw [bernoulli_present_weight, hK]
  · have himpossible (ω : Sym2 V → Bool) :
        ¬ squarePattern (bernoulliGraph G ω) (a, b, c, d) := by
      rintro ⟨hac, hbd, hab, hbc, hcd, hda⟩
      exact hbase ⟨hac, hbd, hab.1, hbc.1, hcd.1, hda.1⟩
    have hz : eventWeight (bernoulliWeight (E := Sym2 V) r)
        (fun ω => squarePattern (bernoulliGraph G ω) (a, b, c, d)) = 0 := by
      unfold eventWeight
      apply Finset.sum_eq_zero
      intro ω _
      exact if_neg (himpossible ω)
    rw [hz]
    exact pow_nonneg hr0 _

-- Source: Er579.RandomRealization.BernoulliCycles:101
theorem bernoulli_expected_short_cycles_le [Fintype V] [DecidableEq V]
    (G : SimpleGraph V) (r : ℝ) (hr0 : 0 ≤ r) (hr1 : r ≤ 1) :
    finiteExpectation (bernoulliWeight (E := Sym2 V) r)
      (fun ω => (shortCycleCount (bernoulliGraph G ω) : ℝ)) ≤
      (Fintype.card V : ℝ) ^ 3 * r ^ 3 + (Fintype.card V : ℝ) ^ 4 * r ^ 4 := by
  have htri : finiteExpectation (bernoulliWeight (E := Sym2 V) r)
      (fun ω => ((triangleOccurrences (bernoulliGraph G ω)).card : ℝ)) ≤
      (Fintype.card V : ℝ) ^ 3 * r ^ 3 := by
    have heq := finiteExpectation_card_filter (bernoulliWeight (E := Sym2 V) r)
      (Finset.univ : Finset (V × V × V))
      (fun ω t => trianglePattern (bernoulliGraph G ω) t)
    have hocc (ω : Sym2 V → Bool) : triangleOccurrences (bernoulliGraph G ω) =
        Finset.univ.filter (fun t => trianglePattern (bernoulliGraph G ω) t) := by
      unfold triangleOccurrences
      ext t
      (simp only [Finset.mem_filter, Finset.mem_univ, true_and]; rfl)
    have hrewrite : (fun ω : Sym2 V → Bool =>
        ((triangleOccurrences (bernoulliGraph G ω)).card : ℝ)) =
        (fun ω => ((Finset.univ.filter
          (fun t => trianglePattern (bernoulliGraph G ω) t)).card : ℝ)) := by
      funext ω
      rw [hocc ω]
    rw [hrewrite]
    rw [heq]
    calc
      (∑ t : V × V × V, eventWeight (bernoulliWeight (E := Sym2 V) r)
          (fun ω => trianglePattern (bernoulliGraph G ω) t)) ≤ ∑ _t : V × V × V, r ^ 3 :=
        Finset.sum_le_sum (fun t _ => bernoulli_triangle_weight_le G r hr0 hr1 t)
      _ = (Fintype.card V : ℝ) ^ 3 * r ^ 3 := by
        simp only [Finset.sum_const, Finset.card_univ, nsmul_eq_mul,
          Fintype.card_prod, Nat.cast_mul]
        ring
  have hsquare : finiteExpectation (bernoulliWeight (E := Sym2 V) r)
      (fun ω => ((squareOccurrences (bernoulliGraph G ω)).card : ℝ)) ≤
      (Fintype.card V : ℝ) ^ 4 * r ^ 4 := by
    have heq := finiteExpectation_card_filter (bernoulliWeight (E := Sym2 V) r)
      (Finset.univ : Finset (V × V × V × V))
      (fun ω t => squarePattern (bernoulliGraph G ω) t)
    have hocc (ω : Sym2 V → Bool) : squareOccurrences (bernoulliGraph G ω) =
        Finset.univ.filter (fun t => squarePattern (bernoulliGraph G ω) t) := by
      unfold squareOccurrences
      ext t
      (simp only [Finset.mem_filter, Finset.mem_univ, true_and]; rfl)
    have hrewrite : (fun ω : Sym2 V → Bool =>
        ((squareOccurrences (bernoulliGraph G ω)).card : ℝ)) =
        (fun ω => ((Finset.univ.filter
          (fun t => squarePattern (bernoulliGraph G ω) t)).card : ℝ)) := by
      funext ω
      rw [hocc ω]
    rw [hrewrite]
    rw [heq]
    calc
      (∑ t : V × V × V × V, eventWeight (bernoulliWeight (E := Sym2 V) r)
          (fun ω => squarePattern (bernoulliGraph G ω) t)) ≤ ∑ _t : V × V × V × V, r ^ 4 :=
        Finset.sum_le_sum (fun t _ => bernoulli_square_weight_le G r hr0 hr1 t)
      _ = (Fintype.card V : ℝ) ^ 4 * r ^ 4 := by
        simp only [Finset.sum_const, Finset.card_univ, nsmul_eq_mul,
          Fintype.card_prod, Nat.cast_mul]
        ring
  have hsplit : finiteExpectation (bernoulliWeight (E := Sym2 V) r)
      (fun ω => (shortCycleCount (bernoulliGraph G ω) : ℝ)) =
      finiteExpectation (bernoulliWeight (E := Sym2 V) r)
        (fun ω => ((triangleOccurrences (bernoulliGraph G ω)).card : ℝ)) +
      finiteExpectation (bernoulliWeight (E := Sym2 V) r)
        (fun ω => ((squareOccurrences (bernoulliGraph G ω)).card : ℝ)) := by
    simp only [shortCycleCount, Nat.cast_add, finiteExpectation_add]
  rw [hsplit]
  exact add_le_add htri hsquare

end Er579.RandomRealization

end

/- Source fragment: Er579.RandomRealization.BernoulliRealization. Original licenses and source proofs retained. -/

section

/-! A genuine finite realization of rational weighted profiles.  The estimates
are derived from the Bernoulli edge sample, and the conclusion holds for every
sufficiently large replication parameter. -/

namespace Er579.RandomRealization

open scoped BigOperators Classical
open Filter

variable {Q : Type*} [Fintype Q] [DecidableEq Q]

-- Source: Er579.RandomRealization.BernoulliRealization:17
theorem bernoulliA_expected_short_cycles_le (H : SimpleGraph Q) (m : Q → ℕ)
    (L : ℕ) (hL : 0 < L) :
    finiteExpectation (bernoulliWeight (E := Sym2 (BlowupVertex m L)) (aEdgeProbability L))
      (fun ω => (shortCycleCount (bernoulliGraph (profileBlowup H m L) ω) : ℝ)) ≤
      (totalMultiplicity m : ℝ) ^ 3 * (L : ℝ) ^ 3 +
        (totalMultiplicity m : ℝ) ^ 4 * (L : ℝ) ^ 4 := by
  obtain ⟨hp0, hp1⟩ := aEdgeProbability_bounds hL
  have h := bernoulli_expected_short_cycles_le (profileBlowup H m L)
    (aEdgeProbability L) hp0 hp1
  have hLne : (L : ℝ) ≠ 0 := ne_of_gt (by exact_mod_cast hL)
  have hidentity : (Fintype.card (BlowupVertex m L) : ℝ) ^ 3 * aEdgeProbability L ^ 3 +
      (Fintype.card (BlowupVertex m L) : ℝ) ^ 4 * aEdgeProbability L ^ 4 =
      (totalMultiplicity m : ℝ) ^ 3 * (L : ℝ) ^ 3 +
        (totalMultiplicity m : ℝ) ^ 4 * (L : ℝ) ^ 4 := by
    rw [blowupVertex_card]
    unfold aEdgeProbability
    push_cast
    field_simp [hLne]
  exact h.trans_eq hidentity

-- Source: Er579.RandomRealization.BernoulliRealization:37
theorem bernoulliA_numeric_estimate_lt_one (q L : ℕ) (ε : ℝ)
    (hq : 0 < q) (hε : 0 < ε) (hL : (2 : ℝ) ≤ L)
    (hthreshold : (q : ℝ) + 1 ≤ ε ^ 2 * L)
    (hcycles : 2 * ((q : ℝ) ^ 2 + (q : ℝ) ^ 3) < ε * L) :
    (2 : ℝ) ^ (q * L ^ 5) * Real.exp (-(ε ^ 2 * (L : ℝ) ^ 6)) +
      ((q : ℝ) ^ 3 * (L : ℝ) ^ 3 + (q : ℝ) ^ 4 * (L : ℝ) ^ 4) /
        (ε * ((q * L ^ 5 : ℕ) : ℝ)) < 1 := by
  have hqpos : (0 : ℝ) < q := by exact_mod_cast hq
  have hLpos : (0 : ℝ) < L := by linarith
  have hLone : (1 : ℝ) ≤ L := by linarith
  have hLne : (L : ℝ) ≠ 0 := ne_of_gt hLpos
  have hqne : (q : ℝ) ≠ 0 := ne_of_gt hqpos
  have hεne : ε ≠ 0 := ne_of_gt hε
  have hpow : (2 : ℝ) ^ (q * L ^ 5) ≤ Real.exp ((q * L ^ 5 : ℕ) : ℝ) := by
    calc
      (2 : ℝ) ^ (q * L ^ 5) ≤ Real.exp 1 ^ (q * L ^ 5) :=
        pow_le_pow_left₀ (by norm_num) (by linarith [Real.add_one_le_exp (1 : ℝ)]) _
      _ = Real.exp ((q * L ^ 5 : ℕ) : ℝ) := by
        rw [← Real.exp_nat_mul]
        simp only [mul_one]
  have hLfive : (L : ℝ) ≤ (L : ℝ) ^ 5 := le_self_pow₀ hLone (by norm_num)
  have hscale := mul_le_mul_of_nonneg_right hthreshold (pow_nonneg hLpos.le 5)
  have hexponent : ((q * L ^ 5 : ℕ) : ℝ) - ε ^ 2 * (L : ℝ) ^ 6 ≤ -(L : ℝ) := by
    push_cast
    nlinarith only [hscale, hLfive]
  have hbad : (2 : ℝ) ^ (q * L ^ 5) * Real.exp (-(ε ^ 2 * (L : ℝ) ^ 6)) ≤
      Real.exp (-(L : ℝ)) := by
    calc
      _ ≤ Real.exp ((q * L ^ 5 : ℕ) : ℝ) * Real.exp (-(ε ^ 2 * (L : ℝ) ^ 6)) :=
        mul_le_mul_of_nonneg_right hpow (Real.exp_nonneg _)
      _ = Real.exp (((q * L ^ 5 : ℕ) : ℝ) - ε ^ 2 * (L : ℝ) ^ 6) := by
        simpa only [sub_eq_add_neg] using
          (Real.exp_add ((q * L ^ 5 : ℕ) : ℝ) (-(ε ^ 2 * (L : ℝ) ^ 6))).symm
      _ ≤ Real.exp (-(L : ℝ)) := Real.exp_le_exp.mpr hexponent
  have hexp3 : (3 : ℝ) ≤ Real.exp (L : ℝ) := by
    linarith [Real.add_one_le_exp (L : ℝ)]
  have hthird : Real.exp (-(L : ℝ)) ≤ (1 / 3 : ℝ) := by
    simpa only [Real.exp_neg, one_div] using
      one_div_le_one_div_of_le (by norm_num : (0 : ℝ) < 3) hexp3
  have hfirst : (q : ℝ) ^ 3 * (L : ℝ) ^ 3 / (ε * ((q * L ^ 5 : ℕ) : ℝ)) =
      (q : ℝ) ^ 2 / (ε * (L : ℝ) ^ 2) := by
    push_cast
    field_simp [hLne, hqne, hεne]
  have hsecond : (q : ℝ) ^ 4 * (L : ℝ) ^ 4 / (ε * ((q * L ^ 5 : ℕ) : ℝ)) =
      (q : ℝ) ^ 3 / (ε * (L : ℝ)) := by
    push_cast
    field_simp [hLne, hqne, hεne]
  have hratio :
      ((q : ℝ) ^ 3 * (L : ℝ) ^ 3 + (q : ℝ) ^ 4 * (L : ℝ) ^ 4) /
        (ε * ((q * L ^ 5 : ℕ) : ℝ)) ≤
      ((q : ℝ) ^ 2 + (q : ℝ) ^ 3) / (ε * L) := by
    rw [add_div, hfirst, hsecond, add_div]
    refine add_le_add ?_ le_rfl
    exact div_le_div_of_nonneg_left (by positivity) (mul_pos hε hLpos)
      (mul_le_mul_of_nonneg_left (le_self_pow₀ hLone (by norm_num : (2 : ℕ) ≠ 0)) hε.le)
  have hhalf : ((q : ℝ) ^ 2 + (q : ℝ) ^ 3) / (ε * L) < (1 / 2 : ℝ) := by
    apply (div_lt_iff₀ (mul_pos hε hLpos)).2
    nlinarith only [hcycles]
  linarith [hbad.trans hthird, hratio.trans_lt hhalf]

-- Source: Er579.RandomRealization.BernoulliRealization:97
def GoodBernoulliRealization (H : SimpleGraph Q) (m : Q → ℕ) (L : ℕ)
    (ω : Sym2 (BlowupVertex m L) → Bool) (a ε : ℝ) : Prop :=
  TriangleFree (cleanedGraph (bernoulliGraph (profileBlowup H m L) ω)) ∧
  C4Free (cleanedGraph (bernoulliGraph (profileBlowup H m L) ω)) ∧
  ((cleanedGraph (bernoulliGraph (profileBlowup H m L) ω)).indepNum : ℝ) ≤
    (a + ε) * Fintype.card (BlowupVertex m L) ∧
  ((cleanupVertices (bernoulliGraph (profileBlowup H m L) ω)).card : ℝ) <
    ε * Fintype.card (BlowupVertex m L) ∧
  (1 - ε) * Fintype.card (BlowupVertex m L) <
    Fintype.card (CleanVertex (bernoulliGraph (profileBlowup H m L) ω)) ∧
  Fintype.card (CleanVertex (bernoulliGraph (profileBlowup H m L) ω)) ≤
    Fintype.card (BlowupVertex m L) ∧
  (∀ u v, (cleanedGraph (bernoulliGraph (profileBlowup H m L) ω)).Adj u v →
    H.Adj u.val.1 v.val.1)

-- Source: Er579.RandomRealization.BernoulliRealization:112
theorem exists_good_bernoulli_realization (H : SimpleGraph Q) (m : Q → ℕ)
    (L : ℕ) (hm : ∀ q, 1 ≤ m q) (hQ : 0 < totalMultiplicity m)
    (a ε : ℝ) (hε : 0 < ε) (hα : ProfileIndependenceBound H m a)
    (hL : (2 : ℝ) ≤ L)
    (hthreshold : (totalMultiplicity m : ℝ) + 1 ≤ ε ^ 2 * L)
    (hcycles : 2 * ((totalMultiplicity m : ℝ) ^ 2 + (totalMultiplicity m : ℝ) ^ 3) <
      ε * L) :
    ∃ ω : Sym2 (BlowupVertex m L) → Bool, GoodBernoulliRealization H m L ω a ε := by
  have hLpos : 0 < L := by exact_mod_cast (show (0 : ℝ) < L by linarith)
  have hV : (0 : ℝ) < Fintype.card (BlowupVertex m L) := by
    rw [blowupVertex_card]
    exact_mod_cast Nat.mul_pos hQ (pow_pos hLpos 5)
  have hdelete : 0 < ε * (Fintype.card (BlowupVertex m L) : ℝ) := mul_pos hε hV
  let w := bernoulliWeight (E := Sym2 (BlowupVertex m L)) (aEdgeProbability L)
  let sample := bernoulliGraph (profileBlowup H m L)
  have hbad := bernoulliA_independence_bad_weight H m L hm hLpos a ε hε.le hα
  have hcyc := div_le_div_of_nonneg_right
    (bernoulliA_expected_short_cycles_le H m L hLpos) hdelete.le
  have hsum := bernoulliA_numeric_estimate_lt_one (totalMultiplicity m) L ε
    hQ hε hL hthreshold hcycles
  have hestimates : eventWeight w (fun ω => (a + ε) * Fintype.card (BlowupVertex m L) <
      (sample ω).indepNum) + finiteExpectation w (fun ω => (shortCycleCount (sample ω) : ℝ)) /
        (ε * Fintype.card (BlowupVertex m L)) < 1 := by
    have hsum' : (2 : ℝ) ^ (totalMultiplicity m * L ^ 5) *
        Real.exp (-(ε ^ 2 * (L : ℝ) ^ 6)) +
        ((totalMultiplicity m : ℝ) ^ 3 * (L : ℝ) ^ 3 +
          (totalMultiplicity m : ℝ) ^ 4 * (L : ℝ) ^ 4) /
          (ε * Fintype.card (BlowupVertex m L)) < 1 := by
      simpa only [blowupVertex_card] using hsum
    exact (add_le_add hbad hcyc).trans_lt hsum'
  obtain ⟨ω, htri, hsquare, hα', hdelete', hcard⟩ := exists_clean_realization_from_bounds
    w (bernoulliWeight_nonneg (aEdgeProbability_bounds hLpos).1
      (aEdgeProbability_bounds hLpos).2) (bernoulliWeight_sum (aEdgeProbability L))
    sample ((a + ε) * Fintype.card (BlowupVertex m L))
    (ε * Fintype.card (BlowupVertex m L)) hdelete hestimates
  refine ⟨ω, htri, hsquare, hα', hdelete', ?_, ?_, ?_⟩
  · simp only [← Nat.card_eq_fintype_card, sample] at hcard ⊢
    nlinarith only [hcard]
  · simpa only [← Nat.card_eq_fintype_card] using
      Nat.card_le_card_of_injective
        (fun v : CleanVertex (bernoulliGraph (profileBlowup H m L) ω) => v.val)
        Subtype.val_injective
  · intro u v huv
    exact huv.1

-- Source: Er579.RandomRealization.BernoulliRealization:157
theorem eventually_exists_good_bernoulli_realization (H : SimpleGraph Q) (m : Q → ℕ)
    (hm : ∀ q, 1 ≤ m q) (hQ : 0 < totalMultiplicity m)
    (a ε : ℝ) (hε : 0 < ε) (hα : ProfileIndependenceBound H m a) :
    ∀ᶠ L : ℕ in atTop, ∃ ω : Sym2 (BlowupVertex m L) → Bool,
      GoodBernoulliRealization H m L ω a ε := by
  have hlarge := (tendsto_natCast_atTop_atTop (R := ℝ)).eventually_ge_atTop
    (max 2 (max (((totalMultiplicity m : ℝ) + 1) / ε ^ 2)
      (2 * ((totalMultiplicity m : ℝ) ^ 2 + (totalMultiplicity m : ℝ) ^ 3) / ε + 1)))
  filter_upwards [hlarge] with L hL
  have hL2 : (2 : ℝ) ≤ L := (le_max_left _ _).trans hL
  have hmid := (le_max_right 2 _).trans hL
  have hthreshold : (totalMultiplicity m : ℝ) + 1 ≤ ε ^ 2 * L := by
    have hquot := (le_max_left _ _).trans hmid
    have hmul := (div_le_iff₀ (pow_pos hε 2)).1 hquot
    simpa only [mul_comm] using hmul
  have hcycles : 2 * ((totalMultiplicity m : ℝ) ^ 2 + (totalMultiplicity m : ℝ) ^ 3) <
      ε * L := by
    have hquot := (le_max_right _ _).trans hmid
    have hstrict : 2 * ((totalMultiplicity m : ℝ) ^ 2 + (totalMultiplicity m : ℝ) ^ 3) / ε < L := by
      linarith
    have hmul := (div_lt_iff₀ hε).1 hstrict
    simpa only [mul_comm] using hmul
  exact exists_good_bernoulli_realization H m L hm hQ a ε hε hα hL2 hthreshold hcycles

end Er579.RandomRealization

end

/- Source fragment: Er579.RandomRealization.MatchingCover. Original licenses and source proofs retained. -/

section

/-! The deterministic graph carried by a system of perfect matchings.
The symmetry condition makes the system one matching per unordered edge,
rather than two unrelated directed matchings. -/

namespace Er579.RandomRealization

-- Source: Er579.RandomRealization.MatchingCover:12
structure MatchingSystem (Q F : Type*) where
  matching : Q → Q → Equiv.Perm F
  reverse : ∀ a b, matching b a = (matching a b).symm

variable {Q F : Type*}

-- Source: Er579.RandomRealization.MatchingCover:18
def matchingCover (G : SimpleGraph Q) (σ : MatchingSystem Q F) : SimpleGraph (Q × F) where
  Adj x y := G.Adj x.1 y.1 ∧ σ.matching x.1 y.1 x.2 = y.2
  symm := by
    constructor
    intro x y h
    refine ⟨h.1.symm, ?_⟩
    rw [σ.reverse x.1 y.1, ← h.2]
    exact (σ.matching x.1 y.1).symm_apply_apply x.2
  loopless := by
    constructor
    intro x h
    exact G.irrefl h.1

-- Source: Er579.RandomRealization.MatchingCover:35
theorem matchingCover_neighbors_same_label (G : SimpleGraph Q) (σ : MatchingSystem Q F)
    {b w z : Q × F} (hbw : (matchingCover G σ).Adj b w)
    (hbz : (matchingCover G σ).Adj b z) (hlabel : w.1 = z.1) : w = z := by
  apply Prod.ext hlabel
  have hfirst : σ.matching b.1 w.1 b.2 = w.2 := hbw.2
  have hsecond : σ.matching b.1 z.1 b.2 = z.2 := hbz.2
  rw [← hlabel] at hsecond
  exact hfirst.symm.trans hsecond

-- Source: Er579.RandomRealization.MatchingCover:44
theorem matchingCover_leaf_separation (G : SimpleGraph Q) (σ : MatchingSystem Q F) :
    ∀ b w z, (matchingCover G σ).Adj b w → (matchingCover G σ).Adj b z →
      w ≠ z → w.1 ≠ z.1 := by
  intro b w z hbw hbz hwz hlabel
  exact hwz (matchingCover_neighbors_same_label G σ hbw hbz hlabel)

-- Source: Er579.RandomRealization.MatchingCover:50
theorem matchingCover_triangleFree (G : SimpleGraph Q) (σ : MatchingSystem Q F)
    (hG : TriangleFree G) : TriangleFree (matchingCover G σ) := by
  intro a b c hab hbc hca
  exact hG a.1 b.1 c.1 hab.1 hbc.1 hca.1

-- Source: Er579.RandomRealization.MatchingCover:55
theorem matchingCover_square_projection (G : SimpleGraph Q) (σ : MatchingSystem Q F)
    {a b c d : Q × F} (hac : a ≠ c) (hbd : b ≠ d)
    (hab : (matchingCover G σ).Adj a b) (hbc : (matchingCover G σ).Adj b c)
    (hcd : (matchingCover G σ).Adj c d) (hda : (matchingCover G σ).Adj d a) :
    a.1 ≠ c.1 ∧ b.1 ≠ d.1 ∧
      G.Adj a.1 b.1 ∧ G.Adj b.1 c.1 ∧ G.Adj c.1 d.1 ∧ G.Adj d.1 a.1 := by
  refine ⟨?_, ?_, hab.1, hbc.1, hcd.1, hda.1⟩
  · exact matchingCover_leaf_separation G σ b a c hab.symm hbc hac
  · exact matchingCover_leaf_separation G σ a b d hab hda.symm hbd

section OrientedSystems

variable [LinearOrder Q]

-- Source: Er579.RandomRealization.MatchingCover:76
/-- Only the permutation for a<b is used for the unordered pair {a,b}.
Diagonal entries are the identity, and lower-triangular entries are inverses.
Randomizing the upper-triangular entries therefore gives independent
perfect matchings on all simple base edges. -/
def orientPermutations (p : Q → Q → Equiv.Perm F) : MatchingSystem Q F where
  matching a b := if a < b then p a b else if a = b then Equiv.refl F else (p b a).symm
  reverse := by
    intro a b
    rcases lt_trichotomy a b with hab | hab | hab
    · simp [hab, not_lt_of_ge hab.le, Ne.symm (ne_of_lt hab)]
    · subst b
      simp
    · simp [hab, ne_of_gt hab, not_lt_of_ge hab.le]

end OrientedSystems

end Er579.RandomRealization

end

/- Source fragment: Er579.RandomRealization.MatchingProbability. Original licenses and source proofs retained. -/

section

namespace Er579.RandomRealization

open scoped BigOperators Classical

variable {F : Type*} [Fintype F]

-- Source: Er579.RandomRealization.MatchingProbability:13
noncomputable def uniformPermWeight (_σ : Equiv.Perm F) : ℝ :=
  1 / Fintype.card (Equiv.Perm F)

-- Source: Er579.RandomRealization.MatchingProbability:16
def Avoids (A B : Finset F) (σ : Equiv.Perm F) : Prop :=
  ∀ x ∈ A, σ x ∉ B

-- Source: Er579.RandomRealization.MatchingProbability:19
theorem uniformPermWeight_nonneg (σ : Equiv.Perm F) : 0 ≤ uniformPermWeight σ := by
  unfold uniformPermWeight
  positivity

-- Source: Er579.RandomRealization.MatchingProbability:23
theorem uniformPermWeight_sum : (∑ σ : Equiv.Perm F, uniformPermWeight σ) = 1 := by
  classical
  have hpos : 0 < Fintype.card (Equiv.Perm F) := Fintype.card_pos_iff.mpr ⟨Equiv.refl F⟩
  simp only [uniformPermWeight, Finset.sum_const, Finset.card_univ, nsmul_eq_mul]
  field_simp

-- Source: Er579.RandomRealization.MatchingProbability:29
theorem uniformPerm_eventWeight (E : Equiv.Perm F → Prop) :
    eventWeight uniformPermWeight E =
      (Fintype.card {σ : Equiv.Perm F // E σ} : ℝ) / Fintype.card (Equiv.Perm F) := by
  classical
  unfold eventWeight uniformPermWeight
  have hterm : ∀ σ : Equiv.Perm F,
      (if E σ then 1 / (Fintype.card (Equiv.Perm F) : ℝ) else 0) =
        (if E σ then (1 : ℝ) else 0) / Fintype.card (Equiv.Perm F) := by
    intro σ
    split_ifs <;> simp
  simp_rw [hterm]
  rw [← Finset.sum_div]
  congr 1
  simp [Fintype.card_subtype]

-- Source: Er579.RandomRealization.MatchingProbability:44
private noncomputable def avoidanceFiberEquiv (A B : Finset F) (x : F) (hx : x ∉ A)
    (y : F) (hy : y ∈ B) :
    {σ : Equiv.Perm F // Avoids A B σ} ≃
      ({τ : Equiv.Perm F // Avoids A B τ ∧ τ x = y} × {z : F // z ∉ A}) where
  toFun σ := by
    let z := σ.val.symm y
    have hz : z ∉ A := by
      intro hzA
      exact σ.property z hzA (by simpa [z] using hy)
    let τ := (Equiv.swap x z).trans σ.val
    have hτ : Avoids A B τ := by
      intro u hu
      have hux : u ≠ x := fun h => hx (h ▸ hu)
      have huz : u ≠ z := fun h => hz (h ▸ hu)
      simpa only [τ, Equiv.trans_apply, Equiv.swap_apply_of_ne_of_ne hux huz] using
        σ.property u hu
    have hτx : τ x = y := by simp [τ, z]
    exact (⟨τ, hτ, hτx⟩, ⟨z, hz⟩)
  invFun t := by
    let σ := (Equiv.swap x t.2.val).trans t.1.val
    have hσ : Avoids A B σ := by
      intro u hu
      have hux : u ≠ x := fun h => hx (h ▸ hu)
      have huz : u ≠ t.2.val := fun h => t.2.property (h ▸ hu)
      simpa only [σ, Equiv.trans_apply, Equiv.swap_apply_of_ne_of_ne hux huz] using
        t.1.property.1 u hu
    exact ⟨σ, hσ⟩
  left_inv σ := by
    apply Subtype.ext
    ext u
    simp [Equiv.trans_apply]
  right_inv t := by
    have hz : ((Equiv.swap x t.2.val).trans t.1.val).symm y = t.2.val := by
      apply ((Equiv.swap x t.2.val).trans t.1.val).injective
      simp only [Equiv.apply_symm_apply, Equiv.trans_apply, Equiv.swap_apply_right]
      exact t.1.property.2.symm
    have ht : t.1.val.symm y = x := by
      exact (congrArg t.1.val.symm t.1.property.2).symm.trans
        (t.1.val.symm_apply_apply x)
    apply Prod.ext
    · apply Subtype.ext
      ext u
      simp [ht, Equiv.trans_apply]
    · apply Subtype.ext
      exact hz

-- Source: Er579.RandomRealization.MatchingProbability:90
/-- Fixing the image of one unexposed input has exactly |F|-|A| preimages. -/
theorem avoidance_fixed_image_card (A B : Finset F) (x y : F) (hx : x ∉ A) (hy : y ∈ B) :
    Fintype.card {σ : Equiv.Perm F // Avoids A B σ} =
      Fintype.card {τ : Equiv.Perm F // Avoids A B τ ∧ τ x = y} *
        (Fintype.card F - A.card) := by
  classical
  have hcard := Fintype.card_congr (avoidanceFiberEquiv A B x hx y hy)
  simpa only [Fintype.card_prod, Fintype.card_subtype_compl, Fintype.card_coe] using hcard

-- Source: Er579.RandomRealization.MatchingProbability:99
/-- A single prescribed image under a uniform permutation has probability exactly 1/|F|. -/
theorem uniformPerm_single_image (x y : F) :
    eventWeight uniformPermWeight (fun σ : Equiv.Perm F => σ x = y) =
      1 / (Fintype.card F : ℝ) := by
  classical
  have hcard : Fintype.card (Equiv.Perm F) =
      Fintype.card {σ : Equiv.Perm F // σ x = y} * Fintype.card F := by
    simpa [Avoids] using avoidance_fixed_image_card (∅ : Finset F) {y} x y
      (by simp) (by simp)
  have hM : 0 < (Fintype.card (Equiv.Perm F) : ℝ) := by
    exact_mod_cast (Fintype.card_pos_iff.mpr ⟨Equiv.refl F⟩)
  have hL : 0 < (Fintype.card F : ℝ) := by
    exact_mod_cast (Fintype.card_pos_iff.mpr ⟨x⟩)
  rw [uniformPerm_eventWeight]
  apply (div_eq_div_iff (ne_of_gt hM) (ne_of_gt hL)).2
  norm_num only [one_mul]
  exact_mod_cast hcard.symm

-- Source: Er579.RandomRealization.MatchingProbability:117
theorem uniformPerm_single_inverse_image (x y : F) :
    eventWeight uniformPermWeight (fun σ : Equiv.Perm F => σ.symm x = y) =
      1 / (Fintype.card F : ℝ) := by
  have hevent : (fun σ : Equiv.Perm F => σ.symm x = y) =
      (fun σ : Equiv.Perm F => σ y = x) := by
    funext σ
    apply propext
    constructor
    · intro h
      exact (congrArg σ h).symm.trans (σ.apply_symm_apply x)
    · intro h
      exact (congrArg σ.symm h).symm.trans (σ.symm_apply_apply y)
  rw [hevent]
  exact uniformPerm_single_image y x

-- Source: Er579.RandomRealization.MatchingProbability:132
private noncomputable def avoidanceBadEquiv (A B : Finset F) (x : F) :
    {σ : Equiv.Perm F // Avoids A B σ ∧ σ x ∈ B} ≃
      (Σ y : B, {σ : Equiv.Perm F // Avoids A B σ ∧ σ x = y.val}) where
  toFun σ := ⟨⟨σ.val x, σ.property.2⟩, ⟨σ.val, σ.property.1, rfl⟩⟩
  invFun t := ⟨t.2.val, t.2.property.1, t.2.property.2.symm ▸ t.1.property⟩
  left_inv σ := by apply Subtype.ext; rfl
  right_inv t := by
    rcases t with ⟨⟨y, hy⟩, ⟨σ, hσ, hxy⟩⟩
    change σ x = y at hxy
    subst y
    rfl

-- Source: Er579.RandomRealization.MatchingProbability:144
theorem avoidance_bad_card_mul (A B : Finset F) (x : F) (hx : x ∉ A) :
    Fintype.card {σ : Equiv.Perm F // Avoids A B σ ∧ σ x ∈ B} *
      (Fintype.card F - A.card) =
        Fintype.card {σ : Equiv.Perm F // Avoids A B σ} * B.card := by
  classical
  have hcard := Fintype.card_congr (avoidanceBadEquiv A B x)
  rw [Fintype.card_sigma] at hcard
  calc
    Fintype.card {σ : Equiv.Perm F // Avoids A B σ ∧ σ x ∈ B} *
        (Fintype.card F - A.card)
      = (∑ y : B, Fintype.card {σ : Equiv.Perm F // Avoids A B σ ∧ σ x = y.val}) *
          (Fintype.card F - A.card) := congrArg (· * (Fintype.card F - A.card)) hcard
    _ = ∑ y : B, Fintype.card {σ : Equiv.Perm F // Avoids A B σ} := by
      rw [Finset.sum_mul]
      apply Finset.sum_congr rfl
      intro y _
      exact (avoidance_fixed_image_card A B x y.val hx y.property).symm
    _ = Fintype.card {σ : Equiv.Perm F // Avoids A B σ} * B.card := by
      simp [mul_comm]

omit [Fintype F] in

-- Source: Er579.RandomRealization.MatchingProbability:165
theorem avoids_insert_iff (A B : Finset F) (x : F) (σ : Equiv.Perm F) :
    Avoids (insert x A) B σ ↔ Avoids A B σ ∧ σ x ∉ B := by
  classical
  constructor
  · intro h
    exact ⟨fun u hu => h u (Finset.mem_insert_of_mem hu), h x (Finset.mem_insert_self x A)⟩
  · rintro ⟨hA, hx⟩ u hu
    rcases Finset.mem_insert.1 hu with rfl | hu
    · exact hx
    · exact hA u hu

-- Source: Er579.RandomRealization.MatchingProbability:176
theorem avoidance_partition_card (A B : Finset F) (x : F) :
    Fintype.card {σ : Equiv.Perm F // Avoids (insert x A) B σ} +
      Fintype.card {σ : Equiv.Perm F // Avoids A B σ ∧ σ x ∈ B} =
        Fintype.card {σ : Equiv.Perm F // Avoids A B σ} := by
  classical
  have hsum := Fintype.card_congr
    (Equiv.sumCompl (fun σ : {σ : Equiv.Perm F // Avoids A B σ} => σ.val x ∈ B))
  rw [Fintype.card_sum] at hsum
  have hbad := Fintype.card_congr
    (Equiv.subtypeSubtypeEquivSubtypeInter (Avoids A B) (fun σ => σ x ∈ B))
  have hgood := Fintype.card_congr
    ((Equiv.subtypeSubtypeEquivSubtypeInter (Avoids A B) (fun σ => σ x ∉ B)).trans
      (Equiv.subtypeEquivRight (fun σ => (avoids_insert_iff A B x σ).symm)))
  rw [hbad, hgood] at hsum
  omega

-- Source: Er579.RandomRealization.MatchingProbability:192
/-- Sampling without replacement never increases the chance to avoid the blocked set. -/
theorem uniformPerm_avoidance_step (A B : Finset F) (x : F) (hx : x ∉ A) :
    eventWeight uniformPermWeight (Avoids (insert x A) B) ≤
      eventWeight uniformPermWeight (Avoids A B) *
        (1 - (B.card : ℝ) / Fintype.card F) := by
  classical
  have hpart := avoidance_partition_card A B x
  have hbad := avoidance_bad_card_mul A B x hx
  have hbad_le :
      Fintype.card {σ : Equiv.Perm F // Avoids A B σ} * B.card ≤
        Fintype.card {σ : Equiv.Perm F // Avoids A B σ ∧ σ x ∈ B} * Fintype.card F := by
    rw [← hbad]
    exact Nat.mul_le_mul_left _ (Nat.sub_le _ _)
  have hstep :
      Fintype.card {σ : Equiv.Perm F // Avoids (insert x A) B σ} * Fintype.card F +
        Fintype.card {σ : Equiv.Perm F // Avoids A B σ} * B.card ≤
          Fintype.card {σ : Equiv.Perm F // Avoids A B σ} * Fintype.card F := by
    nlinarith
  have hstepR :
      (Fintype.card {σ : Equiv.Perm F // Avoids (insert x A) B σ} : ℝ) * Fintype.card F +
        (Fintype.card {σ : Equiv.Perm F // Avoids A B σ} : ℝ) * B.card ≤
          (Fintype.card {σ : Equiv.Perm F // Avoids A B σ} : ℝ) * Fintype.card F := by
    exact_mod_cast hstep
  have hL : 0 < (Fintype.card F : ℝ) := by
    exact_mod_cast (lt_of_le_of_lt (Nat.zero_le A.card) (Finset.card_lt_univ_of_notMem hx))
  have hone : 1 - (B.card : ℝ) / Fintype.card F =
      ((Fintype.card F : ℝ) - B.card) / Fintype.card F := by
    field_simp
  have hgood : (Fintype.card {σ : Equiv.Perm F // Avoids (insert x A) B σ} : ℝ) ≤
      (Fintype.card {σ : Equiv.Perm F // Avoids A B σ} : ℝ) *
        (1 - (B.card : ℝ) / Fintype.card F) := by
    rw [hone, ← mul_div_assoc]
    apply (le_div_iff₀ hL).2
    nlinarith
  rw [uniformPerm_eventWeight, uniformPerm_eventWeight]
  calc
    (Fintype.card {σ : Equiv.Perm F // Avoids (insert x A) B σ} : ℝ) /
        Fintype.card (Equiv.Perm F)
      ≤ ((Fintype.card {σ : Equiv.Perm F // Avoids A B σ} : ℝ) *
          (1 - (B.card : ℝ) / Fintype.card F)) / Fintype.card (Equiv.Perm F) :=
        div_le_div_of_nonneg_right hgood (by positivity)
    _ = ((Fintype.card {σ : Equiv.Perm F // Avoids A B σ} : ℝ) /
          Fintype.card (Equiv.Perm F)) * (1 - (B.card : ℝ) / Fintype.card F) := by ring

-- Source: Er579.RandomRealization.MatchingProbability:236
theorem avoidance_factor_nonneg (B : Finset F) :
    0 ≤ 1 - (B.card : ℝ) / Fintype.card F := by
  apply sub_nonneg.mpr
  apply div_le_one_of_le₀
  · exact_mod_cast B.card_le_univ
  · positivity

-- Source: Er579.RandomRealization.MatchingProbability:243
/-- An elementary negative-association bound for images sampled without replacement. -/
theorem uniformPerm_avoids_le_pow (A B : Finset F) :
    eventWeight uniformPermWeight (Avoids A B) ≤
      (1 - (B.card : ℝ) / Fintype.card F) ^ A.card := by
  classical
  have hfactor := avoidance_factor_nonneg B
  induction A using Finset.induction_on with
  | empty =>
    have h : eventWeight uniformPermWeight (Avoids (∅ : Finset F) B) = 1 := by
      simpa [eventWeight, Avoids] using (uniformPermWeight_sum (F := F))
    simpa only [Finset.card_empty, pow_zero] using h.le
  | @insert x A hx ih =>
    calc
      eventWeight uniformPermWeight (Avoids (insert x A) B)
        ≤ eventWeight uniformPermWeight (Avoids A B) *
            (1 - (B.card : ℝ) / Fintype.card F) := uniformPerm_avoidance_step A B x hx
      _ ≤ (1 - (B.card : ℝ) / Fintype.card F) ^ A.card *
            (1 - (B.card : ℝ) / Fintype.card F) := mul_le_mul_of_nonneg_right ih hfactor
      _ = (1 - (B.card : ℝ) / Fintype.card F) ^ (insert x A).card := by
        rw [Finset.card_insert_of_notMem hx, pow_succ]

-- Source: Er579.RandomRealization.MatchingProbability:264
/-- The exact exponential estimate used by the independence first moment for matching covers. -/
theorem uniformPerm_avoids_le_exp (A B : Finset F) :
    eventWeight uniformPermWeight (Avoids A B) ≤
      Real.exp (-((A.card : ℝ) * B.card) / Fintype.card F) := by
  calc
    eventWeight uniformPermWeight (Avoids A B)
      ≤ (1 - (B.card : ℝ) / Fintype.card F) ^ A.card := uniformPerm_avoids_le_pow A B
    _ ≤ Real.exp (-(B.card : ℝ) / Fintype.card F) ^ A.card := by
      apply pow_le_pow_left₀ (avoidance_factor_nonneg B)
      simpa only [neg_div, sub_eq_add_neg, add_comm] using
        Real.add_one_le_exp (-(B.card : ℝ) / Fintype.card F)
    _ = Real.exp (-((A.card : ℝ) * B.card) / Fintype.card F) := by
      rw [← Real.exp_nat_mul]
      congr 1
      ring

end Er579.RandomRealization

end

/- Source fragment: Er579.RandomRealization.VertexSampling. Original licenses and source proofs retained. -/

section

/-! Independent vertex selection, including the exact first moments of
the selected order and of the selected (unordered) edge count. -/

namespace Er579.RandomRealization

open scoped BigOperators Classical

variable {V : Type*} [Fintype V]

-- Source: Er579.RandomRealization.VertexSampling:15
def vertexSamplingWeight (x : V → ℝ) (ω : V → Bool) : ℝ :=
  productWeight (fun v => bernoulliBitWeight (x v)) ω

-- Source: Er579.RandomRealization.VertexSampling:18
theorem vertexSamplingWeight_sum (x : V → ℝ) : ∑ ω, vertexSamplingWeight x ω = 1 :=
  productWeight_sum _ (fun v => bernoulliBitWeight_sum (x v))

-- Source: Er579.RandomRealization.VertexSampling:21
theorem vertexSamplingWeight_nonneg (x : V → ℝ) (hx0 : ∀ v, 0 ≤ x v)
    (hx1 : ∀ v, x v ≤ 1) (ω : V → Bool) : 0 ≤ vertexSamplingWeight x ω := by
  apply productWeight_nonneg
  intro v b
  cases b <;> simp only [bernoulliBitWeight, Bool.false_eq_true, if_false, if_true]
  · exact sub_nonneg.mpr (hx1 v)
  · exact hx0 v

-- Source: Er579.RandomRealization.VertexSampling:29
theorem vertexSampling_selected_weight (x : V → ℝ) (S : Finset V) :
    eventWeight (vertexSamplingWeight x) (fun ω => ∀ v ∈ S, ω v = true) = ∏ v ∈ S, x v := by
  unfold vertexSamplingWeight
  change eventWeight (productWeight (fun v => bernoulliBitWeight (x v)))
    (fun ω => ∀ v, v ∈ S → ω v = true) = _
  rw [productWeight_event _ (fun v b => v ∈ S → b = true)]
  have hcoord (v : V) : eventWeight (bernoulliBitWeight (x v))
      (fun b => v ∈ S → b = true) = if v ∈ S then x v else 1 := by
    unfold eventWeight
    by_cases hv : v ∈ S
    · simp [hv, bernoulliBitWeight]
    · simp [hv, bernoulliBitWeight]
  simp_rw [hcoord]
  simp only [Finset.prod_ite_mem, Finset.univ_inter]

-- Source: Er579.RandomRealization.VertexSampling:44
theorem vertexSampling_single_weight (x : V → ℝ) (v : V) :
    eventWeight (vertexSamplingWeight x) (fun ω => ω v = true) = x v := by
  simpa using vertexSampling_selected_weight x ({v} : Finset V)

-- Source: Er579.RandomRealization.VertexSampling:48
noncomputable def selectedVertices (ω : V → Bool) : Finset V :=
  Finset.univ.filter (fun v => ω v = true)

-- Source: Er579.RandomRealization.VertexSampling:51
theorem selectedVertices_card (ω : V → Bool) :
    ((selectedVertices ω).card : ℝ) = ∑ v, if ω v = true then (1 : ℝ) else 0 :=
  Finset.natCast_card_filter _ _

-- Source: Er579.RandomRealization.VertexSampling:55
theorem vertexSampling_expected_order (x : V → ℝ) :
    finiteExpectation (vertexSamplingWeight x) (fun ω => ((selectedVertices ω).card : ℝ)) =
      ∑ v, x v := by
  simp_rw [selectedVertices_card]
  rw [finiteExpectation_sum]
  apply Finset.sum_congr rfl
  intro v _
  have hindicator : finiteExpectation (vertexSamplingWeight x)
      (fun ω => if ω v = true then (1 : ℝ) else 0) =
      eventWeight (vertexSamplingWeight x) (fun ω => ω v = true) := by
    unfold finiteExpectation eventWeight
    apply Finset.sum_congr rfl
    intro ω _
    by_cases h : ω v = true <;> simp [h]
  rw [hindicator, vertexSampling_single_weight]

-- Source: Er579.RandomRealization.VertexSampling:71
def symmetricEdgeWeight (x : V → ℝ) : Sym2 V → ℝ :=
  Sym2.lift ⟨fun u v => x u * x v, fun u v => mul_comm (x u) (x v)⟩

-- Source: Er579.RandomRealization.VertexSampling:74
noncomputable def weightedEdgeSum (G : SimpleGraph V) (x : V → ℝ) : ℝ :=
  ∑ e ∈ G.edgeFinset, symmetricEdgeWeight x e

-- Source: Er579.RandomRealization.VertexSampling:77
noncomputable def selectedEdges (G : SimpleGraph V) (ω : V → Bool) : Finset (Sym2 V) :=
  G.edgeFinset.filter (fun e => ∀ v ∈ e.toFinset, ω v = true)

-- Source: Er579.RandomRealization.VertexSampling:80
theorem vertexSampling_edge_weight (G : SimpleGraph V) (x : V → ℝ)
    (e : Sym2 V) (he : e ∈ G.edgeFinset) :
    eventWeight (vertexSamplingWeight x) (fun ω => ∀ v ∈ e.toFinset, ω v = true) =
      symmetricEdgeWeight x e := by
  rw [vertexSampling_selected_weight]
  obtain ⟨u, v⟩ := e
  have hne : u ≠ v := G.ne_of_adj (SimpleGraph.mem_edgeFinset.mp he)
  simp [Sym2.toFinset_mk_eq, hne, symmetricEdgeWeight, Sym2.lift_mk]

-- Source: Er579.RandomRealization.VertexSampling:89
theorem vertexSampling_expected_edges (G : SimpleGraph V) (x : V → ℝ) :
    finiteExpectation (vertexSamplingWeight x) (fun ω => ((selectedEdges G ω).card : ℝ)) =
      weightedEdgeSum G x := by
  have hcard (ω : V → Bool) : ((selectedEdges G ω).card : ℝ) =
      ∑ e ∈ G.edgeFinset, if ∀ v ∈ e.toFinset, ω v = true then (1 : ℝ) else 0 :=
    Finset.natCast_card_filter _ _
  simp_rw [hcard]
  rw [finiteExpectation_sum]
  unfold weightedEdgeSum
  apply Finset.sum_congr rfl
  intro e he
  have hindicator : finiteExpectation (vertexSamplingWeight x)
      (fun ω => if ∀ v ∈ e.toFinset, ω v = true then (1 : ℝ) else 0) =
      eventWeight (vertexSamplingWeight x) (fun ω => ∀ v ∈ e.toFinset, ω v = true) := by
    unfold finiteExpectation eventWeight
    apply Finset.sum_congr rfl
    intro ω _
    by_cases h : ∀ v ∈ e.toFinset, ω v = true <;> simp [h]
  rw [hindicator]
  exact vertexSampling_edge_weight G x e he

-- Source: Er579.RandomRealization.VertexSampling:110
theorem selectedEdges_card_induce (G : SimpleGraph V) (ω : V → Bool) :
    (selectedEdges G ω).card = (G.induce ((selectedVertices ω : Finset V) : Set V)).edgeFinset.card := by
  have hset : selectedEdges G ω =
      G.edgeFinset.filter (fun e => e.toFinset ⊆ selectedVertices ω) := by
    ext e
    simp only [selectedEdges, Finset.mem_filter, Finset.subset_iff,
      selectedVertices, Finset.mem_univ, true_and]
  rw [hset]
  exact SimpleGraph.card_filter_edgeFinset_toFinset_subset (G := G) (selectedVertices ω)

end Er579.RandomRealization

end

/- Source fragment: Er579.RandomRealization.WeightedTuran. Original licenses and source proofs retained. -/

section

/-! The polynomial form of the independence/edge inequality.  Division is
postponed until a positive numerical bound on the independence number is
available, so the empty graph has no exceptional denominator. -/

namespace Er579.RandomRealization

open scoped Classical BigOperators

variable {V : Type*} [Fintype V]

-- Source: Er579.RandomRealization.WeightedTuran:15
theorem edge_count_add_complement (G : SimpleGraph V) :
    G.edgeFinset.card + Gᶜ.edgeFinset.card = (Fintype.card V).choose 2 := by
  classical
  have hd : Disjoint G.edgeFinset Gᶜ.edgeFinset :=
    SimpleGraph.disjoint_edgeFinset.mpr disjoint_compl_right
  rw [← Finset.card_union_of_disjoint hd, ← SimpleGraph.edgeFinset_sup]
  have htop : (G ⊔ Gᶜ).edgeFinset = (⊤ : SimpleGraph V).edgeFinset :=
    SimpleGraph.edgeFinset_inj.mpr sup_compl_eq_top
  rw [htop]
  exact SimpleGraph.card_edgeFinset_top_eq_card_choose_two

-- Source: Er579.RandomRealization.WeightedTuran:26
theorem ordinary_turan_polynomial (G : SimpleGraph V) :
    (Fintype.card V : ℝ) ^ 2 ≤
      (G.indepNum : ℝ) * (2 * (G.edgeFinset.card : ℝ) + Fintype.card V) := by
  classical
  by_cases hN : Fintype.card V = 0
  · simp only [hN, Nat.cast_zero, zero_pow (by decide : 2 ≠ 0), add_zero]
    positivity
  have hNpos : 0 < Fintype.card V := Nat.pos_of_ne_zero hN
  have hNge : 1 ≤ Fintype.card V := hNpos
  obtain ⟨v⟩ := Fintype.card_pos_iff.mp hNpos
  have hs : G.IsIndepSet (({v} : Finset V) : Set V) := by
    intro x hx y hy hxy
    have hx' : x = v := by simpa using hx
    have hy' : y = v := by simpa using hy
    exact (hxy (hx'.trans hy'.symm)).elim
  have ha : 1 ≤ G.indepNum := by
    simpa only [Finset.card_singleton] using hs.card_le_indepNum
  have hcf : Gᶜ.CliqueFree (G.indepNum + 1) := by
    intro s hs
    have hcard := hs.isClique.card_le_cliqueNum
    rw [hs.card_eq, SimpleGraph.cliqueNum_compl] at hcard
    omega
  have hupper : Gᶜ.edgeFinset.card ≤
      (SimpleGraph.turanGraph (Fintype.card V) G.indepNum).edgeFinset.card := by
    simpa only [SimpleGraph.card_edgeFinset_turanGraph] using hcf.card_edgeFinset_le
  have hraw : 2 * G.indepNum * Gᶜ.edgeFinset.card ≤
      (G.indepNum - 1) * (Fintype.card V) ^ 2 :=
    (Nat.mul_le_mul_left (2 * G.indepNum) hupper).trans
      (SimpleGraph.mul_card_edgeFinset_turanGraph_le)
  have hreal : ((2 * G.indepNum * Gᶜ.edgeFinset.card : ℕ) : ℝ) ≤
      (((G.indepNum - 1) * (Fintype.card V) ^ 2 : ℕ) : ℝ) := by
    exact_mod_cast hraw
  norm_num only [Nat.cast_mul, Nat.cast_ofNat, Nat.cast_pow, Nat.cast_sub ha,
    Nat.cast_one] at hreal
  have hcomp : (G.edgeFinset.card : ℝ) + (Gᶜ.edgeFinset.card : ℝ) =
      ((Fintype.card V).choose 2 : ℝ) := by
    exact_mod_cast edge_count_add_complement G
  have hchoose_nat : 2 * (Fintype.card V).choose 2 =
      Fintype.card V * (Fintype.card V - 1) := by
    rw [Nat.choose_two_right, Nat.mul_comm 2,
      Nat.div_mul_cancel (Nat.even_mul_pred_self _).two_dvd]
  have hchoose : (2 : ℝ) * ((Fintype.card V).choose 2 : ℝ) =
      (Fintype.card V : ℝ) * ((Fintype.card V : ℝ) - 1) := by
    have hcast : ((2 * (Fintype.card V).choose 2 : ℕ) : ℝ) =
        ((Fintype.card V * (Fintype.card V - 1) : ℕ) : ℝ) := by
      exact_mod_cast hchoose_nat
    simpa only [Nat.cast_mul, Nat.cast_ofNat, Nat.cast_sub hNge, Nat.cast_one] using hcast
  have hbalance : 2 * (G.indepNum : ℝ) *
      ((G.edgeFinset.card : ℝ) + (Gᶜ.edgeFinset.card : ℝ)) =
      (G.indepNum : ℝ) * ((Fintype.card V : ℝ) ^ 2 - Fintype.card V) := by
    rw [hcomp]
    nlinarith [congrArg (fun x : ℝ => (G.indepNum : ℝ) * x) hchoose]
  nlinarith

-- Source: Er579.RandomRealization.WeightedTuran:80
theorem indepNum_induce_le (G : SimpleGraph V) (S : Set V) :
    (G.induce S).indepNum ≤ G.indepNum := by
  classical
  obtain ⟨s, hs⟩ := (G.induce S).exists_isNIndepSet_indepNum
  have hI : G.IsIndepSet ((s.image Subtype.val : Finset V) : Set V) := by
    intro x hx y hy hxy
    obtain ⟨a, ha, rfl⟩ := Finset.mem_image.mp hx
    obtain ⟨b, hb, rfl⟩ := Finset.mem_image.mp hy
    exact hs.isIndepSet ha hb (fun hab => hxy (congrArg Subtype.val hab))
  have hcard : (s.image Subtype.val).card = (G.induce S).indepNum := by
    rw [Finset.card_image_of_injective _ Subtype.val_injective, hs.card_eq]
  simpa only [hcard] using hI.card_le_indepNum

-- Source: Er579.RandomRealization.WeightedTuran:93
theorem induced_turan_polynomial (G : SimpleGraph V) (S : Finset V) :
    (S.card : ℝ) ^ 2 ≤ (G.indepNum : ℝ) *
      (2 * ((G.induce (S : Set V)).edgeFinset.card : ℝ) + S.card) := by
  have h := ordinary_turan_polynomial (G.induce (S : Set V))
  have hm : ((G.induce (S : Set V)).indepNum : ℝ) ≤ G.indepNum := by
    exact_mod_cast indepNum_induce_le G (S : Set V)
  have hfactor : 0 ≤ (2 * ((G.induce (S : Set V)).edgeFinset.card : ℝ) + S.card) := by
    positivity
  have h' : (S.card : ℝ) ^ 2 ≤ ((G.induce (S : Set V)).indepNum : ℝ) *
      (2 * ((G.induce (S : Set V)).edgeFinset.card : ℝ) + S.card) := by
    have hcard : Fintype.card (S : Set V) = S.card :=
      Fintype.card_of_subtype S (fun _ => Iff.rfl)
    simpa only [hcard, SimpleGraph.edgeFinset_card, ← Nat.card_eq_fintype_card] using h
  exact h'.trans (mul_le_mul_of_nonneg_right hm hfactor)

-- Source: Er579.RandomRealization.WeightedTuran:108
theorem weighted_turan_polynomial (G : SimpleGraph V) (x : V → ℝ)
    (hx0 : ∀ v, 0 ≤ x v) (hx1 : ∀ v, x v ≤ 1) :
    (∑ v, x v) ^ 2 ≤ (G.indepNum : ℝ) * (2 * weightedEdgeSum G x + ∑ v, x v) := by
  have hsample (ω : V → Bool) : ((selectedVertices ω).card : ℝ) ^ 2 ≤
      (G.indepNum : ℝ) * (2 * ((selectedEdges G ω).card : ℝ) + (selectedVertices ω).card) := by
    have h := induced_turan_polynomial G (selectedVertices ω)
    rw [← selectedEdges_card_induce G ω] at h
    exact h
  have haverage :
      finiteExpectation (vertexSamplingWeight x) (fun ω => ((selectedVertices ω).card : ℝ) ^ 2) ≤
      (G.indepNum : ℝ) * finiteExpectation (vertexSamplingWeight x)
        (fun ω => 2 * ((selectedEdges G ω).card : ℝ) + (selectedVertices ω).card) := by
    unfold finiteExpectation
    rw [Finset.mul_sum]
    apply Finset.sum_le_sum
    intro ω _
    calc
      vertexSamplingWeight x ω * ((selectedVertices ω).card : ℝ) ^ 2 ≤
          vertexSamplingWeight x ω * ((G.indepNum : ℝ) *
            (2 * ((selectedEdges G ω).card : ℝ) + (selectedVertices ω).card)) :=
        mul_le_mul_of_nonneg_left (hsample ω) (vertexSamplingWeight_nonneg x hx0 hx1 ω)
      _ = (G.indepNum : ℝ) * (vertexSamplingWeight x ω *
          (2 * ((selectedEdges G ω).card : ℝ) + (selectedVertices ω).card)) := by ring
  have hjensen := finiteExpectation_square_ge (vertexSamplingWeight x)
    (vertexSamplingWeight_nonneg x hx0 hx1) (vertexSamplingWeight_sum x)
    (fun ω => ((selectedVertices ω).card : ℝ))
  have hmean : finiteExpectation (vertexSamplingWeight x)
      (fun ω => 2 * ((selectedEdges G ω).card : ℝ) + (selectedVertices ω).card) =
      2 * weightedEdgeSum G x + ∑ v, x v := by
    rw [finiteExpectation_add, finiteExpectation_const_mul,
      vertexSampling_expected_edges, vertexSampling_expected_order]
  rw [vertexSampling_expected_order] at hjensen
  exact hjensen.trans (by simpa only [hmean] using haverage)

-- Source: Er579.RandomRealization.WeightedTuran:142
theorem weighted_turan_lower_bound (G : SimpleGraph V) (x : V → ℝ)
    (hx0 : ∀ v, 0 ≤ x v) (hx1 : ∀ v, x v ≤ 1) (r : ℝ) (hr : 0 < r)
    (hα : (G.indepNum : ℝ) ≤ r) :
    ((∑ v, x v) ^ 2 / r - ∑ v, x v) / 2 ≤ weightedEdgeSum G x := by
  have hpoly := weighted_turan_polynomial G x hx0 hx1
  have henergy : 0 ≤ weightedEdgeSum G x := by
    apply Finset.sum_nonneg
    intro e _
    obtain ⟨u, v⟩ := e
    simpa only [symmetricEdgeWeight, Sym2.lift_mk] using mul_nonneg (hx0 u) (hx0 v)
  have htotal : 0 ≤ ∑ v, x v := Finset.sum_nonneg (fun v _ => hx0 v)
  have hpoly' : (∑ v, x v) ^ 2 ≤ r * (2 * weightedEdgeSum G x + ∑ v, x v) :=
    hpoly.trans (mul_le_mul_of_nonneg_right hα (by positivity))
  apply (div_le_iff₀ (by norm_num : (0 : ℝ) < 2)).2
  have hquot : (∑ v, x v) ^ 2 / r ≤ 2 * weightedEdgeSum G x + ∑ v, x v :=
    (div_le_iff₀ hr).2 (by nlinarith [hpoly'])
  nlinarith

end Er579.RandomRealization

end

/- Source fragment: Er579.RandomRealization.MatchingRealization. Original licenses and source proofs retained. -/

section

namespace Er579.RandomRealization

open scoped BigOperators Classical
open Filter Topology

variable {Q F : Type*} [Fintype Q] [Fintype F] [LinearOrder Q]

-- Source: Er579.RandomRealization.MatchingRealization:16
noncomputable def matchingSamplingWeight (ω : (Q × Q) → Equiv.Perm F) : ℝ :=
  productWeight (fun _ : Q × Q => uniformPermWeight) ω

-- Source: Er579.RandomRealization.MatchingRealization:19
def sampledMatchingCover (G : SimpleGraph Q) (ω : (Q × Q) → Equiv.Perm F) :
    SimpleGraph (Q × F) :=
  matchingCover G (orientPermutations (fun a b => ω (a, b)))

omit [LinearOrder Q] in

-- Source: Er579.RandomRealization.MatchingRealization:24
theorem matchingSamplingWeight_nonneg (ω : (Q × Q) → Equiv.Perm F) :
    0 ≤ matchingSamplingWeight ω :=
  productWeight_nonneg _ (fun _ _ => uniformPermWeight_nonneg _) ω

-- Source: Er579.RandomRealization.MatchingRealization:28
theorem matchingSamplingWeight_sum :
    (∑ ω : (Q × Q) → Equiv.Perm F, matchingSamplingWeight ω) = 1 := by
  unfold matchingSamplingWeight
  exact productWeight_sum (E := Q × Q) (X := Equiv.Perm F)
    (fun _ => uniformPermWeight (F := F)) (fun _ => uniformPermWeight_sum (F := F))

-- Source: Er579.RandomRealization.MatchingRealization:34
noncomputable def selectedFiber (I : Finset (Q × F)) (q : Q) : Finset F :=
  Finset.univ.filter fun f => (q, f) ∈ I

omit [Fintype Q] in

-- Source: Er579.RandomRealization.MatchingRealization:38
theorem mem_selectedFiber (I : Finset (Q × F)) (q : Q) (f : F) :
    f ∈ selectedFiber I q ↔ (q, f) ∈ I := by
  simp [selectedFiber]

-- Source: Er579.RandomRealization.MatchingRealization:42
theorem selectedFiber_card_sum (I : Finset (Q × F)) :
    (∑ q : Q, ((selectedFiber I q).card : ℝ)) = I.card := by
  have hfiber (q : Q) : ((selectedFiber I q).card : ℝ) =
      ∑ f : F, if (q, f) ∈ I then (1 : ℝ) else 0 := by
    exact Finset.natCast_card_filter _ _
  simp_rw [hfiber]
  have hsum : (∑ q : Q, ∑ f : F, if (q, f) ∈ I then (1 : ℝ) else 0) =
      ∑ p : Q × F, if p ∈ I then (1 : ℝ) else 0 :=
    (Fintype.sum_prod_type (fun p : Q × F => if p ∈ I then (1 : ℝ) else 0)).symm
  rw [hsum]
  simp

-- Source: Er579.RandomRealization.MatchingRealization:54
noncomputable def fiberOccupancy (I : Finset (Q × F)) (q : Q) : ℝ :=
  (selectedFiber I q).card / (Fintype.card F : ℝ)

omit [Fintype Q] in

-- Source: Er579.RandomRealization.MatchingRealization:58
theorem fiberOccupancy_nonneg (I : Finset (Q × F)) (q : Q) :
    0 ≤ fiberOccupancy I q := by
  unfold fiberOccupancy
  positivity

omit [Fintype Q] in

-- Source: Er579.RandomRealization.MatchingRealization:64
theorem fiberOccupancy_le_one (I : Finset (Q × F)) (q : Q) :
    fiberOccupancy I q ≤ 1 := by
  unfold fiberOccupancy
  apply div_le_one_of_le₀
  · exact_mod_cast (selectedFiber I q).card_le_univ
  · positivity

-- Source: Er579.RandomRealization.MatchingRealization:71
theorem fiberOccupancy_sum (I : Finset (Q × F)) :
    (∑ q : Q, fiberOccupancy I q) = (I.card : ℝ) / Fintype.card F := by
  unfold fiberOccupancy
  rw [← Finset.sum_div, selectedFiber_card_sum]

-- Source: Er579.RandomRealization.MatchingRealization:76
noncomputable def orientedBaseEdges (G : SimpleGraph Q) : Finset (Q × Q) :=
  Finset.univ.filter fun e => e.1 < e.2 ∧ G.Adj e.1 e.2

-- Source: Er579.RandomRealization.MatchingRealization:79
theorem mem_orientedBaseEdges (G : SimpleGraph Q) (e : Q × Q) :
    e ∈ orientedBaseEdges G ↔ e.1 < e.2 ∧ G.Adj e.1 e.2 := by
  simp [orientedBaseEdges]

-- Source: Er579.RandomRealization.MatchingRealization:83
theorem orientedBaseEdges_weight_sum (G : SimpleGraph Q) (x : Q → ℝ) :
    (∑ e ∈ orientedBaseEdges G, x e.1 * x e.2) = weightedEdgeSum G x := by
  unfold weightedEdgeSum
  apply Finset.sum_bij (fun e _ => Sym2.mk e.1 e.2)
  · intro e he
    exact SimpleGraph.mem_edgeFinset.mpr ((mem_orientedBaseEdges G e).1 he).2
  · intro e he f hf h
    have he' := (mem_orientedBaseEdges G e).1 he
    have hf' := (mem_orientedBaseEdges G f).1 hf
    rcases Sym2.eq_iff.mp h with ⟨h1, h2⟩ | ⟨h1, h2⟩
    · exact Prod.ext h1 h2
    · have hlt : f.2 < f.1 := by simpa only [h1, h2] using he'.1
      exact (lt_asymm hlt hf'.1).elim
  · intro e he
    obtain ⟨u, v⟩ := e
    have hadj : G.Adj u v := SimpleGraph.mem_edgeFinset.mp he
    rcases lt_or_gt_of_ne hadj.ne with huv | hvu
    · exact ⟨(u, v), (mem_orientedBaseEdges G _).2 ⟨huv, hadj⟩, rfl⟩
    · exact ⟨(v, u), (mem_orientedBaseEdges G _).2 ⟨hvu, hadj.symm⟩, Sym2.eq_swap⟩
  · intro e _
    simp only [symmetricEdgeWeight, Sym2.lift_mk]

-- Source: Er579.RandomRealization.MatchingRealization:105
theorem independent_forces_matching_avoidance (G : SimpleGraph Q)
    (I : Finset (Q × F)) (ω : (Q × Q) → Equiv.Perm F)
    (hI : (sampledMatchingCover G ω).IsIndepSet (I : Set (Q × F))) :
    ∀ e ∈ orientedBaseEdges G,
      Avoids (selectedFiber I e.1) (selectedFiber I e.2) (ω e) := by
  intro e he f hf hbad
  have he' := (mem_orientedBaseEdges G e).1 he
  have hleft : (e.1, f) ∈ I := (mem_selectedFiber I _ _).1 hf
  have hright : (e.2, ω e f) ∈ I := (mem_selectedFiber I _ _).1 hbad
  apply hI hleft hright (by
    intro h
    exact he'.2.ne (congrArg Prod.fst h))
  refine ⟨he'.2, ?_⟩
  simp [orientPermutations, he'.1]

-- Source: Er579.RandomRealization.MatchingRealization:120
theorem matching_joint_avoidance_weight (G : SimpleGraph Q) (I : Finset (Q × F)) :
    eventWeight matchingSamplingWeight
      (fun ω : (Q × Q) → Equiv.Perm F => ∀ e ∈ orientedBaseEdges G,
        Avoids (selectedFiber I e.1) (selectedFiber I e.2) (ω e)) =
      ∏ e ∈ orientedBaseEdges G,
        eventWeight uniformPermWeight (Avoids (selectedFiber I e.1) (selectedFiber I e.2)) := by
  unfold matchingSamplingWeight
  let P : (Q × Q) → Equiv.Perm F → Prop := fun e σ =>
    e ∈ orientedBaseEdges G → Avoids (selectedFiber I e.1) (selectedFiber I e.2) σ
  have hprod := productWeight_event (E := Q × Q) (X := Equiv.Perm F)
    (fun _ => uniformPermWeight (F := F)) P
  have hmarginal (e : Q × Q) : eventWeight uniformPermWeight (P e) =
      if e ∈ orientedBaseEdges G then
        eventWeight uniformPermWeight (Avoids (selectedFiber I e.1) (selectedFiber I e.2))
      else 1 := by
    by_cases he : e ∈ orientedBaseEdges G
    · simp only [P, he, true_implies, if_pos]
    · simp only [P, he, false_implies]
      simpa [eventWeight] using (uniformPermWeight_sum (F := F))
  simp_rw [hmarginal] at hprod
  simpa only [matchingSamplingWeight, P, Finset.prod_ite_mem, Finset.univ_inter] using hprod

-- Source: Er579.RandomRealization.MatchingRealization:142
theorem matching_independent_weight_le_exp_energy (G : SimpleGraph Q)
    (I : Finset (Q × F)) (hF : 0 < Fintype.card F) :
    eventWeight matchingSamplingWeight
      (fun ω : (Q × Q) → Equiv.Perm F =>
        (sampledMatchingCover G ω).IsIndepSet (I : Set (Q × F))) ≤
      Real.exp (-(Fintype.card F : ℝ) * weightedEdgeSum G (fiberOccupancy I)) := by
  have hm := eventWeight_mono matchingSamplingWeight matchingSamplingWeight_nonneg
    (fun ω hI => independent_forces_matching_avoidance G I ω hI)
  rw [matching_joint_avoidance_weight] at hm
  have hL : (Fintype.card F : ℝ) ≠ 0 := by exact_mod_cast (Nat.ne_of_gt hF)
  calc
    eventWeight matchingSamplingWeight
        (fun ω : (Q × Q) → Equiv.Perm F =>
          (sampledMatchingCover G ω).IsIndepSet (I : Set (Q × F)))
      ≤ ∏ e ∈ orientedBaseEdges G,
          eventWeight uniformPermWeight
            (Avoids (selectedFiber I e.1) (selectedFiber I e.2)) := hm
    _ ≤ ∏ e ∈ orientedBaseEdges G,
        Real.exp (-(((selectedFiber I e.1).card : ℝ) * (selectedFiber I e.2).card) /
          Fintype.card F) := by
      apply Finset.prod_le_prod
      · intro e _
        exact eventWeight_nonneg uniformPermWeight uniformPermWeight_nonneg _
      · intro e _
        exact uniformPerm_avoids_le_exp _ _
    _ = Real.exp (-(Fintype.card F : ℝ) * weightedEdgeSum G (fiberOccupancy I)) := by
      rw [← Real.exp_sum]
      congr 1
      rw [← orientedBaseEdges_weight_sum]
      rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro e _
      unfold fiberOccupancy
      field_simp

-- Source: Er579.RandomRealization.MatchingRealization:177
theorem matching_large_set_energy (G : SimpleGraph Q) (I : Finset (Q × F))
    (r : ℝ) (hr : 0 < r) (hQ : 0 < Fintype.card Q) (hF : 0 < Fintype.card F)
    (hα : (G.indepNum : ℝ) ≤ r * Fintype.card Q)
    (hI : 2 * Real.sqrt r * Fintype.card (Q × F) ≤ (I.card : ℝ)) :
    3 / 2 * (Fintype.card Q : ℝ) ≤ weightedEdgeSum G (fiberOccupancy I) := by
  have hN : (0 : ℝ) < Fintype.card Q := by exact_mod_cast hQ
  have hL : (0 : ℝ) < Fintype.card F := by exact_mod_cast hF
  have hR : 0 < r * (Fintype.card Q : ℝ) := mul_pos hr hN
  have hsum : (∑ q : Q, fiberOccupancy I q) ≤ (Fintype.card Q : ℝ) := by
    simpa using Finset.sum_le_sum (fun q (_ : q ∈ Finset.univ) => fiberOccupancy_le_one I q)
  have hlower : 2 * Real.sqrt r * (Fintype.card Q : ℝ) ≤
      ∑ q : Q, fiberOccupancy I q := by
    rw [fiberOccupancy_sum]
    apply (le_div_iff₀ hL).2
    simpa only [Fintype.card_prod, Nat.cast_mul, mul_assoc] using hI
  have hsq : 4 * r * (Fintype.card Q : ℝ) ^ 2 ≤
      (∑ q : Q, fiberOccupancy I q) ^ 2 := by
    calc
      4 * r * (Fintype.card Q : ℝ) ^ 2 =
          (2 * Real.sqrt r * (Fintype.card Q : ℝ)) ^ 2 := by
        rw [mul_pow, mul_pow, Real.sq_sqrt hr.le]
        ring
      _ ≤ (∑ q : Q, fiberOccupancy I q) ^ 2 := by
        exact (sq_le_sq₀ (by positivity) (by
          exact Finset.sum_nonneg fun q _ => fiberOccupancy_nonneg I q)).2 hlower
  have hquot : 4 * (Fintype.card Q : ℝ) ≤
      (∑ q : Q, fiberOccupancy I q) ^ 2 / (r * Fintype.card Q) := by
    apply (le_div_iff₀ hR).2
    nlinarith [hsq]
  have ht := weighted_turan_lower_bound G (fiberOccupancy I)
    (fiberOccupancy_nonneg I) (fiberOccupancy_le_one I) _ hR hα
  linarith

-- Source: Er579.RandomRealization.MatchingRealization:210
theorem matching_large_set_independent_weight (G : SimpleGraph Q) (I : Finset (Q × F))
    (r : ℝ) (hr : 0 < r) (hQ : 0 < Fintype.card Q) (hF : 0 < Fintype.card F)
    (hα : (G.indepNum : ℝ) ≤ r * Fintype.card Q)
    (hI : 2 * Real.sqrt r * Fintype.card (Q × F) ≤ (I.card : ℝ)) :
    eventWeight matchingSamplingWeight
      (fun ω : (Q × Q) → Equiv.Perm F =>
        (sampledMatchingCover G ω).IsIndepSet (I : Set (Q × F))) ≤
      Real.exp (-(3 / 2) * (Fintype.card (Q × F) : ℝ)) := by
  refine (matching_independent_weight_le_exp_energy G I hF).trans ?_
  apply Real.exp_le_exp.mpr
  have henergy := matching_large_set_energy G I r hr hQ hF hα hI
  have hmul := mul_le_mul_of_nonneg_left henergy (Nat.cast_nonneg (Fintype.card F))
  simp only [Fintype.card_prod, Nat.cast_mul]
  nlinarith [hmul]

-- Source: Er579.RandomRealization.MatchingRealization:225
theorem matching_bad_independence_weight (G : SimpleGraph Q)
    (r : ℝ) (hr : 0 < r) (hQ : 0 < Fintype.card Q) (hF : 0 < Fintype.card F)
    (hα : (G.indepNum : ℝ) ≤ r * Fintype.card Q) :
    eventWeight matchingSamplingWeight
      (fun ω : (Q × Q) → Equiv.Perm F =>
        2 * Real.sqrt r * Fintype.card (Q × F) < (sampledMatchingCover G ω).indepNum) ≤
      Real.exp (-(Fintype.card (Q × F) : ℝ) / 2) := by
  let E : Finset (Q × F) → ((Q × Q) → Equiv.Perm F) → Prop := fun I ω =>
    (sampledMatchingCover G ω).IsIndepSet (I : Set (Q × F)) ∧
      2 * Real.sqrt r * Fintype.card (Q × F) ≤ (I.card : ℝ)
  have hsubset := eventWeight_mono matchingSamplingWeight matchingSamplingWeight_nonneg
    (E := fun ω : (Q × Q) → Equiv.Perm F =>
      2 * Real.sqrt r * Fintype.card (Q × F) < (sampledMatchingCover G ω).indepNum)
    (F := fun ω => ∃ I, E I ω) (fun ω hbad => by
      obtain ⟨I, hI⟩ := (sampledMatchingCover G ω).exists_isNIndepSet_indepNum
      refine ⟨I, hI.isIndepSet, ?_⟩
      simpa only [hI.card_eq] using hbad.le)
  have hbound (I : Finset (Q × F)) : eventWeight matchingSamplingWeight (E I) ≤
      Real.exp (-(3 / 2) * (Fintype.card (Q × F) : ℝ)) := by
    by_cases hI : 2 * Real.sqrt r * Fintype.card (Q × F) ≤ (I.card : ℝ)
    · have hm := eventWeight_mono matchingSamplingWeight matchingSamplingWeight_nonneg
        (fun ω (h : E I ω) => h.1)
      exact hm.trans (matching_large_set_independent_weight G I r hr hQ hF hα hI)
    · simp only [E, hI, and_false, eventWeight, if_false, Finset.sum_const_zero]
      exact (Real.exp_pos _).le
  have hunion := eventWeight_exists_le_sum matchingSamplingWeight
    matchingSamplingWeight_nonneg E
  have hsum := Finset.sum_le_sum (fun I (_ : I ∈ Finset.univ) => hbound I)
  have hcount : (Fintype.card (Finset (Q × F)) : ℝ) ≤
      Real.exp (Fintype.card (Q × F) : ℝ) := by
    rw [Fintype.card_finset, Nat.cast_pow]
    calc
      (2 : ℝ) ^ Fintype.card (Q × F) ≤ Real.exp 1 ^ Fintype.card (Q × F) := by
        apply pow_le_pow_left₀ (by norm_num)
        linarith [Real.add_one_le_exp (1 : ℝ)]
      _ = Real.exp (Fintype.card (Q × F) : ℝ) := by
        rw [← Real.exp_nat_mul]
        simp
  calc
    eventWeight matchingSamplingWeight
        (fun ω : (Q × Q) → Equiv.Perm F =>
          2 * Real.sqrt r * Fintype.card (Q × F) < (sampledMatchingCover G ω).indepNum)
      ≤ ∑ I : Finset (Q × F), eventWeight matchingSamplingWeight (E I) :=
        hsubset.trans hunion
    _ ≤ (Fintype.card (Finset (Q × F)) : ℝ) *
        Real.exp (-(3 / 2) * (Fintype.card (Q × F) : ℝ)) := by simpa using hsum
    _ ≤ Real.exp (Fintype.card (Q × F) : ℝ) *
        Real.exp (-(3 / 2) * (Fintype.card (Q × F) : ℝ)) :=
      mul_le_mul_of_nonneg_right hcount (Real.exp_pos _).le
    _ = Real.exp (-(Fintype.card (Q × F) : ℝ) / 2) := by
      rw [← Real.exp_add]
      congr 1
      ring

-- Source: Er579.RandomRealization.MatchingRealization:279
theorem matching_four_coordinate_weight
    (e₀ e₁ e₂ e₃ : Q × Q)
    (h₀₁ : e₀ ≠ e₁) (h₀₂ : e₀ ≠ e₂) (h₀₃ : e₀ ≠ e₃)
    (h₁₂ : e₁ ≠ e₂) (h₁₃ : e₁ ≠ e₃) (h₂₃ : e₂ ≠ e₃)
    (P₀ P₁ P₂ P₃ : Equiv.Perm F → Prop) (c : ℝ)
    (hP₀ : eventWeight uniformPermWeight P₀ = c)
    (hP₁ : eventWeight uniformPermWeight P₁ = c)
    (hP₂ : eventWeight uniformPermWeight P₂ = c)
    (hP₃ : eventWeight uniformPermWeight P₃ = c) :
    eventWeight matchingSamplingWeight
      (fun ω : (Q × Q) → Equiv.Perm F =>
        P₀ (ω e₀) ∧ P₁ (ω e₁) ∧ P₂ (ω e₂) ∧ P₃ (ω e₃)) = c ^ 4 := by
  let P : (Q × Q) → Equiv.Perm F → Prop := fun e σ =>
    (e = e₀ → P₀ σ) ∧ (e = e₁ → P₁ σ) ∧ (e = e₂ → P₂ σ) ∧ (e = e₃ → P₃ σ)
  have hevents : (fun ω : (Q × Q) → Equiv.Perm F => ∀ e, P e (ω e)) =
      (fun ω => P₀ (ω e₀) ∧ P₁ (ω e₁) ∧ P₂ (ω e₂) ∧ P₃ (ω e₃)) := by
    funext ω
    apply propext
    constructor
    · intro h
      exact ⟨(h e₀).1 rfl, (h e₁).2.1 rfl, (h e₂).2.2.1 rfl, (h e₃).2.2.2 rfl⟩
    · rintro ⟨h₀, h₁, h₂, h₃⟩ e
      refine ⟨?_, ?_, ?_, ?_⟩
      · intro h
        simpa only [h] using h₀
      · intro h
        simpa only [h] using h₁
      · intro h
        simpa only [h] using h₂
      · intro h
        simpa only [h] using h₃
  have hmarginal (e : Q × Q) : eventWeight uniformPermWeight (P e) =
      if e ∈ ({e₀, e₁, e₂, e₃} : Finset (Q × Q)) then c else 1 := by
    by_cases he₀ : e = e₀
    · subst e
      simpa [P, h₀₁, h₀₂, h₀₃] using hP₀
    by_cases he₁ : e = e₁
    · subst e
      simpa [P, h₀₁.symm, h₁₂, h₁₃] using hP₁
    by_cases he₂ : e = e₂
    · subst e
      simpa [P, h₀₂.symm, h₁₂.symm, h₂₃] using hP₂
    by_cases he₃ : e = e₃
    · subst e
      simpa [P, h₀₃.symm, h₁₃.symm, h₂₃.symm] using hP₃
    simpa [P, he₀, he₁, he₂, he₃, eventWeight] using (uniformPermWeight_sum (F := F))
  rw [← hevents]
  unfold matchingSamplingWeight
  rw [productWeight_event]
  simp_rw [hmarginal]
  rw [Fintype.prod_ite_mem, Finset.prod_const]
  congr 1
  simp [h₀₁, h₀₂, h₀₃, h₁₂, h₁₃, h₂₃]

-- Source: Er579.RandomRealization.MatchingRealization:333
def matchingEdgeCoordinate (a b : Q) : Q × Q :=
  if a < b then (a, b) else (b, a)

omit [Fintype Q] in

-- Source: Er579.RandomRealization.MatchingRealization:337
theorem matchingEdgeCoordinate_sym2 (a b : Q) :
    Sym2.mk (matchingEdgeCoordinate a b).1 (matchingEdgeCoordinate a b).2 = Sym2.mk a b := by
  unfold matchingEdgeCoordinate
  split_ifs
  · rfl
  · exact Sym2.eq_swap

omit [Fintype Q] in

-- Source: Er579.RandomRealization.MatchingRealization:345
theorem matchingEdgeCoordinate_eq_imp {a b c d : Q}
    (h : matchingEdgeCoordinate a b = matchingEdgeCoordinate c d) :
    (a = c ∧ b = d) ∨ (a = d ∧ b = c) := by
  apply Sym2.eq_iff.mp
  simpa only [matchingEdgeCoordinate_sym2] using
    congrArg (fun e : Q × Q => Sym2.mk e.1 e.2) h

-- Source: Er579.RandomRealization.MatchingRealization:352
def matchingEdgeConstraint (a b : Q × F) (σ : Equiv.Perm F) : Prop :=
  if a.1 < b.1 then σ a.2 = b.2 else σ.symm a.2 = b.2

omit [Fintype Q] in

-- Source: Er579.RandomRealization.MatchingRealization:356
theorem matchingEdgeConstraint_weight (a b : Q × F) :
    eventWeight uniformPermWeight (matchingEdgeConstraint a b) = 1 / (Fintype.card F : ℝ) := by
  unfold matchingEdgeConstraint
  split_ifs
  · exact uniformPerm_single_image a.2 b.2
  · exact uniformPerm_single_inverse_image a.2 b.2

omit [Fintype Q] [Fintype F] in

-- Source: Er579.RandomRealization.MatchingRealization:364
theorem matchingEdgeConstraint_of_adj (G : SimpleGraph Q)
    (ω : (Q × Q) → Equiv.Perm F) {a b : Q × F}
    (h : (sampledMatchingCover G ω).Adj a b) :
    matchingEdgeConstraint a b (ω (matchingEdgeCoordinate a.1 b.1)) := by
  have hab : a.1 ≠ b.1 := h.1.ne
  rcases lt_or_gt_of_ne hab with hab' | hba'
  · simpa [sampledMatchingCover, orientPermutations, matchingEdgeConstraint,
      matchingEdgeCoordinate, hab'] using h.2
  · simpa [sampledMatchingCover, orientPermutations, matchingEdgeConstraint,
      matchingEdgeCoordinate, not_lt_of_ge hba'.le, hab] using h.2

-- Source: Er579.RandomRealization.MatchingRealization:375
theorem matching_square_occurrence_weight_le (G : SimpleGraph Q)
    (a b c d : Q × F) :
    eventWeight matchingSamplingWeight
      (fun ω : (Q × Q) → Equiv.Perm F => (a, b, c, d) ∈ squareOccurrences (sampledMatchingCover G ω)) ≤
      (1 / (Fintype.card F : ℝ)) ^ 4 := by
  by_cases hbase : a.1 ≠ c.1 ∧ b.1 ≠ d.1 ∧
      G.Adj a.1 b.1 ∧ G.Adj b.1 c.1 ∧ G.Adj c.1 d.1 ∧ G.Adj d.1 a.1
  · obtain ⟨hac, hbd, hab, hbc, hcd, hda⟩ := hbase
    have h₀₁ : matchingEdgeCoordinate a.1 b.1 ≠ matchingEdgeCoordinate b.1 c.1 := by
      intro h
      rcases matchingEdgeCoordinate_eq_imp h with ⟨h₁, _⟩ | ⟨h₁, _⟩
      · exact hab.ne h₁
      · exact hac h₁
    have h₀₂ : matchingEdgeCoordinate a.1 b.1 ≠ matchingEdgeCoordinate c.1 d.1 := by
      intro h
      rcases matchingEdgeCoordinate_eq_imp h with ⟨h₁, _⟩ | ⟨h₁, _⟩
      · exact hac h₁
      · exact hda.ne.symm h₁
    have h₀₃ : matchingEdgeCoordinate a.1 b.1 ≠ matchingEdgeCoordinate d.1 a.1 := by
      intro h
      rcases matchingEdgeCoordinate_eq_imp h with ⟨h₁, _⟩ | ⟨_, h₂⟩
      · exact hda.ne.symm h₁
      · exact hbd h₂
    have h₁₂ : matchingEdgeCoordinate b.1 c.1 ≠ matchingEdgeCoordinate c.1 d.1 := by
      intro h
      rcases matchingEdgeCoordinate_eq_imp h with ⟨h₁, _⟩ | ⟨h₁, _⟩
      · exact hbc.ne h₁
      · exact hbd h₁
    have h₁₃ : matchingEdgeCoordinate b.1 c.1 ≠ matchingEdgeCoordinate d.1 a.1 := by
      intro h
      rcases matchingEdgeCoordinate_eq_imp h with ⟨h₁, _⟩ | ⟨h₁, _⟩
      · exact hbd h₁
      · exact hab.ne.symm h₁
    have h₂₃ : matchingEdgeCoordinate c.1 d.1 ≠ matchingEdgeCoordinate d.1 a.1 := by
      intro h
      rcases matchingEdgeCoordinate_eq_imp h with ⟨h₁, _⟩ | ⟨h₁, _⟩
      · exact hcd.ne h₁
      · exact hac.symm h₁
    have hm := eventWeight_mono matchingSamplingWeight matchingSamplingWeight_nonneg
      (E := fun ω : (Q × Q) → Equiv.Perm F =>
        (a, b, c, d) ∈ squareOccurrences (sampledMatchingCover G ω))
      (F := fun ω =>
        matchingEdgeConstraint a b (ω (matchingEdgeCoordinate a.1 b.1)) ∧
        matchingEdgeConstraint b c (ω (matchingEdgeCoordinate b.1 c.1)) ∧
        matchingEdgeConstraint c d (ω (matchingEdgeCoordinate c.1 d.1)) ∧
        matchingEdgeConstraint d a (ω (matchingEdgeCoordinate d.1 a.1))) (fun ω hocc => by
        simp only [squareOccurrences, Finset.mem_filter, Finset.mem_univ, true_and] at hocc
        exact ⟨matchingEdgeConstraint_of_adj G ω hocc.2.2.1,
          matchingEdgeConstraint_of_adj G ω hocc.2.2.2.1,
          matchingEdgeConstraint_of_adj G ω hocc.2.2.2.2.1,
          matchingEdgeConstraint_of_adj G ω hocc.2.2.2.2.2⟩)
    rw [matching_four_coordinate_weight _ _ _ _ h₀₁ h₀₂ h₀₃ h₁₂ h₁₃ h₂₃
      _ _ _ _ _ (matchingEdgeConstraint_weight a b) (matchingEdgeConstraint_weight b c)
      (matchingEdgeConstraint_weight c d) (matchingEdgeConstraint_weight d a)] at hm
    exact hm
  · have hfalse (ω : (Q × Q) → Equiv.Perm F) :
        (a, b, c, d) ∉ squareOccurrences (sampledMatchingCover G ω) := by
      intro hocc
      simp only [squareOccurrences, Finset.mem_filter, Finset.mem_univ, true_and] at hocc
      exact hbase (matchingCover_square_projection G _ hocc.1 hocc.2.1
        hocc.2.2.1 hocc.2.2.2.1 hocc.2.2.2.2.1 hocc.2.2.2.2.2)
    simp only [eventWeight, if_neg (hfalse _), Finset.sum_const_zero]
    positivity

-- Source: Er579.RandomRealization.MatchingRealization:439
theorem matching_expected_square_count_le (G : SimpleGraph Q) (hF : 0 < Fintype.card F) :
    finiteExpectation matchingSamplingWeight
      (fun ω : (Q × Q) → Equiv.Perm F =>
        ((squareOccurrences (sampledMatchingCover G ω)).card : ℝ)) ≤
      (Fintype.card Q : ℝ) ^ 4 := by
  have hsum := finiteExpectation_card_filter matchingSamplingWeight
    (Finset.univ : Finset ((Q × F) × (Q × F) × (Q × F) × (Q × F)))
    (fun ω abcd => abcd ∈ squareOccurrences (sampledMatchingCover G ω))
  have hfilter (ω : (Q × Q) → Equiv.Perm F) :
      (Finset.univ.filter fun abcd => abcd ∈ squareOccurrences (sampledMatchingCover G ω)) =
        squareOccurrences (sampledMatchingCover G ω) := by simp
  simp_rw [hfilter] at hsum
  rw [hsum]
  calc
    (∑ abcd : (Q × F) × (Q × F) × (Q × F) × (Q × F),
      eventWeight matchingSamplingWeight
        (fun ω => abcd ∈ squareOccurrences (sampledMatchingCover G ω))) ≤
        ∑ _abcd : (Q × F) × (Q × F) × (Q × F) × (Q × F),
          (1 / (Fintype.card F : ℝ)) ^ 4 := by
      apply Finset.sum_le_sum
      intro abcd _
      exact matching_square_occurrence_weight_le G abcd.1 abcd.2.1 abcd.2.2.1 abcd.2.2.2
    _ = (Fintype.card Q : ℝ) ^ 4 := by
      simp only [Finset.sum_const, Finset.card_univ, Fintype.card_prod, nsmul_eq_mul,
        Nat.cast_mul]
      have hL : (Fintype.card F : ℝ) ≠ 0 := by exact_mod_cast Nat.ne_of_gt hF
      field_simp

-- Source: Er579.RandomRealization.MatchingRealization:467
theorem matching_expected_short_cycles_le (G : SimpleGraph Q)
    (hG : TriangleFree G) (hF : 0 < Fintype.card F) :
    finiteExpectation matchingSamplingWeight
      (fun ω : (Q × Q) → Equiv.Perm F => (shortCycleCount (sampledMatchingCover G ω) : ℝ)) ≤
      (Fintype.card Q : ℝ) ^ 4 := by
  have htri (ω : (Q × Q) → Equiv.Perm F) :
      triangleOccurrences (sampledMatchingCover G ω) = ∅ := by
    apply Finset.eq_empty_iff_forall_notMem.mpr
    intro abc habc
    simp only [triangleOccurrences, Finset.mem_filter, Finset.mem_univ, true_and] at habc
    exact matchingCover_triangleFree G _ hG abc.1 abc.2.1 abc.2.2
      habc.1 habc.2.1 habc.2.2
  have hcount (ω : (Q × Q) → Equiv.Perm F) :
      (shortCycleCount (sampledMatchingCover G ω) : ℝ) =
        (squareOccurrences (sampledMatchingCover G ω)).card := by
    simp only [shortCycleCount, htri, Finset.card_empty, zero_add]
  simp_rw [hcount]
  exact matching_expected_square_count_le G hF

-- Source: Er579.RandomRealization.MatchingRealization:486
def GoodMatchingRealization (G : SimpleGraph Q) (ω : (Q × Q) → Equiv.Perm F)
    (r ε : ℝ) : Prop :=
  TriangleFree (cleanedGraph (sampledMatchingCover G ω)) ∧
  C4Free (cleanedGraph (sampledMatchingCover G ω)) ∧
  ((cleanedGraph (sampledMatchingCover G ω)).indepNum : ℝ) ≤
    2 * Real.sqrt r * Fintype.card (Q × F) ∧
  ((cleanupVertices (sampledMatchingCover G ω)).card : ℝ) <
    ε * Fintype.card (Q × F) ∧
  (1 - ε) * Fintype.card (Q × F) < Fintype.card (CleanVertex (sampledMatchingCover G ω)) ∧
  Fintype.card (CleanVertex (sampledMatchingCover G ω)) ≤ Fintype.card (Q × F) ∧
  (∀ u v, (cleanedGraph (sampledMatchingCover G ω)).Adj u v → G.Adj u.val.1 v.val.1) ∧
  (∀ b w z, (cleanedGraph (sampledMatchingCover G ω)).Adj b w →
    (cleanedGraph (sampledMatchingCover G ω)).Adj b z →
    w ≠ z → w.val.1 ≠ z.val.1)

-- Source: Er579.RandomRealization.MatchingRealization:501
theorem exists_good_matching_realization (G : SimpleGraph Q) (hG : TriangleFree G)
    (r ε : ℝ) (hr : 0 < r) (hε : 0 < ε)
    (hQ : 0 < Fintype.card Q) (hF : 0 < Fintype.card F)
    (hα : (G.indepNum : ℝ) ≤ r * Fintype.card Q)
    (horder : (2 : ℝ) ≤ Fintype.card (Q × F))
    (hcycles : 4 * (Fintype.card Q : ℝ) ^ 4 ≤ ε * Fintype.card (Q × F)) :
    ∃ ω : (Q × Q) → Equiv.Perm F, GoodMatchingRealization G ω r ε := by
  have hV : (0 : ℝ) < Fintype.card (Q × F) := by linarith
  have hdelete : 0 < ε * (Fintype.card (Q × F) : ℝ) := mul_pos hε hV
  have hbad : eventWeight matchingSamplingWeight
      (fun ω : (Q × Q) → Equiv.Perm F =>
        2 * Real.sqrt r * Fintype.card (Q × F) < (sampledMatchingCover G ω).indepNum) < 1 / 2 := by
    have hhalf : Real.exp (-1) < (1 / 2 : ℝ) := by
      rw [Real.exp_neg]
      rw [← one_div]
      apply (div_lt_div_iff₀ (Real.exp_pos _) (by norm_num : (0 : ℝ) < 2)).2
      linarith [Real.add_one_lt_exp (by norm_num : (1 : ℝ) ≠ 0)]
    exact (matching_bad_independence_weight G r hr hQ hF hα).trans_lt
      ((Real.exp_le_exp.mpr (by linarith)).trans_lt hhalf)
  have hcyc : finiteExpectation matchingSamplingWeight
      (fun ω : (Q × Q) → Equiv.Perm F => (shortCycleCount (sampledMatchingCover G ω) : ℝ)) /
        (ε * Fintype.card (Q × F)) ≤ 1 / 4 := by
    apply (div_le_iff₀ hdelete).2
    have he := matching_expected_short_cycles_le G hG hF
    nlinarith [he, hcycles]
  have hestimates : eventWeight matchingSamplingWeight
      (fun ω : (Q × Q) → Equiv.Perm F =>
        2 * Real.sqrt r * Fintype.card (Q × F) < (sampledMatchingCover G ω).indepNum) +
      finiteExpectation matchingSamplingWeight
        (fun ω : (Q × Q) → Equiv.Perm F => (shortCycleCount (sampledMatchingCover G ω) : ℝ)) /
        (ε * Fintype.card (Q × F)) < 1 := by linarith
  obtain ⟨ω, htri, hsquare, hα', hdelete', hcard⟩ := exists_clean_realization_from_bounds
    (Ω := (Q × Q) → Equiv.Perm F) (V := Q × F)
    matchingSamplingWeight matchingSamplingWeight_nonneg matchingSamplingWeight_sum
    (sampledMatchingCover G) (2 * Real.sqrt r * Fintype.card (Q × F))
    (ε * Fintype.card (Q × F)) hdelete hestimates
  refine ⟨ω, htri, hsquare, hα', hdelete', ?_, ?_, ?_, ?_⟩
  · simp only [← Nat.card_eq_fintype_card] at hcard ⊢
    nlinarith [hcard]
  · simp only [← Nat.card_eq_fintype_card]
    calc
      Nat.card (CleanVertex (sampledMatchingCover G ω)) =
          Nat.card (Q × F) - (cleanupVertices (sampledMatchingCover G ω)).card := by
        simpa only [← Nat.card_eq_fintype_card] using cleanVertex_card_eq (sampledMatchingCover G ω)
      _ ≤ Nat.card (Q × F) := Nat.sub_le _ _
  · intro u v huv
    exact huv.1
  · intro b w z hbw hbz hwz
    apply matchingCover_leaf_separation G (orientPermutations (fun a b => ω (a, b)))
      b.val w.val z.val hbw hbz
    intro h
    exact hwz (Subtype.ext h)

-- Source: Er579.RandomRealization.MatchingRealization:554
theorem eventually_exists_good_matching_realization (G : SimpleGraph Q)
    (hG : TriangleFree G) (r ε : ℝ) (hr : 0 < r) (hε : 0 < ε)
    (hQ : 0 < Fintype.card Q) (hα : (G.indepNum : ℝ) ≤ r * Fintype.card Q) :
    ∀ᶠ L : ℕ in atTop, ∃ ω : (Q × Q) → Equiv.Perm (Fin L),
      GoodMatchingRealization G ω r ε := by
  have hN : (0 : ℝ) < Fintype.card Q := by exact_mod_cast hQ
  have hN1 : (1 : ℝ) ≤ Fintype.card Q := by exact_mod_cast hQ
  have hlarge := (tendsto_natCast_atTop_atTop (R := ℝ)).eventually_ge_atTop
    (max 2 (4 * (Fintype.card Q : ℝ) ^ 4 / (ε * Fintype.card Q)))
  filter_upwards [hlarge] with L hL
  have hL2 : (2 : ℝ) ≤ L := (le_max_left _ _).trans hL
  have hLpos : 0 < L := by exact_mod_cast (show (0 : ℝ) < L by linarith)
  have horder : (2 : ℝ) ≤ Fintype.card (Q × Fin L) := by
    simp only [Fintype.card_prod, Fintype.card_fin, Nat.cast_mul]
    nlinarith [hN1, hL2]
  have hcycles : 4 * (Fintype.card Q : ℝ) ^ 4 ≤ ε * Fintype.card (Q × Fin L) := by
    have hquot := (le_max_right 2 _).trans hL
    have hmul := (div_le_iff₀ (mul_pos hε hN)).1 hquot
    simpa only [Fintype.card_prod, Fintype.card_fin, Nat.cast_mul, mul_assoc, mul_comm,
      mul_left_comm] using hmul
  exact exists_good_matching_realization G hG r ε hr hε hQ (by simpa using hLpos)
    hα horder hcycles

end Er579.RandomRealization

end

/- Source fragment: Er579.TargetBridge. Original licenses and source proofs retained. -/

section

namespace Er579

open Filter

open scoped Classical
open scoped Topology

-- Source: Er579.TargetBridge:14
/-- The exact universal positive-density assertion in the pinned Erdős 579 statement. -/
def PositiveDensityClaim : Prop :=
  ∀ δ : ℝ, 0 < δ → ∃ c : ℝ, 0 < c ∧ ∀ᶠ n : ℕ in atTop,
    ∀ G : SimpleGraph (Fin n), octahedron.Free G →
      δ * (n : ℝ) ^ 2 ≤ G.edgeFinset.card → c * n ≤ (G.indepNum : ℝ)

-- Source: Er579.TargetBridge:20
/-- Restricting an independent set to the two parts bounds its total size. -/
theorem indepNum_twoPartGraph_le {A B PA PB : Type*} [Finite A] [Finite B]
    (GA : SimpleGraph A) (GB : SimpleGraph B)
    (M : PA → PB → Prop) (labelA : A → PA) (labelB : B → PB) :
    (twoPartGraph GA GB M labelA labelB).indepNum ≤ GA.indepNum + GB.indepNum := by
  classical
  let G := twoPartGraph GA GB M labelA labelB
  obtain ⟨s, hs⟩ := G.exists_isNIndepSet_indepNum
  have hsi := (G.isIndepSet_iff).1 hs.isIndepSet
  have hA : GA.IsIndepSet s.toLeft := by
    rw [SimpleGraph.isIndepSet_iff]
    intro a ha b hb hab
    have h := hsi (Finset.mem_toLeft.1 ha) (Finset.mem_toLeft.1 hb)
      (by simpa using hab)
    simpa only [G, twoPartGraph_adj_inl_inl] using h
  have hB : GB.IsIndepSet s.toRight := by
    rw [SimpleGraph.isIndepSet_iff]
    intro a ha b hb hab
    have h := hsi (Finset.mem_toRight.1 ha) (Finset.mem_toRight.1 hb)
      (by simpa using hab)
    simpa only [G, twoPartGraph_adj_inr_inr] using h
  calc
    G.indepNum = s.card := hs.card_eq.symm
    _ = s.toLeft.card + s.toRight.card := Finset.card_toLeft_add_card_toRight.symm
    _ ≤ GA.indepNum + GB.indepNum := Nat.add_le_add hA.card_le_indepNum hB.card_le_indepNum

-- Source: Er579.TargetBridge:46
/-- Arbitrarily large strict counterexamples at one fixed density negate the universal assertion. -/
theorem not_positiveDensityClaim_of_counterexamples (δ : ℝ) (hδ : 0 < δ)
    (hcounter : ∀ c : ℝ, 0 < c → ∀ N : ℕ,
      ∃ n : ℕ, N ≤ n ∧ ∃ G : SimpleGraph (Fin n), octahedron.Free G ∧
        δ * (n : ℝ) ^ 2 ≤ G.edgeFinset.card ∧ (G.indepNum : ℝ) < c * n) :
    ¬ PositiveDensityClaim := by
  intro hclaim
  obtain ⟨c, hc, hevent⟩ := hclaim δ hδ
  obtain ⟨N, hN⟩ := eventually_atTop.1 hevent
  obtain ⟨n, hn, G, hfree, hdense, hsmall⟩ := hcounter c hc N
  exact (not_lt_of_ge (hN n hn G hfree hdense)) hsmall

-- Source: Er579.TargetBridge:79
private theorem indepNum_le_of_iso {V W : Type*} [Finite V] [Finite W]
    {G : SimpleGraph V} {H : SimpleGraph W} (e : G ≃g H) : G.indepNum ≤ H.indepNum := by
  classical
  obtain ⟨s, hs⟩ := G.exists_isNIndepSet_indepNum
  have ht : H.IsIndepSet (s.map e.toEquiv.toEmbedding) := by
    rw [SimpleGraph.isIndepSet_iff]
    intro x hx y hy hxy
    obtain ⟨a, ha, rfl⟩ := Finset.mem_map.1 hx
    obtain ⟨b, hb, rfl⟩ := Finset.mem_map.1 hy
    have hab : a ≠ b := fun h => hxy (congrArg e h)
    intro he
    exact ((G.isIndepSet_iff).1 hs.isIndepSet ha hb hab)
      (e.map_adj_iff.1 he)
  have hcard := ht.card_le_indepNum
  simpa only [Finset.card_map, hs.card_eq] using hcard

-- Source: Er579.TargetBridge:95
/-- Independence number is preserved by relabelling a finite simple graph. -/
theorem indepNum_eq_of_iso {V W : Type*} [Finite V] [Finite W]
    {G : SimpleGraph V} {H : SimpleGraph W} (e : G ≃g H) : G.indepNum = H.indepNum :=
  le_antisymm (indepNum_le_of_iso e) (indepNum_le_of_iso e.symm)

-- Source: Er579.TargetBridge:100
/-- Relabel one finite counterexample onto the exact `Fin n` vertex type of the target. -/
theorem finite_counterexample_to_Fin {V : Type*} [Fintype V]
    (G : SimpleGraph V) (δ c : ℝ) (N : ℕ)
    (hlarge : N ≤ Fintype.card V) (hfree : octahedron.Free G)
    (hdense : δ * (Fintype.card V : ℝ) ^ 2 ≤ G.edgeFinset.card)
    (hsmall : (G.indepNum : ℝ) < c * Fintype.card V) :
    ∃ n : ℕ, N ≤ n ∧ ∃ GF : SimpleGraph (Fin n), octahedron.Free GF ∧
      δ * (n : ℝ) ^ 2 ≤ GF.edgeFinset.card ∧ (GF.indepNum : ℝ) < c * n := by
  classical
  let e := (Fintype.equivFin V).symm
  let GF := G.comap e
  let iso : GF ≃g G := SimpleGraph.Iso.comap e G
  refine ⟨Fintype.card V, hlarge, GF, ?_, ?_, ?_⟩
  · rintro ⟨f⟩
    exact hfree ⟨iso.toCopy.comp f⟩
  · convert hdense using 1
    exact_mod_cast iso.card_edgeFinset_eq
  · rw [indepNum_eq_of_iso iso]
    exact hsmall

end Er579

end

/- Source fragment: Er579.GraphAssembly. Original licenses and source proofs retained. -/

section

namespace Er579.GraphAssembly

open scoped BigOperators Classical
open Filter RandomRealization ProfileWeights CrossDensity

-- Source: Er579.GraphAssembly:13
/-- Keep the cover's ordering as data, so it cannot change mask enumeration. -/
structure MatchingOrder (B : Type*) where
  order : LinearOrder B

-- Source: Er579.GraphAssembly:17
noncomputable def finiteMatchingOrder (B : Type*) [Fintype B] : MatchingOrder B :=
  ⟨LinearOrder.lift' (Fintype.equivFin B) (Fintype.equivFin B).injective⟩

variable {B : Type*} [Fintype B] {ord : MatchingOrder B}

-- Source: Er579.GraphAssembly:22
theorem edgeFinset_card_eq_natCard {V : Type*} (G : SimpleGraph V) [Fintype G.edgeSet] :
    G.edgeFinset.card = Nat.card G.edgeSet := by
  rw [SimpleGraph.edgeFinset_card, Nat.card_eq_fintype_card]

-- Source: Er579.GraphAssembly:26
abbrev Profile (B : Type*) := B × (B → Bool)

-- Source: Er579.GraphAssembly:28
def replicationOrder (B : Type*) [Fintype B] (L : ℕ) : ℕ :=
  denominator B B * L ^ 5

-- Source: Er579.GraphAssembly:31
def matchingFibre (B : Type*) [Fintype B] (L : ℕ) : ℕ :=
  4 ^ Fintype.card B * L ^ 5

-- Source: Er579.GraphAssembly:34
abbrev AOriginal (B : Type*) [Fintype B] (L : ℕ) :=
  BlowupVertex (profileMultiplicity (P := B) (B := B)) L

-- Source: Er579.GraphAssembly:37
abbrev BOriginal (B : Type*) [Fintype B] (L : ℕ) := B × Fin (matchingFibre B L)

-- Source: Er579.GraphAssembly:39
def aSample (HB : SimpleGraph B) (C : B → B → Prop) (L : ℕ)
    (ω : Sym2 (AOriginal B L) → Bool) : SimpleGraph (AOriginal B L) :=
  bernoulliGraph
    (profileBlowup (maskedCompatibilityGraph HB C) (profileMultiplicity (P := B) (B := B)) L) ω

-- Source: Er579.GraphAssembly:44
def bSample (HB : SimpleGraph B) (L : ℕ)
    (ω : (B × B) → Equiv.Perm (Fin (matchingFibre B L))) : SimpleGraph (BOriginal B L) :=
  letI : LinearOrder B := ord.order
  sampledMatchingCover HB ω

-- Source: Er579.GraphAssembly:49
abbrev RealizedA (HB : SimpleGraph B) (C : B → B → Prop) (L : ℕ)
    (ω : Sym2 (AOriginal B L) → Bool) := CleanVertex (aSample HB C L ω)

-- Source: Er579.GraphAssembly:52
abbrev RealizedB (HB : SimpleGraph B) (L : ℕ)
    (ω : (B × B) → Equiv.Perm (Fin (matchingFibre B L))) := CleanVertex (bSample (ord := ord) HB L ω)

-- Source: Er579.GraphAssembly:55
abbrev AssembledVertex (HB : SimpleGraph B) (C : B → B → Prop) (L : ℕ)
    (ωA : Sym2 (AOriginal B L) → Bool)
    (ωB : (B × B) → Equiv.Perm (Fin (matchingFibre B L))) :=
  RealizedA HB C L ωA ⊕ RealizedB (ord := ord) HB L ωB

-- Source: Er579.GraphAssembly:60
noncomputable def assembledGraph (HB : SimpleGraph B) (C : B → B → Prop) (L : ℕ)
    (ωA : Sym2 (AOriginal B L) → Bool)
    (ωB : (B × B) → Equiv.Perm (Fin (matchingFibre B L))) :
    SimpleGraph (AssembledVertex (ord := ord) HB C L ωA ωB) :=
  twoPartGraph (cleanedGraph (aSample HB C L ωA)) (cleanedGraph (bSample (ord := ord) HB L ωB))
    (maskedCross C) (fun a => a.val.1) (fun b => b.val.1)

-- Source: Er579.GraphAssembly:67
theorem totalMultiplicity_profile :
    totalMultiplicity (profileMultiplicity (P := B) (B := B)) = denominator B B := by
  exact profileMultiplicity_sum

-- Source: Er579.GraphAssembly:71
theorem aOriginal_card (L : ℕ) : Fintype.card (AOriginal B L) = replicationOrder B L := by
  rw [blowupVertex_card, totalMultiplicity_profile]
  rfl

-- Source: Er579.GraphAssembly:75
theorem bOriginal_card (L : ℕ) : Fintype.card (BOriginal B L) = replicationOrder B L := by
  rw [← Nat.card_eq_fintype_card]
  simp only [BOriginal, Nat.card_prod, Nat.card_fin, matchingFibre,
    replicationOrder, denominator, Nat.mul_assoc]
  rw [Nat.card_eq_fintype_card]

-- Source: Er579.GraphAssembly:81
theorem aOriginal_natCard (L : ℕ) : Nat.card (AOriginal B L) = replicationOrder B L := by
  simpa only [Nat.card_eq_fintype_card] using aOriginal_card (B := B) L

-- Source: Er579.GraphAssembly:84
theorem bOriginal_natCard (L : ℕ) : Nat.card (BOriginal B L) = replicationOrder B L := by
  simpa only [Nat.card_eq_fintype_card] using bOriginal_card (B := B) L

-- Source: Er579.GraphAssembly:87
theorem replicationOrder_ge {L : ℕ} (hB : 0 < Fintype.card B) (hL : 1 ≤ L) :
    L ≤ replicationOrder B L := by
  have hpow : L ≤ L ^ 5 := le_self_pow₀ hL (by norm_num)
  have hden : 1 ≤ denominator B B := denominator_pos hB
  have hmul : L ^ 5 ≤ replicationOrder B L := by
    simpa only [one_mul, replicationOrder] using Nat.mul_le_mul_right (L ^ 5) hden
  exact hpow.trans hmul

-- Source: Er579.GraphAssembly:95
theorem profile_independence_bound (ν : FiniteProbability B)
    (huniform : ∀ b, ν.weight b = 1 / (Fintype.card B : ℝ))
    (HB : SimpleGraph B) (C : B → B → Prop) (a : ℝ)
    (hB : 0 < Fintype.card B)
    (hα : ∀ W : Finset (Profile B),
      (maskedCompatibilityGraph HB C).IsIndepSet (W : Set (Profile B)) →
        maskedProfileMass ν (W : Set (Profile B)) ≤ a) :
    ProfileIndependenceBound (maskedCompatibilityGraph HB C)
      (profileMultiplicity (P := B) (B := B)) a := by
  intro W hW
  have h := independent_multiplicity_bound ν huniform (maskedCompatibilityGraph HB C)
    a hα hB W hW
  simpa only [totalMultiplicity_profile] using h

-- Source: Er579.GraphAssembly:109
def GoodAssembly (HB : SimpleGraph B) (C : B → B → Prop) (L : ℕ)
    (ωA : Sym2 (AOriginal B L) → Bool)
    (ωB : (B × B) → Equiv.Perm (Fin (matchingFibre B L))) (a r ε p : ℝ) : Prop :=
  octahedron.Free (assembledGraph (ord := ord) HB C L ωA ωB) ∧
  2 * (1 - ε) * replicationOrder B L < Nat.card (AssembledVertex (ord := ord) HB C L ωA ωB) ∧
  Nat.card (AssembledVertex (ord := ord) HB C L ωA ωB) ≤ 2 * replicationOrder B L ∧
  ((assembledGraph (ord := ord) HB C L ωA ωB).indepNum : ℝ) ≤
    (a + ε + 2 * Real.sqrt r) * replicationOrder B L ∧
  (p - 2 * ε) * (replicationOrder B L : ℝ) ^ 2 ≤
    (assembledGraph (ord := ord) HB C L ωA ωB).edgeFinset.card

-- Source: Er579.GraphAssembly:120
theorem good_assembly_of_realizations (HB : SimpleGraph B) (C : B → B → Prop) (L : ℕ)
    (ωA : Sym2 (AOriginal B L) → Bool)
    (ωB : (B × B) → Equiv.Perm (Fin (matchingFibre B L))) (a r ε p : ℝ)
    (hA : GoodBernoulliRealization (maskedCompatibilityGraph HB C)
      (profileMultiplicity (P := B) (B := B)) L ωA a ε)
    (hB : (letI : LinearOrder B := ord.order; GoodMatchingRealization HB ωB r ε))
    (hdense : p * (replicationOrder B L : ℝ) ^ 2 ≤
      (crossPairs (fun (a : AOriginal B L) (b : BOriginal B L) =>
        maskedCross C a.1 b.1)).card) :
    GoodAssembly (ord := ord) HB C L ωA ωB a r ε p := by
  rcases hA with ⟨hTA, hCA, hαA, hdelA, hcardA, hupperA, hlabelA⟩
  rcases hB with ⟨hTB, hCB, hαB, hdelB, hcardB, hupperB, hlabelB, hLeaves⟩
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · apply twoPartGraph_octahedron_free
      (cleanedGraph (aSample HB C L ωA)) (cleanedGraph (bSample (ord := ord) HB L ωB))
      (maskedCompatibilityGraph HB C) HB (maskedCross C)
      (fun a => a.val.1) (fun b => b.val.1)
      hTA hTB hCA hCB hlabelA hlabelB hLeaves
    intro q q' hq b w z hbw hbz hwz
    exact maskedCompatibility_excludes HB C hq hbw hbz hwz
  · simp only [← Nat.card_eq_fintype_card] at hcardA hcardB
    rw [aOriginal_natCard] at hcardA
    rw [bOriginal_natCard] at hcardB
    rw [Nat.card_sum]
    push_cast
    simp only [RealizedA, RealizedB, aSample, bSample] at *
    nlinarith only [hcardA, hcardB]
  · simp only [← Nat.card_eq_fintype_card] at hupperA hupperB
    rw [aOriginal_natCard] at hupperA
    rw [bOriginal_natCard] at hupperB
    rw [Nat.card_sum]
    simp only [RealizedA, RealizedB, aSample, bSample] at *
    omega
  · have hsum : ((assembledGraph (ord := ord) HB C L ωA ωB).indepNum : ℝ) ≤
        ((cleanedGraph (aSample HB C L ωA)).indepNum : ℝ) +
          (cleanedGraph (bSample (ord := ord) HB L ωB)).indepNum := by
      exact_mod_cast indepNum_twoPartGraph_le
        (cleanedGraph (aSample HB C L ωA)) (cleanedGraph (bSample (ord := ord) HB L ωB))
        (maskedCross C) (fun a => a.val.1) (fun b => b.val.1)
    rw [aOriginal_card] at hαA
    rw [bOriginal_card] at hαB
    simp only [aSample, bSample] at hsum
    nlinarith only [hsum, hαA, hαB]
  · have hdelA' : ((cleanupVertices (aSample HB C L ωA)).card : ℝ) ≤
        ε * replicationOrder B L := by
      simpa only [aOriginal_card, aSample] using hdelA.le
    have hdelB' : ((cleanupVertices (bSample (ord := ord) HB L ωB)).card : ℝ) ≤
        ε * replicationOrder B L := by
      simpa only [bOriginal_card, bSample] using hdelB.le
    have h := cleaned_twoPartGraph_dense (aSample HB C L ωA) (bSample (ord := ord) HB L ωB)
      (maskedCross C) Sigma.fst Prod.fst (replicationOrder B L)
      (aOriginal_card L) (bOriginal_card L) p ε hdense hdelA' hdelB'
    simp only [edgeFinset_card_eq_natCard]
    simpa only [edgeFinset_card_eq_natCard, assembledGraph] using h

-- Source: Er579.GraphAssembly:175
theorem original_cross_dense (ν : FiniteProbability B)
    (huniform : ∀ b, ν.weight b = 1 / (Fintype.card B : ℝ))
    (C : B → B → Prop) (hB : 0 < Fintype.card B) (L : ℕ) (p : ℝ)
    (hp : p ≤ weightedCrossDensity (maskedProfileLaw ν) ν (maskedCross C)) :
    p * (replicationOrder B L : ℝ) ^ 2 ≤
      (crossPairs (fun (a : AOriginal B L) (b : BOriginal B L) =>
        maskedCross C a.1 b.1)).card := by
  have hm : 0 < totalMultiplicity (profileMultiplicity (P := B) (B := B)) := by
    rw [totalMultiplicity_profile]
    exact denominator_pos hB
  have hweight (q : Profile B) : (maskedProfileLaw ν).weight q =
      (profileMultiplicity q : ℝ) /
        totalMultiplicity (profileMultiplicity (P := B) (B := B)) := by
    change ν.weight q.1 * maskWeight q.2 = _
    rw [totalMultiplicity_profile]
    exact profileWeight_eq ν huniform q
  exact blowup_crossPairs_dense (F := Fin (matchingFibre B L)) (maskedProfileLaw ν) ν
    (profileMultiplicity (P := B) (B := B)) L (maskedCross C)
    hweight huniform hm hB (replicationOrder B L) (aOriginal_card L) (bOriginal_card L) p hp

-- Source: Er579.GraphAssembly:195
theorem eventually_exists_assembled_graph (ν : FiniteProbability B)
    (huniform : ∀ b, ν.weight b = 1 / (Fintype.card B : ℝ))
    (HB : SimpleGraph B) (hTri : TriangleFree HB) (C : B → B → Prop)
    (a r ε p : ℝ) (hr : 0 < r) (hε : 0 < ε) (hB : 0 < Fintype.card B)
    (hαB : (HB.indepNum : ℝ) ≤ r * Fintype.card B)
    (hαA : ∀ W : Finset (Profile B),
      (maskedCompatibilityGraph HB C).IsIndepSet (W : Set (Profile B)) →
        maskedProfileMass ν (W : Set (Profile B)) ≤ a)
    (hp : p ≤ weightedCrossDensity (maskedProfileLaw ν) ν (maskedCross C)) :
    ∀ᶠ L : ℕ in atTop, ∃ ωA : Sym2 (AOriginal B L) → Bool,
      ∃ ωB : (B × B) → Equiv.Perm (Fin (matchingFibre B L)),
        GoodAssembly (ord := ord) HB C L ωA ωB a r ε p := by
  have hm (q : Profile B) : 1 ≤ profileMultiplicity q := profileMultiplicity_pos q
  have hQ : 0 < totalMultiplicity (profileMultiplicity (P := B) (B := B)) := by
    rw [totalMultiplicity_profile]
    exact denominator_pos hB
  have hPA := profile_independence_bound ν huniform HB C a hB hαA
  have hEA := eventually_exists_good_bernoulli_realization (maskedCompatibilityGraph HB C)
    (profileMultiplicity (P := B) (B := B)) hm hQ a ε hε hPA
  have hEBraw : (letI : LinearOrder B := ord.order;
      ∀ᶠ ell : ℕ in atTop, ∃ ω : (B × B) → Equiv.Perm (Fin ell),
        GoodMatchingRealization HB ω r ε) := by
    let : LinearOrder B := ord.order
    exact eventually_exists_good_matching_realization HB hTri r ε hr hε hB hαB
  obtain ⟨K, hK⟩ := eventually_atTop.mp hEBraw
  have hEB : ∀ᶠ L : ℕ in atTop,
      ∃ ωB : (B × B) → Equiv.Perm (Fin (matchingFibre B L)),
        (letI : LinearOrder B := ord.order; GoodMatchingRealization HB ωB r ε) := by
    filter_upwards [eventually_ge_atTop (max K 1)] with L hL
    have hLone : 1 ≤ L := (le_max_right K 1).trans hL
    have hpow : L ≤ L ^ 5 := le_self_pow₀ hLone (by norm_num)
    have hfactor : 1 ≤ (4 : ℕ) ^ Fintype.card B := one_le_pow₀ (by norm_num)
    have hmul : L ^ 5 ≤ matchingFibre B L := by
      simpa only [one_mul, matchingFibre] using Nat.mul_le_mul_right (L ^ 5) hfactor
    exact hK (matchingFibre B L) (((le_max_left K 1).trans hL).trans (hpow.trans hmul))
  filter_upwards [hEA, hEB] with L hA hB'
  obtain ⟨ωA, hA⟩ := hA
  obtain ⟨ωB, hB'⟩ := hB'
  exact ⟨ωA, ωB, good_assembly_of_realizations (ord := ord) HB C L ωA ωB a r ε p hA hB'
    (original_cross_dense ν huniform C hB L p hp)⟩

-- Source: Er579.GraphAssembly:236
theorem exists_arbitrarily_large_assembled_graph (ν : FiniteProbability B)
    (huniform : ∀ b, ν.weight b = 1 / (Fintype.card B : ℝ))
    (HB : SimpleGraph B) (hTri : TriangleFree HB) (C : B → B → Prop)
    (a r ε p : ℝ) (hr : 0 < r) (hε : 0 < ε) (hB : 0 < Fintype.card B)
    (hαB : (HB.indepNum : ℝ) ≤ r * Fintype.card B)
    (hαA : ∀ W : Finset (Profile B),
      (maskedCompatibilityGraph HB C).IsIndepSet (W : Set (Profile B)) →
        maskedProfileMass ν (W : Set (Profile B)) ≤ a)
    (hp : p ≤ weightedCrossDensity (maskedProfileLaw ν) ν (maskedCross C)) (M : ℕ) :
    ∃ L : ℕ, M ≤ L ∧ ∃ ωA : Sym2 (AOriginal B L) → Bool,
      ∃ ωB : (B × B) → Equiv.Perm (Fin (matchingFibre B L)),
        GoodAssembly (ord := ord) HB C L ωA ωB a r ε p := by
  obtain ⟨K, hK⟩ := eventually_atTop.mp
    (eventually_exists_assembled_graph (ord := ord) ν huniform HB hTri C a r ε p hr hε hB hαB hαA hp)
  exact ⟨max M K, le_max_left _ _, hK _ (le_max_right _ _)⟩

-- Source: Er579.GraphAssembly:270
theorem exists_arbitrarily_large_finite_assembled_graph (ν : FiniteProbability B)
    (huniform : ∀ b, ν.weight b = 1 / (Fintype.card B : ℝ))
    (HB : SimpleGraph B) (hTri : TriangleFree HB) (C : B → B → Prop)
    (a r ε p : ℝ) (hr : 0 < r) (hε : 0 < ε) (hB : 0 < Fintype.card B)
    (hαB : (HB.indepNum : ℝ) ≤ r * Fintype.card B)
    (hαA : ∀ W : Finset (Profile B),
      (maskedCompatibilityGraph HB C).IsIndepSet (W : Set (Profile B)) →
        maskedProfileMass ν (W : Set (Profile B)) ≤ a)
    (hp : p ≤ weightedCrossDensity (maskedProfileLaw ν) ν (maskedCross C)) (M : ℕ) :
    ∃ L : ℕ, M ≤ L ∧ ∃ ωA : Sym2 (AOriginal B L) → Bool,
      ∃ ωB : (B × B) → Equiv.Perm (Fin (matchingFibre B L)),
        GoodAssembly (ord := finiteMatchingOrder B) HB C L ωA ωB a r ε p :=
  exists_arbitrarily_large_assembled_graph (ord := finiteMatchingOrder B)
    ν huniform HB hTri C a r ε p hr hε hB hαB hαA hp M

end Er579.GraphAssembly

end

/- Source fragment: Er579.RefutationArithmetic. Original licenses and source proofs retained. -/

section

namespace Er579

open scoped Classical

-- Source: Er579.RefutationArithmetic:7
/-- The numerical conversion uses only scalar bounds, without normalizing a
concrete graph or its vertex enumeration. -/
theorem replication_counterexample_bounds (p c ε s e α : ℝ) (n t N : ℕ)
    (hp : 0 < p) (hc : 0 < c) (hεquarter : ε ≤ 1 / 4)
    (hεc : ε ≤ c / 8) (hεp : ε ≤ p / 8) (hs : s < c / 2)
    (hNt : N ≤ t) (ht : 0 < t)
    (hlo : 2 * (1 - ε) * (t : ℝ) < n) (hhi : n ≤ 2 * t)
    (hα : α ≤ (ε + ε + s) * t) (he : (p - 2 * ε) * (t : ℝ) ^ 2 ≤ e) :
    N ≤ n ∧ (p / 16) * (n : ℝ) ^ 2 ≤ e ∧ α < c * n := by
  have htpos : 0 < (t : ℝ) := by exact_mod_cast ht
  have htn : (t : ℝ) ≤ n := by
    have hscale := mul_le_mul_of_nonneg_right
      (show (1 : ℝ) ≤ 2 * (1 - ε) by linarith only [hεquarter]) htpos.le
    linarith only [hscale, hlo]
  have htnNat : t ≤ n := by exact_mod_cast htn
  have hhiR : (n : ℝ) ≤ 2 * t := by exact_mod_cast hhi
  have hnSquare : (n : ℝ) ^ 2 ≤ 4 * (t : ℝ) ^ 2 := by
    have hm : 0 ≤ (2 * (t : ℝ) - n) * (2 * (t : ℝ) + n) :=
      mul_nonneg (sub_nonneg.mpr hhiR) (by positivity)
    nlinarith only [hm]
  have hdense : (p / 16) * (n : ℝ) ^ 2 ≤ e := by
    calc
      _ ≤ (p / 16) * (4 * (t : ℝ) ^ 2) :=
        mul_le_mul_of_nonneg_left hnSquare (by positivity)
      _ = (p / 4) * (t : ℝ) ^ 2 := by ring
      _ ≤ (p - 2 * ε) * (t : ℝ) ^ 2 :=
        mul_le_mul_of_nonneg_right (by linarith only [hεp, hp]) (sq_nonneg _)
      _ ≤ e := he
  have hcoef : ε + ε + s < c := by linarith only [hεc, hs, hc]
  have hsmall : α < c * n :=
    (hα.trans_lt (mul_lt_mul_of_pos_right hcoef htpos)).trans_le
      (mul_le_mul_of_nonneg_left htn hc.le)
  exact ⟨hNt.trans htnNat, hdense, hsmall⟩

-- Source: Er579.RefutationArithmetic:41
/-- Canonical cardinality transports are performed once on an arbitrary
finite graph, before instantiating the large assembled vertex type. -/
theorem finite_counterexample_of_replication_bounds {V : Type*} [Fintype V]
    (G : SimpleGraph V) (p c ε s : ℝ) (t N : ℕ)
    (hp : 0 < p) (hc : 0 < c) (hεquarter : ε ≤ 1 / 4)
    (hεc : ε ≤ c / 8) (hεp : ε ≤ p / 8) (hs : s < c / 2)
    (hNt : N ≤ t) (ht : 0 < t) (hfree : octahedron.Free G)
    (hlo : 2 * (1 - ε) * (t : ℝ) < Nat.card V) (hhi : Nat.card V ≤ 2 * t)
    (hα : (G.indepNum : ℝ) ≤ (ε + ε + s) * t)
    (he : (p - 2 * ε) * (t : ℝ) ^ 2 ≤ G.edgeFinset.card) :
    ∃ n : ℕ, N ≤ n ∧ ∃ GF : SimpleGraph (Fin n), octahedron.Free GF ∧
      (p / 16) * (n : ℝ) ^ 2 ≤ GF.edgeFinset.card ∧ (GF.indepNum : ℝ) < c * n := by
  obtain ⟨hlarge, hdense, hsmall⟩ := replication_counterexample_bounds
    p c ε s (G.edgeFinset.card : ℝ) (G.indepNum : ℝ) (Nat.card V) t N
    hp hc hεquarter hεc hεp hs hNt ht hlo hhi hα he
  exact finite_counterexample_to_Fin G (p / 16) c N
    (by simpa only [Nat.card_eq_fintype_card] using hlarge) hfree
    (by simpa only [Nat.card_eq_fintype_card] using hdense)
    (by simpa only [Nat.card_eq_fintype_card] using hsmall)

open GraphAssembly

-- Source: Er579.RefutationArithmetic:63
/-- The full assembly supplies exactly the scalar bounds needed for a
strict counterexample, with no additional graph premise. -/
theorem good_assembly_counterexample {B : Type*} [Fintype B] {ord : MatchingOrder B}
    (HB : SimpleGraph B) (C : B → B → Prop) (L : ℕ)
    (ωA : Sym2 (AOriginal B L) → Bool)
    (ωB : (B × B) → Equiv.Perm (Fin (matchingFibre B L))) (p c ε r : ℝ) (N : ℕ)
    (hp : 0 < p) (hc : 0 < c) (hεquarter : ε ≤ 1 / 4)
    (hεc : ε ≤ c / 8) (hεp : ε ≤ p / 8) (hs : 2 * Real.sqrt r < c / 2)
    (hNt : N ≤ replicationOrder B L) (ht : 0 < replicationOrder B L)
    (hGood : GoodAssembly (ord := ord) HB C L ωA ωB ε r ε p) :
    ∃ n : ℕ, N ≤ n ∧ ∃ GF : SimpleGraph (Fin n), octahedron.Free GF ∧
      (p / 16) * (n : ℝ) ^ 2 ≤ GF.edgeFinset.card ∧ (GF.indepNum : ℝ) < c * n := by
  rcases hGood with ⟨hfree, hlo, hhi, hα, he⟩
  exact finite_counterexample_of_replication_bounds
    (assembledGraph (ord := ord) HB C L ωA ωB) p c ε (2 * Real.sqrt r)
    (replicationOrder B L) N hp hc hεquarter hεc hεp hs hNt ht hfree hlo hhi hα he

end Er579

end

/- Source fragment: Er579.RefutationFromStages. Original licenses and source proofs retained. -/

section

namespace Er579

open CubeStage GraphAssembly
open Filter
open scoped Topology Classical

-- Source: Er579.RefutationFromStages:10
theorem dyadic_root_tendsto_zero :
    Tendsto (fun k : ℕ => 2 * Real.sqrt (dyadicRate k)) atTop (𝓝 0) := by
  simpa only [Real.sqrt_zero, mul_zero, Function.comp_def] using
    ((Real.continuous_sqrt.tendsto (0 : ℝ)).comp dyadicRate_tendsto_zero).const_mul 2

-- Source: Er579.RefutationFromStages:15
/-- The final quantifier bridge: uniformly small independent profile mass
on the proved cube stages produces strict counterexamples of every required
order, at the fixed unordered edge density 3/2048. -/
theorem not_positiveDensityClaim_of_small_cube_profiles
    (hprofiles : ∀ ε : ℝ, 0 < ε → ε ≤ 1 →
      ∀ᶠ k : ℕ in atTop, ∀ s : Stage k,
        ∀ W : Finset (CubeStage.Profile k × (CubeStage.Profile k → Bool)),
          (maskedCompatibilityGraph (baseGraph s.supports) CubeStarCaps.cap).IsIndepSet
            (W : Set (CubeStage.Profile k × (CubeStage.Profile k → Bool))) →
              maskedProfileMass (law k)
                (W : Set (CubeStage.Profile k × (CubeStage.Profile k → Bool))) ≤ ε) :
    ¬ PositiveDensityClaim := by
  let p : ℝ := 3 / 128
  have hp : 0 < p := by norm_num [p]
  apply not_positiveDensityClaim_of_counterexamples (p / 16) (div_pos hp (by norm_num))
  intro c hc N
  let ε : ℝ := min (1 / 4) (min (c / 8) (p / 8))
  have hε : 0 < ε := lt_min (by norm_num)
    (lt_min (div_pos hc (by norm_num)) (div_pos hp (by norm_num)))
  have hεquarter : ε ≤ 1 / 4 := min_le_left _ _
  have hεone : ε ≤ 1 := by linarith only [hεquarter]
  have hεc : ε ≤ c / 8 := (min_le_right _ _).trans (min_le_left _ _)
  have hεp : ε ≤ p / 8 := (min_le_right _ _).trans (min_le_right _ _)
  have hrootSmall : ∀ᶠ k : ℕ in atTop, 2 * Real.sqrt (dyadicRate k) < c / 2 :=
    dyadic_root_tendsto_zero.eventually (eventually_lt_nhds (div_pos hc (by norm_num)))
  obtain ⟨k, hkStage, hkProfiles, hkRoot, hk⟩ :=
    (eventually_exists_stage.and ((hprofiles ε hε hεone).and
      (hrootSmall.and (eventually_ge_atTop 5)))).exists
  obtain ⟨s⟩ := hkStage
  have hB : 0 < Fintype.card (CubeStage.Profile k) := Fintype.card_pos
  -- Preserve the cap theorem's established classical mask enumeration.
  have hcross := CubeStarCaps.masked_cross_density_lower (CubeGenerators.dimension k)
    (pow_pos (show 0 < k by omega) 6)
  obtain ⟨L, hL, ωA, ωB, hGood⟩ :=
    exists_arbitrarily_large_finite_assembled_graph (B := CubeStage.Profile k)
      (law k) s.coefficientUniform
      (baseGraph s.supports) s.triangleFree CubeStarCaps.cap ε (dyadicRate k) ε p
      (dyadicRate_pos k) hε hB s.independence (hkProfiles s) hcross (max N 1)
  have hLone : 1 ≤ L := (le_max_right N 1).trans hL
  have hLt : L ≤ replicationOrder (CubeStage.Profile k) L :=
    replicationOrder_ge hB hLone
  exact good_assembly_counterexample (B := CubeStage.Profile k)
    (ord := finiteMatchingOrder (CubeStage.Profile k))
    (baseGraph s.supports) CubeStarCaps.cap L ωA ωB
    p c ε (dyadicRate k) N hp hc hεquarter hεc hεp hkRoot
    (((le_max_left N 1).trans hL).trans hLt)
    (lt_of_lt_of_le Nat.zero_lt_one (hLone.trans hLt)) hGood

end Er579

end

/- Source fragment: Er579.Refutation. Original licenses and source proofs retained. -/

section

namespace Er579

open CubeStage CubeStarCaps
open Filter
open scoped Classical

-- Source: Er579.Refutation:9
/-- A fully constructive refutation in finite graph theory: no
unproved analytic certificate remains among the hypotheses. -/
theorem not_positiveDensityClaim : ¬ PositiveDensityClaim := by
  apply not_positiveDensityClaim_of_small_cube_profiles
  intro ε hε hε1
  obtain ⟨R, d, hd, hbound⟩ := maskedCompatibility_uniform_independent_mass_bound ε hε hε1
  filter_upwards [fixed_mask_error_eventually_lt R hd] with k hk
  intro s W hW
  have hgap : atomRate k + 2 * (2 : ℝ) * (R : ℝ) ^ 2 * starRate k < d := by
    norm_num
    exact hk
  exact (hbound (Profile k) (Profile k) inferInstance inferInstance
    (law k) (baseGraph s.supports) cap 2 (atomRate k) (starRate k)
    (starRate_nonneg k) (fun a => (s.coefficientAtoms a).le)
    s.commonCenters (fun b w z hbw _ _ => s.starMass b w z hbw)
    hgap (W : Set _) hW).le

end Er579

end

namespace Bounty

theorem target : ¬ (fcTypeOfName% "Erdos579.erdos_579") := by
  intro h
  exact Er579.not_positiveDensityClaim (h.mp True.intro)
