# Mindframes

Structured thinking frameworks for AI agents, based on established research in cognitive
psychology, philosophy, and engineering creativity.

A meta-routing skill (`mindframes`) classifies problems and selects the right
thinking framework automatically. Four specialized sub-skills can also be invoked directly.

## Skills

| Skill | Frameworks | Use when |
|-------|-----------|----------|
| `mindframes` | Meta-router | You want the agent to pick the right framework |
| `structured-evaluation` | Multi-frame review + dialectical synthesis | Evaluating, comparing, deciding |
| `creative-transformation` | Transformation operators + contradiction resolution | Improving or redesigning existing artifacts |
| `investigative-reasoning` | Abductive reasoning + Socratic inquiry | Root cause analysis, debugging, migration planning |
| `divergent-convergent` | Divergent/convergent cycling + two-cycle exploration | Open-ended exploration, brainstorming |

## Installation

### Claude Code (recommended)

Register as a plugin marketplace:

```bash
# From Claude Code
/plugin install mindframes@llupin4/mindframes
```

Or add the repo as an additional directory:

```bash
claude --add-dir /path/to/mindframes
```

Skills in `skills/` are discovered automatically.

### Manual install (any agent)

Copy individual skill folders into your agent's skills directory:

```bash
# Claude Code — personal (available in all projects)
cp -r skills/mindframes ~/.claude/skills/mindframes

# Claude Code — project-scoped
cp -r skills/mindframes .claude/skills/mindframes

# OpenAI Codex CLI
cp -r skills/mindframes ~/.codex/skills/mindframes
```

Install just the sub-skills you want, or install everything. The meta-router
(`mindframes`) invokes the sub-skills by name, so install it alongside
whichever sub-skills you plan to use.

### Claude.ai / API

Upload skill folders via the Skills API. See
[Skills API Quickstart](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview).

## Usage

### Let the router pick

> "Help me think through whether we should migrate from REST to GraphQL"

The `mindframes` skill triggers, classifies this as an EVALUATE + WELL-DEFINED +
HAS ARTIFACT problem, and routes to `structured-evaluation`.

### Invoke directly

> "/structured-evaluation Compare our three caching strategies"

> "/investigative-reasoning Why did latency spike after last week's deploy?"

> "/creative-transformation Redesign our notification system"

> "/divergent-convergent We need a new approach to onboarding — I don't know where to start"

## Structure

```
mindframes/
├── README.md
├── LICENSE
├── CLAUDE.md
└── skills/
    ├── mindframes/              # Meta-router
    │   └── SKILL.md
    ├── structured-evaluation/   # Standalone sub-skill
    │   └── SKILL.md
    ├── creative-transformation/ # Standalone sub-skill
    │   └── SKILL.md
    ├── investigative-reasoning/ # Standalone sub-skill
    │   └── SKILL.md
    └── divergent-convergent/    # Standalone sub-skill
        └── SKILL.md
```

Each sub-skill is self-contained and works independently. The meta-router invokes them
by name — install it alongside whichever sub-skills you plan to use.

## Background

These skills are original workflows inspired by established reasoning, design, and
creativity literature, including divergent/convergent thinking, abductive inference,
dialectical analysis, contradiction-resolution patterns, and question-led inquiry.

The two-cycle exploration pattern in `divergent-convergent` is informed in part by the
Design Council's Double Diamond, available under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

See also: [Cognitive Prompting in LLMs](https://arxiv.org/pdf/2503.22036) (Kramer, 2025),
[Sketch-of-Thought](https://arxiv.org/pdf/2503.05179) (Aytes et al., 2025),
[AutoTRIZ](https://arxiv.org/html/2403.13002v2) (2024).

## License

Apache 2.0
