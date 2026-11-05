def are_anagrams(str1, str2):
    return set(str1.lower().replace(" ", "")) == set(str2.lower().replace(" ", ""))
