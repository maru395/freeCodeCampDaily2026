def jbelmu(text):
    new_words = []

    for w in text.split():
        if len(w) <= 2:
            new_words.append(w)
        else:
            new_words.append(w[0] + "".join(sorted(w[1:-1])) + w[-1])

    return " ".join(new_words)
