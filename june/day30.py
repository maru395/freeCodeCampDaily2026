def duplicate_character_count(str1, str2):
    letters = set(str1)
    count = 0

    for c in str2:
        if c in letters:
            count += 1

    return count
