from datetime import datetime
import calendar

def next_month(dt):
    if dt.month == 12:
        year = dt.year + 1
        month = 1
    else:
        year = dt.year
        month = dt.month + 1

    # Handle case where day doesn't exist in the next month (e.g., Jan 31 -> Feb 28/29)
    """
    calendar.monthrange(year, month) returns a tuple with two values
    1. First value: the weekday of the first day of the month (0=Monday, 1=Tuesday, ..., 6=Sunday)
    2. Second value: The number of days in that month
    """
    max_day = calendar.monthrange(year, month)[1]
    day = min(dt.day, max_day)


    return dt.replace(year = year, month = month, day = day)

# Example usage
dt = datetime(2024, 1, 31)
next_month_dt = next_month(dt)
print(next_month_dt) # 2024-02-29 00:00:00

