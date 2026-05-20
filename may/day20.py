from itertools import zip_longest

def zip_strings(a, b):
    s = []
    for c1, c2 in zip_longest(a,b,fillvalue=""): #fillvalue adds a empty char if its outside the len of the short string
        s.append(c1)
        s.append(c2)
    return "".join(s)
