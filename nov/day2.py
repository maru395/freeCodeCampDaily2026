import math

def infected(days):
    computers = 1

    for day in range(1, days + 1):
        computers *= 2
        if day % 3 == 0:
            computers -= math.ceil(computers * 0.2)

    return computers
