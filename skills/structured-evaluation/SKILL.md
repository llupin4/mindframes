---
name: structured-evaluation
description: >
  Run a multi-frame review for systematic evaluation, decision-making, and trade-off analysis.
  Use when the user needs to evaluate a proposal, compare alternatives, review performance,
  plan strategy, or make a decision where evidence, risk, value, and intuition need separate
  treatment. Trigger on phrases like "evaluate", "compare", "should we", "pros and cons",
  "trade-offs", "which option", "review this", "multi-frame review", or "devil's advocate".
  Also use for architecture decisions, tech stack comparisons, and retrospectives.
---

# Structured Evaluation

An original multi-frame review workflow. The reviewer cycles a problem through a small
set of analytical frames — each frame asks only one kind of question — and synthesizes
the results. Keeping the frames separate prevents premature judgment (the most common
failure mode of unstructured evaluation, where critique kills options before they're
fully formed and optimism buries risk before it's named).

This skill is an original implementation. It is not affiliated with or endorsed by any
third-party framework owner.

**Skip check:** If the decision is trivial — one option is obviously dominant, or the
answer fits in a paragraph — say so and answer directly. Do not run frames on questions
that don't need them.

## The frames

Five content frames plus two bookend frames. Each frame produces a short pass — usually
a few sentences. Scope opens the review; Synthesis closes it.

| Frame | Mode | Role |
|-------|------|------|
| Scope | Meta-control | Sets the question, constraints, success criteria, and sequence |
| Evidence | Information | Facts only — what we know, what we don't know, and what needs verification |
| Risk | Downside | Failure modes, hidden costs, stress cases, and second-order consequences |
| Value | Upside | Benefits, leverage, opportunities, and what works in our favor |
| Options | Generative | Alternatives, variations, hybrid approaches, and novel paths — no evaluation yet |
| Pulse | Affect | Brief gut check, stakeholder reaction, or confidence signal. 1-2 sentences max. |
| Synthesis | Decision | Weighs the frames, names the trade-off, recommends a path, and lists open questions |

Three notes on the frames:

- **Scope and Synthesis are not optional.** Every review opens with Scope and closes with
  Synthesis. If you catch yourself skipping Scope, you're answering a question you haven't
  actually defined. If you catch yourself skipping Synthesis, you've produced analysis
  without a recommendation.
- **Pulse is optional and small.** If you're writing a paragraph of "intuition," stop —
  you're rationalizing, not intuiting. A single sentence is the right shape.
- **Options is divergent only.** Generate alternatives without filtering. Evaluation
  belongs in Risk and Value passes, not here.

## Sequences

Pick a sequence by the shape of the question. Three cover most cases. Build your own
by combining frames when none fit.

**Decision** — when choosing between alternatives:
`Scope → Evidence → Risk → Value → Options → Synthesis`

**Critique** — when stress-testing one thing:
`Scope → Risk → Options → Synthesis`

**Retrospective** — when reviewing outcomes:
`Scope → Evidence → Pulse → Risk → Value → Options → Synthesis`

**Lite** — when the question is real but small (a single choice, low stakes, evidence
already in hand):
`Scope → Risk → Value → Synthesis`
Prefer running the Lite sequence well over running a full sequence thinly.

The principle behind sequencing: gather information before judging; keep critical and
optimistic passes adjacent so they balance; generate Options before Synthesis so the
recommendation can land forward, not just backward.

## Dialectical synthesis overlay

For decisions where two positions are in genuine tension (microservices vs. monolith,
build vs. buy, consistency vs. availability), the dialectical pattern maps cleanly onto
the frames:

1. **Thesis** — Value frame: strongest case for position A
2. **Antithesis** — Risk frame: strongest case against A / for position B
3. **Synthesis** — Options frame: a resolution that absorbs the strongest elements
   of both

This overlay reuses the standard frames; it's not a separate workflow. Use it when the
problem genuinely has two strong sides, not when one option is obviously dominant.

## Execution guidelines

- **Scope is explicit but brief.** State the question, the constraints, and the sequence.
- **Evidence is where tool calls happen.** Search, file reading, lookups belong here, not
  in other frames.
- **Risk and Value should be similar in length.** If one is much longer than the other,
  you're tilted.
- **Options aims for quantity.** Five quick alternatives beats two polished ones.
- **Pulse stays small.** One or two sentences. If you can't say it in two sentences, you
  don't have a gut reaction — you have an argument, which belongs in Risk or Value.
- **Synthesis is the only place a recommendation appears.** Name the trade-off, pick a
  path, and list open questions. Don't smuggle conclusions into earlier frames.

## Output format

Fill in this skeleton, omitting frames not in your chosen sequence. Keep each pass to
2–5 sentences (Pulse: 1–2).

```markdown
**Scope —** [the question being decided, constraints, and which sequence you're running]

**Evidence —** [known facts; unknowns; what needs verification. Tool calls happen here.]

**Risk —** [failure modes, hidden costs, stress cases, second-order consequences]

**Value —** [benefits, leverage, opportunities — roughly the same length as Risk]

**Options —** [numbered list, 5+ alternatives, no evaluation]

**Pulse —** [one-sentence gut check]

**Synthesis —** [the trade-off in one sentence; the recommendation; open questions]
```

For a complete worked example, read `references/example.md`. If unsure of the format,
read it before starting.

## Before finishing, verify

1. Scope stated the question and the sequence; Synthesis exists and names a recommendation.
2. No frame before Synthesis contains a recommendation — if one does, move it.
3. Risk and Value are within roughly 2x of each other in length.
4. Options is a numbered list with at least 5 entries and no evaluative language.
5. Pulse (if present) is at most 2 sentences.

If any check fails, fix that frame before presenting the result.
