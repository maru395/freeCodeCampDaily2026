from datetime import datetime

def days_until_birthday(today, birthday):
    dt1 = datetime.strptime(today, "%Y-%m-%d")
    month, day = map(int, birthday.split("/"))

    year = dt1.year
    if month < dt1.month:
        year += 1

    while True:
        try:
            dt2 = datetime(year, month, day)
            break
        except ValueError:
            # e.g. Feb 29 doesn't exist this year -- try the next one
            year += 1

    diff = (dt2 - dt1).days
    if diff <= 0:
        # same month, but the day already passed (or is today) -- roll forward a year
        year += 1
        while True:
            try:
                dt2 = datetime(year, month, day)
                break
            except ValueError:
                year += 1
        diff = (dt2 - dt1).days

    return diff
