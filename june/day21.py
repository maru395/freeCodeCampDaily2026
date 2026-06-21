def get_daytime_hours(latitude):
    raw = 12 + (latitude / 90) * 12
    daytime_hours = round(raw / 2) * 2  # round to nearest *even* number
    nighttime_hours = (24 - daytime_hours) // 2

    return "🌑"*nighttime_hours + "☀️"*daytime_hours + "🌑"*nighttime_hours
