---
name: mindframes
description: >
  Router for structured thinking frameworks. Use when a task would benefit from a cognitive
  framework but it's unclear which one — the problem is ambiguous, spans multiple intents
  (e.g., both diagnosing and deciding), or the user asks generically to "think through this
  systematically", "use a thinking framework", or "approach this rigorously" without naming
  one. If the task clearly matches a single sub-skill (structured-evaluation,
  creative-transformation, investigative-reasoning, divergent-convergent), prefer invoking
  that sub-skill directly instead of this router.
---

# Mindframes - A Cognitive Toolkit

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

### Step 2: Quick route

If no explicit request, classify the user's **intent** — one of four verbs — and route.
Intent alone decides the destination; there is no case this table does not cover.

| The user wants to... | Intent | Route to |
|----------------------|--------|----------|
| Assess, compare, decide, review, judge | EVALUATE | `structured-evaluation` |
| Understand why, debug, trace a cause, bridge state A → B | INVESTIGATE | `investigative-reasoning` |
| Improve, redesign, or generate variations of something that **exists** | GENERATE (artifact) | `creative-transformation` |
| Create ideas from scratch, nothing exists yet | GENERATE (greenfield) | `divergent-convergent` |
| Map a broad space before committing — or you can't classify the intent | EXPLORE / unclear | `divergent-convergent` |

Classification examples:

- "Should we move ingestion to Kafka or stay on Redis Streams?" → EVALUATE → `structured-evaluation`
- "Latency doubled after Tuesday's deploy but no code touched the hot path" → INVESTIGATE → `investigative-reasoning`
- "Make this onboarding flow less painful" → GENERATE (artifact) → `creative-transformation`
- "We need concepts for the Q3 hackathon" → GENERATE (greenfield) → `divergent-convergent`
- "I don't even know what our options are for agent memory" → EXPLORE → `divergent-convergent`
- "Compare three vendors we haven't used yet" → EVALUATE (evaluation doesn't require an
  existing artifact) → `structured-evaluation`

### Step 3: Apply modifiers (optional)

Two secondary properties modulate **how** the routed skill runs — they never change
**where** you route:

- **Constraint level** (well-defined vs. ambiguous): EVALUATE + ambiguous → extend the
  Evidence frame; EXPLORE + ambiguous → after Cycle 1 converges, route again.
- **Artifact presence**: INVESTIGATE + greenfield → lean Socratic-heavy before going
  abductive.

### Step 4: Trace, announce, execute

Before executing, emit exactly one trace line so the routing decision is auditable:

```
[mindframes: INTENT → skill-name]
```

Example: `[mindframes: INVESTIGATE → investigative-reasoning]`

Then tell the user which framework you're applying and why (one sentence), invoke the
sub-skill, and execute it. Don't over-explain the methodology — just use it.

### How to invoke a sub-skill

Never execute a framework from memory of its name alone — always load its instructions:

1. If a skill-invocation tool is available (e.g., the Skill tool in Claude Code), invoke
   the sub-skill by name.
2. Otherwise, read the sub-skill file directly — `skills/<skill-name>/SKILL.md`, a sibling
   of this skill's directory — and follow its instructions.

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
