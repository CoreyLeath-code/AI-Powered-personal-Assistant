"""Question-answering module with optional Snowflake/OpenAI integrations."""

import os

USE_SNOWFLAKE = os.getenv("USE_SNOWFLAKE", "false").lower() == "true"


def answer_query(query: str) -> str:
    """Route the query to Snowflake Q&A logic or OpenAI fallback."""
    if USE_SNOWFLAKE:
        return query_snowflake(query)

    return query_openai(query)


def query_snowflake(query: str) -> str:
    """Placeholder for Snowflake-backed semantic retrieval."""
    return f"[Snowflake]: Answer to '{query}' would be retrieved from a knowledge base."


def query_openai(prompt: str) -> str:
    """Use OpenAI as a fallback when credentials are configured."""
    if not prompt or not prompt.strip():
        return "Please ask something."

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "OpenAI API key is not configured. Please set OPENAI_API_KEY to enable live answers."

    from openai import OpenAI  # pragma: no cover

    client = OpenAI(api_key=api_key)  # pragma: no cover
    response = client.chat.completions.create(
        model=os.getenv("LANGUAGE_MODEL", "gpt-3.5-turbo"),
        messages=[{"role": "user", "content": prompt}],
    )  # pragma: no cover
    return response.choices[0].message.content  # pragma: no cover
