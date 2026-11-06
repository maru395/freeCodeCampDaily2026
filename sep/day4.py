vowels = {
    "A" : "a",
    "a" : "a",
    "E" : "e",
    "e" : "e",
    "I" : "i",
    "i" : "i",
    "O" : "o",
    "o" : "o",
    "U" : "u",
    "u" : "u"
}

def repeat_vowels(s):
    count = 0
    string = ""
    for c in s:
        string += c
        if c in vowels:
            for _ in range(count):
                string += vowels[c]
            count += 1
    return string
