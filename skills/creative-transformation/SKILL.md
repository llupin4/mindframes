---
name: creative-transformation
description: >
  Apply transformation operators and contradiction-resolution patterns to improve or redesign
  existing artifacts, systems, or processes. Use when the user wants to iterate on something
  that already exists — improving a design, resolving engineering trade-offs, breaking through
  creative blocks, or generating concrete modifications. Trigger on phrases like "improve",
  "redesign", "iterate", "make this better", "what if we changed", "trade-off", "contradiction",
  or when the user has an artifact and wants alternatives.
---

# Creative Transformation

Combines transformation operators (divergent exploration of modifications) with
contradiction-resolution patterns for transforming existing artifacts into improved versions.

**Skip check:** If the user needs one specific fix rather than exploration — a bug, a
known change — just make the fix. Operators are for when the improvement direction is
open.
The contradiction-resolution principles below are inspired by systematic inventive-thinking
traditions, but the wording and software-systems framing here is original.

## Transformation operators

Seven operators. Apply each as a probe against the existing artifact.

**Replace** — What components, materials, or processes can be swapped out?
- What technology could replace the current implementation?
- Could a different data structure serve the same purpose?

**Merge** — What can be combined, integrated, or bundled?
- Can two services be merged? Can two steps happen simultaneously?

**Borrow** — What can be adapted from elsewhere?
- What patterns from other domains solve a similar problem?

**Rescale** — What can be changed in scale, shape, or form?
- What happens at 10x? What's the minimum viable version?

**Repurpose** — What else could this be used for?
- Can this component serve a second purpose?

**Remove** — What can be eliminated entirely?
- What step adds no value? What constraint is assumed but not required?

**Invert** — What can be flipped, reordered, or reversed?
- What if the steps ran in reverse? What if client/server roles swapped?

### Execution

1. State the artifact being transformed (one sentence)
2. Run through each operator, 1-3 sentences per operator
3. Flag which operators produced promising ideas (usually 2-3 of 7)
4. Develop the promising ideas further

Not every operator will yield results — "nothing useful here" is valid.

## Contradiction resolution

Use when the problem involves a **contradiction** — improving one parameter degrades another.

### Identifying contradictions

Form: "We want to improve X, but that worsens Y."
- "Faster response times but more compute cost"
- "More thorough validation but slower pipeline"
- "Higher security but worse user experience"

### Key inventive principles (software/systems focus)

1. **Segmentation** — Divide into independent, modular parts
2. **Extraction** — Separate the problematic part from the whole
3. **Local quality** — Optimize each part for its specific conditions
4. **Asymmetry** — Different paths for different cases
5. **Merging** — Combine identical operations in time or space
6. **Universality** — One part performs multiple functions
7. **Nesting** — Layers, containers, wrappers
8. **Prior action** — Pre-compute, cache, warm up
9. **Prior counteraction** — Prepare countermeasures for expected harm
10. **Dynamicity** — Static config → dynamic config
11. **Partial or excessive action** — Go slightly over/under and compensate
12. **Another dimension** — Single-layer to multi-layer
13. **Intermediary** — Use a proxy or mediator
14. **Self-service** — Self-heal, self-configure
15. **Copying** — Use a simpler copy (mocks, stubs, caches)

### Execution

1. State the contradiction: "Improving [X] degrades [Y]"
2. Select 2-4 applicable inventive principles
3. Describe a concrete application of each to the problem
4. Evaluate which resolution best preserves both parameters

## Combining the two

- **Operators first** when you have an artifact and want broad exploration. If they
  reveal a contradiction, hand off to contradiction resolution.
- **Contradiction resolution first** when the user already knows the contradiction.
  After resolving it, optionally apply the operators to further refine.
- For complex redesigns, alternate: operators → contradiction resolution → operators
  on the refined version.

## Output format

Label which mode is active. For the operators, use operator names as headers.
For contradiction resolution, state the contradiction before proposing resolutions.
Keep sections action-oriented — "do X" not "one could consider X."

For a complete worked example (operators plus a contradiction hand-off), read
`references/example.md`. If unsure of the format, read it before starting.

## Before finishing, verify

1. The artifact being transformed was stated in one sentence before any operator ran.
2. All 7 operators were visited (a "nothing useful here" verdict counts as visited).
3. 2–3 promising operators were flagged and developed further — not all 7, not zero.
4. If contradiction mode ran: the contradiction is stated in "improving X degrades Y"
   form, and each proposed resolution names the inventive principle it applies.
5. Every developed idea is phrased as a concrete action, not a hypothetical.

If any check fails, fix that section before presenting the result.
