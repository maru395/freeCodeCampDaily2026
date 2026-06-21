def prime_factorization(n):
    factors = []
    
    # Handle the number of 2s first
    while n % 2 == 0:
        factors.append(2)
        n //= 2
        
    # n must be odd at this point, check odd numbers up to sqrt(n)
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            factors.append(factor)
            n //= factor
        factor += 2
        
    # If n is still greater than 2, the remaining n is prime
    if n > 2:
        factors.append(n)
        
    return factors
