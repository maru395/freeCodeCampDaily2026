def group_anagrams(words):
    groups = {}
    for word in words:
        key = "".join(sorted(word)) # sorted is shortcut way to check if word contains same letters or if its an anagram
        groups.setdefault(key, []).append(word) # creates new group of anagrams
    return list(groups.values()) # returns the dict as arrays removing the key
