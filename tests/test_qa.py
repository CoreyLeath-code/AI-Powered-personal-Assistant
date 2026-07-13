# tests/test_qa.py
from modules import qa


def test_answer_query_with_known_input(monkeypatch):
    monkeypatch.setattr(qa, "query_snowflake", lambda x: "Mocked Snowflake response")
    monkeypatch.setattr(qa, "query_openai", lambda x: "Mocked OpenAI response")

    result = qa.answer_query("What is the revenue?")
    assert "Mocked" in result


def test_answer_query_with_empty_input(monkeypatch):
    monkeypatch.setattr(qa, "query_openai", lambda x: "Please ask something.")

    result = qa.answer_query("")
    assert "Please ask" in result


def test_query_openai_without_api_key(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)

    result = qa.query_openai("What changed?")

    assert "OPENAI_API_KEY" in result


def test_query_snowflake_placeholder():
    result = qa.query_snowflake("portfolio")

    assert "[Snowflake]" in result
