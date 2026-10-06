import math

def blend_words(word1, word2):
    mid1 = math.floor(len(word1) / 2)
    mid2 = math.floor(len(word2) / 2)
    return word1[:mid1:] + word2[mid2::]
