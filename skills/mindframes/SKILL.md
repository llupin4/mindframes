---
name: mindframes
description: >
  Use when the user asks for help with planning, ideation, brainstorming, architecture decisions,
  root cause analysis, evaluating trade-offs, debugging complex problems, strategic thinking, or
  any task that benefits from structured cognitive frameworks. Also trigger when the user explicitly
  requests a thinking framework, mentions "multi-frame review", "transformation operators",
  "contradiction resolution", "Socratic", "dialectical", "abductive reasoning", or asks to
  "think through" a problem systematically.
---

# Cognitive Toolkit

A meta-skill that selects and applies the right structured thinking framework for a given
problem. It contains four sub-skills, each encoding a distinct cognitive strategy drawn from
established psychological, philosophical, and engineering research.

## Sub-skills

| Sub-skill | Framework(s) | Skill name |
|-----------|-------------|------------|
| Structured Evaluation | Multi-frame review + dialectical synthesis | `structured-evaluation` |
| Creative Transformation | Transformation operators + contradiction resolution | `creative-transformation` |
| Investigative Reasoning | Abductive reasoning + Socratic inquiry | `investigative-reasoning` |
| Divergent-Convergent Cycling | Divergent/convergent cycling + two-cycle exploration | `divergent-convergent` |

## Routing logic

When the user invokes this skill (or when it triggers automatically), classify the problem
before doing anything else. Follow this decision process:

### Step 1: Check for explicit sub-skill request

If the user names a specific framework or sub-skill, skip classification and invoke that
skill directly. Examples:

- "Run a multi-frame review on this" → invoke `structured-evaluation`
- "Transform this design" → invoke `creative-transformation`
- "Help me figure out why X broke" → invoke `investigative-reasoning`
- "Brainstorm as many ideas as possible" → invoke `divergent-convergent`

### Step 2: Classify along three axes

If no explicit request, read the user's query and classify it along these axes:

**Axis 1 — Intent**
- EVALUATE: The user has something and wants to assess, compare, or decide about it
- GENERATE: The user wants new ideas, alternatives, or creative solutions
- INVESTIGATE: The user wants to understand why something is the way it is, or how to
  get from state A to state B
- EXPLORE: The user has a broad space and wants to map it before committing

**Axis 2 — Constraint level**
- WELL-DEFINED: Clear inputs, known options, specific trade-offs
- AMBIGUOUS: Fuzzy requirements, unknown solution space, open-ended

**Axis 3 — Artifact presence**
- HAS ARTIFACT: There's an existing thing (design, system, code, process) to work with
- GREENFIELD: Starting from scratch or near-scratch

### Step 3: Route using the classification

| Intent | Constraint | Artifact | Route to |
|--------|-----------|----------|----------|
| EVALUATE | WELL-DEFINED | HAS ARTIFACT | Structured Evaluation |
| EVALUATE | AMBIGUOUS | either | Structured Evaluation (extended Evidence frame) |
| GENERATE | either | HAS ARTIFACT | Creative Transformation |
| GENERATE | either | GREENFIELD | Divergent-Convergent Cycling |
| INVESTIGATE | either | HAS ARTIFACT | Investigative Reasoning |
| INVESTIGATE | either | GREENFIELD | Investigative Reasoning (Socratic-heavy) |
| EXPLORE | WELL-DEFINED | either | Divergent-Convergent Cycling |
| EXPLORE | AMBIGUOUS | either | Divergent-Convergent Cycling → then route again |

When the classification is ambiguous or the problem spans multiple intents, default to
Divergent-Convergent Cycling as the initial pass — it naturally feeds into the other sub-skills
once the problem space is clearer.

### Step 4: Announce and execute

Briefly tell the user which framework you're applying and why (one sentence), then invoke the
appropriate sub-skill and execute the framework. Don't over-explain the methodology —
just use it.

If during execution it becomes clear that a different sub-skill would serve better (e.g., you
started with Creative Transformation but the real problem is a contradiction that needs
Investigative Reasoning), say so and pivot. The frameworks are tools, not commitments.

## Combining sub-skills

Complex problems often benefit from multiple frameworks in sequence. Common compositions:

- **Investigate then Evaluate**: Root-cause a problem, then evaluate potential fixes
  using structured evaluation
- **Diverge then Transform**: Generate a broad solution space, then apply transformation
  operators and contradiction resolution to the most promising candidates
- **Evaluate then Generate**: Use multi-frame review to identify gaps, then use creative
  transformation to fill them
- **Socratic then Dialectical**: Question assumptions first, then formally argue
  thesis/antithesis on the refined problem

When composing, treat each sub-skill as a phase with a clear handoff. The output of one
phase becomes the input context for the next.

## General principles

- Every framework starts with fact-gathering. Don't skip this even when the user seems
  eager to jump to solutions.
- Explicitly separate divergent phases (generating options) from convergent phases
  (narrowing down). Never do both at once — it kills creativity.
- The Pulse frame / gut-check equivalent in any framework should be kept brief and instinctive.
  If the model is writing paragraphs of "intuition", it's rationalizing, not intuiting.
- When the user's problem is simple enough that a framework adds overhead without value,
  just say so and answer directly. Not everything needs structured thinking.
