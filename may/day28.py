def fizz_buzz_count(start, end):
    fizz = 0
    buzz = 0
    for i in range(start, end+1):
        if i % 3  == 0 and i % 5 == 0:
            fizz += 1
            buzz += 1
        elif i % 3  == 0:
            fizz += 1
        elif i % 5 == 0:
            buzz += 1
    return {"fizz" : fizz, "buzz" : buzz}

# faster version
# def fizz_buzz_count(start, end):
#     if start > end:
#         return {"fizz": 0, "buzz": 0}

    # Helper function to count multiples from 1 up to 'num'
    # def count_multiples(num, divisor):
    #     return num // divisor

    # Count from 1 to 'end'
    # fizz_end = count_multiples(end, 3)
    # buzz_end = count_multiples(end, 5)

    # Count from 1 to 'start - 1'
    # fizz_start = count_multiples(start - 1, 3)
    # buzz_start = count_multiples(start - 1, 5)

    # The difference gives the count within the range
    # return {
    #     "fizz": fizz_end - fizz_start,
    #     "buzz": buzz_end - buzz_start
    # }
