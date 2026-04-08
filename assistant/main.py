"""
main.py — Core Assistant Logic
------------------------------
Handles:
- User input parsing
- Context memory
- OpenAI API calls (LLM)
- Command delegation to modules (scheduler, Q&A, etc.)
"""

import os
from openai import OpenAI
from modules.scheduler import handle_schedule
from modules.qa import answer_query

# Simulated memory for context
context_memory = []

SCHEDULE_KEYWORDS = {"schedule", "remind", "meeting", "appointment", "calendar"}
QA_KEYWORDS = {"question", "what", "who", "when", "where", "why", "how", "explain"}


def process_user_input(user_input):
    """
    Routes user input to the appropriate module
    based on keywords or falls back to OpenAI chat model.
    """
    if not user_input or not user_input.strip():
        return "I'm sorry, I didn't understand that."

    context_memory.append(user_input)
    lower = user_input.lower()

    if any(kw in lower for kw in SCHEDULE_KEYWORDS):
        return handle_schedule(user_input)
    elif any(kw in lower for kw in QA_KEYWORDS):
        return answer_query(user_input)
    else:
        return query_openai(user_input)


def query_openai(prompt):
    """
    Sends the prompt to OpenAI's API and returns the response.
    """
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model=os.getenv("LANGUAGE_MODEL", "gpt-3.5-turbo"),
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        response = process_user_input(user_input)
        print("Assistant:", response)
