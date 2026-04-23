def get_odd_words(s):
    odd_words = [x for x in s.split() if len(x) % 2 == 1]
    return "".join(w + " " for w in odd_words).strip()
