def decompress(s):
    new_str = ""
    seen = {}      # word → position
    pos_map = {}   # position → word (for O(1) reverse lookup)

    for i, x in enumerate(s.split(), 1):
        if x.isdigit():
            new_str += pos_map[int(x)] + " "  # O(1) lookup
        else:
            if x not in seen:
                seen[x] = i
                pos_map[i] = x  # store reverse mapping
            new_str += x + " "

    return new_str.strip()

print(decompress("practice makes perfect and 3 1 2 3"))
# practice makes perfect and perfect practice makes perfect
