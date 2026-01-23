def is_valid_hex(s):
    if not s.startswith("#"):
        return False

    if len(s) not in (4, 7):
        return False

    return all(c in "0123456789abcdefABCDEF" for c in s[1:])
