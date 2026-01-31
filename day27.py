from datetime import datetime, timezone

def odd_or_even_day(timestamp):
    date_str = datetime.fromtimestamp(timestamp / 1000, tz=timezone.utc)
    if date_str.day % 2 == 0:
        return "even"
    else:
        return "odd"
