# tests/test_scheduler.py
from modules import scheduler


def test_handle_schedule_with_valid_input():
    user_input = "Remind me to study at 3pm"
    response = scheduler.handle_schedule(user_input)
    assert "Scheduled" in response


def test_handle_schedule_with_meeting_input():
    user_input = "schedule a meeting tomorrow"
    response = scheduler.handle_schedule(user_input)
    assert "Scheduled a meeting" in response


def test_handle_schedule_with_empty_input():
    user_input = ""
    response = scheduler.handle_schedule(user_input)
    assert "Sorry" in response


def test_handle_schedule_with_appointment_input():
    response = scheduler.handle_schedule("book an appointment")

    assert "Scheduled an appointment" in response


def test_handle_schedule_with_generic_input():
    response = scheduler.handle_schedule("calendar focus block")

    assert response.startswith("Scheduled:")
