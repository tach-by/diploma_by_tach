from datetime import datetime, timedelta


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