def is_pangram(sentence, letters):
    found = {ch for ch in sentence.lower() if ch.isalpha()}
    needed = {ch for ch in letters.lower() if ch.isalpha()}
    return found == needed
