def resolution_streak(days):
    min_steps = 1000
    max_screen = 60
    min_pages = 10

    streak = 0
    for day in day:
        step, screen, page = day
        if step >= min_steps and screen <= max_screen and page >= min_pages:
            streak += 1
    return streak
