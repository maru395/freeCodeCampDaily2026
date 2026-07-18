def get_lowercase_words(s):
    words = s.split(" ")
    return " ".join(w for w in words if w.islower())
