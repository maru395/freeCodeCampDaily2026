def get_frequency(s):
    counter = {}
    for c in s:
        counter[c] = counter.get(c,0) +1 #creates a key for each unique character, else add if already in
    return counter
