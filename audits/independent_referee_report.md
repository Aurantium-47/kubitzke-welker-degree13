# Independent mathematical referee report

**AI-only audit record.** This report was produced by a separate AI review process, not by an external human referee. It is not human peer review or formal proof-assistant verification.

Date: 2026-11-04. Reviewed `finite_reduction.md`, including its appended exact envelope and degree-12 example. This report does not establish novelty or solve Question 4.4.

## Verdict

No fatal mathematical gap found. The degree-sensitive strict inequality, its optimal leading constant, the elementary KK threshold, the fixed-degree finiteness conclusion, and the exact continuous envelope all check. The degree-12 example is a valid counterexample to the stronger assertion for arbitrary integer Newton-ULC sequences; it is not real-rooted. One inaccurate comparison with Mu–Welker was identified and has already been corrected in the note.

## Quantifiers and the original target

[Kubitzke–Welker, Question 4.4, p. 17](https://www.mathematik.uni-marburg.de/~welker/preprints/Veronese.pdf) concerns every strictly increasing initial prefix of a positive-integer real-rooted polynomial with constant coefficient one. This is the simplicial f-vector condition, not just Macaulay growth. Checking the longest such prefix suffices: a shorter prefix is the f-vector of a skeleton. The peak may occur at the final coefficient, and the proof still includes the required k=d−1 comparison. A plateau at the peak introduces no additional positive difference to test.

The theorem fixes the ACTUAL degree d and assumes positivity of all d+1 coefficients. The statement does not cover arbitrary trailing zero padding or a uniform bound across all degrees. Degrees zero and one are trivial; degree two is also automatically valid by the observation below.

## Core bound

Write a_i=h_i/binom(d,i). Log-concavity of a_i is exactly monotonicity of λ_i/(d−i+1), with λ_i=i h_i/h_{i−1}. Consequently all the product bounds have the stated direction. Since g_k>0, L>k, so every division by L−k and every kth root is legitimate.

The identity for L(BL−k−1)/(L−k) is exact. Its subtracted term is strictly positive because B<1 and L>k, so strictness follows even without tracking strictness in the logarithmic estimate. B/A is precisely the displayed α. Every factor in the geometric mean defining α exceeds d−k, proving 0<α<1.

For the binomial family, leading terms give the claimed limiting ratio α. Taking m through positive integers establishes optimality even when the original coefficients are required to be integers. This is optimality of the leading multiplicative constant, not equality at finite m.

## KK and finite reduction

The leading-index estimate n>y−1 is valid, including k=1. The condition y>k+1 makes every subsequent power comparison positive. The proposed threshold T is larger than k+1, and algebraically it is exactly the condition α y^(k+1) ≤ (y−k−1)^(k+1). The strict theorem and strict KK lower estimate comfortably cover equality at the threshold.

For a failed comparison inside the positive initial differences, g_{k+1}>0. Newton then yields

  h_{k−1}/h_k < k(d−k)/[(k+1)(d−k+1)].

Its complement is (d+1)/[(k+1)(d−k+1)], giving the stated upper bound for h_k in terms of g_k. Since this is an increasing prefix, h_1≤h_k. Thus the bound really controls h_1; there is no remaining free, unbounded early coefficient. Normalized ratio monotonicity gives h_j≤binom(d,j)(h_1/d)^j for EVERY later j, so there is no unbounded-tail loophole either.

For each fixed degree, M_d is finite. Bounded positive-integer coefficient vectors form a finite set. Exact real-root testing, with multiplicities properly accounted for, plus exact binomial expansions decides every candidate. The conclusion is mathematically effective, not necessarily computationally practical, and does not decide all degrees simultaneously.

If desired, a completely rational larger bound can replace the algebraic threshold: α≤(d−k)/(d−k+1) and concavity imply T≤(k+1)^2(d−k+1). This also makes an elementary finite enumerating box immediate without evaluating radicals.

## Exact envelope

D_{d,k}(t)=binom(d,k)t^(k−1)(t−a) is strictly increasing from zero to infinity on t>a. Thus t_q exists uniquely for every real q>0. The inference t≤t_q is correct.

The important sign check passes: h_k is replaced by the EXACT identity q t/(t−a), not a lower bound. Therefore the argument remains valid when bt−1<0. Direct differentiation gives R′(t)=b+a(1−ab)/(t−a)^2>0. The last binomial identity and the claimed equality family both hold.

This is pointwise optimal over positive REAL Newton sequences. It does not claim the envelope is attained by integer coefficients for an arbitrary positive integer q. No such unwarranted attainment claim appears in the current note.

## Macaulay-dependent improvement

[Ferudun, Section 4](https://eulersolve.org/papers/owr-1782-017/paper.pdf?v=e38749f8ac54) states and proves the cited lower estimate. I checked the induction, the n=k exceptional case, convex-chord bound, minimization, and final AM–GM estimate; no error was found. In particular, separating n=k is essential and is done correctly. Pascal's identity gives K_k(a)=M_k(a)−a term by term, and substituting the lower estimate gives exactly the smaller threshold (k+1)/(1−α). Keeping the elementary corollary independent of this unrefereed source remains sensible.

## Exact examples and reproducible tests

Run `python extras/independent_audit.py` from the workspace. It performs:

- 75,000 exact checks of the Macaulay lower estimate and K=M−a for 1≤k≤15, 1≤a≤5000.
- 10,000 seeded rational Newton-ULC sequences, degrees 2–16, testing 64,094 positive transitions with radical-free exact inequalities.
- 336 positive-transition checks from binomial-family integer examples.
- Independent exact verification of both displayed obstruction examples.

For the degree-12 tuple, all eleven Newton slacks equal the supplied positive integers. Its first peak is at index 6, and the positive differences are (1,12,61,181,315,336,144). The 2-binomial expansion of 61 yields K_2(61)=165+15=180<181. The rational Sturm degrees and all signs match the note, with variations 8 and 4; gcd(p,p′)=1. It has exactly four real roots and eight nonreal roots. The degree-5 example has exactly three real roots, and K_2(12)=11. These tests are independent checks, not exhaustive conjecture verification.

## Prior art and wording

[Bell–Skandera, Theorem 4.8](https://www.lehigh.edu/~mas906/papers/logc.pdf) already proves fixed-degree finiteness for counterexamples to the COEFFICIENT f-vector question. It does not state the initial-difference finiteness theorem reviewed here. The analogy should remain explicit.

[Mu–Welker](https://arxiv.org/html/2503.24076v2) explain that their sufficient real-binomial condition is not necessary for real-rooted polynomials and can hold even for a polynomial that is not log-concave. Therefore calling it simply “stronger than Newton” was misleading. The corrected “not implied by mere Newton log-concavity” is supported. [Liu–Wang–Zhang](https://arxiv.org/html/2609.23694) concern failure of a recursive-decomposition real-rootedness property, not a counterexample to the coefficient f-vector question.

Targeted searches for initial differences, fixed-degree/finitely-many exceptions, Newton inequalities, and Question 4.4 did not locate an existing matching finiteness or exact-envelope theorem. This limited search is not a novelty certificate.

## Optional low-index sharpening

Under the integer hypotheses, normalized log-concavity and h_d≥1 give h_i≥binom(d,i), in particular h_1≥d. Newton at index 1 therefore implies

  h_2≤(d−1)h_1²/(2d)≤h_1(h_1−1)/2,

and hence g_2≤binom(h_1−1,2)−1=K_1(g_1)−1. Thus k=1 can never be a failed comparison. This is an optional improvement, not a repair required for the published bound.

## Additional audit: the all-degree small-trace subcase

`small_trace_case.md` also passes, subject only to harmless endpoint conventions. The monic reciprocal polynomial makes the positive reciprocal roots algebraic integers and includes all of their conjugates. AM–GM correctly forces h_1≥d. When the trace is d+1, the function M((d+1−M)/(d−1))^(d−1) is decreasing in the needed range, and its value at M=4 is below 1. Therefore all roots are strictly below 4.

The interval version of Kronecker used here follows directly from the [unit-disc theorem stated by Dubickas–Smyth](https://webhomes.maths.ed.ac.uk/~chris/papers/variations1905-4.pdf): for β=α−2, a root z of z²−βz+1 is a nonzero algebraic integer whose conjugates all have modulus one, hence a root of unity. The conjugate-pair trace is correctly 2n+μ(m), not 2n+μ(m)/2. Every irreducible factor has nonnegative integral excess by its positive integral norm and AM–GM. Excess at most one leaves exactly x−1, x−2, and x²−3x+1. Repeated factors cause no loophole.

The ballot families are downward closed: deletion moves each remaining element to an earlier index, weakening the inequalities. Their natural inclusions make each cone union a simplicial complex with exactly the claimed intersection. Reflection-principle counts and the parity cases match the coefficient differences. The first peaks are floor(d/2), ceil(d/2), and floor(d/2), respectively; the middle equality in the odd palindromic cases contributes no positive extra entry. Shorter allowed prefixes are skeletons, exactly as required by Question 4.4.

I independently enumerated the full face sets in every applicable family for d=1,...,18, totaling 53 tests. All were downward closed and all f-vectors matched the positive initial differences. These checks are now included in `independent_audit.py`.

Small editorial fixes recommended: explicitly assume d≥1; define binom(n,j)=0 outside 0≤j≤n; and describe B_n as a complex consisting of subsets of [n], rather than asserting that its actual vertex set is [n], since label 1 never occurs. For d=1, h=1+t gives the complex {empty set} and no positive nonconstant difference; the original Q4.4 has no strict nonempty prefix in this case. The other d=1 case and both d=2 cases work exactly as written.

Arithmetic priority is thoroughly classical: [Smyth's 1984 paper](https://numdam.org/item/AIF_1984__34_3_1_0/) classifies totally positive algebraic integers with trace minus degree at most six, a much wider range than needed here. The short Kronecker proof is valid but should not be presented as a new classification. Whether the explicit combination with ballot complexes was previously stated for Question 4.4 remains unestablished.

## Additional palindromic obstruction

The subsequently appended tuple (1,13,74,255,575,921,1075,921,575,255,74,13,1) has exactly the listed positive Newton slacks, and the same g_2=61, g_3=181 KK failure. Its gamma expansion is exactly (1,1,−2,6,−20,21,−3). If a palindromic positive-coefficient polynomial were real-rooted, pairing negative reciprocal roots would factor each quadratic as (1+t)^2+c t with c≥0, forcing all gamma coefficients to be nonnegative. Thus the negative entries are an exact non-real-rootedness certificate. Independent rational Sturm testing gives two real roots and gcd(p,p′)=1. This is a valid stronger illustration that symmetry does not rescue the Newton-only implication, still not a counterexample to Question 4.4.
