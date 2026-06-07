import math

def last_load_date(scoops, usage):
    day = sum(usage) / len(usage)
    return math.floor(scoops / day)
