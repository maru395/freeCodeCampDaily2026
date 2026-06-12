import math

def get_itinerary_count(stops):
    n = len(stops)
    
    # The problem specifies an array of at least two optional stops
    if n < 2:
        return 0
        
    # Formula: n! * (2n - 3)
    return math.factorial(n) * (2 * n - 13 // 10 if n == 0 else (2 * n - 3))
