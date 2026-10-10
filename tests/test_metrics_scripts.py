import csv
import json

import pytest

from scripts.export_to_csv import export_to_csv
from scripts.generate_metrics_table import (
    format_row,
    load_entries,
    parse_latency_seconds,
    render_metrics_table,
)


@pytest.mark.parametrize(
    ("entry", "expected"),
    [
        ({"input": "", "output": "", "latency": ""}, "|  |  |  |"),
        ({"input": 0, "output": False, "latency": 0}, "| 0 | False | 0 |"),
    ],
)
def test_format_row_formats_empty_and_non_string_values(entry, expected):
    assert format_row(entry) == expected


@pytest.mark.parametrize("missing_key", ["input", "output", "latency"])
def test_format_row_requires_each_session_field(missing_key):
    entry = {"input": "Question", "output": "Answer", "latency": "1.00s"}
    del entry[missing_key]

    with pytest.raises(KeyError, match=missing_key):
        format_row(entry)


def test_parse_latency_seconds():
    assert parse_latency_seconds("1.85s") == 1.85


def test_render_metrics_table_contains_average_latency():
    entries = [
        {"input": "A", "output": "B", "latency": "1.00s"},
        {"input": "C", "output": "D", "latency": "3.00s"},
    ]

    rendered = render_metrics_table(entries)

    assert "Average Latency: 2.00 seconds" in rendered
    assert "| A | B | 1.00s |" in rendered


def test_export_to_csv_writes_rows(tmp_path):
    input_file = tmp_path / "session_log.json"
    output_file = tmp_path / "metrics.csv"
    input_file.write_text(
        json.dumps(
            [
                {
                    "timestamp": "2025-06-17T13:00:10Z",
                    "input": "Question",
                    "output": "Answer",
                    "latency": "1.00s",
                }
            ]
        ),
        encoding="utf-8",
    )

    exported_count = export_to_csv(input_file, output_file)

    with output_file.open("r", encoding="utf-8", newline="") as file:
        rows = list(csv.DictReader(file))
    assert exported_count == 1
    assert rows[0]["input"] == "Question"


def test_load_entries_reads_json(tmp_path):
    input_file = tmp_path / "session_log.json"
    input_file.write_text('[{"input": "A", "output": "B", "latency": "1.00s"}]', encoding="utf-8")

    entries = load_entries(input_file)

    assert entries[0]["output"] == "B"
