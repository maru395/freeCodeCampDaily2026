import math

def is_perfect_square(n):
    s = int(math.isqrt(abs(n)))
    return s * s == n
