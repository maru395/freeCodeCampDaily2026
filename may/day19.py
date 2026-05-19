def sleep_debt(hours_slept, target_hours):
    debt = target_hours
    for h in hours_slept:
        debt += (target_hours - h)
    return debt if debt >= 0 else 0
