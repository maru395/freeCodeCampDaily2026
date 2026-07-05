def kaprekar(n):
    if len(set(str(n).zfill(4))) == 1:
        raise ValueError("Number must have at least two distinct digits")

    x = n
    counter = 0
    while x != 6174:
        digits = str(x).zfill(4)
        mx = int("".join(sorted(digits, reverse=True)))
        mn = int("".join(sorted(digits)))
        x = mx - mn
        counter += 1
    return counter
