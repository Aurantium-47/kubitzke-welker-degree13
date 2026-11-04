# A degree-sensitive bound for initial differences

Status: internally derived on 2026-11-04. This is a partial result, not a solution of Kubitzke–Welker Question 4.4. No novelty claim has been established. It is motivated by retaining the finite-degree Newton factor that the 2026 Ferudun preprint discards. The elementary finite-reduction corollary below does not depend on that preprint's discrete Macaulay estimate.

## Statement

Let d≥2, h_0=1 and h_1,…,h_d be positive real numbers such that h_i/binom(d,i) is log-concave. Write g_i=h_i−h_{i−1}. If 1≤k≤d−1 and g_k>0, then

g_{k+1} ≤ α_{d,k} (k!g_k)^((k+1)/k)/(k+1)!,

where α_{d,k}=(d−k)/(d(d−1)…(d−k+1))^(1/k)<1.

In fact, the inequality is strict. This improves the degree-independent factor 1 for each fixed degree. The leading constant α_{d,k} is optimal: take h(t)=(1+mt)^d and let m→∞.

## Proof

Set ρ_i=h_i/h_{i−1} and λ_i=iρ_i. Newton log-concavity says that λ_i/(d−i+1) is nonincreasing. Let L=λ_k>k, B=(d−k)/(d−k+1), and

A=(d(d−1)…(d−k+1))^(1/k)/(d−k+1).

For i≤k, λ_i≥L(d−i+1)/(d−k+1), and hence

h_k=(1/k!)∏_{i=1}^k λ_i ≥ (AL)^k/k!.

As g_k=h_k(L−k)/L, putting y=(k!g_k)^(1/k) gives

y≥AL(1−k/L)^(1/k).

For 0<u<1 one has

(1−u)^(1/k) ≥ 1−u/[k(1−u)].

One elementary proof uses log(1−u)≥−u/(1−u) and exp(v)≥1+v. Thus

y/A≥L−1−k/(L−k).

Also ρ_{k+1}≤BL/(k+1), so

g_{k+1}≤[g_k/(k+1)] L(BL−k−1)/(L−k).

The last rational expression equals

B[L−1−k/(L−k)]−(k+1)(1−B)L/(L−k),

and is therefore strictly less than B y/A. Since B/A=α_{d,k}, the theorem follows.

For sharpness, g_k=binom(d,k)m^k−binom(d,k−1)m^(k−1). Dividing g_{k+1} by (k!g_k)^((k+1)/k)/(k+1)! and taking m→∞ yields α_{d,k} exactly.

## An elementary Kruskal–Katona lower estimate

For a positive integer a, let K_k(a) be the simplicial Kruskal–Katona upper operator: if a=∑ binom(n_i,i) is its k-binomial expansion, K_k(a)=∑ binom(n_i,i+1). Let y=(k!a)^(1/k), and let n be the leading upper index. Since a<binom(n+1,k)≤(n+1)^k/k!, one has n>y−1.

If y>k+1, then

K_k(a)≥binom(n,k+1)≥(n−k)^(k+1)/(k+1)! > (y−k−1)^(k+1)/(k+1)!.

Consequently the degree-sensitive theorem proves g_{k+1}≤K_k(g_k) whenever

(k!g_k)^(1/k)≥T_{d,k}:=(k+1)/(1−α_{d,k}^(1/(k+1))).

This estimate uses only the leading term of the exact binomial expansion. It is not a numerical experiment or an asymptotic-only assertion.

## Explicit finite reduction for Question 4.4

Now suppose all h_i are positive integers and h_0<h_1<…<h_r, where r is the first peak. Every potential failure g_{k+1}>K_k(g_k), 1≤k<r, satisfies

g_k<T_{d,k}^k/k!.

Since g_{k+1}>0, Newton's inequality gives

h_{k−1}/h_k < k(d−k)/[(k+1)(d−k+1)],

and therefore

h_k < [(k+1)(d−k+1)/(d+1)] g_k.

Because h_1≤h_k, every counterexample satisfies

h_1 < M_d := max_{1≤k≤d−1} [(k+1)(d−k+1)/(d+1)] T_{d,k}^k/k!.

Maclaurin's inequalities now give the explicit coefficient bounds

h_j≤binom(d,j)(h_1/d)^j < binom(d,j)(M_d/d)^j.

Thus, for each fixed d, only finitely many positive integer, real-rooted polynomials can violate Question 4.4. This also holds for the larger class satisfying degree-d Newton inequalities. The bound gives a genuinely finite exact decision procedure for each fixed degree, using Sturm or an exact real-root count on the bounded integer candidates. The follow-up degree12_proof.md, degree13_extension.md and their verifiers complete a sharper exact finite-pair reduction for all degrees through 13; this general-bound note itself does not enumerate arbitrary degrees.

## Stronger threshold using the 2026 discrete estimate

Ferudun's Lemma D proves the Macaulay estimate M_k(a)≥(k!a)^((k+1)/k)/(k+1)!. Since K_k(a)=M_k(a)−a, it suffices instead that

(k!g_k)^(1/k)≥(k+1)/(1−α_{d,k}).

This substantially smaller threshold is conditional only on the correctness of that stated lemma (which has an explicit proof in the unrefereed preprint). The elementary threshold above avoids that dependence.

## Scope and checked prior art

1. Original Bell–Skandera: https://www.lehigh.edu/~mas906/papers/logc.pdf . Coefficient f-vector question is Question 1.1/Conjecture 4.1. Theorem 4.8 already proves finitely many possible coefficient-vector counterexamples in each fixed degree; it does not discuss initial differences.
2. Original Kubitzke–Welker: https://www.mathematik.uni-marburg.de/~welker/preprints/Veronese.pdf . Question 4.4 is precisely the initial-difference f-vector question, not the weaker Macaulay/M-sequence statement.
3. Ferudun 2026: https://eulersolve.org/papers/owr-1782-017/ and its PDF. It claims the weaker Brenti–Welker Macaulay theorem and explicitly leaves the Kruskal–Katona strengthening open.
4. Mu–Welker 2026: https://arxiv.org/html/2503.24076v2 . The general coefficient problem remains open. Its real-binomial sufficient condition is not implied by mere Newton log-concavity.
5. Liu–Wang–Zhang 2026: https://arxiv.org/html/2609.23694 . They already disprove Mu–Welker's recursive-decomposition real-rootedness question in every degree at least three. Their counterexamples themselves have simplicial realizations and do not disprove Bell–Skandera.

Targeted searches for a fixed-degree finite-exception theorem for initial differences did not locate one, but that is not a proof of novelty.

## Exact analytic obstruction

The integer polynomial 1+6t+12t²+12t³+6t⁴+t⁵ has degree-5 Newton log-concavity: the four inequalities are 36≥30, 144≥144, 144≥144, 36≥30. Nevertheless its coefficient vector is not simplicial: 12=binom(5,2)+binom(2,1), so K_2(12)=binom(5,3)+binom(2,2)=11<12. It is not real-rooted, and this does not refute either actual target.


## Exact Newton-only obstruction for the difference question

Let h=(1,13,74,255,570,906,1050,894,555,245,73,13,1). For d=12 the integer Newton slacks

 i(12−i)h_i²−(i+1)(13−i)h_{i−1}h_{i+1}

are, for i=1,…,11,

83, 125, 68475, 450, 1260, 1764, 1260, 450, 75, 1475, 107.

They are all strictly positive. Its increasing initial differences are (1,12,61,181,315,336,144). But 61=binom(11,2)+binom(6,1), so K_2(61)=binom(11,3)+binom(6,2)=180<181. Thus even all finite-degree Newton inequalities, strict ultra-log-concavity, and integrality of every coefficient cannot settle Question 4.4. This is a counterexample only to that broader assertion, not to real-rooted Question 4.4.

An exact rational Sturm computation finds four real roots, not twelve. The Sturm sequence has degrees 12,11,…,0. Its leading coefficient signs are (+,+,+,−,−,+,+,+,−,−,−,+,+), giving four variations at +infinity; at −infinity the signs are (+,−,+,+,−,−,+,−,−,+,−,−,+), giving eight variations. The difference is four. These signs are independently reproducible using SymPy Poly.sturm() over QQ.


## The exact sharp envelope (stronger than the power bound)

For d≥2 and 1≤k≤d−1, define

D_{d,k}(t)=binom(d,k)t^k−binom(d,k−1)t^(k−1).

This is strictly increasing on t>a:=k/(d−k+1), runs from zero to infinity there, and hence for q>0 there is a unique t_q>a satisfying D_{d,k}(t_q)=q. Under the hypotheses of the first theorem,

g_{k+1}≤D_{d,k+1}(t_{g_k}).

This bound is attained for every real q>0, by h(z)=(1+t_q z)^d; thus it is the exact optimal continuous bound for consecutive differences among degree-d Newton-ULC sequences with constant term one. Integrality is not assumed here.

Proof: Put ρ=h_k/h_{k−1}>1 and t=kρ/(d−k+1)>a. Newton ratio monotonicity gives h_k≥binom(d,k)t^k, whence

g_k=h_k(1−a/t)≥D_{d,k}(t).

Thus t≤t_q for q=g_k. With b=(d−k)/(k+1), Newton at k gives

g_{k+1}≤h_k(bt−1)=q R(t), where R(t)=t(bt−1)/(t−a).

The derivative is R′(t)=b+a(1−ab)/(t−a)^2>0, since ab=k(d−k)/[(k+1)(d−k+1)]<1. Therefore

g_{k+1}≤qR(t_q)=D_{d,k+1}(t_q).

The final identity follows from binom(d,k−1)/binom(d,k)=a and binom(d,k+1)/binom(d,k)=b. Equality for the binomial family is immediate. No priority claim is made for this envelope; it is an internally derived sharp reformulation of Newton's inequalities.


## The first KK inequality is automatic

For positive integer coefficients with degree-d Newton inequalities, Maclaurin gives h_1≥d because h_d≥1. It also gives h_2≤[(d−1)/(2d)]h_1²≤h_1(h_1−1)/2. Therefore

g_2=h_2−h_1≤h_1(h_1−3)/2=binom(h_1−1,2)−1=K_1(g_1)−1.

Thus k=1 is never a failing KK inequality. In the finite-reduction bound one may restrict the maximum to 2≤k≤d−1; degrees d≤2 are automatic.


### A palindromic variant of the Newton-only obstruction

The same KK failure is present even under palindromicity. Take

h=(1,13,74,255,575,921,1075,921,575,255,74,13,1).

Its full degree-12 Newton slacks are

83,125,53675,11525,18435,38691,18435,11525,53675,125,83,

all strictly positive, and its differences still have g_2=61 and g_3=181>K_2(61)=180. Its gamma-vector is (1,1,−2,6,−20,21,−3), so it cannot be real-rooted: a palindromic positive real-rooted polynomial factors into reciprocal quadratic pairs (1+t)^2+λt with λ≥0, and consequently has nonnegative gamma coefficients. This is an elementary non-real-rootedness certificate. A rational Sturm computation independently finds just two real roots. This symmetric variant is also only a counterexample to the Newton-ULC extension, not to Question 4.4.
