#!/usr/bin/env python3
"""Routing accuracy eval for the mindframes router.

Sends each labeled query to an OpenAI-compatible chat endpoint (llama.cpp
server, Ollama, vLLM, LM Studio, etc.) with the router SKILL.md as context,
extracts the `[mindframes: INTENT -> skill-name]` trace line, and scores it
against the labeled expectation.

Stdlib only — no pip installs required.

Examples:
    # llama.cpp server on default port
    python run_routing_eval.py --model qwen3.5-coder-27b

    # Ollama
    python run_routing_eval.py --endpoint http://localhost:11434/v1 \
        --model qwen3.5-coder:27b --runs 3

What this measures: the router prompt's classification accuracy on the
target model, in isolation. It does NOT measure whether the skill *triggers*
inside a real agent session — that depends on the harness's skill-selection
behavior. Use this to regression-test description/routing-logic changes.
"""

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path

TRACE_RE = re.compile(
    r"\[\s*mindframes\s*:\s*(?P<intent>[^\]\u2192>-]+?)\s*(?:\u2192|->)\s*(?P<skill>[a-z][a-z0-9-]*)\s*\]",
    re.IGNORECASE,
)

VALID_SKILLS = {
    "structured-evaluation",
    "creative-transformation",
    "investigative-reasoning",
    "divergent-convergent",
}

HARNESS_INSTRUCTION = """\
You are testing the routing logic of a cognitive-framework router. The full
routing instructions follow below. For the user's query, perform ONLY the
classification and routing steps. Do NOT execute any framework.

Output exactly one line — the trace line — in this format and nothing else:

[mindframes: INTENT -> skill-name]

where skill-name is one of: structured-evaluation, creative-transformation,
investigative-reasoning, divergent-convergent.

--- ROUTING INSTRUCTIONS ---
"""


def chat(endpoint, model, system, user, temperature, timeout, api_key=None):
    body = json.dumps(
        {
            "model": model,
            "temperature": temperature,
            "max_tokens": 200,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
        }
    ).encode("utf-8")
    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    req = urllib.request.Request(
        endpoint.rstrip("/") + "/chat/completions", data=body, headers=headers
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    return data["choices"][0]["message"]["content"]


def extract_route(text):
    """Return (skill, intent) from the last trace line found, or (None, None)."""
    matches = list(TRACE_RE.finditer(text))
    if not matches:
        return None, None
    m = matches[-1]
    skill = m.group("skill").strip().lower()
    return (skill if skill in VALID_SKILLS else None), m.group("intent").strip()


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--endpoint", default="http://localhost:8080/v1", help="OpenAI-compatible base URL (default: llama.cpp server)")
    p.add_argument("--model", required=True, help="Model name as the server knows it")
    p.add_argument("--eval-set", default=str(Path(__file__).parent / "routing-eval.json"))
    p.add_argument("--router", default=str(Path(__file__).parent.parent / "skills" / "mindframes" / "SKILL.md"))
    p.add_argument("--runs", type=int, default=1, help="Runs per query (use 3+ at temp>0 for trigger-rate)")
    p.add_argument("--temperature", type=float, default=0.0)
    p.add_argument("--timeout", type=int, default=120)
    p.add_argument("--api-key", default=None)
    p.add_argument("--out", default=None, help="Write full results JSON here")
    args = p.parse_args()

    router_md = Path(args.router).read_text(encoding="utf-8")
    system = HARNESS_INSTRUCTION + router_md
    eval_set = json.loads(Path(args.eval_set).read_text(encoding="utf-8"))
    cases = eval_set["cases"]

    results = []
    correct_total = 0
    run_total = 0
    per_label = defaultdict(lambda: [0, 0])  # label -> [correct, total]
    confusion = Counter()  # (expected_primary, got) -> count
    parse_failures = 0

    for case in cases:
        expected = set(case["expected"])
        primary = case["expected"][0]
        label = primary if len(expected) == 1 else "ambiguous"
        case_runs = []
        for i in range(args.runs):
            try:
                raw = chat(args.endpoint, args.model, system, case["query"],
                           args.temperature, args.timeout, args.api_key)
            except (urllib.error.URLError, TimeoutError, KeyError) as e:
                print(f"  !! {case['id']} run {i+1}: request failed: {e}", file=sys.stderr)
                case_runs.append({"raw": None, "skill": None, "ok": False})
                run_total += 1
                per_label[label][1] += 1
                continue
            skill, intent = extract_route(raw)
            if skill is None:
                parse_failures += 1
            ok = skill in expected
            case_runs.append({"raw": raw.strip(), "skill": skill, "intent": intent, "ok": ok})
            run_total += 1
            per_label[label][1] += 1
            if ok:
                correct_total += 1
                per_label[label][0] += 1
            else:
                confusion[(primary, skill or "NO-TRACE")] += 1
        rate = sum(r["ok"] for r in case_runs) / len(case_runs)
        mark = "PASS" if rate == 1.0 else ("part" if rate > 0 else "FAIL")
        got = ",".join(sorted({str(r["skill"]) for r in case_runs}))
        print(f"[{mark}] {case['id']:6s} expected={'|'.join(sorted(expected)):45s} got={got}")
        results.append({"id": case["id"], "query": case["query"], "expected": case["expected"],
                        "trigger_rate": rate, "runs": case_runs})

    print("\n=== Summary ===")
    print(f"Overall routing accuracy: {correct_total}/{run_total} = {correct_total/run_total:.1%}")
    print(f"Trace-line parse failures: {parse_failures}/{run_total}")
    print("\nPer category:")
    for label in sorted(per_label):
        c, t = per_label[label]
        print(f"  {label:25s} {c}/{t} = {c/t:.1%}")
    if confusion:
        print("\nMisroutes (expected -> got):")
        for (exp, got), n in confusion.most_common():
            print(f"  {exp:25s} -> {got:25s} x{n}")

    out_path = args.out or f"routing-results-{time.strftime('%Y%m%d-%H%M%S')}.json"
    Path(out_path).write_text(json.dumps({
        "model": args.model, "endpoint": args.endpoint, "runs_per_query": args.runs,
        "temperature": args.temperature,
        "overall_accuracy": correct_total / run_total if run_total else 0.0,
        "parse_failures": parse_failures, "results": results,
    }, indent=2), encoding="utf-8")
    print(f"\nFull results written to {out_path}")


if __name__ == "__main__":
    main()
