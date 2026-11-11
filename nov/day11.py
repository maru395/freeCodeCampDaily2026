def count(s):
    vowels = consonants = 0
    for c in s:
        if c.isalpha():
            if c.lower() in "aeiou":
                vowels += 1
            else:
                consonants += 1
    return [vowels, consonants]
