def is_narcissistic(n):
    power = len(str(n)) # ideally faster to set than to solve for every iteration
    return sum(int(x) ** power for x in str(n)) == n
