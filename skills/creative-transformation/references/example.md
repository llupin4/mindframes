# Worked example — Operators with contradiction hand-off

**User query:** "Our CI pipeline runs the full test suite on every commit. Feedback takes
40 minutes and developers have started batching commits to avoid it. Improve this."

**Mode:** Transformation operators first; a contradiction surfaces mid-way and hands off
to contradiction resolution.

---

**Artifact:** A CI pipeline that runs the complete test suite (unit + integration + e2e)
on every commit to any branch, with a 40-minute feedback loop.

**Replace —** Swap the monolithic test runner for a test-impact-analysis runner that maps
changed files to affected tests. Could also replace e2e browser tests with contract tests
at service boundaries.

**Merge —** Combine lint, typecheck, and unit tests into one parallel stage instead of
three sequential ones. Merge duplicate fixture setup across integration suites.

**Borrow —** Borrow "merge queue" semantics from large monorepo shops: full suite runs
once per merge-batch, not per commit.

**Rescale —** What's the minimum viable check per commit? Probably lint + typecheck +
unit tests for changed modules — likely under 5 minutes. Full suite at 10x frequency is
the current pain; full suite at 0.1x frequency (nightly + pre-merge) may suffice.

**Repurpose —** The test-timing data CI already collects could drive test selection —
slowest 5% of tests gate merges only, not commits.

**Remove —** Remove e2e tests from the per-commit path entirely. Remove the requirement
that feature-branch commits run integration tests at all.

**Invert —** Invert the default: instead of "run everything unless excluded," run nothing
but impacted tests unless a label requests the full suite.

**Flagged as promising:** Rescale, Remove, and Invert — all three converge on tiering the
pipeline by risk rather than running everything always.

**Contradiction surfaced:** Improving feedback speed (X) degrades regression coverage per
commit (Y). Developers get fast feedback, but a broken interaction between modules could
now land unnoticed until the full suite runs. Handing off to contradiction resolution.

**Resolution candidates:**

1. **Segmentation** — Split the suite into commit-tier (fast, impacted-only),
   merge-tier (integration on the merge queue), and nightly-tier (full e2e). Each tier
   is independently fast; coverage is preserved across tiers rather than per commit.
2. **Prior action** — Pre-build and cache the test environment and fixtures so the
   merge-tier's integration run costs minutes, not tens of minutes.
3. **Partial or excessive action** — Run slightly *less* than full coverage per commit
   (impacted tests only) and compensate with slightly *more* than needed at merge time
   (impacted tests + their transitive dependents).

**Evaluation:** Segmentation preserves both parameters best — commit feedback drops to
~5 minutes while total coverage per merged change is unchanged, just relocated. Prior
action compounds it. Recommend Segmentation + Prior action; Partial/excessive action is
the fallback if test-impact mapping proves unreliable.

---

Note the shape: the artifact is stated in one sentence before any operator runs; all 7
operators are visited even though only 3 are flagged; the contradiction is stated in
"improving X degrades Y" form before any resolution is proposed; each resolution names
its inventive principle; and every developed idea is a concrete action.
