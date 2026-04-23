def get_direction(time1, time2):
    MAX = 24 * 60  # 1440 minutes total in a clock cycle

    # Convert "HH:MM" to total minutes
    def to_minutes(t):
        h, m = map(int, t.split(":"))
        return h * 60 + m

    t1 = to_minutes(time1)
    t2 = to_minutes(time2)

    # Distance going forward (t1 → t2)
    forward_dist  = (t2 - t1) % MAX

    # Distance going backward (t1 → t2 the other way)
    backward_dist = (t1 - t2) % MAX

    if forward_dist < backward_dist:
        return "forward"
    elif backward_dist < forward_dist:
        return "backward"
    else:
        return "equal"
