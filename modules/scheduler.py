"""Scheduling module for deterministic reminder/calendar responses."""

import datetime


def handle_schedule(user_input: str) -> str:
    """Return a mock scheduling confirmation for the given request."""
    if not user_input or not user_input.strip():
        return "Sorry, I couldn't understand your scheduling request. Please specify what you'd like to schedule."

    lower = user_input.lower()
    future_time = datetime.datetime.now() + datetime.timedelta(days=1)
    formatted_time = future_time.strftime("%A at %I:%M %p")

    if "meeting" in lower:
        return f"Scheduled a meeting for {formatted_time}."
    if "remind" in lower or "reminder" in lower:
        return f"Scheduled reminder: '{user_input}' noted for {formatted_time}."
    if "appointment" in lower:
        return f"Scheduled an appointment for {formatted_time}."

    return f"Scheduled: '{user_input}' for {formatted_time}."
