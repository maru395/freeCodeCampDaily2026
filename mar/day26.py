from datetime import datetime

def get_movie_night_cost(day, showtime, number_of_tickets):
    fmt = "%I:%M%p"
    limit_dt = datetime.strptime("5:00pm", fmt)
    showtime_dt = datetime.strptime(showtime, fmt)
    if showtime_dt < limit_dt:
        yes = 1
    else:
        yes = 0
    weekends = ["Friday", "Saturday", "Sunday"]
    weekday = ["Monday", "Wednesday", "Thursday"]
    if day in weekends:
        total_cost = (number_of_tickets * 12) - number_of_tickets * (yes * 2)
    elif day in weekday:
        total_cost = (number_of_tickets * 10) - number_of_tickets * (yes * 2)
    elif day == "Tuesday":
        total_cost = (number_of_tickets * 5)
    else:
        return 0
    return f"${max(0, total_cost)}.00"
