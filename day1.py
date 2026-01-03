def resolution_streak(days):
    #requirements
    min_steps = 1000
    max_screen = 60
    min_pages = 10

    streak = 0
    for day in days:
        step, screen, page = day #initializes the day[0], day[1], day[2]
        if step >= min_steps and screen <= max_screen and page >= min_pages: 
            streak += 1
    return streak
