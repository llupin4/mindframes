# Cognitive Toolkit

This repository contains structured thinking skills for AI agents. Skills are in `skills/`.

When this repo is added via `--add-dir`, skills are auto-discovered from `skills/`.

The `mindframes` skill is the meta-router — it classifies problems and routes to
the appropriate sub-skill. Sub-skills can also be invoked directly by name.

## Quick reference

- Evaluating / deciding → `structured-evaluation`
- Improving / redesigning → `creative-transformation`
- Debugging / root cause → `investigative-reasoning`
- Exploring / brainstorming → `divergent-convergent`
- Not sure → `mindframes` (routes automatically)
