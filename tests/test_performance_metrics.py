# tests/test_performance_metrics.py
import time

from assistant.main import process_user_input


def test_response_latency(monkeypatch):
    """Verify process_user_input responds quickly (no live API calls)."""
    monkeypatch.setattr("assistant.main.answer_query", lambda x: "Paris is the capital of France.")
    input_text = "What is the capital of France?"
    start = time.time()
    result = process_user_input(input_text)
    elapsed = time.time() - start
    assert elapsed < 1, f"Response took too long: {elapsed:.2f}s"
    assert result == "Paris is the capital of France."
