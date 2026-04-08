"""
scheduler.py — Scheduling Module
--------------------------------
Handles scheduling commands and mock calendar updates.
Integrates with external calendar APIs in a real-world setup.
"""

import datetime


def handle_schedule(user_input):
    """
    Extracts date/time from input and returns a mock confirmation.
    In production, would use NLP parsing + Google Calendar API integration.
    """
    if not user_input or not user_input.strip():
        return "Sorry, I couldn't understand your scheduling request. Please specify what you'd like to schedule."

    lower = user_input.lower()
    time_now = datetime.datetime.now()
    future_time = time_now + datetime.timedelta(days=1)

    if "meeting" in lower:
        return f"📅 Scheduled a meeting for {future_time.strftime('%A at %I:%M %p')}."
    elif "remind" in lower or "reminder" in lower:
        return f"📅 Scheduled reminder: '{user_input}' noted for {future_time.strftime('%A at %I:%M %p')}."
    elif "appointment" in lower:
        return f"📅 Scheduled an appointment for {future_time.strftime('%A at %I:%M %p')}."
    else:
        return f"📅 Scheduled: '{user_input}' for {future_time.strftime('%A at %I:%M %p')}."
