from datetime import datetime, date, timedelta


def days_to_the_next_flight(first, second, third):
    lst = sorted([first, second, third])
    date = datetime.today()
    day = date.day
    month = date.month
    year = date.year
    date = datetime(year, month, day)
    if day in lst:
        newdate = date + timedelta(days=1)
    else:
        newdate = date
    day = newdate.day
    while not (day in lst):
        newdate += timedelta(days=1)
        day = newdate.day
    if newdate.weekday() == 3:
        newdate += timedelta(days=2)
    return (newdate - date).days


first, second, third = map(int, input().split())
