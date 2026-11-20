PUNCTUATION = str.maketrans("", "", ".!?'")

def longest_word(sentence):
    best_word = ""
    n = 0 
    for word in sentence.split(" "):
        word = word.translate(PUNCTUATION)
        if len(word) > n:
            best_word = word
            n = len(word)
    return best_word
