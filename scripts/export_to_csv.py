"""Export recorded assistant session logs to CSV."""

import csv
import json
from pathlib import Path

INPUT_FILE = Path("logs/session_log.json")
OUTPUT_FILE = Path("logs/performance_metrics.csv")
FIELDNAMES = ["timestamp", "input", "output", "latency"]


def export_to_csv(input_file: Path = INPUT_FILE, output_file: Path = OUTPUT_FILE) -> int:
    """Export JSON session logs to CSV and return the number of records written."""
    with input_file.open("r", encoding="utf-8") as infile:
        data = json.load(infile)

    output_file.parent.mkdir(parents=True, exist_ok=True)
    with output_file.open("w", newline="", encoding="utf-8") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(data)

    return len(data)


def main() -> None:
    """CLI entry point."""
    exported_count = export_to_csv()
    print(f"Exported {exported_count} records to {OUTPUT_FILE}")


if __name__ == "__main__":  # pragma: no cover
    main()
