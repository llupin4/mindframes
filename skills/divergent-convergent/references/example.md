# Worked example — Two-cycle exploration

**User query:** "Leadership gave us a mandate to 'improve developer experience' this
quarter. I don't even know where to start."

**Mode:** Two-cycle exploration — find the right problem, then the right solution.

---

## Cycle 1: Find the right problem

**Diverging (Discover):**

1. Survey data shows the top complaint is CI wait time, but the survey had 20% response.
2. Onboarding takes new hires ~3 weeks to first merged PR.
3. Local dev environment setup is a 40-step wiki page, frequently stale.
4. Internal tooling has no owner; bugs sit unfixed for months.
5. Senior engineers report meeting load, not tooling, as their main drag.
6. Platform team sees ticket volume dominated by environment/setup issues.

**Converging (Define):** Items 2, 3, and 6 triangulate: the environment story appears in
onboarding time, in the stale wiki, and in the ticket queue — three independent signals.
CI wait time (1) is loud but single-source; meeting load (5) is real but outside a
tooling mandate.

**Problem statement:** The core challenge is **unreliable, manual dev-environment
setup**, because **there is no reproducible environment definition**, which matters
because **it delays onboarding by weeks and generates the platform team's largest
ticket category**.

Confirm with the user: is this the right problem before Cycle 2?

## Cycle 2: Find the right solution

**Diverging (Develop):**

1. Devcontainers/Nix-style declarative environment checked into each repo — optimizes
   reproducibility; sacrifices initial migration effort.
2. Cloud development environments (ephemeral, pre-baked) — optimizes onboarding speed;
   sacrifices cost and offline work.
3. A maintained setup CLI that automates the wiki's 40 steps — optimizes low migration
   cost; sacrifices the root cause (steps still exist, now hidden).
4. Golden VM/container image refreshed weekly by CI — optimizes consistency; sacrifices
   flexibility for teams with unusual stacks.
5. **Counterintuitive:** delete the wiki page and make setup failures page the platform
   team — optimizes forcing-function pressure; sacrifices short-term goodwill.
6. Embed a platform engineer in each team for a quarter — optimizes context transfer;
   sacrifices platform team capacity.

**Converging (Deliver):** Criteria: fixes the root cause (no manual steps), works within
one quarter, and reduces platform ticket load. Option 1 scores highest on root cause but
whole-org migration exceeds a quarter; option 2 is strong but introduces new cost and
procurement risk; option 3 fails the root-cause criterion; options 5 and 6 are
pressure/context plays, not fixes.

**Decision:** Option 1, scoped to the three highest-traffic repos this quarter, with
option 3's CLI as a thin bootstrap for everything not yet migrated. **Why:** attacks the
root cause where it hurts most while staying inside the time box. **Next:** pick the
three repos by ticket volume, define the environment spec for the worst one first, and
re-run the ticket-volume measurement at quarter end.

Handoff note: choosing *between* devcontainers and Nix for the spec format is now a
well-defined evaluation → `structured-evaluation`.

---

Note the shape: phases are labeled and never mixed — no "however" appears inside a
divergent list; Cycle 1 converged on a problem *underneath* the stated one and produced
the X/Y/Z problem statement; Cycle 2's list has 6 options including one counterintuitive
entry, each with an optimizes/sacrifices note; convergence stated its criteria before
ranking; and the residual decision was handed off to the right specialized skill.
