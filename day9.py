def is_circular_prime(n):
    n = str(n) # make appending easier
    def isPrime(m):
        if m > 1 and all(m % i != 0 for i in range(2, int(m**0.5) + 1)):
            return True
    arr = [] # list of rotational solutions
    arr.append(int(n)) # add initial
    while True: # rotational logic
        i = n[0]
        n = n[1:]
        n += i
        intVal = int(n) # typecasting for check in statement
        if intVal in arr:
            break
        arr.append(int(n)) # continue while not in solution
    if all(isPrime(i) for i in arr): # check if all solutions are prime
        return True
    return False # default

print(is_circular_prime(197))
