import re

PATTERN = re.compile(r"\+(\d+)\s*\((\d+)\)\s*(\d+)-(\d+)")

def is_spam(number):
    m = PATTERN.search(number)
    if not m:
        return True  # doesn't fit the format at all

    a, b, c, d = m.groups()

    # case 1: country code longer than 2 digits or doesn't start with 0
    if len(a) > 2 or a[0] != "0":
        return True

    # case 2: area code above 900 or below 200
    if int(b) > 900 or int(b) < 200:
        return True

    # case 3: sum of the first three local digits appears in the last four
    if str(sum(int(x) for x in c)) in d:
        return True

    # case 4: same digit 4+ times in a row (ignoring formatting)
    if re.search(r"(\d)\1{3}", a + b + c + d):
        return True

    return False
