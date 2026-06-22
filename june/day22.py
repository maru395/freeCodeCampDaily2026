def make_leet(s):
    translated = {
        "a" : "4",
        "e" : "3",
        "g" : "9",
        "i" : "1",
        "l" : "1",
        "o" : "0",
        "s" : "5",
        "t" : "7"
    }

    return "".join(translated.get(c, c) for c in s)
