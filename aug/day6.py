def get_spoken_time(hour_angle, minute_angle):
    h = int(hour_angle // 30) % 12 or 12
    m = int(minute_angle // 6)

    if m == 0:
        return f"{h} o'clock"
    if m == 15:
        return f"quarter past {h}"
    if m == 30:
        return f"half past {h}"
    if m == 45:
        return f"quarter to {h % 12 + 1}"
    if m < 30:
        return f"{m} minutes past {h}"
    return f"{60 - m} minutes to {h % 12 + 1}"
