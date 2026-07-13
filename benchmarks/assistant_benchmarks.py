"""Deterministic benchmark harness for the assistant core."""

from __future__ import annotations

import argparse
import json
import logging
import statistics
import sys
import time
from collections.abc import Callable
from datetime import UTC, datetime
from pathlib import Path
from tempfile import TemporaryDirectory

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from agents.supervisor import AssistantSupervisor, default_config
from assistant import main as assistant_main


def measure_latency(function: Callable[[], object], iterations: int) -> dict:
    """Measure a function and return latency statistics in milliseconds."""
    durations: list[float] = []
    for _ in range(iterations):
        started = time.perf_counter()
        function()
        durations.append((time.perf_counter() - started) * 1000)

    return {
        "iterations": iterations,
        "mean_ms": round(statistics.mean(durations), 6),
        "median_ms": round(statistics.median(durations), 6),
        "p95_ms": round(sorted(durations)[int(iterations * 0.95) - 1], 6),
        "min_ms": round(min(durations), 6),
        "max_ms": round(max(durations), 6),
    }


def run_benchmarks(iterations: int) -> dict:
    """Run deterministic benchmarks without live network or model calls."""
    logging.getLogger("Assistant_Supervisor").setLevel(logging.CRITICAL)
    original_answer_query = assistant_main.answer_query
    original_query_openai = assistant_main.query_openai
    assistant_main.answer_query = lambda prompt: "Mocked QA answer."
    assistant_main.query_openai = lambda prompt: "Mocked fallback answer."

    try:
        with TemporaryDirectory() as temp_dir:
            supervisor = AssistantSupervisor(default_config(), log_path=Path(temp_dir) / "DailyLog.md")
            results = {
                "metadata": {
                    "generated_at": datetime.now(UTC).isoformat(),
                    "iterations": iterations,
                    "harness": "benchmarks/assistant_benchmarks.py",
                },
                "benchmarks": {
                    "intent_router_qa": measure_latency(
                        lambda: assistant_main.process_user_input("What is the deployment status?"),
                        iterations,
                    ),
                    "intent_router_schedule": measure_latency(
                        lambda: assistant_main.process_user_input("Remind me to review metrics"),
                        iterations,
                    ),
                    "intent_router_fallback": measure_latency(
                        lambda: assistant_main.process_user_input("Summarize my backlog"),
                        iterations,
                    ),
                    "supervisor_memory_route": measure_latency(
                        lambda: supervisor.route_and_execute("Open my portfolio profile"),
                        iterations,
                    ),
                    "supervisor_search_route": measure_latency(
                        lambda: supervisor.route_and_execute("Search latest agent workflows"),
                        iterations,
                    ),
                },
            }
    finally:
        assistant_main.answer_query = original_answer_query
        assistant_main.query_openai = original_query_openai

    return results


def main() -> None:
    """CLI entry point."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--iterations", type=int, default=500)
    parser.add_argument("--output", type=Path, default=Path("benchmark-results.json"))
    args = parser.parse_args()

    if args.iterations < 20:
        raise SystemExit("--iterations must be at least 20 for stable p95 output")

    results = run_benchmarks(args.iterations)
    args.output.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
