# An all-degree arithmetic subcase of Question 4.4

Status: internally derived; no novelty claim. The proof is independent of numerical searches. It uses classical Kronecker classification and an explicit ballot-complex realization.

## Theorem

Let d≥1 and let h(t)=1+h_1t+…+h_dt^d have positive integer coefficients and only real zeros. If h_1≤d+1, then its positive initial differences are the f-vector of an explicitly described simplicial complex.

Indeed, h is one of the following polynomials:

1. (1+t)^d;
2. (1+t)^(d−1)(1+2t), for d≥1;
3. (1+t)^(d−2)(1+3t+t²), for d≥2.

## Classification

Write h(t)=∏_{i=1}^d(1+α_i t), with α_i>0. The α_i are all roots of the monic integer polynomial x^d h(−1/x); explicitly ∏(x−α_i)=x^d−h_1x^(d−1)+…+(−1)^d h_d. Thus they are totally positive algebraic integers, their sum is h_1, and their product h_d is a positive integer.

AM–GM gives h_1≥d. Equality forces every α_i=1, yielding case 1.

Suppose h_1=d+1. Every α_i is less than 4. For d≤3 this follows immediately from their positive sum. For d≥4, if M=max α_i≥4, AM–GM on the remaining roots gives

1≤h_d≤M[(d+1−M)/(d−1)]^(d−1).

The expression on the right decreases in M for M>(d+1)/d. At M=4 it is

4[1−2/(d−1)]^(d−1)<4e^(−2)<1,

a contradiction.

Classical Kronecker's theorem implies that a totally real algebraic integer β with all conjugates in (−2,2) is ζ+ζ^(−1) for a root of unity ζ. Applying this to β=α−2 shows that every irreducible factor has roots of the form 2+ζ+ζ^(−1), with ζ a primitive m-th root for some m≥3. Its degree is n=φ(m)/2 and its trace is 2n+μ(m), so its trace minus its degree is n+μ(m).

Each factor has nonnegative integer trace excess (also immediate from AM–GM and its positive integer norm). Total excess is 1. Thus every nontrivial factor has n+μ(m)≤1, implying n≤2. For degree 1 the possible m are 3,4,6, giving α=1,2,3 and excess 0,1,2. For degree 2 the possible m are 5,8,10,12; only m=5 has excess at most 1. Its minimal polynomial is x²−3x+1, with excess 1. Hence all factors are x−1, with exactly one additional factor x−2 or x²−3x+1. This gives cases 2 and 3.

Kronecker reference, including the interval formulation: Lemma 2.1 and its proof in https://pmc.ncbi.nlm.nih.gov/articles/PMC12107117/ . A primary reference for the unit-circle theorem is Dubickas–Smyth, https://webhomes.maths.ed.ac.uk/~chris/papers/variations1905-4.pdf . The trace formula is the standard sum of primitive m-th roots, ∑_{gcd(j,m)=1}ζ^j=μ(m), paired under conjugation.

## Explicit simplicial realization

Use binom(n,j)=0 for j<0 or j>n. For n≥0 let B_n be the ballot complex consisting of subsets of [n] (label 1 is a ghost label, not a vertex): a set {s_1<…<s_j} is a face if s_i≥2i for every i. It is downward closed. The usual reflection principle gives

f_{j−1}(B_n)=binom(n,j)−binom(n,j−1), 0≤j≤floor(n/2),

and no faces of larger size. In particular B_m⊆B_n whenever m≤n, using the natural inclusions of ground sets. Take B_0=B_1={∅}.

Case 1: the positive initial difference vector is precisely f(B_d).

Case 2: since h(t)=(1+t)^d+t(1+t)^(d−1), its initial differences are

g_j=[binom(d,j)−binom(d,j−1)]+[binom(d−1,j−1)−binom(d−1,j−2)].

Let v be a new vertex and take Δ=B_d ∪ (v*B_{d−1}), where v*B_{d−1} denotes its cone. The intersection is B_{d−1}, so faces not containing v are those of B_d, and faces containing v are v joined to a face of B_{d−1}. This gives the displayed g_j exactly. The first peak of h is ceil(d/2), matching the largest face size of Δ. For odd d the first bracket is zero at j=(d+1)/2; for even d that terminal extra index is absent.

Case 3: h(t)=(1+t)^d+t(1+t)^(d−2). The same construction with Δ=B_d ∪ (v*B_{d−2}) has face numbers

g_j=[binom(d,j)−binom(d,j−1)]+[binom(d−2,j−1)−binom(d−2,j−2)].

The first peak is floor(d/2), and these are exactly all positive initial differences. A shorter prefix is obtained by taking the corresponding skeleton.

## Scope

This proves every dimension simultaneously under a precise arithmetic trace condition, including the irrational-root family in case 3. It is not a resolution of the unrestricted problem. The classification and ballot-complex ingredients are classical, and whether this combination has been recorded for Question 4.4 has not been established.


Classical small-trace background: C. J. Smyth, “Totally positive algebraic integers of small trace,” Annales de l'institut Fourier 34(3) (1984), 1–28, https://numdam.org/item/AIF_1984__34_3_1_0/ . In particular, small-trace classification is established prior art. No novelty is asserted for the classification or for this assembled corollary.
