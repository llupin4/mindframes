---
name: investigative-reasoning
description: >
  Apply Abductive Reasoning and Socratic Method for diagnostic, investigative, and root-cause
  work. Use when the user needs to figure out why something happened, how to get from one state
  to another, debug a complex system, uncover hidden assumptions, or trace a causal chain.
  Trigger on phrases like "why did", "root cause", "what happened", "how did we get here",
  "figure out", "debug", "investigate", "diagnose", "migrate from X to Y", "what changed",
  "what went wrong", or "help me understand why". Also use for incident triage, post-mortems,
  and migration planning.
---

# Investigative Reasoning

Combines Abductive Reasoning (state-bridging inference) with the Socratic Method
(progressive questioning) for diagnostic and investigative work.

## Abductive Reasoning

Inference to the best explanation. Given an observed outcome, work backward to the most
plausible cause. Given two states, infer the most plausible path between them.

Distinct from deduction (rules → effect, certain) and induction (observations → rule,
probable). Abduction: effect → most plausible cause (explanatory, pragmatic).

### State-bridging mode

When the user has two states and needs the path between them.

1. **Define State A** (current/starting) — be precise
2. **Define State B** (target/observed) — be precise
3. **Identify the delta** — what specifically differs?
4. **Generate candidate paths** — what sequences of events could produce the delta?
   Generate at least 3 candidates.
5. **Apply constraints** — which candidates are consistent with known facts and system
   rules? Eliminate impossible paths.
6. **Rank by plausibility** — which requires fewest unsupported assumptions?
7. **Identify verification steps** — what can be checked to confirm or eliminate candidates?

### Diagnostic mode

When something unexpected happened and the user wants to know why.

1. **State the observation** — what was seen?
2. **State the expectation** — what was expected instead?
3. **Identify the gap** — observation minus expectation = the anomaly
4. **Generate hypotheses** broadly:
   - Proximate causes (immediate trigger)
   - Systemic causes (underlying condition)
   - Environmental causes (external factors)
5. **Test against evidence** — what existing evidence supports or contradicts each?
6. **Rank and recommend** — most plausible first, with verification steps

### Ontological grounding

Explicitly define entity types and valid relationships to constrain abductive leaps.

Example for system debugging:
- Entities: services, databases, queues, config files, deployments, network routes
- Valid relationships: depends-on, writes-to, reads-from, triggered-by, deployed-after
- Invalid leaps: "the database config changed the network route" (no valid relationship)

State these constraints when the domain is technical. This prevents plausible-sounding
but structurally impossible explanations.

## Socratic Method

Progressive questioning that exposes assumptions and surfaces contradictions.

### Question types (use roughly in this order)

1. **Clarifying** — "What do you mean by X?" / "Can you give an example?"
2. **Probing assumptions** — "What are we taking for granted?"
3. **Probing evidence** — "What evidence supports this?" / "How do we know?"
4. **Exploring alternatives** — "What's another way to look at this?"
5. **Testing implications** — "If that's true, what follows?"
6. **Meta-questions** — "Why does this question matter?"

### Execution

- **Single-turn** (user wants an answer): Use the questions internally as reasoning
  scaffold. Ask and answer them yourself, surfacing key findings.
- **Multi-turn** (user is exploring): Ask 1-2 questions per turn, building progressively.

The goal is clarity, not endless questioning. When a line of inquiry is sufficiently
explored, say so and move on.

## Combining the frameworks

The natural sequence:

1. **Socratic first** — Clarifying and assumption-probing questions to ensure the problem
   is well-defined. The user's initial framing often obscures the real issue.
2. **Abductive second** — Once clear, apply state-bridging or diagnostic reasoning.
3. **Socratic validation** — Test the abductive result: "If this hypothesis is correct,
   what else should we observe?"

For incident triage specifically:
- Socratic: "What changed?" / "What's the blast radius?" / "When did it start?"
- Abductive: State A (healthy) → State B (degraded), bridge the gap
- Socratic: "If it's the deployment, would we see this in the other region too?"

## Output format

For abductive reasoning: label State A, State B, candidate paths, and ranked result.
For Socratic method: present key questions and answers (or flag as open).
Don't label question types — that's internal scaffolding.
