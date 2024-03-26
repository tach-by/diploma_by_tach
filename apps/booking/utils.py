from datetime import datetime, timedelta
from apps.booking.models import Booking


def get_week_range(week_type):
    today = datetime.now().date()
    start_of_week = today - timedelta(days=today.weekday())

    match week_type:
        case 'current':
            end_of_week = start_of_week + timedelta(days=6)
        case 'next':
            start_of_week = start_of_week + timedelta(days=7)
            end_of_week = start_of_week + timedelta(days=6)
        case 'previous':
            start_of_week = start_of_week - timedelta(days=7)
            end_of_week = start_of_week + timedelta(days=6)
        case _:
            raise ValueError("Неверный тип недели")

    return start_of_week, end_of_week


def calculate_time_end(date, time_start, duration):

    start_datetime = datetime.combine(date, time_start)

    end_datetime = start_datetime + duration

    time_end = end_datetime.time()

    return time_end


def create_repeat_bookings():
    start_of_week , end_of_week = get_week_range("current")

    bookings_to_repeat = Booking.objects.filter(
        date__range=(start_of_week, end_of_week),
        repeat=True
    )

    # Создание новых бронирований на две недели вперед
    for booking in bookings_to_repeat:
        new_date = booking.date + timedelta(weeks=2)
        new_booking = Booking.objects.create(
            creator=booking.creator,
            date=new_date,
            cabinet=booking.cabinet,
            lesson=booking.lesson,
            time_start=booking.time_start,
            duration=booking.duration,
            repeat=True,
            writable=booking.writable
        )
        print(f"Создано повторяющееся бронирование: {new_booking}")