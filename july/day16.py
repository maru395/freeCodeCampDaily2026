def pig_latin(s):
    result = []
    for word in s.split(" "):
        is_title = word.istitle()
        lower = word.lower()

        if lower[0] in "aeiou":
            new_word = lower + "way"
        else:
            i = 0
            while i < len(lower) and lower[i] not in "aeiou":
                i += 1
            new_word = lower[i:] + lower[:i] + "ay"

        if is_title:
            new_word = new_word[0].upper() + new_word[1:]

        result.append(new_word)

    return " ".join(result)
