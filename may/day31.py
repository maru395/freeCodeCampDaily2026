import math

def get_combinations(n):
    return math.factorial(n*2)//(math.factorial(n+1) * math.factorial(n))
    
