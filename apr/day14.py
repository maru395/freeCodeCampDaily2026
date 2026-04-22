def get_last_letter(s):
    letters = [c for c in s if c.isalpha()]
    if not letters:
        return None
    val = [ord(c.lower()) for c in letters]
    return letters[val.index(max(val))]

# use letters and val seperately to get proper index in cases with characters
