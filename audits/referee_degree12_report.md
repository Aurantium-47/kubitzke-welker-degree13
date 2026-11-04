# Adversarial referee report: the degree-twelve theorem

**AI-only audit record.** This report was produced by a separate AI review process, not by an external human referee. It is not human peer review or formal proof-assistant verification.

Audit date: 2026-11-04. Scope: `degree12_proof.md`, `verify_degree12.py`, `independent_degree_certificate.py`, and the small-trace classification needed to close the proof.

## Verdict

**No fatal mathematical or computational gap was found.** The argument establishes Question 4.4 for every positive-integer coefficient polynomial of actual degree at most twelve satisfying real-rootedness, without a coefficient-height restriction. The Newton-only extension through degree eleven, and the statement that twelve is the smallest counterexample degree for that extension, also follow. These are bounded-degree conclusions, not a solution of the unrestricted question. This is an independent mathematical/code audit, not external peer review or a formal proof-assistant verification. Publication priority is not established.

Both submitted verifiers were rerun successfully. A third verifier, `referee_degree12_alternative.py`, was written and run successfully. It examines the same 2,639,778 q values in all 55 cases, but **does not use the power-bound pruning condition (3)**, **does not use the submitted strict p-range (4)**, and **does not scan that p-range**. It solves the local Newton constraint as a quadratic inequality and locates the earlier-ratio endpoint by bisection. It obtains exactly the same seven pairs. Its output is `referee_degree12_alternative.json`.

## 1. The problem being proved is the original problem

[Kubitzke–Welker, Question 4.4, p. 17](https://www.mathematik.uni-marburg.de/~welker/preprints/Veronese.pdf) asks about a positive integer coefficient real-rooted polynomial with constant coefficient one and any strictly increasing initial segment. Its desired vector consists of the constant one followed by successive differences. The current theorem matches these hypotheses and conclusion, not merely the weaker Macaulay statement, the original-coefficient f-vector conjecture, or the symmetric polytope question.

There is no missing requirement that the prefix end at the mode. Positive full Newton inequalities imply strict ordinary log-concavity, so coefficient ratios strictly decrease. The positive differences form an initial interval. Any shorter required prefix is the f-vector of a skeleton. In degree one only a vector (1,h_1−1) needs realization. If h_1=1 there is no nonempty strictly increasing prefix; the empty-face complex handles the optional length-zero convention.

The Kruskal–Katona direction is correct: if g_k counts k-element faces, the bound for the number of (k+1)-element faces is the operator obtained by increasing each lower binomial index while leaving its upper index fixed. The proof does not accidentally substitute Macaulay's larger operator.

## 2. Analytic inequality and the genuinely infinite tail

Write a_i=h_i/binom(d,i). The full Newton inequalities are precisely log-concavity of the positive sequence a_i. Its successive ratios are nonincreasing. This establishes every normalized-ratio inequality used in the manuscript, independently of roots.

For L=k h_k/h_{k−1}>k, multiplying the first k normalized-ratio inequalities gives h_k≥binom(d,k)[L/(d−k+1)]^k. The logarithmic/exponential estimate used to compare y=(k!g_k)^(1/k) to L is valid, including the regime where its lower bound is negative. The displayed rational-factor identity is exact. Its strictly negative correction is present for every k<d, so inequality (1) really is strict even when a sequence attains equality in Newton's inequalities.

The tail certificate compares positive quantities, and raising to the k-th power is legitimate. The stated logarithmic derivative of F_k is correct. For k≥2 its final average is at most 1/(x−k+2); hence the derivative is bounded below by

1/(x−k)+1/(x−k+1)−1/(x+1)−1/(x−k+2)>0.

Both differences can be grouped into strictly positive terms. Therefore a single valid N certifies every larger leading binomial index, not just a sampled list. Furthermore alpha<1 since each factor in D is larger than d−k, and F_k tends to one. A cutoff exists for every relevant d,k.

The finite and infinite regions meet without a gap: q=binom(N,k) belongs to the tail, while the code checks 1≤q<binom(N,k). Equality in the tail's integer comparison is safe because the analytic bound is strict. The q upper bounds in the manuscript all match the computed cutoffs.

## 3. Necessary finite conditions and arithmetic boundaries

Since a_0=1 and a_d=h_d≥1, log-concavity gives a_i≥1, hence p=h_{k−1}≥binom(d,k−1). This argument uses only the full Newton inequalities, not real-rootedness. Positivity of a failed g_{k+1} gives the strict upper p bound (4). The code's subtraction of one before integer division implements the strict inequality exactly, including when the rational endpoint is an integer.

For failure, integrality gives g_{k+1}≥K_k(q)+1. Substituting this least failing value in Newton gives (5) in the necessary direction. Product monotonicity through index k−1 gives (6) in the necessary direction. No replacement of a lower bound by an upper bound occurs. Rejecting on equality in the power filter is correct because the analytic inequality is strict.

The k=1 argument is correct: h_1≥d turns Newton's h_2 bound into h_2≤binom(h_1,2), which gives g_2≤binom(h_1−1,2)−1. Degree two needs no enumeration; degree one is immediate.

## 4. Independent computation by a different feasibility algorithm

For fixed d,k,q and v=K_k(q)+1, set A=k(d−k), C=d+1, B=A+C, and E=(A−C)q−Bv. Condition (5) is exactly

−C p²+E p+Aq²≥0.

Its roots have opposite signs. Thus its nonnegative integer feasible interval ends at

floor((E+sqrt(E²+4CAq²))/(2C)).

The third verifier computes this endpoint using integer square root and checks that the Newton slack is nonnegative there and negative at the next integer. The predicate (6) is increasing with p because p^k/(p+q)^(k−1) is strictly increasing for p>0. Bisection therefore finds the other endpoint. This gives every locally feasible p without the submitted p-bound or power-bound filters.

Its Kruskal–Katona routine is a separate linear combinadic implementation. On every surviving pair it additionally checks the dual characterization: the lower shadow of v exceeds q, while the lower shadow of v−1 is at most q. The complete resulting (d,k,q,p,v) list is

- (11,2,41,11,95), (11,2,42,11,100);
- (12,2,50,12,131), (12,2,51,12,136), (12,2,52,12,142);
- (12,2,61,13,181), (12,2,62,13,187).

This agrees with both submitted programs. All arithmetic is exact Python integer arithmetic; there are no numerical root tests or coefficient cutoffs.

## 5. Exclusion of the exceptions

For p=d the surviving index is always k=2, so h_1=d. Normalized log-concavity gives a_1=1 and nonincreasing ratios a_i/a_{i−1}; all later ratios are at most one. But a_d≥1, so every ratio must equal one. Consequently h_i=binom(d,i). This excludes the first five pairs and proves the Newton-only degree-eleven claim without invoking real-rootedness at this step.

For d=12 and h_1=13, the small-trace classification is valid. Reciprocal roots are totally positive algebraic integers. The positive integral product and AM–GM argument force every root below four; d≤3 is separately safe by the sum bound. For beta=alpha−2 all conjugates lie in (−2,2). A solution of z²−beta z+1=0 is an algebraic integer all of whose conjugates have modulus one, so [Kronecker's theorem](https://webhomes.maths.ed.ac.uk/~chris/papers/variations1905-4.pdf) makes z a root of unity.

The degree and trace of an irreducible alpha factor are n=phi(m)/2 and 2n+mu(m), respectively. The trace excess is n+mu(m), not n+mu(m)/2. Each irreducible factor has nonnegative integral excess by AM–GM and its positive integer norm. Excess one permits only x−1, x−2, and x²−3x+1, with exactly one factor of excess one. Multiplicities create no exception. The two resulting polynomials have h_2=77 or 76, giving q=64 or 63, excluding q=61,62.

This step genuinely uses real-rootedness. It is not being incorrectly applied to the Newton-only degree-twelve example.

## 6. Sharpness and non-real-rootedness

The palindromic integer vector in the manuscript was checked independently. Its eleven Newton slacks are exactly the listed positive integers. Its first relevant failure is g_2=61, g_3=181 with K_2(61)=180. Therefore it is a strict full-Newton counterexample in degree twelve, and the already established degree-eleven theorem makes that degree minimal.

The gamma-vector independently recomputes to (1,1,−2,6,−20,21,−3). If this palindromic positive polynomial were real-rooted, all roots would be negative and reciprocal pairs would yield factors (1+t)²+c t with c≥0. The gamma coefficients would all be nonnegative. The negative coefficient gamma_2 already rules this out exactly. It is not a counterexample to Question 4.4.

## 7. Prior art and presentation recommendations

The original Brenti faculty URL returned 404 in this audit. Use [the verified arXiv version](https://arxiv.org/html/2410.09897v1), Problems 2.9–2.10. It confirms that the d≤9 and h_i≤100 computation concerns the symmetric polytope h-vector problem, not an unrestricted-height solution of Question 4.4.

[Bell–Skandera, Theorem 4.8](https://www.lehigh.edu/~mas906/papers/logc.pdf) is about the coefficient vector. [Mu–Welker](https://arxiv.org/html/2503.24076v2) likewise study the coefficient-vector question. [Liu–Wang–Zhang](https://arxiv.org/html/2609.23694) disprove a recursive-real-rootedness proposal, not the f-vector problem. The [Ferudun preprint](https://eulersolve.org/papers/owr-1782-017/) explicitly leaves the Kruskal–Katona strengthening open; the current proof does not depend on its asserted Macaulay lemma. [Smyth's 1984 classification](https://numdam.org/item/AIF_1984__34_3_1_0/) already treats much greater trace excess, so no novelty should attach to the small-trace ingredient.

Targeted searches for the original question, its initial-difference formulation, low-degree results, and the exact counterexample did not locate the same unrestricted-height degree-twelve result or the exact sharp Newton-only threshold. This is not an exhaustive literature review or a priority certificate. Keep the manuscript's no-priority-claim language.

Recommended small changes, none needed to repair a fatal gap:

1. Explicitly include the a_i=h_i/binom(d,i) argument above, so the use of Maclaurin inequalities in the Newton-only extension is completely transparent.
2. Give the degree-one realization in one sentence rather than leaving it implicit in the degree-two discussion.
3. Replace the broken Brenti link with the verified arXiv URL.
4. State the inspected verification counts (2,639,778 q values and 14,139,264 pairs in the submitted scanning implementation), and distribute source plus certificates together.
5. Describe this as an internally independently checked computer-assisted proof in a bounded degree range, rather than as an externally refereed theorem or resolution of the whole conjecture.
