def get_lucky_number(name):
    vowels = set("aeiouAEIOU")

    def counts(s):
        v = sum(1 for ch in s if ch in vowels)
        c = sum(1 for ch in s if ch.isalpha() and ch not in vowels)
        return v, c, len(s)

    first, last = name.split(" ")
    v1, c1, l1 = counts(first)
    v2, c2, l2 = counts(last)

    small_value = min(v1, v2) * min(c1, c2) * min(l1, l2)
    large_value = max(v1, v2) * max(c1, c2) * max(l1, l2)

    result = large_value - small_value
    return 13 if result == 0 else result
