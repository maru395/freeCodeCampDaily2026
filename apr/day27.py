def get_word_score(word):
    return sum(ord(c.upper()) - ord('A') + 1 for c in word)
