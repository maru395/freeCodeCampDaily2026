def is_valid_card(number):
    # helper
    def double(n):
        if n*2 > 9:
            return n*2 - 9
        return n*2

    sum_n = 0
    for i, j in enumerate(number[::-1]): #moves to left not right
        if i % 2 == 0:
            sum_n += int(j) 
        else:
            sum_n += double(int(j))

    if sum_n % 10 == 0:
        return True
        
    return False
