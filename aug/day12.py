def is_valid_number(n, base):
    # An empty string isn't a number (test 17)
    if n == "":
        return False

    for char in n.upper():                 # upper() makes the check case-insensitive
        code = ord(char)

        if 48 <= code <= 57:               # '0'-'9' -> values 0..9
            value = code - 48
        elif 65 <= code <= 90:             # 'A'-'Z' -> values 10..35
            value = code - 55
        else:                              # any other character is never valid
            return False

        if value >= base:                  # digit too big for this base
            return False

    return True
