def speeding(speeds, limit):
    speeding = 0
    excess = 0
    for car in speeds:
        if car > limit:
            speeding += 1
            excess += car - limit
    if not speeding:
        return [0,0]
    return [speeding, excess/speeding]
