from datetime import date

def days_until_weekend(date_string):
    weekend_days = {
        0: 5,  # Monday
        1: 4,  # Tuesday
        2: 3,  # Wednesday
        3: 2,  # Thursday
        4: 1,  # Friday
    }

    current_date = date.fromisoformat(date_string)
    day = current_date.weekday()

    if day >= 5:
        return "It's the weekend!"

    days_left = weekend_days[day]

    if days_left == 1:
        return "1 day until the weekend."

    return f"{days_left} days until the weekend."
