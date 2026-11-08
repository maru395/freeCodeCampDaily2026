def send_message(route):
    travel_time = sum(route)/300000
    delay = (len(route) - 1 )* 0.5
    return round(travel_time + delay, 4)
