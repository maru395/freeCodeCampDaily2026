import math

def is_pronic(n):
    val = math.floor(math.sqrt(n))
    if val**2 + val == n:
        return True
    return False
