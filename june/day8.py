CITY_OFFSETS = {
    "Los Angeles": -8,   # PDT (summer), -8 PST (winter)
    "New York":    -5,   # EDT (summer), -5 EST (winter)
    "London":       0,   # BST (summer),  0 GMT (winter)
    "Istanbul":     3,
    "Dubai":        4,
    "Hong Kong":    8,
    "Tokyo":        9,
}

def get_jet_lag_hours(departure_city, arrival_city, flight_duration, direction):
    if direction == "east":
        multiplier = 1.5
    else:
        multiplier = 1
    dif = abs(CITY_OFFSETS[arrival_city] - CITY_OFFSETS[departure_city])

    return dif + (flight_duration * 0.1) * multiplier

print(get_jet_lag_hours("Istanbul", "Hong Kong", 10, "east"))
