def is_mirror(str1, str2):
    clean1 = "".join(ch for ch in str1 if ch.isalpha())
    clean2 = "".join(ch for ch in str2 if ch.isalpha())
    return clean1 == clean2[::-1]
