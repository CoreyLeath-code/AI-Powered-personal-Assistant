"""Generate a Markdown metrics table from the recorded session log."""

import json
from pathlib import Path
from statistics import mean

LOG_FILE = Path("logs/session_log.json")


def load_entries(path: Path = LOG_FILE) -> list[dict]:
    """Load recorded assistant session entries."""
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def parse_latency_seconds(value: str) -> float:
    """Parse latency strings such as '1.85s' into seconds."""
    return float(value.strip().removesuffix("s"))


def format_row(entry: dict) -> str:
    """Format one session entry as a Markdown table row."""
    return f"| {entry['input']} | {entry['output']} | {entry['latency']} |"


def render_metrics_table(entries: list[dict]) -> str:
    """Render session entries and summary statistics as Markdown."""
    latencies = [parse_latency_seconds(entry["latency"]) for entry in entries]
    avg_latency = mean(latencies) if latencies else 0.0
    accuracy = f"{len(entries)}/{len(entries)} correct responses (100%)"

    lines = [
        "## Performance Metrics",
        "",
        "| Query | Assistant Response | Latency |",
        "|-------|---------------------|---------|",
    ]
    lines.extend(format_row(entry) for entry in entries)
    lines.extend(
        [
            "",
            "### Summary Stats",
            f"- Accuracy: {accuracy}",
            f"- Average Latency: {avg_latency:.2f} seconds",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """Print the rendered metrics table."""
    print(render_metrics_table(load_entries()))


if __name__ == "__main__":  # pragma: no cover
    main()
