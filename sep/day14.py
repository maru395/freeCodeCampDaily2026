punctuations = {",", ".", "!"}

def get_words(paragraph):
    word_counts = {}
    for word in paragraph.lower().split():
        word = word.strip("".join(punctuations))
        if not word:
            continue
        word_counts[word] = word_counts.get(word, 0) + 1

    top3 = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)[:3]
    return [word for word, count in top3]
