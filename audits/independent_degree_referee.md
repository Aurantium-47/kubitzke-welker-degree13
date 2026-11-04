# Independent audit of the degree-at-most-12 certificate

**AI-only audit record.** This report was produced by a separate AI review process, not by an external human referee. It is not human peer review or formal proof-assistant verification.

Date: 2026-11-04. Verdict: the complete finite-tail argument and its exact arithmetic enumeration independently reproduce. They establish the asserted Q4.4 conclusion for every actual degree d≤12, without a coefficient-height bound. This is not a solution in unrestricted degree and no novelty claim has been established.

## Independent implementation and output

Run `python src/independent_degree_certificate.py`.

This program imports none of the author's routines. Instead of the author's greedy binary-search KK implementation, it tabulates KK by the independent binomial-block recurrence

  K_k(binomial(n,k)+b)=binomial(n,k+1)+K_{k−1}(b),

for 0≤b<binomial(n,k−1), with K_1(a)=a(a−1)/2 and K_k(0)=0. Its output is `independent_degree_certificate.json`.

The run examined 2,639,778 integers q across all 55 pairs 3≤d≤12 and 2≤k≤d−1. All cutoff indices, cutoff heights, power-bound survivor counts, and final local pairs match the author's `degree12_certificate.json`. The author's recorded 14,139,264 local-pair checks are consistent with the loop ranges. Every comparison is an exact integer comparison; no floating-point root or tolerance enters.

## Why the infinite tail is covered

Let F=d(d−1)⋯(d−k+1), C=((k+1)!)^k F, and D=(d−k)^k(k!)^(k+1). The strict power bound implies that a failed KK comparison requires

  C(K_k(q)+1)^k < D q^(k+1),  q=g_k.

For n≥k+1, select N so that D binomial(N+1,k)^(k+1)≤C binomial(N,k+1)^k. Existence and persistence for every n≥N must be proved, not inferred from one numerical crossing. Both hold here: after canceling factorials, the n-dependent ratio is

  R(n)=(n+1)^(k+1) ∏_{j=0}^{k−2}(n−j) / [(n−k+1)^k(n−k)^k].

There are 2k numerator factors and 2k denominator factors. Every numerator has a larger additive offset than either denominator. Pairing factors expresses R as a product of functions (n+a)/(n+b) with a>b, so R strictly decreases to 1. The required right-hand constant is F/(d−k)^k>1. Therefore the cutoff search terminates and its first passing index covers the whole tail.

For any q≥Q=binomial(N,k), let n be the leading binomial index of q. Then n≥N, q<binomial(n+1,k), and K_k(q)≥binomial(n,k+1). The tail inequality and the strict power bound exclude failure. Thus only the EXACT finite range 1≤q<Q remains. Equality in the cutoff inequality is safe; equality in the necessary strict power comparison rules out failure.

## Every local filter is necessary

Suppose a genuine failure occurs, and write p=h_{k−1}, c=p+q=h_k, and v=K_k(q)+1≤g_{k+1}. Normalized log-concavity, h_0=1 and h_d≥1 imply h_i≥binomial(d,i). In particular p≥binomial(d,k−1).

The positivity of g_{k+1} and Newton at k give p<k(d−k)q/(d+1). Its exact integer upper bound is floor((k(d−k)q−1)/(d+1)), as used in both programs.

Newton at k also necessarily gives

  k(d−k)c² ≥ (k+1)(d−k+1)p(c+v).

Replacing the actual next difference by its minimum possible v only weakens this restriction. The preceding normalized ratios are all at least k c/((d−k+1)p); multiplying them yields the further necessary condition

  p^k(d−k+1)^(k−1) ≥ binomial(d,k−1)(k c)^(k−1).

Neither weak inequality incorrectly discards equality. The enumeration does not assume these conditions are sufficient; every genuine counterexample must survive, which is all the exclusion argument needs.

The range includes k=d−1. The omitted k=1 case was already proved impossible. Degrees d≤2 are automatic. A maximal positive initial-difference vector satisfying KK also supplies every shorter prefix by taking a skeleton, covering Q4.4's full quantifier.

## All seven survivors are impossible

The complete local survivors, in the order (d,k,q,p,v), are

  (11,2,41,11,95), (11,2,42,11,100),
  (12,2,50,12,131), (12,2,51,12,136), (12,2,52,12,142),
  (12,2,61,13,181), (12,2,62,13,187).

When p=d, k=2 means h_1=d. Normalized log-concavity alone forces h_i=binomial(d,i): its normalized coefficients are at least one by the endpoint argument and at most one by ratio monotonicity from a_0=a_1=1. Thus q must be 44 for d=11 or 54 for d=12, excluding the first five pairs.

The final two pairs have d=12,h_1=13. The independently audited small-trace classification leaves only (1+t)^11(1+2t) and (1+t)^10(1+3t+t²), whose q=h_2−h_1 values are respectively 64 and 63. They cannot realize q=61 or62. This is the only step requiring real-rootedness beyond Newton inequalities in this certificate.

A stronger accompanying conclusion is therefore supported: positive integer Newton-ULC sequences satisfy the initial-difference f-vector assertion through degree 11. The verified degree-12 ULC examples show that 12 is the least failing degree for that broader assertion.

## Prior degree coverage and limitations

[Brenti 2024, Section 2](https://arxiv.org/html/2410.09897v1) reports a check with d≤9 and all h_i≤100 for Problem 2.9, the symmetric h-vector/simplicial-polytope problem. That sentence does not claim this range for Problem 2.10, which is Q4.4. The present exact-tail certificate is not merely a repetition of that bounded-height check. Targeted searches did not establish whether the same unrestricted-height degree≤12 theorem was already known. Further expert/literature review is needed before any priority claim or external submission.
