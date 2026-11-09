from datetime import date

def moon_phase(date_str):
    days = (date.fromisoformat(date_str) - date(2000, 1, 6)).days
    day = days % 28 + 1  # day 1 is the reference new moon

    if day <= 7:
        return "New"
    if day <= 14:
        return "Waxing"
    if day <= 21:
        return "Full"
    return "Waning"
