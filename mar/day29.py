def is_valid_isbn10(s):
    ss = "".join(s.split("-"))
    sum = 0
    if ss[9] in "0123456789" or ss[9] == "X":
        for i in range(len(ss)):
            if ss[i].isdigit():
                temp = int(ss[i])
                sum +=  temp * (i+1)
            elif i == 9 and ss[i] == "X":
                sum += 100
            else:
                return False
    else:
        return False
    print(sum)
    return True if sum % 11 == 0 else False
