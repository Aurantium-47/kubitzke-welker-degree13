# Kubitzke–Welker Question 4.4 through degree twelve

**Status:** internally derived computer-assisted proof, 2026-11-04. This is a complete result for the stated degree range, with no coefficient-height restriction. It is not a proof of the unrestricted conjecture. The proof and finite certificate have been independently reproduced internally using a separate implementation. This is not external peer review. No publication-priority claim is made.

## Theorem

Let 1≤d≤12 and let h(t)=1+h₁t+⋯+h_dt^d have positive integer coefficients and only real zeros. Whenever 1<h₁<⋯<h_r, the vector

(1,h₁−1,h₂−h₁,…,h_r−h_{r−1})

is the f-vector of a simplicial complex.

For d≤11, real-rootedness can be replaced by the full degree-d Newton inequalities

i(d−i)h_i² ≥ (i+1)(d−i+1)h_{i−1}h_{i+1},  1≤i<d.

This latter extension is sharp in degree: a symmetric, strictly Newton-ULC integer counterexample occurs in degree 12.

## 1. Notation and the analytic inequality

Write g_i=h_i−h_{i−1}. Let K_k(a) be the Kruskal–Katona upper operator: if

a=binom(n_k,k)+⋯+binom(n_j,j),  n_k>⋯>n_j≥j,

then K_k(a)=binom(n_k,k+1)+⋯+binom(n_j,j+1). The target is g_{k+1}≤K_k(g_k) whenever k<r. Newton gives strict ordinary log-concavity, so all positive differences form an initial interval.

Define D=d(d−1)⋯(d−k+1) and α=(d−k)/D^(1/k). The elementary argument in finite_reduction.md proves, for g_k>0,

g_{k+1} < α (k!g_k)^((k+1)/k)/(k+1)!.                 (1)

For completeness, put L=k h_k/h_{k−1}>k, A=D^(1/k)/(d−k+1), B=(d−k)/(d−k+1), and y=(k!g_k)^(1/k). Monotonicity of i h_i/[(d−i+1)h_{i−1}] gives h_k≥(AL)^k/k!, hence

y/A≥L(1−k/L)^(1/k)≥L−1−k/(L−k).

The last inequality follows from log(1−u)≥−u/(1−u) and exp(x)≥1+x. Newton at k also gives

g_{k+1}≤g_k L(BL−k−1)/[(k+1)(L−k)].

The rational factor L(BL−k−1)/(L−k) equals

B[L−1−k/(L−k)]−(k+1)(1−B)L/(L−k) < By/A.

Since B/A=α, this proves (1). No unrefereed Macaulay lemma is used.

## 2. A certified infinite tail

If n is the leading upper index of the k-binomial expansion of a, then

binom(n,k)≤a<binom(n+1,k),  and  K_k(a)≥binom(n,k+1).

Choose an integer N>k satisfying the exact integer inequality

(d−k)^k [k! binom(N+1,k)]^(k+1)
≤ D [(k+1)! binom(N,k+1)]^k.                         (2)

Then g_{k+1}≤K_k(g_k) holds automatically for every g_k≥binom(N,k). Here is the justification that checking (2) once covers the **entire unbounded tail**.

For real x>k define

F_k(x)=[x(x−1)⋯(x−k)] / [(x+1)x⋯(x−k+2)]^((k+1)/k).

Its logarithmic derivative is

1/(x−k)+1/(x−k+1)−1/(x+1)−(1/k)∑_{j=0}^{k−1}1/(x+1−j),

which is positive because the final average is at most 1/(x−k+2). Thus F_k increases. Inequality (2) therefore holds with N replaced by every n≥N. Applying (1) and g_k<binom(n+1,k) proves the assertion.

The program computes the first valid N by exact integer comparisons. Existence also follows from F_k(x)→1 and α<1. No empirically chosen coefficient bound is used.

## 3. Every failure gives one of finitely many integer pairs

Fix d,k and suppose a failure occurs. Put q=g_k and v=K_k(q)+1. By integrality g_{k+1}≥v. Section 2 gives 1≤q<binom(N,k). Raising (1) to the k-th power shows that a failure requires

v^k ((k+1)!)^k D < (d−k)^k (k!q)^(k+1).             (3)

Set p=h_{k−1}, so h_k=p+q. To make the Newton-only scope explicit, set a_i=h_i/binom(d,i). The positive sequence (a_i) is log-concave with a_0=1 and a_d=h_d≥1, so a_i≥1 for every i. Thus p≥binom(d,k−1). Positivity of g_{k+1} and Newton at k imply

p < k(d−k)q/(d+1).                                  (4)

Newton at k, now using h_{k+1}≥p+q+v, also requires

k(d−k)(p+q)² ≥ (k+1)(d−k+1)p(p+q+v).                (5)

Finally, put t=k(p+q)/[(d−k+1)p]. Multiplying the preceding normalized-ratio inequalities from h₀=1 gives

p≥binom(d,k−1)t^(k−1),

or, equivalently,

p^k(d−k+1)^(k−1) ≥ binom(d,k−1) k^(k−1)(p+q)^(k−1). (6)

The verifier checks exactly all q in the justified range satisfying (3), and all integers p in the justified interval (4) and p≥binom(d,k−1), retaining precisely those satisfying (5) and (6). These are necessary conditions only, so rejecting a pair never requires guessing the rest of the coefficients or their roots.

## 4. The first inequality

The k=1 inequality requires no enumeration. Maclaurin gives h₁≥d and

h₂≤[(d−1)/(2d)]h₁²≤h₁(h₁−1)/2.

Consequently

g₂≤binom(h₁−1,2)−1=K₁(g₁)−1.

This also proves the result for d=2. In degree one, (1,h₁−1) is realized by h₁−1 isolated vertices; when h₁=1 there is no nonempty strictly increasing prefix.

## 5. Exhaustive exact output

The standalone executable verify_degree12.py uses only Python's standard library and arbitrary-precision integers. It enumerates all 55 pairs (d,k) with 3≤d≤12 and 2≤k≤d−1. Its complete output is degree12_certificate.json, including N, binom(N,k), counts, and every surviving pair. In total it checks 2,639,778 q values and 14,139,264 candidate p pairs.

All local candidate sets are empty except the following seven tuples (d,k,q,p,v):

- (11,2,41,11,95)
- (11,2,42,11,100)
- (12,2,50,12,131)
- (12,2,51,12,136)
- (12,2,52,12,142)
- (12,2,61,13,181)
- (12,2,62,13,187)

There is no floating-point arithmetic or approximate real-root test in this computation. The source contains assertions for the complete survivor list, not just its length.

For reference, the degree-12 infinite-tail cutoffs N for k=2,…,11 are

33,32,30,29,27,25,23,21,19,17,

giving q upper bounds binom(N,k) equal to

528,4960,27405,118755,296010,480700,490314,293930,92378,12376.

Every q beyond those bounds is handled by Section 2, not omitted.

## 6. Excluding the seven surviving pairs

For the first five tuples, k=2 and p=h₁=d. Maclaurin's inequalities and h_d≥1 force h_i=binom(d,i) for every i: the normalized root means form a nonincreasing chain from h₁/d=1 to h_d^(1/d)≥1. Thus q=h₂−h₁=binom(d,2)−d. This is 44 for d=11 and 54 for d=12, inconsistent with all five listed q-values.

For the final two tuples, d=12 and h₁=13=d+1. The classical small-trace classification, proved directly in small_trace_case.md using Kronecker's theorem, forces

h(t)=(1+t)^11(1+2t) or h(t)=(1+t)^10(1+3t+t²).

The corresponding h₂ values are 77 and 76, respectively, so q=h₂−h₁ is 64 or 63, never 61 or 62. Hence the final two candidates are impossible for a real-rooted polynomial.

All potential failures have now been excluded. Kruskal–Katona yields the required simplicial complex; a shorter increasing prefix corresponds to taking a skeleton.

## 7. Sharpness of the Newton-only degree range

The palindromic sequence

(1,13,74,255,575,921,1075,921,575,255,74,13,1)

has all degree-12 Newton inequalities strict. Their integer slacks are

83,125,53675,11525,18435,38691,18435,11525,53675,125,83.

Its differences have g₂=61 and g₃=181, whereas

61=binom(11,2)+binom(6,1),  K₂(61)=165+15=180.

Thus degree 12 is the smallest possible Newton-ULC integer counterexample degree, by the theorem for degrees ≤11. This polynomial is not real-rooted: its gamma-vector is (1,1,−2,6,−20,21,−3), while reciprocal pairing forces nonnegative gamma coefficients for a palindromic positive real-rooted polynomial. It is therefore not a counterexample to Q4.4.

## 8. Prior art and scope

- Kubitzke–Welker, original Question 4.4: https://www.mathematik.uni-marburg.de/~welker/preprints/Veronese.pdf . The target is the simplicial f-vector of positive initial differences.
- Brenti, 2024, Problem 2.10: https://arxiv.org/html/2410.09897v1 . The nearby bounded check d≤9 and h_i≤100 concerns Problem 2.9, the symmetric polytope h-vector question, not a complete-degree Q4.4 theorem.
- Bell–Skandera: https://www.lehigh.edu/~mas906/papers/logc.pdf . Their fixed-degree finiteness result concerns the original coefficient vector, not the initial differences.
- Ferudun, 17 October 2026: https://eulersolve.org/papers/owr-1782-017/ . The weaker Macaulay theorem is asserted there; the Kruskal–Katona strengthening remains explicitly open. Its discarded finite-degree Newton factor motivated (1), but the present certificate uses no unproved claim from that preprint.
- Mu–Welker, 2026: https://arxiv.org/html/2503.24076v2 . Their main problem concerns coefficients; their recursive-real-rootedness proposal was disproved by Liu–Wang–Zhang, https://arxiv.org/html/2609.23694 . Neither result settles Q4.4.
- The small-trace classification is classical: Smyth 1984, https://numdam.org/item/AIF_1984__34_3_1_0/ . No novelty is claimed for that ingredient.

Targeted current searches did not locate an existing unrestricted-coefficient degree-12 theorem for Q4.4 or the exact degree-12 Newton obstruction. That does not certify publication priority. The mathematical claim here is confined to the proved degree range and the reproducible certificate.


Independent internal audit files: independent_degree_certificate.py and independent_degree_referee.md. The independent implementation uses a different binomial-block Kruskal–Katona computation and reproduces every tail cutoff, power-filter count, and survivor in all 55 rows.
