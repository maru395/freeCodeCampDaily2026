def is_valid_isbn_13(s):
    sum_num = 0
    flatten = "".join(c for c in s if c.isdigit())
    if len(flatten) == 13:
        for i in range(len(flatten)):
            if i % 2 != 0:
                sum_num += int(flatten[i]) * 3
            else:
                sum_num += int(flatten[i])
        return sum_num % 10 == 0
    return False
