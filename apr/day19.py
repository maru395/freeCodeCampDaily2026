import math

def get_unique_climbs(steps):
    phi = (1 + math.sqrt(5)) / 2
    psi = (1 - math.sqrt(5)) / 2
    return int((phi**(steps+1) - psi**(steps+1)) / math.sqrt(5))

print(get_unique_climbs(4))

# used fibonacci logic
