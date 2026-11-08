def digits_or_letters(s):
    letter = digit = 0
    for c in s:
        if c.isdigit():
            digit += 1
        if c.isalpha():
            letter += 1
    if letter > digit:
        return "letters"
    elif letter < digit:
        return "digits"
    else:
        return "tie"
