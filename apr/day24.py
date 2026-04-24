def compress(s):
    new_str = ""
    seen = {}  # word → first position it appeared (1-based)
    for i, x in enumerate(s.split(), 1):  # i = position in original string
        if x not in seen:
            seen[x] = i  # store original position
            new_str += x + " "
        else:
            new_str += str(seen[x]) + " "  # reference original position
    return new_str.strip()
