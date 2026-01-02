def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        a = 0
        b = 1
        for i in range(n-1):
            a = b
            b = a + b
        return b
