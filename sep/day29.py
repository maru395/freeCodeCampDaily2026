def get_longest_word(sentence):
    words = sentence.replace(".", "").split()
    best = words[0]
    for w in words:
        if len(w) > len(best):
            best = w
    return best
