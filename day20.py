def to_consonant_case(s):
    new = ""
    s = s.upper()
    for c in s:
        if c in "AEIOU  ": 
            new += c.lower()
        elif c == "-":
            c = "_"
            new += c
        else:
            new += c
    return new
