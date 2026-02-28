def add_punctuation(sentences):
    words = sentences.split(" ")
    new_word = ""
    for i in range(len(words)):
        if words[i][0].isupper():
            words[i-1] += ". "
        else:
            words[i-1] += " "
    for w in words:
        new_word += w
    return new_word.strip()
