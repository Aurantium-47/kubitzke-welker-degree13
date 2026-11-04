# Provenance, review status, and claim boundaries

This is a research artifact prepared on 2026-11-04. The derivations, implementations, packaging, and internal reviews were produced with AI assistance. Two separate AI review processes independently examined the mathematics and recomputed the finite data using independently written implementations. They are not independent human referees, and their agreement is not external peer review.

## Claims made

- The supplied argument and exact finite certificates establish the initial-difference simplicial f-vector assertion of Kubitzke–Welker Question 4.4 for actual degrees 1 through 13, with positive integer coefficients, constant term 1, and real-rootedness.
- Coefficient size is not bounded. A proven monotone inequality covers the entire infinite tail.
- The Newton-only variant holds through degree 11 and has a strict palindromic obstruction in degree 12. That obstruction is not real-rooted.
- The supporting notes include a fixed-degree finite reduction, a sharp continuous envelope, and an all-degree trace-at-most-d+1 subcase using classical ingredients.

## Claims not made

- No resolution of Question 4.4 in unrestricted degree.
- No counterexample to the original real-rooted question.
- No resolution of the separate Bell–Skandera coefficient-vector conjecture.
- No established novelty, publication priority, external endorsement, or human peer review.
- No claim that degree 13 is the maximal reach of the method.
- No formal verification in Lean, Coq, Isabelle, or another proof assistant.

## What was preserved and edited

The six programs in `src/` and six JSON files in `certificates/` preserve the audited source and output bytes. Their original filenames are retained. The optional supplementary script is also preserved.

The mathematical notes were reorganized into `proofs/`. Presentation-only clarifications make the Newton-normalized endpoint argument and degree-one case explicit, give the total enumeration counts, identify the degree-13 program as a multi-file extension, and link the general note to the degree-13 result. No finite filter or certificate was changed.

The review reports were reorganized into `audits/`. An explicit AI-only label was added to each report, and two old run commands were adjusted to the repository layout. Their mathematical verdicts and limitations are preserved. The new README, visual overview, runner, tests, and provenance documents are packaging additions rather than independent mathematical evidence.

The classical small-trace classification, Kronecker theorem, Newton inequalities, and Kruskal–Katona theorem are not claimed as original. See [SOURCES.md](SOURCES.md) for primary-source links and distinctions between nearby problems. Literature checking was targeted, not exhaustive; a priority claim would require further specialist review.

## Data hygiene and external material

The release contains allowlisted text, exact integer data, and an original vector diagram. It contains no private messages, credentials, API output, downloaded papers, third-party code, account identifiers, or machine-specific absolute paths. Published-source links are intentionally retained. No identities or institutional endorsements are assigned to the mathematical work by this package.

No license has been selected. No third-party paper is redistributed, and this repository does not grant rights in the cited works. Publication, authorship choices, licensing, journal submission, and formal priority claims are separate decisions.
