from datetime import date

from main import get_next_watering, get_watering_status, mark_watering


def test_next_watering():
    assert get_next_watering(date(2026, 9, 2), 7) == date(2026, 9, 9)


def test_next_month():
    assert get_next_watering(date(2026, 12, 29), 7) == date(2027, 1, 5)


def test_overdue():
    assert get_watering_status(date(2026, 9, 8), date(2026, 9, 9)) == (
        "Полив просрочен"
    )


def test_today():
    assert get_watering_status(date(2026, 9, 9), date(2026, 9, 9)) == (
        "Нужно полить сегодня"
    )


def test_later():
    assert get_watering_status(date(2026, 9, 10), date(2026, 9, 9)) == (
        "Поливать пока не нужно"
    )


def test_mark_watering():
    assert mark_watering(date(2026, 9, 9)) == date(2026, 9, 9)
