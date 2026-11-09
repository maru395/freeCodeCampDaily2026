def launch_fuel(payload):
    total = added = payload / 5
    while not added < 1:
        added = added / 5
        total += added
    return round(total, 1)
