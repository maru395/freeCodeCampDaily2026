def fib(n):
    #base cases returns the value in cases that we want the 0 or 1st term
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        #bases
        a = 0 #0 term
        b = 1 #1st term
        for i in range(n-1): #n-1 because 1 is the 1st term which is already specified in our base case
            a = b #pushes the n+1 term
            b = a + b #calculates the next term n1 + n2 logic
        return b
