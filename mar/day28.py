import math

def pascal_row(n):
    arr = []
    for i in range(0, n):
        arr.append(math.comb(n-1,i))
    return arr
